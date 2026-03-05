"""Dual-strategy PDF figure extraction with LLM-based ranking.

Extracts candidate figures from PDFs using raster and vector strategies,
filters out decorative images (logos, icons), parses captions, and uses
an LLM to select the most important figures for blog posts.
"""

import io
import logging
import re
from pathlib import Path

import pymupdf
from PIL import Image

from pipeline.config import settings

logger = logging.getLogger(__name__)

# Regex for figure captions: "Figure 1:", "Fig. 2:", "Figure 3.", etc.
_CAPTION_RE = re.compile(
    r"(?:Figure|Fig\.?)\s*(\d+)\s*[.:]\s*(.+?)(?:\n\n|\Z)",
    re.IGNORECASE | re.DOTALL,
)


class FigureExtractor:
    """Extracts significant figures from paper PDFs using raster and vector strategies.

    When an LLM client is provided, uses it to rank candidates by relevance
    to the paper's narrative. Falls back to geometric scoring otherwise.
    """

    def __init__(
        self,
        output_dir: str | None = None,
        min_size: int = 100,
        min_area_ratio: float = 0.02,
    ):
        self.output_dir = output_dir or settings.FIGURES_DIR
        self.min_size = min_size
        self.min_area_ratio = min_area_ratio

    async def extract_figures(
        self,
        pdf_path: str,
        arxiv_id: str,
        max_figures: int = 3,
        paper_title: str | None = None,
        paper_abstract: str | None = None,
        llm_client=None,
    ) -> list[dict]:
        """Extract top figures from a PDF using raster and vector strategies.

        Args:
            pdf_path: Path to the PDF file.
            arxiv_id: arXiv ID for organizing output.
            max_figures: Maximum number of figures to extract.
            paper_title: Paper title for LLM-based ranking.
            paper_abstract: Paper abstract for LLM-based ranking.
            llm_client: LLM client instance for ranking (optional).

        Returns:
            List of dicts with path, page_number, width, height,
            extraction_type keys.
        """
        doc = None
        try:
            doc = pymupdf.open(pdf_path)
            total_pages = len(doc)
            candidates = []

            for page_num in range(total_pages):
                page = doc[page_num]
                page_rect = page.rect
                page_area = page_rect.width * page_rect.height

                # Strategy 1: Raster images
                candidates.extend(
                    self._extract_raster(doc, page, page_num, page_area)
                )

                # Strategy 2: Vector drawings
                candidates.extend(
                    self._extract_vector(page, page_num, page_area)
                )

            # Filter out decorative images
            candidates = self._filter_decorative(candidates, total_pages)

            if not candidates:
                logger.warning("No significant figures found in %s", arxiv_id)
                return []

            # Parse figure captions from PDF text
            captions = self._parse_figure_captions(doc)

            # Match captions to candidates by page proximity
            for c in candidates:
                c["caption"] = self._match_caption(c, captions)

            # Rank candidates
            if llm_client and paper_title:
                try:
                    selected = await self._llm_rank_figures(
                        candidates, paper_title, paper_abstract or "",
                        llm_client, max_figures,
                    )
                except Exception as exc:
                    logger.warning(
                        "LLM ranking failed, falling back to geometric: %s", exc
                    )
                    selected = self._geometric_rank(
                        candidates, total_pages, max_figures
                    )
            else:
                selected = self._geometric_rank(
                    candidates, total_pages, max_figures
                )

            # Save selected figures
            return self._save_figures(selected, arxiv_id)

        finally:
            if doc:
                doc.close()

    def _extract_raster(
        self,
        doc: pymupdf.Document,
        page: pymupdf.Page,
        page_num: int,
        page_area: float,
    ) -> list[dict]:
        """Extract raster images from a page."""
        candidates = []
        try:
            images = page.get_images(full=True)
        except Exception as exc:
            logger.warning("Failed to get images from page %d: %s", page_num, exc)
            return candidates

        for img_info in images:
            xref = img_info[0]
            try:
                img_data = doc.extract_image(xref)
                if not img_data:
                    continue

                width = img_data["width"]
                height = img_data["height"]

                if not self._is_significant(width, height, page_area):
                    continue

                candidates.append({
                    "type": "raster",
                    "page": page_num,
                    "width": width,
                    "height": height,
                    "xref": xref,
                    "data": img_data["image"],
                    "ext": img_data["ext"],
                })
            except Exception as exc:
                logger.debug(
                    "Failed to extract image xref=%d from page %d: %s",
                    xref, page_num, exc,
                )

        return candidates

    def _extract_vector(
        self,
        page: pymupdf.Page,
        page_num: int,
        page_area: float,
    ) -> list[dict]:
        """Extract vector drawing clusters from a page."""
        candidates = []
        try:
            paths = page.get_drawings()
        except Exception as exc:
            logger.warning(
                "Failed to get drawings from page %d: %s", page_num, exc
            )
            return candidates

        if not paths:
            return candidates

        try:
            clusters = page.cluster_drawings(drawings=paths)
        except Exception as exc:
            logger.debug(
                "Failed to cluster drawings on page %d: %s", page_num, exc
            )
            return candidates

        for box in clusters:
            rect = pymupdf.Rect(box)
            width = int(rect.width)
            height = int(rect.height)

            if not self._is_significant(width, height, page_area):
                continue

            try:
                pixmap = page.get_pixmap(clip=rect, dpi=150)
                candidates.append({
                    "type": "vector",
                    "page": page_num,
                    "width": pixmap.width,
                    "height": pixmap.height,
                    "pixmap": pixmap,
                })
            except Exception as exc:
                logger.debug(
                    "Failed to render vector cluster on page %d: %s",
                    page_num, exc,
                )

        return candidates

    def _filter_decorative(
        self, candidates: list[dict], total_pages: int
    ) -> list[dict]:
        """Filter out likely decorative images (logos, icons, banners).

        Removes:
        - Very small images on page 0 (likely journal logos/headers)
        - Extreme aspect ratios (likely banners, rules, or separators)
        - Very low resolution raster images (icons/bullets)
        """
        filtered = []
        for c in candidates:
            w, h = c["width"], c["height"]

            # Skip tiny images on first page (logos, journal headers)
            if c["page"] == 0 and w * h < 40000:
                logger.debug("Filtered small page-0 image: %dx%d", w, h)
                continue

            # Skip extreme aspect ratios (> 5:1 or < 1:5) — banners/rules
            if w > 0 and h > 0:
                ratio = min(w, h) / max(w, h)
                if ratio < 0.15:
                    logger.debug(
                        "Filtered extreme aspect ratio image: %dx%d (%.2f)",
                        w, h, ratio,
                    )
                    continue

            # Skip very small raster images (icons, bullets)
            if c["type"] == "raster" and w < 80 and h < 80:
                logger.debug("Filtered tiny raster: %dx%d", w, h)
                continue

            # For raster images, check if it's a low-color image (likely icon/logo)
            if c["type"] == "raster" and "data" in c:
                try:
                    img = Image.open(io.BytesIO(c["data"]))
                    # Convert to RGB if needed for color analysis
                    if img.mode in ("RGBA", "P", "LA"):
                        img = img.convert("RGB")
                    # Sample center region for unique color count
                    small = img.resize((32, 32), Image.LANCZOS)
                    colors = len(set(small.getdata()))
                    if colors < 8:
                        logger.debug(
                            "Filtered low-color image: %dx%d (%d colors)",
                            w, h, colors,
                        )
                        continue
                except Exception:
                    pass  # If we can't analyze, keep the candidate

            filtered.append(c)

        logger.info(
            "Filtered %d → %d candidates (removed %d decorative)",
            len(candidates) + (len(candidates) - len(filtered)),
            len(filtered),
            len(candidates) - len(filtered),
        )
        return filtered

    def _parse_figure_captions(self, doc: pymupdf.Document) -> list[dict]:
        """Extract figure captions from the PDF text.

        Returns list of {number, caption, page} dicts.
        """
        captions = []
        for page_num in range(len(doc)):
            try:
                text = doc[page_num].get_text()
            except Exception:
                continue

            for match in _CAPTION_RE.finditer(text):
                fig_num = int(match.group(1))
                caption_text = match.group(2).strip()
                # Truncate long captions
                if len(caption_text) > 300:
                    caption_text = caption_text[:300] + "..."
                captions.append({
                    "number": fig_num,
                    "caption": caption_text,
                    "page": page_num,
                })

        logger.info("Parsed %d figure captions from PDF", len(captions))
        return captions

    def _match_caption(
        self, candidate: dict, captions: list[dict]
    ) -> str | None:
        """Match a candidate image to the nearest figure caption by page proximity."""
        if not captions:
            return None

        page = candidate["page"]
        # Find captions on the same page or adjacent pages
        nearby = [
            c for c in captions
            if abs(c["page"] - page) <= 1
        ]

        if not nearby:
            return None

        # Prefer same-page captions, then by figure number
        nearby.sort(key=lambda c: (abs(c["page"] - page), c["number"]))
        best = nearby[0]
        return f"Figure {best['number']}: {best['caption']}"

    def _geometric_rank(
        self, candidates: list[dict], total_pages: int, max_figures: int
    ) -> list[dict]:
        """Rank candidates using geometric heuristics (fallback)."""
        for c in candidates:
            c["score"] = self._score_candidate(c, total_pages)

        candidates.sort(key=lambda c: c["score"], reverse=True)
        return candidates[:max_figures]

    async def _llm_rank_figures(
        self,
        candidates: list[dict],
        paper_title: str,
        paper_abstract: str,
        llm_client,
        max_figures: int,
    ) -> list[dict]:
        """Use LLM to select the most important figures for a blog post.

        Sends candidate descriptions (page, size, caption) along with
        paper context, asks the LLM to pick the best figures.
        """
        # Build candidate descriptions for the LLM
        descriptions = []
        for i, c in enumerate(candidates):
            desc = (
                f"[{i}] Page {c['page'] + 1}, "
                f"{c['width']}x{c['height']}px, "
                f"type={c['type']}"
            )
            if c.get("caption"):
                desc += f", caption: {c['caption']}"
            else:
                desc += ", no caption found"
            descriptions.append(desc)

        candidates_text = "\n".join(descriptions)

        system_prompt = (
            "You are a scientific figure analyst. You select the most important "
            "figures from a research paper for use in a blog post summary. "
            "Prioritize: (1) key results plots showing main findings, "
            "(2) method/architecture diagrams, (3) comparison plots. "
            "Avoid: logos, stock images, simple tables, trivial diagrams."
        )

        user_prompt = (
            f"Paper: {paper_title}\n\n"
            f"Abstract: {paper_abstract}\n\n"
            f"The following candidate figures were extracted from the PDF. "
            f"Select the {max_figures} most important for a blog post, "
            f"in order of importance.\n\n"
            f"Candidates:\n{candidates_text}\n\n"
            f"Reply with ONLY the candidate indices (numbers in brackets), "
            f"one per line, most important first. Example:\n2\n5\n0"
        )

        response = await llm_client.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            max_tokens=256,
        )

        # Parse indices from response
        selected_indices = []
        for line in response.strip().splitlines():
            line = line.strip().strip("[]")
            # Extract first number from each line
            match = re.search(r"\d+", line)
            if match:
                idx = int(match.group())
                if 0 <= idx < len(candidates) and idx not in selected_indices:
                    selected_indices.append(idx)
            if len(selected_indices) >= max_figures:
                break

        if not selected_indices:
            logger.warning("LLM returned no valid indices, falling back to geometric")
            return self._geometric_rank(candidates, 0, max_figures)

        selected = [candidates[i] for i in selected_indices]
        logger.info(
            "LLM selected figures: indices=%s (from %d candidates)",
            selected_indices, len(candidates),
        )
        return selected

    def _score_candidate(self, candidate: dict, total_pages: int = 1) -> float:
        """Score a figure candidate by area, aspect ratio, and page position.

        Penalizes page 0 (likely title page with logos) and prefers
        middle-to-late pages (where results typically appear).
        """
        width = candidate["width"]
        height = candidate["height"]
        page = candidate["page"]

        area = width * height

        # Aspect ratio score: penalize very narrow strips
        if width > 0 and height > 0:
            ratio = min(width, height) / max(width, height)
            aspect_score = 1.0 if ratio >= 0.3 else ratio / 0.3
        else:
            aspect_score = 0.0

        # Page position score: penalize page 0, prefer middle-to-late pages
        if page == 0:
            page_score = 0.3  # Strong penalty for title page
        elif total_pages > 1:
            # Peak around 60-80% through the paper (results section)
            relative_pos = page / total_pages
            if relative_pos < 0.3:
                page_score = 0.6 + relative_pos  # 0.6-0.9 for early pages
            elif relative_pos < 0.8:
                page_score = 1.0  # Full score for middle-to-late pages
            else:
                page_score = 0.9  # Slight penalty for appendix pages
        else:
            page_score = 0.5

        # Caption bonus: figures with captions are more likely real figures
        caption_bonus = 1.3 if candidate.get("caption") else 1.0

        return area * aspect_score * page_score * caption_bonus

    def _is_significant(
        self, width: int, height: int, page_area: float
    ) -> bool:
        """Check if an image meets minimum size requirements."""
        if width < self.min_size or height < self.min_size:
            return False
        if page_area > 0 and (width * height) / page_area < self.min_area_ratio:
            return False
        return True

    def _save_figures(
        self, candidates: list[dict], arxiv_id: str
    ) -> list[dict]:
        """Save selected figure candidates as PNG files."""
        # Use sanitized arxiv_id for directory name
        safe_id = arxiv_id.replace("/", "_").replace(".", "_")
        fig_dir = Path(self.output_dir) / safe_id
        fig_dir.mkdir(parents=True, exist_ok=True)

        results = []
        for idx, candidate in enumerate(candidates):
            filename = f"figure_{idx + 1}.png"
            out_path = fig_dir / filename

            try:
                if candidate["type"] == "raster":
                    # Convert raw image data to PNG via Pillow
                    img = Image.open(io.BytesIO(candidate["data"]))
                    img.save(str(out_path), "PNG")
                elif candidate["type"] == "vector":
                    # Save pixmap directly as PNG
                    candidate["pixmap"].save(str(out_path))
                else:
                    continue

                results.append({
                    "path": str(out_path),
                    "page_number": candidate["page"],
                    "width": candidate["width"],
                    "height": candidate["height"],
                    "extraction_type": candidate["type"],
                })

                logger.info(
                    "Saved figure %d: %s (%dx%d, %s, page %d%s)",
                    idx + 1, out_path, candidate["width"],
                    candidate["height"], candidate["type"],
                    candidate["page"],
                    f", caption: {candidate['caption'][:60]}..."
                    if candidate.get("caption") else "",
                )

            except Exception as exc:
                logger.warning(
                    "Failed to save figure %d for %s: %s",
                    idx + 1, arxiv_id, exc,
                )

        return results
