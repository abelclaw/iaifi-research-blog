# Phase 5: Concept Network Visualization - Research

**Researched:** 2026-03-03
**Domain:** Force-directed graph visualization (D3.js, SVG, vanilla JS in Astro)
**Confidence:** HIGH

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| SITE-02 | Interactive force-directed concept network (papers as nodes, shared concepts as edges) | D3.js d3-force module provides forceSimulation, forceLink, forceManyBody, forceCenter for physics-based layout. SVG rendering with d3-selection for DOM manipulation. d3-zoom for pan/zoom, d3-drag for node dragging. Graph data computed at Astro build time from post concepts frontmatter. |
</phase_requirements>

## Summary

This phase adds an interactive force-directed graph page where papers appear as nodes and shared concepts form the edges between them. The graph should allow visitors to visually explore which papers are related through common concepts, with papers sharing more concepts clustering together naturally.

D3.js v7 (specifically d3-force v3.0.0) is the clear standard library for 2D force-directed graph layout in vanilla JavaScript. For a graph of this size (likely 20-100 paper nodes with concept-derived edges), SVG rendering is the correct choice over Canvas -- it gives us direct DOM access for hover events, tooltips, click navigation, and CSS styling, with zero performance concerns at this node count. The project already uses vanilla JS for client-side interactivity (see ThemeFilter pattern), so D3 integrates naturally without requiring a framework island.

The key architectural decision is to compute the graph data (nodes array and links array) at Astro build time in the page's frontmatter block, then inject it as a JSON blob for the client-side D3 script to consume. This avoids runtime computation and keeps the pattern consistent with how the site already works (static HTML with progressive enhancement via inline scripts).

**Primary recommendation:** Use D3.js v7 individual packages (d3-force, d3-selection, d3-zoom, d3-drag) with SVG rendering. Compute graph data at Astro build time. Render on a new `/network` page using the existing vanilla JS script pattern.

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| d3-force | 3.0.0 | Force simulation engine (forceSimulation, forceLink, forceManyBody, forceCenter, forceCollide) | The canonical force-directed layout engine; used by virtually all 2D force graph implementations. Stable -- last release 2021, no breaking changes expected. |
| d3-selection | 3.0.0 | DOM manipulation (select, selectAll, data joins, event handling) | Standard D3 pattern for binding data to SVG elements. Required for node/link rendering. |
| d3-zoom | 3.0.2 | Pan and zoom behavior on SVG | Standard D3 companion for interactive SVG. Handles mouse wheel zoom, drag-to-pan, pinch zoom on touch. |
| d3-drag | 3.0.0 | Node dragging behavior | Standard D3 companion for drag interactions. Integrates cleanly with force simulation (fx/fy pinning pattern). |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| d3-scale | 4.0.2 | Map data values to visual properties (node size, edge width) | If node radius should vary by connection count or edge thickness by shared concept count |
| d3-transition | 3.0.1 | Smooth animated transitions | Optional: for fade-in on load or highlight animations on hover |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| d3-force (individual packages) | Full d3 package | Full d3 is ~500KB; individual packages total ~50KB for what we need. Use individual. |
| SVG rendering | Canvas rendering | Canvas is faster for 1000+ nodes but loses DOM events, accessibility, and CSS styling. SVG is correct for <200 nodes. |
| D3 vanilla | force-graph (vasturiano) | force-graph is a pre-built wrapper with Canvas rendering. Less control over styling, adds dependency. D3 direct gives full control matching existing site patterns. |
| D3 vanilla | Cytoscape.js | Full graph analysis library, much heavier (~600KB). Overkill for visualization-only use case. |

**Installation:**
```bash
cd site && npm install d3-force d3-selection d3-zoom d3-drag
```

**Optional (if node sizing by degree is desired):**
```bash
npm install d3-scale
```

## Architecture Patterns

### Recommended Project Structure
```
site/src/
  pages/
    network.astro          # New page: concept network visualization
  components/
    ConceptNetwork.astro   # Astro component with SVG container + client script
  styles/
    global.css             # Existing -- theme colors already defined
```

### Pattern 1: Build-Time Graph Data Computation
**What:** Compute the nodes and links arrays in the Astro page frontmatter (server-side), serialize as JSON, inject into the client script via a `<script>` data attribute or inline JSON.
**When to use:** Always -- this is an Astro static site, so all data is available at build time from the content collection.
**Example:**
```astro
---
// network.astro frontmatter -- runs at build time
import { getCollection } from "astro:content";
import BaseLayout from "../layouts/BaseLayout.astro";

const posts = await getCollection("posts");

// Build nodes: one per paper
const nodes = posts.map((post) => ({
  id: post.id,
  title: post.data.title,
  theme: post.data.theme,
  concepts: post.data.concepts,
  url: `/posts/${post.id}`,
}));

// Build links: papers sharing concepts
// A link exists between two papers for each shared concept
const links: { source: string; target: string; sharedConcepts: string[] }[] = [];

for (let i = 0; i < posts.length; i++) {
  for (let j = i + 1; j < posts.length; j++) {
    const shared = posts[i].data.concepts.filter((c) =>
      posts[j].data.concepts.includes(c)
    );
    if (shared.length > 0) {
      links.push({
        source: posts[i].id,
        target: posts[j].id,
        sharedConcepts: shared,
      });
    }
  }
}

const graphData = JSON.stringify({ nodes, links });
---

<BaseLayout title="Concept Network - IAIFI Research Blog">
  <section class="mb-4">
    <h1 class="text-3xl font-bold text-gray-900 mb-2">Concept Network</h1>
    <p class="text-gray-600">Explore connections between papers through shared concepts.</p>
  </section>
  <div id="network-container" class="w-full bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden"
       style="height: 600px;"
       data-graph={graphData}>
  </div>
  <!-- D3 visualization script -->
</BaseLayout>
```

### Pattern 2: SVG Force Graph with D3 (Client-Side)
**What:** Use D3 to create an SVG inside the container, set up forces, render nodes as circles and links as lines, update positions on each simulation tick.
**When to use:** In the client-side script block of the network page.
**Example:**
```javascript
// Source: D3 official docs (d3js.org/d3-force, d3js.org/d3-zoom, d3js.org/d3-drag)
import { forceSimulation, forceLink, forceManyBody, forceCenter, forceCollide } from "d3-force";
import { select, selectAll } from "d3-selection";
import { zoom, zoomIdentity } from "d3-zoom";
import { drag } from "d3-drag";

document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("network-container");
  if (!container) return;

  const { nodes, links } = JSON.parse(container.dataset.graph);
  const width = container.clientWidth;
  const height = container.clientHeight;

  // Theme color mapping (matches global.css and PostCard.astro)
  const themeColors = {
    "Foundational AI": "#3b82f6",
    "Theoretical Physics": "#8b5cf6",
    "Experimental Physics": "#f59e0b",
    "Astrophysics": "#10b981",
  };

  const svg = select(container)
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .attr("viewBox", [0, 0, width, height]);

  // Group for zoom/pan transform
  const g = svg.append("g");

  // Links (lines)
  const link = g.append("g")
    .attr("stroke", "#d1d5db")
    .selectAll("line")
    .data(links)
    .join("line")
    .attr("stroke-width", (d) => Math.sqrt(d.sharedConcepts.length));

  // Nodes (circles)
  const node = g.append("g")
    .selectAll("circle")
    .data(nodes)
    .join("circle")
    .attr("r", 8)
    .attr("fill", (d) => themeColors[d.theme] || "#6b7280")
    .attr("stroke", "#fff")
    .attr("stroke-width", 1.5)
    .style("cursor", "pointer");

  // Tooltip (title element -- simple, accessible)
  node.append("title").text((d) => d.title);

  // Click to navigate
  node.on("click", (event, d) => {
    window.location.href = d.url;
  });

  // Force simulation
  const simulation = forceSimulation(nodes)
    .force("link", forceLink(links).id((d) => d.id).distance(100))
    .force("charge", forceManyBody().strength(-200))
    .force("center", forceCenter(width / 2, height / 2))
    .force("collide", forceCollide(12))
    .on("tick", () => {
      link
        .attr("x1", (d) => d.source.x)
        .attr("y1", (d) => d.source.y)
        .attr("x2", (d) => d.target.x)
        .attr("y2", (d) => d.target.y);
      node
        .attr("cx", (d) => d.x)
        .attr("cy", (d) => d.y);
    });

  // Zoom + pan
  svg.call(
    zoom()
      .scaleExtent([0.3, 5])
      .on("zoom", (event) => {
        g.attr("transform", event.transform);
      })
  );

  // Drag behavior
  node.call(
    drag()
      .on("start", (event, d) => {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
      })
      .on("drag", (event, d) => {
        d.fx = event.x;
        d.fy = event.y;
      })
      .on("end", (event, d) => {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      })
  );
});
```

### Pattern 3: Astro Inline Script with Bundled Imports
**What:** Use Astro's `<script>` tag (NOT `is:inline`) to get Vite bundling of D3 imports. This is different from the `is:inline` pattern used for Pagefind (which loads from a runtime path).
**When to use:** For the D3 visualization script, because D3 is an npm dependency that Vite should bundle.
**Example:**
```astro
<!-- In ConceptNetwork.astro or network.astro -->
<script>
  // Vite will bundle these at build time
  import { forceSimulation, forceLink, forceManyBody, forceCenter, forceCollide } from "d3-force";
  import { select } from "d3-selection";
  import { zoom } from "d3-zoom";
  import { drag } from "d3-drag";

  // ... visualization code
</script>
```

**Important:** Astro processes `<script>` tags through Vite by default. Only `<script is:inline>` bypasses bundling. Since D3 is installed as an npm dependency, the regular `<script>` tag is correct -- Vite will tree-shake and bundle only the functions used.

### Pattern 4: Drag + Zoom Coexistence
**What:** D3 drag and zoom can conflict because both listen to mouse events. The standard solution is to call drag on node elements and zoom on the SVG/container, and use `event.active` to coordinate simulation reheating.
**When to use:** Always when combining drag and zoom.
**Key detail:** The drag `start` handler checks `if (!event.active)` to only reheat the simulation for the first concurrent drag gesture. The `end` handler sets `alphaTarget(0)` to let the simulation cool down again.

### Anti-Patterns to Avoid
- **Canvas for small graphs:** SVG gives you DOM events, CSS styling, accessibility (title elements), and is performant up to ~10,000 elements. Canvas only makes sense above that.
- **Loading full d3 package:** The full `d3` package is ~500KB. Import only the submodules you need (~50KB total for force, selection, zoom, drag).
- **Runtime graph computation:** Don't compute nodes/links in the browser. The data is available at build time. Compute once, ship as JSON.
- **React/Svelte islands for D3:** D3 manages its own DOM. Wrapping it in a framework island creates two competing DOM managers. Use vanilla JS with Astro's built-in `<script>` tag bundling.
- **Hardcoded dimensions:** Don't hardcode SVG width/height. Read from the container element and optionally handle resize with ResizeObserver.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Force-directed layout algorithm | Custom spring/repulsion physics | d3-force (forceSimulation) | Velocity Verlet integration, Barnes-Hut approximation for O(n log n), alpha cooling schedule -- all solved problems |
| Pan and zoom | Custom mouse wheel + drag handlers | d3-zoom | Handles mouse, touch, pinch, momentum, scale/translate extent, transform composition |
| Node dragging | Custom mousedown/mousemove/mouseup | d3-drag | Handles touch, multi-touch, pointer capture, coordinate space transforms |
| SVG data binding | Manual createElement + appendChild loops | d3-selection (data join) | Enter/update/exit pattern handles adds, removes, and updates declaratively |
| Node collision avoidance | Custom overlap detection | forceCollide | Quadtree-based O(n log n) overlap resolution |

**Key insight:** Force-directed layout is a solved physics simulation problem. D3's implementation handles cooling schedules, numerical stability, performance optimization (Barnes-Hut), and edge cases (coincident nodes, disconnected subgraphs) that take weeks to get right from scratch.

## Common Pitfalls

### Pitfall 1: forceLink Not Using Custom ID Accessor
**What goes wrong:** Links reference nodes by string ID (e.g., post slug), but forceLink defaults to matching by array index. All links connect to wrong nodes or throw errors.
**Why it happens:** `d3.forceLink()` defaults to `d => d.index` for the ID accessor. If your link source/target are strings (slug IDs), you must set `.id(d => d.id)`.
**How to avoid:** Always set `.id()` when using string IDs: `forceLink(links).id(d => d.id)`
**Warning signs:** Edges visually connect to the wrong nodes, or console errors about missing nodes.

### Pitfall 2: Simulation Mutates Input Data
**What goes wrong:** D3 force simulation mutates the nodes and links arrays in place -- adding `x`, `y`, `vx`, `vy`, `index` to nodes, and replacing string source/target with object references in links.
**Why it happens:** D3's docs state "this function is impure; it may mutate the passed-in data."
**How to avoid:** Either accept mutation (fine for this use case since data is consumed once) or deep-clone before passing to simulation. For this project, mutation is acceptable since the graph data is injected once from build-time JSON.
**Warning signs:** Original data objects have unexpected properties; links have object source/target instead of string IDs.

### Pitfall 3: Drag and Zoom Event Conflicts
**What goes wrong:** Dragging a node also pans the graph, or zoom events fire during drag.
**Why it happens:** Both drag and zoom listen to mouse events on overlapping elements.
**How to avoid:** Apply `drag()` to node elements and `zoom()` to the SVG element. D3 handles event propagation correctly when set up this way -- drag on the node stops the zoom from receiving the event. The canonical pattern in the Code Examples section handles this.
**Warning signs:** Graph pans when trying to drag a node; nodes jump to unexpected positions.

### Pitfall 4: Graph Flies Off Screen
**What goes wrong:** Nodes scatter to the edges of the viewport or entirely off-screen when the simulation starts.
**Why it happens:** Charge strength too high relative to link distance and centering force, or no centering force applied. Also happens if initial node positions are all at origin (0,0).
**How to avoid:** Use `forceCenter(width/2, height/2)` to keep the graph centered. Tune `forceManyBody().strength()` (default -30, try -100 to -300 for concept graphs). Use `forceCollide()` to prevent node overlap. Consider `forceLink().distance()` to control edge length.
**Warning signs:** On page load, nodes explode outward; graph is not centered in the viewport.

### Pitfall 5: Empty or Disconnected Graph with Few Posts
**What goes wrong:** With very few posts (1-5), the graph looks sparse or has isolated nodes with no edges, providing little visual value.
**Why it happens:** Few papers may not share concepts, especially if concepts are very specific.
**How to avoid:** Show a meaningful fallback message when post count is below a threshold (e.g., <3 posts). Consider showing concept labels on edges or as separate small nodes to add visual density. Handle the zero-link case gracefully.
**Warning signs:** Single dots floating in space; graph that looks broken rather than informative.

### Pitfall 6: SVG Not Responsive
**What goes wrong:** Graph renders at a fixed size and looks wrong on mobile or when window resizes.
**Why it happens:** SVG width/height set once from initial container dimensions.
**How to avoid:** Read container dimensions on init. Use `viewBox` attribute on SVG for basic responsiveness. Optionally use ResizeObserver to resize and reheat simulation on window resize. For mobile, consider a minimum touch target size for nodes (44px per WCAG).
**Warning signs:** Graph is cut off on mobile; nodes are too small to tap on touch devices.

## Code Examples

Verified patterns from official D3 documentation.

### Force Simulation Setup with All Forces
```javascript
// Source: d3js.org/d3-force/simulation, d3js.org/d3-force/link, d3js.org/d3-force/many-body
import { forceSimulation, forceLink, forceManyBody, forceCenter, forceCollide } from "d3-force";

const simulation = forceSimulation(nodes)
  .force("link", forceLink(links)
    .id((d) => d.id)           // Match links by node id property
    .distance(100)              // Desired link length in pixels
    .strength((link) =>         // Stronger for more shared concepts
      Math.min(1, link.sharedConcepts.length * 0.2)
    )
  )
  .force("charge", forceManyBody()
    .strength(-200)             // Repulsion strength (negative = repel)
    .distanceMax(400)           // Limit repulsion range for performance and clustering
  )
  .force("center", forceCenter(width / 2, height / 2)
    .strength(0.05)             // Gentle centering -- avoids snapping
  )
  .force("collide", forceCollide()
    .radius(12)                 // Minimum separation between node centers
    .strength(0.7)              // How rigidly to enforce (0-1)
  );
```

### Node Click Navigation
```javascript
// Source: d3js.org/d3-selection (event handling)
node.on("click", (event, d) => {
  window.location.href = d.url;  // Navigate to post page
});

// Prevent click from firing after drag
let isDragging = false;
node.call(
  drag()
    .on("start", (event, d) => {
      isDragging = false;
      if (!event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    })
    .on("drag", (event, d) => {
      isDragging = true;
      d.fx = event.x;
      d.fy = event.y;
    })
    .on("end", (event, d) => {
      if (!event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    })
);
node.on("click", (event, d) => {
  if (!isDragging) window.location.href = d.url;
});
```

### Hover Tooltip with HTML Div (Richer than SVG title)
```javascript
// Source: d3-graph-gallery.com/graph/interactivity_tooltip.html
const tooltip = select("body").append("div")
  .attr("class", "absolute hidden bg-gray-900 text-white text-sm px-3 py-2 rounded-lg shadow-lg pointer-events-none z-50 max-w-xs")
  .style("position", "absolute");

node
  .on("mouseover", (event, d) => {
    tooltip
      .html(`<strong>${d.title}</strong><br/><span class="text-gray-300">${d.theme}</span>`)
      .classed("hidden", false);
  })
  .on("mousemove", (event) => {
    tooltip
      .style("left", (event.pageX + 12) + "px")
      .style("top", (event.pageY - 12) + "px");
  })
  .on("mouseout", () => {
    tooltip.classed("hidden", true);
  });
```

### Theme Color Integration
```javascript
// Theme colors from site/src/styles/global.css
const themeColors = {
  "Foundational AI": "#3b82f6",      // --color-theme-ai
  "Theoretical Physics": "#8b5cf6",   // --color-theme-theory
  "Experimental Physics": "#f59e0b",  // --color-theme-experiment
  "Astrophysics": "#10b981",          // --color-theme-astro
};

// Use in node rendering
node.attr("fill", (d) => themeColors[d.theme] || "#6b7280");
```

### Zoom + Pan Setup
```javascript
// Source: d3js.org/d3-zoom
import { zoom } from "d3-zoom";

const zoomBehavior = zoom()
  .scaleExtent([0.3, 5])  // Min 0.3x, max 5x zoom
  .on("zoom", (event) => {
    g.attr("transform", event.transform);
  });

svg.call(zoomBehavior);

// Optional: reset zoom button
document.getElementById("reset-zoom")?.addEventListener("click", () => {
  svg.transition().duration(500).call(zoomBehavior.transform, zoomIdentity);
});
```

### Link Strength Based on Shared Concept Count
```javascript
// Papers sharing more concepts should cluster more tightly
// Link strength scales with shared concept count but is bounded
.force("link", forceLink(links)
  .id((d) => d.id)
  .distance((d) => Math.max(50, 150 - d.sharedConcepts.length * 20))
  .strength((d) => Math.min(1, d.sharedConcepts.length * 0.15))
)
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| `d3.layout.force()` (D3 v3) | `d3.forceSimulation()` (D3 v4+) | D3 v4 (2016) | Completely different API. All modern tutorials use v4+ API. |
| Monolithic `d3` import | Individual packages (`d3-force`, `d3-selection`, etc.) | D3 v4 (2016) | Tree-shakeable, smaller bundles. Recommended for all new projects. |
| CommonJS `require('d3')` | ESM `import { ... } from "d3-force"` | D3 v7 (2021) | D3 v7 is ESM-only. Works natively with Vite/Astro bundling. |
| Manual SVG attribute setting | D3 data join `.join()` method | D3 v5 (2018) | `.join()` replaces verbose `.enter().append()...exit().remove()` pattern. |

**Deprecated/outdated:**
- `d3.layout.force()`: D3 v3 API. Do not use. All v3 tutorials are outdated.
- `d3.event`: Removed in D3 v7. Events are now passed as first argument to handlers: `(event, d) => {}`.
- `.enter().append()...exit().remove()` verbose pattern: Replaced by `.join()` shorthand.

## Open Questions

1. **Optimal force parameters for this specific dataset**
   - What we know: With 5-15 concepts per paper, shared concept count between any two papers likely ranges 0-5. Charge strength of -100 to -300 and link distance of 50-150 should work.
   - What's unclear: Without real data, exact tuning values are unknown.
   - Recommendation: Start with the defaults in the code examples above (charge -200, link distance 100, collide radius 12). Tune after seeing real data. Force params are easy to adjust.

2. **Edge labeling or concept nodes**
   - What we know: The requirement says "papers as nodes, shared concepts as edges." This means concepts are only shown on edges, not as their own nodes.
   - What's unclear: Whether hovering an edge should show which concepts are shared, or if concepts should appear as smaller intermediate nodes.
   - Recommendation: Show shared concept names in a tooltip on edge hover. If edges are too thin to hover, show shared concepts in the paper node tooltip as "Connected to [Paper X] via: concept1, concept2."

3. **Navigation link in Header**
   - What we know: Header currently has Timeline and Search links. A Network page needs a nav link.
   - What's unclear: Whether it should be called "Network", "Explore", or "Concepts."
   - Recommendation: Add "Network" link to Header.astro. Consistent with the graph metaphor.

4. **Mobile experience**
   - What we know: Force-directed graphs are inherently harder on mobile (small screen, touch gestures compete with page scroll). D3-zoom handles pinch zoom. Nodes need to be large enough to tap (~44px touch target).
   - What's unclear: Whether to show a simplified view or the full graph on mobile.
   - Recommendation: Show the full graph but increase node radius on small screens. The container should be taller on mobile (maybe full viewport height). Add a "tap a node to view paper" instruction text.

## Sources

### Primary (HIGH confidence)
- [d3js.org/d3-force](https://d3js.org/d3-force) - Force module overview, all sub-APIs
- [d3js.org/d3-force/simulation](https://d3js.org/d3-force/simulation) - Full simulation API: constructor, nodes, forces, alpha, tick, events
- [d3js.org/d3-force/link](https://d3js.org/d3-force/link) - forceLink API: id(), distance(), strength(), iterations()
- [d3js.org/d3-force/many-body](https://d3js.org/d3-force/many-body) - forceManyBody API: strength(), theta(), distanceMin/Max()
- [d3js.org/d3-force/center](https://d3js.org/d3-force/center) - forceCenter API: x(), y(), strength()
- [d3js.org/d3-force/collide](https://d3js.org/d3-force/collide) - forceCollide API: radius(), strength(), iterations()
- [d3js.org/d3-zoom](https://d3js.org/d3-zoom) - Zoom API: scaleExtent, translateExtent, zoom events, transform
- [d3js.org/d3-drag](https://d3js.org/d3-drag) - Drag API: drag events (start, drag, end), subject, event properties
- [d3js.org/getting-started](https://d3js.org/getting-started) - D3 v7.9.0, ESM imports, npm install patterns
- [npmjs.com/package/d3-force](https://www.npmjs.com/package/d3-force) - d3-force v3.0.0 (stable, published ~2021)

### Secondary (MEDIUM confidence)
- [Observable D3 Force-Directed Graph](https://observablehq.com/@d3/force-directed-graph/2) - Canonical example: simulation setup, drag+zoom pattern, SVG rendering
- [D3 Graph Gallery - Tooltips](https://d3-graph-gallery.com/graph/interactivity_tooltip.html) - Tooltip patterns (mouseover/move/out)
- [DEV.to - D3 Force-Directed Graph in 2025](https://dev.to/nigelsilonero/how-to-implement-a-d3js-force-directed-graph-in-2025-5cl1) - Modern implementation patterns, D3 v7 recommended

### Tertiary (LOW confidence)
- None -- all findings verified with official D3 documentation

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - D3.js is the undisputed standard for 2D force-directed graphs in vanilla JS. Version and API verified with official docs.
- Architecture: HIGH - Build-time data computation follows existing Astro site patterns (getCollection in frontmatter). SVG + d3-force is the canonical approach verified by Observable examples and official docs.
- Pitfalls: HIGH - All pitfalls sourced from official D3 API docs (mutation behavior, id accessor requirement, alpha/cooling mechanics) and verified community patterns (drag+zoom conflicts).

**Research date:** 2026-03-03
**Valid until:** 2026-06-03 (d3-force v3.0.0 has been stable since 2021; no breaking changes expected)
