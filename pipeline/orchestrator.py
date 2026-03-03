"""Discovery pipeline orchestrator.

Coordinates the full paper discovery flow: scrape IAIFI website, cross-reference
against database, fetch arXiv metadata, download PDFs, and record results.
"""

import logging
from collections.abc import Callable
from datetime import datetime

from pipeline.config import settings
from pipeline.db import Database
from pipeline.fetcher import arxiv_client as arxiv_mod
from pipeline.fetcher import iaifi_scraper as scraper_mod
from pipeline.models import DiscoveryResult, PaperStatus

logger = logging.getLogger(__name__)


class DiscoveryOrchestrator:
    """Orchestrates the paper discovery pipeline."""

    def __init__(
        self,
        db: Database,
        scraper=None,
        arxiv_client: arxiv_mod.ArxivClient | None = None,
    ):
        self.db = db
        self.scraper = scraper or scraper_mod
        self.arxiv_client = arxiv_client or arxiv_mod.ArxivClient()

    async def discover(
        self,
        on_progress: Callable[[str, dict], None] | None = None,
    ) -> DiscoveryResult:
        """Run the full discovery pipeline.

        Steps:
            1. Scrape IAIFI website for all papers
            2. Cross-reference against database to find new papers
            3. Insert new papers with status DISCOVERED
            4. Fetch arXiv metadata in batches
            5. Download PDFs
            6. Record discovery run

        Args:
            on_progress: Optional callback(step_name, details) for progress tracking.

        Returns:
            DiscoveryResult with counts and any error messages.
        """
        errors: list[str] = []
        metadata_fetched_count = 0
        pdfs_downloaded_count = 0

        # Create discovery run record
        run_id = await self.db.create_discovery_run()

        def _progress(step: str, details: dict | None = None):
            if on_progress:
                on_progress(step, details or {})

        try:
            # Step 1: Scrape IAIFI
            _progress("scraping", {"message": "Scraping IAIFI website..."})
            logger.info("Step 1: Scraping IAIFI website")
            scraped_papers = self.scraper.scrape_all_papers()
            total_scraped = len(scraped_papers)
            logger.info(f"Scraped {total_scraped} papers from IAIFI")
            _progress("scraped", {"total": total_scraped})

            # Step 2: Cross-reference against database
            _progress("cross_referencing", {"message": "Checking for new papers..."})
            logger.info("Step 2: Cross-referencing against database")
            existing_ids = await self.db.get_all_arxiv_ids()
            new_papers = [
                p for p in scraped_papers if p.arxiv_id not in existing_ids
            ]
            logger.info(
                f"Found {len(new_papers)} new papers "
                f"({len(existing_ids)} already in database)"
            )
            _progress("cross_referenced", {
                "new": len(new_papers),
                "existing": len(existing_ids),
            })

            # Step 3: Insert new papers with DISCOVERED status
            _progress("inserting", {"message": "Inserting new papers..."})
            logger.info("Step 3: Inserting new papers into database")
            for paper in new_papers:
                try:
                    await self.db.insert_paper({
                        "arxiv_id": paper.arxiv_id,
                        "title": paper.title,
                        "authors": paper.authors,
                        "abstract": paper.abstract or "",
                        "arxiv_categories": [],
                        "iaifi_category": paper.category,
                        "code_url": paper.code_url,
                        "status": PaperStatus.DISCOVERED.value,
                    })
                except Exception as e:
                    error_msg = f"Failed to insert paper {paper.arxiv_id}: {e}"
                    logger.error(error_msg)
                    errors.append(error_msg)

            # Step 4: Fetch arXiv metadata in batches
            _progress("fetching_metadata", {
                "message": "Fetching arXiv metadata..."
            })
            logger.info("Step 4: Fetching arXiv metadata")
            new_ids = [p.arxiv_id for p in new_papers]
            batch_size = settings.ARXIV_BATCH_SIZE

            for i in range(0, len(new_ids), batch_size):
                batch = new_ids[i : i + batch_size]
                batch_num = (i // batch_size) + 1
                total_batches = (len(new_ids) + batch_size - 1) // batch_size
                logger.info(
                    f"Fetching metadata batch {batch_num}/{total_batches} "
                    f"({len(batch)} papers)"
                )
                _progress("metadata_batch", {
                    "batch": batch_num,
                    "total_batches": total_batches,
                })

                try:
                    results = self.arxiv_client.fetch_metadata_batch(batch)
                    for arxiv_id, result in results.items():
                        try:
                            await self.db.update_paper_status(
                                arxiv_id,
                                PaperStatus.METADATA_FETCHED.value,
                                title=result.title,
                                authors=[a.name for a in result.authors],
                                abstract=result.summary,
                                arxiv_categories=list(result.categories),
                                arxiv_id_versioned=result.get_short_id(),
                                published=(
                                    result.published.isoformat()
                                    if result.published
                                    else None
                                ),
                                pdf_url=result.pdf_url,
                            )
                            metadata_fetched_count += 1
                        except Exception as e:
                            error_msg = (
                                f"Failed to update metadata for "
                                f"{arxiv_id}: {e}"
                            )
                            logger.error(error_msg)
                            errors.append(error_msg)
                except Exception as e:
                    error_msg = f"Failed to fetch metadata batch: {e}"
                    logger.error(error_msg)
                    errors.append(error_msg)

            # Step 5: Download PDFs
            _progress("downloading_pdfs", {
                "message": "Downloading PDFs..."
            })
            logger.info("Step 5: Downloading PDFs")

            # Re-fetch metadata results for PDF download
            # (we need the arxiv.Result objects for download_pdf)
            for i in range(0, len(new_ids), batch_size):
                batch = new_ids[i : i + batch_size]
                try:
                    results = self.arxiv_client.fetch_metadata_batch(batch)
                    for arxiv_id, result in results.items():
                        try:
                            pdf_path = self.arxiv_client.download_pdf(result)
                            if pdf_path:
                                await self.db.update_paper_status(
                                    arxiv_id,
                                    PaperStatus.PDF_DOWNLOADED.value,
                                    pdf_path=str(pdf_path),
                                )
                                pdfs_downloaded_count += 1
                            else:
                                logger.warning(
                                    f"PDF download returned None for {arxiv_id}"
                                )
                        except Exception as e:
                            error_msg = (
                                f"Failed to download PDF for {arxiv_id}: {e}"
                            )
                            logger.error(error_msg)
                            errors.append(error_msg)
                except Exception as e:
                    error_msg = f"Failed PDF batch download: {e}"
                    logger.error(error_msg)
                    errors.append(error_msg)

            # Step 6: Update discovery run record
            completed_at = datetime.utcnow().isoformat()
            await self.db.update_discovery_run(
                run_id,
                completed_at=completed_at,
                total_scraped=total_scraped,
                new_papers=len(new_papers),
                metadata_fetched=metadata_fetched_count,
                pdfs_downloaded=pdfs_downloaded_count,
                errors=errors,
                status="complete",
            )

            _progress("complete", {
                "total_scraped": total_scraped,
                "new_papers": len(new_papers),
                "metadata_fetched": metadata_fetched_count,
                "pdfs_downloaded": pdfs_downloaded_count,
            })

        except Exception as e:
            error_msg = f"Discovery pipeline failed: {e}"
            logger.exception(error_msg)
            errors.append(error_msg)

            # Mark run as failed
            try:
                await self.db.update_discovery_run(
                    run_id,
                    completed_at=datetime.utcnow().isoformat(),
                    errors=errors,
                    status="failed",
                )
            except Exception:
                logger.exception("Failed to update discovery run as failed")

            return DiscoveryResult(
                total_scraped=0,
                new_papers=0,
                metadata_fetched=0,
                pdfs_downloaded=0,
                errors=errors,
            )

        result = DiscoveryResult(
            total_scraped=total_scraped,
            new_papers=len(new_papers),
            metadata_fetched=metadata_fetched_count,
            pdfs_downloaded=pdfs_downloaded_count,
            errors=errors,
        )

        logger.info(
            f"Discovery complete: {result.total_scraped} scraped, "
            f"{result.new_papers} new, {result.metadata_fetched} metadata, "
            f"{result.pdfs_downloaded} PDFs"
        )

        return result
