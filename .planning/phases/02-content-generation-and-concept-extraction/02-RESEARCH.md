# Phase 2: Content Generation and Concept Extraction - Research

**Researched:** 2026-03-03
**Domain:** LLM-powered content generation, PDF figure extraction, scientific concept extraction
**Confidence:** HIGH

## Summary

Phase 2 transforms ingested papers into draft blog posts with extracted figures and structured concept data. The core technical domains are: (1) LLM integration via LiteLLM for provider-agnostic generation with structured output, (2) PDF figure extraction using PyMuPDF for both raster images and vector graphics, (3) multi-pass content refinement using a journalist-reader-editor prompt chain, and (4) concept extraction as structured JSON for downstream network visualization.

The existing codebase provides a solid foundation: 554 papers in SQLite with PDFs downloaded, async database layer with WAL mode, Pydantic models, and an orchestrator pattern to extend. Phase 2 adds three new pipeline stages (LLM generation, figure extraction, concept extraction) that slot into the existing staged pipeline architecture.

**Primary recommendation:** Use LiteLLM with disk caching, PyMuPDF for dual-strategy figure extraction (raster + vector), Jinja2 prompt templates, and Pydantic response models for all structured LLM outputs. Avoid pymupdf4llm for figure extraction (use it only for text-to-markdown conversion) -- use raw PyMuPDF `get_images()` and `cluster_drawings()` directly for figure selection.

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| GEN-01 | LLM generates ~800-1500 word blog post from paper | LiteLLM `acompletion()` with Jinja2 templates; word count enforced via prompt + validation |
| GEN-02 | Blog posts start accessible then get more technical | Prompt template structure with explicit sections; multi-pass refinement validates accessibility gradient |
| GEN-03 | LLM uses structured templates for consistent post format | Jinja2 templates with sections: overview, highlights, impact/implications; Pydantic model for structured output |
| GEN-04 | Multi-pass readability refinement (journalist-reader-editor) | Three-pass LLM chain: journalist drafts, reader simplifies, editor polishes; each pass has distinct system prompt |
| GEN-05 | System auto-selects 1-3 most informative figures from paper PDF | PyMuPDF dual strategy: `get_images()` for raster + `cluster_drawings()` for vector; scoring by size/position/aspect ratio |
| GEN-06 | Flexible LLM backend (Claude, OpenAI, others via LiteLLM) | LiteLLM `acompletion()` with model string from config; env vars for API keys; disk caching to avoid re-generation |
| CONCEPT-01 | LLM extracts 5-15 scientific concepts per paper as structured data | LiteLLM with Pydantic `response_format`; structured JSON output with concept name, relevance score, category |
| CONCEPT-02 | Papers auto-categorized into IAIFI themes | Already have `iaifi_category` from Phase 1 scraping; LLM can refine/validate using paper abstract |
| CONCEPT-03 | Concept data stored as JSON for network visualization | Pydantic models serialize to JSON; stored in SQLite as JSON column + written to filesystem for site consumption |
</phase_requirements>

## Standard Stack

### Core

| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| LiteLLM | latest (1.82+) | Multi-provider LLM gateway | Unified `acompletion()` for Claude, OpenAI, Gemini, Ollama. Handles provider differences. Built-in cost tracking. Disk caching. |
| PyMuPDF | 1.27.1 | PDF figure extraction | Fastest Python PDF library. Dual extraction: `get_images()` for raster, `cluster_drawings()` for vector graphics. Pure compiled C, no system deps. |
| pymupdf4llm | 0.3.4 | PDF to markdown conversion | Converts academic PDFs to LLM-digestible markdown. Preserves headers, tables, reading order. Used to feed paper content to LLM (NOT for figure extraction). |
| Jinja2 | 3.1+ | Prompt templates | Standard Python templating. Separate prompt text from code. Supports conditionals, loops, template inheritance. Already a FastAPI transitive dependency. |
| Pydantic | 2.12+ (already installed) | Structured LLM output schemas | Define response models as Python classes. Auto-generates JSON Schema for LLM `response_format`. Validates LLM output. |

### Supporting

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| Pillow | 11+ | Image post-processing | Resize extracted figures, convert formats, check dimensions. Needed for figure quality filtering. |
| python-dotenv | 1.2+ (already installed) | Environment variable management | Load API keys from `.env` file. Already in project. |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| LiteLLM | Direct anthropic/openai SDKs | Only if committed to single provider. LiteLLM adds ~100ms overhead but eliminates vendor lock-in entirely. |
| LiteLLM | LangChain | Massive overkill. We need `completion()` not agent chains. LangChain adds 50+ dependencies for zero benefit here. |
| PyMuPDF for figures | pdfplumber | Better at tables, worse at figures. Slower. Cannot extract vector graphics. |
| PyMuPDF for figures | Marker / Nougat | ML-based, much heavier (requires torch). Better for very complex layouts but way too heavy for figure extraction. |
| Jinja2 | f-strings | Works for simple prompts but becomes unmanageable with multi-section templates, conditionals, and template inheritance. |
| Jinja2 | banks (prompt library) | Adds a dependency for marginal gain. Jinja2 is already proven and well-understood. |

**Installation:**
```bash
uv pip install litellm pymupdf pymupdf4llm jinja2 pillow
```

## Architecture Patterns

### Recommended Project Structure (additions to existing)
```
pipeline/
├── generator/              # NEW: LLM content generation
│   ├── __init__.py
│   ├── llm_client.py       # LiteLLM wrapper with caching + cost tracking
│   ├── post_generator.py   # Multi-pass blog post generation orchestrator
│   ├── concept_extractor.py # LLM-based concept extraction
│   └── prompts/            # Jinja2 prompt templates
│       ├── blog_draft.j2       # Journalist pass: initial draft
│       ├── blog_simplify.j2    # Reader pass: accessibility refinement
│       ├── blog_polish.j2      # Editor pass: final polish
│       └── concepts.j2         # Concept extraction prompt
├── extractor/              # NEW: PDF processing
│   ├── __init__.py
│   ├── figure_extractor.py # PyMuPDF figure extraction + scoring
│   └── pdf_reader.py       # pymupdf4llm text extraction
├── models.py               # EXTEND: add BlogPost, Concept, GenerationResult models
├── config.py               # EXTEND: add LLM config settings
├── db.py                   # EXTEND: add blog_posts, concepts tables
└── orchestrator.py         # EXTEND: add generation pipeline stages
```

### Pattern 1: LLM Client with Disk Caching

**What:** A thin wrapper around LiteLLM that adds disk caching (keyed on prompt hash + model), cost tracking, and retry logic. All LLM calls in the project go through this single client.

**When to use:** Every LLM call. Never call LiteLLM directly from business logic.

**Example:**
```python
# pipeline/generator/llm_client.py
import hashlib
import json
import litellm
from litellm.caching.caching import Cache
from pydantic import BaseModel

class LLMClient:
    """Provider-agnostic LLM client with caching and cost tracking."""

    def __init__(self, model: str = "claude-sonnet-4-20250514", temperature: float = 0.7):
        self.model = model
        self.temperature = temperature
        self.total_cost = 0.0
        # Enable disk caching to avoid re-generation during development
        litellm.cache = Cache(type="disk", disk_cache_dir="data/llm_cache")

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        max_tokens: int = 4096,
    ) -> str:
        """Generate text completion."""
        response = await litellm.acompletion(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=self.temperature,
            max_tokens=max_tokens,
        )
        # Track cost
        cost = response._hidden_params.get("response_cost", 0)
        self.total_cost += cost
        return response.choices[0].message.content

    async def generate_structured(
        self,
        system_prompt: str,
        user_prompt: str,
        response_model: type[BaseModel],
        max_tokens: int = 4096,
    ) -> BaseModel:
        """Generate structured JSON output validated by Pydantic."""
        response = await litellm.acompletion(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format=response_model,
            temperature=self.temperature,
            max_tokens=max_tokens,
        )
        return response_model.model_validate_json(
            response.choices[0].message.content
        )
```
Source: [LiteLLM Structured Outputs Docs](https://docs.litellm.ai/docs/completion/json_mode), [LiteLLM Async Docs](https://docs.litellm.ai/docs/completion/stream), [LiteLLM Caching Docs](https://docs.litellm.ai/docs/caching/all_caches)

### Pattern 2: Multi-Pass Generation (Journalist-Reader-Editor)

**What:** Three separate LLM calls with distinct system prompts, each refining the output of the previous pass. The journalist drafts from the paper, the reader simplifies for accessibility, the editor polishes for consistency and quality.

**When to use:** For blog post generation (GEN-04). Not needed for concept extraction (single pass is sufficient).

**Example:**
```python
# pipeline/generator/post_generator.py
from jinja2 import Environment, FileSystemLoader

class PostGenerator:
    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client
        self.env = Environment(
            loader=FileSystemLoader("pipeline/generator/prompts")
        )

    async def generate_post(self, paper: Paper, pdf_markdown: str) -> BlogPost:
        # Pass 1: Journalist drafts from paper content
        draft_prompt = self.env.get_template("blog_draft.j2").render(
            title=paper.title,
            authors=paper.authors,
            abstract=paper.abstract,
            paper_content=pdf_markdown[:8000],  # Truncate to fit context
            iaifi_category=paper.iaifi_category,
        )
        draft = await self.llm.generate(
            system_prompt="You are a science journalist...",
            user_prompt=draft_prompt,
        )

        # Pass 2: Reader simplifies opening sections
        simplify_prompt = self.env.get_template("blog_simplify.j2").render(
            draft=draft,
        )
        simplified = await self.llm.generate(
            system_prompt="You are an educated general reader...",
            user_prompt=simplify_prompt,
        )

        # Pass 3: Editor polishes for consistency
        polish_prompt = self.env.get_template("blog_polish.j2").render(
            draft=simplified,
            target_words=(800, 1500),
        )
        final = await self.llm.generate(
            system_prompt="You are a senior science editor...",
            user_prompt=polish_prompt,
        )

        return BlogPost(
            paper_arxiv_id=paper.arxiv_id,
            content=final,
            status="draft",
        )
```

### Pattern 3: Dual-Strategy Figure Extraction

**What:** Extract figures from PDFs using two complementary strategies: `get_images()` for embedded raster images and `cluster_drawings()` for vector graphics (which are common in academic papers). Score and rank all candidates, then select the top 1-3.

**When to use:** For every paper PDF (GEN-05).

**Example:**
```python
# pipeline/extractor/figure_extractor.py
import pymupdf
from pathlib import Path

class FigureExtractor:
    def __init__(self, output_dir: str = "data/figures"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.min_size = 100       # Minimum dimension in pixels
        self.min_area_ratio = 0.02  # Minimum fraction of page area

    def extract_figures(self, pdf_path: str, arxiv_id: str, max_figures: int = 3) -> list[dict]:
        doc = pymupdf.open(pdf_path)
        candidates = []

        for page_num, page in enumerate(doc):
            page_area = page.rect.width * page.rect.height

            # Strategy 1: Raster images
            for img_info in page.get_images(full=True):
                xref = img_info[0]
                img = doc.extract_image(xref)
                if img and self._is_significant(img["width"], img["height"], page_area):
                    candidates.append({
                        "type": "raster",
                        "page": page_num,
                        "width": img["width"],
                        "height": img["height"],
                        "xref": xref,
                        "data": img["image"],
                        "ext": img["ext"],
                    })

            # Strategy 2: Vector graphics (clustered drawings)
            paths = page.get_drawings()
            if paths:
                clusters = page.cluster_drawings(drawings=paths)
                for box in clusters:
                    box_area = box.width * box.height
                    if box_area / page_area >= self.min_area_ratio:
                        pix = page.get_pixmap(clip=box, dpi=150)
                        candidates.append({
                            "type": "vector",
                            "page": page_num,
                            "width": pix.width,
                            "height": pix.height,
                            "pixmap": pix,
                        })

        doc.close()

        # Score and select top candidates
        scored = sorted(candidates, key=self._score_candidate, reverse=True)
        selected = scored[:max_figures]

        # Save selected figures
        saved = []
        fig_dir = self.output_dir / arxiv_id
        fig_dir.mkdir(parents=True, exist_ok=True)
        for i, fig in enumerate(selected):
            path = fig_dir / f"figure-{i+1}.png"
            if fig["type"] == "raster":
                path.write_bytes(fig["data"])
            else:
                fig["pixmap"].save(str(path))
            saved.append({
                "path": str(path),
                "page": fig["page"],
                "width": fig["width"],
                "height": fig["height"],
                "type": fig["type"],
            })
        return saved

    def _score_candidate(self, candidate: dict) -> float:
        """Score figure candidates by size and aspect ratio."""
        area = candidate["width"] * candidate["height"]
        aspect = min(candidate["width"], candidate["height"]) / max(candidate["width"], candidate["height"])
        # Penalize very tall/narrow or very wide/short images (likely decorations)
        aspect_score = aspect if aspect > 0.3 else aspect * 0.5
        # Prefer figures from early pages (more likely to be key results)
        page_score = 1.0 / (1 + candidate["page"] * 0.1)
        return area * aspect_score * page_score

    def _is_significant(self, width: int, height: int, page_area: float) -> bool:
        return (width >= self.min_size and height >= self.min_size
                and (width * height) / page_area >= self.min_area_ratio)
```
Source: [PyMuPDF Image Extraction Docs](https://pymupdf.readthedocs.io/en/latest/recipes-images.html), [PyMuPDF Discussion #4584](https://github.com/pymupdf/PyMuPDF/discussions/4584)

### Pattern 4: Structured Concept Extraction

**What:** Use LLM with Pydantic `response_format` to extract scientific concepts as structured JSON. Each concept has a name, brief description, and relevance score. The LLM also validates/refines the IAIFI category.

**When to use:** For every paper (CONCEPT-01, CONCEPT-02, CONCEPT-03).

**Example:**
```python
# Pydantic response models
from pydantic import BaseModel, Field

class ExtractedConcept(BaseModel):
    name: str = Field(description="Short concept name, 1-4 words")
    description: str = Field(description="One-sentence explanation")
    relevance: float = Field(ge=0, le=1, description="How central to the paper, 0-1")

class ConceptExtractionResult(BaseModel):
    concepts: list[ExtractedConcept] = Field(
        min_length=5, max_length=15,
        description="5-15 scientific concepts from the paper"
    )
    iaifi_theme: str = Field(
        description="Primary IAIFI theme: Foundational AI, Theoretical Physics, Experimental Physics, or Astrophysics"
    )
    secondary_themes: list[str] = Field(
        default_factory=list,
        description="Additional relevant IAIFI themes"
    )

# Usage in concept_extractor.py
result = await llm_client.generate_structured(
    system_prompt="You are a scientific concept analyst...",
    user_prompt=concept_prompt,
    response_model=ConceptExtractionResult,
)
```
Source: [LiteLLM Structured Output](https://docs.litellm.ai/docs/completion/json_mode), [Pydantic for LLM Outputs](https://pydantic.dev/articles/llm-intro)

### Anti-Patterns to Avoid

- **Calling LLM APIs directly without caching:** LLM calls cost money and are slow (2-5s each). Without caching, re-running the pipeline during development re-generates every post. Use LiteLLM disk cache keyed on prompt hash + model.
- **Putting prompts inline in Python code:** Multi-paragraph prompts with examples become unreadable as f-strings. Use Jinja2 templates loaded from `prompts/` directory.
- **Using pymupdf4llm for figure extraction:** pymupdf4llm's `write_images` parameter has known bugs with `image_path` handling when `pymupdf.layout` is active. Use raw PyMuPDF `get_images()` + `cluster_drawings()` for figures. Use pymupdf4llm ONLY for text-to-markdown conversion.
- **Single-pass blog generation:** A single LLM call produces inconsistent quality. The journalist-reader-editor pattern catches accessibility issues, jargon, and structural problems that a single pass misses.
- **Unbounded PDF text input to LLM:** Academic PDFs can be 30+ pages. Sending the full text exceeds context windows and wastes tokens. Truncate to first 8000-10000 characters of markdown (covers abstract + introduction + key sections).

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Multi-provider LLM switching | Custom API wrappers per provider | LiteLLM | Different auth, response formats, rate limits, streaming protocols per provider. LiteLLM handles all of it. |
| Prompt template management | String concatenation / f-strings | Jinja2 templates | Prompts are multi-paragraph with conditionals. Templates are testable, versionable, and readable. |
| PDF text extraction | Custom PDF parser | pymupdf4llm `to_markdown()` | Academic PDF layout (columns, headers, tables, equations) is extremely complex. pymupdf4llm handles reading order, headers, formatting. |
| Figure extraction from vector PDFs | Page-to-image conversion | PyMuPDF `cluster_drawings()` | Converting whole pages to images loses resolution and includes text. `cluster_drawings()` identifies individual figure boundaries. |
| JSON schema for LLM output | Manual schema dict construction | Pydantic `BaseModel` | Pydantic auto-generates JSON Schema, validates responses, provides type hints, and integrates with LiteLLM `response_format`. |
| LLM response caching | Custom file-based cache | LiteLLM disk cache | LiteLLM caches by prompt+model hash, handles TTL, and supports per-request cache control. |

**Key insight:** This phase involves three mature ecosystems (LLM APIs, PDF processing, prompt engineering) where the libraries are dramatically better than hand-rolled solutions. The complexity is in the prompts and scoring heuristics, not the plumbing.

## Common Pitfalls

### Pitfall 1: Vector Graphics Treated as Missing Figures
**What goes wrong:** `page.get_images()` returns nothing for pages with clearly visible figures. Developer concludes the PDF has no figures.
**Why it happens:** Academic papers (especially from LaTeX) render figures as vector graphics (paths/curves), not embedded raster images. `get_images()` only finds raster images.
**How to avoid:** Always use both `get_images()` AND `cluster_drawings()` strategies. Score all candidates together regardless of extraction method.
**Warning signs:** Empty image lists from PDFs that visually contain figures.

### Pitfall 2: LLM Structured Output Failures
**What goes wrong:** LLM returns text that doesn't parse as valid JSON, or JSON that doesn't match the Pydantic schema. Pipeline crashes on `model_validate_json()`.
**Why it happens:** Not all models support native `json_schema` response format. Some models occasionally include markdown code fences around JSON. Older/smaller models may not follow schema constraints (e.g., `min_length=5`).
**How to avoid:** Wrap `model_validate_json()` in try/except with retry logic. Strip markdown code fences from response before parsing. Set `litellm.enable_json_schema_validation = True` for models that don't support native schemas. Use Claude or GPT-4o for best structured output compliance.
**Warning signs:** `ValidationError` from Pydantic during concept extraction.

### Pitfall 3: Exceeding LLM Context Window
**What goes wrong:** Sending a 40-page paper's full text to the LLM causes a 400 error or silent truncation.
**Why it happens:** Academic PDFs can be 15,000+ tokens when converted to markdown. Combined with system prompt + examples, this exceeds some models' context windows.
**How to avoid:** Use pymupdf4llm to extract text, then truncate to first N characters (8000-10000) which typically covers abstract + introduction + key methodology. For the journalist pass, also include the conclusion section. Set `max_tokens` explicitly.
**Warning signs:** HTTP 400 errors from LLM API, unexpectedly short or incomplete blog posts.

### Pitfall 4: pymupdf4llm image_path Bug
**What goes wrong:** Images extracted by pymupdf4llm with `write_images=True` end up in the wrong directory, or path construction fails with an exception.
**Why it happens:** Known bug in pymupdf4llm when `pymupdf.layout` is imported. The `image_path` parameter gets ignored or mangled.
**How to avoid:** Do NOT use pymupdf4llm for figure extraction. Use it ONLY for text-to-markdown conversion (with `write_images=False`, `ignore_images=True`). Handle figure extraction separately with raw PyMuPDF.
**Warning signs:** FileNotFoundError during pymupdf4llm calls, images appearing in unexpected directories.

### Pitfall 5: Inconsistent Blog Post Length
**What goes wrong:** LLM generates posts ranging from 400 to 3000 words despite the prompt requesting 800-1500.
**Why it happens:** LLMs approximate word counts poorly. A single instruction like "write 800-1500 words" is unreliable.
**How to avoid:** Validate word count after generation. If outside range, include word count feedback in the editor pass prompt: "The current draft is X words. Adjust to 800-1500 words." Add a retry with explicit length guidance if still out of range.
**Warning signs:** Blog posts consistently too short (< 700 words) or too long (> 1800 words).

### Pitfall 6: Tiny/Decorative Images Treated as Figures
**What goes wrong:** The figure extractor selects journal logos, LaTeX equation renderings, or 1x1 tracking pixels as "figures."
**Why it happens:** `get_images()` returns ALL embedded images including tiny icons, backgrounds, and decorative elements.
**How to avoid:** Filter by minimum dimensions (100x100 pixels minimum), minimum area ratio relative to page (2%+), and aspect ratio (reject very narrow strips). Score by area, position on page, and aspect ratio before selecting top candidates.
**Warning signs:** Selected figures are tiny, have extreme aspect ratios, or appear to be logos/icons.

### Pitfall 7: LLM API Key Not Configured
**What goes wrong:** Pipeline crashes on first LLM call with authentication error. User has PDFs and metadata but can't generate content.
**Why it happens:** LiteLLM expects provider-specific env vars (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`). These are easy to forget, especially in a new environment.
**How to avoid:** Check for required API key at LLMClient initialization, not at first call. Provide a clear error message: "Set ANTHROPIC_API_KEY or OPENAI_API_KEY in .env file." Add a `pipeline/generator/check_config.py` utility.
**Warning signs:** `AuthenticationError` from LiteLLM.

## Code Examples

### PDF to Markdown for LLM Consumption
```python
# Source: pymupdf4llm docs (https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/)
import pymupdf4llm

def extract_paper_text(pdf_path: str, max_chars: int = 10000) -> str:
    """Extract paper text as markdown, truncated for LLM context."""
    md_text = pymupdf4llm.to_markdown(
        pdf_path,
        write_images=False,     # Don't extract images (handle separately)
        ignore_images=True,     # Skip image placeholders in markdown
        show_progress=False,
    )
    # Truncate to fit LLM context window
    if len(md_text) > max_chars:
        md_text = md_text[:max_chars] + "\n\n[Content truncated for processing]"
    return md_text
```

### LiteLLM Provider Switching via Config
```python
# Source: LiteLLM docs (https://docs.litellm.ai/docs/set_keys)
# pipeline/config.py additions
import os

@dataclass
class LLMSettings:
    """LLM configuration with environment variable overrides."""
    MODEL: str = os.environ.get("IAIFI_LLM_MODEL", "claude-sonnet-4-20250514")
    TEMPERATURE: float = float(os.environ.get("IAIFI_LLM_TEMPERATURE", "0.7"))
    MAX_TOKENS: int = int(os.environ.get("IAIFI_LLM_MAX_TOKENS", "4096"))
    CACHE_DIR: str = os.environ.get("IAIFI_LLM_CACHE_DIR", "data/llm_cache")

# Switching providers requires only changing the env var:
#   IAIFI_LLM_MODEL=gpt-4o           (OpenAI)
#   IAIFI_LLM_MODEL=claude-sonnet-4-20250514   (Anthropic)
#   IAIFI_LLM_MODEL=ollama/llama3    (Local via Ollama)
```

### Jinja2 Blog Post Draft Template
```jinja2
{# pipeline/generator/prompts/blog_draft.j2 #}
Write a science blog post about the following research paper.

## Paper Information
- **Title:** {{ title }}
- **Authors:** {{ authors | join(', ') }}
- **Category:** {{ iaifi_category }}

## Abstract
{{ abstract }}

## Paper Content (excerpt)
{{ paper_content }}

## Instructions
Write an 800-1500 word blog post with the following structure:

### Overview (2-3 paragraphs)
Start with a broad, accessible explanation of what this research is about.
Use analogies and everyday language. A scientifically curious non-expert
should understand this section fully.

### Key Highlights (2-3 paragraphs)
Describe the main findings, methods, or innovations. You can introduce
technical terms here but always explain them on first use. Be specific
about what makes this work novel or interesting.

### Impact and Implications (1-2 paragraphs)
What does this mean for the field? How might it affect future research
in AI and/or fundamental physics? Connect it to broader scientific goals.

Important:
- Start accessible, then gradually increase technical depth
- Never fabricate results or claims not supported by the paper
- Use active voice and present tense where natural
- Include specific numbers, methods, or results from the paper
```

### Database Schema Extensions
```sql
-- New tables for Phase 2

CREATE TABLE IF NOT EXISTS blog_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_arxiv_id TEXT NOT NULL REFERENCES papers(arxiv_id),
    title TEXT NOT NULL,
    slug TEXT NOT NULL UNIQUE,
    content TEXT NOT NULL,
    word_count INTEGER NOT NULL,
    llm_model TEXT NOT NULL,
    generation_cost REAL DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'draft',
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS figures (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_arxiv_id TEXT NOT NULL REFERENCES papers(arxiv_id),
    figure_path TEXT NOT NULL,
    page_number INTEGER NOT NULL,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL,
    extraction_type TEXT NOT NULL,  -- 'raster' or 'vector'
    sort_order INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS concepts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_arxiv_id TEXT NOT NULL REFERENCES papers(arxiv_id),
    name TEXT NOT NULL,
    description TEXT,
    relevance REAL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_blog_posts_paper ON blog_posts(paper_arxiv_id);
CREATE INDEX IF NOT EXISTS idx_blog_posts_status ON blog_posts(status);
CREATE INDEX IF NOT EXISTS idx_figures_paper ON figures(paper_arxiv_id);
CREATE INDEX IF NOT EXISTS idx_concepts_paper ON concepts(paper_arxiv_id);
CREATE INDEX IF NOT EXISTS idx_concepts_name ON concepts(name);
```

### Concept JSON Export for Visualization
```python
# Source: Architecture research (graph.json contract)
import json

def export_concepts_json(papers_with_concepts: list[dict], output_path: str):
    """Export concept data as JSON for network visualization."""
    concept_counts: dict[str, int] = {}
    paper_concepts: dict[str, list[str]] = {}

    for paper in papers_with_concepts:
        arxiv_id = paper["arxiv_id"]
        concepts = [c["name"] for c in paper["concepts"]]
        paper_concepts[arxiv_id] = concepts
        for concept in concepts:
            concept_counts[concept] = concept_counts.get(concept, 0) + 1

    # Build graph data structure
    nodes = [
        {
            "id": p["arxiv_id"],
            "title": p["title"],
            "date": p.get("published", ""),
            "category": p.get("iaifi_category", ""),
            "url": f"/posts/{p['arxiv_id']}",
        }
        for p in papers_with_concepts
    ]

    # Build edges: papers sharing concepts
    links = []
    paper_ids = list(paper_concepts.keys())
    for i in range(len(paper_ids)):
        for j in range(i + 1, len(paper_ids)):
            shared = set(paper_concepts[paper_ids[i]]) & set(paper_concepts[paper_ids[j]])
            if shared:
                links.append({
                    "source": paper_ids[i],
                    "target": paper_ids[j],
                    "concepts": sorted(shared),
                    "weight": len(shared),
                })

    graph_data = {
        "nodes": nodes,
        "links": links,
        "concepts": [
            {"name": name, "count": count}
            for name, count in sorted(concept_counts.items(), key=lambda x: -x[1])
        ],
    }

    with open(output_path, "w") as f:
        json.dump(graph_data, f, indent=2)
```

### Extended PaperStatus Enum
```python
# pipeline/models.py additions
class PaperStatus(str, Enum):
    DISCOVERED = "discovered"
    METADATA_FETCHED = "metadata_fetched"
    PDF_DOWNLOADED = "pdf_downloaded"
    INGESTION_COMPLETE = "ingestion_complete"
    # Phase 2 additions:
    FIGURES_EXTRACTED = "figures_extracted"
    CONCEPTS_EXTRACTED = "concepts_extracted"
    POST_GENERATED = "post_generated"
    POST_REVIEWED = "post_reviewed"      # Phase 3 will use this
    PUBLISHED = "published"              # Phase 4 will use this
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Direct OpenAI SDK calls | LiteLLM unified interface | 2024-2025 | Switch providers by changing model string. No code changes needed. |
| JSON mode (`{"type": "json_object"}`) | Structured output with json_schema + Pydantic | 2024-2025 | Schema-enforced output. LLMs respect field types, constraints, required fields. |
| pdfminer/pdfplumber for academic PDFs | pymupdf4llm for LLM-ready markdown | 2025-2026 | Preserves reading order, handles multi-column, detects headers. Purpose-built for LLM consumption. |
| Page-to-image for figure extraction | cluster_drawings() for vector graphics | 2024-2025 | Extracts individual figures instead of whole pages. Handles LaTeX-rendered vector figures. |
| Single-shot LLM generation | Multi-pass refinement chains | 2024-2025 | Dramatically better quality through iterative improvement. Each pass has focused objective. |

**Deprecated/outdated:**
- `pymupdf4llm` < 0.2.0: No layout support. Upgrade to 0.3.4+.
- LiteLLM `response_format={"type": "json_object"}`: Still works but prefer `response_format=PydanticModel` for schema enforcement.
- `@astrojs/tailwind` integration: Deprecated for Tailwind v4. Use `@tailwindcss/vite` directly (relevant for Phase 4).

## Open Questions

1. **Optimal PDF text truncation strategy**
   - What we know: First 8000-10000 chars covers abstract + intro for most papers. pymupdf4llm `page_chunks=True` can return per-page data.
   - What's unclear: Whether to include conclusion section (at end of PDF) in addition to intro. Whether page_chunks is more reliable than character truncation.
   - Recommendation: Start with simple character truncation. If quality is poor for longer papers, try extracting first 3 pages + last page.

2. **Concept deduplication across papers**
   - What we know: LLMs will extract similar concepts with slight wording variations ("neural network" vs "neural networks" vs "deep neural network").
   - What's unclear: Whether to normalize at extraction time or as a post-processing step. How aggressively to deduplicate.
   - Recommendation: Extract as-is, then apply a normalization pass (lowercase, singularize, group synonyms). Consider an LLM pass to merge similar concepts across the corpus after initial extraction.

3. **LLM cost per paper**
   - What we know: 3 passes for blog post + 1 for concept extraction = 4 LLM calls per paper. At Claude Sonnet pricing (~$3/M input, $15/M output), rough estimate is $0.05-0.15 per paper.
   - What's unclear: Exact token counts after prompt templates are finalized.
   - Recommendation: Use LiteLLM cost tracking to measure actual costs. Enable disk caching to avoid re-paying during development/iteration.

4. **Raster image format handling**
   - What we know: PyMuPDF `extract_image()` returns images in their original format (JPEG, PNG, JBIG2, etc.). Some formats may not display well in browsers.
   - What's unclear: Whether to convert all extracted images to PNG or keep originals.
   - Recommendation: Convert all figures to PNG using Pillow for consistent web display.

## Sources

### Primary (HIGH confidence)
- [LiteLLM Structured Outputs Docs](https://docs.litellm.ai/docs/completion/json_mode) - JSON mode, Pydantic support, provider compatibility
- [LiteLLM Async Completion Docs](https://docs.litellm.ai/docs/completion/stream) - `acompletion()` API, async streaming
- [LiteLLM Caching Docs](https://docs.litellm.ai/docs/caching/all_caches) - Disk cache, in-memory cache, per-request control
- [LiteLLM Provider: Anthropic](https://docs.litellm.ai/docs/providers/anthropic) - Claude model names, structured output support
- [LiteLLM API Key Configuration](https://docs.litellm.ai/docs/set_keys) - Environment variables for all providers
- [LiteLLM Cost Tracking](https://docs.litellm.ai/docs/completion/token_usage) - `response_cost`, `completion_cost()`
- [PyMuPDF Image Extraction Docs](https://pymupdf.readthedocs.io/en/latest/recipes-images.html) - `get_images()`, `extract_image()`, mask handling
- [pymupdf4llm API Reference](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/api.html) - `to_markdown()` full parameter list
- [pymupdf4llm PyPI](https://pypi.org/project/pymupdf4llm/) - Version 0.3.4, released Feb 2026
- [PyMuPDF PyPI](https://pypi.org/project/PyMuPDF/) - Version 1.27.1, released Feb 2026

### Secondary (MEDIUM confidence)
- [PyMuPDF Discussion #4584](https://github.com/pymupdf/PyMuPDF/discussions/4584) - Academic PDF figure extraction with `cluster_drawings()`; verified approach from maintainer
- [pymupdf4llm Issue #352](https://github.com/pymupdf/pymupdf4llm/issues/352) - `image_path` bug when `pymupdf.layout` is active; confirmed open issue
- [Pydantic for LLM Outputs Guide](https://pydantic.dev/articles/llm-intro) - Schema generation, validation patterns
- [Simon Willison: LLM Structured Extraction](https://simonwillison.net/2025/Feb/28/llm-schemas/) - Pydantic schema best practices
- [Jinja2 Prompt Templates Guide](https://blog.promptlayer.com/prompt-templates-with-jinja2-2/) - Jinja2 for prompt management

### Tertiary (LOW confidence)
- [PDFFigures 2.0](https://dl.acm.org/doi/10.1145/2910896.2910904) - Academic figure extraction algorithms (Java-based, not directly applicable but informs scoring heuristics)
- Multi-pass generation pattern (journalist-reader-editor) - Based on general prompt engineering best practices; no single authoritative source. Pattern is well-established in content generation workflows but not formally documented under this name.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - LiteLLM, PyMuPDF, pymupdf4llm all verified with official docs, current versions confirmed on PyPI
- Architecture: HIGH - Patterns derive from existing Phase 1 codebase + official library examples
- Figure extraction: MEDIUM-HIGH - Dual strategy verified from maintainer discussion; `cluster_drawings()` API confirmed but no formal tutorial
- Multi-pass generation: MEDIUM - Pattern is sound but "journalist-reader-editor" naming is informal; prompt quality depends on iteration
- Concept extraction: MEDIUM - Structured output via Pydantic is well-documented; quality of extraction depends on prompt engineering
- Pitfalls: HIGH - All pitfalls verified through official issues, docs, or known library behaviors

**Research date:** 2026-03-03
**Valid until:** 2026-04-03 (30 days - stack is stable, LiteLLM releases frequently but API is stable)
