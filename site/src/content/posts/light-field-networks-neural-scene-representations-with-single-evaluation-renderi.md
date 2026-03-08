---
abstract: Inferring representations of 3D scenes from 2D observations is a fundamental
  problem of computer graphics, computer vision, and artificial intelligence. Emerging
  3D-structured neural scene representations are a promising approach to 3D scene
  understanding. In this work, we propose a novel neural scene representation, Light
  Field Networks or LFNs, which represent both geometry and appearance of the underlying
  3D scene in a 360-degree, four-dimensional light field parameterized via a neural
  implicit representation. Rendering a ray from an LFN requires only a single network
  evaluation, as opposed to hundreds of evaluations per ray for ray-marching or volumetric
  based renderers in 3D-structured neural scene representations. In the setting of
  simple scenes, we leverage meta-learning to learn a prior over LFNs that enables
  multi-view consistent light field reconstruction from as little as a single image
  observation. This results in dramatic reductions in time and memory complexity,
  and enables real-time rendering. The cost of storing a 360-degree light field via
  an LFN is two orders of magnitude lower than conventional methods such as the Lumigraph.
  Utilizing the analytical differentiability of neural implicit representations and
  a novel parameterization of light space, we further demonstrate the extraction of
  sparse depth maps from LFNs.
arxivId: '2106.02634'
arxivUrl: https://arxiv.org/abs/2106.02634
authors:
- Vincent Sitzmann
- Semon Rezchikov
- William T. Freeman
- Joshua B. Tenenbaum
- Fredo Durand
concepts:
- light field networks
- representation learning
- neural operators
- meta-learning prior
- inverse problems
- scalability
- plücker ray parameterization
- generative models
- embeddings
- surrogate modeling
- semi-supervised learning
figures:
- /iaifi-research-blog/figures/2106_02634/figure_1.png
- /iaifi-research-blog/figures/2106_02634/figure_1.png
- /iaifi-research-blog/figures/2106_02634/figure_2.png
- /iaifi-research-blog/figures/2106_02634/figure_2.png
- /iaifi-research-blog/figures/2106_02634/figure_3.png
- /iaifi-research-blog/figures/2106_02634/figure_3.png
pdfUrl: https://arxiv.org/pdf/2106.02634v2
published: '2021-06-04T17:54:49+00:00'
theme: Foundational AI
title: 'Light Field Networks: Neural Scene Representations with Single-Evaluation
  Rendering'
wordCount: 1021
---

## The Big Picture

Imagine trying to memorize what a room looks like. One approach: memorize the color and texture of every surface at every point in 3D space. Another: memorize exactly what color of light travels along every possible line of sight.

The second approach might seem strange, but it's exactly how your eyes work — light rays, not surface points, are what reach your retina. For computers rendering 3D scenes, this shift in perspective can make things thousands of times faster.

Rendering photorealistic 3D scenes from neural networks has become one of the hottest problems in computer vision. Systems like **NeRF (Neural Radiance Fields)** can reconstruct stunning scenes from a handful of photos. But they come with a brutal cost: a single 256×256 image can take tens of seconds to render, because the system must query a neural network hundreds of times per pixel, marching step-by-step through 3D space to compute what each ray of light hits. Real-time rendering — the kind needed for video games, augmented and virtual reality, or interactive visualization — is essentially impossible.

Researchers at MIT CSAIL and Columbia University have found a way to sidestep this bottleneck entirely. Their method, **Light Field Networks (LFNs)**, encodes an entire 3D scene not as a volume but as a four-dimensional function over light rays — and renders each ray with exactly one calculation, delivering real-time performance at a fraction of the memory cost.

> **Key Insight:** Instead of asking "what's at each point in 3D space?", Light Field Networks ask "what color does each possible camera ray see?" — collapsing hundreds of compute steps into one.

## How It Works

The foundation is a classical concept from optics: the **light field**, or plenoptic function. A light field describes the color of every ray of light traveling in every direction through space. For a scene in free space, this is a four-dimensional function — two parameters to locate a point, two more to specify direction. If you know the light field, you can render any view instantly, just by looking up the ray corresponding to each pixel.

An LFN represents this function with a single neural network. Given any camera ray as input, the network outputs the color that ray would observe. No marching, no iterative surface-finding — just input ray → output pixel color.

The key engineering challenge is how to *parameterize* rays. The authors chose **Plücker coordinates**, a 6-dimensional representation of 3D lines borrowed from classical geometry. Although technically over-parameterizing a 4D space, Plücker coordinates handle any ray direction, including full 360-degree coverage, without the mathematical breakdowns and gaps that plague simpler two-plane parameterizations.

Light fields aren't inherently multi-view consistent — different rays hitting the same 3D point could be assigned different colors independently. To enforce consistency, the researchers embed LFNs in a **meta-learning** framework, a technique where a system learns from many examples how to quickly adapt to new ones:

1. During training, the system sees many different 3D scenes
2. It learns a prior — a sense of what valid, physically plausible light fields look like — as a compressed recipe space for generating them
3. At inference time, given even a single photograph, the system rapidly optimizes a **latent code** — a compact numerical summary — that produces an LFN consistent with that observation
4. The resulting network renders the scene from any viewpoint, in real time

![Figure 1](/iaifi-research-blog/figures/2106_02634/figure_1.png)

The meta-learning step is what enforces consistency. The prior encodes physical regularities — coherent object shapes, predictable light behavior — so the reconstructed light field generalizes to unseen viewpoints rather than memorizing the training image.

![Figure 2](/iaifi-research-blog/figures/2106_02634/figure_1.png)

## Why It Matters

The numbers are striking. Compared to volumetric renderers like NeRF, LFNs are roughly **three orders of magnitude faster** per ray at test time. Storing a 360-degree light field as an LFN requires **two orders of magnitude less memory** than the Lumigraph — an early approach that stored complete light fields as dense data tables. Reconstruction from a single image, which takes NeRF-style approaches multiple GPU-hours, happens in seconds.

![Figure 3](/iaifi-research-blog/figures/2106_02634/figure_2.png)

There's also something deeper here. Geometry isn't lost just because explicit 3D structure has been abandoned. By taking the *analytical derivative* of the LFN with respect to its inputs — asking how predicted color changes as you nudge a ray by a tiny amount — the system extracts sparse depth maps and recovers surface location.

This exploits a unique property of **neural implicit representations** — neural networks used to encode continuous functions like surfaces or fields — which are smoothly differentiable at every point. You can ask calculus questions of them that are impossible with discrete 3D pixel grids (voxels) or point clouds.

The immediate applications are generating views from angles never photographed and 3D reconstruction for simple scenes. But the framework points toward a broader principle: the right choice of *representation space* can be just as important as network architecture. Encoding scenes in ray space rather than object space unlocks a fundamentally different computational profile — one better matched to the task of rendering.

> **Bottom Line:** Light Field Networks achieve real-time 3D rendering by encoding scenes as neural functions over light rays rather than 3D volumes, cutting rendering time by 1000× and memory by 100× while enabling single-image scene reconstruction.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies classical optics — the plenoptic function and Plücker line coordinates from projective geometry — as the mathematical backbone for a modern deep learning architecture, exemplifying how physics-grounded representations can reshape AI methodology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">LFNs demonstrate that representation space choice can yield order-of-magnitude computational gains over architecture tuning alone, with broad implications for neural rendering and implicit scene understanding.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By recovering scene geometry through analytical differentiation of a neural field — without explicit 3D supervision — this work advances differentiable physics-based reasoning, with relevance to simulation and inverse problems across science.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include scaling LFNs to complex real-world scenes and combining them with local feature conditioning; the paper appeared at NeurIPS 2021 and is available on arXiv.</span></div></div>
</div>
