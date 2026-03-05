"""LLM-based concept extraction with Pydantic structured output."""

import logging
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

from pipeline.models import ConceptExtractionResult, Paper

logger = logging.getLogger(__name__)

CONCEPT_SYSTEM_PROMPT = (
    "You are a scientific concept analyst specializing in AI and fundamental "
    "physics research. You identify the key technical concepts, methods, and "
    "phenomena in research papers. You provide structured, precise analysis."
)

# Default taxonomy path relative to project root
_TAXONOMY_PATH = Path(__file__).parent.parent / "concepts_taxonomy.yaml"


def load_taxonomy(path: Path | None = None) -> dict[str, list[str]]:
    """Load the IAIFI concept taxonomy from YAML.

    Returns a flat dict of category_name -> list of concept names.
    """
    path = path or _TAXONOMY_PATH
    with open(path) as f:
        data = yaml.safe_load(f)

    taxonomy = {}
    for category, concepts in data.get("categories", {}).items():
        taxonomy[category] = concepts
    return taxonomy


def build_taxonomy_set(taxonomy: dict[str, list[str]]) -> set[str]:
    """Build a flat set of all canonical concept names (lowercased)."""
    names = set()
    for concepts in taxonomy.values():
        for c in concepts:
            names.add(c.lower().strip())
    return names


class ConceptExtractor:
    """Extracts structured scientific concepts from papers using LLM analysis.

    Uses a curated IAIFI taxonomy to ensure consistent concept vocabulary
    across papers, enabling meaningful network connections.
    """

    def __init__(
        self,
        llm_client,
        prompts_dir: str = "pipeline/generator/prompts",
        taxonomy_path: Path | None = None,
    ):
        self.llm = llm_client
        self.env = Environment(
            loader=FileSystemLoader(prompts_dir),
            keep_trailing_newline=True,
        )
        self.taxonomy = load_taxonomy(taxonomy_path)
        self.canonical_names = build_taxonomy_set(self.taxonomy)
        logger.info(
            "ConceptExtractor initialized with %d taxonomy concepts from %d categories",
            len(self.canonical_names),
            len(self.taxonomy),
        )

    def _normalize_concept_name(self, name: str) -> str:
        """Normalize a concept name against the taxonomy.

        If the lowercased name matches a taxonomy entry, return the
        canonical form. Otherwise return the original (lowercased).
        """
        lower = name.lower().strip()
        if lower in self.canonical_names:
            return lower
        # Try fuzzy: strip trailing 's' for simple plural
        if lower.endswith("s") and lower[:-1] in self.canonical_names:
            return lower[:-1]
        return lower

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
            taxonomy=self.taxonomy,
        )

        result = await self.llm.generate_structured(
            system_prompt=CONCEPT_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            response_model=ConceptExtractionResult,
        )

        # Normalize concept names against taxonomy
        for concept in result.concepts:
            concept.name = self._normalize_concept_name(concept.name)

        logger.info(
            "Extracted %d concepts for '%s' (theme: %s)",
            len(result.concepts),
            paper.title,
            result.iaifi_theme,
        )

        return result
