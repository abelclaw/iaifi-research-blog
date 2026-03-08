---
abstract: A search for the standard model (SM) Higgs boson (H) produced with transverse
  momentum greater than 450 GeV and decaying to a charm quark-antiquark ($\mathrm{c\bar{c}}$)
  pair is presented. The search is performed using proton-proton collision data collected
  at $\sqrt{s}$ = 13 TeV by the CMS experiment at the LHC, corresponding to an integrated
  luminosity of 138 fb$^{-1}$. Boosted H $\to$ $\mathrm{c\bar{c}}$ decay products
  are reconstructed as a single large-radius jet and identified using a deep neural
  network charm tagging technique. The method is validated by measuring the Z $\to$
  $\mathrm{c\bar{c}}$ decay process, which is observed in association with jets at
  high $p_\mathrm{T}$ for the first time with a signal strength of 1.00 $_{-0.14}^{+0.17}$
  (syst) $\pm$ 0.08 (theo) $\pm$ 0.06 (stat), defined as the ratio of the observed
  process rate to the standard model expectation. The observed (expected) upper limit
  on $σ$(H) $\mathcal{B}$(H $\to$ $\mathrm{c\bar{c}}$) is set at 47 (39) times the
  SM prediction at 95% confidence level.
arxivId: '2211.14181'
arxivUrl: https://arxiv.org/abs/2211.14181
authors:
- CMS Collaboration
concepts:
- collider physics
- jet physics
- charm jet tagging
- new physics searches
- standard model
- classification
- signal detection
- hypothesis testing
- detector simulation
- monte carlo methods
- trigger systems
figures:
- /iaifi-research-blog/figures/2211_14181/figure_1.png
- /iaifi-research-blog/figures/2211_14181/figure_2.png
pdfUrl: https://arxiv.org/pdf/2211.14181v2
published: '2022-11-25T15:37:52+00:00'
theme: Experimental Physics
title: Search for Higgs boson and observation of Z boson through their decay into
  a charm quark-antiquark pair in boosted topologies in proton-proton collisions at
  $\sqrt{s}$ = 13 TeV
wordCount: 1043
---

## The Big Picture

Imagine trying to identify a specific person at a crowded concert from a single blurry photograph. Now imagine that person is moving at nearly the speed of light, and the photograph is replaced by billions of particle collisions every second. That's roughly the challenge physicists face when trying to catch the Higgs boson decaying into a pair of charm quarks, a signal so faint it has eluded every search so far.

The Higgs boson, discovered in 2012, gives other particles their mass. But physicists must still verify that it interacts with all the right particles at exactly the right strength. The Standard Model predicts how strongly the Higgs should couple to each type of matter particle. Heavier particles interact more strongly, which is why signals involving bottom quarks and tau leptons have already been confirmed.

Charm quarks sit one rung down the mass ladder. They interact with the Higgs at a rate about 20 times weaker than bottom quarks, making their signal extraordinarily faint. Finding it is like picking out a whisper in a hurricane.

A new result from the CMS Collaboration at CERN takes a different approach: instead of conventional Higgs production modes, they look for ultra-fast Higgs bosons recoiling at extreme transverse momentum. To make it work, they built a neural-network charm detector that enables this search for the first time.

> **Key Insight:** CMS has made the first-ever observation of the Z boson decaying to charm quarks in boosted topologies, validating a new AI-powered tagging approach and setting the tightest constraints yet on Higgs-to-charm decays in gluon-gluon fusion production.

## How It Works

The strategy hinges on boosting. When a Higgs boson is produced with enormous transverse momentum (more than 450 GeV, roughly 450 times the mass of a proton), its decay products are crammed together so tightly that a traditional detector can't separate them. The CMS team treats this as a feature rather than a problem: both charm quarks merge into a single wide jet, and that merged structure carries distinctive internal fingerprints.

These merged jets are reconstructed as **AK8 jets**, large-radius particle clusters spanning an angular cone of size 0.8, built with the anti-kT algorithm. Before analysis, the team applies the **soft-drop algorithm**, which strips away soft, wide-angle radiation. This reveals the jet's underlying mass and suppresses the overwhelming background from ordinary strong-force multijet events. The cleaned jet mass, mSD, must fall between 40 and 201 GeV, a window containing both the Z boson peak (~91 GeV) and the Higgs peak (~125 GeV).

![Figure 1](figure:1)

The real muscle comes from deep neural network charm taggers, AI models trained to pick out charm-quark jets from the flood of ordinary jets. These taggers are **mass-decorrelated**: their output scores don't depend on jet mass. Without this property, a tagger could inadvertently sculpt a fake signal peak into the mass distribution, which would be fatal for a search defined by its mass window.

Mass-decorrelation buys two things. First, it lets the team estimate the background of ordinary jets directly from data, without relying on simulations. Second, it enables a built-in cross-check: searching for Z→cc simultaneously with H→cc, using the known Z boson signal as real-world proof that the whole procedure works.

The search fits jet mass distributions across multiple regions at once:

- A charm-enriched signal region, defined by high scores in both the charm-vs-light and charm-vs-bottom taggers
- A top control region, used to pin down the top quark-pair background from data
- QCD background, estimated entirely from data via a polynomial fit in signal-depleted regions

This multi-region fit extracts both the Z→cc and H→cc signal strengths (how much signal is observed relative to the Standard Model prediction) in one go.

## Why It Matters

The Z boson observation is more than a calibration check. Measuring Z→cc at high transverse momentum with a signal strength of 1.00, perfectly matching the Standard Model, confirms that the charm tagger and analysis framework work as designed. This is the first observation of Z→cc in association with jets in the boosted regime, and it sets a new benchmark for flavor tagging at high momentum.

![Figure 2](figure:2)

For the Higgs, the result sets an observed upper limit of 47 times the Standard Model prediction for σ(H)×B(H→cc) at 95% confidence level, with an expected limit of 39 times. Those numbers might sound large, but they come from gluon-gluon fusion, a production mode never before explored for this decay channel. Combined with ongoing searches in associated production, this measurement adds an entirely new handle on the Higgs-charm coupling. Every independent constraint narrows the room for deviations from the Standard Model.

The High-Luminosity LHC upgrade will multiply the available dataset substantially, potentially bringing sensitivity much closer to the Standard Model prediction itself. The **charm Yukawa coupling**, the strength of the Higgs-charm interaction, remains one of the last major unmeasured parameters in the Standard Model's fermion sector. Experiments like this one are steadily closing in on it.

> **Bottom Line:** CMS has observed, for the first time, Z bosons decaying to charm quarks in boosted topologies, with results that match theory perfectly. The same AI-powered tagging method pushes the frontier on Higgs-to-charm searches in a production mode that had never been explored before.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work sits squarely at the intersection of machine learning and experimental particle physics, deploying mass-decorrelated deep neural networks as the central tool for identifying charm quarks inside boosted jets, a task that is out of reach for traditional cut-based approaches.

- **Impact on Artificial Intelligence:** The mass-decorrelated charm tagger shows how architectural constraints on neural networks can eliminate systematic artifacts like sculpted backgrounds while preserving discriminating power, a lesson that applies broadly to ML in high-energy physics.

- **Impact on Fundamental Interactions:** The first observation of boosted Z→cc validates a new experimental channel and constrains the Higgs-charm Yukawa coupling from gluon-gluon fusion production for the first time, complementing existing VH-based searches.

- **Outlook and References:** With the High-Luminosity LHC expected to increase the dataset by an order of magnitude, this boosted strategy may eventually reach Standard Model sensitivity for H→cc. The result was published in *Physical Review Letters* ([arXiv:2211.14181](https://arxiv.org/abs/2211.14181)).
