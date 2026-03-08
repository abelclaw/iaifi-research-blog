---
abstract: 'We propose RelitLRM, a Large Reconstruction Model (LRM) for generating
  high-quality Gaussian splatting representations of 3D objects under novel illuminations
  from sparse (4-8) posed images captured under unknown static lighting. Unlike prior
  inverse rendering methods requiring dense captures and slow optimization, often
  causing artifacts like incorrect highlights or shadow baking, RelitLRM adopts a
  feed-forward transformer-based model with a novel combination of a geometry reconstructor
  and a relightable appearance generator based on diffusion. The model is trained
  end-to-end on synthetic multi-view renderings of objects under varying known illuminations.
  This architecture design enables to effectively decompose geometry and appearance,
  resolve the ambiguity between material and lighting, and capture the multi-modal
  distribution of shadows and specularity in the relit appearance. We show our sparse-view
  feed-forward RelitLRM offers competitive relighting results to state-of-the-art
  dense-view optimization-based baselines while being significantly faster. Our project
  page is available at: https://relit-lrm.github.io/.'
arxivId: '2410.06231'
arxivUrl: https://arxiv.org/abs/2410.06231
authors:
- Tianyuan Zhang
- Zhengfei Kuang
- Haian Jin
- Zexiang Xu
- Sai Bi
- Hao Tan
- He Zhang
- Yiwei Hu
- Milos Hasan
- William T. Freeman
- Kai Zhang
- Fujun Luan
concepts:
- transformers
- diffusion models
- 3d gaussian splatting
- disentangled representations
- generative models
- feed-forward reconstruction
- inverse problems
- attention mechanisms
- novel view synthesis
- transfer learning
figures:
- /iaifi-research-blog/figures/2410_06231/figure_1.png
- /iaifi-research-blog/figures/2410_06231/figure_2.png
- /iaifi-research-blog/figures/2410_06231/figure_3.png
pdfUrl: https://arxiv.org/pdf/2410.06231v2
published: '2024-10-08T17:40:01+00:00'
theme: Foundational AI
title: 'RelitLRM: Generative Relightable Radiance for Large Reconstruction Models'
wordCount: 1189
---

## The Big Picture

Imagine you snap a few quick photos of a ceramic vase on your kitchen counter on an overcast afternoon. Now imagine handing those photos to a computer system that, within seconds, returns a perfect 3D model you can drop into a sun-drenched desert scene, a neon-lit nightclub, or a candlelit room, and have it look exactly right. Shadows fall where they should. Glossy highlights flare at the correct angles. The vase belongs.

That scenario has been a holy grail of computer vision for decades. The core problem is brutal: lighting and material properties are hopelessly entangled in any photograph. When you see a bright spot on that vase, is it because the ceramic is shiny, or because the light source is intense? A camera can't tell you.

Untangling this so you can re-render an object under entirely new lighting, a task called **relighting**, has traditionally demanded hundreds of images taken under controlled, laboratory-grade illumination, followed by hours of computational optimization. Impressive, but impractical outside a professional visual-effects pipeline.

Researchers from MIT, Stanford, Cornell, and Adobe Research have built RelitLRM, a system that achieves competitive relighting quality from just 4–8 casual photographs in roughly one second.

> **Key Insight:** RelitLRM separates the job of figuring out *where* an object is in 3D space from the job of figuring out *how light plays across it*, using two fundamentally different AI approaches for each and letting it handle the ambiguity that defeats simpler systems.

## How It Works

The trick at RelitLRM's core is architectural: don't try to solve the whole problem at once. Split it into two sequential tasks, each suited to a different machine-learning paradigm.

1. **Reconstruct the geometry.** A transformer-based geometry reconstructor (a large neural network that compares small patches of an image to every other patch) identifies how parts of the scene relate in 3D space. This is the same architecture that powers modern language models, adapted here for visual information. The output is the object's structure encoded as **3D Gaussian Splatting (3DGS)** primitives: millions of tiny translucent blobs, each with a position, size, orientation, and opacity. 3DGS has become the field's go-to compact, fast-to-render representation since 2023.

2. **Generate the appearance under new light.** Once geometry is locked in, RelitLRM hands off to a **diffusion-based appearance generator**, the family of models behind image generators like Stable Diffusion. Why diffusion? Because relighting is *fundamentally uncertain*. A glossy surface can produce **specular highlights** (intense bright spots where light bounces directly toward the camera) that could appear in several plausible positions depending on tiny, unknown surface details. A regression model trained to predict a single "best" output averages over those possibilities, producing a blurry smear. A diffusion model samples from the full distribution of plausible appearances, picking one sharp, physically coherent answer instead of the washed-out mean.

![Figure 1](/iaifi-research-blog/figures/2410_06231/figure_1.png)

The two stages are trained **end-to-end** (optimized together as a single system) on a large synthetic dataset of 3D objects rendered under many known illuminations. The target lighting condition is fed in as an additional input token, telling the system not just what the object looks like, but what kind of light to simulate. On a single A100 GPU, inference takes about one second.

![Figure 2](/iaifi-research-blog/figures/2410_06231/figure_2.png)

This design also sidesteps **shadow baking**, a persistent flaw in earlier methods. Per-scene optimization often accidentally embeds the original lighting (shadows, highlights, and all) directly into the surface material representation. The result: artifacts stubbornly remain when you try to relight, like a shadow that won't move when the sun does. Training end-to-end across diverse illuminations teaches RelitLRM to pull apart lighting and material properties from the start.

## Why It Matters

The obvious applications are in digital content creation, gaming, and augmented reality, anywhere you need 3D assets that look correct under different lighting. The paper shows this directly: photograph a real object, run RelitLRM, and insert it into a synthetic 3D scene. It looks like it belongs.

But the deeper significance is methodological. RelitLRM makes the case that the right answer to a physically ambiguous inverse problem isn't always to push harder on optimization. Sometimes it's to reframe the problem as generative sampling. The material-lighting ambiguity that has dogged inverse rendering researchers for two decades is a **multi-modal** uncertainty (many equally valid answers exist, not just one), and diffusion models are well-suited to represent exactly that kind of uncertainty. The same logic should apply wherever physics produces genuinely ambiguous observations.

![Figure 3](/iaifi-research-blog/figures/2410_06231/figure_3.png)

Open questions remain. The system trains on synthetic data, and real-world photographs introduce mismatches that the authors acknowledge. The geometry stage still relies on images where the camera position is roughly known. And the diffusion-based appearance generator, while excellent at capturing high-frequency specular effects, introduces some randomness that regression-based methods avoid.

The clearest next steps are fully unconstrained casual capture, larger and more diverse training datasets, and tighter integration between the geometry and appearance stages.

> **Bottom Line:** RelitLRM turns a problem that once required a photography studio and a supercomputer into one that runs on a single GPU in about a second, by being smart about which parts of the problem need deterministic answers and which need probabilistic ones.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work brings together physically-based rendering, rooted in optics and light-transport physics, with modern deep learning, using transformer and diffusion architectures to implicitly learn how light interacts with surfaces.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">RelitLRM advances feed-forward generative 3D reconstruction by showing that combining regression-based geometry estimation with diffusion-based appearance synthesis outperforms either approach alone on ambiguous inverse problems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By disentangling geometry, material properties, and illumination from sparse observations, the system performs learned inverse rendering, recovering physically meaningful scene properties without explicit physical simulation at inference time.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include training on larger real-world datasets to close the synthetic-to-real gap and extending the framework to full scene relighting beyond individual objects; the work is available on [arXiv:2410.06231](https://arxiv.org/abs/2410.06231) and at relit-lrm.github.io.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">RelitLRM: Generative Relightable Radiance for Large Reconstruction Models</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2410.06231</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Tianyuan Zhang", "Zhengfei Kuang", "Haian Jin", "Zexiang Xu", "Sai Bi", "Hao Tan", "He Zhang", "Yiwei Hu", "Milos Hasan", "William T. Freeman", "Kai Zhang", "Fujun Luan"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We propose RelitLRM, a Large Reconstruction Model (LRM) for generating high-quality Gaussian splatting representations of 3D objects under novel illuminations from sparse (4-8) posed images captured under unknown static lighting. Unlike prior inverse rendering methods requiring dense captures and slow optimization, often causing artifacts like incorrect highlights or shadow baking, RelitLRM adopts a feed-forward transformer-based model with a novel combination of a geometry reconstructor and a relightable appearance generator based on diffusion. The model is trained end-to-end on synthetic multi-view renderings of objects under varying known illuminations. This architecture design enables to effectively decompose geometry and appearance, resolve the ambiguity between material and lighting, and capture the multi-modal distribution of shadows and specularity in the relit appearance. We show our sparse-view feed-forward RelitLRM offers competitive relighting results to state-of-the-art dense-view optimization-based baselines while being significantly faster. Our project page is available at: https://relit-lrm.github.io/.</span></div></div>
</div>
