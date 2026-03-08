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
wordCount: 1134
---

## The Big Picture

Imagine trying to figure out whether a crowd came from two different cities — without asking anyone where they're from. All you can do is observe their behavior, clothes, and speech patterns, then use statistics to infer the mixture. That's essentially the challenge physicists face when looking at "jets" — the sprays of particles that shoot out when protons smash together inside the Large Hadron Collider.

At the heart of every proton collision are quarks and gluons — the fundamental building blocks of matter, bound by the strong nuclear force, described by a theory called **quantum chromodynamics** (QCD). But you can never catch a single quark or gluon in isolation. **Color confinement** ensures these particles immediately cluster into cascading sprays of hundreds of other particles the moment they're knocked free. These sprays are the jets.

So when you record a jet in a detector, you know *something* initiated it — but was it a quark? A gluon? The two types behave differently, and understanding those differences is crucial for testing QCD and searching for new physics. But labeling any given jet as "quark-initiated" or "gluon-initiated" is fundamentally ambiguous — the detector only sees the spray, never the source.

A team from MIT's Center for Theoretical Physics — Patrick Komiske, Serhii Kryhin, and Jesse Thaler — tackled this using publicly available CMS detector data from 2 million real particle collisions. Their approach: borrow a technique from text mining, apply it to real LHC data, and use machine learning to extract separate quark and gluon distributions from samples that only ever show their mixture.

> **Key Insight:** By treating quark and gluon jets like "topics" in a statistical mixture, the researchers extracted individual quark and gluon distributions directly from real LHC data for the first time — using open-access CMS collisions from 2011, no simulation labels required.

## How It Works

The core framework is **jet topic modeling**, adapted from the natural language processing technique used to identify latent themes in document collections. Just as a document can be a mixture of "topics" (say, 70% politics, 30% economics), a jet sample can be a mixture of quark and gluon jets. Given two samples with *different* mixing fractions, you can — in principle — solve for the underlying pure distributions.

The two mixed samples were created using **pseudorapidity** (η) — a measure of a jet's angle relative to the beam. Central jets (|η| ≤ 0.65) are quark-enriched; forward jets (|η| > 0.65) are gluon-enriched. Neither sample is pure, but their differences are sufficient to work with.

![Figure 1](/iaifi-research-blog/figures/2205_04459/figure_1.png)

The challenge is then extracting the **reducibility factors** — numbers that pin down how much of one distribution "leaks" into the other, fixing the quark fraction in each sample. The paper introduces and compares three approaches:

- **Anchor bin method** (existing): Identify regions of phase space that are nearly 100% quark or gluon and use them as statistical anchors. Works in principle, but those regions are rare — statistical noise degrades precision fast.
- **Log-likelihood ratio fit (L-fit)**: Fit probability distributions across all data using quantile binning — dividing data into equally populated buckets. More data contribute to the estimate, improving stability.
- **ROC curve fit (R-fit)**: The most novel approach. Train a machine learning classifier to distinguish central from forward jets, then analyze the endpoints of the resulting **receiver operating characteristic (ROC) curve**. These endpoints encode the reducibility factors directly, bypassing binning altogether.

![Figure 2](/iaifi-research-blog/figures/2205_04459/figure_1.png)

The R-fit proved most robust. By parametrizing only the endpoints of the ROC curve rather than its full shape, it avoids sensitivity to training imperfections and statistical fluctuations in the body of the distribution.

One significant complication: the CMS detector doesn't respond to jets identically at all pseudorapidities. A gluon jet in the central region gets measured differently than one in the forward region — not because the physics changes, but because the detector does. This **sample dependence** would introduce spurious differences between the two jet samples, corrupting the topic modeling.

To correct this, the team applied **OmniFold** — a machine-learning-based **unfolding** technique that statistically removes detector distortions to recover the true underlying particle distributions. This marked the first application of full phase-space unfolding to real collider data. After unfolding, the extracted quark/gluon fractions agreed well with predictions from Pythia, the standard LHC collision simulation.

![Figure 3](/iaifi-research-blog/figures/2205_04459/figure_2.png)

## Why It Matters

The immediate payoff is a set of extracted quark and gluon jet distributions — substructure shapes, tagging performance curves, and rapidity spectra — derived empirically from data rather than assumed from theory or simulation.

One result stands out as a particularly elegant validation: **Casimir scaling of intrinsic dimensionality**. The "intrinsic dimensionality" of a jet captures how many independent degrees of freedom are needed to describe it — roughly, how complex the particle spray is. QCD predicts this quantity should scale with the **Casimir factor** of the initiating particle: 4/3 for quarks, 3 for gluons.

When the researchers extracted intrinsic dimensionality from the unfolded quark and gluon samples, they found exactly this ratio — confirming a deep QCD prediction using machine learning on publicly available data, with no proprietary datasets or special experimental access required.

![Figure 5](/iaifi-research-blog/figures/2205_04459/figure_3.png)

The broader implications cut two ways. For particle physics, this demonstrates that jet topic modeling can work on real experimental data, opening the door to using open LHC data as a testbed for QCD measurements previously thought to require direct quark/gluon labels. For machine learning in science, it shows that methods like OmniFold and ROC-curve-based inference can handle messy real-world data — not just clean simulations.

> **Bottom Line:** By combining jet topic modeling with machine-learning-based unfolding on 2 million CMS collisions, this work separates quark and gluon jets from data alone — no simulation labels required — and validates QCD's Casimir scaling prediction, marking the first full phase-space unfolding of real LHC data.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges statistical topic modeling from computational linguistics with experimental particle physics, extracting fundamental QCD properties from real LHC data without requiring direct quark or gluon labels.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces a novel ROC-curve-fit method and applies OmniFold to real collider data for the first time, demonstrating that ML-based inference can handle the statistical and systematic challenges of real experimental environments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By extracting separate quark and gluon jet distributions from CMS Open Data and observing Casimir scaling in their intrinsic dimensionality, the work provides a new empirical handle on QCD jet physics that is independent of Monte Carlo simulation assumptions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend this approach to include full systematic uncertainty analyses and apply topic modeling to other mixed jet samples at the LHC; the full analysis is publicly available, and the paper appears as arXiv:2205.10343.</span></div></div>
</div>
