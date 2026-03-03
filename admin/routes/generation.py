"""Generation API routes for triggering and monitoring content generation."""

import logging
import time
from datetime import datetime, timezone

from fastapi import APIRouter, BackgroundTasks, HTTPException

from pipeline.config import settings
from pipeline.db import Database
from pipeline.orchestrator import ContentGenerator

logger = logging.getLogger(__name__)

router = APIRouter()

# In-memory task tracking (same pattern as discovery.py)
_gen_tasks: dict[str, dict] = {}


@router.post("/api/generate/{arxiv_id}")
async def trigger_generation(arxiv_id: str, background_tasks: BackgroundTasks):
    """Trigger content generation for a paper in the background.

    Runs figure extraction, blog post generation, and concept extraction.
    Returns immediately with a task_id that can be used to poll for status.
    """
    task_id = f"gen-{arxiv_id}-{int(time.time())}"
    _gen_tasks[task_id] = {
        "task_id": task_id,
        "arxiv_id": arxiv_id,
        "status": "running",
        "step": "starting",
        "result": None,
        "error": None,
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    background_tasks.add_task(run_generation, task_id, arxiv_id)
    return {"task_id": task_id, "status": "started"}


@router.get("/api/generate/{task_id}/status")
async def generation_status(task_id: str):
    """Get the status of a generation task.

    Returns the full task dict including status, current step,
    result (if complete), and error (if failed).
    """
    if task_id not in _gen_tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return _gen_tasks[task_id]


async def run_generation(task_id: str, arxiv_id: str) -> None:
    """Background function that runs the full content generation pipeline.

    Instantiates Database + ContentGenerator, runs generation, and
    updates the task status on completion or failure.
    """
    try:
        db = Database(db_path=settings.DB_PATH)
        await db.initialize()

        generator = ContentGenerator(db=db)

        def on_progress(step: str, details: dict):
            _gen_tasks[task_id]["step"] = step
            _gen_tasks[task_id]["details"] = details

        result = await generator.generate_content(
            arxiv_id, on_progress=on_progress
        )

        _gen_tasks[task_id].update({
            "status": "complete",
            "step": "complete",
            "result": {
                "figures": len(result["figures"]),
                "word_count": result["blog_post"]["word_count"],
                "concepts": len(result["concepts"]),
                "generation_cost": result["generation_cost"],
            },
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
        logger.info(
            "Generation task %s complete for %s", task_id, arxiv_id
        )

    except Exception as e:
        logger.exception("Generation task %s failed for %s", task_id, arxiv_id)
        _gen_tasks[task_id].update({
            "status": "error",
            "error": str(e),
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
