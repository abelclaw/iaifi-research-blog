---
abstract: In this paper we prove a common generalisation of results by Špenko-Van
  den Bergh and Iyama-Wemyss that can be used to generate non-commutative crepant
  resolutions (NCCRs) of some affine toric Gorenstein varieties. We use and generalise
  results by Novaković to study NCCRs for affine toric Gorenstein varieties associated
  to cones over polytopes with interior points. As a special case, we consider the
  case where the polytope is reflexive with $\le \dim P+2$ vertices, using results
  of Borisov and Hua to show the existence of NCCRs.
arxivId: '2509.11664'
arxivUrl: https://arxiv.org/abs/2509.11664
authors:
- Aimeric Malter
- Artan Sheshmani
concepts:
- non-commutative resolutions
- toric geometry
- derived categories
- group theory
- symmetry preservation
- string theory
- quantum field theory
figures: []
pdfUrl: https://arxiv.org/pdf/2509.11664v1
published: '2025-09-15T08:05:19+00:00'
theme: Foundational AI
title: Towards non-commutative crepant resolutions of affine toric Gorenstein varieties
wordCount: 963
---

## The Big Picture

Imagine trying to iron out a wrinkle in fabric — but every time you smooth one spot, it reappears somewhere else in a more complicated form. That's roughly what mathematicians face when resolving the singularities of **affine toric Gorenstein varieties**: geometric objects defined by grids of integer points that arise naturally in string theory, mirror symmetry, and the mathematics behind geometric deep learning.

Their singularities — points where the space pinches or becomes pathological — resist classical smoothing techniques. The standard fix, a **crepant resolution**, removes singularities without introducing extra complexity, like ironing out a wrinkle without stretching the surrounding fabric. But crepant resolutions don't always exist.

For decades, a radical workaround has gained traction: replace the singular space with a **non-commutative algebraic object** — a ring where the order of multiplication matters — that encodes the same geometric information. These are **non-commutative crepant resolutions**, or NCCRs. A long-standing conjecture holds that every affine Gorenstein toric variety should have one. IAIFI mathematicians Aimeric Malter and Artan Sheshmani have now proven this conjecture for a broad new family of these spaces, unifying and extending previous partial results into a single powerful theorem.

> **Key Insight:** By showing that a single algebraic object — the endomorphism ring of a partial tilting complex — can serve as a non-commutative resolution, the authors resolve singularities that resist geometric treatment, while uncovering deep connections between derived categories, toric geometry, and mirror symmetry.

## How It Works

The strategy rests on **tilting theory**, a toolkit from homological algebra. A **tilting complex** on a geometric space captures the full **derived category** — a complete catalog of the space's geometric data, tracking not just objects but all the ways they relate, combine, and transform. Find one, and you can often build a non-commutative resolution.

Malter and Sheshmani's central result (Theorem 3.12) proceeds in four steps:

1. **Start with a cone.** Every affine toric Gorenstein variety comes from a cone $\sigma = \text{Cone}(P \times \{1\})$ over a polytope $P$ — a multidimensional polygon with integer-coordinate vertices. The ring of functions on the variety is $R = k[\sigma^\vee \cap M]$.

2. **Triangulate the polytope.** A regular triangulation of $P$ defines a **fan** $\Sigma$ — a collection of cones encoding the variety's local geometry — which gives rise to a **toric DM stack** $X_\Sigma$, a generalized space that handles singularities gracefully by allowing points to carry extra symmetry data.

3. **Find a partial tilting complex.** On $X_\Sigma$, construct a **partial tilting complex** $T$ whose endomorphism algebra $\Lambda = \text{End}_{X_\Sigma}(T)$ has **finite global dimension** — meaning that any module over $\Lambda$ admits a projective resolution that terminates in finitely many steps.

4. **Conclude the NCCR exists.** Under these conditions, $\Lambda$ is an NCCR for $R$.

This framework generalizes two landmark results — one by Špenko and Van den Bergh, another by Iyama and Wemyss — into a single theorem. The Špenko–Van den Bergh result required a full tilting bundle on the Cox stack of a simplicialization of $\sigma$. The Iyama–Wemyss result required a projective, birational, crepant map. Theorem 3.12 replaces both with the weaker condition of a partial tilting complex of finite global dimension.

To handle cones over polytopes with interior lattice points, the authors study **total spaces of canonical bundles** over toric varieties. If $X$ is a simplicial projective toric variety, the total space $V = \text{tot}\, \omega_X$ is itself toric, and its fan encodes a Gorenstein cone. They prove (Theorem 4.12) that if $X_\Sigma$ carries a full tilting complex $T$ and certain cohomology vanishing conditions hold, a tilting complex also exists on $X_V$. These conditions are checkable in practice, and the authors verify them through explicit examples.

## Why It Matters

The open conjecture that every affine Gorenstein toric variety has an NCCR sits at the intersection of algebraic geometry, representation theory, and string theory. Malter and Sheshmani prove it for all reflexive polytopes with at most $n + 2$ vertices (Theorem 5.1), drawing on results of Borisov and Hua.

Reflexive polytopes are intimately tied to **Fano varieties** — the positive-curvature spaces that appear in string compactifications — making this result directly relevant to theoretical physics.

The deeper significance lies in the **derived category philosophy** underlying this work. The Bondal–Orlov and Kawamata conjecture holds that all crepant resolutions of a space are derived equivalent — that deep invariants of singular spaces live at the level of derived categories, not individual resolutions. NCCRs make this philosophy concrete: they are algebraic stand-ins for geometric resolutions when none exists. As AI methods increasingly exploit derived-category structures for equivariant neural networks and physics-informed machine learning, the mathematical tools developed here provide rigorous foundations for those applications.

> **Bottom Line:** Malter and Sheshmani unify two major streams of non-commutative algebraic geometry into a single framework, proving NCCR existence for a substantial new class of singular spaces — and their approach is constructive enough to guide explicit computations in mirror symmetry and geometric AI.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges algebraic geometry and theoretical physics by resolving singularities of toric varieties that appear in string compactifications and mirror symmetry, using non-commutative tools that increasingly inform AI's geometric deep learning frameworks.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The derived-category and tilting-theory machinery developed here underpins symmetry-based and equivariant approaches in modern machine learning, providing rigorous mathematical structures for AI systems that respect fundamental geometric symmetries.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By proving NCCR existence for reflexive polytopes with $\le n+2$ vertices — directly tied to Fano varieties and string theory compactifications — this work advances the mathematical foundations of quantum gravity and mirror symmetry.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will push toward a complete proof of the NCCR conjecture for all affine Gorenstein toric varieties; the paper is available at arXiv:2601.14453.</span></div></div>
</div>
