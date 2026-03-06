---
abstract: Strong gravitational lensing has emerged as a promising approach for probing
  dark matter models on sub-galactic scales. Recent work has proposed the subhalo
  effective density slope as a more reliable observable than the commonly used subhalo
  mass function. The subhalo effective density slope is a measurement independent
  of assumptions about the underlying density profile and can be inferred for individual
  subhalos through traditional sampling methods. To go beyond individual subhalo measurements,
  we leverage recent advances in machine learning and introduce a neural likelihood-ratio
  estimator to infer an effective density slope for populations of subhalos. We demonstrate
  that our method is capable of harnessing the statistical power of multiple subhalos
  (within and across multiple images) to distinguish between characteristics of different
  subhalo populations. The computational efficiency warranted by the neural likelihood-ratio
  estimator over traditional sampling enables statistical studies of dark matter perturbers
  and is particularly useful as we expect an influx of strong lensing systems from
  upcoming surveys.
arxivId: '2208.13796'
arxivUrl: https://arxiv.org/abs/2208.13796
authors:
- Gemma Zhang
- Siddharth Mishra-Sharma
- Cora Dvorkin
concepts:
- dark matter
- likelihood ratio
- subhalo effective density slope
- simulation-based inference
- gravitational lensing
- posterior estimation
- inverse problems
- bayesian inference
- convolutional networks
- density estimation
- monte carlo methods
- cosmological simulation
figures:
- /iaifi-research-blog/figures/2208_13796/figure_1.png
- /iaifi-research-blog/figures/2208_13796/figure_2.png
- /iaifi-research-blog/figures/2208_13796/figure_3.png
pdfUrl: https://arxiv.org/pdf/2208.13796v2
published: '2022-08-29T18:00:01+00:00'
theme: Astrophysics
title: Inferring subhalo effective density slopes from strong lensing observations
  with neural likelihood-ratio estimation
wordCount: 949
---

## The Big Picture

Imagine trying to understand the contents of a room by watching shadows on a wall. You can't see the objects directly — only the distorted shapes they cast. At cosmic scales, galaxies bend light from even more distant galaxies into rings, arcs, and multiple images. This is the strange, beautiful science of **strong gravitational lensing**, and it's one of the few tools we have for probing one of the universe's deepest mysteries: dark matter.

Dark matter makes up about 84% of all matter in the universe, yet it emits no light, reflects none, and interacts with ordinary matter only through gravity. We know it exists from its gravitational pull — but figuring out its fundamental nature requires looking at the smallest scales, far below individual galaxies. Sub-galactic clumps called **subhalos** contain no stars, making them essentially invisible except through their gravitational fingerprints on passing light. Strong lensing can detect exactly that.

The challenge: existing methods are either imprecise or grind to a halt computationally when analyzing more than one or two subhalos at a time. Researchers at Harvard and MIT have introduced a machine learning approach — a neural network trained to judge which dark matter model best fits an observed lensing image — that analyzes entire populations of subhalos simultaneously, harvesting statistical power previously out of reach.

> **Key Insight:** By replacing traditional sampling with a trained neural network, this approach combines information from many subhalos across multiple lensing images at once, enabling population-level inferences about dark matter that were previously computationally infeasible.

## How It Works

Most previous studies measured the **subhalo mass function** — a census of subhalo masses — but doing so requires assumptions about internal density profiles in regions not directly observed, introducing systematic errors. Instead, the team focused on the **effective density slope**: how steeply a subhalo's density falls off from its center, measured at the scale where lensing is most sensitive. This slope can be extracted directly from lensing data without assuming any particular profile shape. It's cleaner, more robust, and encodes complementary information about dark matter physics that pure mass measurements miss.

![Figure 1](/iaifi-research-blog/figures/2208_13796/figure_1.png)

The forward model works like this:

1. **Simulate a lensing system**: Use `lenstronomy` to generate mock 100×100 pixel images at 0.08 arcseconds per pixel, including a background source galaxy, a foreground lens galaxy, and a population of dark matter subhalos drawn from some distribution.
2. **Vary the population parameter**: The key parameter is the mean effective density slope — a number that distinguishes cold dark matter (cuspy, concentrated profiles) from alternatives like warm or self-interacting dark matter (cored, less concentrated profiles).
3. **Train a neural network**: The network learns to estimate the **likelihood ratio** — how much more probable one explanation is than another — between two hypotheses: that an image came from a population with slope θ₁ versus slope θ₂.
4. **Deploy across many images**: After training, the network processes new lensing images rapidly, combining evidence from each and multiplying statistical power without multiplying computational cost.

![Figure 2](/iaifi-research-blog/figures/2208_13796/figure_2.png)

The key architectural insight is that the network learns to ignore the noise. A lensing image contains enormous variation in individual subhalo details — exact masses, positions, individual slopes — none of which directly reveals the population-level pattern. The network bypasses measuring any of those individual properties, learning instead to extract only the signal that distinguishes one dark matter population from another. This is **simulation-based inference** — training on realistic simulations, then deploying the trained network on new observations — operating at its most powerful.

## Why It Matters

The timing is not an accident. Upcoming sky surveys — the Euclid space telescope and the Rubin Observatory's Legacy Survey of Space and Time — are expected to increase known strong lensing systems from the current few hundred to potentially hundreds of thousands. Each system contains information about dark matter substructure. Without a computationally efficient analysis method, that information sits unused.

![Figure 3](/iaifi-research-blog/figures/2208_13796/figure_3.png)

Traditional Markov chain Monte Carlo sampling — which works by randomly exploring all possible explanations until it homes in on the ones that best fit the data — scales badly with both the number of subhalos per image and the number of images per dataset. The neural likelihood-ratio approach pays a one-time training cost, then processes each new image in a fraction of a second. That's the difference between a method that handles a handful of systems and one that operates at survey scale. Beyond this immediate application, the work demonstrates how simulation-based inference can be adapted to population-level problems across astrophysics — a template for similarly intractable inference challenges throughout cosmology and beyond.

> **Bottom Line:** By combining a carefully chosen dark matter observable with neural likelihood-ratio estimation, this method unlocks population-level dark matter science from strong gravitational lensing — and grows more powerful with every new lensing system future surveys discover.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges modern machine learning — simulation-based inference and neural likelihood-ratio estimation — with fundamental astrophysics, using AI to unlock population-level dark matter constraints from gravitational lensing data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The approach demonstrates how neural likelihood-ratio estimators can be applied to high-dimensional astrophysical data with large latent spaces, providing a scalable alternative to traditional sampling that generalizes to population-level inference across scientific domains.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling robust measurements of the subhalo effective density slope across populations, this method offers a new, assumption-independent probe of dark matter's fundamental properties at sub-galactic scales.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend this approach to real observational data and incorporate additional systematics such as line-of-sight perturbers; the paper is available at arXiv:2211.13927 (submitted November 2022).</span></div></div>
</div>
