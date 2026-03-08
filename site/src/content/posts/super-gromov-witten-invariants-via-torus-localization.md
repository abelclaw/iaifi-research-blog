---
abstract: In this article we propose a definition of super Gromov-Witten invariants
  by postulating a torus localization property for the odd directions of the moduli
  spaces of super stable maps and super stable curves of genus zero. That is, we define
  super Gromov-Witten invariants as the integral over the pullback of homology classes
  along the evaluation maps divided by the equivariant Euler class of the normal bundle
  of the embedding of the moduli space of stable spin maps into the moduli space of
  super stable maps. This definition sidesteps the difficulties of defining a supergeometric
  intersection theory and works with classical intersection theory only. The properties
  of the normal bundles, known from the differential geometric construction of the
  moduli space of super stable maps, imply that super Gromov-Witten invariants satisfy
  a generalization of Kontsevich-Manin axioms and allow for the construction of a
  super small quantum cohomology ring. We describe a method to calculate super Gromov-Witten
  invariants of $\mathbb{P}^n$ of genus zero by a further geometric torus localization
  and give explicit numbers in degree one when dimension and number of marked points
  are small.
arxivId: '2311.09074'
arxivUrl: https://arxiv.org/abs/2311.09074
authors:
- Enno Keßler
- Artan Sheshmani
- Shing-Tung Yau
concepts:
- super gromov-witten invariants
- supergeometric moduli spaces
- torus localization
- quantum cohomology
- spin structures
- symmetry preservation
- string theory
- quantum field theory
- group theory
- scattering amplitudes
figures: []
pdfUrl: https://arxiv.org/pdf/2311.09074v1
published: '2023-11-15T16:17:08+00:00'
theme: Foundational AI
title: Super Gromov-Witten Invariants via torus localization
wordCount: 1273
---

## The Big Picture

Imagine trying to count something inherently slippery: not apples or electrons, but the number of ways a surface can be mapped into a curved, high-dimensional space while satisfying specific constraints. That's what **Gromov-Witten invariants** do. The resulting numbers encode hidden information about a space's shape and structure, and since the 1980s and 90s they've become one of geometry's most powerful tools, connecting string theory, algebraic geometry, and combinatorics.

Now imagine the surfaces themselves become "super." In superstring theory, the mathematical spaces physicists work with carry not just ordinary coordinates but an additional layer governed by strange arithmetic: two of these new coordinates multiplied in either order give opposite signs, and any coordinate squared equals zero. These are **Grassmann coordinates**, the mathematical language of **fermions** (electrons, quarks, the particles that make up ordinary matter). In superstring theory, they aren't optional extras. They're fundamental.

A supersymmetric version of Gromov-Witten theory should exist, but building it has stalled for years against a basic obstacle. The standard toolkit for "counting" in geometry, **intersection theory**, doesn't yet work in the extended supersymmetric setting. You can't count things you can't integrate over.

Enno Keßler, Artan Sheshmani, and Shing-Tung Yau have found a way around that wall. Their [paper](https://arxiv.org/abs/2311.09074) defines **super Gromov-Witten invariants** by completely sidestepping the missing machinery, then proves the resulting invariants are well-behaved, calculable, and genuinely new.

> **Key Insight:** By assuming that a classical technique called "torus localization" extends to supergeometry, the authors convert an impossibly hard supergeometric calculation into a classical one that existing tools can handle.

## How It Works

The trick at the heart of this paper comes from **equivariant geometry**, the study of spaces carrying a built-in symmetry like a circle rotating around an axis. Within that field, **torus localization** is a classical tool: when a torus (a group of rotations) acts on a space, an integral over the whole space can be reduced to an integral over just the fixed points of that action, corrected by a geometric factor. Think of computing the average temperature across a rotating planet by measuring only at the poles, then dividing by a correction term.

Here's the central structural observation. The **moduli space of super stable maps**, which catalogs every valid supersymmetric curve mapping into a target (one point per configuration), contains an embedded classical subspace. These are **stable spin maps**: ordinary curves equipped with a spin structure, a geometric decoration that captures a consistent notion of "square root" of the curve's geometry. The fermionic directions of the super moduli space form a **vector bundle** over this classical subspace, called the SUSY normal bundle, recording all the fermionic degrees of freedom that have been factored out.

For a convex target scheme $X$ and degree $\beta$, the SUSY normal bundle $N_{k,\beta}$ is built from three ingredients:

- The spinor bundle $S = \mathcal{O}(1)$ extended over the curve
- The tangent bundle of $X$, pulled back via the map
- Evaluation terms at the marked points

The super Gromov-Witten invariant is then an integral over the classical moduli space of stable spin maps, with cohomology classes pulled back from the target, divided by the equivariant Euler class of the SUSY normal bundle. The Euler class measures the "size" of the fermionic directions at each point: the numerator is the ordinary Gromov-Witten-style integral, and the denominator accounts for the surrounding fermionic space.

This construction has three notable features. First, no supergeometric intersection theory is required; the entire computation lives in classical algebraic geometry. Second, when the cohomology classes have the right total degree, the super invariants reduce to ordinary Gromov-Witten invariants up to a polynomial prefactor. Third, genuinely new invariants exist: when the degree mismatch is positive, the inverse Euler class contributes characteristic classes of the SUSY normal bundle, information that cannot be recovered from classical descendants.

To calculate these invariants for projective space $\mathbb{P}^n$, the authors apply torus localization a second time, now using a geometric torus action on $\mathbb{P}^n$ itself (the standard engine for computing Gromov-Witten invariants via graphs). The result: explicit numbers for genus zero, degree one maps into low-dimensional projective spaces with few marked points.

## Why It Matters

The authors prove that super Gromov-Witten invariants satisfy a generalized **Kontsevich-Manin axiom system**, the structural rules that make classical Gromov-Witten invariants so computable. These axioms govern what happens when you add a marked point, change the degree, or split a curve along a node. Satisfying them means the invariants fit into a coherent algebraic framework, not just a one-off definition.

That coherence lets the invariants be assembled into a **super small quantum cohomology ring**, extending classical quantum cohomology to encode how geometric objects in the target space intersect in the supersymmetric setting.

For physics, the stakes are higher. Super Gromov-Witten invariants are the right mathematical objects for computing scattering amplitudes in superstring theory on curved backgrounds, where the worldsheet is a super Riemann surface rather than an ordinary one. For decades, such amplitudes have been computed through a patchwork of methods, never with the clean algebraic geometry machinery available for bosonic strings. This paper offers a route toward that machinery: a well-defined, axiom-satisfying, explicitly calculable invariant that incorporates genuine supergeometric information.

Open questions remain. Most importantly, the assumed torus localization theorem still needs a proof in full generality. But the authors have shown that the *answer* is mathematically coherent even before that proof is complete.

> **Bottom Line:** Keßler, Sheshmani, and Yau define super Gromov-Witten invariants by making a precise assumption about torus localization, then proving those invariants satisfy all the structural axioms needed for a viable supergeometric enumerative theory connecting superstring physics and rigorous algebraic geometry.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly connects superstring theory and algebraic geometry by providing rigorous mathematical definitions for invariants that theoretical physics has needed for decades.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The construction of super small quantum cohomology rings introduces new algebraic structures that may inform AI-assisted mathematical exploration and symbolic computation in high-energy physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Super Gromov-Witten invariants provide the mathematical scaffolding for computing superstring scattering amplitudes on curved backgrounds in a rigorous, axiom-satisfying framework, advancing fully algebraic treatments of superstring theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will focus on proving the assumed torus localization theorem in full generality and extending calculations beyond genus zero and degree one; the full paper is available at [arXiv:2311.09074](https://arxiv.org/abs/2311.09074).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Super Gromov-Witten Invariants via torus localization</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2311.09074</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Enno Ke\u00dfler", "Artan Sheshmani", "Shing-Tung Yau"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">In this article we propose a definition of super Gromov-Witten invariants by postulating a torus localization property for the odd directions of the moduli spaces of super stable maps and super stable curves of genus zero. That is, we define super Gromov-Witten invariants as the integral over the pullback of homology classes along the evaluation maps divided by the equivariant Euler class of the normal bundle of the embedding of the moduli space of stable spin maps into the moduli space of super stable maps. This definition sidesteps the difficulties of defining a supergeometric intersection theory and works with classical intersection theory only. The properties of the normal bundles, known from the differential geometric construction of the moduli space of super stable maps, imply that super Gromov-Witten invariants satisfy a generalization of Kontsevich-Manin axioms and allow for the construction of a super small quantum cohomology ring. We describe a method to calculate super Gromov-Witten invariants of $\mathbb{P}^n$ of genus zero by a further geometric torus localization and give explicit numbers in degree one when dimension and number of marked points are small.</span></div></div>
</div>
