---
abstract: 'In this study, we investigate the application of the New Physics Learning
  Machine (NPLM) algorithm as an alternative to the standard CWoLa method with Boosted
  Decision Trees (BDTs), particularly for scenarios with rare signal events. NPLM
  offers an end-to-end approach to anomaly detection and hypothesis testing by utilizing
  an in-sample evaluation of a binary classifier to estimate a log-density ratio,
  which can improve detection performance without prior assumptions on the signal
  model. We examine two approaches: (1) a end-to-end NPLM application in cases with
  reliable background modelling and (2) an NPLM-based classifier used for signal selection
  when accurate background modelling is unavailable, with subsequent performance enhancement
  through a hyper-test on multiple values of the selection threshold. Our findings
  show that NPLM-based methods outperform BDT-based approaches in detection performance,
  particularly in low signal injection scenarios, while significantly reducing epistemic
  variance due to hyperparameter choices. This work highlights the potential of NPLM
  for robust resonant anomaly detection in particle physics, setting a foundation
  for future methods that enhance sensitivity and consistency under signal variability.'
arxivId: '2501.01778'
arxivUrl: https://arxiv.org/abs/2501.01778
authors:
- Gaia Grosso
- Debajyoti Sengupta
- Tobias Golling
- Philip Harris
concepts:
- anomaly detection
- hypothesis testing
- likelihood ratio
- new physics searches
- signal detection
- collider physics
- weakly supervised anomaly detection
- classification
- density estimation
- ensemble methods
- uncertainty quantification
- goodness-of-fit testing
figures:
- /iaifi-research-blog/figures/2501_01778/figure_1.png
- /iaifi-research-blog/figures/2501_01778/figure_1.png
- /iaifi-research-blog/figures/2501_01778/figure_2.png
- /iaifi-research-blog/figures/2501_01778/figure_2.png
- /iaifi-research-blog/figures/2501_01778/figure_3.png
- /iaifi-research-blog/figures/2501_01778/figure_3.png
pdfUrl: https://arxiv.org/pdf/2501.01778v1
published: '2025-01-03T12:20:09+00:00'
theme: Experimental Physics
title: Robust resonant anomaly detection with NPLM
wordCount: 998
---

## The Big Picture

Imagine scanning an entire city for one person wearing a red hat in a crowd of millions. Most search strategies require you to already know roughly what that person looks like, or at least have a description. But what if you had no idea who you were looking for, only that they were *different* from everyone else? That's the challenge facing physicists hunting for new particles at the Large Hadron Collider.

New particles should appear as tiny bumps, resonant peaks rising ever so slightly above a smooth, steeply falling background of ordinary particle collisions. These bumps might be extraordinarily rare: a handful of exotic events buried in billions of mundane ones. Physicists don't always know in advance what shape the bump should take, which particles it breaks apart into, or how strong the signal will be. Current machine learning methods help, but they struggle hardest right where it matters most, when signals are at their faintest.

A team from MIT, Harvard, and the University of Geneva has shown that a newer algorithm called the **New Physics Learning Machine (NPLM)** outperforms standard approaches in exactly this regime. It works better at low signal strengths and carries far less sensitivity to the arbitrary tuning choices that currently plague the field.

> **Key Insight:** NPLM's "in-sample" evaluation strategy lets it detect extremely rare anomalies more reliably than existing methods, while dramatically cutting variance caused by arbitrary hyperparameter choices.

## How It Works

The reigning approach for resonant anomaly detection is **CWoLa (Classification Without Labels)**, typically paired with **Boosted Decision Trees (BDTs)**, an ensemble method that chains many simple decision rules into a powerful classifier. CWoLa defines a "signal region," the narrow mass range where a new particle might appear, and a surrounding control zone called a "sideband." It then trains a classifier to distinguish events in one from events in the other. Genuine differences between the two regions signal a discovery.

But CWoLa-BDT has a known vulnerability: performance swings wildly depending on four key knobs — number of trees, tree depth, learning rate, and regularization strength. These are **hyperparameters**, the design choices governing how a machine learning algorithm behaves, separate from what it actually learns from data. Choosing them poorly can mean the difference between discovering new physics and missing it entirely. In practice, physicists rarely know the right settings in advance.

![Figure 1](/iaifi-research-blog/figures/2501_01778/figure_1.png)

NPLM takes a different approach. Rather than training a classifier on held-out data and applying it separately, NPLM uses **in-sample evaluation**, training and evaluating on the *same* dataset simultaneously. It directly estimates the **log-density ratio**: a score measuring how much more likely a given event is to come from real signal than from background noise. That score is, provably, the most statistically powerful possible test for whether a signal exists, per the Neyman-Pearson lemma.

NPLM isn't just detecting anomalies. It's simultaneously computing the optimal test for whether those anomalies are real.

The researchers explored two distinct scenarios:

1. **End-to-end NPLM** — When an accurate background model is available, skip the signal-selection step entirely and let NPLM handle both anomaly detection and hypothesis testing in one shot.
2. **NPLM as a classifier with hyper-testing** — When background modeling is imperfect, use NPLM's classifier for signal enrichment, then run a **hyper-test**: scan across multiple values of the selection threshold and combine results, capturing signal sensitivity across a range of possible signal strengths.

![Figure 2](/iaifi-research-blog/figures/2501_01778/figure_1.png)

The hyper-test approach is particularly clever. Instead of committing to a single threshold, a choice that could include too much background noise or cut genuine signal, the method aggregates evidence across many thresholds. It's like casting a wide net and asking: "At what mesh size do we catch the most fish with the least seaweed?"

## Why It Matters

The numbers back this up. Across low signal injection scenarios, where signal events might represent only a tiny fraction of total data, NPLM-based methods consistently beat BDT-based approaches in detection power. They also show much lower **epistemic variance**, the spread in results caused by different reasonable hyperparameter choices.

A detector at ATLAS or CMS can't re-run an experiment just to tune a machine learning model; the data come once. Methods that hold up across hyperparameter choices aren't just convenient. They're essential for trustworthy results.

![Figure 3](/iaifi-research-blog/figures/2501_01778/figure_2.png)

The same bump-hunt strategy appears across fields, from gravitational wave detection to spectroscopy to drug trial analysis. Any domain where you're searching for a rare, unpredictable signal embedded in well-characterized noise could benefit from NPLM's approach. Folding anomaly detection and hypothesis testing into a single framework is a concrete step toward the automated, assumption-free searches next-generation experiments will need.

Open questions remain. NPLM's end-to-end mode requires a high-quality background template, a condition sometimes hard to meet in real analyses. The authors flag extending these methods to realistic background estimation pipelines and higher-dimensional feature spaces as natural next steps. The full study is available at [arXiv:2501.01778](https://arxiv.org/abs/2501.01778).

> **Bottom Line:** NPLM-based resonant anomaly detection outperforms standard BDT methods where it counts most, at low signal strengths, while slashing sensitivity to arbitrary hyperparameter choices. It offers a more statistically principled path to discovering new physics at the LHC.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies end-to-end density-ratio estimation directly to one of the central challenges in experimental high-energy physics: model-agnostic new particle searches at the LHC, squarely within IAIFI's mission at the intersection of AI and fundamental physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The NPLM framework shows that in-sample classifier evaluation produces more statistically principled anomaly detection with lower variance than standard out-of-sample approaches, a principle applicable well beyond particle physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By improving sensitivity to rare signals and reducing dependence on hyperparameter tuning, NPLM-based methods sharpen the LHC's ability to detect signatures of physics beyond the Standard Model in resonant searches at ATLAS and CMS.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend NPLM to realistic background modeling pipelines and higher-dimensional feature spaces. The full study is available at [arXiv:2501.01778](https://arxiv.org/abs/2501.01778).</span></div></div>
</div>
