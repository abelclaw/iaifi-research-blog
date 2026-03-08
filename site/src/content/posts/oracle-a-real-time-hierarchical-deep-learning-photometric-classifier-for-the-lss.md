---
abstract: We present ORACLE, the first hierarchical deep-learning model for real-time,
  context-aware classification of transient and variable astrophysical phenomena.
  ORACLE is a recurrent neural network with Gated Recurrent Units (GRUs), and has
  been trained using a custom hierarchical cross-entropy loss function to provide
  high-confidence classifications along an observationally-driven taxonomy with as
  little as a single photometric observation. Contextual information for each object,
  including host galaxy photometric redshift, offset, ellipticity and brightness,
  is concatenated to the light curve embedding and used to make a final prediction.
  Training on $\sim$0.5M events from the Extended LSST Astronomical Time-Series Classification
  Challenge, we achieve a top-level (Transient vs Variable) macro-averaged precision
  of 0.96 using only 1 day of photometric observations after the first detection in
  addition to contextual information, for each event; this increases to $>$0.99 once
  64 days of the light curve has been obtained, and 0.83 at 1024 days after first
  detection for 19-way classification (including supernova sub-types, active galactic
  nuclei, variable stars, microlensing events, and kilonovae). We also compare ORACLE
  with other state-of-the-art classifiers and report comparable performance for the
  19-way classification task, in addition to delivering accurate top-level classifications
  much earlier. The code and model weights used in this work are publicly available
  at our associated GitHub repository (https://github.com/uiucsn/ELAsTiCC-Classification).
arxivId: '2501.01496'
arxivUrl: https://arxiv.org/abs/2501.01496
authors:
- Ved G. Shah
- Alex Gagliano
- Konstantin Malanchev
- Gautham Narayan
- Alex I. Malz
- The LSST Dark Energy Science Collaboration
concepts:
- hierarchical classification
- recurrent networks
- classification
- loss function design
- photometric light curves
- supernova classification
- feature extraction
- embeddings
- calibration
- galaxy classification
- multi-task learning
- scalability
figures:
- /iaifi-research-blog/figures/2501_01496/figure_1.png
- /iaifi-research-blog/figures/2501_01496/figure_1.png
- /iaifi-research-blog/figures/2501_01496/figure_2.png
- /iaifi-research-blog/figures/2501_01496/figure_2.png
- /iaifi-research-blog/figures/2501_01496/figure_3.png
- /iaifi-research-blog/figures/2501_01496/figure_3.png
pdfUrl: https://arxiv.org/pdf/2501.01496v2
published: '2025-01-02T19:00:05+00:00'
theme: Astrophysics
title: 'ORACLE: A Real-Time, Hierarchical, Deep-Learning Photometric Classifier for
  the LSST'
wordCount: 955
---

## The Big Picture

Imagine you're a triage nurse in the world's busiest emergency room, except instead of patients, thousands of exploding stars and warping spacetime events are rushing through the door every night. You have seconds to decide which ones need immediate attention. That's the situation astronomers face with the Vera C. Rubin Observatory's Legacy Survey of Space and Time (LSST), which will discover roughly 100 times more temporary celestial events than any telescope before it.

The arithmetic is brutal. Spectroscopy, spreading starlight into its component wavelengths to read chemical fingerprints and velocities, is the gold standard for identifying what an object actually is. But LSST will generate so many events that spectroscopic follow-up will be possible for less than 1% of them. Miss the window on a rare kilonova (the cosmic forge that makes gold and uranium) and that science is gone forever. Wait too long for a confident classification and the source has dimmed beyond reach.

A team led by Ved G. Shah, including IAIFI researcher Alex Gagliano, built **ORACLE** (Online Ranked Astrophysical CLass Estimator), a neural network that classifies cosmic events almost from the moment they appear, using as little as a single observation. The trick: ORACLE gets *less* specific early and *more* specific as data accumulates, always matching the confidence of the classifier to what the data can actually support.

## How It Works

ORACLE's core is a **recurrent neural network** built with **gated recurrent units (GRUs)**, specialized memory cells that decide what to remember and what to discard as new observations arrive. Unlike classifiers that wait for a complete picture, GRUs update their internal state with each new measurement. This makes them naturally suited to astronomical data, where a **light curve** (an object's brightness record over time) arrives point by point over days, months, or years.

![Figure 1](figure:1)

The real innovation is the training objective. Shah et al. developed a **hierarchical cross-entropy loss function** that encodes 19 astrophysical classes in a tree structure, teaching the model to be correct at multiple levels of detail simultaneously.

At the top, everything is either a "transient" (something that changes and fades, like a supernova) or a "variable" (something that oscillates repeatedly, like a pulsating star). Below that, branches split into supernova subtypes, active galactic nuclei, microlensing events, variable star classes, and kilonovae. The loss function rewards correctness at every level of the tree, not just at the leaves. So what does this hierarchy buy you in practice?

- After **1 day** of data: 0.96 macro-averaged precision at the top level (transient vs. variable), already actionable for urgent follow-up decisions
- After **64 days**: top-level precision exceeds 0.99
- After **1024 days**: 0.83 precision across all 19 classes

![Figure 2](figure:2)

ORACLE also ingests host galaxy context: photometric redshift (distance), the transient's spatial offset from the galaxy's center, ellipticity, and brightness. These features combine with the light curve summary before the final prediction. A transient in the outskirts of a dim dwarf galaxy is probably not the same phenomenon as one sitting dead-center in a massive elliptical, and the model learns these associations from data rather than hand-coded rules.

Training used roughly half a million simulated events from the **Extended LSST Astronomical Time-series Classification Challenge (ELAsTiCC)**, a community benchmark designed to stress-test classifiers against the realistic heterogeneity of LSST's anticipated data stream.

## Why It Matters

Most existing classifiers treat classification as a single-shot problem: accumulate enough data, then output a label. ORACLE treats it as a *continuous dialogue* between telescope and algorithm, committing only to the level of specificity the data can support at each moment. That's a genuine change in how astronomical machine learning works.

Benchmarked against state-of-the-art competitors, ORACLE delivers comparable performance on the 19-way task while dramatically outperforming rivals at early times on the top-level triage decision.

![Figure 3](figure:3)

The payoff goes well beyond supernovae. Kilonovae evolve on timescales of hours to days; an early, confident "transient" flag could trigger spectroscopic resources before the optical emission fades. The same logic applies to tidal disruption events, fast blue optical transients, and any rare phenomenon whose secrets live in early-phase behavior.

As LSST comes online and alert rates climb to millions of events per night, classifiers like ORACLE will be the first filter, separating signal from noise at a scale no human team can handle alone. ORACLE achieves 96% precision in distinguishing transients from variables with just one day of data, scaling to 83% precision across 19 classes with full light curves, giving astronomers a real-time triage system for the most information-rich sky survey ever built.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** ORACLE puts deep sequence modeling to work on a fundamental problem in time-domain astrophysics, embedding physical taxonomy directly into the loss function so the network learns the structure of the cosmos alongside its data.
- **Impact on Artificial Intelligence:** The hierarchical cross-entropy loss function is a generalizable technique for any domain where class relationships form a meaningful tree, from medical diagnosis to ecological species identification.
- **Impact on Fundamental Interactions:** By enabling near-instantaneous classification of rare events like kilonovae, ORACLE directly supports multi-messenger astronomy and the study of neutron star mergers, the physical laboratories where the universe forges heavy elements through r-process nucleosynthesis.
- **Outlook and References:** The team plans to deploy ORACLE within LSST's live alert broker infrastructure. Code and model weights are publicly available at [github.com/uiucsn/ELAsTiCC-Classification](https://github.com/uiucsn/ELAsTiCC-Classification), and the work appears in *The Astrophysical Journal* (2025). [arXiv:2501.01496](https://arxiv.org/abs/2501.01496)

## Original Paper Details
- **Title:** ORACLE: A Real-Time, Hierarchical, Deep-Learning Photometric Classifier for the LSST
- **arXiv ID:** [2501.01496](https://arxiv.org/abs/2501.01496)
- **Authors:** Ved G. Shah, Alex Gagliano, Konstantin Malanchev, Gautham Narayan, Alex I. Malz, The LSST Dark Energy Science Collaboration
- **Abstract:** We present ORACLE, the first hierarchical deep-learning model for real-time, context-aware classification of transient and variable astrophysical phenomena. ORACLE is a recurrent neural network with Gated Recurrent Units (GRUs), and has been trained using a custom hierarchical cross-entropy loss function to provide high-confidence classifications along an observationally-driven taxonomy with as little as a single photometric observation. Contextual information for each object, including host galaxy photometric redshift, offset, ellipticity and brightness, is concatenated to the light curve embedding and used to make a final prediction. Training on ~0.5M events from the Extended LSST Astronomical Time-Series Classification Challenge, we achieve a top-level (Transient vs Variable) macro-averaged precision of 0.96 using only 1 day of photometric observations after the first detection in addition to contextual information, for each event; this increases to >0.99 once 64 days of the light curve has been obtained, and 0.83 at 1024 days after first detection for 19-way classification (including supernova sub-types, active galactic nuclei, variable stars, microlensing events, and kilonovae). We also compare ORACLE with other state-of-the-art classifiers and report comparable performance for the 19-way classification task, in addition to delivering accurate top-level classifications much earlier. The code and model weights used in this work are publicly available at our associated GitHub repository (https://github.com/uiucsn/ELAsTiCC-Classification).
