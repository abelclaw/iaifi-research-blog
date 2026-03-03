"""Pipeline orchestrators for discovery and content generation.

Coordinates the full paper discovery flow: scrape IAIFI website, cross-reference
against database, fetch arXiv metadata, download PDFs, and record results.

Also provides ContentGenerator which orchestrates figure extraction, blog post
generation, and concept extraction for a single paper.
"""

import json
import logging
from collections.abc import Callable
from datetime import datetime
from pathlib import Path

from pipeline.config import settings
from pipeline.db import Database
from pipeline.extractor.figure_extractor import FigureExtractor
from pipeline.extractor.pdf_reader import extract_paper_text
from pipeline.fetcher import arxiv_client as arxiv_mod
from pipeline.fetcher import iaifi_scraper as scraper_mod
from pipeline.generator.concept_extractor import ConceptExtractor
from pipeline.generator.llm_client import LLMClient
from pipeline.generator.post_generator import PostGenerator
from pipeline.models import DiscoveryResult, Paper, PaperStatus

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


class ContentGenerator:
    """Orchestrates the full content generation pipeline for a paper.

    Runs figure extraction, blog post generation, and concept extraction
    in sequence, persisting all results to the database and updating paper
    status at each step.
    """

    def __init__(self, db: Database):
        self.db = db
        self.llm = LLMClient()
        self.post_generator = PostGenerator(llm_client=self.llm)
        self.concept_extractor = ConceptExtractor(llm_client=self.llm)
        self.figure_extractor = FigureExtractor()

    async def generate_content(
        self,
        arxiv_id: str,
        on_progress: Callable[[str, dict], None] | None = None,
    ) -> dict:
        """Run the full content generation pipeline for a paper.

        Steps:
            1. Extract figures from PDF
            2. Extract text from PDF
            3. Generate blog post (three-pass LLM chain)
            4. Extract concepts (structured LLM output)

        Args:
            arxiv_id: arXiv ID of the paper to generate content for.
            on_progress: Optional callback(step_name, details) for
                progress tracking.

        Returns:
            Dict with blog_post, figures, concepts, and generation_cost.

        Raises:
            ValueError: If the paper is not found in the database.
            FileNotFoundError: If the paper's PDF file is missing.
        """

        def _progress(step: str, details: dict | None = None):
            if on_progress:
                on_progress(step, details or {})

        try:
            # Fetch paper from database
            papers = await self.db.get_papers()
            paper_dict = None
            for p in papers:
                if p["arxiv_id"] == arxiv_id:
                    paper_dict = p
                    break

            if paper_dict is None:
                raise ValueError(f"Paper not found in database: {arxiv_id}")

            # Construct Paper model from DB dict
            paper = Paper(
                arxiv_id=paper_dict["arxiv_id"],
                arxiv_id_versioned=paper_dict.get("arxiv_id_versioned"),
                title=paper_dict["title"],
                authors=paper_dict["authors"],
                abstract=paper_dict["abstract"],
                arxiv_categories=paper_dict["arxiv_categories"],
                iaifi_category=paper_dict["iaifi_category"],
                published=paper_dict.get("published"),
                pdf_path=paper_dict.get("pdf_path"),
                pdf_url=paper_dict.get("pdf_url"),
                code_url=paper_dict.get("code_url"),
                status=paper_dict.get("status", "discovered"),
            )

            # Verify PDF exists
            pdf_path = paper.pdf_path
            if not pdf_path or not Path(pdf_path).exists():
                raise FileNotFoundError(
                    f"PDF not found for paper {arxiv_id}: {pdf_path}"
                )

            cost_before = self.llm.total_cost

            # Step 1: Extract figures
            _progress("extracting_figures", {
                "message": f"Extracting figures from {arxiv_id}...",
            })
            logger.info("Step 1: Extracting figures for %s", arxiv_id)
            figures = self.figure_extractor.extract_figures(pdf_path, arxiv_id)
            for fig in figures:
                await self.db.insert_figure({
                    "paper_arxiv_id": arxiv_id,
                    "figure_path": fig["path"],
                    "page_number": fig["page_number"],
                    "width": fig["width"],
                    "height": fig["height"],
                    "extraction_type": fig["extraction_type"],
                    "sort_order": figures.index(fig),
                })
            await self.db.update_paper_status(
                arxiv_id, PaperStatus.FIGURES_EXTRACTED.value
            )
            logger.info("Extracted %d figures for %s", len(figures), arxiv_id)

            # Step 2: Extract text from PDF
            _progress("extracting_text", {
                "message": "Extracting paper text...",
            })
            logger.info("Step 2: Extracting text for %s", arxiv_id)
            pdf_text = extract_paper_text(pdf_path)

            # Step 3: Generate blog post
            _progress("generating_post", {
                "message": "Generating blog post...",
            })
            logger.info("Step 3: Generating blog post for %s", arxiv_id)
            blog_post = await self.post_generator.generate_post(
                paper, pdf_path
            )
            await self.db.insert_blog_post({
                "paper_arxiv_id": blog_post.paper_arxiv_id,
                "title": blog_post.title,
                "slug": blog_post.slug,
                "content": blog_post.content,
                "word_count": blog_post.word_count,
                "llm_model": blog_post.llm_model,
                "generation_cost": blog_post.generation_cost,
                "status": blog_post.status,
            })
            await self.db.update_paper_status(
                arxiv_id, PaperStatus.POST_GENERATED.value
            )
            logger.info(
                "Blog post generated for %s: %d words",
                arxiv_id, blog_post.word_count,
            )

            # Step 4: Extract concepts
            _progress("extracting_concepts", {
                "message": "Extracting scientific concepts...",
            })
            logger.info("Step 4: Extracting concepts for %s", arxiv_id)
            concept_result = await self.concept_extractor.extract_concepts(
                paper, pdf_text
            )
            await self.db.insert_concepts(
                arxiv_id,
                [c.model_dump() for c in concept_result.concepts],
            )
            await self.db.update_paper_status(
                arxiv_id, PaperStatus.CONCEPTS_EXTRACTED.value
            )
            logger.info(
                "Extracted %d concepts for %s (theme: %s)",
                len(concept_result.concepts),
                arxiv_id,
                concept_result.iaifi_theme,
            )

            generation_cost = self.llm.total_cost - cost_before

            _progress("complete", {
                "message": f"Content generation complete for {arxiv_id}",
                "figures": len(figures),
                "word_count": blog_post.word_count,
                "concepts": len(concept_result.concepts),
                "cost": generation_cost,
            })

            return {
                "blog_post": blog_post.model_dump(),
                "figures": figures,
                "concepts": [
                    c.model_dump() for c in concept_result.concepts
                ],
                "generation_cost": generation_cost,
            }

        except Exception as e:
            error_msg = f"Content generation failed for {arxiv_id}: {e}"
            logger.exception(error_msg)
            _progress("error", {"message": error_msg})
            raise
