# Project Research Summary

**Project:** IAIFI Automated Science Blog Generator
**Domain:** Academic paper processing + LLM content generation + static site publishing
**Researched:** 2026-03-03
**Confidence:** MEDIUM-HIGH

## Executive Summary

This project is an automated pipeline that transforms academic physics/AI papers from IAIFI (Institute for Artificial Intelligence and Fundamental Interactions) into accessible blog posts, published on a static site with a force-directed concept network as the primary discovery mechanism. The expert approach is a two-language architecture: Python handles paper ingestion, PDF processing, LLM orchestration, and admin workflows; Astro (with React islands) handles the static blog and interactive concept graph. The two halves communicate through the filesystem -- Python writes markdown and JSON, Astro reads them at build time. This separation exploits each language's strengths without introducing API coupling or shared runtime complexity.

The recommended approach is a staged pipeline with persistent state, where each paper moves through well-defined processing stages (discovered, metadata fetched, PDF downloaded, figures extracted, concepts extracted, post generated, reviewed, published). LiteLLM provides vendor-agnostic LLM access, PyMuPDF handles PDF processing, and the admin interface is a lightweight FastAPI app for local use. The concept network -- the project's key differentiator -- uses react-force-graph-2d for canvas-based rendering of papers as nodes and LLM-extracted shared concepts as edges. No existing tool combines LLM-generated accessible summaries, concept-based network visualization, and figure extraction from papers.

The dominant risk is reputational: LLM-generated science content can overgeneralize claims, hallucinate equations, and produce confidently wrong summaries. Research shows LLMs are nearly five times more likely to broaden scientific claims than human writers, and up to 73% of LLM-generated scientific summaries contain inaccuracies. Human review is not a nice-to-have -- it is a launch requirement. The admin review interface must make publishing physically impossible without explicit approval. Secondary risks include PDF figure extraction fragmentation (academic PDFs are not semantic documents), two-column layout text garbling, and concept network performance degradation at scale.

## Key Findings

### Recommended Stack

The stack splits cleanly across two languages. Python 3.12+ powers the pipeline: FastAPI for the admin API, LiteLLM for provider-agnostic LLM calls, PyMuPDF + pymupdf4llm for PDF-to-markdown conversion and figure extraction, arxiv.py for paper metadata, BeautifulSoup4 for IAIFI website scraping, and SQLite for pipeline state. Astro 5.x powers the static site: React 19 for interactive islands (concept graph), Tailwind CSS 4.x via the Vite plugin for styling, react-force-graph-2d for the force-directed visualization, and MDX for enhanced markdown rendering.

**Core technologies:**
- **LiteLLM:** Multi-provider LLM gateway -- eliminates vendor lock-in with a single `completion()` interface across 100+ providers
- **PyMuPDF + pymupdf4llm:** PDF processing -- fastest Python PDF library (0.12s extraction), purpose-built LLM-friendly markdown conversion
- **Astro 5.x:** Static site generation -- zero JS by default, first-class content collections, islands architecture for selective React hydration
- **react-force-graph-2d:** Concept network rendering -- canvas-based D3 wrapper handling zoom/pan/drag/hover, smooth at 200-500 nodes
- **FastAPI:** Admin web app -- async-first, auto-generated API docs, minimal overhead for a local-only interface
- **SQLite:** Pipeline state -- zero-config, ships with Python, perfect for single-user local app tracking paper processing status

### Expected Features

**Must have (table stakes):**
- Paper ingestion from IAIFI website + arXiv (the entire pipeline starts here)
- Single-pass LLM blog post generation (800-1500 words, jargon translation)
- Figure extraction from paper PDFs (visual content is critical for science posts)
- LLM concept extraction (5-15 concepts per paper, powers the network graph)
- Admin review/approval workflow (mandatory human gate before publishing)
- Static site with chronological timeline (standard blog navigation)
- Basic force-directed concept network (functional paper-concept graph)
- Paper metadata display (author, date, arXiv link, abstract)

**Should have (differentiators):**
- Multi-pass readability refinement (JRE-L pattern for measurably better accessibility)
- "Why this matters" contextual framing (Quanta Magazine-style significance)
- Concept detail panels (click a concept to see all related papers)
- Visual theme clustering in network (color-coded IAIFI research areas)
- Reading difficulty indicator (accessibility badge per post)
- Automated pipeline orchestration (one-click fetch-generate-queue flow)
- Search (client-side via Pagefind or Lunr.js)

**Defer (v2+):**
- Scheduled automatic fetching (cron-based new paper detection)
- RSS feed (only valuable once publishing cadence is established)
- Historical paper backfill (IAIFI's full 60+ paper archive)
- API for concept data (programmatic access to concept network)

### Architecture Approach

The architecture follows a pipeline-as-library pattern where the Python pipeline package is imported by the FastAPI admin app, not invoked via HTTP. Each pipeline stage (fetch, generate, extract figures, extract concepts) operates independently with SQLite tracking progress. Output is written as file artifacts: markdown posts go to `site/src/content/posts/`, figures to `site/public/figures/`, and concept network data to `site/src/data/graph.json`. The Astro site reads these at build time with zero runtime coupling.

**Major components:**
1. **Paper Fetcher** -- scrapes IAIFI paper listings, enriches via arXiv API, downloads PDFs
2. **LLM Generator** -- transforms paper metadata + abstract into blog-quality markdown via LiteLLM
3. **Figure Extractor** -- pulls figures from PDFs using PyMuPDF; LaTeX source extraction preferred
4. **Concept Extractor** -- extracts key scientific concepts for network graph edges via LLM + KeyBERT
5. **Pipeline Orchestrator** -- sequences stages, persists state to SQLite, handles retries and resume
6. **Admin Web App** -- FastAPI local UI for triggering discovery, reviewing/editing/approving posts
7. **Static Site** -- Astro with content collections, MDX posts, timeline feed, concept network island

### Critical Pitfalls

1. **LLM generalization bias** -- LLMs broaden and overgeneralize scientific claims in up to 73% of summaries. Avoid by using low temperature, enforcing hedging language preservation in prompts, requiring anchored quotes from the original paper, and implementing claim-strength comparison during review.

2. **PDF figure extraction fragmentation** -- PyMuPDF splits single figures into fragments, misses vector graphics entirely, and includes surrounding text. Avoid by extracting figures from LaTeX source files (arXiv tar.gz archives) as the primary path, with PDF extraction as fallback only.

3. **Two-column layout text garbling** -- PDF text extraction interleaves left and right column text from two-column academic layouts. Avoid by preferring LaTeX source parsing over PDF, and falling back to abstract + conclusion (single-column sections) as primary LLM input.

4. **No human review gate** -- automation bias leads to rubber-stamping LLM output. Avoid by making approval physically blocking, providing side-by-side source comparison, and requiring a structured review checklist.

5. **Concept network becomes unusable hairball** -- force-directed graphs degrade above 300-500 nodes in SVG. Avoid by using canvas rendering (react-force-graph-2d), pre-computing layouts at build time, showing focused subgraphs by default, and clustering by IAIFI theme.

## Implications for Roadmap

Based on research, suggested phase structure:

### Phase 1: Foundation -- Data Layer and Paper Ingestion
**Rationale:** Everything depends on reliably getting paper data. The IAIFI scraper, arXiv client, PDF downloader, and SQLite state tracking must work before any content generation is possible. Architecture research explicitly identifies this as the base of the dependency chain.
**Delivers:** Working paper discovery pipeline that scrapes IAIFI, enriches via arXiv, downloads PDFs, and persists state to SQLite. Data models (Pydantic) for papers, posts, and pipeline state.
**Addresses:** Paper ingestion, paper metadata display, IAIFI theme categorization
**Avoids:** arXiv rate limiting (3-second delays, exponential backoff), silent data loss from pagination ceiling, two-column text garbling (implement LaTeX source extraction path here)
**Stack:** Python 3.12+, arxiv.py, BeautifulSoup4, requests, SQLite, Pydantic, PyMuPDF/pymupdf4llm

### Phase 2: Content Generation -- LLM Pipeline and Figure Extraction
**Rationale:** With paper data available from Phase 1, the core value proposition can be built: turning papers into accessible blog posts. LLM generation and figure extraction are the two content-producing components that feed everything downstream. These can be developed in parallel.
**Delivers:** LLM-generated blog post drafts with extracted figures. Prompt templates for blog generation and concept extraction. Concept data as structured JSON.
**Addresses:** LLM blog post generation, figure extraction, LLM concept extraction
**Avoids:** LLM generalization bias (claim-fidelity checking in prompts), equation hallucination (no invented equations rule), figure fragmentation (LaTeX source extraction primary path)
**Stack:** LiteLLM, Jinja2 (prompt templates), PyMuPDF (figures), KeyBERT (concepts)

### Phase 3: Admin Review Interface
**Rationale:** Human review is a launch requirement, not a post-launch enhancement. The admin interface wraps the pipeline in a usable UI and ensures no content publishes without explicit approval. Must be built before the static site because it controls what content flows to the site.
**Delivers:** FastAPI local web app with paper listing, post review/edit/approve workflow, pipeline trigger, side-by-side source comparison for review.
**Addresses:** Admin review/approval workflow, pipeline monitoring
**Avoids:** No human review gate (mandatory approval), rubber-stamp reviews (structured checklist, side-by-side view)
**Stack:** FastAPI, Uvicorn, Jinja2 (HTML templates), vanilla JS frontend

### Phase 4: Static Site -- Blog Layout and Timeline
**Rationale:** With real generated and approved content available, the public-facing site can be built using actual data rather than mocks. Content collections, post rendering, and timeline navigation are standard Astro patterns with well-documented approaches.
**Delivers:** Working static blog with post pages, chronological timeline feed, IAIFI theme filtering, responsive design, paper metadata display on each post.
**Addresses:** Static site generation, chronological timeline feed, responsive design, paper metadata display
**Avoids:** Over-engineering (pure static HTML, no server runtime), deploying drafts (only approved content flows to site build)
**Stack:** Astro 5.x, Tailwind CSS 4.x, MDX, TypeScript

### Phase 5: Concept Network Visualization
**Rationale:** The concept network is the project's key differentiator but also its highest-complexity interactive component. It depends on quality concept data (Phase 2), the site shell (Phase 4), and enough published papers to make the graph meaningful. Building it last among core features allows the concept extraction quality to be validated first.
**Delivers:** Interactive force-directed graph with papers as nodes and shared concepts as edges. Canvas-based rendering. Zoom, pan, click-to-navigate. IAIFI theme color coding.
**Addresses:** Force-directed concept network, visual theme clustering, concept detail panels
**Avoids:** Network hairball (canvas rendering, focused subgraphs, pre-computed layouts), poor mobile experience (simplified static view on mobile)
**Stack:** React 19, react-force-graph-2d, D3.js (d3-force)

### Phase 6: Pipeline Orchestration and Quality Enhancement
**Rationale:** Only automate a pipeline that works. With all stages individually tested and validated through Phases 1-5, orchestration wires them into a one-click flow. Quality enhancements (multi-pass refinement, readability indicators) layer on top of proven generation.
**Delivers:** End-to-end pipeline orchestration, multi-pass readability refinement (JRE-L pattern), reading difficulty badges, "why this matters" sections, search.
**Addresses:** Automated pipeline orchestration, multi-pass readability, reading difficulty indicator, "why this matters" framing, search
**Avoids:** Automating a broken pipeline, style monotony (multiple prompt templates by paper type)
**Stack:** Pipeline state machine over SQLite, Pagefind/Lunr.js (search)

### Phase 7: Integration, Deployment, and Polish
**Rationale:** Final phase wires admin-to-pipeline-to-site-to-deploy into a seamless workflow. Adds deployment automation, RSS, and remaining polish.
**Delivers:** GitHub Pages deployment pipeline, cache invalidation, RSS feed, accessibility audit, performance optimization, documentation.
**Addresses:** Deployment workflow, RSS feed, remaining polish items
**Avoids:** CI/CD security issues (pinned dependencies, minimal permissions), cache staleness

### Phase Ordering Rationale

- **Phases 1-2 (Pipeline) must precede Phase 3 (Admin) and Phase 4 (Site)** because both the admin interface and the static site consume pipeline output. Building them first means the admin and site work with real data, not mocks.
- **Phase 3 (Admin) precedes Phase 4 (Site)** because the admin controls the content flow. The site should only render approved content, so the approval workflow must exist before the publishing workflow.
- **Phase 5 (Concept Network) is deliberately late** because its quality depends entirely on validated concept extraction data from Phase 2. Building it earlier risks building against bad data.
- **Phase 6 (Orchestration + Quality) follows all individual stages** because you cannot automate what does not work. The architecture research explicitly flags this: "Don't automate a pipeline that doesn't work."
- **Phases 2's sub-components (LLM generation, figure extraction, concept extraction) can be parallelized** since they all depend only on Phase 1 output.

### Research Flags

Phases likely needing deeper research during planning:
- **Phase 1 (Paper Ingestion):** LaTeX source extraction from arXiv tar.gz archives needs investigation -- the `.tex` parsing approach (resolving `\input{}` includes, finding `\includegraphics{}` references) requires specific research into arXiv source file conventions.
- **Phase 2 (Content Generation):** Prompt engineering for claim-fidelity and physics jargon translation is research-sensitive. The multi-pass JRE-L pattern needs validation against IAIFI-specific paper types. Concept extraction quality directly determines network quality.
- **Phase 5 (Concept Network):** Performance tuning at scale (pre-computed layouts, subgraph selection, mobile degradation) needs benchmarking with realistic IAIFI data volumes.

Phases with standard patterns (skip research-phase):
- **Phase 3 (Admin Interface):** Standard FastAPI CRUD app with Jinja2 templates. Well-documented patterns, no novel complexity.
- **Phase 4 (Static Site):** Standard Astro content site with content collections and MDX. Extensively documented in official Astro guides.
- **Phase 7 (Deployment):** Standard GitHub Pages or Netlify static site deployment. No novel complexity.

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | MEDIUM-HIGH | All technologies verified against official sources and current versions. Two-language split is well-justified. LiteLLM and react-force-graph-2d are less battle-tested than core tools but actively maintained. |
| Features | MEDIUM-HIGH | Feature landscape validated against competitor analysis (Connected Papers, Semantic Scholar, Quanta Magazine). MVP scope is well-defined. Concept extraction quality is the least predictable feature. |
| Architecture | HIGH | Pipeline-as-library, file-based integration, and Astro islands are proven patterns with official documentation. Build order is grounded in hard dependencies. |
| Pitfalls | MEDIUM-HIGH | Critical pitfalls backed by peer-reviewed research (Royal Society, CVPR 2025). LLM generalization bias and PDF extraction issues are well-documented. Recovery strategies are practical. |

**Overall confidence:** MEDIUM-HIGH

### Gaps to Address

- **LaTeX source parsing specifics:** The research recommends extracting figures and text from LaTeX source rather than PDFs, but the specific approach for parsing arXiv source archives (tar.gz structure, file conventions, handling `\input{}` includes) needs implementation-level research during Phase 1 planning.
- **Concept extraction quality baseline:** How good is LLM-based concept extraction for physics/AI papers? No benchmark exists for this specific task. Plan to evaluate extraction quality on 10-20 IAIFI papers early in Phase 2 before building the network visualization.
- **LLM cost projections:** LiteLLM supports cost tracking, but actual per-paper costs depend on prompt length, model choice, and multi-pass iteration count. Budget modeling should happen during Phase 2 planning once prompt templates are drafted.
- **IAIFI website scraping stability:** The scraper targets a specific HTML structure on iaifi.org/papers.html. If IAIFI redesigns their site, the scraper breaks. An adapter interface is recommended but the fallback strategy (direct arXiv queries by author affiliation) needs validation.
- **KeyBERT vs. pure LLM concept extraction:** Architecture recommends KeyBERT for embedding-based keyword extraction alongside LLM concept tagging. Whether both are needed, or LLM-only extraction suffices, should be determined empirically in Phase 2.

## Sources

### Primary (HIGH confidence)
- [Astro 5.x Documentation](https://docs.astro.build/) -- content collections, islands architecture, MDX support
- [Astro 2025 Year in Review](https://astro.build/blog/year-in-review-2025/) -- version at 5.16.6, release cadence
- [Tailwind CSS v4.2](https://tailwindcss.com/blog/tailwindcss-v4) -- Vite plugin approach, deprecated Astro integration
- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/) -- image extraction, figure handling, pymupdf4llm integration
- [arXiv API Docs](https://info.arxiv.org/help/api/basics.html) -- rate limits, endpoints, Terms of Use
- [arXiv Bulk Data Access](https://info.arxiv.org/help/bulk_data_s3.html) -- S3 bucket for historical data
- [FastAPI Documentation](https://fastapi.tiangolo.com/) -- async patterns, Pydantic integration
- [IAIFI Papers Page](https://iaifi.org/papers.html) -- verified HTML structure, paper listing format
- [D3-force Documentation](https://d3js.org/d3-force) -- force simulation parameters, performance characteristics
- [Generalization Bias in LLM Summarization -- Royal Society Open Science (2025)](https://royalsocietypublishing.org/doi/10.1098/rsos.241776) -- LLM claim broadening statistics

### Secondary (MEDIUM confidence)
- [LiteLLM GitHub](https://github.com/BerriAI/litellm) -- 100+ provider support, cost tracking
- [react-force-graph-2d npm](https://www.npmjs.com/package/react-force-graph-2d) -- version 1.29.1, canvas rendering
- [arxiv.py PyPI](https://pypi.org/project/arxiv/) -- version 2.4.0, Jan 2026 release
- [PDF Parsing Comparative Study (2024)](https://arxiv.org/html/2410.09871v1) -- extraction tool benchmarks
- [OmniDocBench CVPR 2025](https://github.com/opendatalab/OmniDocBench) -- PDF document parsing benchmarks
- [JRE-L Multi-LLM Science Journalism (2025)](https://arxiv.org/html/2501.16865) -- journalist-reader-editor framework
- [Papers-to-Posts (2024)](https://arxiv.org/html/2406.10370v1) -- multi-stage paper-to-blog conversion
- [Graph Visualization Efficiency (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12061801/) -- SVG vs Canvas vs WebGL benchmarks

### Tertiary (needs validation)
- [KeyBERT for concept extraction](https://jaketae.github.io/study/keyword-extraction/) -- needs empirical validation against pure LLM extraction for physics concepts
- [FastAPI adoption at 38%](https://www.programming-helper.com/tech/fastapi-2026-python-api-framework-ai-ml-adoption-enterprise) -- JetBrains survey statistic, secondary source

---
*Research completed: 2026-03-03*
*Ready for roadmap: yes*
