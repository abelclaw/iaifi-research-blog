---
abstract: Diffusion generative models have excelled at diverse image generation and
  reconstruction tasks across fields. A less explored avenue is their application
  to discriminative tasks involving regression or classification problems. The cornerstone
  of modern cosmology is the ability to generate predictions for observed astrophysical
  fields from theory and constrain physical models from observations using these predictions.
  This work uses a single diffusion generative model to address these interlinked
  objectives -- as a surrogate model or emulator for cold dark matter density fields
  conditional on input cosmological parameters, and as a parameter inference model
  that solves the inverse problem of constraining the cosmological parameters of an
  input field. The model is able to emulate fields with summary statistics consistent
  with those of the simulated target distribution. We then leverage the approximate
  likelihood of the diffusion generative model to derive tight constraints on cosmology
  by using the Hamiltonian Monte Carlo method to sample the posterior on cosmological
  parameters for a given test image. Finally, we demonstrate that this parameter inference
  approach is more robust to small perturbations of noise to the field than baseline
  parameter inference networks.
arxivId: '2405.05255'
arxivUrl: https://arxiv.org/abs/2405.05255
authors:
- Nayantara Mudur
- Carolina Cuesta-Lazaro
- Douglas P. Finkbeiner
concepts:
- diffusion models
- monte carlo methods
- posterior estimation
- score-based models
- bayesian inference
- inverse problems
- field-level inference
- likelihood estimation
- simulation-based inference
- surrogate modeling
- dark matter
- cosmological simulation
- robustness
- convolutional networks
figures:
- /iaifi-research-blog/figures/2405_05255/figure_1.png
- /iaifi-research-blog/figures/2405_05255/figure_1.png
- /iaifi-research-blog/figures/2405_05255/figure_2.png
- /iaifi-research-blog/figures/2405_05255/figure_2.png
- /iaifi-research-blog/figures/2405_05255/figure_3.png
- /iaifi-research-blog/figures/2405_05255/figure_3.png
pdfUrl: https://arxiv.org/pdf/2405.05255v2
published: '2024-05-08T17:59:03+00:00'
theme: Astrophysics
title: 'Diffusion-HMC: Parameter Inference with Diffusion-model-driven Hamiltonian
  Monte Carlo'
wordCount: 987
---

## The Big Picture

Imagine a detective who can both reconstruct a crime from a single photo and generate realistic crime scene images from a description alone. That dual ability — simulate and deduce — is exactly what cosmologists dream of, and what researchers from Harvard and MIT have now demonstrated for one of physics' deepest questions: what dark matter looks like, and how much of it there is.

Two numbers govern the universe's large-scale structure: **Ω_m** (the fraction of the universe made of matter) and **σ_8** (how unevenly that matter is clumped). These leave subtle fingerprints on the **dark matter density field** — a map of where matter congregates across cosmic scales. Reading those fingerprints back out from an observation means working from effect to cause, and that's notoriously difficult.

Traditional approaches compress the field into a **power spectrum** — a curve capturing structure at each scale — losing information in the process. Richer methods that work directly with the full map require computing how likely a given observation is, which is expensive. Researchers Nayantara Mudur, Carolina Cuesta-Lazaro, and Douglas Finkbeiner have now built a single diffusion model that does both: generate realistic dark matter fields for any cosmology, and work backward from an observed field to tightly constrain Ω_m and σ_8.

> **Key Insight:** By leveraging the approximate likelihood built into a trained diffusion model, the researchers run Hamiltonian Monte Carlo to sample the full posterior over cosmological parameters — achieving tight, noise-robust constraints without bespoke summary statistics.

## How It Works

The foundation is a **denoising diffusion probabilistic model (DDPM)** — the same mathematical machinery behind image generators like Stable Diffusion. The model learns to progressively blur an image into noise, then reverse that process to reconstruct the original. Crucially, it is *conditional*: it takes Ω_m and σ_8 as inputs, learning what dark matter fields look like across a wide range of cosmologies.

Training data comes from the CAMELS Multifield Dataset, drawn from IllustrisTNG simulations. Each simulation tracks 256³ dark matter particles over a 25 Mpc/h volume — roughly 6,000 CPU hours per run. The team trained on 10,500 two-dimensional field slices spanning 700 cosmologies, using a U-Net with **circular convolutions** to respect the periodic boundary conditions of cosmological simulations.

![Figure 1](/iaifi-research-blog/figures/2405_05255/figure_1.png)

Once trained, the model serves two roles:

1. **Forward emulator**: Given Ω_m and σ_8, generate realistic dark matter density fields whose power spectra and higher-order statistics match true simulation outputs across the full parameter range.
2. **Inference engine**: Given an observed field, constrain the parameters that produced it.

The inference step uses **Hamiltonian Monte Carlo (HMC)**, a sampling method borrowed from physics. Think of a ball rolling across a hilly landscape where valleys mark likely parameter combinations — HMC uses gradient information to explore efficiently. The gradients come from the diffusion model itself: by tracking how reconstruction error changes as Ω_m and σ_8 are varied, the team extracts a differentiable approximate likelihood and uses HMC to walk through it, building a full **posterior distribution**.

![Figure 3](/iaifi-research-blog/figures/2405_05255/figure_2.png)

The result is not just a best-fit cosmology but a complete picture of consistent values and their trade-offs. The method also proves resilient under noise. When the researchers added Gaussian noise to test fields and compared Diffusion-HMC against a standard discriminative CNN, the CNN's performance degraded noticeably. The diffusion model held up — trained to denoise fields at every corruption level, it retained structural knowledge of the signal even when noise intruded.

![Figure 5](/iaifi-research-blog/figures/2405_05255/figure_3.png)

![Figure 6](/iaifi-research-blog/figures/2405_05255/figure_3.png)

## Why It Matters

This work sits at the intersection of generative AI and **simulation-based inference (SBI)** — the emerging paradigm for doing statistics when the likelihood is too expensive to compute analytically. The core insight — that a diffusion model's approximate likelihood can drive HMC — is genuinely new. It establishes a broader principle: generative models built for synthesis can be repurposed for analysis, using the same learned probability structure in reverse.

For cosmology, full-field inference rather than power-spectrum compression matters enormously. Non-Gaussian features in the dark matter distribution — significant at small scales where gravity has scrambled initial conditions — carry real information about fundamental physics. Capturing that information with a single trainable model, without hand-crafting bespoke statistics, is a meaningful step forward.

The noise robustness is not a footnote. Upcoming surveys — DESI, the Vera Rubin Observatory's LSST, the Nancy Grace Roman Space Telescope — will generate data at unprecedented scale but also with complex systematic effects. Methods that degrade gracefully under noise are far more valuable than those requiring pristine conditions.

The current model is conditioned only on Ω_m and σ_8; extending it to the full CAMELS parameter space is a natural next step. And since HMC relies on an *approximate* likelihood, quantifying where that approximation breaks down will be essential before applying the method to real survey data.

> **Bottom Line:** A single diffusion model trained on dark matter simulations can both generate realistic cosmic fields and constrain cosmological parameters — with HMC-based inference proving more noise-robust than discriminative neural network baselines, opening a new path toward field-level cosmological analysis with upcoming surveys.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses score-based generative modeling from machine learning with Hamiltonian Monte Carlo from statistical physics, demonstrating that a model built for synthesis can simultaneously serve as a precision measurement tool for cosmological inference.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper establishes a novel dual use of diffusion models — as both generative emulators and approximate likelihood engines — creating a template for deploying generative AI in scientific inverse problems beyond image synthesis.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling full-field inference on dark matter density maps, this approach extracts cosmological constraints beyond power-spectrum summaries, probing non-Gaussian structure that encodes information about matter clustering and fundamental cosmological parameters.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend the framework to real observed fields and the full CAMELS parameter space; the paper is available at arXiv:2405.05849.</span></div></div>
</div>
