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

Imagine comparing two abstract paintings by measuring how much paint you'd have to physically move to transform one into the other. That's essentially what particle physicists do every time they analyze a collision event at the Large Hadron Collider, and until now, it required a slow, grueling calculation every single time.

When protons smash together at the LHC, they spray hundreds of particles across a detector in complex patterns. Physicists need precise mathematical tools to compare these "events," classify them, and extract the underlying physics.

The **Energy Mover's Distance (EMD)**, the minimum energy cost to rearrange one collision event's particle spray into another, became a gold-standard tool for exactly this purpose. But it has a serious bottleneck: there's no simple formula for it. You have to run a slow numerical calculation from scratch for every pair of events, and with millions of events per second streaming from the LHC, that adds up fast.

Researchers at MIT and UCLA have now derived a simpler alternative called the **Spectral Energy Mover's Distance (SEMD)**. It has an exact, plug-in formula rather than requiring numerical optimization. Their computational framework, SPECTER, runs up to a thousand times faster than standard tools.

> **Key Insight:** By transforming collision events into a one-dimensional "spectral" representation, the SEMD can be computed exactly with a simple formula rather than a numerical optimization, enabling 1 million metric evaluations per second on a GPU.

## How It Works

The trick is a mathematical transformation. A standard collision event lives in two dimensions: a scatter plot of energy deposits across a spherical detector surface. Computing the EMD on this 2D surface requires solving an **optimal transport problem**, finding the most efficient way to "move" one particle pattern into another. It's a transportation logistics puzzle with no shortcut formula. Two-dimensional point clouds have no natural ordering, so no clean, general equation exists.

The SEMD sidesteps this entirely. Each event is converted into a **spectral function**, a one-dimensional summary that encodes all pairwise angles between particles, weighted by their energy products. Think of taking a 2D photograph and computing a 1D histogram of all pairwise pixel distances. You lose specific particle positions but retain the relational geometry. And one-dimensional distributions *do* have a natural ordering.

![Figure 1](figure:1)

In one dimension, the **Wasserstein-2 distance** (a standard measure of how different two distributions are) has a clean, exact formula: the integral of the squared difference of their **quantile functions**. Quantile functions describe each distribution by its percentile thresholds, putting both on a common scale. For the p=2 SEMD, this integral reduces to an explicit algebraic expression involving pairwise angle cosines between particles from both events. No optimization loop. Just plug in the numbers.

The computational savings are stark:

- **EMD**: O(N³), scaling with the cube of particle count
- **SEMD**: O(N² log N), where the log N overhead comes only from sorting particle pairs

For a typical LHC jet with ~50 particles, that's roughly 10,000× fewer operations.

The SPECTER code implements the SEMD and a family of new observables in a parallelized GPU architecture. It introduces a zoo of **spectral shape observables**, geometric quantities that characterize jet shape by measuring distance to idealized reference configurations:

- **N-sPronginess**: Does the jet look like one, two, or three back-to-back streams?
- **spRinginess**: Does the jet energy form a ring?
- **spLineliness** and **sDiskiness**: Is the jet pencil-like or disk-like?
- **sThrust**, **spIsotropy**, **spEquatorialness**: Global shapes measuring how isotropically particles are distributed

Many of these also have exact, plug-in formulas. Computing event isotropy the old way required solving a full optimal transport problem. With SEMD, it's a formula you can write on a napkin.

![Figure 3](figure:3)

In benchmarks, SPECTER evaluates the SEMD up to 1,000 times faster than the POT (Python Optimal Transport) library evaluates the EMD. On a GPU, it reaches 1 million pairwise distance evaluations per second, compressing hours-long computations into seconds.

## Why It Matters

These speed gains make previously impractical analyses routine. Computing pairwise distances across an entire dataset reveals the **correlation dimension** of event space, a geometric measure of how many independent degrees of freedom the particle dynamics actually explore. With millions of events, this was simply too expensive before.

The exact formulas also make the SEMD accessible to pen-and-paper theory in a way the EMD never was. Because the EMD required solving an optimization problem, it resisted analytical treatment. The SEMD's closed-form expression enables **perturbative QCD calculations**, connecting a practical measurement tool directly to first-principles predictions from the theory of the strong nuclear force.

At the LHC trigger level, where collision events must be filtered in real time with microsecond latency, SPECTER's speed could enable event-shape observables that were previously too expensive to compute online.

The SEMD and EMD aren't identical. Degeneracies in the spectral representation mean two physically different events can occasionally have zero SEMD. But for jet classification, event shape measurement, and QCD studies, empirical tests show the two metrics perform comparably, with SEMD offering its massive speed advantage.

> **Bottom Line:** SPECTER delivers the first exact, closed-form metric on particle collision events, implemented in a framework up to 1,000× faster than existing tools and potentially fast enough for real-time event shape analysis at the LHC.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work applies optimal transport theory from mathematics and machine learning to particle physics, deriving closed-form geometric observables that connect abstract measure theory with QCD phenomenology at the LHC.

- **Impact on Artificial Intelligence:** The spectral transformation technique, converting 2D unordered point clouds to 1D ordered distributions to obtain closed-form distances, is a strategy applicable well beyond collider physics to geometric learning and set-based metric computations more broadly.

- **Impact on Fundamental Interactions:** SPECTER enables practical computation of IRC-safe event shape observables at collider scale, making perturbative QCD calculations of metric-based observables feasible and potentially supporting real-time event classification at the LHC trigger level.

- **Outlook and References:** Future directions include extending spectral observables to three-dimensional detectors, exploring SEMD-based machine learning for event classification, and computing perturbative QCD predictions for the new spectral shapes; the paper is available at [arXiv:2410.05379](https://arxiv.org/abs/2410.05379).
