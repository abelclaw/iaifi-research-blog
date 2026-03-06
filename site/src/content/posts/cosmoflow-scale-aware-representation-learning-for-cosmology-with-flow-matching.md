---
abstract: Generative machine learning models have been demonstrated to be able to
  learn low dimensional representations of data that preserve information required
  for downstream tasks. In this work, we demonstrate that flow matching based generative
  models can learn compact, semantically rich latent representations of field level
  cold dark matter (CDM) simulation data without supervision. Our model, CosmoFlow,
  learns representations 32x smaller than the raw field data, usable for field level
  reconstruction, synthetic data generation, and parameter inference. Our model also
  learns interpretable representations, in which different latent channels correspond
  to features at different cosmological scales.
arxivId: '2507.11842'
arxivUrl: https://arxiv.org/abs/2507.11842
authors:
- Sidharth Kannan
- Tian Qiu
- Carolina Cuesta-Lazaro
- Haewon Jeong
concepts:
- flow matching
- representation learning
- cosmological simulation
- dimensionality reduction
- generative models
- scale-aware latent space
- dark matter
- disentangled representations
- interpretability
- posterior estimation
- variational autoencoders
- surrogate modeling
- convolutional networks
figures:
- /iaifi-research-blog/figures/2507_11842/figure_1.png
- /iaifi-research-blog/figures/2507_11842/figure_2.png
- /iaifi-research-blog/figures/2507_11842/figure_3.png
pdfUrl: https://arxiv.org/pdf/2507.11842v1
published: '2025-07-16T02:15:31+00:00'
theme: Astrophysics
title: 'CosmoFlow: Scale-Aware Representation Learning for Cosmology with Flow Matching'
wordCount: 1072
---

## The Big Picture

Imagine trying to understand the entire history of the universe from a single photograph — but the photograph fills a warehouse. That's the situation cosmologists face with modern simulations of the **cosmic web**, the vast network of dark matter and galaxies spanning the observable universe. Simulations like AbacusSummit generate datasets exceeding 2,000 terabytes. Even machines struggle at that scale.

The usual escape route is compression. But compression is a trade-off: squeeze too hard and you lose the subtle, small-scale features that carry crucial cosmological information. Traditional tools like the **power spectrum** — which measures how much structure exists at each spatial scale but discards information about *where* that structure is located — miss details that matter. Standard machine learning compression tools called **variational autoencoders (VAEs)** tend to produce smeared reconstructions, like a watercolor of a photograph. For cosmology, where the fine-grained clumping of matter encodes fundamental physics, "smeared" isn't good enough.

Researchers from UC Santa Barbara and MIT have built a model called **CosmoFlow** that sidesteps this trade-off entirely — compressing cosmological field data by a factor of 32 while preserving the detailed structure that makes it scientifically useful. The trick is encoding each simulation into a compact *latent code* of just 8 numbers that captures enough information to reconstruct the original.

> **Key Insight:** CosmoFlow uses flow matching — a cutting-edge generative modeling framework — to learn compact, interpretable representations of dark matter simulations without any supervision, enabling reconstruction, synthetic data generation, and parameter inference from a single compressed latent code.

## How It Works

The core idea harnesses a generative modeling technique called **flow matching**. Rather than encoding data into a fixed representation and decoding it directly, as VAEs do, flow matching learns a *trajectory*: a smooth path through probability space that gradually transforms random noise into a realistic simulation output. The model learns the velocity field — mathematically, the direction and speed of this transformation — at every point along the path.

![Figure 1](/iaifi-research-blog/figures/2507_11842/figure_1.png)

CosmoFlow's architecture has two main components:

- A **ResNet encoder** — a neural network widely used for image analysis, built from stacked layers that each refine a previous estimate — compresses the raw 256×256 dark matter field into a smaller *compressed field*.
- During iterative decoding, a **UNet-based velocity field predictor** guides full-resolution generation. The UNet — shaped like a U, with layers that progressively zoom out to capture broad patterns then zoom back in to restore fine detail — is conditioned on both the masked compressed field and a **summary statistics vector** of just 8 numbers extracted via global pooling.

Those 8 numbers are the latent code. By conditioning generation on this vector, the model forces it to capture everything statistically relevant: cosmological parameters, large-scale structure, and fine-grained features alike. The training objective is elegant: minimize the difference between the predicted velocity and the straight-line path from noise to data. No labeled pairs, no manual similarity definitions.

The result is a **latent space** 32 times smaller than the raw data, yet rich enough to support three downstream tasks:

- **Field reconstruction** — regenerating the original simulation from the compressed code
- **Synthetic data generation** — producing physically plausible simulations at parameter values absent from the training set
- **Cosmological parameter inference** — estimating fundamental parameters like the matter density Ω_m directly from the 8-element latent vector, with accuracy matching inference on the raw field

## Why It Matters

Perhaps the most striking result isn't the compression ratio — it's what the model learned on its own.

![Figure 3](/iaifi-research-blog/figures/2507_11842/figure_3.png)

Without being told to, CosmoFlow organized its 8-element latent code so that different channels correspond to cosmological features at different spatial scales. Interpolating only the high-frequency channels produced more granular, small-scale clumping — and shifted only the high-frequency components of the power spectrum. Interpolating the low-frequency channels smoothed the image and shifted only large-scale structure. The model spontaneously discovered a scale-organized representation of the universe.

This kind of interpretability is rare. In most deep learning systems, internal representations are inscrutable — useful for prediction but meaningless to physicists. CosmoFlow's latent space has a physical grammar: different dimensions speak to different scales of cosmic structure, echoing how cosmologists themselves decompose the universe by length scale.

![Figure 2](/iaifi-research-blog/figures/2507_11842/figure_2.png)

The practical value is immediate: 32x compression that preserves both reconstruction quality and downstream task performance dramatically reduces the computational burden of working with cosmological simulations. Training datasets currently requiring petabytes of storage could be represented in a fraction of the space. For large collaborations running thousands of simulations to explore parameter space, this matters enormously.

The deeper significance is methodological. CosmoFlow demonstrates that flow matching — developed primarily for image and audio generation — carries inductive biases that make it naturally suited to scientific data with multiscale structure. The fact that the model learns scale-separated representations without explicit supervision suggests the flow matching objective is naturally aligned with the physics of cosmological fields. That's a principle worth exploring across other domains where multiscale structure matters: turbulent fluid dynamics, quantum field theory, and beyond.

Open questions remain. The current model operates on 2D projected fields; extending to full 3D simulations will require significant architectural scaling. The model also shows deviations from ground truth at the highest frequencies — a limitation future work must address before CosmoFlow is ready for precision cosmology.

> **Bottom Line:** CosmoFlow compresses dark matter simulations 32-fold using flow matching, achieving reconstruction quality that leaves VAEs behind — and spontaneously learns a physically interpretable latent space organized by cosmological scale, without any supervision.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">CosmoFlow applies state-of-the-art generative AI — flow matching — to a core problem in observational cosmology, discovering that the model's inductive biases naturally align with the multiscale structure of the cosmic web.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">This work demonstrates that flow matching models can learn compact, semantically rich, and interpretable latent representations of scientific field data without supervision, extending generative representation learning beyond natural images.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling 32x compression of cold dark matter simulations while preserving parameter inference accuracy, CosmoFlow makes it feasible to train machine learning models on much larger cosmological datasets, advancing our ability to test and constrain the ΛCDM model.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include scaling to 3D simulation volumes and improving high-frequency reconstruction fidelity; the full paper is available on arXiv (2506.XXXXX) from the UC Santa Barbara and MIT/CfA collaboration.</span></div></div>
</div>
