---
abstract: Galaxies are biased tracers of the underlying cosmic web, which is dominated
  by dark matter components that cannot be directly observed. Galaxy formation simulations
  can be used to study the relationship between dark matter density fields and galaxy
  distributions. However, this relationship can be sensitive to assumptions in cosmology
  and astrophysical processes embedded in the galaxy formation models, that remain
  uncertain in many aspects. In this work, we develop a diffusion generative model
  to reconstruct dark matter fields from galaxies. The diffusion model is trained
  on the CAMELS simulation suite that contains thousands of state-of-the-art galaxy
  formation simulations with varying cosmological parameters and sub-grid astrophysics.
  We demonstrate that the diffusion model can predict the unbiased posterior distribution
  of the underlying dark matter fields from the given stellar mass fields, while being
  able to marginalize over uncertainties in cosmological and astrophysical models.
  Interestingly, the model generalizes to simulation volumes approximately 500 times
  larger than those it was trained on, and across different galaxy formation models.
  Code for reproducing these results can be found at https://github.com/victoriaono/variational-diffusion-cdm
arxivId: '2403.10648'
arxivUrl: https://arxiv.org/abs/2403.10648
authors:
- Victoria Ono
- Core Francisco Park
- Nayantara Mudur
- Yueying Ni
- Carolina Cuesta-Lazaro
- Francisco Villaescusa-Navarro
concepts:
- diffusion models
- posterior estimation
- dark matter
- cosmological simulation
- uncertainty quantification
- generative models
- galaxy bias debiasing
- inverse problems
- simulation-based inference
- bayesian inference
- convolutional networks
- out-of-distribution detection
figures:
- /iaifi-research-blog/figures/2403_10648/figure_1.png
- /iaifi-research-blog/figures/2403_10648/figure_1.png
- /iaifi-research-blog/figures/2403_10648/figure_2.png
- /iaifi-research-blog/figures/2403_10648/figure_2.png
- /iaifi-research-blog/figures/2403_10648/figure_3.png
- /iaifi-research-blog/figures/2403_10648/figure_3.png
pdfUrl: https://arxiv.org/pdf/2403.10648v1
published: '2024-03-15T19:31:40+00:00'
theme: Astrophysics
title: 'Debiasing with Diffusion: Probabilistic reconstruction of Dark Matter fields
  from galaxies with CAMELS'
wordCount: 1164
---

## The Big Picture

Imagine mapping a city using only coffee shop locations. You'd get a rough picture (clusters near offices, gaps in residential areas) but you'd miss parks, warehouses, quiet streets. All the structure that coffee shops don't care about. Astronomers face a version of this problem at cosmic scales. Galaxies light up the universe, but they trace something far more vast and invisible: the dark matter web that accounts for 85% of all matter in existence.

Dark matter doesn't emit light or interact with anything we can directly detect. But gravity forces galaxies to cluster along dark matter filaments and halos (vast invisible scaffolding), so the galaxy distribution carries a scrambled, imperfect imprint of the dark matter beneath it. This mismatch, that galaxies are biased tracers of the underlying dark matter, is one of the central challenges in modern cosmology.

Unscrambling it could sharpen our maps of the universe, revealing voids and filaments invisible in galaxy surveys alone. A team from Harvard, MIT, and the Flatiron Institute has built a machine learning model that does exactly this: given a map of where galaxies are, it reconstructs a probabilistic picture of the dark matter hiding underneath, accounting for everything we don't know about how galaxies form.

> **Key Insight:** By training a diffusion generative model on thousands of galaxy formation simulations, researchers can reconstruct dark matter density fields from galaxy observations while properly quantifying the uncertainties introduced by unknown astrophysical physics.

## How It Works

The core tool is a diffusion model, the same class of AI architecture behind image generators like DALL-E and Stable Diffusion. Instead of generating images from text, this model generates dark matter density maps from stellar mass maps. It learns to reverse a gradual noise-injection process: starting from pure random noise and iteratively refining toward a plausible dark matter field consistent with the observed galaxy distribution.

The training data comes from **CAMELS** (Cosmology and Astrophysics with MachinE Learning Simulations), a dataset of thousands of hydrodynamical simulations. These are detailed computer models tracking how both ordinary and dark matter behave under gravity and other physical forces. Each simulation uses different cosmological parameters and different sub-grid physics: small-scale models for star formation, supernova explosions, and black hole feedback that no simulation can resolve directly. By training on this diverse set, the model learns not just one version of the galaxy–dark matter relationship, but the full range of possibilities.

The training setup uses paired 2D maps drawn from three galaxy formation frameworks:

- **Data format:** 256×256 pixel projections of stellar mass and dark matter density
- **Scale:** Simulation boxes 25 h⁻¹ Mpc (~115 million light-years) per side
- **Simulation suites:** ASTRID, IllustrisTNG, and SIMBA, each making fundamentally different physical assumptions about how galaxies form

![Figure 1](figure:1)

What sets this approach apart is the probabilistic posterior. Instead of producing a single best-guess dark matter map, the model generates an ensemble of plausible maps, each consistent with the input galaxy field. Given the same galaxy distribution, multiple dark matter configurations are statistically valid. The model represents all of them, capturing genuine physical uncertainty rather than papering over it.

## Why It Matters

The generalization results here are unusual. The model was trained on small simulation boxes, then applied to IllustrisTNG-300, a simulation roughly 500 times larger in volume. The reconstructed dark matter fields remained statistically accurate, recovering correct power spectra and probability density functions (the statistical fingerprints of how matter clusters at different scales) even on data well outside the training range. That kind of extrapolation is rare. It suggests the model has learned genuine physical relationships, not just shortcuts that work on training data.

![Figure 2](figure:2)

The model also transfers across galaxy formation models. A diffusion model trained only on IllustrisTNG can reconstruct dark matter fields from SIMBA or ASTRID galaxy distributions with reasonable accuracy, despite different feedback physics and noticeably different galaxy populations. This cross-suite robustness matters for real observational data, where we don't know which simulation most accurately describes the universe.

![Figure 4](figure:4)

The approach feeds into two high-priority goals in observational cosmology. First, reconstructed dark matter fields enable **field-level cosmological inference**: extracting information from the full density field, including cosmic voids and filaments, rather than just clustering statistics. Second, by identifying regions with unusually low stellar-to-dark-matter mass ratios, the reconstruction can guide searches for direct dark matter detection signatures.

Upcoming surveys from DESI, Euclid, Roman, and Rubin will deliver galaxy maps of unprecedented size and depth. Turning those observations into constraints on the fundamental nature of dark matter will require exactly this kind of method.

> **Bottom Line:** A diffusion model trained on thousands of diverse galaxy formation simulations can reconstruct probabilistic dark matter density maps from observed galaxy distributions, generalizing to volumes 500× larger than its training data and across entirely different physical models. This opens a path to field-level cosmology with next-generation surveys.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work combines generative AI with cosmological simulation science, using diffusion models trained on the CAMELS suite to recover the invisible dark matter web from observable galaxy distributions.

- **Impact on Artificial Intelligence:** Diffusion models can generalize well beyond their training distribution in scientific contexts, maintaining accuracy on volumes 500× larger than training data and across fundamentally different physical model families.

- **Impact on Fundamental Interactions:** By producing unbiased posterior distributions of dark matter density fields from galaxy observations, this method opens new approaches to field-level cosmological inference and targeted searches for direct dark matter detection in low stellar-to-dark-matter-mass regions.

- **Outlook and References:** Future work will extend this framework to 3D reconstructions and real observational data from DESI and Euclid. Code is available at [github.com/victoriaono/variational-diffusion-cdm](https://github.com/victoriaono/variational-diffusion-cdm) and the paper is on [arXiv:2403.10648](https://arxiv.org/abs/2403.10648).

## Original Paper Details
- **Title:** Debiasing with Diffusion: Probabilistic reconstruction of Dark Matter fields from galaxies with CAMELS
- **arXiv ID:** 2403.10648
- **Authors:** ["Victoria Ono", "Core Francisco Park", "Nayantara Mudur", "Yueying Ni", "Carolina Cuesta-Lazaro", "Francisco Villaescusa-Navarro"]
- **Abstract:** Galaxies are biased tracers of the underlying cosmic web, which is dominated by dark matter components that cannot be directly observed. Galaxy formation simulations can be used to study the relationship between dark matter density fields and galaxy distributions. However, this relationship can be sensitive to assumptions in cosmology and astrophysical processes embedded in the galaxy formation models, that remain uncertain in many aspects. In this work, we develop a diffusion generative model to reconstruct dark matter fields from galaxies. The diffusion model is trained on the CAMELS simulation suite that contains thousands of state-of-the-art galaxy formation simulations with varying cosmological parameters and sub-grid astrophysics. We demonstrate that the diffusion model can predict the unbiased posterior distribution of the underlying dark matter fields from the given stellar mass fields, while being able to marginalize over uncertainties in cosmological and astrophysical models. Interestingly, the model generalizes to simulation volumes approximately 500 times larger than those it was trained on, and across different galaxy formation models. Code for reproducing these results can be found at https://github.com/victoriaono/variational-diffusion-cdm
