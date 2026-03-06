---
abstract: 'The advent of sensitive gravitational wave (GW) detectors, coupled with
  wide-field, high cadence optical time-domain surveys, raises the possibility of
  the first joint GW-electromagnetic (EM) detections of core-collapse supernovae (CCSNe).
  For targeted searches of GWs from CCSNe optical observations can be used to increase
  the sensitivity of the search by restricting the relevant time interval, defined
  here as the GW search window (GSW). The extent of the GSW is a critical factor in
  determining the achievable false alarm probability (FAP) for a triggered CCSN search.
  The ability to constrain the GSW from optical observations depends on how early
  a CCSN is detected, as well as the ability to model the early optical emission.
  Here we present several approaches to constrain the GSW, ranging in complexity from
  model-independent analytical fits of the early light curve, model-dependent fits
  of the rising or entire light curve, and a new data-driven approach using existing
  well-sampled CCSN light curves from {\it Kepler} and the Transiting Exoplanet Survey
  Satellite (TESS). We use these approaches to determine the time of core-collapse
  and its associated uncertainty (i.e., the GSW). We apply our methods to two Type
  II SNe that occurred during LIGO/Virgo Observing Run 3: SN\,2019fcn and SN\,2019ejj
  (both in the same galaxy at $d=15.7$ Mpc). Our approach shortens the duration of
  the GSW and improves the robustness of the GSW compared to techniques used in past
  GW CCSN searches.'
arxivId: '2201.03609'
arxivUrl: https://arxiv.org/abs/2201.03609
authors:
- Kiranjyot Gill
- Griffin Hosseinzadeh
- Edo Berger
- Michele Zanolin
- Marek Szczepanczyk
concepts:
- gravitational waves
- light curve fitting
- shock breakout timing
- uncertainty quantification
- supernova classification
- signal detection
- bayesian inference
- regression
- surrogate modeling
- simulation-based inference
- stellar evolution
- neutrino detection
figures:
- /iaifi-research-blog/figures/2201_03609/figure_1.png
- /iaifi-research-blog/figures/2201_03609/figure_2.png
- /iaifi-research-blog/figures/2201_03609/figure_3.png
pdfUrl: https://arxiv.org/pdf/2201.03609v1
published: '2022-01-10T19:22:59+00:00'
theme: Astrophysics
title: Constraining the Time of Gravitational Wave Emission from Core-Collapse Supernovae
wordCount: 1138
---

## The Big Picture

Imagine searching for a needle in a haystack without knowing when it was dropped in. Now imagine you could narrow your search to just the handful of seconds when someone walked past. Finding that needle goes from nearly impossible to achievable. That's precisely the challenge facing gravitational wave hunters when a massive star dies.

When a star more than eight times the mass of our Sun reaches the end of its life, its core collapses catastrophically in a fraction of a second. The result is a supernova — one of the most energetic explosions in the universe. That implosion should also send ripples through spacetime itself: **gravitational waves (GWs)**, distortions in space and time that travel outward at the speed of light. But unlike the gravitational wave signals from merging black holes that LIGO — the Laser Interferometer Gravitational-Wave Observatory — famously detected in 2015, supernova gravitational waves are messy, faint, and don't follow a clean, predictable pattern that detectors can easily recognize.

Detecting them means sifting through noise across a time window, and the wider that window, the harder it becomes to distinguish a real signal from a random blip.

A team led by Kiranjyot Gill at the Center for Astrophysics at Harvard & Smithsonian has developed a suite of methods to solve this problem — using the supernova's own light to pin down precisely when its core collapsed.

> **Key Insight:** By carefully modeling the earliest optical light from a supernova, researchers can shrink the gravitational wave search window from weeks down to hours, dramatically boosting the chances of a confirmed detection.

## How It Works

The central insight is elegant: while we can't directly observe the core collapse, we *can* watch for the first flash of light that escapes the dying star. This first light, called **shock breakout (SBO)**, occurs when the shockwave from the collapsing core plows through the star's outer layers and erupts from the surface. The delay between core collapse and shock breakout is calculable from physics simulations — typically a few hours — so pinning down when shock breakout happened lets you trace back to when gravitational waves were emitted.

The team presents four methods for constraining the **gravitational wave search window (GSW)** — the time interval during which detectors must hunt for a signal, where a narrower window means fewer false alarms:

1. **Power-law fits** — A model-independent approach (no assumptions about the star's internal structure) that fits the early rising **light curve** (brightness over time) to a simple mathematical function.
2. **Shock cooling emission model** — A physics-based fit modeling how expanding, cooling shocked gas produces light. More assumptions, but potentially tighter constraints.
3. **Full light curve modeling** — Fitting the entire observed light curve to detailed explosion models, squeezing out every bit of timing information.
4. **Template matching with Kepler/TESS data** — A data-driven approach using ultra-high-cadence observations from space telescopes that have caught supernovae in the act, serving as timing templates for the critical early hours.

![Figure 1](/iaifi-research-blog/figures/2201_03609/figure_1.png)

That fourth method is particularly clever. The *Kepler* space telescope and the Transiting Exoplanet Survey Satellite (TESS) were designed to stare at the same patches of sky for months, hunting for tiny dips in starlight caused by orbiting planets. As a side effect, they've caught several supernovae in unprecedented detail — including the very first moments of shock breakout. The team repurposes these observations as a library of supernova timing templates, anchoring new detections to well-characterized examples.

The researchers tested all four approaches on two real supernovae: **SN 2019fcn** and **SN 2019ejj**, a pair of Type II supernovae (produced when massive stars with hydrogen-rich outer layers explode) that went off within days of each other in the same galaxy, ESO 430-G 020, roughly 51 million light-years away. Both occurred during LIGO/Virgo Observing Run 3 — a coordinated detection campaign run jointly by the LIGO detectors in the United States and the Virgo detector in Italy — making them genuine candidates for a joint gravitational wave and optical search. SN 2019fcn was caught just 21.7 hours after explosion by the Las Cumbres Observatory's global telescope network, serendipitously, because it exploded in a galaxy astronomers were already watching.

![Figure 2](/iaifi-research-blog/figures/2201_03609/figure_2.png)

## Why It Matters

The **false alarm probability (FAP)** — the chance that a random noise fluctuation mimics a real signal — scales directly with how long you have to look. A search spanning two weeks might produce hundreds of noise fluctuations that resemble a signal; a search spanning 12 hours might produce just one. The methods developed here can compress the search window by a factor of ten or more compared to older techniques — a game-changing improvement in statistical confidence.

There's a deeper physics payoff too. Gravitational waves from a collapsing stellar core encode information that no light-based telescope can access: the degree of asymmetry in the explosion, how much angular momentum the core carries, whether turbulent convective flows or oscillations in the shock front shaped the collapse. These are the fundamental questions about how massive stars die.

The optical and gravitational wave signals are complementary, each revealing a different face of the same catastrophe. But you can only read those complementary stories together if you know when to listen.

![Figure 3](/iaifi-research-blog/figures/2201_03609/figure_3.png)

With next-generation detectors like Einstein Telescope and Cosmic Explorer on the horizon, and wide-field surveys like the Vera Rubin Observatory's LSST set to catch supernovae within minutes of explosion, the methods developed here will become increasingly powerful. The pipeline from optical detection to gravitational wave search window is being built now, in anticipation of a universe that's about to become much louder.

> **Bottom Line:** By using a supernova's own light as a clock, researchers have shown they can shrink the gravitational wave search window from weeks to hours — directly improving the odds that LIGO and Virgo will one day catch the dying scream of a collapsing stellar core.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges gravitational wave physics and optical astronomy by developing a systematic framework that converts photometric observations into precise timing constraints for GW searches, uniting two entirely different observational windows on the same explosive event.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The data-driven template-matching approach draws on machine-learning-adjacent methodology, using a library of well-characterized Kepler and TESS light curves to classify and time-align new supernovae without relying on physical models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Constraining the gravitational wave search window directly improves the achievable false alarm probability for core-collapse supernova searches, bringing the first joint GW-optical detection of a stellar death within reach of current detectors for nearby events.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future applications to Rubin Observatory detections and next-generation GW detectors could extend this method to supernovae caught within minutes of explosion, enabling robust multi-messenger astronomy of stellar core collapse; see arXiv:2112.00846.</span></div></div>
</div>
