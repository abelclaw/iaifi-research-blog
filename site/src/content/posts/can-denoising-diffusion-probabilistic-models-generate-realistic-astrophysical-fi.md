---
abstract: 'Score-based generative models have emerged as alternatives to generative
  adversarial networks (GANs) and normalizing flows for tasks involving learning and
  sampling from complex image distributions. In this work we investigate the ability
  of these models to generate fields in two astrophysical contexts: dark matter mass
  density fields from cosmological simulations and images of interstellar dust. We
  examine the fidelity of the sampled cosmological fields relative to the true fields
  using three different metrics, and identify potential issues to address. We demonstrate
  a proof-of-concept application of the model trained on dust in denoising dust images.
  To our knowledge, this is the first application of this class of models to the interstellar
  medium.'
arxivId: '2211.12444'
arxivUrl: https://arxiv.org/abs/2211.12444
authors:
- Nayantara Mudur
- Douglas P. Finkbeiner
concepts:
- diffusion models
- score-based models
- cosmological simulation
- generative models
- dark matter
- emulation
- minkowski functionals
- inverse problems
- convolutional networks
- generative adversarial networks
- spectral methods
- normalizing flows
- cosmic microwave background
figures:
- /iaifi-research-blog/figures/2211_12444/figure_1.png
- /iaifi-research-blog/figures/2211_12444/figure_2.png
- /iaifi-research-blog/figures/2211_12444/figure_3.png
pdfUrl: https://arxiv.org/pdf/2211.12444v1
published: '2022-11-22T17:54:47+00:00'
theme: Astrophysics
title: Can denoising diffusion probabilistic models generate realistic astrophysical
  fields?
wordCount: 939
---

## The Big Picture

Imagine trying to map the skeleton of the universe, the vast, invisible scaffolding of dark matter that holds galaxies together, using only a handful of expensive simulations. Each cosmological simulation costs thousands of CPU hours, and scientists need thousands of them to probe the full range of possible universes. Now imagine a machine that could generate statistically faithful replicas of that cosmic skeleton on demand, for free. That's what Harvard physicists Nayantara Mudur and Douglas Finkbeiner set out to test.

They asked whether AI systems that generate images by learning to remove noise (the same technology behind tools like DALL-E or Midjourney) could learn and reproduce the statistics of two very different astrophysical datasets: simulated dark matter density fields and real images of interstellar dust. These aren't pretty photographs. They're scientific data products where every pixel encodes physical information, and getting the statistics wrong would make a model scientifically useless.

What they deliver is a proof of concept: AI-generated astrophysical fields that could supplement or replace expensive simulations, plus AI-powered denoising tools that can clean up dirty astronomical observations.

> **Key Insight:** DDPMs can generate cosmological dark matter fields that match many statistical properties of real simulations, and can be repurposed as a denoiser for interstellar dust images. This is the first time this class of model has been applied to the interstellar medium.

## How It Works

The core idea is intuitive. Start with a real image and gradually bury it in noise over hundreds of steps until it's pure static. Then train a neural network to reverse that process, denoising one small step at a time, learning the underlying structure of the data. To generate something new, start with random noise and let the network walk it backward into a plausible image.

![Figure 1](figure:1)

Mudur and Finkbeiner trained two separate models. One learned from **cold dark matter mass density fields**, maps showing how dark matter is distributed across a simulated patch of the universe, drawn from the CAMELS simulation suite. The other learned from patches of an interstellar dust map. For the dark matter application, they used log-transformed density fields at two resolutions (64×64 and 128×128 pixels) spanning a wide range of cosmological and astrophysical parameters across 1,000 simulations.

The 128×128 model trained on 252,000 augmented fields using rotations, flips, and translational shifts. The architecture is a U-Net with ResNet blocks, group normalization, and attention layers, trained for 60,000 iterations under a linear noise schedule from 10⁻⁴ to 2×10⁻² over T=2,000 steps.

The real question: do the generated fields actually *look* like the real ones, statistically? The team measured fidelity using three complementary metrics:

- **Power spectrum**: how much structure exists at each spatial scale, the cosmic equivalent of a sound's frequency content
- **Pixel intensity histograms**: whether the distribution of density values matches the real data
- **Minkowski functionals**: topological descriptors sensitive to non-Gaussian structure, capturing the connectivity and curvature of dense regions that simpler statistics miss

![Figure 2](figure:2)

## Why It Matters

The results are promising but mixed. Generated fields capture many statistical features of the real data, but the team also identifies real shortcomings. At 128×128, discrepancies appear in the Minkowski functionals, pointing to gaps in the model's grasp of topological structure. This matters for science: a model that looks visually plausible but fails topological tests would produce systematically biased cosmological inferences. The honest accounting here is what distinguishes careful benchmarking from hype.

The dust application takes a different angle. Rather than generating new dust images for their own sake, Mudur and Finkbeiner repurposed the trained model as a **denoiser**. Given a noisy dust observation, the model uses its learned prior about what real dust looks like to reconstruct the underlying signal. Cleaned-up dust maps could help astronomers working to subtract foreground dust contamination from Cosmic Microwave Background observations, where precision matters enormously.

The path to full scientific utility runs through conditional generation. Right now these models generate fields unconditionally, pulling random draws from the learned distribution. The next step is conditioning on specific cosmological parameters, which would make diffusion models viable as fast emulators for parameter inference. If a researcher wants to know what dark matter looks like when the matter density Ω_m shifts slightly, a conditional model could answer in seconds instead of days.

> **Bottom Line:** Diffusion models can generate astrophysical fields with realistic statistics and double as scientifically useful denoisers. This is a credible first step toward AI emulators that could make expensive cosmological simulations far more accessible.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects the diffusion model framework behind modern text-to-image systems to cosmological science, benchmarking AI-generated fields against physical statistics including Minkowski functionals and power spectra.

- **Impact on Artificial Intelligence:** The paper provides one of the first systematic evaluations of diffusion models on scientific data distributions, going beyond visual fidelity to measure statistical and topological consistency, a standard that matters when AI tools are used for physical inference.

- **Impact on Fundamental Interactions:** By showing that diffusion models can reproduce the statistical properties of dark matter density fields, this work points toward fast AI emulators for cosmological parameter inference and improved dust foreground models for CMB polarization searches.

- **Outlook and References:** Future work will focus on conditional generation tied to specific cosmological parameter vectors, unlocking the emulator potential of this approach. The paper is available at [arXiv:2211.12444](https://arxiv.org/abs/2211.12444).

## Original Paper Details
- **Title:** Can denoising diffusion probabilistic models generate realistic astrophysical fields?
- **arXiv ID:** [2211.12444](https://arxiv.org/abs/2211.12444)
- **Authors:** Nayantara Mudur, Douglas P. Finkbeiner
