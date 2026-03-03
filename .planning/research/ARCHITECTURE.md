# Architecture Research

**Domain:** Automated science blog generation from academic papers
**Researched:** 2026-03-03
**Confidence:** HIGH

## System Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          LOCAL ADMIN WEB APP                                │
│  ┌──────────┐  ┌──────────────┐  ┌─────────────┐  ┌──────────────────┐    │
│  │ Discovery │  │ Post Review  │  │ Pipeline    │  │ Settings /       │    │
│  │ Trigger   │  │ & Edit       │  │ Monitor     │  │ LLM Config       │    │
│  └─────┬─────┘  └──────┬───────┘  └──────┬──────┘  └────────┬─────────┘    │
│        │               │                 │                   │              │
├────────┴───────────────┴─────────────────┴───────────────────┴──────────────┤
│                          PIPELINE ORCHESTRATOR                              │
│  ┌──────────┐  ┌────────────┐  ┌──────────────┐  ┌────────────────────┐    │
│  │  Paper   │  │  LLM       │  │  Figure      │  │  Concept           │    │
│  │  Fetcher │→ │  Generator │→ │  Extractor   │→ │  Extractor         │    │
│  └────┬─────┘  └─────┬──────┘  └──────┬───────┘  └────────┬───────────┘    │
│       │              │                │                    │               │
├───────┴──────────────┴────────────────┴────────────────────┴───────────────┤
│                            DATA LAYER                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐                  │
│  │  SQLite DB   │  │  Markdown    │  │  Extracted       │                  │
│  │  (metadata)  │  │  Posts       │  │  Assets          │                  │
│  └──────────────┘  └──────────────┘  └──────────────────┘                  │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                          STATIC SITE (Astro)                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐                  │
│  │  Blog Posts  │  │  Timeline    │  │  Concept Network  │                  │
│  │  (MDX)       │  │  Feed        │  │  (D3 Force Graph) │                  │
│  └──────────────┘  └──────────────┘  └──────────────────┘                  │
└────────────────────────────────────────────────────────────────────────────┘

External Services:
  ┌──────────┐   ┌──────────┐   ┌──────────┐
  │  IAIFI   │   │  arXiv   │   │  LLM API │
  │  Website │   │  API     │   │  (flex)  │
  └──────────┘   └──────────┘   └──────────┘
```

## Component Responsibilities

| Component | Responsibility | Typical Implementation |
|-----------|----------------|------------------------|
| **Paper Fetcher** | Scrape IAIFI paper listings, enrich via arXiv API, download PDFs | Python: requests + BeautifulSoup (IAIFI scrape), arxiv.py (metadata + PDF) |
| **LLM Generator** | Transform paper metadata + abstract into blog-quality markdown | Python: LiteLLM for provider-agnostic LLM calls, structured prompts with chain-of-thought |
| **Figure Extractor** | Pull figures and diagrams from paper PDFs as PNG/SVG assets | Python: PyMuPDF (fitz) for image extraction, pymupdf4llm for layout-aware extraction |
| **Concept Extractor** | Extract key concepts/topics from papers for network graph edges | Python: KeyBERT for embedding-based keyword extraction, LLM-assisted concept tagging |
| **Pipeline Orchestrator** | Sequence pipeline stages, track state, handle retries and errors | Python: simple state machine over SQLite, no heavy framework needed |
| **Admin Web App** | Local UI for triggering discovery, reviewing/editing posts, monitoring pipeline | Python: FastAPI backend + vanilla HTML/JS frontend (or lightweight Svelte) |
| **Data Layer** | Persist paper metadata, pipeline state, generated content, extracted assets | SQLite (metadata + state), filesystem (markdown posts, images) |
| **Static Site** | Public-facing blog with posts, timeline, concept network | Astro with content collections, MDX for posts, D3.js force-directed graph |

## Recommended Project Structure

```
blogger/
├── pipeline/                   # Python pipeline package
│   ├── __init__.py
│   ├── fetcher/                # Paper discovery and download
│   │   ├── __init__.py
│   │   ├── iaifi_scraper.py    # Scrape IAIFI papers page
│   │   ├── arxiv_client.py     # arXiv API wrapper
│   │   └── pdf_downloader.py   # Download and cache PDFs
│   ├── generator/              # LLM content generation
│   │   ├── __init__.py
│   │   ├── llm_client.py       # LiteLLM abstraction layer
│   │   ├── prompts/            # Prompt templates (Jinja2 or plain text)
│   │   │   ├── blog_post.txt
│   │   │   ├── summary.txt
│   │   │   └── concepts.txt
│   │   └── post_generator.py   # Orchestrate multi-step generation
│   ├── extractor/              # PDF and concept extraction
│   │   ├── __init__.py
│   │   ├── figure_extractor.py # PyMuPDF figure/image extraction
│   │   └── concept_extractor.py# KeyBERT + LLM concept tagging
│   ├── orchestrator.py         # Pipeline state machine
│   ├── models.py               # Data models (dataclasses or Pydantic)
│   └── config.py               # Configuration management
├── admin/                      # Local admin web application
│   ├── __init__.py
│   ├── app.py                  # FastAPI application
│   ├── routes/                 # API route handlers
│   │   ├── papers.py           # Paper discovery, listing
│   │   ├── posts.py            # Post review, edit, approve
│   │   ├── pipeline.py         # Pipeline trigger, status
│   │   └── settings.py         # LLM config, site settings
│   ├── static/                 # Admin frontend assets
│   │   ├── index.html
│   │   ├── app.js
│   │   └── style.css
│   └── templates/              # Jinja2 templates (if server-rendered)
├── site/                       # Astro static site
│   ├── astro.config.mjs
│   ├── src/
│   │   ├── content/
│   │   │   └── posts/          # Generated markdown blog posts
│   │   ├── content.config.ts   # Content collection schema
│   │   ├── components/
│   │   │   ├── ConceptNetwork.svelte  # D3 force graph (Svelte island)
│   │   │   ├── TimelineFeed.astro     # Timeline component
│   │   │   ├── PostCard.astro         # Post preview card
│   │   │   └── SearchBar.svelte       # Interactive search
│   │   ├── layouts/
│   │   │   ├── BaseLayout.astro
│   │   │   └── PostLayout.astro
│   │   ├── pages/
│   │   │   ├── index.astro            # Home / timeline feed
│   │   │   ├── network.astro          # Concept network page
│   │   │   ├── posts/
│   │   │   │   └── [...slug].astro    # Dynamic post pages
│   │   │   └── about.astro
│   │   └── data/
│   │       └── graph.json             # Concept network data
│   ├── public/
│   │   └── figures/                   # Extracted paper figures
│   └── package.json
├── data/                       # Local data directory (git-ignored)
│   ├── papers.db               # SQLite database
│   ├── pdfs/                   # Downloaded paper PDFs
│   └── cache/                  # LLM response cache
├── tests/
│   ├── test_fetcher.py
│   ├── test_generator.py
│   ├── test_extractor.py
│   └── test_pipeline.py
├── pyproject.toml              # Python project config
└── README.md
```

### Structure Rationale

- **pipeline/:** Isolated Python package for all data processing. No web framework dependencies. Testable independently. Each stage (fetcher, generator, extractor) is a separate subpackage with clear input/output contracts.
- **admin/:** Separate FastAPI application that imports pipeline as a library. Keeps admin UI concerns separate from processing logic. Runs locally only -- no auth complexity needed.
- **site/:** Completely decoupled Astro project. Consumes only the output of the pipeline (markdown files, images, graph JSON). Can be built and deployed independently. Uses Astro content collections for type-safe markdown handling.
- **data/:** Runtime data directory, git-ignored. SQLite for metadata and pipeline state. Filesystem for PDFs and cache. Simple, portable, no database server needed.

## Architectural Patterns

### Pattern 1: Pipeline-as-Library with Admin-as-Consumer

**What:** The pipeline is a standalone Python package that the admin web app imports and invokes. The pipeline knows nothing about HTTP or web UI. The admin knows nothing about how papers are fetched or posts are generated.

**When to use:** Always. This is the foundational separation.

**Trade-offs:** Slightly more initial setup than a monolithic script, but dramatically easier to test, modify, and extend each part independently.

**Example:**
```python
# pipeline/orchestrator.py
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class PaperStatus(Enum):
    DISCOVERED = "discovered"
    METADATA_FETCHED = "metadata_fetched"
    PDF_DOWNLOADED = "pdf_downloaded"
    FIGURES_EXTRACTED = "figures_extracted"
    CONCEPTS_EXTRACTED = "concepts_extracted"
    POST_GENERATED = "post_generated"
    POST_REVIEWED = "post_reviewed"
    PUBLISHED = "published"

@dataclass
class PipelineResult:
    paper_id: str
    status: PaperStatus
    error: Optional[str] = None

class PipelineOrchestrator:
    def __init__(self, db, llm_client, config):
        self.db = db
        self.llm_client = llm_client
        self.config = config

    async def process_paper(self, arxiv_id: str) -> PipelineResult:
        """Run full pipeline for a single paper."""
        paper = await self.fetch_metadata(arxiv_id)
        paper = await self.download_pdf(paper)
        figures = await self.extract_figures(paper)
        concepts = await self.extract_concepts(paper)
        post = await self.generate_post(paper, figures, concepts)
        return PipelineResult(paper_id=arxiv_id, status=PaperStatus.POST_GENERATED)
```

```python
# admin/routes/pipeline.py
from fastapi import APIRouter
from pipeline.orchestrator import PipelineOrchestrator

router = APIRouter()

@router.post("/api/pipeline/discover")
async def trigger_discovery():
    """Admin triggers paper discovery -- pipeline does the work."""
    orchestrator = get_orchestrator()
    new_papers = await orchestrator.discover_new_papers()
    return {"discovered": len(new_papers), "papers": new_papers}
```

### Pattern 2: Staged Pipeline with Persistent State

**What:** Each pipeline stage transitions a paper through a well-defined status. State is persisted to SQLite after each stage. If the pipeline crashes mid-run, it resumes from the last completed stage rather than starting over.

**When to use:** Always for the pipeline. LLM calls are expensive and slow. PDF downloads take time. Never redo work.

**Trade-offs:** Adds a state tracking layer, but the complexity is minimal with SQLite and the payoff is enormous -- especially during development when you are iterating on prompts.

**Example:**
```python
# pipeline/models.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Paper(BaseModel):
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str
    categories: list[str]
    published: datetime
    pdf_path: Optional[str] = None
    status: str = "discovered"
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

class GeneratedPost(BaseModel):
    paper_id: str
    title: str
    slug: str
    content: str           # Markdown body
    summary: str           # Short description
    concepts: list[str]    # Extracted concepts for graph
    figures: list[str]     # Paths to extracted figures
    status: str = "draft"  # draft -> reviewed -> published
```

### Pattern 3: LLM Provider Abstraction via LiteLLM

**What:** All LLM calls go through a single abstraction layer (LiteLLM) that normalizes the interface across providers. Configuration specifies which model to use. Switching from OpenAI to Anthropic to a local model requires only a config change.

**When to use:** Always. The project explicitly requires "flexible LLM backend."

**Trade-offs:** Adds a dependency (LiteLLM), but it is lightweight and actively maintained. The alternative -- hand-rolling provider switching -- is fragile and tedious.

**Example:**
```python
# pipeline/generator/llm_client.py
import litellm
from typing import Optional

class LLMClient:
    def __init__(self, model: str = "gpt-4o", temperature: float = 0.7):
        self.model = model
        self.temperature = temperature

    async def generate(self, system_prompt: str, user_prompt: str,
                       max_tokens: int = 4096) -> str:
        response = await litellm.acompletion(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=self.temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content

    async def generate_structured(self, system_prompt: str,
                                   user_prompt: str,
                                   response_format: dict) -> dict:
        """Generate with JSON structured output."""
        response = await litellm.acompletion(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format=response_format,
            temperature=self.temperature,
        )
        return json.loads(response.choices[0].message.content)
```

### Pattern 4: Astro Islands for Interactive Components

**What:** The static site is mostly pre-rendered HTML (fast, SEO-friendly). Interactive components like the concept network graph and search are hydrated as Astro islands using Svelte and D3.js. Only the interactive parts ship JavaScript.

**When to use:** For the concept network visualization and any interactive search/filter functionality. Blog post pages and the timeline should be fully static.

**Trade-offs:** Requires managing two mental models (static Astro templates and interactive Svelte components), but the performance benefit is significant and the concept network absolutely requires client-side JavaScript.

**Example:**
```astro
---
// site/src/pages/network.astro
import BaseLayout from '../layouts/BaseLayout.astro';
import ConceptNetwork from '../components/ConceptNetwork.svelte';
import graphData from '../data/graph.json';
---
<BaseLayout title="Concept Network">
  <h1>Research Concept Network</h1>
  <p>Papers as nodes, shared concepts as edges.</p>
  <!-- client:load hydrates immediately -- the graph IS the page -->
  <ConceptNetwork client:load data={graphData} />
</BaseLayout>
```

### Pattern 5: Generated Content as File Artifacts

**What:** The pipeline writes its output as files on disk (markdown posts in `site/src/content/posts/`, figures in `site/public/figures/`, graph data in `site/src/data/graph.json`). The Astro site reads these files at build time. There is no runtime API between pipeline and site.

**When to use:** Always. This is the key architectural boundary that keeps the pipeline and site fully decoupled.

**Trade-offs:** Requires a build step after pipeline runs. But this is desirable -- you want human review before publishing. The admin app triggers the pipeline, the human reviews in the admin, then the site is rebuilt.

## Data Flow

### Full Pipeline Data Flow

```
[Admin triggers "Discover Papers"]
    │
    ▼
[IAIFI Scraper] ──scrape──> iaifi.org/papers.html
    │                        iaifi.org/papers-ai.html
    │  HTML with arxiv IDs
    ▼
[arXiv Client] ──API call──> export.arxiv.org/api/query
    │  title, authors, abstract, categories, PDF URL
    ▼
[PDF Downloader] ──HTTP──> arxiv.org/pdf/{id}
    │  PDF file saved to data/pdfs/
    ▼
[Figure Extractor] ──PyMuPDF──> data/pdfs/{id}.pdf
    │  PNG images saved to site/public/figures/{id}/
    ▼
[Concept Extractor] ──KeyBERT + LLM──> abstract + title text
    │  concepts: ["neural networks", "lattice QCD", ...]
    ▼
[Post Generator] ──LiteLLM──> LLM API (configurable provider)
    │  Input: abstract, title, authors, concepts, figure refs
    │  Output: structured blog post markdown
    ▼
[Markdown Writer]
    │  Writes: site/src/content/posts/{slug}.md (with frontmatter)
    │  Updates: site/src/data/graph.json (concept network data)
    │  Updates: papers.db (status -> "post_generated")
    ▼
[Admin reviews post in web UI]
    │  Can edit markdown, approve/reject
    │  Status: "post_generated" -> "post_reviewed" -> "published"
    ▼
[Astro Build] ──npm run build──> site/dist/
    │  Static HTML, CSS, JS bundle
    ▼
[Deploy] ──rsync/gh-pages/netlify──> Public URL
```

### Concept Network Data Flow

```
[Paper A] ──concepts──> ["neural networks", "symmetry", "QCD"]
[Paper B] ──concepts──> ["neural networks", "optimization", "lattice"]
[Paper C] ──concepts──> ["symmetry", "lattice", "QCD"]

    ▼ (concept_extractor aggregates)

graph.json:
{
  "nodes": [
    {"id": "paper-a", "title": "...", "date": "...", "url": "/posts/paper-a"},
    {"id": "paper-b", "title": "...", "date": "...", "url": "/posts/paper-b"},
    {"id": "paper-c", "title": "...", "date": "...", "url": "/posts/paper-c"}
  ],
  "links": [
    {"source": "paper-a", "target": "paper-b", "concepts": ["neural networks"], "weight": 1},
    {"source": "paper-a", "target": "paper-c", "concepts": ["symmetry", "QCD"], "weight": 2},
    {"source": "paper-b", "target": "paper-c", "concepts": ["lattice"], "weight": 1}
  ],
  "concepts": [
    {"name": "neural networks", "count": 2},
    {"name": "symmetry", "count": 2},
    {"name": "QCD", "count": 2},
    {"name": "optimization", "count": 1},
    {"name": "lattice", "count": 2}
  ]
}
```

### Admin Web App Data Flow

```
[Browser] ──HTTP──> [FastAPI Admin App]
    │                      │
    │  GET /api/papers     │──> SQLite (paper listing + status)
    │  POST /api/discover  │──> Pipeline Orchestrator (trigger scrape)
    │  GET /api/posts/{id} │──> Filesystem (read markdown)
    │  PUT /api/posts/{id} │──> Filesystem (write markdown) + SQLite (update status)
    │  POST /api/publish   │──> Shell (astro build + deploy)
    │  GET /api/settings   │──> Config file / SQLite
    │                      │
    ▼                      ▼
[Admin HTML/JS UI]    [Pipeline + Data Layer]
```

### Key Data Flows Summary

1. **Paper Discovery:** IAIFI website -> scraper extracts arxiv IDs -> arXiv API enriches metadata -> SQLite stores paper records
2. **Content Generation:** Paper metadata + abstract -> LLM prompt chain -> structured markdown output -> filesystem
3. **Figure Extraction:** PDF binary -> PyMuPDF page analysis -> image files on disk -> referenced in markdown via relative paths
4. **Concept Network:** Paper abstracts + titles -> KeyBERT/LLM extraction -> aggregation into graph.json -> D3 renders at client
5. **Publishing:** Admin approval -> status change in SQLite -> Astro reads content collections + graph.json -> static build -> deploy

## Scaling Considerations

| Scale | Architecture Adjustments |
|-------|--------------------------|
| 0-200 papers (IAIFI current scale) | Current architecture is more than sufficient. SQLite handles this trivially. Single pipeline run processes all papers in minutes. D3 renders hundreds of nodes smoothly. |
| 200-1000 papers | Add pagination to the timeline feed. Consider chunking the concept network (filter by date range or category). LLM costs become meaningful -- add response caching aggressively. |
| 1000+ papers | Unlikely for a single institute blog. If reached: switch to incremental builds (Astro supports this). Consider WebGL rendering for the graph (vasturiano/3d-force-graph). Batch LLM calls. |

### Scaling Priorities

1. **First bottleneck: LLM API costs and latency.** Each paper requires 1-3 LLM calls (blog post generation, concept extraction, optional summary). At $0.01-0.10 per call, 200 papers costs $6-60. Cache aggressively. Never re-generate unless the prompt template changes.
2. **Second bottleneck: Concept network rendering.** D3 force-directed layouts handle ~1000 nodes well in 2D. Beyond that, performance degrades. For IAIFI's scale (80-90 AI papers + similar counts in physics categories), this is not a concern for years.

## Anti-Patterns

### Anti-Pattern 1: Monolithic Pipeline Script

**What people do:** Write a single Python script that scrapes, downloads, generates, extracts, and publishes in one long function.
**Why it's wrong:** Cannot resume after failure. Cannot test individual stages. Cannot inspect intermediate results. Cannot run stages independently (e.g., re-extract figures without re-generating posts).
**Do this instead:** Pipeline-as-library with discrete stages and persistent state. Each stage is independently callable and testable.

### Anti-Pattern 2: Database for Generated Content

**What people do:** Store generated blog posts in SQLite and have the static site generator read from the database at build time.
**Why it's wrong:** Adds unnecessary coupling. Markdown files are the natural input for Astro content collections. Version control works on files, not database rows. Editing posts becomes harder.
**Do this instead:** Pipeline writes markdown files with frontmatter to `site/src/content/posts/`. SQLite tracks metadata and pipeline state only. The markdown files are the source of truth for content.

### Anti-Pattern 3: Real-Time Site Generation

**What people do:** Build the pipeline to generate and deploy the site automatically after each paper is processed, with no human in the loop.
**Why it's wrong:** LLM output quality varies. Generated posts may contain hallucinations about the paper's findings, incorrect technical terminology, or awkward phrasing. Publishing without review damages credibility, especially for an academic institution.
**Do this instead:** Pipeline generates drafts. Admin reviews and edits. Publishing is an explicit human action.

### Anti-Pattern 4: Over-Engineering the Admin UI

**What people do:** Build a full SPA with React, Redux, authentication, and role-based access control for what is a local tool used by 1-3 people.
**Why it's wrong:** Massive time investment for zero user benefit. This runs on localhost. The "users" are the blog maintainers sitting at the machine.
**Do this instead:** FastAPI with server-rendered HTML templates (Jinja2), or at most a lightweight Svelte/vanilla JS frontend. No auth needed for localhost. Keep it functional, not pretty.

### Anti-Pattern 5: Tight Coupling Between Concept Extraction and Graph Rendering

**What people do:** Embed concept extraction logic into the D3 visualization component or vice versa.
**Why it's wrong:** Concept extraction is a Python/NLP task. Graph rendering is a browser/JavaScript task. Mixing them makes both harder to test and iterate on.
**Do this instead:** Concept extraction writes to `graph.json`. D3 reads `graph.json`. The JSON file is the contract between the two. Either side can change independently.

## Integration Points

### External Services

| Service | Integration Pattern | Notes |
|---------|---------------------|-------|
| **IAIFI Website** | HTTP scrape of papers.html / papers-ai.html with BeautifulSoup | Pages list papers with arxiv IDs in `[arXiv:XXXX.XXXXX]` format. Scrape periodically or on admin trigger. Respect robots.txt. Cache the scraped page. |
| **arXiv API** | REST API via `arxiv` Python package | Returns Atom XML. Rate limit: 1 request per 3 seconds minimum. Use `arxiv.Client(delay_seconds=3.0)`. Returns: title, authors, abstract, categories, PDF URL, publication date. |
| **arXiv PDF Download** | HTTP download of PDF binary | URL pattern: `https://arxiv.org/pdf/{id}`. Cache downloaded PDFs in `data/pdfs/`. Never re-download. |
| **LLM API (configurable)** | REST API via LiteLLM | Supports OpenAI, Anthropic, local models (Ollama), and 100+ others. Config specifies model string (e.g., `gpt-4o`, `claude-sonnet-4-20250514`, `ollama/llama3`). Response caching via hash of prompt + model. |

### Internal Boundaries

| Boundary | Communication | Notes |
|----------|---------------|-------|
| **Pipeline <-> Data Layer** | Direct Python function calls + SQLite queries | Pipeline imports data access functions. No HTTP between them. SQLite for metadata, filesystem for content. |
| **Admin <-> Pipeline** | Python import (admin imports pipeline as library) | Admin routes call pipeline orchestrator methods directly. No IPC, no message queue. Same Python process. |
| **Pipeline <-> Site** | Filesystem artifacts (markdown files, images, JSON) | Pipeline writes to `site/src/content/posts/`, `site/public/figures/`, `site/src/data/graph.json`. Astro reads at build time. Zero runtime coupling. |
| **Admin <-> Site** | Shell command (`astro build`) | Admin triggers build via subprocess. Could also trigger a deploy script. No API between them. |
| **Concept Extractor <-> Graph Viz** | `graph.json` file contract | Python writes JSON, D3/Svelte reads JSON. Schema is the contract. |

## Build Order (Dependency Chain)

The following order reflects hard dependencies between components:

```
Phase 1: Data Layer + Paper Fetcher
    │  (Must exist before anything else can work)
    │  SQLite schema, data models, IAIFI scraper, arXiv client
    ▼
Phase 2: LLM Abstraction + Post Generator
    │  (Depends on: paper metadata from Phase 1)
    │  LiteLLM client, prompt templates, markdown output
    ▼
Phase 3: Figure Extractor + Concept Extractor
    │  (Depends on: PDFs from Phase 1, feeds into posts from Phase 2)
    │  PyMuPDF extraction, KeyBERT concepts, graph.json generation
    ▼
Phase 4: Pipeline Orchestrator
    │  (Depends on: all pipeline stages from Phases 1-3)
    │  State machine, stage sequencing, error handling, resume logic
    ▼
Phase 5: Admin Web App
    │  (Depends on: pipeline orchestrator from Phase 4)
    │  FastAPI app, paper listing, post review/edit, pipeline trigger
    ▼
Phase 6: Static Site (Astro)
    │  (Depends on: content artifacts from pipeline output)
    │  Blog layout, post rendering, timeline feed
    ▼
Phase 7: Concept Network Visualization
    │  (Depends on: graph.json from Phase 3, site shell from Phase 6)
    │  D3 force graph in Svelte island, interactive features
    ▼
Phase 8: Integration + Polish
    (Wire admin -> pipeline -> site build -> deploy)
```

**Why this order:**
- Phases 1-3 are the "data pipeline" -- getting papers, generating content, extracting assets. Each phase produces artifacts the next needs.
- Phase 4 wires the pipeline stages together. Cannot be built until all stages exist.
- Phase 5 (admin) wraps the pipeline in a UI. Cannot be built until the pipeline works end-to-end.
- Phases 6-7 (site) consume pipeline output. Can technically be built in parallel with the pipeline using mock data, but it is more efficient to build after real content exists.
- Phase 8 is integration: making admin trigger pipeline, pipeline output flow to site, site build and deploy work end-to-end.

**Parallelization opportunity:** Phases 2 and 3 can be developed in parallel since they both depend only on Phase 1 output. Phase 6 can begin in parallel with Phase 5 if mock content is used.

## Sources

- [arXiv API Basics](https://info.arxiv.org/help/api/basics.html) -- API endpoints, Atom format, query parameters (MEDIUM confidence, official docs)
- [arxiv.py Python wrapper](https://github.com/lukasschwab/arxiv.py) -- Client configuration, rate limiting, generator pattern (MEDIUM confidence, official GitHub)
- [IAIFI Papers page](https://iaifi.org/papers.html) -- Paper listing structure with arxiv IDs (HIGH confidence, verified by fetch)
- [IAIFI Foundational AI Papers](https://iaifi.org/papers-ai.html) -- ~80-90 papers, consistent format (HIGH confidence, verified by fetch)
- [PyMuPDF4LLM](https://github.com/pymupdf/pymupdf4llm) -- Image extraction with write_images, dpi control (MEDIUM confidence, GitHub + docs)
- [PyMuPDF Image Recipes](https://pymupdf.readthedocs.io/en/latest/recipes-images.html) -- extract_image API (HIGH confidence, official docs)
- [D3 Force-Directed Graph](https://d3js.org/d3-force) -- Force simulation, velocity Verlet (HIGH confidence, official docs)
- [LiteLLM](https://github.com/BerriAI/litellm) -- 100+ provider support, OpenAI-compatible interface (MEDIUM confidence, GitHub + community)
- [Astro Islands Architecture](https://docs.astro.build/en/concepts/islands/) -- client:load/idle/visible directives (HIGH confidence, official docs)
- [Astro Content Collections](https://docs.astro.build/en/tutorial/6-islands/4/) -- Content Layer API, Zod schema, src/content.config.ts (HIGH confidence, official docs)
- [KeyBERT](https://jaketae.github.io/study/keyword-extraction/) -- BERT embedding-based keyword extraction (MEDIUM confidence, multiple sources)
- [FastAPI](https://fastapi.tiangolo.com/) -- Async, type hints, auto docs (HIGH confidence, official docs)

---
*Architecture research for: IAIFI Research Blog -- Automated Science Blog Generation*
*Researched: 2026-03-03*
