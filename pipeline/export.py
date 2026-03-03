"""Export approved blog posts from SQLite to Astro content files.

This is a synchronous build-time script that bridges the Python pipeline
(Phases 1-3) with the Astro static site generator (Phase 4). It reads
approved blog posts from the database and writes markdown files with
YAML frontmatter to the Astro content directory.

Usage:
    python -m pipeline.export
"""

import glob
import json
import logging
import os
import shutil
import sqlite3
from pathlib import Path

import yaml

from pipeline.config import settings

logger = logging.getLogger(__name__)


def export_approved_posts(db_path: str, site_dir: str) -> int:
    """Export all approved blog posts to Astro content markdown files.

    Args:
        db_path: Path to the SQLite database file.
        site_dir: Path to the Astro site directory (e.g., "site").

    Returns:
        Number of posts exported.
    """
    posts_dir = Path(site_dir) / "src" / "content" / "posts"
    figures_dest = Path(site_dir) / "public" / "figures"

    # Create output directories
    posts_dir.mkdir(parents=True, exist_ok=True)
    figures_dest.mkdir(parents=True, exist_ok=True)

    # Clear existing markdown files to prevent stale content
    for md_file in glob.glob(str(posts_dir / "*.md")):
        os.remove(md_file)
        logger.debug(f"Removed stale file: {md_file}")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    try:
        # Check that required tables exist (they may not if pipeline
        # hasn't been run yet)
        tables = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
        }
        required = {"blog_posts", "papers", "concepts", "figures"}
        if not required.issubset(tables):
            missing = required - tables
            logger.info(
                f"Required tables not yet created: {missing}. "
                "Run the pipeline first. Exporting 0 posts."
            )
            return 0

        # Query all approved blog posts joined with paper metadata
        cursor = conn.execute(
            """
            SELECT bp.*, p.authors, p.abstract, p.iaifi_category,
                   p.published, p.arxiv_id, p.pdf_url
            FROM blog_posts bp
            JOIN papers p ON bp.paper_arxiv_id = p.arxiv_id
            WHERE bp.status = 'approved'
            ORDER BY p.published DESC
            """
        )
        posts = cursor.fetchall()

        count = 0
        for post in posts:
            arxiv_id = post["arxiv_id"]

            # Query concepts for this paper
            concept_cursor = conn.execute(
                "SELECT name, description, relevance FROM concepts "
                "WHERE paper_arxiv_id = ? ORDER BY relevance DESC",
                (arxiv_id,),
            )
            concepts = concept_cursor.fetchall()

            # Query figures for this paper
            figure_cursor = conn.execute(
                "SELECT figure_path FROM figures "
                "WHERE paper_arxiv_id = ? ORDER BY sort_order",
                (arxiv_id,),
            )
            figures = figure_cursor.fetchall()

            # Copy figure files to site/public/figures/
            figure_urls = []
            for fig in figures:
                fig_path = Path(fig["figure_path"])
                if fig_path.exists():
                    dest = figures_dest / fig_path.name
                    shutil.copy2(str(fig_path), str(dest))
                    figure_urls.append(f"/figures/{fig_path.name}")
                    logger.debug(f"Copied figure: {fig_path} -> {dest}")
                else:
                    logger.warning(f"Figure not found: {fig_path}")

            # Parse authors from JSON string
            try:
                authors = json.loads(post["authors"])
            except (json.JSONDecodeError, TypeError):
                authors = []
                logger.warning(
                    f"Could not parse authors for {arxiv_id}"
                )

            # Build frontmatter
            pdf_url = post["pdf_url"] or f"https://arxiv.org/pdf/{arxiv_id}"
            frontmatter = {
                "title": post["title"],
                "arxivId": arxiv_id,
                "authors": authors,
                "abstract": post["abstract"] or "",
                "theme": post["iaifi_category"],
                "published": post["published"] or "",
                "arxivUrl": f"https://arxiv.org/abs/{arxiv_id}",
                "pdfUrl": pdf_url,
                "concepts": [c["name"] for c in concepts],
                "figures": figure_urls,
                "wordCount": post["word_count"],
            }

            # Write markdown file
            slug = post["slug"]
            output_path = posts_dir / f"{slug}.md"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write("---\n")
                f.write(yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True))
                f.write("---\n\n")
                f.write(post["content"])

            count += 1
            logger.info(f"Exported: {slug} ({arxiv_id})")

        return count

    finally:
        conn.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    db_path = settings.DB_PATH
    site_dir = "site"
    count = export_approved_posts(db_path, site_dir)
    print(f"Exported {count} approved posts to {site_dir}/src/content/posts/")
