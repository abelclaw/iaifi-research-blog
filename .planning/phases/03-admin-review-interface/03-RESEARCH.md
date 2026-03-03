# Phase 3: Admin Review Interface - Research

**Researched:** 2026-03-03
**Domain:** FastAPI admin UI for blog post review/edit/approve workflow (vanilla JS frontend)
**Confidence:** HIGH

## Summary

Phase 3 extends the existing FastAPI admin application with a review workflow for generated blog posts. The existing codebase already has a FastAPI app (`admin/app.py`), static HTML UI (`admin/static/index.html`), SQLite database with `blog_posts` and `figures` tables, and API routes for discovery and generation. The blog_posts table already has a `status` field defaulting to `"draft"`. The work is primarily: (1) new API endpoints for listing drafts, fetching post details with figures, updating post content, and changing approval status; (2) new Database methods for querying and updating blog posts; (3) a new review UI page with markdown editing and figure display; and (4) wiring the existing discovery + generation pipelines into a single "run pipeline" trigger.

The technical risk is LOW. All building blocks exist -- FastAPI routes, aiosqlite database methods, and vanilla JS patterns are already established in the codebase. The main design decisions are: how to render markdown for preview (use `marked.js` via CDN), how to provide editing (split-pane textarea + live preview), and how to serve extracted figure images (mount `data/figures` as a second static files directory).

**Primary recommendation:** Extend the existing admin app with new routes under `admin/routes/posts.py`, add Database helper methods for blog post CRUD, and build a review UI page using the same vanilla JS pattern as `index.html` -- keeping it simple with `marked.js` from CDN for markdown rendering and a plain textarea for editing.

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| ADMIN-01 | Local web app for reviewing generated blog post drafts | Extend existing FastAPI app + static HTML. Add `GET /api/posts` endpoint to list drafts. Add new `review.html` page. See Architecture Patterns: Multi-Page Static HTML. |
| ADMIN-02 | Admin can view extracted figures inline with blog text | Mount `data/figures` as static files route. Fetch figures via `GET /api/posts/{arxiv_id}` which returns figure paths. Render as `<img>` tags alongside blog content. See Code Examples: Serving Figures. |
| ADMIN-03 | Admin can edit generated blog text before approval | Use textarea with `marked.js` for live preview. Submit edits via `PUT /api/posts/{arxiv_id}` endpoint. See Architecture Patterns: Split-Pane Editor. |
| ADMIN-04 | Admin can approve or reject drafts | Add `POST /api/posts/{arxiv_id}/approve` and `POST /api/posts/{arxiv_id}/reject` endpoints. Update blog_posts.status to "approved" or "rejected". See Architecture Patterns: Status Workflow. |
| ADMIN-05 | Admin can trigger paper discovery and blog generation pipeline | Add `POST /api/pipeline/run` endpoint that chains discovery -> generation for all eligible papers. Extend existing background task pattern. See Code Examples: Full Pipeline Trigger. |
</phase_requirements>

## Standard Stack

### Core (Already in Place)
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| FastAPI | >=0.115 | API backend | Already used in admin/app.py; async, auto-docs, Pydantic integration |
| aiosqlite | >=0.22 | Async SQLite | Already used in pipeline/db.py; connection-per-operation pattern established |
| Pydantic | >=2.10 | Request/response models | Already used in pipeline/models.py; v2 `model_dump(exclude_unset=True)` for PATCH updates |
| uvicorn | >=0.34 | ASGI server | Already configured for dev with reload |

### New (Frontend Only -- CDN, No Install)
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| marked.js | latest (CDN) | Markdown to HTML rendering | 48KB minified, zero dependencies, used via `<script>` tag from jsDelivr CDN, renders markdown content as HTML preview |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| marked.js (CDN) | EasyMDE (CDN) | EasyMDE provides a full editor toolbar with formatting buttons but adds 200KB+ (CodeMirror + Font Awesome). Overkill for admin-only editing where the user knows markdown. |
| marked.js (CDN) | showdown.js (CDN) | showdown.js is comparable but marked.js is faster and more widely used. No meaningful reason to prefer showdown. |
| Plain textarea | contenteditable div | contenteditable introduces complex DOM manipulation, cursor management issues, and inconsistent cross-browser behavior. textarea is simpler, more reliable, and the content is markdown anyway. |
| Multi-page HTML | Single SPA | The existing UI is already a single HTML file. Adding review as a separate page (or a section in the same page) follows the established pattern. No build tooling needed. |

**Installation:** No new Python dependencies required. Frontend libraries loaded from CDN in HTML.

## Architecture Patterns

### Recommended Project Structure
```
admin/
  app.py                 # FastAPI app (existing -- add figures mount)
  routes/
    discovery.py         # Existing -- no changes
    generation.py        # Existing -- no changes
    papers.py            # Existing -- no changes
    posts.py             # NEW -- blog post review CRUD endpoints
    pipeline.py          # NEW -- full pipeline trigger endpoint
  static/
    index.html           # Existing -- add navigation to review page
    review.html          # NEW -- blog post review/edit/approve UI
pipeline/
  db.py                  # Existing -- add blog post query/update methods
  models.py              # Existing -- add BlogPostStatus enum
```

### Pattern 1: Blog Post Status Workflow
**What:** Blog posts transition through explicit states: `draft` -> `approved` or `draft` -> `rejected`. Only approved posts are eligible for Phase 4 (static site generation). Rejection is final for that draft but the paper can be regenerated.
**When to use:** Every status change endpoint.
**Schema:**
```python
# pipeline/models.py -- add to existing file
class BlogPostStatus(str, Enum):
    DRAFT = "draft"
    APPROVED = "approved"
    REJECTED = "rejected"
```
**Valid transitions:**
- `draft` -> `approved` (admin approves)
- `draft` -> `rejected` (admin rejects)
- `rejected` -> `draft` (regeneration creates new draft, replacing rejected version)

**Key constraint:** Approving or rejecting a non-draft post should return 400 Bad Request. This prevents double-approving or approving an already-rejected post.

### Pattern 2: Multi-Page Static HTML (Admin Navigation)
**What:** Instead of a single-page application, use multiple HTML pages served as static files, with shared navigation. Each page is self-contained with its own JS. Navigation between pages uses standard `<a href>` links.
**When to use:** Extending the admin UI with new views.
**Rationale:** The existing `index.html` follows this pattern. Adding `review.html` as a sibling is the simplest extension. No build tools, no client-side routing, no state management library needed. The admin is a local tool for 1 person.

### Pattern 3: Split-Pane Markdown Editor
**What:** A textarea on the left for editing raw markdown, a rendered HTML preview on the right using `marked.js`. The preview updates on every keystroke via an `input` event listener on the textarea.
**When to use:** The blog post edit view.
**Implementation:**
```html
<div class="editor-container">
    <textarea id="editor" oninput="updatePreview()"></textarea>
    <div id="preview" class="preview-pane"></div>
</div>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
function updatePreview() {
    document.getElementById('preview').innerHTML =
        marked.parse(document.getElementById('editor').value);
}
</script>
```

### Pattern 4: Figure Serving via Static Mount
**What:** Mount the `data/figures` directory as a second static files route so figure images are directly accessible via URL. The figures table stores filesystem paths like `data/figures/2501_09081/figure_1.png`. The URL becomes `/figures/2501_09081/figure_1.png`.
**When to use:** Always -- needed for ADMIN-02 (inline figures).
**Implementation:**
```python
# admin/app.py -- add BEFORE the catch-all static mount
from pathlib import Path
from pipeline.config import settings

figures_path = Path(settings.FIGURES_DIR)
figures_path.mkdir(parents=True, exist_ok=True)
app.mount(
    "/figures",
    StaticFiles(directory=str(figures_path)),
    name="figures",
)
```
**Critical ordering:** This mount MUST come before the catch-all `/` static mount (which serves `admin/static/`), otherwise the root mount will intercept `/figures/*` requests.

### Pattern 5: Connection-Per-Operation Database Access
**What:** Each route handler instantiates its own `Database` object (which opens a new aiosqlite connection per operation). This matches the established pattern in the existing routes.
**When to use:** All new route handlers.
**Rationale:** The existing codebase uses this pattern consistently (see `admin/routes/papers.py` line 31, `admin/routes/discovery.py` line 61). While connection pooling would be more efficient, consistency with the existing architecture takes priority. WAL mode enables concurrent reads.

### Anti-Patterns to Avoid
- **Building a SPA framework:** Do not add React, Vue, or any frontend build system. The existing app uses vanilla JS and that should continue. The admin runs locally for one person.
- **Using contenteditable for markdown editing:** It creates more problems than it solves. Use a plain textarea -- the admin user writes markdown, not rich text.
- **Storing edited content only in the frontend:** Always save to the database. If the browser tab closes, unsaved edits are lost. Add an explicit "Save" action that hits the API.
- **Adding authentication:** This is a local app. No auth is needed. The architecture research explicitly calls this out as anti-pattern #4.
- **Creating a separate database for blog post drafts:** The `blog_posts` table already exists with a `status` field. Use it.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Markdown rendering | Custom markdown parser | `marked.js` via CDN | Markdown parsing has hundreds of edge cases (nested lists, code blocks, escaping). A 48KB library solves this completely. |
| Rich text editing | Custom contenteditable editor | Plain textarea + marked.js preview | contenteditable is notoriously buggy cross-browser, has cursor management nightmares, and the content is markdown anyway. |
| Figure path to URL mapping | String manipulation in JS | Static file mount in FastAPI | FastAPI's StaticFiles handles caching headers, MIME types, and 404s correctly. |
| Background task tracking | Custom task queue | FastAPI BackgroundTasks + in-memory dict | Already established in `discovery.py` and `generation.py`. Same pattern for pipeline trigger. |

**Key insight:** This phase is primarily a CRUD UI over existing data. The database schema, pipeline orchestration, and content generation all exist. The work is gluing them together with API endpoints and a frontend. Resist the urge to over-engineer the admin UI -- it runs locally for one person.

## Common Pitfalls

### Pitfall 1: Static File Mount Ordering
**What goes wrong:** The catch-all `app.mount("/", StaticFiles(...), name="static")` at the bottom of `app.py` intercepts all requests that don't match API routes, including `/figures/*` paths. If the figures mount comes after the root mount, figure images 404.
**Why it happens:** FastAPI/Starlette processes mounts in registration order. The root mount is greedy.
**How to avoid:** Register all specific mounts (like `/figures`) BEFORE the catch-all root mount. API routes registered via `include_router` already take precedence because they are matched before mounts.
**Warning signs:** Figure images return HTML (the index page) instead of PNG data.

### Pitfall 2: Figure Path Mismatch Between DB and URL
**What goes wrong:** The `figures` table stores absolute filesystem paths like `data/figures/2501_09081/figure_1.png`. The frontend needs URL paths like `/figures/2501_09081/figure_1.png`. If the API returns raw filesystem paths, the frontend cannot display images.
**Why it happens:** The figure extractor saves absolute or relative filesystem paths. The web frontend operates with URL paths.
**How to avoid:** The API endpoint that returns post details should transform figure paths: strip the `data/figures/` prefix (or the configured `FIGURES_DIR`) and prepend `/figures/`. Do this transformation in the API layer, not the frontend.
**Warning signs:** Broken image tags with `src="data/figures/..."` in the browser.

### Pitfall 3: Losing Edits on Page Navigation
**What goes wrong:** Admin spends 10 minutes editing a blog post, accidentally clicks a link or closes the tab, loses all changes.
**Why it happens:** No autosave or unsaved-changes warning. The edit state exists only in the textarea.
**How to avoid:** Add a `beforeunload` event listener that warns when there are unsaved changes. Optionally, save draft-in-progress to `localStorage` as a safety net. But the primary protection is the `beforeunload` prompt.
**Warning signs:** User complaints about lost work.

### Pitfall 4: Not Handling Missing Blog Posts or Figures
**What goes wrong:** The review UI assumes every paper with status `post_generated` has a blog post and figures in the database. If generation partially failed (e.g., post exists but figures failed), the UI crashes or shows broken content.
**Why it happens:** The generation pipeline can fail partway through. A paper might have status `figures_extracted` (figures done) but no blog post yet, or `post_generated` but with zero figures (papers without significant images).
**How to avoid:** The API should return what exists and gracefully handle missing data. The frontend should show "No figures extracted" instead of breaking. Check for null/empty responses for both blog post and figures independently.
**Warning signs:** JavaScript errors in console when viewing certain posts.

### Pitfall 5: Word Count Drift After Editing
**What goes wrong:** Admin edits the blog post content but the `word_count` field in the database still reflects the original generated content. Phase 4 (static site) may use word count for reading time estimates, producing inaccurate results.
**Why it happens:** The `PUT /api/posts/{arxiv_id}` endpoint updates content but forgets to recalculate word count.
**How to avoid:** When saving edited content, always recalculate `word_count = len(content.split())` on the server side before persisting.
**Warning signs:** Reading time estimates on the static site that don't match actual post length.

### Pitfall 6: Pipeline Trigger Runs Discovery But Skips Generation
**What goes wrong:** The "Run Full Pipeline" button triggers discovery successfully but does not chain into generation for newly discovered papers. The admin has to manually trigger generation for each paper.
**Why it happens:** Discovery and generation are separate background tasks with separate tracking. Chaining them requires the discovery task to know it should trigger generation upon completion.
**How to avoid:** The pipeline trigger endpoint should run both sequentially: (1) discovery, (2) generation for all papers with `pdf_downloaded` status that don't yet have a blog post. This is a new orchestration method that wraps the existing `DiscoveryOrchestrator.discover()` and `ContentGenerator.generate_content()`.
**Warning signs:** After running the full pipeline, new papers appear in the list but have no blog post drafts.

## Code Examples

Verified patterns from the existing codebase and official FastAPI documentation:

### Database Methods for Blog Post CRUD
```python
# pipeline/db.py -- add these methods to the Database class

async def get_blog_posts(self, status: str | None = None) -> list[dict]:
    """Retrieve all blog posts, optionally filtered by status."""
    async with aiosqlite.connect(self.db_path) as db:
        db.row_factory = aiosqlite.Row
        if status:
            cursor = await db.execute(
                "SELECT * FROM blog_posts WHERE status = ? ORDER BY created_at DESC",
                (status,),
            )
        else:
            cursor = await db.execute(
                "SELECT * FROM blog_posts ORDER BY created_at DESC"
            )
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]

async def update_blog_post_content(
    self, arxiv_id: str, content: str
) -> None:
    """Update blog post content and recalculate word count."""
    word_count = len(content.split())
    async with aiosqlite.connect(self.db_path) as db:
        await db.execute(
            """UPDATE blog_posts
               SET content = ?, word_count = ?, updated_at = datetime('now')
               WHERE paper_arxiv_id = ?""",
            (content, word_count, arxiv_id),
        )
        await db.commit()

async def update_blog_post_status(
    self, arxiv_id: str, status: str
) -> None:
    """Update blog post status (draft/approved/rejected)."""
    async with aiosqlite.connect(self.db_path) as db:
        await db.execute(
            """UPDATE blog_posts
               SET status = ?, updated_at = datetime('now')
               WHERE paper_arxiv_id = ?""",
            (status, arxiv_id),
        )
        await db.commit()
```

### Post Review API Routes
```python
# admin/routes/posts.py
# Source: follows existing pattern from admin/routes/papers.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pipeline.config import settings
from pipeline.db import Database

router = APIRouter()

class PostUpdateRequest(BaseModel):
    content: str

@router.get("/api/posts")
async def list_posts(status: str | None = None):
    """List all blog posts with associated paper info."""
    db = Database(db_path=settings.DB_PATH)
    posts = await db.get_blog_posts(status=status)
    return posts

@router.get("/api/posts/{arxiv_id}")
async def get_post_detail(arxiv_id: str):
    """Get full blog post with figures for review."""
    db = Database(db_path=settings.DB_PATH)
    post = await db.get_blog_post(arxiv_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    figures = await db.get_figures(arxiv_id)
    # Transform figure paths to URLs
    figures_dir = settings.FIGURES_DIR
    for fig in figures:
        path = fig["figure_path"]
        if path.startswith(figures_dir):
            fig["url"] = "/figures" + path[len(figures_dir):]
        else:
            fig["url"] = "/figures/" + path.split("figures/", 1)[-1] if "figures/" in path else path
    return {"post": post, "figures": figures}

@router.put("/api/posts/{arxiv_id}")
async def update_post(arxiv_id: str, body: PostUpdateRequest):
    """Update blog post content (admin editing)."""
    db = Database(db_path=settings.DB_PATH)
    post = await db.get_blog_post(arxiv_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    await db.update_blog_post_content(arxiv_id, body.content)
    return {"status": "updated", "word_count": len(body.content.split())}

@router.post("/api/posts/{arxiv_id}/approve")
async def approve_post(arxiv_id: str):
    """Approve a draft blog post."""
    db = Database(db_path=settings.DB_PATH)
    post = await db.get_blog_post(arxiv_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    if post["status"] != "draft":
        raise HTTPException(status_code=400, detail=f"Cannot approve post with status '{post['status']}'")
    await db.update_blog_post_status(arxiv_id, "approved")
    return {"status": "approved"}

@router.post("/api/posts/{arxiv_id}/reject")
async def reject_post(arxiv_id: str):
    """Reject a draft blog post."""
    db = Database(db_path=settings.DB_PATH)
    post = await db.get_blog_post(arxiv_id)
    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")
    if post["status"] != "draft":
        raise HTTPException(status_code=400, detail=f"Cannot reject post with status '{post['status']}'")
    await db.update_blog_post_status(arxiv_id, "rejected")
    return {"status": "rejected"}
```

### Serving Figures via Static Mount
```python
# admin/app.py -- add BEFORE the catch-all mount
# Source: FastAPI official docs (https://fastapi.tiangolo.com/tutorial/static-files/)
from pathlib import Path

figures_path = Path(settings.FIGURES_DIR)
figures_path.mkdir(parents=True, exist_ok=True)

# Mount figures directory for serving extracted images
app.mount(
    "/figures",
    StaticFiles(directory=str(figures_path)),
    name="figures",
)

# Mount static files AFTER figures and API routes
app.mount(
    "/",
    StaticFiles(directory="admin/static", html=True),
    name="static",
)
```

### Full Pipeline Trigger
```python
# admin/routes/pipeline.py -- chain discovery + generation

@router.post("/api/pipeline/run")
async def trigger_full_pipeline(background_tasks: BackgroundTasks):
    """Run full pipeline: discovery -> generation for all eligible papers."""
    task_id = f"pipeline-{int(time.time())}"
    _pipeline_tasks[task_id] = {
        "task_id": task_id,
        "status": "running",
        "step": "starting",
        "result": None,
        "error": None,
    }
    background_tasks.add_task(run_full_pipeline, task_id)
    return {"task_id": task_id, "status": "started"}

async def run_full_pipeline(task_id: str):
    """Background: discover papers, then generate content for eligible ones."""
    try:
        db = Database(db_path=settings.DB_PATH)
        await db.initialize()

        # Step 1: Discovery
        _pipeline_tasks[task_id]["step"] = "discovery"
        orchestrator = DiscoveryOrchestrator(db=db, arxiv_client=ArxivClient(...))
        discovery_result = await orchestrator.discover()

        # Step 2: Generate for papers with PDF but no blog post
        _pipeline_tasks[task_id]["step"] = "generation"
        papers = await db.get_papers(status="pdf_downloaded")
        generator = ContentGenerator(db=db)
        generated = 0
        for paper in papers:
            existing_post = await db.get_blog_post(paper["arxiv_id"])
            if not existing_post:
                await generator.generate_content(paper["arxiv_id"])
                generated += 1

        _pipeline_tasks[task_id].update({
            "status": "complete",
            "step": "complete",
            "result": {
                "papers_discovered": discovery_result.new_papers,
                "posts_generated": generated,
            },
        })
    except Exception as e:
        _pipeline_tasks[task_id].update({
            "status": "error",
            "error": str(e),
        })
```

### Markdown Preview with marked.js
```html
<!-- Include via CDN -- no npm/build required -->
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
// Render markdown content to HTML
function renderMarkdown(markdownText) {
    return marked.parse(markdownText);
}

// Live preview: update on every keystroke
document.getElementById('editor').addEventListener('input', function() {
    document.getElementById('preview').innerHTML = renderMarkdown(this.value);
});
</script>
```

### Unsaved Changes Warning
```javascript
// Track whether content has been modified
let hasUnsavedChanges = false;

document.getElementById('editor').addEventListener('input', function() {
    hasUnsavedChanges = true;
    updatePreview();
});

window.addEventListener('beforeunload', function(e) {
    if (hasUnsavedChanges) {
        e.preventDefault();
        e.returnValue = '';
    }
});

// Clear flag after successful save
async function saveContent() {
    // ... save via PUT /api/posts/{arxiv_id} ...
    hasUnsavedChanges = false;
}
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| `@app.on_event("startup")` | `@app.lifespan` context manager | FastAPI 0.109+ | Current code uses deprecated `on_event`. Works fine but should be updated eventually. Not blocking for Phase 3. |
| Pydantic v1 `.dict()` | Pydantic v2 `.model_dump()` | Pydantic 2.0 (2023) | Existing code already uses v2 patterns correctly. |
| `response_model` on every route | Return dicts directly | N/A | Existing pattern returns dicts. Fine for a local admin tool. |

**Deprecated/outdated:**
- `@app.on_event("startup")` in `admin/app.py` is deprecated but functional. Not a Phase 3 concern.

## Open Questions

1. **Should editing support markdown toolbar buttons?**
   - What we know: The admin writes/edits markdown. A plain textarea works. EasyMDE provides a toolbar but adds 200KB+.
   - What's unclear: Whether the admin user is comfortable with raw markdown or needs toolbar assistance.
   - Recommendation: Start with plain textarea + preview. If the user wants a toolbar, EasyMDE can be added later via CDN swap (non-breaking change). Keep it simple.

2. **Should the full pipeline trigger include papers that already have posts?**
   - What we know: A paper might have a rejected post and the admin wants to regenerate. The pipeline trigger currently only generates for papers WITHOUT a blog post.
   - What's unclear: Whether regeneration should overwrite the existing post or create a new version.
   - Recommendation: The pipeline trigger should only generate for papers that have NO blog post yet. Regeneration of rejected posts should be a separate explicit action (a "Regenerate" button on the review page) to avoid accidental overwriting.

3. **Where should review.html live -- separate page or section within index.html?**
   - What we know: index.html currently handles discovery and paper listing. Adding review UI there would make it very long.
   - What's unclear: Whether the user prefers a single page or multi-page navigation.
   - Recommendation: Separate `review.html` page with navigation links between pages. Keeps each page focused and manageable. The existing `index.html` gets a nav link to the review page and vice versa.

## Sources

### Primary (HIGH confidence)
- Existing codebase analysis: `admin/app.py`, `admin/routes/*.py`, `pipeline/db.py`, `pipeline/models.py`, `pipeline/orchestrator.py`, `admin/static/index.html` -- direct code reading
- FastAPI StaticFiles documentation: https://fastapi.tiangolo.com/tutorial/static-files/ -- static file serving patterns
- FastAPI Body Updates documentation: https://fastapi.tiangolo.com/tutorial/body-updates/ -- PATCH/PUT patterns with Pydantic
- marked.js official documentation: https://marked.js.org/ -- markdown rendering API

### Secondary (MEDIUM confidence)
- EasyMDE GitHub: https://github.com/Ionaru/easy-markdown-editor -- CDN integration, feature comparison
- `.planning/research/ARCHITECTURE.md` -- architectural patterns for admin routes (`posts.py`), data flow diagrams
- `.planning/research/PITFALLS.md` -- review workflow pitfalls (Pitfall 7: no human-in-the-loop)
- `.planning/research/FEATURES.md` -- admin review feature requirements and dependencies

### Tertiary (LOW confidence)
- None -- all findings verified against code or official documentation

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - No new Python dependencies; existing patterns reused; `marked.js` is well-documented
- Architecture: HIGH - Extending existing FastAPI app with same patterns already proven in Phases 1-2
- Pitfalls: HIGH - Most pitfalls identified from direct code analysis (mount ordering, path mismatches) rather than speculation

**Research date:** 2026-03-03
**Valid until:** 2026-04-03 (stable -- no rapidly changing dependencies)
