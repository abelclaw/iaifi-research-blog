---
abstract: 'We present an approach to solving the ground state of Fermi systems that
  contain spin or other discrete degrees of freedom in addition to continuous coordinates.
  The approach combines a Markov chain Monte Carlo sampling for energy estimation
  that we adapted to cover the extended configuration space with a transformer-based
  wavefunction to represent fermionic states. This sampling is necessary when the
  Hamiltonian contains explicit spin dependence and, for spin-independent Hamiltonians,
  we find that the inclusion of spin updates leads to faster convergence to an antiferromagnetic
  ground state. A transformer with both continuous position and discrete spin as inputs
  achieves universal approximation to spinful generalized orbitals. We validate the
  method on a range of two-dimensional material problems: a two-dimensional electron
  gas with Rashba spin-orbit coupling, a noncollinear spin texture, and a quantum
  antiferromagnet in a honeycomb moiré potential.'
arxivId: '2510.18621'
arxivUrl: https://arxiv.org/abs/2510.18621
authors:
- Alexander Avdoshkin
- Max Geier
- Liang Fu
concepts:
- neural variational monte carlo
- spinful fermionic ansatz
- transformers
- monte carlo methods
- quantum states
- attention mechanisms
- quantum simulation
- hamiltonian systems
- symmetry preservation
- phase transitions
- moiré materials
figures:
- /iaifi-research-blog/figures/2510_18621/figure_1.png
- /iaifi-research-blog/figures/2510_18621/figure_1.png
- /iaifi-research-blog/figures/2510_18621/figure_2.png
- /iaifi-research-blog/figures/2510_18621/figure_2.png
- /iaifi-research-blog/figures/2510_18621/figure_3.png
- /iaifi-research-blog/figures/2510_18621/figure_3.png
pdfUrl: https://arxiv.org/pdf/2510.18621v1
published: '2025-10-21T13:20:31+00:00'
theme: Theoretical Physics
title: An integrated neural wavefunction solver for spinful Fermi systems
wordCount: 1264
---

## The Big Picture

Imagine tracking a flock of birds where every bird's movement depends on every other bird's simultaneously, and each bird also has a hidden internal state that shapes how it responds to its neighbors. Now scale that to trillions of electrons. Each electron has both a position in space and a quantum property called **spin**, a built-in compass needle that can point up, down, or anywhere in between. That's the challenge of quantum many-body physics, and it's one of the hardest computational problems in science.

Neural networks have made real progress on the simpler version: finding the quantum ground state (the lowest-energy arrangement) of electrons described purely by their positions. But most interesting quantum materials, including magnets, superconductors, and topological insulators, owe their exotic properties to the interplay between *where* electrons sit and *what their spins are doing*. Neural network solvers have largely choked when spin enters the picture.

A team of physicists at MIT has built a method that handles position *and* spin simultaneously, using a neural network architecture borrowed from AI language models and pairing it with a smarter search procedure that flips spins as well as moves electrons.

> **Key Insight:** By combining a transformer architecture that processes continuous positions and discrete spins jointly with a Monte Carlo sampler that flips spins as well as moves electrons, the MIT team achieved a universal neural wavefunction solver capable of describing the full complexity of spinful quantum matter.

## How It Works

The method is built on **variational Monte Carlo (VMC)**: parameterize a guess for the quantum wavefunction, then optimize those parameters to minimize the system's energy. You can't compute the energy directly. Instead, you *sample* electron configurations according to the wavefunction's probability distribution and average over them. For position-only systems, existing neural VMC methods work well. When electrons also carry spin, an intrinsic angular momentum that can point up or down, the sampling breaks down unless you explicitly include moves that flip spins.

![Figure 1](figure:1)

The researchers solved the sampling problem with a **Markov chain Monte Carlo (MCMC)** procedure, a systematic technique for exploring states by taking guided random steps, that alternates between two types of moves:

- **Coordinate updates:** electrons drift in real space according to a Gaussian proposal distribution
- **Spin flip updates:** spins are randomly flipped, either freely (allowing total magnetization to change) or via "sector-preserving" swaps that exchange spin states between electrons while keeping total magnetization fixed

Without spin updates, the sampler gets stuck in configurations with the wrong spin arrangement, causing slow convergence or outright failure to find the true ground state. With spin updates, the method explores the full configuration space efficiently.

The wavefunction is represented by a **transformer neural network**, the same architecture powering large language models, repurposed for quantum physics. The transformer takes continuous positions and discrete spin labels of all electrons simultaneously. Its attention mechanisms, which weigh relationships between all inputs at once, capture correlations between electrons whether those correlations are position-mediated, spin-mediated, or both.

The authors prove mathematically that this architecture is a **universal approximator** of spinful generalized orbitals: it can represent any physically valid fermionic wavefunction. That's a significant theoretical guarantee. Fermionic antisymmetry (the Pauli exclusion principle, which forbids two fermions from occupying the same quantum state) is enforced by taking determinants of the neural network outputs, following earlier neural wavefunction networks like FermiNet and Psiformer, but extended here to the spinful setting.

![Figure 2](figure:2)

## Why It Matters

The team validated their solver on three increasingly complex physical problems.

First: a two-dimensional electron gas with **Rashba spin-orbit coupling**, where electrons moving through a material with broken mirror symmetry experience an effective magnetic field that locks spin to momentum. This coupling is a key ingredient in topological insulators and certain superconductors.

Second: a noncollinear spin texture, where spins wind around in real space like a slowly rotating compass needle. These textures arise in magnetic skyrmion systems and resist simulation because no single fixed reference direction exists for measuring spin.

Third: a quantum antiferromagnet in a honeycomb moiré potential, directly relevant to moiré materials like twisted bilayer graphene. Two atomically thin sheets stacked at a slight angle create exotic correlated phases. The antiferromagnetic ground state emerges purely from electrical repulsion among electrons, with no magnetic interactions explicitly built in.

![Figure 3](figure:3)

A bonus finding: even for systems where spin updates aren't strictly required for accuracy, including them dramatically speeds convergence to antiferromagnetic ground states. The sampler discovers the correct spin ordering faster when it can explore spin configurations directly.

![Figure 4](figure:4)

The materials most likely to harbor next-generation superconductors, quantum computers, and topological devices are precisely those where spin and spatial correlations are inseparable: moiré systems, magnetic topological insulators, frustrated magnets, heavy fermion materials. A reliable first-principles tool for these systems removes a major bottleneck between theoretical proposal and experimental validation.

![Figure 5](figure:5)

Transformers aren't just for language and images. Here they provide a provably expressive framework for quantum states with mixed continuous and discrete inputs. The ideas extend to any quantum system with internal degrees of freedom: nuclear spins, orbital quantum numbers, valley pseudospin in 2D materials, or color charge in quark systems.

![Figure 6](figure:6)

Current runs handle tens of electrons in 2D geometries. Extending to three dimensions and larger particle numbers, where the most technologically relevant materials live, will require further algorithmic and computational advances. But the framework is in place.

> **Bottom Line:** MIT physicists have built the first integrated neural wavefunction solver that handles spin and position on equal footing, combining a transformer architecture with extended Monte Carlo sampling to crack open a wide class of quantum matter problems previously out of reach for neural network methods.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work marries transformer architectures from modern machine learning with the variational Monte Carlo framework of quantum physics, showing that neural network tools developed for language and vision can be rigorously adapted to solve fundamental condensed matter problems.
- **Impact on Artificial Intelligence:** The paper proves that transformers with mixed continuous-discrete inputs are universal approximators for spinful fermionic wavefunctions, giving a theoretical foundation for using attention-based architectures in quantum many-body machine learning.
- **Impact on Fundamental Interactions:** The solver captures correlated magnetic and spin-orbit phenomena in two-dimensional systems, including moiré antiferromagnetism and noncollinear spin textures, directly from first principles, without prior assumptions about ground state structure.
- **Outlook and References:** Scaling to three-dimensional materials and larger system sizes could make this a standard tool for predicting properties of correlated quantum materials; the paper is available at [arXiv:2510.18621](https://arxiv.org/abs/2510.18621) (Avdoshkin, Geier, Fu, MIT Department of Physics).

## Original Paper Details
- **Title:** An integrated neural wavefunction solver for spinful Fermi systems
- **arXiv ID:** 2510.18621
- **Authors:** ["Alexander Avdoshkin", "Max Geier", "Liang Fu"]
- **Abstract:** We present an approach to solving the ground state of Fermi systems that contain spin or other discrete degrees of freedom in addition to continuous coordinates. The approach combines a Markov chain Monte Carlo sampling for energy estimation that we adapted to cover the extended configuration space with a transformer-based wavefunction to represent fermionic states. This sampling is necessary when the Hamiltonian contains explicit spin dependence and, for spin-independent Hamiltonians, we find that the inclusion of spin updates leads to faster convergence to an antiferromagnetic ground state. A transformer with both continuous position and discrete spin as inputs achieves universal approximation to spinful generalized orbitals. We validate the method on a range of two-dimensional material problems: a two-dimensional electron gas with Rashba spin-orbit coupling, a noncollinear spin texture, and a quantum antiferromagnet in a honeycomb moiré potential.
