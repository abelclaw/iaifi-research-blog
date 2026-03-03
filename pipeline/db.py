"""SQLite database layer for paper persistence."""

import json
import logging
from pathlib import Path

import aiosqlite

logger = logging.getLogger(__name__)

SCHEMA = """
CREATE TABLE IF NOT EXISTS papers (
    arxiv_id TEXT PRIMARY KEY,
    arxiv_id_versioned TEXT,
    title TEXT NOT NULL,
    authors TEXT NOT NULL,
    abstract TEXT NOT NULL,
    arxiv_categories TEXT NOT NULL,
    iaifi_category TEXT NOT NULL,
    published TEXT,
    updated TEXT,
    pdf_path TEXT,
    pdf_url TEXT,
    code_url TEXT,
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
    errors TEXT,
    status TEXT NOT NULL DEFAULT 'running'
);

CREATE INDEX IF NOT EXISTS idx_papers_status ON papers(status);
CREATE INDEX IF NOT EXISTS idx_papers_iaifi_category ON papers(iaifi_category);
"""


class Database:
    """Async SQLite database for paper storage and discovery tracking."""

    def __init__(self, db_path: str = "data/papers.db"):
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    async def initialize(self) -> None:
        """Create tables and enable WAL mode."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("PRAGMA journal_mode=WAL")
            await db.executescript(SCHEMA)
            await db.commit()
        logger.info(f"Database initialized at {self.db_path}")

    async def get_all_arxiv_ids(self) -> set[str]:
        """Return all arxiv IDs currently in the database."""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("SELECT arxiv_id FROM papers")
            rows = await cursor.fetchall()
            return {row[0] for row in rows}

    async def insert_paper(self, paper: dict) -> None:
        """Insert a new paper record. Ignores duplicates by arxiv_id."""
        authors_json = json.dumps(paper.get("authors", []))
        categories_json = json.dumps(paper.get("arxiv_categories", []))

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """
                INSERT OR IGNORE INTO papers
                (arxiv_id, arxiv_id_versioned, title, authors, abstract,
                 arxiv_categories, iaifi_category, published, pdf_url,
                 code_url, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    paper["arxiv_id"],
                    paper.get("arxiv_id_versioned"),
                    paper["title"],
                    authors_json,
                    paper.get("abstract", ""),
                    categories_json,
                    paper["iaifi_category"],
                    paper.get("published"),
                    paper.get("pdf_url"),
                    paper.get("code_url"),
                    paper.get("status", "discovered"),
                ),
            )
            await db.commit()

    async def update_paper_status(
        self, arxiv_id: str, status: str, **fields
    ) -> None:
        """Update a paper's status and optional additional fields."""
        set_parts = ["status = ?", "updated_at = datetime('now')"]
        values: list = [status]

        for key, value in fields.items():
            if key in ("authors", "arxiv_categories"):
                value = json.dumps(value)
            set_parts.append(f"{key} = ?")
            values.append(value)

        values.append(arxiv_id)
        set_clause = ", ".join(set_parts)

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                f"UPDATE papers SET {set_clause} WHERE arxiv_id = ?",
                values,
            )
            await db.commit()

    async def get_papers(self, status: str | None = None) -> list[dict]:
        """Retrieve papers, optionally filtered by status."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            if status:
                cursor = await db.execute(
                    "SELECT * FROM papers WHERE status = ? ORDER BY created_at DESC",
                    (status,),
                )
            else:
                cursor = await db.execute(
                    "SELECT * FROM papers ORDER BY created_at DESC"
                )
            rows = await cursor.fetchall()
            papers = []
            for row in rows:
                paper = dict(row)
                paper["authors"] = json.loads(paper["authors"])
                paper["arxiv_categories"] = json.loads(
                    paper["arxiv_categories"]
                )
                papers.append(paper)
            return papers

    async def create_discovery_run(self) -> int:
        """Create a new discovery run record and return its ID."""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                "INSERT INTO discovery_runs (status) VALUES ('running')"
            )
            await db.commit()
            return cursor.lastrowid  # type: ignore[return-value]

    async def update_discovery_run(self, run_id: int, **fields) -> None:
        """Update a discovery run with results."""
        set_parts = []
        values: list = []
        for key, value in fields.items():
            if key == "errors":
                value = json.dumps(value)
            set_parts.append(f"{key} = ?")
            values.append(value)

        if not set_parts:
            return

        values.append(run_id)
        set_clause = ", ".join(set_parts)
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                f"UPDATE discovery_runs SET {set_clause} WHERE id = ?",
                values,
            )
            await db.commit()
