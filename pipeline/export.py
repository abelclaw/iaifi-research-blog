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
import re
import shutil
import sqlite3
from pathlib import Path

import yaml

from pipeline.config import settings

logger = logging.getLogger(__name__)

# Highlight categories → logo SVG paths and accent colors
_HIGHLIGHT_CONFIG = [
    {
        "key": "Interdisciplinary Research Achievement",
        "icon": "/images/logo-fi-black.svg",
        "color": "#1a1a1a",
        "bg": "#f5f5f5",
        "border": "#d4d4d4",
    },
    {
        "key": "Impact on Artificial Intelligence",
        "icon": "/images/logo-ai-blue.svg",
        "color": "#2c5f8a",
        "bg": "#eff6ff",
        "border": "#bfdbfe",
    },
    {
        "key": "Impact on Fundamental Interactions",
        "icon": "/images/logo-fi-purple.svg",
        "color": "#7b2d8e",
        "bg": "#faf5ff",
        "border": "#e9d5ff",
    },
    {
        "key": "Outlook and References",
        "icon": "",
        "color": "#059669",
        "bg": "#ecfdf5",
        "border": "#a7f3d0",
    },
]


def _transform_highlights(content: str, base_path: str) -> str:
    """Replace the IAIFI Research Highlights markdown section with styled HTML cards."""
    marker = "## IAIFI Research Highlights"
    idx = content.find(marker)
    if idx == -1:
        return content

    before = content[:idx]
    highlights_text = content[idx + len(marker):]

    # Parse bullet items: "- **Label:** text"
    items = re.findall(
        r"-\s+\*\*([^*]+?):\*\*\s*(.+?)(?=\n-\s+\*\*|\Z)",
        highlights_text,
        re.DOTALL,
    )

    if not items:
        return content

    # Build HTML cards
    cards_html = []
    cards_html.append(
        '<div style="margin-top:2rem;">'
        '<h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">'
        'IAIFI Research Highlights</h2>'
    )

    for label, text in items:
        label = label.strip()
        text = text.strip()

        # Find matching config
        cfg = next((c for c in _HIGHLIGHT_CONFIG if c["key"] == label), None)
        if not cfg:
            cfg = {"icon": "", "color": "#374151", "bg": "#f9fafb", "border": "#e5e7eb"}

        icon_html = ""
        if cfg["icon"]:
            icon_src = f'{base_path}{cfg["icon"]}' if base_path else cfg["icon"]
            icon_html = (
                f'<img src="{icon_src}" alt="" '
                f'style="width:32px;height:32px;flex-shrink:0;" />'
            )

        cards_html.append(
            f'<div style="display:flex;gap:0.75rem;align-items:flex-start;'
            f'padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;'
            f'background:{cfg["bg"]};border:1px solid {cfg["border"]};">'
            f'{icon_html}'
            f'<div>'
            f'<strong style="color:{cfg["color"]};">{label}</strong><br/>'
            f'<span style="color:#374151;">{text}</span>'
            f'</div>'
            f'</div>'
        )

    cards_html.append('</div>')

    return before + "\n".join(cards_html) + "\n"


def _read_astro_base(site_dir: str) -> str:
    """Read the base path from astro.config.mjs."""
    config_path = Path(site_dir) / "astro.config.mjs"
    if config_path.exists():
        match = re.search(r'base:\s*["\']([^"\']+)["\']', config_path.read_text())
        if match:
            return match.group(1).rstrip("/")
    return ""


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
    base_path = _read_astro_base(site_dir)  # e.g. "/iaifi-research-blog"

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

            # Copy figure files to site/public/figures/<arxiv_subdir>/
            arxiv_subdir = arxiv_id.replace(".", "_")
            paper_fig_dest = figures_dest / arxiv_subdir
            paper_fig_dest.mkdir(parents=True, exist_ok=True)

            figure_urls = []
            for fig in figures:
                fig_path = Path(fig["figure_path"])
                if fig_path.exists():
                    dest = paper_fig_dest / fig_path.name
                    shutil.copy2(str(fig_path), str(dest))
                    figure_urls.append(f"{base_path}/figures/{arxiv_subdir}/{fig_path.name}")
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

            # Resolve figure:N placeholders to actual image paths
            content = post["content"]
            def _resolve_figure_ref(match):
                alt = match.group(1)
                num = int(match.group(2))
                idx = num - 1  # figure:N is 1-indexed
                if 0 <= idx < len(figure_urls):
                    return f"![{alt}]({figure_urls[idx]})"
                return match.group(0)  # leave unresolved if out of range

            content = re.sub(
                r"!\[([^\]]*)\]\(figure:(\d+)\)", _resolve_figure_ref, content
            )

            # Transform IAIFI Research Highlights into styled HTML cards
            content = _transform_highlights(content, base_path)

            # Write markdown file
            slug = post["slug"]
            output_path = posts_dir / f"{slug}.md"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write("---\n")
                f.write(yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True))
                f.write("---\n\n")
                f.write(content)

            count += 1
            logger.info(f"Exported: {slug} ({arxiv_id})")

        return count

    finally:
        conn.close()


def _load_iaifi_members(site_dir: str) -> dict[str, str]:
    """Load IAIFI member -> institution mapping from iaifi-members.json."""
    members_path = Path(site_dir) / "scripts" / "iaifi-members.json"
    if members_path.exists():
        with open(members_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def _get_primary_institution(authors: list[str], member_map: dict[str, str]) -> str | None:
    """Determine primary institution for a paper from its authors."""
    inst_count: dict[str, int] = {}
    for a in authors:
        inst = member_map.get(a)
        if inst:
            inst_count[inst] = inst_count.get(inst, 0) + 1
    if not inst_count:
        return None
    return max(inst_count, key=inst_count.get)  # type: ignore[arg-type]


def export_approved_concepts(db_path: str, site_dir: str) -> int:
    """Export approved concepts to a unified metadata JSON file.

    Writes site/src/data/concepts.json with all papers that have approved
    concepts, including: abstract, nickname, institution, arXiv/PDF URLs.

    Returns:
        Number of papers exported.
    """
    data_dir = Path(site_dir) / "src" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    member_map = _load_iaifi_members(site_dir)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    try:
        # Get all papers with approved concepts
        cursor = conn.execute(
            """SELECT p.arxiv_id, p.title, p.iaifi_category, p.published,
                      p.authors, p.abstract, p.nickname
               FROM papers p
               WHERE p.concepts_status = 'approved'
               ORDER BY p.published DESC"""
        )
        papers = cursor.fetchall()

        entries = []
        for paper in papers:
            arxiv_id = paper["arxiv_id"]
            concept_cursor = conn.execute(
                "SELECT name, description, relevance FROM concepts "
                "WHERE paper_arxiv_id = ? ORDER BY relevance DESC",
                (arxiv_id,),
            )
            concepts = [
                {"name": c["name"], "description": c["description"], "relevance": c["relevance"]}
                for c in concept_cursor.fetchall()
            ]

            # Check if this paper has an exported blog post
            slug_cursor = conn.execute(
                "SELECT slug FROM blog_posts WHERE paper_arxiv_id = ? AND status = 'approved'",
                (arxiv_id,),
            )
            slug_row = slug_cursor.fetchone()

            # Parse authors JSON
            authors_raw = paper["authors"] or "[]"
            try:
                authors = json.loads(authors_raw) if isinstance(authors_raw, str) else authors_raw
            except (json.JSONDecodeError, TypeError):
                authors = []
            if not isinstance(authors, list):
                authors = []

            institution = _get_primary_institution(authors, member_map)

            entries.append({
                "arxivId": arxiv_id,
                "title": paper["title"],
                "nickname": paper["nickname"] or None,
                "theme": paper["iaifi_category"],
                "published": paper["published"] or "",
                "authors": authors,
                "institution": institution,
                "abstract": paper["abstract"] or "",
                "concepts": [c["name"] for c in concepts],
                "conceptDetails": concepts,
                "arxivUrl": f"https://arxiv.org/abs/{arxiv_id}",
                "pdfUrl": f"https://arxiv.org/pdf/{arxiv_id}",
                "blogSlug": slug_row["slug"] if slug_row else None,
            })

        output_path = data_dir / "concepts.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(entries, f, indent=2, ensure_ascii=False)

        logger.info("Exported %d papers with approved concepts to %s", len(entries), output_path)
        return len(entries)

    finally:
        conn.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    db_path = settings.DB_PATH
    site_dir = "site"
    count = export_approved_posts(db_path, site_dir)
    print(f"Exported {count} approved posts to {site_dir}/src/content/posts/")
    concept_count = export_approved_concepts(db_path, site_dir)
    print(f"Exported {concept_count} papers with approved concepts")
