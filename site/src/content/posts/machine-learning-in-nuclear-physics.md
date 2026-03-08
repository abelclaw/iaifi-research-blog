---
abstract: "Advances in machine learning methods provide tools that have broad applicability\
  \ in scientific research. These techniques are being applied across the diversity\
  \ of nuclear physics research topics, leading to advances that will facilitate scientific\
  \ discoveries and societal applications.\n  This Review gives a snapshot of nuclear\
  \ physics research which has been transformed by machine learning techniques."
arxivId: '2112.02309'
arxivUrl: https://arxiv.org/abs/2112.02309
authors:
- Amber Boehnlein
- Markus Diefenthaler
- Cristiano Fanelli
- Morten Hjorth-Jensen
- Tanja Horn
- Michelle P. Kuchera
- Dean Lee
- Witold Nazarewicz
- Kostas Orginos
- Peter Ostroumov
- Long-Gang Pang
- Alan Poon
- Nobuo Sato
- Malachi Schram
- Alexander Scheinker
- Michael S. Smith
- Xin-Nian Wang
- Veronique Ziegler
concepts:
- bayesian inference
- uncertainty quantification
- surrogate modeling
- lattice qcd
- monte carlo methods
- classification
- inverse problems
- effective field theory
- regression
- anomaly detection
- particle tracking
- simulation-based inference
- experimental design
figures:
- /iaifi-research-blog/figures/2112_02309/figure_1.png
- /iaifi-research-blog/figures/2112_02309/figure_1.png
- /iaifi-research-blog/figures/2112_02309/figure_2.png
- /iaifi-research-blog/figures/2112_02309/figure_2.png
- /iaifi-research-blog/figures/2112_02309/figure_3.png
- /iaifi-research-blog/figures/2112_02309/figure_3.png
pdfUrl: https://arxiv.org/pdf/2112.02309v2
published: '2021-12-04T11:26:00+00:00'
theme: Theoretical Physics
title: Machine Learning in Nuclear Physics
wordCount: 1058
---

## The Big Picture

Imagine trying to solve a jigsaw puzzle with a trillion pieces, where every piece connects to every other piece in ways governed by quantum mechanics. That is, roughly speaking, what nuclear physicists face every day.

The atomic nucleus, a tiny bundle of protons and neutrons crammed into a space millions of times smaller than a single atom, is one of the most complex physical systems in the universe. Predicting how nuclei behave, how they smash together at high energies, or how they decay requires calculations of immense difficulty. Classical computational methods strain under the load.

A new review by researchers from Jefferson Lab, MIT, Michigan State, Lawrence Berkeley, and more than a dozen other institutions surveys how machine learning is reshaping this centuries-old field. The paper covers everything from detector design to taming mathematical obstacles that have blocked certain quantum calculations for decades. The transformation it describes is already well underway.

This is not a promise of future breakthroughs. It is a field already transformed.

> **Key Insight:** Machine learning is not just speeding up calculations in nuclear physics. It is making previously intractable problems solvable, from predicting nuclear structure properties to reconstructing particle collisions in real time.

## How It Works

The authors organize ML applications into four major pillars: **nuclear theory**, **experimental methods**, **accelerator science**, and **nuclear data**. Each pillar uses different architectures to address fundamentally different problems.

![Figure 1](figure:1)

Start with nuclear theory. **Low-energy nuclear theory**, the study of how forces between protons and neutrons determine nuclear structure, has long been limited by quantum-mechanical complexity. Even moderate nuclei contain dozens of interacting particles, and exact solutions are computationally forbidden. ML now provides surrogate models that predict nuclear masses, binding energies, and decay rates orders of magnitude faster than traditional methods.

Researchers have applied **Gaussian processes** (statistical techniques that express predictions as probability distributions rather than single values), **Bayesian neural networks** (which track uncertainty alongside predictions), and deep feedforward networks to interpolate and extrapolate nuclear properties across the chart of nuclides, the periodic-table-like map of all known atomic nuclei.

**Lattice QCD**, the leading computational approach to the theory of quarks and gluons, is where ML tackles two of the hardest outstanding problems. The **sign problem** arises because the mathematical weight assigned to each possible field configuration can become a complex number rather than a simple positive one, causing catastrophic cancellations when summing millions of contributions. ML-based flow models now generate configurations that avoid the worst of these cancellations.

**Normalizing flows** and **generative models**, techniques that learn to sample from complex probability distributions, also produce independent lattice field configurations far more efficiently than traditional Markov-chain Monte Carlo methods, which generate configurations one laborious step at a time. This could cut the cost of a single lattice calculation by orders of magnitude.

On the experimental side, the challenges are different but equally brutal:

- **Charged particle tracking** in detectors produces millions of hits per second; ML-based graph neural networks reconstruct particle trajectories in real time with accuracy rivaling hand-tuned algorithms
- **Calorimetry** uses convolutional neural networks to extract energies and positions from pixel-level detector readout
- **Particle identification** and **event classification** use boosted decision trees and deep networks to distinguish signal from noise in flooded data environments
- **Streaming detector readout** poses a data-volume problem that ML-based trigger systems address by compressing and filtering data on the fly, before it can be written to disk

![Figure 2](figure:2)

Accelerator science brings its own set of headaches. Modern accelerators are enormously complex machines with thousands of coupled parameters. **ML-based surrogate models** trained on simulation data replace expensive physics-based models during real-time optimization, enabling feedback loops fast enough to correct beam instabilities as they emerge. **Adaptive ML** handles the additional wrinkle that accelerator systems are non-stationary: components age, conditions drift, and a model trained yesterday may fail today.

## Why It Matters

The review's real contribution isn't any single technique. It's the convergence it documents. Nuclear physics covers roughly fifteen orders of magnitude in energy scale, from binding energies of a few MeV (million electron volts) to quark-gluon plasma temperatures above a trillion Kelvin. Experiments at CERN, Jefferson Lab, and RHIC (the Relativistic Heavy Ion Collider) each generate petabytes of data annually.

The theoretical models that interpret this data are among the most computationally expensive in all of science. Machine learning is not a convenience here. It is becoming infrastructure.

The impact reaches outside nuclear physics, too. Techniques born in this field, like uncertainty quantification in neural networks, equivariant architectures that respect physical symmetries, and flow-based samplers for quantum field theory, are feeding back into ML research. Nuclear physicists are becoming ML innovators, and tools built for hadron spectroscopy (classifying subatomic particles by quark content) or accelerator control are shaping how the broader community thinks about physics-informed machine learning.

Open questions remain sharp. How do we rigorously propagate uncertainties through deep neural networks used as theory emulators? Can generative models ever fully solve the sign problem, or only alleviate it? How do we ensure that ML-based event reconstruction does not introduce subtle biases that corrupt precision measurements? The authors do not shy away from these tensions, and the review is honest about both the promise and the open methodological challenges.

> **Bottom Line:** Machine learning has already reshaped nuclear physics across theory, experiment, and infrastructure. This review provides a detailed map of that transformation, revealing a field not waiting for AI but actively co-developing it.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This review, co-authored by MIT IAIFI affiliate Cristiano Fanelli, documents the two-way partnership between nuclear physics and machine learning: physics problems drive new ML methods, and ML opens regimes of nuclear science that were previously out of reach.

- **Impact on Artificial Intelligence:** Nuclear physics has been a proving ground for physics-informed generative models, uncertainty-aware Bayesian networks, and equivariant architectures that enforce fundamental symmetries, all of which now influence ML research more broadly.

- **Impact on Fundamental Interactions:** ML is opening up problems in nuclear structure, lattice QCD at finite density, and real-time detector reconstruction that were previously beyond reach, pushing toward more precise measurements of the forces governing matter.

- **Outlook and References:** The paper anticipates that ML will become standard infrastructure in nuclear science over the next decade, particularly for accelerator control and lattice field theory; see [arXiv:2112.02309](https://arxiv.org/abs/2112.02309) for the full review.
