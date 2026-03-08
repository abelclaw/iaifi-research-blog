---
abstract: 'Perceiving the shape and material of an object from a single image is inherently
  ambiguous, especially when lighting is unknown and unconstrained. Despite this,
  humans can often disentangle shape and material, and when they are uncertain, they
  often move their head slightly or rotate the object to help resolve the ambiguities.
  Inspired by this behavior, we introduce a novel conditional denoising-diffusion
  model that generates samples of shape-and-material maps from a short video of an
  object undergoing differential motions. Our parameter-efficient architecture allows
  training directly in pixel-space, and it generates many disentangled attributes
  of an object simultaneously. Trained on a modest number of synthetic object-motion
  videos with supervision on shape and material, the model exhibits compelling emergent
  behavior: For static observations, it produces diverse, multimodal predictions of
  plausible shape-and-material maps that capture the inherent ambiguities; and when
  objects move, the distributions converge to more accurate explanations. The model
  also produces high-quality shape-and-material estimates for less ambiguous, real-world
  objects. By moving beyond single-view to continuous motion observations, and by
  using generative perception to capture visual ambiguities, our work suggests ways
  to improve visual reasoning in physically-embodied systems.'
arxivId: '2506.02473'
arxivUrl: https://arxiv.org/abs/2506.02473
authors:
- Xinran Nicole Han
- Ko Nishino
- Todd Zickler
concepts:
- diffusion models
- generative perception
- generative models
- disentangled representations
- differential motion cues
- shape-material ambiguity
- uncertainty quantification
- posterior estimation
- attention mechanisms
- transformers
- inverse problems
- score-based models
- representation learning
figures:
- /iaifi-research-blog/figures/2506_02473/figure_1.png
- /iaifi-research-blog/figures/2506_02473/figure_2.png
- /iaifi-research-blog/figures/2506_02473/figure_3.png
pdfUrl: https://arxiv.org/pdf/2506.02473v2
published: '2025-06-03T05:43:20+00:00'
theme: Foundational AI
title: Generative Perception of Shape and Material from Differential Motion
wordCount: 962
---

## The Big Picture

Pick up a coffee mug and tilt it slightly. In an instant, the sheen shifts across its surface, and your brain immediately "knows" the mug is curved, ceramic, and matte. Now try to figure the same thing out from a single photograph. Suddenly it's a puzzle. Is that a glossy sphere, or a flat painted circle under a spotlight? Is the object convex or concave? Without knowing the lighting, a single image leaves these questions genuinely, mathematically unresolved.

This is one of the oldest open problems in computer vision: **inverse rendering**, or reconstructing the intrinsic properties of an object (its shape and material) from the light that bounces off it. The challenge isn't just technical difficulty. The problem has no unique solution: infinitely many combinations of geometry, surface texture, and lighting can produce exactly the same photograph.

Most AI systems dodge this by predicting a single "best guess," sweeping the ambiguity under the rug.

Researchers at Harvard and Kyoto University took a different approach, one inspired by how humans actually handle visual uncertainty. Their new model doesn't collapse to a single answer. It reasons like a curious observer, sitting with ambiguity until motion provides the evidence needed to resolve it.

> **Key Insight:** Rather than predicting one "best" answer for shape and material, this model generates a *distribution* of plausible explanations. As an object moves, those possibilities converge toward the truth.

## How It Works

The core idea is simple but powerful: when you're uncertain, move. A few degrees of object rotation changes highlights, shadows, and surface shading in ways that single images cannot. The researchers built a model to exploit exactly this signal.

![Figure 1](/iaifi-research-blog/figures/2506_02473/figure_1.png)

Their architecture is a **conditional denoising-diffusion model**, a generative model that gradually sculpts structured outputs from random noise, guided by input observations. The model, called **U-ViT3D-Mixer**, takes a short three-frame video of an object undergoing small rotations and jointly produces:

- **Surface normal maps**, encoding the 3D orientation of every visible surface point
- **Diffuse albedo**, the object's base color, stripped of lighting effects
- **Roughness and metallic maps**, capturing how shiny, matte, or metallic the surface is

All four attributes are inferred *simultaneously* within a single model backbone. Prior work predicted them independently, treating normals, albedo, and roughness as separate problems with separate models. Here, cross-channel mixing layers let information about shape directly influence material estimates, and vice versa.

The spatial design matters too. At coarse scales, global spatiotemporal attention captures object-level constraints: overall geometry, broad patterns of highlights. At fine scales, the model switches to **neighborhood attention**, a lightweight mechanism that enforces local consistency across both space and time. The entire model operates directly in 256×256 pixel space, with no compression step that might discard fine details.

Training used synthetic videos (3D objects rendered under varied lighting, rotating slightly between frames). Despite this, the model generalizes to real photographs, a sign it learned something genuine about the physics of light and surface interaction rather than memorizing dataset artifacts.

The most interesting behavior is emergent. Given a *static* single image, the model produces *multiple* diverse hypotheses, including the classic convex/concave ambiguity, where the same image is equally consistent with a bump, a dent, or a flat painted surface. It doesn't pick one. It generates all three as distinct plausible worlds.

Then, when motion frames arrive, the distribution tightens. Inconsistent explanations get ruled out, and the model converges toward the geometrically correct answer.

![Figure 2](/iaifi-research-blog/figures/2506_02473/figure_2.png)

## Why It Matters

Today's robots, autonomous vehicles, and embodied AI systems make decisions based on visual input, but typically by extracting single fixed guesses about depth, surface type, or material. A robot navigating a kitchen can't afford to confuse a glossy wet floor for a dry one, or mistake a painted curb for an actual drop. These are shape-and-material problems in the wild, and they need a system that knows when it *doesn't* know.

By modeling visual ambiguity explicitly and showing that motion resolves it, this work offers a template for building AI systems that reason more like humans: generating hypotheses, testing them against new observations, and updating accordingly. The authors call this framework **generative perception** and argue it should be a core capability for physically-embodied AI. The model's ability to transfer from synthetic training data to real-world images also suggests broader generalizability than most task-specific vision systems achieve.

Open questions remain. Can the model scale to complex multi-object scenes? How many frames of motion are needed for different ambiguity types? Can this uncertainty-aware perception loop integrate with touch or other sensory modalities?

> **Bottom Line:** By training a diffusion model to *embrace* rather than suppress visual ambiguity, this work shows that motion (even just a few video frames) can do for AI what a head-tilt does for humans: transform an uncertain guess into a confident, accurate read of the world.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits at the intersection of computer vision and the physics of light-surface interaction, using the mathematics of inverse rendering as the foundation for a learning-based system that jointly recovers shape and material without explicit knowledge of illumination.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The U-ViT3D-Mixer architecture shows that generative models can capture multimodal uncertainty in visual inference and use temporal observations to resolve it, opening the door to uncertainty-aware visual reasoning in embodied AI.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The model encodes physical priors about how surface normals, diffuse albedo, and specular reflectance jointly determine an object's appearance, tying AI perception directly to the underlying physics of light transport.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending generative perception to multi-object scenes, integrating touch and other modalities, and applying the framework to robotics applications where material disambiguation is safety-critical. The full paper is available at [arXiv:2506.02473](https://arxiv.org/abs/2506.02473).</span></div></div>
</div>
