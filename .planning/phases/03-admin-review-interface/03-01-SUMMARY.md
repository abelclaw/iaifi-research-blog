---
phase: 03-admin-review-interface
plan: 01
subsystem: api
tags: [fastapi, sqlite, crud, blog-posts, pipeline, static-files]

# Dependency graph
requires:
  - phase: 02-content-generation-and-concept-extraction
    provides: "Blog post generation pipeline, database schema with blog_posts/figures/concepts tables"
provides:
  - "Blog post review API: list, detail, update, approve, reject endpoints"
  - "Pipeline trigger API: chains discovery and generation in single background task"
  - "BlogPostStatus enum for draft/approved/rejected workflow"
  - "Database CRUD methods for blog post querying and updating"
  - "Figure static file serving via /figures/ mount"
affects: [03-02-review-ui, 04-static-site-generation]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "Status workflow: draft -> approved/rejected with guard validation"
    - "Figure path transformation: filesystem paths to /figures/ URLs in API layer"
    - "Pipeline chaining: discovery then generation as single background task"

key-files:
  created:
    - "admin/routes/posts.py"
    - "admin/routes/pipeline.py"
  modified:
    - "pipeline/models.py"
    - "pipeline/db.py"
    - "admin/app.py"

key-decisions:
  - "Figure path transformation done server-side in API, not client-side in JS"
  - "Pipeline generation targets pdf_downloaded, figures_extracted, and concepts_extracted statuses"
  - "Individual generation failures in pipeline do not abort the entire pipeline run"

patterns-established:
  - "Post review routes follow same Database-per-request pattern as papers.py"
  - "Pipeline background task pattern matches discovery.py with in-memory dict tracking"
  - "Approve/reject guard: only draft posts can transition, 400 for non-draft"

requirements-completed: [ADMIN-01, ADMIN-02, ADMIN-03, ADMIN-04, ADMIN-05]

# Metrics
duration: 2min
completed: 2026-03-03
---

# Phase 3 Plan 1: Post Review API Summary

**Blog post review CRUD API with approve/reject workflow, pipeline trigger chaining discovery+generation, and /figures/ static mount for image serving**

## Performance

- **Duration:** 2 min
- **Started:** 2026-03-03T17:24:22Z
- **Completed:** 2026-03-03T17:26:52Z
- **Tasks:** 2
- **Files modified:** 5

## Accomplishments
- 5 API endpoints for blog post review (list, detail with figures+concepts, update with word count recalc, approve, reject)
- 2 API endpoints for full pipeline trigger (run and status polling)
- BlogPostStatus enum and 3 new Database methods (get_blog_posts with JOIN, update content, update status)
- Figure static mount at /figures/ before catch-all / mount for correct routing
- Figure path transformation from filesystem to URL in API layer

## Task Commits

Each task was committed atomically:

1. **Task 1: Add BlogPostStatus enum, Database CRUD methods, and post review API routes** - `f7b53e6` (feat)
2. **Task 2: Add pipeline trigger route and wire everything into app.py with figures mount** - `e2c1b91` (feat)

## Files Created/Modified
- `pipeline/models.py` - Added BlogPostStatus enum (DRAFT, APPROVED, REJECTED)
- `pipeline/db.py` - Added get_blog_posts (with paper JOIN), update_blog_post_content (recalcs word count), update_blog_post_status methods
- `admin/routes/posts.py` - Blog post review CRUD: list, detail (with figure URL transform and concepts), update, approve, reject
- `admin/routes/pipeline.py` - Full pipeline trigger: chains discovery then generation for eligible papers
- `admin/app.py` - Registered posts and pipeline routers, mounted /figures/ before catch-all /

## Decisions Made
- Figure path transformation is done server-side in the API response, not client-side in JavaScript -- keeps the frontend simple and ensures consistency
- Pipeline generation targets papers with statuses pdf_downloaded, figures_extracted, or concepts_extracted (not just pdf_downloaded) to catch papers at various pipeline stages
- Individual paper generation failures within the pipeline are logged but do not abort the entire pipeline run -- allows partial success

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered
None.

## User Setup Required
None - no external service configuration required.

## Next Phase Readiness
- All 7 API endpoints ready for the review UI (Plan 02) to consume
- /figures/ mount serves extracted images for inline display
- Post detail endpoint returns figures with URLs and concepts for rich review UI

## Self-Check: PASSED

- All 5 files verified on disk
- Both task commits (f7b53e6, e2c1b91) verified in git log

---
*Phase: 03-admin-review-interface*
*Completed: 2026-03-03*
