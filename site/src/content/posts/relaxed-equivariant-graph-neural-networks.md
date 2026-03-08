---
abstract: 3D Euclidean symmetry equivariant neural networks have demonstrated notable
  success in modeling complex physical systems. We introduce a framework for relaxed
  $E(3)$ graph equivariant neural networks that can learn and represent symmetry breaking
  within continuous groups. Building on the existing e3nn framework, we propose the
  use of relaxed weights to allow for controlled symmetry breaking. We show empirically
  that these relaxed weights learn the correct amount of symmetry breaking.
arxivId: '2407.20471'
arxivUrl: https://arxiv.org/abs/2407.20471
authors:
- Elyssa Hofgard
- Rui Wang
- Robin Walters
- Tess Smidt
concepts:
- equivariant neural networks
- relaxed equivariance
- group theory
- symmetry breaking
- relaxed weights
- geometric deep learning
- graph neural networks
- symmetry preservation
- phase transitions
- representation learning
- molecular dynamics
figures:
- /iaifi-research-blog/figures/2407_20471/figure_1.png
- /iaifi-research-blog/figures/2407_20471/figure_2.png
- /iaifi-research-blog/figures/2407_20471/figure_3.png
pdfUrl: https://arxiv.org/pdf/2407.20471v2
published: '2024-07-30T00:16:50+00:00'
theme: Foundational AI
title: Relaxed Equivariant Graph Neural Networks
wordCount: 993
---

## The Big Picture

Imagine teaching a child to recognize a coffee mug. You'd want them to know it's the same mug whether it's right-side up or tilted. That consistency makes learning easier. Now imagine the mug is melting. The symmetry breaks, and a neural network that *only* knows about perfect mugs will struggle with the melting one.

This is the challenge at the heart of modern physics-informed machine learning. Researchers have spent years building neural networks that respect the fundamental symmetries of nature: rotational symmetry, mirror symmetry, translational symmetry. These **symmetry-aware neural networks** have proven very powerful for modeling molecules, crystals, and quantum systems.

But nature isn't always symmetric. Crystals undergo phase transitions, sudden structural changes like water turning to ice, where the regular symmetry of the material breaks down. Fluids respond to temperature gradients. Biological molecules feel the asymmetric tug of their environment. When symmetry breaks, the most powerful physics-AI tools can become the least flexible.

A team from MIT and Northeastern University, led by Elyssa Hofgard, has built a framework that lets these networks *learn* how much symmetry to break, and when, directly from data.

> **Key Insight:** Instead of forcing a neural network to be fully symmetric or fully asymmetric, these adaptive networks learn the degree of symmetry breaking that the data actually requires, adapting to the physical reality of the system being modeled.

## How It Works

The starting point is the **E(3) group**, the mathematical structure encoding all symmetries of 3D Euclidean space: translations, rotations, and reflections. Standard equivariant neural networks are built so that rotating your input molecule produces a rotated (but otherwise identical) output, making them robust and data-efficient.

The **e3nn framework**, an open-source library for building symmetry-aware neural networks, is what this work extends. It achieves equivariance through a two-part recipe:

1. **Spherical harmonics** project geometric relationships between atoms onto basis functions that capture directional information in a form that transforms predictably under rotation. Think of it as a mathematical language for encoding "which way things point."
2. **Tensor product decompositions** combine inputs and filters using **Clebsch-Gordan coefficients**, numbers that encode the precise rules for how geometric quantities (scalars, vectors, and their higher-dimensional relatives) combine while obeying the group's symmetry rules.

Each "path" in this tensor product can be independently weighted by a scalar, and this is where things get interesting. Normally, those scalar weights are constrained to be identical across all orientations, which guarantees equivariance. Hofgard and colleagues introduce **relaxed weights**: weights that are *mostly* equivariant but carry a small learnable perturbation that can break symmetry in a controlled, data-driven way.

![Figure 1](figure:1)

The relaxed weight for each tensor product path takes the standard equivariant weight and adds a symmetry-breaking correction. The network learns the magnitude of this correction from training data. If the physics truly respects E(3) symmetry, the correction learns to be zero. If the system has broken symmetry (say, a crystal undergoing a phase transition) the correction grows to capture that asymmetry.

![Figure 2](figure:2)

This connects to **Landau theory**, the classical physics framework for describing phase transitions. In Landau theory, an "order parameter" tracks how much symmetry a system has broken: zero in the disordered phase, nonzero below the transition temperature. The relaxed weights function as learned order parameters, measures of symmetry breaking that emerge automatically from training rather than being specified by hand.

![Figure 3](figure:3)

Empirically, these relaxed weights converge to the correct amount of symmetry breaking for systems with known, controllable asymmetry. The network neither over-breaks symmetry nor under-breaks it. It finds the physics.

## Why It Matters

Many of the most scientifically important systems live in regimes where symmetry is approximate rather than exact. Superconductors lose all electrical resistance near a critical temperature. Proteins fold in asymmetric cellular environments. Fluids driven by external fields break the symmetry of undisturbed flow.

Prior equivariant networks forced a binary choice: impose full symmetry and accept model errors, or abandon equivariance entirely and lose the efficiency and generalization that made these networks valuable. Relaxed equivariant networks dissolve that false choice.

A model trained on crystal structures can now handle both the symmetric high-temperature phase and the symmetry-broken low-temperature phase within a single architecture. For fluid dynamics, a network can encode the baseline Euclidean symmetry of an undisturbed fluid while learning the asymmetry introduced by a temperature gradient. Materials science, climate modeling, biophysics: wherever the interesting physics happens at the boundary between order and disorder, this applies.

Symmetry constraints are one of the best tools for building models that generalize well from limited data. This work gives a mathematically grounded way to handle *approximate* symmetry, which in practice is far more common than perfect symmetry.

> **Bottom Line:** Relaxed equivariant graph neural networks give physicists and AI researchers a principled tool for modeling symmetry breaking in continuous 3D space, learning the right amount of asymmetry from data without sacrificing the geometric structure that makes equivariant networks powerful.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects abstract group representation theory with practical neural network architecture design, producing a framework fluent in both Clebsch-Gordan coefficients and PyTorch tensor operations.

- **Impact on Artificial Intelligence:** Relaxed equivariant networks extend learnable symmetry structures in geometric deep learning from discrete groups to the continuous E(3) group, enabling richer inductive biases for real-world physical data.

- **Impact on Fundamental Interactions:** By connecting learned symmetry-breaking weights to Landau order parameters, the framework offers a data-driven route to characterizing phase transitions and spontaneous symmetry breaking in condensed matter systems.

- **Outlook and References:** Future directions include applying relaxed equivariance to molecular dynamics simulations under external fields and crystallographic phase transition modeling. The work appeared at the Geometry-grounded Representation Learning workshop at ICML 2024.

## Original Paper Details
- **Title:** Relaxed Equivariant Graph Neural Networks
- **arXiv ID:** [arXiv:2407.20471](https://arxiv.org/abs/2407.20471)
- **Authors:** Elyssa Hofgard, Rui Wang, Robin Walters, Tess Smidt
- **Abstract:** 3D Euclidean symmetry equivariant neural networks have demonstrated notable success in modeling complex physical systems. We introduce a framework for relaxed E(3) graph equivariant neural networks that can learn and represent symmetry breaking within continuous groups. Building on the existing e3nn framework, we propose the use of relaxed weights to allow for controlled symmetry breaking. We show empirically that these relaxed weights learn the correct amount of symmetry breaking.
