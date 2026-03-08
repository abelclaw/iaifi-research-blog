---
abstract: Identifying the governing equations of a nonlinear dynamical system is key
  to both understanding the physical features of the system and constructing an accurate
  model of the dynamics that generalizes well beyond the available data. We propose
  a machine learning framework for discovering these governing equations using only
  partial observations, combining an encoder for state reconstruction with a sparse
  symbolic model. Our tests show that this method can successfully reconstruct the
  full system state and identify the underlying dynamics for a variety of ODE and
  PDE systems.
arxivId: '2107.10879'
arxivUrl: https://arxiv.org/abs/2107.10879
authors:
- Peter Y. Lu
- Joan Ariño
- Marin Soljačić
concepts:
- sparse models
- symbolic regression
- interpretability
- system identification
- autoencoders
- inverse problems
- hidden state reconstruction
- representation learning
- self-supervised learning
- loss function design
- physics-informed neural networks
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2107_10879/figure_1.png
- /iaifi-research-blog/figures/2107_10879/figure_1.png
- /iaifi-research-blog/figures/2107_10879/figure_2.png
- /iaifi-research-blog/figures/2107_10879/figure_2.png
- /iaifi-research-blog/figures/2107_10879/figure_3.png
- /iaifi-research-blog/figures/2107_10879/figure_3.png
pdfUrl: https://arxiv.org/pdf/2107.10879v2
published: '2021-07-22T18:23:23+00:00'
theme: Foundational AI
title: Discovering Sparse Interpretable Dynamics from Partial Observations
wordCount: 987
---

## The Big Picture

Imagine trying to understand the rules of chess by watching only half the board. You can see some pieces moving, but others are hidden behind a curtain. From those limited observations, could you reconstruct where the hidden pieces are *and* figure out the rules of the game simultaneously? That's roughly the challenge facing scientists who study complex physical systems like turbulent fluids or laser pulses traveling through fiber-optic cables, where complete measurements are often impossible or prohibitively expensive.

Modern physics and engineering are filled with systems where sensors capture only a partial snapshot. A weather station measures temperature and pressure but not every air molecule's velocity. A telescope records the intensity of light but not its **phase**, the wave's timing and rhythm, which carries information that brightness alone cannot reveal.

Without the full picture, even powerful AI models struggle to learn true underlying rules. And without those rules, predictions collapse the moment conditions shift.

A team of MIT physicists has built a machine learning framework that does both at once: it reconstructs the hidden parts of a system's state *and* discovers the symbolic governing equations, all from incomplete observations.

> **Key Insight:** By combining a neural network encoder with a sparse symbolic model and training them jointly, this method recovers both hidden variables and exact mathematical laws governing a dynamical system using only partial measurements.

## How It Works

The architecture has two components. First, an **encoder**: a neural network that takes a sequence of visible measurements and infers the values of unobserved variables. Second, a **sparse symbolic model** that represents governing equations as a weighted sum of candidate mathematical terms (polynomials, spatial derivatives, trigonometric functions, whatever is physically plausible).

![Figure 1](figure:1)

How do you train these components together when you can only compare predictions against *partial* observations? The answer involves **higher-order time derivatives**: not just rates of change, but rates of change *of* rates of change, the way acceleration describes how velocity is shifting rather than position itself. The training loop works like this:

1. The encoder produces a reconstructed full state (visible + estimated hidden variables).
2. The symbolic model generates predicted time derivatives of that reconstructed state.
3. Using **automatic differentiation**, a technique for computing exact rates of change through chains of mathematical operations, the framework computes higher-order derivatives of the *visible* states.
4. Those predicted derivatives are compared against **finite-difference estimates** (approximations of rates of change computed from measurements at nearby moments in time) taken directly from the data.
5. The entire system is trained end-to-end to minimize the mismatch.

This neatly sidesteps a chicken-and-egg problem. You don't need to know the hidden states to train the symbolic model, and you don't need full governing equations to train the encoder. The training signal flows entirely through observable quantities: time derivatives of what you *can* measure.

The sparsity piece matters too. Real physical laws tend to be parsimonious; Newton's second law has three terms, not three hundred. The framework imposes a **sparsity prior** on the symbolic model's coefficients, pushing the network toward compact, interpretable equations. The result isn't a black-box prediction. It's an actual equation you can write down and reason about.

![Figure 2](figure:2)

The team tested their framework across multiple systems. For ordinary differential equations, they recovered coupled nonlinear oscillators with hidden coordinates. For partial differential equations, they tackled the **nonlinear Schrödinger equation**, a workhorse of fiber optics and quantum mechanics, reconstructing the phase of the field from intensity-only measurements (a classic problem called **phase retrieval**) while simultaneously discovering the governing equation. The method correctly identified the symbolic dynamics in each case.

![Figure 3](figure:3)

## Why It Matters

Discovering governing equations from partial observations could change how scientists build physical models. Fitting interpretable equations to data today typically requires either complete measurements or strong prior assumptions about system structure. This framework relaxes both requirements, opening equation discovery to settings where complete instrumentation is physically impossible: deep ocean dynamics, biological neural circuits, plasma physics in fusion reactors.

There's a broader AI angle here. Most data-driven dynamics models are black boxes, accurate within training conditions but brittle outside them. A symbolic equation captures the *structure* of the physics, not just its surface statistics. A model that discovers `dψ/dt = i(∂²ψ/∂x² + |ψ|²ψ)` doesn't just interpolate; it encodes a law that generalizes across initial conditions, boundary conditions, and system sizes. That's the kind of generalization symbolic methods offer over purely neural approaches.

Open questions remain. The method currently assumes the number of hidden state dimensions is known, a hyperparameter chosen before training rather than learned from data. Scaling to very high-dimensional PDE systems with many hidden fields hasn't been demonstrated yet. And like all sparse regression methods, it depends on a good candidate library of terms: if the true dynamics involve functions not in your library, you won't find them. Domain-specific physics constraints offer one promising path forward on each of these fronts.

> **Bottom Line:** Machine learning can simultaneously reconstruct hidden system states and discover sparse, interpretable governing equations from partial observations alone, bringing physics-informed symbolic discovery to a much broader class of real-world problems.

---

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work merges machine learning methodology with classical physics system identification, using neural encoders to solve a physics-motivated inverse problem and producing symbolic equations with genuine physical interpretability.

- **Impact on Artificial Intelligence:** The joint encoder–symbolic model architecture, trained end-to-end via higher-order derivative matching, introduces a principled technique for learning interpretable dynamics under partial observability, pushing the boundaries of physics-informed machine learning.

- **Impact on Fundamental Interactions:** By enabling phase reconstruction and equation discovery for the nonlinear Schrödinger equation from intensity-only data, the method tackles a longstanding measurement challenge in quantum optics, fiber communications, and wave physics.

- **Outlook and References:** Future extensions may tackle higher-dimensional PDE systems and relax assumptions about the number of hidden variables; see [arXiv:2107.10879](https://arxiv.org/abs/2107.10879) for the full paper from MIT's IAIFI-affiliated researchers.
