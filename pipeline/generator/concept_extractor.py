"""LLM-based concept extraction with Pydantic structured output."""

import logging

from jinja2 import Environment, FileSystemLoader

from pipeline.generator.llm_client import LLMClient
from pipeline.models import ConceptExtractionResult, Paper

logger = logging.getLogger(__name__)

CONCEPT_SYSTEM_PROMPT = (
    "You are a scientific concept analyst specializing in AI and fundamental "
    "physics research. You identify the key technical concepts, methods, and "
    "phenomena in research papers. You provide structured, precise analysis."
)


class ConceptExtractor:
    """Extracts structured scientific concepts from papers using LLM analysis.

    Uses Pydantic structured output to produce 5-15 concepts with name,
    description, and relevance score. Also validates/corrects the paper's
    IAIFI theme categorization.
    """

    def __init__(
        self,
        llm_client: LLMClient,
        prompts_dir: str = "pipeline/generator/prompts",
    ):
        self.llm = llm_client
        self.env = Environment(
            loader=FileSystemLoader(prompts_dir),
            keep_trailing_newline=True,
        )
        logger.info(
            "ConceptExtractor initialized with prompts from %s", prompts_dir
        )

    async def extract_concepts(
        self, paper: Paper, pdf_text: str
    ) -> ConceptExtractionResult:
        """Extract scientific concepts from a paper.

        Args:
            paper: Paper model with metadata (title, authors, abstract, etc.).
            pdf_text: Markdown text extracted from the paper's PDF.

        Returns:
            ConceptExtractionResult with concepts, primary theme, and
            secondary themes.
        """
        template = self.env.get_template("concepts.j2")
        user_prompt = template.render(
            title=paper.title,
            authors=paper.authors,
            abstract=paper.abstract,
            paper_content=pdf_text,
            iaifi_category=paper.iaifi_category,
        )

        result = await self.llm.generate_structured(
            system_prompt=CONCEPT_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_model=ConceptExtractionResult,
        )

        logger.info(
            "Extracted %d concepts for '%s' (theme: %s)",
            len(result.concepts),
            paper.title,
            result.iaifi_theme,
        )

        return result
