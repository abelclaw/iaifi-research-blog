---
abstract: Diffuse interstellar bands (DIBs) are broad absorption features associated
  with interstellar dust and can serve as chemical and kinematic tracers. Conventional
  measurements of DIBs in stellar spectra are complicated by residuals between observations
  and best-fit stellar models. To overcome this, we simultaneously model the spectrum
  as a combination of stellar, dust, and residual components, with full posteriors
  on the joint distribution of the components. This decomposition is obtained by modeling
  each component as a draw from a high-dimensional Gaussian distribution in the data-space
  (the observed spectrum) -- a method we call "Marginalized Analytic Data-space Gaussian
  Inference for Component Separation" (MADGICS). We use a data-driven prior for the
  stellar component, which avoids missing stellar features not well-modeled by synthetic
  spectra. This technique provides statistically rigorous uncertainties and detection
  thresholds, which are required to work in the low signal-to-noise regime that is
  commonplace for dusty lines of sight. We reprocess all public Gaia DR3 RVS spectra
  and present an improved 8621 Å DIB catalog, free of detectable stellar line contamination.
  We constrain the rest-frame wavelength to $8623.14 \pm 0.087$ Å (vacuum), find no
  significant evidence for DIBs in the Local Bubble from the $1/6^{\rm{th}}$ of RVS
  spectra that are public, and show unprecedented correlation with kinematic substructure
  in Galactic CO maps. We validate the catalog, its reported uncertainties, and biases
  using synthetic injection tests. We believe MADGICS provides a viable path forward
  for large-scale spectral line measurements in the presence of complex spectral contamination.
arxivId: '2212.03879'
arxivUrl: https://arxiv.org/abs/2212.03879
authors:
- Andrew K. Saydjari
- Ana Sofía M. Uzsoy
- Catherine Zucker
- J. E. G. Peek
- Douglas P. Finkbeiner
concepts:
- spectral component separation
- bayesian inference
- diffuse interstellar band mapping
- signal detection
- posterior estimation
- uncertainty quantification
- inverse problems
- density estimation
- model validation
- goodness-of-fit testing
- stellar evolution
- dimensionality reduction
figures:
- /iaifi-research-blog/figures/2212_03879/figure_1.png
- /iaifi-research-blog/figures/2212_03879/figure_2.png
- /iaifi-research-blog/figures/2212_03879/figure_3.png
pdfUrl: https://arxiv.org/pdf/2212.03879v3
published: '2022-12-07T19:00:00+00:00'
theme: Astrophysics
title: 'Measuring the 8621 Å Diffuse Interstellar Band in Gaia DR3 RVS Spectra: Obtaining
  a Clean Catalog by Marginalizing over Stellar Types'
wordCount: 1184
---

## The Big Picture

Imagine trying to hear a whisper in a crowded room where the acoustics shift depending on who's speaking. That's the challenge astronomers face when hunting for **diffuse interstellar bands** (DIBs): faint dips in starlight caused by mysterious molecules drifting through the space between stars. When starlight passes through interstellar clouds, those molecules absorb specific colors of light, leaving dark notches in the spectrum. The whisper is the DIB. The crowd noise is the star itself.

DIBs are one of astronomy's longest-standing mysteries. Since their discovery over a century ago, astronomers have catalogued hundreds of these dark notches. Yet the identity of the molecules responsible for most of them remains unknown.

Their value goes beyond chemistry. A molecule moving toward or away from us shifts the color of light it absorbs slightly, via the Doppler effect (the same principle that makes a passing ambulance's siren change pitch). By measuring that shift, astronomers can map how the **interstellar medium**, the thin soup of gas and dust between stars, flows across the Galaxy, tracing spiral arms and large-scale structure.

But clean measurements are hard. Every star carries its own messy absorption pattern that can mimic or hide the DIB signal.

A team at Harvard and the Space Telescope Science Institute tackled this head-on. They developed a statistical framework that simultaneously untangles stellar and interstellar contributions to each spectrum, then applied it to nearly a million spectra from the European Space Agency's Gaia satellite.

> **Key Insight:** By modeling stellar and dust components jointly as draws from learned Gaussian distributions, the MADGICS method produces DIB measurements that are statistically clean, uncertainty-aware, and reliable even in low signal-to-noise conditions where traditional methods fail.

## How It Works

The conventional approach is intuitive but flawed: fit a stellar model, divide it out, and look for the DIB in the residuals. The trouble is that stellar models are imperfect. Real stars have features synthetic spectra miss, and those mismatches leave ghost signals that masquerade as DIBs or bury real ones.

**MADGICS** (Marginalized Analytic Data-space Gaussian Inference for Component Separation) takes a fundamentally different approach. Rather than treating the stellar model as fixed truth to be subtracted, it treats the stellar spectrum as a *random variable* drawn from a high-dimensional distribution learned directly from observations. The spectrum is modeled as a sum of three components:

1. **Stellar component** — learned from a data-driven prior built from thousands of clean, low-extinction spectra
2. **DIB component** — a Gaussian absorption profile at the 8621 Å feature (Å = Ångström; 8621 Å is deep red, nearly infrared)
3. **Residual component** — capturing anything the first two miss

Because all three components are modeled as Gaussians in the space of observed spectral bins, the posterior (the full probability distribution over all possible component values given the data) can be computed analytically. No sampling, no iterative fitting. Just matrix algebra. This makes MADGICS fast enough to run on millions of spectra while still providing complete uncertainty information.

![Figure 1](figure:1)

The stellar prior was built from Gaia DR3 RVS (Radial Velocity Spectrometer) spectra of stars with low dust extinction, where minimal interstellar material lies between the source and Earth. The prior therefore learns what real stars look like, undistorted by interstellar contamination.

This data-driven prior sidesteps the long-standing problem of incomplete stellar line lists. If a feature appears in real stars, the prior learns it, whether or not theory predicted it.

The result is something rare in large-scale pipelines: uncertainty estimates that honestly reflect measurement difficulty. For dusty lines of sight, where DIBs are strongest but stars appear dim and noisy, traditional methods break down. MADGICS was built for exactly this regime.

## The Results

Processing all 999,645 publicly available Gaia DR3 RVS spectra, the team produced a catalog with 7,789 high-quality DIB detections. That's far fewer than the Gaia team's own 50,787, but dramatically cleaner. The reduction isn't a failure; it's the method working as intended, requiring genuine freedom from stellar contamination rather than accepting borderline cases.

![Figure 2](figure:2)

The catalog delivers several headline results. The rest-frame wavelength of the 8621 Å DIB is pinned to 8623.14 ± 0.087 Å (vacuum), a precision enabled by marginalizing over stellar types. Toward the Local Bubble, the dust-free cavity surrounding our solar neighborhood, the team finds no significant DIB signal. Exactly as expected: no dust, no DIB carriers.

Most striking is the agreement with CO maps. Carbon monoxide traces cold molecular gas, and its emission velocities reflect the kinematic structure of the Galaxy's spiral arms. The MADGICS catalog shows tight alignment with these features, resolving substructure that previous catalogs blurred over.

![Figure 3](figure:3)

Validation came from synthetic injection tests: artificially inserting DIB signals of known strength into real spectra, running MADGICS blind, and confirming that recovered measurements matched injected values within reported uncertainties. The error bars are honest.

## Why It Matters

The 8621 Å DIB is a proof of concept. MADGICS is a general framework for spectral component separation. Wherever a complex foreground obscures a weaker signal of interest, this approach applies. The authors identify atomic interstellar absorption lines and emission line surveys as natural extensions.

Gaia is releasing more spectra. SDSS-V is surveying millions of stars. The next decade will produce data volumes that dwarf what exists today, and without methods that scale gracefully while maintaining statistical integrity, most of that potential for interstellar science will go unrealized. MADGICS points toward a path where catalog quality scales with data quantity, where more spectra means sharper maps, not just larger piles of noisy measurements.

The deeper question, *what molecule actually causes the 8621 Å DIB?*, remains open. But maps clean enough to trace kinematic substructure bring laboratory spectroscopists closer to matching candidate molecules to observed features.

> **Bottom Line:** MADGICS turns a century-old data analysis headache into a tractable Bayesian inference problem, producing the cleanest large-scale catalog of the 8621 Å diffuse interstellar band to date and establishing a template for next-generation spectroscopic surveys.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work marries machine learning-style data-driven priors with rigorous Bayesian inference to solve a core problem in observational astrophysics, showing how statistical AI methods can directly unlock new science from large astronomical surveys.

- **Impact on Artificial Intelligence:** MADGICS introduces an analytically tractable Gaussian component separation framework that scales to millions of high-dimensional data vectors, offering a general template for blind source separation in any domain with learned mixture models.

- **Impact on Fundamental Interactions:** The resulting catalog maps the kinematic structure of the interstellar medium with new fidelity, advancing the use of DIBs as chemical and dynamical tracers of the Milky Way's spiral structure and the environments where dust and its associated molecules form.

- **Outlook and References:** Future work will process the full 5.6 million Gaia RVS spectra, and the MADGICS framework is positioned to extend to other DIBs and atomic interstellar lines in upcoming large spectroscopic surveys; see [arXiv:2212.03879](https://arxiv.org/abs/2212.03879).
