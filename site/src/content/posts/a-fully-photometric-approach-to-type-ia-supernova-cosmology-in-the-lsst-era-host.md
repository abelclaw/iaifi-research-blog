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

Imagine trying to identify a million strangers from photographs alone, no names, no ID cards, just their faces and the neighborhoods they live in. That's roughly the challenge astronomers face as the Vera C. Rubin Observatory prepares to come online and flood the world with cosmic explosions.

Type Ia supernovae are the universe's gold standard for measuring cosmic distances. Decades of careful observation of these stellar detonations first revealed that the universe's expansion is *accelerating*, a discovery that earned the 2011 Nobel Prize in Physics.

Those early measurements used only a handful of events, each confirmed by spectroscopic follow-up: slow, expensive telescope time that analyzes an explosion's full light spectrum to verify what type of event it is. When the Legacy Survey of Space and Time (LSST) begins cataloguing the sky from Chile, it will discover nearly a million Type Ia supernovae. There is simply no way to take spectra of them all.

A new study from Mitra et al. develops and tests a fully photometric pipeline, one that relies on brightness measurements alone, no spectrum required, to unlock the dark energy science buried in LSST's data.

> **Key Insight:** By combining neural network classification, photometric redshifts, and Bayesian statistical frameworks, the pipeline achieves a dark energy Figure of Merit of ~150, nearly three times better than the current state-of-the-art from the Dark Energy Survey.

## How It Works

The team built their analysis on a simulation framework called **ELAsTiCC** (Extended LSST Astronomical Time Series Classification Challenge), which generates realistic mock observations mimicking what LSST will actually see. This isn't a clean theoretical exercise. The simulations include contamination from other types of exploding stars, incorrect host galaxy associations, and the full complexity of photometric redshift errors.

![Figure 1](figure:1)

The pipeline proceeds in four steps:

1. **Light curve fitting** — each transient's brightness evolution across six optical filters is fitted using the SALT3 model, extracting peak brightness, color, and stretch parameters that standardize Type Ia supernovae as distance indicators.
2. **Host galaxy association and photometric redshifts** — rather than taking a full spectrum, the team performs a joint SN+host photometric redshift (photo-z) fit. This estimates distance from how an object's colors shift with increasing distance, using the host galaxy's color-brightness profile alongside the supernova light curve to pin down distance without a spectrum.
3. **Photometric classification with SCONE** — a neural network classifier trained to distinguish true Type Ia supernovae from impostors (core-collapse supernovae, peculiar events) using only multi-band light curve shape. SCONE assigns each event a probability of being a genuine Type Ia.
4. **BEAMS with Bias Corrections (BBC)** — rather than cutting the sample to only "clean" events, this statistical framework uses each event's classification probability to weight its contribution to the final Hubble diagram, the plot of distance versus recession velocity that traces dark energy's influence on cosmic expansion.

The combined dataset covers two survey strategies: deep, narrow Deep Drilling Fields (DDF) reaching to high redshift, and the broader Wide Fast Deep (WFD) survey, which contributes a spectroscopically confirmed low-redshift anchor sample. Together, they yield roughly 6,000 simulated events for cosmological analysis.

![Figure 2](figure:2)

## Why It Matters

The headline number: fitting the **wCDM model**, where dark energy has a constant but potentially non-standard equation of state, the team achieves a Figure of Merit (FoM) of approximately 150. The FoM is a standard metric for how tightly an experiment can simultaneously pin down dark energy parameters. Higher is better.

For comparison, the DES-SN5YR analysis, currently among the most powerful supernova cosmology datasets ever published, achieved an FoM of 54. LSST, analyzed with fully photometric methods, could be nearly three times more constraining.

![Figure 3](figure:3)

The team isn't declaring victory, though. Averaging cosmological parameter fits across 25 independent simulation realizations, they find small but statistically significant biases: the recovered dark energy parameters don't perfectly match the true values baked into the simulations.

These biases are a warning flag. The pipeline works well, but needs refinement before it can be trusted at LSST's level of precision. That's exactly what simulation-based stress-testing is for. The biases point to where development must focus next: better photo-z calibration, more robust contamination modeling, and tighter control of systematic uncertainties.

On the machine learning side, neural network classifiers like SCONE represent a new generation of tools that can process light curve data at scales no human team could manage. On the physics side, LSST's supernova sample will probe whether dark energy truly behaves like a cosmological constant or whether it evolves over time, as hinted by recent results from DESI and Pantheon+. A photometric pipeline that handles a million events without spectroscopic confirmation isn't a convenience; it's a scientific necessity.

The **CPL w0wa model**, which allows dark energy to evolve in time, also shows competitive FoM gains, positioning this framework to probe the most pressing open questions in cosmology as real LSST data arrive.

> **Bottom Line:** LSST can achieve world-leading dark energy constraints using a fully photometric analysis, no spectra required, while the identified systematic biases set a clear agenda for what must be solved before the method is ready for real data.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** The work deploys neural network classifiers and Bayesian statistical frameworks to tackle one of observational cosmology's central challenges: extracting dark energy science from an unprecedented photometric supernova survey.

- **Impact on Artificial Intelligence:** The SCONE neural network classifier shows that deep learning can reliably separate Type Ia supernovae from contaminants using multi-band light curves alone, making photometric classification a viable replacement for spectroscopic confirmation at LSST scale.

- **Impact on Fundamental Interactions:** With a projected dark energy Figure of Merit of ~150, nearly three times the DES-SN5YR result, LSST's photometric supernova sample has the statistical power to detect or rule out dynamical dark energy at high significance.

- **Outlook and References:** The identified parameter biases set the agenda for the next phase of LSST supernova cosmology pipeline development; the full framework will be validated against early LSST data as the survey comes online. See [arXiv:2512.06319](https://arxiv.org/abs/2512.06319) for details.

## Original Paper Details
- **Title:** A Fully Photometric Approach to Type Ia Supernova Cosmology in the LSST Era: Host Galaxy Redshifts and Supernova Classification
- **arXiv ID:** 2512.06319
- **Authors:** ["Ayan Mitra", "Richard Kessler", "Rebecca C. Chen", "Alex Gagliano", "Matthew Grayling", "Surhud More", "Gautham Narayan", "Helen Qu", "Srinivasan Raghunathan", "Alex I. Malz", "Michelle Lochner", "The LSST Dark Energy Science Collaboration"]
- **Abstract:** The upcoming Vera C. Rubin Observatory's Legacy Survey of Space and Time (LSST) is expected to discover nearly a million Type Ia supernovae (SNeIa), offering an unprecedented opportunity to constrain dark energy. The vast majority of these events will lack spectroscopic classification and redshifts, necessitating a fully photometric approach to maximize cosmology constraining power. We present detailed simulations based on the Extended LSST Astronomical Time Series Classification Challenge (ELAsTiCC), and a cosmological analysis using photometrically classified SNeIa with host galaxy photometric redshifts. This dataset features realistic multi-band light curves, non-SNIa contamination, host mis-associations, and transient-host correlations across the high-redshift Deep Drilling Fields (DDF) (~ 50 deg^2). We also include a spectroscopically confirmed low-redshift sample based on the Wide Fast Deep (WFD) fields. We employ a joint SN+host photometric redshift fit, a neural network based photometric classifier (SCONE), and BEAMS with Bias Corrections (BBC) methodology to construct a bias-corrected Hubble diagram. We produce statistical + systematic covariance matrices, and perform cosmology fitting with a prior using Cosmic Microwave Background constraints. We fit and present results for the wCDM dark energy model, and the more general Chevallier-Polarski-Linder (CPL) w0wa model. With a simulated sample of ~6000 events, we achieve a Figure of Merit (FoM) value of about 150, which is significantly larger than the DESVYR FoM of 54. Averaging analysis results over 25 independent samples, we find small but significant biases indicating a need for further analysis testing and development.
