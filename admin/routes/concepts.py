"""Concepts review API routes for listing, viewing, and approving concepts."""

import logging
from pathlib import Path

import yaml
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from pipeline.config import settings
from pipeline.db import Database
from pipeline.export import export_approved_concepts

logger = logging.getLogger(__name__)

router = APIRouter()

# Load taxonomy once at import time
_TAXONOMY_PATH = Path(__file__).parent.parent.parent / "pipeline" / "concepts_taxonomy.yaml"


def _load_taxonomy() -> dict[str, list[str]]:
    with open(_TAXONOMY_PATH) as f:
        data = yaml.safe_load(f)
    return data.get("categories", {})


@router.get("/api/concepts-review")
async def list_concepts_for_review(status: str | None = None):
    """List papers that have extracted concepts, with counts.

    Args:
        status: Filter by concepts_status (pending/approved/rejected).
    """
    db = Database(db_path=settings.DB_PATH)
    return await db.get_papers_with_concepts(concepts_status=status)


@router.get("/api/concepts-review/{arxiv_id}")
async def get_concepts_detail(arxiv_id: str):
    """Get all concepts for a paper, for review.

    Returns paper info + full concept list.
    """
    db = Database(db_path=settings.DB_PATH)
    concepts = await db.get_concepts(arxiv_id)
    if not concepts:
        raise HTTPException(status_code=404, detail="No concepts found for this paper")

    papers = await db.get_papers()
    paper = next((p for p in papers if p["arxiv_id"] == arxiv_id), None)
    if not paper:
        raise HTTPException(status_code=404, detail="Paper not found")

    return {
        "arxiv_id": arxiv_id,
        "title": paper["title"],
        "iaifi_category": paper.get("iaifi_category"),
        "concepts_status": paper.get("concepts_status"),
        "concepts": concepts,
    }


class ConceptDeleteRequest(BaseModel):
    """Request body for deleting specific concepts."""
    concept_ids: list[int]


@router.post("/api/concepts-review/{arxiv_id}/approve")
async def approve_concepts(arxiv_id: str):
    """Approve concepts for a paper (makes them visible in the network)."""
    db = Database(db_path=settings.DB_PATH)
    concepts = await db.get_concepts(arxiv_id)
    if not concepts:
        raise HTTPException(status_code=404, detail="No concepts found")
    await db.set_concepts_status(arxiv_id, "approved")

    # Export all approved concepts to the Astro site
    try:
        count = export_approved_concepts(settings.DB_PATH, "site")
        logger.info("Exported %d papers with approved concepts", count)
    except Exception as e:
        logger.error("Concept export failed: %s", e)

    return {"status": "approved", "exported": True}


@router.post("/api/concepts-review/{arxiv_id}/reject")
async def reject_concepts(arxiv_id: str):
    """Reject concepts for a paper."""
    db = Database(db_path=settings.DB_PATH)
    await db.set_concepts_status(arxiv_id, "rejected")
    return {"status": "rejected"}


@router.delete("/api/concepts-review/{arxiv_id}/concepts/{concept_id}")
async def delete_concept(arxiv_id: str, concept_id: int):
    """Delete a single concept by ID (during review)."""
    db = Database(db_path=settings.DB_PATH)
    import aiosqlite
    async with aiosqlite.connect(db.db_path) as conn:
        cursor = await conn.execute(
            "DELETE FROM concepts WHERE id = ? AND paper_arxiv_id = ?",
            (concept_id, arxiv_id),
        )
        await conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Concept not found")
    return {"status": "deleted"}


class ConceptUpdate(BaseModel):
    """Request body for updating a concept's relevance."""
    relevance: float


@router.patch("/api/concepts-review/{arxiv_id}/concepts/{concept_id}")
async def update_concept(arxiv_id: str, concept_id: int, body: ConceptUpdate):
    """Update a concept's relevance score."""
    if not 0 <= body.relevance <= 1:
        raise HTTPException(status_code=400, detail="Relevance must be between 0 and 1")
    import aiosqlite
    db = Database(db_path=settings.DB_PATH)
    async with aiosqlite.connect(db.db_path) as conn:
        cursor = await conn.execute(
            "UPDATE concepts SET relevance = ? WHERE id = ? AND paper_arxiv_id = ?",
            (body.relevance, concept_id, arxiv_id),
        )
        await conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Concept not found")
    return {"status": "updated", "relevance": body.relevance}


class ConceptAdd(BaseModel):
    """Request body for adding a new concept."""
    name: str
    description: str = ""
    relevance: float = 0.8


@router.post("/api/concepts-review/{arxiv_id}/concepts")
async def add_concept(arxiv_id: str, body: ConceptAdd):
    """Add a new concept to a paper."""
    if not 0 <= body.relevance <= 1:
        raise HTTPException(status_code=400, detail="Relevance must be between 0 and 1")
    import aiosqlite
    from datetime import datetime
    db = Database(db_path=settings.DB_PATH)
    async with aiosqlite.connect(db.db_path) as conn:
        cursor = await conn.execute(
            "INSERT INTO concepts (paper_arxiv_id, name, description, relevance, created_at) VALUES (?, ?, ?, ?, ?)",
            (arxiv_id, body.name.lower().strip(), body.description, body.relevance, datetime.utcnow().isoformat()),
        )
        await conn.commit()
        new_id = cursor.lastrowid
    return {"status": "added", "id": new_id, "name": body.name.lower().strip(), "relevance": body.relevance}


@router.get("/api/taxonomy")
async def get_taxonomy():
    """Return the concept taxonomy for the add-concept dropdown."""
    return _load_taxonomy()
