"""SQLite database layer for paper persistence."""

import json
import logging
from datetime import datetime
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
        """Create tables, enable WAL mode, and run migrations."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("PRAGMA journal_mode=WAL")
            await db.executescript(SCHEMA)
            # Migration: add concepts_status column if missing
            cursor = await db.execute("PRAGMA table_info(papers)")
            columns = {row[1] for row in await cursor.fetchall()}
            if "concepts_status" not in columns:
                await db.execute(
                    "ALTER TABLE papers ADD COLUMN concepts_status TEXT DEFAULT NULL"
                )
                logger.info("Migrated: added concepts_status column to papers")
            if "nickname" not in columns:
                await db.execute(
                    "ALTER TABLE papers ADD COLUMN nickname TEXT DEFAULT NULL"
                )
                logger.info("Migrated: added nickname column to papers")
            # Migration: add fix_count column to blog_posts if missing
            bp_cursor = await db.execute("PRAGMA table_info(blog_posts)")
            bp_columns = {row[1] for row in await bp_cursor.fetchall()}
            if "fix_count" not in bp_columns:
                await db.execute(
                    "ALTER TABLE blog_posts ADD COLUMN fix_count INTEGER DEFAULT 0"
                )
                logger.info("Migrated: added fix_count column to blog_posts")
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
            now = datetime.utcnow().isoformat()
            cursor = await db.execute(
                """
                INSERT INTO blog_posts
                (paper_arxiv_id, title, slug, content, word_count,
                 llm_model, generation_cost, status, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                    now,
                    now,
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
                 extraction_type, sort_order, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    figure["paper_arxiv_id"],
                    figure["figure_path"],
                    figure["page_number"],
                    figure["width"],
                    figure["height"],
                    figure["extraction_type"],
                    figure.get("sort_order", 0),
                    figure.get("created_at", datetime.utcnow().isoformat()),
                ),
            )
            await db.commit()
            return cursor.lastrowid  # type: ignore[return-value]

    async def insert_concepts(
        self, arxiv_id: str, concepts: list[dict]
    ) -> None:
        """Insert multiple concept records for a paper."""
        async with aiosqlite.connect(self.db_path) as db:
            now = datetime.utcnow().isoformat()
            await db.executemany(
                """
                INSERT INTO concepts
                (paper_arxiv_id, name, description, relevance, created_at)
                VALUES (?, ?, ?, ?, ?)
                """,
                [
                    (
                        arxiv_id,
                        c["name"],
                        c.get("description", ""),
                        c.get("relevance", 0),
                        now,
                    )
                    for c in concepts
                ],
            )
            await db.commit()

    async def delete_concepts(self, arxiv_id: str) -> None:
        """Delete all concepts for a paper (for re-extraction)."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                "DELETE FROM concepts WHERE paper_arxiv_id = ?", (arxiv_id,)
            )
            await db.commit()

    async def set_concepts_status(self, arxiv_id: str, status: str) -> None:
        """Set the concepts review status for a paper."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                "UPDATE papers SET concepts_status = ? WHERE arxiv_id = ?",
                (status, arxiv_id),
            )
            await db.commit()

    async def get_papers_with_concepts(
        self, concepts_status: str | None = None
    ) -> list[dict]:
        """Get papers that have concepts, with paper info and concept count.

        Args:
            concepts_status: Filter by concepts_status (pending/approved/rejected).
        """
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            if concepts_status:
                cursor = await db.execute(
                    """SELECT p.arxiv_id, p.title, p.iaifi_category,
                              p.concepts_status, COUNT(c.id) as concept_count
                       FROM papers p
                       JOIN concepts c ON c.paper_arxiv_id = p.arxiv_id
                       WHERE p.concepts_status = ?
                       GROUP BY p.arxiv_id
                       ORDER BY c.created_at DESC""",
                    (concepts_status,),
                )
            else:
                cursor = await db.execute(
                    """SELECT p.arxiv_id, p.title, p.iaifi_category,
                              p.concepts_status, COUNT(c.id) as concept_count
                       FROM papers p
                       JOIN concepts c ON c.paper_arxiv_id = p.arxiv_id
                       GROUP BY p.arxiv_id
                       ORDER BY c.created_at DESC""",
                )
            return [dict(row) for row in await cursor.fetchall()]

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

    async def get_fix_count(self, arxiv_id: str) -> int | None:
        """Get the current fix_count for a blog post."""
        async with aiosqlite.connect(self.db_path) as db:
            cur = await db.execute(
                "SELECT fix_count FROM blog_posts WHERE paper_arxiv_id = ?",
                (arxiv_id,),
            )
            row = await cur.fetchone()
            return row[0] if row else None

    async def increment_fix_count(self, arxiv_id: str) -> None:
        """Increment the fix_count for a blog post."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                """UPDATE blog_posts
                   SET fix_count = COALESCE(fix_count, 0) + 1,
                       updated_at = datetime('now')
                   WHERE paper_arxiv_id = ?""",
                (arxiv_id,),
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
        """Retrieve a blog post by paper arxiv_id with paper metadata."""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            cursor = await db.execute(
                """SELECT bp.*, p.title as paper_title, p.authors as paper_authors,
                          p.iaifi_category
                   FROM blog_posts bp
                   LEFT JOIN papers p ON bp.paper_arxiv_id = p.arxiv_id
                   WHERE bp.paper_arxiv_id = ?""",
                (arxiv_id,),
            )
            row = await cursor.fetchone()
            if not row:
                return None
            result = dict(row)
            # Authors are stored as JSON array in papers table
            if result.get("paper_authors"):
                try:
                    result["paper_authors"] = json.loads(result["paper_authors"])
                except (json.JSONDecodeError, TypeError):
                    pass
            return result

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
