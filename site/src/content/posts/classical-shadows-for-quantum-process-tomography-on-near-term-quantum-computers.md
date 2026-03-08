---
abstract: Quantum process tomography is a powerful tool for understanding quantum
  channels and characterizing properties of quantum devices. Inspired by recent advances
  using classical shadows in quantum state tomography [H.-Y. Huang, R. Kueng, and
  J. Preskill, Nat. Phys. 16, 1050 (2020).], we have developed ShadowQPT, a classical
  shadow method for quantum process tomography. We introduce two related formulations
  with and without ancilla qubits. ShadowQPT stochastically reconstructs the Choi
  matrix of the device allowing for an a-posteri classical evaluation of the device
  on arbitrary inputs with respect to arbitrary outputs. Using shadows we then show
  how to compute overlaps, generate all $k$-weight reduced processes, and perform
  reconstruction via Hamiltonian learning. These latter two tasks are efficient for
  large systems as the number of quantum measurements needed scales only logarithmically
  with the number of qubits. A number of additional approximations and improvements
  are developed including the use of a pair-factorized Clifford shadow and a series
  of post-processing techniques which significantly enhance the accuracy for recovering
  the quantum channel. We have implemented ShadowQPT using both Pauli and Clifford
  measurements on the IonQ trapped ion quantum computer for quantum processes up to
  $n=4$ qubits and achieved good performance.
arxivId: '2110.02965'
arxivUrl: https://arxiv.org/abs/2110.02965
authors:
- Ryan Levy
- Di Luo
- Bryan K. Clark
concepts:
- quantum process tomography
- classical shadow tomography
- choi matrix reconstruction
- quantum computing
- quantum states
- hamiltonian systems
- monte carlo methods
- inverse problems
- entanglement
- sparse models
- bayesian inference
figures:
- /iaifi-research-blog/figures/2110_02965/figure_1.png
- /iaifi-research-blog/figures/2110_02965/figure_1.png
- /iaifi-research-blog/figures/2110_02965/figure_2.png
- /iaifi-research-blog/figures/2110_02965/figure_2.png
- /iaifi-research-blog/figures/2110_02965/figure_3.png
- /iaifi-research-blog/figures/2110_02965/figure_3.png
pdfUrl: https://arxiv.org/pdf/2110.02965v3
published: '2021-10-06T18:00:01+00:00'
theme: Theoretical Physics
title: Classical Shadows for Quantum Process Tomography on Near-term Quantum Computers
wordCount: 1023
---

## The Big Picture

Imagine trying to understand a mysterious machine by feeding it inputs and observing outputs. Simple enough, until the machine obeys quantum mechanics.

In the quantum world, measuring disturbs what you're measuring. That's not a flaw in your instruments; it's a fundamental rule of physics. And for a device with even a few quantum bits, the number of measurements needed to fully characterize its behavior grows exponentially. Fully mapping a 10-qubit quantum device with traditional methods could require more experiments than there are atoms in the observable universe.

This is the problem at the heart of **quantum process tomography (QPT)**: characterizing what a quantum device *does*, not just for one specific input, but for any possible input. QPT is essential for building trustworthy quantum computers, but its costs have historically been staggering.

A team from the University of Illinois, the Flatiron Institute, MIT, and Harvard's NSF AI Institute (IAIFI) has developed **ShadowQPT**, a smarter approach that slashes those costs using a technique called **classical shadows**.

> ShadowQPT extends the classical shadows trick from quantum states to quantum processes, enabling full characterization of quantum devices with logarithmically, not exponentially, many measurements for many practical tasks.

## How It Works

Classical shadows, introduced by Huang, Kueng, and Preskill in 2020, work like a statistical compression scheme. Instead of measuring every property of a quantum state directly, you apply random quantum operations, measure in a fixed basis, and store compact "shadow" records. Later, you estimate many different properties from those records without returning to the quantum device. Think of it as taking quick snapshots from random angles, then using geometry to reconstruct a 3D object.

ShadowQPT extends this logic from quantum *states* to quantum *processes*. The bridge between the two is the **Choi matrix**, a technique that encodes an entire quantum channel (the complete description of how a process transforms quantum information) as a single quantum state in a doubled mathematical space. Shadow tomography on that doubled-up state reveals everything about the underlying process.

The team develops two formulations: one using **ancilla qubits** (extra quantum bits entangled with the input) and one applying random operations on both input and output sides, a two-sided scheme that works without ancillas.

![Figure 1](figure:1)

The measurement procedure follows concrete steps:

1. **Prepare random input states** by applying random quantum operations to a fixed reference state.
2. **Run the quantum process** on those inputs.
3. **Apply random measurement operations** and record outcomes in the computational basis.
4. **Store classical shadow records**, compact descriptions of each measurement outcome.
5. **Post-process classically** to estimate properties of the Choi matrix.

One practical improvement stands out: the **pair-factorized Clifford shadow**. Instead of costly global random Clifford gates (structured quantum operations that are mathematically convenient but expensive to implement across all qubits simultaneously), the team applies random two-qubit Clifford gates to neighboring pairs. This is far more tractable on real hardware while preserving most of the statistical benefits.

![Figure 2](figure:2)

Raw shadow reconstructions can be unphysical, producing matrices with negative probabilities or other artifacts. The team addresses this by projecting the reconstructed Choi matrix back into the space of valid physical channels and applying a purification step. These corrections make a measurable difference on noisy hardware.

![Figure 3](figure:3)

The efficiency gains are stark. For tasks like predicting how a process acts on a specific input/output pair, or extracting the behavior of any *k*-qubit subsystem, measurements scale only **logarithmically** with qubit count. That's the difference between needing 30 measurements versus 10³⁰ for a 100-qubit system.

The team validated ShadowQPT on IonQ's trapped-ion quantum computer, characterizing processes on 2, 3, and 4 qubits using both Pauli and Clifford measurements. They tested both unitary processes (clean, reversible quantum gates) and non-unitary channels involving noise.

![Figure 4](figure:4)

ShadowQPT-reconstructed processes showed good agreement with direct measurements. Clifford shadows outperformed Pauli measurements for full process reconstruction, consistent with theory. The physical projection and purification steps measurably boosted accuracy.

![Figure 5](figure:5)

The team also demonstrated **Hamiltonian learning**, reconstructing the physical equations governing a quantum system directly from ShadowQPT data. They recovered parameters of a random 1D Ising model (a standard model of interacting quantum particles arranged in a line), with measurement requirements scaling logarithmically in system size.

![Figure 6](figure:6)

## Why It Matters

Quantum computing is entering an era where devices are just large enough to do interesting things but too noisy to run ideal algorithms. Every quantum algorithm on real hardware runs on a *noisy quantum channel*, not a perfect unitary. ShadowQPT gives experimentalists a practical, scalable tool to characterize that channel, to understand not just whether a device is broken, but *how* it's broken.

The connection to Hamiltonian learning opens a further path: using quantum computers to study physics itself. If you can efficiently extract the effective Hamiltonian governing a quantum system's dynamics from process tomography data, near-term hardware becomes a probe of materials, molecules, and field theories. Logarithmic scaling keeps this feasible as systems grow.

Classical shadow ideas were developed in quantum information theory, but they transfer well to the noisier, messier world of NISQ-era (Noisy Intermediate-Scale Quantum) experimentation. ShadowQPT is evidence of that.

> ShadowQPT provides the first classical-shadow approach to quantum process tomography, achieving exponential measurement savings for tasks of practical interest and validated on real trapped-ion hardware. It is a concrete step forward for characterizing and trusting near-term quantum devices.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work merges quantum information theory, quantum physics, and machine learning-inspired statistical methods into a practical tool for quantum device characterization, connecting theoretical guarantees with experimental implementation.

- **Impact on Artificial Intelligence:** ShadowQPT's logarithmic measurement scaling parallels advances in efficient learning theory, showing how AI-inspired statistical compression can drastically cut the data requirements for learning complex quantum systems.

- **Impact on Fundamental Interactions:** By enabling efficient Hamiltonian learning from quantum process data, ShadowQPT opens a route for quantum computers to reconstruct the physical laws governing quantum many-body systems, directly supporting IAIFI's mission of using AI to probe fundamental physics.

- **Outlook and References:** Future work will extend ShadowQPT to larger qubit counts, more complex noise models, and continuous-variable systems; the full paper is available at [arXiv:2110.02965](https://arxiv.org/abs/2110.02965).
