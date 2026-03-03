# Stack Research

**Domain:** Automated science blog generator (academic paper processing + LLM content creation + static site publishing)
**Researched:** 2026-03-03
**Confidence:** MEDIUM-HIGH

## Architecture Decision: Two-Language Split

This project has two distinct halves that map naturally to different languages:

1. **Pipeline backend (Python)** -- Paper fetching, PDF processing, LLM orchestration, admin API. Python dominates the academic/ML/PDF ecosystem. Fighting this with Node.js would mean inferior libraries for every critical task.

2. **Static site output (Astro + React)** -- Blog rendering, force-directed graph, content collections. Astro is purpose-built for content-heavy static sites with islands of interactivity.

The two halves communicate through the filesystem: Python writes markdown files + JSON data into the Astro content directory. Astro builds them into static HTML. This is the simplest possible integration -- no API coupling, no shared runtime.

---

## Recommended Stack

### Pipeline Backend (Python)

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Python | 3.12+ | Runtime | Current stable. Required by FastAPI and modern async patterns. Type hints mature. |
| FastAPI | 0.115+ | Admin web app / API server | 38% Python dev adoption (JetBrains 2025). Auto-generates Swagger docs. Async-first. Used for the local review/approval UI and pipeline orchestration API. |
| Uvicorn | 0.34+ | ASGI server | Standard FastAPI companion. `fastapi dev` wraps it with auto-reload for local development. |
| LiteLLM | 1.82+ | Multi-provider LLM gateway | Unified interface to Claude, OpenAI, Gemini, DeepSeek, and 100+ providers. One API call, swap models by changing a string. Includes cost tracking. Eliminates vendor lock-in. |
| PyMuPDF | 1.27+ | PDF processing and figure extraction | Fastest Python PDF library (benchmarked at 0.12s extraction). Handles both embedded images (`get_images()`) and vector graphics (`cluster_drawings()`). Critical for extracting figures from arxiv PDFs. |
| pymupdf4llm | 0.0.17+ | PDF-to-markdown conversion | Converts academic PDFs to LLM-friendly markdown. Preserves headers, tables, reading order. Extracts images as referenced files. Built on PyMuPDF. Purpose-built for our exact use case. |
| arxiv.py | 2.4+ | ArXiv paper fetching | Official Python wrapper for arXiv API. Handles search, metadata retrieval, and PDF download. Actively maintained (Jan 2026 release). |
| BeautifulSoup4 | 4.12+ | IAIFI website scraping | The IAIFI papers page is static HTML with no API. BS4 + requests is the standard approach for scraping structured HTML listings. Simple, proven, well-documented. |
| requests | 2.32+ | HTTP client | Standard Python HTTP library for fetching IAIFI pages and downloading PDFs. |
| SQLite | (stdlib) | Pipeline state database | Tracks paper processing status, draft metadata, approval state. Zero-config, ships with Python, perfect for single-user local app. No need for PostgreSQL complexity. |
| Pydantic | 2.10+ | Data validation / schemas | Bundled with FastAPI. Define paper metadata, blog post, and pipeline state schemas with type safety. |
| Jinja2 | 3.1+ | Markdown template rendering | Generate blog post markdown from LLM output using templates. Standard Python templating. FastAPI uses it for HTML templates too. |

### Static Site (JavaScript/TypeScript)

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Astro | 5.x (stable) | Static site generator | Ships zero JS by default. Content collections natively handle markdown/MDX. Islands architecture for selective interactivity (force graph). 2-3x faster than Next.js for content sites. 113 releases in 2025 -- actively maintained. |
| React | 19+ | Interactive islands | Used ONLY for the force-directed graph and any interactive components. Astro hydrates React islands on demand -- rest of site is pure HTML. |
| Tailwind CSS | 4.2+ | Styling | New v4 engine: 5x faster builds, 100x faster incremental. Use via `@tailwindcss/vite` plugin (NOT deprecated `@astrojs/tailwind`). |
| react-force-graph-2d | 1.29+ | Force-directed concept network | Purpose-built React wrapper around d3-force + canvas rendering. Handles zoom/pan/drag/hover/click. Canvas-based so performs well at 200-500 nodes. Actively maintained (monthly releases). |
| D3.js (d3-force) | 7.x | Physics simulation engine | Underlying force simulation for the concept graph. Used indirectly through react-force-graph-2d. May also use directly for custom force behaviors. |
| MDX | 3.x | Enhanced markdown | Allows embedding React components in blog posts (interactive figures, concept links). Astro has first-class MDX support via `@astrojs/mdx`. |
| TypeScript | 5.7+ | Type safety | Astro has native TypeScript support. Content collection schemas generate types automatically. |

### Development Tools

| Tool | Purpose | Notes |
|------|---------|-------|
| uv | Python package manager | Faster than pip. Modern resolver. Handles virtual environments. Replaces pip + venv + pip-tools. |
| npm | Node.js package manager | Standard for Astro ecosystem. |
| Ruff | Python linter + formatter | Replaces flake8 + black + isort. 10-100x faster. Single tool. |
| ESLint + Prettier | JS/TS linting + formatting | Standard Astro/React tooling. |

---

## Installation

```bash
# --- Python Pipeline ---
# Create virtual environment
uv venv
source .venv/bin/activate

# Core pipeline
uv pip install fastapi uvicorn[standard] litellm pymupdf pymupdf4llm arxiv beautifulsoup4 requests pydantic jinja2

# Dev dependencies
uv pip install ruff pytest httpx

# --- Static Site ---
# Create Astro project
npm create astro@latest site -- --template minimal

# Core site dependencies
cd site && npm install react react-dom @astrojs/react @astrojs/mdx react-force-graph-2d

# Tailwind v4 (via Vite plugin, NOT @astrojs/tailwind)
npm install @tailwindcss/vite tailwindcss

# Dev dependencies
npm install -D typescript @types/react @types/react-dom eslint prettier
```

---

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| Astro (static site) | Next.js | If you need SSR, user auth, or dynamic server features. Overkill for a blog that rebuilds on publish. |
| Astro (static site) | Hugo / 11ty | If you want zero JavaScript anywhere. But we need React for the interactive force graph, so Astro's islands architecture is the sweet spot. |
| LiteLLM (LLM gateway) | Direct SDK per provider | If you commit to a single LLM provider permanently. LiteLLM adds trivial overhead but massive flexibility. |
| LiteLLM (LLM gateway) | LangChain | If you need complex agent chains, RAG pipelines, or memory. Massive overkill for "send prompt, get blog post." LangChain adds complexity without value here. |
| PyMuPDF + pymupdf4llm | pdfplumber | If you primarily need table extraction. pdfplumber is slightly better at tables but slower overall and worse at figure/image extraction. |
| PyMuPDF + pymupdf4llm | Marker / Nougat | If you need ML-based PDF understanding for very complex layouts. Heavier dependencies (torch), slower, but handles edge cases better. Consider as a fallback. |
| react-force-graph-2d | Raw D3.js | If you need pixel-perfect custom rendering. But react-force-graph-2d wraps D3 with React bindings, saving weeks of integration work. |
| react-force-graph-2d | vis-network / Cytoscape.js | If you need advanced graph analysis (shortest path, centrality). We need visualization, not graph algorithms. react-force-graph is more focused. |
| SQLite | PostgreSQL | If multiple users access the admin simultaneously. SQLite is single-writer. For a local admin app used by one person, SQLite is perfect. |
| FastAPI | Flask | If simplicity matters more than performance. But FastAPI is equally simple for basic apps and adds async + auto-docs + type validation for free. |
| BeautifulSoup4 | Scrapy | If you need to crawl hundreds of pages with rate limiting, retries, and pipelines. We scrape ONE page (IAIFI papers list). BS4 + requests is sufficient. |

---

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| LangChain | Massive abstraction layer. Adds complexity, dependency churn, and debugging difficulty for what amounts to "call LLM API with a prompt." Our use case is simple prompt engineering, not agent chains. | LiteLLM for multi-provider support + direct prompt templates |
| @astrojs/tailwind (integration) | Deprecated for Tailwind v4. Will cause confusion and version conflicts. | @tailwindcss/vite plugin directly |
| Puppeteer/Playwright for PDF | Headless browser is wildly overkill for extracting figures from academic PDFs. Slow, memory-hungry, fragile. | PyMuPDF for direct PDF manipulation |
| Next.js for the blog | Requires a Node.js runtime or complex export config for static output. Ships unnecessary JS. Content collections are less mature than Astro's. | Astro -- purpose-built for content-heavy static sites |
| MongoDB / PostgreSQL | Unnecessary operational complexity for a local admin app with one user. Connection management, migrations, service management -- all overhead with zero benefit. | SQLite -- zero-config, file-based, ships with Python |
| pdf2image / poppler | Requires system-level poppler installation. Fragile across OS versions. Only converts pages to images, doesn't extract embedded figures. | PyMuPDF -- pure Python (compiled C), handles all PDF operations |
| ChatGPT web interface (manual) | Defeats the purpose of automation. No API access, no reproducibility, no pipeline integration. | LiteLLM + any model API |

---

## Stack Patterns by Variant

**If deploying to GitHub Pages (most likely):**
- Astro static export to `dist/` directory
- GitHub Actions to build and deploy on push to main
- Python pipeline runs locally, commits generated content to repo

**If deploying to Vercel/Netlify:**
- Same Astro static export
- Auto-deploys on push
- Slightly easier setup but same architecture

**If the concept graph exceeds 500 nodes:**
- Switch from react-force-graph-2d (canvas) to a WebGL renderer
- Pre-compute layout in a web worker or at build time
- Consider 3d-force-graph for WebGL rendering with Three.js
- Or use force-graph (vanilla JS) directly with PixiJS for WebGL

**If IAIFI changes their website structure:**
- The scraper is the most fragile component
- Isolate scraping logic behind an adapter interface
- Consider also pulling directly from arxiv API using author affiliation queries as a fallback

---

## Version Compatibility

| Package A | Compatible With | Notes |
|-----------|-----------------|-------|
| Astro 5.x | React 19, Tailwind 4.x | Astro 5.2+ required for Tailwind v4 Vite plugin support |
| Astro 5.x | @astrojs/mdx 4.x | Must match Astro major version |
| react-force-graph-2d 1.29+ | React 18/19 | Works with both; React 19 preferred |
| FastAPI 0.115+ | Pydantic 2.x | FastAPI migrated to Pydantic v2. Do NOT use Pydantic v1. |
| PyMuPDF 1.27+ | pymupdf4llm 0.0.17+ | pymupdf4llm depends on PyMuPDF. Install pymupdf4llm and it pulls the correct PyMuPDF. |
| LiteLLM 1.82+ | anthropic SDK, openai SDK | LiteLLM manages provider SDKs. Install litellm and use its interface rather than importing SDKs directly. |
| Tailwind 4.2+ | @tailwindcss/vite 4.x | Must use Vite plugin, not the deprecated Astro integration |
| Python 3.12+ | All Python packages listed | Python 3.12 is the baseline. 3.13 works but 3.12 has broader library testing. |

---

## Key Technical Decisions Explained

### Why a Two-Repo / Two-Language Architecture

The pipeline and the site serve fundamentally different purposes:
- The pipeline runs **locally, on-demand, by an admin** -- it processes papers, calls LLMs, and generates content
- The site is a **static build artifact** deployed to a CDN -- it renders pre-generated content

Python is objectively the better language for PDF processing, web scraping, and LLM API integration. JavaScript/Astro is objectively the better tool for building a fast, content-driven static site with interactive islands. Forcing everything into one language would mean using suboptimal tools for half the project.

The filesystem is the integration point: Python writes `.md` files + `graph-data.json` into the Astro content directory. Astro reads them at build time. No API coupling, no shared runtime, no deployment coordination beyond "commit and push."

### Why Astro Over Next.js

For a static blog with one interactive widget (the force graph), Astro is the clear choice:
- Zero JS by default (Next.js ships React runtime to every page)
- Content collections are a first-class feature, not an afterthought
- Islands architecture means the force graph loads independently
- Build output is pure static HTML + CSS + minimal JS for islands
- 50-80% less hosting cost than SSR-capable frameworks
- Simpler deployment (just static files, no Node.js runtime needed)

### Why LiteLLM Over Direct SDKs

The project requirements specify "flexible LLM backend (Claude, OpenAI, others)." LiteLLM delivers this with one line of code change. Without it, you'd need to maintain separate API integration code for each provider, handle different response formats, and manage multiple SDK dependencies. LiteLLM normalizes all of this behind a single `completion()` call.

### Why react-force-graph-2d Over Raw D3

Building a production-quality interactive force-directed graph from scratch with D3 takes 2-4 weeks of work: zoom/pan, node dragging, hover interactions, click handling, responsive sizing, performance optimization. react-force-graph-2d provides all of this out of the box as a React component, which Astro can hydrate as an island. The library uses canvas rendering (not SVG), so it handles 200-500 concept nodes smoothly.

---

## Sources

- [Astro 2025 Year in Review](https://astro.build/blog/year-in-review-2025/) -- Verified Astro version at 5.16.6, v6 in beta (HIGH confidence)
- [Astro Content Collections Docs](https://docs.astro.build/en/guides/content-collections/) -- Verified glob/file loaders, MDX support (HIGH confidence)
- [Astro Islands Architecture](https://docs.astro.build/en/concepts/islands/) -- Verified React island hydration approach (HIGH confidence)
- [Tailwind CSS v4.2.0](https://tailwindcss.com/blog/tailwindcss-v4) -- Verified v4 Vite plugin approach, deprecated Astro integration (HIGH confidence)
- [PyMuPDF on PyPI](https://pypi.org/project/PyMuPDF/) -- Version 1.27.1 confirmed (HIGH confidence)
- [PyMuPDF4LLM Docs](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/) -- Verified markdown extraction + image handling (HIGH confidence)
- [PDF Extractor Benchmarks 2025](https://onlyoneaman.medium.com/i-tested-7-python-pdf-extractors-so-you-dont-have-to-2025-edition-c88013922257) -- PyMuPDF speed benchmarks (MEDIUM confidence)
- [arxiv.py on PyPI](https://pypi.org/project/arxiv/) -- Version 2.4.0 confirmed, Jan 2026 release (HIGH confidence)
- [LiteLLM on GitHub](https://github.com/BerriAI/litellm) -- Version 1.82+, 100+ provider support confirmed (HIGH confidence)
- [react-force-graph-2d on npm](https://www.npmjs.com/package/react-force-graph-2d) -- Version 1.29.1 confirmed (HIGH confidence)
- [D3-force Performance Discussion](https://github.com/d3/d3/issues/1936) -- Canvas handles 500-2000 nodes (MEDIUM confidence)
- [FastAPI adoption stats](https://www.programming-helper.com/tech/fastapi-2026-python-api-framework-ai-ml-adoption-enterprise) -- 38% adoption from JetBrains survey (MEDIUM confidence)
- [IAIFI Papers Page](https://iaifi.org/papers.html) -- Verified static HTML structure, scraping approach (HIGH confidence)
- [Astro vs Next.js comparison](https://senorit.de/en/blog/astro-vs-nextjs-2025) -- Performance benchmarks for content sites (MEDIUM confidence)

---
*Stack research for: IAIFI Automated Science Blog Generator*
*Researched: 2026-03-03*
