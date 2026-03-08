---
abstract: 'Scene representations using 3D Gaussian primitives have produced excellent
  results in modeling the appearance of static and dynamic 3D scenes. Many graphics
  applications, however, demand the ability to manipulate both the appearance and
  the physical properties of objects. We introduce Feature Splatting, an approach
  that unifies physics-based dynamic scene synthesis with rich semantics from vision
  language foundation models that are grounded by natural language. Our first contribution
  is a way to distill high-quality, object-centric vision-language features into 3D
  Gaussians, that enables semi-automatic scene decomposition using text queries. Our
  second contribution is a way to synthesize physics-based dynamics from an otherwise
  static scene using a particle-based simulator, in which material properties are
  assigned automatically via text queries. We ablate key techniques used in this pipeline,
  to illustrate the challenge and opportunities in using feature-carrying 3D Gaussians
  as a unified format for appearance, geometry, material properties and semantics
  grounded on natural language. Project website: https://feature-splatting.github.io/'
arxivId: '2404.01223'
arxivUrl: https://arxiv.org/abs/2404.01223
authors:
- Ri-Zhao Qiu
- Ge Yang
- Weijia Zeng
- Xiaolong Wang
concepts:
- representation learning
- 3d gaussian splatting
- feature extraction
- language-grounded scene editing
- embeddings
- material point method
- geometric deep learning
- self-supervised learning
- surrogate modeling
- inverse problems
- interpretability
figures:
- /iaifi-research-blog/figures/2404_01223/figure_1.png
- /iaifi-research-blog/figures/2404_01223/figure_2.png
pdfUrl: https://arxiv.org/pdf/2404.01223v1
published: '2024-04-01T16:31:04+00:00'
theme: Foundational AI
title: 'Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing'
wordCount: 1242
---

## The Big Picture

Imagine photographing a vase of flowers on your kitchen table. The image is static, frozen in time. Now imagine typing "make the flowers sway in a gentle breeze" and watching the petals bend and flutter realistically, each stem flexing according to its actual material stiffness, while the ceramic vase sits immovably rigid beneath them. No animator needed. No physics degree required. Just a sentence.

That's the promise behind **Feature Splatting**, a new system from researchers at UC San Diego and MIT's Institute for AI and Fundamental Interactions (IAIFI). The challenge has always been that 3D scene representations, no matter how photorealistic, are dumb about the world. They can capture what things *look* like, but they know nothing about what things *are* or how they *behave*. A digital flower and a digital rock look different but, to the computer, are equally inert.

Feature Splatting combines three previously separate technologies: a method for building precise 3D scenes from ordinary photographs, AI models trained to understand both images and language, and a physics engine that simulates how real materials move and deform. The result is a system that takes an ordinary set of photographs, builds a 3D scene, and lets users animate it with plain English.

> **Key Insight:** Feature Splatting embeds language-grounded semantic meaning directly into 3D scene geometry, enabling text queries to both identify scene objects *and* automatically assign them physically realistic material properties, turning static captures into dynamic simulations.

## How It Works

The foundation of Feature Splatting is **3D Gaussian Splatting (GS)**, a technique that represents a scene not as a mesh or a neural network, but as a cloud of millions of fuzzy ellipsoids (Gaussians), each carrying color and opacity information. GS renders fast and looks stunning. But those Gaussians are semantically blind. Feature Splatting's first trick is to make them see.

![Figure 1](/iaifi-research-blog/figures/2404_01223/figure_1.png)

The team augments each Gaussian with a high-dimensional **feature vector**, a long list of numbers encoding what that point in the scene semantically "means," distilled from large 2D vision foundation models. Specifically, they use CLIP (which connects images to language) and DINOv2 (which captures rich visual structure). The catch: when these models analyze a photo, their outputs are low-resolution and noisy, and naively projecting them onto 3D Gaussians produces artifacts.

The fix is simple and effective. The team first runs **SAM (Segment Anything Model)** to produce part-level masks, coherent regions like "petal," "stem," or "vase body," and then pools features within those masks before distillation. This produces much cleaner, semantically meaningful feature fields baked into the 3D structure.

![Figure 2](/iaifi-research-blog/figures/2404_01223/figure_2.png)

With features embedded, scene decomposition becomes a text query. A user types "a vase with flowers," and the system finds the Gaussians whose feature vectors are mathematically closest in meaning to that description. This is **open-vocabulary segmentation**: the system doesn't need to have been trained on "vase" or "flowers" as labeled categories. It inherits that knowledge from CLIP's massive pretraining.

The second major contribution handles what happens *after* segmentation: physics. Feature Splatting integrates an **MPM (Material Point Method)** physics engine, a particle-based simulator well-suited to materials that deform, flow, and break. Two ideas make this work:

- **Material assignment via language:** The same text-query mechanism that decomposes scenes also identifies material categories. The system queries whether a segmented region is "rigid," "elastic," "viscous," and so on, then looks up corresponding physical parameters (Young's modulus, Poisson's ratio, yield stress) from a predefined table. These parameters describe stiffness, compressibility, and breaking strength.
- **Infilling for volume-dependent physics:** GS represents surfaces, not volumes. MPM needs particles throughout an object's interior to simulate effects like squishing or bouncing. The team developed an infilling procedure to populate object interiors with physics particles before simulation begins.

As the simulation runs, Gaussian primitives must deform realistically. The team uses a **local affine transformation**, a mathematical operation tracking how each small region stretches, rotates, and shifts, tied to nearby MPM particles. Each Gaussian's position, rotation, and scale updates continuously. This approach handles large deformations better than earlier methods.

## Why It Matters

Feature Splatting sits at an unusual crossroads. On the AI side, it shows that knowledge locked inside large 2D vision-language models, trained on internet-scale image-text pairs, can be *transferred* into explicit 3D representations without retraining those models from scratch. You get the benefit of billion-parameter pretraining without the cost.

The feature-carrying Gaussian format is a unified data structure holding appearance, geometry, semantics, and physics simultaneously. Computer vision researchers have wanted something like this for a long time.

On the physics side, the connection to MPM matters. Material Point Methods have a rich history, from snow simulation in Disney's *Frozen* to soft robotics to geomechanics. Grounding MPM in natural language means a non-expert can specify "this is rubber, this is glass" and get physically plausible results. That's accessible simulation at a scale that used to require domain expertise. As AI systems get better at mapping language to physical properties, the gap between *describing* a scene and *simulating* it shrinks.

Open questions remain. The material property lookup table is hand-curated; future work might learn parameters directly from video observations. Feature quality degrades in cluttered scenes with heavy occlusion, and the pipeline requires reasonably clean multi-view captures. The paper's ablation studies isolate which components contribute most, pointing toward clear next steps.

> **Bottom Line:** Feature Splatting proves that a single 3D representation can simultaneously encode what a scene looks like, what objects are in it, and how those objects behave physically, letting anyone animate a photograph with a sentence.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">Feature Splatting bridges large-scale language-vision AI with classical physics simulation, showing that semantic knowledge from internet-trained foundation models can drive physically correct material dynamics in 3D scene reconstruction.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work introduces a practical method for distilling noisy 2D vision-language features into clean, object-centric 3D Gaussian representations using SAM-pooled masks, advancing open-vocabulary 3D scene understanding without retraining foundation models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By coupling language-grounded segmentation with an MPM physics engine, the system makes particle-based simulation of real-world material behavior accessible through natural language, lowering the barrier to physically realistic dynamic scene synthesis.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include learning material parameters directly from observed dynamics rather than lookup tables, and extending to more complex multi-object interactions; the work is available at https://feature-splatting.github.io/ ([arXiv:2404.01223](https://arxiv.org/abs/2404.01223)).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[arXiv:2404.01223](https://arxiv.org/abs/2404.01223)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">Ri-Zhao Qiu, Ge Yang, Weijia Zeng, Xiaolong Wang</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Scene representations using 3D Gaussian primitives have produced excellent results in modeling the appearance of static and dynamic 3D scenes. Many graphics applications, however, demand the ability to manipulate both the appearance and the physical properties of objects. We introduce Feature Splatting, an approach that unifies physics-based dynamic scene synthesis with rich semantics from vision language foundation models that are grounded by natural language. Our first contribution is a way to distill high-quality, object-centric vision-language features into 3D Gaussians, that enables semi-automatic scene decomposition using text queries. Our second contribution is a way to synthesize physics-based dynamics from an otherwise static scene using a particle-based simulator, in which material properties are assigned automatically via text queries. We ablate key techniques used in this pipeline, to illustrate the challenge and opportunities in using feature-carrying 3D Gaussians as a unified format for appearance, geometry, material properties and semantics grounded on natural language. Project website: https://feature-splatting.github.io/</span></div></div>
</div>
