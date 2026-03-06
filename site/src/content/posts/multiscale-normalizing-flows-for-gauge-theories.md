---
abstract: Scale separation is an important physical principle that has previously
  enabled algorithmic advances such as multigrid solvers. Previous work on normalizing
  flows has been able to utilize scale separation in the context of scalar field theories,
  but the principle has been largely unexploited in the context of gauge theories.
  This work gives an overview of a new method for generating gauge fields using hierarchical
  normalizing flow models. This method builds gauge fields from the outside in, allowing
  different parts of the model to focus on different scales of the problem. Numerical
  results are presented for $U(1)$ and $SU(3)$ gauge theories in 2, 3, and 4 spacetime
  dimensions.
arxivId: '2404.10819'
arxivUrl: https://arxiv.org/abs/2404.10819
authors:
- Ryan Abbott
- Michael S. Albergo
- Denis Boyda
- Daniel C. Hackett
- Gurtej Kanwar
- Fernando Romero-López
- Phiala E. Shanahan
- Julian M. Urban
concepts:
- normalizing flows
- lattice gauge theory
- multiscale hierarchy
- generative models
- monte carlo methods
- equivariant neural networks
- symmetry preservation
- quantum field theory
- density estimation
- scalability
- topological freezing
- bayesian inference
figures:
- /iaifi-research-blog/figures/2404_10819/figure_1.png
- /iaifi-research-blog/figures/2404_10819/figure_2.png
- /iaifi-research-blog/figures/2404_10819/figure_3.png
pdfUrl: https://arxiv.org/pdf/2404.10819v1
published: '2024-04-16T18:00:05+00:00'
theme: Theoretical Physics
title: Multiscale Normalizing Flows for Gauge Theories
wordCount: 1181
---

## The Big Picture

Imagine trying to paint a detailed landscape by starting with every individual brushstroke simultaneously. You'd miss the forest for the trees — the sweeping valleys, ridgelines, and broad swaths of sky that give the scene its structure. Skilled painters rough in large shapes first, then add progressively finer detail. This ancient artistic wisdom also applies to one of the most computationally demanding problems in modern physics: simulating the quantum vacuum of the universe.

Particle physicists studying the strong nuclear force — the glue holding protons and neutrons together — must simulate a **gauge field**: a mathematical object encoding how particles exert forces across space and time. These simulations run on discrete grids called **lattices**, and they suffer from a notorious computational pathology. As physicists push to finer lattice spacings to capture more physical detail, the simulations slow to a crawl. The simulation gets trapped in one configuration for millions of steps, barely exploring the range of states the theory actually predicts.

Machine learning promised a cure, but an important physical principle was left on the table: the idea that physics at different length scales can be separated and handled independently. A new paper from researchers at MIT, NYU, Fermilab, and partner institutions changes that. By building gauge fields coarse-to-fine in a principled hierarchy, their **multiscale normalizing flow** framework brings scale separation to non-Abelian gauge theories — a mathematically richer class of theories governing the actual strong force — for the first time. Results span 2D toy models and four-dimensional SU(3), the specific mathematical group describing the strong force in nature.

> **Key Insight:** By building gauge field configurations hierarchically — from large-scale structure down to fine details — this approach lets different parts of the neural network focus on different physical scales, making the sampler more expressive and physically informed.

## How It Works

**Normalizing flows** are a machine-learning technique for generating samples from complicated probability distributions. The idea is elegant: train a neural network to transform a simple, easy-to-sample distribution into the complex target — in this case, the distribution telling you how likely each field configuration is, given the theory's physical rules. Once trained, you can generate thousands of independent samples almost instantly, potentially bypassing the slow random walk of traditional Monte Carlo methods.

Previous normalizing flow approaches for gauge theories treated the lattice uniformly: every site, every scale, all at once. This ignores a key physical truth. A lattice gauge theory has structure at many scales simultaneously — long-wavelength modes (the "infrared") describing large-scale correlations, and short-wavelength modes (the "ultraviolet") capturing fine local fluctuations. The physics at each scale is different, and so are the modeling challenges.

The multiscale approach solves this with a two-part construction:

1. **Start with a coarse prior.** Rather than beginning from random noise on the full fine lattice, the model first samples values on a much coarser lattice — possibly as coarse as a single site. This coarse configuration captures the large-scale, infrared structure of the field.

2. **Apply successive doubling layers.** A **doubling layer** is a learned neural network transformation that takes a coarse lattice and refines it, doubling the number of sites in one spacetime direction. It does this by splitting each link — the mathematical value living on each edge of the lattice grid — into two components, then sampling new "perpendicular" links from a learned distribution conditioned on the surrounding geometry.

![Figure 1](/iaifi-research-blog/figures/2404_10819/figure_1.png)

The key ingredient is how perpendicular links get generated. The researchers use a small normalizing flow conditioned on the local geometric environment — specifically on the **staples**, the U-shaped paths of neighboring links that close around the new link to form the smallest possible closed loop on the lattice. The model learns to fill in fine-scale structure consistent with the coarse backbone already in place, much as a painter fills in details that harmonize with the broad composition.

By stacking doubling layers — alternating between spacetime directions — the model builds the full fine lattice from scratch, scale by scale. Each layer adds a new octave of detail, and each layer's network can specialize entirely in the physics at that scale.

![Figure 2](/iaifi-research-blog/figures/2404_10819/figure_2.png)

The team tested this framework across U(1) gauge theory (the Abelian case, essentially a lattice version of electromagnetism) in 2, 3, and 4 dimensions, and SU(3) in 4 dimensions. They measured **effective sample size (ESS)** — a number between 0 and 1 quantifying how many independent samples the model actually delivers per generated configuration. An ESS near 1 means nearly every sample is independent; near 0 means the model is badly miscalibrated.

![Figure 3](/iaifi-research-blog/figures/2404_10819/figure_3.png)

Multiscale models showed competitive or improved ESS compared to flat normalizing flow baselines, with hierarchical structure enabling more stable training and better expressiveness across varying **coupling strengths** — the parameter controlling how strongly particles interact.

## Why It Matters

The ultimate goal of lattice QCD — simulating the strong force from first principles — demands both fine lattices (to approach the continuum limit) and large lattices (to capture long-range physics). Traditional Monte Carlo simulations suffer from **critical slowing down** and **topological freezing** as lattice spacing decreases: the simulation gets stuck, and computational cost explodes. Normalizing flows offer a route around this bottleneck, but only if they can scale to physically relevant volumes with high sample quality.

Multiscale architectures are a key piece of this puzzle. Just as **multigrid solvers** — algorithms that accelerate differential equation solving by operating on coarse and fine representations simultaneously — transformed numerical linear algebra, multiscale flows could transform lattice QCD sampling. The physical insight is identical: don't fight the scale structure of the problem, use it.

These results establish that the principle works in the non-Abelian setting where the gauge group is non-commutative — the hard case that matters for the real strong force. Open questions remain around scaling to larger lattices, incorporating fermions, and optimizing per-scale flow architectures, but the foundation is now laid.

> **Bottom Line:** Multiscale normalizing flows bring a proven physical principle — scale separation — to machine-learning-based sampling of gauge theories, enabling more expressive, physically informed models that work for both Abelian and non-Abelian gauge groups in up to four spacetime dimensions.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work translates a classical physics principle — scale separation, as used in multigrid algorithms — directly into a machine learning architecture for quantum field theory, creating a feedback loop where physical insight improves AI and AI enables new physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The hierarchical normalizing flow construction — building samples coarse-to-fine via learned doubling layers — is a general technique applicable beyond physics, advancing structured generative modeling for high-dimensional, geometrically constrained distributions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By demonstrating multiscale sampling for SU(3) gauge theory in four dimensions, this work expands the toolkit for lattice QCD calculations underpinning our understanding of the strong nuclear force and hadron structure.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will focus on scaling to larger lattices and integrating fermions to approach realistic QCD simulations; the full method and results appear in the proceedings of Lattice 2023 (arXiv:2401.08044).</span></div></div>
</div>
