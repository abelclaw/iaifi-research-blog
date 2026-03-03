# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-03-03)

**Core value:** Every IAIFI paper gets a well-written, accessible blog post that connects it to the broader landscape of AI and fundamental physics research -- without requiring manual writing effort.
**Current focus:** Phase 3: Admin Review Interface

## Current Position

Phase: 3 of 5 (Admin Review Interface)
Plan: 1 of 2 in current phase
Status: In progress
Last activity: 2026-03-03 -- Completed 03-01-PLAN.md

Progress: [██████░░░░] 60%

## Performance Metrics

**Velocity:**
- Total plans completed: 6
- Average duration: 3.3min
- Total execution time: 0.30 hours

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 01-paper-ingestion-pipeline | 2/2 | 8min | 4min |
| 02-content-generation-and-concept-extraction | 3/3 | 8min | 2.7min |
| 03-admin-review-interface | 1/2 | 2min | 2min |

**Recent Trend:**
- Last 5 plans: 3min, 3min, 2min, 3min, 2min
- Trend: Fast

*Updated after each plan completion*

## Accumulated Context

### Decisions

Decisions are logged in PROJECT.md Key Decisions table.
Recent decisions affecting current work:

- [Roadmap]: 5-phase structure derived from 26 requirements across 5 categories
- [Roadmap]: Content generation and concept extraction combined into single phase (shared LLM pipeline)
- [Roadmap]: Concept network visualization isolated as final phase (depends on quality concept data + site shell)
- [01-01]: Used hatchling build backend with packages=["pipeline"] for non-standard package name
- [01-01]: Scrape all 4 category pages (not main papers.html) for definitive category assignments
- [01-01]: Store authors/categories as JSON strings in SQLite, parsed to lists on read
- [01-01]: arXiv ID normalization: always strip version suffix for consistent cross-referencing
- [01-02]: Static files mount AFTER API routers to prevent /api/* interception
- [01-02]: In-memory dict for task tracking (sufficient for single-user local app)
- [01-02]: Vanilla JS only for admin UI (no frontend framework needed)
- [01-02]: Database instantiated per-request matching aiosqlite connection-per-op pattern
- [02-01]: Used litellm for provider-agnostic LLM access -- single model string config switches between Claude, GPT, Ollama
- [02-01]: Disk caching via litellm Cache avoids redundant API calls during development iteration
- [02-01]: Dual figure extraction: raster + vector captures both embedded images and drawn diagrams
- [02-01]: Figure scoring by area * aspect_ratio * page_position prefers large, well-proportioned, early-page figures
- [02-01]: Pillow normalizes all extracted images to PNG for consistent downstream handling
- [02-02]: Three distinct system prompts give each LLM pass a clear persona: journalist drafts, reader simplifies, editor polishes
- [02-02]: Word count tolerance (700-1600) wider than target (800-1500) to avoid rejecting borderline posts
- [02-02]: Cost tracked per post via LLMClient total_cost delta rather than per-call tracking
- [02-03]: ConceptExtractor uses generate_structured() with Pydantic response_format for reliable JSON extraction
- [02-03]: ContentGenerator runs all steps sequentially (figures -> text -> blog -> concepts) with status updates between each
- [02-03]: Generation task IDs include arxiv_id and timestamp for uniqueness and traceability
- [03-01]: Figure path transformation done server-side in API, not client-side in JS
- [03-01]: Pipeline generation targets pdf_downloaded, figures_extracted, and concepts_extracted statuses
- [03-01]: Individual generation failures in pipeline do not abort the entire pipeline run

### Pending Todos

None yet.

### Blockers/Concerns

None yet.

## Session Continuity

Last session: 2026-03-03
Stopped at: Completed 03-01-PLAN.md (Post review API and pipeline trigger)
Resume file: None
