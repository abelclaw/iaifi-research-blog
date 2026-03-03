# IAIFI Research Blog

## What This Is

An automated blog generator for IAIFI (Institute for AI and Fundamental Interactions) research papers. A local web app orchestrates a pipeline that fetches papers from the IAIFI website and arxiv, uses LLMs to generate accessible science blog posts with extracted figures, and publishes them to a static website. The site features an interactive force-directed concept network as its main navigation and a chronological timeline feed as an alternative view.

## Core Value

Every IAIFI paper gets a well-written, accessible blog post that connects it to the broader landscape of AI and fundamental physics research — without requiring manual writing effort.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Fetch papers from IAIFI website master list
- [ ] Scan arxiv for IAIFI-affiliated papers and cross-reference against master list
- [ ] Admin-triggered paper discovery (not scheduled — run when admin wants)
- [ ] LLM-generated blog posts from arxiv papers (~800-1500 words)
- [ ] Blog posts follow science blog style: broad overview, highlights, impact/implications
- [ ] Posts start accessible then get more technical (mixed audience)
- [ ] Auto-select 1-3 most informative/compelling figures from each paper
- [ ] Structured templates filled by LLM for consistency
- [ ] Categorize papers into IAIFI themes (interdisciplinary research, AI impact, fundamental physics impact)
- [ ] LLM-extracted concept tags for each paper
- [ ] Draft + human review workflow before publishing
- [ ] Local web app for admin: review drafts with inline images, approve/reject, trigger updates
- [ ] Flexible LLM backend (Claude, OpenAI, others)
- [ ] Static site output (deployable to GitHub Pages, Netlify, Vercel, etc.)
- [ ] Interactive force-directed concept network: papers as nodes, shared concepts as edges, clusters form naturally
- [ ] Chronological timeline feed as alternative view with paper cards
- [ ] Individual blog post pages with full content and figures

### Out of Scope

- Mobile app — web-first, responsive design sufficient
- Real-time/scheduled paper scanning — admin triggers manually
- User accounts or commenting — read-only public site
- Citation network visualization — concept network uses LLM-extracted topics, not citation links
- Automated publishing without review — always draft-first

## Context

IAIFI is a collaboration of scientists at Harvard, MIT, and Northeastern doing research at the intersection of AI and fundamental physics. They produce papers that span both domains. The blog needs to make this interdisciplinary work accessible to a general scientific audience — people who are science-literate but not necessarily experts in either ML or physics.

The poster image shared shows the kind of categories/framing IAIFI uses: "Interdisciplinary Research Achievement," "Impact on Artificial Intelligence," "Impact on Fundamental Interactions." Blog posts should capture this spirit in a narrative science blog format, not a structured poster layout.

"Abel" is the user's AI bot that handles LLM operations. The local web app needs to work with Abel's flexible LLM backend setup.

## Constraints

- **LLM Access**: Blog generation requires LLM API access — the admin running the local app must have API keys configured
- **Arxiv**: Paper content comes from arxiv (PDFs, abstracts, metadata) — need to handle arxiv rate limits and PDF parsing
- **Static Output**: Final site must be static files — no server-side rendering or database at runtime
- **Image Extraction**: Figures come from arxiv paper PDFs — need reliable PDF figure extraction

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Template + LLM for blog generation | Consistency across posts while allowing narrative flexibility | — Pending |
| Static site for public output | Low maintenance, easy deployment, no server costs | — Pending |
| Force-directed graph for concept network | Natural clustering by shared ideas, more discoverable than categories alone | — Pending |
| LLM-extracted concepts (not predefined tags) | Concepts emerge from the papers themselves, no manual taxonomy maintenance | — Pending |
| Local web app for admin | Richer review experience with inline images, more accessible than CLI | — Pending |
| Admin-triggered (not scheduled) paper discovery | Control over when updates happen, avoids surprise publications | — Pending |

---
*Last updated: 2026-03-03 after initialization*
