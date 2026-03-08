---
abstract: The nature of the Fermi gamma-ray Galactic Center Excess (GCE) has remained
  a persistent mystery for over a decade. Although the excess is broadly compatible
  with emission expected due to dark matter annihilation, an explanation in terms
  of a population of unresolved astrophysical point sources e.g., millisecond pulsars,
  remains viable. The effort to uncover the origin of the GCE is hampered in particular
  by an incomplete understanding of diffuse emission of Galactic origin. This can
  lead to spurious features that make it difficult to robustly differentiate smooth
  emission, as expected for a dark matter origin, from more "clumpy" emission expected
  for a population of relatively bright, unresolved point sources. We use recent advancements
  in the field of simulation-based inference, in particular density estimation techniques
  using normalizing flows, in order to characterize the contribution of modeled components,
  including unresolved point source populations, to the GCE. Compared to traditional
  techniques based on the statistical distribution of photon counts, our machine learning-based
  method is able to utilize more of the information contained in a given model of
  the Galactic Center emission, and in particular can perform posterior parameter
  estimation while accounting for pixel-to-pixel spatial correlations in the gamma-ray
  map. This makes the method demonstrably more resilient to certain forms of model
  misspecification. On application to Fermi data, the method generically attributes
  a smaller fraction of the GCE flux to unresolved point sources when compared to
  traditional approaches. We nevertheless infer such a contribution to make up a non-negligible
  fraction of the GCE across all analysis variations considered, with at least $38^{+9}_{-19}\%$
  of the excess attributed to unresolved point sources in our baseline analysis.
arxivId: '2110.06931'
arxivUrl: https://arxiv.org/abs/2110.06931
authors:
- Siddharth Mishra-Sharma
- Kyle Cranmer
concepts:
- simulation-based inference
- normalizing flows
- density estimation
- posterior estimation
- bayesian inference
- dark matter
- graph neural networks
- feature extraction
- uncertainty quantification
- model misspecification robustness
- signal detection
- monte carlo methods
- inverse problems
figures:
- /iaifi-research-blog/figures/2110_06931/figure_1.png
- /iaifi-research-blog/figures/2110_06931/figure_2.png
pdfUrl: https://arxiv.org/pdf/2110.06931v2
published: '2021-10-13T18:00:00+00:00'
theme: Astrophysics
title: A neural simulation-based inference approach for characterizing the Galactic
  Center $γ$-ray excess
wordCount: 1042
---

## The Big Picture

Picture yourself trying to figure out whether a distant city's glow at night comes from streetlights or scattered bonfires, but you can only observe it through thick, unevenly lit fog. That's roughly the challenge astronomers face when decoding a puzzling blob of gamma-ray light from the center of our galaxy. The signal is real. What's causing it has sparked a decade of fierce debate.

The **Fermi Galactic Center Excess (GCE)** is an anomalous overabundance of high-energy photons, measured in gigaelectronvolts, detected by NASA's Fermi Large Area Telescope near the Milky Way's core. It matches what physicists would expect if dark matter particles were colliding and annihilating each other there.

But the signal could also be the collective whisper of thousands of **millisecond pulsars**, rapidly spinning neutron stars too faint to see individually, blending into an indistinguishable glow. The fog in the analogy is real too: patchy, poorly understood background radiation from the galaxy itself muddies every measurement.

Siddharth Mishra-Sharma and Kyle Cranmer developed a machine learning-powered method that wrings more information from gamma-ray maps than any previous approach and reached a surprising conclusion about how much of the excess could be hiding in millions of dim, unresolved point sources.

> **Key Insight:** By using neural networks to capture *spatial correlations* across the entire gamma-ray sky map, not just pixel-by-pixel statistics, the new method proves more resilient to systematic errors. It attributes a smaller but still significant fraction of the GCE to unresolved point sources than traditional analyses.

## How It Works

The traditional workhorse for this problem is the **1-point probability distribution function (1pPDF)**, a technique that examines the statistical distribution of photon counts in each pixel independently. It's like judging whether a painting was made by one artist or a hundred by examining each brushstroke in isolation, ignoring how strokes relate to each other. You capture something, but you discard structural information.

Mishra-Sharma and Cranmer instead turned to **simulation-based inference (SBI)**, a framework that learns to draw statistical conclusions by running thousands of simulations rather than deriving complex mathematical formulas by hand. The pipeline works in three stages:

1. **Forward model**: The team built a detailed simulator of the Galactic Center, modeling dark matter templates, point source populations with a realistic spread of brightnesses, Galactic diffuse emission, isotropic backgrounds, and more. Millions of random parameter combinations generated corresponding simulated gamma-ray skies.

2. **Neural summary statistics**: Rather than hand-crafting features, they fed 2D gamma-ray maps into a **graph neural network** (a neural network architecture designed for data spread across curved surfaces like the celestial sphere). This network compressed each map into a compact set of summary statistics optimized for the inference task.

3. **Normalizing flows**: These summaries trained a **normalizing flow**, a neural network that models complex probability distributions by transforming a simple distribution through a series of invertible steps. The output is a full **posterior distribution**: a complete picture of which parameter values are plausible given the observed data, along with their uncertainties.

![Figure 1](/iaifi-research-blog/figures/2110_06931/figure_1.png)

The real advantage over 1pPDF methods is that the neural network exploits *pixel-to-pixel spatial correlations*. Smooth dark matter emission and clumpy point-source emission don't just differ pixel by pixel. They differ in how neighboring pixels relate to each other. By capturing that structure, the method extracts information that simpler statistics throw away.

![Figure 2](/iaifi-research-blog/figures/2110_06931/figure_2.png)

The team validated their approach extensively on simulated data before touching real Fermi observations. One telling test: they deliberately injected known mismodeling (adding unaccounted point source populations or tweaking the galaxy's background glow) and measured how each method responded. The SBI approach held up far better. Its parameter estimates shifted much less under these deliberate distortions than the 1pPDF approach, which can mistake a mismodeled foreground for genuine point-source signal.

## Why It Matters

Applied to real Fermi data, the neural SBI method consistently attributes a *smaller* fraction of the GCE flux to unresolved point sources than traditional photon-count statistics. In the baseline analysis, at least **38⁺⁹₋₁₉% of the excess** comes from point sources. That's non-negligible, but it leaves substantial room for a smooth component that could be dark matter.

Traditional approaches often push this fraction higher, sometimes toward a predominantly point-source interpretation.


The stakes here are high. If the GCE is mostly unresolved pulsars, it tells us relatively little about dark matter. If a substantial smooth component remains after accounting for all astrophysical backgrounds, that's a genuine signal worth chasing. The new method suggests the smooth component may have been underestimated, though a point-source contribution cannot be ruled out. The debate isn't over; it's been sharpened.

Beyond this specific mystery, the methodology points toward something broader. Simulation-based inference with learned summary statistics is increasingly powerful wherever the likelihood function is unknown, complex, or too expensive to compute, and that description fits a huge swath of modern astrophysics and particle physics. Here, the ML-based approach proved not just more powerful than classical methods but more resilient against the systematic errors that have long plagued real astronomical data.

> **Bottom Line:** The Fermi Galactic Center Excess remains ambiguous, but a neural simulation-based inference approach finds less evidence for a point-source origin than traditional methods while proving more resistant to the foreground modeling errors that have clouded this debate for a decade.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits squarely at the intersection of machine learning methodology (normalizing flows and graph neural networks) and one of the most active open problems in dark matter astrophysics. It shows that ML can improve both the power and the reliability of astronomical inference.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Simulation-based inference with learned neural summary statistics outperformed hand-crafted statistical methods on real scientific data, advancing SBI as a practical tool for high-dimensional scientific inference problems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By providing more reliable constraints on the unresolved point-source fraction of the Galactic Center Excess, this analysis sharpens the observational case for or against dark matter annihilation as a contributor to the excess, directly informing the search for physics beyond the Standard Model.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend this framework to higher-dimensional parameter spaces and improved diffuse foreground models, with similar SBI pipelines applicable to other astrophysical anomalies; the full analysis is available at [arXiv:2110.06931](https://arxiv.org/abs/2110.06931).</span></div></div>
</div>
