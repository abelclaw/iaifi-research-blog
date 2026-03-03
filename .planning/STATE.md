# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-03-03)

**Core value:** Every IAIFI paper gets a well-written, accessible blog post that connects it to the broader landscape of AI and fundamental physics research -- without requiring manual writing effort.
**Current focus:** Phase 2: Content Generation and Concept Extraction

## Current Position

Phase: 2 of 5 (Content Generation and Concept Extraction)
Plan: 1 of 3 in current phase
Status: Executing phase
Last activity: 2026-03-03 -- Completed 02-01-PLAN.md

Progress: [███░░░░░░░] 30%

## Performance Metrics

**Velocity:**
- Total plans completed: 3
- Average duration: 4min
- Total execution time: 0.18 hours

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 01-paper-ingestion-pipeline | 2/2 | 8min | 4min |
| 02-content-generation-and-concept-extraction | 1/3 | 3min | 3min |

**Recent Trend:**
- Last 5 plans: 5min, 3min, 3min
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

### Pending Todos

None yet.

### Blockers/Concerns

None yet.

## Session Continuity

Last session: 2026-03-03
Stopped at: Completed 02-01-PLAN.md (Foundation infrastructure for Phase 2)
Resume file: None
