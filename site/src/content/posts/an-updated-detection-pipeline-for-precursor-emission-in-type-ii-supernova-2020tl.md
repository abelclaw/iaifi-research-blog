---
abstract: We present a new photometric pipeline for the detection of pre-supernova
  (pre-SN) emission in the Young Supernova Experiment (YSE) sky survey. The method
  described is applied to SN 2020tlf, a type II SN (SN II) with precursor emission
  in the last ~100 days before first light. We re-analyze the YSE griz-band light
  curves of SN 2020tlf and provide revised pre-explosion photometry that includes
  a robust list of confident detection and limiting magnitudes. Compared to the results
  of Jacobson-Galan et al. 2022a, this new analysis yields fewer total r/i/z-band
  pre-SN detections at phases > -100 days. Furthermore, we discourage the use of the
  blackbody modeling of the pre-explosion spectral energy distribution, the pre-SN
  bolometric light curve and the blackbody model parameters presented in Jacobson-Galan
  et al. 2022a. Nevertheless, binned photometry of SN 2020tlf confirms a consistent
  progenitor luminosity of ~10$^{40}$ erg s$^{-1}$ before explosion.
arxivId: '2501.08475'
arxivUrl: https://arxiv.org/abs/2501.08475
authors:
- Wynn Jacobson-Galán
- Sebastian Gonzalez
- Shreyas Patel
- Luc Dessart
- David Jones
- Deanne Coppejans
- Georgios Dimitriadis
- Ryan J. Foley
- Charles D. Kilpatrick
- David Matthews
- Sofia Rest
- Giacomo Terreran
- Patrick D. Aleo
- Katie Auchettl
- Peter K. Blanchard
- David A. Coulter
- Kyle W. Davis
- Thomas de Boer
- Lindsay DeMarchi
- Maria R. Drout
- Nicholas Earl
- Alexander Gagliano
- Christa Gall
- Jens Hjorth
- Mark E. Huber
- Adaeze L. Ibik
- Danny Milisavljevic
- Yen-Chen Pan
- Armin Rest
- Ryan Ridden-Harper
- Cesar Rojas-Bravo
- Matthew R. Siebert
- Ken W. Smith
- Kirsty Taggart
- Samaporn Tinyanont
- Qinan Wang
- Yossef Zenati
concepts:
- signal detection
- pre-supernova precursor emission
- scientific workflows
- artificial source injection
- difference image photometry
- hypothesis testing
- model validation
- uncertainty quantification
- calibration
- stellar evolution
- supernova classification
figures:
- /iaifi-research-blog/figures/2501_08475/figure_1.png
- /iaifi-research-blog/figures/2501_08475/figure_1.png
- /iaifi-research-blog/figures/2501_08475/figure_2.png
- /iaifi-research-blog/figures/2501_08475/figure_2.png
- /iaifi-research-blog/figures/2501_08475/figure_3.png
- /iaifi-research-blog/figures/2501_08475/figure_3.png
pdfUrl: https://arxiv.org/pdf/2501.08475v1
published: '2025-01-14T22:39:05+00:00'
theme: Astrophysics
title: An Updated Detection Pipeline for Precursor Emission in Type II Supernova 2020tlf
wordCount: 1334
---

## The Big Picture

Imagine trying to predict a volcanic eruption by studying the subtle rumblings that happen weeks before the mountain blows, using a seismometer that wasn't even pointed directly at it. That's roughly what astronomers face when hunting for **pre-supernova emission**: the faint, restless glow a massive star emits in its final days before it tears itself apart.

In 2022, a landmark paper announced the detection of precursor activity in SN 2020tlf, a Type II supernova (the core-collapse explosion of a massive star) with telltale brightening in the ~100 days before explosion. Direct measurements of light showing a star shedding material violently before its death. But science is built on scrutiny.

Now the same lead author returns with a critical update: a new, more careful detection pipeline. The revised analysis confirms that SN 2020tlf's progenitor star (the star that later exploded) was genuinely luminous before it went off. But it also walks back finer details, reducing the number of confident detections and explicitly discouraging use of earlier temperature and luminosity estimates.

> **Key Insight:** This paper introduces a more conservative, statistically sound detection pipeline that confirms pre-supernova activity in SN 2020tlf while pruning away less reliable detections from the original analysis. Sometimes correcting your own work is the point.

## How It Works

The detection challenge is formidable. You're searching for a faint point of light at the future supernova location in archival survey images, before anyone knew a supernova was coming. Sky background and host galaxy glow conspire to wash out subtle signals.

Getting this right requires knowing exactly how faint a source you could have detected in each image. That means **artificial source injection**: literally adding fake stars to real images to test whether the pipeline can find them.

Here's how the new pipeline works:

1. **Build control light curves.** Rather than placing background apertures along an isophotal ellipse (an oval brightness contour used as a rough stand-in for local background variation), the new method places apertures along an isophotal contour that follows the actual brightness curve of the galaxy. This better captures true local background variation while avoiding the supernova location.

2. **Inject fake sources.** For each aperture position, the pipeline adds increasing amounts of artificial flux until the signal-to-noise ratio exceeds 3σ (three times the typical random background fluctuation, the standard threshold for a real detection). The fraction of apertures where the injected source is recovered yields a **recovery fraction curve** as a function of flux.

3. **Set a conservative threshold.** A pre-explosion measurement is flagged as a real detection only when it's brighter than the 80% recovery limiting magnitude, the flux level at which more than 80% of injected fake sources are successfully recovered. The 2022 study used a 50% efficiency threshold. That 30-percentage-point increase in conservatism makes a real difference.

![Figure 1](/iaifi-research-blog/figures/2501_08475/figure_1.png)

4. **Compare to actual photometry.** Measurements at the supernova location from the `Photpipe` reduction pipeline are compared against these conservative limits. Only those that clear the bar count as detections.

The numbers tell the story. The 2022 paper reported 2, 11, and 6 detections in the r, i, and z bands respectively. The new pipeline at the 80% recovery level finds just 1, 5, and 3. Nearly half of previous detections no longer clear the higher bar.

The team is also explicit that the blackbody spectral energy distribution fits (which used colors and brightness to estimate the pre-explosion source's temperature and physical size) and the derived temperature and radius parameters from 2022 should not be used going forward. The photometric basis for those fits was less reliable than understood at the time.

![Figure 2](/iaifi-research-blog/figures/2501_08475/figure_1.png)

What survives stricter scrutiny? The core physical result. Binned photometry across all bands consistently shows a progenitor luminosity of roughly 10⁴⁰ erg/s before explosion, about 2.5 million times the Sun's luminosity. That's bright even for a red supergiant in its death throes. Pre-explosion absolute magnitudes settle around M ≈ −11.5 to −12 in the riz bands.

The team also measured **forced photometry** (extracting a brightness measurement at a fixed sky location even when no obvious source is visible) at the supernova site using pre-explosion Pan-STARRS 3π survey imaging from 2011 to 2014, over three thousand days before first light. This quantifies how much underlying progenitor flux was subtracted out during **image differencing**, where a "before" image is subtracted from an "after" image to isolate new sources of light. That kind of careful bookkeeping separates a mature analysis from a preliminary one.

![Figure 3](/iaifi-research-blog/figures/2501_08475/figure_2.png)

## Why It Matters

Pre-supernova outbursts sit at the frontier of stellar physics. We still lack a first-principles model explaining why some massive stars erupt violently in the months before collapse while others go quietly. Catching these precursors requires being in the right place at the right time with the right sensitivity, and knowing with confidence what you've actually detected.

The new pipeline isn't just for SN 2020tlf. It's already been applied to other events in the Young Supernova Experiment survey. By establishing a community standard for detection (with injection recovery curves, conservative thresholds, and careful comparison to limiting magnitudes) this work lays the methodological foundation for a growing field.

As wide-field surveys like the Vera Rubin Observatory's LSST come online and capture unprecedented volumes of transient data, clean and reproducible detection algorithms matter more than ever. The pipeline described here offers a template.

> **Bottom Line:** SN 2020tlf really did show pre-explosion activity, but with fewer detections than previously reported and without the fine-grained spectral detail once claimed. This honest self-correction, paired with a more careful open-source pipeline, puts future pre-supernova science on firmer ground.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges observational astrophysics and data pipeline engineering, developing a statistical framework for detecting faint transient signals against noisy survey backgrounds, a challenge shared across many domains of AI-assisted astronomical discovery.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The artificial source injection and recovery fraction methodology offers a principled approach to calibrating detection thresholds in image-subtraction pipelines, directly applicable to machine learning classifiers trained on survey photometry.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By confirming pre-supernova luminosity at ~10⁴⁰ erg/s and revising earlier detections with stricter criteria, this paper sharpens observational constraints on the final evolutionary stages of massive stars before core collapse.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future wide-field surveys will dramatically expand the sample of pre-SN candidates, making well-calibrated pipelines like this one essential; the paper is available as [arXiv:2501.08475](https://arxiv.org/abs/2501.08475) as part of the ongoing Young Supernova Experiment program.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">An Updated Detection Pipeline for Precursor Emission in Type II Supernova 2020tlf</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2501.08475](https://arxiv.org/abs/2501.08475)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">Wynn Jacobson-Galán, Sebastian Gonzalez, Shreyas Patel, Luc Dessart, David Jones, Deanne Coppejans, Georgios Dimitriadis, Ryan J. Foley, Charles D. Kilpatrick, David Matthews, Sofia Rest, Giacomo Terreran, Patrick D. Aleo, Katie Auchettl, Peter K. Blanchard, David A. Coulter, Kyle W. Davis, Thomas de Boer, Lindsay DeMarchi, Maria R. Drout, Nicholas Earl, Alexander Gagliano, Christa Gall, Jens Hjorth, Mark E. Huber, Adaeze L. Ibik, Danny Milisavljevic, Yen-Chen Pan, Armin Rest, Ryan Ridden-Harper, Cesar Rojas-Bravo, Matthew R. Siebert, Ken W. Smith, Kirsty Taggart, Samaporn Tinyanont, Qinan Wang, Yossef Zenati</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We present a new photometric pipeline for the detection of pre-supernova (pre-SN) emission in the Young Supernova Experiment (YSE) sky survey. The method described is applied to SN 2020tlf, a type II SN (SN II) with precursor emission in the last ~100 days before first light. We re-analyze the YSE griz-band light curves of SN 2020tlf and provide revised pre-explosion photometry that includes a robust list of confident detection and limiting magnitudes. Compared to the results of Jacobson-Galan et al. 2022a, this new analysis yields fewer total r/i/z-band pre-SN detections at phases > -100 days. Furthermore, we discourage the use of the blackbody modeling of the pre-explosion spectral energy distribution, the pre-SN bolometric light curve and the blackbody model parameters presented in Jacobson-Galan et al. 2022a. Nevertheless, binned photometry of SN 2020tlf confirms a consistent progenitor luminosity of ~10$^{40}$ erg s$^{-1}$ before explosion.</span></div></div>
</div>
