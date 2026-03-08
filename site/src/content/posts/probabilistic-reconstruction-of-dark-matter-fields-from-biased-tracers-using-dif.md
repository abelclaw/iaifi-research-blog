---
abstract: Galaxies are biased tracers of the underlying cosmic web, which is dominated
  by dark matter components that cannot be directly observed. The relationship between
  dark matter density fields and galaxy distributions can be sensitive to assumptions
  in cosmology and astrophysical processes embedded in the galaxy formation models,
  that remain uncertain in many aspects. Based on state-of-the-art galaxy formation
  simulation suites with varied cosmological parameters and sub-grid astrophysics,
  we develop a diffusion generative model to predict the unbiased posterior distribution
  of the underlying dark matter fields from the given stellar mass fields, while being
  able to marginalize over the uncertainties in cosmology and galaxy formation.
arxivId: '2311.08558'
arxivUrl: https://arxiv.org/abs/2311.08558
authors:
- Core Francisco Park
- Victoria Ono
- Nayantara Mudur
- Yueying Ni
- Carolina Cuesta-Lazaro
concepts:
- diffusion models
- dark matter
- posterior estimation
- cosmological simulation
- uncertainty quantification
- galaxy-dark matter bias
- generative models
- inverse problems
- convolutional networks
- simulation-based inference
- data augmentation
figures:
- /iaifi-research-blog/figures/2311_08558/figure_1.png
- /iaifi-research-blog/figures/2311_08558/figure_1.png
- /iaifi-research-blog/figures/2311_08558/figure_2.png
- /iaifi-research-blog/figures/2311_08558/figure_2.png
- /iaifi-research-blog/figures/2311_08558/figure_3.png
- /iaifi-research-blog/figures/2311_08558/figure_3.png
pdfUrl: https://arxiv.org/pdf/2311.08558v1
published: '2023-11-14T21:40:20+00:00'
theme: Astrophysics
title: Probabilistic reconstruction of Dark Matter fields from biased tracers using
  diffusion models
wordCount: 968
---

## The Big Picture

Imagine trying to map an entire city using only the locations of coffee shops. They cluster in busy neighborhoods, but the relationship is messy. Some areas have dozens of cafes, others surprisingly few, and the reasons involve rent, foot traffic, cultural history, and factors you can't fully measure. Now scale that up: the "city" is the universe, the "coffee shops" are galaxies, and what you're actually trying to map is dark matter, an invisible substance making up about 85% of all matter in existence.

That's the core problem in modern cosmology. We can observe galaxies with telescopes. We cannot observe dark matter directly. And the relationship between the two is tangled up in complex physics: supernova explosions, black hole jets blasting energy into their surroundings, the messy details of star formation. No model fully captures all of it. Previous machine learning approaches sidestepped this by training on a single simulation, baking in all its assumptions and leaving no room for uncertainty.

Researchers at Harvard, MIT, and the Harvard-Smithsonian Center for Astrophysics took a different approach. Instead of predicting a single dark matter map, they built a model that generates an entire *probability distribution* of possible dark matter fields, capturing not just the most likely answer but the full range of what we don't know.

> **Key Insight:** By training a diffusion model on over 1,000 simulations with varied cosmological and astrophysical parameters, this work produces probabilistic dark matter reconstructions that honestly reflect uncertainty about galaxy formation, a step needed for unbiased cosmological inference.

## How It Works

The core tool is a **diffusion generative model**, the same class of AI behind image generators like DALL-E and Stable Diffusion, repurposed for physics. Instead of generating pictures from text prompts, this model generates dark matter density maps from stellar mass maps showing where galaxies are and how much star-forming material they contain.

Training data comes from **CAMELS** (Cosmology and Astrophysics with MachinE Learning Simulations), a suite of over 1,000 galaxy formation simulations. These simulations systematically vary both cosmological parameters (like Ω_m, the matter density of the universe, and σ_8, how clumpy matter is) and astrophysical parameters controlling supernova feedback and black hole jet strength. Training across this wide parameter space is what makes the approach work: the model learns to reconstruct dark matter fields without anchoring to any single set of physical assumptions.

![Figure 1](figure:1)

The reconstruction works in three stages:

1. **Start with noise.** The model begins with a completely random field, pure static.
2. **Denoise conditioned on galaxies.** Over 250 iterative steps, a **U-Net neural network** (an hourglass-shaped architecture that compresses information down through layers, then builds it back up) progressively removes that noise. At each step, the observed stellar mass field guides the process. The network learns which dark matter configurations are consistent with the galaxies it sees.
3. **Repeat to get a posterior.** Run this 100 times and you get 100 different dark matter maps, all consistent with the same galaxy observation but spanning the genuine uncertainty in what the underlying dark matter looks like.

The result is a **posterior distribution** p(x_DM | x_stars): the full probabilistic answer to "given these galaxies, what could the dark matter field look like?" The posterior mean gives the best single estimate. The posterior standard deviation reveals where the model is confident (near dense galaxy clusters) and where it isn't (in **cosmic filaments**, the vast thread-like bridges of dark matter stretching between galaxy clusters, visible in simulations but not directly traced by stars).

## Why It Matters

![Figure 2](figure:2)

The numbers hold up well. Comparing 100 sampled dark matter fields against ground truth from simulations, the model achieves cross-correlations consistently above 0.8. The generated fields closely track the true spatial clustering of dark matter across scales. Density histograms and power spectra match the true distributions with high fidelity, and the uncertainty estimates appear well-calibrated: confident where stellar structures directly constrain the dark matter, appropriately uncertain where galaxies provide weak information.

This has real implications for what's coming next. The Vera Rubin Observatory's LSST and the Euclid space telescope will map hundreds of millions of galaxies across cosmic history. Extracting dark matter information from those observations, with honest uncertainty quantification, is essential for testing fundamental physics and measuring dark energy. A model that accounts for galaxy formation uncertainty rather than assuming it away is a prerequisite for that science.

The approach also represents a broader methodological shift: using generative AI not just to make predictions but to characterize the *space of possibilities* consistent with data. In a field where the gap between observation and theory is often bridged by unverified assumptions, that probabilistic honesty is itself a scientific contribution.

> **Bottom Line:** A diffusion model trained on 1,000+ cosmological simulations can reconstruct the invisible dark matter web from galaxy maps. Unlike previous approaches, it tells you not just what the dark matter probably looks like, but *how uncertain that answer is*, which may prove just as valuable.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects deep generative AI with observational cosmology, applying diffusion models to one of the most fundamental unmeasurable quantities in physics: the dark matter density field.

- **Impact on Artificial Intelligence:** The paper shows that diffusion models trained across heterogeneous simulation suites can produce calibrated, physically meaningful posterior distributions, establishing a template for uncertainty-aware scientific inference with generative AI.

- **Impact on Fundamental Interactions:** By simultaneously marginalizing over cosmological and astrophysical uncertainties, this approach removes a systematic bias in dark matter field reconstruction, bringing surveys closer to unbiased constraints on fundamental parameters like Ω_m.

- **Outlook and References:** Future extensions could apply this framework to 3D reconstructions and real observational data from Euclid and LSST. The work appeared at the Machine Learning and the Physical Sciences Workshop at NeurIPS 2023 ([arXiv:2311.08558](https://arxiv.org/abs/2311.08558)).
