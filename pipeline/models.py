"""Data models for the IAIFI paper ingestion pipeline."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class PaperStatus(str, Enum):
    """Tracks a paper's progress through the ingestion pipeline."""

    DISCOVERED = "discovered"
    METADATA_FETCHED = "metadata_fetched"
    PDF_DOWNLOADED = "pdf_downloaded"
    INGESTION_COMPLETE = "ingestion_complete"
    FIGURES_EXTRACTED = "figures_extracted"
    CONCEPTS_EXTRACTED = "concepts_extracted"
    POST_GENERATED = "post_generated"


class BlogPostStatus(str, Enum):
    """Tracks a blog post's review status."""

    DRAFT = "draft"
    APPROVED = "approved"
    REJECTED = "rejected"


class ScrapedPaper(BaseModel):
    """Raw paper data scraped from the IAIFI website."""

    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str | None = None
    category: str
    code_url: str | None = None
    source_url: str


class Paper(BaseModel):
    """Full paper model with arXiv metadata and pipeline status."""

    arxiv_id: str
    arxiv_id_versioned: str | None = None
    title: str
    authors: list[str]
    abstract: str
    arxiv_categories: list[str]
    iaifi_category: str
    published: datetime | None = None
    pdf_path: str | None = None
    pdf_url: str | None = None
    code_url: str | None = None
    status: PaperStatus = PaperStatus.DISCOVERED
    created_at: datetime | None = None
    updated_at: datetime | None = None


class BlogPost(BaseModel):
    """Generated blog post for a paper."""

    paper_arxiv_id: str
    title: str
    slug: str
    content: str
    word_count: int
    llm_model: str
    generation_cost: float = 0.0
    status: str = "draft"
    created_at: datetime | None = None
    updated_at: datetime | None = None


class Figure(BaseModel):
    """Extracted figure from a paper PDF."""

    paper_arxiv_id: str
    figure_path: str
    page_number: int
    width: int
    height: int
    extraction_type: str
    sort_order: int = 0
    created_at: datetime | None = None


class ExtractedConcept(BaseModel):
    """A single concept extracted from a paper."""

    name: str
    description: str
    relevance: float = Field(ge=0, le=1)


class ConceptExtractionResult(BaseModel):
    """Result of concept extraction from a paper."""

    concepts: list[ExtractedConcept] = Field(min_length=5, max_length=15)
    iaifi_theme: str
    secondary_themes: list[str] = Field(default_factory=list)


class DiscoveryResult(BaseModel):
    """Summary of a discovery pipeline run."""

    total_scraped: int
    new_papers: int
    metadata_fetched: int
    pdfs_downloaded: int
    errors: list[str]
