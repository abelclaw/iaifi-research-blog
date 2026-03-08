---
abstract: We construct a sheaf theoretic and derived geometric machinery to study
  nonlinear partial differential equations and their singular supports. We establish
  a notion of derived microlocalization for solution spaces of non-linear equations
  and develop a formalism to pose and solve singular non-linear Cauchy problems globally.
  Using this approach we estimate the domains of propagation for the solutions of
  non-linear systems. It is achieved by exploiting the fact that one may greatly enrich
  and simplify the study of derived non-linear PDEs over a space $X$ by studying its
  derived linearization which is a module over the sheaf of functions on the $S^1$-equivariant
  derived loop stack $\mathcal{L}X$.
arxivId: '2312.05226'
arxivUrl: https://arxiv.org/abs/2312.05226
authors:
- Jacob Kryczka
- Artan Sheshmani
- Shing-Tung Yau
concepts:
- derived algebraic geometry
- nonlinear pde theory
- microlocal analysis
- derived loop stacks
- sheaf theory
- hodge theory
- quantum field theory
- spectral methods
- symmetry breaking
- inverse problems
figures:
- /iaifi-research-blog/figures/2312_05226/figure_1.png
- /iaifi-research-blog/figures/2312_05226/figure_1.png
pdfUrl: https://arxiv.org/pdf/2312.05226v2
published: '2023-12-08T18:23:29+00:00'
theme: Foundational AI
title: 'Derived Moduli Spaces of Nonlinear PDEs I: Singular Propagations'
wordCount: 1125
---

## The Big Picture

Imagine trying to predict where a crack will spread through a sheet of glass. You can see the crack, but the real challenge is the invisible forces at its tip — the singular point where mathematics breaks down. Scale that problem up to the equations governing spacetime, quantum fields, or the geometry of the universe itself, and you have the challenge at the heart of a sweeping new paper by Jacob Kryczka, Artan Sheshmani, and Shing-Tung Yau.

**Nonlinear partial differential equations** (NLPDEs) — equations where outputs feed back into the equation itself — are the fundamental language of physics. Einstein's field equations, fluid dynamics, the **Yang-Mills equations** governing how fundamental particles interact: all share this character, and all are ferociously hard to solve. The central difficulty is not finding solutions, but understanding where they break down — where they blow up to infinity, develop sudden jumps, or spread failure in ways that make predictions impossible.

Classical tools handle this reasonably well on smooth, simple geometric spaces. But modern theoretical physics demands more: equations on abstract spaces with sharp corners, holes, and other pathologies. This paper delivers a rigorous new framework — rooted in **derived algebraic geometry** — that tracks exactly how breakdowns propagate, even on the most exotic geometric backgrounds imaginable.

> **Key Insight:** By lifting nonlinear equations into derived geometry and studying them through an associated "loop stack," the authors reduce brutally hard nonlinear problems to tractable linear ones — without losing any singular, topological, or structural information.

## How It Works

Rather than attacking a nonlinear equation head-on, the team embeds it inside a richer geometric object: the **derived moduli space of solutions** — the space of all possible solutions simultaneously, treated as a geometric landscape. The "derived" part uses **homotopy theory** (the study of how paths and loops within spaces can be continuously deformed) to track degeneracies and infinitesimal symmetries that ordinary geometry discards.

The key technical tool is the **derived loop stack** $\mathcal{L}X$ — the space of closed paths in $X$, equipped with a natural rotational symmetry. Functions on $\mathcal{L}X$ are precisely the algebraic structure needed to see a nonlinear PDE's linearization as a module, making the connection between nonlinear and linear geometry precise and functorial.

![Figure 1](/iaifi-research-blog/figures/2312_05226/figure_1.png)

Here is the architecture of the approach:

1. **Encode the PDE as a derived substack.** The nonlinear PDE is realized as a derived closed substack $\mathcal{Y}$ inside an infinite jet bundle. The solution space $\text{RSol}_X(\mathcal{Y})$ becomes a geometric object with a well-defined homotopy type.

2. **Impose D-finiteness.** The authors introduce **D-finiteness** — a condition analogous to requiring a vector space to be finite-dimensional — ensuring the existence of a globally dualizable cotangent complex. This makes the rest of the machinery work.

3. **Linearize around a solution.** Given a solution $\phi$, linearizing the derived PDE yields a sheaf $T_{\mathcal{Y}, \phi}$ — the tangent complex at $\phi$ — encoding how the solution would change under tiny perturbations.

4. **Micro-linearize via the Hodge stack.** The linearization sheaf lifts to the **Hodge stack** $X^{\text{Hod}}$, a geometric object interpolating between two complementary algebraic pictures of the same space. Passing to the associated graded object produces a perfect complex on the cotangent stack $T^*X$ — the authors' **derived micro-linearization** $\mathbf{R}_\mu(T_{\mathcal{Y}, \phi})$.

5. **Read off the characteristic variety.** The support of $\mathbf{R}_\mu(T_{\mathcal{Y}, \phi})$ defines the **characteristic variety** $\text{Ch}_\phi(\mathcal{Y})$ — the locus in $T^*X$ identifying which directions are singular for the PDE at $\phi$. Think of it as a map of danger zones: directions where small disturbances grow rather than smooth out.

The payoff is Theorem A: for D-finitary derived PDEs admitting deformation theory, the linearization sheaf is locally constant in non-characteristic directions. This is the derived, nonlinear analog of the classical result that solutions propagate smoothly away from characteristic directions — and it holds on singular, derived, and non-archimedean spaces alike.

![Figure 2](/iaifi-research-blog/figures/2312_05226/figure_1.png)

Theorems B and C generalize the classical Cauchy-Kowalevski-Kashiwara theorem to the nonlinear derived setting: if the initial data surface avoids the dangerous directions, the singular nonlinear Cauchy problem is globally well-posed. Given appropriate starting conditions, the equation has a unique, globally-controlled solution — a major guarantee for the physical systems these equations describe.

The framework also handles **tempered distributions** and generalized function spaces — highly irregular objects that don't behave well enough to form ordinary sheaves. The authors manage these using **condensed mathematics** (developed by Clausen and Scholze), which provides a more flexible notion of continuity that tames these ill-behaved objects.

## Why It Matters

In pure mathematics, this work provides the first systematic derived geometric framework for global propagation of singularities in NLPDEs, unifying algebraic, analytic, and non-archimedean settings under one coherent framework. It opens the door to derived index theory for nonlinear operators — a generalization of the **Atiyah-Singer index theorem**, a landmark 20th-century result connecting the geometry of a space to the behavior of differential equations defined on it — which the authors flag as the subject of a companion paper.

For fundamental physics, the stakes are higher still. The equations of quantum gravity, string theory, and topological field theory involve NLPDEs on highly singular or derived geometric backgrounds. The ability to track singularity propagation globally is essential for making sense of these theories. The treatment of overconvergent jets and analytic de Rham functors also opens a path toward a homotopical generalization of the **Cartan-Kähler theorem**, which governs the existence of solutions to systems of equations describing geometric constraints on surfaces and higher-dimensional spaces.

> **Bottom Line:** By recasting nonlinear PDEs as derived geometric objects and micro-linearizing them through loop stacks and Hodge deformations, Kryczka, Sheshmani, and Yau prove that solution singularities propagate along characteristic directions — even on the most exotic spaces physics demands — giving mathematicians and physicists a powerful new handle on some of the hardest equations in science.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work unifies derived algebraic geometry, microlocal analysis, and D-module theory to attack nonlinear PDE problems central to both pure mathematics and theoretical physics, demonstrating the power of abstract geometric machinery in concrete analytical settings.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The derived moduli framework provides a rigorous foundation for studying solution spaces of complex nonlinear systems — mathematical infrastructure directly relevant to understanding the geometry of loss landscapes and solution manifolds in machine learning models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The global propagation-of-singularities theorems apply directly to the NLPDEs of general relativity and gauge theory, providing new tools to analyze singularity formation and well-posedness in the equations governing fundamental forces.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">This paper is the first in a multi-part series; upcoming work will develop derived tricomplexes and non-linear index theory with direct applications to mathematical physics. Available on arXiv (submitted June 2024) by Kryczka, Sheshmani, and Yau.</span></div></div>
</div>
