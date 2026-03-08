---
abstract: Physical data are representations of the fundamental laws governing the
  Universe, hiding complex compositional structures often well captured by hierarchical
  graphs. Hyperbolic spaces are endowed with a non-Euclidean geometry that naturally
  embeds those structures. To leverage the benefits of non-Euclidean geometries in
  representing natural data we develop machine learning on $\mathcal P \mathcal M$
  spaces, Cartesian products of constant curvature Riemannian manifolds. As a use
  case we consider the classification of "jets", sprays of hadrons and other subatomic
  particles produced by the hadronization of quarks and gluons in collider experiments.
  We compare the performance of $\mathcal P \mathcal M$-MLP and $\mathcal P \mathcal
  M$-Transformer models across several possible representations. Our experiments show
  that $\mathcal P \mathcal M$ representations generally perform equal or better to
  fully Euclidean models of similar size, with the most significant gains found for
  highly hierarchical jets and small models. We discover significant correlation between
  the degree of hierarchical structure at a per-jet level and classification performance
  with the $\mathcal P \mathcal M$-Transformer in top tagging benchmarks. This is
  a promising result highlighting a potential direction for further improving machine
  learning model performance through tailoring geometric representation at a per-sample
  level in hierarchical datasets. These results reinforce the view of geometric representation
  as a key parameter in maximizing both performance and efficiency of machine learning
  on natural data.
arxivId: '2412.07033'
arxivUrl: https://arxiv.org/abs/2412.07033
authors:
- Nathaniel S. Woodward
- Sang Eon Park
- Gaia Grosso
- Jeffrey Krupa
- Philip Harris
concepts:
- product manifold spaces
- manifold learning
- geometric deep learning
- jet physics
- hyperbolic embeddings
- representation learning
- transformers
- embeddings
- gromov-delta hyperbolicity
- classification
- collider physics
- equivariant neural networks
figures:
- /iaifi-research-blog/figures/2412_07033/figure_1.png
- /iaifi-research-blog/figures/2412_07033/figure_1.png
- /iaifi-research-blog/figures/2412_07033/figure_2.png
- /iaifi-research-blog/figures/2412_07033/figure_2.png
- /iaifi-research-blog/figures/2412_07033/figure_3.png
- /iaifi-research-blog/figures/2412_07033/figure_3.png
pdfUrl: https://arxiv.org/pdf/2412.07033v1
published: '2024-12-09T22:45:27+00:00'
theme: Experimental Physics
title: Product Manifold Machine Learning for Physics
wordCount: 995
---

## The Big Picture

Imagine trying to draw a family tree on a flat piece of paper. The further back you go, the more ancestors you have, and branches multiply exponentially. Sooner or later, the page runs out of room. This is essentially the problem physicists face when teaching machines to understand particle jets: the geometry of the data doesn't fit the geometry of the math.

When a quark or gluon is knocked loose in a collider like the Large Hadron Collider, it doesn't travel alone. It breaks apart in a chain reaction — splitting into daughter particles, which split again and again — producing a tightly-focused spray of hundreds of particles called a **jet**.

This process is deeply hierarchical, like a family tree written in subatomic ink. Standard machine learning operates in flat, **Euclidean space** — the ordinary geometry of straight lines and right angles — which struggles to represent branching, tree-like data. There's a fundamental mismatch between the shape of the physics and the shape of the math.

A team from MIT's Laboratory for Nuclear Science and IAIFI decided to fix that mismatch at its root. Rather than forcing jet data into flat geometry, they built models that operate on curved spaces tailored to the data's natural shape — and found that matching geometry to structure pays real dividends.

> **Key Insight:** By embedding jet data in curved, non-Euclidean spaces that naturally accommodate hierarchical structure, this work achieves better classification performance with smaller models — especially for the most complex, deeply branching jets.

## How It Works

The central concept is the **product manifold (PM) space**: a combination of several constant-curvature geometric spaces, mixed and matched to represent different aspects of the data. Think of it as blending a saddle-shaped surface (hyperbolic space, which expands exponentially and naturally fits tree-like data), a flat plane (Euclidean space, efficient for local structure), and a sphere (positive curvature, suited to cyclic relationships). Each component handles different features of the jet.

The key ingredient is **hyperbolic space** — a non-Euclidean geometry where available "room" grows exponentially with distance from any point. This mirrors precisely how a branching tree grows: at each level, the number of branches multiplies. Fitting a deep tree into flat space requires enormous distortion; hyperbolic space accommodates it almost naturally.

The researchers formalize this using **Gromov-δ hyperbolicity** — a mathematical measure of how tree-like a data structure actually is. Small δ means highly tree-like; large δ means more tangled and complex.

![Figure 1](/iaifi-research-blog/figures/2412_07033/figure_1.png)

The team built two architectures adapted to operate natively in curved spaces:

- **PM-MLP**: A multilayer perceptron — a standard neural network — where each layer's operations are generalized to product manifolds, using non-Euclidean analogs of addition, distance, and aggregation.
- **PM-Transformer**: A transformer architecture — the same family behind large language models like ChatGPT — extended to operate on product manifold representations. It processes each particle individually, then aggregates into a jet-level representation.

Both architectures were benchmarked on **JetClass**, a large-scale dataset of simulated jets across ten classes including top quarks, Higgs bosons decaying to quark pairs, and simple quark/gluon jets. The researchers systematically tested different PM combinations — pure Euclidean, pure hyperbolic, mixed, and spherical — to find which geometry worked best for which jet type.

![Figure 2](/iaifi-research-blog/figures/2412_07033/figure_1.png)

The results are striking: PM representations matched or outperformed Euclidean models of similar parameter count, with the largest gains appearing for the most hierarchical jet types and for small models. Under computational constraints, curved space does more work with fewer parameters.

## Why It Matters

The most exciting finding isn't that PM spaces help on average — it's *when* they help. The researchers measured the Gromov-δ hyperbolicity of individual jets and found a statistically significant correlation: jets with lower δ (more tree-like, more hierarchical) are classified more accurately by the PM-Transformer than by its Euclidean counterpart. The geometry of the model and the geometry of the data are genuinely aligned.

![Figure 3](/iaifi-research-blog/figures/2412_07033/figure_2.png)

This opens a provocative door. If the benefit of non-Euclidean geometry tracks the actual hierarchical structure of individual data points, future models might adapt their geometry *on the fly* — choosing or weighting different manifold components based on how tree-like each jet is. That would be a fundamentally new kind of inductive bias: not just architecture or training data, but *the shape of the mathematical space itself* as a tunable parameter per input.

The implications extend well beyond particle physics. Biological data — protein interaction networks, evolutionary trees, neural connectomes — is also deeply hierarchical. Social networks. Language structures. Any domain where data naturally branches and stratifies could benefit from this geometric matching approach. IAIFI researchers have demonstrated a proof-of-concept in one of physics' hardest classification problems; the framework is general.

![Figure 4](/iaifi-research-blog/figures/2412_07033/figure_2.png)

> **Bottom Line:** Matching the geometry of a machine learning model to the hierarchical geometry of physical data isn't just mathematically elegant — it measurably improves performance, and the improvement is largest exactly where it matters most: deeply branching jets and tight computational budgets.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges differential geometry and deep learning with experimental particle physics, showing that mathematical structure from Riemannian manifold theory translates into concrete performance gains on one of collider physics' central classification challenges.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The PM-Transformer demonstrates that transformer architectures can be rigorously extended to non-Euclidean product manifolds without sacrificing generality — opening a framework applicable to any hierarchical dataset, from particle jets to biological networks.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Better jet classification directly improves sensitivity in searches for new physics at the LHC, including Higgs boson measurements and dark matter production signals, by more accurately distinguishing signal jets from QCD background.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The per-sample correlation between classification accuracy and Gromov-δ hyperbolicity motivates future adaptive-geometry models that tune their manifold representation per input; the full paper is available on arXiv and was produced by researchers at MIT, Harvard, and SLAC affiliated with the NSF IAIFI institute.</span></div></div>
</div>
