---
abstract: The geometry of 4-string contact interaction of closed string field theory
  is characterized using machine learning. We obtain Strebel quadratic differentials
  on 4-punctured spheres as a neural network by performing unsupervised learning with
  a custom-built loss function. This allows us to solve for local coordinates and
  compute their associated mapping radii numerically. We also train a neural network
  distinguishing vertex from Feynman region. As a check, 4-tachyon contact term in
  the tachyon potential is computed and a good agreement with the results in the literature
  is observed. We argue that our algorithm is manifestly independent of number of
  punctures and scaling it to characterize the geometry of $n$-string contact interaction
  is feasible.
arxivId: '2211.09129'
arxivUrl: https://arxiv.org/abs/2211.09129
authors:
- Harold Erbin
- Atakan Hilmi Fırat
concepts:
- string theory
- strebel quadratic differentials
- physics-informed neural networks
- loss function design
- quantum field theory
- string vertex region
- regression
- classification
- surrogate modeling
- inverse problems
- scalability
- tachyon potential
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2211_09129/figure_1.png
- /iaifi-research-blog/figures/2211_09129/figure_1.png
- /iaifi-research-blog/figures/2211_09129/figure_2.png
- /iaifi-research-blog/figures/2211_09129/figure_2.png
- /iaifi-research-blog/figures/2211_09129/figure_3.png
- /iaifi-research-blog/figures/2211_09129/figure_3.png
pdfUrl: https://arxiv.org/pdf/2211.09129v1
published: '2022-11-16T19:00:00+00:00'
theme: Theoretical Physics
title: Characterizing 4-string contact interaction using machine learning
wordCount: 1060
---

## The Big Picture

Imagine trying to understand how four rubber bands interact when they touch — except instead of rubber bands, you're dealing with the fundamental objects of the universe, undergoing quantum interactions described by equations so complex that even supercomputers struggle with them. That's the challenge researchers face when computing **string contact interactions** in closed string field theory. For decades, the math has fought back.

**Closed string field theory** (CSFT) describes how closed strings — the one-dimensional loops that form the alphabet of string theory — interact, collide, and exchange energy. It is one of the most mathematically elaborate frameworks in physics.

To compute anything useful in CSFT, physicists need to work out the precise geometry of how strings merge and split. For four strings interacting at once, classical numerical methods can just barely manage. For six or more, the problem becomes essentially intractable.

Now, researchers Harold Erbin and Atakan Hilmi Fırat at MIT's Center for Theoretical Physics have found a way through: train a neural network to do it. Their algorithm solves the geometric problem for four-string interactions and, crucially, is designed to scale to any number of strings.

> **Key Insight:** By representing a notoriously difficult geometric object — the Strebel quadratic differential — as a neural network trained with a custom loss function, the researchers sidestep the combinatorial complexity that has blocked progress in closed string field theory for decades.

## How It Works

At the heart of the problem lies an object called a **Strebel quadratic differential**: a special mathematical function defined on a sphere with punctures — holes, one per string. Think of it as a map assigning a "flow direction" to every point on the sphere, with punctures acting like sources and sinks. Getting this map right is what allows physicists to compute string amplitudes. But finding it requires knowing the **critical graph** — the network of special paths connecting punctures — which you can only determine once you already have the Strebel differential. A classic chicken-and-egg problem.

Classical approaches like Newton's method sidestep this for simple cases by guessing the critical graph topology. As the number of punctures grows, the number of possible topologies explodes, and the approach breaks down.

The key innovation is a **loss function** — the quantity a neural network minimizes during training — that requires no prior knowledge of the critical graph. The team defined the **complex length** of a path: an integral measuring how "Strebel-like" a quadratic differential is along any trajectory. When a differential is truly Strebel, all non-contractible paths on the punctured sphere have imaginary part exactly 2π. The loss function penalizes deviations from this condition, driving training toward the correct solution.

The workflow breaks into three steps:

1. **Train the accessory parameter network.** The Strebel differential on a 4-punctured sphere depends on a single unknown constant — the **accessory parameter** — for each arrangement of punctures. A small neural network learns to output this number directly from the puncture coordinates, bypassing iterative root-finding.

2. **Extract local coordinates and mapping radii.** Once the Strebel differential is known, the researchers expand it around each puncture to find the **local coordinates** — the precise way to "zoom in" on each string interaction point. The associated **mapping radii**, which set the physical size of each interaction region, come from numerically evaluating a specific integral.

3. **Train the indicator function network.** Not every arrangement of four punctures corresponds to a genuine string contact interaction. Some belong to **Feynman regions** — diagrams that can be built from simpler lower-order interactions and shouldn't be double-counted. A second neural network learns the **indicator function** Θ₀,₄: a binary classifier that outputs 1 for configurations in the **vertex region** (a true contact interaction) and 0 otherwise.

![Figure 1](/iaifi-research-blog/figures/2211_09129/figure_1.png)

This classifier replaces an explicit geometric description of the vertex region with a trainable function — one that can be retrained for any number of punctures.

![Figure 3](/iaifi-research-blog/figures/2211_09129/figure_2.png)

As a validation, the team computed the **4-tachyon contact term** in the tachyon potential — a benchmark involving an unstable particle-like state called a *tachyon*, previously calculated by Nicolas Moeller using classical methods. Their result agreed well with the literature.

## Why It Matters

The deeper significance extends well beyond four strings. The entire algorithm is **manifestly independent of the number of punctures**. The same framework — custom loss function, accessory parameter network, indicator function — applies in principle to six, seven, or arbitrarily many punctured spheres. This is precisely the regime where classical methods fail and where progress in CSFT has stalled.

Computing interactions on higher-punctured spheres would unlock higher-order terms in the tachyon potential, potentially answering one of the most tantalizing open questions in string theory: does bosonic closed string tachyon condensation produce a stable vacuum? The answer may require sextic-order terms and beyond — exactly where this algorithm is headed next.

There's also a broader message for computational physics. Unsupervised learning with a physics-motivated loss function can solve problems in complex analysis and differential geometry that defeat conventional numerics. The same design philosophy — encode the constraint directly into the loss, train without labels, scale by construction — could find applications well outside string theory.

> **Bottom Line:** A neural network trained with a graph-agnostic loss function can solve the geometry of string contact interactions — and unlike every previous approach, it's built to scale to as many strings as needed.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly fuses deep learning methodology with one of the most mathematically demanding areas of theoretical physics, using neural networks to solve a geometric problem in closed string field theory that has resisted classical methods for over two decades.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper demonstrates that unsupervised learning with a physics-motivated loss function can perform non-parametric regression on complex mathematical objects — a technique applicable to a broad class of computational problems in mathematics and physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By providing a scalable algorithm for computing Strebel differentials and vertex regions for n-punctured spheres, this work opens a concrete path toward higher-order terms in the closed string tachyon potential and a deeper understanding of tachyon condensation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The authors plan to extend the algorithm to six- and higher-punctured spheres, with the longer-term goal of resolving the closed string tachyon vacuum problem; the paper is available at arXiv:2211.09563.</span></div></div>
</div>
