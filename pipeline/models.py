"""Data models for the IAIFI paper ingestion pipeline."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class PaperStatus(str, Enum):
    """Tracks a paper's progress through the ingestion pipeline."""

    DISCOVERED = "discovered"
    METADATA_FETCHED = "metadata_fetched"
    PDF_DOWNLOADED = "pdf_downloaded"
    INGESTION_COMPLETE = "ingestion_complete"


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


class DiscoveryResult(BaseModel):
    """Summary of a discovery pipeline run."""

    total_scraped: int
    new_papers: int
    metadata_fetched: int
    pdfs_downloaded: int
    errors: list[str]
