---
abstract: Algorithms based on normalizing flows are emerging as promising machine
  learning approaches to sampling complicated probability distributions in a way that
  can be made asymptotically exact. In the context of lattice field theory, proof-of-principle
  studies have demonstrated the effectiveness of this approach for scalar theories,
  gauge theories, and statistical systems. This work develops approaches that enable
  flow-based sampling of theories with dynamical fermions, which is necessary for
  the technique to be applied to lattice field theory studies of the Standard Model
  of particle physics and many condensed matter systems. As a practical demonstration,
  these methods are applied to the sampling of field configurations for a two-dimensional
  theory of massless staggered fermions coupled to a scalar field via a Yukawa interaction.
arxivId: '2106.05934'
arxivUrl: https://arxiv.org/abs/2106.05934
authors:
- Michael S. Albergo
- Gurtej Kanwar
- Sébastien Racanière
- Danilo J. Rezende
- Julian M. Urban
- Denis Boyda
- Kyle Cranmer
- Daniel C. Hackett
- Phiala E. Shanahan
concepts:
- normalizing flows
- pseudofermion method
- generative models
- lattice qcd
- quantum field theory
- monte carlo methods
- symmetry preservation
- density estimation
- equivariant neural networks
- staggered fermions
- phase transitions
- stochastic processes
figures:
- /iaifi-research-blog/figures/2106_05934/figure_1.png
- /iaifi-research-blog/figures/2106_05934/figure_1.png
- /iaifi-research-blog/figures/2106_05934/figure_2.png
- /iaifi-research-blog/figures/2106_05934/figure_2.png
- /iaifi-research-blog/figures/2106_05934/figure_3.png
- /iaifi-research-blog/figures/2106_05934/figure_3.png
pdfUrl: https://arxiv.org/pdf/2106.05934v2
published: '2021-06-10T17:32:47+00:00'
theme: Theoretical Physics
title: Flow-based sampling for fermionic lattice field theories
wordCount: 1197
---

## The Big Picture

Imagine mapping the interior of a vast, tangled forest by sending in a single hiker who can only take tiny steps. In the densest regions, the hiker slows to a crawl — getting stuck in pockets and backtracking endlessly. This is essentially the problem facing physicists who study the strong nuclear force using **lattice field theory**, which simulates quantum fields on a discrete grid of points. Their computational tools grind to a halt precisely where physics gets most interesting.

The standard approach relies on **Markov Chain Monte Carlo** (MCMC) sampling: generating a sequence of snapshots of the quantum field, each slightly modified from the last, until the collection statistically represents the true physical ground state. Near phase transitions — or when zooming into finer grid resolutions — these step-by-step algorithms suffer **critical slowing down**: new snapshots become highly correlated with previous ones, requiring vastly more samples to get independent results, and cost explodes.

Enter machine learning. **Normalizing flows** — neural networks trained to transform simple random noise into samples from complicated target distributions — have emerged as a promising replacement for MCMC. The catch: every demonstration so far has been restricted to bosonic fields — particles like photons and the Higgs boson whose mathematics plays nicely with conventional tools. The other half of the particle zoo — fermions, the quarks and electrons that make up ordinary matter — have resisted this treatment. A new paper from a collaboration spanning MIT, NYU, DeepMind, and Argonne National Laboratory changes that.

> **Key Insight:** By combining normalizing flows with the pseudofermion method, this work demonstrates the first flow-based sampling framework for lattice field theories with dynamical fermions — a prerequisite for eventually applying these ML-powered methods to quantum chromodynamics and the full Standard Model.

## How It Works

The core difficulty with fermions is mathematical. Unlike bosons, fermions obey the Pauli exclusion principle, forcing their field variables to be **Grassmann numbers** — abstract objects that anti-commute rather than commute. You can't plug Grassmann numbers into a neural network; they don't exist as ordinary numbers.

The standard workaround is to integrate them out. In the **path integral** — the quantum-mechanical sum over all possible field configurations that determines physical probabilities — Grassmann variables can be handled analytically, leaving a purely bosonic expression containing a **fermion determinant**: a single complex number encoding all fermionic dynamics. Computing this determinant exactly scales as the cube of the lattice volume — simply intractable on modern QCD lattices.

![Figure 1](/iaifi-research-blog/figures/2106_05934/figure_1.png)

The team's solution is the **pseudofermion method**: auxiliary bosonic fields are introduced whose statistical properties exactly encode fermion dynamics. This transforms the problem into sampling bosonic degrees of freedom over a joint space of physical scalar fields and pseudofermion fields, with a modified action coupling them. The flow model learns to sample this joint distribution.

The paper identifies four distinct sampling schemes, each representing a different decomposition of the joint distribution:

- **Joint sampling**: a single flow models the full (boson + pseudofermion) distribution simultaneously
- **Bosonic marginal + conditional**: one flow learns the marginalized boson distribution; a second learns fermion configurations conditioned on the bosons
- **Pseudofermion refreshment**: the flow handles only the pseudofermion sector, while **Hamiltonian Monte Carlo** (HMC) — a physics-inspired sampler that uses simulated particle trajectories to propose new configurations — handles the bosons
- **Flow-accelerated HMC**: the learned model augments traditional HMC sampling

Each scheme offers different tradeoffs between expressiveness and computational cost.

![Figure 2](/iaifi-research-blog/figures/2106_05934/figure_1.png)

Building the flow architectures required careful attention to symmetry. The pseudofermion action possesses **translational symmetry** — the physics is identical whether you shift every grid point by the same amount. But there's a twist: **boundary conditions** differ between bosons and fermions. Fermion fields are **antiperiodic** — they flip sign when wrapping around the time direction — while bosons use ordinary periodic conditions.

The team constructed **equivariant coupling layers**: neural network building blocks engineered to respect these mixed boundary conditions automatically, so the model never wastes capacity on structure that symmetry already determines.

![Figure 3](/iaifi-research-blog/figures/2106_05934/figure_2.png)

The demonstration targets a two-dimensional **Yukawa model** — a theory coupling a scalar bosonic field to a fermionic field, using **staggered fermions**, a discretization scheme that efficiently represents fermionic degrees of freedom on the lattice. This is a standard testbed in lattice field theory: complex enough to contain genuine fermionic physics, simple enough to benchmark rigorously. Flow-based sampling produces statistically independent configurations with **acceptance rates** — the fraction of proposed configurations accepted as valid samples — far exceeding standard HMC, with the gap widening near more challenging parameter regimes.

![Figure 4](/iaifi-research-blog/figures/2106_05934/figure_2.png)

## Why It Matters

The Standard Model is dominated by fermions. Quantum chromodynamics — the theory of the strong force — involves quarks (fermions) bound by gluons into protons and neutrons. Computing proton properties from first principles, understanding the **quark-gluon plasma** (the hot soup of free quarks and gluons that existed microseconds after the Big Bang), or searching for new physics in precision measurements all require accurate lattice QCD calculations. Those calculations are fundamentally limited by the sampling problem this paper addresses.

![Figure 5](/iaifi-research-blog/figures/2106_05934/figure_3.png)

The reach extends beyond particle physics. **Strongly correlated electron systems** — condensed matter materials like high-temperature superconductors, where intense quantum interactions produce exotic collective behavior — share the same underlying mathematical structure as fermionic lattice field theories. Sampling improvements that work for lattice QCD translate directly to materials science.

The four sampling schemes here aren't alternatives to HMC so much as a toolkit. The pseudofermion refreshment scheme, for instance, can drop into existing HMC workflows as a direct upgrade, reducing autocorrelations without requiring a complete algorithmic overhaul.

![Figure 6](/iaifi-research-blog/figures/2106_05934/figure_3.png)

The immediate frontier is scaling. The two-dimensional Yukawa demonstration is a proof of principle; next steps are three- and four-dimensional theories, non-Abelian gauge fields (gluons), and eventually the full QCD action. Each step brings new architectural challenges — flow models must scale efficiently with lattice volume while preserving exact gauge and fermionic symmetries. But the conceptual barrier has been cleared: flow-based sampling is no longer bosons-only.

> **Bottom Line:** This work opens fermionic lattice field theory to ML-powered sampling for the first time — demonstrating on a 2D Yukawa model that normalizing flows can generate statistically independent fermionic field configurations, pointing toward a future where critical slowing down no longer throttles first-principles calculations of the strong nuclear force.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses deep learning with lattice field theory, building normalizing flow samplers that encode exact physical symmetries — including antiperiodic fermionic boundary conditions — through purpose-built equivariant coupling layers.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper advances generative modeling for structured physical distributions, developing equivariant architectures that enforce mixed bosonic/fermionic symmetries — a template for ML sampling in any system with constrained anti-commuting degrees of freedom.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling flow-based sampling of dynamical fermions, this research clears the primary obstacle to applying ML-accelerated lattice methods to QCD and the full Standard Model, where fermions are not optional.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions to four-dimensional gauge theories with non-Abelian symmetries and physical quark masses will determine whether these methods can challenge state-of-the-art HMC in production QCD calculations; see arXiv:2106.05934 for the full paper.</span></div></div>
</div>
