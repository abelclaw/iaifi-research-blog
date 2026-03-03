"""Discovery API routes for triggering and monitoring paper discovery."""

import logging
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, BackgroundTasks, HTTPException

from pipeline.config import settings
from pipeline.db import Database
from pipeline.fetcher.arxiv_client import ArxivClient
from pipeline.fetcher.iaifi_scraper import scrape_all_papers
from pipeline.orchestrator import DiscoveryOrchestrator

logger = logging.getLogger(__name__)

router = APIRouter()

# In-memory task tracking (sufficient for single-user local app)
_tasks: dict[str, dict] = {}


@router.post("/api/discover")
async def trigger_discovery(background_tasks: BackgroundTasks):
    """Trigger paper discovery pipeline in the background.

    Returns immediately with a task_id that can be used to poll for status.
    """
    task_id = str(uuid.uuid4())
    _tasks[task_id] = {
        "task_id": task_id,
        "status": "running",
        "result": None,
        "error": None,
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    background_tasks.add_task(run_discovery, task_id)
    return {"task_id": task_id, "status": "started"}


@router.get("/api/discover/{task_id}/status")
async def discovery_status(task_id: str):
    """Get the status of a discovery task.

    Returns the full task dict including status, result (if complete),
    and error (if failed).
    """
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return _tasks[task_id]


async def run_discovery(task_id: str) -> None:
    """Background function that runs the full discovery pipeline.

    Instantiates all pipeline components, runs discovery, and updates
    the task status on completion or failure.
    """
    try:
        # Initialize pipeline components from config
        db = Database(db_path=settings.DB_PATH)
        await db.initialize()

        arxiv_client = ArxivClient(
            pdf_dir=settings.PDF_DIR,
            delay_seconds=settings.ARXIV_DELAY_SECONDS,
        )

        orchestrator = DiscoveryOrchestrator(
            db=db,
            arxiv_client=arxiv_client,
        )

        # Run the discovery pipeline
        result = await orchestrator.discover()

        # Update task with success
        _tasks[task_id].update({
            "status": "complete",
            "result": {
                "total_scraped": result.total_scraped,
                "new_papers": result.new_papers,
                "metadata_fetched": result.metadata_fetched,
                "pdfs_downloaded": result.pdfs_downloaded,
                "errors": result.errors,
            },
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
        logger.info(
            f"Discovery task {task_id} complete: "
            f"{result.new_papers} new papers found"
        )

    except Exception as e:
        logger.exception(f"Discovery task {task_id} failed")
        _tasks[task_id].update({
            "status": "error",
            "error": str(e),
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
