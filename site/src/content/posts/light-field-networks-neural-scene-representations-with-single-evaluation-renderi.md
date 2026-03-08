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
wordCount: 1239
---

## The Big Picture

Imagine trying to memorize what a room looks like. One approach: memorize the color and texture of every surface at every point in 3D space. Another: memorize exactly what color of light travels along every possible line of sight.

The second approach might seem strange, but it's exactly how your eyes work. Light rays, not surface points, are what reach your retina. For computers rendering 3D scenes, this shift in perspective can make things thousands of times faster.

Rendering photorealistic 3D scenes from neural networks has become one of the hottest problems in computer vision. Systems like **NeRF (Neural Radiance Fields)** can reconstruct impressive scenes from a handful of photos, but the cost is brutal. A single 256×256 image can take tens of seconds to render because the system must query a neural network hundreds of times per pixel, marching step by step through 3D space to figure out what each ray of light hits. Real-time rendering, the kind needed for video games, AR/VR, or interactive visualization, is essentially off the table.

Researchers at MIT CSAIL and Columbia University found a way to sidestep this bottleneck entirely. Their method, **Light Field Networks (LFNs)**, encodes an entire 3D scene not as a volume but as a four-dimensional function over light rays. Each ray gets rendered with exactly one network evaluation, delivering real-time performance at a fraction of the memory cost.

> **Key Insight:** Instead of asking "what's at each point in 3D space?", Light Field Networks ask "what color does each possible camera ray see?", collapsing hundreds of compute steps into one.

## How It Works

The foundation is a classical concept from optics: the **light field**, or plenoptic function. A light field describes the color of every ray of light traveling in every direction through space. For a scene in free space, this is a four-dimensional function: two parameters to locate a point, two more to specify direction. If you know the light field, you can render any view instantly by looking up the ray corresponding to each pixel.

An LFN represents this function with a single neural network. Given any camera ray as input, the network outputs the color that ray would observe. No marching, no iterative surface-finding. Input ray, output pixel color.

The main engineering challenge is how to *parameterize* rays. The authors chose **Plücker coordinates**, a 6-dimensional representation of 3D lines from classical geometry. This technically over-parameterizes a 4D space, but Plücker coordinates handle any ray direction, including full 360-degree coverage, without the mathematical breakdowns that plague simpler two-plane parameterizations.

Light fields aren't inherently multi-view consistent. Different rays hitting the same 3D point could be assigned different colors independently, and nothing in the raw formulation prevents that. To enforce consistency, the researchers embed LFNs in a **meta-learning** framework (a technique where a system learns from many examples how to quickly adapt to new ones):

1. During training, the system sees many different 3D scenes
2. It learns a prior, a sense of what valid, physically plausible light fields look like, encoded as a compressed recipe space for generating them
3. At inference time, given even a single photograph, the system rapidly optimizes a **latent code** (a compact numerical summary) that produces an LFN consistent with that observation
4. The resulting network renders the scene from any viewpoint, in real time

![Figure 1](figure:1)

The meta-learning step is what makes consistency work. The prior encodes physical regularities like coherent object shapes and predictable light behavior, so the reconstructed light field generalizes to unseen viewpoints rather than just memorizing the training image.

![Figure 2](figure:2)

## Why It Matters

The performance gains are hard to overstate. Compared to volumetric renderers like NeRF, LFNs are roughly **three orders of magnitude faster** per ray at test time. Storing a 360-degree light field as an LFN takes **two orders of magnitude less memory** than the Lumigraph, an early approach that stored complete light fields as dense data tables. And reconstruction from a single image, which takes NeRF-style methods multiple GPU-hours, happens in seconds.

![Figure 3](figure:3)

Geometry isn't lost just because explicit 3D structure has been dropped, either. By taking the *analytical derivative* of the LFN with respect to its inputs (asking how predicted color changes as you nudge a ray), the system extracts sparse depth maps and recovers surface locations. This works because **neural implicit representations**, neural networks encoding continuous functions like surfaces or fields, are smoothly differentiable everywhere. You can ask calculus questions of them that are impossible with discrete voxel grids or point clouds.

The immediate applications are novel view synthesis and 3D reconstruction for simple scenes. But the result also carries a broader lesson: the right choice of *representation space* can matter just as much as network architecture. Encoding scenes in ray space rather than object space opens up a fundamentally different computational profile, one that fits the rendering problem far more naturally.

> **Bottom Line:** Light Field Networks achieve real-time 3D rendering by encoding scenes as neural functions over light rays rather than 3D volumes, cutting rendering time by 1000× and memory by 100× while enabling single-image scene reconstruction.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work takes classical optics (the plenoptic function and Plücker line coordinates from projective geometry) and uses it as the mathematical backbone for a modern deep learning architecture. It's a clean example of how physics-grounded representations can change what's computationally possible in AI.

- **Impact on Artificial Intelligence:** LFNs show that choosing the right representation space can yield order-of-magnitude computational gains where architecture tuning alone cannot, with broad implications for neural rendering and implicit scene understanding.

- **Impact on Fundamental Interactions:** Recovering scene geometry through analytical differentiation of a neural field, without any explicit 3D supervision, pushes forward the toolkit of differentiable physics-based reasoning. The same ideas apply to simulation and inverse problems across the sciences.

- **Outlook and References:** Open directions include scaling LFNs to complex real-world scenes and combining them with local feature conditioning. The paper appeared at NeurIPS 2021 and is available at [arXiv:2106.02634](https://arxiv.org/abs/2106.02634).

## Original Paper Details
- **Title:** Light Field Networks: Neural Scene Representations with Single-Evaluation Rendering
- **arXiv ID:** [2106.02634](https://arxiv.org/abs/2106.02634)
- **Authors:** ["Vincent Sitzmann", "Semon Rezchikov", "William T. Freeman", "Joshua B. Tenenbaum", "Fredo Durand"]
- **Abstract:** Inferring representations of 3D scenes from 2D observations is a fundamental problem of computer graphics, computer vision, and artificial intelligence. Emerging 3D-structured neural scene representations are a promising approach to 3D scene understanding. In this work, we propose a novel neural scene representation, Light Field Networks or LFNs, which represent both geometry and appearance of the underlying 3D scene in a 360-degree, four-dimensional light field parameterized via a neural implicit representation. Rendering a ray from an LFN requires only a single network evaluation, as opposed to hundreds of evaluations per ray for ray-marching or volumetric based renderers in 3D-structured neural scene representations. In the setting of simple scenes, we leverage meta-learning to learn a prior over LFNs that enables multi-view consistent light field reconstruction from as little as a single image observation. This results in dramatic reductions in time and memory complexity, and enables real-time rendering. The cost of storing a 360-degree light field via an LFN is two orders of magnitude lower than conventional methods such as the Lumigraph. Utilizing the analytical differentiability of neural implicit representations and a novel parameterization of light space, we further demonstrate the extraction of sparse depth maps from LFNs.
