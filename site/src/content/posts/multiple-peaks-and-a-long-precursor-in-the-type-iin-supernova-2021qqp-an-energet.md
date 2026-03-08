---
abstract: We present optical photometry and spectroscopy of the Type IIn supernova
  (SN) 2021qqp. Its unusual light curve is marked by a long precursor for $\approx300$
  days, a rapid increase in brightness for $\approx60$ days, and then a sharp increase
  of $\approx1.6$ mag in only a few days to a first peak of $M_r \approx -19.5$ mag.
  The light curve then declines rapidly until it re-brightens to a second distinct
  peak of $M_r \approx -17.3$ mag centered at $\approx335$ days after the first peak.
  The spectra are dominated by Balmer lines with a complex morphology, including a
  narrow component with a width of $\approx 1300$ km s$^{-1}$ (first peak) and $\approx
  2500$ km s$^{-1}$ (second peak) that we associate with the circumstellar medium
  (CSM) and a P Cygni component with an absorption velocity of $\approx 8500$ km s$^{-1}$
  (first peak) and $\approx 5600$ km s$^{-1}$ (second peak) that we associate with
  the SN-CSM interaction shell. Using the luminosity and velocity evolution, we construct
  a flexible analytical model, finding two significant mass-loss episodes with peak
  mass loss rates of $\approx 10$ and $\approx 5\,M_{\odot}$ yr$^{-1}$ about $0.8$
  and $2$ yr before explosion, respectively, with a total CSM mass of $\approx 2-4\,M_{\odot}$.
  We show that the most recent mass-loss episode could explain the precursor for the
  year preceding the explosion. The SN ejecta mass is constrained to be $\approx 5-30\,M_{\odot}$
  for an explosion energy of $\approx (3-10)\times10^{51}$ erg. We discuss eruptive
  massive stars (luminous blue variable, pulsational pair instability) and an extreme
  stellar merger with a compact object as possible progenitor channels.
arxivId: '2305.11168'
arxivUrl: https://arxiv.org/abs/2305.11168
authors:
- Daichi Hiramatsu
- Tatsuya Matsumoto
- Edo Berger
- Conor Ransome
- V. Ashley Villar
- Sebastian Gomez
- Yvette Cendes
- Kishalay De
- K. Azalee Bostroem
- Joseph Farah
- D. Andrew Howell
- Curtis McCully
- Megan Newsome
- Estefania Padilla Gonzalez
- Craig Pellegrino
- Akihiro Suzuki
- Giacomo Terreran
concepts:
- circumstellar interaction
- supernova classification
- mass-loss episodes
- multi-peak light curve
- stellar evolution
- inverse problems
- bayesian inference
- surrogate modeling
- regression
- anomaly detection
figures:
- /iaifi-research-blog/figures/2305_11168/figure_1.png
- /iaifi-research-blog/figures/2305_11168/figure_1.png
- /iaifi-research-blog/figures/2305_11168/figure_2.png
- /iaifi-research-blog/figures/2305_11168/figure_2.png
- /iaifi-research-blog/figures/2305_11168/figure_3.png
- /iaifi-research-blog/figures/2305_11168/figure_3.png
pdfUrl: https://arxiv.org/pdf/2305.11168v2
published: '2023-05-18T17:57:47+00:00'
theme: Astrophysics
title: 'Multiple Peaks and a Long Precursor in the Type IIn Supernova 2021qqp: An
  Energetic Explosion in a Complex Circumstellar Environment'
wordCount: 1148
---

## The Big Picture

Imagine a star so massive and so unstable that it begins tearing itself apart *before* it explodes, hurling enormous shells of gas into space for years in advance, like a condemned building shedding floors before it finally comes down. That's what astronomers caught happening with SN 2021qqp, a stellar explosion that lit up the sky in 2021 and broke almost every rule in the supernova playbook.

Supernovae (the violent deaths of massive stars) typically follow recognizable patterns: they brighten, peak, and fade. SN 2021qqp refused to cooperate. It flickered ominously for nearly a year before exploding, blazed to extraordinary brightness, dimmed rapidly, then *brightened again* over a year later to a second distinct peak. For astronomers trying to understand how the most massive stars die, this is an extraordinary gift: a star caught in the act of its own unraveling.

A team led by Daichi Hiramatsu at the Center for Astrophysics | Harvard & Smithsonian decoded SN 2021qqp by tracking how its brightness changed over time and analyzing the chemical fingerprints in its light, then building a physical model that reconstructs the full story of the star's violent final years.

> **Key Insight:** SN 2021qqp reveals that some of the most extreme stellar deaths are preceded by years of catastrophic mass ejection, and the resulting "traffic jams" of gas shells in space can produce multiple brightness peaks long after the initial explosion.

## How It Works

The Zwicky Transient Facility (ZTF) first spotted SN 2021qqp on May 23, 2021, but the real story started earlier. Archival data from Pan-STARRS showed the source brightening roughly 150 days *before* discovery, and tracing back further revealed a **precursor**: a prolonged brightening lasting about 300 days before the main explosion. Stars don't usually glow brighter years before dying. This one did.

![Figure 1](figure:1)

The light curve (a graph of how brightness changed over time) is the paper's most striking feature. After the precursor, SN 2021qqp shot up by 1.6 magnitudes in just a few days, reaching a first peak of M_r ≈ -19.5 mag. On the astronomical magnitude scale, more negative means brighter, placing this among the most luminous supernovae ever recorded.

It then faded for nearly a year before doing something almost unheard of: brightening again to a second distinct peak of M_r ≈ -17.3 mag, about 335 days after the first. Two peaks, separated by almost a year.

The spectra tell the deeper story. SN 2021qqp is classified as a **Type IIn supernova**, where the "n" stands for "narrow," referring to characteristic narrow hydrogen emission lines produced when supernova ejecta slam into surrounding gas that the star previously shed (the **circumstellar medium**, or CSM). The team measured two distinct velocity components:

- A **narrow component** at ~1300 km/s (first peak) and ~2500 km/s (second peak), tracing the CSM itself
- A **P Cygni component** at ~8500 km/s (first peak) and ~5600 km/s (second peak), tracing where ejecta crash into the CSM. P Cygni profiles are a spectral signature, named after the famous eruptive star P Cygni, that reveals fast-moving gas rushing toward the observer.

![Figure 3](figure:3)

The slowing velocities aren't random. They're a diagnostic: faster ejecta hitting denser gas slow down more. By modeling how both luminosity *and* velocity evolved together, the team reconstructed what the star was doing in its final years.

![Figure 5](figure:5)

Their model reveals **two distinct mass-loss episodes**: one about 2 years before explosion, shedding roughly 5 solar masses per year, and a more intense burst about 0.8 years before explosion reaching ~10 solar masses per year. For comparison, our Sun loses about one ten-trillionth of its mass annually through the solar wind. This star was shedding mass tens of trillions of times faster, briefly, catastrophically, and repeatedly.

The total CSM from both episodes amounts to roughly 2–4 solar masses. The explosion itself carried 5–30 solar masses of ejecta, propelled by an energy of roughly (3–10) × 10^51 ergs, placing it among the most energetic core-collapse explosions on record.

The two-peak light curve falls out naturally from this geometry. The first peak occurs when fast-moving ejecta plow into the inner, recently ejected CSM shell. After punching through, luminosity drops. Then the shock hits the older, more distant shell, producing the second peak roughly a year later, like a wave hitting a second sandbar.

## Why It Matters

Why massive stars shed so much material just before they explode remains one of the big open questions in stellar astrophysics. No pre-explosion image of SN 2021qqp's progenitor exists, but the observations narrow down the candidates. The team considers three possibilities: a **luminous blue variable** (LBV), a class of enormous, unstable stars prone to giant eruptions; a star undergoing **pulsational pair instability**, where extreme temperatures trigger runaway nuclear reactions that repeatedly shake the star before collapse; or an **extreme stellar merger** between a massive star and a compact object like a neutron star or black hole.

The extreme mass-loss rates and multi-episode structure push beyond what LBVs can produce through known mechanisms, making pulsational pair instability or a merger scenario especially interesting. The source may still be evolving, and future observations could help distinguish between these channels.

SN 2021qqp also shows that structured CSM environments produce light curves far richer than simple models predict. As survey telescopes like the Rubin Observatory's Legacy Survey of Space and Time scan the sky at higher cadence, astronomers expect to find many more objects like this, each one opening a window into the final, turbulent years of a massive star's life.

> **Bottom Line:** SN 2021qqp's double-peaked light curve and long precursor reveal a star that catastrophically shed multiple solar masses of gas in two separate eruptions before exploding. The resulting shells produced distinct luminosity peaks as the supernova shock crashed through them in sequence.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work uses flexible analytical modeling to extract physical structure from multi-wavelength time-series data, combining observational astronomy with quantitative physical inference in ways that reflect IAIFI's approach of bringing AI-informed techniques to fundamental astrophysics.

- **Impact on Artificial Intelligence:** The analytical framework simultaneously fits luminosity and velocity measurements to extract CSM density profiles and explosion parameters. This kind of data-driven physical modeling is exactly what machine learning methods are being developed to automate and scale across large transient surveys.

- **Impact on Fundamental Interactions:** SN 2021qqp offers rare direct observational evidence of extreme pre-explosion mass loss from a massive star, constraining the physics of stellar instability near the pair-instability threshold and the dynamics of shock-CSM interaction in energetic core-collapse events.

- **Outlook and References:** Next-generation surveys like Rubin/LSST are expected to discover thousands of similar multi-peaked transients, and the modeling framework from this paper will be a natural starting point for systematic characterization. The paper is available at [arXiv:2305.11168](https://arxiv.org/abs/2305.11168) and was led by Daichi Hiramatsu at the Center for Astrophysics | Harvard & Smithsonian and IAIFI.
