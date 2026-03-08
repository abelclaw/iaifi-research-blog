---
abstract: For the first time, we show high-fidelity generation of LArTPC-like data
  using a generative neural network. This demonstrates that methods developed for
  natural images do transfer to LArTPC-produced images, which, in contrast to natural
  images, are globally sparse but locally dense. We present the score-based diffusion
  method employed. We evaluate the fidelity of the generated images using several
  quality metrics, including modified measures used to evaluate natural images, comparisons
  between high-dimensional distributions, and comparisons relevant to LArTPC experiments.
arxivId: '2307.13687'
arxivUrl: https://arxiv.org/abs/2307.13687
authors:
- Zeviel Imani
- Shuchin Aeron
- Taritree Wongjirad
concepts:
- score-based models
- diffusion models
- detector simulation
- generative models
- surrogate modeling
- neutrino detection
- sparse image generation
- monte carlo methods
- convolutional networks
- simulation-based inference
- transfer learning
- density estimation
figures:
- /iaifi-research-blog/figures/2307_13687/figure_1.png
- /iaifi-research-blog/figures/2307_13687/figure_2.png
- /iaifi-research-blog/figures/2307_13687/figure_3.png
pdfUrl: https://arxiv.org/pdf/2307.13687v3
published: '2023-07-25T17:47:50+00:00'
theme: Theoretical Physics
title: Score-based Diffusion Models for Generating Liquid Argon Time Projection Chamber
  Images
wordCount: 1070
---

## The Big Picture

Imagine trying to photograph a lightning bolt, but instead of a camera, you're using a detector the size of a house, filled with ultra-cold liquid argon. When a neutrino passes through and strikes an argon atom, it knocks loose a cascade of electrons, a trail of electric charge like a ghost's footprint in snow. Physicists reconstruct the entire collision from those wire-by-wire electrical signals, building up 2D images of particle tracks.

The problem? Simulating those images accurately enough to do real physics takes *minutes per event*, and modern experiments need millions of them.

That simulation bottleneck is serious. Experiments like MicroBooNE, SBND, and the future DUNE detector all rely on Liquid Argon Time Projection Chambers (LArTPCs), detectors that scale to tens of meters while still resolving particle tracks to the millimeter. But their complexity makes Monte Carlo simulation (the standard approach of running millions of randomized physics calculations) brutally expensive. Researchers have spent years trying to replace that pipeline with generative neural networks, with limited success.

A team from Tufts University and IAIFI has now shown, for the first time, that a modern AI image generation technique can produce LArTPC images of high fidelity. Their tool of choice: the same class of models powering today's AI art generators.

> **Key Insight:** Score-based diffusion models, the architecture behind many leading image generators, can learn to produce realistic particle physics detector images, even though those images look almost nothing like the natural photographs the models were designed for.

## How It Works

The core challenge isn't just generating images. It's generating the *right kind* of images. LArTPC images are structurally unlike photographs. A natural image is densely populated with information in every pixel. A LArTPC image is **globally sparse but locally dense**: mostly empty space, with thin bright streaks of particle tracks cutting across it. Previous generative approaches, including GANs and Normalizing Flows, struggled with this unusual structure.

The researchers turned to **score-based generative models (SGMs)**. Rather than learning the probability distribution of images directly, you learn its *gradient*, the score function that points toward higher-probability regions. Training unfolds in three stages:

1. **Forward diffusion:** Start with a real LArTPC image and progressively corrupt it with Gaussian noise, described by a stochastic differential equation (SDE), until the image is pure static.
2. **Score estimation:** Train a neural network to estimate the score function at each noise level, learning how to denoise at every stage.
3. **Reverse diffusion:** At generation time, start from random noise and run the reverse SDE, using the learned score to guide the system back toward the data manifold, the narrow slice of possible images that actually look like real physics data.

![Figure 1](/iaifi-research-blog/figures/2307_13687/figure_1.png)

The theoretical payoff is stability. SGMs can provably learn high-dimensional, multi-modal distributions (distributions with many distinct clusters) even when data lives on a low-dimensional manifold. That's exactly the situation here: a LArTPC image might show a muon going straight, a muon scattering sharply, or an electron shower branching like a tree. The model must capture all those modes without collapsing to a single average.

Evaluating the results required more than standard metrics. Fréchet Inception Distance (FID), the usual benchmark for image generators, uses a network trained on photographs, which makes it a poor judge of particle tracks. The team developed a multi-pronged approach: modified image quality metrics, high-dimensional distribution comparisons, and physics-specific measures including track length distributions, pixel intensity profiles, and rates of different event topologies.

![Figure 2](/iaifi-research-blog/figures/2307_13687/figure_2.png)

![Figure 3](/iaifi-research-blog/figures/2307_13687/figure_3.png)

Across all these metrics, the diffusion model succeeded where previous approaches had failed. Tracks looked like tracks. The sparse-but-dense structure was preserved. Physical quantities matched.

## Why It Matters

For neutrino physics, this opens a path toward fast surrogate models for detector simulation. A diffusion model that generates realistic LArTPC images quickly could replace slow Geant4 simulation for tasks not requiring absolute physical accuracy, cutting the time needed to fill experiment analysis pipelines. There's also a deeper possibility: generative models capable of estimating likelihoods of raw detector data could enable statistical inference techniques that traditional simulation can't support.

For AI in physics more broadly, this is an important existence proof. The particle physics community has had real success adapting generative models to LHC collider data (jets, calorimeter showers, and related outputs). But LArTPC data resisted those methods. The fact that score-based diffusion transfers to this domain, despite its unusual sparsity structure, suggests the approach is more general than previously assumed.

Which other scientific image domains might be next? Electron microscopy, gravitational wave spectrograms, radio telescope maps. The immediate next step is scaling: moving from 64×64 toy images to the full-resolution data real experiments produce.

> **Bottom Line:** By applying score-based diffusion models to LArTPC detector images, this work achieves the first high-fidelity generative model for this class of neutrino physics data, showing that modern AI image generation can handle the globally-sparse, locally-dense structure of particle detectors and pointing toward faster, AI-accelerated simulation pipelines.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects generative AI and experimental neutrino physics by adapting score-based diffusion models, developed for natural image generation, to the structurally distinct domain of LArTPC detector images.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Score-based diffusion models generalize beyond natural images to scientifically unusual data distributions. Their ability to handle multi-modal, low-dimensional-manifold data holds up in practice, and the work motivates new domain-specific evaluation metrics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">High-fidelity generative models for LArTPC data could replace computationally expensive Geant4 Monte Carlo simulation and enable likelihood-based inference on raw detector data, accelerating analyses in current and future neutrino experiments like DUNE.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work must scale from 64×64 proof-of-concept images to the full 1000×1000-pixel resolution of real LArTPC detectors; see [arXiv:2307.13687](https://arxiv.org/abs/2307.13687) for the full paper and methodology.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Score-based Diffusion Models for Generating Liquid Argon Time Projection Chamber Images</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2307.13687</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Zeviel Imani", "Shuchin Aeron", "Taritree Wongjirad"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">For the first time, we show high-fidelity generation of LArTPC-like data using a generative neural network. This demonstrates that methods developed for natural images do transfer to LArTPC-produced images, which, in contrast to natural images, are globally sparse but locally dense. We present the score-based diffusion method employed. We evaluate the fidelity of the generated images using several quality metrics, including modified measures used to evaluate natural images, comparisons between high-dimensional distributions, and comparisons relevant to LArTPC experiments.</span></div></div>
</div>
