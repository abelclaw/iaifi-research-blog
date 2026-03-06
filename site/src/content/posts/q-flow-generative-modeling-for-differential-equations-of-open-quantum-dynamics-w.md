---
abstract: Studying the dynamics of open quantum systems can enable breakthroughs both
  in fundamental physics and applications to quantum engineering and quantum computation.
  Since the density matrix $ρ$, which is the fundamental description for the dynamics
  of such systems, is high-dimensional, customized deep generative neural networks
  have been instrumental in modeling $ρ$. However, the complex-valued nature and normalization
  constraints of $ρ$, as well as its complicated dynamics, prohibit a seamless connection
  between open quantum systems and the recent advances in deep generative modeling.
  Here we lift that limitation by utilizing a reformulation of open quantum system
  dynamics to a partial differential equation (PDE) for a corresponding probability
  distribution $Q$, the Husimi Q function. Thus, we model the Q function seamlessly
  with off-the-shelf deep generative models such as normalizing flows. Additionally,
  we develop novel methods for learning normalizing flow evolution governed by high-dimensional
  PDEs based on the Euler method and the application of the time-dependent variational
  principle. We name the resulting approach $Q$-$Flow$ and demonstrate the scalability
  and efficiency of Q-Flow on open quantum system simulations, including the dissipative
  harmonic oscillator and the dissipative bosonic model. Q-Flow is superior to conventional
  PDE solvers and state-of-the-art physics-informed neural network solvers, especially
  in high-dimensional systems.
arxivId: '2302.12235'
arxivUrl: https://arxiv.org/abs/2302.12235
authors:
- Owen Dugan
- Peter Y. Lu
- Rumen Dangovski
- Di Luo
- Marin Soljačić
concepts:
- normalizing flows
- husimi q function
- open quantum dynamics
- quantum simulation
- quantum states
- euler-kl method
- generative models
- density estimation
- physics-informed neural networks
- likelihood estimation
- monte carlo methods
- variational autoencoders
figures:
- /iaifi-research-blog/figures/2302_12235/figure_1.png
- /iaifi-research-blog/figures/2302_12235/figure_1.png
- /iaifi-research-blog/figures/2302_12235/figure_2.png
- /iaifi-research-blog/figures/2302_12235/figure_2.png
- /iaifi-research-blog/figures/2302_12235/figure_3.png
- /iaifi-research-blog/figures/2302_12235/figure_3.png
pdfUrl: https://arxiv.org/pdf/2302.12235v2
published: '2023-02-23T18:54:27+00:00'
theme: Theoretical Physics
title: 'Q-Flow: Generative Modeling for Differential Equations of Open Quantum Dynamics
  with Normalizing Flows'
wordCount: 989
---

## The Big Picture

Imagine trying to describe the behavior of a quantum system constantly nudged and disrupted by its surroundings — a qubit leaking energy to its environment, a laser-driven atom radiating photons, a quantum computer losing coherence to thermal noise. These are **open quantum systems**, and simulating them is one of the most computationally brutal problems in modern physics.

The difficulty comes down to bookkeeping. The complete mathematical description of such a system lives in a **density matrix** — a grid of numbers tracking all quantum probabilities and correlations. For a system of *k* identical components, this grid has N²ᵏ entries. Add one more component and the storage requirement doesn't just grow — it explodes. This is the curse of dimensionality, and for open quantum systems, it bites hard.

Researchers at MIT and IAIFI have found a clever way around this wall. By rethinking *what* mathematical object you're trying to model, they've built a bridge between deep generative models called normalizing flows and the messy physics of quantum systems that don't live in isolation. The result is Q-Flow.

> **Key Insight:** By replacing the quantum density matrix with a related probability distribution called the Husimi Q function, Q-Flow lets researchers use powerful off-the-shelf generative AI models to simulate complex open quantum systems — no custom quantum-specific neural architecture required.

## How It Works

The core trick in Q-Flow is a change of representation. Instead of working with the **density matrix** ρ — which involves imaginary numbers and must satisfy strict mathematical constraints that make it awkward for standard machine learning — the team reformulates the physics in terms of the **Husimi Q function**.

The Q function is a *quasi-probability distribution*: real-valued, always non-negative, and normalized like an ordinary probability distribution. The "quasi" prefix is a physicist's caveat — it encodes quantum information, but looks classical from the outside.

![Figure 1](/iaifi-research-blog/figures/2302_12235/figure_1.png)

This reformulation transforms the problem. The **quantum master equation** governing how the density matrix evolves becomes a **partial differential equation (PDE)** for the Q function — high-dimensional, but living entirely in the world of real-valued probability distributions. And modeling probability distributions is exactly what modern generative AI excels at.

The team chose **normalizing flows** as their generative model. A normalizing flow learns to transform a simple distribution (like a Gaussian) into a complex, irregular one through a sequence of smooth, reversible steps. Critically, normalizing flows provide both fast sampling and exact probability density values — both essential for optimizing a high-dimensional quantum simulation.

Training the flow to follow the Q function's time evolution required two complementary methods:

- **Euler-KL method**: Advances the simulation one small time step at a time. At each step, the current flow predicts the Q function a moment later, and **KL divergence** — a standard measure of distributional mismatch — adjusts the flow to match. Conceptually clean and scalable.
- **TDVP (Time-Dependent Variational Principle)**: A more sophisticated update derived from the Euler approach that accounts for the internal geometry of the model's parameter space, making updates more efficient and better-conditioned.

![Figure 2](/iaifi-research-blog/figures/2302_12235/figure_1.png)

The team tested Q-Flow on two canonical problems: the **dissipative harmonic oscillator** and a **dissipative bosonic model**, both run across increasing numbers of dimensions. In low dimensions, Q-Flow matches or beats traditional PDE solvers — finite-difference and pseudo-spectral methods — in accuracy. As dimension increases, those classical methods collapse under exponential cost. Q-Flow doesn't.

![Figure 3](/iaifi-research-blog/figures/2302_12235/figure_2.png)

Q-Flow also outperforms **physics-informed neural networks (PINNs)**, a popular approach that trains neural networks to satisfy PDE residuals. PINNs struggle to scale; Q-Flow's normalizing flow representation is better matched to high-dimensional probability distributions, and the Euler-KL training signal is more stable than minimizing raw residuals.

The key conceptual result: for Q-Flow, the computational bottleneck is no longer *dimension* — it's the *complexity of the Q function itself*. If the quantum state isn't wildly irregular, Q-Flow handles systems that are completely out of reach for conventional methods.

![Figure 4](/iaifi-research-blog/figures/2302_12235/figure_2.png)

## Why It Matters

Open quantum systems are everywhere in the physics that matters most right now. Quantum computers decohere. Quantum sensors interact with their measurement apparatus. Quantum networks transmit information through lossy channels. Every one of these devices operates under the physics Q-Flow is designed to simulate.

Beyond applications, this work opens a conceptual door. For years, the quantum machine learning community has built custom neural architectures to handle quantum-specific constraints — complex numbers, trace normalization, positivity. Q-Flow suggests a different philosophy: change the representation until the problem looks like something machine learning already knows how to solve.

The Husimi Q function is a real probability distribution. So use tools built for real probability distributions — normalizing flows, diffusion models, flow matching. Future advances in generative AI could flow directly into quantum physics simulation, with no translation layer required.

> **Bottom Line:** Q-Flow turns the simulation of open quantum systems into a generative modeling problem by working with the Husimi Q function instead of the density matrix — unlocking state-of-the-art deep learning tools for high-dimensional quantum physics and outperforming both classical PDE solvers and physics-informed neural networks where it counts most.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">Q-Flow bridges deep generative modeling and open quantum system simulation by reformulating quantum dynamics as a PDE over a real probability distribution, enabling direct application of machine learning tools to fundamental physics problems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work introduces novel training methods — Euler-KL and TDVP — for teaching normalizing flows to evolve according to high-dimensional PDEs, advancing the frontier of physics-constrained generative modeling.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Q-Flow enables scalable simulation of continuous-variable open quantum systems in high dimensions, a regime where all prior methods fail, with direct applications to quantum computing and quantum engineering.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending Q-Flow to fermionic systems, exploring diffusion models and flow matching as alternative architectures, and applying the framework to real quantum hardware noise modeling; the full paper is available at arXiv:2303.02536.</span></div></div>
</div>
