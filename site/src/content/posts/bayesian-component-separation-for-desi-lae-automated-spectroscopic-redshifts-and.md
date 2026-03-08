---
abstract: Lyman Alpha Emitters (LAEs) are valuable high-redshift cosmological probes
  traditionally identified using specialized narrow-band photometric surveys. In ground-based
  spectroscopy, it can be difficult to distinguish the sharp LAE peak from residual
  sky emission lines using automated methods, leading to misclassified redshifts.
  We present a Bayesian spectral component separation technique to automatically determine
  spectroscopic redshifts for LAEs while marginalizing over sky residuals. We use
  visually inspected spectra of LAEs obtained using the Dark Energy Spectroscopic
  Instrument (DESI) to create a data-driven prior and can determine redshift by jointly
  inferring sky residual, LAE, and residual components for each individual spectrum.
  We demonstrate this method on 910 spectroscopically observed $z = 2-4$ DESI LAE
  candidate spectra and determine their redshifts with $>$90% accuracy when validated
  against visually inspected redshifts. Using the $Δχ^2$ value from our pipeline as
  a proxy for detection confidence, we then explore potential survey design choices
  and implications for targeting LAEs with medium-band photometry. This method allows
  for scalability and accuracy in determining redshifts from DESI spectra, and the
  results provide recommendations for LAE targeting in anticipation of future high-redshift
  spectroscopic surveys.
arxivId: '2504.06870'
arxivUrl: https://arxiv.org/abs/2504.06870
authors:
- Ana Sofía M. Uzsoy
- Andrew K. Saydjari
- Arjun Dey
- Anand Raichoor
- Douglas P. Finkbeiner
- Eric Gawiser
- Kyoung-Soo Lee
- Steven Ahlen
- Davide Bianchi
- David Brooks
- Todd Claybaugh
- Andrei Cuceu
- Axel de la Macorra
- Peter Doel
- Andreu Font-Ribera
- Jaime E. Forero-Romero
- Enrique Gaztañaga
- Satya Gontcho A Gontcho
- Gaston Gutierrez
- Mustapha Ishak
- Robert Kehoe
- David Kirkby
- Anthony Kremin
- Martin Landriau
- Laurent Le Guillou
- Aaron Meisner
- Ramon Miquel
- John Moustakas
- Nathalie Palanque-Delabrouille
- Francisco Prada
- Ignasi Pérez-Ràfols
- Graziano Rossi
- Eusebio Sanchez
- David Schlegel
- Michael Schubnell
- Hee-Jong Seo
- David Sprayberry
- Gregory Tarlé
- Benjamin Alan Weaver
- Hu Zou
concepts:
- bayesian inference
- posterior estimation
- sky residual marginalization
- signal detection
- spectral methods
- data-driven spectral prior
- likelihood ratio
- inverse problems
- galaxy classification
- scalability
- experimental design
figures:
- /iaifi-research-blog/figures/2504_06870/figure_1.png
- /iaifi-research-blog/figures/2504_06870/figure_1.png
- /iaifi-research-blog/figures/2504_06870/figure_2.png
- /iaifi-research-blog/figures/2504_06870/figure_2.png
- /iaifi-research-blog/figures/2504_06870/figure_3.png
- /iaifi-research-blog/figures/2504_06870/figure_3.png
pdfUrl: https://arxiv.org/pdf/2504.06870v1
published: '2025-04-09T13:21:20+00:00'
theme: Astrophysics
title: Bayesian Component Separation for DESI LAE Automated Spectroscopic Redshifts
  and Photometric Targeting
wordCount: 1075
---

## The Big Picture

Imagine trying to hear a whisper in a crowded stadium. You know the whisper exists — you can even predict what frequency it'll be — but the roar of the crowd keeps drowning it out. That's roughly the challenge astronomers face when hunting for some of the universe's most ancient galaxies from the ground.

**Lyman Alpha Emitters**, or **LAEs**, are young, intensely star-forming galaxies that glow brightly at a specific wavelength of ultraviolet light. This glow acts like a fingerprint — a signature color that lets astronomers identify these galaxies across cosmic distances. We see them as they appeared 10 to 12 billion years ago, measured by **redshift**: the stretching of light as it travels through an expanding universe, where a higher number means the light has traveled farther and longer.

LAEs are extraordinary time capsules. They illuminate the epoch of reionization — the early chapter when the universe's hydrogen gas turned from opaque to transparent, finally letting light travel freely — and may be the ancestors of galaxies like our own Milky Way.

The problem: Earth's atmosphere emits its own light at exactly the wavelengths you care about. These **sky residuals** — faint glows and artifacts from imperfect removal of the atmosphere's emission — look remarkably like the galaxy signals you're hunting for. Automated software routinely mistakes them for real detections, real discoveries get lost, and catalogs fill with contaminants.

A team led by Ana Sofía Uzsoy and Andrew Saydjari at the Center for Astrophysics | Harvard & Smithsonian has built a Bayesian pipeline that solves this automatically — achieving over 90% redshift accuracy on nearly a thousand LAE candidates without a single human examining the spectra.

> **Key Insight:** By treating sky contamination not as noise to subtract but as a component to *model simultaneously* with the galaxy signal, the new pipeline correctly recovers LAE redshifts even when sky residuals mimic the very emission feature being sought.

## How It Works

The core idea is **Bayesian spectral component separation**: instead of removing sky contamination first and then finding the galaxy, the pipeline asks what combination of (1) an LAE signal, (2) sky residuals, and (3) a smooth background continuum best explains the observed spectrum.

![Figure 1](/iaifi-research-blog/figures/2504_06870/figure_1.png)

Building the model requires a data-driven prior — a statistical description of what typical LAE spectra look like, constructed from real examples rather than assumptions. This is the same philosophy used to separate the cosmic microwave background (the faint afterglow of the Big Bang) from foreground emissions in all-sky maps — now applied at the scale of individual galaxy spectra.

The team built this prior from visually inspected spectra collected by the **Dark Energy Spectroscopic Instrument (DESI)**, a spectrograph at Kitt Peak Observatory in Arizona capable of observing 5,000 galaxies simultaneously. From confirmed LAEs, they constructed a **principal component analysis (PCA)** basis — a compact catalog of the most common spectral shapes in real LAEs that can reconstruct any individual galaxy's spectrum without overfitting. Sky residuals get their own PCA basis, derived from blank sky regions observed alongside the galaxies.

For each candidate spectrum, the inference proceeds:

1. Evaluate a grid of candidate redshifts
2. At each redshift, fit the spectrum as a linear combination of LAE templates + sky residual templates + smooth continuum
3. Compute **Δχ²** (delta chi-squared) — the improvement in fit quality when including the LAE component versus excluding it
4. The redshift with the highest Δχ² wins

![Figure 2](/iaifi-research-blog/figures/2504_06870/figure_1.png)

This Δχ² statistic does double duty: it identifies the best-fit redshift *and* serves as a confidence metric. High Δχ² signals a clean detection; low Δχ² flags spectra where sky contamination may be masquerading as a galaxy. The pipeline ranks its own confidence without requiring ad-hoc quality cuts.

![Figure 3](/iaifi-research-blog/figures/2504_06870/figure_2.png)

## Why It Matters

Applied to 910 DESI LAE candidates spanning redshifts z = 2–4 — galaxies whose light has traveled for most of the universe's 13.8 billion year history — the pipeline achieved **greater than 90% redshift accuracy** against the gold standard of human visual inspection. That's not just useful; it's sufficient for building cosmological catalogs.

The team also showed how the Δχ² metric can guide future survey design. Medium-band photometric filters — broader than traditional narrow-band filters but narrower than wide-field imaging — offer a compromise between survey efficiency and targeting precision. Redder filters capture more objects at higher redshift but admit more contaminants. The pipeline's confidence metric provides a principled way to navigate these tradeoffs, yielding concrete recommendations for DESI-II and next-generation facilities.

![Figure 4](/iaifi-research-blog/figures/2504_06870/figure_2.png)

![Figure 5](/iaifi-research-blog/figures/2504_06870/figure_3.png)

![Figure 6](/iaifi-research-blog/figures/2504_06870/figure_3.png)

The elegance of the approach is that it doesn't try to outsmart the sky — it builds a better model of it. By treating sky residuals as structured signal with its own PCA basis rather than featureless noise, the pipeline avoids the systematic errors that plague simpler subtraction methods. That same philosophy applies to other spectroscopic surveys and other emission-line galaxy populations.

Upcoming surveys — DESI's extended campaigns, the Subaru Prime Focus Spectrograph, eventually the Extremely Large Telescope — will collect tens of thousands of LAE spectra. Automated, reliable redshift determination at scale isn't a nice-to-have; it's a prerequisite for the science. A pipeline that achieves 90%+ accuracy while quantifying its own uncertainty and informing photometric targeting strategy is a genuine operational advance.

> **Bottom Line:** A Harvard-led team has built a Bayesian pipeline that automatically determines redshifts for distant Lyman Alpha Emitter galaxies observed by DESI with >90% accuracy — by modeling sky contamination as a component to fit rather than noise to remove — directly enabling the scalable LAE surveys needed to probe the universe's first billion years.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines Bayesian inference, principal component analysis, and observational spectroscopy to solve a core data analysis challenge in cosmology, exemplifying how statistical AI methods can directly unlock fundamental astrophysics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The pipeline demonstrates that data-driven priors built from expert-labeled examples enable accurate automated classification even when signal and contaminant are spectrally similar — a transferable lesson for scientific machine learning broadly.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling scalable, accurate redshift determination for LAEs at z = 2–4, the method unlocks population-level constraints on reionization history and the large-scale structure of the early universe from DESI data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The pipeline's survey design recommendations position it as a planning tool for DESI-II and next-generation spectroscopic facilities; the full analysis is available at arXiv:2510.18621.</span></div></div>
</div>
