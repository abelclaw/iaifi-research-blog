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

CREATE TABLE IF NOT EXISTS blog_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_arxiv_id TEXT NOT NULL REFERENCES papers(arxiv_id),
    title TEXT NOT NULL,
    slug TEXT NOT NULL UNIQUE,
    content TEXT NOT NULL,
    word_count INTEGER NOT NULL,
    llm_model TEXT NOT NULL,
    generation_cost REAL DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'draft',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS figures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_arxiv_id TEXT NOT NULL REFERENCES papers(arxiv_id),
    figure_path TEXT NOT NULL,
    page_number INTEGER NOT NULL,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL,
    extraction_type TEXT NOT NULL,
    sort_order INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS concepts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_arxiv_id TEXT NOT NULL REFERENCES papers(arxiv_id),
    name TEXT NOT NULL,
    description TEXT,
    relevance REAL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_papers_status ON papers(status);
CREATE INDEX IF NOT EXISTS idx_papers_iaifi_category ON papers(iaifi_category);
CREATE INDEX IF NOT EXISTS idx_blog_posts_paper ON blog_posts(paper_arxiv_id);
CREATE INDEX IF NOT EXISTS idx_blog_posts_status ON blog_posts(status);
CREATE INDEX IF NOT EXISTS idx_figures_paper ON figures(paper_arxiv_id);
CREATE INDEX IF NOT EXISTS idx_concepts_paper ON concepts(paper_arxiv_id);
CREATE INDEX IF NOT EXISTS idx_concepts_name ON concepts(name);
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

    async def insert_blog_post(self, post: dict) -> int:
        """Insert a new blog post and return its ID."""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                """
                INSERT INTO blog_posts
                (paper_arxiv_id, title, slug, content, word_count,
                 llm_model, generation_cost, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    post["paper_arxiv_id"],
                    post["title"],
                    post["slug"],
                    post["content"],
                    post["word_count"],
                    post["llm_model"],
                    post.get("generation_cost", 0),
                    post.get("status", "draft"),
                ),
            )
            await db.commit()
            return cursor.lastrowid  # type: ignore[return-value]

    async def insert_figure(self, figure: dict) -> int:
        """Insert a figure record and return its ID."""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                """
                INSERT INTO figures
                (paper_arxiv_id, figure_path, page_number, width, height,
                 extraction_type, sort_order)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    figure["paper_arxiv_id"],
                    figure["figure_path"],
                    figure["page_number"],
                    figure["width"],
                    figure["height"],
                    figure["extraction_type"],
                    figure.get("sort_order", 0),
                ),
            )
            await db.commit()
            return cursor.lastrowid  # type: ignore[return-value]

    async def insert_concepts(
        self, arxiv_id: str, concepts: list[dict]
    ) -> None:
        """Insert multiple concept records for a paper."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.executemany(
                """
                INSERT INTO concepts
                (paper_arxiv_id, name, description, relevance)
                VALUES (?, ?, ?, ?)
                """,
                [
                    (
                        arxiv_id,
                        c["name"],
                        c.get("description", ""),
                        c.get("relevance", 0),
                    )
                    for c in concepts
                ],
            )
            await db.commit()

    async def get_blog_posts(self, status: str | None = None) -> list[dict]:
        """Retrieve all blog posts, optionally filtered by status.

        Joins with papers table to include paper title and iaifi_category.
        Ordered by created_at DESC.
        """
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            if status:
                cursor = await db.execute(
                    """SELECT bp.*, p.title as paper_title, p.iaifi_category
                       FROM blog_posts bp
                       LEFT JOIN papers p ON bp.paper_arxiv_id = p.arxiv_id
                       WHERE bp.status = ?
                       ORDER BY bp.created_at DESC""",
                    (status,),
                )
            else:
                cursor = await db.execute(
                    """SELECT bp.*, p.title as paper_title, p.iaifi_category
                       FROM blog_posts bp
                       LEFT JOIN papers p ON bp.paper_arxiv_id = p.arxiv_id
                       ORDER BY bp.created_at DESC"""
                )
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]

    async def update_blog_post_content(
        self, arxiv_id: str, content: str
    ) -> None:
        """Update blog post content and recalculate word count.

        Recalculates word_count server-side to prevent drift.
        """
        word_count = len(content.split())
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """UPDATE blog_posts
                   SET content = ?, word_count = ?, updated_at = datetime('now')
                   WHERE paper_arxiv_id = ?""",
                (content, word_count, arxiv_id),
            )
            await db.commit()

    async def update_blog_post_status(
        self, arxiv_id: str, status: str
    ) -> None:
        """Update blog post status (draft/approved/rejected)."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """UPDATE blog_posts
                   SET status = ?, updated_at = datetime('now')
                   WHERE paper_arxiv_id = ?""",
                (status, arxiv_id),
            )
            await db.commit()

    async def get_blog_post(self, arxiv_id: str) -> dict | None:
        """Retrieve a blog post by paper arxiv_id."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                "SELECT * FROM blog_posts WHERE paper_arxiv_id = ?",
                (arxiv_id,),
            )
            row = await cursor.fetchone()
            return dict(row) if row else None

    async def get_figures(self, arxiv_id: str) -> list[dict]:
        """Retrieve all figures for a paper, ordered by sort_order."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                "SELECT * FROM figures WHERE paper_arxiv_id = ? ORDER BY sort_order",
                (arxiv_id,),
            )
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]

    async def get_concepts(self, arxiv_id: str) -> list[dict]:
        """Retrieve all concepts for a paper, ordered by relevance."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                "SELECT * FROM concepts WHERE paper_arxiv_id = ? ORDER BY relevance DESC",
                (arxiv_id,),
            )
            rows = await cursor.fetchall()
            return [dict(row) for row in rows]
