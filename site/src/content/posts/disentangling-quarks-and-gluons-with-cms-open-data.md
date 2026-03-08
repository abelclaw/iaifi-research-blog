---
abstract: We study quark and gluon jets separately using public collider data from
  the CMS experiment. Our analysis is based on 2.3/fb of proton-proton collisions
  at 7 TeV, collected at the Large Hadron Collider in 2011. We define two non-overlapping
  samples via a pseudorapidity cut -- central jets with |eta| < 0.65 and forward jets
  with |eta| > 0.65 -- and employ jet topic modeling to extract individual distributions
  for the maximally separable categories. Under certain assumptions, such as sample
  independence and mutual irreducibility, these categories correspond to "quark" and
  "gluon" jets, as given by a recently proposed operational definition. We consider
  a number of different methods for extracting reducibility factors from the central
  and forward datasets, from which the fractions of quark jets in each sample can
  be determined. The greatest stability and robustness to statistical uncertainties
  is achieved by a novel method based on parametrizing the endpoints of a receiver
  operating characteristic (ROC) curve. To mitigate detector effects, which would
  otherwise induce unphysical differences between central and forward jets, we use
  the OmniFold method to perform central value unfolding. As a demonstration of the
  power of this method, we extract the intrinsic dimensionality of the quark and gluon
  jet samples, which exhibit Casimir scaling, as expected from the strongly-ordered
  limit. To our knowledge, this work is the first application of full phase space
  unfolding to real collider data, and one of the first applications of topic modeling
  to extract separate quark and gluon distributions at the LHC.
arxivId: '2205.04459'
arxivUrl: https://arxiv.org/abs/2205.04459
authors:
- Patrick T. Komiske
- Serhii Kryhin
- Jesse Thaler
concepts:
- jet physics
- jet topic modeling
- collider physics
- unfolding
- roc curve fit
- classification
- likelihood ratio
- dimensionality reduction
- monte carlo methods
- quantum field theory
- anomaly detection
figures:
- /iaifi-research-blog/figures/2205_04459/figure_1.png
- /iaifi-research-blog/figures/2205_04459/figure_1.png
- /iaifi-research-blog/figures/2205_04459/figure_2.png
- /iaifi-research-blog/figures/2205_04459/figure_2.png
- /iaifi-research-blog/figures/2205_04459/figure_3.png
- /iaifi-research-blog/figures/2205_04459/figure_3.png
pdfUrl: https://arxiv.org/pdf/2205.04459v2
published: '2022-05-09T17:59:59+00:00'
theme: Theoretical Physics
title: Disentangling Quarks and Gluons with CMS Open Data
wordCount: 1079
---

## The Big Picture

Imagine trying to figure out whether a crowd came from two different cities without asking anyone where they're from. All you can do is observe their behavior, clothes, and speech patterns, then use statistics to infer the mixture. That's the challenge physicists face when looking at "jets," the sprays of particles that shoot out when protons smash together inside the Large Hadron Collider.

At the heart of every proton collision are quarks and gluons, bound together by the strong nuclear force as described by **quantum chromodynamics** (QCD). You can never catch a single quark or gluon in isolation. **Color confinement** ensures these particles immediately cluster into cascading sprays of hundreds of other particles the moment they're knocked free. Those sprays are the jets.

When you record a jet in a detector, you know *something* initiated it, but was it a quark or a gluon? The two types produce different-looking sprays, and telling them apart matters for testing QCD and hunting for new physics. The catch: labeling any given jet as "quark-initiated" or "gluon-initiated" is fundamentally ambiguous. The detector sees the spray, never the source.

Patrick Komiske, Serhii Kryhin, and Jesse Thaler at MIT's Center for Theoretical Physics tackled this problem using publicly available CMS detector data from 2.3 fb⁻¹ of real proton-proton collisions at 7 TeV. They borrowed a technique from text mining, applied it to actual LHC data, and used machine learning to pull apart quark and gluon distributions from samples that only ever show their mixture.

> **Key Insight:** By treating quark and gluon jets like "topics" in a statistical mixture, the researchers extracted individual quark and gluon distributions directly from real LHC data for the first time, using open-access CMS collisions from 2011 with no simulation labels required.

## How It Works

The core framework is **jet topic modeling**, borrowed from natural language processing, where it identifies latent themes in document collections. A document might be 70% politics and 30% economics. Similarly, a jet sample is a mixture of quark and gluon jets. Given two samples with *different* mixing fractions, you can solve for the underlying pure distributions.

The two mixed samples come from splitting jets by **pseudorapidity** (η), a measure of a jet's angle relative to the beam. Central jets (|η| ≤ 0.65) tend to be quark-enriched; forward jets (|η| > 0.65) tend to be gluon-enriched. Neither sample is pure, but their differences are enough to work with.

![Figure 1](figure:1)

The challenge is then extracting the **reducibility factors**, numbers that pin down how much of one distribution "leaks" into the other and fix the quark fraction in each sample. The paper introduces and compares three approaches:

- **Anchor bin method** (existing): Identify regions of phase space that are nearly 100% quark or gluon and use them as statistical anchors. In practice, those regions are rare, and statistical noise degrades precision fast.
- **Log-likelihood ratio fit (L-fit)**: Fit probability distributions across all data using quantile binning, dividing data into equally populated buckets. More data contribute to the estimate, which improves stability.
- **ROC curve fit (R-fit)**: The most original approach. Train a machine learning classifier to distinguish central from forward jets, then analyze the endpoints of the resulting **receiver operating characteristic (ROC) curve**. These endpoints encode the reducibility factors directly, bypassing binning altogether.

![Figure 2](figure:2)

The R-fit turned out to be the most stable option. By parametrizing only the endpoints of the ROC curve rather than its full shape, it sidesteps sensitivity to training imperfections and statistical fluctuations in the body of the distribution.

One significant complication: the CMS detector doesn't respond to jets identically at all pseudorapidities. A gluon jet in the central region gets measured differently than one in the forward region, not because the physics changes, but because the detector does. This **sample dependence** would introduce spurious differences between the two jet samples, corrupting the topic modeling.

To correct for this, the team applied **OmniFold**, a machine-learning-based unfolding technique that statistically removes detector distortions to recover the true underlying particle distributions. This was the first application of full phase-space unfolding to real collider data. After unfolding, the extracted quark/gluon fractions agreed well with predictions from Pythia, the standard LHC collision simulator.

![Figure 3](figure:3)

## Why It Matters

The immediate result is a set of extracted quark and gluon jet distributions (substructure shapes, tagging performance curves, rapidity spectra) derived empirically from data rather than assumed from theory or simulation.

One finding offers a clean validation: **Casimir scaling of intrinsic dimensionality**. The "intrinsic dimensionality" of a jet captures how many independent degrees of freedom describe it, roughly how complex the particle spray is. QCD predicts this quantity should scale with the **Casimir factor** of the initiating particle: 4/3 for quarks, 3 for gluons.

The extracted intrinsic dimensionality from the unfolded quark and gluon samples follows exactly this ratio. A deep QCD prediction, confirmed with machine learning on publicly available data. No proprietary datasets, no special experimental access.

![Figure 5](figure:5)

For particle physics, the takeaway is that jet topic modeling works on real experimental data. Open LHC data can serve as a testbed for QCD measurements that previously seemed to require direct quark/gluon labels. For machine learning in science, methods like OmniFold and ROC-curve-based inference can handle messy real-world data, not just clean simulations.

> **Bottom Line:** By combining jet topic modeling with machine-learning-based unfolding on CMS Open Data, this work separates quark and gluon jets from data alone and validates QCD's Casimir scaling prediction, marking the first full phase-space unfolding of real LHC data.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects statistical topic modeling from computational linguistics with experimental particle physics, extracting fundamental QCD properties from real LHC data without requiring direct quark or gluon labels.

- **Impact on Artificial Intelligence:** The paper introduces a ROC-curve-fit method and applies OmniFold to real collider data for the first time, showing that ML-based inference can handle the statistical and systematic challenges of actual experimental environments.

- **Impact on Fundamental Interactions:** By extracting separate quark and gluon jet distributions from CMS Open Data and observing Casimir scaling in their intrinsic dimensionality, the work provides a new empirical handle on QCD jet physics that does not depend on Monte Carlo simulation assumptions.

- **Outlook and References:** Future work will extend this approach to include full systematic uncertainty analyses and apply topic modeling to other mixed jet samples at the LHC. The full analysis is publicly available; the paper appears as [arXiv:2205.04459](https://arxiv.org/abs/2205.04459).
