"""Papers API routes for listing and retrieving ingested papers."""

import json
import logging
from typing import Optional

from fastapi import APIRouter, HTTPException

from pipeline.config import settings
from pipeline.db import Database

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

    # Ensure JSON string fields are parsed to lists
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

    return papers


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
