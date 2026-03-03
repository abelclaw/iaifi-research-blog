# Feature Research

**Domain:** Automated science blog generation from academic papers (research institute context)
**Researched:** 2026-03-03
**Confidence:** MEDIUM-HIGH

## Feature Landscape

### Table Stakes (Users Expect These)

Features that an admin or reader would assume exist. Missing these and the product feels broken or amateur.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| **Paper ingestion from IAIFI website + arXiv** | The entire pipeline starts here; without reliable paper fetching nothing works | MEDIUM | IAIFI lists papers at iaifi.org/papers.html with arXiv IDs, abstracts, authors, and category tags. The Python `arxiv` library provides a mature API wrapper. Must handle both scraping the IAIFI page for their curated list and fetching full metadata/PDFs from arXiv. |
| **LLM-generated blog post drafts** | Core value proposition -- turning papers into accessible prose | HIGH | Target 800-1500 words at mixed audience readability. Research shows multi-pass LLM approaches (journalist-reader-editor pattern from JRE-L) significantly improve accessibility. Single-pass generation produces text that reads fluently but scores poorly on actual comprehension. Must handle physics jargon translation. |
| **Figure extraction from papers** | Blog posts about scientific papers without figures feel hollow; figures carry critical information | MEDIUM | PDF figure extraction is a well-studied problem. Tools like PyMuPDF, pdfplumber, or dedicated libraries can extract embedded images. Multimodal LLMs (GPT-4o, Claude) can generate contextual captions. MLBCAP research shows multi-LLM captioning outperforms single-model approaches. |
| **Admin review/approval workflow** | LLM output requires human oversight before publication -- no responsible science communication tool publishes automatically | MEDIUM | Standard editorial states: Draft -> Review -> Approved -> Published. Admin must be able to edit generated text before publishing. This is a local web app so single-admin is fine; no need for multi-role permissions. |
| **Static site generation and publishing** | The output is a static website; this is the delivery mechanism | MEDIUM | Standard SSG pipeline (build markdown/data into HTML). Must support the two navigation modes (concept network + timeline). Incremental builds preferred so adding one post doesn't rebuild everything. |
| **Chronological timeline feed** | Standard blog navigation pattern; readers expect reverse-chronological browsing | LOW | Straightforward to implement. Each post has a date (paper publication date or blog generation date). Filter by IAIFI theme (Foundational AI, Theoretical Physics, Experimental Physics, Astrophysics). |
| **Paper metadata display** | Readers need to trace back to the original paper; authors, arXiv link, publication date, abstract | LOW | Already available from IAIFI website scraping + arXiv API. Display as structured header on each blog post. Link to original arXiv page. |
| **Responsive design** | Modern web users expect mobile-friendly layouts | LOW | Standard CSS/framework concern. The concept network needs special attention on mobile (touch interactions, small screens). |
| **IAIFI theme categorization** | Papers are organized by IAIFI themes; the blog should reflect this structure | LOW | IAIFI already categorizes into Foundational AI, Theoretical Physics, Experimental Physics, Astrophysics. Map these during ingestion. Allow filtering in both timeline and network views. |
| **Search** | With growing content, readers need to find specific topics or papers | LOW | Client-side search (Pagefind, Lunr.js) is sufficient for a static site with dozens to low hundreds of posts. Index on title, concepts, authors, abstract. |

### Differentiators (Competitive Advantage)

Features that make this project distinctive versus a generic "LLM summarizes paper" tool or a standard research blog.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| **Interactive force-directed concept network** | The defining navigation feature. Papers as nodes, LLM-extracted shared concepts as edges. Lets readers explore research connections visually rather than scrolling a list. No comparable research blog does this. | HIGH | D3.js force-directed graphs are the proven approach (d3-force module). Connected Papers uses a similar algorithm for bibliographic coupling. Key design decisions: node sizing (by citations? recency?), edge weighting (concept overlap strength), clustering (by IAIFI theme via color), click-to-navigate to blog post. Performance tested up to ~1000 nodes with D3. Must degrade gracefully on mobile. |
| **LLM-extracted concept tagging** | Powers the concept network. Goes beyond keyword extraction to identify substantive scientific concepts and methods shared across papers. | HIGH | Use structured LLM prompts to extract 5-15 concepts per paper (methods, phenomena, theoretical frameworks, techniques). Store as structured data. Concept overlap between papers creates network edges. Quality of concept extraction directly determines quality of the network -- this is the most research-sensitive feature. |
| **Multi-pass readability refinement** | Instead of single-shot generation, use iterative LLM passes (generate -> evaluate readability -> revise) to hit the mixed-audience accessibility target | MEDIUM | Research validates this approach: the JRE-L framework (Journalist-Reader-Editor LLM loop) produces measurably more accessible articles. Apply readability metrics (Flesch-Kincaid, Coleman-Liau) as automated quality gates between passes. Target grade level 10-12 for mixed audience. |
| **Concept detail panels** | Click a concept node in the network to see all papers involving that concept, with brief explanations | MEDIUM | Requires the concept extraction to produce not just labels but brief descriptions. Creates a secondary navigation path: concept-first rather than paper-first. Useful for readers who want to understand "what is IAIFI doing with normalizing flows?" |
| **Visual theme clustering in network** | Color-code and spatially cluster papers by IAIFI theme in the force-directed graph, making research areas visually apparent | LOW | Straightforward D3.js implementation once the network is built. Use force simulation groups to cluster by theme. Color palette should be accessible (colorblind-safe). |
| **"Why this matters" contextual framing** | Each blog post includes a short section explaining significance beyond the paper itself -- why should a non-specialist care? | MEDIUM | LLM prompt engineering challenge. Requires the model to contextualize within broader science, not just summarize. This is what separates a good science blog (Quanta Magazine style) from a dry summary. |
| **Automated pipeline orchestration** | One-click or scheduled: fetch new papers, generate drafts, queue for review. Admin doesn't manually trigger each step. | MEDIUM | Pipeline: scrape IAIFI -> identify new papers -> fetch arXiv data -> extract figures -> generate blog draft -> extract concepts -> queue for admin review. Should be idempotent (re-running doesn't duplicate). |
| **Reading difficulty indicator** | Show a simple difficulty badge (e.g., "Accessible / Intermediate / Advanced") on each post so readers self-select | LOW | Calculate from readability scores already computed during multi-pass refinement. Simple UI element with high information value for mixed audiences. |

### Anti-Features (Commonly Requested, Often Problematic)

Features that seem valuable but would add complexity without proportional benefit, or actively harm the project.

| Feature | Why Requested | Why Problematic | Alternative |
|---------|---------------|-----------------|-------------|
| **Fully automated publishing (no human review)** | "Automate everything end-to-end" | LLM-generated science content MUST be reviewed. Hallucinated claims, misrepresented results, or oversimplified physics could damage IAIFI's reputation. Research consistently shows LLM accuracy varies with content complexity. | Admin review queue with approve/edit/reject workflow. Make review fast, not optional. |
| **Multi-user CMS with role-based permissions** | "We need editors, writers, reviewers" | This is a local web app for a small team. Full CMS complexity (Strapi, Contentful-style) is massive overkill. Role-based workflows add auth, permissions, database complexity. | Single admin interface. If team grows, add basic auth later. Do not build a CMS. |
| **Real-time collaborative editing** | "Multiple people should edit drafts simultaneously" | Google Docs-level collaboration requires CRDT/OT algorithms, WebSocket infrastructure, conflict resolution. Enormous complexity for a tool where one admin reviews generated content. | Admin edits in a simple rich-text/markdown editor. If collaboration needed, share the draft externally (copy-paste to Google Docs). |
| **User accounts and personalization** | "Let readers create accounts, save favorites, get recommendations" | Adds authentication, database, privacy concerns (GDPR), session management. The blog is a public static site; user accounts break the static model entirely. | Bookmark via browser. RSS feed for updates. Concept network IS the discovery mechanism. |
| **Comment system** | "Readers should discuss papers" | Moderation burden, spam, static site incompatibility. Academic discussion happens on arXiv, Twitter/X, and in seminars, not blog comments. | Link to arXiv for discussion. Link to AlphaXiv if discussion platform is desired. |
| **AI-generated figures/diagrams** | "Generate custom illustrations for each post" | AI image generation (DALL-E, etc.) produces scientifically inaccurate diagrams. Physics figures require precision. Generated art looks generic and undermines credibility. | Extract actual figures from the paper PDF. These are the authoritative visuals the authors created. |
| **Multi-language support** | "Translate posts to other languages" | Massive scope increase. Translation quality for scientific content is unreliable. IAIFI's audience reads English. | English only. Defer indefinitely. |
| **PDF generation of blog posts** | "Let users download posts as PDFs" | The original paper IS a PDF. Why recreate one from the blog version? Adds print stylesheet complexity and a download pipeline. | Link directly to the arXiv PDF for the original paper. |
| **Social media auto-posting** | "Automatically tweet new blog posts" | API access to social platforms is increasingly restricted and paid. Auto-posting without review risks amplifying errors. Platform policies change frequently. | Generate a shareable summary card (OG meta tags) so manual sharing looks good. |
| **3D force-directed graph** | "Make the network visualization 3D for wow factor" | 3D graphs (three.js/WebGL) are harder to navigate, perform worse on mobile, and don't add information value for this use case. 2D is more readable. | 2D force-directed graph with zoom, pan, and hover. Proven usability pattern from Connected Papers. |

## Feature Dependencies

```
[Paper Ingestion (IAIFI + arXiv)]
    |
    +---> [LLM Blog Post Generation]
    |         |
    |         +---> [Multi-pass Readability Refinement]
    |         |         |
    |         |         +---> [Reading Difficulty Indicator]
    |         |
    |         +---> ["Why This Matters" Framing]
    |
    +---> [Figure Extraction from PDFs]
    |
    +---> [LLM Concept Extraction]
    |         |
    |         +---> [Concept Detail Panels]
    |         |
    |         +---> [Force-Directed Concept Network]
    |                   |
    |                   +---> [Visual Theme Clustering]
    |
    +---> [Paper Metadata Display]

[Admin Review Workflow]
    |
    +---> [Static Site Generation] ---> [Chronological Timeline Feed]
    |                              ---> [Force-Directed Concept Network]
    |                              ---> [Search]
    |
    +---> requires [LLM Blog Post Generation]
    +---> requires [Figure Extraction]
    +---> requires [Concept Extraction]

[Automated Pipeline Orchestration]
    |
    +---> orchestrates all of the above end-to-end
    +---> requires all upstream features to be individually working first
```

### Dependency Notes

- **Concept Network requires Concept Extraction:** The network visualization is only as good as the concept data feeding it. These must be developed in tandem, with concept extraction quality validated before building the network UI.
- **Admin Review requires all generation features:** The review interface must display the blog post, extracted figures, and extracted concepts together so the admin can approve or edit the complete package.
- **Pipeline Orchestration is last:** Don't automate a pipeline that doesn't work. Build each stage independently, test manually, then wire up orchestration.
- **Static Site Generation requires Admin approval flow:** Nothing gets published without going through review. The site build reads from approved content only.
- **Multi-pass refinement enhances but doesn't block Generation:** V1 can ship with single-pass generation. Multi-pass is an enhancement that measurably improves quality.

## MVP Definition

### Launch With (v1)

Minimum viable product -- prove the concept works end-to-end for a small batch of papers.

- [ ] **Paper ingestion from IAIFI website + arXiv** -- fetch metadata, PDFs, and abstracts for IAIFI papers
- [ ] **Single-pass LLM blog post generation** -- produce 800-1500 word accessible summaries with jargon translation
- [ ] **Figure extraction from paper PDFs** -- pull key figures with basic captions
- [ ] **LLM concept extraction** -- extract 5-15 concepts per paper as structured data
- [ ] **Admin review interface** -- view draft, edit text, approve/reject, view figures and concepts
- [ ] **Static site with chronological timeline** -- published posts in reverse-chronological order with theme filtering
- [ ] **Basic concept network** -- force-directed graph showing papers and concept connections (functional, not polished)
- [ ] **Paper metadata display** -- author, date, arXiv link, abstract on each post

### Add After Validation (v1.x)

Features to add once the core pipeline is validated with real IAIFI papers and admin feedback.

- [ ] **Multi-pass readability refinement** -- add when single-pass output quality is understood; implement JRE-L pattern
- [ ] **"Why this matters" framing sections** -- add after blog generation quality is baselined
- [ ] **Concept detail panels** -- add when concept extraction quality is validated and concepts are stable
- [ ] **Visual theme clustering** -- add after network is functional and has enough papers to cluster meaningfully
- [ ] **Reading difficulty indicator** -- add alongside multi-pass refinement (uses same readability metrics)
- [ ] **Automated pipeline orchestration** -- add after each stage has been run manually and debugged
- [ ] **Search** -- add after there are enough posts to need it (10+ posts)

### Future Consideration (v2+)

Features to defer until the product is proven useful and maintained.

- [ ] **Scheduled automatic fetching** -- cron/scheduled checks for new IAIFI papers (requires pipeline orchestration to be solid)
- [ ] **RSS feed** -- low effort but only valuable once there's regular publishing cadence
- [ ] **API for concept data** -- if others want to consume the concept network data programmatically
- [ ] **Historical paper backfill** -- process IAIFI's full paper archive (60+ papers) rather than just new ones

## Feature Prioritization Matrix

| Feature | User Value | Implementation Cost | Priority |
|---------|------------|---------------------|----------|
| Paper ingestion (IAIFI + arXiv) | HIGH | MEDIUM | P1 |
| LLM blog post generation | HIGH | HIGH | P1 |
| Figure extraction | HIGH | MEDIUM | P1 |
| Admin review workflow | HIGH | MEDIUM | P1 |
| Static site + timeline | HIGH | MEDIUM | P1 |
| LLM concept extraction | HIGH | HIGH | P1 |
| Force-directed concept network | HIGH | HIGH | P1 |
| Paper metadata display | MEDIUM | LOW | P1 |
| IAIFI theme categorization | MEDIUM | LOW | P1 |
| Responsive design | MEDIUM | LOW | P1 |
| Multi-pass readability refinement | HIGH | MEDIUM | P2 |
| "Why this matters" framing | HIGH | LOW | P2 |
| Concept detail panels | MEDIUM | MEDIUM | P2 |
| Visual theme clustering | MEDIUM | LOW | P2 |
| Reading difficulty indicator | MEDIUM | LOW | P2 |
| Pipeline orchestration | HIGH | MEDIUM | P2 |
| Search | MEDIUM | LOW | P2 |
| Scheduled fetching | MEDIUM | LOW | P3 |
| RSS feed | LOW | LOW | P3 |
| Historical backfill | MEDIUM | MEDIUM | P3 |

**Priority key:**
- P1: Must have for launch -- proves the concept end-to-end
- P2: Should have, add when core is validated
- P3: Nice to have, future consideration

## Competitor Feature Analysis

| Feature | Connected Papers | Semantic Scholar | AlphaXiv | Quanta Magazine | Our Approach |
|---------|-----------------|------------------|----------|-----------------|--------------|
| Paper discovery graph | Force-directed similarity graph (single paper seed) | Citation graph, related papers | Discussion threads on papers | None (editorial selection) | Force-directed concept network (all IAIFI papers, concept edges) |
| Content accessibility | None (shows raw papers) | AI-generated TLDRs (1-2 sentences) | User discussions | Professional journalist-written articles | LLM-generated 800-1500 word blog posts with readability refinement |
| Figure handling | None | None | None | Custom illustrations by artists | Extracted from original papers with LLM-generated captions |
| Concept extraction | Bibliographic coupling (implicit) | Topic/keyword tags | None | Editorial topic tagging | LLM-extracted substantive concepts (methods, phenomena, frameworks) |
| Navigation | Single-paper graph exploration | Search + recommendations | Chronological + trending | Category browsing + search | Dual: concept network + chronological timeline |
| Review workflow | N/A | N/A | Community moderation | Professional editorial team | Single admin review before publish |
| Audience | Researchers | Researchers | Researchers | General educated public | Mixed: researchers + science-interested public + IAIFI community |
| Scope | All of CS/physics/math | All academic papers | All arXiv papers | Curated stories across math/physics/CS/bio | IAIFI papers only (focused scope) |

### Key Competitive Insight

No existing tool combines all three of: (1) LLM-generated accessible summaries, (2) concept-based network visualization, and (3) figure extraction from papers. Connected Papers has the graph but no content generation. Semantic Scholar has TLDRs but no blog-length content or concept networks. Quanta Magazine has excellent accessibility but is manually produced and covers a broad scope. The IAIFI blog uniquely fills the niche of an automated, institute-scoped research blog with network-based discovery.

## Sources

- [Papers-to-Posts: LLM-Supported Planning, Drafting, and Revising of Research-Paper Blog Posts (arxiv.org)](https://arxiv.org/html/2406.10370v1) -- validated multi-stage approach to paper-to-blog conversion, user study findings on planning/drafting/revising
- [JRE-L: Journalist, Reader, and Editor LLMs for Science Journalism (arxiv.org)](https://arxiv.org/html/2501.16865) -- multi-LLM collaboration framework for accessible science writing, readability metrics
- [LLM-Collaboration on Automatic Science Journalism (arxiv.org)](https://arxiv.org/html/2407.09756v1) -- three-agent system for iterative readability improvement
- [Connected Papers](https://www.connectedpapers.com/) -- force-directed graph visualization of paper similarity, UX reference
- [Litmaps vs ResearchRabbit vs Connected Papers comparison (effortlessacademic.com)](https://effortlessacademic.com/litmaps-vs-researchrabbit-vs-connected-papers-the-best-literature-review-tool-in-2025/) -- graph visualization feature comparison
- [IAIFI Papers page (iaifi.org)](https://iaifi.org/papers.html) -- source data structure: titles, authors, arXiv IDs, abstracts, categories
- [IAIFI Homepage (iaifi.org)](https://iaifi.org/) -- current communication strategy and website structure
- [D3.js Force-Directed Graph (d3js.org)](https://d3js.org/d3-force) -- proven library for force-directed network visualization
- [MLBCAP: Multi-LLM Figure Captioning (emergentmind.com)](https://www.emergentmind.com/topics/multi-llm-collaborative-figure-caption-generation-mlbcap) -- state of art in scientific figure captioning
- [LLM Knowledge Graph Builder (Neo4j)](https://medium.com/neo4j/llm-knowledge-graph-builder-first-release-of-2025-532828c4ba76) -- LLM-based concept/entity extraction approaches
- [AlphaXiv (alphaxiv.org)](https://www.alphaxiv.org/) -- paper discussion platform, community approach to paper accessibility
- [Quanta Magazine (quantamagazine.org)](https://www.quantamagazine.org/) -- gold standard for accessible science communication design
- [9 Best AI Research Paper Summarizers 2026 (paperguide.ai)](https://paperguide.ai/blog/ai-research-paper-summarizers/) -- summarization tool feature landscape
- [Semantic Scholar](https://www.semanticscholar.org/) -- TLDR generation, paper metadata, citation graphs

---
*Feature research for: IAIFI Research Blog -- Automated Science Blog Generator*
*Researched: 2026-03-03*
