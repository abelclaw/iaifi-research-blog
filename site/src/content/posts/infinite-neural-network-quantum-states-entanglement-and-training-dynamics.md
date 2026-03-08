---
abstract: We study infinite limits of neural network quantum states ($\infty$-NNQS),
  which exhibit representation power through ensemble statistics, and also tractable
  gradient descent dynamics. Ensemble averages of Renyi entropies are expressed in
  terms of neural network correlators, and architectures that exhibit volume-law entanglement
  are presented. A general framework is developed for studying the gradient descent
  dynamics of neural network quantum states (NNQS), using a quantum state neural tangent
  kernel (QS-NTK). For $\infty$-NNQS the training dynamics is simplified, since the
  QS-NTK becomes deterministic and constant. An analytic solution is derived for quantum
  state supervised learning, which allows an $\infty$-NNQS to recover any target wavefunction.
  Numerical experiments on finite and infinite NNQS in the transverse field Ising
  model and Fermi Hubbard model demonstrate excellent agreement with theory. $\infty$-NNQS
  opens up new opportunities for studying entanglement and training dynamics in other
  physics applications, such as in finding ground states.
arxivId: '2112.00723'
arxivUrl: https://arxiv.org/abs/2112.00723
authors:
- Di Luo
- James Halverson
concepts:
- quantum states
- neural network quantum states
- entanglement
- kernel methods
- quantum state neural tangent kernel
- stochastic processes
- ensemble methods
- volume-law entanglement
- quantum simulation
- bayesian inference
- representation learning
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2112_00723/figure_1.png
- /iaifi-research-blog/figures/2112_00723/figure_1.png
- /iaifi-research-blog/figures/2112_00723/figure_2.png
- /iaifi-research-blog/figures/2112_00723/figure_2.png
- /iaifi-research-blog/figures/2112_00723/figure_3.png
- /iaifi-research-blog/figures/2112_00723/figure_3.png
pdfUrl: https://arxiv.org/pdf/2112.00723v2
published: '2021-12-01T18:57:17+00:00'
theme: Theoretical Physics
title: 'Infinite Neural Network Quantum States: Entanglement and Training Dynamics'
wordCount: 1033
---

## The Big Picture

Imagine describing every grain of sand on every beach on Earth, not just each grain's position, but how it's entangled with every other grain in a vast, invisible web. That's roughly the challenge of simulating quantum many-body systems. A quantum state doesn't just grow bigger as you add particles; it grows *exponentially* bigger. Add one more electron and the complexity doubles. Add ten and you're in a different universe of computational difficulty.

Neural network quantum states (NNQS), where a neural network compactly represents a quantum wavefunction, have attracted a lot of attention as a potential escape hatch. Neural networks are extraordinarily flexible: they can, in principle, encode any quantum state. But "in principle" and "in practice" are two different things. Do we actually understand *how well* they encode quantum information? Do we know *why* training works, or when it fails?

Di Luo and James Halverson at IAIFI tackled these questions by pushing neural network quantum states to a dramatic limit: infinite size. Their framework, ∞-NNQS (infinite neural network quantum states), provides the first mathematically exact, solvable picture of both how quantum correlations are captured and how these networks learn.

> **Key Insight:** By taking neural networks to infinite width, the authors derive exact, closed-form solutions for quantum state representation and learning dynamics, turning an opaque black box into a transparent, solvable system.

## How It Works

The central trick comes from a well-known result in machine learning theory: as a neural network grows infinitely wide, its behavior simplifies dramatically. The network's outputs become a **Gaussian process** (GP), a probability distribution over functions whose statistics are fully determined by simple, computable rules. This is the neural network Gaussian process (NNGP) correspondence, and Luo and Halverson exploit it to study quantum states.

For a neural network representing a quantum wavefunction, the NNGP limit means the ensemble of possible wavefunctions has Gaussian statistics. This matters enormously for **entanglement entropy**, which measures quantum correlations between regions of a system, essentially quantifying how much quantum information is shared between two subsystems.

The authors show that ensemble averages of Rényi entanglement entropies (a family of entropy measures, each capturing a different slice of the correlation structure) can be expressed in terms of neural network correlators. In the Gaussian limit, these correlators become exactly computable using Wick's theorem, a quantum field theory technique that reduces complex calculations to products of two-point correlations.

As a concrete example, the team analyzes the Cos-net architecture, where the wavefunction is built from cosine activations with random weights. In the infinite-width limit, Cos-net's two-point correlation function takes a clean Gaussian form. Tuning one parameter (σ_w → ∞), the wavefunction ensemble approaches states exhibiting **volume-law entanglement**, where entanglement grows proportionally to system size. This is the richest possible entanglement structure, characteristic of the most complex quantum states.

![Figure 1](figure:1)

The team tested this prediction numerically using Cos-net networks at widths N = 400, 1000, and 4000. The Von Neumann entanglement entropy converges toward the Page value (the theoretical maximum for random states) as width increases, confirming the theory.

---

The second major contribution addresses training. The authors introduce the **quantum state neural tangent kernel** (QS-NTK), a framework that tracks how the wavefunction changes as network parameters are updated during gradient descent.

In general, the QS-NTK depends on the current parameters and evolves during training, making it hard to analyze. At infinite width, though, the QS-NTK becomes deterministic and constant. It no longer changes as training progresses. This transforms gradient descent from a complex nonlinear system into a linear ordinary differential equation with an analytic solution.

![Figure 2](figure:2)

The practical payoff is clear. For quantum state supervised learning, where an NNQS is trained to match a target wavefunction, the authors prove that an ∞-NNQS with a well-behaved QS-NTK can *always* recover any target wavefunction exactly. No approximation, no guesswork: a provable guarantee.

- Training dynamics follow an exponential convergence curve, fully determined by the QS-NTK's eigenvalues
- The QS-NTK computed at initialization accurately predicts training trajectories for *finite*-width networks, provided widths are large enough
- The framework applies broadly: ground state optimization, quantum state tomography (reconstructing a quantum state from measurements), and supervised learning all fit within the same mathematical structure

![Figure 3](figure:3)

The team validated these predictions on two canonical models: the transverse field Ising model (a paradigm of quantum phase transitions) and the Fermi Hubbard model (a cornerstone of condensed matter physics for strongly correlated electrons). In both cases, finite-width networks converged toward the infinite-width analytic predictions as width increased.

![Figure 4](figure:4)

## Why It Matters

This work hits two targets at once. On the AI side, it extends the neural tangent kernel framework, a major theoretical achievement in understanding deep learning, into quantum physics. The QS-NTK isn't a straightforward transplant: quantum wavefunctions are complex-valued and must be normalized, which introduces subtleties requiring genuinely new mathematical machinery.

On the physics side, analytically characterizing entanglement in NNQS ensembles opens the door to what you might call entanglement engineering. Physicists studying topological phases, quantum error correction, or many-body ground states could choose neural network architectures specifically to match desired entanglement patterns. Finite-width corrections introduce non-Gaussianities beyond the simple infinite limit, hinting at a rich variety of entanglement behaviors accessible by tuning architecture and width.

![Figure 5](figure:5)

> **Bottom Line:** Infinite neural network quantum states give physicists their first complete analytic handle on both the entanglement structure and training dynamics of NNQS, grounding a promising but poorly understood tool in rigorous, predictive theory.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work directly fuses neural tangent kernel theory from machine learning with entanglement entropy calculations from quantum physics, producing results neither field could have reached alone.

- **Impact on Artificial Intelligence:** The QS-NTK extends deep learning theory to complex-valued, normalized function spaces, providing provable convergence guarantees for a fundamentally new class of learning problems.

- **Impact on Fundamental Interactions:** Analytically characterizing volume-law entanglement in ∞-NNQS creates new theoretical directions for studying strongly correlated quantum matter and designing quantum representations with tailored entanglement.

- **Outlook and References:** Future directions include applying ∞-NNQS to ground state optimization and exploring how finite-width non-Gaussianities shape entanglement in physically relevant systems; the full paper is available at [arXiv:2112.00723](https://arxiv.org/abs/2112.00723).
