# Phase 4: Static Site and Timeline - Research

**Researched:** 2026-03-03
**Domain:** Static site generation with Astro, content collections, client-side search, responsive design
**Confidence:** HIGH

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| SITE-01 | Static site generated from approved content (deployable to GitHub Pages/Netlify/Vercel) | Astro 5.x with custom content loader from SQLite; GitHub Pages deployment via official `withastro/action@v5`; build output to `dist/` |
| SITE-03 | Chronological timeline feed with paper cards | Astro content collection with `getCollection()` sorted by `published` date; PostCard component with theme color coding |
| SITE-04 | Individual blog post pages with full content, figures, and metadata | Dynamic routes via `[...slug].astro` + `getStaticPaths()`; MDX rendering with `render()`; figures from `public/figures/` |
| SITE-05 | IAIFI theme filtering on both timeline view | Client-side JavaScript filtering on timeline page using `data-pagefind-filter` for search integration; vanilla JS filter buttons for timeline |
| SITE-06 | Client-side search across posts (title, concepts, authors) | Pagefind 1.4.0 with `data-pagefind-meta` for authors/concepts, `data-pagefind-filter` for themes, custom search UI |
| SITE-07 | Responsive design (mobile-friendly) | Tailwind CSS 4.2 via `@tailwindcss/vite` plugin; mobile-first approach with responsive breakpoints |
| SITE-08 | Paper metadata display (authors, arxiv link, date, abstract) | Frontmatter schema with all metadata fields; PostMetadata component rendering authors, arXiv link, date, abstract |
</phase_requirements>

## Summary

Phase 4 builds the public-facing static site that renders approved blog posts from the existing SQLite database into a deployable static site. The architecture centers on Astro 5.x with a custom content loader that reads approved posts directly from the SQLite database at build time, eliminating the need for a separate file-export step. This is the cleanest approach because it uses Astro's Content Layer API (introduced in v5.0) to define a loader function that queries the database, validates entries against a Zod schema, and populates the content store -- all within the standard Astro build pipeline.

The site consists of three page types: a chronological timeline feed (home page) showing paper cards sorted by publication date with IAIFI theme filtering, individual blog post pages rendering the full markdown content with figures and paper metadata, and a search results page powered by Pagefind. Tailwind CSS v4.2 provides styling via the Vite plugin (the old `@astrojs/tailwind` integration is deprecated for v4). Pagefind provides client-side search by indexing the built HTML after the Astro build completes, requiring zero server infrastructure. The site deploys to GitHub Pages, Netlify, or Vercel with no server runtime.

The critical architectural decision is how to bridge the Python/SQLite backend (Phases 1-3) to the Astro frontend. Two approaches exist: (1) a Python export script that writes markdown files with YAML frontmatter to `site/src/content/posts/`, or (2) a custom Astro content loader that reads SQLite directly at build time using `better-sqlite3`. Approach (2) is recommended because it eliminates a separate export step, keeps content collections as the single source of truth, and leverages Astro's built-in schema validation. However, Approach (1) is simpler and avoids Node.js SQLite dependencies. Both are documented below so the planner can choose based on implementation complexity.

**Primary recommendation:** Use Astro 5.x with a Python export script that writes markdown files + YAML frontmatter from the SQLite database, Tailwind CSS 4.2 via Vite plugin, Pagefind 1.4 for client-side search, and deploy to GitHub Pages with the official Astro GitHub Action.

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| Astro | 5.18.x | Static site generation, content collections, page routing | Leading SSG for content sites; zero JS by default; Content Layer API for type-safe collections; 5x faster Markdown builds in v5 |
| Tailwind CSS | 4.2.x | Utility-first CSS framework | Mobile-first responsive design; v4 uses Vite plugin instead of PostCSS; `@import "tailwindcss"` replaces config file |
| @tailwindcss/vite | 4.2.x | Tailwind integration for Astro/Vite | Official v4 integration method; replaces deprecated `@astrojs/tailwind` |
| @astrojs/mdx | latest | MDX support in content collections | Enables component usage in blog posts; works with glob loader for `.md` and `.mdx` files |
| Pagefind | 1.4.0 | Client-side static search | Zero-server search; indexes HTML post-build; chunked index loads only needed fragments; supports filtering and metadata |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| @astrojs/sitemap | latest | Generate sitemap.xml | Always; SEO requirement for any public site |
| sharp | latest | Image optimization | Astro's default image service for optimizing figures |
| npm-run-all | latest | Sequential build scripts | Chain `astro build` then `pagefind` indexing |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Pagefind | Lunr.js / Fuse.js | Pagefind auto-indexes HTML (no manual index); Lunr requires building index manually; Fuse.js is fuzzy-only with no pagination |
| Tailwind CSS | Plain CSS / vanilla CSS | Tailwind provides responsive utilities, consistent design system, rapid prototyping; plain CSS is more maintenance for responsive layouts |
| Python export script | Custom Astro content loader (better-sqlite3) | Content loader is architecturally cleaner but adds Node.js SQLite dependency and more complex debugging; export script is simpler and keeps Python/Node concerns fully separated |
| MDX | Plain Markdown | MDX allows embedding components (e.g., figure galleries, metadata cards); plain Markdown is simpler but limits interactive elements within posts |

**Installation:**
```bash
# Create Astro project in site/ directory
npm create astro@latest site -- --template minimal
cd site

# Install core dependencies
npm install @astrojs/mdx @astrojs/sitemap
npm install tailwindcss @tailwindcss/vite

# Install dev dependencies
npm install -D pagefind npm-run-all
```

## Architecture Patterns

### Recommended Project Structure
```
site/
├── astro.config.mjs          # Astro + Tailwind vite plugin config
├── src/
│   ├── content/
│   │   └── posts/            # Exported markdown blog posts (from Python script)
│   │       ├── paper-slug-1.md
│   │       └── paper-slug-2.md
│   ├── content.config.ts     # Content collection schema (Zod validation)
│   ├── components/
│   │   ├── PostCard.astro    # Paper card for timeline feed
│   │   ├── PostMetadata.astro # Authors, arXiv link, date, abstract
│   │   ├── ThemeFilter.astro  # IAIFI theme filter buttons
│   │   ├── SearchBar.astro    # Pagefind search UI wrapper
│   │   └── Header.astro       # Site navigation header
│   ├── layouts/
│   │   ├── BaseLayout.astro   # HTML shell, head, global CSS
│   │   └── PostLayout.astro   # Blog post page layout with metadata
│   ├── pages/
│   │   ├── index.astro        # Timeline feed (home page)
│   │   ├── posts/
│   │   │   └── [...slug].astro # Dynamic blog post pages
│   │   └── search.astro       # Search page
│   ├── styles/
│   │   └── global.css         # @import "tailwindcss" + custom styles
│   └── data/                  # Static data files
│       └── themes.json        # IAIFI theme definitions + colors
├── public/
│   └── figures/               # Extracted paper figures (copied from data/figures/)
├── package.json
└── tsconfig.json
```

### Pattern 1: Python Export Script (Database to Content Files)
**What:** A Python script that queries the SQLite database for approved blog posts, joins with paper metadata, figures, and concepts, then writes markdown files with YAML frontmatter to `site/src/content/posts/`.
**When to use:** Before every Astro build. This is the bridge between the Python pipeline and the Astro site.
**Example:**
```python
# pipeline/export.py
# Source: Project-specific pattern based on Astro content collection requirements
import json
import shutil
import sqlite3
from pathlib import Path

def export_approved_posts(db_path: str, site_dir: str) -> int:
    """Export approved blog posts as markdown files for Astro."""
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    posts_dir = Path(site_dir) / "src" / "content" / "posts"
    posts_dir.mkdir(parents=True, exist_ok=True)
    figures_dir = Path(site_dir) / "public" / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    # Clear existing posts to avoid stale content
    for f in posts_dir.glob("*.md"):
        f.unlink()

    cursor = conn.execute("""
        SELECT bp.*, p.authors, p.abstract, p.iaifi_category,
               p.published, p.arxiv_id, p.pdf_url
        FROM blog_posts bp
        JOIN papers p ON bp.paper_arxiv_id = p.arxiv_id
        WHERE bp.status = 'approved'
        ORDER BY p.published DESC
    """)

    count = 0
    for row in cursor:
        arxiv_id = row["arxiv_id"]
        authors = json.loads(row["authors"])

        # Get concepts for this paper
        concepts_cursor = conn.execute(
            "SELECT name, description, relevance FROM concepts "
            "WHERE paper_arxiv_id = ? ORDER BY relevance DESC",
            (arxiv_id,),
        )
        concepts = [dict(c) for c in concepts_cursor]

        # Get figures for this paper
        figures_cursor = conn.execute(
            "SELECT figure_path FROM figures "
            "WHERE paper_arxiv_id = ? ORDER BY sort_order",
            (arxiv_id,),
        )
        figure_paths = [dict(f)["figure_path"] for f in figures_cursor]

        # Copy figures to site/public/figures/
        figure_urls = []
        for fig_path in figure_paths:
            src = Path(fig_path)
            if src.exists():
                dest = figures_dir / src.name
                shutil.copy2(src, dest)
                figure_urls.append(f"/figures/{src.name}")

        # Write frontmatter + content
        frontmatter = {
            "title": row["title"],
            "arxivId": arxiv_id,
            "authors": authors,
            "abstract": row["abstract"],
            "theme": row["iaifi_category"],
            "published": row["published"],
            "arxivUrl": f"https://arxiv.org/abs/{arxiv_id}",
            "pdfUrl": row["pdf_url"] or f"https://arxiv.org/pdf/{arxiv_id}",
            "concepts": [c["name"] for c in concepts],
            "figures": figure_urls,
            "wordCount": row["word_count"],
        }

        # Write as YAML frontmatter + markdown body
        import yaml
        md_content = f"---\n{yaml.dump(frontmatter, default_flow_style=False)}---\n\n{row['content']}"

        output_path = posts_dir / f"{row['slug']}.md"
        output_path.write_text(md_content)
        count += 1

    conn.close()
    return count
```

### Pattern 2: Content Collection Schema with Zod
**What:** Define a typed schema for blog post frontmatter that Astro validates at build time. This catches data errors early.
**When to use:** Always. This is the foundation of type-safe content collections.
**Example:**
```typescript
// site/src/content.config.ts
// Source: https://docs.astro.build/en/guides/content-collections/
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const posts = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/posts" }),
  schema: z.object({
    title: z.string(),
    arxivId: z.string(),
    authors: z.array(z.string()),
    abstract: z.string(),
    theme: z.enum([
      "Foundational AI",
      "Theoretical Physics",
      "Experimental Physics",
      "Astrophysics",
    ]),
    published: z.coerce.date(),
    arxivUrl: z.string().url(),
    pdfUrl: z.string().url(),
    concepts: z.array(z.string()),
    figures: z.array(z.string()).default([]),
    wordCount: z.number(),
  }),
});

export const collections = { posts };
```

### Pattern 3: Dynamic Blog Post Pages with getStaticPaths
**What:** Generate one page per blog post at build time using Astro's dynamic routing.
**When to use:** For the `[...slug].astro` page that renders individual blog posts.
**Example:**
```astro
---
// site/src/pages/posts/[...slug].astro
// Source: https://docs.astro.build/en/guides/routing/
import { getCollection, render } from 'astro:content';
import PostLayout from '../../layouts/PostLayout.astro';

export async function getStaticPaths() {
  const posts = await getCollection('posts');
  return posts.map((post) => ({
    params: { slug: post.id },
    props: { post },
  }));
}

const { post } = Astro.props;
const { Content } = await render(post);
---
<PostLayout
  title={post.data.title}
  authors={post.data.authors}
  arxivUrl={post.data.arxivUrl}
  theme={post.data.theme}
  published={post.data.published}
  abstract={post.data.abstract}
  figures={post.data.figures}
  concepts={post.data.concepts}
>
  <Content />
</PostLayout>
```

### Pattern 4: Timeline Feed with Theme Filtering
**What:** Home page renders all posts as cards sorted by date, with client-side filtering by IAIFI theme.
**When to use:** For the main timeline/index page.
**Example:**
```astro
---
// site/src/pages/index.astro
import { getCollection } from 'astro:content';
import BaseLayout from '../layouts/BaseLayout.astro';
import PostCard from '../components/PostCard.astro';
import ThemeFilter from '../components/ThemeFilter.astro';

const posts = await getCollection('posts');
const sortedPosts = posts.sort(
  (a, b) => b.data.published.getTime() - a.data.published.getTime()
);
---
<BaseLayout title="IAIFI Research Blog">
  <ThemeFilter />
  <div id="timeline" class="space-y-6">
    {sortedPosts.map((post) => (
      <PostCard post={post} />
    ))}
  </div>
</BaseLayout>
```

### Pattern 5: Pagefind Integration with Custom Metadata and Filters
**What:** Add Pagefind data attributes to blog post pages so search indexes authors, concepts, and themes.
**When to use:** On every blog post page. Pagefind reads these attributes from the built HTML.
**Example:**
```astro
<!-- In PostLayout.astro -->
<article data-pagefind-body>
  <h1 data-pagefind-meta="title">{title}</h1>
  <span data-pagefind-filter="theme">{theme}</span>
  <span data-pagefind-meta="authors">{authors.join(', ')}</span>
  {concepts.map((c) => (
    <span data-pagefind-meta="concepts" class="hidden">{c}</span>
  ))}
  <time data-pagefind-meta="date" datetime={published.toISOString()}>
    {published.toLocaleDateString()}
  </time>
  <slot />
</article>
```

### Anti-Patterns to Avoid
- **Server-side rendering for a content blog:** Astro defaults to static output. Do NOT add `output: 'server'` -- this site has no dynamic data needs at runtime. All content is known at build time.
- **Importing Astro's old @astrojs/tailwind integration:** This is deprecated for Tailwind CSS v4. Use `@tailwindcss/vite` plugin in the Vite config instead.
- **Building a custom search engine:** Pagefind handles tokenization, indexing, chunking, and progressive loading. Do not build a custom inverted index.
- **Storing rendered HTML in the database:** The database stores raw markdown. Astro renders it at build time. Do not pre-render HTML in Python.
- **Using `src/pages/posts/[slug].astro` (single bracket):** Use `[...slug].astro` (rest parameter) to support nested slugs and avoid 404 issues with slugs containing slashes.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Client-side search | Custom inverted index, Trie, or fuzzy matcher | Pagefind 1.4 | Pagefind auto-indexes HTML, chunks the index for bandwidth efficiency, supports metadata and filtering, handles CJK tokenization |
| Responsive CSS | Custom media queries from scratch | Tailwind CSS 4.2 responsive utilities | Consistent breakpoints, mobile-first by default, utility classes like `md:grid-cols-2 lg:grid-cols-3` |
| Markdown rendering | Custom markdown-to-HTML pipeline | Astro content collections + MDX | Astro handles remark/rehype plugins, syntax highlighting, heading extraction, frontmatter parsing |
| Static page generation | Custom template engine | Astro pages + `getStaticPaths()` | Astro generates optimal static HTML with zero JS by default, handles routing, generates sitemap |
| Content validation | Manual frontmatter checking | Zod schema in `content.config.ts` | Type-safe validation at build time, auto-generates TypeScript types, catches data errors before deploy |
| Image optimization | Manual resize/compress pipeline | Astro's built-in Image service (sharp) | Automatic format conversion, responsive srcset, layout shift prevention |
| Build pipeline (search index) | Manual post-build scripts | npm-run-all with `build:astro` then `build:pagefind` | Sequential execution, cross-platform, declarative in package.json |

**Key insight:** The entire static site layer is "build and serve static files." Every component has a mature, well-documented solution. The only custom code needed is the export script bridging Python/SQLite to Astro content files, and the Astro components/layouts themselves.

## Common Pitfalls

### Pitfall 1: Tailwind CSS v4 Integration Mismatch
**What goes wrong:** Using `@astrojs/tailwind` (the old Astro integration) with Tailwind CSS v4, which results in build errors or no styles applied.
**Why it happens:** Tailwind CSS v4 fundamentally changed its integration approach from PostCSS-based to Vite plugin-based. The old `@astrojs/tailwind` package only supports v3.
**How to avoid:** Install `tailwindcss` and `@tailwindcss/vite`, add the Vite plugin in `astro.config.mjs`, create `src/styles/global.css` with `@import "tailwindcss"`, and import this CSS file in your base layout. Do NOT install `@astrojs/tailwind`.
**Warning signs:** `Cannot find module '@tailwindcss/...'` errors, styles not applying, `tailwind.config.js` being required (v4 does not use a config file by default).

### Pitfall 2: Stale Content After Pipeline Changes
**What goes wrong:** Astro builds with old content because the export script was not run before the build, or old markdown files remain from deleted/rejected posts.
**Why it happens:** The export script and Astro build are separate processes. If someone runs `astro build` without first running the export, the site renders stale content.
**How to avoid:** Create a single `npm run build` command that chains: `python -m pipeline.export && astro build && npx pagefind --site dist`. Clear the `src/content/posts/` directory at the start of every export to remove stale files.
**Warning signs:** Post count on site does not match approved count in admin, rejected posts still visible.

### Pitfall 3: Pagefind Not Indexing Content
**What goes wrong:** Search returns no results or missing results because Pagefind could not find content to index.
**Why it happens:** Pagefind indexes the built HTML in `dist/`. If the build output structure is unexpected, or if `data-pagefind-body` is not set, Pagefind may index navigation/footer text instead of post content.
**How to avoid:** Add `data-pagefind-body` to the main `<article>` element on post pages. Run Pagefind AFTER `astro build` completes. Verify index size in Pagefind output.
**Warning signs:** Pagefind reports 0 pages indexed, search returns irrelevant snippets from header/footer.

### Pitfall 4: Figure Paths Breaking Between Environments
**What goes wrong:** Figures display in development but 404 in production, or vice versa.
**Why it happens:** Figures are stored in `data/figures/` by the Python pipeline but need to be in `site/public/figures/` for Astro. Path mismatches between the admin (which serves figures via FastAPI at `/figures/`) and the static site (which serves from `public/figures/`).
**How to avoid:** The export script MUST copy figures from `data/figures/` to `site/public/figures/` and write figure paths in frontmatter as `/figures/filename.png` (root-relative). Use consistent naming conventions.
**Warning signs:** Broken image icons on deployed site, images loading locally but not in production.

### Pitfall 5: GitHub Pages Base Path Issues
**What goes wrong:** CSS, JS, and internal links all 404 on GitHub Pages because the site is served at `/<repo-name>/` instead of `/`.
**Why it happens:** GitHub Pages (for non-`<user>.github.io` repos) serves at a subpath. All assets and links need this base path prepended.
**How to avoid:** Set `site` and `base` in `astro.config.mjs`. Use Astro's built-in path helpers. Test with `astro preview` before deploying.
**Warning signs:** Blank page on GitHub Pages, console shows 404s for all assets.

### Pitfall 6: Pagefind Filter Attributes Not Working for Theme Filtering
**What goes wrong:** Theme filters in Pagefind return no results or all results, because filter values do not match the attribute content.
**Why it happens:** Pagefind filter values are case-sensitive and must exactly match the text content of the element with `data-pagefind-filter`. If the theme is "Foundational AI" in the database but rendered differently in HTML, filters break.
**How to avoid:** Ensure theme values are consistent between the database, frontmatter, and the rendered HTML element that carries `data-pagefind-filter="theme"`. Use the exact enum values from the schema.
**Warning signs:** Filter checkboxes appear but selecting them shows 0 results.

## Code Examples

Verified patterns from official sources:

### Astro Configuration (astro.config.mjs)
```javascript
// Source: https://tailwindcss.com/docs/installation/framework-guides/astro
//         https://docs.astro.build/en/guides/deploy/github/
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://<username>.github.io",
  // base: "/repo-name",  // Only if not using custom domain
  integrations: [mdx(), sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
});
```

### Global CSS File
```css
/* site/src/styles/global.css */
/* Source: https://tailwindcss.com/docs/installation/framework-guides/astro */
@import "tailwindcss";

/* Custom IAIFI theme colors */
@theme {
  --color-theme-ai: #3b82f6;        /* blue-500 */
  --color-theme-theory: #8b5cf6;    /* violet-500 */
  --color-theme-experiment: #f59e0b; /* amber-500 */
  --color-theme-astro: #10b981;     /* emerald-500 */
}
```

### Base Layout with Global CSS Import
```astro
---
// site/src/layouts/BaseLayout.astro
// Source: https://docs.astro.build/en/tutorial/3-components/
import "../styles/global.css";

interface Props {
  title: string;
  description?: string;
}

const { title, description = "IAIFI Research Blog" } = Astro.props;
---
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content={description} />
    <title>{title} | IAIFI Blog</title>
  </head>
  <body class="bg-white text-gray-900 min-h-screen">
    <header class="border-b px-4 py-3">
      <nav class="max-w-4xl mx-auto flex justify-between items-center">
        <a href="/" class="text-xl font-bold">IAIFI Research Blog</a>
        <div class="flex gap-4">
          <a href="/">Timeline</a>
          <a href="/search">Search</a>
        </div>
      </nav>
    </header>
    <main class="max-w-4xl mx-auto px-4 py-8">
      <slot />
    </main>
    <footer class="border-t px-4 py-6 text-center text-sm text-gray-500">
      <p>IAIFI - Institute for Artificial Intelligence and Fundamental Interactions</p>
    </footer>
  </body>
</html>
```

### PostCard Component
```astro
---
// site/src/components/PostCard.astro
interface Props {
  post: {
    id: string;
    data: {
      title: string;
      authors: string[];
      abstract: string;
      theme: string;
      published: Date;
      concepts: string[];
      arxivUrl: string;
    };
  };
}

const { post } = Astro.props;
const themeColors: Record<string, string> = {
  "Foundational AI": "bg-blue-100 text-blue-800",
  "Theoretical Physics": "bg-violet-100 text-violet-800",
  "Experimental Physics": "bg-amber-100 text-amber-800",
  "Astrophysics": "bg-emerald-100 text-emerald-800",
};
const themeClass = themeColors[post.data.theme] || "bg-gray-100 text-gray-800";
---
<article
  class="border rounded-lg p-6 hover:shadow-md transition-shadow"
  data-theme={post.data.theme}
>
  <div class="flex items-center gap-2 mb-2">
    <span class={`text-xs font-medium px-2 py-1 rounded ${themeClass}`}>
      {post.data.theme}
    </span>
    <time class="text-sm text-gray-500" datetime={post.data.published.toISOString()}>
      {post.data.published.toLocaleDateString("en-US", {
        year: "numeric", month: "long", day: "numeric"
      })}
    </time>
  </div>
  <h2 class="text-xl font-semibold mb-2">
    <a href={`/posts/${post.id}`} class="hover:text-blue-600">
      {post.data.title}
    </a>
  </h2>
  <p class="text-sm text-gray-600 mb-2">
    {post.data.authors.slice(0, 3).join(", ")}
    {post.data.authors.length > 3 && ` et al.`}
  </p>
  <p class="text-gray-700 line-clamp-3">{post.data.abstract}</p>
  <div class="mt-3 flex flex-wrap gap-1">
    {post.data.concepts.slice(0, 5).map((concept) => (
      <span class="text-xs bg-gray-100 text-gray-600 px-2 py-0.5 rounded">
        {concept}
      </span>
    ))}
  </div>
</article>
```

### Theme Filter Component (Client-Side)
```astro
---
// site/src/components/ThemeFilter.astro
const themes = [
  { name: "All", value: "all" },
  { name: "Foundational AI", value: "Foundational AI" },
  { name: "Theoretical Physics", value: "Theoretical Physics" },
  { name: "Experimental Physics", value: "Experimental Physics" },
  { name: "Astrophysics", value: "Astrophysics" },
];
---
<div class="flex flex-wrap gap-2 mb-6" id="theme-filters">
  {themes.map((theme) => (
    <button
      class="px-3 py-1.5 rounded-full text-sm font-medium border transition-colors
             data-[active]:bg-gray-900 data-[active]:text-white"
      data-filter={theme.value}
      data-active={theme.value === "all" ? "" : undefined}
    >
      {theme.name}
    </button>
  ))}
</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll("#theme-filters button");
    const cards = document.querySelectorAll("#timeline article");

    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const filter = btn.getAttribute("data-filter");

        // Update active state
        buttons.forEach((b) => b.removeAttribute("data-active"));
        btn.setAttribute("data-active", "");

        // Filter cards
        cards.forEach((card) => {
          if (filter === "all" || card.getAttribute("data-theme") === filter) {
            (card as HTMLElement).style.display = "";
          } else {
            (card as HTMLElement).style.display = "none";
          }
        });
      });
    });
  });
</script>
```

### Search Page with Pagefind
```astro
---
// site/src/pages/search.astro
import BaseLayout from "../layouts/BaseLayout.astro";
---
<BaseLayout title="Search">
  <h1 class="text-2xl font-bold mb-6">Search Papers</h1>
  <div id="search-container"></div>
  <link rel="stylesheet" href="/pagefind/pagefind-ui.css" />
  <script is:inline src="/pagefind/pagefind-ui.js"></script>
  <script is:inline>
    window.addEventListener("DOMContentLoaded", () => {
      new PagefindUI({
        element: "#search-container",
        showSubResults: true,
        showImages: false,
      });
    });
  </script>
</BaseLayout>
```

### Build Script (package.json)
```json
{
  "scripts": {
    "export": "cd .. && python -m pipeline.export",
    "build:astro": "astro build",
    "build:search": "npx pagefind --site dist",
    "build": "npm-run-all -s export build:astro build:search",
    "dev": "astro dev",
    "preview": "astro preview"
  }
}
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| `@astrojs/tailwind` integration | `@tailwindcss/vite` plugin | Tailwind CSS v4 (Jan 2025) | Must use Vite plugin config, not Astro integration. No `tailwind.config.js` needed in v4. |
| `src/content/config.ts` in content dir | `src/content.config.ts` at project root | Astro 5.0 (Dec 2024) | Content config moved to project root. Uses `glob()` and `file()` loaders. |
| `entry.render()` method | `render(entry)` function import | Astro 5.0 (Dec 2024) | Import `render` from `astro:content` instead of calling `.render()` on entry. |
| Legacy content collections (file-based) | Content Layer API with loaders | Astro 5.0 (Dec 2024) | Collections now use explicit loaders (`glob`, `file`, or custom). Much faster builds. |
| Lunr.js / custom search | Pagefind | Pagefind 1.0 (2023) | Pagefind auto-indexes HTML, no manual index building needed. Lower bandwidth than Lunr. |
| Astro 5.x stable | Astro 6.0 beta available | Jan 2026 | Astro 6 is beta; use 5.18.x for production stability. |

**Deprecated/outdated:**
- `@astrojs/tailwind`: Deprecated for Tailwind v4; only for legacy v3 projects
- `entry.render()`: Replaced by `render(entry)` function in Astro 5.0
- `src/content/config.ts`: Moved to `src/content.config.ts` (project root) in Astro 5.0
- Content collections without loaders: Must now specify a loader (`glob`, `file`, or custom)

## Open Questions

1. **Export script vs. custom content loader**
   - What we know: Both approaches work. Python export script writes .md files with YAML frontmatter. Custom Astro loader can read SQLite via `better-sqlite3`.
   - What's unclear: Whether `better-sqlite3` (Node.js) can reliably read the same SQLite database that Python writes with WAL mode enabled. Cross-process SQLite concurrency requires careful handling.
   - Recommendation: Use the Python export script approach. It is simpler, keeps the Python/Node boundary clean, and avoids Node.js native dependency complications. The export script runs before `astro build`, so there is no concurrency issue.

2. **Figure naming conflicts**
   - What we know: Figures are stored in `data/figures/` with paths like `data/figures/figure_2401.12345_p3_0.png`. The export script copies them to `site/public/figures/`.
   - What's unclear: Whether figures from different papers could have name collisions if paper-specific subdirectories are not used.
   - Recommendation: Use paper-specific subdirectories: `site/public/figures/{arxiv_id}/`. This prevents collisions and groups figures logically.

3. **Pagination for timeline at scale**
   - What we know: IAIFI currently has ~554 papers. If all were approved, that is a long single page.
   - What's unclear: Whether Astro's built-in pagination should be used now or deferred.
   - Recommendation: Start without pagination (render all cards). The 554 paper count is manageable with lazy loading/virtual scrolling. Add pagination in Phase 7 if needed.

4. **MDX vs plain Markdown for blog posts**
   - What we know: Blog posts are LLM-generated markdown stored in the database. They do not contain JSX components.
   - What's unclear: Whether any post content needs interactive components.
   - Recommendation: Use plain Markdown (`.md`) for exported posts. Install `@astrojs/mdx` for future flexibility but do not require it now. The glob loader handles both `.md` and `.mdx` files.

## Sources

### Primary (HIGH confidence)
- [Astro Content Collections docs](https://docs.astro.build/en/guides/content-collections/) - Content Layer API, glob loader, Zod schema, getCollection(), render()
- [Astro Content Loader API Reference](https://docs.astro.build/en/reference/content-loader-reference/) - Custom loader interface, store.set API, meta store for caching
- [Astro MDX Integration docs](https://docs.astro.build/en/guides/integrations-guide/mdx/) - Installation, content collection usage, render()
- [Astro GitHub Pages Deployment](https://docs.astro.build/en/guides/deploy/github/) - site/base config, GitHub Action workflow
- [Tailwind CSS v4 Astro Setup](https://tailwindcss.com/docs/installation/framework-guides/astro) - @tailwindcss/vite plugin, CSS import, astro.config.mjs
- [Pagefind Getting Started](https://pagefind.app/docs/) - Installation, indexing, default UI
- [Pagefind Metadata](https://pagefind.app/docs/metadata/) - data-pagefind-meta attribute, inline and attribute-based metadata
- [Pagefind Filtering](https://pagefind.app/docs/filtering/) - data-pagefind-filter attribute, filter API
- [Astro Content Layer Deep Dive](https://astro.build/blog/content-layer-deep-dive/) - Inline vs object loaders, store API, metadata persistence

### Secondary (MEDIUM confidence)
- [Astro 5.0 Release Blog](https://astro.build/blog/astro-5/) - Content Layer API, 5x faster Markdown builds, breaking changes
- [Pagefind + Astro Integration Guide](https://syntackle.com/blog/pagefind-search-in-astro-site/) - Build scripts, pagefind.yml, custom API usage
- [Pagefind Filtering in Astro](https://younagi.dev/blog/astro-with-pagefind-filtering-search/) - Custom filter UI with data-pagefind-filter, JavaScript search API
- [Astro Routing docs](https://docs.astro.build/en/guides/routing/) - getStaticPaths, dynamic routes, rest parameters
- [Astro GitHub Releases](https://github.com/withastro/astro/releases) - Current version 5.18.0

### Tertiary (LOW confidence)
- [Astro 6 Beta announcement](https://astro.build/blog/astro-6-beta/) - Astro 6 features (NOT recommended for this project; use stable 5.x)
- Tailwind v4 custom `@theme` directive usage patterns -- based on training data and official blog, not verified against current docs

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - All versions verified via npm/official docs; Astro 5.18.x, Tailwind 4.2.x, Pagefind 1.4.0
- Architecture: HIGH - Content collections, dynamic routes, and Pagefind integration are well-documented standard Astro patterns
- Export bridge: MEDIUM - The Python export script is a custom pattern; the approach is sound but requires careful implementation of the frontmatter format
- Pitfalls: HIGH - All pitfalls verified against official docs (Tailwind v4 migration, Astro v5 breaking changes, Pagefind indexing)

**Research date:** 2026-03-03
**Valid until:** 2026-04-03 (30 days; Astro and Tailwind are stable releases)
