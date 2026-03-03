"""Blog post review API routes for listing, viewing, editing, and approving posts."""

import logging

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from pipeline.config import settings
from pipeline.db import Database

logger = logging.getLogger(__name__)

router = APIRouter()


class PostUpdateRequest(BaseModel):
    """Request body for updating blog post content."""

    content: str


@router.get("/api/posts")
async def list_posts(status: str | None = None):
    """List all blog posts with associated paper info.

    Args:
        status: Optional filter by post status (draft, approved, rejected).

    Returns:
        List of blog post dicts with paper_title and iaifi_category joined.
    """
    db = Database(db_path=settings.DB_PATH)
    posts = await db.get_blog_posts(status=status)
    return posts


@router.get("/api/posts/{arxiv_id}")
async def get_post_detail(arxiv_id: str):
    """Get full blog post with figures and concepts for review.

    Transforms figure filesystem paths to web-accessible /figures/ URLs.

    Args:
        arxiv_id: The base arXiv ID of the paper.

    Returns:
        Dict with post, figures (with transformed URLs), and concepts.
    """
    db = Database(db_path=settings.DB_PATH)
    post = await db.get_blog_post(arxiv_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")

    figures = await db.get_figures(arxiv_id)
    concepts = await db.get_concepts(arxiv_id)

    # Transform figure paths to web-accessible URLs
    figures_dir = settings.FIGURES_DIR
    for fig in figures:
        path = fig["figure_path"]
        if path.startswith(figures_dir):
            # Strip the FIGURES_DIR prefix and prepend /figures/
            relative = path[len(figures_dir) :]
            if relative.startswith("/"):
                fig["url"] = "/figures" + relative
            else:
                fig["url"] = "/figures/" + relative
        elif "figures/" in path:
            # Fallback: split on "figures/" and reconstruct
            fig["url"] = "/figures/" + path.split("figures/", 1)[-1]
        else:
            fig["url"] = path

    return {"post": post, "figures": figures, "concepts": concepts}


@router.put("/api/posts/{arxiv_id}")
async def update_post(arxiv_id: str, body: PostUpdateRequest):
    """Update blog post content (admin editing).

    Recalculates word count server-side.

    Args:
        arxiv_id: The base arXiv ID of the paper.
        body: Request body containing new content.

    Returns:
        Status and updated word count.
    """
    db = Database(db_path=settings.DB_PATH)
    post = await db.get_blog_post(arxiv_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    await db.update_blog_post_content(arxiv_id, body.content)
    return {"status": "updated", "word_count": len(body.content.split())}


@router.post("/api/posts/{arxiv_id}/approve")
async def approve_post(arxiv_id: str):
    """Approve a draft blog post.

    Only draft posts can be approved. Returns 400 for non-draft posts.

    Args:
        arxiv_id: The base arXiv ID of the paper.

    Returns:
        Status confirmation.
    """
    db = Database(db_path=settings.DB_PATH)
    post = await db.get_blog_post(arxiv_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    if post["status"] != "draft":
        raise HTTPException(
            status_code=400,
            detail=f"Cannot approve post with status '{post['status']}'",
        )
    await db.update_blog_post_status(arxiv_id, "approved")
    return {"status": "approved"}


@router.post("/api/posts/{arxiv_id}/reject")
async def reject_post(arxiv_id: str):
    """Reject a draft blog post.

    Only draft posts can be rejected. Returns 400 for non-draft posts.

    Args:
        arxiv_id: The base arXiv ID of the paper.

    Returns:
        Status confirmation.
    """
    db = Database(db_path=settings.DB_PATH)
    post = await db.get_blog_post(arxiv_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    if post["status"] != "draft":
        raise HTTPException(
            status_code=400,
            detail=f"Cannot reject post with status '{post['status']}'",
        )
    await db.update_blog_post_status(arxiv_id, "rejected")
    return {"status": "rejected"}
