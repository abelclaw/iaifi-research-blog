---
abstract: Direct imaging of exoplanets is crucial for advancing our understanding
  of planetary systems beyond our solar system, but it faces significant challenges
  due to the high contrast between host stars and their planets. Wavefront aberrations
  introduce speckles in the telescope science images, which are patterns of diffracted
  starlight that can mimic the appearance of planets, complicating the detection of
  faint exoplanet signals. Traditional post-processing methods, operating primarily
  in the image intensity domain, do not integrate wavefront sensing data. These data,
  measured mainly for adaptive optics corrections, have been overlooked as a potential
  resource for post-processing, partly due to the challenge of the evolving nature
  of wavefront aberrations. In this paper, we present a differentiable rendering approach
  that leverages these wavefront sensing data to improve exoplanet detection. Our
  differentiable renderer models wave-based light propagation through a coronagraphic
  telescope system, allowing gradient-based optimization to significantly improve
  starlight subtraction and increase sensitivity to faint exoplanets. Simulation experiments
  based on the James Webb Space Telescope configuration demonstrate the effectiveness
  of our approach, achieving substantial improvements in contrast and planet detection
  limits. Our results showcase how the computational advancements enabled by differentiable
  rendering can revitalize previously underexploited wavefront data, opening new avenues
  for enhancing exoplanet imaging and characterization.
arxivId: '2501.01912'
arxivUrl: https://arxiv.org/abs/2501.01912
authors:
- Brandon Y. Feng
- Rodrigo Ferrer-Chávez
- Aviad Levis
- Jason J. Wang
- Katherine L. Bouman
- William T. Freeman
concepts:
- exoplanets
- inverse problems
- differentiable rendering
- wavefront aberration estimation
- signal detection
- surrogate modeling
- coronagraphic imaging
- physics-informed neural networks
- simulation-based inference
- superresolution
- bayesian inference
figures:
- /iaifi-research-blog/figures/2501_01912/figure_1.png
- /iaifi-research-blog/figures/2501_01912/figure_1.png
- /iaifi-research-blog/figures/2501_01912/figure_2.png
- /iaifi-research-blog/figures/2501_01912/figure_2.png
- /iaifi-research-blog/figures/2501_01912/figure_3.png
- /iaifi-research-blog/figures/2501_01912/figure_3.png
pdfUrl: https://arxiv.org/pdf/2501.01912v1
published: '2025-01-03T17:30:44+00:00'
theme: Astrophysics
title: Exoplanet Detection via Differentiable Rendering
wordCount: 1036
---

## The Big Picture

Imagine trying to spot a firefly hovering next to a lighthouse beam, from a hundred miles away. That's roughly the challenge astronomers face when attempting to directly photograph planets around other stars. Earth-like planets can be ten billion times fainter than their host stars, and even the most advanced space telescopes struggle to tease the two apart.

The James Webb Space Telescope has coronagraphs (specialized optics that block starlight like a hand held over the sun) but residual light still bleeds through. It forms ghostly interference patterns called **speckles** that can convincingly impersonate planets.

For decades, astronomers have dealt with speckles by taking reference images and subtracting them, a painstaking process that consumes precious telescope time and still leaves systematic errors. Meanwhile, every major observatory continuously measures the shape of incoming light waves, a process called **wavefront sensing**, to keep their optics precisely aligned. Think of it as the telescope constantly checking and correcting its own vision. This data has been sitting largely untouched as far as planet-hunting is concerned, dismissed as too complex to fold into the analysis pipeline.

Researchers from MIT, Caltech, Northwestern, and the University of Toronto have now found a way to put that overlooked wavefront data to work, using a technique borrowed from computer graphics: **differentiable rendering**.

> **Key Insight:** By building a physics-based, differentiable model of how light propagates through a telescope, this approach uses gradient descent (an optimization algorithm that iteratively nudges parameters toward lower error, like water finding its way downhill) to reconstruct and subtract starlight far more accurately than existing methods, without requiring extra reference observations.

## How It Works

The central idea borrows from a shift in computer vision: differentiable rendering, where you build a mathematical model of image formation precise enough to run gradients through it and optimize parameters directly. In computer graphics, this lets artists tune lighting, geometry, and materials to match a target image. Here, the "scene" is a coronagraphic telescope, and the goal is to precisely reconstruct the star's contribution to every pixel so it can be subtracted.

![Figure 1](figure:1)

The pipeline has three connected stages:

1. **Wavefront estimation.** The system ingests wavefront sensor measurements taken throughout an observation. Because the telescope's optics flex and drift over time, these measurements encode a time-varying map of aberrations: tiny deformations of the incoming light waves that determine exactly which speckle pattern appears in the science image at any given moment.

2. **Differentiable forward model.** The team built a renderer that simulates wave optics from first principles, propagating light through the coronagraph's optical components (including its pupil plane, focal plane mask, and Lyot stop) all the way to the detector. This produces a predicted image of the star's **point spread function** (PSF, the characteristic blur pattern a point source makes on a detector) for a given set of wavefront parameters. Every operation in this chain is differentiable, meaning the system can compute how the predicted image would change if you nudged any parameter.

3. **Gradient-based optimization.** Given the predicted PSF and the actual science image, the optimizer iteratively adjusts the wavefront model to minimize residuals. Because the renderer accounts for physics that empirical methods ignore (how a specific wavefront shape produces a specific speckle at a specific location), it achieves tighter starlight subtraction than statistical post-processing approaches like PCA. Those methods treat the PSF as a pattern to be learned from data rather than physics to be modeled directly.

![Figure 2](figure:2)

One technical wrinkle: wavefront aberrations aren't static. They evolve on multiple timescales as the telescope drifts thermally or mechanically between exposures. The method handles this by treating each exposure's wavefront state as a separate variable to be estimated, while sharing learned parameters (like telescope mirror properties) across the full sequence. This temporal structure lets the model track how speckles evolve rather than assuming they're frozen.

## Why It Matters

The significance here goes beyond a better algorithm for one telescope. Differentiable rendering is already reshaping fields from medical imaging to autonomous driving by enabling physics-aware optimization that purely data-driven models can't match. This work brings that toolkit to astronomy, and the timing matters. JWST is actively collecting coronagraphic data, the Roman Space Telescope is approaching launch, and the proposed Habitable Worlds Observatory targets exactly the problem this technique addresses: detecting Earth-like planets in habitable zones.

![Figure 4](figure:4)

The approach also recasts wavefront sensing data, already collected at every major observatory, as a scientific asset rather than an engineering byproduct. If wavefront telemetry that would otherwise be discarded can feed a differentiable post-processing pipeline, it represents an enormous untapped resource. Future work could extend the approach to ground-based adaptive optics systems, where wavefront sensing runs at kilohertz rates and produces a continuous stream of atmospheric information that current post-processing methods completely ignore.

Open questions remain. The current simulations use JWST-like configurations, and real data will introduce noise sources and instrument systematics that simulations can only approximate. Handling chromatic aberrations, where the speckle pattern shifts with wavelength, would unlock integration with spectral differential imaging. And as differentiable physics simulators grow faster, this approach could eventually run in near-real-time, enabling adaptive observations that respond to the telescope's live optical state.

> **Bottom Line:** By applying differentiable rendering to wavefront sensing data that telescopes already collect, this work achieves substantially better starlight subtraction than conventional methods, potentially expanding the range of directly detectable exoplanets without spending a single additional minute on reference stars.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work embeds wave-optics physics directly into a differentiable computational graph, letting machine learning optimization tackle a fundamental astronomical measurement problem. It's AI-physics integration at its most concrete.

- **Impact on Artificial Intelligence:** The research extends differentiable rendering from computer vision into high-contrast astronomical imaging, showing that physics-informed gradient-based optimization can outperform statistical post-processing on scientific imaging problems.

- **Impact on Fundamental Interactions:** Better exoplanet detection directly advances the search for potentially habitable worlds. The approach has been validated on JWST-configuration simulations and is applicable to the next generation of large space and ground telescopes targeting Earth-like planets.

- **Outlook and References:** Future directions include extension to real on-sky data, chromatic aberration modeling, and ground-based adaptive optics. The work is available as [arXiv:2501.01912](https://arxiv.org/abs/2501.01912).
