---
abstract: This paper presents the results of a Neural Network (NN)-based search for
  short-duration gravitational-wave transients in data from the third observing run
  of LIGO, Virgo, and KAGRA. The search targets unmodeled transients with durations
  of milliseconds to a few seconds in the 30-1500 Hz frequency band, without assumptions
  about the incoming signal direction, polarization, or morphology. Using the Gravitational
  Wave Anomalous Knowledge (GWAK) method, three compact binary coalescences (CBCs)
  identified by existing pipelines are successfully detected, along with a range of
  detector glitches. The algorithm constructs a low-dimensional embedded space to
  capture the physical features of signals, enabling the detection of CBCs, detector
  glitches, and unmodeled transients. This study demonstrates GWAK's ability to enhance
  gravitational-wave searches beyond the limits of existing pipelines, laying the
  groundwork for future detection strategies.
arxivId: '2412.19883'
arxivUrl: https://arxiv.org/abs/2412.19883
authors:
- Ryan Raikman
- Eric A. Moreno
- Katya Govorkova
- Siddharth Soni
- Ethan Marx
- William Benoit
- Alec Gunny
- Deep Chatterjee
- Christina Reissel
- Malina M. Desai
- Rafia Omer
- Muhammed Saleem
- Philip Harris
- Erik Katsavounidis
- Michael W. Coughlin
- Dylan Rankin
concepts:
- gravitational waves
- anomaly detection
- autoencoders
- signal detection
- semi-supervised learning
- unmodeled burst search
- dimensionality reduction
- out-of-distribution detection
- representation learning
- embeddings
- convolutional networks
- detector simulation
figures:
- /iaifi-research-blog/figures/2412_19883/figure_1.png
- /iaifi-research-blog/figures/2412_19883/figure_1.png
- /iaifi-research-blog/figures/2412_19883/figure_2.png
- /iaifi-research-blog/figures/2412_19883/figure_2.png
- /iaifi-research-blog/figures/2412_19883/figure_3.png
- /iaifi-research-blog/figures/2412_19883/figure_3.png
pdfUrl: https://arxiv.org/pdf/2412.19883v1
published: '2024-12-27T19:00:01+00:00'
theme: Astrophysics
title: A Neural Network-Based Search for Unmodeled Transients in LIGO-Virgo-KAGRA's
  Third Observing Run
wordCount: 1076
---

## The Big Picture

Imagine listening for a conversation in a crowded, noisy room, but you don't know what language the speakers are using. You can't just look for familiar words. You need a system smart enough to notice something *different* from all the background chatter, even if you've never heard those particular sounds before. That's the challenge facing gravitational-wave astronomers today.

Since LIGO first detected gravitational waves in 2015, physicists have gotten very good at finding what they expect to find: the characteristic "chirps" of merging black holes and neutron stars. These signals are so well-understood that existing algorithms can match detector data against thousands of pre-calculated templates, like a fingerprint database of known events. But the universe doesn't limit itself to what we've modeled. Core-collapse supernovae (the violent deaths of massive stars), excited neutron stars (ultra-dense stellar remnants that ring like bells), cosmic string kinks (hypothetical defects woven into the fabric of spacetime), and phenomena we haven't yet theorized could all send gravitational ripples our way. Template-based searches would completely miss them.

A team from MIT, LIGO, and the University of Minnesota tackled this problem head-on, deploying a neural network framework called **GWAK** (Gravitational Wave Anomalous Knowledge) on the full dataset from LIGO-Virgo-KAGRA's third observing run (O3). Their goal: find short-duration transient signals lurking in the data that no existing algorithm was designed to catch.

> **Key Insight:** GWAK doesn't look for specific signal shapes. It learns to distinguish "astrophysically interesting" from "pure detector noise," even for signals it has never seen, by mapping data into a compact feature space that reveals underlying physical structure.

## How It Works

GWAK is built on a **semi-supervised learning** architecture, a hybrid that uses labeled examples of known signal types to build intuition but doesn't require labels for every possible event. The team trained a collection of **autoencoders**, each specializing in a different signal class:

- **Background noise** — learns to reconstruct detector noise perfectly, and nothing else
- **CBC signals** — compact binary coalescences: merging black holes and neutron stars
- **Other target classes** — trained on simulated burst morphologies including sine-Gaussians and white-noise bursts

An autoencoder compresses input data through a bottleneck (a low-dimensional **latent space**) then tries to reconstruct the original on the other side. Reconstruction error reveals how well the model "understands" the input. A noise-trained autoencoder handles noise well but stumbles on gravitational-wave signals; a CBC-trained autoencoder does the opposite.

![Figure 1](figure:1)

GWAK's key move is combining multiple autoencoders into a unified **embedding space**. Think of this as a map: each region corresponds to a different "flavor" of signal, and any new data gets placed based on which autoencoders recognize it. Rather than asking "does this match template X?", GWAK asks "where does this sit in the space of all possible physical phenomena?"

![Figure 2](figure:2)

The search covered 203.3 days of coincident data from the Hanford (H1) and Livingston (L1) detectors, targeting the 30–1500 Hz band with signal durations from milliseconds to a few seconds. The algorithm assumed nothing about signal direction, polarization, or waveform shape, making this the broadest possible search criteria.

One methodological choice worth noting: rather than training on simulated Gaussian noise, the team trained directly on real O3 background data. Real detector noise is messy, **non-stationary** (its statistical character shifts over time), and full of **glitches**, transient artifacts from scattered light, electronics, and seismic activity. Training on real background made the models far better suited to actual deployment conditions.

## Results: What GWAK Found

The search successfully recovered three compact binary coalescence events already identified by conventional pipelines, confirming that the method works as expected. GWAK also flagged a substantial number of known detector glitches, which makes sense: the embedding space cleanly separates glitch-like features from astrophysical signal features.

![Figure 3](figure:3)

After excluding the three CBC candidates and vetoing known glitch categories, the team found **no statistically significant new detections** of unmodeled gravitational-wave bursts in O3. This is a genuinely meaningful null result. It places new constraints on the rate and strength of burst sources in the local universe, and it establishes GWAK as a credible, operational search pipeline ready for future observing runs.

![Figure 4](figure:4)

No new detections isn't a failure. It's the baseline. A neural network-based pipeline now has proven O3 performance and is ready for O4 and O5 data, where detectors will probe deeper into the universe than ever before.

![Figure 5](figure:5)

## Why It Matters

Gravitational-wave astronomy is entering a new era. The fourth and fifth observing runs bring significantly improved detector sensitivity, which means both more signals and more complex noise. Template-based pipelines will keep finding CBC events, but they'll remain blind to the unexpected. GWAK gives astronomers a qualitatively different capability: the ability to search for gravitational-wave signatures that no theorist has yet written down.

The implications reach well beyond gravitational waves. The semi-supervised autoencoder framework is a general strategy for anomaly detection in high-dimensional time-series data from physics experiments, adaptable to particle physics searches at the LHC, pulsar timing arrays searching for nanohertz gravitational waves, or neutrino detectors watching for supernova bursts. Machine learning here isn't just a faster way to do what we were already doing. It's a new kind of scientific sensor.

![Figure 6](figure:6)

> **Bottom Line:** GWAK's first full observing run search finds no new gravitational-wave burst sources beyond known CBCs, but in doing so, it proves that neural network-based anomaly detection is ready for real deployment in gravitational-wave astronomy, setting the stage for discoveries in more sensitive future runs.

---

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects deep learning methodology with gravitational-wave physics, putting a semi-supervised autoencoder framework into operation as an astrophysical search pipeline on real observing data for the first time.

- **Impact on Artificial Intelligence:** GWAK's embedding-space approach, training specialized autoencoders on distinct signal classes and combining their representations, provides a reusable template for model-agnostic anomaly detection in high-dimensional physics data streams.

- **Impact on Fundamental Interactions:** By completing the first neural network-based all-sky unmodeled search of O3 data, this work extends gravitational-wave astronomy's reach to entirely new signal classes, including core-collapse supernovae, neutron star excitations, and cosmic string phenomena.

- **Outlook and References:** Next-generation detectors will substantially expand the discovery reach of GWAK-style searches; the full methodology and O3 results are detailed in [arXiv:2412.19883](https://arxiv.org/abs/2412.19883).

## Original Paper Details
- **Title:** A Neural Network-Based Search for Unmodeled Transients in LIGO-Virgo-KAGRA's Third Observing Run
- **arXiv ID:** 2412.19883
- **Authors:** ["Ryan Raikman", "Eric A. Moreno", "Katya Govorkova", "Siddharth Soni", "Ethan Marx", "William Benoit", "Alec Gunny", "Deep Chatterjee", "Christina Reissel", "Malina M. Desai", "Rafia Omer", "Muhammed Saleem", "Philip Harris", "Erik Katsavounidis", "Michael W. Coughlin", "Dylan Rankin"]
- **Abstract:** This paper presents the results of a Neural Network (NN)-based search for short-duration gravitational-wave transients in data from the third observing run of LIGO, Virgo, and KAGRA. The search targets unmodeled transients with durations of milliseconds to a few seconds in the 30-1500 Hz frequency band, without assumptions about the incoming signal direction, polarization, or morphology. Using the Gravitational Wave Anomalous Knowledge (GWAK) method, three compact binary coalescences (CBCs) identified by existing pipelines are successfully detected, along with a range of detector glitches. The algorithm constructs a low-dimensional embedded space to capture the physical features of signals, enabling the detection of CBCs, detector glitches, and unmodeled transients. This study demonstrates GWAK's ability to enhance gravitational-wave searches beyond the limits of existing pipelines, laying the groundwork for future detection strategies.
