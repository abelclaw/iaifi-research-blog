# Phase 1: Paper Ingestion Pipeline - Research

**Researched:** 2026-03-03
**Domain:** Web scraping (IAIFI), arXiv API integration, PDF downloading, SQLite state management, FastAPI admin trigger
**Confidence:** HIGH

## Summary

Phase 1 builds the data foundation: scraping the IAIFI website for paper listings, enriching them via the arXiv API, downloading PDFs, persisting state in SQLite, and providing an admin trigger endpoint. The IAIFI website is a Jekyll-built static site with four category pages (Foundational AI, Theoretical Physics, Experimental Physics, Astrophysics) plus a combined listing page -- all static HTML with consistent formatting. Each paper entry contains a title, authors, arXiv ID link, optional code link, category tag, and abstract.

The arXiv API (via the `arxiv.py` wrapper) provides full metadata enrichment and PDF download. The key constraint is a mandatory 3-second delay between API requests. For IAIFI's scale (~250-300 total papers across 4 categories), a full discovery run takes approximately 12-15 minutes for metadata fetching. The cross-referencing requirement (INGEST-03) is straightforward: scrape IAIFI pages to get the master list of arxiv IDs, then compare against the SQLite database of previously ingested papers to identify new ones.

The admin trigger (INGEST-04) uses FastAPI with BackgroundTasks to run the discovery pipeline asynchronously while returning an immediate response. Progress can be tracked via polling or SSE. The admin UI for this phase is minimal -- a trigger button and a results list, not the full review interface (that is Phase 3).

**Primary recommendation:** Build the IAIFI scraper, arXiv client, and SQLite storage as independent pipeline modules, with a thin FastAPI layer that imports and orchestrates them. Use `arxiv.py` 2.4.0 for arXiv integration (not raw API calls). Use `aiosqlite` for async database access within FastAPI's async context.

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| INGEST-01 | System can scrape IAIFI website (iaifi.org/papers.html) for paper list with arxiv IDs, authors, abstracts, categories | IAIFI site is static HTML across 5 pages (main + 4 categories). BeautifulSoup4 parses the consistent entry format: bold/italic title, author text, arXiv link, category link, abstract. Scrape all 4 category pages to get complete coverage with category assignments. |
| INGEST-02 | System can fetch full paper metadata and PDFs from arxiv API | `arxiv.py` 2.4.0 provides `Search(id_list=[...])` for batch ID lookup and `Result.download_pdf()` for PDF download. Built-in rate limiting via `Client(delay_seconds=3.0)`. Returns title, authors, abstract, categories, published date, PDF URL. |
| INGEST-03 | System cross-references arxiv scan against IAIFI master list to identify new papers | SQLite stores all previously ingested arxiv IDs. On each discovery run, scrape IAIFI for current IDs, query SQLite for existing IDs, compute the set difference. New papers = IAIFI IDs minus already-ingested IDs. |
| INGEST-04 | Admin can trigger paper discovery on demand via local web app | FastAPI endpoint `POST /api/discover` triggers the pipeline via BackgroundTasks. Returns immediately with a task ID. Admin polls `GET /api/discover/{task_id}/status` for progress. Minimal HTML UI with a button and results table. |
</phase_requirements>

## Standard Stack

### Core

| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| Python | 3.12+ | Runtime | Current stable. Required by FastAPI, async patterns, and modern type hints. |
| FastAPI | 0.115+ | Admin API and trigger endpoint | Async-first, auto-generates Swagger docs, built-in BackgroundTasks for pipeline triggering. |
| Uvicorn | 0.34+ | ASGI server | Standard FastAPI companion. `fastapi dev` wraps it with auto-reload. |
| BeautifulSoup4 | 4.14.3 | IAIFI website scraping | Standard HTML parser. IAIFI pages are static HTML -- no JS rendering needed. |
| arxiv.py | 2.4.0 | arXiv API client | Official Python wrapper. Handles search, metadata, PDF download, rate limiting. Released Jan 2026. |
| requests | 2.32+ | HTTP client for IAIFI page fetching | Standard Python HTTP library. Used by BS4 scraping. |
| aiosqlite | 0.22.1 | Async SQLite access | Async bridge to stdlib sqlite3. Works with FastAPI's async handlers. |
| Pydantic | 2.10+ | Data models and validation | Bundled with FastAPI. Define Paper and DiscoveryResult schemas. |

### Supporting

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| lxml | 5.x | Fast HTML parser backend for BS4 | Use as BS4's parser for better performance: `BeautifulSoup(html, 'lxml')` |
| httpx | 0.28+ | Async HTTP client | If IAIFI scraping needs to be async (optional -- requests is fine for 5 pages) |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| arxiv.py | Raw arXiv API via requests | arxiv.py handles pagination, rate limiting, Atom XML parsing. Raw API means reimplementing all of this. |
| BeautifulSoup4 | Scrapy | Scrapy is a full crawling framework. We scrape 5 static pages -- BS4 + requests is sufficient and simpler. |
| aiosqlite | SQLAlchemy async | SQLAlchemy adds ORM complexity. For 3 tables with simple queries, raw SQL via aiosqlite is clearer. |
| SQLite | JSON files | JSON lacks querying, indexing, and transactional safety. SQLite is zero-config and handles concurrency. |

**Installation:**
```bash
uv pip install fastapi uvicorn[standard] beautifulsoup4 lxml arxiv requests aiosqlite pydantic
```

## Architecture Patterns

### Recommended Project Structure (Phase 1 scope)
```
pipeline/
    __init__.py
    models.py               # Pydantic models: Paper, DiscoveryResult, PaperStatus
    config.py                # Configuration (paths, delays, URLs)
    db.py                    # SQLite schema, queries, connection management
    fetcher/
        __init__.py
        iaifi_scraper.py     # Scrape IAIFI website for paper listings
        arxiv_client.py      # arXiv API wrapper (metadata + PDF download)
    orchestrator.py          # Discovery pipeline: scrape -> cross-ref -> fetch -> store
admin/
    __init__.py
    app.py                   # FastAPI application
    routes/
        __init__.py
        discovery.py         # POST /api/discover, GET /api/discover/status
        papers.py            # GET /api/papers (list ingested papers)
    static/
        index.html           # Minimal admin UI (trigger button + results table)
data/                        # Runtime data (git-ignored)
    papers.db                # SQLite database
    pdfs/                    # Downloaded PDFs
```

### Pattern 1: Scraper with Adapter Interface

**What:** Isolate IAIFI scraping behind a clean interface so it can be replaced if the website structure changes.

**When to use:** Always. The IAIFI website is the most fragile dependency in the system.

**Example:**
```python
# pipeline/fetcher/iaifi_scraper.py
from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests
import re

@dataclass
class ScrapedPaper:
    """Raw paper data from IAIFI website scraping."""
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str | None
    category: str          # "Foundational AI", "Theoretical Physics", etc.
    code_url: str | None
    source_url: str        # Which IAIFI page it was scraped from

CATEGORY_PAGES = {
    "Foundational AI": "https://iaifi.org/papers-ai.html",
    "Theoretical Physics": "https://iaifi.org/papers-theory.html",
    "Experimental Physics": "https://iaifi.org/papers-experiment.html",
    "Astrophysics": "https://iaifi.org/papers-astro.html",
}

ARXIV_ID_PATTERN = re.compile(r"arXiv:(\d{4}\.\d{4,5}(?:v\d+)?)")

def scrape_all_papers() -> list[ScrapedPaper]:
    """Scrape all 4 IAIFI category pages and return deduplicated paper list."""
    all_papers: dict[str, ScrapedPaper] = {}
    for category, url in CATEGORY_PAGES.items():
        papers = scrape_category_page(url, category)
        for paper in papers:
            if paper.arxiv_id not in all_papers:
                all_papers[paper.arxiv_id] = paper
    return list(all_papers.values())

def scrape_category_page(url: str, category: str) -> list[ScrapedPaper]:
    """Scrape a single IAIFI category page."""
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    # Parse paper entries from the page structure
    # (implementation details depend on exact HTML -- see Code Examples below)
    ...
```

### Pattern 2: arXiv Client with Rate Limiting

**What:** Wrap arxiv.py with project-specific defaults and batch operations.

**When to use:** For all arXiv API interactions.

**Example:**
```python
# pipeline/fetcher/arxiv_client.py
import arxiv
from pathlib import Path
from pipeline.models import Paper

class ArxivClient:
    def __init__(self, pdf_dir: str = "data/pdfs", delay_seconds: float = 3.0):
        self.client = arxiv.Client(
            page_size=100,
            delay_seconds=delay_seconds,
            num_retries=3,
        )
        self.pdf_dir = Path(pdf_dir)
        self.pdf_dir.mkdir(parents=True, exist_ok=True)

    def fetch_metadata(self, arxiv_ids: list[str]) -> list[arxiv.Result]:
        """Fetch metadata for a list of arXiv IDs."""
        search = arxiv.Search(id_list=arxiv_ids)
        return list(self.client.results(search))

    def download_pdf(self, result: arxiv.Result) -> Path:
        """Download PDF for a single paper. Returns path to downloaded file."""
        short_id = result.get_short_id().replace("/", "_")
        filepath = self.pdf_dir / f"{short_id}.pdf"
        if filepath.exists():
            return filepath  # Already downloaded -- skip
        result.download_pdf(dirpath=str(self.pdf_dir), filename=f"{short_id}.pdf")
        return filepath
```

### Pattern 3: SQLite State Tracking with Status Enum

**What:** Track each paper's progress through the pipeline with a status field. Resume from last completed stage on failure.

**When to use:** Always. The pipeline is long-running and expensive. Never redo work.

**Example:**
```python
# pipeline/models.py
from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class PaperStatus(str, Enum):
    DISCOVERED = "discovered"         # Found on IAIFI, not yet enriched
    METADATA_FETCHED = "metadata_fetched"  # arXiv metadata retrieved
    PDF_DOWNLOADED = "pdf_downloaded"       # PDF saved to disk
    INGESTION_COMPLETE = "ingestion_complete"  # Ready for Phase 2

class Paper(BaseModel):
    arxiv_id: str                     # Primary key (e.g., "2601.22029")
    title: str
    authors: list[str]
    abstract: str
    categories: list[str]             # arXiv categories (e.g., ["cs.AI", "hep-th"])
    iaifi_category: str               # IAIFI category from scraping
    published: datetime | None = None
    pdf_path: str | None = None
    code_url: str | None = None
    status: PaperStatus = PaperStatus.DISCOVERED
    created_at: datetime | None = None
    updated_at: datetime | None = None
```

### Pattern 4: Discovery Orchestrator

**What:** Sequence the full discovery pipeline: scrape IAIFI, identify new papers, fetch metadata, download PDFs.

**When to use:** This is the core pipeline for Phase 1.

**Example:**
```python
# pipeline/orchestrator.py
from dataclasses import dataclass

@dataclass
class DiscoveryResult:
    total_scraped: int
    new_papers: int
    metadata_fetched: int
    pdfs_downloaded: int
    errors: list[str]

class DiscoveryOrchestrator:
    def __init__(self, db, scraper, arxiv_client):
        self.db = db
        self.scraper = scraper
        self.arxiv_client = arxiv_client

    async def discover(self, on_progress=None) -> DiscoveryResult:
        """Full discovery pipeline."""
        # Step 1: Scrape IAIFI for all papers
        scraped = self.scraper.scrape_all_papers()

        # Step 2: Cross-reference against database
        existing_ids = await self.db.get_all_arxiv_ids()
        new_papers = [p for p in scraped if p.arxiv_id not in existing_ids]

        # Step 3: Fetch metadata from arXiv for new papers
        if new_papers:
            new_ids = [p.arxiv_id for p in new_papers]
            metadata = self.arxiv_client.fetch_metadata(new_ids)
            # ... store to database, download PDFs ...

        return DiscoveryResult(...)
```

### Pattern 5: FastAPI Background Task with Status Tracking

**What:** The discovery endpoint triggers the pipeline in the background and returns immediately. A status endpoint lets the admin check progress.

**When to use:** For the INGEST-04 admin trigger requirement.

**Example:**
```python
# admin/routes/discovery.py
from fastapi import APIRouter, BackgroundTasks
import uuid

router = APIRouter()
_tasks: dict[str, dict] = {}  # In-memory task tracking (sufficient for local app)

@router.post("/api/discover")
async def trigger_discovery(background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    _tasks[task_id] = {"status": "running", "result": None}
    background_tasks.add_task(run_discovery, task_id)
    return {"task_id": task_id, "status": "started"}

@router.get("/api/discover/{task_id}/status")
async def discovery_status(task_id: str):
    if task_id not in _tasks:
        raise HTTPException(404, "Task not found")
    return _tasks[task_id]

async def run_discovery(task_id: str):
    try:
        orchestrator = get_orchestrator()
        result = await orchestrator.discover()
        _tasks[task_id] = {"status": "complete", "result": result}
    except Exception as e:
        _tasks[task_id] = {"status": "error", "error": str(e)}
```

### Anti-Patterns to Avoid

- **Scraping the main papers.html only:** The main page appears to be a highlights/recent selection, not the complete list. Scrape all 4 category pages for full coverage.
- **Direct arXiv API calls without arxiv.py:** Reimplements rate limiting, pagination, Atom XML parsing. arxiv.py handles all of this.
- **Synchronous pipeline in FastAPI route handler:** The discovery pipeline takes 12-15 minutes for a full run. Must use BackgroundTasks or similar async mechanism.
- **Storing paper data only in JSON files:** Loses querying, indexing, and transactional guarantees. SQLite is zero-config and handles this perfectly.
- **Re-downloading PDFs on every run:** Cache PDFs by arxiv ID. Check for existence before downloading.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| arXiv API client | Custom HTTP + XML parsing | `arxiv.py` 2.4.0 | Handles Atom XML, pagination, rate limiting, retries, PDF download. Maintained, 2.4K GitHub stars. |
| Rate limiting | Custom sleep/retry logic | `arxiv.Client(delay_seconds=3.0, num_retries=3)` | Built into arxiv.py's Client class. Handles connection pooling and backoff. |
| HTML parsing | Regex on raw HTML | BeautifulSoup4 with lxml | Regex breaks on malformed HTML, entity encoding, nested tags. BS4 handles all edge cases. |
| Async SQLite | Thread pool executor wrapping sqlite3 | `aiosqlite` 0.22.1 | Production-stable async bridge. Same API as sqlite3 but async. |
| Background task management | Custom thread/process pool | FastAPI `BackgroundTasks` | Built into FastAPI. Handles async/sync functions. Sufficient for single-user local app. |

**Key insight:** Phase 1's value is in the orchestration and data model, not in low-level API wrapping. Every external service integration has a well-maintained Python library. Use them.

## Common Pitfalls

### Pitfall 1: IAIFI Website Structure Changes Break Scraper
**What goes wrong:** IAIFI updates their Jekyll site, paper entry formatting changes, scraper silently returns zero or partial results.
**Why it happens:** Screen scraping is inherently fragile. No contract exists between the website and the scraper.
**How to avoid:**
- Validate scraper output: if a category page returns 0 papers, raise an error (it should never be empty).
- Store the raw HTML of each scrape for debugging.
- Log paper counts per category and alert if they drop significantly from the previous run.
- Build the scraper with clear separation between HTML fetching and parsing so the parser can be updated independently.
**Warning signs:** Discovery run returns significantly fewer papers than the last run. Paper counts drop to zero for a category.

### Pitfall 2: arXiv Rate Limiting Causes Silent Data Loss
**What goes wrong:** Exceeding the 3-second rate limit causes the API to return empty results or throttle requests. The pipeline treats empty responses as "no papers found" and continues.
**Why it happens:** arxiv.py's built-in rate limiting handles individual requests, but batch operations (fetching metadata for 50+ papers) can still hit limits if the connection pool is misconfigured.
**How to avoid:**
- Use `arxiv.Client(delay_seconds=3.0)` -- never lower than 3 seconds.
- After fetching metadata for a batch, compare the count of results against the count of requested IDs. If they differ, some papers were missed.
- Log every arXiv API response. Check for HTTP 429 status codes.
- For initial bulk ingestion of all IAIFI papers (~250-300), process in batches of 20-30 IDs with explicit delays between batches.
**Warning signs:** Metadata fetch returns fewer results than requested IDs. HTTP 429 in logs.

### Pitfall 3: Papers Appearing on Multiple Category Pages
**What goes wrong:** The same paper appears on the main papers.html and one or more category pages (e.g., a paper tagged "Foundational AI" appears on both papers.html and papers-ai.html). Without deduplication, the pipeline processes it multiple times.
**Why it happens:** IAIFI categorizes papers but some papers span categories or appear on the main page as highlights.
**How to avoid:**
- Use arxiv ID as the deduplication key across all pages.
- Scrape all 4 category pages, build a dict keyed by arxiv ID, skip duplicates.
- The first encountered category assignment wins (or store all categories as a list).
**Warning signs:** Paper count from scraping is higher than expected unique papers. Same arxiv ID appears in database twice.

### Pitfall 4: arxiv IDs With and Without Version Numbers
**What goes wrong:** IAIFI pages link to `arXiv:2601.22029` (no version) while the arXiv API returns `2601.22029v1` (with version). The cross-reference logic fails because the IDs don't match.
**Why it happens:** arXiv IDs can be versioned (v1, v2, etc.) or unversioned (latest). The IAIFI website consistently uses unversioned IDs, but the API returns versioned IDs.
**How to avoid:**
- Normalize all arxiv IDs by stripping the version suffix before comparison.
- Store the base ID (no version) as the primary key and the full versioned ID as a separate field.
- Regex: `re.sub(r'v\d+$', '', arxiv_id)` to strip version suffixes.
**Warning signs:** Papers that exist in both the scraped list and the database are being treated as "new."

### Pitfall 5: PDF Download Failures for Older Papers
**What goes wrong:** Some older arXiv papers have PDFs that time out, redirect, or are temporarily unavailable. The pipeline fails mid-download and leaves a partial file on disk.
**Why it happens:** arXiv serves PDFs from multiple mirrors. During high-traffic periods, downloads can be slow or fail. Old papers occasionally have format issues.
**How to avoid:**
- Implement retry logic for PDF downloads (3 retries with exponential backoff).
- Use atomic file writes: download to a temp file, rename on success. Never leave partial PDFs.
- Track download status separately from metadata fetch. A failed download should not block further processing of other papers.
- PDF download is non-blocking for Phase 1 completion -- the paper's metadata is valuable even without the PDF.
**Warning signs:** `.pdf` files with 0 bytes or suspiciously small sizes. Papers stuck in "metadata_fetched" status.

### Pitfall 6: SQLite Locking Under Concurrent Access
**What goes wrong:** The FastAPI admin endpoint and the background discovery task both access SQLite simultaneously, causing "database is locked" errors.
**Why it happens:** SQLite allows only one writer at a time. If the discovery background task holds a write lock while the admin polls for status, reads can block.
**How to avoid:**
- Enable WAL (Write-Ahead Logging) mode: `PRAGMA journal_mode=WAL;` -- this allows concurrent reads during writes.
- Keep write transactions short. Commit after each paper is processed, not at the end of the entire batch.
- Use a single aiosqlite connection shared across the application (connection pool of 1 is fine for SQLite).
**Warning signs:** "database is locked" errors in logs. Admin UI hangs when polling during active discovery.

## Code Examples

### IAIFI Page HTML Parsing

Based on verified IAIFI page structure (fetched 2026-03-03). Papers follow this pattern:

```
**_Paper Title_**
Author1, Author2, Author3
[ arXiv:XXXX.XXXXX | code ]
[Category](/papers-category.html)

Abstract Abstract text here...
```

```python
# pipeline/fetcher/iaifi_scraper.py
import re
from bs4 import BeautifulSoup, Tag

ARXIV_ID_RE = re.compile(r"arXiv:(\d{4}\.\d{4,5}(?:v\d+)?)")
ARXIV_LINK_RE = re.compile(r"https://arxiv\.org/abs/(\d{4}\.\d{4,5}(?:v\d+)?)")

def parse_papers_from_html(html: str, category: str) -> list[ScrapedPaper]:
    """Parse paper entries from an IAIFI category page.

    The IAIFI pages are Jekyll-generated static HTML. Papers are rendered as
    sequences of <p> and other block elements. Each paper entry contains:
    - A bold+italic title: <strong><em>Title</em></strong>
    - Author names as plain text
    - An arXiv link: <a href="https://arxiv.org/abs/XXXX.XXXXX">arXiv:XXXX.XXXXX</a>
    - Optional code link
    - Abstract text (may be in italics, prefixed with "Abstract")
    """
    soup = BeautifulSoup(html, "lxml")
    papers = []

    # Find all arXiv links as anchors for paper entries
    arxiv_links = soup.find_all("a", href=ARXIV_LINK_RE)

    for link in arxiv_links:
        arxiv_id_match = ARXIV_LINK_RE.search(link.get("href", ""))
        if not arxiv_id_match:
            continue
        arxiv_id = arxiv_id_match.group(1)
        # Strip version suffix for normalization
        base_id = re.sub(r"v\d+$", "", arxiv_id)

        # Navigate up to find the containing block for this paper
        # Extract title, authors, abstract from surrounding elements
        # (Exact navigation depends on final HTML structure -- test with real pages)

        paper = ScrapedPaper(
            arxiv_id=base_id,
            title="...",       # Extract from nearest <strong><em> ancestor
            authors=["..."],   # Extract from text between title and arXiv link
            abstract=None,     # Extract from "Abstract" prefixed text
            category=category,
            code_url=None,     # Extract from sibling "code" link if present
            source_url=f"iaifi.org category: {category}",
        )
        papers.append(paper)

    return papers
```

### SQLite Schema

```python
# pipeline/db.py
import aiosqlite
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS papers (
    arxiv_id TEXT PRIMARY KEY,           -- Base ID without version (e.g., "2601.22029")
    arxiv_id_versioned TEXT,             -- Full versioned ID (e.g., "2601.22029v1")
    title TEXT NOT NULL,
    authors TEXT NOT NULL,               -- JSON array of author names
    abstract TEXT NOT NULL,
    arxiv_categories TEXT NOT NULL,      -- JSON array (e.g., ["cs.AI", "hep-th"])
    iaifi_category TEXT NOT NULL,        -- IAIFI category name
    published TEXT,                      -- ISO datetime from arXiv
    updated TEXT,                        -- ISO datetime from arXiv
    pdf_path TEXT,                       -- Local path to downloaded PDF
    pdf_url TEXT,                        -- arXiv PDF URL
    code_url TEXT,                       -- GitHub/code URL from IAIFI page
    status TEXT NOT NULL DEFAULT 'discovered',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS discovery_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at TEXT NOT NULL DEFAULT (datetime('now')),
    completed_at TEXT,
    total_scraped INTEGER DEFAULT 0,
    new_papers INTEGER DEFAULT 0,
    metadata_fetched INTEGER DEFAULT 0,
    pdfs_downloaded INTEGER DEFAULT 0,
    errors TEXT,                          -- JSON array of error messages
    status TEXT NOT NULL DEFAULT 'running'  -- running, complete, failed
);

CREATE INDEX IF NOT EXISTS idx_papers_status ON papers(status);
CREATE INDEX IF NOT EXISTS idx_papers_iaifi_category ON papers(iaifi_category);
"""

class Database:
    def __init__(self, db_path: str = "data/papers.db"):
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    async def initialize(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("PRAGMA journal_mode=WAL")
            await db.executescript(SCHEMA)
            await db.commit()

    async def get_all_arxiv_ids(self) -> set[str]:
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("SELECT arxiv_id FROM papers")
            rows = await cursor.fetchall()
            return {row[0] for row in rows}

    async def insert_paper(self, paper: dict):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT OR IGNORE INTO papers
                (arxiv_id, arxiv_id_versioned, title, authors, abstract,
                 arxiv_categories, iaifi_category, published, pdf_url, code_url, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                paper["arxiv_id"], paper.get("arxiv_id_versioned"),
                paper["title"], paper["authors"], paper["abstract"],
                paper["arxiv_categories"], paper["iaifi_category"],
                paper.get("published"), paper.get("pdf_url"),
                paper.get("code_url"), paper.get("status", "discovered"),
            ))
            await db.commit()

    async def update_paper_status(self, arxiv_id: str, status: str, **fields):
        set_clause = ", ".join(f"{k} = ?" for k in fields)
        if set_clause:
            set_clause = ", " + set_clause
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                f"UPDATE papers SET status = ?, updated_at = datetime('now'){set_clause} WHERE arxiv_id = ?",
                (status, *fields.values(), arxiv_id),
            )
            await db.commit()
```

### arXiv Batch Metadata Fetch

```python
# pipeline/fetcher/arxiv_client.py
import arxiv
import re
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class ArxivClient:
    """Wrapper around arxiv.py with IAIFI-specific defaults."""

    def __init__(self, pdf_dir: str = "data/pdfs", delay_seconds: float = 3.0):
        self.client = arxiv.Client(
            page_size=100,          # Results per API page
            delay_seconds=delay_seconds,  # Minimum 3s per arXiv TOS
            num_retries=3,
        )
        self.pdf_dir = Path(pdf_dir)
        self.pdf_dir.mkdir(parents=True, exist_ok=True)

    def fetch_metadata_batch(self, arxiv_ids: list[str]) -> dict[str, arxiv.Result]:
        """Fetch metadata for multiple arXiv IDs. Returns dict keyed by base ID."""
        search = arxiv.Search(id_list=arxiv_ids)
        results = {}
        for result in self.client.results(search):
            base_id = re.sub(r"v\d+$", "", result.get_short_id())
            results[base_id] = result

        # Verify all requested IDs were returned
        missing = set(arxiv_ids) - set(results.keys())
        if missing:
            logger.warning(f"arXiv API did not return results for: {missing}")

        return results

    def download_pdf(self, result: arxiv.Result) -> Path | None:
        """Download PDF, skipping if already cached. Returns path or None on failure."""
        short_id = re.sub(r"v\d+$", "", result.get_short_id()).replace("/", "_")
        filepath = self.pdf_dir / f"{short_id}.pdf"

        if filepath.exists() and filepath.stat().st_size > 0:
            logger.debug(f"PDF already cached: {filepath}")
            return filepath

        try:
            result.download_pdf(dirpath=str(self.pdf_dir), filename=f"{short_id}.pdf")
            if filepath.exists() and filepath.stat().st_size > 0:
                return filepath
            else:
                logger.error(f"PDF download produced empty file: {filepath}")
                filepath.unlink(missing_ok=True)
                return None
        except Exception as e:
            logger.error(f"PDF download failed for {short_id}: {e}")
            filepath.unlink(missing_ok=True)  # Clean up partial downloads
            return None
```

### Minimal Admin HTML

```html
<!-- admin/static/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>IAIFI Blog Admin - Paper Discovery</title>
    <style>
        body { font-family: system-ui; max-width: 900px; margin: 2rem auto; padding: 0 1rem; }
        button { padding: 0.5rem 1rem; font-size: 1rem; cursor: pointer; }
        table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
        th, td { border: 1px solid #ddd; padding: 0.5rem; text-align: left; }
        th { background: #f5f5f5; }
        .status { padding: 0.25rem 0.5rem; border-radius: 4px; font-size: 0.9rem; }
        .running { background: #fff3cd; }
        .complete { background: #d1e7dd; }
        .error { background: #f8d7da; }
    </style>
</head>
<body>
    <h1>IAIFI Paper Discovery</h1>
    <button id="discover-btn" onclick="triggerDiscovery()">Discover New Papers</button>
    <div id="status"></div>
    <h2>Ingested Papers</h2>
    <table id="papers-table">
        <thead><tr><th>arXiv ID</th><th>Title</th><th>Category</th><th>Status</th></tr></thead>
        <tbody id="papers-body"></tbody>
    </table>
    <script>
        async function triggerDiscovery() {
            const btn = document.getElementById('discover-btn');
            btn.disabled = true;
            const resp = await fetch('/api/discover', { method: 'POST' });
            const data = await resp.json();
            pollStatus(data.task_id);
        }
        async function pollStatus(taskId) {
            const statusDiv = document.getElementById('status');
            const poll = setInterval(async () => {
                const resp = await fetch(`/api/discover/${taskId}/status`);
                const data = await resp.json();
                statusDiv.innerHTML = `<span class="status ${data.status}">${data.status}</span>`;
                if (data.status !== 'running') {
                    clearInterval(poll);
                    document.getElementById('discover-btn').disabled = false;
                    if (data.result) {
                        statusDiv.innerHTML += ` Found ${data.result.new_papers} new papers`;
                    }
                    loadPapers();
                }
            }, 2000);
        }
        async function loadPapers() {
            const resp = await fetch('/api/papers');
            const papers = await resp.json();
            const tbody = document.getElementById('papers-body');
            tbody.innerHTML = papers.map(p =>
                `<tr><td><a href="https://arxiv.org/abs/${p.arxiv_id}">${p.arxiv_id}</a></td>
                 <td>${p.title}</td><td>${p.iaifi_category}</td><td>${p.status}</td></tr>`
            ).join('');
        }
        loadPapers();
    </script>
</body>
</html>
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| arxiv.py 1.x (sync only) | arxiv.py 2.4.0 (Client class, built-in rate limiting) | 2024 (v2.0) | Client class manages connection pooling and delays. Old `arxiv.query()` function is removed. |
| sqlite3 + threads for async | aiosqlite 0.22.1 | 2023-2025 | Native async/await for SQLite in FastAPI. No manual thread management. |
| pip + venv | uv | 2024-2025 | 10-100x faster package installation. Replaces pip, venv, pip-tools in one tool. |
| FastAPI with Celery for background tasks | FastAPI BackgroundTasks (built-in) | Always existed | For single-user local apps, Celery is overkill. BackgroundTasks is sufficient. |

**Deprecated/outdated:**
- `arxiv.query()` function: Removed in arxiv.py 2.0. Use `arxiv.Client().results(arxiv.Search(...))` instead.
- `@astrojs/tailwind` integration: Deprecated for Tailwind v4. Not relevant to Phase 1 but noted for later phases.
- `feedparser` for arXiv: Some old tutorials suggest using feedparser to parse arXiv Atom feeds directly. Use arxiv.py instead -- it wraps this properly.

## Open Questions

1. **IAIFI page HTML structure precision**
   - What we know: Pages are static HTML with consistent formatting. Papers have bold/italic titles, author text, arXiv links, category links, and abstracts.
   - What's unclear: The exact DOM structure (nested divs, specific CSS classes) is not fully visible through WebFetch content extraction. The page may use Markdown-to-HTML conversion that produces slightly different element nesting.
   - Recommendation: Build the scraper first, test against the live pages, and adjust selectors. Store raw HTML for each scrape so parsing can be refined iteratively. This is a ~1 hour calibration task, not a research blocker.

2. **Papers on main page vs category pages**
   - What we know: The main papers.html page lists papers AND links to 4 category pages. Some papers appear on both.
   - What's unclear: Whether the main page is a complete superset of all category pages, or a curated subset.
   - Recommendation: Scrape all 4 category pages (not the main page) to get definitive category assignments. Use the main page only as a fallback or for cross-validation. Deduplicate by arxiv ID.

3. **How many total unique papers exist across all IAIFI pages**
   - What we know: Foundational AI has ~70+ papers, Theoretical Physics ~85+, Experimental Physics ~60+, Astrophysics ~50+.
   - What's unclear: Exact unique count after deduplication across categories.
   - Recommendation: Expect ~250-300 unique papers. The initial bulk ingestion will take 12-15 minutes of arXiv API time (at 3 seconds per request). Plan for this in the admin UI.

## Sources

### Primary (HIGH confidence)
- [arxiv.py API documentation](https://lukasschwab.me/arxiv.py/arxiv.html) -- Full Client, Search, Result class API. Version 2.4.0 confirmed.
- [arxiv.py on PyPI](https://pypi.org/project/arxiv/) -- Version 2.4.0, released January 5, 2026. Python >=3.9.
- [arXiv API User's Manual](https://info.arxiv.org/help/api/user-manual.html) -- Endpoint, parameters, rate limits, pagination.
- [arXiv API Terms of Use](https://info.arxiv.org/help/api/tou.html) -- 3-second rate limit requirement.
- [IAIFI Papers page](https://iaifi.org/papers.html) -- Verified structure: 4 category pages, static HTML, arXiv links (fetched 2026-03-03).
- [IAIFI Foundational AI Papers](https://iaifi.org/papers-ai.html) -- ~70+ papers, consistent format (fetched 2026-03-03).
- [IAIFI Theoretical Physics Papers](https://iaifi.org/papers-theory.html) -- ~85+ papers, same format (fetched 2026-03-03).
- [IAIFI Experimental Physics Papers](https://iaifi.org/papers-experiment.html) -- ~60+ papers, same format (fetched 2026-03-03).
- [IAIFI Astrophysics Papers](https://iaifi.org/papers-astro.html) -- ~50+ papers, same format (fetched 2026-03-03).
- [aiosqlite on PyPI](https://pypi.org/project/aiosqlite/) -- Version 0.22.1, released December 23, 2025.
- [beautifulsoup4 on PyPI](https://pypi.org/project/beautifulsoup4/) -- Version 4.14.3, released November 30, 2025.
- [FastAPI BackgroundTasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) -- Official docs for background task pattern.

### Secondary (MEDIUM confidence)
- [arxiv.py GitHub repository](https://github.com/lukasschwab/arxiv.py) -- Client usage patterns, issue tracker.
- [aiosqlite GitHub repository](https://github.com/omnilib/aiosqlite) -- Async SQLite bridge documentation.
- [arXiv Bulk Data Access](https://info.arxiv.org/help/bulk_data.html) -- S3 and OAI-PMH alternatives for large-scale access.
- Project-level research documents (.planning/research/STACK.md, ARCHITECTURE.md, PITFALLS.md) -- Stack decisions, architecture patterns, pitfall catalog.

### Tertiary (LOW confidence)
- IAIFI page exact HTML DOM structure -- WebFetch shows content but not raw HTML tags. Scraper selectors need live testing against actual page source.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- all libraries verified on PyPI with current versions and release dates
- Architecture: HIGH -- patterns derived from project-level architecture research and verified library APIs
- IAIFI scraping: MEDIUM -- page content verified but exact HTML selectors need live testing
- arXiv integration: HIGH -- official API docs + arxiv.py docs fully reviewed
- Pitfalls: HIGH -- derived from verified arXiv rate limits, SQLite concurrency docs, and project-level pitfall research

**Research date:** 2026-03-03
**Valid until:** 2026-04-03 (stable domain -- libraries and IAIFI site unlikely to change within 30 days)
