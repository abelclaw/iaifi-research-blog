"""Generation API routes for triggering and monitoring blog + concept tasks."""

import asyncio
import json
import logging
import subprocess
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

import httpx
from fastapi import APIRouter, BackgroundTasks, HTTPException

import aiosqlite

from pipeline.config import settings
from pipeline.db import Database
from pipeline.orchestrator import ContentGenerator

BULK_LOG_DIR = Path("data/logs")
BULK_LOG_DIR.mkdir(parents=True, exist_ok=True)


def _log_bulk_error(task_id: str, arxiv_id: str, error: Exception) -> None:
    """Append an error entry to the bulk task log file."""
    log_file = BULK_LOG_DIR / f"{task_id}.log"
    timestamp = datetime.now(timezone.utc).isoformat()
    tb = traceback.format_exception(type(error), error, error.__traceback__)
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] FAIL {arxiv_id}\n")
        f.write(f"  {type(error).__name__}: {error}\n")
        f.write("  " + "  ".join(tb[-3:]))
        f.write("\n")


async def _get_paper_metadata(arxiv_id: str) -> dict | None:
    """Fetch paper title, authors, abstract directly from DB."""
    async with aiosqlite.connect(settings.DB_PATH) as conn:
        conn.row_factory = aiosqlite.Row
        cur = await conn.execute(
            "SELECT title, authors, abstract FROM papers WHERE arxiv_id = ?",
            (arxiv_id,),
        )
        row = await cur.fetchone()
        return dict(row) if row else None

logger = logging.getLogger(__name__)

USAGE_THRESHOLD = 80.0  # Pause bulk generation above this % of 5-hour limit
USAGE_CHECK_INTERVAL = 60  # Seconds between re-checks while waiting


async def _get_claude_oauth_token() -> str | None:
    """Retrieve Claude Code OAuth access token from macOS Keychain."""
    try:
        result = subprocess.run(
            ["security", "find-generic-password", "-s", "Claude Code-credentials", "-w"],
            capture_output=True, text=True, timeout=5,
        )
        if result.returncode != 0:
            logger.warning("Failed to read Claude Code credentials from Keychain")
            return None
        creds = json.loads(result.stdout.strip())
        return creds.get("claudeAiOauth", {}).get("accessToken")
    except Exception as e:
        logger.warning("Could not retrieve Claude OAuth token: %s", e)
        return None


async def _get_claude_usage() -> dict | None:
    """Check Claude Code subscription usage via the OAuth usage endpoint.

    Returns dict with five_hour/seven_day utilization, or None on failure.
    """
    token = await _get_claude_oauth_token()
    if not token:
        return None
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(
                "https://api.anthropic.com/api/oauth/usage",
                headers={
                    "Authorization": f"Bearer {token}",
                    "anthropic-beta": "oauth-2025-04-20",
                    "User-Agent": "claude-code/2.0.32",
                    "Accept": "application/json",
                },
                timeout=10,
            )
            resp.raise_for_status()
            return resp.json()
    except Exception as e:
        logger.warning("Failed to check Claude usage: %s", e)
        return None


async def _wait_for_usage_clearance(task_id: str, bulk_tasks: dict, usage: dict | None = None) -> None:
    """If 5-hour usage is above threshold, wait until it drops below."""
    if usage is None:
        usage = await _get_claude_usage()
    if not usage:
        logger.info("Could not check usage, continuing without throttle")
        return

    five_hour = usage.get("five_hour", {})
    utilization = five_hour.get("utilization", 0.0)
    resets_at = five_hour.get("resets_at")

    if utilization < USAGE_THRESHOLD:
        logger.info("Claude 5h usage at %.1f%% (threshold %.0f%%), continuing",
                     utilization, USAGE_THRESHOLD)
        return

    logger.info("Claude 5h usage at %.1f%% (>= %.0f%%), pausing bulk generation",
                utilization, USAGE_THRESHOLD)
    bulk_tasks[task_id]["step"] = (
        f"paused — Claude usage at {utilization:.0f}% "
        f"(waiting for < {USAGE_THRESHOLD:.0f}%)"
    )
    if resets_at:
        bulk_tasks[task_id]["usage_resets_at"] = resets_at

    while utilization >= USAGE_THRESHOLD:
        await asyncio.sleep(USAGE_CHECK_INTERVAL)
        # Check if cancelled while waiting
        if task_id in _bulk_cancelled:
            return
        usage = await _get_claude_usage()
        if not usage:
            logger.info("Usage check failed, resuming to avoid infinite wait")
            break
        utilization = usage.get("five_hour", {}).get("utilization", 0.0)
        bulk_tasks[task_id]["usage_5h"] = utilization
        bulk_tasks[task_id]["step"] = (
            f"paused — Claude usage at {utilization:.0f}% "
            f"(waiting for < {USAGE_THRESHOLD:.0f}%)"
        )
        logger.info("Claude 5h usage at %.1f%%, threshold %.0f%%",
                     utilization, USAGE_THRESHOLD)

    logger.info("Claude usage cleared (%.1f%%), resuming bulk generation", utilization)


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
    for task_type in ("generate", "concepts", "fix"):
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


# --- Usage endpoint ---

@router.get("/api/usage")
async def get_usage():
    """Return current Claude subscription usage (5h and 7d windows)."""
    usage = await _get_claude_usage()
    if not usage:
        return {"error": "Could not fetch usage", "five_hour": None, "seven_day": None}
    return usage


# --- Bulk operations (server-side, survive page refresh) ---

@router.get("/api/bulk/active")
async def get_active_bulk():
    """Return the currently running bulk task, if any."""
    for task in _bulk_tasks.values():
        if task["status"] == "running":
            return task
    return {"status": "none"}


@router.post("/api/bulk/fix-unfixed")
async def trigger_bulk_fix_unfixed(background_tasks: BackgroundTasks):
    """Fix only blog posts that have never been fixed (fix_count = 0)."""
    for task in _bulk_tasks.values():
        if task["status"] == "running":
            raise HTTPException(status_code=409, detail="A bulk task is already running")
    task_id = f"bulk-fixu-{int(time.time())}"
    _bulk_tasks[task_id] = {
        "task_id": task_id,
        "type": "fix-unfixed",
        "status": "running",
        "step": "starting",
        "done": 0,
        "errors": 0,
        "total": 0,
        "current_paper": None,
        "result": None,
        "error": None,
        "usage_5h": None,
        "last_fix_duration": None,
        "log_file": str(BULK_LOG_DIR / f"{task_id}.log"),
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    background_tasks.add_task(_run_bulk_fix_unfixed, task_id)
    return {"task_id": task_id, "status": "started"}


async def _run_bulk_fix_unfixed(task_id: str) -> None:
    """Background: fix only blog posts with fix_count = 0."""
    try:
        db = Database(db_path=settings.DB_PATH)
        await db.initialize()

        from pipeline.generator.post_fixer import PostFixer
        from pipeline.generator.claude_cli_client import ClaudeCLIClient

        llm = ClaudeCLIClient(model="claude-opus-4-6")
        fixer = PostFixer(llm_client=llm)

        # Get only unfixed posts
        all_posts = await db.get_blog_posts()
        eligible = [
            p for p in all_posts
            if p.get("content") and (not p.get("fix_count") or p["fix_count"] == 0)
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
        for i, post in enumerate(eligible):
            if task_id in _bulk_cancelled:
                _bulk_cancelled.discard(task_id)
                _bulk_tasks[task_id].update({
                    "status": "cancelled", "step": "cancelled",
                    "done": done, "errors": errors,
                    "result": {"done": done, "errors": errors, "total": len(eligible)},
                    "completed_at": datetime.now(timezone.utc).isoformat(),
                })
                logger.info("Bulk fix-unfixed %s: cancelled after %d/%d", task_id, done, len(eligible))
                return

            aid = post["paper_arxiv_id"]
            _bulk_tasks[task_id].update({
                "step": f"fixing ({i + 1}/{len(eligible)}): {aid}",
                "current_paper": aid,
                "done": done,
                "errors": errors,
            })
            try:
                paper = await _get_paper_metadata(aid)
                if not paper:
                    raise ValueError(f"No paper found for {aid}")

                fix_start = time.time()
                fixed_content = await fixer.fix_post(
                    content=post["content"],
                    title=paper["title"],
                    arxiv_id=aid,
                    authors=paper.get("authors", ""),
                    abstract=paper.get("abstract", ""),
                )
                fix_duration = round(time.time() - fix_start, 1)
                # Re-check fix_count before writing — guard against overlap
                # with a previous cancelled task that finished its last fix
                current_fc = await db.get_fix_count(aid)
                if current_fc and current_fc > 0:
                    logger.info("Skipping %s: already fixed (fix_count=%s)", aid, current_fc)
                    done += 1
                    _bulk_tasks[task_id]["done"] = done
                    _bulk_tasks[task_id]["last_fix_duration"] = fix_duration
                    continue
                await db.update_blog_post_content(aid, fixed_content)
                await db.increment_fix_count(aid)
                done += 1
                _bulk_tasks[task_id]["done"] = done
                _bulk_tasks[task_id]["last_fix_duration"] = fix_duration
            except Exception as e:
                errors += 1
                _bulk_tasks[task_id]["errors"] = errors
                _log_bulk_error(task_id, aid, e)
                logger.error("Bulk fix-unfixed %s: failed for %s: %s", task_id, aid, e)

            # Check usage after each fix
            usage = await _get_claude_usage()
            if usage:
                _bulk_tasks[task_id]["usage_5h"] = usage.get("five_hour", {}).get("utilization", 0.0)
            await _wait_for_usage_clearance(task_id, _bulk_tasks, usage=usage)
            if task_id in _bulk_cancelled:
                _bulk_cancelled.discard(task_id)
                _bulk_tasks[task_id].update({
                    "status": "cancelled", "step": "cancelled",
                    "done": done, "errors": errors,
                    "result": {"done": done, "errors": errors, "total": len(eligible)},
                    "completed_at": datetime.now(timezone.utc).isoformat(),
                })
                logger.info("Bulk fix-unfixed %s: cancelled while waiting, %d/%d", task_id, done, len(eligible))
                return

        _bulk_tasks[task_id].update({
            "status": "complete", "step": "complete",
            "done": done, "errors": errors,
            "result": {"done": done, "errors": errors, "total": len(eligible)},
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
        logger.info("Bulk fix-unfixed %s: complete, %d done, %d errors", task_id, done, errors)

    except Exception as e:
        logger.exception("Bulk fix-unfixed %s failed", task_id)
        _bulk_tasks[task_id].update({
            "status": "error", "error": str(e),
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })


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
        "log_file": str(BULK_LOG_DIR / f"{task_id}.log"),
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
                _log_bulk_error(task_id, aid, e)
                logger.error("Bulk generate %s: failed for %s: %s", task_id, aid, e)

            # Check usage after each blog, show it in status, and wait if above threshold
            usage = await _get_claude_usage()
            if usage:
                _bulk_tasks[task_id]["usage_5h"] = usage.get("five_hour", {}).get("utilization", 0.0)
            await _wait_for_usage_clearance(task_id, _bulk_tasks, usage=usage)
            if task_id in _bulk_cancelled:
                _bulk_cancelled.discard(task_id)
                _bulk_tasks[task_id].update({
                    "status": "cancelled", "step": "cancelled",
                    "done": done, "errors": errors,
                    "result": {"done": done, "errors": errors, "total": len(eligible)},
                    "completed_at": datetime.now(timezone.utc).isoformat(),
                })
                logger.info("Bulk generate %s: cancelled while waiting for usage, %d/%d", task_id, done, len(eligible))
                return

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


# --- Blog post fixing (remove LLM signatures, fix references) ---

@router.post("/api/fix/{arxiv_id}")
async def trigger_fix(arxiv_id: str, background_tasks: BackgroundTasks):
    """Trigger blog post fix (remove LLM signatures, fix typos) in the background."""
    task_id = f"fix-{arxiv_id}-{int(time.time())}"
    _tasks[task_id] = {
        "task_id": task_id,
        "arxiv_id": arxiv_id,
        "type": "fix",
        "status": "running",
        "step": "starting",
        "result": None,
        "error": None,
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    _paper_tasks[(arxiv_id, "fix")] = task_id
    background_tasks.add_task(_run_fix, task_id, arxiv_id)
    return {"task_id": task_id, "status": "started"}


async def _run_fix(task_id: str, arxiv_id: str) -> None:
    """Background: fix a single blog post."""
    try:
        db = Database(db_path=settings.DB_PATH)
        await db.initialize()

        _tasks[task_id]["step"] = "loading_post"

        # Get the blog post
        post = await db.get_blog_post(arxiv_id)
        if not post:
            raise ValueError(f"No blog post found for {arxiv_id}")

        # Get the paper for metadata
        paper = await _get_paper_metadata(arxiv_id)
        if not paper:
            raise ValueError(f"No paper found for {arxiv_id}")

        _tasks[task_id]["step"] = "fixing_post"

        # Initialize fixer with the same LLM client used for generation
        from pipeline.generator.post_fixer import PostFixer
        from pipeline.generator.claude_cli_client import ClaudeCLIClient

        llm = ClaudeCLIClient(model="claude-opus-4-6")
        fixer = PostFixer(llm_client=llm)

        fixed_content = await fixer.fix_post(
            content=post["content"],
            title=paper["title"],
            arxiv_id=arxiv_id,
            authors=paper.get("authors", ""),
            abstract=paper.get("abstract", ""),
        )

        # Update the blog post in the database
        word_count = len(fixed_content.split())
        await db.update_blog_post_content(arxiv_id, fixed_content)
        await db.increment_fix_count(arxiv_id)

        _tasks[task_id].update({
            "status": "complete",
            "step": "complete",
            "result": {
                "word_count": word_count,
            },
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
        logger.info("Fix task %s complete for %s (%d words)", task_id, arxiv_id, word_count)

    except Exception as e:
        logger.exception("Fix task %s failed for %s", task_id, arxiv_id)
        _tasks[task_id].update({
            "status": "error",
            "error": str(e),
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })


@router.post("/api/bulk/fix")
async def trigger_bulk_fix(background_tasks: BackgroundTasks):
    """Fix all blog posts that have content (remove LLM signatures)."""
    for task in _bulk_tasks.values():
        if task["status"] == "running":
            raise HTTPException(status_code=409, detail="A bulk task is already running")
    task_id = f"bulk-fix-{int(time.time())}"
    _bulk_tasks[task_id] = {
        "task_id": task_id,
        "type": "fix",
        "status": "running",
        "step": "starting",
        "done": 0,
        "errors": 0,
        "total": 0,
        "current_paper": None,
        "result": None,
        "error": None,
        "usage_5h": None,
        "last_fix_duration": None,
        "log_file": str(BULK_LOG_DIR / f"{task_id}.log"),
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    background_tasks.add_task(_run_bulk_fix, task_id)
    return {"task_id": task_id, "status": "started"}


async def _run_bulk_fix(task_id: str) -> None:
    """Background: fix all blog posts."""
    try:
        db = Database(db_path=settings.DB_PATH)
        await db.initialize()

        from pipeline.generator.post_fixer import PostFixer
        from pipeline.generator.claude_cli_client import ClaudeCLIClient

        llm = ClaudeCLIClient(model="claude-opus-4-6")
        fixer = PostFixer(llm_client=llm)

        # Get all posts with content
        all_posts = await db.get_blog_posts()
        eligible = [p for p in all_posts if p.get("content")]
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
        for i, post in enumerate(eligible):
            if task_id in _bulk_cancelled:
                _bulk_cancelled.discard(task_id)
                _bulk_tasks[task_id].update({
                    "status": "cancelled", "step": "cancelled",
                    "done": done, "errors": errors,
                    "result": {"done": done, "errors": errors, "total": len(eligible)},
                    "completed_at": datetime.now(timezone.utc).isoformat(),
                })
                logger.info("Bulk fix %s: cancelled after %d/%d", task_id, done, len(eligible))
                return

            aid = post["paper_arxiv_id"]
            _bulk_tasks[task_id].update({
                "step": f"fixing ({i + 1}/{len(eligible)}): {aid}",
                "current_paper": aid,
                "done": done,
                "errors": errors,
            })
            try:
                paper = await _get_paper_metadata(aid)
                if not paper:
                    raise ValueError(f"No paper found for {aid}")

                fix_start = time.time()
                fixed_content = await fixer.fix_post(
                    content=post["content"],
                    title=paper["title"],
                    arxiv_id=aid,
                    authors=paper.get("authors", ""),
                    abstract=paper.get("abstract", ""),
                )
                fix_duration = round(time.time() - fix_start, 1)
                await db.update_blog_post_content(aid, fixed_content)
                await db.increment_fix_count(aid)
                done += 1
                _bulk_tasks[task_id]["done"] = done
                _bulk_tasks[task_id]["last_fix_duration"] = fix_duration
            except Exception as e:
                errors += 1
                _bulk_tasks[task_id]["errors"] = errors
                _log_bulk_error(task_id, aid, e)
                logger.error("Bulk fix %s: failed for %s: %s", task_id, aid, e)

            # Check usage after each fix, show it in status, and wait if above threshold
            usage = await _get_claude_usage()
            if usage:
                _bulk_tasks[task_id]["usage_5h"] = usage.get("five_hour", {}).get("utilization", 0.0)
            await _wait_for_usage_clearance(task_id, _bulk_tasks, usage=usage)
            if task_id in _bulk_cancelled:
                _bulk_cancelled.discard(task_id)
                _bulk_tasks[task_id].update({
                    "status": "cancelled", "step": "cancelled",
                    "done": done, "errors": errors,
                    "result": {"done": done, "errors": errors, "total": len(eligible)},
                    "completed_at": datetime.now(timezone.utc).isoformat(),
                })
                logger.info("Bulk fix %s: cancelled while waiting for usage, %d/%d", task_id, done, len(eligible))
                return

        _bulk_tasks[task_id].update({
            "status": "complete", "step": "complete",
            "done": done, "errors": errors,
            "result": {"done": done, "errors": errors, "total": len(eligible)},
            "completed_at": datetime.now(timezone.utc).isoformat(),
        })
        logger.info("Bulk fix %s: complete, %d done, %d errors", task_id, done, errors)

    except Exception as e:
        logger.exception("Bulk fix %s failed", task_id)
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
        "log_file": str(BULK_LOG_DIR / f"{task_id}.log"),
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
                _log_bulk_error(task_id, aid, e)
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
