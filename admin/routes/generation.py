"""Generation API routes for triggering and monitoring blog + concept tasks."""

import logging
import time
from datetime import datetime, timezone

from fastapi import APIRouter, BackgroundTasks, HTTPException

from pipeline.config import settings
from pipeline.db import Database
from pipeline.orchestrator import ContentGenerator

logger = logging.getLogger(__name__)

router = APIRouter()

# In-memory task tracking (shared across generate and concepts tasks)
_tasks: dict[str, dict] = {}

# Track latest task per paper per type: (arxiv_id, type) -> task_id
_paper_tasks: dict[tuple[str, str], str] = {}

# Bulk task tracking
_bulk_tasks: dict[str, dict] = {}
_bulk_cancelled: set[str] = set()


# --- Lookup active task for a paper ---

@router.get("/api/tasks/{arxiv_id}")
async def get_paper_tasks(arxiv_id: str):
    """Get active/recent tasks for a paper (blog + concepts).

    Returns task info if a task exists, so the UI can resume polling.
    """
    result = {}
    for task_type in ("generate", "concepts"):
        key = (arxiv_id, task_type)
        task_id = _paper_tasks.get(key)
        if task_id and task_id in _tasks:
            result[task_type] = _tasks[task_id]
    return result


# --- Blog generation ---

@router.post("/api/generate/{arxiv_id}")
async def trigger_generation(arxiv_id: str, background_tasks: BackgroundTasks):
    """Trigger blog post generation (figures + blog) in the background."""
    task_id = f"gen-{arxiv_id}-{int(time.time())}"
    _tasks[task_id] = {
        "task_id": task_id,
        "arxiv_id": arxiv_id,
        "type": "generate",
        "status": "running",
        "step": "starting",
        "result": None,
        "error": None,
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    _paper_tasks[(arxiv_id, "generate")] = task_id
    background_tasks.add_task(_run_generation, task_id, arxiv_id)
    return {"task_id": task_id, "status": "started"}


@router.get("/api/generate/{task_id}/status")
async def generation_status(task_id: str):
    """Get the status of a generation or concepts task."""
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return _tasks[task_id]


async def _run_generation(task_id: str, arxiv_id: str) -> None:
    """Background: run figure extraction + blog post generation."""
    try:
        db = Database(db_path=settings.DB_PATH)
        await db.initialize()
        generator = ContentGenerator(db=db)

        def on_progress(step: str, details: dict):
            _tasks[task_id]["step"] = step
            _tasks[task_id]["details"] = details

        result = await generator.generate_content(
            arxiv_id, on_progress=on_progress
        )

        _tasks[task_id].update({
            "status": "complete",
            "step": "complete",
            "result": {
                "figures": len(result["figures"]),
                "word_count": result["blog_post"]["word_count"],
                "generation_cost": result["generation_cost"],
            },
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
        logger.info("Generation task %s complete for %s", task_id, arxiv_id)

    except Exception as e:
        logger.exception("Generation task %s failed for %s", task_id, arxiv_id)
        _tasks[task_id].update({
            "status": "error",
            "error": str(e),
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })


# --- Concept extraction ---

@router.post("/api/concepts/{arxiv_id}")
async def trigger_concepts(arxiv_id: str, background_tasks: BackgroundTasks):
    """Trigger concept extraction for a paper in the background."""
    task_id = f"con-{arxiv_id}-{int(time.time())}"
    _tasks[task_id] = {
        "task_id": task_id,
        "arxiv_id": arxiv_id,
        "type": "concepts",
        "status": "running",
        "step": "starting",
        "result": None,
        "error": None,
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    _paper_tasks[(arxiv_id, "concepts")] = task_id

    # Mark paper as extracting in DB so state persists across page refresh
    db = Database(db_path=settings.DB_PATH)
    await db.set_concepts_status(arxiv_id, "extracting")

    background_tasks.add_task(_run_concepts, task_id, arxiv_id)
    return {"task_id": task_id, "status": "started"}


@router.get("/api/concepts/{task_id}/status")
async def concepts_status(task_id: str):
    """Get the status of a concept extraction task."""
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return _tasks[task_id]


async def _run_concepts(task_id: str, arxiv_id: str) -> None:
    """Background: run concept extraction."""
    try:
        db = Database(db_path=settings.DB_PATH)
        await db.initialize()
        generator = ContentGenerator(db=db)

        def on_progress(step: str, details: dict):
            _tasks[task_id]["step"] = step
            _tasks[task_id]["details"] = details

        result = await generator.extract_concepts_only(
            arxiv_id, on_progress=on_progress
        )

        _tasks[task_id].update({
            "status": "complete",
            "step": "complete",
            "result": {
                "concept_count": result["concept_count"],
            },
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
        # concepts_status set to "pending" by orchestrator
        logger.info(
            "Concepts task %s complete for %s (%d concepts)",
            task_id, arxiv_id, result["concept_count"],
        )

    except Exception as e:
        logger.exception("Concepts task %s failed for %s", task_id, arxiv_id)
        _tasks[task_id].update({
            "status": "error",
            "error": str(e),
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
        # Reset concepts_status on failure
        try:
            db = Database(db_path=settings.DB_PATH)
            await db.set_concepts_status(arxiv_id, None)
        except Exception:
            pass


# --- Bulk operations (server-side, survive page refresh) ---

@router.get("/api/bulk/active")
async def get_active_bulk():
    """Return the currently running bulk task, if any."""
    for task in _bulk_tasks.values():
        if task["status"] == "running":
            return task
    return {"status": "none"}


@router.get("/api/bulk/{task_id}/status")
async def bulk_status(task_id: str):
    """Get the status of a bulk task."""
    if task_id not in _bulk_tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return _bulk_tasks[task_id]


@router.post("/api/bulk/{task_id}/cancel")
async def cancel_bulk(task_id: str):
    """Cancel a running bulk task. Stops after the current paper finishes."""
    if task_id not in _bulk_tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    if _bulk_tasks[task_id]["status"] != "running":
        raise HTTPException(status_code=400, detail="Task is not running")
    _bulk_cancelled.add(task_id)
    _bulk_tasks[task_id]["step"] = "cancelling"
    return {"status": "cancelling"}


@router.post("/api/bulk/generate")
async def trigger_bulk_generate(background_tasks: BackgroundTasks):
    """Generate blog posts for all eligible papers (server-side)."""
    # Prevent duplicate runs
    for task in _bulk_tasks.values():
        if task["status"] == "running":
            raise HTTPException(status_code=409, detail="A bulk task is already running")
    task_id = f"bulk-gen-{int(time.time())}"
    _bulk_tasks[task_id] = {
        "task_id": task_id,
        "type": "generate",
        "status": "running",
        "step": "starting",
        "done": 0,
        "errors": 0,
        "total": 0,
        "current_paper": None,
        "result": None,
        "error": None,
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    background_tasks.add_task(_run_bulk_generate, task_id)
    return {"task_id": task_id, "status": "started"}


async def _run_bulk_generate(task_id: str) -> None:
    """Background: generate blog posts for all eligible papers."""
    try:
        db = Database(db_path=settings.DB_PATH)
        await db.initialize()
        generator = ContentGenerator(db=db)

        all_papers = await db.get_papers()
        eligible = [
            p for p in all_papers
            if p.get("pdf_path") and not (await db.get_blog_post(p["arxiv_id"]))
        ]
        _bulk_tasks[task_id]["total"] = len(eligible)

        if not eligible:
            _bulk_tasks[task_id].update({
                "status": "complete", "step": "complete",
                "result": {"done": 0, "errors": 0, "total": 0},
                "completed_at": datetime.now(timezone.utc).isoformat(),
            })
            return

        done = 0
        errors = 0
        for i, paper in enumerate(eligible):
            if task_id in _bulk_cancelled:
                _bulk_cancelled.discard(task_id)
                _bulk_tasks[task_id].update({
                    "status": "cancelled", "step": "cancelled",
                    "done": done, "errors": errors,
                    "result": {"done": done, "errors": errors, "total": len(eligible)},
                    "completed_at": datetime.now(timezone.utc).isoformat(),
                })
                logger.info("Bulk generate %s: cancelled after %d/%d", task_id, done, len(eligible))
                return

            aid = paper["arxiv_id"]
            _bulk_tasks[task_id].update({
                "step": f"generating ({i + 1}/{len(eligible)}): {aid}",
                "current_paper": aid,
                "done": done,
                "errors": errors,
            })
            try:
                await generator.generate_content(aid)
                done += 1
                _bulk_tasks[task_id]["done"] = done
            except Exception as e:
                errors += 1
                _bulk_tasks[task_id]["errors"] = errors
                logger.error("Bulk generate %s: failed for %s: %s", task_id, aid, e)

        _bulk_tasks[task_id].update({
            "status": "complete", "step": "complete",
            "done": done, "errors": errors,
            "result": {"done": done, "errors": errors, "total": len(eligible)},
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
        logger.info("Bulk generate %s: complete, %d done, %d errors", task_id, done, errors)

    except Exception as e:
        logger.exception("Bulk generate %s failed", task_id)
        _bulk_tasks[task_id].update({
            "status": "error", "error": str(e),
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })


@router.post("/api/bulk/concepts")
async def trigger_bulk_concepts(background_tasks: BackgroundTasks):
    """Extract concepts for all eligible papers (server-side)."""
    for task in _bulk_tasks.values():
        if task["status"] == "running":
            raise HTTPException(status_code=409, detail="A bulk task is already running")
    task_id = f"bulk-con-{int(time.time())}"
    _bulk_tasks[task_id] = {
        "task_id": task_id,
        "type": "concepts",
        "status": "running",
        "step": "starting",
        "done": 0,
        "errors": 0,
        "total": 0,
        "current_paper": None,
        "result": None,
        "error": None,
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    background_tasks.add_task(_run_bulk_concepts, task_id)
    return {"task_id": task_id, "status": "started"}


async def _run_bulk_concepts(task_id: str) -> None:
    """Background: extract concepts for all eligible papers."""
    try:
        db = Database(db_path=settings.DB_PATH)
        await db.initialize()
        generator = ContentGenerator(db=db)

        all_papers = await db.get_papers()
        eligible = [
            p for p in all_papers
            if p.get("pdf_path")
            and not p.get("has_concepts")
            and p.get("concepts_status") not in ("extracting", "pending", "approved", "rejected")
        ]
        _bulk_tasks[task_id]["total"] = len(eligible)

        if not eligible:
            _bulk_tasks[task_id].update({
                "status": "complete", "step": "complete",
                "result": {"done": 0, "errors": 0, "total": 0},
                "completed_at": datetime.now(timezone.utc).isoformat(),
            })
            return

        done = 0
        errors = 0
        for i, paper in enumerate(eligible):
            if task_id in _bulk_cancelled:
                _bulk_cancelled.discard(task_id)
                _bulk_tasks[task_id].update({
                    "status": "cancelled", "step": "cancelled",
                    "done": done, "errors": errors,
                    "result": {"done": done, "errors": errors, "total": len(eligible)},
                    "completed_at": datetime.now(timezone.utc).isoformat(),
                })
                logger.info("Bulk concepts %s: cancelled after %d/%d", task_id, done, len(eligible))
                return

            aid = paper["arxiv_id"]
            _bulk_tasks[task_id].update({
                "step": f"extracting ({i + 1}/{len(eligible)}): {aid}",
                "current_paper": aid,
                "done": done,
                "errors": errors,
            })
            try:
                await generator.extract_concepts_only(aid)
                done += 1
                _bulk_tasks[task_id]["done"] = done
            except Exception as e:
                errors += 1
                _bulk_tasks[task_id]["errors"] = errors
                logger.error("Bulk concepts %s: failed for %s: %s", task_id, aid, e)

        _bulk_tasks[task_id].update({
            "status": "complete", "step": "complete",
            "done": done, "errors": errors,
            "result": {"done": done, "errors": errors, "total": len(eligible)},
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
        logger.info("Bulk concepts %s: complete, %d done, %d errors", task_id, done, errors)

    except Exception as e:
        logger.exception("Bulk concepts %s failed", task_id)
        _bulk_tasks[task_id].update({
            "status": "error", "error": str(e),
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
