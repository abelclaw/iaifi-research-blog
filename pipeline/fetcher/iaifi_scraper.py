"""IAIFI website scraper for paper listings.

Scrapes all 4 IAIFI category pages (Foundational AI, Theoretical Physics,
Experimental Physics, Astrophysics) and extracts paper entries with arXiv IDs,
titles, authors, abstracts, and code URLs.
"""

import logging
import re

import requests
from bs4 import BeautifulSoup

from pipeline.config import settings
from pipeline.models import ScrapedPaper

logger = logging.getLogger(__name__)

ARXIV_LINK_RE = re.compile(r"https://arxiv\.org/abs/(\d{4}\.\d{4,5}(?:v\d+)?)")


def scrape_category_page(url: str, category: str) -> list[ScrapedPaper]:
    """Scrape a single IAIFI category page for paper entries.

    Each paper entry follows this HTML pattern:
        <p>
          <strong><em>Title</em></strong> <br/>
          Author1, Author2 <br/>
          [ <a href="arxiv.org/abs/ID">arXiv:ID</a> | <a href="...">code</a> ]
        </p>
        <div><details><summary>Abstract</summary><em>text</em></details></div>

    Args:
        url: URL of the IAIFI category page.
        category: Category name (e.g., "Foundational AI").

    Returns:
        List of ScrapedPaper objects extracted from the page.
    """
    logger.info(f"Scraping {category} page: {url}")

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    papers: list[ScrapedPaper] = []

    arxiv_links = soup.find_all("a", href=ARXIV_LINK_RE)
    logger.info(f"Found {len(arxiv_links)} arXiv links on {category} page")

    seen_ids: set[str] = set()

    for link in arxiv_links:
        href = link.get("href", "")
        id_match = ARXIV_LINK_RE.search(href)
        if not id_match:
            continue

        arxiv_id = id_match.group(1)
        # Normalize: strip version suffix
        base_id = re.sub(r"v\d+$", "", arxiv_id)

        # Skip duplicates within the same page
        if base_id in seen_ids:
            continue
        seen_ids.add(base_id)

        # Find the containing <p> tag
        p_tag = link.find_parent("p")
        if not p_tag:
            logger.warning(
                f"arXiv link for {base_id} has no parent <p> tag, skipping"
            )
            continue

        # Extract title from <strong><em>
        title = _extract_title(p_tag, base_id)

        # Extract authors from text between title and bracket section
        authors = _extract_authors(p_tag, base_id)

        # Extract code URL from sibling links
        code_url = _extract_code_url(p_tag)

        # Extract abstract from the next sibling <div> with <details>
        abstract = _extract_abstract(p_tag)

        paper = ScrapedPaper(
            arxiv_id=base_id,
            title=title,
            authors=authors,
            abstract=abstract,
            category=category,
            code_url=code_url,
            source_url=url,
        )
        papers.append(paper)

    logger.info(f"Scraped {len(papers)} unique papers from {category} page")
    return papers


def scrape_all_papers() -> list[ScrapedPaper]:
    """Scrape all 4 IAIFI category pages and return deduplicated paper list.

    Papers are deduplicated by arXiv ID. The first category encountered wins
    for category assignment.

    Returns:
        Deduplicated list of ScrapedPaper objects from all categories.
    """
    all_papers: dict[str, ScrapedPaper] = {}

    for category, url in settings.CATEGORY_PAGES.items():
        try:
            papers = scrape_category_page(url, category)
            if len(papers) == 0:
                logger.warning(
                    f"Category '{category}' returned 0 papers -- "
                    "scraper may be broken or page structure changed"
                )
            for paper in papers:
                if paper.arxiv_id not in all_papers:
                    all_papers[paper.arxiv_id] = paper
        except Exception:
            logger.exception(f"Failed to scrape category '{category}' at {url}")

    total = len(all_papers)
    logger.info(f"Scraped {total} unique papers across all categories")
    return list(all_papers.values())


def _extract_title(p_tag, arxiv_id: str) -> str:
    """Extract paper title from the <strong><em> element in the <p> tag."""
    strong = p_tag.find("strong")
    if strong:
        em = strong.find("em")
        if em:
            return em.get_text(strip=True)
        return strong.get_text(strip=True)

    # Fallback: use first line of text
    text_lines = [
        line.strip()
        for line in p_tag.get_text().split("\n")
        if line.strip()
    ]
    if text_lines:
        logger.warning(
            f"No <strong><em> found for {arxiv_id}, using first text line"
        )
        return text_lines[0]

    logger.warning(f"Could not extract title for {arxiv_id}")
    return f"Untitled ({arxiv_id})"


def _extract_authors(p_tag, arxiv_id: str) -> list[str]:
    """Extract author names from text between title and bracket section."""
    text = p_tag.get_text()
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    # Expected structure: [Title, Authors, [arXiv:ID | code]]
    # Authors are on the second line
    if len(lines) >= 2:
        author_line = lines[1]
        # Clean up: remove any bracket artifacts
        if author_line.startswith("["):
            logger.warning(f"Author line looks like links for {arxiv_id}")
            return []
        # Split by comma, strip whitespace
        authors = [a.strip() for a in author_line.split(",") if a.strip()]
        return authors

    logger.warning(f"Could not extract authors for {arxiv_id}")
    return []


def _extract_code_url(p_tag) -> str | None:
    """Extract code URL (GitHub link) from the <p> tag."""
    all_links = p_tag.find_all("a")
    for a in all_links:
        href = a.get("href", "")
        # Check for code link by text or GitHub URL
        link_text = a.get_text(strip=True).lower()
        if link_text == "code" or (
            "github.com" in href and "arxiv" not in href
        ):
            return href
    return None


def _extract_abstract(p_tag) -> str | None:
    """Extract abstract from the <details> element following the <p> tag."""
    # The abstract is in a <div> sibling right after the <p> tag
    next_sib = p_tag.find_next_sibling()
    if not next_sib:
        return None

    # Look for <details> containing the abstract
    details = next_sib.find("details") if next_sib else None
    if not details:
        return None

    # Abstract text is in <em> inside the details
    em = details.find("em")
    if em:
        return em.get_text(strip=True)

    # Fallback: get all text after the <summary> tag
    summary = details.find("summary")
    if summary:
        # Remove the summary text and get the rest
        full_text = details.get_text(strip=True)
        summary_text = summary.get_text(strip=True)
        if full_text.startswith(summary_text):
            return full_text[len(summary_text):].strip()

    return details.get_text(strip=True)
