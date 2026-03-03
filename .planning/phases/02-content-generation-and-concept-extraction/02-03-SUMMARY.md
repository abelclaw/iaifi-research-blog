---
phase: 02-content-generation-and-concept-extraction
plan: 03
subsystem: generation, extraction, api
tags: [concept-extraction, pydantic-structured-output, content-pipeline, orchestrator, fastapi-background-tasks]

# Dependency graph
requires:
  - phase: 02-content-generation-and-concept-extraction
    plan: 01
    provides: "LLMClient, FigureExtractor, extract_paper_text, Database CRUD, Pydantic models"
  - phase: 02-content-generation-and-concept-extraction
    plan: 02
    provides: "PostGenerator with three-pass blog generation"
provides:
  - "ConceptExtractor class with LLM structured output for 5-15 concepts per paper"
  - "ContentGenerator orchestrator wiring figures + blog post + concepts pipeline"
  - "Admin API endpoint for triggering content generation (POST /api/generate/{arxiv_id})"
  - "Generation status polling (GET /api/generate/{task_id}/status)"
  - "Paper status progression through FIGURES_EXTRACTED -> POST_GENERATED -> CONCEPTS_EXTRACTED"
affects: [03-site-generation, 04-concept-network]

# Tech tracking
tech-stack:
  added: []
  patterns: [structured-concept-extraction, content-generation-orchestrator, background-task-with-progress]

key-files:
  created:
    - pipeline/generator/prompts/concepts.j2
    - pipeline/generator/concept_extractor.py
    - admin/routes/generation.py
  modified:
    - pipeline/orchestrator.py
    - admin/app.py

key-decisions:
  - "ConceptExtractor uses generate_structured() with Pydantic response_format for reliable JSON extraction"
  - "ContentGenerator runs all steps sequentially (figures -> text -> blog -> concepts) with status updates between each"
  - "Generation task IDs include arxiv_id and timestamp for uniqueness and traceability"

patterns-established:
  - "Content pipeline pattern: orchestrator creates sub-components in __init__, runs sequential async steps with progress callbacks"
  - "Paper model reconstruction: DB dict parsed into Pydantic model for type-safe downstream use"
  - "Background generation pattern: same in-memory dict tracking as discovery, with step-level progress updates"

requirements-completed: [CONCEPT-01, CONCEPT-02, CONCEPT-03]

# Metrics
duration: 3min
completed: 2026-03-03
---

# Phase 2 Plan 3: Concept Extraction and Generation Pipeline Summary

**LLM structured concept extraction with Pydantic response_format, full content generation orchestrator wiring figures + blog + concepts, and admin API endpoint for triggering generation**

## Performance

- **Duration:** 3 min
- **Started:** 2026-03-03T17:02:12Z
- **Completed:** 2026-03-03T17:04:55Z
- **Tasks:** 2
- **Files modified:** 5

## Accomplishments
- ConceptExtractor uses LLM structured output to extract 5-15 scientific concepts with name, description, and relevance score per paper
- ContentGenerator orchestrates the complete pipeline: figure extraction, text extraction, blog post generation, and concept extraction in sequence
- All generated data (figures, blog posts, concepts) persisted to SQLite with paper status progression
- Admin can trigger generation via POST /api/generate/{arxiv_id} with background execution and step-level progress polling

## Task Commits

Each task was committed atomically:

1. **Task 1: Create concept extraction prompt and ConceptExtractor class** - `68b4325` (feat)
2. **Task 2: Wire generation orchestrator and add admin API endpoint** - `2b0b5bc` (feat)

## Files Created/Modified
- `pipeline/generator/prompts/concepts.j2` - Jinja2 prompt template for structured concept extraction with IAIFI theme validation
- `pipeline/generator/concept_extractor.py` - ConceptExtractor class using LLM structured output (Pydantic response_format)
- `pipeline/orchestrator.py` - Added ContentGenerator class orchestrating full content generation pipeline
- `admin/routes/generation.py` - API routes for triggering generation and polling status
- `admin/app.py` - Registered generation router before static file mount

## Decisions Made
- ConceptExtractor uses generate_structured() with Pydantic response_format for reliable JSON extraction -- same pattern as LLMClient already supports
- ContentGenerator runs all steps sequentially (figures -> text -> blog -> concepts) with status updates between each step
- Generation task IDs include arxiv_id and timestamp for uniqueness and traceability (e.g., gen-2301.12345-1709478132)

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required. (LLM API keys from plan 02-01 still required for actual content generation.)

## Next Phase Readiness
- Phase 2 complete: all content generation and concept extraction infrastructure built
- Full pipeline can be triggered via admin API: discovery -> figure extraction -> blog post -> concept extraction
- Site generation phase can consume blog_posts, figures, and concepts from SQLite
- Concept network phase can query structured concept data per paper

## Self-Check: PASSED

- All 3 created files verified on disk
- Both task commits (68b4325, 2b0b5bc) verified in git log

---
*Phase: 02-content-generation-and-concept-extraction*
*Plan: 03*
*Completed: 2026-03-03*
