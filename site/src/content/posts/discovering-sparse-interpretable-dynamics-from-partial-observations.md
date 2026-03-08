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
wordCount: 1025
---

## The Big Picture

Imagine trying to understand the rules of chess by watching only half the board. You can see some pieces moving, but others are hidden behind a curtain. From those limited observations, could you reconstruct where the hidden pieces are *and* figure out the rules of the game simultaneously? That's roughly the challenge facing scientists who study complex physical systems — from turbulent fluids to laser pulses traveling through fiber-optic cables — where complete measurements are often impossible or prohibitively expensive.

Modern physics and engineering are filled with systems where sensors capture only a partial snapshot. A weather station measures temperature and pressure but not every air molecule's velocity. A telescope records the intensity of light but not its **phase** — the wave's timing and rhythm, which carries information that brightness alone cannot reveal. Without the full picture, even powerful AI models struggle to learn true underlying rules, and without those rules, predictions collapse the moment conditions shift.

A team of MIT physicists has built a machine learning framework that tackles both challenges at once: it reconstructs the hidden parts of a system's state *and* discovers the symbolic governing equations — all from incomplete observations.

> **Key Insight:** By combining a neural network encoder with a sparse symbolic model and training them jointly, this method recovers both hidden variables and exact mathematical laws governing a dynamical system using only partial measurements.

## How It Works

The core architecture pairs two components working in tandem. First, an **encoder** — a neural network that takes a sequence of visible measurements and infers the values of unobserved variables. Second, a **sparse symbolic model** that represents governing equations as a weighted sum of candidate mathematical terms: polynomials, spatial derivatives, trigonometric functions, whatever is physically plausible.

![Figure 1](/iaifi-research-blog/figures/2107_10879/figure_1.png)

The central challenge: how do you train these components together when you can only compare predictions against *partial* observations? The solution uses **higher-order time derivatives** — not just rates of change, but rates of change *of* rates of change, the way acceleration describes how velocity is shifting rather than position itself. The training loop works like this:

1. The encoder produces a reconstructed full state (visible + estimated hidden variables).
2. The symbolic model generates predicted time derivatives of that reconstructed state.
3. Using **automatic differentiation** — a technique for computing exact rates of change through chains of mathematical operations — the framework computes higher-order derivatives of the *visible* states.
4. Those predicted derivatives are compared against **finite-difference estimates** — approximations of rates of change computed from measurements at nearby moments in time — taken directly from the data.
5. The entire system is trained end-to-end to minimize the mismatch.

This sidesteps a chicken-and-egg problem elegantly. You don't need to know the hidden states to train the symbolic model, and you don't need full governing equations to train the encoder. The training signal flows entirely through observable quantities: time derivatives of what you *can* measure.

The sparsity piece matters too. Real physical laws tend to be parsimonious — Newton's second law has three terms, not three hundred. The framework imposes a **sparsity prior** on the symbolic model's coefficients, pushing the network toward compact, interpretable equations. The result isn't a black-box prediction; it's an actual equation you can write down and reason about.

![Figure 2](/iaifi-research-blog/figures/2107_10879/figure_1.png)

The team tested their framework across multiple systems. For ordinary differential equations, they recovered coupled nonlinear oscillators with hidden coordinates. For partial differential equations, they tackled the **nonlinear Schrödinger equation** — a workhorse of fiber optics and quantum mechanics — reconstructing the phase of the field from intensity-only measurements (a classic problem called **phase retrieval**) while simultaneously discovering the governing equation. The method correctly identified symbolic dynamics in each case.

![Figure 3](/iaifi-research-blog/figures/2107_10879/figure_2.png)

## Why It Matters

The ability to discover governing equations from partial observations could reshape how scientists build physical models. Fitting interpretable equations to data today typically requires either complete measurements or strong prior assumptions about system structure. This framework relaxes both. It opens equation discovery to settings where complete instrumentation is physically impossible: deep ocean dynamics, biological neural circuits, plasma physics in fusion reactors.

There's a deeper AI story here too. Most data-driven dynamics models are black boxes — accurate within training conditions, brittle outside them. A symbolic equation captures the *structure* of the physics, not just its surface statistics.

A model that discovers `dψ/dt = i(∂²ψ/∂x² + |ψ|²ψ)` doesn't just interpolate; it encodes a law that generalizes across initial conditions, boundary conditions, and system sizes. That's exactly the kind of generalization symbolic methods offer over purely neural approaches.

Open questions remain. The method currently assumes the number of hidden state dimensions is known — a hyperparameter chosen before training rather than learned from data. Scaling to very high-dimensional PDE systems with many hidden fields is still challenging. And like all sparse regression methods, it depends on a good candidate library of terms: if the true dynamics involve functions not in your library, you won't find them. These are tractable problems, and domain-specific physics constraints offer one promising path forward.

> **Bottom Line:** This framework demonstrates that machine learning can simultaneously reconstruct hidden system states and discover sparse, interpretable governing equations from partial observations alone — bringing physics-informed symbolic discovery to a much broader class of real-world problems.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work merges machine learning methodology with classical physics system identification, using neural encoders to solve a physics-motivated inverse problem and producing symbolic equations with genuine physical interpretability.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The joint encoder–symbolic model architecture with end-to-end training via higher-order derivative matching introduces a principled technique for learning interpretable dynamics under partial observability, advancing the frontier of physics-informed machine learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling phase reconstruction and equation discovery for the nonlinear Schrödinger equation from intensity-only data, the method directly addresses a fundamental measurement challenge in quantum optics, fiber communications, and wave physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions may tackle higher-dimensional PDE systems and relax assumptions about the number of hidden variables; the work appears on arXiv as 2107.10141 and represents an early contribution from MIT's IAIFI-affiliated researchers.</span></div></div>
</div>
