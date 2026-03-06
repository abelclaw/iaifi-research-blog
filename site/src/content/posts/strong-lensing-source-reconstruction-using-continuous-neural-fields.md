---
abstract: From the nature of dark matter to the rate of expansion of our Universe,
  observations of distant galaxies distorted through strong gravitational lensing
  have the potential to answer some of the major open questions in astrophysics. Modeling
  galaxy-galaxy strong lensing observations presents a number of challenges as the
  exact configuration of both the background source and foreground lens galaxy is
  unknown. A timely call, prompted by a number of upcoming surveys anticipating high-resolution
  lensing images, demands methods that can efficiently model lenses at their full
  complexity. In this work, we introduce a method that uses continuous neural fields
  to non-parametrically reconstruct the complex morphology of a source galaxy while
  simultaneously inferring a distribution over foreground lens galaxy configurations.
  We demonstrate the efficacy of our method through experiments on simulated data
  targeting high-resolution lensing images similar to those anticipated in near-future
  astrophysical surveys.
arxivId: '2206.14820'
arxivUrl: https://arxiv.org/abs/2206.14820
authors:
- Siddharth Mishra-Sharma
- Ge Yang
concepts:
- continuous neural fields
- gravitational lensing
- inverse problems
- posterior estimation
- bayesian inference
- simulation-based inference
- differentiable rendering
- uncertainty quantification
- physics-informed neural networks
- dark matter
- superresolution
figures:
- /iaifi-research-blog/figures/2206_14820/figure_1.png
- /iaifi-research-blog/figures/2206_14820/figure_2.png
- /iaifi-research-blog/figures/2206_14820/figure_3.png
pdfUrl: https://arxiv.org/pdf/2206.14820v2
published: '2022-06-29T18:00:01+00:00'
theme: Astrophysics
title: Strong Lensing Source Reconstruction Using Continuous Neural Fields
wordCount: 1044
---

## The Big Picture

Imagine holding a magnifying glass over a photograph — but instead of a glass lens, it's an entire galaxy, and instead of a photograph, it's another galaxy billions of light-years away. That's gravitational lensing: massive objects curve the fabric of space, and light traveling through that curved space bends along with it. When the geometry aligns, the foreground galaxy warps and stretches the background source into arcs, rings, and multiple images. It's one of the most spectacular phenomena in observational astronomy.

It's also one of the most powerful scientific tools we have. Strong gravitational lensing has been used to measure the expansion rate of the Universe, probe dark matter abundance, and reveal distant galaxies too faint to detect directly. But there's a fundamental problem: when you look at a lensed image, you're seeing a distorted projection of something you've never seen directly.

The true shape of the background source galaxy and the mass distribution of the foreground lens are both unknown simultaneously. Disentangling them is like reconstructing a face and the shape of a funhouse mirror at once, using only the distorted reflection — a puzzle with many solutions that fit the data equally well.

Researchers Siddharth Mishra-Sharma and Ge Yang have developed a new approach that treats the source galaxy not as a pixelized grid or a simple mathematical profile, but as a **continuous neural field** — a small neural network queried at any point in space to return a brightness value. Combined with principled statistical inference over lens parameters, their method reconstructs complex, high-resolution galaxy morphologies from lensed images, all at once.

> **Key Insight:** By representing the source galaxy as a continuous neural field, this method sidesteps the limitations of pixel grids and analytic profiles, enabling unconstrained reconstruction of arbitrarily complex galaxy shapes while simultaneously inferring the lens mass distribution.

## How It Works

The approach follows an "analysis by synthesis" philosophy: rather than directly inverting the lensed image, the method builds a forward model — a **differentiable renderer** (a physics simulator designed so that optimization algorithms can systematically adjust its inputs to better match observed data) — that simulates what any source galaxy would look like after being lensed by a given foreground mass. Then it optimizes backward, asking: what source and lens configuration best explains the observed image?

![Figure 1](/iaifi-research-blog/figures/2206_14820/figure_1.png)

The pipeline has three main components:

1. **The differentiable lensing simulator.** Built on `gigalens`, a JAX-based gravitational lensing package, the renderer centers on the lens equation *β = θ − φ(θ)*, which maps positions in the lens plane (*θ*) to positions in the source plane (*β*) via a deflection vector *φ*. The foreground lens mass is modeled as a **Singular Isothermal Ellipsoid (SIE)** — a standard model for galactic mass distributions shaped like a stretched sphere — with 7 free parameters including the Einstein radius (the characteristic angular scale of the lensing effect), source-lens offset, eccentricities, and external shear.

2. **The neural source representation.** Instead of a pixel grid (resolution-fixed) or a **Sérsic profile** (a smooth mathematical curve commonly used to describe galaxy brightness, but too rigid for irregular shapes), the source is encoded in a small neural network *F_Θ: ℝ² → ℝ²*. Feed it any (x, y) coordinate in the source plane and it returns the brightness there. This continuous neural field represents arbitrarily complex morphologies at any resolution and remains fully differentiable — gradients flow through the source representation during optimization.

3. **Variational inference over everything.** With both the source (neural network weights) and the lens (7 physical parameters) as unknowns, the method applies **gradient-based variational inference** — a technique for efficiently mapping the full range of plausible solutions consistent with the data — to simultaneously optimize the neural field and estimate a probability distribution over lens parameters. This probabilistic treatment is essential: rather than a single best-fit answer, it yields a **posterior** that captures our uncertainty about the lens configuration.

![Figure 2](/iaifi-research-blog/figures/2206_14820/figure_2.png)

The results on simulated data are striking. Tested on a mock lensed image of galaxy NGC2906, the reconstructed source closely matches the true source, with residuals consistent with noise. The predicted lensed image agrees with the true observation at the noise level, and the recovered posterior over lens parameters correctly encompasses the true values.

## Why It Matters

A new generation of telescopes — JWST, the Euclid space mission, and the Extremely Large Telescope — is already delivering or will soon deliver high-resolution lensing images at unprecedented scale. Surveys are expected to discover tens of thousands of strong lenses. Traditional methods, which rely on pixelized source reconstructions with hand-tuned regularization or simple analytic profiles, will struggle to keep pace with either the volume or the resolution of this data.

The continuous neural field approach scales naturally. The source network doesn't commit to a resolution at the outset, and the fully differentiable pipeline — from source coordinates through the physics simulator to observed pixels — enables end-to-end gradient-based optimization that modern deep learning infrastructure is built for. Downstream science, from measuring the Hubble constant to detecting dark matter substructure, requires accurate probabilistic modeling of both source and lens. This method provides exactly that.

> **Bottom Line:** Neural fields offer a flexible, resolution-independent way to reconstruct complex galaxy morphologies from gravitational lensing observations — and combining them with differentiable physics simulators and variational inference enables principled uncertainty quantification over both source and lens, precisely what next-generation surveys will demand.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges neural representation learning with observational astrophysics, applying continuous neural fields to a classical inverse problem in gravitational lensing that has resisted clean solutions for decades.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper demonstrates that implicit neural representations, typically used in computer vision for 3D scene reconstruction, transfer powerfully to physics-driven inverse problems when embedded in a differentiable simulation framework with variational inference.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling high-fidelity, probabilistic reconstruction of strongly lensed source galaxies, this method improves our ability to probe dark matter substructure and measure cosmological parameters like the Hubble constant from next-generation survey data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend this approach to real telescope data and explore more expressive lens mass models; the full method is described in arXiv:2206.14820, presented at ICML 2022.</span></div></div>
</div>
