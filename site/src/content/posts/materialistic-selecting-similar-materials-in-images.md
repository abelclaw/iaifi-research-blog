---
abstract: Separating an image into meaningful underlying components is a crucial first
  step for both editing and understanding images. We present a method capable of selecting
  the regions of a photograph exhibiting the same material as an artist-chosen area.
  Our proposed approach is robust to shading, specular highlights, and cast shadows,
  enabling selection in real images. As we do not rely on semantic segmentation (different
  woods or metal should not be selected together), we formulate the problem as a similarity-based
  grouping problem based on a user-provided image location. In particular, we propose
  to leverage the unsupervised DINO features coupled with a proposed Cross-Similarity
  module and an MLP head to extract material similarities in an image. We train our
  model on a new synthetic image dataset, that we release. We show that our method
  generalizes well to real-world images. We carefully analyze our model's behavior
  on varying material properties and lighting. Additionally, we evaluate it against
  a hand-annotated benchmark of 50 real photographs. We further demonstrate our model
  on a set of applications, including material editing, in-video selection, and retrieval
  of object photographs with similar materials.
arxivId: '2305.13291'
arxivUrl: https://arxiv.org/abs/2305.13291
authors:
- Prafull Sharma
- Julien Philip
- Michaël Gharbi
- William T. Freeman
- Fredo Durand
- Valentin Deschaintre
concepts:
- cross-similarity feature weighting
- representation learning
- self-supervised learning
- feature extraction
- cross-image material similarity
- transformers
- embeddings
- synthetic-to-real generalization
- attention mechanisms
- transfer learning
- contrastive learning
- inverse problems
figures:
- /iaifi-research-blog/figures/2305_13291/figure_1.png
- /iaifi-research-blog/figures/2305_13291/figure_1.png
- /iaifi-research-blog/figures/2305_13291/figure_2.png
- /iaifi-research-blog/figures/2305_13291/figure_2.png
- /iaifi-research-blog/figures/2305_13291/figure_3.png
- /iaifi-research-blog/figures/2305_13291/figure_3.png
pdfUrl: https://arxiv.org/pdf/2305.13291v1
published: '2023-05-22T17:50:48+00:00'
theme: Foundational AI
title: 'Materialistic: Selecting Similar Materials in Images'
wordCount: 953
---

## The Big Picture

Imagine walking into a furniture store and pointing to a chair, asking the salesperson to find everything else made from the same wood. You wouldn't be confused by different lighting, the sheen of varnish, or a lamp's shadow. You'd just *know* — that table shares the same grain. For decades, computer vision researchers have been trying to teach machines to do the same thing. It turns out to be remarkably hard.

The challenge isn't recognizing a material category like "wood" or "metal." It's recognizing *this specific wood* — with its grain, color, and reflective character — versus *that other wood* across the room, while ignoring how dramatically lighting changes a surface's appearance. Shading, specular highlights, and cast shadows transform how a material looks without changing what it is. Standard color-picking tools and AI labeling systems fail under these conditions.

**Materialistic**, developed by researchers at MIT and Adobe Research, takes on this challenge by rethinking the problem from the ground up.

> **Key Insight:** By framing material selection as a *similarity* problem rather than a *classification* problem, Materialistic identifies matching materials without being fooled by lighting effects — and generalizes to real photographs despite training entirely on synthetic scenes.

## How It Works

The core design decision is philosophical: don't classify materials into fixed buckets. Traditional segmentation systems label pixels as "wood," "metal," or "fabric," but coarse labels can't distinguish two different woods in the same scene. Materialistic asks instead: given a user-clicked pixel, which other pixels are made of the *same stuff*?

To answer this, the system builds on **DINO** (self-distillation with no labels), a pretrained visual model that learns to recognize meaningful structure in image patches without human annotation. Raw DINO features mix color, texture, shape, and object type together. Materialistic adds a specialized layer on top.

![Figure 1](/iaifi-research-blog/figures/2305_13291/figure_1.png)

The pipeline works in three steps:

1. **Feature extraction**: DINO processes the image at multiple scales, producing compact numerical summaries for each image region.
2. **Cross-Similarity Feature Weighting**: A novel module takes the query pixel's summary and reweights features across the entire image — asking which properties elsewhere are most diagnostic for matching the query. This operates at multiple resolutions simultaneously.
3. **MLP scoring head**: A lightweight multilayer perceptron takes the modulated, multi-scale summaries and outputs a per-pixel similarity heatmap indicating which regions share the same material.

Training data posed its own challenge. Real photographs rarely carry per-pixel material identity labels. To sidestep this, the team built a synthetic dataset of 50,000 physically rendered images from 100 indoor scenes using 16,000 **physically-based materials**. A physics-based light simulator ensured that shading, reflections, and shadows behave realistically — providing ground-truth labels while exposing the model to the full complexity of light interacting with surfaces.

![Figure 2](/iaifi-research-blog/figures/2305_13291/figure_1.png)

The striking result: despite training only on synthetic indoor scenes, the model generalizes to real-world photographs, including outdoor images with entirely different lighting and materials. This **synthetic-to-real transfer** suggests the Cross-Similarity module is learning genuine material identity rather than overfitting to rendering artifacts.

Evaluation used a hand-annotated benchmark of 50 real photographs — assembled precisely because no ground-truth material selection benchmark previously existed. Controlled ablation studies systematically varied lighting angle, material glossiness, query pixel location, and image resolution to isolate each component's contribution.

## Why It Matters

Material selection sounds niche, but it unlocks a broad set of downstream capabilities. The paper demonstrates material editing and replacement (change all the upholstery in a scene at once), in-video selection (identify a material in one frame and track it across subsequent frames), and image retrieval (find product photographs containing objects made from a specific material). Each has clear applications in e-commerce, digital content creation, architectural visualization, and film production.

![Figure 3](/iaifi-research-blog/figures/2305_13291/figure_2.png)

More fundamentally, Materialistic contributes to a long-standing computer vision goal: decomposing images into physical constituents. An image isn't just a pixel grid — it's the result of geometry, illumination, and materials interacting through the physics of light. Systems that disentangle these components advance **inverse rendering** (inferring 3D scene properties from 2D photos), physically accurate image synthesis, and AI that reasons about the world in terms of physical properties rather than surface statistics.

Open questions remain. The method operates at the patch level, limiting spatial precision at fine material boundaries. Highly transparent or translucent materials — where light behavior is especially complex — remain challenging. And while synthetic-to-real generalization works impressively here, further work could explore whether AI-generated image augmentation could close the domain gap further on difficult real-world cases.

> **Bottom Line:** Materialistic proves that material identity can be extracted from photographs robustly and without semantic labels, using a query-driven similarity architecture over self-supervised features — a meaningful step toward AI that understands the physical world, not just its appearance.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges computer graphics and machine learning by using physically-based rendering to generate training data for a visual AI system, combining light transport physics with self-supervised deep learning to solve a problem neither field could tackle alone.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The Cross-Similarity Feature Weighting module demonstrates a principled way to condition patch-level visual features on a user query, enabling open-vocabulary similarity tasks that go beyond fixed-class classification — a design pattern with broad applicability across visual computing.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By learning to separate material identity from illumination, Materialistic advances the scientific goal of inverse rendering: recovering physical scene parameters — geometry, materials, and lights — from raw image data, a key problem in physically-grounded computer vision.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include finer spatial resolution, improved handling of transparent materials, and integration with full inverse rendering pipelines; the work and synthetic dataset are publicly released (ACM Trans. Graph. 42, 4, 2023).</span></div></div>
</div>
