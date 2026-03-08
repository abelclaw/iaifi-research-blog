---
abstract: We numerically study the phase structure of the two-flavor Schwinger model
  with matrix product states, focusing on the (1+1)-dimensional analog of the CP-violating
  Dashen phase in QCD. We simulate the two-flavor Schwinger model around the point
  where the positive mass of one fermion flavor corresponds to the negative mass of
  the other fermion flavor, which is a sign-problem afflicted regime for conventional
  Monte Carlo techniques. Our results indicate that the model undergoes a CP-violating
  Dashen phase transition at this point, which manifests itself in abrupt changes
  of the average electric field and the analog of the pion condensate in the model.
  Studying the scaling of the bipartite entanglement entropy as a function of the
  volume, we find clear indications that this transition is not of first order.
arxivId: '2303.03799'
arxivUrl: https://arxiv.org/abs/2303.03799
authors:
- Lena Funcke
- Karl Jansen
- Stefan Kühn
concepts:
- phase transitions
- tensor networks
- matrix product states
- lattice gauge theory
- cp violation
- symmetry breaking
- quantum field theory
- entanglement
- sign problem
- quantum simulation
- hamiltonian systems
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2303_03799/figure_1.png
- /iaifi-research-blog/figures/2303_03799/figure_1.png
- /iaifi-research-blog/figures/2303_03799/figure_2.png
- /iaifi-research-blog/figures/2303_03799/figure_2.png
- /iaifi-research-blog/figures/2303_03799/figure_3.png
- /iaifi-research-blog/figures/2303_03799/figure_3.png
pdfUrl: https://arxiv.org/pdf/2303.03799v2
published: '2023-03-07T11:07:51+00:00'
theme: Theoretical Physics
title: Exploring the CP-violating Dashen phase in the Schwinger model with tensor
  networks
wordCount: 1025
---

## The Big Picture

Imagine trying to photograph a ghost. Standard cameras are useless because the ghost simply doesn't interact with film. But what if you had a detector that could capture its shadow by measuring how it warps the surrounding space? That's the challenge physicists face when studying certain regimes of quantum field theory with conventional computing.

At the heart of particle physics lies a deep puzzle: why does the universe contain more matter than antimatter? One theoretical window into this mystery is **CP symmetry violation**, the subtle breaking of symmetry between matter and antimatter. In QCD (the theory of quarks and gluons), a prediction by Roger Dashen described a dramatic **phase transition**, analogous to water suddenly freezing, where this matter-antimatter symmetry spontaneously shatters.

The catch? This happens precisely where standard computational tools break down. Monte Carlo simulations work by randomly sampling millions of possible quantum states, but the mathematical weights needed for sampling become negative or complex numbers. This is the **sign problem**, and it causes the entire probabilistic approach to collapse.

A team from MIT, the University of Bonn, and DESY Zeuthen found a way around it. Using **tensor network** methods, a framework that represents quantum states as interconnected webs of data rather than random samples, they directly simulated the CP-violating Dashen phase transition in a lower-dimensional analog of QCD. This is territory that was previously off-limits to computation.

> **Key Insight:** Tensor networks bypass the sign problem by working directly with quantum wavefunctions rather than probabilistic ensembles, making it possible to simulate CP-violating physics that conventional Monte Carlo methods cannot access.

## How It Works

The researchers work with the **two-flavor Schwinger model**: quantum electrodynamics in one spatial dimension plus time, with two types of fermions acting as analogs of up and down quarks. This model is a physicist's favorite sandbox. It's tractable yet rich enough to capture QCD-like phenomena including **confinement** (quarks unable to escape each other), **chiral symmetry breaking** (a shift in how mass is generated), and a Dashen-like phase transition.

The critical parameter is the **topological theta-term**, which controls the degree of matter-antimatter asymmetry. At θ = π, one fermion flavor has positive mass and the other negative. The mass of the neutral pion, the lightest quark-antiquark bound state, is proportional to the sum of these masses. When that sum goes negative, the pion mass becomes imaginary, signaling condensation: the pion acquires a nonzero average value throughout space and breaks CP symmetry. Think of a pencil balanced on its tip. Past the critical point, it tips over into a broken-symmetry state.

![Figure 1](figure:1)

To study this transition, the team used **matrix product states (MPS)**, a tensor network that represents quantum states as chains of interconnected tensors (multidimensional data arrays linked in sequence). Unlike Monte Carlo sampling, MPS directly encode the quantum wavefunction. The sign problem never arises because there is no sampling step.

Their numerical workflow:
- **Discretizing the Hamiltonian** onto a lattice using Kogut-Susskind staggered fermions, a technique for encoding fermion physics onto a discrete grid while preserving key symmetries
- **Solving the Gauss law constraint** analytically, eliminating the gauge field variables and leaving only fermionic degrees of freedom
- **Running DMRG** (density matrix renormalization group), the standard algorithm for optimizing MPS, to find the ground state across parameter space
- **Measuring observables**: average electric field, the pion condensate, and bipartite entanglement entropy, a measure of quantum correlations across a cut through the system

![Figure 2](figure:2)

As the fermion mass ratio crosses the critical point, both the electric field and the pion condensate show abrupt jumps. That's the hallmark of a phase transition, and it lands precisely where Dashen's prediction locates it.

## Why It Matters

Finding the transition is one thing; determining its *type* is another, and far more consequential. Earlier theoretical arguments suggested the Dashen transition should be **first-order**: a sudden, discontinuous jump in thermodynamic variables, like water freezing into ice. The order of the transition carries real implications for QCD and beyond-the-Standard-Model physics.

The team probed this by studying how bipartite entanglement entropy scales with system size. In a first-order transition, entanglement entropy grows proportionally to system volume. In a second-order (continuous) transition, it grows logarithmically, with a coefficient tied to the central charge of the underlying conformal field theory. The data shows clear logarithmic scaling, inconsistent with a first-order transition. This is strong evidence that the Dashen phase transition is continuous.

![Figure 4](figure:4)

The implications reach beyond the Schwinger model. The Dashen transition appears in several beyond-the-Standard-Model scenarios, and its order shapes how CP violation might manifest in early-universe phase transitions. The fact that tensor networks can access this sign-problem-afflicted regime also opens a path toward studying analogous physics in higher-dimensional theories, including full QCD with a topological theta-term. Future quantum computers may eventually make such simulations routine; for now, tensor networks are showing what classical computation can still pull off.

> **Bottom Line:** Using matrix product states to sidestep the sign problem, this work delivers the first direct numerical evidence of the CP-violating Dashen phase transition in a QCD-like theory and finds it is continuous rather than first-order, changing how we understand this fundamental symmetry-breaking phenomenon.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work applies quantum information tools (tensor networks and entanglement entropy) to a foundational problem in high-energy physics, showing how computational methods from quantum science can reach physics that traditional Monte Carlo simulations cannot.

- **Impact on Artificial Intelligence:** The study advances density matrix renormalization group and matrix product state algorithms as scalable, physically interpretable numerical methods, with implications for quantum machine learning and simulation of strongly correlated quantum systems.

- **Impact on Fundamental Interactions:** The results provide the first numerical evidence that the Dashen CP-violating phase transition in a QCD-like model is continuous rather than first-order, with direct consequences for our understanding of CP symmetry breaking in the Standard Model and beyond.

- **Outlook and References:** Future work could extend these tensor network methods to higher-dimensional gauge theories and explore real-time dynamics of the Dashen transition; the full study is available at [arXiv:2303.03799](https://arxiv.org/abs/2303.03799).
