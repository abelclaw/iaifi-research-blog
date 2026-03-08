---
abstract: Kilonovae, the ultraviolet/optical/infrared counterparts to binary neutron
  star mergers, are an exceptionally rare class of transients. Optical follow-up campaigns
  are plagued by contaminating transients, which may mimic kilonovae, but do not receive
  sufficient observations to measure the full photometric evolution. In this work,
  we present an analysis of the multi-wavelength dataset of supernova (SN) 2025ulz,
  a proposed kilonova candidate following the low-significance detection of gravitational
  waves originating from the potential binary neutron star merger S250818k. Despite
  an early rapid decline in brightness, our multi-wavelength observations of SN 2025ulz
  reveal that it is a type IIb supernova. As part of this analysis, we demonstrate
  the capabilities of a novel quantitative scoring algorithm to determine the likelihood
  that a transient candidate is a kilonova, based primarily on its 3D location and
  light curve evolution. We also apply our scoring algorithm to other transient candidates
  in the localization volume of S250818k and find that, at all times after the discovery
  of SN 2025ulz, there are $\geq 4$ candidates with a score comparable to SN 2025ulz,
  indicating that the kilonova search may have benefited from the additional follow-up
  of other candidates. During future kilonova searches, this type of scoring algorithm
  will be useful to rule out contaminating transients in real time, optimizing the
  use of valuable telescope resources.
arxivId: '2510.17104'
arxivUrl: https://arxiv.org/abs/2510.17104
authors:
- Noah Franz
- Bhagya Subrayan
- Charles D. Kilpatrick
- Griffin Hosseinzadeh
- David J. Sand
- Kate D. Alexander
- Wen-fai Fong
- Collin T. Christy
- Jeniveve Pearson
- Tanmoy Laskar
- Brian Hsu
- Jillian Rastinejad
- Michael J. Lundquist
- Edo Berger
- K. Azalee Bostroem
- Clecio R. Bom
- Phelipe Darc
- Mark Gurwell
- Shelbi Hostler Schimpf
- Garrett K. Keating
- Phillip Noel
- Conor Ransome
- Ramprasad Rao
- Luidhy Santana-Silva
- A. Souza Santos
- Manisha Shrestha
- Ramya Anche
- Jennifer E. Andrews
- Sanchayeeta Borthakur
- Nathaniel R. Butler
- Deanne L. Coppejans
- Philip N Daly
- Kathryne J. Daniel
- Paul C. Duffell
- Tarraneh Eftekhari
- Carl E. Fields
- Alexander T. Gagliano
- Walter W. Golay
- Aldana Grichener
- Erika T. Hamden
- Daichi Hiramatsu
- Harsh Kumar
- Vikram Manikantan
- Raffaella Margutti
- Vasileios Paschalidis
- Kerry Paterson
- Daniel E. Reichart
- Mathieu Renzo
- Kali Salmas
- Genevieve Schroeder
- Nathan Smith
- Kristine Spekkens
- Jay Strader
- David E. Trilling
- Nicholas Vieira
- Benjamin Weiner
- Peter K. G. Williams
concepts:
- gravitational waves
- kilonova scoring
- supernova classification
- transient contamination
- signal detection
- classification
- multi-messenger follow-up
- anomaly detection
- experimental design
- hypothesis testing
- model validation
figures:
- /iaifi-research-blog/figures/2510_17104/figure_1.png
- /iaifi-research-blog/figures/2510_17104/figure_2.png
- /iaifi-research-blog/figures/2510_17104/figure_3.png
pdfUrl: https://arxiv.org/pdf/2510.17104v2
published: '2025-10-20T02:32:26+00:00'
theme: Astrophysics
title: 'Optimizing Kilonova Searches: A Case Study of the Type IIb SN 2025ulz in the
  Localization Volume of the Low-Significance Gravitational Wave Event S250818k'
wordCount: 1119
---

## The Big Picture

Imagine receiving a text message that might be the most important news of your lifetime, but the signal is so garbled it could be noise. That's what astronomers faced on August 18, 2025, when LIGO's gravitational wave detectors picked up a faint ripple in spacetime: S250818k, a low-significance signal possibly produced by two colliding neutron stars.

When two neutron stars merge, they trigger a cosmic fireworks show called a **kilonova**: a brief, brilliant flash of ultraviolet, optical, and infrared light powered by the radioactive decay of freshly synthesized heavy elements like gold and platinum. The 2017 detection of kilonova AT 2017gfo alongside GW170817 was a landmark. For the first time, we watched a neutron star merger with both gravitational waves and light simultaneously.

But GW170817 was a best-case scenario. Most gravitational wave alerts are fuzzier. The sky regions they point to are enormous, and finding the actual kilonova among hundreds of unrelated stellar explosions is like finding a specific firefly in a field of fireworks.

In a new paper, a team led by Noah Franz and Bhagya Subrayan at the University of Arizona details their pursuit of a kilonova following S250818k, what they found instead, and a new scoring algorithm that could change how these searches are conducted.

> The researchers caught a supernova masquerading as a kilonova, then developed a quantitative scoring tool that, applied in real time, could help astronomers stop chasing false leads and concentrate follow-up resources where they matter most.

## How It Works

The search began immediately after S250818k was flagged. The alert came with a **localization volume**, a three-dimensional region of sky consistent with the signal's source, and teams worldwide began scanning for any new optical transient that could be the kilonova.

One candidate stood out early: **SN 2025ulz**. It was bright, appeared to fade quickly, and sat within the GW localization region. Rapid fading is a kilonova hallmark. Unlike supernovae that stay bright for weeks, kilonovae typically dim within days. SN 2025ulz ticked that box.

![Figure 1](figure:1)

The team didn't stop at first impressions. They mobilized telescopes across ultraviolet, optical, infrared, and radio bands to build a **multi-wavelength dataset** over multiple epochs. That kind of coverage is what separates a confident identification from a lucky guess.

The data told a different story. SN 2025ulz's spectrum showed classic signatures of a **Type IIb supernova**, a core-collapse explosion from a massive star that had shed most of its hydrogen envelope. These events can briefly display an early, rapidly fading **shock cooling emission** phase when the blast wave breaks through the thin outer envelope, before settling into a slower decline. That early drop can look deceptively like a kilonova. Hydrogen and helium absorption lines, combined with a brightness curve that didn't match kilonova models, let the team conclusively rule out the kilonova interpretation.

**The Scoring Algorithm**

Rather than just reporting that SN 2025ulz fooled them, the team built a quantitative scoring algorithm to evaluate every transient candidate in a GW localization volume. It combines four factors into a single score:

- **3D spatial probability:** How well does the candidate's position align with the gravitational wave localization volume, including the distance estimate?
- **Light curve evolution:** Does brightness evolve on kilonova timescales (fast and fading) or slower, like a supernova?
- **Host galaxy properties:** Is the candidate near a galaxy of the right type and at the right redshift?
- **Multi-wavelength behavior:** Does color evolution match what we'd expect from a kilonova's neutron-rich ejecta?

Applied retroactively to all candidates from the S250818k campaign, the result was striking: at every moment after SN 2025ulz was discovered, at least four other candidates had comparable or higher scores. SN 2025ulz had been heavily prioritized by the observing community, but it never clearly dominated the field. Resources spent characterizing it might have been better distributed.

![Figure 2](figure:2)

Telescope time during GW follow-up campaigns is genuinely precious. Observers race against the clock, juggling instruments across hemispheres, making judgment calls under pressure. A tool that turns expert intuition into a reproducible number can make those calls faster and fairer.

![Figure 3](figure:3)

## Why It Matters

The LIGO-Virgo-KAGRA network has been running its fourth observing run, generating gravitational wave alerts at an unprecedented rate. Each alert potentially represents a neutron star merger, which is simultaneously a natural laboratory for nuclear physics, a factory for heavy elements, and a test of general relativity. With dozens of candidates per year, the community cannot afford to send its most powerful telescopes chasing every lead.

The scoring algorithm points toward a future where machine learning could automate real-time triage. The current system uses well-understood physical priors, but neural networks trained on archival multi-wavelength data could eventually distinguish early supernovae from true kilonovae with greater speed and confidence. IAIFI researchers Alexander Gagliano and Harsh Kumar, both co-authors on this work, are working on exactly those extensions.

A deeper open question remains: how common are genuine kilonovae relative to the supernovae, active galactic nuclei, and other transients that contaminate the search? Each follow-up campaign, whether it ends in a positive identification or not, builds a richer empirical picture. Tools like this scoring algorithm get better calibrated with use.

> SN 2025ulz was a cosmic impersonator, a supernova that briefly mimicked the rarest of events. But the real discovery is a smarter way to search: a scoring algorithm that could prevent future teams from investing all their telescope hours in a single red herring.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work combines gravitational wave astronomy, multi-wavelength transient astrophysics, and algorithmic data analysis to address one of multi-messenger astronomy's core practical challenges: distinguishing real kilonova signals from an overwhelming background of impostor transients.

- **Impact on Artificial Intelligence:** The quantitative scoring algorithm introduced here is a direct precursor to automated machine-learning classifiers that could triage gravitational wave follow-up candidates in real time, cutting the delay between alert and informed decision.

- **Impact on Fundamental Interactions:** By systematically characterizing what a kilonova is *not*, this study sharpens the community's ability to identify genuine neutron star merger counterparts. These events encode information about r-process nucleosynthesis (the process that forges heavy elements like gold in neutron star mergers), the nuclear equation of state, and the engines of short gamma-ray bursts.

- **Outlook and References:** Future GW observing runs will generate more alerts than ever, making real-time candidate scoring essential. This work, available at [arXiv:2510.17104](https://arxiv.org/abs/2510.17104), lays the groundwork for fully automated kilonova identification pipelines.
