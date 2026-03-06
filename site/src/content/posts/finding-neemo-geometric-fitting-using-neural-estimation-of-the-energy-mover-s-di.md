---
abstract: 'A novel neural architecture was recently developed that enforces an exact
  upper bound on the Lipschitz constant of the model by constraining the norm of its
  weights in a minimal way, resulting in higher expressiveness compared to other techniques.
  We present a new and interesting direction for this architecture: estimation of
  the Wasserstein metric (Earth Mover''s Distance) in optimal transport by employing
  the Kantorovich-Rubinstein duality to enable its use in geometric fitting applications.
  Specifically, we focus on the field of high-energy particle physics, where it has
  been shown that a metric for the space of particle-collider events can be defined
  based on the Wasserstein metric, referred to as the Energy Mover''s Distance (EMD).
  This metrization has the potential to revolutionize data-driven collider phenomenology.
  The work presented here represents a major step towards realizing this goal by providing
  a differentiable way of directly calculating the EMD. We show how the flexibility
  that our approach enables can be used to develop novel clustering algorithms.'
arxivId: '2209.15624'
arxivUrl: https://arxiv.org/abs/2209.15624
authors:
- Ouail Kitouni
- Niklas Nolte
- Mike Williams
concepts:
- optimal transport
- energy mover's distance
- lipschitz networks
- kantorovich-rubinstein duality
- jet physics
- collider physics
- clustering
- geometric deep learning
- loss function design
- physics-informed neural networks
figures:
- /iaifi-research-blog/figures/2209_15624/figure_1.png
- /iaifi-research-blog/figures/2209_15624/figure_2.png
- /iaifi-research-blog/figures/2209_15624/figure_3.png
pdfUrl: https://arxiv.org/pdf/2209.15624v1
published: '2022-09-30T17:54:09+00:00'
theme: Experimental Physics
title: 'Finding NEEMo: Geometric Fitting using Neural Estimation of the Energy Mover''s
  Distance'
wordCount: 1072
---

## The Big Picture

Imagine you're trying to compare two sandstorms — one swirling over the Sahara, another churning above the Gobi Desert. How different are they, really? You could count the grains, measure the wind speed, or — more cleverly — ask: how much work would it take to rearrange the sand from one storm into the pattern of the other? That "minimum work" is the Earth Mover's Distance, a mathematical concept with surprising power.

At the heart of a particle physics detector, the same question arises with each collision: how different are these two sprays of particles, and what geometry best describes them?

At the Large Hadron Collider, protons smash together millions of times per second, spraying exotic debris across sensitive detectors. Physicists make sense of this chaos by clustering debris into **jets** — cone-shaped sprays of particles tracing back to quarks and gluons, the most fundamental building blocks of matter. But comparing collision events precisely is hard.

The best metric for this job, the **Energy Mover's Distance (EMD)** — essentially the Earth Mover's Distance applied to particle collisions — has been difficult to compute efficiently and *differentiably*. Differentiability means the computation can be smoothly tuned by an algorithm, like turning a dial rather than flipping switches; without it, you can't plug the metric into modern machine learning pipelines and let them optimize automatically.

A team from MIT's IAIFI has now built NEEMo — Neural Estimation of the Energy Mover's Distance — a system that computes the EMD exactly and differentiably using a specially constrained neural network, unlocking a new generation of geometry-aware clustering algorithms for collider physics.

> **Key Insight:** By parameterizing the Kantorovich-Rubinstein dual of the Wasserstein metric with a Lipschitz-bounded neural network, NEEMo computes the exact Energy Mover's Distance in a fully differentiable way — no approximations required.

## How It Works

The EMD between two particle distributions is formally a **Wasserstein-1 metric** — a mathematical measure of the minimum cost to transport energy from one radiation pattern into another, as if energy were earth being moved from pile to pile. Computing it directly is expensive. A clever mathematical trick, the **Kantorovich-Rubinstein (KR) duality**, reformulates the transport problem into something tractable: instead of finding the cheapest moving plan, find a scoring function that maximizes the difference in expectations between two distributions, subject to the function being **1-Lipschitz** — meaning it can't change faster than the distance between its inputs, with no sudden cliffs.

That Lipschitz constraint is the crux. Most neural networks are not automatically Lipschitz-bounded, and enforcing the constraint while keeping the network expressive is non-trivial.

Previous approaches used **spectral normalization** — a technique that limits how sharply each layer can transform its inputs — or other proxies that sacrifice expressiveness. The architecture underpinning NEEMo enforces an exact upper bound on the Lipschitz constant by directly constraining weight matrix norms, in a minimal way that wastes almost none of the model's capacity.

![Figure 2](/iaifi-research-blog/figures/2209_15624/figure_2.png)

The training procedure works as a minimax game — two optimizers competing in alternating rounds. Given a collision event Q and a parameterized geometric shape P_θ (say, a set of circles or rings), NEEMo alternates between:

1. **Maximize** over Lipschitz network parameters φ to find the Kantorovich potential — the scoring function that, evaluated on both distributions, yields the EMD.
2. **Minimize** over geometric parameters θ to move shape P_θ closer to event distribution Q.

Because everything is differentiable — the Lipschitz network, the geometric parameters, the energy weights — gradients flow freely. This replaces the **ε-Sinkhorn** estimation used in the prior SHAPER framework, which blurs the transport problem slightly to make it tractable but only approximates the EMD to order ε.

![Figure 1](/iaifi-research-blog/figures/2209_15624/figure_1.png)

The results are visually compelling. Starting from randomly placed circles, NEEMo iteratively deforms them to match three synthetic target clusters. By epoch 100, the circles are in roughly the right neighborhood; by epoch 1000, they snap into nearly perfect alignment. The heatmap overlaid on each frame shows the Kantorovich potential itself — a force field whose gradients push the geometric shapes toward the data.

## Why It Matters

Jet clustering is one of the most fundamental operations in experimental particle physics — it runs on every collision event recorded at the LHC, trillions of times over an experiment's lifetime. The algorithms currently used (like anti-k_T) were designed for computational efficiency, not geometric optimality. The EMD offers a principled, geometry-aware alternative, but its use has been limited by the difficulty of computing it fast enough and differentiably enough for real optimization pipelines.

NEEMo changes that calculus. By making the EMD exact and differentiable, it opens the door to end-to-end trainable clustering algorithms — systems where every component is optimized together directly against physics objectives, rather than tuned piecemeal. The authors specifically flag the **future Electron-Ion Collider** as a target application, where traditional clustering methods perform poorly and where EMD-based observables could yield qualitatively new insights into quark-gluon structure.

Beyond collider physics, the approach generalizes to any optimal transport problem — Wasserstein distances appear in generative models, domain adaptation, and distributional robustness, all of which stand to benefit.

![Figure 3](/iaifi-research-blog/figures/2209_15624/figure_3.png)

The main current limitation is speed: gradient-based minimax optimization of a neural network is slower than fast approximate solvers, making real-time detector application impractical today. But powerful custom optimizers could close this gap, and differentiability already unlocks offline analysis tasks where compute time is less critical.

> **Bottom Line:** NEEMo delivers the first exact, differentiable computation of the Energy Mover's Distance via Lipschitz-constrained neural networks, turning a hard combinatorial transport problem into a smooth optimization — and handing particle physicists a powerful new tool for understanding the geometry of collisions.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">NEEMo directly bridges mathematical optimal transport theory, neural network architecture design, and experimental particle physics, translating an abstract duality theorem into a working tool for collider data analysis.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work demonstrates that exact Lipschitz-constrained networks are not just theoretically elegant but practically powerful, offering a blueprint for deploying Wasserstein-based losses in any differentiable ML pipeline without approximation error.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By making EMD-based jet clustering exact and gradient-friendly, NEEMo advances the data-driven phenomenology toolkit for current LHC experiments and next-generation facilities like the Electron-Ion Collider.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work targets faster optimization to enable near-real-time use at detectors; the paper is available on arXiv and the weight-constraint implementation is open-source at github.com/niklasnolte/MonotOneNorm.</span></div></div>
</div>
