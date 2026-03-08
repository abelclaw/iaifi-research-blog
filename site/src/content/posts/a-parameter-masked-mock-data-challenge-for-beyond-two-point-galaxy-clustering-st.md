---
abstract: The last few years have seen the emergence of a wide array of novel techniques
  for analyzing high-precision data from upcoming galaxy surveys, which aim to extend
  the statistical analysis of galaxy clustering data beyond the linear regime and
  the canonical two-point (2pt) statistics. We test and benchmark some of these new
  techniques in a community data challenge "Beyond-2pt", initiated during the Aspen
  2022 Summer Program "Large-Scale Structure Cosmology beyond 2-Point Statistics,"
  whose first round of results we present here. The challenge dataset consists of
  high-precision mock galaxy catalogs for clustering in real space, redshift space,
  and on a light cone. Participants in the challenge have developed end-to-end pipelines
  to analyze mock catalogs and extract unknown ("masked") cosmological parameters
  of the underlying $Λ$CDM models with their methods. The methods represented are
  density-split clustering, nearest neighbor statistics, BACCO power spectrum emulator,
  void statistics, LEFTfield field-level inference using effective field theory (EFT),
  and joint power spectrum and bispectrum analyses using both EFT and simulation-based
  inference. In this work, we review the results of the challenge, focusing on problems
  solved, lessons learned, and future research needed to perfect the emerging beyond-2pt
  approaches. The unbiased parameter recovery demonstrated in this challenge by multiple
  statistics and the associated modeling and inference frameworks supports the credibility
  of cosmology constraints from these methods. The challenge data set is publicly
  available and we welcome future submissions from methods that are not yet represented.
arxivId: '2405.02252'
arxivUrl: https://arxiv.org/abs/2405.02252
authors:
- Beyond-2pt Collaboration
- ':'
- Elisabeth Krause
- Yosuke Kobayashi
- Andrés N. Salcedo
- Mikhail M. Ivanov
- Tom Abel
- Kazuyuki Akitsu
- Raul E. Angulo
- Giovanni Cabass
- Sofia Contarini
- Carolina Cuesta-Lazaro
- ChangHoon Hahn
- Nico Hamaus
- Donghui Jeong
- Chirag Modi
- Nhat-Minh Nguyen
- Takahiro Nishimichi
- Enrique Paillas
- Marcos Pellejero Ibañez
- Oliver H. E. Philcox
- Alice Pisani
- Fabian Schmidt
- Satoshi Tanaka
- Giovanni Verza
- Sihan Yuan
- Matteo Zennaro
concepts:
- beyond-2pt statistics
- cosmological simulation
- simulation-based inference
- effective field theory
- bayesian inference
- model validation
- posterior estimation
- field-level inference
- emulation
- dark energy
- density estimation
- dark matter
figures:
- /iaifi-research-blog/figures/2405_02252/figure_1.png
- /iaifi-research-blog/figures/2405_02252/figure_1.png
- /iaifi-research-blog/figures/2405_02252/figure_2.png
- /iaifi-research-blog/figures/2405_02252/figure_2.png
- /iaifi-research-blog/figures/2405_02252/figure_3.png
- /iaifi-research-blog/figures/2405_02252/figure_3.png
pdfUrl: https://arxiv.org/pdf/2405.02252v1
published: '2024-05-03T17:09:52+00:00'
theme: Astrophysics
title: A Parameter-Masked Mock Data Challenge for Beyond-Two-Point Galaxy Clustering
  Statistics
wordCount: 912
---

## The Big Picture

Imagine trying to reconstruct a symphony from only the bass line. You'd capture the rhythm and some structure, but miss the harmonics, the countermelodies, the rich texture that makes the music what it is.

For decades, cosmologists have been doing something analogous: mapping the universe's large-scale structure using only its simplest pairwise measurements — essentially counting how often galaxies appear close together at various distances. It works remarkably well. But the universe has far more to say.

As galaxies cluster under gravity over billions of years, the initially near-random distribution of matter develops complex, irregular patterns: **filaments** (vast bridges of galaxies), **voids** (enormous empty regions between them), clusters, and intricate web-like structures. Simple pairwise measurements can't capture this complexity — they're blind to information encoded in triangles, voids, and higher-order arrangements.

With next-generation surveys like DESI, Euclid, and the Rubin Observatory about to flood the field with unprecedented data, cosmologists need better statistical tools — ones that can hear the full symphony.

A large international collaboration, the **Beyond-2pt Collaboration**, ran a rigorous community data challenge to test whether the new generation of "beyond two-point" analysis methods actually works — and whether they can reliably extract fundamental **cosmological parameters** (the handful of numbers describing the universe's composition and history) from realistic mock data.

> **Key Insight:** Multiple independent beyond-two-point methods successfully recovered hidden cosmological parameters from realistic mock galaxy catalogs, validating a new generation of statistical tools that promise to dramatically improve our maps of the universe.

## How It Works

The challenge was designed with a crucial safeguard: **parameter masking**, where the true cosmological parameters were hidden from participants until after they submitted results. This prevented analysts from unconsciously tuning their methods to match expected answers — the statistical equivalent of a double-blind clinical trial.

The mock data came from high-precision **N-body simulations** — massive computer calculations that evolve millions of simulated dark matter particles under gravity to produce realistic galaxy distributions. The challenge included three flavors of mock catalogs: galaxies in "real space" (without observational distortions), "redshift space" (with the distortions real telescopes see), and on a "light cone" (the most realistic scenario, mimicking how surveys observe the sky across cosmic time).

![Figure 1](/iaifi-research-blog/figures/2405_02252/figure_1.png)

Six distinct analysis methods competed, each targeting different aspects of the **non-Gaussian** information hidden in galaxy clustering:

- **Density-split clustering** divides the survey volume into regions of different galaxy density and measures clustering in each environment separately
- **Nearest neighbor statistics** characterize how isolated or crowded each galaxy is relative to its neighbors
- **Void statistics** extract information from the large empty regions between galaxy filaments
- **BACCO power spectrum emulator** uses machine learning to interpolate between simulations, extending power spectrum analysis to smaller, nonlinear scales
- **LEFTfield** performs **field-level inference** — rather than compressing observations into summary statistics, it analyzes the full three-dimensional galaxy density field directly using **Effective Field Theory (EFT)**, a framework borrowed from particle physics that describes matter clustering at large scales without requiring a model of every small-scale detail
- **Joint power spectrum and bispectrum analyses** add the **bispectrum** (three-point correlations measuring triangular galaxy configurations) using both EFT and **simulation-based inference (SBI)**

![Figure 2](/iaifi-research-blog/figures/2405_02252/figure_1.png)

SBI trains neural networks on thousands of simulations to learn the statistical relationship between observations and parameters — bypassing the need for an analytic likelihood function, which becomes intractable for complex statistics. Field-level inference and SBI represent particularly striking applications of modern machine learning to fundamental cosmology.

## Why It Matters

The validation is significant precisely because it's hard. Each method involves a long chain of modeling choices: how to simulate galaxy formation, how to handle observational effects, how to build a statistical model, how to sample parameter space. Any link can introduce systematic bias. That multiple independent methods — using completely different mathematical frameworks — all recovered the true parameters consistently provides strong evidence the field is on the right track.

![Figure 3](/iaifi-research-blog/figures/2405_02252/figure_2.png)

The challenge also exposed where work remains. Some methods struggled with light-cone geometry or scale cuts; others showed tension between real-space and redshift-space results requiring further investigation. The collaboration frames this as a living challenge: the dataset is publicly available, and teams are invited to submit results from methods not yet tested. The next frontier includes realistic survey complications — survey geometry, photometric redshift uncertainties, and the full complexity of **galaxy bias**, the messy relationship between where galaxies live and where the underlying dark matter actually is.

> **Bottom Line:** The Beyond-2pt challenge demonstrates that a new toolkit of statistical methods can reliably decode cosmological information that traditional analyses miss — a critical step toward extracting the universe's secrets from the data deluge coming from next-generation surveys.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work unites simulation-based inference and machine learning emulators with rigorous statistical cosmology, showing how AI-driven methods can be validated against traditional analytic approaches in a controlled community challenge.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Simulation-based inference and neural network emulators like BACCO proved competitive with analytic methods, demonstrating that learned statistical models can recover unbiased cosmological parameters from complex, high-dimensional data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Recovering ΛCDM parameters — including matter density and the amplitude of density fluctuations — from beyond-two-point statistics directly constrains the physics of dark matter, dark energy, and the growth of large-scale structure.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future challenge rounds will tackle realistic survey systematics and tighter constraints on extensions to ΛCDM; full results and data are described in arXiv:2405.02252.</span></div></div>
</div>
