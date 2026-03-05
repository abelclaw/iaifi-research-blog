"""Pipeline API routes for triggering the full discovery + generation pipeline."""

import asyncio
import logging
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, BackgroundTasks, HTTPException

from pipeline.config import settings
from pipeline.db import Database
from pipeline.export import export_approved_concepts, export_approved_posts
from pipeline.fetcher.arxiv_client import ArxivClient
from pipeline.orchestrator import ContentGenerator, DiscoveryOrchestrator

logger = logging.getLogger(__name__)

router = APIRouter()

# In-memory task tracking (same pattern as discovery.py and generation.py)
_pipeline_tasks: dict[str, dict] = {}
_cancelled: set[str] = set()  # task IDs that have been cancelled


@router.get("/api/pipeline/active")
async def get_active_pipeline():
    """Return the currently running pipeline task, if any."""
    for task in _pipeline_tasks.values():
        if task["status"] == "running":
            return task
    return {"status": "none"}


@router.post("/api/pipeline/run")
async def trigger_full_pipeline(background_tasks: BackgroundTasks):
    """Run full pipeline: discovery then generation for all eligible papers.

    Chains paper discovery with content generation for papers that have
    PDFs downloaded but no blog post yet.

    Returns immediately with a task_id for status polling.
    """
    task_id = f"pipeline-{int(time.time())}"
    _pipeline_tasks[task_id] = {
        "task_id": task_id,
        "status": "running",
        "step": "starting",
        "result": None,
        "error": None,
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    background_tasks.add_task(run_full_pipeline, task_id)
    return {"task_id": task_id, "status": "started"}


@router.get("/api/pipeline/{task_id}/status")
async def pipeline_status(task_id: str):
    """Get the status of a pipeline task.

    Returns the full task dict including status, current step,
    result (if complete), and error (if failed).
    """
    if task_id not in _pipeline_tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return _pipeline_tasks[task_id]


@router.post("/api/pipeline/{task_id}/cancel")
async def cancel_pipeline(task_id: str):
    """Cancel a running pipeline task. It will stop after the current paper finishes."""
    if task_id not in _pipeline_tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    if _pipeline_tasks[task_id]["status"] != "running":
        raise HTTPException(status_code=400, detail="Task is not running")
    _cancelled.add(task_id)
    _pipeline_tasks[task_id]["step"] = "cancelling"
    return {"status": "cancelling"}


async def run_full_pipeline(task_id: str) -> None:
    """Background: discover papers, then generate content for eligible ones.

    Step 1: Run discovery pipeline (scrape, metadata, PDF download).
    Step 2: Generate blog posts for all papers with PDF that lack a blog post.
    """
    try:
        db = Database(db_path=settings.DB_PATH)
        await db.initialize()

        # Step 1: Discovery
        _pipeline_tasks[task_id]["step"] = "discovery"
        logger.info("Pipeline %s: starting discovery", task_id)

        arxiv_client = ArxivClient(
            pdf_dir=settings.PDF_DIR,
            delay_seconds=settings.ARXIV_DELAY_SECONDS,
        )
        orchestrator = DiscoveryOrchestrator(
            db=db,
            arxiv_client=arxiv_client,
        )
        discovery_result = await orchestrator.discover()

        # Step 2: Generation for eligible papers
        _pipeline_tasks[task_id]["step"] = "generation"
        logger.info("Pipeline %s: starting generation", task_id)

        # Get papers with PDF downloaded or figures extracted that lack blog posts
        all_papers = await db.get_papers()
        eligible_papers = [
            p for p in all_papers
            if p["status"] in (
                "pdf_downloaded",
                "figures_extracted",
                "post_generated",
            )
        ]

        generator = ContentGenerator(db=db)
        generated = 0
        cancelled = False
        for paper in eligible_papers:
            if task_id in _cancelled:
                cancelled = True
                _cancelled.discard(task_id)
                logger.info("Pipeline %s: cancelled by user after %d generated", task_id, generated)
                break
            existing_post = await db.get_blog_post(paper["arxiv_id"])
            if not existing_post:
                _pipeline_tasks[task_id]["step"] = f"generating ({generated + 1}/{len(eligible_papers)}): {paper['arxiv_id']}"
                try:
                    await generator.generate_content(paper["arxiv_id"])
                    generated += 1
                except Exception as e:
                    logger.error(
                        "Pipeline %s: generation failed for %s: %s",
                        task_id, paper["arxiv_id"], e,
                    )

        _pipeline_tasks[task_id].update({
            "status": "cancelled" if cancelled else "complete",
            "step": "cancelled" if cancelled else "complete",
            "result": {
                "papers_discovered": discovery_result.new_papers,
                "posts_generated": generated,
            },
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
        logger.info(
            "Pipeline %s complete: %d discovered, %d generated",
            task_id, discovery_result.new_papers, generated,
        )

    except Exception as e:
        logger.exception("Pipeline %s failed", task_id)
        _pipeline_tasks[task_id].update({
            "status": "error",
            "error": str(e),
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })


# --- Search reindex ---

_reindex_tasks: dict[str, dict] = {}


@router.post("/api/pipeline/reindex")
async def reindex_search(background_tasks: BackgroundTasks):
    """Export posts, rebuild Astro site, and regenerate Pagefind search index."""
    task_id = f"reindex-{int(time.time())}"
    _reindex_tasks[task_id] = {
        "task_id": task_id,
        "status": "running",
        "step": "starting",
        "error": None,
    }
    background_tasks.add_task(_run_reindex, task_id)
    return {"task_id": task_id, "status": "started"}


@router.get("/api/pipeline/reindex/{task_id}/status")
async def reindex_status(task_id: str):
    if task_id not in _reindex_tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return _reindex_tasks[task_id]


async def _run_reindex(task_id: str) -> None:
    site_dir = "site"
    try:
        # Step 1: Export posts and concepts
        _reindex_tasks[task_id]["step"] = "exporting"
        posts = export_approved_posts(settings.DB_PATH, site_dir)
        concepts = export_approved_concepts(settings.DB_PATH, site_dir)
        logger.info("Reindex: exported %d posts, %d concept papers", posts, concepts)

        # Step 2: Astro build
        _reindex_tasks[task_id]["step"] = "building site"
        proc = await asyncio.create_subprocess_exec(
            "npm", "run", "build:astro",
            cwd=site_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            raise RuntimeError(f"Astro build failed: {stderr.decode()[-500:]}")

        # Step 3: Pagefind index
        _reindex_tasks[task_id]["step"] = "indexing search"
        proc = await asyncio.create_subprocess_exec(
            "npx", "pagefind", "--site", "dist",
            cwd=site_dir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            raise RuntimeError(f"Pagefind failed: {stderr.decode()[-500:]}")

        # Step 4: Copy index to public/ for dev server
        _reindex_tasks[task_id]["step"] = "copying index"
        dist_pagefind = Path(site_dir) / "dist" / "pagefind"
        public_pagefind = Path(site_dir) / "public" / "pagefind"
        if public_pagefind.exists():
            shutil.rmtree(public_pagefind)
        shutil.copytree(dist_pagefind, public_pagefind)

        _reindex_tasks[task_id].update({
            "status": "complete",
            "step": "done",
            "result": {"posts_exported": posts, "concepts_exported": concepts},
        })
        logger.info("Reindex %s complete", task_id)

    except Exception as e:
        logger.exception("Reindex %s failed", task_id)
        _reindex_tasks[task_id].update({
            "status": "error",
            "step": "failed",
            "error": str(e),
        })
