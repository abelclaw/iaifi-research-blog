"""PDF to markdown conversion for LLM consumption."""

import logging

import pymupdf4llm

logger = logging.getLogger(__name__)


def extract_paper_text(pdf_path: str, max_chars: int = 10000) -> str:
    """Convert a paper PDF to LLM-digestible markdown text.

    Args:
        pdf_path: Path to the PDF file.
        max_chars: Maximum characters to return. Content beyond this
            is truncated with a notice.

    Returns:
        Markdown text extracted from the PDF.

    Raises:
        FileNotFoundError: If the PDF file does not exist.
    """
    from pathlib import Path

    if not Path(pdf_path).exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    logger.info("Extracting text from %s (max %d chars)", pdf_path, max_chars)

    text = pymupdf4llm.to_markdown(
        pdf_path,
        write_images=False,
        show_progress=False,
    )

    if len(text) > max_chars:
        text = text[:max_chars] + "\n\n[Content truncated for processing]"

    logger.info("Extracted %d chars from %s", len(text), pdf_path)
    return text
