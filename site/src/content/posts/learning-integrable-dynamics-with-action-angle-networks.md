---
abstract: Machine learning has become increasingly popular for efficiently modelling
  the dynamics of complex physical systems, demonstrating a capability to learn effective
  models for dynamics which ignore redundant degrees of freedom. Learned simulators
  typically predict the evolution of the system in a step-by-step manner with numerical
  integration techniques. However, such models often suffer from instability over
  long roll-outs due to the accumulation of both estimation and integration error
  at each prediction step. Here, we propose an alternative construction for learned
  physical simulators that are inspired by the concept of action-angle coordinates
  from classical mechanics for describing integrable systems. We propose Action-Angle
  Networks, which learn a nonlinear transformation from input coordinates to the action-angle
  space, where evolution of the system is linear. Unlike traditional learned simulators,
  Action-Angle Networks do not employ any higher-order numerical integration methods,
  making them extremely efficient at modelling the dynamics of integrable physical
  systems.
arxivId: '2211.15338'
arxivUrl: https://arxiv.org/abs/2211.15338
authors:
- Ameya Daigavane
- Arthur Kosmala
- Miles Cranmer
- Tess Smidt
- Shirley Ho
concepts:
- action-angle coordinates
- hamiltonian systems
- integrable systems
- normalizing flows
- symmetry preservation
- representation learning
- symplectic structure
- physics-informed neural networks
- surrogate modeling
- conservation laws
- inverse problems
figures:
- /iaifi-research-blog/figures/2211_15338/figure_1.png
- /iaifi-research-blog/figures/2211_15338/figure_1.png
- /iaifi-research-blog/figures/2211_15338/figure_2.png
- /iaifi-research-blog/figures/2211_15338/figure_2.png
- /iaifi-research-blog/figures/2211_15338/figure_3.png
- /iaifi-research-blog/figures/2211_15338/figure_3.png
pdfUrl: https://arxiv.org/pdf/2211.15338v1
published: '2022-11-24T17:37:20+00:00'
theme: Foundational AI
title: Learning Integrable Dynamics with Action-Angle Networks
wordCount: 1002
---

## The Big Picture

Imagine predicting where a pendulum will be in an hour by simulating every tiny tick of time between now and then. Each step introduces a small error — a rounding here, an approximation there — and those errors stack up like interest on a debt. By the end, your prediction might be wildly wrong. This is the fundamental curse haunting most machine learning simulators for physical systems: they work step-by-step, and step-by-step mistakes compound into catastrophic drift.

Physics has known a secret for over a century. Certain physical systems — called **integrable systems** — possess so much hidden symmetry that their behavior can be described with surprising simplicity. Describe them in the right coordinates, and predicting the future requires nothing more than multiplication and addition. A spinning top, an orbiting planet, a vibrating crystal: wildly complicated in everyday terms, but change your perspective and they're just clocks ticking at steady rates.

A team of researchers from MIT, Princeton, LMU Munich, and the Flatiron Institute has built a neural network that learns to find those magical coordinates automatically — and uses them to simulate physical systems without ever accumulating a single step-by-step error.

> **Key Insight:** Action-Angle Networks transform complex physical dynamics into a space where evolution is perfectly linear, eliminating the error accumulation that plagues traditional learned simulators and making long-range predictions orders of magnitude more stable.

## How It Works

The mathematical engine behind this idea comes from classical mechanics: **action-angle coordinates**. These special coordinates exist for physical systems with enough hidden symmetry — technically called **Hamiltonian systems**, a framework describing motion through positions and momenta. The right coordinate transformation splits the description into two parts.

The *actions* — think of them as the energy content or "shape" of the motion — stay constant forever. The *angles* — the phase or position along the motion's cycle — increase at a perfectly steady rate. In these coordinates, predicting the future is trivially easy: multiply angular velocity by time elapsed and add. No integration. No error accumulation.

The catch? Finding these coordinates has historically required deep mathematical insight. The Action-Angle Network learns them from data. The architecture breaks into three clean stages:

1. **Encode:** A stack of **symplectic normalizing flows** — transformations specially designed to preserve the conservation laws baked into the physics — maps ordinary positions and momenta into an intermediate representation. A polar coordinate transformation then converts this into proper action-angle coordinates (I, θ). This constraint ensures the transformation can never violate conservation of energy or momentum.

2. **Evolve:** A small **multi-layer perceptron (MLP)** takes the actions I and predicts the angular velocities θ̇. Because the actions are constant along any trajectory, this only needs to be computed once. The angles then advance as: θ(t + Δt) = θ(t) + θ̇ · Δt (mod 2π). Just arithmetic.

3. **Decode:** The inverse transformation maps the updated action-angle state back to physical coordinates — positions and momenta — using the inverse of the learned symplectic map.

![Figure 1](/iaifi-research-blog/figures/2211_15338/figure_1.png)

One elegant engineering choice deserves mention: the network doesn't map directly onto a **torus** (the donut-shaped surface that is the natural geometry for looping angle coordinates), which would create numerical breakdowns at the edges. Instead, it outputs Cartesian components converted to polar form — a small trick that makes training dramatically more stable.

![Figure 2](/iaifi-research-blog/figures/2211_15338/figure_1.png)

The result is a simulator whose inference time doesn't depend on the time step at all. Want to predict a system's state one second in the future, or one million seconds? Same computation. Same cost. Traditional integrators work proportionally harder for larger time jumps; Action-Angle Networks don't.

## Why It Matters

The implications stretch in two directions — toward AI and toward physics.

On the AI side, this work joins a growing movement to embed physical *structure* directly into neural networks rather than hoping the network learns that structure from data alone. Constraining the encoder to only learn symplectic transformations isn't just mathematical nicety; it's what makes the whole approach trustworthy over long rollouts. The network cannot violate conservation laws even if it wanted to.

On the physics side, the ability to automatically discover action-angle coordinates for complex systems opens real doors. Integrable systems appear throughout fundamental physics — from particles in electromagnetic traps to quantum spin chains to planetary orbital mechanics. If a researcher suspects a system might be integrable but doesn't know its action-angle coordinates analytically, this framework offers a data-driven path to finding them.

The learned coordinates themselves become scientific artifacts worth examining. Future extensions might tackle *nearly* integrable systems — where weak perturbations break exact integrability — potentially connecting to the rich physics of chaos and the **KAM theorem**, the mathematical result describing how ordered motion gradually breaks down as a system is disturbed.

> **Bottom Line:** By teaching a neural network to find the coordinates where physics becomes linear, Action-Angle Networks sidestep the error accumulation problem entirely — delivering fast, stable, parameter-efficient simulations that improve with the elegance of the physics, not despite it.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work transplants a century-old concept from classical mechanics — action-angle coordinates — into a modern neural network architecture, demonstrating that deep physical symmetry principles can be encoded as inductive biases to yield qualitatively better learned simulators.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Action-Angle Networks achieve competitive trajectory prediction with significantly fewer parameters than standard learned simulators, and uniquely offer inference time independent of the prediction horizon — a fundamental efficiency gain over all step-by-step integration approaches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The framework provides a data-driven method to automatically discover the hidden integrable structure of physical systems, potentially accelerating the identification of conserved quantities and symmetries across domains from celestial mechanics to condensed matter physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend the framework to approximately integrable and chaotic systems, explore connections to quantum integrability, and scale to higher-dimensional field theories; the paper appeared at the Machine Learning and the Physical Sciences workshop at NeurIPS 2022 (arXiv: 2209.11440).</span></div></div>
</div>
