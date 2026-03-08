---
abstract: We perform a reanalysis of the BOSS CMASS DR12 galaxy dataset using a simulation-based
  emulator for the Wavelet Scattering Transform (WST) coefficients. Moving beyond
  our previous works, which laid the foundation for the first galaxy clustering application
  of this estimator, we construct a neural net-based emulator for the cosmological
  dependence of the WST coefficients and the 2-point correlation function multipoles,
  trained from the state-of-the-art suite of \textsc{AbacusSummit} simulations combined
  with a flexible Halo Occupation Distribution (HOD) galaxy model. In order to confirm
  the accuracy of our pipeline, we subject it to a series of thorough internal and
  external mock parameter recovery tests, before applying it to reanalyze the CMASS
  observations in the redshift range $0.46<z<0.57$. We find that a joint WST + 2-point
  correlation function likelihood analysis allows us to obtain marginalized 1$σ$ errors
  on the $Λ$CDM parameters that are tighter by a factor of $2.5-6$, compared to the
  2-point correlation function, and by a factor of $1.4-2.5$ compared to the WST-only
  results. This corresponds to a competitive $0.9\%$, $2.3\%$ and $1\%$ level of determination
  for parameters $ω_c$, $σ_8$ $\&$ $n_s$, respectively, and also to a $0.7\%$ $\&$
  $2.5 \%$ constraint on derived parameters h and $f(z)σ_8(z)$, in agreement with
  the \textit{Planck} 2018 results. Our results reaffirm the constraining power of
  the WST and highlight the exciting prospect of employing higher-order statistics
  in order to fully exploit the power of upcoming Stage-IV spectroscopic observations.
arxivId: '2310.16116'
arxivUrl: https://arxiv.org/abs/2310.16116
authors:
- Georgios Valogiannis
- Sihan Yuan
- Cora Dvorkin
concepts:
- wavelet scattering transform
- simulation-based inference
- emulation
- bayesian inference
- feature extraction
- cosmological simulation
- posterior estimation
- model validation
- dark energy
- halo occupation distribution
- dark matter
- convolutional networks
figures:
- /iaifi-research-blog/figures/2310_16116/figure_1.png
- /iaifi-research-blog/figures/2310_16116/figure_1.png
- /iaifi-research-blog/figures/2310_16116/figure_2.png
- /iaifi-research-blog/figures/2310_16116/figure_2.png
- /iaifi-research-blog/figures/2310_16116/figure_3.png
- /iaifi-research-blog/figures/2310_16116/figure_3.png
pdfUrl: https://arxiv.org/pdf/2310.16116v3
published: '2023-10-24T18:33:11+00:00'
theme: Astrophysics
title: Precise Cosmological Constraints from BOSS Galaxy Clustering with a Simulation-Based
  Emulator of the Wavelet Scattering Transform
wordCount: 1173
---

## The Big Picture

Imagine trying to recognize a face using only the average brightness of a photograph. You'd get something — a rough sense of how light or dark the image is — but you'd miss the wrinkles, the curve of a smile, the specific arrangement of features that makes a face unique.

For decades, cosmologists have relied heavily on the **2-point correlation function** — a statistical tool measuring how likely you are to find two galaxies at any given distance apart. It works. But it throws away a staggering amount of information.

The universe isn't a smooth, uniform distribution of matter. Gravity has spent 13 billion years sculpting gas and dark matter into a cosmic web of filaments (thread-like bridges between galaxy clusters), sheets (flat walls of galaxies), voids (enormous empty bubbles), and halos (dense knots where galaxies take root). This intricate three-dimensional architecture encodes fundamental cosmological parameters — how fast the universe is expanding, how clumpy matter became over time.

The 2-point function captures only the skeleton of this picture. To read the full portrait, you need tools that detect specific textures, shapes, and multi-point arrangements — patterns involving three, four, or more galaxies at once — that pairwise statistics miss entirely.

A team from Harvard and Stanford has now shown that one such tool — the **Wavelet Scattering Transform (WST)**, borrowed from computer vision — can be deployed on real galaxy survey data with a neural network emulator, delivering constraints on cosmological parameters up to six times tighter than the standard approach.

> **Key Insight:** By combining the Wavelet Scattering Transform with the traditional 2-point correlation function and a neural net emulator trained on thousands of simulations, researchers extracted significantly more cosmological information from the same galaxy data — without needing new observations.

## How It Works

The WST takes inspiration from convolutional neural networks but with a crucial difference: it's interpretable. Instead of learning arbitrary filters through training, it applies a fixed bank of wavelet filters (mathematical probes that detect patterns at specific sizes and orientations, like edge-detectors in computer vision) at multiple scales, measures each response, and averages the results. The output is a set of **WST coefficients** — compact numbers describing clustering patterns in a 3D galaxy map, capturing filamentarity (how much galaxies arrange into strands and sheets) and void statistics (the sizes and distribution of empty regions) that the 2-point function cannot see.

![Figure 1](/iaifi-research-blog/figures/2310_16116/figure_1.png)

To use these coefficients for parameter inference, you need to know how they depend on cosmology. Valogiannis, Yuan, and Dvorkin solved this with a **neural network emulator** — a fast surrogate model trained on the **AbacusSummit** simulation suite (thousands of virtual universes run with different cosmological settings). For each simulated cosmology, they modeled the galaxy population using a **Halo Occupation Distribution (HOD)** — a flexible prescription for how many galaxies occupy dark matter halos of given masses. The emulator predicts WST coefficients and 2-point function multipoles for any point in a high-dimensional parameter space in milliseconds rather than hours.

The pipeline runs in four stages:

1. **Train the emulator** on hundreds of AbacusSummit simulations, covering 8 cosmological parameters and flexible HOD parameters
2. **Validate rigorously** with internal and external mock recovery tests — confirming the pipeline recovers the right answers on simulated data with known parameters
3. **Analyze real BOSS CMASS data**, specifically the DR12 galaxy sample in the redshift window 0.46 < z < 0.57
4. **Run a joint likelihood analysis** combining WST coefficients and 2-point correlation function multipoles

![Figure 3](/iaifi-research-blog/figures/2310_16116/figure_2.png)

The validation step was especially thorough. Internal tests used AbacusSummit simulations; external tests used independent galaxy mocks from different simulation codes entirely. An emulator that only works on its training data isn't trustworthy. Successful recovery in both cases confirmed the pipeline was learning genuine cosmological signal, not simulation artifacts.

## Why It Matters

The numbers are striking. Compared to the 2-point correlation function alone, the joint WST + 2PCF analysis shrinks error bars by a factor of **2.5 to 6** across standard **ΛCDM** (Lambda Cold Dark Matter — the current best model of the universe's evolution) parameters. The joint analysis also gains an additional factor of **1.4 to 2.5** over WST alone, showing the two statistics are genuinely complementary.

![Figure 5](/iaifi-research-blog/figures/2310_16116/figure_3.png)

Concretely: a **0.9% measurement of ωc** (cold dark matter density), a **2.3% measurement of σ8** (amplitude of matter fluctuations — how clumpy the universe is on large scales), and a **1% measurement of ns** (spectral tilt of primordial fluctuations). The Hubble parameter h is constrained to **0.7%**, and the growth rate parameter f(z)σ8(z) to **2.5%**. All results are consistent with Planck 2018 measurements — confirming the pipeline is physically sound.

These are competitive constraints from a single galaxy redshift bin and a dataset with years of traditional analysis behind it. The WST didn't slightly improve things; it unlocked substantially more information that was always encoded in those galaxy positions, waiting for the right tool.

Cosmology is entering a golden age of data. Surveys like **DESI**, the **Vera C. Rubin Observatory's LSST**, and **Euclid** will map tens to hundreds of millions of galaxies with unprecedented precision. But precision data is only valuable if you have statistical tools powerful enough to extract the physics inside it.

If the community relies solely on 2-point functions, vast amounts of hard-won observational data will go to waste. This work demonstrates that higher-order statistics — specifically the WST paired with a neural emulator — are ready for prime time on actual survey data, not just forecasts. The methodology is extensible: the same framework can incorporate other beyond-2-point statistics, richer simulations, and more flexible galaxy models. As Stage-IV surveys come online, tools like this won't just be nice to have. They'll be essential.

> **Bottom Line:** The Wavelet Scattering Transform, powered by a neural network emulator trained on thousands of simulations, can squeeze up to six times more cosmological information from existing galaxy data than the standard 2-point correlation function alone — a preview of how AI-enhanced statistics will transform precision cosmology in the DESI and Euclid era.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges machine learning and observational cosmology, applying a computer-vision-derived transform to real galaxy survey data via a neural network emulator — demonstrating that AI methods can be rigorously validated and deployed for fundamental physics inference.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The neural network emulator approach shows how deep learning can serve as a fast, accurate surrogate for expensive simulations, enabling Bayesian inference over high-dimensional cosmological parameter spaces that would otherwise be computationally intractable.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The analysis delivers sub-percent constraints on core ΛCDM parameters — including cold dark matter density, matter fluctuation amplitude, and the Hubble constant — from a single galaxy redshift bin, reaffirming the power of higher-order statistics for precision cosmology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">This pipeline is poised for application to next-generation surveys like DESI and Euclid, where information gains from WST-based analysis will be even more dramatic; the full methodology is detailed in arXiv:2310.16116 by Valogiannis, Yuan, and Dvorkin.</span></div></div>
</div>
