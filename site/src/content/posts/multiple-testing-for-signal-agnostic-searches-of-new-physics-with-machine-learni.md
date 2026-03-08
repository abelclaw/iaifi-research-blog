---
abstract: In this work, we address the question of how to enhance signal-agnostic
  searches by leveraging multiple testing strategies. Specifically, we consider hypothesis
  tests relying on machine learning, where model selection can introduce a bias towards
  specific families of new physics signals. We show that it is beneficial to combine
  different tests, characterised by distinct choices of hyperparameters, and that
  performances comparable to the best available test are generally achieved while
  providing a more uniform response to various types of anomalies. Focusing on the
  New Physics Learning Machine, a methodology to perform a signal-agnostic likelihood-ratio
  test, we explore a number of approaches to multiple testing, such as combining p-values
  and aggregating test statistics.
arxivId: '2408.12296'
arxivUrl: https://arxiv.org/abs/2408.12296
authors:
- Gaia Grosso
- Marco Letizia
concepts:
- hypothesis testing
- multiple testing
- likelihood ratio
- new physics searches
- anomaly detection
- kernel methods
- goodness-of-fit testing
- p-value combination
- ensemble methods
- collider physics
- uncertainty quantification
figures:
- /iaifi-research-blog/figures/2408_12296/figure_1.png
- /iaifi-research-blog/figures/2408_12296/figure_1.png
- /iaifi-research-blog/figures/2408_12296/figure_2.png
- /iaifi-research-blog/figures/2408_12296/figure_2.png
- /iaifi-research-blog/figures/2408_12296/figure_3.png
- /iaifi-research-blog/figures/2408_12296/figure_3.png
pdfUrl: https://arxiv.org/pdf/2408.12296v1
published: '2024-08-22T11:14:37+00:00'
theme: Experimental Physics
title: Multiple testing for signal-agnostic searches of new physics with machine learning
wordCount: 1141
---

## The Big Picture

Imagine searching for a counterfeit coin hidden in a massive vault. You could deploy one detector tuned to catch gold fakes — but what if the forger used platinum? You'd walk right past it. The smarter strategy: deploy multiple detectors, each calibrated differently, and combine their reports. If *any* of them flags an anomaly, you investigate.

That's the challenge facing physicists hunting for new physics at the Large Hadron Collider. The Standard Model — our best description of the subatomic world — has withstood decades of experimental scrutiny. But theorists are increasingly without a roadmap for what comes next. No dark matter signal, no supersymmetric mirror particles, no obvious pointer.

Experimentalists must therefore search without a predetermined target, scanning collision data for *any* deviation from Standard Model expectations.

Machine learning has emerged as a powerful ally in this hunt. But it carries a hidden trap: the design of any machine learning model quietly bakes in assumptions about what kind of anomaly you're looking for. Researchers Gaia Grosso and Marco Letizia now show that deploying *multiple* machine learning tests simultaneously and combining their outputs sidesteps this trap, producing a more uniformly powerful search.

> **Key Insight:** No single machine learning model is equally sensitive to all possible new physics signals. Running several tests with different hyperparameters and combining their results achieves performance close to the *best* individual test — without having to know in advance which test that is.

## How It Works

The core framework is the **New Physics Learning Machine (NPLM)**, a signal-agnostic hypothesis testing methodology. The setup: you have two datasets — a *reference sample* (simulating Standard Model collisions) and a *data sample* (actual experimental measurements). NPLM asks one statistical question: are these two populations drawn from the same underlying distribution?

To answer it, NPLM trains a model based on **kernel methods** — a technique that builds a flexible mathematical picture of the data by comparing each measurement to its neighbors, weighting contributions by distance — to estimate the **likelihood ratio** between the data and the reference. The likelihood ratio measures how much more probable the observed data would be under a new-physics scenario than under the Standard Model alone.

If the Standard Model is correct, the likelihood ratio should be flat. If new physics is lurking, the model learns a nontrivial deformation, producing a large **test statistic** — a number summarizing how different the two datasets look — that translates into a small **p-value**, the probability of seeing a discrepancy this large purely by chance. A small enough p-value becomes a potential discovery claim.

![Figure 1](/iaifi-research-blog/figures/2408_12296/figure_1.png)

The problem arises during **model selection** — choosing the kernel's bandwidth (how broadly the model peers at each data point), regularization strength (a penalty against overfitting), and other settings. Different choices make the model sensitive to different signals. A narrow kernel catches sharp localized resonances but misses broad spectral distortions. A wide kernel does the opposite. In a real search, you don't know which setting is best — because you don't know what new physics looks like.

Grosso and Letizia's solution: don't pick. Run many versions of the test, each with a different combination of settings, and combine their outputs. They explore several strategies:

- **Combining p-values** — using classical methods (Fisher's, Stouffer's, minimum p-value) to merge significance levels from each test into one global p-value
- **Aggregating test statistics** — directly averaging or taking the maximum across all runs before computing a single p-value
- **Correcting for the look-elsewhere effect** — calibrating the combined statistic against its null distribution to prevent multiple tests from inflating the false positive rate

![Figure 2](/iaifi-research-blog/figures/2408_12296/figure_1.png)

That last point is crucial. Running 20 tests instead of 1 naively makes you 20 times more likely to flag noise as a discovery. The combined test statistic is compared against its distribution *under the null hypothesis* — assuming the Standard Model is exactly right, with thresholds computed empirically — so the false positive rate stays properly controlled. You get the sensitivity benefits of multiple probes without sacrificing statistical rigor.

![Figure 3](/iaifi-research-blog/figures/2408_12296/figure_2.png)

In numerical experiments, the authors tested their framework against a range of synthetic anomalies — sharp resonances, broad excesses, rate deviations — and compared the combined tests to individual ones. The result: the combined approach reliably matches or approaches the performance of the *best* individual test for each signal type, while no single test dominates across all signal types. The combination is a generalist; each individual test is a specialist. And since you don't know which specialist to call, the generalist wins.

![Figure 4](/iaifi-research-blog/figures/2408_12296/figure_2.png)

## Why It Matters

Particle physics is entering an era of increasingly ambitious model-independent searches, driven by the absence of clear theoretical targets and the growing maturity of machine learning tools. But "model-independent" has always been a slight misnomer — every algorithm carries implicit assumptions, and kernel methods are no exception.

The multiple testing framework offers a principled, statistically controlled way to soften those assumptions. The authors connect their approach to recent work on **Maximum Mean Discrepancy** tests — a technique for comparing two distributions by measuring the average gap between them — suggesting that multiple testing strategies could become standard toolkit items for signal-agnostic searches across high-energy physics.

The combination methods explored here, particularly aggregating test statistics with proper null calibration, are simple enough to slot into existing analysis pipelines.

![Figure 5](/iaifi-research-blog/figures/2408_12296/figure_3.png)

Open questions remain: how to optimally weight tests with different expected sensitivities, whether adaptive methods focusing on promising hyperparameter regions outperform uniform grids, and how the approach scales to the high-dimensional feature spaces of modern LHC analyses. But the framework is already practical, and the authors have released code to reproduce their results.

> **Bottom Line:** By running many versions of a machine learning anomaly detector with different hyperparameters and combining their outputs, physicists can achieve robust, near-optimal sensitivity to new physics signals — without guessing what those signals look like in advance. This is a practical, statistically principled step toward genuinely model-independent searches at the LHC and beyond.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges statistical machine learning and experimental particle physics, applying multiple testing theory — a classical statistics tool — to signal-agnostic new physics searches powered by kernel-based ML models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Combining outputs from multiple ML models with different hyperparameters, rather than selecting a single model, produces more robust and uniformly sensitive anomaly detection — a lesson applicable broadly to ML-driven scientific discovery.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By reducing the implicit model-dependence introduced by hyperparameter choices, the framework strengthens the case for genuinely agnostic searches for Beyond the Standard Model physics at collider experiments like the LHC.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will explore adaptive hyperparameter weighting and extension to higher-dimensional collider observables; the paper and code are available on arXiv and at `github.com/mletizia/multiple-testing-nplm`.</span></div></div>
</div>
