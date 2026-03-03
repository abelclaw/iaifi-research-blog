"""Pipeline API routes for triggering the full discovery + generation pipeline."""

import logging
import time
from datetime import datetime, timezone

from fastapi import APIRouter, BackgroundTasks, HTTPException

from pipeline.config import settings
from pipeline.db import Database
from pipeline.fetcher.arxiv_client import ArxivClient
from pipeline.orchestrator import ContentGenerator, DiscoveryOrchestrator

logger = logging.getLogger(__name__)

router = APIRouter()

# In-memory task tracking (same pattern as discovery.py and generation.py)
_pipeline_tasks: dict[str, dict] = {}


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
                "concepts_extracted",
            )
        ]

        generator = ContentGenerator(db=db)
        generated = 0
        for paper in eligible_papers:
            existing_post = await db.get_blog_post(paper["arxiv_id"])
            if not existing_post:
                try:
                    await generator.generate_content(paper["arxiv_id"])
                    generated += 1
                except Exception as e:
                    logger.error(
                        "Pipeline %s: generation failed for %s: %s",
                        task_id, paper["arxiv_id"], e,
                    )

        _pipeline_tasks[task_id].update({
            "status": "complete",
            "step": "complete",
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
