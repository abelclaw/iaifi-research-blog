---
abstract: We construct smooth $\mathbb{C}^*$-actions on the moduli spaces of super
  $J$-holomorphic curves as well as super stable curves and super stable maps of genus
  zero and fixed tree type such that their reduced spaces are torus invariant. Furthermore,
  we give explicit descriptions of the normal bundles to the fixed loci in terms of
  spinor bundles and their sections. Main steps to the construction of the $\mathbb{C}^*$-action
  are the proof that the charts of the moduli space of super $J$-holomorphic curves
  obtained by the implicit function theorem yield a smooth split atlas and a detailed
  study of the superconformal automorphism group of $\mathbb{P}_{\mathbb{C}}^{1|1}$
  and its action on component fields.
arxivId: '2306.09730'
arxivUrl: https://arxiv.org/abs/2306.09730
authors:
- Enno Keßler
- Artan Sheshmani
- Shing-Tung Yau
concepts:
- super moduli spaces
- supergeometry
- torus localization
- string theory
- spinor bundles
- group theory
- quantum field theory
- symmetry breaking
- scattering amplitudes
- manifold learning
- geometric deep learning
figures: []
pdfUrl: https://arxiv.org/pdf/2306.09730v1
published: '2023-06-16T09:55:02+00:00'
theme: Foundational AI
title: Torus Actions on Moduli Spaces of Super Stable Maps of Genus Zero
wordCount: 1226
---

## The Big Picture

Imagine counting the number of ways a path can loop through a geometric space — where two paths count as the same only if you can smoothly deform one into the other. That rough picture captures what mathematicians call "counting holomorphic curves," the heart of **Gromov-Witten theory**. Emerging from string theory in the 1990s, this field transformed our understanding of geometry and quantum gravity.

Now, Enno Keßler, Artan Sheshmani, and Shing-Tung Yau have taken a major step toward extending curve-counting into the realm of *supersymmetry*. In physics, supersymmetry proposes that every known particle has a hidden partner. Mathematically, it means equipping space with extra "odd" dimensions that obey unusual rules: multiply two together and you get zero; swap their order and you get a minus sign. These **anti-commuting dimensions** don't appear in everyday geometry, but they're essential for superstring theory — the leading candidate for a unified theory of all physical forces.

Extending curve-counting to this super setting requires building new mathematical scaffolding. Previous work by the same authors constructed spaces to catalog all possible super curves. What was missing was a tool to actually compute with them.

That tool is the **torus action** — a symmetry that rotates space in a controlled way, making previously intractable computations suddenly feasible. This paper constructs explicit torus actions on super curve spaces and proves they behave well with respect to all natural geometric operations.

> **Key Insight:** By constructing torus actions whose fixed points are precisely the "classical" (non-super) curves, the authors unlock torus localization for supersymmetric curve-counting — transforming an infinite-dimensional supergeometric problem into a tractable computation on ordinary spaces.

## How It Works

**Torus localization** is a strategy that reduces big computations to smaller ones. When a symmetry group acts on a space, you can often reduce a computation over the entire space to a computation over just the **fixed points** — the parts left unchanged by the symmetry. Fixed-point sets are typically far smaller and more manageable. In classical Gromov-Witten theory, torus localization is one of the most powerful tools known; Keßler, Sheshmani, and Yau are building the same machinery for the super setting.

Their central objects are **super J-holomorphic curves**: maps from a super Riemann surface into a target space, satisfying an equation that generalizes the Cauchy-Riemann equations of complex analysis. A **super Riemann surface** is like an ordinary Riemann surface — a two-dimensional surface with a compatible complex structure — but augmented with an anti-commuting coordinate. The governing equation is:

$$D_J \Phi = \frac{1}{2}(d\Phi + I \otimes J\, d\Phi)|_D = 0$$

The collection of all such maps forms a **moduli space** M(A) — a space that parameterizes all solutions. Its "reduced" part, obtained by setting anti-commuting coordinates to zero, recovers the classical space of ordinary J-holomorphic curves.

The first main result, **Theorem 2.4.2**, establishes that M(A) admits a **split atlas**: a coordinate system in which the odd (fermionic) and even (bosonic) directions are cleanly separated. Three conditions are required:

- The gravitino (the field encoding the surface's superstructure) must vanish
- The moduli space must be smoothly obstructed
- The target must be **Kähler** — equipped with compatible complex and symplectic structures

Under these conditions, functions on the super moduli space factor through the exterior algebra of the normal bundle. The odd directions separate cleanly, making the space dramatically simpler to work with.

With this split structure in hand, the torus action becomes constructible. Given a solution (φ, ψ) — where φ is an ordinary J-holomorphic map and ψ is a **spinor field** satisfying a Dirac equation — the torus simply rescales the spinor: (φ, ψ) ↦ (φ, tψ) for t ∈ C*. Classical curves, which have ψ = 0, are left fixed.

The second main result, **Theorem 4.5.1**, extends this to **super stable maps** of genus zero — "stable" meaning finitely many symmetries, "genus zero" meaning sphere-like surfaces. This **compactified** setting, where curves can degenerate into tree-like bubble configurations, is essential for getting finite, well-defined invariants. The paper establishes that:

- Each component space M_T({Aα}), parameterizing stable maps of a fixed tree type T, carries a compatible torus action
- The fixed points are precisely the classical (reduced) curves
- The **gluing maps** — instructions for assembling tree components into full stable maps — are equivariant with respect to the torus action

That last point is technically demanding. A torus action on a product of super moduli spaces doesn't automatically descend to a quotient. The paper circumvents this by re-expressing the moduli space through successive quotients, isolating a subgroup of the superconformal automorphism group of the super projective line P^{1|1}_C that commutes with the torus action.

The paper also provides explicit descriptions of the **normal bundles** to the fixed loci — vector bundles that measure how the super moduli space extends beyond its classical reduced part. These decompose into pieces arising from spinor bundles on the underlying curves, their sections, and restrictions to marked points — a decomposition that feeds directly into localization formulas.

## Why It Matters

Gromov-Witten invariants are not just abstract curve counts. They encode deep information about the geometry of **Calabi-Yau manifolds** — compact six-dimensional spaces hypothesized by superstring theory to fill the hidden dimensions curled up at every point in space. They also control the structure of **quantum cohomology rings**, algebraic objects that appear across mathematics and physics.

**Mirror symmetry**, one of the most striking discoveries of the past thirty years, relates the Gromov-Witten theory of one Calabi-Yau to the period integrals of another, connecting distant corners of geometry through string-theoretic duality.

A super Gromov-Witten theory would extend all of this to the supersymmetric setting. The authors cite a forthcoming paper that will use torus localization — made possible by the current work — to define super Gromov-Witten invariants themselves. If successful, this program would provide rigorously defined and practically computable tools for counting supersymmetric curves, opening new windows into superstring geometry and supersymmetric quantum field theories.

Open questions remain. The paper proves torus actions on individual strata of fixed tree type; assembling these into a global continuous action on the full compactified moduli space M_{0,k}(A) is left for future work. The conditions required — Kähler target, holomorphically split domain — also limit the current results, and understanding what happens outside these constraints will matter for broader applicability.

> **Bottom Line:** Keßler, Sheshmani, and Yau have built the geometric scaffolding — split atlases, explicit torus actions, and normal bundle descriptions — needed to apply torus localization to supersymmetric curve-counting, clearing a major obstacle on the path to a complete super Gromov-Witten theory.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges advanced supergeometry with the computational machinery of algebraic geometry, constructing mathematical tools directly motivated by superstring theory and extending classical symplectic topology to the supersymmetric domain.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The decomposition of supermanifold structure into tractable split components contributes to the foundational toolbox for understanding quantum field theories, which increasingly inform neural network theory and physics-inspired AI architectures.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By establishing torus actions whose fixed points are precisely the classical J-holomorphic curves, this paper makes super Gromov-Witten invariants computable in principle, advancing string-theoretic curve-counting into the supersymmetric regime.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The forthcoming construction of super Gromov-Witten invariants via torus localization will test and extend this framework; the paper is available as arXiv:2307.08106.</span></div></div>
</div>
