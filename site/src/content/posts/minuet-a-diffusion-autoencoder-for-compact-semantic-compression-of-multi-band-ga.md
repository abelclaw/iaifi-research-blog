---
abstract: The Vera C. Rubin Observatory is slated to observe nearly 20 billion galaxies
  during its decade-long Legacy Survey of Space and Time. The rich imaging data it
  collects will be an invaluable resource for probing galaxy evolution across cosmic
  time, characterizing the host galaxies of transient phenomena, and identifying novel
  populations of anomalous systems. While machine learning models have shown promise
  for extracting galaxy features from multi-band astronomical imaging, the large dimensionality
  of the learned latent space presents a challenge for mechanistic interpretability
  studies. In this work, we present Minuet, a low-dimensional diffusion autoencoder
  for multi-band galaxy imaging. Minuet is trained to reconstruct 72x72-pixel $grz$
  image cutouts of 6M galaxies within $z<1$ from the Dark Energy Camera Legacy Survey
  using only five latent dimensions. By using a diffusion model conditioned on the
  transformer-based autoencoder's output for image reconstruction, we achieve semantically-meaningful
  latent representations of galaxy images while still allowing for high-fidelity,
  probabilistic reconstructions. We train a series of binary classifiers on Minuet's
  latent features to quantify their connection to morphological labels from Galaxy
  Zoo, and a conditional flow to produce posterior distributions of SED-derived redshifts,
  stellar masses, and star-formation rates. We further show the value of Minuet for
  nearest neighbor searches in the learned latent space. Minuet provides strong evidence
  for the low intrinsic dimensionality of galaxy imaging, and introduces a class of
  astrophysical models that produce highly compact representations for diverse science
  goals.
arxivId: '2512.04145'
arxivUrl: https://arxiv.org/abs/2512.04145
authors:
- Alexander T. Gagliano
- Yunyi Shen
- V. A. Villar
concepts:
- diffusion models
- autoencoders
- dimensionality reduction
- representation learning
- self-supervised learning
- transformers
- galaxy classification
- normalizing flows
- disentangled representations
- interpretability
- posterior estimation
- anomaly detection
figures:
- /iaifi-research-blog/figures/2512_04145/figure_1.png
- /iaifi-research-blog/figures/2512_04145/figure_2.png
- /iaifi-research-blog/figures/2512_04145/figure_3.png
pdfUrl: https://arxiv.org/pdf/2512.04145v1
published: '2025-12-03T18:59:59+00:00'
theme: Astrophysics
title: 'Minuet: A Diffusion Autoencoder for Compact Semantic Compression of Multi-Band
  Galaxy Images'
wordCount: 934
---

## The Big Picture

Imagine trying to describe every person on Earth using only five numbers. Not five categories, but five continuous values capturing height, weight, age, personality, and health all at once. It sounds absurd. But that's essentially what a team of IAIFI researchers just did with six million galaxies.

The Vera C. Rubin Observatory will soon begin its decade-long Legacy Survey of Space and Time, cataloging nearly 20 billion galaxies. Each galaxy arrives as a multi-band image with three color channels and thousands of pixels, encoding its age, mass, star-formation rate, and cosmic history. Analyzing all of that by hand is impossible. Even with machine learning, the standard approach produces representations with hundreds or thousands of dimensions, which are hard to interpret or connect to physical meaning.

Researchers Alexander Gagliano, Yunyi Shen, and V. A. Villar built a model called **Minuet** that compresses each galaxy image down to just five numbers. Those five numbers encode a surprising amount of the physics.

> **Key Insight:** The essential visual information in galaxy images lives in an astonishingly low-dimensional space. Just five latent dimensions are enough to reconstruct images, predict physical properties, and find morphological twins across six million galaxies.

## How It Works

The core challenge is a tension that runs through generative AI: models that compress images aggressively lose fine detail, while models that preserve detail encode noise alongside signal. Minuet resolves this by splitting the job between two components.

The first is a **transformer-based autoencoder**, a neural network that reads a 72×72-pixel image in three color bands (*g*, *r*, *z*, corresponding to green, red, and near-infrared light) and distills it into a five-dimensional vector. Think of it as the semantic brain: it captures the meaningful essence of a galaxy's appearance. The second is a **conditional diffusion model**, a generative model that reconstructs a high-fidelity image by starting from random noise and gradually refining it, using the five-dimensional vector as a guide. The diffusion model handles the pixel-level detail that the compact representation can't hold on its own.

![Figure 1](/iaifi-research-blog/figures/2512_04145/figure_1.png)

Training required some ingenuity. The team trained Minuet on roughly six million galaxies from the Dark Energy Camera Legacy Survey (DECaLS), all with redshifts *z* < 1, where redshift measures how much a galaxy's light has stretched as the universe expanded. No labels were used. Minuet learned its five-dimensional summary purely by trying to reconstruct what it compressed.

The result is what the authors call a **semantically meaningful latent space**: a compressed mathematical space where nearby points correspond to galaxies that actually resemble each other, not just ones that share similar pixel statistics. To verify this, the team ran several downstream tests:

- **Morphology classification**: Simple binary classifiers trained on Minuet's five features, using crowdsourced Galaxy Zoo labels, tested whether the latent space captured visual categories like "smooth," "disk-shaped," or "merger." The classifiers worked well. The model had learned morphology without being told to.
- **Physical property estimation**: A **conditional normalizing flow** (a model that learns to translate between probability distributions) trained on the latent features predicted redshifts, stellar masses, and star-formation rates. These quantities were derived independently via spectral energy distribution fitting, so Minuet was effectively rediscovering physics from raw images.
- **Nearest-neighbor search**: Querying the latent space for galaxies near a given point returned visually similar neighbors, giving astronomers a fast similarity engine across millions of objects.

![Figure 2](/iaifi-research-blog/figures/2512_04145/figure_2.png)

## Why It Matters

The practical application is scalability. When Rubin comes online and delivers billions of galaxy images per year, astronomers will need fast, reliable ways to sort, search, and characterize what they see. A five-dimensional embedding is orders of magnitude cheaper to store, transmit, and query than raw images or high-dimensional representations. Minuet's architecture shows one way to build such embeddings without giving up interpretability.

But there's a deeper point here. Minuet provides quantitative evidence for something astronomers have long suspected: galaxy images are not as complex as they look. The underlying structure of galaxy shapes and appearances may be genuinely simple, with most of the variation across the entire population captured by just a handful of continuous parameters.

If true, this changes how we build AI tools for astronomy, how we search for anomalies, and how we think about the information content of wide-field surveys. With only five dimensions, it becomes practical to ask what each one physically means.

![Figure 3](/iaifi-research-blog/figures/2512_04145/figure_3.png)

Future work could extend Minuet to additional wavelength bands, incorporate time-domain information for transient host characterization, or scale training to the full Rubin dataset.

> **Bottom Line:** Minuet compresses six million galaxy images into just five numbers each, and those numbers carry real physical meaning, from morphology to star-formation history. It's a bet that the universe, for all its complexity, keeps its secrets in a surprisingly small space.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">Minuet bridges deep generative modeling with observational astrophysics, using a diffusion autoencoder to extract physically interpretable features from multi-band galaxy imaging without any labeled training data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Five-dimensional latent spaces can be semantically meaningful in scientific domains. Minuet offers a concrete model for interpretable, low-dimensional representation learning with diffusion-based decoders.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By recovering galaxy redshifts, stellar masses, and star-formation rates from raw images encoded in five dimensions, Minuet shows that galaxy evolution physics is embedded in surprisingly compact visual structure, advancing our ability to probe baryonic feedback at scale.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">As the Vera C. Rubin Observatory begins its decade-long survey, Minuet-style compact representations could become essential infrastructure for anomaly detection and fast physical property estimation across billions of galaxies. See [arXiv:2512.04145](https://arxiv.org/abs/2512.04145).</span></div></div>
</div>
