---
abstract: The Wilson action for Euclidean lattice gauge theory defines a positive-definite
  transfer matrix that corresponds to a unitary lattice gauge theory time-evolution
  operator if analytically continued to real time. Hoshina, Fujii, and Kikukawa (HFK)
  recently pointed out that applying the Wilson action discretization to continuum
  real-time gauge theory does not lead to this, or any other, unitary theory and proposed
  an alternate real-time lattice gauge theory action that does result in a unitary
  real-time transfer matrix. The character expansion defining the HFK action is divergent,
  and in this work we apply a path integral contour deformation to obtain a convergent
  representation for U(1) HFK path integrals suitable for numerical Monte Carlo calculations.
  We also introduce a class of real-time lattice gauge theory actions based on analytic
  continuation of the Euclidean heat-kernel action. Similar divergent sums are involved
  in defining these actions, but for one action in this class this divergence takes
  a particularly simple form, allowing construction of a path integral contour deformation
  that provides absolutely convergent representations for U(1) and SU(N) real-time
  lattice gauge theory path integrals. We perform proof-of-principle Monte Carlo calculations
  of real-time U(1) and SU(3) lattice gauge theory and verify that exact results for
  unitary time evolution of static quark-antiquark pairs in (1 + 1)D are reproduced.
arxivId: '2103.02602'
arxivUrl: https://arxiv.org/abs/2103.02602
authors:
- Gurtej Kanwar
- Michael L. Wagman
concepts:
- lattice gauge theory
- path integral contour deformation
- monte carlo methods
- sign problem
- real-time transfer matrix
- symmetry preservation
- quantum field theory
- group theory
- stochastic processes
- quantum simulation
figures:
- /iaifi-research-blog/figures/2103_02602/figure_1.png
- /iaifi-research-blog/figures/2103_02602/figure_2.png
pdfUrl: https://arxiv.org/pdf/2103.02602v3
published: '2021-03-03T18:57:21+00:00'
theme: Theoretical Physics
title: 'Real-time lattice gauge theory actions: unitarity, convergence, and path integral
  contour deformations'
wordCount: 1272
---

## The Big Picture

Imagine trying to film a movie with a camera that can only take still photographs. For decades, physicists studying the strong nuclear force have faced exactly this problem. Lattice gauge theory, a computational technique for studying quantum chromodynamics (QCD), excels at capturing equilibrium snapshots of matter. But watching things *evolve* in real time? That's where the method breaks down.

The trouble is a mathematical trap. To make calculations tractable, physicists replace real time with "imaginary time," transforming their equations into a form computers can handle. The mathematical weights assigned to different field configurations then behave like ordinary probabilities, and efficient random sampling via **Monte Carlo methods** becomes possible: a sophisticated lottery for exploring which configurations matter most.

Flip back to real time, and those weights become rapidly oscillating quantities, swinging positive and negative, endlessly canceling each other out. Computing an average over them is like finding the average direction of a spinning compass: the signal drowns in noise. This is the infamous **sign problem**, and it has blocked physicists from computing real-time phenomena like the dynamics of quark-gluon plasma, early-universe phase transitions, and inclusive hadron scattering.

Progress requires two things: a real-time lattice formulation that preserves **unitarity** (the requirement that quantum probabilities sum to one) and a way to actually compute with it numerically. Hoshina, Fujii, and Kikukawa (HFK) solved the first problem but left the second open. Now, Gurtej Kanwar and Michael Wagman have tackled it, building convergent, computable representations of real-time lattice gauge theory using **path integral contour deformation**.

> **Key Insight:** Wick-rotating the standard Wilson action to real time produces a non-unitary theory. Kanwar and Wagman introduce a new class of actions with path integral deformations that are simultaneously unitary *and* numerically tractable, making possible the first proof-of-principle Monte Carlo calculations of real-time SU(3) gauge theory.

## How It Works

Start with why the naive approach fails. The **Wilson action**, the workhorse of Euclidean lattice gauge theory, defines **plaquettes**: tiny loops of gauge field tiling the lattice like squares on graph paper, whose contributions sum to the total action. Wick-rotating this to real time yields a **transfer matrix** (the object encoding how the quantum system evolves moment to moment) that is *not* unitary.

HFK's fix was to analytically continue the **character expansion** of the kinetic term, rewriting the action as a sum over fundamental symmetry modes of the gauge group, like decomposing a chord into individual notes. This produces a unitary transfer matrix. But there's a catch: the HFK action is an infinite series that diverges. For many field configurations the sum never converges to a finite number, making Monte Carlo sampling impossible. Kanwar and Wagman show this divergence is a generic feature of any local real-time lattice action with a unitary transfer matrix, not a quirk of HFK's particular construction.

![Figure 1](/iaifi-research-blog/figures/2103_02602/figure_1.png)

Their solution: **path integral contour deformation**. Borrowed from work on the sign problem in quantum mechanics and finite-density systems, the idea is to deform the integration contour in complexified field space. By Cauchy's theorem, certain deformations leave the total integral unchanged while taming the divergence. For the **U(1) HFK action** (U(1) being the simplest gauge theory, describing a single circular symmetry) Kanwar and Wagman construct an explicit deformation by:

1. Starting with the Euclidean action where everything converges
2. Continuously rotating the prefactor from −1 toward *i* (the Minkowski limit)
3. Tracking the contour deformation needed to maintain convergence at each step
4. Canceling contour segments related by periodicity

The result is an absolutely convergent representation of the U(1) HFK path integral, the first ever constructed.

![Figure 2](/iaifi-research-blog/figures/2103_02602/figure_2.png)

For **non-abelian** gauge theories like QCD, where symmetry operations don't commute, the HFK contour deformation becomes technically daunting. This motivated the paper's second major contribution: a new class of actions based on the **heat-kernel action** of Menotti and Onofri. Its advantage is that unitarity holds exactly at all lattice spacings, not just in the continuum limit, and the divergent sum takes a far simpler form.

A contour deformation tailored to this simpler structure gives absolutely convergent representations for both U(1) and **SU(N)**, the family of gauge theories that includes SU(3), the gauge group of QCD.


## Why It Matters

The payoff is immediate. Kanwar and Wagman perform the first numerical Monte Carlo calculations of real-time U(1) and SU(3) lattice gauge theory. Their benchmark, computing the time evolution of a static quark-antiquark pair in (1+1) dimensions, reproduces exact analytic results. It's a proof of principle, but the principle is the hard part.

SU(3) is the gauge group of QCD. Convergent real-time Monte Carlo sampling for SU(3) puts within reach a class of out-of-equilibrium phenomena that lattice methods have been unable to touch for decades. Transport coefficients of the quark-gluon plasma, needed to interpret heavy-ion collisions, require real-time correlators. So do inclusive hadron scattering cross-sections and properties of early-universe phase transitions.

The contour deformation framework is also naturally algorithmic, a structured mathematical transformation that could be learned and optimized by machine learning. Normalizing flow methods, which have already been applied to Euclidean lattice calculations, are a natural fit.


> **Bottom Line:** By combining a new unitary real-time lattice action with explicit path integral contour deformations, Kanwar and Wagman deliver the first convergent Monte Carlo calculations of real-time SU(3) gauge theory, opening a door to computing the dynamics of strongly coupled quantum fields.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits at the intersection of mathematical physics (path integral methods, group representation theory) and numerical computation (Monte Carlo sampling, contour deformations), applying algorithmic thinking directly to a fundamental physics problem.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The path integral contour deformation framework is a structured, learnable transformation and a natural target for machine learning optimization, which could improve sampling efficiency in future real-time lattice calculations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper resolves a long-standing obstacle to computing real-time observables in QCD, providing unitary, convergent actions for both U(1) and SU(3) gauge theories with proof-of-principle Monte Carlo verification.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend these contour deformations to (3+1)D and higher-dimensional gauge groups, and explore machine-learned deformations for improved sign-problem mitigation; see [arXiv:2103.02602](https://arxiv.org/abs/2103.02602) for the full paper.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Real-time lattice gauge theory actions: unitarity, convergence, and path integral contour deformations</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2103.02602</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Gurtej Kanwar", "Michael L. Wagman"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">The Wilson action for Euclidean lattice gauge theory defines a positive-definite transfer matrix that corresponds to a unitary lattice gauge theory time-evolution operator if analytically continued to real time. Hoshina, Fujii, and Kikukawa (HFK) recently pointed out that applying the Wilson action discretization to continuum real-time gauge theory does not lead to this, or any other, unitary theory and proposed an alternate real-time lattice gauge theory action that does result in a unitary real-time transfer matrix. The character expansion defining the HFK action is divergent, and in this work we apply a path integral contour deformation to obtain a convergent representation for U(1) HFK path integrals suitable for numerical Monte Carlo calculations. We also introduce a class of real-time lattice gauge theory actions based on analytic continuation of the Euclidean heat-kernel action. Similar divergent sums are involved in defining these actions, but for one action in this class this divergence takes a particularly simple form, allowing construction of a path integral contour deformation that provides absolutely convergent representations for U(1) and SU(N) real-time lattice gauge theory path integrals. We perform proof-of-principle Monte Carlo calculations of real-time U(1) and SU(3) lattice gauge theory and verify that exact results for unitary time evolution of static quark-antiquark pairs in (1 + 1)D are reproduced.</span></div></div>
</div>
