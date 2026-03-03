"""Dual-strategy PDF figure extraction with scoring."""

import io
import logging
from pathlib import Path

import pymupdf
from PIL import Image

from pipeline.config import settings

logger = logging.getLogger(__name__)


class FigureExtractor:
    """Extracts significant figures from paper PDFs using raster and vector strategies."""

    def __init__(
        self,
        output_dir: str | None = None,
        min_size: int = 100,
        min_area_ratio: float = 0.02,
    ):
        self.output_dir = output_dir or settings.FIGURES_DIR
        self.min_size = min_size
        self.min_area_ratio = min_area_ratio

    def extract_figures(
        self,
        pdf_path: str,
        arxiv_id: str,
        max_figures: int = 3,
    ) -> list[dict]:
        """Extract top figures from a PDF using raster and vector strategies.

        Args:
            pdf_path: Path to the PDF file.
            arxiv_id: arXiv ID for organizing output.
            max_figures: Maximum number of figures to extract.

        Returns:
            List of dicts with path, page_number, width, height,
            extraction_type keys.
        """
        doc = None
        try:
            doc = pymupdf.open(pdf_path)
            candidates = []

            for page_num in range(len(doc)):
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

            # Score and select top candidates
            for c in candidates:
                c["score"] = self._score_candidate(c)

            candidates.sort(key=lambda c: c["score"], reverse=True)
            selected = candidates[:max_figures]

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

    def _score_candidate(self, candidate: dict) -> float:
        """Score a figure candidate by area, aspect ratio, and page position."""
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

        # Page position score: prefer earlier pages
        page_score = 1.0 / (1 + page * 0.1)

        return area * aspect_score * page_score

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
                    "Saved figure %d: %s (%dx%d, %s, page %d)",
                    idx + 1, out_path, candidate["width"],
                    candidate["height"], candidate["type"],
                    candidate["page"],
                )

            except Exception as exc:
                logger.warning(
                    "Failed to save figure %d for %s: %s",
                    idx + 1, arxiv_id, exc,
                )

        return results
