---
abstract: 'The Laser Interferometer Gravitational-Wave Observatory (LIGO) and Virgo
  Interferometer Collaborations have now detected all three classes of compact binary
  mergers: binary black hole (BBH), binary neutron star (BNS), and neutron star-black
  hole (NSBH). For coalescences involving neutron stars, the simultaneous observation
  of gravitational and electromagnetic radiation produced by an event, has broader
  potential to enhance our understanding of these events, and also to probe the equation
  of state (EOS) of dense matter. However, electromagnetic follow-up to gravitational
  wave (GW) events requires rapid real-time detection and classification of GW signals,
  and conventional detection approaches are computationally prohibitive for the anticipated
  rate of detection of next-generation GW detectors. In this work, we present the
  first deep learning based results of classification of GW signals from NSBH mergers
  in \textit{real} LIGO data. We show for the first time that a deep neural network
  can successfully distinguish all three classes of compact binary mergers and separate
  them from detector noise. Specifically, we train a convolutional neural network
  (CNN) on $\sim 500,000$ data samples of real LIGO noise with injected BBH, BNS,
  and NSBH GW signals, and we show that our network has high sensitivity and accuracy.
  Most importantly, we successfully recover the two confirmed NSBH events to-date
  (GW200105 and GW200115) and the two confirmed BNS mergers to-date (GW170817 and
  GW190425), together with $\approx 90\%$ of all BBH candidate events from the third
  Gravitational Wave Transient Catalog, GWTC-3. These results are an important step
  towards low-latency real-time GW detection, enabling multi-messenger astronomy.'
arxivId: '2210.15888'
arxivUrl: https://arxiv.org/abs/2210.15888
authors:
- Richard Qiu
- Plamen Krastev
- Kiranjyot Gill
- Edo Berger
concepts:
- gravitational waves
- convolutional networks
- classification
- signal detection
- compact binary coalescence
- multi-messenger astronomy
- scalability
- data augmentation
- feature extraction
- anomaly detection
- transfer learning
figures:
- /iaifi-research-blog/figures/2210_15888/figure_1.png
- /iaifi-research-blog/figures/2210_15888/figure_2.png
- /iaifi-research-blog/figures/2210_15888/figure_3.png
pdfUrl: https://arxiv.org/pdf/2210.15888v2
published: '2022-10-28T04:34:48+00:00'
theme: Astrophysics
title: Deep Learning Detection and Classification of Gravitational Waves from Neutron
  Star-Black Hole Mergers
wordCount: 1024
---

## The Big Picture

Imagine trying to hear a whisper in a thunderstorm. One that lasts a fraction of a second, arrives from a billion light-years away, and carries the sound of two dead stars colliding. That's what gravitational wave astronomers do every time LIGO detects a cosmic event. A team at Harvard's Center for Astrophysics has now trained a neural network to handle the full classification problem at once, across every known category of cosmic collision.

Gravitational waves come in flavors. Two black holes spiraling together produce one kind of signal. Two neutron stars produce another. The rarest pairing, a neutron star swallowed by a black hole, produces a third, subtly different chirp that encodes information about the densest matter in the universe.

Until recently, no deep learning system had sorted all three classes from real detector noise. The standard approach, **matched filtering**, compares incoming data against millions of pre-calculated waveform templates to check whether the detector recorded anything matching a known pattern of cosmic collision. It works brilliantly today, but it's headed toward a computational wall. The Einstein Telescope and Cosmic Explorer, planned for the next decade, are expected to detect millions of events per year. Matched filtering can't scale to that.

Researchers Richard Qiu, Plamen Krastev, Kiranjyot Gill, and Edo Berger set out to show that a convolutional neural network could handle all three merger classes at once, and they tested it on real LIGO data rather than synthetic noise.

> **Key Insight:** For the first time, a deep neural network has successfully distinguished all three classes of compact binary mergers (binary black holes, binary neutron stars, and neutron star–black hole systems) from each other and from detector noise, recovering confirmed real events from LIGO's third observing run.

## How It Works

The team made a fundamental choice early on: train on reality, not idealization. Instead of generating clean Gaussian noise, they pulled actual data from the LIGO Livingston detector during the O2 and O3b observing runs, specifically segments containing no known gravitational wave events. Real detector noise is non-stationary and non-Gaussian. It glitches, drifts, and misbehaves in ways that Gaussian approximations miss entirely.

Into this real noise, they injected simulated signals across all three merger classes:

- **BBH (binary black hole):** component masses 2–95 solar masses, mass ratio ≤ 10, using the `SEOBNRv4` waveform approximant
- **BNS (binary neutron star):** component masses 1–2 solar masses, using `TaylorF2`
- **NSBH (neutron star–black hole):** neutron star mass 1–2 solar masses, black hole mass 2–15 solar masses, using `SEOBNRv4_ROM_NRTidalv2_NSBH`

Roughly 500,000 labeled training samples went into a **convolutional neural network (CNN)**, the same class of architecture that powers image recognition. The "image" here is a **Q-transform spectrogram**: a visual map of how signal energy distributes across frequencies over time. The characteristic upward-sweeping chirp of a merger shows up as a recognizable shape, and the CNN learns to tell the subtle differences apart. A neutron star inspiral is slower and longer. A black hole inspiral is faster and more massive.

![Figure 1](/iaifi-research-blog/figures/2210_15888/figure_1.png)

The network outputs a four-class probability: BBH, BNS, NSBH, or noise. Training pushed the model toward high sensitivity across all four categories, preventing it from collapsing into simply labeling everything as the most common class.

![Figure 2](/iaifi-research-blog/figures/2210_15888/figure_2.png)

The real test came when the team turned the trained network loose on confirmed detections from GWTC-3, LIGO's third gravitational wave transient catalog. The CNN recovered both confirmed NSBH events, GW200105 and GW200115, along with both confirmed BNS mergers: GW170817 (the historic 2017 neutron star collision that produced a gamma-ray burst and kilonova) and GW190425. It also recovered roughly 90% of all BBH candidates in the catalog.

These aren't injections. These are real signals buried in real noise, and the network found them.

![Figure 3](/iaifi-research-blog/figures/2210_15888/figure_3.png)

## Why It Matters

The stakes go well beyond speed. When neutron stars merge, the collision doesn't just produce gravitational waves. It erupts in electromagnetic radiation. **Kilonovae**, the glowing debris clouds forged in these collisions, synthesize heavy elements like gold and platinum, and they're visible across the electromagnetic spectrum.

That light fades fast. The window for follow-up observations can be as short as hours. Right now, the delay between a gravitational wave trigger and confident classification can mean the difference between catching the kilonova at peak brightness and missing it entirely. A deep learning pipeline that classifies events in near-real-time, without waiting for matched-filter template banks to finish, could transform how astronomers respond to every detection.

There's a fundamental physics angle too. Neutron stars are nature's densest laboratories, and the **equation of state (EOS)** of their interiors, describing how pressure relates to density in ultra-dense nuclear matter, remains one of the great open questions. Multi-messenger observations of BNS and NSBH mergers can constrain the EOS in ways no terrestrial experiment can match. But only if we catch enough events, quickly enough, to build statistics. A fast, accurate classifier is the prerequisite for doing that science at the scale next-generation detectors will demand.

> **Bottom Line:** By training a CNN on half a million real-noise samples and validating it against every confirmed neutron star merger on record, this work shows that deep learning can replace or dramatically augment matched filtering for real-time gravitational wave classification, enabling rapid multi-messenger follow-up at the scale of millions of events per year.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies a computer vision architecture to real LIGO strain data, using deep learning to solve a classification problem that conventional physics-based methods cannot scale to meet.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Training CNNs on real, non-Gaussian, non-stationary detector noise and showing they generalize to unseen real events validates a strategy applicable to noisy time-series classification problems across scientific domains.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Recovering all confirmed neutron star merger events from GWTC-3 opens a path to rapid electromagnetic follow-up of BNS and NSBH events, the primary astrophysical probes of dense matter and the nuclear equation of state.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will focus on reducing detection latency toward real-time operation and extending the framework to next-generation detectors like Einstein Telescope and Cosmic Explorer; the full study is available at [arXiv:2210.15888](https://arxiv.org/abs/2210.15888).</span></div></div>
</div>
