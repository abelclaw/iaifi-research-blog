---
abstract: This work presents gauge-equivariant architectures for flow-based sampling
  in fermionic lattice field theories using pseudofermions as stochastic estimators
  for the fermionic determinant. This is the default approach in state-of-the-art
  lattice field theory calculations, making this development critical to the practical
  application of flow models to theories such as QCD. Methods by which flow-based
  sampling approaches can be improved via standard techniques such as even/odd preconditioning
  and the Hasenbusch factorization are also outlined. Numerical demonstrations in
  two-dimensional U(1) and SU(3) gauge theories with $N_f=2$ flavors of fermions are
  provided.
arxivId: '2207.08945'
arxivUrl: https://arxiv.org/abs/2207.08945
authors:
- Ryan Abbott
- Michael S. Albergo
- Denis Boyda
- Kyle Cranmer
- Daniel C. Hackett
- Gurtej Kanwar
- Sébastien Racanière
- Danilo J. Rezende
- Fernando Romero-López
- Phiala E. Shanahan
- Betsy Tian
- Julian M. Urban
concepts:
- normalizing flows
- lattice gauge theory
- equivariant neural networks
- pseudofermion sampling
- lattice qcd
- symmetry preservation
- generative models
- parallel transporter convolution
- monte carlo methods
- density estimation
- group theory
- convolutional networks
- stochastic processes
- hasenbusch factorization
figures:
- /iaifi-research-blog/figures/2207_08945/figure_1.png
- /iaifi-research-blog/figures/2207_08945/figure_1.png
- /iaifi-research-blog/figures/2207_08945/figure_2.png
- /iaifi-research-blog/figures/2207_08945/figure_2.png
- /iaifi-research-blog/figures/2207_08945/figure_3.png
- /iaifi-research-blog/figures/2207_08945/figure_3.png
pdfUrl: https://arxiv.org/pdf/2207.08945v3
published: '2022-07-18T21:13:34+00:00'
theme: Theoretical Physics
title: Gauge-equivariant flow models for sampling in lattice field theories with pseudofermions
wordCount: 1013
---

## The Big Picture

Imagine trying to understand matter at its most fundamental level: quarks and gluons, the building blocks of protons and neutrons. Physicists break spacetime into a microscopic grid called a **lattice** and run enormous numbers of randomized numerical experiments, essentially rolling weighted dice at each grid point to explore all possible quantum states. The catch is that these simulations are extraordinarily expensive. For **Quantum Chromodynamics (QCD)**, the theory governing the strong nuclear force, generating a single dataset can demand months of supercomputer time.

Machine learning has offered a promising shortcut. **Flow-based generative models**, neural networks that transform simple random noise into physically realistic field configurations, could dramatically accelerate this step. But QCD isn't just a theory of force-carrying fields. It includes fermions (the quarks themselves), and handling fermions in flow models has proven stubbornly difficult.

The obstacle is the **fermion determinant**, a single enormous number encoding all fermionic quantum contributions for a given field snapshot. Computing it exactly costs as much as the *cube* of the lattice volume. Scale up the simulation, and the cost explodes.

A new paper from a collaboration spanning MIT, NYU, Argonne, DeepMind, and several European institutions tackles this head-on: gauge-equivariant flow architectures that handle fermions the same way lattice QCD already does, through a trick called **pseudofermions**.

> By replacing the intractable fermion determinant with pseudofermion stochastic estimators, and building flow models that respect QCD's gauge symmetry, this work brings ML-accelerated sampling to the doorstep of realistic QCD simulations.

## How It Works

The core challenge is symmetry. QCD's **gauge symmetry**, the mathematical redundancy that keeps the theory consistent, means any sampling method must treat physically equivalent field configurations as genuinely equivalent. Earlier flow models achieved this for gauge fields (the force carriers) by constructing gauge-equivariant architectures: neural networks whose outputs transform in lockstep with their inputs under gauge transformations. Fermions add another layer of difficulty.

The standard solution in lattice QCD is elegant. Instead of tracking fermionic degrees of freedom directly (fields with mathematically awkward properties that resist numerical simulation), you integrate them out analytically, leaving the fermion determinant. Rather than computing it exactly, physicists introduce **pseudofermions**: auxiliary bosonic fields $\phi$ whose statistical average reproduces the determinant at a fraction of the cost. Think of them as stand-ins, complex scalar fields doing the fermion's job cheaply.

![Figure 1](figure:1)

The new flow architecture is built around a joint model that splits sampling into two stages:

1. **Marginal sampling**: A flow model samples gauge field configurations $U$, trained on the pure-gauge part of the action.
2. **Conditional sampling**: Given a fixed gauge configuration, a second flow model samples pseudofermion fields $\phi$ that correctly estimate the fermion determinant.

The conditional piece required new architectural machinery. The authors introduce a **parallel transporter convolutional network**, a layer that convolves field data across the lattice while transporting it along gauge links, preserving gauge equivariance at every step. This is the architectural heart of the paper. It lets the flow model "see" local gauge geometry when placing pseudofermion fields.

![Figure 2](figure:2)

The paper also incorporates two proven tricks from conventional lattice QCD. **Even/odd preconditioning** reorganizes the lattice into checkerboard sublattices, reducing the effective matrix size the model must invert. **Hasenbusch factorization** splits the fermion determinant into a product of individually easier terms, a divide-and-conquer strategy the flow model exploits directly.

![Figure 3](figure:3)

To validate the approach, the authors tested on two 2D theories: the **Schwinger model** (a U(1) gauge theory with fermions, analogous to 2D QED) and a 2D SU(3) gauge theory with two fermion flavors, sharing QCD's gauge group without its full complexity. Both are tractable enough to compare against exact results while complex enough to stress-test the architecture. The flow models reproduced correct distributions of physical observables, with accuracy improving as the number of pseudofermion samples per gauge configuration increased.

![Figure 4](figure:4)

## Why It Matters

The path to simulating QCD at physically relevant parameters (heavy quark masses, large volumes, fine lattice spacings) runs directly through fermionic sampling. Every modern lattice QCD calculation already uses pseudofermions. By building flow models that speak the same language, this work plugs into existing computational infrastructure rather than demanding a wholesale reinvention.

The deeper payoff is algorithmic. Conventional lattice QCD sampling via Hybrid Monte Carlo (HMC) generates new field configurations through small physically-guided steps, accepting or rejecting each probabilistically. Near phase transitions, successive samples become highly correlated. This is called **critical slowing-down**, and it means exponentially more computation to obtain independent configurations.

Flow-based models generate independent samples by construction. Combined with the pseudofermion approach developed here, they could eventually sidestep this bottleneck for theories with dynamical fermions, the regime where critical slowing-down has historically been most severe. Scaling to four-dimensional QCD, handling lighter quark masses, and improving joint-model training efficiency are all substantial open problems. But the architectural foundation is now in place.

> This paper delivers the toolkit needed to apply flow-based machine learning to realistic fermionic gauge theories, matching the pseudofermion framework lattice QCD has relied on for decades and opening a credible path toward ML-accelerated simulations of the strong nuclear force.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work fuses deep learning architecture design with the mathematical structure of quantum field theory, constructing neural network layers that are provably consistent with gauge symmetry. It is an advance that neither pure ML nor pure physics could have produced alone.

- **Impact on Artificial Intelligence:** The parallel transporter convolutional network introduces a new class of geometrically structured neural network layers that respect non-Abelian gauge symmetry, pushing equivariant deep learning into territory relevant to fundamental physics.

- **Impact on Fundamental Interactions:** By enabling flow-based sampling with pseudofermions in both U(1) and SU(3) gauge theories, the work provides a scalable route to applying ML-accelerated Monte Carlo methods to QCD.

- **Outlook and References:** Future work targets scaling these architectures to four-dimensional QCD and lighter quark masses. The paper is available at [arXiv:2207.08945](https://arxiv.org/abs/2207.08945).

## Original Paper Details
- **Title:** Gauge-equivariant flow models for sampling in lattice field theories with pseudofermions
- **arXiv ID:** [2207.08945](https://arxiv.org/abs/2207.08945)
- **Authors:** Ryan Abbott, Michael S. Albergo, Denis Boyda, Kyle Cranmer, Daniel C. Hackett, Gurtej Kanwar, Sébastien Racanière, Danilo J. Rezende, Fernando Romero-López, Phiala E. Shanahan, Betsy Tian, Julian M. Urban
- **Abstract:** This work presents gauge-equivariant architectures for flow-based sampling in fermionic lattice field theories using pseudofermions as stochastic estimators for the fermionic determinant. This is the default approach in state-of-the-art lattice field theory calculations, making this development critical to the practical application of flow models to theories such as QCD. Methods by which flow-based sampling approaches can be improved via standard techniques such as even/odd preconditioning and the Hasenbusch factorization are also outlined. Numerical demonstrations in two-dimensional U(1) and SU(3) gauge theories with $N_f=2$ flavors of fermions are provided.
