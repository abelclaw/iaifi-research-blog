"""Evaluate and filter figures for blog posts using Claude vision."""

import base64
import json
import logging
import subprocess
from pathlib import Path

import httpx
from PIL import Image

logger = logging.getLogger(__name__)

MAX_FIGURES = 3
MIN_DIMENSION = 80  # Reject images smaller than this in either dimension


def _get_oauth_token() -> str | None:
    """Retrieve Claude Code OAuth access token from macOS Keychain."""
    try:
        result = subprocess.run(
            ["security", "find-generic-password", "-s", "Claude Code-credentials", "-w"],
            capture_output=True, text=True, timeout=5,
        )
        if result.returncode != 0:
            return None
        creds = json.loads(result.stdout.strip())
        return creds.get("claudeAiOauth", {}).get("accessToken")
    except Exception as e:
        logger.warning("Could not retrieve OAuth token: %s", e)
        return None


def _too_small(path: str) -> bool:
    """Quick PIL check: reject images that are too small to be informative."""
    try:
        img = Image.open(path)
        w, h = img.size
        return w < MIN_DIMENSION or h < MIN_DIMENSION
    except Exception:
        return True


def _encode_image(path: str) -> tuple[str, str]:
    """Return (base64_data, media_type) for an image file."""
    p = Path(path)
    ext = p.suffix.lower()
    media_type = "image/png" if ext == ".png" else "image/jpeg"
    with open(path, "rb") as f:
        data = base64.standard_b64encode(f.read()).decode()
    return data, media_type


async def _score_figures_with_vision(
    figures: list[dict],
    paper_title: str,
    token: str,
) -> list[int]:
    """Ask Claude to rate each figure 0–3 for blog suitability.

    Returns a list of integer scores aligned with the figures list.
    """
    content = []

    content.append({
        "type": "text",
        "text": (
            f"You are evaluating figures from a research paper titled: \"{paper_title}\".\n\n"
            "For each figure below, rate its suitability as an illustration in a blog post "
            "aimed at an educated general audience (not specialists):\n\n"
            "  0 = Useless for a blog: blank, empty wireframe, trivial geometric shape, "
            "table of numbers, or otherwise uninformative\n"
            "  1 = Poor: very hard to interpret without reading the full paper\n"
            "  2 = OK: somewhat informative, passable illustration\n"
            "  3 = Good: visually informative, shows results or an interesting concept clearly\n\n"
            "Respond with ONLY a JSON array of integers, one per figure, in order. "
            f"Example for {len(figures)} figures: [2, 0, 3]\n\n"
            "Figures:"
        ),
    })

    for i, fig in enumerate(figures):
        path = fig["figure_path"]
        try:
            data, media_type = _encode_image(path)
        except Exception as e:
            logger.warning("Could not encode figure %s: %s", path, e)
            content.append({"type": "text", "text": f"\nFigure {i + 1}: [could not load image]"})
            continue

        content.append({"type": "text", "text": f"\nFigure {i + 1}:"})
        content.append({
            "type": "image",
            "source": {"type": "base64", "media_type": media_type, "data": data},
        })

    async with httpx.AsyncClient(timeout=60) as client:
        resp = await client.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "Authorization": f"Bearer {token}",
                "anthropic-version": "2023-06-01",
                "anthropic-beta": "oauth-2025-04-20",
                "content-type": "application/json",
            },
            json={
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": 64,
                "messages": [{"role": "user", "content": content}],
            },
        )
        resp.raise_for_status()
        text = resp.json()["content"][0]["text"].strip()

    # Parse JSON array
    start = text.find("[")
    end = text.rfind("]") + 1
    scores = json.loads(text[start:end])
    # Ensure we have a score for each figure
    while len(scores) < len(figures):
        scores.append(1)
    return [int(max(0, min(3, s))) for s in scores[:len(figures)]]


class ImageFixer:
    """Evaluates and filters figures, keeping only the best 0–MAX_FIGURES."""

    def __init__(self, paper_title: str = ""):
        self.paper_title = paper_title

    async def select_figures(self, figures: list[dict]) -> list[dict]:
        """Evaluate figures and return list of {id, selected} decisions.

        Uses Claude vision via OAuth token. Falls back to keeping all figures
        if vision is unavailable.
        """
        if not figures:
            return []

        # Quick pre-filter: remove images that are too small
        valid = []
        results = []
        for fig in figures:
            if _too_small(fig["figure_path"]):
                logger.info("Pre-filter reject (too small): %s", fig["figure_path"])
                results.append({"id": fig["id"], "selected": False})
            else:
                valid.append(fig)

        if not valid:
            return results

        token = _get_oauth_token()
        if not token:
            logger.warning("No OAuth token available — keeping all figures as-is")
            for fig in valid:
                results.append({"id": fig["id"], "selected": True})
            return results

        try:
            scores = await _score_figures_with_vision(valid, self.paper_title, token)
        except Exception as e:
            logger.error("Vision scoring failed: %s — keeping all figures", e)
            for fig in valid:
                results.append({"id": fig["id"], "selected": True})
            return results

        logger.info("Vision scores for %s: %s", self.paper_title, scores)

        # Select up to MAX_FIGURES with score >= 2, or best available if none qualify
        scored_valid = list(zip(valid, scores))
        scored_valid.sort(key=lambda x: x[1], reverse=True)

        kept = 0
        selected_ids = set()
        for fig, score in scored_valid:
            if score >= 2 and kept < MAX_FIGURES:
                selected_ids.add(fig["id"])
                kept += 1

        # If nothing scored >= 2, keep nothing (0 images is fine)
        for fig in valid:
            results.append({"id": fig["id"], "selected": fig["id"] in selected_ids})

        kept_count = len(selected_ids)
        logger.info(
            "ImageFixer: kept %d/%d figures for '%s'",
            kept_count, len(figures), self.paper_title,
        )
        return results
