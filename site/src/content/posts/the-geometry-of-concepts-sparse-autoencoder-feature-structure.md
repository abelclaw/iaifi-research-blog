---
abstract: 'Sparse autoencoders have recently produced dictionaries of high-dimensional
  vectors corresponding to the universe of concepts represented by large language
  models. We find that this concept universe has interesting structure at three levels:
  1) The "atomic" small-scale structure contains "crystals" whose faces are parallelograms
  or trapezoids, generalizing well-known examples such as (man-woman-king-queen).
  We find that the quality of such parallelograms and associated function vectors
  improves greatly when projecting out global distractor directions such as word length,
  which is efficiently done with linear discriminant analysis. 2) The "brain" intermediate-scale
  structure has significant spatial modularity; for example, math and code features
  form a "lobe" akin to functional lobes seen in neural fMRI images. We quantify the
  spatial locality of these lobes with multiple metrics and find that clusters of
  co-occurring features, at coarse enough scale, also cluster together spatially far
  more than one would expect if feature geometry were random. 3) The "galaxy" scale
  large-scale structure of the feature point cloud is not isotropic, but instead has
  a power law of eigenvalues with steepest slope in middle layers. We also quantify
  how the clustering entropy depends on the layer.'
arxivId: '2410.19750'
arxivUrl: https://arxiv.org/abs/2410.19750
authors:
- Yuxiao Li
- Eric J. Michaud
- David D. Baek
- Joshua Engels
- Xiaoqing Sun
- Max Tegmark
concepts:
- autoencoders
- sparse models
- feature geometry
- representation learning
- interpretability
- embeddings
- clustering
- linear representation hypothesis
- eigenvalue decomposition
- spectral methods
- dimensionality reduction
- disentangled representations
figures:
- /iaifi-research-blog/figures/2410_19750/figure_1.png
- /iaifi-research-blog/figures/2410_19750/figure_2.png
- /iaifi-research-blog/figures/2410_19750/figure_3.png
pdfUrl: https://arxiv.org/pdf/2410.19750v2
published: '2024-10-10T17:58:47+00:00'
theme: Foundational AI
title: 'The Geometry of Concepts: Sparse Autoencoder Feature Structure'
wordCount: 1114
---

## The Big Picture

Imagine opening a large language model's "mind" and seeing how it organizes concepts — not as a tangled mess of numbers, but as a structured universe with its own geography. Galaxies of related ideas. Brain-like lobes for math and code. Crystals encoding the logical relationships between words. That's exactly what a team of MIT physicists and AI researchers have found lurking inside the hidden layers of modern language models.

For years, the internal workings of LLMs have been largely opaque. We know these systems can write poetry, solve math problems, and debate philosophy — but *how* they do it remains one of the deepest mysteries in AI. Making sense of billions of numbers requires more than raw inspection. It requires finding the right language to describe what's happening inside.

That language may now be available. Using **sparse autoencoders (SAEs)** — tools that analyze a model's internal activity patterns to identify distinct "features," each corresponding roughly to a concept — a team led by Max Tegmark at MIT has mapped the geometry of those concepts across three radically different scales. The result: a richly structured universe that behaves more like a physical system than a random collection of data points.

> **Key Insight:** The concepts inside large language models aren't arranged randomly — they form structured geometric patterns at multiple scales, from crystal-like local clusters to brain-like functional lobes to galaxy-scale distributions following power laws.

## How It Works

At any given moment, a language model's internal signals can be thought of as a blend of many "features," each representing a concept — like "royalty," "Paris," or "negation." Most features are dormant: only a handful switch on for any particular word or sentence. (That's what *sparse* means here — most of the pattern is zero, with just a few active signals.) An SAE is trained to discover which features are active and reconstruct the original signal from them. Think of it as separating a complex chord into its individual notes.

Once you have a dictionary of such features — the researchers use publicly available SAEs trained on the Gemma language model — you can ask: how are these features arranged geometrically? The team examined structure at three scales.

**Scale 1: Crystal Structures**

The classic example of geometric structure in word representations is the parallelogram: *man − woman ≈ king − queen*. The researchers find that SAE features form analogous parallelograms at the concept level, and many such parallelograms tile together into crystal-like structures — for instance, a grid of (country, capital, language, demonym) relationships.

![Figure 1](/iaifi-research-blog/figures/2410_19750/figure_1.png)

Crucially, these parallelograms become *dramatically* cleaner when you remove "distractor" directions — global patterns like word length that contaminate the geometry. The team accomplishes this with **linear discriminant analysis (LDA)**, a statistical technique that filters out background noise, isolating the clean geometric signal from irrelevant variation. After this correction, both parallelogram quality and related "function vectors" (vectors encoding a consistent semantic operation) improve substantially.

**Scale 2: Functional Lobes**

At intermediate scales, the SAE feature space has spatial modularity that resembles the functional organization of a biological brain. Math features cluster together. Code features form their own region. Language-specific features occupy distinct neighborhoods.

The team quantifies this using multiple metrics — including nearest-neighbor locality tests and co-activation clustering — finding that concept clusters at coarse spatial scales are far more localized than you'd expect from random arrangement. Just as neuroscientists use fMRI to identify brain regions that "light up" together, co-occurring SAE features tend to be spatially proximate. At fine scales the clustering is modest, but zoom out far enough and the structure becomes striking.

![Figure 2](/iaifi-research-blog/figures/2410_19750/figure_2.png)

**Scale 3: Large-Scale Anisotropy**

At the largest scale, the full cloud of feature vectors is anything but a uniform sphere. The researchers compute the **eigenvalue spectrum** of the feature covariance matrix — essentially measuring how much the cloud of features stretches in different directions — and find a power-law distribution, a hallmark of structured, non-random systems.

The slope of this power law is steepest in the middle layers of the model, suggesting that intermediate processing stages have the richest geometric structure. **Clustering entropy** — a measure of how evenly features are distributed across concept clusters — varies by layer in consistent patterns, potentially reflecting how the model builds increasingly abstract representations.

![Figure 3](/iaifi-research-blog/figures/2410_19750/figure_3.png)

## Why It Matters

This work sits at the intersection of two urgent questions in AI: *What do language models actually represent?* and *Can we trust what we can't see?* Mechanistic interpretability has made remarkable progress with sparse autoencoders. But understanding individual features is only part of the puzzle. If we want to audit AI systems for hidden goals or deceptive behavior, we need to understand not just what individual concepts look like, but how the entire concept space is organized.

The geometric structure uncovered here opens concrete new directions:

- **Crystal-like local structure** suggests systematic semantic relationships — analogies, transformations, hierarchies — are encoded in precise geometric form, meaning we might "read" a model's internal logic by examining the shapes of these crystals.
- **Brain-like modularity** suggests LLMs develop functional specialization organically during training, not because they were explicitly designed to.
- **Galaxy-scale power laws** hint at deep connections between language model representations and statistical physics — a link Tegmark's group is actively pursuing.

Future work will need to test whether this geometric structure is universal across model families and scales, and whether the "lobes" correspond to computational modules that can be manipulated or interpreted independently. Each question brings us closer to language models we can genuinely understand — not just use.

> **Bottom Line:** Language model concepts aren't just vectors in a void — they form a richly structured geometric universe with crystal-like clusters, brain-like functional lobes, and galaxy-scale power laws, offering a new map for navigating AI interpretability.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work synthesizes tools from statistics, condensed matter physics, and neuroscience to understand the internal structure of large language models — a genuinely cross-disciplinary contribution from MIT's IAIFI.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">By characterizing the geometric structure of sparse autoencoder feature spaces at multiple scales, this research provides new quantitative tools for mechanistic interpretability and for auditing AI systems for hidden or misaligned behaviors.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The discovery of power-law eigenvalue spectra and crystal-like geometric structures in neural concept spaces reveals deep connections between language model representations and the mathematics of physical systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will test whether this geometric structure generalizes across model families and scales, and whether it can be leveraged for AI safety applications; the full paper is available on arXiv and published in *Entropy* (2025).</span></div></div>
</div>
