---
abstract: The Vera C. Rubin Observatory has now seen first light, and over a 10 year
  duration, LSST is projected to catalogue tens of millions of quasars, many of which
  are expected to be associated with sub-parsec supermassive black hole binaries (SMBHBs).
  Out of these SMBHBs, up to thousands of relatively massive binary-quasars are expected
  to exhibit gravitational self-lensing flares (SLFs) that last for at least 20-30
  days. We assess the effectiveness of the Lomb-Scargle (LS) periodogram and matched
  filters (MFs) as methods for systematic searches for these binaries, using toy-models
  of hydrodynamical, Doppler, and self-lensing variability from equal-mass, eccentric
  SMBHBs. We inject SLFs into random realizations of damped random walk (DRW) lightcurves,
  representing stochastic quasar variability, and compute the LS periodogram with
  and without the SLF. We find that periodograms of SLF+DRW light-curves do not have
  maximum peak heights that could not arise from DRW-only periodograms. On the other
  hand, the matched filter signal-to-noise ratio (SNR) can distinguish SLFs from noise
  even with LSST-like cadences and DRW noise. Furthermore, we develop a three-step
  procedure with matched filters, which can also recover injected binary parameters
  from these light-curves. We expect this method to be computationally efficient enough
  to be applicable to millions of quasar light-curves in LSST.
arxivId: '2512.08427'
arxivUrl: https://arxiv.org/abs/2512.08427
authors:
- Kevin Park
- Zoltan Haiman
- Chengcheng Xin
- Tzuken Shen
- Ashley Villar
- Jordy Davelaar
concepts:
- self-lensing flares
- supermassive black hole binaries
- signal detection
- matched filter
- stochastic processes
- spectral methods
- hypothesis testing
- gravitational waves
- bayesian inference
- cosmological simulation
figures:
- /iaifi-research-blog/figures/2512_08427/figure_1.png
- /iaifi-research-blog/figures/2512_08427/figure_2.png
- /iaifi-research-blog/figures/2512_08427/figure_3.png
pdfUrl: https://arxiv.org/pdf/2512.08427v1
published: '2025-12-09T09:55:42+00:00'
theme: Astrophysics
title: 'Self-lensing flares from black hole binaries V: systematic searches in LSST'
wordCount: 1112
---

## The Big Picture

Imagine two supermassive black holes locked in an orbital dance, each billions of times the mass of our Sun, spiraling closer together over millions of years. Twice per orbit, one passes directly behind the other, and for a brief window, gravity acts like a lens, bending and magnifying the background black hole's light into a brilliant flare. These **gravitational self-lensing flares** are among the most distinctive signatures in astrophysics. The problem? Finding them in the cosmic haystack.

The Vera C. Rubin Observatory in Chile saw first light in 2025, kicking off its decade-long Legacy Survey of Space and Time (LSST). Over ten years, LSST will photograph the southern sky every few nights, building brightness records (called **light-curves**) for tens of millions of quasars: the luminous cores of distant galaxies powered by actively feeding black holes.

Hidden among those millions of quasars, models predict, could be thousands of supermassive black hole binary systems close enough to produce detectable self-lensing flares. The question isn't whether those flares are out there. It's whether we can find them.

This paper gives a clear answer: the standard search method fails, but a smarter alternative works, and it scales to millions of sources.

> **Key Insight:** The Lomb-Scargle periodogram, astronomy's go-to tool for finding periodicity, cannot reliably detect self-lensing flares above quasar background noise. Matched filters can, and they can even recover the binary's orbital parameters.

## How It Works

The team built a realistic simulation pipeline to test two competing detection strategies. Using `binlite`, a Python package for generating synthetic light-curves of eccentric supermassive black hole binaries, they produced toy-model signals capturing three physical effects:

- **Hydrodynamical variability** — periodic brightness changes driven by gas swirling in the shared disk between the two black holes
- **Relativistic Doppler boosting** — a brightness shift from the black holes' high orbital speeds: as one moves toward us, its light brightens; as it recedes, it dims
- **Self-lensing flares** — the gravitational magnification events themselves

On top of the binary signal, they layered realistic quasar "noise" using the **damped random walk (DRW)** model, a standard description of how quasar brightness drifts irregularly over time. They then downsampled the light-curves to mimic LSST's actual observing cadence, including gaps and sporadic visits, with realistic measurement uncertainties added in. The result: simulated light-curves that look like what LSST will actually deliver.

![Figure 1](figure:1)

With those synthetic light-curves in hand, they applied two detection methods:

1. **Lomb-Scargle (LS) periodogram** — astronomy's standard workhorse for periodicity. It fits sinusoids at many trial frequencies and returns a power spectrum showing which rhythms appear strongest in the data. The trouble is that quasars naturally produce tall, narrow peaks in their power spectra even without true periodicity; their slow, random brightness wandering mimics a periodic signal at the very frequencies the algorithm tests.

 When the team injected self-lensing flares into simulated DRW light-curves and computed the LS periodogram, the resulting peak heights were statistically indistinguishable from DRW noise alone. Flares are simply too brief per orbit (a sharp spike rather than a sustained sinusoid) for the periodogram to latch onto.

2. **Matched filters (MFs)** — a signal processing technique borrowed from radar and gravitational wave detection. Instead of searching for generic periodicity, a matched filter cross-correlates a known signal template against the data, returning a signal-to-noise ratio (SNR) at each trial position. The approach is specifically tuned to the distinctive shape of a self-lensing flare: a symmetric, roughly Gaussian brightening lasting 20–30 days.

Matched filters blew the periodogram out of the water. Even with LSST-like sparse cadences and realistic DRW noise, matched filter SNR reliably distinguished injected flares from noise.

![Figure 2](figure:2)

Beyond simple detection, the team developed a **three-step matched filter procedure** for parameter recovery:

- **Step 1:** Scan the full light-curve with a broad library of flare templates to identify candidate flare times and estimate flare duration.
- **Step 2:** Use candidate flare detections to constrain the orbital period. Since flares occur twice per orbit, pairs separated by half a period give a direct period estimate.
- **Step 3:** Refine binary parameters (mass ratio, eccentricity, inclination) by fitting the full multi-component light-curve model to the data.

![Figure 3](figure:3)

The whole pipeline is computationally cheap enough to run on millions of quasar light-curves, a hard requirement for any method aimed at LSST's enormous catalog.

## Why It Matters

The payoff goes well beyond cataloging exotic objects. Supermassive black hole binaries are the loudest sources of gravitational waves in the universe at nanohertz frequencies, exactly the band that pulsar timing arrays (PTAs) are now detecting as a faint, pervasive background hum. In 2023, PTAs announced compelling evidence for this gravitational wave background, consistent with a cosmological population of coalescing black hole pairs.

An electromagnetic catalog of supermassive black hole binary (SMBHB) candidates from LSST could let astronomers cross-match optical and gravitational wave observations from the same systems. That would enable new tests of general relativity that neither probe can achieve alone.

The matched filter method also connects naturally to how LIGO and the future space-based detector LISA search for gravitational wave signals. Porting that logic to optical time-domain astronomy is a conceptual bridge worth building. **Multi-messenger astrophysics**, the practice of combining light-based and gravitational wave observations of the same events, is still young, and tools like this help it grow.

Open questions remain. How well does the three-step procedure handle realistic diversity in binary mass ratios, eccentricities, and inclinations? The paper doesn't fully answer that yet, but the foundation is there.

> **Bottom Line:** Standard periodogram searches are blind to self-lensing flares hidden in quasar noise, but matched filters can detect and characterize them at LSST scale, opening a path to discovering thousands of supermassive black hole binary systems in the next decade.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects gravitational astrophysics and signal processing, bringing matched filter techniques from gravitational wave detection to the problem of finding rare astrophysical transients in large optical surveys.

- **Impact on Artificial Intelligence:** The matched filter pipeline provides a computationally efficient, template-based approach to anomaly detection in time-series data, and could serve as a useful baseline when benchmarking ML methods against classical signal processing for astronomical transient searches.

- **Impact on Fundamental Interactions:** Identifying self-lensing flares in LSST would provide direct electromagnetic evidence for sub-parsec supermassive black hole binaries, the dominant sources of the nanohertz gravitational wave background and key targets for future LISA observations.

- **Outlook and References:** The method will be stress-tested against full LSST simulation outputs and realistic binary population models; the paper is available at [arXiv:2512.08427](https://arxiv.org/abs/2512.08427).

## Original Paper Details
- **Title:** Self-lensing flares from black hole binaries V: systematic searches in LSST
- **arXiv ID:** 2512.08427
- **Authors:** ["Kevin Park", "Zoltan Haiman", "Chengcheng Xin", "Tzuken Shen", "Ashley Villar", "Jordy Davelaar"]
- **Abstract:** The Vera C. Rubin Observatory has now seen first light, and over a 10 year duration, LSST is projected to catalogue tens of millions of quasars, many of which are expected to be associated with sub-parsec supermassive black hole binaries (SMBHBs). Out of these SMBHBs, up to thousands of relatively massive binary-quasars are expected to exhibit gravitational self-lensing flares (SLFs) that last for at least 20-30 days. We assess the effectiveness of the Lomb-Scargle (LS) periodogram and matched filters (MFs) as methods for systematic searches for these binaries, using toy-models of hydrodynamical, Doppler, and self-lensing variability from equal-mass, eccentric SMBHBs. We inject SLFs into random realizations of damped random walk (DRW) lightcurves, representing stochastic quasar variability, and compute the LS periodogram with and without the SLF. We find that periodograms of SLF+DRW light-curves do not have maximum peak heights that could not arise from DRW-only periodograms. On the other hand, the matched filter signal-to-noise ratio (SNR) can distinguish SLFs from noise even with LSST-like cadences and DRW noise. Furthermore, we develop a three-step procedure with matched filters, which can also recover injected binary parameters from these light-curves. We expect this method to be computationally efficient enough to be applicable to millions of quasar light-curves in LSST.
