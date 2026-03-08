---
abstract: We present the discovery of the Type II supernova SN 2023ixf in M101 and
  follow-up photometric and spectroscopic observations, respectively, in the first
  month and week of its evolution. Our discovery was made within a day of estimated
  first light, and the following light curve is characterized by a rapid rise ($\approx5$
  days) to a luminous peak ($M_V\approx-18.2$ mag) and plateau ($M_V\approx-17.6$
  mag) extending to $30$ days with a fast decline rate of $\approx0.03$ mag day$^{-1}$.
  During the rising phase, $U-V$ color shows blueward evolution, followed by redward
  evolution in the plateau phase. Prominent flash features of hydrogen, helium, carbon,
  and nitrogen dominate the spectra up to $\approx5$ days after first light, with
  a transition to a higher ionization state in the first $\approx2$ days. Both the
  $U-V$ color and flash ionization states suggest a rise in the temperature, indicative
  of a delayed shock breakout inside dense circumstellar material (CSM). From the
  timescales of CSM interaction, we estimate its compact radial extent of $\sim(3-7)\times10^{14}$
  cm. We then construct numerical light-curve models based on both continuous and
  eruptive mass-loss scenarios shortly before explosion. For the continuous mass-loss
  scenario, we infer a range of mass-loss history with $0.1-1.0\,M_\odot\,{\rm yr}^{-1}$
  in the final $2-1$ yr before explosion, with a potentially decreasing mass loss
  of $0.01-0.1\,M_\odot\,{\rm yr}^{-1}$ in $\sim0.7-0.4$ yr toward the explosion.
  For the eruptive mass-loss scenario, we favor eruptions releasing $0.3-1\,M_\odot$
  of the envelope at about a year before explosion, which result in CSM with mass
  and extent similar to the continuous scenario. We discuss the implications of the
  available multiwavelength constraints obtained thus far on the progenitor candidate
  and SN 2023ixf to our variable CSM models.
arxivId: '2307.03165'
arxivUrl: https://arxiv.org/abs/2307.03165
authors:
- Daichi Hiramatsu
- Daichi Tsuna
- Edo Berger
- Koichi Itagaki
- Jared A. Goldberg
- Sebastian Gomez
- Kishalay De
- Griffin Hosseinzadeh
- K. Azalee Bostroem
- Peter J. Brown
- Iair Arcavi
- Allyson Bieryla
- Peter K. Blanchard
- Gilbert A. Esquerdo
- Joseph Farah
- D. Andrew Howell
- Tatsuya Matsumoto
- Curtis McCully
- Megan Newsome
- Estefania Padilla Gonzalez
- Craig Pellegrino
- Jaehyon Rhee
- Giacomo Terreran
- József Vinkó
- J. Craig Wheeler
concepts:
- supernova classification
- circumstellar interaction
- stellar evolution
- shock breakout
- flash spectroscopy
- inverse problems
- surrogate modeling
- signal detection
- bayesian inference
- stochastic processes
- neutrino detection
figures:
- /iaifi-research-blog/figures/2307_03165/figure_1.png
- /iaifi-research-blog/figures/2307_03165/figure_1.png
- /iaifi-research-blog/figures/2307_03165/figure_2.png
- /iaifi-research-blog/figures/2307_03165/figure_2.png
- /iaifi-research-blog/figures/2307_03165/figure_3.png
- /iaifi-research-blog/figures/2307_03165/figure_3.png
pdfUrl: https://arxiv.org/pdf/2307.03165v2
published: '2023-07-06T17:47:01+00:00'
theme: Astrophysics
title: 'From Discovery to the First Month of the Type II Supernova 2023ixf: High and
  Variable Mass Loss in the Final Year before Explosion'
wordCount: 1081
---

## The Big Picture

Imagine watching a star die in real time. Most stellar explosions are found days or weeks after they begin, the initial flash already faded, the critical first moments lost. But in May 2023, astronomers caught something extraordinary: a massive star in the nearby Pinwheel Galaxy (M101) detonating almost in the act. The supernova, dubbed SN 2023ixf, became one of the closest and best-observed stellar explosions in decades.

The central mystery wasn't the explosion itself. Scientists have known for decades that stars more than eight times the Sun's mass end their lives as supernovae. The puzzle is what happens in the months and years *before* the detonation. Standard stellar evolution theory predicts relatively calm, gradual mass loss as a star ages. But a growing body of evidence says something far more dramatic and erratic happens right before the end.

A team led by Daichi Hiramatsu at the Center for Astrophysics | Harvard & Smithsonian tracked SN 2023ixf from discovery through its first month. They combined brightness measurements, light-spectrum analysis, and computer simulations to reconstruct what the dying star was doing in its final year.

> **Key Insight:** SN 2023ixf shows that the massive red giant star that exploded was shedding mass at extraordinarily high rates, up to a solar mass per year, in the year before exploding. That far exceeds what standard stellar physics predicts and may point to violent eruptive events.

## How It Works

Amateur astronomer Koichi Itagaki spotted the supernova on May 19, 2023, and the team confirmed it within hours. Observations began within roughly one day of **first light**, the moment the explosion's radiation first escaped the star. That head start proved invaluable.

![Figure 1](figure:1)

The team assembled a detailed **light curve** spanning the first 30 days. The behavior was striking:

- A rapid rise to peak brightness in just ~5 days
- A luminous peak of M_V ≈ −18.2 magnitudes
- A plateau phase at M_V ≈ −17.6 extending to 30 days, declining at ~0.03 magnitudes per day
- An unusual blueward shift in ultraviolet-optical color during the rise, followed by a redward drift during the plateau

That color evolution matters. Normally, supernovae cool and redden as they expand. A blueward shift during the rise indicates the shock was *heating up* as it plowed through something dense right outside the star.

![Figure 3](figure:3)

The real tell came from **flash spectroscopy**, a technique that captures the light signatures of specific elements in the first days after an explosion. The spectra showed prominent signatures of hydrogen, helium, carbon, and nitrogen, glowing because the explosion's intense ultraviolet radiation was stripping electrons from gas the star had previously shed.

These **flash features** (light signatures from energized atoms that appear and fade within days) are only visible if you catch a supernova early enough. The team tracked them for ~5 days after first light and observed a jump to a higher-energy state in the first ~2 days, indicating temperature was *rising* rather than falling. That's what you'd expect if the shock was still traveling through dense surrounding gas rather than breaking out into empty space.

The color evolution and flash features together pointed to a **delayed shock breakout**: the explosion's shockwave punching through a shell of dense **circumstellar material (CSM)**, gas the star had cast off before dying. From the timescales involved, the team calculated how far that shell extended outward, roughly (3–7) × 10¹⁴ cm, or about 20 to 47 times the Earth-Sun distance.

![Figure 5](figure:5)

To figure out how that CSM got there, the researchers built two classes of numerical light-curve models:

1. **Continuous mass-loss scenario**: The star steadily shed material at 0.1–1.0 solar masses per year during the final 1–2 years before explosion, possibly tapering to 0.01–0.1 solar masses per year in the last few months.
2. **Eruptive mass-loss scenario**: The star underwent one or more violent eruptions roughly a year before exploding, each ejecting 0.3–1 solar mass of its outer envelope in a short burst.

Both scenarios produce similar CSM masses and extents, so the observations alone can't definitively distinguish between them. But both demand mass-loss rates *orders of magnitude* higher than standard stellar evolution theory expects.

## Why It Matters

The progenitor of SN 2023ixf was almost certainly a **red supergiant**, a bloated, cool giant with a mass between roughly 8 and 25 times the Sun's. Pre-explosion archival images from Hubble, Spitzer, and ground-based observatories had already flagged a dust-obscured candidate with a ~1000-day periodic variability, hinting that the star was pulsating dramatically in its final years.

![Figure 6](figure:6)

The extreme mass loss revealed by SN 2023ixf fits a disturbing pattern: massive stars don't quietly collapse. They convulse and heave material into space in their final moments, reshaping their immediate surroundings before the core gives way.

This has real consequences for how we model stellar evolution, supernova light curves, and the chemical enrichment of galaxies. If massive stars routinely dump solar masses of material into surrounding space in their last year, the textbook picture of slow, steady stellar winds is badly incomplete. It also means the very early hours and days of a supernova, the phase traditionally missed, are when the most revealing physics is happening. SN 2023ixf makes a strong case for rapid-response observing networks and the emerging field of **time-domain astronomy**, the science of tracking how objects in the sky change over time.

> **Bottom Line:** SN 2023ixf exposes the chaotic, poorly understood final year of a massive star's life, revealing mass-loss rates up to 100 times higher than standard theory predicts and raising new questions about what drives such extreme stellar behavior just before core collapse.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work combines rapid multiwavelength observational astronomy with numerical hydrodynamic modeling to decode the physics of stellar death, spanning computational astrophysics and fundamental stellar physics.

- **Impact on Artificial Intelligence:** Modern time-domain survey infrastructure and rapid data pipelines, increasingly powered by machine-learning alert systems, enabled near-instantaneous detection and follow-up of this rare transient event within hours of first light.

- **Impact on Fundamental Interactions:** SN 2023ixf provides the most detailed constraints yet on pre-supernova mass loss from a red supergiant, revealing mass-loss rates of 0.1–1.0 solar masses per year that challenge standard stellar evolution theory and call for new physics to explain the final year before core collapse.

- **Outlook and References:** Future multiwavelength observations, especially in X-ray and radio, will further constrain the CSM geometry and progenitor properties; the full study is available at [arXiv:2307.03165](https://arxiv.org/abs/2307.03165).
