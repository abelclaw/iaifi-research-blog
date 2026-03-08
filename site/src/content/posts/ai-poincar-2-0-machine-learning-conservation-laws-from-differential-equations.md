---
abstract: We present a machine learning algorithm that discovers conservation laws
  from differential equations, both numerically (parametrized as neural networks)
  and symbolically, ensuring their functional independence (a non-linear generalization
  of linear independence). Our independence module can be viewed as a nonlinear generalization
  of singular value decomposition. Our method can readily handle inductive biases
  for conservation laws. We validate it with examples including the 3-body problem,
  the KdV equation and nonlinear Schrödinger equation.
arxivId: '2203.12610'
arxivUrl: https://arxiv.org/abs/2203.12610
authors:
- Ziming Liu
- Varun Madhavan
- Max Tegmark
concepts:
- conservation laws
- functional independence
- differential rank
- hamiltonian systems
- manifold learning
- automated discovery
- symbolic regression
- physics-informed neural networks
- eigenvalue decomposition
- loss function design
- interpretability
figures:
- /iaifi-research-blog/figures/2203_12610/figure_2.png
- /iaifi-research-blog/figures/2203_12610/figure_2.png
- /iaifi-research-blog/figures/2203_12610/figure_3.png
pdfUrl: https://arxiv.org/pdf/2203.12610v2
published: '2022-03-23T17:57:01+00:00'
theme: Foundational AI
title: 'AI Poincaré 2.0: Machine Learning Conservation Laws from Differential Equations'
wordCount: 1101
---

## The Big Picture

Imagine a marble rolling inside a bowl. Without solving any equations, you know something fundamental: energy is conserved. The marble trades speed for height and back again, forever.

This intuition, that certain quantities never change no matter how a system evolves, is one of the deepest ideas in physics. Physicists call these **conservation laws**, and they've unlocked everything from predicting planetary orbits to understanding subatomic particles.

Finding conservation laws by hand is hard. For a simple pendulum, it's straightforward. For three gravitating bodies careening through space, or a nonlinear wave sloshing through a medium, the derivations take pages of painstaking algebra. For genuinely new systems, there's no guarantee we'd recognize a conservation law even if it were staring at us.

A team at MIT and IIT Kharagpur set out to change that. Their algorithm, **AI Poincaré 2.0**, takes a mathematical description of a physical system as input and automatically discovers all its independent conservation laws, outputting them as both numerical functions and human-readable symbolic formulas.

> **Key Insight:** AI Poincaré 2.0 can automatically discover *all* conservation laws of a dynamical system starting from its equations of motion, handling the notoriously tricky problem of functional independence without any human guidance.

## How It Works

The algorithm operates in three stages.

![Figure 1](/iaifi-research-blog/figures/2203_12610/figure_2.png)

**Stage 1: Train neural networks to be conserved quantities.** For any dynamical system, a conserved quantity H must satisfy one condition: its value doesn't change as the system evolves. Mathematically, if **f**(**z**) describes how the system moves, a conservation law H must obey ∇H · **f** = 0. Its gradient must always be perpendicular to the direction of motion. The team represents H as a neural network and trains it to minimize a **conservation loss**, penalizing the network whenever its gradient isn't perpendicular to the flow.

To find *multiple* conservation laws simultaneously, they train several networks at once. A second term, the **independence loss**, discourages networks from converging on the same answer by penalizing pairs whose gradients point in the same direction.

**Stage 2: Count independent conservation laws.** Training multiple networks doesn't guarantee genuinely independent results. Two networks might encode the same quantity in different disguises: energy E and 2E are different functions but carry identical information.

The team addresses this with **functional independence**, a nonlinear generalization of ordinary linear independence. Two quantities are functionally dependent if one can be derived from the other through *any* transformation (squaring, taking a logarithm, you name it). To detect this, they develop a **differential rank** module, a nonlinear cousin of singular value decomposition (SVD). It examines the **Jacobian matrix**, which captures how each candidate conservation law changes with respect to each variable, across many points in **phase space**. From this, the algorithm determines how many truly independent quantities exist.

**Stage 3: Extract symbolic formulas.** Once numerical conservation laws are pinned down, the algorithm searches for human-readable symbolic expressions, using physical inductive biases like polynomial structure to narrow the search.

The method was tested on a demanding suite of classical problems:

- **Kepler problem** (planet orbiting a star): 3 conservation laws recovered ✓
- **2D isotropic harmonic oscillator**: 3 conservation laws recovered ✓
- **2D anisotropic harmonic oscillator**: 3 conservation laws recovered ✓
- **Three-body problem**: 4 conservation laws recovered from a 12-dimensional state space ✓
- **KdV wave equation**: 2–4 conservation laws recovered ✓
- **Nonlinear Schrödinger equation**: 1–3 conservation laws recovered ✓

![Figure 2](/iaifi-research-blog/figures/2203_12610/figure_2.png)

The KdV result stands out. The Korteweg–De Vries equation describes solitons, wave packets that travel without dispersing. Because solitons move in one direction, they violate the **ergodicity** assumption that earlier methods required: the idea that a system will eventually visit every possible state. AI Poincaré 1.0 would have stumbled here. Version 2.0 works directly from the equations rather than observed trajectories, so ergodicity is irrelevant.

![Figure 3](/iaifi-research-blog/figures/2203_12610/figure_3.png)

For the three-body problem, notorious for its chaotic complexity, the algorithm extracted known conserved quantities including total energy and momentum components as interpretable symbolic formulas, not opaque network weights.

## Why It Matters

Conservation laws are the skeleton of physics. **Noether's theorem** establishes that every conservation law corresponds to a symmetry of nature: energy conservation from time-translation symmetry, momentum conservation from spatial symmetry. Finding new conservation laws means discovering new symmetries and uncovering hidden structure in systems we don't yet understand.

The work has implications for AI as well. The functional independence framework applies well beyond physics. Any machine learning task that needs genuinely diverse outputs from an ensemble, where redundant representations are a failure mode, could benefit from the differential rank technique. It's a mathematical tool that stands on its own.

The natural next step is applying this to systems where conservation laws are *unknown*: turbulence, biological networks, novel materials. These are systems where human physicists haven't yet written down the invariants. AI Poincaré 2.0 is a step toward letting the machine do that discovery autonomously.


> **Bottom Line:** AI Poincaré 2.0 shows that machine learning can systematically uncover the hidden invariants of dynamical systems, including famously hard cases like the three-body problem and nonlinear wave equations, by combining neural network training with a nonlinear independence test that works where classical linear algebra falls short.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects deep learning and classical physics by teaching neural networks to discover conservation laws and translate that understanding into symbolic formulas physicists can directly use.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The differential rank module introduces a nonlinear generalization of SVD that measures functional independence among learned representations, with applications to ensemble learning and representation diversity beyond physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The algorithm identifies all known conservation laws for the three-body problem, the KdV equation, and the nonlinear Schrödinger equation without human guidance, providing a general-purpose tool for discovering invariants in complex physical systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could apply AI Poincaré 2.0 to systems with unknown conservation laws, from turbulence to quantum many-body physics, potentially uncovering new symmetries; the paper is available at [arXiv:2203.12610](https://arxiv.org/abs/2203.12610).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">AI Poincaré 2.0: Machine Learning Conservation Laws from Differential Equations</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2203.12610</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Ziming Liu", "Varun Madhavan", "Max Tegmark"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We present a machine learning algorithm that discovers conservation laws from differential equations, both numerically (parametrized as neural networks) and symbolically, ensuring their functional independence (a non-linear generalization of linear independence). Our independence module can be viewed as a nonlinear generalization of singular value decomposition. Our method can readily handle inductive biases for conservation laws. We validate it with examples including the 3-body problem, the KdV equation and nonlinear Schrödinger equation.</span></div></div>
</div>
