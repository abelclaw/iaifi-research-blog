---
abstract: Models for inferring monocular shape of surfaces with diffuse reflection
  -- shape from shading -- ought to produce distributions of outputs, because there
  are fundamental mathematical ambiguities of both continuous (e.g., bas-relief) and
  discrete (e.g., convex/concave) types that are also experienced by humans. Yet,
  the outputs of current models are limited to point estimates or tight distributions
  around single modes, which prevent them from capturing these effects. We introduce
  a model that reconstructs a multimodal distribution of shapes from a single shading
  image, which aligns with the human experience of multistable perception. We train
  a small denoising diffusion process to generate surface normal fields from $16\times
  16$ patches of synthetic images of everyday 3D objects. We deploy this model patch-wise
  at multiple scales, with guidance from inter-patch shape consistency constraints.
  Despite its relatively small parameter count and predominantly bottom-up structure,
  we show that multistable shape explanations emerge from this model for ambiguous
  test images that humans experience as being multistable. At the same time, the model
  produces veridical shape estimates for object-like images that include distinctive
  occluding contours and appear less ambiguous. This may inspire new architectures
  for stochastic 3D shape perception that are more efficient and better aligned with
  human experience.
arxivId: '2405.14530'
arxivUrl: https://arxiv.org/abs/2405.14530
authors:
- Xinran Nicole Han
- Todd Zickler
- Ko Nishino
concepts:
- diffusion models
- multistable perception
- shape from shading
- patch-based diffusion
- inverse problems
- posterior estimation
- uncertainty quantification
- generative models
- stochastic processes
- convolutional networks
- score-based models
figures:
- /iaifi-research-blog/figures/2405_14530/figure_1.png
- /iaifi-research-blog/figures/2405_14530/figure_1.png
- /iaifi-research-blog/figures/2405_14530/figure_2.png
- /iaifi-research-blog/figures/2405_14530/figure_2.png
- /iaifi-research-blog/figures/2405_14530/figure_3.png
- /iaifi-research-blog/figures/2405_14530/figure_3.png
pdfUrl: https://arxiv.org/pdf/2405.14530v2
published: '2024-05-23T13:15:24+00:00'
theme: Foundational AI
title: Multistable Shape from Shading Emerges from Patch Diffusion
wordCount: 1031
---

## The Big Picture

Stare at an image of a dimpled golf ball long enough and something strange happens: the dimples suddenly pop outward, becoming bumps. Flip the photo upside down and they sink back in. Your brain hasn't changed, and neither has the image — but your perception of the three-dimensional shape has flipped entirely, toggling between two equally valid interpretations.

This isn't a quirk. It's a fundamental mathematical truth: when a matte (non-shiny) surface is photographed from a single viewpoint, multiple three-dimensional shapes can produce the exact same pattern of light and shadow. The image is genuinely ambiguous.

Humans experience this directly, alternating between competing shape interpretations in what vision scientists call **multistable perception**. Yet virtually every existing AI model for 3D shape recognition ignores this reality, committing to a single "best guess" and pretending the ambiguity doesn't exist.

Researchers at Harvard University and Kyoto University have now built a model that does what humans do: rather than committing to a single answer, it holds multiple valid shape interpretations open simultaneously — in a package so small it fits in 10 megabytes.

> **Key Insight:** By training a tiny diffusion model on local 16×16 image patches and deploying it at multiple scales with consistency constraints, the researchers show that global perceptual ambiguity — the kind humans experience — emerges automatically from purely local, bottom-up processing.

## How It Works

The core insight is deceptively simple: train a small model to understand tiny image patches, then let the pieces talk to each other.

![Figure 2](/iaifi-research-blog/figures/2405_14530/figure_1.png)

The team trained a **denoising diffusion process** — a generative model that learns to reconstruct clean images by reversing a step-by-step noise-adding process — on 16×16 pixel crops from synthetic images of matte objects. The model predicts **surface normal fields**, which encode the 3D orientation of each surface point as a vector perpendicular to the surface. Training on patches rather than whole images keeps the model compact (just 10MB of weights) and forces it to learn local shading relationships without baking in global scene biases.

During inference, the approach unfolds in three stages:

1. **Patch-wise generation**: The diffusion model runs in parallel across non-overlapping 16×16 patches, sampling possible surface normals for each patch independently.
2. **Inter-patch consistency guidance**: Two constraint losses nudge neighboring patches toward a globally coherent shape. A **curvature smoothness loss** penalizes abrupt, physically unrealistic changes in surface bending between patches. An **integrability loss** enforces the geometric requirement that surface normals correspond to a valid 3D surface — without it, adjacent patches could each make local sense but fail to form a coherent object.
3. **Multi-scale V-cycle sampling**: The model cycles between fine and coarse spatial resolutions during the diffusion process — a "fine-coarse-fine" approach borrowed from image-processing optimization algorithms — resampling predictions at intermediate noise levels before resuming denoising. Ablation experiments confirm this step is essential for finding globally consistent solutions rather than getting trapped in locally coherent but globally contradictory ones.

Lighting gets an elegant treatment. Instead of estimating a precise global light source — ill-posed given real-world complications like interreflections and ambient occlusion — each patch nominates a dominant light direction. When the model detects a global convex/concave ambiguity, all patches flip their interpretations in concert via a **global flip mechanism**. This flexible approach respects physical constraints without over-committing to a precise lighting model.

![Figure 1](/iaifi-research-blog/figures/2405_14530/figure_1.png)

The result is striking. For images that humans flip between — like the golf ball — the model produces genuinely multimodal output: distinct samples corresponding to concave and convex interpretations. For ordinary objects with clear occluding contours, it converges on a single accurate estimate. No special rule governs when to be certain versus uncertain; that behavior emerged from the architecture itself.

## Why It Matters

The immediate practical payoff is efficiency. Previous diffusion-based shape models like Marigold and Wonder3D require 2–3 gigabytes of weights and still produce unimodal outputs — single guesses that ignore perceptual ambiguity entirely. This model achieves competitive accuracy on unambiguous images while additionally capturing multistability, all in a package 200–300 times smaller. For robotics, augmented reality, or any application requiring real-time 3D scene understanding from a single camera, that efficiency matters enormously.

The deeper implication points toward a new theory of visual perception. The fact that global multistability emerges from purely local patch-level processing — with no high-level understanding of objects or scenes — suggests the human visual system might operate on similar principles. David Marr's "principle of least commitment," a foundational idea in vision science, argued that perception should avoid premature decisions that might need to be undone. This model puts that principle into practice through a probabilistic architecture that keeps multiple shape interpretations alive simultaneously, resolving ambiguity only when the evidence demands it.

Future work could extend the framework to non-Lambertian surfaces (shiny or transparent materials that don't scatter light uniformly), incorporate sparse depth cues to study selective disambiguation, or push toward richer multi-scale coordination — each direction probing how visual systems manage the fundamental underdetermination of 3D shape from 2D images.

> **Bottom Line:** A tiny patch-based diffusion model trained only on local image regions spontaneously learns to perceive 3D shape the way humans do — holding multiple conflicting interpretations simultaneously — suggesting that efficient, ambiguity-aware 3D perception is achievable without massive models or global scene understanding.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges computational vision, perceptual psychology, and generative AI by building a mathematical model of multistable shape perception — a phenomenon studied for decades in human vision science — using modern diffusion architectures.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">A 10MB patch-based diffusion model matches or outperforms gigabyte-scale models on shape estimation while additionally capturing perceptual ambiguity, pointing toward a new paradigm of efficient, uncertainty-aware 3D perception.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By formalizing the mathematical ambiguities of Lambertian shading — including bas-relief transformations and global convex/concave flips — and encoding them as a learned generative distribution, the work connects physical light-transport laws directly to perceptual phenomena.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending the framework to non-Lambertian surfaces and incorporating sparse depth cues to study selective disambiguation; the paper appeared at NeurIPS 2024 (arXiv: 2405.XXXXX by Han, Zickler, and Nishino).</span></div></div>
</div>
