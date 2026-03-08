---
abstract: Since the first detection of gravitational waves in 2015 by LIGO from the
  binary black hole merger GW150914, gravitational-wave astronomy has developed significantly,
  with over 200 compact binary merger events cataloged. The use of neural networks
  has the potential to significantly speed up the detection, classification, and especially
  parameter estimation for gravitational wave events, compared to current techniques,
  quite important for electromagnetic follow-up of events. In this work, we present
  a machine learning pipeline using neural networks to detect gravitational wave events.
  We generate training data using real LIGO data to train and refine neural networks
  that can detect binary black hole (BBH) mergers, and apply these models to search
  through LIGO's first three observing runs. We detect 57 out of the 75 total cataloged
  BBH events with two detectors of data in O1, O2, and O3, with 57 false positives
  that can mostly be ruled out with parameter inference and human inspection. Finally,
  we extensively test this pipeline on time-shifted data to characterize its False
  Alarm Rate (FAR). These results are an important step in developing machine learning-based
  GW searches, enabling low-latency detection and multi-messenger astronomy.
arxivId: '2512.17204'
arxivUrl: https://arxiv.org/abs/2512.17204
authors:
- Ethan Silver
- Plamen Krastev
- Edo Berger
concepts:
- gravitational waves
- convolutional networks
- signal detection
- classification
- hypothesis testing
- data augmentation
- feature extraction
- multi-messenger astronomy
- anomaly detection
- model validation
- bayesian inference
figures:
- /iaifi-research-blog/figures/2512_17204/figure_1.png
- /iaifi-research-blog/figures/2512_17204/figure_2.png
- /iaifi-research-blog/figures/2512_17204/figure_3.png
pdfUrl: https://arxiv.org/pdf/2512.17204v2
published: '2025-12-19T03:29:45+00:00'
theme: Astrophysics
title: A Search for Binary Black Hole Mergers in LIGO O1-O3 Data with Convolutional
  Neural Networks
wordCount: 1055
---

## The Big Picture

Imagine trying to hear a whisper from a billion light-years away, lasting less than a second, buried beneath the constant rumble of traffic, wind, and seismic noise. That is more or less what physicists do every time they hunt for gravitational waves at LIGO. The signal from two colliding black holes arrives as a ripple in spacetime so faint that the detector mirrors move by a distance a thousand times smaller than a proton's width.

For a decade, LIGO has relied on **matched filtering**, cross-checking incoming data against millions of pre-calculated signal templates. It works well, but it's slow and computationally expensive. It's also poorly suited for the rapid alerts astronomers need when two neutron stars collide and their light starts fading within hours.

Machine learning offers a faster path. Neural networks can be trained to recognize the characteristic "chirp" of a black hole merger (a rapid upward sweep in frequency as two objects spiral together) and classify new data in milliseconds rather than minutes.

Researchers Ethan Silver, Plamen Krastev, and Edo Berger at Harvard and IAIFI have built a machine-learning search pipeline that scans all three of LIGO's first observing runs and recovers 57 out of 75 cataloged binary black hole mergers.

> **Key Insight:** By training convolutional neural networks directly on real LIGO noise, not simulated Gaussian noise, this pipeline achieves competitive detection rates across three full observing runs while running orders of magnitude faster than traditional matched-filter methods.

## How It Works

The pipeline starts with real data. The team pulled roughly 22 days of continuous output from LIGO's second observing run (O2), from both the Livingston (L1) and Hanford (H1) detectors, sampled at 4096 Hz. They injected simulated black hole merger waveforms into half of these snippets, creating a labeled training set of "signal" and "noise" examples.

Getting the mass distribution right was critical. Real binary black hole events span a wide range of masses, but sampling each independently from a uniform distribution yields very few systems where both holes are low-mass, even though those systems produce longer, harder-to-detect signals. The team solved this with intentional oversampling: they first drew a maximum mass from a triangular distribution peaked at 5 solar masses, then sampled individual masses uniformly below that ceiling. This ensured the training set included plenty of challenging low-mass events.

![Figure 1](figure:1)

Waveforms were generated using the **SEOBNRv4** approximant, a state-of-the-art model for the time-domain gravitational wave signal from spinning, non-precessing black hole binaries, via the PyCBC library. Both signal and noise were then **whitened**: a preprocessing step that flattens the noise power spectrum so the network sees a statistically uniform background. Each 4-second template captures the inspiral (gradual approach), merger (collision), and ringdown (final settling) of the signal across both detectors simultaneously.

The team trained two distinct families of models:

- **Time-series CNNs** that process raw whitened strain data directly. (CNNs, or convolutional neural networks, are a class of neural network that detects patterns in sequential data.)
- **Time-frequency CNNs** that operate on **spectrograms**, visual representations of how signal power varies across frequency bands over time.

Both architectures learned to distinguish the characteristic chirp from noise transients. Running them in parallel and requiring agreement between them helped suppress false alarms.

## Why It Matters

The pipeline scanned all of LIGO's O1, O2, and O3 data, covering 75 binary black hole events with two-detector data available, and recovered 57 of those 75 events: a detection rate of 76%. That compares favorably to recent competing ML searches; AresGW found 40 of 65 O3 events, and AFrame found 38. The 57 false positives can largely be eliminated through quick parameter inference (fitting the signal to extract mass and spin) and human review, reducing the burden to a manageable vetting step.

![Figure 2](figure:2)

To measure how often the network would flag non-existent signals, the team ran an extensive **time-shift test**. They offset the L1 and H1 data streams by amounts large enough to destroy any genuine coincident signal. A real gravitational wave arrives at both detectors within ~10 milliseconds; a 100-second shift eliminates all real coincidences. Detections in this shifted data measured the **false alarm rate (FAR)** as a function of detection threshold, which is the standard LIGO method for characterizing detection significance.

![Figure 3](figure:3)

Speed is the central motivation. LIGO O4 has cataloged over 200 events in its first 23 months, and next-generation detectors like Einstein Telescope and Cosmic Explorer promise event rates orders of magnitude higher. The field needs tools that triage candidates instantly. A neural network processing 4 seconds of data in milliseconds can send alerts to optical telescopes while a neutron star merger's kilonova is still brightening.

Binary neutron star and neutron star-black hole mergers produce electromagnetic counterparts: gamma-ray bursts, kilonovae, radio afterglows. These carry independent information about nuclear physics and cosmology. Catching them within minutes of the gravitational wave trigger is the difference between a full multi-messenger portrait and a missed opportunity.

> **Bottom Line:** A CNN-based pipeline trained on real LIGO noise recovers 76% of known binary black hole mergers across O1–O3, with a false alarm rate low enough for practical use. Machine learning is ready to play a central role in the next era of gravitational wave astronomy.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work sits squarely at the intersection of gravitational wave astrophysics and deep learning, using convolutional neural networks trained on real interferometer data to tackle one of observational physics' most demanding signal-detection problems.

- **Impact on Artificial Intelligence:** The pipeline shows that CNNs can generalize from training data to perform blind searches over years of real-world detector output, handling non-Gaussian noise artifacts and multi-detector coincidence analysis.

- **Impact on Fundamental Interactions:** By recovering 57 of 75 cataloged binary black hole mergers across LIGO O1–O3, the work validates ML as a viable complement to matched filtering, directly advancing detection infrastructure for gravitational wave and multi-messenger astronomy.

- **Outlook and References:** Future work will extend the approach to binary neutron star and neutron star-black hole mergers and explore low-latency deployment for real-time alerts; the paper is available at [arXiv:2512.17204](https://arxiv.org/abs/2512.17204).

## Original Paper Details
- **Title:** A Search for Binary Black Hole Mergers in LIGO O1-O3 Data with Convolutional Neural Networks
- **arXiv ID:** 2512.17204
- **Authors:** ["Ethan Silver", "Plamen Krastev", "Edo Berger"]
- **Abstract:** Since the first detection of gravitational waves in 2015 by LIGO from the binary black hole merger GW150914, gravitational-wave astronomy has developed significantly, with over 200 compact binary merger events cataloged. The use of neural networks has the potential to significantly speed up the detection, classification, and especially parameter estimation for gravitational wave events, compared to current techniques, quite important for electromagnetic follow-up of events. In this work, we present a machine learning pipeline using neural networks to detect gravitational wave events. We generate training data using real LIGO data to train and refine neural networks that can detect binary black hole (BBH) mergers, and apply these models to search through LIGO's first three observing runs. We detect 57 out of the 75 total cataloged BBH events with two detectors of data in O1, O2, and O3, with 57 false positives that can mostly be ruled out with parameter inference and human inspection. Finally, we extensively test this pipeline on time-shifted data to characterize its False Alarm Rate (FAR). These results are an important step in developing machine learning-based GW searches, enabling low-latency detection and multi-messenger astronomy.
