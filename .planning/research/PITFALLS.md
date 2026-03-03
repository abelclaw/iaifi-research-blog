# Pitfalls Research

**Domain:** Automated science blog generation from academic papers (physics/AI)
**Researched:** 2026-03-03
**Confidence:** MEDIUM-HIGH (multiple web sources corroborated; domain-specific experience from published research)

## Critical Pitfalls

### Pitfall 1: LLM Generalization Bias -- Overstating and Broadening Scientific Claims

**What goes wrong:**
LLM-generated summaries of scientific papers are nearly five times more likely to contain broad generalizations than human-authored summaries. When summarizing physics/AI papers, the LLM replaces hedged, precise language ("our results suggest X under conditions Y") with sweeping claims ("X has been proven"). A 2025 Royal Society Open Science study found LLMs produce inaccurate conclusions in up to 73% of scientific summaries.

**Why it happens:**
LLMs are trained to produce confident, helpful text. Next-token prediction rewards fluency over epistemic precision. The model does not understand the difference between "evidence supports" and "proves," and its training data conflates press-release-style science writing with actual paper language. Surprisingly, prompting for accuracy can make this *worse* -- the model doubles down on confident-sounding generalizations.

**How to avoid:**
- Use Claude (identified as having the highest generalization accuracy among tested models) at low temperature (0.3-0.5).
- Enforce indirect, past-tense reporting in prompts: "The researchers found..." not "It has been shown..."
- Include explicit instructions: "Preserve all hedging language from the original paper. Do not upgrade 'suggests' to 'shows' or 'demonstrates.'"
- Require the LLM to quote key claims directly from the abstract/conclusion, then rephrase around those anchored quotes.
- Implement a post-generation verification step that compares claim strength between source and output.

**Warning signs:**
- Blog drafts that contain no hedging language ("suggests," "indicates," "under certain conditions")
- Conclusions that sound more definitive than the paper's own abstract
- Missing scope limitations (e.g., "works for all particle physics" when the paper tested one specific model)
- Absence of the word "may" or "might" when the original paper uses them

**Phase to address:**
Phase 1 (LLM Pipeline) -- bake claim-fidelity checking into the prompt engineering and review workflow from day one. This is the single most reputation-damaging pitfall for a research institute blog.

**Confidence:** HIGH -- Royal Society Open Science study (2025), multiple corroborating sources

---

### Pitfall 2: Mathematical Notation and Equation Loss in Summarization

**What goes wrong:**
Physics and AI papers are dense with equations, variable definitions, and mathematical notation. When an LLM summarizes these papers, it either drops equations entirely, renders them incorrectly, or "explains" them with fabricated formulas that sound plausible but are wrong. The transformer architecture reinterprets formalized elements (formulas, equations) through self-attention rather than preserving them literally.

**Why it happens:**
LLMs process equations as token sequences, not mathematical objects. LaTeX notation like `\frac{\partial \mathcal{L}}{\partial \theta}` gets tokenized in ways that lose mathematical structure. The model may produce valid-looking LaTeX that encodes a different equation, or simplify notation in ways that change meaning. For physics papers at IAIFI (quantum field theory, neural network theory), this is especially dangerous because subtle notational differences carry significant meaning.

**How to avoid:**
- Do NOT ask the LLM to reproduce or explain specific equations in blog posts. Instead, reference them by number ("Equation 3 in the paper defines...").
- For blog-level explanation, instruct the LLM to describe what an equation *does* conceptually, not to rewrite it.
- If equations must appear in the blog, extract them directly from the LaTeX source (not LLM-generated) and embed them as rendered images or KaTeX blocks.
- Implement a "no invented equations" rule: any equation in the blog must have a direct source in the paper.

**Warning signs:**
- Blog drafts containing inline LaTeX that was not copy-pasted from the source paper
- Equations that "look right" but have different variable names or operators than the original
- Summaries that claim to explain a key equation but get the relationship between variables wrong

**Phase to address:**
Phase 1 (LLM Pipeline) -- prompt design must explicitly handle equation treatment. Phase 2 (Figure Extraction) -- extract equations as images from PDFs when they need to appear in posts.

**Confidence:** HIGH -- multiple academic sources on LLM mathematical reasoning limitations, corroborated by hallucination research

---

### Pitfall 3: PDF Figure Extraction Produces Fragmented or Incomplete Images

**What goes wrong:**
PyMuPDF (and similar PDF parsers) frequently split a single academic figure into multiple image fragments, miss vector graphics entirely (common in physics plots), or include surrounding text/captions as part of the figure image. For arxiv papers compiled from LaTeX, figures containing multiple sub-panels (e.g., Figure 1a, 1b, 1c) often extract as separate disconnected pieces. Graphs rendered as vector paths (not embedded raster images) may not extract at all.

**Why it happens:**
PDFs are display-format documents, not semantic documents. A "figure" in a PDF is just a collection of drawing commands and embedded images at specific coordinates -- there is no semantic boundary marking "this is one figure." PyMuPDF extracts embedded image objects, but vector graphics (lines, curves, fills) that make up most scientific plots are not images in the PDF sense. LaTeX-generated PDFs are particularly tricky because figures may be composited from multiple layers.

**How to avoid:**
- **Primary strategy:** Extract figures from LaTeX source files, not PDFs. Arxiv stores the original `.tex` source with figure files (`.png`, `.pdf`, `.eps`) in tar.gz archives. Parse the `.tex` file to find `\includegraphics{}` commands and extract the original figure files directly.
- **Fallback strategy:** If source is unavailable, use PyMuPDF4LLM's `write_images=True` mode which attempts page-level image extraction, then crop based on figure caption locations.
- **Verify extraction:** Automated check that compares the number of extracted figures against the figure count mentioned in the paper text (count occurrences of "Figure N" or "Fig. N").
- **Never silently fail:** If figure extraction produces suspicious results (tiny images, wrong aspect ratios), flag for manual review rather than publishing broken figures.

**Warning signs:**
- Extracted images that are much smaller than expected (fragments)
- Figure count mismatch between extracted images and paper references
- Missing plots/graphs (vector graphics not extracted)
- Images that include caption text or adjacent body text

**Phase to address:**
Phase 2 (Figure Extraction) -- this requires dedicated engineering. Build the LaTeX-source extraction path first, PDF extraction as fallback only.

**Confidence:** HIGH -- PyMuPDF GitHub issues document these exact problems, corroborated by academic PDF parsing benchmarks (OmniDocBench CVPR 2025)

---

### Pitfall 4: Arxiv API Rate Limiting and Silent Data Loss

**What goes wrong:**
The arxiv API enforces a strict rate limit of 1 request per 3 seconds. Beyond rate limits, the API silently returns empty results when paginating past 1,000 results using the `start` parameter. Developers build a pipeline that works in testing (small result sets) but silently drops papers in production when querying active categories. Additionally, OAI-PMH datestamps for older articles do not correspond to original submission times due to bulk metadata updates, causing incremental harvesting to miss papers or re-process already-handled ones.

**Why it happens:**
The arxiv API documentation is sparse and does not prominently warn about the 1,000-result pagination ceiling. The rate limit is lenient enough for manual testing but breaks automated pipelines that need to sync multiple categories. OAI-PMH datestamp semantics are a known source of confusion across all OAI-PMH implementations, not just arxiv.

**How to avoid:**
- Implement exponential backoff with a minimum of 3-second intervals between requests.
- For IAIFI papers specifically, use targeted queries by author affiliation or arxiv category (hep-th, cs.AI, astro-ph, etc.) to keep result sets under 1,000.
- Use OAI-PMH for metadata discovery, then fetch individual papers via the standard API or direct PDF/source download.
- Store the arxiv ID of every processed paper locally and use it as the deduplication key -- never rely solely on datestamps for incremental sync.
- For bulk historical data, use the S3 requester-pays bucket (legitimate, sanctioned by arxiv) rather than scraping the API.
- Log response sizes: if a query returns exactly 0 results or suspiciously few, flag it rather than treating it as "no new papers."

**Warning signs:**
- HTTP 429 responses or connection resets from arxiv
- A category that should have papers returning zero results
- Duplicate processing of the same papers on consecutive runs
- Metadata showing unexpected "update" dates on old papers

**Phase to address:**
Phase 1 or early Phase 2 (Data Ingestion) -- the arxiv integration is foundational. Get rate limiting and pagination right before building anything on top of it.

**Confidence:** HIGH -- arxiv official API docs and Terms of Use confirm rate limits; Google Groups discussions confirm the 1,000-result ceiling

---

### Pitfall 5: Concept Network Becomes an Unusable Hairball

**What goes wrong:**
Force-directed graph visualizations of concept networks degrade rapidly as node count grows. SVG-based D3 graphs become janky above ~500 nodes. With an active research institute publishing across physics and AI, the concept network quickly reaches thousands of nodes and edges, resulting in an unreadable, slow-loading visualization that provides no insight. Users see a dense blob of overlapping labels and give up.

**Why it happens:**
Force-directed layout algorithms are O(n^2) per tick for naive implementations (n-body gravity simulation). D3's default SVG rendering creates a DOM element per node and per edge, and browsers struggle above 1,000 DOM elements for interactive content. More fundamentally, dense graphs with many cross-connections do not produce meaningful visual layouts regardless of performance -- the layout itself becomes uninformative.

**How to avoid:**
- **Cap the visible graph:** Show a focused subgraph (e.g., concepts related to the currently viewed paper, or a selected research theme) rather than the entire network. Let users drill into neighborhoods.
- **Use Canvas or WebGL rendering:** Switch from SVG to Canvas for graphs above 200 nodes. For 1,000+ nodes, use WebGL via PIXI.js or a library like `force-graph` (vasturiano) which uses Three.js.
- **Pre-compute layouts:** Run force-directed simulation at build time (during static site generation), save node positions, and render a static layout with only interaction (hover, click) handled client-side.
- **Cluster before display:** Group related concepts into clusters and show the cluster-level graph by default, expanding on click.
- **Progressive loading:** Load the core network structure first, add detail on demand.

**Warning signs:**
- Page load time exceeds 3 seconds on the concept network page
- Frame rate drops below 30fps during graph interaction
- Users cannot identify distinct clusters or meaningful patterns visually
- The graph looks the same regardless of which research area you focus on

**Phase to address:**
Phase 3 (Concept Network Visualization) -- this is inherently a later-phase feature. Design the data model for concepts early (Phase 1), but defer visualization to a dedicated phase where performance can be properly addressed.

**Confidence:** HIGH -- D3 performance benchmarks and graph visualization research confirm these thresholds

---

### Pitfall 6: Two-Column LaTeX Layout Destroys Text Extraction Order

**What goes wrong:**
Most arxiv physics papers use two-column layouts. PDF text extraction tools read text in a left-to-right, top-to-bottom order across the full page width, interleaving text from the left and right columns. The extracted text becomes garbled: sentences from different sections get merged, paragraphs are split mid-sentence, and the LLM receives nonsensical input that it then confidently summarizes (compounding the error).

**Why it happens:**
PDFs encode text as positioned character sequences, not as semantic paragraphs. Two-column layouts place text blocks at coordinates that, when sorted naively by position, interleave the columns. While some tools (PyMuPDF, pdfplumber) have column-detection heuristics, they fail on papers with mixed layouts (single-column abstract, two-column body, full-width figures and equations).

**How to avoid:**
- **Prefer LaTeX source over PDF for text extraction.** Parse the `.tex` file directly to get properly ordered, semantically structured text.
- If PDF parsing is necessary, use PyMuPDF4LLM which has reading-order heuristics, or use a layout-aware parser like Nougat or GROBID that understands academic paper structure.
- **Validate extracted text:** Check for obvious column-interleaving artifacts (sentences that start mid-word, sudden topic switches within a paragraph).
- **Fall back to abstract + conclusion:** For summarization, the abstract and conclusion are usually single-column and extract cleanly. Use these as the primary input, with body text as supplementary context.

**Warning signs:**
- Extracted text contains sentence fragments or mid-word breaks
- Paragraph text suddenly switches topic and then switches back
- Section headers appear inside paragraphs rather than at the start
- The LLM summary mentions concepts from wildly different sections as if they are related

**Phase to address:**
Phase 1 (Paper Ingestion Pipeline) -- text extraction quality directly determines summarization quality. This must be solved before the LLM step.

**Confidence:** HIGH -- documented in PDF parsing benchmarks, pdfplumber GitHub issues, and OmniDocBench (CVPR 2025)

---

### Pitfall 7: No Human-in-the-Loop Means Hallucinations Ship to Production

**What goes wrong:**
The pipeline works end-to-end, generates plausible blog posts, and the team assumes automated quality is "good enough." Hallucinated claims, wrong attributions, or subtly distorted findings get published on an official institute blog. One incorrect post noticed by the research community damages IAIFI's credibility. The blog goes from asset to liability.

**Why it happens:**
Automation bias: once a pipeline produces reasonable-looking output, reviewers skim rather than verify. Physics/AI researchers are time-constrained and may rubber-stamp reviews. The editorial workflow lacks friction points that force careful reading. There is no structured checklist for what to verify.

**How to avoid:**
- **Make review mandatory and blocking.** No post publishes without explicit admin approval through a dedicated review interface (not just a "publish" button).
- **Structured review checklist:** Provide reviewers with a side-by-side view of the original paper abstract/conclusions and the generated blog post. Include specific checkpoints: "Are all claims supported by the paper? Are hedging words preserved? Are equations correctly referenced?"
- **Author notification:** Email the paper's authors (IAIFI researchers) a preview link before publishing. They are the best fact-checkers for their own work.
- **Confidence scoring:** Have the LLM self-assess which claims it is least confident about. Flag these for reviewers.
- **Start conservative:** Launch with more editorial friction than you think you need. Reduce it as you build trust in the pipeline, not the other way around.

**Warning signs:**
- Reviews are being completed in under 2 minutes (too fast for meaningful verification)
- Blog posts go live the same day they are generated (no review buffer)
- No one has ever rejected or substantially edited a generated post
- Paper authors express surprise at claims in the blog post

**Phase to address:**
Phase 1 (Core Pipeline) -- the admin review interface is not a nice-to-have, it is a launch requirement. Build it as part of the MVP, not as a later enhancement.

**Confidence:** HIGH -- editorial workflow research and NEJM AI publications on human-AI review confirm this pattern

---

## Technical Debt Patterns

Shortcuts that seem reasonable but create long-term problems.

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
|----------|-------------------|----------------|-----------------|
| Hardcoding arxiv category filters | Quick setup for IAIFI's specific categories | Adding new research areas requires code changes; categories evolve over time | MVP only; move to config within first month |
| Storing generated posts as flat files only | Simple, no database needed | No structured querying, no easy way to track generation metadata, re-generation history, or review status | Never for the review workflow; flat files OK for final published content (static site) |
| Skipping LaTeX source parsing, using PDF-only extraction | Avoids building a LaTeX parser | Permanently worse figure extraction, garbled two-column text, lost equation semantics | Only if LaTeX source is genuinely unavailable for the paper |
| Using a single LLM prompt for all paper types | One prompt to maintain | Physics theory papers, experimental papers, ML papers, and review articles need different summarization approaches | Acceptable for first 10 posts; must specialize before scaling |
| Not versioning generated content | Simpler data model | Cannot track how regeneration with updated prompts changed output; no rollback capability | Never; version from day one with minimal overhead (git or timestamps) |

## Integration Gotchas

Common mistakes when connecting to external services.

| Integration | Common Mistake | Correct Approach |
|-------------|----------------|------------------|
| Arxiv API | Polling at high frequency from a cron job without rate limiting | Use a 3-second minimum delay between requests; implement a queue with backoff; cache responses |
| Arxiv API | Relying on search API for paper discovery | Use OAI-PMH for systematic harvesting of new papers in target categories; use search API only for ad-hoc lookups |
| Arxiv S3 | Downloading full tar archives to get one paper's source | Use the individual paper source endpoint (`/src/{arxiv_id}`) for single-paper access; only use S3 for bulk historical ingestion |
| LLM API (OpenAI/Anthropic) | Not handling token limits for long papers (30+ pages) | Use semantic chunking: abstract + intro + conclusion first (fits in one context window); add methods/results only if needed for specific claims |
| LLM API | Sending raw PDF text (with extraction artifacts) to the LLM | Clean extracted text first: remove page numbers, headers/footers, reference lists, and column-interleaving artifacts before sending to LLM |
| Static site deployment (GitHub Pages / Netlify) | Triggering rebuild on every new draft | Only rebuild when posts move to "published" status; use a separate staging build for draft review |

## Performance Traps

Patterns that work at small scale but fail as usage grows.

| Trap | Symptoms | Prevention | When It Breaks |
|------|----------|------------|----------------|
| SVG-based concept network with all nodes rendered | Smooth at 50 nodes | Use Canvas/WebGL; pre-compute layout at build time | >300 nodes (likely reached within 6 months of papers) |
| Loading all blog post metadata on the homepage | Fast with 10 posts | Paginate; load metadata on demand; use a lightweight index file | >100 posts (year 2 of operation) |
| Regenerating all posts when prompt template changes | Fine for 10 posts | Version prompts; regenerate selectively; mark posts as "needs regeneration" | >50 posts (regeneration takes hours with rate-limited LLM calls) |
| Storing extracted figures as full-resolution PNGs | Fast enough locally | Compress images; serve WebP with PNG fallback; lazy-load below fold | >200 figures total (site becomes multi-GB) |
| Running force simulation client-side on page load | Works on developer's MacBook | Pre-compute layout; serve static positions; only simulate on interaction | Mobile devices or any machine with limited CPU |

## Security Mistakes

Domain-specific security issues beyond general web security.

| Mistake | Risk | Prevention |
|---------|------|------------|
| Storing LLM API keys in the static site repository | Keys exposed via public GitHub repo or client-side JS | Use server-side generation only; keys never touch the static site build; use environment variables in CI |
| Allowing arxiv paper IDs in URLs without validation | Path traversal or injection if IDs are used in file system operations | Validate arxiv ID format strictly (`YYMM.NNNNN` pattern); sanitize before any file system or API use |
| Publishing draft posts at predictable URLs | Unpublished content accessible if URL pattern is guessable | Use random tokens for draft preview URLs; do not deploy drafts to the public static site |
| LLM prompt injection via paper content | A malicious paper title or abstract could contain instructions that alter the LLM's behavior | Sanitize paper text before including in prompts; use system messages to separate instructions from content; monitor output for off-topic content |
| CI/CD pipeline with overly broad permissions | Compromised dependency can exfiltrate secrets during build | Pin all dependencies; use minimal CI permissions; audit GitHub Actions for credential exposure |

## UX Pitfalls

Common user experience mistakes in this domain.

| Pitfall | User Impact | Better Approach |
|---------|-------------|-----------------|
| Blog posts read like paper abstracts (too technical) | Non-specialist readers bounce; defeats the purpose of "accessible" science communication | Write for a scientifically literate but non-specialist audience; define jargon; use analogies; target ~800 words |
| No link back to the original paper | Researchers who want details cannot find the source; undermines credibility | Prominent, persistent link to the arxiv page at the top of every post |
| Concept network has no legend or explanation | Users see a pretty graph but do not understand what nodes/edges represent or how to interact | Include a brief "How to read this graph" overlay on first visit; label node types and edge meanings |
| Generated posts all sound identical in structure and voice | Blog feels robotic; readers lose interest | Vary prompt templates; use different structural approaches (narrative, Q&A, "why this matters"); include researcher quotes when available |
| Figures shown without context or captions | Images appear decorative rather than informative; readers skip them | Always include the original figure caption; add a one-sentence plain-language explanation above each figure |
| Mobile users cannot interact with concept network | Force-directed graphs are touch-hostile; pinch/zoom conflicts with page scroll | Provide a simplified static view on mobile; full interactive version on desktop only |

## "Looks Done But Isn't" Checklist

Things that appear complete but are missing critical pieces.

- [ ] **Paper ingestion:** Often missing handling for papers with supplementary materials -- verify the pipeline handles multi-file arxiv submissions (not just the main PDF/tex file)
- [ ] **Figure extraction:** Often missing alt-text for accessibility -- verify every extracted figure has descriptive alt text (can be LLM-generated from the caption)
- [ ] **Blog generation:** Often missing proper citation formatting -- verify the post includes the full paper citation (authors, title, journal, year, arxiv ID) in a standard format
- [ ] **Concept network:** Often missing edge labels -- verify relationships between concepts are labeled, not just "connected"
- [ ] **Static site build:** Often missing RSS feed -- verify the blog has a working RSS/Atom feed for subscribers (standard expectation for a blog)
- [ ] **Review workflow:** Often missing rejection/feedback path -- verify reviewers can send posts back for regeneration with specific feedback, not just approve/reject
- [ ] **LaTeX source extraction:** Often missing handling for papers that use `\input{}` to include sub-files -- verify the pipeline resolves file includes
- [ ] **Deployment:** Often missing cache invalidation -- verify that publishing a new post actually appears for visitors (CDN caching can delay by hours)

## Recovery Strategies

When pitfalls occur despite prevention, how to recover.

| Pitfall | Recovery Cost | Recovery Steps |
|---------|---------------|----------------|
| Published post contains hallucinated claim | MEDIUM | Issue correction notice on the post; notify paper authors; add the specific hallucination pattern to the prompt's "do not do" list; re-generate with strengthened prompt |
| Figure extraction pipeline breaks on new paper format | LOW | Fall back to no-figures mode (text-only post with link to paper); manually extract figures for the specific post; fix extraction for the new format |
| Concept network crashes browser | MEDIUM | Serve a pre-rendered static image as fallback; cap visible nodes to last-known-working count; move to WebGL renderer |
| Arxiv API access revoked due to rate limit violation | HIGH | Switch to OAI-PMH for metadata and S3 for source files; both are sanctioned alternatives. Contact arxiv support to restore API access |
| Generated posts all sound the same (style drift noticed late) | LOW | Create 3-5 distinct prompt templates categorized by paper type; retroactively regenerate posts that feel most similar; A/B test with readers |
| Two-column text interleaving corrupts summaries | MEDIUM | Switch to LaTeX source parsing; for already-published posts, re-extract text using layout-aware parser (Nougat/GROBID) and regenerate |

## Pitfall-to-Phase Mapping

How roadmap phases should address these pitfalls.

| Pitfall | Prevention Phase | Verification |
|---------|------------------|--------------|
| LLM generalization bias | Phase 1: Prompt Engineering | Compare claim strength of 10 generated posts against source abstracts; zero should be stronger than the source |
| Equation hallucination | Phase 1: Prompt Engineering | Audit generated posts for any LaTeX that does not appear verbatim in the source paper |
| PDF figure fragmentation | Phase 2: Figure Extraction | Count extracted figures vs. figure references in paper; match rate should be >90% |
| Arxiv rate limiting / data loss | Phase 1: Data Ingestion | Run ingestion for 24 hours; verify zero HTTP 429 errors and all expected papers are captured |
| Concept network hairball | Phase 3: Visualization | Test with 500+ nodes; frame rate must stay above 30fps; users can identify 3+ distinct clusters |
| Two-column text garbling | Phase 1: Text Extraction | Spot-check 20 extracted papers; zero should have column-interleaving artifacts |
| No human review | Phase 1: MVP | Verify that publishing is physically impossible without clicking "approve" in the admin interface |
| Style monotony | Phase 2: Content Quality | Have 3 non-technical readers rate variety across 10 posts; average uniqueness score >3/5 |
| Silent API failures | Phase 1: Data Ingestion | Verify alerting fires when arxiv returns empty results for a category that should have papers |
| Prompt injection via paper content | Phase 1: Prompt Engineering | Test with adversarial paper titles containing prompt-injection attempts; verify output is unaffected |

## Sources

- [Generalization bias in LLM summarization of scientific research -- Royal Society Open Science (2025)](https://royalsocietypublishing.org/doi/10.1098/rsos.241776)
- [Prominent chatbots routinely exaggerate science findings -- phys.org (2025)](https://phys.org/news/2025-05-prominent-chatbots-routinely-exaggerate-science.html)
- [Unable to extract entire figure from PDF -- PyMuPDF GitHub Discussion #4584](https://github.com/pymupdf/PyMuPDF/discussions/4584)
- [Some images are wrongly extracted -- pymupdf4llm GitHub Issue #148](https://github.com/pymupdf/pymupdf4llm/issues/148)
- [A Comparative Study of PDF Parsing Tools -- arxiv (2024)](https://arxiv.org/html/2410.09871v1)
- [OmniDocBench: Benchmarking Diverse PDF Document Parsing -- CVPR 2025](https://github.com/opendatalab/OmniDocBench)
- [Terms of Use for arXiv APIs](https://info.arxiv.org/help/api/tou.html)
- [arXiv API User's Manual](https://info.arxiv.org/help/api/user-manual.html)
- [arXiv Bulk Data Access -- S3](https://info.arxiv.org/help/bulk_data_s3.html)
- [arXiv OAI-PMH interface](https://info.arxiv.org/help/oa/index.html)
- [550 Hallucinations, Zero Discoveries -- LLM Mathematics (2026)](https://medium.com/@contact.n8n410/550-hallucinations-zero-discoveries-what-happens-when-you-force-an-llm-to-invent-mathematics-ab796d4257e4)
- [Vectara Hallucination Leaderboard](https://github.com/vectara/hallucination-leaderboard)
- [Graph visualization efficiency of popular web-based libraries -- PMC (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12061801/)
- [Scale Up D3 Graph Visualization with PIXI.js -- GraphAware](https://graphaware.com/blog/scale-up-your-d3-graph-visualisation-webgl-canvas-with-pixi-js/)
- [SVG vs Canvas vs WebGL performance benchmarks (2025)](https://www.svggenie.com/blog/svg-vs-canvas-vs-webgl-performance-2025)
- [Building AI into Editorial Workflows: Early Lessons -- Hum](https://blog.hum.works/posts/building-ai-into-editorial-workflows)
- [Accelerating Science with Human+AI Review -- NEJM AI](https://ai.nejm.org/doi/full/10.1056/AIe2501175)
- [How Examples Improve LLM Style Consistency -- Latitude](https://latitude-blog.ghost.io/blog/how-examples-improve-llm-style-consistency/)
- [LLM-empowered knowledge graph construction survey (2025)](https://arxiv.org/pdf/2510.20345)
- [Parsing PDF with 2 columns -- pdfplumber GitHub Discussion #885](https://github.com/jsvine/pdfplumber/discussions/885)
- [Chunking Strategies for LLM Applications -- Pinecone](https://www.pinecone.io/learn/chunking-strategies/)

---
*Pitfalls research for: IAIFI Research Blog -- Automated science blog generation from physics/AI academic papers*
*Researched: 2026-03-03*
