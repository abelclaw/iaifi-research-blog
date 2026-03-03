# Roadmap: IAIFI Research Blog

## Overview

This roadmap transforms IAIFI research papers into accessible blog posts through a five-phase pipeline. We start by building reliable paper ingestion from IAIFI and arxiv, then layer on LLM-powered content generation and concept extraction, add a human review interface to gate publication, build the public-facing static site with timeline navigation, and finish with the force-directed concept network -- the project's key differentiator. Each phase delivers a complete, verifiable capability that the next phase builds on.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Paper Ingestion Pipeline** - Fetch papers from IAIFI website and arxiv, download PDFs, persist state
- [ ] **Phase 2: Content Generation and Concept Extraction** - LLM-generated blog posts, figure extraction, and concept tagging
- [ ] **Phase 3: Admin Review Interface** - Local web app for reviewing, editing, and approving blog post drafts
- [ ] **Phase 4: Static Site and Timeline** - Public blog with post pages, chronological feed, filtering, and search
- [ ] **Phase 5: Concept Network Visualization** - Interactive force-directed graph connecting papers through shared concepts

## Phase Details

### Phase 1: Paper Ingestion Pipeline
**Goal**: Admin can discover IAIFI papers and the system reliably fetches their full metadata and PDFs
**Depends on**: Nothing (first phase)
**Requirements**: INGEST-01, INGEST-02, INGEST-03, INGEST-04
**Success Criteria** (what must be TRUE):
  1. Admin can trigger paper discovery from the local web app and see newly found papers listed
  2. System scrapes IAIFI website and returns paper entries with arxiv IDs, authors, and categories
  3. System fetches full metadata and downloads PDFs from arxiv for each discovered paper
  4. System identifies which papers are new by cross-referencing against previously ingested papers
**Plans**: 2 plans

Plans:
- [ ] 01-01-PLAN.md -- Pipeline core: project setup, data models, SQLite database, IAIFI scraper, arXiv client, discovery orchestrator
- [ ] 01-02-PLAN.md -- Admin layer: FastAPI app, discovery/papers API routes, admin HTML interface, end-to-end verification

### Phase 2: Content Generation and Concept Extraction
**Goal**: Every ingested paper gets a draft blog post with figures and concept tags ready for human review
**Depends on**: Phase 1
**Requirements**: GEN-01, GEN-02, GEN-03, GEN-04, GEN-05, GEN-06, CONCEPT-01, CONCEPT-02, CONCEPT-03
**Success Criteria** (what must be TRUE):
  1. System generates an 800-1500 word blog post for a paper that starts accessible and becomes more technical
  2. Generated posts follow a consistent template structure (overview, highlights, impact/implications)
  3. System extracts 1-3 figures from the paper PDF and associates them with the blog post
  4. System extracts 5-15 scientific concepts per paper and stores them as structured JSON
  5. LLM backend can be switched between providers (Claude, OpenAI, others) via configuration
**Plans**: TBD

Plans:
- [ ] 02-01: TBD
- [ ] 02-02: TBD
- [ ] 02-03: TBD

### Phase 3: Admin Review Interface
**Goal**: Admin can review, edit, and approve or reject generated blog posts before they reach the public site
**Depends on**: Phase 2
**Requirements**: ADMIN-01, ADMIN-02, ADMIN-03, ADMIN-04, ADMIN-05
**Success Criteria** (what must be TRUE):
  1. Admin can open the local web app and see a list of all draft blog posts awaiting review
  2. Admin can view a draft with extracted figures displayed inline alongside the blog text
  3. Admin can edit the generated blog text directly in the review interface
  4. Admin can approve or reject each draft, and only approved posts proceed to publication
  5. Admin can trigger the full pipeline (paper discovery through blog generation) from the interface
**Plans**: TBD

Plans:
- [ ] 03-01: TBD
- [ ] 03-02: TBD

### Phase 4: Static Site and Timeline
**Goal**: Approved blog posts are published to a static site with chronological navigation, filtering, and search
**Depends on**: Phase 3
**Requirements**: SITE-01, SITE-03, SITE-04, SITE-05, SITE-06, SITE-07, SITE-08
**Success Criteria** (what must be TRUE):
  1. Running the site build produces static files deployable to GitHub Pages, Netlify, or Vercel
  2. Visitor can browse a chronological timeline feed of paper cards and filter by IAIFI theme
  3. Visitor can click a paper card to read the full blog post with figures and paper metadata (authors, arxiv link, date, abstract)
  4. Visitor can search across posts by title, concepts, or authors and get relevant results
  5. Site is responsive and usable on mobile devices
**Plans**: TBD

Plans:
- [ ] 04-01: TBD
- [ ] 04-02: TBD
- [ ] 04-03: TBD

### Phase 5: Concept Network Visualization
**Goal**: Visitors can explore the research landscape through an interactive force-directed graph that reveals connections between papers
**Depends on**: Phase 4
**Requirements**: SITE-02
**Success Criteria** (what must be TRUE):
  1. Visitor sees an interactive force-directed graph where papers appear as nodes and shared concepts form edges
  2. Papers with more shared concepts cluster together naturally in the graph
  3. Visitor can click a paper node to navigate to its blog post page
  4. Graph renders smoothly with zoom, pan, and hover interactions
**Plans**: TBD

Plans:
- [ ] 05-01: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4 -> 5

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Paper Ingestion Pipeline | 1/2 | In Progress | - |
| 2. Content Generation and Concept Extraction | 0/3 | Not started | - |
| 3. Admin Review Interface | 0/2 | Not started | - |
| 4. Static Site and Timeline | 0/3 | Not started | - |
| 5. Concept Network Visualization | 0/1 | Not started | - |
