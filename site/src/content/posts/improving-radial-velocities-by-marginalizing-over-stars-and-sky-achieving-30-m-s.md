---
abstract: The radial velocity catalog from the Apache Point Observatory Galactic Evolution
  Experiment (APOGEE) is unique in its simultaneously large volume and high precision
  as a result of its decade-long survey duration, multiplexing (600 fibers), and spectral
  resolution of $R \sim 22,500$. However, previous data reductions of APOGEE have
  not fully realized the potential radial velocity (RV) precision of the instrument.
  Here we present an RV catalog based on a new reduction of all 2.6 million visits
  of APOGEE DR17 and validate it against improved estimates for the theoretical RV
  performance. The core ideas of the new reduction are the simultaneous modeling of
  all components in the spectra, rather than a separate subtraction of point estimates
  for the sky, and a marginalization over stellar types, rather than a grid search
  for an optimum. We show that this catalog, when restricted to RVs measured with
  the same fiber, achieves noise-limited precision down to 30 m/s and delivers well-calibrated
  uncertainties. We also introduce a general method for calibrating fiber-to-fiber
  constant RV offsets and demonstrate its importance for high RV precision work in
  multi-fiber spectrographs. After calibration, we achieve 47 m/s RV precision on
  the combined catalog with RVs measured with different fibers. This degradation in
  precision relative to measurements with only a single fiber suggests that refining
  line spread function models should be a focus in SDSS-V to improve the fiber-unified
  RV catalog.
arxivId: '2408.07126'
arxivUrl: https://arxiv.org/abs/2408.07126
authors:
- Andrew K. Saydjari
- Douglas P. Finkbeiner
- Adam J. Wheeler
- Jon A. Holtzman
- John C. Wilson
- Andrew R. Casey
- Sophia Sánchez-Maes
- Joel R. Brownstein
- David W. Hogg
- Michael R. Blanton
concepts:
- bayesian inference
- spectral component separation
- calibration
- uncertainty quantification
- fiber systematics calibration
- inverse problems
- signal detection
- line spread function modeling
- sparse models
- stellar evolution
- exoplanets
figures:
- /iaifi-research-blog/figures/2408_07126/figure_1.png
- /iaifi-research-blog/figures/2408_07126/figure_1.png
- /iaifi-research-blog/figures/2408_07126/figure_2.png
- /iaifi-research-blog/figures/2408_07126/figure_2.png
- /iaifi-research-blog/figures/2408_07126/figure_3.png
- /iaifi-research-blog/figures/2408_07126/figure_3.png
pdfUrl: https://arxiv.org/pdf/2408.07126v1
published: '2024-08-13T18:00:01+00:00'
theme: Astrophysics
title: 'Improving Radial Velocities by Marginalizing over Stars and Sky: Achieving
  30 m/s RV Precision for APOGEE in the Plate Era'
wordCount: 1085
---

## The Big Picture

Imagine trying to hear a whispered conversation from across a stadium while a rock concert is playing. Now imagine that whisper contains the only clue to whether a distant planet exists — or whether two stars are locked in an invisible gravitational embrace. That's essentially the challenge astronomers face when measuring the **radial velocities** of stars: detecting tiny shifts in the color of starlight — called **Doppler shifts** — that betray motion, while contending with a symphony of interference from Earth's own atmosphere.

Radial velocity — the speed at which a star moves toward or away from us — is one of astronomy's most powerful tools. It reveals exoplanets tugging on their host stars, uncovers binary star systems, traces the ghostly streams of disrupted galaxies, and illuminates how the Milky Way assembled itself over cosmic time.

Specialized instruments designed to study one star at a time, like HARPS and ESPRESSO, can detect motions smaller than 1 meter per second. But surveys that observe hundreds of thousands of stars simultaneously sacrifice precision for volume. Until now.

A team of astronomers led by Andrew Saydjari at Harvard has fundamentally rethought how to extract radial velocities from **APOGEE**, a decade-long survey that has mapped the motions of millions of Milky Way stars. They squeezed 30 meters per second precision out of an instrument observing 600 stars at once — a result that rewrites what's possible in large-scale stellar astronomy.

> **Key Insight:** By simultaneously modeling stellar and sky light rather than subtracting them separately — and by considering all possible stellar types at once rather than committing to a single best guess — the researchers achieved noise-limited radial velocity precision of 30 m/s without upgrading a single piece of hardware.

## How It Works

The Apache Point Observatory Galactic Evolution Experiment, APOGEE, spent a decade pointing its twin spectrographs at the Milky Way. Each spectrograph feeds on 300 optical fibers, capturing near-infrared starlight across 15,000–17,000 Angstroms at a **spectral resolution** of R ~ 22,500 — a measure of how finely it can distinguish neighboring wavelengths. The result: 2.6 million individual stellar visits logged in data release DR17. But previous analysis pipelines left precision on the table.

The old approach had two fundamental weaknesses. First, **sky subtraction** — removing the atmospheric glow — happened as a separate, upfront step. Any error in that estimate contaminated every subsequent measurement. **Telluric absorption features** (where atmospheric gases absorb specific wavelengths) and **sky emission lines** (bright wavelengths where the atmosphere itself glows) would bleed into the stellar signal, biasing velocity measurements.

Second, the pipeline searched for the best-matching **stellar template** by scanning a grid of options and picking the winner. Grid searches discard information: they throw away all the "almost right" templates and commit to a single answer.

![Figure 1](/iaifi-research-blog/figures/2408_07126/figure_1.png)

Saydjari and colleagues replaced both steps with a unified probabilistic framework, implemented in a Julia package called `apMADGICS.jl`. The key innovations:

- **Simultaneous component separation:** The model fits stellar light, sky emission, and telluric absorption all at once. Each component is modeled jointly, so uncertainty in one propagates correctly into the others — no sequential subtraction, no compounding errors.
- **Marginalization over stellar types:** Rather than picking one best template, the method integrates over the entire library of stellar types. The stellar type becomes an unknown whose uncertainty folds automatically into the final velocity measurement — mathematically equivalent to asking: "Given all possible stellar types, what radial velocity best fits the data?"

The result is a fundamentally cleaner measurement. Residual sky contamination no longer systematically biases the answer, and the uncertainty estimates are properly calibrated: when the pipeline reports uncertainty X, it actually means it.

![Figure 3](/iaifi-research-blog/figures/2408_07126/figure_2.png)

## Why It Matters

The numbers tell the story. The previous APOGEE pipeline struggled to reach its theoretical limits. The new catalog, when measurements are restricted to the same fiber, achieves noise-limited precision down to **30 m/s** — matching the theoretical floor. That's several times better than what surveys of comparable scale have achieved. The closest competitor, the GALAH survey (R ~ 28,000), delivered ~140 m/s precision across ~340,000 stars; APOGEE DR17 covers ~730,000 stars, advancing on both axes simultaneously.

![Figure 5](/iaifi-research-blog/figures/2408_07126/figure_3.png)

The team also uncovered something subtle and important: individual fibers in a **multi-object spectrograph** — an instrument that simultaneously captures light from hundreds of stars through separate optical threads — introduce constant velocity offsets relative to each other. This fiber-to-fiber bias had been lurking in APOGEE data, quietly degrading the combined catalog. Saydjari and colleagues introduced a new calibration method to characterize and remove these offsets.

After calibration, the combined catalog achieves 47 m/s precision. The gap between 30 and 47 m/s points to the next frontier: improving the **line spread function** (LSF) models — the precise characterization of how each fiber blurs and distorts incoming light. The authors flag this as a priority for SDSS-V, the ongoing successor survey, where the same APOGEE spectrographs continue operating.

The broader implication is methodological. Simultaneous component separation isn't specific to APOGEE. Any spectroscopic survey contaminated by sky emission or telluric absorption — which is essentially all of them — could benefit from treating the problem as joint inference rather than sequential subtraction. As SDSS-V, 4MOST, WEAVE, and other next-generation surveys come online, this approach could become the new standard.

> **Bottom Line:** By replacing sequential pipeline steps with a unified probabilistic model, this work extracts 30 m/s radial velocity precision from APOGEE's 2.6 million stellar visits — transforming an already remarkable survey into an instrument-limited precision machine, through software alone.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies Bayesian probabilistic inference and marginalization — tools from machine learning and statistics — to the observational challenge of precision stellar spectroscopy, demonstrating how modern computational methods can unlock untapped precision in existing astronomical datasets.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The marginalization-over-templates approach replaces discrete grid search with principled probabilistic integration, offering a generalizable template for how AI-inspired statistical methods can replace heuristic pipeline steps in large-scale data reduction.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Achieving 30 m/s RV precision at survey scale opens new windows into Galactic archaeology, binary star demographics, and exoplanet population statistics — science that demands both the precision of dedicated instruments and the statistical power of hundreds of thousands of targets.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The authors identify improved line spread function modeling as the critical next step for SDSS-V's fiber-unified catalog; the full dataset and code are publicly available (Saydjari et al., APOGEE DR17 RV catalog, arXiv).</span></div></div>
</div>
