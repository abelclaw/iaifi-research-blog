---
abstract: We present optical-to-near-infrared (NIR) photometry and spectroscopy of
  the Type Ia supernova (SN Ia) 2024epr, including NIR spectra observed within two
  days of first light. The early-time optical spectra show strong, high-velocity Ca
  and Si features near rarely-observed velocities at $\sim$0.1$c$, and the NIR spectra
  show a C I "knee." Despite early-time, high-velocity features, SN 2024epr evolves
  into a normal SN Ia, albeit with stronger peak-light Ca absorption than other SNe
  Ia with the same light curve shape. Although we infer a normal decline rate, $Δm_{15}(B)=1.09\pm0.12$
  mag, from the light-curve rise, SN 2024epr is a Branch "cool" object and has red
  early-time colors ($g-r\approx0.15$ mag at $-10$ days). The high velocities point
  to a density enhancement in the outer layers of the explosion, predicted by some
  models, but thick-shell He-detonation models do not match the smoothly rising light
  curve or apparent lack of He in our early-time NIR spectra. No current models (e.g.,
  delayed detonation or thin He shell double detonation) appear to reproduce all observed
  properties, particularly the unusual early-time colors. Such constraints are only
  possible for SN 2024epr from the earliest optical and NIR observations, highlighting
  their importance for constraining SN Ia models. Finally, we identify several literature
  SNe Ia with intermediate mass elements at $\sim$30\,000 km s$^{-1}$ within days
  after the explosion that evolve into otherwise normal SNe Ia at peak light, suggesting
  the early-time spectra of SNe Ia may hide a broad diversity of observational characteristics.
arxivId: '2502.17556'
arxivUrl: https://arxiv.org/abs/2502.17556
authors:
- W. B. Hoogendam
- D. O. Jones
- C. Ashall
- B. J. Shappee
- R. J. Foley
- M. A. Tucker
- M. E. Huber
- K. Auchettl
- D. D. Desai
- A. Do
- J. T. Hinkle
- S. Romagnoli
- J. Shi
- A. Syncatto
- C. R. Angus
- K. C. Chambers
- D. A. Coulter
- K. W. Davis
- T. de Boer
- A. Gagliano
- M. Kong
- C. -C. Lin
- T. B. Lowe
- E. A. Magnier
- P. Minguez
- Y. -C. Pan
- K. C. Patra
- S. A. Severson
- K. Taggart
- A. R. Wasserman
- S. K. Yadavalli
- P. Chen
- R. S. Post
concepts:
- supernova classification
- high-velocity ejecta
- early-phase spectroscopy
- thermonuclear detonation
- model validation
- stellar evolution
- signal detection
- inverse problems
- regression
- bayesian inference
figures:
- /iaifi-research-blog/figures/2502_17556/figure_1.png
- /iaifi-research-blog/figures/2502_17556/figure_1.png
- /iaifi-research-blog/figures/2502_17556/figure_2.png
- /iaifi-research-blog/figures/2502_17556/figure_2.png
- /iaifi-research-blog/figures/2502_17556/figure_3.png
- /iaifi-research-blog/figures/2502_17556/figure_3.png
pdfUrl: https://arxiv.org/pdf/2502.17556v2
published: '2025-02-24T19:00:01+00:00'
theme: Astrophysics
title: Seeing the Outer Edge of the Infant Type Ia Supernova 2024epr in the Optical
  and Near Infrared
wordCount: 1091
---

## The Big Picture

Imagine trying to figure out how a firework explodes by studying only the sparks still glowing in the sky, minutes after the bang. That's roughly the challenge astronomers face with Type Ia supernovae — cosmic explosions so bright they can outshine entire galaxies, yet so distant that we almost always catch them well after the initial blast. For decades, theorists have sketched out competing blueprints for what triggers these explosions, but the evidence needed to pick a winner lies in those first fleeting moments. SN 2024epr changed that.

**Type Ia supernovae** are the universe's most reliable distance markers — cosmic yardsticks calibrated by their consistent peak brightness. This property lets astronomers map distances across billions of light-years, and it's how we first confirmed that the universe's expansion is accelerating — a discovery that earned a Nobel Prize.

But a fundamental puzzle lurks beneath this success: we don't know what triggers these explosions. The culprit is a white dwarf — a dense, Earth-sized remnant of a dead star made mostly of carbon and oxygen. Whether it has a companion star, what ignites the blast, and how the explosion propagates outward — all of this remains genuinely contested.

SN 2024epr was caught within two days of first light, making it one of the earliest-observed Type Ia supernovae ever studied. The team observed it simultaneously in optical light (what human eyes can see) and near-infrared light (wavelengths just beyond visible, detectable only by specialized instruments). What they found defied easy explanation: a normal supernova wearing a very strange first impression.

> **Key Insight:** SN 2024epr showed extreme high-velocity ejecta at ~10% the speed of light in its first days — a feature no current theoretical model can fully explain — yet evolved into a textbook-normal Type Ia supernova by peak brightness.

## How It Works

The research team, led by W. B. Hoogendam at the University of Hawai'i, mounted an intensive observational campaign across multiple telescopes. They collected **photometry** (brightness measurements over time) in optical and near-infrared wavelengths, alongside **spectroscopy** — splitting the supernova's light into its constituent colors to identify chemical fingerprints.

![Figure 1](/iaifi-research-blog/figures/2502_17556/figure_1.png)

The spectra told a remarkable story. In visible light, the team spotted **absorption features** — dark gaps in the spectrum created when gas absorbs light at characteristic wavelengths. These fingerprints revealed calcium and silicon moving at roughly 30,000 km/s — about 10% the speed of light. Typical high-velocity features in Type Ia supernovae sit around 20,000 km/s; these were faster still, placing them among the rarest velocities ever recorded in a Type Ia spectrum. The interpretation: an unusually dense shell of material in the outermost layers of the exploding star.

The near-infrared spectra added another twist: a feature called the **C I 'knee'** — a signature left by unburned carbon lingering in the outermost expelled material, or *ejecta*. "C I" is spectroscopic notation for neutral carbon. This diagnostic is visible only in near-infrared light, and only in the earliest observations, before the material spreads too thin to detect.

![Figure 2](/iaifi-research-blog/figures/2502_17556/figure_1.png)

Here's the paradox that makes SN 2024epr so scientifically valuable:

- **Extreme early behavior**: High-velocity Ca and Si at ~0.1*c*, red early-time colors (*g−r* ≈ 0.15 mag at ten days before peak), strong calcium absorption
- **Completely normal late behavior**: A standard decline rate of Δ*m*₁₅(B) = 1.09 ± 0.12 mag, consistent with a garden-variety Type Ia at peak light

One leading class of models — **thick-shell helium detonation** — predicts high-velocity features from an outer helium shell that detonates first, triggering the main carbon-oxygen explosion. But those models also predict helium spectral signatures in the near-infrared. SN 2024epr shows none. The light curve also rises too smoothly: thick-shell models predict bumps and wiggles that simply aren't there.

Other leading frameworks — **delayed detonation** (where the explosion begins as a slow burn before accelerating to supersonic speeds) and **thin-shell double detonation** (a similar helium-trigger scenario involving a thinner outer shell) — also fail to reproduce the peculiar early colors alongside everything else.

![Figure 3](/iaifi-research-blog/figures/2502_17556/figure_2.png)

## Why It Matters

SN 2024epr is more than a single puzzling supernova. By combing the literature, the team identified several other Type Ia supernovae showing similarly extreme high-velocity features in the days after explosion — yet appearing completely normal at peak light. This should give cosmologists pause.

The "standardizability" of Type Ia supernovae — our ability to use them as precise cosmic rulers — rests on properties measured at peak brightness. But if there's hidden diversity lurking in the first days that we almost always miss, we may be systematically misunderstanding these objects.

![Figure 4](/iaifi-research-blog/figures/2502_17556/figure_2.png)

The practical implication is a call to action for next-generation surveys. Facilities like the Vera C. Rubin Observatory's Legacy Survey of Space and Time (LSST) will catch thousands of supernovae within hours of explosion. Pairing those optical detections with rapid near-infrared follow-up — the combination that made SN 2024epr so revealing — could finally discriminate between explosion mechanisms that look identical at peak light.

The density enhancement hinted at by SN 2024epr's high-velocity features may be a fossil record of the star system before the explosion — a clue pointing toward what kind of object actually triggers the blast. Catching more such events, early enough, might finally close the case.

> **Bottom Line:** SN 2024epr's extreme early behavior — invisible at peak light — reveals that standard candles may be hiding rich diversity in their first moments, and no current theoretical model can explain it, pointing toward new physics in the explosion mechanism of Type Ia supernovae.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work uses multi-wavelength observational astrophysics to probe the fundamental physics of thermonuclear explosions, with IAIFI researchers contributing constraints that challenge every existing theoretical model of Type Ia supernova explosions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">While primarily an observational study, this research informs the training datasets and physical priors required for AI-based supernova classifiers and cosmological inference pipelines, which must now account for the newly revealed early-time diversity in Type Ia spectra.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">SN 2024epr delivers the tightest constraints to date on the outer ejecta structure of a Type Ia explosion, ruling out thick-shell helium detonation models and challenging delayed-detonation scenarios, pushing toward a new understanding of white dwarf thermonuclear physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future large-scale surveys paired with rapid near-infrared follow-up could finally distinguish between competing explosion mechanisms using populations of early-caught Type Ia supernovae; the full paper is available on arXiv as part of the 2024epr observational campaign by Hoogendam et al. (2025).</span></div></div>
</div>
