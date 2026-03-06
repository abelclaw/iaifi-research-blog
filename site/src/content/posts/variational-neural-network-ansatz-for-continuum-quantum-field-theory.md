---
abstract: Physicists dating back to Feynman have lamented the difficulties of applying
  the variational principle to quantum field theories. In non-relativistic quantum
  field theories, the challenge is to parameterize and optimize over the infinitely
  many $n$-particle wave functions comprising the state's Fock space representation.
  Here we approach this problem by introducing neural-network quantum field states,
  a deep learning ansatz that enables application of the variational principle to
  non-relativistic quantum field theories in the continuum. Our ansatz uses the Deep
  Sets neural network architecture to simultaneously parameterize all of the $n$-particle
  wave functions comprising a quantum field state. We employ our ansatz to approximate
  ground states of various field theories, including an inhomogeneous system and a
  system with long-range interactions, thus demonstrating a powerful new tool for
  probing quantum field theories.
arxivId: '2212.00782'
arxivUrl: https://arxiv.org/abs/2212.00782
authors:
- John M. Martyn
- Khadijeh Najafi
- Di Luo
concepts:
- quantum field theory
- quantum states
- neural-network quantum field states
- monte carlo methods
- symmetry preservation
- tensor networks
- equivariant neural networks
- quantum simulation
- fock space variational ansatz
- entanglement
- physics-informed neural networks
- renormalization
figures:
- /iaifi-research-blog/figures/2212_00782/figure_1.png
- /iaifi-research-blog/figures/2212_00782/figure_2.png
- /iaifi-research-blog/figures/2212_00782/figure_3.png
pdfUrl: https://arxiv.org/pdf/2212.00782v4
published: '2022-12-01T18:58:40+00:00'
theme: Experimental Physics
title: Variational Neural-Network Ansatz for Continuum Quantum Field Theory
wordCount: 1024
---

## The Big Picture

Imagine trying to describe a river — not just a snapshot, but every possible arrangement of water molecules at every depth, every eddy, every turbulent swirl, all at once. Now imagine the river can spontaneously create or destroy molecules, and every possible count must be accounted for simultaneously. That is, roughly, the challenge facing physicists who try to apply the variational principle to quantum field theories.

The variational principle is one of physics' most elegant tools: guess the shape of a quantum state, adjust it until the energy is minimized, and you've found the **ground state** — the lowest-energy configuration a system can settle into. It works beautifully for atoms and molecules.

But **quantum field theories** — the mathematical framework describing everything from superconductors to the strong nuclear force — govern systems where particle number itself fluctuates. Every configuration with zero, one, two, or more particles must be captured at once. Richard Feynman identified this as a fundamental barrier. The problem isn't the physics; it's that no one had a good way to write down a variational guess that was both flexible enough and computationally tractable.

Researchers at MIT and IBM Quantum have found that deep learning offers a surprisingly natural solution. Their framework, **neural-network quantum field states** (NQFS), uses a specific neural network architecture to simultaneously represent wave functions for every possible particle number — then optimizes the whole thing to find ground states of these theories.

> **Key Insight:** By exploiting the Deep Sets neural network architecture, NQFS can represent a quantum field state spanning all possible particle numbers using a *finite* set of neural network parameters — turning an infinitely complex problem into a tractable optimization.

## How It Works

The mathematical heart of quantum field theory is **Fock space** — a unified structure combining separate spaces for zero particles, one particle, two particles, and so on. A quantum field state is a superposition of wave functions across all these sectors simultaneously. To apply the variational principle, you need an **ansatz**: a parameterized family of states you can tune. The catch is that a general ansatz must handle wave functions for *any* particle number using a *shared* set of parameters.

![Figure 1](/iaifi-research-blog/figures/2212_00782/figure_1.png)

The **Deep Sets** architecture, originally developed for machine learning on unordered sets, turns out to be exactly right for this job. It computes a **permutation-invariant** function — giving the same result regardless of the order particles are listed, which is essential for identical bosons — by applying a network to each element individually, summing the results, then passing that sum through another network. Crucially, it is also **variadic**: it accepts any number of inputs.

The NQFS ansatz uses two Deep Sets networks in tandem: one operating on particle positions, the other on pairwise separations. Their product gives the wave function for any particle number. The full state is:

- A sum over all particle sectors (0, 1, 2, ...)
- Each sector described by integrating the n-particle wave function over all possible positions
- All wave functions parameterized by the same shared neural networks

Optimization uses **variational Monte Carlo (VMC)** — a technique that estimates quantum mechanical quantities by randomly sampling particle configurations rather than computing them exactly — adapted here to work directly in Fock space. Particle configurations, including particle number itself, are sampled from the continuous state. Energy estimates drive gradient updates. No grid; no discretization; entirely in the continuum.

The team validated NQFS on three test cases of increasing complexity:

1. **Lieb-Liniger model** — bosons with contact interactions in 1D. This model is exactly solvable, so results could be checked directly against the known answer. NQFS matched ground state energies to within fractions of a percent across interaction strengths, including the strongly-interacting regime where perturbation theory fails.

2. **Calogero-Sutherland model** — bosons with long-range inverse-square interactions. Previous continuous matrix product state (cMPS) methods required special approximations here. NQFS handles long-range forces naturally, without modification.

3. **Regularized Klein-Gordon model** — an inhomogeneous system with a spatially varying mass term. cMPS is notoriously unstable for inhomogeneous systems and typically falls back on discretization. NQFS solved it directly in the continuum.

![Figure 2](/iaifi-research-blog/figures/2212_00782/figure_2.png)

Across all three cases, variational energies converged reliably to the ground state.

## Why It Matters

This paper closes a gap open for decades. Lattice field theory — discretizing spacetime onto a grid — is the workhorse for non-perturbative calculations in nuclear and particle physics, but reaching the true continuum limit requires extrapolating across many lattice spacings, which is computationally brutal. Continuous matrix product states offered a continuum alternative but struggled with inhomogeneity and long-range interactions. NQFS sidesteps both.

![Figure 3](/iaifi-research-blog/figures/2212_00782/figure_3.png)

More broadly, this work shows that modern deep learning architectures can be matched to the mathematical structure of quantum field theories in principled ways. The Deep Sets architecture isn't a hack — permutation invariance is fundamental to quantum mechanics for identical particles, making it the right tool by design. Future extensions could target fermionic systems (requiring antisymmetric wave functions), higher spatial dimensions, and relativistic theories including quantum chromodynamics (QCD). The variational toolbox for quantum field theory just got significantly more powerful.

> **Bottom Line:** Neural-network quantum field states provide the first practical, continuum variational ansatz that handles variable particle number, long-range interactions, and inhomogeneous systems — a long-sought capability that opens new computational routes into strongly-interacting quantum field theories.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges deep learning and quantum field theory by recognizing that Fock space — the natural language of QFT — maps directly onto the Deep Sets architecture, enabling each field to inform the other.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">NQFS demonstrates that permutation-invariant, variadic neural networks can parameterize infinite-dimensional mathematical objects, expanding the scope of neural network quantum states beyond fixed-particle systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling variational calculations directly in the continuum, NQFS opens a new computational pathway to ground states of strongly-interacting field theories, including systems with long-range interactions where prior methods required approximations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extensions to fermions, higher dimensions, and relativistic theories such as QCD; the full paper is available at arXiv:2212.00782.</span></div></div>
</div>
