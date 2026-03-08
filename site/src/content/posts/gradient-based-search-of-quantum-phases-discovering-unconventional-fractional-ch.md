---
abstract: 'The discovery and understanding of new quantum phases has time and again
  transformed both fundamental physics and technology, yet progress often relies on
  slow, intuition-based theoretical considerations or experimental serendipity. Here,
  we introduce a general gradient-based framework for targeted phase discovery. We
  define a differentiable function, dubbed "target-phase loss function", which encodes
  spectral fingerprints of a quantum state, thereby recasting phase search as a tractable
  optimization problem in Hamiltonian space. The method is broadly applicable to phases
  characterized by ground-state degeneracy and can be extended to a wide range of
  symmetry-broken and topological orders. As a demonstration, we apply it to spinless
  fermions on the kagome lattice and discover two distinctive fractional Chern insulators
  (FCIs), verified through detailed exact diagonalization: (i) at filling $ν= 1/3$,
  a "non-ideal" Abelian FCI whose band geometry lies far beyond the Landau-level mimicry
  paradigm and all recent generalizations; and (ii) at $ν= 1/2$, a non-Abelian FCI
  stabilized purely by finite-range two-body interactions. These results provide the
  first explicit realization of such types of FCIs and establish a versatile paradigm
  for systematic quantum-phase discovery.'
arxivId: '2509.10438'
arxivUrl: https://arxiv.org/abs/2509.10438
authors:
- André Grossi Fonseca
- Eric Wang
- Sachin Vaidya
- Patrick J. Ledwith
- Ashvin Vishwanath
- Marin Soljačić
concepts:
- loss function design
- fractional chern insulators
- hamiltonian systems
- spectral methods
- quantum states
- automated discovery
- topological order
- symmetry preservation
- exact diagonalization
- eigenvalue decomposition
- quantum simulation
- phase transitions
- symmetry breaking
figures:
- /iaifi-research-blog/figures/2509_10438/figure_1.png
- /iaifi-research-blog/figures/2509_10438/figure_1.png
- /iaifi-research-blog/figures/2509_10438/figure_2.png
- /iaifi-research-blog/figures/2509_10438/figure_2.png
- /iaifi-research-blog/figures/2509_10438/figure_3.png
- /iaifi-research-blog/figures/2509_10438/figure_3.png
pdfUrl: https://arxiv.org/pdf/2509.10438v1
published: '2025-09-12T17:47:46+00:00'
theme: Theoretical Physics
title: 'Gradient-based search of quantum phases: discovering unconventional fractional
  Chern insulators'
wordCount: 1000
---

## The Big Picture

Imagine searching for a specific crystal in a vast, featureless desert. No map, no compass, just a vague sense it exists somewhere. For decades, that's roughly how physicists hunted for exotic quantum phases of matter: distinct states with properties far stranger than ordinary solids, liquids, or gases, navigated through enormous parameter spaces with mostly intuition and luck.

These phases aren't academic curiosities. Superconductivity gave us MRI machines and particle accelerators. The quantum mechanics of crystalline solids built the semiconductor industry. Today, physicists believe phases with **topological order**, where quantum information is encoded in a material's global structure rather than any single site, making it highly resistant to local errors, could form the backbone of fault-tolerant quantum computers.

A team from MIT, Harvard, and IAIFI has now turned this wandering into a directed march. By treating quantum phase discovery as a machine learning optimization problem, they built a systematic method that locates exotic quantum phases on demand, including ones no one expected to find.

> **Key Insight:** By encoding the spectral fingerprints of a desired quantum state into a differentiable loss function, the researchers transform quantum phase discovery into gradient descent optimization, enabling systematic, targeted exploration of Hamiltonian parameter space.

## How It Works

Every quantum phase leaves a characteristic fingerprint in a system's energy spectrum: particular patterns of **ground-state degeneracy** distributed across different **symmetry sectors**. Write down what that fingerprint should look like mathematically, define a loss function measuring how far any Hamiltonian is from producing it, then use gradient descent to find parameters that minimize it. That's the core idea.

The **target-phase loss function** works as follows. Given a Hamiltonian parameterized by a vector of numbers (hopping amplitudes, interaction strengths, lattice geometry), the algorithm partitions the low-energy spectrum into a "target manifold" (states you want as ground states) and a "complement manifold" (everything else). The loss measures the energy gap between the highest target state and the lowest complement state. Negative gap means you've found the phase. Positive gap means gradient descent can point you in the right direction.

![Figure 1](figure:1)

The workflow has three steps:

1. **Specify the target:** Encode the expected spectral fingerprints, including which symmetry sectors host ground states, how many, and how the spectrum evolves under magnetic flux insertion.
2. **Minimize the loss:** Run gradient descent through Hamiltonian parameter space, adjusting physical parameters to drive the system toward the target phase.
3. **Verify with exact diagonalization:** Once the optimizer converges, use **exact diagonalization (ED)**, a numerically exact method for small quantum systems, to confirm the phase is genuine and map the surrounding phase diagram.

The loss function is differentiable with respect to Hamiltonian parameters, which is what makes gradient optimization possible. Quantum energy spectra involve matrix eigenvalues that can change discontinuously, so the team handles this carefully to maintain a smooth optimization landscape.

The researchers tested their framework on spinless fermions on the **kagome lattice**, a tiling of corner-sharing triangles found experimentally in materials like herbertsmithite. They searched for **fractional Chern insulators (FCIs)**, exotic topological phases where electrons organize into collective states carrying fractional charges. FCIs are lattice analogues of the fractional quantum Hall effect, potentially accessible without enormous magnetic fields.

![Figure 2](figure:2)

First target: an Abelian FCI at filling fraction ν = 1/3. Most known FCIs live near the "ideal" regime, where band geometry closely mimics the lowest Landau level. The optimizer found a non-ideal FCI whose band geometry lies far outside any ideal description, directly contradicting a widespread assumption in the field.

![Figure 3](figure:3)

The second target was more ambitious: a **non-Abelian FCI** at filling ν = 1/2. Non-Abelian phases are the holy grail of topological quantum computing. Their exotic excitations, non-Abelian anyons, store quantum information in ways intrinsically protected from errors. Previously known examples required either three-body interactions or unrealistically long interaction ranges. The search turned up a **Moore–Read state**, the prototypical non-Abelian FCI first proposed in the 1990s, stabilized purely by finite-range, two-body interactions. This is the first explicit realization of such a phase.

![Figure 4](figure:4)

Both discoveries were confirmed through exact diagonalization, spectral flow analysis under flux insertion, and phase diagram mapping.

## Why It Matters

What matters most here isn't any single discovery but the methodology itself. The gradient-based framework applies broadly: any phase with identifiable spectral fingerprints and continuous Hamiltonian parameters is a candidate. Charge density waves, quantum spin liquids, various topological orders. All fair game. Researchers encode domain knowledge about what a phase should look like; the optimizer finds where it lives.

![Figure 5](figure:5)

The non-Abelian FCI discovery raises immediate theoretical questions. Why does this phase appear with finite-range interactions? What framework describes fractionalization in bands this far from the ideal limit? Concrete examples like this tend to accelerate theoretical understanding much the way experimental discoveries do.

The method could extend to finite-temperature phases, disordered systems, or open quantum systems. It could also interface with materials databases, running searches over realistic parameters and pointing experimentalists toward specific compounds worth synthesizing.

> **Bottom Line:** By treating quantum phase discovery as a machine learning optimization problem, this team found two fractional Chern insulators that shouldn't exist according to conventional wisdom and built a framework that could systematically map the exotic quantum phases hiding throughout condensed matter physics.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work directly imports gradient-based optimization, the engine of modern deep learning, into many-body quantum physics, enabling systematic phase discovery that neither field could achieve alone.
- **Impact on Artificial Intelligence:** The paper shows that differentiable programming and gradient descent apply to quantum eigenvalue problems, extending AI-assisted scientific discovery from pattern recognition to active hypothesis generation and search.
- **Impact on Fundamental Interactions:** The discovery of a non-Abelian fractional Chern insulator stabilized by finite-range two-body interactions provides the first explicit realization of this phase, challenging existing theoretical frameworks and opening new territory in topological quantum matter.
- **Outlook and References:** Future work can extend this framework to realistic material parameters and finite-temperature phases; the full results are available at [arXiv:2509.10438](https://arxiv.org/abs/2509.10438).
