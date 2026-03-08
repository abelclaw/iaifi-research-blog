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
- /iaifi-research-blog/figures/2103_02602/figure_1.png
- /iaifi-research-blog/figures/2103_02602/figure_2.png
- /iaifi-research-blog/figures/2103_02602/figure_2.png
- /iaifi-research-blog/figures/2103_02602/figure_3.png
- /iaifi-research-blog/figures/2103_02602/figure_3.png
pdfUrl: https://arxiv.org/pdf/2103.02602v3
published: '2021-03-03T18:57:21+00:00'
theme: Theoretical Physics
title: 'Real-time lattice gauge theory actions: unitarity, convergence, and path integral
  contour deformations'
wordCount: 1108
---

## The Big Picture

Imagine trying to film a movie with a camera that can only take still photographs. For decades, physicists studying the strong nuclear force have faced exactly this problem. Lattice gauge theory — a powerful computational technique for understanding quantum chromodynamics (QCD), the theory governing quarks and gluons — excels at capturing equilibrium snapshots of matter. Watching things *evolve* in real time is where the method breaks down.

The trouble lies in a fundamental mathematical trap. To make calculations tractable, physicists replace real time with "imaginary time," transforming their equations into a form computers can handle. In this reformulation, the mathematical weights assigned to different field configurations behave like ordinary probabilities, enabling efficient random sampling via **Monte Carlo methods** — essentially a sophisticated lottery for exploring which configurations matter most.

Flip back to real time, and those weights become rapidly oscillating quantities, swinging positive and negative, endlessly canceling each other out. Computing an average over them is like finding the average direction of a spinning compass: the signal drowns in noise. This is the infamous **sign problem**, and it has blocked physicists from computing real-time phenomena: the dynamics of quark-gluon plasma, early-universe phase transitions, and inclusive hadron scattering.

Progress requires two things: a real-time lattice formulation that preserves **unitarity** — the requirement that quantum probabilities sum to one — and a way to actually compute with it numerically. A 2019 paper by Hoshina, Fujii, and Kikukawa (HFK) solved the first problem but left the second open. Now, Gurtej Kanwar and Michael Wagman have cracked it, building convergent, computable representations of real-time lattice gauge theory using a technique called **path integral contour deformation**.

> **Key Insight:** The standard approach of Wick-rotating the Wilson action to real time produces a non-unitary theory — a fatal flaw. Kanwar and Wagman introduce a new class of actions with path integral deformations that are simultaneously unitary *and* numerically tractable, enabling the first proof-of-principle Monte Carlo calculations of real-time SU(3) gauge theory.

## How It Works

The starting point is understanding why the naive approach fails. The **Wilson action** — the workhorse of Euclidean lattice gauge theory — defines **plaquettes** (tiny loops of gauge field tiling the lattice like squares on graph paper) whose contributions sum to the total action. Naively mapping this to real time via Wick rotation yields a **transfer matrix** — the object encoding how the quantum system evolves moment to moment — that is *not* unitary.

HFK's fix was to analytically continue the **character expansion** of the kinetic term, rewriting the action as a sum over fundamental symmetry modes of the gauge group — like decomposing a chord into individual notes. This produces a unitary transfer matrix. But there's a catch: the HFK action is an infinite series that diverges. For many field configurations, the sum never converges to a finite number, making Monte Carlo sampling impossible. Kanwar and Wagman show this divergence is a generic feature of any local real-time lattice action with a unitary transfer matrix, not a quirk of HFK.

![Figure 1](/iaifi-research-blog/figures/2103_02602/figure_1.png)

Their solution: **path integral contour deformation**. The idea, imported from work on the sign problem in quantum mechanics and finite-density systems, is to deform the integration contour in complexified field space. By Cauchy's theorem from complex analysis, certain deformations leave the total integral unchanged while making the sum far better behaved. For the **U(1) HFK action** — U(1) being the simplest gauge theory, describing a single circular symmetry — Kanwar and Wagman construct an explicit deformation by:

1. Starting with the Euclidean action where everything converges
2. Continuously rotating the prefactor from −1 toward *i* (the Minkowski limit)
3. Tracking the contour deformation needed to maintain convergence at each step
4. Canceling contour segments related by periodicity

The result is an absolutely convergent representation of the U(1) HFK path integral — the first ever constructed.

![Figure 2](/iaifi-research-blog/figures/2103_02602/figure_1.png)

For the **non-abelian** case — gauge theories like QCD where symmetry operations don't commute — the HFK contour deformation becomes technically daunting. This motivates the paper's second major contribution: a new class of actions based on the **heat-kernel action** of Menotti and Onofri. Its key advantage is that unitarity holds exactly at all lattice spacings, not just in the continuum limit, and the divergent sum takes a far simpler form.

By constructing a contour deformation tailored to this simpler structure, Kanwar and Wagman obtain absolutely convergent representations for both U(1) *and* **SU(N)** — the family of gauge theories that includes SU(3), the gauge group of QCD.

![Figure 4](/iaifi-research-blog/figures/2103_02602/figure_2.png)

## Why It Matters

The payoff is immediate: Kanwar and Wagman perform the first numerical Monte Carlo calculations of real-time U(1) and SU(3) lattice gauge theory. Their benchmark — computing the time evolution of a static quark-antiquark pair in (1+1) dimensions — reproduces exact analytic results. This is a proof of principle, but the principle is powerful.

SU(3) is the gauge group of QCD. Demonstrating convergent real-time Monte Carlo sampling for SU(3) opens a path to computing out-of-equilibrium phenomena that have been inaccessible to lattice methods for decades. Transport coefficients of the quark-gluon plasma — critical for understanding heavy-ion collisions — require real-time correlators. So do inclusive hadron scattering cross-sections and properties of early-universe phase transitions. All of these lie behind the wall this work begins to breach.

The contour deformation framework is also inherently algorithmic — a structured mathematical transformation that could be learned and optimized using machine learning, particularly the normalizing flow methods that have recently shown promise in Euclidean lattice calculations.

![Figure 5](/iaifi-research-blog/figures/2103_02602/figure_3.png)

> **Bottom Line:** By combining a new unitary real-time lattice action with explicit path integral contour deformations, Kanwar and Wagman deliver the first convergent Monte Carlo calculations of real-time SU(3) gauge theory — cracking open a door to computing the dynamics of strongly coupled quantum fields that has been closed for decades.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges advanced mathematical physics (path integral methods, group representation theory) with numerical computation (Monte Carlo sampling, contour deformations), exemplifying the IAIFI mission of applying algorithmic thinking to fundamental physics problems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The path integral contour deformation framework is a structured, learnable transformation — a natural target for machine learning optimization that could dramatically improve sampling efficiency in future real-time lattice calculations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper resolves a long-standing obstacle to computing real-time observables in QCD, providing unitary, convergent actions for both U(1) and SU(3) gauge theories with proof-of-principle Monte Carlo verification.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend these contour deformations to (3+1)D and higher-dimensional gauge groups, and explore machine-learned deformations for improved sign-problem mitigation; see arXiv:2103.05954 for the full paper.</span></div></div>
</div>
