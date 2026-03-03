# IAIFI Research Blog

## What This Is

An automated blog generator for IAIFI (Institute for AI and Fundamental Interactions) research papers. A local web app orchestrates a pipeline that fetches papers from the IAIFI website and arxiv, uses LLMs to generate accessible science blog posts with extracted figures, and publishes them to a static website. The site features an interactive force-directed concept network as its main navigation and a chronological timeline feed as an alternative view.

## Current State

Shipped v1.0 MVP (2026-03-03). Full pipeline operational:
- **Python pipeline** (2,793 LOC): IAIFI scraper, arXiv client, LLM blog generator, figure extractor, concept extractor, admin FastAPI server
- **Static site** (774 LOC): Astro 5.x with Tailwind CSS v4, timeline feed, blog post pages, Pagefind search, D3.js concept network
- **Tech stack**: Python (FastAPI, aiosqlite, LiteLLM, PyMuPDF, Pillow, BeautifulSoup4), Node.js (Astro, Tailwind, Pagefind, D3.js)
- **Database**: SQLite with papers, blog_posts, figures, concepts tables
- 554 IAIFI papers discoverable, full end-to-end pipeline from scraping to published static site

## Core Value

Every IAIFI paper gets a well-written, accessible blog post that connects it to the broader landscape of AI and fundamental physics research -- without requiring manual writing effort.

## Requirements

### Validated

- ✓ Fetch papers from IAIFI website master list -- v1.0
- ✓ Scan arxiv for IAIFI-affiliated papers and cross-reference against master list -- v1.0
- ✓ Admin-triggered paper discovery (not scheduled) -- v1.0
- ✓ LLM-generated blog posts from arxiv papers (~800-1500 words) -- v1.0
- ✓ Blog posts follow science blog style: broad overview, highlights, impact/implications -- v1.0
- ✓ Posts start accessible then get more technical (mixed audience) -- v1.0
- ✓ Auto-select 1-3 most informative/compelling figures from each paper -- v1.0
- ✓ Structured templates filled by LLM for consistency -- v1.0
- ✓ Categorize papers into IAIFI themes -- v1.0
- ✓ LLM-extracted concept tags for each paper -- v1.0
- ✓ Draft + human review workflow before publishing -- v1.0
- ✓ Local web app for admin: review drafts with inline images, approve/reject, trigger updates -- v1.0
- ✓ Flexible LLM backend (Claude, OpenAI, others) -- v1.0
- ✓ Static site output (deployable to GitHub Pages, Netlify, Vercel) -- v1.0
- ✓ Interactive force-directed concept network -- v1.0
- ✓ Chronological timeline feed with paper cards -- v1.0
- ✓ Individual blog post pages with full content and figures -- v1.0

### Active

(None -- v1.0 scope complete. See v2 candidates below.)

### v2 Candidates

- "Why this matters" contextual framing sections in blog posts
- Reading difficulty indicator badge per post
- Concept detail panels (click concept to see all related papers)
- Scheduled automatic paper fetching (cron-based)
- RSS feed for new blog posts
- Historical paper backfill (process full IAIFI archive)
- Visual theme clustering in concept network

### Out of Scope

- Mobile app -- web-first, responsive design sufficient
- Real-time/scheduled paper scanning -- admin triggers manually
- User accounts or commenting -- read-only public site
- Citation network visualization -- concept network uses LLM-extracted topics, not citation links
- Automated publishing without review -- always draft-first
- AI-generated figures -- scientifically inaccurate; use actual paper figures
- 3D force-directed graph -- harder to navigate, no information gain over 2D

## Context

IAIFI is a collaboration of scientists at Harvard, MIT, and Northeastern doing research at the intersection of AI and fundamental physics. They produce papers that span both domains. The blog needs to make this interdisciplinary work accessible to a general scientific audience -- people who are science-literate but not necessarily experts in either ML or physics.

## Constraints

- **LLM Access**: Blog generation requires LLM API access -- the admin must have API keys configured
- **Arxiv**: Paper content comes from arxiv (PDFs, abstracts, metadata) -- need to handle arxiv rate limits and PDF parsing
- **Static Output**: Final site must be static files -- no server-side rendering or database at runtime
- **Image Extraction**: Figures come from arxiv paper PDFs -- need reliable PDF figure extraction

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Template + LLM for blog generation | Consistency across posts while allowing narrative flexibility | ✓ Good -- three-pass journalist/reader/editor pattern |
| Static site for public output | Low maintenance, easy deployment, no server costs | ✓ Good -- Astro 5.x with Tailwind CSS v4 |
| Force-directed graph for concept network | Natural clustering by shared ideas, more discoverable than categories alone | ✓ Good -- D3.js with zoom/pan/drag/hover |
| LLM-extracted concepts (not predefined tags) | Concepts emerge from the papers themselves, no manual taxonomy maintenance | ✓ Good -- Pydantic structured extraction |
| Local web app for admin | Richer review experience with inline images, more accessible than CLI | ✓ Good -- FastAPI with vanilla JS |
| Admin-triggered (not scheduled) paper discovery | Control over when updates happen, avoids surprise publications | ✓ Good |
| LiteLLM for provider-agnostic LLM access | Single model string config switches between Claude, GPT, Ollama | ✓ Good -- easy provider switching |
| Sync sqlite3 for export script | Build-time script doesn't need async | ✓ Good -- simpler code |
| Tailwind CSS v4 via @tailwindcss/vite | Latest approach, deprecated @astrojs/tailwind avoided | ✓ Good |
| Pagefind for client-side search | No server needed, indexes at build time | ✓ Good |
| Individual D3 packages vs full bundle | Tree-shaking for smaller bundle size | ✓ Good |

---
*Last updated: 2026-03-03 after v1.0 milestone*
