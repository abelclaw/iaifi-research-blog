---
abstract: We use the embedding formalism to construct conformal fields in $D$ dimensions,
  by restricting Lorentz-invariant ensembles of homogeneous neural networks in $(D+2)$
  dimensions to the projective null cone. Conformal correlators may be computed using
  the parameter space description of the neural network. Exact four-point correlators
  are computed in a number of examples, and we perform a 4D conformal block decomposition
  that elucidates the spectrum. In some examples the analysis is facilitated by recent
  approaches to Feynman integrals. Generalized free CFTs are constructed using the
  infinite-width Gaussian process limit of the neural network, enabling a realization
  of the free boson. The extension to deep networks constructs conformal fields at
  each subsequent layer, with recursion relations relating their conformal dimensions
  and four-point functions. Numerical approaches are discussed.
arxivId: '2409.12222'
arxivUrl: https://arxiv.org/abs/2409.12222
authors:
- James Halverson
- Joydeep Naskar
- Jiahua Tian
concepts:
- conformal field theory
- neural network field theory
- quantum field theory
- symmetry preservation
- conformal block decomposition
- group theory
- stochastic processes
- scattering amplitudes
- deep network recursion
- renormalization
- monte carlo methods
- phase transitions
figures: []
pdfUrl: https://arxiv.org/pdf/2409.12222v2
published: '2024-09-18T18:00:00+00:00'
theme: Theoretical Physics
title: Conformal Fields from Neural Networks
wordCount: 1191
---

## The Big Picture

Imagine designing a building that looks identical from every angle, not just rotated but stretched, squeezed, and viewed from any distance. That's the challenge facing physicists who study **conformal field theories** (CFTs): mathematical frameworks invariant under rotation, translation, and rescaling. These theories appear everywhere from the physics of boiling water to the deep structure of string theory, yet constructing new ones from scratch has always been brutally hard.

A team at Northeastern University and East China Normal University has found an unexpected shortcut: build conformal fields out of neural networks. Not train a network to *approximate* a CFT, but actually use the architecture and parameter statistics of a neural network as the literal definition of a new quantum field theory. The mathematics fit together cleanly.

Halverson, Naskar, and Tian show that by choosing a neural network built from homogeneous functions and restricting it to a carefully chosen surface in higher-dimensional space, you automatically get a conformally symmetric field theory. The result opens a new factory for exactly solvable CFTs, complete with computable predictions for field interactions and particle-like states.

> Neural networks, viewed as parameter-dependent functions rather than learning machines, can serve as direct constructions of conformal field theories. Integration over parameters plays the role of the path integral.

## How It Works

The construction rests on a geometric trick called the **embedding formalism**, originally due to Dirac. Conformal symmetry in *D* dimensions is secretly equivalent to rotational symmetry in *D+2* dimensions. So instead of working in physical spacetime, you lift everything to a higher-dimensional space, then project back down onto the **projective null cone**: the set of lightlike directions in that larger space.

Neural networks enter here. The researchers define a network Φ(X) on the full (D+2)-dimensional space with one crucial constraint: the network must be homogeneous, meaning scaling the input by λ scales the output by λ^Δ for a fixed exponent Δ. Homogeneous activation functions like monomials x^n make this straightforward to build.

Restricting the network to the projective null cone produces a field that automatically obeys all transformation laws of a conformal field in D dimensions. Δ becomes the **conformal dimension**, the number encoding how the field responds to rescaling.

The workflow has four steps:

1. **Choose an architecture** — a neural network with homogeneous activations, specific depth and width
2. **Choose a parameter distribution** P(Θ) — the analog of choosing an action in conventional field theory
3. **Restrict to the null cone** — project the network from D+2 down to D dimensions
4. **Compute correlators** — integrate over network weights instead of field configurations

That last step is the computational payoff. For shallow networks with simple parameter distributions, the integrals are tractable, sometimes exactly. The paper computes exact four-point correlation functions in multiple examples: measurements of how four points simultaneously influence each other, where most of the rich physics (operator spectra, OPE coefficients, conformal block data) lives.

A particularly clean result comes from the **infinite-width Gaussian process limit**. When a network is made infinitely wide with Gaussian-distributed weights, its outputs become a Gaussian process, which is effectively a free field theory. The researchers use this to construct generalized free CFTs, including an explicit realization of the free boson reproduced from first principles.

Deep networks add structure layer by layer. Each layer produces its own conformal field, and the authors derive recursion relations linking conformal dimensions and four-point functions of successive layers. Going deeper corresponds to RG-flow-like transformations, a connection to the **renormalization group** that looks worth pursuing seriously.

The paper also borrows tools from particle physics. Techniques developed for Feynman integrals apply directly to the parameter-space integrals here, and the exchange goes both ways: collider physics tools help construct conformal theories, while the neural network picture may offer new intuition for amplitude calculations.

## Why It Matters

CFTs occupy a foundational role in theoretical physics. The renormalization group, which explains why vastly different physical systems share the same critical behavior, can be understood as flows between CFT fixed points. The **conformal bootstrap** uses consistency conditions to constrain and solve CFTs without writing down an explicit Lagrangian. It is one of the most productive programs in modern theoretical physics. The neural network construction offers something different: explicit, computable realizations where spectra and correlators can be extracted directly.

The two approaches are complementary. Where bootstrap methods derive powerful bounds from symmetry and unitarity, the neural network construction builds specific examples from the ground up. A natural next step is combining them, using bootstrap constraints to filter which neural network architectures yield physically sensible theories.

The paper leaves **reflection positivity** (the Euclidean analog of unitarity, ensuring probabilities stay positive) as an open problem. Solving it could enable systematic classification of CFTs accessible via this construction. On the numerical side, Monte Carlo sampling over parameter space provides an approximation strategy for architectures where exact integrals are out of reach, effectively treating neural network inference as a simulation tool for quantum field theory.

> By treating neural network architectures as homogeneous functions on a higher-dimensional null cone, this work turns machine learning machinery into a construction kit for conformal field theories. It yields exact four-point functions, free field limits, and recursive deep-network extensions that open a new path into quantum field theory.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects the theory of neural networks as statistical function ensembles with the mathematical physics of conformal field theories. The embedding formalism provides the geometric link between the two disciplines, producing a single framework that spans fields which rarely talked to each other.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper reframes neural networks not as learning machines but as parameter families of functions. Their statistical properties (Gaussian process limits, depth-dependent recursions) directly encode quantum field-theoretic data like conformal dimensions and operator spectra.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The construction provides an explicit, computable method for generating new conformal field theories, including exact four-point functions and conformal block decompositions. It offers fresh examples for the conformal bootstrap program and new connections to scattering amplitude techniques.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will focus on imposing unitarity constraints within the neural network framework and connecting deep-network recursion relations to renormalization group flows; the full paper is available at [arXiv:2409.12222](https://arxiv.org/abs/2409.12222).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Conformal Fields from Neural Networks</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2409.12222</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["James Halverson", "Joydeep Naskar", "Jiahua Tian"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We use the embedding formalism to construct conformal fields in $D$ dimensions, by restricting Lorentz-invariant ensembles of homogeneous neural networks in $(D+2)$ dimensions to the projective null cone. Conformal correlators may be computed using the parameter space description of the neural network. Exact four-point correlators are computed in a number of examples, and we perform a 4D conformal block decomposition that elucidates the spectrum. In some examples the analysis is facilitated by recent approaches to Feynman integrals. Generalized free CFTs are constructed using the infinite-width Gaussian process limit of the neural network, enabling a realization of the free boson. The extension to deep networks constructs conformal fields at each subsequent layer, with recursion relations relating their conformal dimensions and four-point functions. Numerical approaches are discussed.</span></div></div>
</div>
