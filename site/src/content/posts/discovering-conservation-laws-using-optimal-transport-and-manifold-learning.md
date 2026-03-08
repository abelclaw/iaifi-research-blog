---
abstract: Conservation laws are key theoretical and practical tools for understanding,
  characterizing, and modeling nonlinear dynamical systems. However, for many complex
  systems, the corresponding conserved quantities are difficult to identify, making
  it hard to analyze their dynamics and build stable predictive models. Current approaches
  for discovering conservation laws often depend on detailed dynamical information
  or rely on black box parametric deep learning methods. We instead reformulate this
  task as a manifold learning problem and propose a non-parametric approach for discovering
  conserved quantities. We test this new approach on a variety of physical systems
  and demonstrate that our method is able to both identify the number of conserved
  quantities and extract their values. Using tools from optimal transport theory and
  manifold learning, our proposed method provides a direct geometric approach to identifying
  conservation laws that is both robust and interpretable without requiring an explicit
  model of the system nor accurate time information.
arxivId: '2208.14995'
arxivUrl: https://arxiv.org/abs/2208.14995
authors:
- Peter Y. Lu
- Rumen Dangovski
- Marin Soljačić
concepts:
- manifold learning
- optimal transport
- conservation laws
- phase space isosurface embedding
- dimensionality reduction
- wasserstein geometry
- hamiltonian systems
- spectral methods
- inverse problems
- interpretability
- stochastic processes
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2208_14995/figure_1.png
- /iaifi-research-blog/figures/2208_14995/figure_1.png
- /iaifi-research-blog/figures/2208_14995/figure_2.png
- /iaifi-research-blog/figures/2208_14995/figure_2.png
- /iaifi-research-blog/figures/2208_14995/figure_3.png
- /iaifi-research-blog/figures/2208_14995/figure_3.png
pdfUrl: https://arxiv.org/pdf/2208.14995v2
published: '2022-08-31T17:50:04+00:00'
theme: Theoretical Physics
title: Discovering Conservation Laws using Optimal Transport and Manifold Learning
wordCount: 1223
---

## The Big Picture

Imagine watching a marble roll inside a bowl, blindfolded, with only a list of the marble's positions. No clock, no equations, no knowledge of the bowl's shape. Could you figure out what stays constant as the marble moves? For centuries, physicists have wrestled with this kind of problem: hidden conservation laws lurk inside complex physical systems, and finding them can unlock everything from a system's long-term behavior to whether it's solvable at all.

Conservation laws are physics' great gift. Energy, momentum, angular momentum: these quantities don't change over time, no matter how wildly a system evolves. They act as invisible guardrails, constraining what can happen next. But for many real-world systems (turbulent fluids, spreading chemical reactions, some quantum systems) the conserved quantities are unknown and fiendishly hard to find.

Current computational methods either demand high-quality timestamped data or rely on black-box deep learning models that can fit conserved quantities but can't explain *why* they work.

A team at MIT has taken a different approach: reframe the whole problem as a question of *geometry*, and let the shape of trajectories tell you everything you need to know.

> **Key Insight:** By treating each physical trajectory as a geometric object and measuring how its shape varies across different starting conditions, you can identify both the number of conserved quantities and their values. No clock, no equations of motion, no neural network required.

## How It Works

When a dynamical system has conserved quantities, every trajectory in **phase space** (the multi-dimensional map of all possible states) is trapped on a lower-dimensional surface called an **isosurface**. Think of energy conservation like a topographic contour line: a marble can move freely along a line of constant elevation, but it can't jump to a different elevation without violating energy conservation. Each distinct set of conserved values defines a distinct isosurface, and the system's trajectories sample these surfaces.

![Figure 1](/iaifi-research-blog/figures/2208_14995/figure_1.png)

The method works in three stages:

1. **Collect trajectories.** Start many copies of the system from different initial conditions, letting each trace out its own isosurface in phase space.

2. **Measure shape differences using optimal transport.** Two trajectories living on *different* isosurfaces should look geometrically distinct. To quantify this, the researchers compute the **2-Wasserstein distance**, a metric from **optimal transport theory** that measures the "cost" of transforming one point cloud into another. The Wasserstein distance doesn't care about the order in which points were visited, which sidesteps the need for accurate timestamps entirely.

3. **Extract the embedding with diffusion maps.** Once you have a pairwise distance matrix between all trajectories, **diffusion maps** (a technique for uncovering hidden geometric structure in high-dimensional data) find the low-dimensional shape hiding in that matrix. Each axis of the resulting embedding corresponds directly to one conserved quantity.

![Figure 2](/iaifi-research-blog/figures/2208_14995/figure_1.png)

The output isn't just a count of conserved quantities. It's a map of the space those quantities inhabit. For a simple harmonic oscillator, where energy is the only conserved quantity, the embedding is a one-dimensional curve. For a system with two conserved quantities, it's a two-dimensional surface.

The researchers verified this analytically for the harmonic oscillator and numerically for systems ranging from a double pendulum to the **Korteweg–De Vries (KdV) equation**, a classic model of shallow water waves famously discovered to have *infinitely many* conserved quantities. Their method correctly identifies the leading conserved modes without ever being told the equations of motion.

![Figure 3](/iaifi-research-blog/figures/2208_14995/figure_2.png)

The approach handles real-world messiness well. Noise in measurements, missing phase-space dimensions, and approximate conservation laws all degrade results only gradually. Because the geometry is built on statistical distributions of points rather than individual precise measurements, it holds up where point-by-point methods would break down.

## Why It Matters

The traditional physics discovery process has long relied on humans noticing patterns, proposing candidate conserved quantities, and testing them analytically. That process doesn't scale, and for messy experimental data, it often doesn't even start.

This work offers something new: a principled, automated way to scan for hidden conserved structure in raw trajectory data, with no model assumptions and no tunable neural-network weights to overfit. The authors report it outperforms prior deep learning-based methods on their benchmarks while running significantly faster.

The payoff extends beyond pure physics. In machine learning for dynamical systems, knowing the conserved quantities lets researchers build prediction models that respect those constraints, so a network trained to simulate fluid dynamics won't accidentally violate mass conservation over long rollouts. In complex systems biology or climate science, where conservation laws may exist but aren't derived from first principles, this tool could surface new conserved quantities that guide theory. And because the embedding coordinates are tied directly to the geometric structure of the data rather than to opaque weight matrices, the results are interpretable by construction.

Open questions remain. The method works best when individual trajectories densely sample their isosurfaces, a condition that may be hard to satisfy for high-dimensional systems or sparse experimental data. Extending the framework to stochastic systems or quantum dynamics is an obvious next step.

> **Bottom Line:** Reframing conservation law discovery as a geometry problem, measuring how trajectory shapes vary across initial conditions, gives you a fast, interpretable, model-free method that beats deep learning baselines on these tasks. Sometimes the most powerful tool isn't a bigger neural network, but a smarter way of looking at the data.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses optimal transport theory, manifold learning, and classical physics into a single discovery tool. It speaks both the language of geometry and the language of dynamics, exactly the kind of AI-physics crossover that IAIFI exists to pursue.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The non-parametric, interpretable approach shows that geometric reasoning can outperform black-box deep learning for structured scientific tasks, offering a template for physics-informed machine learning that doesn't sacrifice transparency.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By automating the identification of conserved quantities in complex nonlinear systems, including partial differential equations like KdV, this method could speed up the discovery of new symmetries and invariants in understudied physical systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions may target stochastic, high-dimensional, or quantum systems where conservation takes more subtle forms. The full method and codebase are openly available; see the [arXiv preprint (arXiv:2208.14995)](https://arxiv.org/abs/2208.14995) by Lu, Dangovski, and Soljačić at MIT.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Discovering Conservation Laws using Optimal Transport and Manifold Learning</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[arXiv:2208.14995](https://arxiv.org/abs/2208.14995)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">Peter Y. Lu, Rumen Dangovski, Marin Soljačić</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Conservation laws are key theoretical and practical tools for understanding, characterizing, and modeling nonlinear dynamical systems. However, for many complex systems, the corresponding conserved quantities are difficult to identify, making it hard to analyze their dynamics and build stable predictive models. Current approaches for discovering conservation laws often depend on detailed dynamical information or rely on black box parametric deep learning methods. We instead reformulate this task as a manifold learning problem and propose a non-parametric approach for discovering conserved quantities. We test this new approach on a variety of physical systems and demonstrate that our method is able to both identify the number of conserved quantities and extract their values. Using tools from optimal transport theory and manifold learning, our proposed method provides a direct geometric approach to identifying conservation laws that is both robust and interpretable without requiring an explicit model of the system nor accurate time information.</span></div></div>
</div>
