---
abstract: We develop a pairing-based graph neural network for simulating quantum many-body
  systems. Our architecture augments a BCS-type geminal wavefunction with a generalized
  pair amplitude parameterized by a graph neural network. Variational Monte Carlo
  with our neural network simultaneously provides an accurate, flexible, and scalable
  method for simulating many-electron systems. We apply this method to two-dimensional
  semiconductor electron-hole bilayers and obtain accurate results on a variety of
  interaction-induced phases, including the exciton Bose-Einstein condensate, electron-hole
  superconductor, and bilayer Wigner crystal. Our study demonstrates the potential
  of physically-motivated neural network wavefunctions for quantum materials simulations.
arxivId: '2311.02143'
arxivUrl: https://arxiv.org/abs/2311.02143
authors:
- Di Luo
- David D. Dai
- Liang Fu
concepts:
- graph neural networks
- quantum simulation
- monte carlo methods
- geminal wavefunction
- quantum states
- physics-informed neural networks
- neural network wavefunction
- phase transitions
- electron-hole bilayer
- symmetry preservation
- transfer learning
- scalability
figures:
- /iaifi-research-blog/figures/2311_02143/figure_1.png
- /iaifi-research-blog/figures/2311_02143/figure_1.png
- /iaifi-research-blog/figures/2311_02143/figure_2.png
- /iaifi-research-blog/figures/2311_02143/figure_2.png
- /iaifi-research-blog/figures/2311_02143/figure_3.png
- /iaifi-research-blog/figures/2311_02143/figure_3.png
pdfUrl: https://arxiv.org/pdf/2311.02143v2
published: '2023-11-03T17:12:29+00:00'
theme: Astrophysics
title: Pairing-based graph neural network for simulating quantum materials
wordCount: 1058
---

## The Big Picture

Imagine trying to predict the behavior of a crowd of thousands of people, where every person's movement depends on the simultaneous positions of everyone else. Now make those people quantum particles, each existing in a blur of possible states, mysteriously linked to all the others. That's roughly the challenge facing physicists who want to simulate quantum materials from scratch.

The math is exact. Schrödinger's equation describes how quantum particles behave, and physicists have known it for nearly a century. But simulating many electrons together is something else entirely: the number of variables grows exponentially with particle count, making exact computation impossible for anything larger than a handful of atoms.

Physicists have spent decades attacking this exponential wall with clever approximations. Hartree-Fock theory, density functional theory, coupled cluster methods: each captures some physics while sacrificing others. Systems where electrons interact too strongly to be treated independently remain especially stubborn. Standard techniques either fail or give dangerously wrong answers.

A team from MIT and Harvard has now developed a **pairing-based graph neural network wavefunction** that combines physics intuition with machine learning flexibility to simulate quantum materials with new levels of accuracy and scalability. Their target is the **electron-hole bilayer**, a two-dimensional semiconductor sandwich where electrons and their positively charged counterparts (holes) interact across an atomically thin gap, producing exotic quantum states that conventional methods struggle to capture simultaneously.

> **Key Insight:** By encoding the physics of electron pairing directly into a graph neural network architecture, this approach achieves accurate, unbiased simulation of multiple competing quantum phases (exciton condensates, superconductors, and Wigner crystals) within a single unified framework.

## How It Works

The core innovation is **GemiNet**, a portmanteau of "geminal" (a quantum chemistry term for paired-particle wavefunctions) and "network." It builds on a classic piece of physics: the **BCS wavefunction**, originally developed to describe superconductors, where electrons pair up into Cooper pairs and condense into a superfluid.

In the BCS picture, the wavefunction is a determinant of pair amplitudes. This automatically enforces a fundamental quantum rule: electrons are fermions, meaning no two can ever occupy exactly the same state simultaneously. But the traditional BCS formula is a mean-field approximation. It averages out detailed particle interactions rather than tracking them, and it's tailored to describe only certain phases of matter.

GemiNet's key move is replacing the simple, hand-crafted pair amplitude with a **generalized pair amplitude parameterized by a graph neural network**. Here's how:

1. **Start with BCS structure.** The wavefunction is a determinant of electron-hole pair amplitudes, mathematically enforcing pairing physics and fermionic statistics from the outset.
2. **Generalize the pair amplitude.** Instead of a fixed functional form, the pair amplitude becomes a learnable function of all particle positions, computed by a graph neural network.
3. **Build the graph.** Electrons and holes become nodes; their interactions become edges. The GNN passes messages between nodes, letting each particle's effective wavefunction depend on its neighbors.
4. **Optimize with Variational Monte Carlo.** Network parameters are trained by minimizing the system's energy, sampling many random configurations of particle positions to estimate the answer.

![Figure 1](figure:1)

The physics is *built in*, not learned from scratch. The BCS skeleton ensures the network starts with sensible pairing structure. The GNN layers then learn corrections that capture strong correlations, spatial pattern formation, and other effects the mean-field treatment misses.

![Figure 2](figure:2)

**Transfer learning across system sizes** turns out to be a practical advantage worth highlighting. Because the GNN operates on local particle interactions, a network trained on a small system can initialize training on a larger one. Purely data-driven approaches lack this kind of scalability. The authors verify the technique works well, enabling simulation of bilayers with up to 30 electron-hole pairs.

## Why It Matters

The electron-hole bilayer is a rich laboratory for quantum phases. Depending on particle density and interlayer separation, the system can be an **exciton Bose-Einstein condensate** (tightly bound electron-hole pairs condensed into a superfluid), an **electron-hole superconductor** (loosely paired carriers in a BCS state), or a **bilayer Wigner crystal** (electrons and holes separately crystallizing into locked lattices). Probing all three phases with a single unbiased method has been a longstanding challenge.

![Figure 3](figure:3)

GemiNet delivers quantitatively accurate energies across the entire phase diagram. It outperforms Hartree-Fock-Bogoliubov calculations, especially in the intermediate-density regime where correlations matter most. The network correctly captures the **BEC-BCS crossover**, the smooth evolution from tightly bound excitons to loosely paired superconducting carriers, as well as the crystalline Wigner phase at large separations and low densities. Because the network doesn't presuppose a particular phase, it detects which one is energetically favored without methodological bias.

![Figure 4](figure:4)

Many of the most scientifically interesting materials fall into the same category of strongly correlated systems where conventional methods break down: high-temperature superconductors, frustrated magnets, topological insulators. Physically motivated neural network wavefunctions offer a route to simulating these materials from first principles, free of the biases baked into hand-crafted starting-point formulas.

![Figure 5](figure:5)

GemiNet's success on the electron-hole bilayer suggests the strategy can extend to twisted bilayer graphene, moiré materials, and systems relevant to quantum computing hardware. Open questions remain: scalability to larger systems, handling of spin-orbit coupling and magnetic fields, and incorporating longer-range correlations into the GNN architecture. Each is a productive frontier.

![Figure 6](figure:6)

> **Bottom Line:** GemiNet shows that fusing physics-motivated wavefunction structure with graph neural network flexibility enables accurate, scalable, and unbiased simulation of competing quantum phases, opening a new route to understanding strongly correlated quantum materials from first principles.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work translates graph neural network architectures from machine learning into a physically motivated quantum wavefunction that outperforms traditional condensed matter methods on a challenging benchmark, directly embodying the IAIFI mission.

- **Impact on Artificial Intelligence:** GemiNet introduces a strategy for physics-informed neural network design, showing that encoding known physical structure (BCS pairing) into the architectural inductive bias improves sample efficiency, accuracy, and scalability over generic approaches.

- **Impact on Fundamental Interactions:** The method achieves accurate simulation of the full electron-hole bilayer phase diagram, spanning exciton BEC, BCS superconductor, and Wigner crystal phases, in a regime where mean-field theory fails. It provides a new quantitative tool for understanding interaction-driven quantum phases in two-dimensional materials.

- **Outlook and References:** Future work may extend GemiNet to twisted moiré systems, spin-orbit coupled materials, and real-time dynamics; the full paper is available at [arXiv:2311.02143](https://arxiv.org/abs/2311.02143).
