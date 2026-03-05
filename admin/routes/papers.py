"""Papers API routes for listing and retrieving ingested papers."""

import asyncio
import json
import logging
from functools import partial
from typing import Optional

from fastapi import APIRouter, HTTPException

from pipeline.config import settings
from pipeline.db import Database
from pipeline.fetcher.arxiv_client import ArxivClient
from pipeline.models import PaperStatus

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/api/papers")
async def list_papers(
    status: Optional[str] = None,
    category: Optional[str] = None,
):
    """List all ingested papers, with optional filtering.

    Args:
        status: Filter by PaperStatus value (e.g., "discovered", "pdf_downloaded").
        category: Filter by IAIFI category (e.g., "Foundational AI").

    Returns:
        List of paper dicts with parsed JSON fields (authors, arxiv_categories).
    """
    db = Database(db_path=settings.DB_PATH)

    # Use the existing get_papers method for status filtering
    papers = await db.get_papers(status=status)

    # Apply category filter if provided
    if category:
        papers = [
            p for p in papers
            if p.get("iaifi_category") == category
        ]

    # Fetch sets of arxiv_ids that have blog posts or concepts
    blog_ids = await _get_ids_with_blog(db)
    concept_ids = await _get_ids_with_concepts(db)

    # Ensure JSON string fields are parsed to lists + add flags
    for paper in papers:
        if isinstance(paper.get("authors"), str):
            try:
                paper["authors"] = json.loads(paper["authors"])
            except (json.JSONDecodeError, TypeError):
                paper["authors"] = []
        if isinstance(paper.get("arxiv_categories"), str):
            try:
                paper["arxiv_categories"] = json.loads(
                    paper["arxiv_categories"]
                )
            except (json.JSONDecodeError, TypeError):
                paper["arxiv_categories"] = []
        paper["has_blog_post"] = paper["arxiv_id"] in blog_ids
        paper["has_concepts"] = paper["arxiv_id"] in concept_ids

    return papers


async def _get_ids_with_blog(db: Database) -> set[str]:
    """Return set of arxiv_ids that have a blog post."""
    import aiosqlite
    async with aiosqlite.connect(db.db_path) as conn:
        cursor = await conn.execute(
            "SELECT DISTINCT paper_arxiv_id FROM blog_posts"
        )
        return {row[0] for row in await cursor.fetchall()}


async def _get_ids_with_concepts(db: Database) -> set[str]:
    """Return set of arxiv_ids that have concepts."""
    import aiosqlite
    async with aiosqlite.connect(db.db_path) as conn:
        cursor = await conn.execute(
            "SELECT DISTINCT paper_arxiv_id FROM concepts"
        )
        return {row[0] for row in await cursor.fetchall()}


@router.get("/api/papers/{arxiv_id}")
async def get_paper(arxiv_id: str):
    """Get a single paper by arXiv ID.

    Args:
        arxiv_id: The base arXiv ID (without version suffix).

    Returns:
        Paper dict with parsed JSON fields, or 404 if not found.
    """
    db = Database(db_path=settings.DB_PATH)
    papers = await db.get_papers()

    # Find the paper with matching arxiv_id
    for paper in papers:
        if paper.get("arxiv_id") == arxiv_id:
            # Ensure JSON string fields are parsed
            if isinstance(paper.get("authors"), str):
                try:
                    paper["authors"] = json.loads(paper["authors"])
                except (json.JSONDecodeError, TypeError):
                    paper["authors"] = []
            if isinstance(paper.get("arxiv_categories"), str):
                try:
                    paper["arxiv_categories"] = json.loads(
                        paper["arxiv_categories"]
                    )
                except (json.JSONDecodeError, TypeError):
                    paper["arxiv_categories"] = []
            return paper

    raise HTTPException(status_code=404, detail="Paper not found")


@router.post("/api/papers/{arxiv_id}/download-pdf")
async def download_paper_pdf(arxiv_id: str):
    """Download PDF for a single paper from arXiv.

    Only works for papers at metadata_fetched or discovered status.
    Updates the paper status to pdf_downloaded on success.
    """
    db = Database(db_path=settings.DB_PATH)
    papers = await db.get_papers()
    paper = next((p for p in papers if p.get("arxiv_id") == arxiv_id), None)
    if not paper:
        raise HTTPException(status_code=404, detail="Paper not found")

    if paper["status"] not in ("discovered", "metadata_fetched"):
        return {"status": "already_downloaded", "pdf_path": paper.get("pdf_path")}

    arxiv_client = ArxivClient(
        pdf_dir=settings.PDF_DIR,
        delay_seconds=settings.ARXIV_DELAY_SECONDS,
    )

    # Run blocking arXiv calls in a thread to avoid blocking the event loop
    loop = asyncio.get_event_loop()

    results = await loop.run_in_executor(
        None, partial(arxiv_client.fetch_metadata_batch, [arxiv_id])
    )
    if arxiv_id not in results:
        raise HTTPException(status_code=502, detail="Could not fetch metadata from arXiv")

    result = results[arxiv_id]
    pdf_path = await loop.run_in_executor(
        None, partial(arxiv_client.download_pdf, result)
    )
    if not pdf_path:
        raise HTTPException(status_code=502, detail="PDF download failed")

    await db.update_paper_status(
        arxiv_id,
        PaperStatus.PDF_DOWNLOADED.value,
        pdf_path=str(pdf_path),
    )

    return {"status": "downloaded", "pdf_path": str(pdf_path)}
