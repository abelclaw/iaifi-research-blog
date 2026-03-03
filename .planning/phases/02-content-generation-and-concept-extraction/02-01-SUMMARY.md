---
phase: 02-content-generation-and-concept-extraction
plan: 01
subsystem: api, database, extraction
tags: [litellm, pymupdf, pymupdf4llm, pydantic, sqlite, llm-client, pdf-extraction, figure-extraction]

# Dependency graph
requires:
  - phase: 01-paper-ingestion-pipeline
    provides: "papers table, PDF downloads, pipeline package structure"
provides:
  - "Provider-agnostic LLM client with disk caching (LLMClient)"
  - "PDF to markdown converter for LLM consumption (extract_paper_text)"
  - "Dual-strategy figure extractor with scoring (FigureExtractor)"
  - "BlogPost, Figure, ExtractedConcept, ConceptExtractionResult Pydantic models"
  - "blog_posts, figures, concepts database tables with CRUD methods"
  - "LLMSettings config with env var overrides"
affects: [02-02, 02-03, 03-site-generation]

# Tech tracking
tech-stack:
  added: [litellm, pymupdf, pymupdf4llm, jinja2, pillow]
  patterns: [provider-agnostic-llm, disk-caching, dual-extraction-strategy, pydantic-structured-output]

key-files:
  created:
    - pipeline/generator/__init__.py
    - pipeline/generator/llm_client.py
    - pipeline/extractor/__init__.py
    - pipeline/extractor/pdf_reader.py
    - pipeline/extractor/figure_extractor.py
  modified:
    - pyproject.toml
    - pipeline/models.py
    - pipeline/config.py
    - pipeline/db.py

key-decisions:
  - "Used litellm for provider-agnostic LLM access -- single model string config switches between Claude, GPT, Ollama"
  - "Disk caching via litellm Cache avoids redundant API calls during development iteration"
  - "Dual figure extraction: raster (get_images) + vector (cluster_drawings) captures both embedded images and drawn diagrams"
  - "Figure scoring by area * aspect_ratio * page_position prefers large, well-proportioned, early-page figures"
  - "Pillow normalizes all extracted images to PNG for consistent downstream handling"

patterns-established:
  - "LLMClient pattern: init validates API keys, generate() for text, generate_structured() for Pydantic models"
  - "Config singleton pattern extended: llm_settings alongside settings for domain-specific config"
  - "Database CRUD pattern: insert returns ID, get returns dict or None, list returns list[dict]"

requirements-completed: [GEN-06, GEN-05]

# Metrics
duration: 3min
completed: 2026-03-03
---

# Phase 2 Plan 1: Foundation Infrastructure Summary

**Provider-agnostic LLM client with litellm disk caching, dual-strategy PDF figure extractor, and extended database schema for blog posts/figures/concepts**

## Performance

- **Duration:** 3 min
- **Started:** 2026-03-03T16:51:18Z
- **Completed:** 2026-03-03T16:54:55Z
- **Tasks:** 2
- **Files modified:** 9

## Accomplishments
- LLM client supporting Claude/GPT/Ollama via single config value with disk caching for zero-cost re-runs
- PDF-to-markdown extraction verified against real IAIFI paper (10036 chars extracted)
- Dual raster+vector figure extraction with scoring algorithm for selecting top 1-3 figures
- Database extended with blog_posts, figures, concepts tables and full CRUD methods
- Five new Pydantic models including structured output support for concept extraction

## Task Commits

Each task was committed atomically:

1. **Task 1: Install dependencies, extend models and config, add database tables** - `dee8618` (feat)
2. **Task 2: Create LLM client, PDF reader, and figure extractor** - `1a2c49d` (feat)

## Files Created/Modified
- `pyproject.toml` - Added litellm, pymupdf, pymupdf4llm, jinja2, pillow dependencies
- `pipeline/models.py` - Added BlogPost, Figure, ExtractedConcept, ConceptExtractionResult models; extended PaperStatus
- `pipeline/config.py` - Added LLMSettings dataclass with env var overrides; added FIGURES_DIR to Settings
- `pipeline/db.py` - Added blog_posts, figures, concepts tables with indexes and 6 CRUD methods
- `pipeline/generator/__init__.py` - Generator package init
- `pipeline/generator/llm_client.py` - Provider-agnostic LLM client with disk caching, retry, structured output
- `pipeline/extractor/__init__.py` - Extractor package init
- `pipeline/extractor/pdf_reader.py` - PDF to markdown via pymupdf4llm with truncation
- `pipeline/extractor/figure_extractor.py` - Dual raster+vector figure extraction with scoring

## Decisions Made
- Used litellm for provider-agnostic LLM access -- single model string config switches between Claude, GPT, Ollama
- Disk caching via litellm Cache avoids redundant API calls during development iteration
- Dual figure extraction: raster (get_images) + vector (cluster_drawings) captures both embedded images and drawn diagrams
- Figure scoring by area * aspect_ratio * page_position prefers large, well-proportioned, early-page figures
- Pillow normalizes all extracted images to PNG for consistent downstream handling

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

External services require manual configuration for LLM content generation:
- **ANTHROPIC_API_KEY** - Required for Claude (default provider). Get from: https://console.anthropic.com/settings/keys
- Alternatively: OPENAI_API_KEY for GPT models, or OPENAI_API_BASE for Ollama/local models
- LLMClient validates API key presence at initialization and provides clear error message

## Next Phase Readiness
- LLM client ready for content generation (plan 02-02) and concept extraction (plan 02-03)
- Figure extractor ready for paper processing pipeline
- PDF reader tested against real papers -- produces clean markdown
- Database schema ready for storing generated blog posts, figures, and concepts

## Self-Check: PASSED

- All 5 created files verified on disk
- Both task commits (dee8618, 1a2c49d) verified in git log

---
*Phase: 02-content-generation-and-concept-extraction*
*Plan: 01*
*Completed: 2026-03-03*
