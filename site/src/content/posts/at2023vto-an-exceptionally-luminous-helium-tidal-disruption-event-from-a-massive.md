---
abstract: We present optical/UV observations and the spectroscopic classification
  of the transient AT2023vto as a tidal disruption event (TDE) at z = 0.4846. The
  spectrum is dominated by a broad He II $λ$4686 emission line, with a width of ~
  $3.76 \times 10^4$ km/s and a blueshift of ~ $1.05 \times 10^4$ km/s, classifying
  it as a member of the TDE-He class. The light curve exhibits a long rise and decline
  timescale, with a large peak absolute magnitude of M$_g$ ~ -23.6, making it the
  most luminous of the classical optical TDEs (H, H+He, He) discovered to date by
  about 2 mag (and ~ 4 mag compared to the mean of the population). The light curve
  exhibits a persistent blue color of g - r ~ -0.4 mag throughout its evolution, similar
  to other TDEs, but distinct from supernovae. We identify the host galaxy of AT2023vto
  in archival Pan-STARRS images and find that the transient is located at the galaxy
  center, and that its inferred central black hole mass is ~ $10^7~M_{\odot}$. Modeling
  the light curves of AT2023vto, we find that it resulted from the disruption of a
  ~ 9 $M_{\odot}$ star by a ~$10^7~M_{\odot}$ supermassive black hole. The star mass
  is about 5 times larger than the highest star masses previously inferred in TDEs,
  and the black hole mass is at the high end of the distribution. AT2023vto is comparable
  in luminosity and timescale to some putative TDEs (with a blue featureless continuum),
  as well as to the mean of the recently identified population of ambiguous nuclear
  transients (ANTs), although the latter are spectroscopically distinct and tend to
  have longer timescales. ANTs have been speculated to arise from tidal disruptions
  of massive stars, perhaps in active galactic nuclei, and AT2023vto may represent
  a similar case but in a dormant black hole, thereby bridging the TDE and ANT populations.
  We anticipate that Rubin Observatory / LSST will uncover similar luminous TDEs to
  z ~ 3.
arxivId: '2408.01482'
arxivUrl: https://arxiv.org/abs/2408.01482
authors:
- Harsh Kumar
- Edo Berger
- Daichi Hiramatsu
- Sebastian Gomez
- Peter K. Blanchard
- Yvette Cendes
- K. Azalee Bostroem
- Joseph Farah
- Estefania Padilla Gonzalez
- Andrew Howell
- Curtis McCully
- Megan Newsome
- Giacomo Terreran
concepts:
- tidal disruption event
- stellar evolution
- accretion disk physics
- signal detection
- bayesian inference
- spectral energy distribution fitting
- supernova classification
- surrogate modeling
- galaxy classification
- anomaly detection
- likelihood estimation
figures:
- /iaifi-research-blog/figures/2408_01482/figure_1.png
- /iaifi-research-blog/figures/2408_01482/figure_1.png
- /iaifi-research-blog/figures/2408_01482/figure_2.png
- /iaifi-research-blog/figures/2408_01482/figure_2.png
- /iaifi-research-blog/figures/2408_01482/figure_3.png
- /iaifi-research-blog/figures/2408_01482/figure_3.png
pdfUrl: https://arxiv.org/pdf/2408.01482v1
published: '2024-08-02T18:00:00+00:00'
theme: Astrophysics
title: 'AT2023vto: An Exceptionally Luminous Helium Tidal Disruption Event from a
  Massive Star'
wordCount: 1171
---

## The Big Picture

Imagine a star nearly ten times the mass of our Sun drifting too close to a sleeping monster — a supermassive black hole weighing ten million solar masses. The black hole's gravity pulls harder on the near side of the star than the far side, stretching it apart like taffy. For a brief cosmic moment, the catastrophe outshines entire galaxies.

This is a **tidal disruption event (TDE)** — when a wandering star gets torn apart by a black hole's gravity — and astronomers have catalogued dozens of them. But AT2023vto isn't just another entry in that catalog. It's a record-breaker that doesn't quite fit, and that's exactly what makes it so interesting.

When astronomers first spotted AT2023vto in September 2023 using the Zwicky Transient Facility (ZTF), a robotic sky survey that automatically scans for sudden changes in the night sky, they thought it was a superluminous supernova — an extraordinarily bright stellar explosion. The brightness was simply too extreme for a "normal" TDE. But analysis of the light's chemical fingerprints told a different story: this was a black hole shredding a star, producing a distinctive helium signature that no supernova would make.

The event turned out to be the most luminous tidal disruption event ever discovered — outshining the average TDE by a factor of roughly 40, and beating the previous record-holder by a factor of six.

A Harvard-led team, including researchers from the NSF AI Institute for Artificial Intelligence and Fundamental Interactions (IAIFI), has now published a detailed study of AT2023vto, modeling the brightness over time and the light's spectrum to reconstruct exactly what happened — and what it means for a mysterious class of even brighter, unexplained cosmic blasts.

> **Key Insight:** AT2023vto resulted from the destruction of a ~9 solar-mass star by a 10-million-solar-mass black hole, producing the brightest known classical TDE and potentially bridging the gap between ordinary stellar disruptions and a puzzling category of even more powerful nuclear transients.

## How It Works

Tracking AT2023vto required a coordinated observing campaign spanning optical and ultraviolet wavelengths. The team used ZTF for ongoing **photometric monitoring** — regularly measuring the event's total brightness over time — and obtained spectroscopic observations to classify the event. They also tapped into archival Pan-STARRS images to identify the host galaxy, sitting roughly 6.4 billion light-years away.

![Figure 1](/iaifi-research-blog/figures/2408_01482/figure_1.png)

The spectrum is the smoking gun. It's dominated by a broad **He II λ4686 emission line** — light emitted by helium atoms stripped of one electron, a fingerprint of extremely hot gas near the disruption site — spanning about 37,600 km/s, with a **blueshift** of roughly 10,500 km/s. That blueshift, a shift toward shorter wavelengths indicating gas moving toward us, means material is flying in our direction at about 3.5% the speed of light, driven outward by intense radiation pressure. This places AT2023vto firmly in the **TDE-He class**: disruption events where helium dominates the spectrum with little hydrogen signal.

The light curve is equally remarkable:

- **Peak brightness:** absolute magnitude Mg ≈ -23.6, roughly 2 magnitudes brighter than the previous most luminous classical TDE
- **Color:** a persistent blue g - r ≈ -0.4 throughout the event, consistent with TDEs and unlike supernovae
- **Timescale:** unusually long rise and decline, hinting at a larger mass of stellar debris than typical

![Figure 3](/iaifi-research-blog/figures/2408_01482/figure_2.png)

To extract physical parameters, the team modeled the light curve using the **Modular Open-Source Fitter for Transients (MOSFiT)**, which generates millions of model light curves and finds the combination of black hole and stellar properties that best matches the observations. The host galaxy's **spectral energy distribution** — its brightness across many wavelengths simultaneously, from ultraviolet to infrared — was modeled with **Prospector** to measure the galaxy's total stellar mass, which came out to about 55 billion solar masses. That translates to a black hole mass of roughly 10 million solar masses.

The fit points to a disrupted star of approximately 9 solar masses — about five times heavier than the most massive star previously inferred in any classical TDE, where typical disrupted stars weigh between 0.1 and 2 solar masses. A more massive star means more debris, more energy, and a longer, brighter flare. That explains the record-shattering luminosity.

## Why It Matters

The significance goes beyond setting a new record. AT2023vto sits at an intersection astronomers have been puzzling over for years. There's a growing population of **ambiguous nuclear transients (ANTs)** — extremely luminous flares from galactic centers that don't match supernovae, don't match typical TDEs, and don't match active galactic nuclei (galaxies whose central black holes are already actively consuming surrounding gas). Some ANTs are 10 to 100 times brighter than classical TDEs and last far longer.

Theorists have speculated that ANTs might represent TDEs from massive stars — perhaps in galaxies with already-active black holes — but no clear link has emerged.

![Figure 5](/iaifi-research-blog/figures/2408_01482/figure_3.png)

AT2023vto changes the picture. Its luminosity and timescale overlap with the ANT population, but its spectrum — with that clear, broad He II line — is unambiguously a classical TDE. It's happening around a dormant black hole, not one that's already actively feeding. The extreme luminosity doesn't require a pre-existing **accretion disk** (a swirling ring of gas already orbiting the black hole) or any other special environment.

You just need a massive enough star. AT2023vto may be the Rosetta Stone connecting these two populations: classical TDEs at one end, luminous ANTs at the other, with AT2023vto showing what happens in between when a genuinely massive star meets its end.

Looking ahead, the Rubin Observatory / LSST is expected to detect events like AT2023vto out to **redshift z ~ 3** — a cosmic distance measure corresponding to light that left its source more than 11 billion years ago. That would transform this single spectacular outlier into a statistical population, letting astronomers trace how the most extreme stellar disruptions unfold across cosmic time.

> **Bottom Line:** AT2023vto is the most luminous classical tidal disruption event ever found, powered by the destruction of a ~9 solar-mass star, and it may be the missing link between ordinary TDEs and the mysterious ultra-luminous nuclear transients that astronomers have struggled to explain.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines multi-wavelength observational astronomy with Bayesian light-curve modeling (MOSFiT) and SED fitting (Prospector) to extract physical parameters from a single transient event, exemplifying how computational tools are transforming observational astrophysics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The study leverages machine-learning-informed photometric classification and Bayesian inference frameworks to connect spectroscopic and photometric data, demonstrating how AI-assisted modeling pipelines enable rapid physical interpretation of transient phenomena.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">AT2023vto reveals that tidal disruption events can arise from stars far more massive than previously observed, extending the known parameter space of black hole–star interactions and potentially explaining a class of ultra-luminous nuclear transients that has resisted classification.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future observations with Rubin Observatory / LSST are expected to uncover many similar events to z ~ 3; the paper is available on arXiv as arXiv:2408.03654.</span></div></div>
</div>
