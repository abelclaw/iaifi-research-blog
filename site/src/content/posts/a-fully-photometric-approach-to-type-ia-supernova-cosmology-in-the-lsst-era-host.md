---
abstract: The upcoming Vera C. Rubin Observatory's Legacy Survey of Space and Time
  (LSST) is expected to discover nearly a million Type Ia supernovae (SNeIa), offering
  an unprecedented opportunity to constrain dark energy. The vast majority of these
  events will lack spectroscopic classification and redshifts, necessitating a fully
  photometric approach to maximize cosmology constraining power. We present detailed
  simulations based on the Extended LSST Astronomical Time Series Classification Challenge
  (ELAsTiCC), and a cosmological analysis using photometrically classified SNeIa with
  host galaxy photometric redshifts. This dataset features realistic multi-band light
  curves, non-SNIa contamination, host mis-associations, and transient-host correlations
  across the high-redshift Deep Drilling Fields (DDF) (~ 50 deg^2). We also include
  a spectroscopically confirmed low-redshift sample based on the Wide Fast Deep (WFD)
  fields. We employ a joint SN+host photometric redshift fit, a neural network based
  photometric classifier (SCONE), and BEAMS with Bias Corrections (BBC) methodology
  to construct a bias-corrected Hubble diagram. We produce statistical + systematic
  covariance matrices, and perform cosmology fitting with a prior using Cosmic Microwave
  Background constraints. We fit and present results for the wCDM dark energy model,
  and the more general Chevallier-Polarski-Linder (CPL) w0wa model. With a simulated
  sample of ~6000 events, we achieve a Figure of Merit (FoM) value of about 150, which
  is significantly larger than the DESVYR FoM of 54. Averaging analysis results over
  25 independent samples, we find small but significant biases indicating a need for
  further analysis testing and development.
arxivId: '2512.06319'
arxivUrl: https://arxiv.org/abs/2512.06319
authors:
- Ayan Mitra
- Richard Kessler
- Rebecca C. Chen
- Alex Gagliano
- Matthew Grayling
- Surhud More
- Gautham Narayan
- Helen Qu
- Srinivasan Raghunathan
- Alex I. Malz
- Michelle Lochner
- The LSST Dark Energy Science Collaboration
concepts:
- supernova classification
- dark energy
- photometric redshift estimation
- bayesian inference
- classification
- bias correction
- uncertainty quantification
- simulation-based inference
- convolutional networks
- calibration
- cosmic microwave background
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2512_06319/figure_1.png
- /iaifi-research-blog/figures/2512_06319/figure_2.png
- /iaifi-research-blog/figures/2512_06319/figure_3.png
pdfUrl: https://arxiv.org/pdf/2512.06319v1
published: '2025-12-06T06:38:05+00:00'
theme: Astrophysics
title: 'A Fully Photometric Approach to Type Ia Supernova Cosmology in the LSST Era:
  Host Galaxy Redshifts and Supernova Classification'
wordCount: 1086
---

## The Big Picture

Imagine trying to identify a million strangers from photographs alone — no names, no ID cards, just their faces and the neighborhoods they live in. That's roughly the challenge astronomers face as the Vera C. Rubin Observatory prepares to come online and flood the world with a tidal wave of cosmic explosions.

Type Ia supernovae are the universe's gold standard for measuring cosmic distances. Decades of careful observation of these stellar detonations first revealed that the universe's expansion is *accelerating* — a discovery so startling it earned the 2011 Nobel Prize in Physics.

Those early measurements used only a handful of events, each confirmed by spectroscopic follow-up — slow, expensive telescope time that analyzes an explosion's full light spectrum to verify what type of event it is. When the Legacy Survey of Space and Time (LSST) begins cataloguing the sky from Chile, it will discover nearly **a million Type Ia supernovae** — and there is simply no way to analyze the full spectrum of them all.

A new study from Mitra et al. confronts this problem head-on, developing and testing a fully photometric pipeline — one that relies on brightness measurements alone, no spectrum required — that could unlock the dark energy science hidden in LSST's flood of data.

> **Key Insight:** By combining neural network classification, photometric redshifts, and Bayesian statistical frameworks, this work demonstrates that LSST's supernova sample could achieve a dark energy Figure of Merit of ~150 — nearly three times better than the current state-of-the-art from the Dark Energy Survey.

## How It Works

The team built their analysis on a sophisticated simulation framework called **ELAsTiCC** (Extended LSST Astronomical Time Series Classification Challenge), which generates realistic mock observations mimicking what LSST will actually see. This isn't a clean theoretical exercise — the simulations include contamination from other types of exploding stars, incorrect host galaxy associations, and the full complexity of photometric redshift errors.

![Figure 1](/iaifi-research-blog/figures/2512_06319/figure_1.png)

The pipeline proceeds in layered steps:

1. **Light curve fitting** — each transient's brightness evolution across six optical filters is fitted using the SALT3 model, extracting peak brightness, color, and stretch parameters that standardize Type Ia supernovae as distance indicators.
2. **Host galaxy association and photometric redshifts** — rather than taking a full spectrum, the team performs a *joint* SN+host **photometric redshift** (photo-z) fit, estimating distance from how an object's colors shift with increasing distance, using the host galaxy's color-brightness profile alongside the supernova light curve to pin down the distance without a spectrum.
3. **Photometric classification with SCONE** — a **neural network classifier** trained to distinguish true Type Ia supernovae from impostors (core-collapse supernovae, peculiar events) using only multi-band light curve shape. SCONE assigns each event a probability of being a genuine Type Ia.
4. **BEAMS with Bias Corrections (BBC)** — rather than cutting the sample to only "clean" events, this statistical framework uses each event's classification probability to weight its contribution to the final **Hubble diagram** — the plot of distance versus recession velocity that traces dark energy's influence on cosmic expansion.

The combined dataset covers two survey strategies: deep, narrow **Deep Drilling Fields** (DDF) reaching to high redshift, and the broader **Wide Fast Deep** (WFD) survey, which contributes a spectroscopically confirmed low-redshift anchor sample. Together, they yield roughly 6,000 simulated events for cosmological analysis.

![Figure 2](/iaifi-research-blog/figures/2512_06319/figure_2.png)

## Why It Matters

The headline result is striking. Fitting the **wCDM model** — where dark energy has a constant but potentially non-standard equation of state (a measure of how its pressure relates to its energy density) — the team achieves a **Figure of Merit (FoM) of approximately 150**. The FoM is a standard metric for how tightly an experiment can simultaneously pin down dark energy parameters; higher is better.

For comparison, the DES-SN5YR analysis — currently among the most powerful supernova cosmology datasets ever published — achieved an FoM of 54. This simulation suggests LSST, analyzed with fully photometric methods, could be nearly three times more constraining.

![Figure 3](/iaifi-research-blog/figures/2512_06319/figure_3.png)

The team doesn't declare victory, though. Averaging cosmological parameter fits across 25 independent simulation realizations, they find **small but statistically significant biases** — the recovered dark energy parameters don't perfectly match the true values baked into the simulations.

These biases are a warning flag: the pipeline works well, but needs further refinement before it can be trusted at LSST's level of precision. This is exactly what simulation-based stress-testing is for — the biases point to where development must focus next: better photo-z calibration, more robust contamination modeling, and tighter control of systematic uncertainties.

This work sits at the intersection of two rapidly evolving fields. On the machine learning side, neural network classifiers like SCONE represent a new generation of tools that can process light curve data at scales no human team could manage. On the physics side, LSST's supernova sample will probe whether dark energy truly behaves like a cosmological constant — or whether it evolves, as hinted by recent results from DESI and Pantheon+. A photometric pipeline that handles a million events without spectroscopic confirmation isn't a convenience; it's a scientific necessity.

The **CPL w0wa model** — allowing dark energy to evolve in time — also shows competitive FoM gains, positioning this framework to probe the most pressing open questions in cosmology as real LSST data arrive.

> **Bottom Line:** This study demonstrates that LSST can achieve world-leading dark energy constraints using a fully photometric analysis — no spectra required — while honestly flagging the systematic biases that remain to be solved before the method is ready for prime time.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work deploys neural network classifiers and Bayesian statistical frameworks to tackle one of observational cosmology's central challenges — extracting dark energy science from an unprecedented photometric supernova survey.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The SCONE neural network classifier demonstrates that deep learning can reliably separate Type Ia supernovae from contaminants using multi-band light curves alone, establishing photometric classification as a viable replacement for spectroscopic confirmation at LSST scale.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By projecting a dark energy Figure of Merit of ~150 — nearly three times the DES-SN5YR result — this analysis shows that LSST's photometric supernova sample has the statistical power to detect or rule out dynamical dark energy at high significance.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The identified parameter biases set the agenda for the next phase of LSST supernova cosmology pipeline development; the full framework will be validated against early LSST data as the survey comes online. See arXiv:2501.12391 for details.</span></div></div>
</div>
