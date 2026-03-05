"""LLM client that shells out to `claude -p` (Claude Code CLI)."""

import asyncio
import json
import logging
import os

from pydantic import BaseModel, ValidationError

from pipeline.config import llm_settings

logger = logging.getLogger(__name__)


class ClaudeCLIClient:
    """LLM client using `claude -p` subprocess calls.

    Drop-in replacement for LLMClient — same interface, but uses
    the Claude Code CLI instead of LiteLLM.  This uses the user's
    existing Claude Code subscription (no separate API key needed).
    """

    def __init__(
        self,
        model: str | None = None,
        temperature: float | None = None,
        cache_dir: str | None = None,  # unused, kept for interface compat
    ):
        self.model = model or llm_settings.MODEL
        self.temperature = temperature if temperature is not None else llm_settings.TEMPERATURE
        self.total_cost = 0.0  # CLI doesn't report cost, but kept for compat

        logger.info(
            "ClaudeCLIClient initialized: model=%s",
            self.model,
        )

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int = 4096,
    ) -> str:
        """Generate text by calling `claude -p`."""
        combined_prompt = f"{system_prompt}\n\n{user_prompt}"

        last_error = None
        for attempt in range(3):
            try:
                result = await self._call_claude(combined_prompt, max_tokens)
                return result
            except (OSError, asyncio.TimeoutError) as exc:
                last_error = exc
                if attempt < 2:
                    logger.warning(
                        "claude -p error (attempt %d/3): %s",
                        attempt + 1, exc,
                    )
                    await asyncio.sleep(2)
                    continue
                raise

        raise last_error  # type: ignore[misc]

    async def generate_structured(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: type[BaseModel],
        max_tokens: int = 4096,
    ) -> BaseModel:
        """Generate structured output via claude -p with JSON schema."""
        schema = json.dumps(response_model.model_json_schema(), indent=2)
        combined_prompt = (
            f"{system_prompt}\n\n{user_prompt}\n\n"
            f"IMPORTANT: You MUST respond with ONLY valid JSON (no explanation, "
            f"no markdown, no text before or after). The JSON must match this "
            f"schema exactly:\n{schema}"
        )

        last_error = None
        for attempt in range(3):
            try:
                raw = await self._call_claude(combined_prompt, max_tokens)
                return self._parse_json_response(raw, response_model)
            except (ValidationError, ValueError):
                # Response was prose — ask a cheap follow-up to convert it to JSON
                logger.info("Got prose response, converting to JSON via follow-up call")
                return await self._convert_prose_to_json(raw, response_model)
            except (OSError, asyncio.TimeoutError) as exc:
                last_error = exc
                if attempt < 2:
                    logger.warning(
                        "claude -p structured error (attempt %d/3): %s",
                        attempt + 1, exc,
                    )
                    await asyncio.sleep(2)
                    continue
                raise

        raise last_error  # type: ignore[misc]

    async def _convert_prose_to_json(
        self, prose: str, response_model: type[BaseModel]
    ) -> BaseModel:
        """Ask Claude to convert a prose response into structured JSON."""
        schema = json.dumps(response_model.model_json_schema(), indent=2)
        conversion_prompt = (
            f"Convert the following text into valid JSON matching the schema below. "
            f"Output ONLY the JSON — no explanation, no markdown fences.\n\n"
            f"Schema:\n{schema}\n\n"
            f"Text to convert:\n{prose}"
        )
        raw = await self._call_claude(conversion_prompt)
        return self._parse_json_response(raw, response_model)

    @staticmethod
    def _parse_json_response(raw: str, response_model: type[BaseModel]) -> BaseModel:
        """Extract and parse JSON from a claude -p response."""
        # Try direct parse first
        try:
            return response_model.model_validate_json(raw)
        except ValidationError:
            pass

        # Strip markdown code fences
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            first_newline = cleaned.index("\n")
            cleaned = cleaned[first_newline + 1:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3].strip()
        try:
            return response_model.model_validate_json(cleaned)
        except ValidationError:
            pass

        # Try to find JSON object in the response
        start = raw.find("{")
        end = raw.rfind("}") + 1
        if start != -1 and end > start:
            return response_model.model_validate_json(raw[start:end])

        raise ValueError(f"No valid JSON found in response: {raw[:200]}...")

    async def _call_claude(
        self,
        prompt: str,
        max_tokens: int = 4096,
        json_schema: dict | None = None,
    ) -> str:
        """Execute `claude -p` as a subprocess and return stdout."""
        cmd = ["claude", "-p", "--model", self.model]

        # NOTE: --json-schema is intentionally NOT used here because it
        # silently returns empty output on longer prompts (claude-code bug).
        # Instead, the prompt itself asks for JSON and _parse_json_response
        # handles extracting JSON from the response.

        # Budget guard: $2 per call max (generous for blog gen)
        cmd.extend(["--max-budget-usd", "2"])

        # No tools needed — pure text generation
        cmd.extend(["--tools", ""])

        logger.debug("Running: %s", " ".join(cmd[:6]) + " ...")

        # Strip CLAUDECODE env var so we don't hit nested-session guard
        env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}

        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
        )

        stdout, stderr = await asyncio.wait_for(
            proc.communicate(input=prompt.encode()),
            timeout=120,
        )

        if proc.returncode != 0:
            error_msg = stderr.decode().strip()
            logger.error("claude -p failed (rc=%d): %s", proc.returncode, error_msg)
            raise OSError(f"claude -p exited with code {proc.returncode}: {error_msg}")

        output = stdout.decode().strip()
        stderr_text = stderr.decode().strip()
        if stderr_text:
            logger.debug("claude -p stderr: %s", stderr_text[:500])

        if not output:
            raise OSError(
                f"claude -p returned empty output (stderr: {stderr_text[:200]})"
            )

        logger.info("claude -p returned %d chars", len(output))
        return output
