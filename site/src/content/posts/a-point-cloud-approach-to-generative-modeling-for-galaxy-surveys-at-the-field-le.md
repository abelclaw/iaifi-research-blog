---
abstract: We introduce a diffusion-based generative model to describe the distribution
  of galaxies in our Universe directly as a collection of points in 3-D space (coordinates)
  optionally with associated attributes (e.g., velocities and masses), without resorting
  to binning or voxelization. The custom diffusion model can be used both for emulation,
  reproducing essential summary statistics of the galaxy distribution, as well as
  inference, by computing the conditional likelihood of a galaxy field. We demonstrate
  a first application to massive dark matter haloes in the Quijote simulation suite.
  This approach can be extended to enable a comprehensive analysis of cosmological
  data, circumventing limitations inherent to summary statistic -- as well as neural
  simulation-based inference methods.
arxivId: '2311.17141'
arxivUrl: https://arxiv.org/abs/2311.17141
authors:
- Carolina Cuesta-Lazaro
- Siddharth Mishra-Sharma
concepts:
- diffusion models
- generative models
- point cloud diffusion
- likelihood estimation
- field-level inference
- graph neural networks
- cosmological simulation
- transformers
- dark matter
- emulation
- density estimation
- geometric deep learning
- simulation-based inference
- bayesian inference
figures:
- /iaifi-research-blog/figures/2311_17141/figure_1.png
- /iaifi-research-blog/figures/2311_17141/figure_1.png
- /iaifi-research-blog/figures/2311_17141/figure_2.png
- /iaifi-research-blog/figures/2311_17141/figure_2.png
- /iaifi-research-blog/figures/2311_17141/figure_3.png
- /iaifi-research-blog/figures/2311_17141/figure_3.png
pdfUrl: https://arxiv.org/pdf/2311.17141v2
published: '2023-11-28T19:00:00+00:00'
theme: Astrophysics
title: A point cloud approach to generative modeling for galaxy surveys at the field
  level
wordCount: 1107
---

## The Big Picture

Imagine trying to describe a night sky by first drawing a grid over it, counting how many stars fall in each box, and analyzing those counts. You'd lose something essential — the precise positions, the clustering patterns at small scales, the relationships between individual stars. This is roughly what cosmologists have been forced to do when studying the large-scale structure of the universe: take a three-dimensional map of millions of galaxies and compress it into a pixelized grid before a computer can begin to analyze it.

The universe's galaxies aren't a smeared-out fog. They're discrete objects — points in space, each with a position, a velocity, a mass. The "cosmic web" — the spider-web-like pattern of galaxy filaments, empty voids, and dense clusters — is encoded in *where* those points sit relative to each other.

Yet nearly every machine learning approach to cosmology has demanded that this point cloud get converted into a three-dimensional grid of boxes (voxelized) first, trading precision for computational convenience. Every conversion discards fine-scale detail and forces arbitrary choices about grid resolution.

Researchers Carolina Cuesta-Lazaro and Siddharth Mishra-Sharma at MIT and Harvard have built a generative model that treats galaxy catalogs the way they actually are: a collection of points in 3D space.

> **Key Insight:** By applying diffusion models directly to point clouds — no voxels, no grids — this approach can both *generate* realistic galaxy distributions and *evaluate* the likelihood of observed configurations, opening a direct path to field-level cosmological inference.

## How It Works

The core engine is a **diffusion model** — the same class of algorithm powering modern AI image generators like DALL-E and Stable Diffusion. Diffusion models learn to reverse a noise-addition process: during training, you gradually corrupt data with Gaussian noise until it becomes pure static, then teach a neural network to run that process backward. At inference time, you start from noise and iteratively denoise your way to a realistic sample.

![Figure 1](/iaifi-research-blog/figures/2311_17141/figure_1.png)

The twist here is that the "data" isn't an image — it's a set of 3D coordinates (and optionally velocities and masses) for thousands of **dark matter halos**, the gravitationally bound clumps of dark matter that host galaxies. Standard diffusion architectures assume a fixed grid; this one doesn't.

The denoising network is built around two architectures that naturally handle unordered sets of points:

- **Graph neural networks (GNNs):** Build a local neighborhood graph connecting each halo to its nearest neighbors, then pass messages between nodes to capture spatial correlations.
- **Transformers:** Use attention mechanisms to let every halo "look at" every other halo, weighting interactions by relevance.

Both architectures respect two critical symmetries. The output shouldn't change if you shuffle the order of the input points (**permutation equivariance**), and it should transform predictably if you rotate or translate the whole catalog (**geometric equivariance**). These symmetries aren't just aesthetic — they're physically required and dramatically reduce the training data needed.

Training data comes from the **Quijote simulation suite**, a large library of N-body cosmological simulations — computer models that track gravitational interactions among millions of particles to simulate how cosmic structure forms — spanning a range of cosmological parameters like matter density (Ω_m) and the amplitude of primordial fluctuations (σ_8).

![Figure 2](/iaifi-research-blog/figures/2311_17141/figure_1.png)

Once trained, the model does two things. **Emulation:** sample new halo catalogs consistent with a given cosmology, acting as a fast surrogate for expensive N-body simulations. **Inference:** compute the conditional likelihood p(x|θ) — the probability that a specific observed galaxy field arose from a given set of cosmological parameters — which is the quantity needed for Bayesian parameter estimation, the statistical framework for determining which physical parameters best explain observed data.

## Why It Matters

The standard toolkit for extracting cosmological information from galaxy surveys relies on **summary statistics** — compressed descriptions like the two-point correlation function, which measures how galaxies cluster in pairs as a function of separation. Summary statistics are well-understood and mathematically tractable. But they're lossy.

Recent work has shown that alternative summaries can more than double the extractable information from existing surveys. But you're still compressing, and every compression discards something.

![Figure 3](/iaifi-research-blog/figures/2311_17141/figure_2.png)

Field-level inference — working directly with the full galaxy catalog rather than any compressed version — is the holy grail. It promises to use *all* available information. The obstacle has been fundamental and computational: computing p(x|θ) requires integrating over an astronomical space of possible cosmic histories.

This point cloud diffusion model sidesteps that problem by *learning* the likelihood from simulations, without voxelizing the data or reducing it to summary statistics. The authors demonstrate that their model correctly captures key statistical properties — including power spectra (measures of how strongly galaxies cluster at different spatial scales) and two-point functions — and that these shift with cosmological parameters in physically expected ways.

The approach complements rather than replaces **neural simulation-based inference (SBI)** methods. SBI typically compresses data to a learned summary before inference; field-level point cloud models can skip that compression entirely, preserving more information for the final parameter constraints.

Future extensions will incorporate baryonic physics (the behavior of ordinary matter — gas and stars — beyond dark matter), luminosities, and colors. The team also plans to add realistic observational effects like survey masks and redshift-space distortions (the way galaxy velocities subtly distort their apparent positions in sky maps), and to scale to full catalogs from upcoming surveys like DESI, Euclid, and the Rubin Observatory.

> **Bottom Line:** Treating galaxies as point clouds rather than pixels lets diffusion models learn the full statistical structure of cosmic large-scale structure — enabling both fast simulation and rigorous likelihood-based inference without the information loss of voxelization or summary statistics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies state-of-the-art generative AI — diffusion models with equivariant neural networks — directly to field-level inference from galaxy surveys, demonstrating a concrete path from machine learning methods to fundamental physics constraints.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper develops permutation- and geometrically-equivariant diffusion architectures for point cloud data, advancing generative modeling of irregular, variable-size 3D point sets well beyond the image and voxel domains where diffusion models have traditionally operated.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling likelihood-based inference directly on the galaxy field without voxelization or summary compression, this approach opens a route to extracting maximal cosmological information from large-scale structure surveys — potentially sharpening constraints on dark matter, dark energy, and the universe's initial conditions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend the framework to baryonic effects, observational systematics, and full galaxy catalogs from DESI and Euclid; code is publicly available and the paper is available as arXiv preprint (MIT-CTP/5651) by Cuesta-Lazaro & Mishra-Sharma.</span></div></div>
</div>
