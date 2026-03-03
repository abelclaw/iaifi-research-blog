"""arXiv API client for metadata fetching and PDF downloading.

Wraps the arxiv.py library with IAIFI-specific defaults: batch operations,
version-stripping ID normalization, and cached PDF downloads.
"""

import logging
import re
from pathlib import Path

import arxiv

from pipeline.config import settings

logger = logging.getLogger(__name__)


class ArxivClient:
    """Wrapper around arxiv.py with project-specific defaults."""

    def __init__(
        self,
        pdf_dir: str | None = None,
        delay_seconds: float | None = None,
    ):
        self.pdf_dir = Path(pdf_dir or settings.PDF_DIR)
        self.pdf_dir.mkdir(parents=True, exist_ok=True)

        delay = delay_seconds if delay_seconds is not None else settings.ARXIV_DELAY_SECONDS

        self.client = arxiv.Client(
            page_size=100,
            delay_seconds=delay,
            num_retries=3,
        )

    def fetch_metadata_batch(
        self, arxiv_ids: list[str]
    ) -> dict[str, arxiv.Result]:
        """Fetch metadata for multiple arXiv IDs.

        Args:
            arxiv_ids: List of base arXiv IDs (without version suffix).

        Returns:
            Dict mapping base arXiv ID to arxiv.Result object.
        """
        if not arxiv_ids:
            return {}

        logger.info(f"Fetching metadata for {len(arxiv_ids)} papers from arXiv")

        search = arxiv.Search(id_list=arxiv_ids)
        results: dict[str, arxiv.Result] = {}

        try:
            for result in self.client.results(search):
                # Normalize ID by stripping version suffix
                base_id = re.sub(r"v\d+$", "", result.get_short_id())
                results[base_id] = result
        except Exception:
            logger.exception("Error fetching metadata batch from arXiv")

        # Verify all requested IDs were returned
        missing = set(arxiv_ids) - set(results.keys())
        if missing:
            logger.warning(
                f"arXiv API did not return results for {len(missing)} IDs: "
                f"{sorted(missing)[:10]}{'...' if len(missing) > 10 else ''}"
            )

        logger.info(
            f"Fetched metadata for {len(results)}/{len(arxiv_ids)} papers"
        )
        return results

    def download_pdf(self, result: arxiv.Result) -> Path | None:
        """Download PDF for a single paper, skipping if already cached.

        Args:
            result: arxiv.Result object from metadata fetch.

        Returns:
            Path to the downloaded PDF, or None if download failed.
        """
        # Compute filename from base ID (no version, / replaced with _)
        short_id = re.sub(r"v\d+$", "", result.get_short_id())
        safe_id = short_id.replace("/", "_")
        filepath = self.pdf_dir / f"{safe_id}.pdf"

        # Return cached path if already downloaded
        if filepath.exists() and filepath.stat().st_size > 0:
            logger.debug(f"PDF already cached: {filepath}")
            return filepath

        try:
            result.download_pdf(
                dirpath=str(self.pdf_dir), filename=f"{safe_id}.pdf"
            )

            if filepath.exists() and filepath.stat().st_size > 0:
                logger.info(f"Downloaded PDF: {filepath}")
                return filepath
            else:
                logger.error(f"PDF download produced empty file: {filepath}")
                filepath.unlink(missing_ok=True)
                return None

        except Exception:
            logger.exception(f"PDF download failed for {safe_id}")
            filepath.unlink(missing_ok=True)
            return None
