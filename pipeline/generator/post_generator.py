"""Multi-pass blog post generation from academic papers."""

import logging
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from pipeline.extractor.pdf_reader import extract_paper_text
from pipeline.models import BlogPost, Paper

logger = logging.getLogger(__name__)

# System prompts for each generation pass
JOURNALIST_SYSTEM = (
    "You are a science journalist who writes engaging, accurate articles about "
    "cutting-edge research at the intersection of AI and fundamental physics. "
    "You write for a broad audience, starting accessible and building to "
    "technical depth."
)

READER_SYSTEM = (
    "You are an educated general reader -- curious about science but not a "
    "specialist. You flag jargon, confusing passages, and assumptions of "
    "background knowledge. When you revise, you make the opening accessible "
    "while preserving technical accuracy in later sections."
)

EDITOR_SYSTEM = (
    "You are a senior science editor at a major publication. You ensure "
    "structural consistency, appropriate length, smooth flow between sections, "
    "and proper use of section headers. You return only the final polished text."
)


def _generate_slug(title: str, arxiv_id: str) -> str:
    """Generate a URL-safe slug from a paper title and arxiv ID.

    Lowercase, replace non-alphanumeric with hyphens, collapse
    multiple hyphens, strip leading/trailing hyphens, truncate to 80 chars.
    Appends arxiv ID to guarantee uniqueness.
    """
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")
    aid = arxiv_id.replace(".", "-")
    slug = slug[:80]
    return f"{slug}-{aid}"


class PostGenerator:
    """Orchestrates three-pass blog post generation from academic papers.

    The three passes follow a journalist-reader-editor refinement chain:
    1. Journalist: Drafts an initial blog post from paper content
    2. Reader: Simplifies for accessibility while preserving depth
    3. Editor: Polishes structure, prose, and enforces word count
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
        logger.info("PostGenerator initialized with prompts from %s", prompts_dir)

    async def generate_post(
        self, paper: Paper, pdf_path: str, figures: list[dict] | None = None,
    ) -> BlogPost:
        """Generate a blog post from a paper through three LLM passes.

        Args:
            paper: Paper model with metadata (title, authors, abstract, etc.).
            pdf_path: Path to the paper's PDF file.
            figures: List of extracted figure dicts with 'path' keys.

        Returns:
            BlogPost model with generated content, word count, and cost.
        """
        figures = figures or []

        # Reset cost tracking for this generation
        cost_before = self.llm.total_cost

        # Extract paper text from PDF
        logger.info("Extracting paper text from %s", pdf_path)
        paper_content = extract_paper_text(pdf_path, max_chars=10000)
        logger.info("Extracted %d chars from PDF", len(paper_content))

        # Pass 1: Journalist drafts from paper content
        logger.info("Pass 1/3: Journalist drafting blog post for '%s'", paper.title)
        draft_template = self.env.get_template("blog_draft.j2")
        draft_prompt = draft_template.render(
            title=paper.title,
            authors=paper.authors,
            abstract=paper.abstract,
            paper_content=paper_content,
            iaifi_category=paper.iaifi_category,
            num_figures=len(figures),
        )
        pass1_output = await self.llm.generate(
            system_prompt=JOURNALIST_SYSTEM,
            user_prompt=draft_prompt,
        )
        pass1_words = len(pass1_output.split())
        logger.info("Pass 1 complete: %d words", pass1_words)

        # Pass 2: Reader simplifies for accessibility
        logger.info("Pass 2/3: Reader simplifying for accessibility")
        simplify_template = self.env.get_template("blog_simplify.j2")
        simplify_prompt = simplify_template.render(draft=pass1_output)
        pass2_output = await self.llm.generate(
            system_prompt=READER_SYSTEM,
            user_prompt=simplify_prompt,
        )
        pass2_words = len(pass2_output.split())
        logger.info("Pass 2 complete: %d words", pass2_words)

        # Pass 3: Editor polishes structure and word count
        logger.info("Pass 3/3: Editor polishing and enforcing word count")
        polish_template = self.env.get_template("blog_polish.j2")
        polish_prompt = polish_template.render(
            draft=pass2_output,
            target_min=800,
            target_max=1500,
        )
        pass3_output = await self.llm.generate(
            system_prompt=EDITOR_SYSTEM,
            user_prompt=polish_prompt,
        )
        final_content = pass3_output

        # Validate word count
        word_count = len(final_content.split())
        logger.info("Final word count: %d", word_count)
        if word_count < 700 or word_count > 1600:
            logger.warning(
                "Word count %d outside tolerance range (700-1600) for '%s'",
                word_count,
                paper.title,
            )

        # Generate slug from paper title
        slug = _generate_slug(paper.title, paper.arxiv_id)

        # Calculate generation cost for this post
        generation_cost = self.llm.total_cost - cost_before
        logger.info(
            "Post generation complete for '%s': %d words, cost=$%.4f",
            paper.title,
            word_count,
            generation_cost,
        )

        return BlogPost(
            paper_arxiv_id=paper.arxiv_id,
            title=paper.title,
            slug=slug,
            content=final_content,
            word_count=word_count,
            llm_model=self.llm.model,
            generation_cost=generation_cost,
            status="draft",
        )
