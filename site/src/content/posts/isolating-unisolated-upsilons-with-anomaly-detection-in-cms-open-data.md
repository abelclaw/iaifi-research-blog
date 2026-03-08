---
abstract: We present the first study of anti-isolated Upsilon decays to two muons
  ($Υ\to μ^+ μ^-$) in proton-proton collisions at the Large Hadron Collider. Using
  a machine learning (ML)-based anomaly detection strategy, we "rediscover" the $Υ$
  in 13 TeV CMS Open Data from 2016, despite overwhelming anti-isolated backgrounds.
  We elevate the signal significance to $6.4 σ$ using these methods, starting from
  $1.6 σ$ using the dimuon mass spectrum alone. Moreover, we demonstrate improved
  sensitivity from using an ML-based estimate of the multi-feature likelihood compared
  to traditional "cut-and-count" methods. Our work demonstrates that it is possible
  and practical to find real signals in experimental collider data using ML-based
  anomaly detection, and we distill a readily-accessible benchmark dataset from the
  CMS Open Data to facilitate future anomaly detection developments.
arxivId: '2502.14036'
arxivUrl: https://arxiv.org/abs/2502.14036
authors:
- Rikab Gambhir
- Radha Mastandrea
- Benjamin Nachman
- Jesse Thaler
concepts:
- anomaly detection
- collider physics
- anti-isolated quarkonia
- density estimation
- likelihood ratio
- normalizing flows
- hypothesis testing
- jet physics
- signal detection
- classification
- new physics searches
- simulation-based inference
figures:
- /iaifi-research-blog/figures/2502_14036/figure_1.png
- /iaifi-research-blog/figures/2502_14036/figure_1.png
- /iaifi-research-blog/figures/2502_14036/figure_2.png
- /iaifi-research-blog/figures/2502_14036/figure_2.png
- /iaifi-research-blog/figures/2502_14036/figure_3.png
- /iaifi-research-blog/figures/2502_14036/figure_3.png
pdfUrl: https://arxiv.org/pdf/2502.14036v2
published: '2025-02-19T19:00:02+00:00'
theme: Experimental Physics
title: Isolating Unisolated Upsilons with Anomaly Detection in CMS Open Data
wordCount: 1162
---

## The Big Picture

Imagine trying to spot a single whispered conversation in a stadium full of screaming fans during the loudest play of the game. That's roughly the challenge particle physicists face when searching for rare quantum particles buried inside the chaos of high-energy proton collisions at the Large Hadron Collider. Most searches sidestep this problem by filtering for "quiet" events, particles that emerge cleanly separated from surrounding debris. But what about the signals hiding *inside* the noise?

The **Upsilon (Υ)** is a particle made of a bottom quark and its antimatter partner, a fleeting bundle that forms from the raw energy of collisions and quickly decays into two muons. Physicists have studied it for decades in clean, uncrowded conditions. When an Upsilon forms *within* a roiling jet of other particles, though, its signal gets drowned out.

That "anti-isolated" scenario is exactly what a team from MIT and Lawrence Berkeley National Laboratory tackled. Nobody had successfully pulled such a signal out of real collider data before. The backgrounds are simply too overwhelming for traditional methods.

Using machine learning-based anomaly detection on publicly available CMS Open Data, the team took a nearly invisible hint and turned it into a clear detection. The signal jumped from a barely perceptible 1.6σ to 6.4σ. In physics, **sigma (σ)** measures statistical confidence: 5σ is the conventional discovery threshold, meaning the chance of a random fluctuation mimicking the signal is less than one in a million. This result clears that bar.

> **Key Insight:** Machine learning anomaly detection can find real physics signals in messy, real-world collider data, not just in clean simulations, opening a new front in the search for unknown particles.

## How It Works

The analysis begins with a clever choice of battlefield. The team pulled data from CMS's 2016 run at 13 TeV, collision energy enough to produce heavy particles like the Upsilon many thousands of times over, focusing on events where two muons were recorded. Rather than requiring the muons to be cleanly separated from surrounding activity, they flipped the script entirely: imposing an **anti-isolation criterion** that forced muon pairs to be *embedded* in surrounding particle activity, with non-muon momentum exceeding 55% of the muon momentum within a cone of radius ΔR = 0.4.

![Figure 1](figure:1)

This cut dramatically suppresses the signal. Without any cuts, Upsilons shine out at 28σ. With anti-isolation imposed, the **dimuon mass spectrum** (a plot of how many muon pairs appear at each combined mass, where a real particle shows up as a bump at its known mass) yields a barely perceptible 1.6σ bump. Two dominant backgrounds conspire to bury the Upsilon's characteristic peaks near 9–10 GeV: uncorrelated hadron decays and **Drell-Yan production**, a process in which a virtual photon briefly materializes and decays into a muon pair, producing a smoothly falling background.

To fight back, the researchers deployed **CATHODE** (Classifying Anomalies THrough Outer Density Estimation), an anomaly detection technique that requires no prior knowledge of what the signal looks like. The strategy works in five steps:

1. **Define a signal region** around the expected Upsilon mass (roughly 8.5–11 GeV) and mask it off
2. **Train a density estimator** on sideband data, events just outside the signal region, to learn how the background behaves in auxiliary feature space
3. **Extrapolate the background model** into the signal region using three additional features: dimuon transverse momentum and the 3D impact parameters of each muon (how far off-center each muon's track is from the collision point)
4. **Build an anomaly score** comparing actual data to the predicted background, so events that don't look like background light up as anomalous
5. **Reweight and scan** the mass spectrum, looking for a resonant bump that anomaly detection makes visible

![Figure 2](figure:2)

The three auxiliary features were chosen carefully. Dimuon transverse momentum and impact parameters carry information about how the Upsilon was produced: fragmentation-produced Upsilons behave differently from background muon pairs. The team verified these features don't sculpt artificial peaks in the mass spectrum, a known pitfall where the anomaly score itself creates false bumps by preferentially selecting events at certain masses.

After applying the learned anomaly score, the Upsilon signal jumps from 1.6σ to 6.4σ. The team also compared two ways of using the anomaly score: a simple **cut-and-count** approach (keeping only events above a chosen threshold) versus **likelihood-ratio reweighting**, which uses the full continuous distribution of anomaly scores rather than drawing a hard cutoff. Reweighting consistently outperformed cuts, a finding worth keeping in mind for future searches.

![Figure 3](figure:3)

## Why It Matters

For particle physics, anti-isolated **quarkonia** (heavy particles made of a quark and its antimatter partner) probe **QCD fragmentation**, the process by which collision energy gradually congeals into massive bound particles, something like cooling steam condensing into water droplets. Understanding how Upsilons form within jets tests the boundary between perturbative QCD, where the underlying math is tractable, and non-perturbative physics, where it isn't. These measurements lay the groundwork for systematic studies of bottomonium-in-jets that could sharpen fragmentation models, just as earlier charmonium measurements did.

The broader significance is methodological. Anomaly detection at the LHC has been tested on synthetic benchmarks and applied by CMS and ATLAS to search for new physics, but with no significant excesses found yet. A previous open data study rediscovered the top quark, but in signal regions people already knew about.

This paper is different. It finds a real signal in real data in a region of **phase space** (the full range of particle configurations and energies an experiment can probe) that nobody had examined before, using methods that require no signal simulation. That's exactly the scenario anomaly detection was built for. The authors also published a curated benchmark dataset alongside their analysis code, giving the ML community a real-world testbed for developing the next generation of search algorithms.

> **Bottom Line:** By pulling a 6.4σ Upsilon signal out of anti-isolated backgrounds that buried it at 1.6σ, this study shows that ML anomaly detection works on real collider data, not just in theory. It's a working tool for finding new physics.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** Machine learning anomaly detection, a technique developed in the AI community, here solves an open problem in experimental particle physics. The result shows that AI tools can extract real signals from regions of phase space where traditional analysis fails.

- **Impact on Artificial Intelligence:** The study validates CATHODE-style density estimation on real, messy experimental data. Likelihood-ratio reweighting outperforms cut-based anomaly score usage, offering practical guidance for future algorithm design.

- **Impact on Fundamental Interactions:** This is the first observation of anti-isolated Υ → μ⁺μ⁻ decays at the LHC, opening a new channel to study QCD bottomonium fragmentation inside jets and to probe the nonperturbative regime of the strong force.

- **Outlook and References:** Future work could apply these methods to search for genuinely unknown resonances in anti-isolated channels. The published CMS Open Data benchmark will support community-wide development of anomaly detection tools. The paper is available at [arXiv:2502.14036](https://arxiv.org/abs/2502.14036).
