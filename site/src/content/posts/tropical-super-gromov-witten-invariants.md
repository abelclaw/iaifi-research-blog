---
abstract: We show that super Gromov-Witten invariants can be defined and computed
  by methods of tropical geometry. When the target is a point, the super invariants
  are descendant invariants on the moduli space of curves, which can be computed tropically.
  When the target is a convex, toric variety $X$, we describe a procedure to compute
  the tropical Euler class of the SUSY normal bundle $\overline{N}_{n, β}$ on $\overline{\mathcal{M}}_{0,n}(X,
  β)$, assuming it is locally tropicalizable in the sense of [CG], [CGM]. Then, we
  define the tropical, genus-0, $n$-marked, super Gromov-Witten invariant of $X$,
  and compute an example. This gives a tropical interpretation of super Gromov-Witten
  invariants of convex, toric varieties.
arxivId: '2510.17400'
arxivUrl: https://arxiv.org/abs/2510.17400
authors:
- Artan Sheshmani
- Shing-Tung Yau
- Benjamin Zhou
concepts:
- super gromov-witten invariants
- tropical geometry
- susy normal bundle
- equivariant euler class
- moduli space of curves
- toric varieties
- quantum field theory
- string theory
- symmetry preservation
- group theory
- stochastic processes
figures:
- /iaifi-research-blog/figures/2510_17400/figure_1.png
- /iaifi-research-blog/figures/2510_17400/figure_2.png
- /iaifi-research-blog/figures/2510_17400/figure_3.png
pdfUrl: https://arxiv.org/pdf/2510.17400v1
published: '2025-10-20T10:40:06+00:00'
theme: Foundational AI
title: Tropical super Gromov-Witten invariants
wordCount: 1051
---

## The Big Picture

Imagine trying to count how many ways a rubber band can wrap around a donut. This seems like a pure geometry problem, but mathematicians found you can answer it by collapsing the donut into something almost laughably simple: a graph of line segments meeting at vertices, governed by a few counting rules. That's the trick behind **tropical geometry**, a branch of mathematics that replaces smooth curves and surfaces with skeletal stick figures made of straight line segments. Hard geometry problems turn into tractable counting problems on simple graphs.

For decades, mathematicians have used this trick to produce numbers called **Gromov-Witten invariants**, which encode how many curves of a given shape can live inside a geometric space. Mikhalkin's landmark 2005 result showed that for spaces with special grid-like symmetry, these curve counts can be read directly off tropical stick-figure diagrams. Since then, tropical methods have been extended to higher-dimensional targets, higher-genus curves, and a growing list of settings where classical approaches struggle.

Artan Sheshmani, Shing-Tung Yau, and Benjamin Zhou have now pushed this framework further. Their paper shows, for the first time, that **super Gromov-Witten invariants** (a supersymmetric generalization that counts "supercurves" rather than ordinary curves) can also be defined and computed using tropical geometry.

> **Key Insight:** By constructing a tropical version of the supersymmetric normal bundle, the authors translate a hard problem in supergeometry into a concrete combinatorial calculation, making super Gromov-Witten invariants computable via tropical methods for the first time.

## How It Works

The starting point is **super Gromov-Witten theory**, a mathematical framework for counting geometric curves inside a given space. Ordinary Gromov-Witten theory counts structure-preserving maps from ordinary curves into a target space X. **Supercurves** are curves enriched with an extra mathematical dimension encoding quantum spin, inspired by supersymmetry (SUSY). Their **moduli space** (a space whose points each represent one valid supercurve map) sits inside the ordinary moduli space via a natural embedding.

The central object is the **SUSY normal bundle** N_{n,β}, which measures how the supersymmetric moduli space curves away from the ordinary one. Super GW invariants equal the ordinary invariants divided by the equivariant Euler class of N_{n,β}, so computing super invariants reduces entirely to understanding this bundle.

![Figure 1](/iaifi-research-blog/figures/2510_17400/figure_1.png)

The paper proceeds in two stages:

1. **The point target.** When X is a single point, super GW invariants become **descendant invariants**, a class of curve-counting numbers on the moduli space M_{0,n} controlled by ψ-classes that track how marked points on a curve can move. The authors construct an enlarged tropical moduli space M^trop and prove that SGW_{0,n}(pt) equals a sum of weights W(Γ_k) over **decorated dual graphs**, combinatorial diagrams carrying integer labels k_1,...,k_n with k_4 + ... + k_n = n−3. Each weight is explicitly computable from the graph structure.

2. **Convex toric targets.** For a general convex toric variety X (such as projective space P^n, built from a combinatorial blueprint called a fan Σ_X), the authors use the **extended cone complex** TSM_{0,n}(Σ_X, β), a tropical moduli space encoding how curves map into X. Assuming local tropicalizability, they show that N_{n,β} is a genuine vector bundle, not merely a sheaf. This lets them define a **tropical inverse equivariant Euler class**: a map that takes a tropical cycle α and outputs a twisted version encoding how the SUSY bundle deforms the geometry. The output is expressed as alternating sums of tropical Chern classes weighted by an equivariant parameter κ.

![Figure 2](/iaifi-research-blog/figures/2510_17400/figure_2.png)

The upshot is a complete procedure: tropicalize the moduli space, compute the tropical Euler class of the SUSY normal bundle, and read off the super Gromov-Witten invariant. The authors verify this on a concrete example (a super GW invariant of P^1) and confirm that when X is a point, the general construction collapses exactly to the weighted-graph formula of stage one.

![Figure 3](/iaifi-research-blog/figures/2510_17400/figure_3.png)

## Why It Matters

Super Gromov-Witten theory sits at the intersection of supersymmetric physics and modern enumerative geometry. The super invariants probe the geometry of supercurves in ways ordinary GW theory cannot, and they are expected to encode data about partition functions in supersymmetric quantum field theories.

Until now, computations required **localization**, applying torus actions to reduce integrals to fixed-point contributions. It works, but it's demanding and often opaque. Tropical methods offer an alternative: they convert analytic and geometric problems into combinatorial ones, making computations more transparent and, in many cases, cheaper.

This paper makes possible calculations that would be out of reach by localization alone. It also points toward connections with tropical mirror symmetry, degeneration formulas, and the broader program of tropical enumerative geometry.

> **Bottom Line:** Sheshmani, Yau, and Zhou prove that supersymmetric curve-counting invariants admit a combinatorial, tropical description, turning a problem in supergeometry into a graph-counting exercise and equipping the field with new computational tools.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects supersymmetric physics with advanced pure mathematics, showing that physical symmetry principles can be given rigorous combinatorial foundations through tropical geometry.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The tropical reformulation provides explicit, algorithmic procedures for computing invariants previously accessible only via abstract localization. This is directly relevant to machine-assisted mathematical computation and symbolic AI for algebraic geometry.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Super Gromov-Witten invariants encode data about supersymmetric quantum field theories; their tropical interpretation ties SUSY physics to combinatorial structures with implications for string theory and mirror symmetry.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending the framework to higher-genus supercurves and establishing a tropical degeneration formula for super invariants; the paper is available at [arXiv:2510.17400](https://arxiv.org/abs/2510.17400).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Tropical super Gromov-Witten invariants</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2510.17400</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Artan Sheshmani", "Shing-Tung Yau", "Benjamin Zhou"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We show that super Gromov-Witten invariants can be defined and computed by methods of tropical geometry. When the target is a point, the super invariants are descendant invariants on the moduli space of curves, which can be computed tropically. When the target is a convex, toric variety $X$, we describe a procedure to compute the tropical Euler class of the SUSY normal bundle $\overline{N}_{n, β}$ on $\overline{\mathcal{M}}_{0,n}(X, β)$, assuming it is locally tropicalizable in the sense of [CG], [CGM]. Then, we define the tropical, genus-0, $n$-marked, super Gromov-Witten invariant of $X$, and compute an example. This gives a tropical interpretation of super Gromov-Witten invariants of convex, toric varieties.</span></div></div>
</div>
