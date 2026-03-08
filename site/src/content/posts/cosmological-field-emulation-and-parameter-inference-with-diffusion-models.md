---
abstract: Cosmological simulations play a crucial role in elucidating the effect of
  physical parameters on the statistics of fields and on constraining parameters given
  information on density fields. We leverage diffusion generative models to address
  two tasks of importance to cosmology -- as an emulator for cold dark matter density
  fields conditional on input cosmological parameters $Ω_m$ and $σ_8$, and as a parameter
  inference model that can return constraints on the cosmological parameters of an
  input field. We show that the model is able to generate fields with power spectra
  that are consistent with those of the simulated target distribution, and capture
  the subtle effect of each parameter on modulations in the power spectrum. We additionally
  explore their utility as parameter inference models and find that we can obtain
  tight constraints on cosmological parameters.
arxivId: '2312.07534'
arxivUrl: https://arxiv.org/abs/2312.07534
authors:
- Nayantara Mudur
- Carolina Cuesta-Lazaro
- Douglas P. Finkbeiner
concepts:
- diffusion models
- cosmological simulation
- emulation
- posterior estimation
- dark matter
- surrogate modeling
- score-based models
- simulation-based inference
- likelihood estimation
- convolutional networks
- spectral methods
- attention mechanisms
figures:
- /iaifi-research-blog/figures/2312_07534/figure_2.png
- /iaifi-research-blog/figures/2312_07534/figure_2.png
- /iaifi-research-blog/figures/2312_07534/figure_3.png
pdfUrl: https://arxiv.org/pdf/2312.07534v1
published: '2023-12-12T18:58:42+00:00'
theme: Astrophysics
title: Cosmological Field Emulation and Parameter Inference with Diffusion Models
wordCount: 1111
---

## The Big Picture

Imagine trying to understand the entire universe by running a single physics experiment, except each "experiment" costs millions of CPU hours and weeks of supercomputer time. That's the reality facing modern cosmologists. To test theories about how matter clumped together after the Big Bang, physicists run **N-body simulations**, massive calculations that track how gravity pulls dark matter into the vast cosmic web of filaments, voids, and galaxy clusters we observe today.

The problem? You can only run a handful of these simulations in a lifetime of research. And the universe has a staggering number of knobs to turn.

Enter the emulator: a shortcut model that predicts what a simulation would produce at a fraction of the cost. The cosmic structures these simulations produce aren't smooth or regular. They carry complex, irregular patterns encoding subtle physical signatures, and if your emulator gets those patterns even slightly wrong, any scientific conclusions built on it could be misleading.

Researchers from Harvard and IAIFI at MIT have now shown that **diffusion models**, the same class of AI that powers image generators like Stable Diffusion, can serve as faithful cosmological emulators. They can even run the problem in reverse: given an observed patch of the universe, the model works backward to pin down the fundamental constants governing how matter distributes itself across the cosmos.

> **Key Insight:** A single diffusion model can both *generate* realistic dark matter density fields conditioned on cosmological parameters and *infer* those parameters from new fields, unifying two tasks that usually require separate pipelines.

## How It Works

The researchers trained their model on the **CAMELS Multifield Dataset**, a collection of cold dark matter density fields (maps showing how invisible dark matter distributes across space) drawn from IllustrisTNG simulations. The dataset spans 1,000 points in parameter space, with 15 field realizations each. Every field covers a 25 h⁻¹ Mpc patch of the universe, tens of millions of light-years, at redshift z = 0: a snapshot of the cosmos today.

The core architecture is a **denoising diffusion probabilistic model (DDPM)**, a neural network that learns to reverse a gradual noising process. Think of it like teaching a network to restore a painting from static. You corrupt the original with noise in small, controlled steps, then train the model to undo them. At inference time, you start from pure noise and let the model sculpt it into a realistic cosmic field.

![Figure 1](/iaifi-research-blog/figures/2312_07534/figure_2.png)

Two design choices made the physics work:

- **Circular convolutions** in the downsampling layers wrap computations around the map's edges, matching the periodic boundary conditions of cosmological simulations, where the field wraps around like a video game map. Standard convolutions would have introduced spurious edge artifacts.
- **Conditioning on cosmological parameters**: the matter density **Ωm** (how much matter exists relative to total energy content) and the amplitude of density fluctuations **σ8** (how "lumpy" the universe is on large scales). Each ResNet block in the U-Net receives the parameter vector as additional input, so the model learns how large-scale structure shifts as you dial these values.

Training proceeded in two stages. First, train on downsampled 64×64 images for 60,000 iterations to learn coarse structure. Then initialize a 256×256 model with those weights and continue for over 500,000 iterations. This curriculum approach drove noticeably faster convergence on full-resolution fields. To verify quality, the team measured a reduced chi-squared statistic on the **power spectrum**, a measure of how much structure exists at each size scale, across 10 validation parameter points.

The generated fields' power spectra matched the simulated distribution closely for three validation parameter sets, with z-scores near zero across nearly all wavenumber bins. The best checkpoint achieved a mean reduced chi-squared of 1.30, versus 1.27 for actual simulation samples. A perfect match scores 1.0. These numbers put the diffusion model's fields statistically on par with real simulations.

![Figure 2](/iaifi-research-blog/figures/2312_07534/figure_2.png)

The model also captures differential signatures. Increasing Ωm boosts power across all scales and shifts the pixel value distribution. Changes in σ8 affect only large scales. These are physically meaningful distinctions the model picked up without being explicitly told.

For parameter inference, the team exploited the **variational lower bound (VLB)** on the log likelihood, a score that diffusion models compute as a byproduct of training. It measures how well a given parameter set explains an observed field. Scanning over parameter space and finding the maximum yields a posterior estimate over which parameter values best explain the data. The constraints were tight, and no additional training was required.

## Why It Matters

Cosmology is entering a data-rich era. Surveys like DESI, Euclid, and the Rubin Observatory's LSST are mapping the universe at unprecedented scale. Extracting parameter constraints from these maps means comparing observations to theoretical predictions, and that comparison is only as good as your emulator. If the emulator misses subtle correlations, you get biased parameter estimates. Diffusion models, with their ability to capture the full distribution of field statistics, offer a path to more faithful emulation.

The dual-use nature of this framework stands out. Emulation and inference are traditionally separate pipelines with separate models. Here, a single trained network handles both directions: generate fields from parameters, or infer parameters from fields. That could simplify the cosmological analysis workflow considerably, especially as **field-level inference** (analyzing the full density map rather than compressing it to a handful of summary statistics) becomes standard practice.

Open questions remain. How well does the model generalize beyond its training parameter range? Can it extend to three-dimensional fields or baryonic matter, which is messier to simulate? Can the inference approach compete with dedicated methods like neural posterior estimation? The work provides a strong foundation for tackling all of them.

> **Bottom Line:** Diffusion models trained on cosmological simulations can generate statistically faithful dark matter density fields *and* recover tight cosmological parameter constraints, doing with one neural network what previously required two separate modeling pipelines.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects generative AI and observational cosmology, showing that the diffusion model architecture powering modern image synthesis can faithfully encode the physical statistics of the cosmic web.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Conditional diffusion models can function simultaneously as high-fidelity scientific emulators and probabilistic inference engines, extending their utility well beyond creative image generation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By accurately emulating cold dark matter density fields and recovering tight constraints on Ωm and σ8, this approach offers a scalable path to field-level cosmological inference from next-generation surveys.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend this framework to 3D fields, baryonic tracers, and larger parameter spaces. The paper was presented at the Machine Learning and the Physical Sciences Workshop at NeurIPS 2023. [arXiv:2312.07534](https://arxiv.org/abs/2312.07534)</span></div></div>
</div>
