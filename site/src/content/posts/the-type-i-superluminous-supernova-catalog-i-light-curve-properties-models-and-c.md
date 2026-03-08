---
abstract: We present the most comprehensive catalog to date of Type I Superluminous
  Supernovae (SLSNe), a class of stripped envelope supernovae (SNe) characterized
  by exceptionally high luminosities. We have compiled a sample of 262 SLSNe reported
  through 2022 December 31. We verified the spectroscopic classification of each SLSN
  and collated an exhaustive data set of UV, optical and IR photometry from both publicly
  available data and our own FLEET observational follow-up program, totaling over
  30,000 photometric detections. Using these data we derive observational parameters
  such as the peak absolute magnitudes, rise and decline timescales, as well as bolometric
  luminosities, temperature and photospheric radius evolution for all SLSNe. Additionally,
  we model all light curves using a hybrid model that includes contributions from
  both a magnetar central engine and the radioactive decay of $^{56}$Ni. We explore
  correlations among various physical and observational parameters, and recover the
  previously found relation between ejecta mass and magnetar spin, as well as the
  overall progenitor pre-explosion mass distribution with a peak at $\approx 6.5$
  M$_\odot$. We find no significant redshift dependence for any parameter, and no
  evidence for distinct sub-types of SLSNe. We find that $< 3$\% of SLSNe are best
  fit with a significant contribution from radioactive decay $\gtrsim 50$\%, representing
  a set of relatively dim and slowly declining SNe. We provide several analytical
  tools designed to simulate typical SLSN light curves across a broad range of wavelengths
  and phases, enabling accurate K-corrections, bolometric scaling calculations, and
  inclusion of SLSNe in survey simulations or future comparison works. The complete
  catalog, including all of the photometry, models, and derived parameters, is made
  available as an open-source resource on GitHub.
arxivId: '2407.07946'
arxivUrl: https://arxiv.org/abs/2407.07946
authors:
- Sebastian Gomez
- Matt Nicholl
- Edo Berger
- Peter K. Blanchard
- V. Ashley Villar
- Sofia Rest
- Griffin Hosseinzadeh
- Aysha Aamer
- Yukta Ajay
- Wasundara Athukoralalage
- David C. Coulter
- Tarraneh Eftekhari
- Achille Fiore
- Noah Franz
- Ori Fox
- Alexander Gagliano
- Daichi Hiramatsu
- D. Andrew Howell
- Brian Hsu
- Mitchell Karmen
- Matthew R. Siebert
- Réka Könyves-Tóth
- Harsh Kumar
- Curtis McCully
- Craig Pellegrino
- Justin Pierel
- Armin Rest
- Qinan Wang
concepts:
- supernova classification
- magnetar central engine
- bolometric light curves
- bayesian inference
- stellar evolution
- surrogate modeling
- model validation
- regression
- calibration
- monte carlo methods
- simulation-based inference
- anomaly detection
figures:
- /iaifi-research-blog/figures/2407_07946/figure_1.png
- /iaifi-research-blog/figures/2407_07946/figure_1.png
- /iaifi-research-blog/figures/2407_07946/figure_2.png
- /iaifi-research-blog/figures/2407_07946/figure_2.png
- /iaifi-research-blog/figures/2407_07946/figure_3.png
- /iaifi-research-blog/figures/2407_07946/figure_3.png
pdfUrl: https://arxiv.org/pdf/2407.07946v1
published: '2024-07-10T18:00:03+00:00'
theme: Astrophysics
title: 'The Type I Superluminous Supernova Catalog I: Light Curve Properties, Models,
  and Catalog Description'
wordCount: 994
---

## The Big Picture

Imagine a star that explodes with the energy of 100 billion suns, so bright it briefly outshines entire galaxies. Now imagine that astronomers had been cataloging these extraordinary events for over a decade, but doing so in scattered, inconsistent ways. Different librarians each inventing their own filing system. You'd have a chaotic mess of data that makes it nearly impossible to answer the basic question: what *are* these things?

That's the situation with **Type I Superluminous Supernovae (SLSNe)**, stellar explosions so luminous they defy the usual rules. Ordinary supernovae are powered by the slow radioactive decay of nickel, a heavy element forged in the blast, like a glowing nuclear afterburn that fades over weeks. But SLSNe shine up to 100 times brighter than their common cousins, and that fuel simply can't account for all that power. Something else is going on.

A team led by Sebastian Gomez at the Space Telescope Science Institute has now built the largest uniformly analyzed catalog of these monsters ever assembled: 262 SLSNe, more than 30,000 individual brightness measurements, and a single consistent set of physical models applied to every event.

> **Key Insight:** By treating 262 superluminous supernovae with a unified framework, this catalog lets astronomers answer population-level questions about what powers these extreme explosions. The answer points overwhelmingly toward a spinning neutron star at the heart of each one.

## How It Works

The team hunted down every confirmed Type I SLSN reported in the scientific literature through the end of 2022. "Confirmed" mattered: the researchers personally verified the **spectroscopic classification** (the chemical fingerprint encoded in light that identifies an explosion type) for all 262 events. No hydrogen in the spectrum, luminosity above a set threshold. Those two criteria define a SLSN.

Then came the **photometry**, systematic brightness measurements over time. The team aggregated data across ultraviolet, optical, and infrared wavelengths from public archives and supplemented it with their own FLEET observational program. The result: 30,000+ data points tracing how each explosion brightened and faded.

![Figure 1](figure:1)

From that data, they extracted a suite of observational quantities for each event:
- **Peak absolute magnitude**: how intrinsically bright did it get at maximum?
- **Rise and decline timescales**: how quickly did it brighten, and how fast did it fade?
- **Bolometric luminosity**: total energy output across all wavelengths
- **Temperature and photospheric radius evolution**: tracking the physical size and heat of the expanding fireball

The real analytical muscle came from fitting every **light curve** (a graph tracking how brightness changes over time) with a hybrid physical model combining two power sources: a **magnetar central engine**, a rapidly spinning, highly magnetized neutron star that bleeds rotational energy into surrounding gas, and radioactive nickel-56 decay. Think of it like fitting a battery model to 262 different electronic devices. Same underlying physics, different specs for each.

![Figure 2](figure:2)

The fitting returned physical parameters for every event: the magnetar's initial spin period, its magnetic field strength, the mass of ejected material, and nickel yield. All of this was done consistently across the entire sample, with no cherry-picking and no case-by-case special treatment.

## Why It Matters

The results paint a coherent picture. The team recovered a previously suspected relationship between ejected mass and magnetar spin rate: faster-spinning magnetars correspond to less ejected material, suggesting a real physical link between the spinning remnant and the explosion dynamics. The inferred progenitor stars cluster around 6.5 solar masses at the time of explosion, pointing to a specific class of massive star that had shed its outer layers before detonating.

![Figure 4](figure:4)

What they *didn't* find may be just as important. Despite scanning 262 events across a wide range of cosmic distances, the team found no significant variation with distance. These explosions look the same whether they happened nearby or billions of light-years ago, meaning their properties haven't evolved across vast stretches of cosmic time.

They also found no evidence for distinct sub-types within the SLSN population, despite years of debate about whether "slow" and "fast" SLSNe represent fundamentally different phenomena. And fewer than 3% of events appear significantly powered by radioactive nickel rather than a magnetar. The magnetar model isn't just favored; it's nearly universal.

The catalog also delivers practical infrastructure for the next generation of sky surveys. The team built analytical functions that let anyone simulate a typical SLSN light curve at any wavelength and any phase. As Rubin Observatory's Legacy Survey of Space and Time comes online and discovers SLSNe by the thousands, calibrated templates and a clean reference sample become essential. The entire catalog (all photometry, model fits, and derived parameters) is publicly available on GitHub.

![Figure 6](figure:6)

> **Bottom Line:** The SLSN Catalog establishes magnetar spin-down as the dominant power source for these record-breaking explosions, delivers a population-level view of their progenitor stars, and provides open-source tools that will anchor superluminous supernova science for years to come.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work applies large-scale statistical analysis and uniform physical modeling to one of astrophysics' most extreme phenomena, connecting observational survey methodology with fundamental questions about neutron star physics and stellar evolution.

- **Impact on Artificial Intelligence:** The catalog's standardized light curve templates and analytical tools provide machine-learning-ready training data for automated transient classifiers operating on surveys like Rubin/LSST.

- **Impact on Fundamental Interactions:** By confirming magnetar central engines as the near-universal power source across 262 events and a wide redshift range, this work constrains the physics of extreme magnetic fields and neutron star formation at the moment of core collapse.

- **Outlook and References:** Future work will extend the catalog to host galaxy properties and environmental studies. The open-source release on GitHub invites community contributions, and the paper is available at [arXiv:2407.07946](https://arxiv.org/abs/2407.07946).
