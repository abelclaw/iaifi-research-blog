---
abstract: Recent results suggest that flow-based algorithms may provide efficient
  sampling of field distributions for lattice field theory applications, such as studies
  of quantum chromodynamics and the Schwinger model. In this work, we provide a numerical
  demonstration of robust flow-based sampling in the Schwinger model at the critical
  value of the fermion mass. In contrast, at the same parameters, conventional methods
  fail to sample all parts of configuration space, leading to severely underestimated
  uncertainties.
arxivId: '2202.11712'
arxivUrl: https://arxiv.org/abs/2202.11712
authors:
- Michael S. Albergo
- Denis Boyda
- Kyle Cranmer
- Daniel C. Hackett
- Gurtej Kanwar
- Sébastien Racanière
- Danilo J. Rezende
- Fernando Romero-López
- Phiala E. Shanahan
- Julian M. Urban
concepts:
- normalizing flows
- lattice gauge theory
- topological freezing
- monte carlo methods
- equivariant neural networks
- phase transitions
- symmetry preservation
- quantum field theory
- density estimation
- symmetry breaking
- lattice qcd
- stochastic processes
figures:
- /iaifi-research-blog/figures/2202_11712/figure_1.png
- /iaifi-research-blog/figures/2202_11712/figure_1.png
- /iaifi-research-blog/figures/2202_11712/figure_2.png
- /iaifi-research-blog/figures/2202_11712/figure_2.png
- /iaifi-research-blog/figures/2202_11712/figure_3.png
- /iaifi-research-blog/figures/2202_11712/figure_3.png
pdfUrl: https://arxiv.org/pdf/2202.11712v1
published: '2022-02-23T19:00:00+00:00'
theme: Theoretical Physics
title: Flow-based sampling in the lattice Schwinger model at criticality
wordCount: 1145
---

## The Big Picture

Imagine mapping an enormous mountain range by hiking through it, but the valleys are so deep and the passes so steep that you could wander for years never reaching the other side. You'd eventually produce a detailed map of the one valley where you started. It would look complete, and you'd never know what you were missing.

That's the crisis facing physicists who study quantum chromodynamics (QCD), the theory of the strong nuclear force that binds quarks into the protons and neutrons at the core of every atom. To compute predictions from QCD, researchers use **lattice field theory**, a technique that divides space and time into a discrete grid (like pixels in an image extended through time) and uses statistical sampling to calculate how quantum fields behave across that grid.

The standard workhorse algorithm, **Hybrid Monte Carlo (HMC)**, navigates this field configuration space like a hiker, evolving configurations one step at a time. Near special parameter values called critical points, the space develops enormous barriers. HMC gets stuck, sampling only a fraction of the space it needs to explore. Worse, it doesn't realize it's lost.

A collaboration spanning MIT, NYU, DeepMind, and other institutions has demonstrated a fundamentally different approach: using machine-learning-based **normalizing flows** to leap over those barriers entirely, producing accurate results precisely where conventional methods silently fail.

> **Key Insight:** At the critical fermion mass in the Schwinger model, flow-based sampling produces correct results with properly scaling uncertainties, while HMC yields confidently wrong answers, underestimating its own errors by a factor that grows with sample size.

## How It Works

The test case is the **Schwinger model**, two-dimensional quantum electrodynamics with two flavors of fermions. Though simpler than full QCD, it shares its most troublesome features: confinement (quarks can't escape their bound states), chiral symmetry breaking (where a left-right symmetry in the fundamental equations spontaneously breaks down, governing how particles acquire mass), and topological structure.

Topological structure is the crux of the problem. Quantum field configurations sort into discrete categories called **topological sectors**, characterized by an integer called the topological charge, essentially a winding number counting how many times the field twists as you traverse the lattice. HMC moves continuously through configuration space, like a ball rolling across a surface. Near criticality, the barriers between sectors grow enormous. The ball stays trapped in one valley forever.

The result is **topological freezing**: HMC samples only a few sectors, producing estimates of observables like the chiral condensate ⟨ψψ⟩ (a measure of how strongly chiral symmetry is broken in the vacuum) that appear statistically stable but are deeply biased.

![Figure 1](figure:1)

The figure tells the story bluntly. Six independent HMC runs on a 16×16 lattice at critical parameters (β = 2.0, κ = 0.276) all converge to the *wrong* answer. Their uncertainties shrink with more samples, creating false confidence. Only when a rare tunneling event occurs does a run jump toward the true value. The flow-based sampler, by contrast, converges cleanly to the correct value with uncertainties that scale as 1/√N, exactly as expected for independent samples.

Flow-based sampling escapes the barrier problem through its architecture. **Normalizing flows** are neural networks trained to transform samples from a simple base distribution into samples matching the target distribution of field configurations. Because they generate samples by direct transformation rather than sequential Markov steps, they aren't bound by the topology of the configuration space. A flow can produce configurations from any topological sector in a single forward pass.

The architecture is built from several components:

- **Gauge-equivariant coupling layers** that respect the gauge symmetry of the theory, ensuring the learned distribution obeys the same physical constraints as the true one
- Each layer updates an "active" subset of lattice links conditioned on a "frozen" subset, with multiple partitionings ensuring all variables get updated
- **Wilson loops**, closed paths around individual lattice squares whose values measure local field strength in a gauge-invariant way, provide context that each coupling layer uses when updating its active variables
- Fermions are handled through exact evaluation of the **fermion determinant**, a single mathematical quantity encoding the full quantum contribution of all fermion fields to each configuration's probability

After training, the flow produces candidate configurations that are accepted or rejected via independence Metropolis sampling. This step guarantees exact samples from the target distribution, correcting for any mismatch between the learned and true distributions.

![Figure 2](figure:2)

The topological charge distribution reveals the mechanism directly. The flow-based sampler populates all sectors with frequencies matching theoretical predictions. HMC samples cluster in a narrow range, entirely missing the tails.

## Why It Matters

Topological freezing is one of the central obstacles to the next generation of lattice QCD calculations. As physicists push toward the continuum limit (finer lattices approaching the true quantum field theory), freezing gets worse, not better. The field has known about this wall for decades.

The results here matter beyond the Schwinger model. Each element of the approach has a four-dimensional analog that could extend to full QCD: gauge equivariance, fermion determinant evaluation, independence Metropolis correction. That extension is a far harder problem. The lattice becomes four-dimensional, the gauge group is SU(3) rather than U(1), and evaluating fermion determinants scales poorly with lattice size. But the blueprint is concrete.

The same topological charge distribution problem afflicts state-of-the-art QCD calculations today. Underestimated uncertainties could silently distort predictions for hadron masses, decay rates, and other quantities that physicists compare against experiment.

There is also a machine learning angle. The training process optimizes the flow to minimize divergence between the learned and target distributions, which is a generative modeling problem. Building the gauge symmetry of the theory directly into the network architecture turns out to be essential: physics-informed architectures solve sampling tasks that generic approaches cannot.

> **Bottom Line:** Flow-based sampling with gauge-equivariant neural networks successfully navigates topological freezing in a fermionic gauge theory at criticality, a regime where the standard algorithm produces confidently wrong results. This opens a concrete path toward more reliable lattice QCD calculations.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work applies normalizing flows and gauge-equivariant neural networks to a core problem in lattice gauge theory, showing that machine learning can overcome sampling barriers that have limited quantum field theory calculations for decades.

- **Impact on Artificial Intelligence:** The research advances gauge-equivariant flow architectures, a class of physics-informed generative models that build symmetry constraints directly into the network structure, yielding samplers that are both expressive and physically consistent.

- **Impact on Fundamental Interactions:** By solving topological freezing in the Schwinger model at criticality, this work establishes a framework that could enable more reliable calculations of QCD observables in the continuum limit, with direct implications for precision tests of the Standard Model.

- **Outlook and References:** The immediate next steps involve scaling these methods to larger lattices and eventually to four-dimensional SU(3) gauge theory; the paper is available at [arXiv:2202.11712](https://arxiv.org/abs/2202.11712).
