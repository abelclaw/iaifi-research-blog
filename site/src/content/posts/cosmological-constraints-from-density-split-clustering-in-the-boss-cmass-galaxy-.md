---
abstract: We present a clustering analysis of the BOSS DR12 CMASS galaxy sample, combining
  measurements of the galaxy two-point correlation function and density-split clustering
  down to a scale of $1\,h^{-1}{\rm Mpc}$. Our theoretical framework is based on emulators
  trained on high-fidelity mock galaxy catalogues that forward model the cosmological
  dependence of the clustering statistics within an extended-$Λ$CDM framework, including
  redshift-space and Alcock-Paczynski distortions. Our base-$Λ$CDM analysis finds
  $ω_{\rm cdm} = 0.1201\pm 0.0022$, $σ_8 = 0.792\pm 0.034$, and $n_s = 0.970\pm 0.018$,
  corresponding to $fσ_8 = 0.462\pm 0.020$ at $z \approx 0.525$, which is in agreement
  with Planck 2018 predictions and various clustering studies in the literature. We
  test single-parameter extensions to base-$Λ$CDM, varying the running of the spectral
  index, the dark energy equation of state, and the density of massless relic neutrinos,
  finding no compelling evidence for deviations from the base model. We model the
  galaxy-halo connection using a halo occupation distribution framework, finding signatures
  of environment-based assembly bias in the data. We validate our pipeline against
  mock catalogues that match the clustering and selection properties of CMASS, showing
  that we can recover unbiased cosmological constraints even with a volume 84 times
  larger than the one used in this study.
arxivId: '2309.16541'
arxivUrl: https://arxiv.org/abs/2309.16541
authors:
- Enrique Paillas
- Carolina Cuesta-Lazaro
- Will J. Percival
- Seshadri Nadathur
- Yan-Chuan Cai
- Sihan Yuan
- Florian Beutler
- Arnaud de Mattia
- Daniel Eisenstein
- Daniel Forero-Sanchez
- Nelson Padilla
- Mathilde Pinon
- Vanina Ruhlmann-Kleider
- Ariel G. Sánchez
- Georgios Valogiannis
- Pauline Zarrouk
concepts:
- density-split clustering
- emulation
- simulation-based inference
- bayesian inference
- dark matter
- cosmological simulation
- posterior estimation
- halo occupation distribution
- dark energy
- assembly bias
- neutrino detection
- regression
figures:
- /iaifi-research-blog/figures/2309_16541/figure_1.png
- /iaifi-research-blog/figures/2309_16541/figure_1.png
- /iaifi-research-blog/figures/2309_16541/figure_2.png
- /iaifi-research-blog/figures/2309_16541/figure_2.png
- /iaifi-research-blog/figures/2309_16541/figure_3.png
- /iaifi-research-blog/figures/2309_16541/figure_3.png
pdfUrl: https://arxiv.org/pdf/2309.16541v2
published: '2023-09-28T15:53:45+00:00'
theme: Astrophysics
title: Cosmological constraints from density-split clustering in the BOSS CMASS galaxy
  sample
wordCount: 1031
---

## The Big Picture

Imagine trying to understand a city's population by counting how many buildings stand within a mile of each other. You'd miss the rich neighborhoods clustered near the park, the sparse suburbs, the dense downtown core.

For decades, cosmologists faced a similar problem. They measured galaxies using the **two-point correlation function** — a method that counts how often galaxy pairs appear at different separations. It's powerful, but it treats dense cosmic filaments and empty voids as equally informative. They're not.

The universe isn't smooth. After 13.8 billion years of gravitational collapse, matter has clumped into a vast cosmic web — filaments, sheets, clusters, and enormous empty voids — and all that structure encodes secrets about dark matter, dark energy, and how fast the universe has been growing. Classic two-point statistics excel on large scales but become unreliable at small scales where gravity creates complex, tangled structures that resist clean mathematical description. Cosmologists have been leaving information on the table.

Now, a team led by Enrique Paillas and collaborators — including IAIFI's Carolina Cuesta-Lazaro — has pushed past this limitation using **density-split clustering** combined with machine-learning emulators to pin down the universe's fundamental properties more precisely than ever before from the BOSS CMASS galaxy survey.

> **Key Insight:** By splitting the galaxy field into regions of different local density and measuring clustering statistics in each environment separately, researchers capture non-Gaussian information that standard two-point analyses miss — squeezing more science from existing survey data.

## How It Works

The core innovation is conceptually elegant. Rather than treating all galaxies equally, the team first smoothed the galaxy density field and divided space into **quintiles** — five bins ranked by local galaxy density, from the emptiest voids to the most crowded clusters. Correlation functions measured in each environment separately carry distinct cosmological fingerprints.

![Figure 1](/iaifi-research-blog/figures/2309_16541/figure_1.png)

To make this practically useful, the team needed a theoretical model that could predict density-split correlation functions for any set of cosmological parameters — without running a full **N-body simulation** (a computer model tracking how millions of particles attract and clump under gravity over cosmic time) every single time. Their solution: train **neural network emulators** on a library of high-fidelity mock galaxy catalogues. These emulators learn to interpolate across a vast parameter space, predicting clustering statistics in milliseconds rather than months.

The pipeline involves:

- **N-body simulations** of dark matter clustering across a range of cosmological parameters
- **Halo occupation distribution (HOD) modeling** — a statistical recipe for deciding which dark matter halos are massive or concentrated enough to host a galaxy, and how many
- **Forward modeling** that translates theoretical predictions into telescope-observable signals
- Corrections for **redshift-space distortions** (how galaxies' velocities smear their apparent distances along the line of sight) and the **Alcock-Paczynski effect** (geometric distortions from assuming the wrong cosmology)
- Emulators trained to predict both the standard two-point function *and* density-split statistics simultaneously

The galaxy sample — BOSS DR12 CMASS, covering roughly 650,000 massive galaxies at redshifts z ≈ 0.43–0.70 — is one of the richest datasets available for this kind of analysis. The team pushed measurements down to scales of just 1 h⁻¹ Mpc, deep into the regime where gravity creates messy, nonlinear structure, but where their emulators remain accurate.

![Figure 3](/iaifi-research-blog/figures/2309_16541/figure_2.png)

A critical part of the analysis was modeling **assembly bias** — whether galaxies' tendency to occupy halos depends not just on halo mass but also on the surrounding environment. The team found genuine signatures: galaxies prefer halos that are more concentrated or differently shaped depending on local density. It's a subtle effect, but ignoring it would bias the cosmological results.

## Why It Matters

The results land squarely in agreement with Planck 2018. The key numbers: ω_cdm = 0.1201 ± 0.0022 (cold dark matter density), σ_8 = 0.792 ± 0.034 (how clumpy matter is today), n_s = 0.970 ± 0.018 (the tilt of primordial fluctuations), and a growth rate fσ_8 = 0.462 ± 0.020 (how fast cosmic structure has been building). That agreement matters: the universe's growth rate, as traced by these massive galaxies, is consistent with predictions from the **CMB** (the faint thermal glow left over from the Big Bang), easing tensions that have plagued cosmology.

![Figure 5](/iaifi-research-blog/figures/2309_16541/figure_3.png)

Beyond the headline numbers, the team tested whether any physics beyond standard **ΛCDM** — the current best model of the universe, built from ordinary matter, cold dark matter, and a constant dark energy — was hiding in the data. They varied the running of the spectral index, the dark energy equation of state, and the density of relic neutrinos. None showed statistically compelling deviations from the base model. A clean null result that still meaningfully constrains exotic physics.

Perhaps most exciting: the team validated their pipeline against mock catalogues 84 times larger than the actual CMASS volume and recovered unbiased constraints even at that scale. The next generation of galaxy surveys — DESI, Euclid, the Vera Rubin Observatory — will deliver exactly that kind of expanded dataset. This methodology is already ready for them.

> **Bottom Line:** Density-split clustering, powered by machine-learning emulators, extracts cosmological information from scales and environments that traditional two-point analyses ignore — and the technique is already validated for the much larger galaxy surveys arriving in the next decade.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges AI and cosmology by deploying neural network emulators — trained on N-body simulations — to perform Bayesian inference on one of the largest galaxy surveys ever assembled, turning a computationally prohibitive problem into a tractable one.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The emulator framework demonstrates how machine learning can replace expensive forward simulations in high-dimensional parameter inference, a technique broadly applicable across any scientific domain requiring simulation-based inference.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By probing galaxy clustering at nonlinear scales through environment-dependent statistics, the analysis delivers competitive constraints on dark matter density, the growth rate of cosmic structure, and extensions to ΛCDM including dark energy and neutrino physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">With DESI and Euclid already collecting data, this pipeline — validated at 84× the CMASS volume — is positioned to sharpen cosmological constraints significantly in the near future; the paper is available at arXiv:2309.16539.</span></div></div>
</div>
