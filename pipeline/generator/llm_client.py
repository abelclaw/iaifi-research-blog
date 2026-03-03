"""Provider-agnostic LLM client with disk caching and cost tracking."""

import logging
import os

import litellm
from litellm import Cache
from pydantic import BaseModel, ValidationError

from pipeline.config import llm_settings

logger = logging.getLogger(__name__)

# Suppress litellm's verbose logging
litellm.suppress_debug_info = True


class LLMClient:
    """LLM client supporting any provider via LiteLLM with disk caching."""

    def __init__(
        self,
        model: str | None = None,
        temperature: float | None = None,
        cache_dir: str | None = None,
    ):
        self.model = model or llm_settings.MODEL
        self.temperature = temperature if temperature is not None else llm_settings.TEMPERATURE
        self.cache_dir = cache_dir or llm_settings.CACHE_DIR
        self.total_cost = 0.0

        # Validate that at least one API key is available
        has_anthropic = bool(os.environ.get("ANTHROPIC_API_KEY"))
        has_openai = bool(os.environ.get("OPENAI_API_KEY"))
        has_ollama = bool(os.environ.get("OPENAI_API_BASE"))
        if not (has_anthropic or has_openai or has_ollama):
            raise ValueError(
                "No LLM API key found. Set one of: "
                "ANTHROPIC_API_KEY (for Claude), "
                "OPENAI_API_KEY (for GPT), "
                "OPENAI_API_BASE (for Ollama/local models)"
            )

        # Enable disk caching so re-runs during development cost nothing
        litellm.cache = Cache(type="disk", disk_cache_dir=self.cache_dir)

        logger.info(
            "LLMClient initialized: model=%s, temperature=%s, cache=%s",
            self.model, self.temperature, self.cache_dir,
        )

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int = 4096,
    ) -> str:
        """Generate text completion with retry logic."""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        last_error = None
        for attempt in range(3):
            try:
                response = await litellm.acompletion(
                    model=self.model,
                    messages=messages,
                    temperature=self.temperature,
                    max_tokens=max_tokens,
                )
                # Track cost
                cost = response._hidden_params.get("response_cost", 0) or 0
                self.total_cost += cost

                return response.choices[0].message.content

            except (TimeoutError, ConnectionError, OSError) as exc:
                last_error = exc
                if attempt < 2:
                    logger.warning(
                        "LLM API transient error (attempt %d/3): %s",
                        attempt + 1, exc,
                    )
                    continue
                raise

        # Should not reach here, but just in case
        raise last_error  # type: ignore[misc]

    async def generate_structured(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: type[BaseModel],
        max_tokens: int = 4096,
    ) -> BaseModel:
        """Generate structured output parsed into a Pydantic model."""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        last_error = None
        for attempt in range(3):
            try:
                response = await litellm.acompletion(
                    model=self.model,
                    messages=messages,
                    temperature=self.temperature,
                    max_tokens=max_tokens,
                    response_format=response_model,
                )
                # Track cost
                cost = response._hidden_params.get("response_cost", 0) or 0
                self.total_cost += cost

                content = response.choices[0].message.content

                # Parse response into the model
                try:
                    return response_model.model_validate_json(content)
                except ValidationError:
                    # Strip markdown code fences and retry parse
                    cleaned = content.strip()
                    if cleaned.startswith("```"):
                        # Remove opening fence (```json or ```)
                        first_newline = cleaned.index("\n")
                        cleaned = cleaned[first_newline + 1:]
                    if cleaned.endswith("```"):
                        cleaned = cleaned[:-3].strip()
                    return response_model.model_validate_json(cleaned)

            except (TimeoutError, ConnectionError, OSError) as exc:
                last_error = exc
                if attempt < 2:
                    logger.warning(
                        "LLM API transient error (attempt %d/3): %s",
                        attempt + 1, exc,
                    )
                    continue
                raise
            except ValidationError as exc:
                raise ValueError(
                    f"Failed to parse LLM response into {response_model.__name__}: {exc}"
                ) from exc

        raise last_error  # type: ignore[misc]
