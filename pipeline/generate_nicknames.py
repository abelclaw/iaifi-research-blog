"""Generate 1-2 word nicknames for all papers using Claude CLI.

Usage:
    python -m pipeline.generate_nicknames [--batch-size 20] [--force]
"""

import argparse
import asyncio
import json
import logging
import sqlite3
import sys

from pydantic import BaseModel

from pipeline.config import settings
from pipeline.generator.claude_cli_client import ClaudeCLIClient

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class NicknamesBatch(BaseModel):
    """Response model for a batch of nickname assignments."""
    nicknames: dict[str, str]  # arxiv_id -> nickname


SYSTEM_PROMPT = """\
You are a scientific paper nickname generator. Given a batch of paper titles and \
their first sentence of abstract, produce a memorable 1-2 word nickname for each.

Rules:
- Each nickname must be 1-2 words (max 3 if absolutely necessary)
- Nicknames should capture the paper's core contribution or method
- Use plain English, avoid jargon abbreviations
- Make each nickname distinctive and memorable
- Examples of good nicknames: "Neural ODE", "Jet Tagging", "Dark Photons", \
"Graph Forces", "Lattice QCD", "Higgs Search", "Star Mapper", "Wave Net"
"""


async def generate_nicknames(
    db_path: str = settings.DB_PATH,
    batch_size: int = 20,
    force: bool = False,
) -> int:
    """Generate nicknames for papers that don't have one yet."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    # Ensure nickname column exists
    cols = {row[1] for row in conn.execute("PRAGMA table_info(papers)").fetchall()}
    if "nickname" not in cols:
        conn.execute("ALTER TABLE papers ADD COLUMN nickname TEXT DEFAULT NULL")
        conn.commit()
        logger.info("Added nickname column")

    # Get papers needing nicknames
    if force:
        papers = conn.execute(
            "SELECT arxiv_id, title, abstract FROM papers WHERE concepts_status = 'approved'"
        ).fetchall()
    else:
        papers = conn.execute(
            "SELECT arxiv_id, title, abstract FROM papers "
            "WHERE concepts_status = 'approved' AND (nickname IS NULL OR nickname = '')"
        ).fetchall()

    if not papers:
        logger.info("All papers already have nicknames.")
        conn.close()
        return 0

    logger.info("Generating nicknames for %d papers in batches of %d", len(papers), batch_size)
    client = ClaudeCLIClient(model="haiku")  # Fast + cheap for short nicknames

    total = 0
    for i in range(0, len(papers), batch_size):
        batch = papers[i : i + batch_size]
        logger.info("Batch %d/%d (%d papers)", i // batch_size + 1,
                     (len(papers) + batch_size - 1) // batch_size, len(batch))

        # Build prompt
        lines = []
        for p in batch:
            abstract = (p["abstract"] or "")[:200]  # First ~sentence
            lines.append(f'- {p["arxiv_id"]}: "{p["title"]}" — {abstract}')
        user_prompt = (
            "Generate a 1-2 word nickname for each paper below. "
            "Return a JSON object mapping arxiv_id to nickname.\n\n"
            + "\n".join(lines)
        )

        try:
            result = await client.generate_structured(
                system_prompt=SYSTEM_PROMPT,
                user_prompt=user_prompt,
                response_model=NicknamesBatch,
                max_tokens=2048,
            )

            # Store in DB
            for arxiv_id, nickname in result.nicknames.items():
                nickname = nickname.strip()[:40]  # Safety cap
                conn.execute(
                    "UPDATE papers SET nickname = ? WHERE arxiv_id = ?",
                    (nickname, arxiv_id),
                )
                total += 1

            conn.commit()
            logger.info("  Stored %d nicknames", len(result.nicknames))

        except Exception as e:
            logger.error("  Batch failed: %s", e)
            continue

    conn.close()
    logger.info("Done. Generated %d nicknames total.", total)
    return total


def main():
    parser = argparse.ArgumentParser(description="Generate paper nicknames")
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--force", action="store_true", help="Regenerate all nicknames")
    args = parser.parse_args()

    count = asyncio.run(generate_nicknames(
        batch_size=args.batch_size,
        force=args.force,
    ))
    print(f"Generated {count} nicknames")


if __name__ == "__main__":
    main()
