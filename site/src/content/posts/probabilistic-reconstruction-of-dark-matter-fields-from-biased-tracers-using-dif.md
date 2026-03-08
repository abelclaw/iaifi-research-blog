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
wordCount: 1078
---

## The Big Picture

Imagine trying to map an entire city using only the locations of coffee shops. You know they tend to cluster in busy neighborhoods, but the relationship is messy — some areas have dozens of cafes, others surprisingly few, and the reasons involve rent, foot traffic, cultural history, and dozens of other factors you can't fully measure. Now imagine the "city" is the universe, the "coffee shops" are galaxies, and what you're actually trying to map is dark matter — an invisible substance comprising about 85% of all matter in existence, the scaffolding on which everything else is built.

That's the challenge at the heart of modern cosmology. We can observe galaxies with telescopes. We cannot observe dark matter directly.

The relationship between the two is tangled up in complex physical processes — supernova explosions, the jets of energy that black holes blast into their surroundings, the messy physics of star formation — that no model fully captures. Previous machine learning approaches sidestepped this by training on a single simulation, baking in all of its assumptions and leaving no room for uncertainty.

Researchers at Harvard, MIT, and the Harvard-Smithsonian Center for Astrophysics took a fundamentally different approach: instead of predicting a single dark matter map, they built a model that generates an entire *probability distribution* of possible dark matter fields — capturing not just the most likely answer, but the full range of what we don't know.

> **Key Insight:** By training a diffusion model on over 1,000 simulations with varied cosmological and astrophysical parameters, this work produces probabilistic dark matter reconstructions that honestly reflect uncertainty about galaxy formation — a crucial step toward unbiased cosmological inference.

## How It Works

The core tool is a **diffusion generative model** — the same class of AI that powers image generators like DALL-E and Stable Diffusion, repurposed for physics. Rather than generating pictures of cats from text prompts, this model generates dark matter density maps from stellar mass maps (images showing where galaxies are and how much star-forming material they contain).

Training data comes from **CAMELS** (Cosmology and Astrophysics with MachinE Learning Simulations), a suite of over 1,000 galaxy formation simulations that systematically vary both cosmological parameters — like Ω_m, the matter density of the universe, and σ_8, a measure of how clumpy matter is — and astrophysical parameters controlling the strength of supernova explosions and the jets of energy that black holes push into their surroundings. This diversity is the key innovation: by training across this wide parameter space, the model learns to reconstruct dark matter fields without anchoring to any single set of physical assumptions.

![Figure 1](/iaifi-research-blog/figures/2311_08558/figure_1.png)

Here's how the reconstruction works:

1. **Start with noise.** The model begins with a completely random field — pure static, like a television screen with no signal.
2. **Denoise conditioned on galaxies.** Over 250 iterative refinement steps, a **U-Net neural network** — an hourglass-shaped architecture where information is compressed down through layers and then built back up — progressively removes that noise, guided at each step by the observed stellar mass field. The network learns which dark matter configurations are consistent with the galaxies it sees.
3. **Repeat to get a posterior.** Run this process 100 times and you get 100 different dark matter maps — all consistent with the same galaxy observation, but spanning the genuine uncertainty about what the underlying dark matter looks like.

The result is a **posterior distribution** p(x_DM | x_stars): the full probabilistic answer to "given these galaxies, what could the dark matter field look like?" Rather than committing to a single answer, it expresses a range of possibilities weighted by likelihood. The posterior mean gives the best single estimate; the posterior standard deviation shows where the model is confident (near dense galaxy clusters) and where it's uncertain (in **cosmic filaments** — the vast thread-like bridges of dark matter stretching between galaxy clusters, visible in simulations but not directly traced by stars).

## Why It Matters

![Figure 2](/iaifi-research-blog/figures/2311_08558/figure_1.png)

The statistical results are compelling. Comparing 100 sampled dark matter fields against ground truth from simulations, the model achieves cross-correlations consistently above 0.8 — the generated fields closely track the true spatial clustering of dark matter across scales. Density histograms and power spectra (which capture how matter clusters at different spatial frequencies) match the true distributions with high fidelity. The uncertainty estimates appear well-calibrated: confident where stellar structures directly constrain the dark matter, appropriately uncertain where galaxies provide weak information.

This matters enormously for the future of cosmology. Next-generation surveys like the Vera Rubin Observatory's LSST and the Euclid space telescope will map hundreds of millions of galaxies across cosmic history. Extracting dark matter information from those observations — with honest uncertainty quantification — is essential for testing fundamental physics, measuring dark energy, and probing extensions to the standard cosmological model.

A model that accounts for galaxy formation uncertainty rather than assuming it away is a prerequisite for that science.

The approach also points toward a broader methodological shift: using generative AI not just to make predictions, but to characterize the *space of possibilities* consistent with data. In a field where the gap between observation and theory is often bridged by unverified assumptions, that probabilistic honesty is itself a scientific advance.

> **Bottom Line:** A diffusion model trained on 1,000+ cosmological simulations can reconstruct the invisible dark matter web from galaxy maps — and unlike previous approaches, it tells you not just what the dark matter probably looks like, but *how uncertain that answer is*, which may prove just as valuable.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges deep generative AI and observational cosmology, applying diffusion models — a state-of-the-art machine learning architecture — to one of the most fundamental unmeasurable quantities in physics: the dark matter density field.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper demonstrates that diffusion models trained across heterogeneous simulation suites can produce calibrated, physically meaningful posterior distributions, establishing a template for uncertainty-aware scientific inference with generative AI.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By simultaneously marginalizing over cosmological and astrophysical uncertainties, this approach removes a key systematic bias in dark matter field reconstruction, bringing surveys closer to unbiased constraints on fundamental parameters like Ω_m.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions could apply this framework to 3D reconstructions and real observational data from Euclid and LSST; the work appeared at the Machine Learning and the Physical Sciences Workshop at NeurIPS 2023 (arXiv: available via CAMELS/IAIFI collaboration outputs).</span></div></div>
</div>
