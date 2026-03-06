"""Fix LLM-generated blog posts: remove AI signatures, fix broken references."""

import logging
import re

from jinja2 import Environment, FileSystemLoader

logger = logging.getLogger(__name__)

FIXER_SYSTEM = (
    "You are an expert editor who removes all traces of AI-generated writing "
    "from blog posts. You fix errors, broken references, and rewrite prose to "
    "sound naturally human-written. You preserve technical accuracy and structure."
)

# Quick regex fixes applied before LLM pass
_QUICK_FIXES = [
    # Broken arXiv references: "arixv:", "arxiv :", etc.
    (re.compile(r"\b[Aa]ri[xX]v\b"), "arXiv"),
    (re.compile(r"\barxiv\s*:\s*", re.IGNORECASE), "arXiv:"),
    # Double spaces
    (re.compile(r"  +"), " "),
    # Trailing whitespace on lines
    (re.compile(r" +\n"), "\n"),
]


class PostFixer:
    """Fixes LLM artifacts in blog posts using a two-step process.

    Step 1: Quick regex fixes for common typos and formatting issues.
    Step 2: LLM pass to rewrite prose, remove AI signatures, verify claims.
    """

    def __init__(
        self,
        llm_client,
        prompts_dir: str = "pipeline/generator/prompts",
    ):
        self.llm = llm_client
        self.env = Environment(
            loader=FileSystemLoader(prompts_dir),
            keep_trailing_newline=True,
        )
        logger.info("PostFixer initialized")

    def quick_fix(self, content: str) -> str:
        """Apply regex-based quick fixes (no LLM needed)."""
        for pattern, replacement in _QUICK_FIXES:
            content = pattern.sub(replacement, content)
        return content

    async def fix_post(
        self,
        content: str,
        title: str,
        arxiv_id: str,
        authors: str,
        abstract: str,
    ) -> str:
        """Fix a blog post: remove LLM signatures, fix references, clean prose.

        Returns the fixed content string.
        """
        cost_before = self.llm.total_cost

        # Step 1: Quick regex fixes
        content = self.quick_fix(content)

        # Step 2: LLM fix pass
        logger.info("Running LLM fix pass for '%s' (%s)", title, arxiv_id)
        fix_template = self.env.get_template("blog_fix.j2")
        fix_prompt = fix_template.render(
            content=content,
            title=title,
            arxiv_id=arxiv_id,
            authors=authors,
            abstract=abstract,
        )

        fixed = await self.llm.generate(
            system_prompt=FIXER_SYSTEM,
            user_prompt=fix_prompt,
        )

        # Validate the output preserved required structure
        required_sections = [
            "## The Big Picture",
            "## How It Works",
            "## Why It Matters",
            "## IAIFI Research Highlights",
        ]
        missing = [s for s in required_sections if s not in fixed]
        if missing:
            logger.warning(
                "Fixer output missing sections for %s: %s — using original",
                arxiv_id, missing,
            )
            # Fall back to just the quick-fixed version
            return content

        # Validate figure references weren't lost
        original_figs = set(re.findall(r"!\[.*?\]\(figure:\d+\)", content))
        fixed_figs = set(re.findall(r"!\[.*?\]\(figure:\d+\)", fixed))
        if original_figs and not fixed_figs:
            logger.warning(
                "Fixer output lost all figure references for %s — using original",
                arxiv_id,
            )
            return content

        cost = self.llm.total_cost - cost_before
        word_count = len(fixed.split())
        logger.info(
            "Fix complete for '%s': %d words, cost=$%.4f",
            title, word_count, cost,
        )

        return fixed
