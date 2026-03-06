---
abstract: 'We present a class of novel optimisers for training neural networks that
  makes use of the Riemannian metric naturally induced when the loss landscape is
  embedded in higher-dimensional space. This is the same metric that underlies common
  visualisations of loss landscapes. By taking this geometric perspective literally
  and using the induced metric, we develop a new optimiser and compare it to existing
  methods, namely: SGD, Adam, AdamW, and Muon, across a range of tasks and architectures.
  Empirically, we conclude that this new class of optimisers is highly effective in
  low dimensional examples, and provides slight improvement over state-of-the-art
  methods for training neural networks. These new optimisers have theoretically desirable
  properties. In particular, the effective learning rate is automatically decreased
  in regions of high curvature acting as a smoothed out form of gradient clipping.
  Similarly, one variant of these optimisers can also be viewed as inducing an effective
  scheduled learning rate and decoupled weight decay is the natural choice from our
  geometric perspective. The basic method can be used to modify any existing preconditioning
  method. The new optimiser has a computational complexity comparable to that of Adam.'
arxivId: '2509.03594'
arxivUrl: https://arxiv.org/abs/2509.03594
authors:
- Thomas R. Harvey
concepts:
- induced riemannian metric
- geometric deep learning
- loss landscape geometry
- curvature-adaptive steps
- loss function design
- scalability
- transformers
- convolutional networks
- hamiltonian systems
- regression
- classification
- lagrangian methods
figures:
- /iaifi-research-blog/figures/2509_03594/figure_1.png
- /iaifi-research-blog/figures/2509_03594/figure_2.png
- /iaifi-research-blog/figures/2509_03594/figure_3.png
pdfUrl: https://arxiv.org/pdf/2509.03594v1
published: '2025-09-03T18:00:33+00:00'
theme: Foundational AI
title: 'The Optimiser Hidden in Plain Sight: Training with the Loss Landscape''s Induced
  Metric'
wordCount: 1096
---

## The Big Picture

Picture a hiker trying to find the lowest valley in a vast, fog-covered mountain range. She can only feel the slope beneath her feet, so she steps in whichever direction tilts downward the steepest. That's **gradient descent**, the engine behind virtually every neural network trained today. But here's the catch: the map she draws and the steps she takes are geometrically inconsistent. When she sketches the terrain, she naturally captures hills and curves. When she moves, she ignores them entirely.

That disconnect is the puzzle Thomas Harvey at MIT's IAIFI set out to close. Researchers have been drawing **loss landscapes** (those swooping, curved surfaces showing how a neural network's errors change as its parameters are adjusted) for decades. Those visualizations implicitly encode a specific geometric structure: a way of measuring distances that accounts for terrain curvature. Yet no one had ever used that geometry to build an **optimizer**, the algorithm that actually adjusts the parameters during training. The curvature was hiding in plain sight.

Harvey's new work takes that visualization geometry seriously as a mathematical object, derives the optimizer it implies, and shows the result is competitive with, and often better than, modern methods like Adam, AdamW, and Muon.

> The same geometric structure researchers use to *visualize* loss landscapes has never been used to *navigate* them, until now. Treating it as a real mathematical measure of curvature yields an optimizer with automatic curvature adaptation and natural connections to gradient clipping, learning rate scheduling, and weight decay.

## How It Works

The technical core rests on **Riemannian geometry**, the mathematics of curved spaces and the same framework Einstein used to describe gravity. When you embed the loss landscape as a surface in a higher-dimensional space, that embedding automatically defines an **induced metric**: a precise way of measuring how far apart two points really are, accounting for the terrain's curvature.

Harvey's key move is to take that induced metric and use it directly in the equation governing how parameters change during training. Standard gradient descent moves parameters in proportion to the raw gradient. With a metric, you instead apply a transformation that warps the step direction to respect local geometry, stretching or shrinking steps based on how curved the terrain is. This is **gradient preconditioning**, and it's exactly what Adam and its relatives already do, just with metrics chosen for numerical convenience rather than geometric principle.

![Figure 1](/iaifi-research-blog/figures/2509_03594/figure_1.png)

The specific metric Harvey derives depends on a choice of **embedding function**, a formula for how you transform the loss value when lifting it into the higher-dimensional space. Two natural choices emerge:

- **Square-root embedding** (*f(L) = √L*): Produces an optimizer that behaves like smoothed gradient clipping. In high-curvature regions where gradients can explode, the effective learning rate automatically shrinks; in flat regions, it stays large.
- **Logarithmic embedding** (*f(L) = log L*): Additionally induces a natural learning rate schedule, decaying step size as training progresses. Decoupled weight decay, the regularization technique that is the "W" in AdamW, also emerges as the geometrically natural choice.

The computational cost is minimal. Both variants require only a single additional dot product per iteration over vanilla SGD, keeping complexity at O(N), the same as Adam. That's a sharp contrast to second-order methods, which require computing or approximating the full **Hessian matrix** (a table of second derivatives capturing how each parameter interacts with every other) and carry prohibitive overhead.

## Why It Matters

Harvey tests the new optimizers across a ladder of problems, from pathological toy functions to large-scale neural networks.

In **low-dimensional optimization**, the log-loss variant was the only optimizer tested that found the global minimum across *all* pathological test functions, strong evidence that the geometric curvature adaptation does exactly what the theory promises.

![Figure 2](/iaifi-research-blog/figures/2509_03594/figure_2.png)

For **neural network training**, the story is more nuanced but still positive. Across MLPs on MNIST, ResNet-18 on CIFAR-10, and transformer models on TinyShakespeare, the RMSprop-preconditioned variant of the new optimizer was the best-performing on average across most tasks. Improvements over Adam and AdamW are modest but consistent.

One result worth noting: the framework is modular. The induced metric correction can be applied on top of *any* existing preconditioning method, including Muon. The geometric insight isn't locked to one algorithm; it's a wrapper that can upgrade existing tools.

![Figure 3](/iaifi-research-blog/figures/2509_03594/figure_3.png)

The practical improvements are incremental rather than revolutionary. Harvey is careful to say as much. But the deeper value is conceptual. The field has accumulated a collection of empirical tricks: gradient clipping to prevent explosions, learning rate schedules to manage convergence, decoupled weight decay to separate regularization from momentum. Each was developed independently, justified by its own ad-hoc rationale.

This paper shows all three fall out naturally from a single geometric principle. That kind of unification is exactly what theoretical physics prizes: not just a new tool, but a cleaner picture of why existing tools work. If the induced metric is really the right geometry for loss landscapes, it opens a systematic research program. What other optimizer behaviors emerge from this framework? What happens with different embedding functions? Can the geometry extend to non-Euclidean parameter spaces?

The connection to physics runs deeper than analogy. The mathematics of Riemannian geometry underlies general relativity; the same tools for describing curved spacetime now appear at the heart of neural network optimization. IAIFI, sitting at precisely the intersection of AI and fundamental physics, is a natural home for this kind of work.

> By taking the geometry of loss landscape visualizations seriously as mathematics, Harvey derives a new family of optimizers that automatically adapt to curvature, unify gradient clipping, learning rate scheduling, and weight decay under one roof, and match or beat state-of-the-art methods, all at Adam-level computational cost.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies Riemannian differential geometry (the mathematical language of curved spacetime in general relativity) directly to neural network optimization, demonstrating a productive exchange of tools between fundamental physics and machine learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The new optimizers achieve competitive or superior performance versus SGD, Adam, AdamW, and Muon across diverse architectures and tasks, while providing a unifying geometric explanation for gradient clipping, learning rate scheduling, and decoupled weight decay.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The geometric framework formalizes the intuition behind loss landscape visualization, connecting physical notions of curvature and induced metrics to the practical problem of training the AI systems used in fundamental physics research.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may explore alternative embedding functions, hybrid geometric-preconditioning schemes, and extensions to non-Euclidean parameter spaces; the paper and code are available at [arXiv:2509.03594](https://arxiv.org/abs/2509.03594) and [github.com/harveyThomas4692/Induced-Metric-Optimiser](https://github.com/harveyThomas4692/Induced-Metric-Optimiser).</span></div></div>
</div>
