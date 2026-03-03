"""Configuration for the IAIFI paper ingestion pipeline."""

import os
from dataclasses import dataclass, field


@dataclass
class Settings:
    """Pipeline configuration with environment variable overrides."""

    DB_PATH: str = os.environ.get("IAIFI_DB_PATH", "data/papers.db")
    PDF_DIR: str = os.environ.get("IAIFI_PDF_DIR", "data/pdfs")
    ARXIV_DELAY_SECONDS: float = float(
        os.environ.get("IAIFI_ARXIV_DELAY", "3.0")
    )
    ARXIV_BATCH_SIZE: int = int(
        os.environ.get("IAIFI_ARXIV_BATCH_SIZE", "20")
    )

    CATEGORY_PAGES: dict[str, str] = field(default_factory=lambda: {
        "Foundational AI": "https://iaifi.org/papers-ai.html",
        "Theoretical Physics": "https://iaifi.org/papers-theory.html",
        "Experimental Physics": "https://iaifi.org/papers-experiment.html",
        "Astrophysics": "https://iaifi.org/papers-astro.html",
    })


# Module-level singleton for convenient imports
settings = Settings()
