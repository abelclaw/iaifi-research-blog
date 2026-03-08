---
abstract: This paper is the second in a series of works dedicated to studying non-linear
  partial differential equations via derived geometric methods. We study a natural
  derived enhancement of the de Rham complex of a non-linear PDE via algebro-geometric
  techniques and examine its consequences for the functional differential calculus
  on the space of solutions. Applications to the BV-formalism with and without boundary
  conditions are discussed.
arxivId: '2406.16825'
arxivUrl: https://arxiv.org/abs/2406.16825
authors:
- Jacob Kryczka
- Artan Sheshmani
- Shing-Tung Yau
concepts:
- derived algebraic geometry
- variational tricomplex
- bv formalism
- quantum field theory
- lagrangian methods
- hamiltonian systems
- symmetry preservation
- group theory
- spectral methods
- string theory
- effective field theory
figures:
- /iaifi-research-blog/figures/2406_16825/figure_1.png
pdfUrl: https://arxiv.org/pdf/2406.16825v1
published: '2024-06-24T17:35:12+00:00'
theme: Foundational AI
title: 'Derived Moduli Spaces of Nonlinear PDEs II: Variational Tricomplex and BV
  Formalism'
wordCount: 1119
---

## The Big Picture

Imagine trying to map a mountain range with instruments that only work on flat terrain. Classical geometry gives you exquisite tools for smooth surfaces — but the moment your landscape gets jagged, full of collapsed valleys and sharp peaks, those tools fail. Physicists face exactly this problem when studying the equations governing subatomic particles and fundamental forces. The spaces of solutions to these equations are rarely smooth; they're riddled with redundancies, symmetries, and singularities that standard mathematics cannot cleanly handle.

Partial differential equations (PDEs) sit at the heart of modern physics: Maxwell's equations, Einstein's field equations, the Seiberg-Witten equations. Mathematicians have long used the **variational bicomplex** — a double-layered algebraic scaffolding built to catalog all the ways a PDE's solutions can vary — to study their geometry. It tracks how solutions deform, how symmetries act, and what conserved quantities emerge.

But this classical tool has a fundamental limitation: it cannot see the hidden layers of geometric information that modern mathematics insists are lurking in solution spaces — structural data about how and why things that *look* exact are only approximately so.

In a new paper, Jacob Kryczka, Artan Sheshmani, and Shing-Tung Yau construct a systematic upgrade — a **derived variational tricomplex** that extends the classical bicomplex into a more flexible, shape-preserving geometry, unlocking a richer calculus on solution spaces and new pathways for quantizing classical field theories.

> **Key Insight:** By replacing the classical variational bicomplex with a derived, homotopy-coherent analog, the authors build a framework that handles singular solution spaces, gauge symmetries, and even theories with no action principle — all within a single unified geometric language.

## How It Works

The classical variational bicomplex organizes differential forms on a PDE's solution space into a grid, with two independent differentials — one tracking changes along spacetime, one tracking changes in field configurations. It's a powerful bookkeeping device, but "closed" in classical geometry means *exactly* closed.

In **derived geometry** — a modern extension that carefully tracks *why* and *how* things that should be zero actually fail to be, encoding that failure as useful information — closed means closed *up to homotopy*, with an infinite tower of conditions encoding exactly how closure fails at each level. That tower is new information, and it matters.

The authors' central construction, the **derived variational tricomplex** (a three-layered algebraic structure incorporating this extra homotopy data), emerges by applying techniques from derived algebraic geometry — specifically the theory of *D-prestacks*, geometric objects bundling algebraic structures with a compatible action of differential operators — to the moduli space of solutions of a nonlinear PDE. The key object is a **differentially structured cotangent complex** $\mathbb{L}_Y$: a homotopy-invariant replacement for the usual space of differential forms, encoding infinitesimal variations of a solution even when that solution space is singular.

![Figure 1](/iaifi-research-blog/figures/2406_16825/figure_1.png)

The construction proceeds in three main moves:

1. **Geometry of D-prestacks:** The authors establish a robust local calculus for D-geometric objects — spaces with a built-in compatible action of differential operators, enabling intrinsic calculus on solution spaces without coordinates.

2. **Shifted symplectic structure:** Borrowing from the PTVV framework, they equip the derived tricomplex with a *shifted symplectic pairing* — a generalization of the **Poisson bracket** (the mathematical gadget encoding how physical quantities interact in classical mechanics), now defined intrinsically on the derived solution space.

3. **Variational factorization homology:** The paper introduces a way of assembling local algebraic data from small patches of spacetime into global invariants of the PDE — like a mosaic built from individual tiles. The factorization structure interleaves with both spacetime and field-space differentials to produce a genuinely three-dimensional algebraic complex.

A crucial payoff is the treatment of **non-Lagrangian theories** — physical systems with no action principle, where there is no single governing equation from which all physics can be derived by standard variational methods. Seiberg-Witten equations, theories with self-dual field strengths, chiral bosons, and higher-spin gauge theories all fall into this category. Classical approaches force these into a Lagrangian mold or exclude them entirely. By working directly with moduli spaces of PDE solutions rather than critical loci of functionals, the derived tricomplex handles Lagrangian and non-Lagrangian theories on equal footing.

## Why It Matters

The **BV (Batalin-Vilkovisky) formalism** is the gold standard for quantizing gauge theories — the machinery behind rigorous treatment of gauge redundancy in the Standard Model and beyond. The authors apply their tricomplex framework to recover and generalize the BV construction, including a careful treatment of boundary conditions.

This is not a minor technical point. Boundaries introduce subtleties — edge modes, holographic degrees of freedom — that the classical BV formalism handles awkwardly. The D-geometric boundary schemes developed here give a clean intrinsic account of what happens at the boundary of a spacetime manifold, with direct implications for holography and topological field theory.

More broadly, this work exemplifies a growing research program: using tools of derived algebraic geometry, originally developed for **enumerative geometry** (the mathematical study of counting geometric objects like curves on a surface), to attack concrete problems in mathematical physics. The derived moduli spaces constructed here carry the same shifted symplectic structures governing sheaf-counting problems on Calabi-Yau fourfolds — six-dimensional geometric spaces central to string theory — suggesting deep structural parallels between enumerative geometry and field-theory quantization.

Future directions include connecting the variational tricomplex to factorization algebras in the sense of Costello-Gwilliam, extending the framework to chiral algebras and vertex operator algebras, and pursuing non-perturbative BV quantization beyond the formal neighborhood of a single classical solution.

> **Bottom Line:** Kryczka, Sheshmani, and Yau have built the first fully derived, homotopy-coherent generalization of the variational bicomplex, giving mathematical physicists a powerful new tool for studying nonlinear PDEs, their symmetries, and their quantization — including theories that classical formalisms cannot even describe.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work forges a direct bridge between abstract derived algebraic geometry and the physics of gauge field theories, demonstrating that homotopy-theoretic methods from algebraic geometry are not merely analogous to, but structurally identical with, the correct mathematical framework for field-theory quantization.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The derived geometric structures developed here — particularly variational factorization homology and D-geometric moduli spaces — provide rigorous mathematical foundations that could inform AI-assisted discovery in theoretical physics, where solution spaces of nonlinear PDEs remain computationally intractable.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The framework handles non-Lagrangian gauge theories (Seiberg-Witten, Donaldson-Uhlenbeck-Yau, higher-spin theories) and provides an intrinsic treatment of BV boundary conditions, opening new mathematical avenues for understanding holography and topological aspects of quantum field theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The series continues with applications to enumerative invariants and non-perturbative quantization; the paper represents the second installment in an ongoing program by Kryczka, Sheshmani, and Yau on derived geometry of PDEs.</span></div></div>
</div>
