---
abstract: The Energy Mover's Distance (EMD) has seen use in collider physics as a
  metric between events and as a geometric method of defining infrared and collinear
  safe observables. Recently, the Spectral Energy Mover's Distance (SEMD) has been
  proposed as a more analytically tractable alternative to the EMD. In this work,
  we obtain a closed-form expression for the Riemannian-like p = 2 SEMD metric between
  events, eliminating the need to numerically solve an optimal transport problem.
  Additionally, we show how the SEMD can be used to define event and jet shape observables
  by minimizing the distance between events and parameterized energy flows (similar
  to the EMD), and we obtain closed-form expressions for several of these observables.
  We also present the SPECTER framework, an efficient and highly parallelized implementation
  of the SEMD metric and SEMD-derived shape observables as an analogue of the previously-introduced
  SHAPER for EMD-based computations. We demonstrate that computing the SEMD with SPECTER
  can be up to a thousand times faster than computing the EMD with standard optimal
  transport libraries.
arxivId: '2410.05379'
arxivUrl: https://arxiv.org/abs/2410.05379
authors:
- Rikab Gambhir
- Andrew J. Larkoski
- Jesse Thaler
concepts:
- optimal transport
- collider physics
- spectral event metric
- jet physics
- spectral methods
- irc-safe observables
- scalability
- event reconstruction
- quantum field theory
- symmetry preservation
- geometric deep learning
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2410_05379/figure_1.png
- /iaifi-research-blog/figures/2410_05379/figure_1.png
- /iaifi-research-blog/figures/2410_05379/figure_2.png
- /iaifi-research-blog/figures/2410_05379/figure_2.png
- /iaifi-research-blog/figures/2410_05379/figure_3.png
- /iaifi-research-blog/figures/2410_05379/figure_3.png
pdfUrl: https://arxiv.org/pdf/2410.05379v3
published: '2024-10-07T18:00:01+00:00'
theme: Theoretical Physics
title: 'SPECTER: Efficient Evaluation of the Spectral EMD'
wordCount: 1053
---

## The Big Picture

Imagine comparing two abstract paintings by measuring how much paint you'd have to physically move to transform one into the other. That's essentially what particle physicists do every time they analyze a collision event at the Large Hadron Collider — and until now, it required a slow, grueling calculation every single time.

When protons smash together at the LHC, they spray hundreds of particles across a detector in complex patterns. Physicists need precise mathematical tools to compare these "events," classify them, and extract the underlying physics.

The **Energy Mover's Distance (EMD)** — the minimum energy cost to rearrange one collision event's particle spray into another — became a gold-standard tool for exactly this purpose. But the EMD has a serious bottleneck: there's no simple formula for it. You have to run a slow numerical calculation from scratch for every pair of events, and with millions of events per second streaming from the LHC, that adds up fast.

Researchers at MIT and UCLA have now derived a fundamentally simpler alternative — the **Spectral Energy Mover's Distance (SEMD)**, which has an exact, plug-in formula rather than requiring a numerical calculation — and wrapped it in a computational framework called SPECTER that runs up to a thousand times faster.

> **Key Insight:** By transforming collision events into a one-dimensional "spectral" representation, the SEMD can be computed exactly with a simple formula rather than a numerical optimization, enabling 1 million metric evaluations per second on a GPU.

## How It Works

The trick lies in a mathematical transformation. A standard collision event lives in two dimensions — a scatter plot of energy deposits on a spherical detector surface. Computing the EMD on this 2D landscape requires solving an **optimal transport problem**: finding the most efficient way to "move" one particle pattern into another, like a transportation logistics puzzle with no shortcut formula. Two-dimensional point clouds have no natural ordering, so no clean, general equation exists.

The SEMD sidesteps this entirely. Each event is converted into a **spectral function** — a one-dimensional summary encoding all pairwise angles between particles, weighted by their energy products. Think of taking a 2D photograph and computing a 1D histogram of all pairwise pixel distances. You lose specific particle positions but retain their relational geometry — and crucially, one-dimensional distributions *do* have a natural ordering.

![Figure 1](/iaifi-research-blog/figures/2410_05379/figure_1.png)

In one dimension, the **Wasserstein-2 distance** — a standard measure of how different two distributions are — has a clean, exact formula: the integral of the squared difference of their **quantile functions**, which describe each distribution by its percentile thresholds and put both on a common scale. For the p=2 SEMD, this integral reduces to an explicit algebraic formula involving pairwise angle cosines between particles from both events. No optimization loop — just plug in the numbers.

The computational savings are dramatic:

- **EMD**: O(N³) — scales with the cube of particle count
- **SEMD**: O(N² log N) — the log N overhead comes only from sorting particle pairs

For a typical LHC jet with ~50 particles, this means roughly 10,000x fewer operations at the algorithmic level.

The SPECTER code, released alongside the paper, implements the SEMD and a family of new observables in a parallelized GPU architecture. It introduces a zoo of **spectral shape observables** — geometric quantities characterizing jet shape by measuring distance to idealized reference configurations:

- **N-sPronginess**: Does the jet look like one, two, or three back-to-back streams?
- **spRinginess**: Does the jet energy form a ring?
- **spLineliness** and **sDiskiness**: Is the jet pencil-like or disk-like?
- **sThrust**, **spIsotropy**, **spEquatorialness**: Global shapes measuring how isotropically particles are distributed

Many of these also have exact, plug-in formulas. Computing event isotropy the old way required solving a full optimal transport problem. With SEMD, it's a formula you can write on a napkin.

![Figure 3](/iaifi-research-blog/figures/2410_05379/figure_2.png)

On benchmark tests, SPECTER evaluates the SEMD up to **1,000 times faster** than the POT (Python Optimal Transport) library evaluates the EMD. On a GPU, SPECTER reaches 1 million pairwise distance evaluations per second — turning hours-long computations into seconds.

## Why It Matters

The speed gains unlock fundamentally new analyses. Computing pairwise distances across an entire dataset reveals the **correlation dimension** of event space — a geometric measure of the data's complexity, indicating how many independent degrees of freedom the particle dynamics actually explore. Previously impractical for large datasets, this becomes routine with SPECTER.

The exact formulas also open a theoretical door that was previously locked. The EMD resisted mathematical analysis because it required solving an optimization problem. The SEMD's explicit formula enables **perturbative QCD calculations** — step-by-step predictions built from the fundamental theory of the strong nuclear force — connecting this practical measurement tool directly to first-principles theory.

At the LHC trigger level, where collision events must be filtered in real time with microsecond latency, SPECTER's speed could enable event-shape observables that were previously too expensive to compute online.

The authors note that SEMD and EMD aren't identical — degeneracies in the spectral representation mean two physically different events can occasionally have zero SEMD. But for jet classification, event shape measurement, and QCD studies, empirical tests show the two metrics perform comparably, with SEMD offering its massive speed advantage.

> **Bottom Line:** SPECTER delivers the first exact, closed-form metric on particle collision events — implemented in a framework up to 1,000x faster than existing tools, potentially enabling real-time event shape analysis at the LHC.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies optimal transport theory from mathematics and machine learning to fundamental particle physics, deriving closed-form geometric observables that bridge abstract measure theory with QCD phenomenology at the LHC.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The spectral transformation technique — converting 2D unordered point clouds to 1D ordered distributions to achieve closed-form distances — is a broadly applicable strategy for accelerating geometric deep learning and set-based metric computations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">SPECTER enables practical computation of IRC-safe event shape observables at collider scale, opening the door to perturbative QCD calculations of metric-based observables and potentially real-time event classification at the LHC trigger level.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending spectral observables to three-dimensional detectors, exploring SEMD-based machine learning for event classification, and computing perturbative QCD predictions for the new spectral shapes; the paper is available at arXiv:2412.15184.</span></div></div>
</div>
