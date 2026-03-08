---
abstract: Enhanced emission in the months to years preceding explosion has been detected
  for several core-collapse supernovae (SNe). Though the physical mechanisms driving
  the emission remain hotly debated, the light curves of detected events show long-lived
  ($\geq$50 days), plateau-like behavior, suggesting hydrogen recombination may significantly
  contribute to the total energy budget. The Vera C. Rubin Observatory's Legacy Survey
  of Space and Time (LSST) will provide a decade-long photometric baseline to search
  for this emission, both in binned pre-explosion observations after an SN is detected
  and in single-visit observations prior to the SN explosion. In anticipation of these
  searches, we simulate a range of eruptive precursor models to core-collapse SNe
  and forecast the discovery rates of these phenomena in LSST data. We find a detection
  rate of ~40-130 yr$^{-1}$ for SN IIP/IIL precursors and ~110 yr$^{-1}$ for SN IIn
  precursors in single-epoch photometry. Considering the first three years of observations
  with the effects of rolling and observing triplets included, this number grows to
  a total of 150-400 in binned photometry, with the highest number recovered when
  binning in 100-day bins for 2020tlf-like precursors and in 20-day bins for other
  recombination-driven models from the literature. We quantify the impact of using
  templates contaminated by residual light (from either long-lived or separate precursor
  emission) on these detection rates, and explore strategies for estimating baseline
  flux to mitigate these issues. Spectroscopic follow-up of the eruptions preceding
  core-collapse SNe and detected with LSST will offer important clues to the underlying
  drivers of terminal-stage mass loss in massive stars.
arxivId: '2408.13314'
arxivUrl: https://arxiv.org/abs/2408.13314
authors:
- A. Gagliano
- E. Berger
- V. A. Villar
- D. Hiramatsu
- R. Kessler
- T. Matsumoto
- A. Gilkis
- E. Laplace
concepts:
- precursor emission
- circumstellar material
- signal detection
- stellar evolution
- monte carlo methods
- photometric binning strategy
- supernova classification
- experimental design
- surrogate modeling
- anomaly detection
- simulation-based inference
figures:
- /iaifi-research-blog/figures/2408_13314/figure_1.png
- /iaifi-research-blog/figures/2408_13314/figure_1.png
- /iaifi-research-blog/figures/2408_13314/figure_2.png
pdfUrl: https://arxiv.org/pdf/2408.13314v2
published: '2024-08-23T18:00:11+00:00'
theme: Experimental Physics
title: 'Finding the Fuse: Prospects for the Detection and Characterization of Hydrogen-Rich
  Core-Collapse Supernova Precursor Emission with the LSST'
wordCount: 1095
---

## The Big Picture

Imagine you could see the fuse burning before a bomb goes off. For decades, astronomers watched stars explode and wondered: were there warning signs we simply missed? Now, with a new sky survey on the horizon, we're about to find out at industrial scale.

Massive stars, those at least eight times heavier than our Sun, end their lives in spectacular explosions called supernovae. But for a growing number of these stellar deaths, the explosion doesn't come without warning. Several supernovae have been caught brightening before their final blast, releasing bursts of energy that hint at violent instabilities in a star's final chapter. These **precursor eruptions**, flares of light that precede the main explosion by days to years, give us a direct look at the turbulent physics of a star tearing itself apart before it dies.

The problem is we've only caught a handful. A new paper from IAIFI researchers at Harvard, MIT, and collaborators worldwide changes that, using detailed simulations to forecast how many precursors the upcoming Vera C. Rubin Observatory will detect and what it will take to find them.

> **Key Insight:** The Rubin Observatory's LSST survey could detect between 150 and 400 supernova precursor events in just its first three years, turning what is currently a rare curiosity into a statistical sample large enough to test theories of stellar death.

## How It Works

The **Legacy Survey of Space and Time (LSST)** will photograph the entire southern sky every few nights for a decade, building an enormous archive of how objects change over time. That temporal baseline is exactly what's needed to hunt for supernova precursors, events that can flicker weeks or months before the main explosion.

The researchers built their forecasts by simulating realistic precursor **light curves** (records of how a star's brightness changes over time) drawn from observed events and theoretical models. They anchored their work on real detected precursors, including:

- SN 2020tlf, a hydrogen-rich supernova whose dying star showed 130 days of plateau-like brightening before exploding
- SN 2010mc, a Type IIn supernova with a dramatic eruption roughly 40 days before the main event
- SN 2015bh, which showed multi-year variability before its terminal explosion
- Several theoretical models for hydrogen recombination-driven outbursts

![Figure 1](/iaifi-research-blog/figures/2408_13314/figure_1.png)

What drives the analysis is a physical pattern: many detected precursors show long-lived, plateau-like light curves rather than sharp spikes. This behavior is a signature of **hydrogen recombination**, where superheated hydrogen gas gradually cools and releases energy steadily over weeks. Think of a lava flow glowing for days after a volcanic eruption, rather than just at the moment of the blast.

The team tested two complementary detection strategies. The first searched **single-epoch observations**, individual nightly images where a bright enough precursor triggers an alert. The second used **binned photometry**, stacking many faint measurements over 20- to 100-day windows to reveal light too dim for any single night's image.

![Figure 2](/iaifi-research-blog/figures/2408_13314/figure_1.png)

For single-epoch searches, detection rates run roughly 40 to 130 precursors per year for Type IIP/IIL supernovae (the most common hydrogen-rich variety, named for the characteristic shapes of their brightness curves) and around 110 per year for the more extreme **Type IIn** class, named for the narrow spectral fingerprints of slow-moving gas surrounding the star before explosion. These numbers already dwarf the handful of precursors known today.

![Figure 3](/iaifi-research-blog/figures/2408_13314/figure_2.png)

The binning strategy is where things get interesting. Over LSST's first three years, stacking images in optimally sized bins yields between 150 and 400 total detections. The right bin size tracks the underlying physics: 100-day bins work best for long-lived plateau-like precursors similar to SN 2020tlf, while 20-day bins are better tuned to shorter, sharper eruptions. It's like choosing the right shutter speed for a photograph.


The paper also tackles **template contamination**. To detect a precursor, astronomers subtract a reference image of the host galaxy from new observations. But if a precursor began months before the reference was taken, its light is already baked into the baseline, hiding subsequent brightening. The team quantifies how much this degrades detection rates and proposes strategies to estimate and subtract the residual flux, a step that will matter a great deal for making LSST searches work in practice.


## Why It Matters

Supernova precursors aren't just astronomical curiosities. They're a direct probe of stellar physics we don't yet understand. Why do some massive stars erupt so violently in their final years? Leading candidates include **convective wave damping** (energy from deep nuclear burning propagates outward and shakes the star's outer layers), **pulsation-driven superwinds** (rhythmic pulsations that fling material from the star's surface into space), and **binary star interaction**, where a companion's gravity triggers instability. Each mechanism leaves different imprints on a precursor's duration, brightness, and color.

With hundreds of detections rather than a handful, LSST will give researchers enough events to test these predictions against real data. Combined with **spectroscopic follow-up**, where a precursor's light is split through a prism-like instrument to identify its chemical fingerprint and speed, astronomers will measure the velocity and composition of ejected material and pin down mass-loss rates and the physics behind them.


The timing matters. Rubin Observatory's survey is set to begin operations imminently. This study is a preparation paper, a roadmap for designing searches, setting detection thresholds, and handling data challenges before the flood of data arrives. Getting the strategy right now means not missing hundreds of cosmic death-rattles when LSST begins.

> **Bottom Line:** By simulating the full range of known precursor models against realistic LSST observing conditions, this study shows the coming survey will transform our ability to catch stars in the act of dying, potentially detecting hundreds of pre-explosion flares and exposing the physics of terminal stellar mass loss.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges astrophysical theory, observational modeling, and survey simulation to forecast discovery rates for a new class of transient phenomena, connecting stellar physics, survey strategy, and data science.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The detection pipeline's optimal data-stacking and template-subtraction strategies will directly inform the automated alert systems and machine learning classifiers needed to identify precursor events in real time from LSST's nightly data stream.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Supernova precursor emission probes the final stages of nuclear burning and mass loss in massive stars, linking the physics of stellar interiors to observable signatures in the surrounding circumstellar environment.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">With LSST operations beginning, these forecasts will guide observing strategies and follow-up campaigns; the work is available at [arXiv:2408.13314](https://arxiv.org/abs/2408.13314) and has been submitted to *The Astrophysical Journal*.</span></div></div>
</div>
