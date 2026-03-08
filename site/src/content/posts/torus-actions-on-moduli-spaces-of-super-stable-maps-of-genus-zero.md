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
wordCount: 1315
---

## The Big Picture

Imagine counting the number of ways a path can loop through a geometric space, where two paths count as the same only if you can smoothly deform one into the other. That rough picture captures what mathematicians call "counting holomorphic curves," the heart of **Gromov-Witten theory**. Born from string theory in the 1990s, this field transformed our understanding of geometry and quantum gravity.

Enno Keßler, Artan Sheshmani, and Shing-Tung Yau have now taken a significant step toward extending curve-counting into the realm of *supersymmetry*. In physics, supersymmetry proposes that every known particle has a hidden partner. Mathematically, it means equipping space with extra "odd" dimensions that obey unusual rules: multiply two together and you get zero; swap their order and pick up a minus sign. These **anti-commuting dimensions** don't appear in everyday geometry, but they're the native language of superstring theory.

Extending curve-counting to this super setting requires new mathematical scaffolding. Previous work by the same authors constructed spaces to catalog all possible super curves. What was missing was a tool to actually compute with them.

That tool is the **torus action**, a symmetry that rotates space in a controlled way, making previously intractable computations suddenly feasible. This paper constructs explicit torus actions on super curve spaces and proves they behave well with respect to all the natural geometric operations.

> **Key Insight:** By constructing torus actions whose fixed points are precisely the "classical" (non-super) curves, the authors unlock torus localization for supersymmetric curve-counting, transforming an infinite-dimensional supergeometric problem into a tractable computation on ordinary spaces.

## How It Works

**Torus localization** reduces big computations to smaller ones. When a symmetry group acts on a space, you can often collapse a computation over the entire space down to one over just the **fixed points**, the parts left unchanged by the symmetry. Fixed-point sets are typically far smaller. In classical Gromov-Witten theory, torus localization is one of the most effective tools available; Keßler, Sheshmani, and Yau are building the same machinery for the super setting.

Their central objects are **super J-holomorphic curves**: maps from a super Riemann surface into a target space, satisfying an equation that generalizes the Cauchy-Riemann equations of complex analysis. A super Riemann surface is like an ordinary Riemann surface (a two-dimensional surface with a compatible complex structure) but augmented with an anti-commuting coordinate. The governing equation is:

$$D_J \Phi = \frac{1}{2}(d\Phi + I \otimes J\, d\Phi)|_D = 0$$

The collection of all such maps forms a **moduli space** M(A), parameterizing all solutions. Its "reduced" part, obtained by setting anti-commuting coordinates to zero, recovers the classical space of ordinary J-holomorphic curves.

The first main result, **Theorem 2.4.2**, establishes that M(A) admits a split atlas: a coordinate system in which the odd (fermionic) and even (bosonic) directions are cleanly separated. Three conditions are required: the gravitino (the field encoding the surface's superstructure) must vanish, the moduli space must be smoothly obstructed, and the target must be Kähler, meaning it carries compatible complex and symplectic structures. Under these conditions, functions on the super moduli space factor through the exterior algebra of the normal bundle. The odd directions decouple, and the space becomes dramatically simpler to work with.

With this split structure in hand, the torus action becomes constructible. Given a solution (φ, ψ), where φ is an ordinary J-holomorphic map and ψ is a spinor field satisfying a Dirac equation, the torus simply rescales the spinor: (φ, ψ) ↦ (φ, tψ) for t ∈ ℂ*. Classical curves, which have ψ = 0, are left fixed.

The second main result, **Theorem 4.5.1**, extends this to super stable maps of genus zero. "Stable" means finitely many symmetries; "genus zero" means sphere-like surfaces. This compactified setting, where curves can degenerate into tree-like bubble configurations, is where you get finite, well-defined invariants. The paper establishes that each component space M_T({Aα}), parameterizing stable maps of a fixed tree type, carries a compatible torus action; the fixed points are precisely the classical (reduced) curves; and the gluing maps that assemble tree components into full stable maps are equivariant with respect to the torus action.

That last point is technically demanding. A torus action on a product of super moduli spaces doesn't automatically descend to a quotient. The paper gets around this by re-expressing the moduli space through successive quotients, isolating a subgroup of the superconformal automorphism group of ℙ^{1|1}_ℂ that commutes with the torus action.

The paper also gives explicit descriptions of the normal bundles to the fixed loci, the vector bundles that measure how the super moduli space extends beyond its classical reduced part. These decompose into pieces arising from spinor bundles on the underlying curves, their sections, and restrictions to marked points. This decomposition feeds directly into localization formulas.

## Why It Matters

Gromov-Witten invariants are not just abstract curve counts. They encode deep information about the geometry of **Calabi-Yau manifolds**, compact six-dimensional spaces hypothesized by superstring theory to fill the hidden dimensions curled up at every point in space. They also control the structure of quantum cohomology rings, algebraic objects that appear across mathematics and physics.

**Mirror symmetry**, one of the most surprising discoveries of the past thirty years, relates the Gromov-Witten theory of one Calabi-Yau to the period integrals of another, connecting distant corners of geometry through string-theoretic duality.

A super Gromov-Witten theory would extend all of this to the supersymmetric setting. The authors cite a forthcoming paper that will use torus localization, made possible by the current work, to define super Gromov-Witten invariants themselves. If the program succeeds, it would produce rigorously defined and practically computable tools for counting supersymmetric curves, with applications to superstring geometry and supersymmetric quantum field theories.

Open questions remain. The paper proves torus actions on individual strata of fixed tree type; assembling these into a global continuous action on the full compactified moduli space M_{0,k}(A) is left for future work. The conditions required (Kähler target, holomorphically split domain) also limit the current results, and understanding what happens outside these constraints matters for broader applicability.

> **Bottom Line:** Keßler, Sheshmani, and Yau have built the geometric scaffolding (split atlases, explicit torus actions, and normal bundle descriptions) needed to apply torus localization to supersymmetric curve-counting, removing a major obstacle on the path to a complete super Gromov-Witten theory.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects advanced supergeometry with the computational machinery of algebraic geometry, constructing mathematical tools directly motivated by superstring theory and extending classical symplectic topology to the supersymmetric domain.

- **Impact on Artificial Intelligence:** The decomposition of supermanifold structure into tractable split components adds to the mathematical toolbox for understanding quantum field theories, which increasingly inform neural network theory and physics-inspired AI architectures.

- **Impact on Fundamental Interactions:** By establishing torus actions whose fixed points are precisely the classical J-holomorphic curves, this paper makes super Gromov-Witten invariants computable in principle, extending string-theoretic curve-counting into the supersymmetric regime.

- **Outlook and References:** The forthcoming construction of super Gromov-Witten invariants via torus localization will test and extend this framework; the paper is available as [arXiv:2306.09730](https://arxiv.org/abs/2306.09730).

## Original Paper Details
- **Title:** Torus Actions on Moduli Spaces of Super Stable Maps of Genus Zero
- **arXiv ID:** 2306.09730
- **Authors:** ["Enno Ke\u00dfler", "Artan Sheshmani", "Shing-Tung Yau"]
- **Abstract:** We construct smooth $\mathbb{C}^*$-actions on the moduli spaces of super $J$-holomorphic curves as well as super stable curves and super stable maps of genus zero and fixed tree type such that their reduced spaces are torus invariant. Furthermore, we give explicit descriptions of the normal bundles to the fixed loci in terms of spinor bundles and their sections. Main steps to the construction of the $\mathbb{C}^*$-action are the proof that the charts of the moduli space of super $J$-holomorphic curves obtained by the implicit function theorem yield a smooth split atlas and a detailed study of the superconformal automorphism group of $\mathbb{P}_{\mathbb{C}}^{1|1}$ and its action on component fields.
