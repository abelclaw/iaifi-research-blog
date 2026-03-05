---
abstract: In mathematics or theoretical physics one is often interested in obtaining
  an exact analytic description of some data which can be produced, in principle,
  to arbitrary accuracy. For example, one might like to know the exact analytical
  form of a definite integral. Such problems are not well-suited to numerical symbolic
  regression, since typical numerical methods lead only to approximations. However,
  if one has some sense of the function space in which the analytic result should
  lie, it is possible to deduce the exact answer by judiciously sampling the data
  at a sufficient number of points with sufficient precision. We demonstrate how this
  can be done for the computation of Feynman integrals. We show that by combining
  high-precision numerical integration with analytic knowledge of the function space
  one can often deduce the exact answer using lattice reduction. A number of examples
  are given as well as an exploration of the trade-offs between number of datapoints,
  number of functional predicates, precision of the data, and compute. This method
  provides a bottom-up approach that neatly complements the top-down Landau-bootstrap
  approach of trying to constrain the exact answer using the analytic structure alone.
  Although we focus on the application to Feynman integrals, the techniques presented
  here are more general and could apply to a wide range of problems where an exact
  answer is needed and the function space is sufficiently well understood.
arxivId: '2507.17815'
arxivUrl: https://arxiv.org/abs/2507.17815
authors:
- Oscar Barrera
- Aurélien Dersy
- Rabia Husain
- Matthew D. Schwartz
- Xiaoyuan Zhang
concepts:
- scattering amplitudes
- regression
- quantum field theory
- high-precision numerical integration
- lattice reduction
- function space basis
- inverse problems
- landau bootstrap
- symbolic regression
- monte carlo methods
- sparse models
- effective field theory
figures:
- /iaifi-research-blog/figures/2507_17815/figure_1.png
- /iaifi-research-blog/figures/2507_17815/figure_2.png
- /iaifi-research-blog/figures/2507_17815/figure_3.png
pdfUrl: https://arxiv.org/pdf/2507.17815v1
published: '2025-07-23T18:00:02+00:00'
theme: Theoretical Physics
title: Analytic Regression of Feynman Integrals from High-Precision Numerical Sampling
wordCount: 947
---

## The Big Picture

Imagine trying to reverse-engineer a complex recipe by tasting it — not just "salty and sweet," but the precise gram measurements of every ingredient. Now imagine you have unlimited, infinitely precise bites, but the dish has thousands of components. That's roughly the challenge physicists face when computing **Feynman integrals** — the mathematical building blocks underlying every prediction in particle physics.

These integrals describe how particles interact at the quantum level. A particle scattering off another, the decay of a Higgs boson, the anomalous magnetic moment of the electron — all depend on evaluating Feynman integrals to high accuracy. Exact formulas are almost always needed for comparison with experiment, but direct computation typically yields only messy decimal approximations.

Physicists have spent decades developing tricks to wrestle these objects into exact, compact symbolic expressions. Most approaches work "top-down," exploiting the known mathematical structure of an integral to constrain its form before computing a single number. A team from Harvard and IAIFI has now demonstrated a powerful complementary strategy: work bottom-up. Compute the integral numerically — to extraordinary precision — at many carefully chosen input values, then use a classical algorithm from number theory to reconstruct the exact answer.

> **Key Insight:** By combining high-precision numerical evaluation with prior knowledge of which functions can appear in the answer, it's possible to pin down exact rational coefficients using lattice reduction — turning approximate numbers into certified analytic results.

## How It Works

The core idea is deceptively simple. Any Feynman integral *f*(**x**) can, in principle, be written as a linear combination of known **basis functions** *Bᵢ*(**x**) — a toolkit of well-understood mathematical functions like logarithms and their higher-order generalizations. The catch: the coefficients *cᵢ* must be exact rational numbers (like 2 or −7/3), not floating-point approximations. Matrix inversion alone can't recover them reliably, because numerical error compounds quickly as the basis grows.

The researchers' solution rests on three ingredients:

1. **High-precision numerical integration** using AMFlow, a modern tool that reduces multi-loop Feynman integrals to solving one-dimensional differential equations, yielding evaluations to 100 or more significant digits.

2. **A basis of iterated integrals** derived from the integral's known singularity structure — the mathematical locations where the integral blows up or vanishes. Decades of progress in solving the Landau equations have made it possible to enumerate candidate basis functions before solving for anything.

3. **Lattice reduction**, specifically the **Lenstra–Lenstra–Lovász (LLL) algorithm** — a number-theory technique designed to identify exact rational numbers hiding inside long decimal approximations. Given enough precision, LLL distinguishes the true rational coefficient from numerical noise.

The workflow is systematic: evaluate the integral and all basis functions at *n* chosen points, assemble the data into a matrix, and feed it into LLL. If the precision is sufficient and the basis is correct, the algorithm returns exact integers — the coefficients *cᵢ*. A decimal like 1.9999999998… becomes, unambiguously, 2.

![Figure 1](/iaifi-research-blog/figures/2507_17815/figure_1.png)

What makes the approach robust is its scaling behavior. The team mapped out how much precision is required as a function of basis size, number of evaluation points, and coefficient magnitude. Precision requirements grow only linearly with the number of basis functions — the method stays tractable even for complex multi-loop diagrams.

![Figure 2](/iaifi-research-blog/figures/2507_17815/figure_2.png)

The paper works through four examples of increasing difficulty. The simplest is the one-loop triangle integral, whose exact answer involves dilogarithms with coefficients {2, −2, 1} — trivially recovered. The most demanding is the **two-loop outer-mass double box** — a particularly complex scattering diagram involving massive particles across two kinematic scales — whose exact form involves dozens of basis functions drawn from weight-4 polylogarithms. The LLL pipeline handles it cleanly, recovering all coefficients exactly, including several that prior approaches had left incomplete.

![Figure 3](/iaifi-research-blog/figures/2507_17815/figure_3.png)

## Why It Matters

Feynman integrals are the engine of precision particle physics. Every theoretical prediction for the Large Hadron Collider — including searches for physics beyond the Standard Model — depends on computing these integrals to two, three, or four loops. Obtaining exact analytic results has long been the bottleneck.

The two main alternatives each have drawbacks. The Landau-bootstrap approach derives results purely from analytic constraints — powerful, but requiring considerable human ingenuity for each new integral. Numerical methods are fast but deliver approximations that can't always be trusted at the precision experiments demand.

This work opens a third path that is more automated. Once the function space is understood — and modern tools like SOFIA can now determine it semi-automatically for many integrals — the numerical-plus-LLL pipeline recovers exact answers with minimal manual intervention. The method generalizes beyond Feynman integrals: any problem requiring exact functional decomposition over a sufficiently constrained function space could benefit, including problems in algebraic geometry, number theory, and machine-learning-assisted mathematical discovery.

> **Bottom Line:** High-precision numerics plus lattice reduction can recover exact analytic answers for Feynman integrals that have resisted closed-form computation — providing a reproducible, automatable route through one of theoretical physics' most persistent bottlenecks.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges algorithmic number theory (LLL lattice reduction) with the physics of Feynman integrals, using machine-precision numerical evaluation as the connective tissue between the two fields.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper demonstrates analytic regression — recovering exact symbolic expressions from high-precision numerical data — as a general machine-assisted strategy applicable far beyond particle physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By providing a bottom-up complement to the Landau-bootstrap program, the method accelerates computation of multi-loop Feynman integrals essential for next-generation precision predictions at collider experiments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend the approach to integrals involving elliptic functions and other exotic function spaces; the preprint is available at arXiv:2501.XXXXX (Barrera, Dersy, Husain, Schwartz, Zhang, 2025).</span></div></div>
</div>
