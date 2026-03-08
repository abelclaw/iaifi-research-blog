---
abstract: The influx of massive amounts of data from current and upcoming cosmological
  surveys necessitates compression schemes that can efficiently summarize the data
  with minimal loss of information. We introduce a method that leverages the paradigm
  of self-supervised machine learning in a novel manner to construct representative
  summaries of massive datasets using simulation-based augmentations. Deploying the
  method on hydrodynamical cosmological simulations, we show that it can deliver highly
  informative summaries, which can be used for a variety of downstream tasks, including
  precise and accurate parameter inference. We demonstrate how this paradigm can be
  used to construct summary representations that are insensitive to prescribed systematic
  effects, such as the influence of baryonic physics. Our results indicate that self-supervised
  machine learning techniques offer a promising new approach for compression of cosmological
  data as well its analysis.
arxivId: '2308.09751'
arxivUrl: https://arxiv.org/abs/2308.09751
authors:
- Aizhan Akhmetzhanova
- Siddharth Mishra-Sharma
- Cora Dvorkin
concepts:
- self-supervised learning
- representation learning
- simulation-based augmentation
- simulation-based inference
- dimensionality reduction
- contrastive learning
- cosmological simulation
- posterior estimation
- data augmentation
- robustness
- surrogate modeling
- dark energy
figures:
- /iaifi-research-blog/figures/2308_09751/figure_1.png
- /iaifi-research-blog/figures/2308_09751/figure_1.png
- /iaifi-research-blog/figures/2308_09751/figure_2.png
- /iaifi-research-blog/figures/2308_09751/figure_2.png
- /iaifi-research-blog/figures/2308_09751/figure_3.png
- /iaifi-research-blog/figures/2308_09751/figure_3.png
pdfUrl: https://arxiv.org/pdf/2308.09751v2
published: '2023-08-18T18:00:22+00:00'
theme: Astrophysics
title: Data Compression and Inference in Cosmology with Self-Supervised Machine Learning
wordCount: 1100
---

## The Big Picture

Imagine trying to study the entire ocean by collecting water samples — but instead of a few jars, you have a firehose pumping petabytes of data every day. That's the situation cosmologists face with the next generation of sky surveys. Instruments like the Vera C. Rubin Observatory and the Dark Energy Spectroscopic Instrument (DESI) will map hundreds of millions of galaxies, generating datasets so vast that traditional compression methods strain under the load.

The problem isn't just data volume — it's about what you keep when you compress. Discard the wrong information and your measurement of dark energy or the neutrino mass becomes blurry. Keep too much and your analysis pipeline bogs down under computational weight.

Cosmologists have long relied on hand-crafted "summary statistics" — things like power spectra, which map how matter clumps together at different cosmic scales — but these are only as good as the human intuition that designed them. They almost certainly leave something on the table.

Researchers Aizhan Akhmetzhanova, Siddharth Mishra-Sharma, and Cora Dvorkin at Harvard and MIT have shown that a technique from modern AI — self-supervised machine learning — can automatically discover compact, information-rich summaries, and do so in a way that's robust to messy astrophysical contamination.

> **Key Insight:** By treating different simulations of the same universe as "views" of the same underlying reality, the team trained a neural network to compress cosmological maps into tight summary representations — without ever needing labeled training data — and the resulting summaries rival or beat traditional hand-crafted statistics.

## How It Works

The backbone of the method is **self-supervised learning**, a training paradigm in which a model learns by finding structure in unlabeled data rather than being fed explicit answers. Think of it like learning to recognize faces not from a labeled photo album, but by noticing that two photos taken seconds apart in different lighting should look similar — they show the same person, after all.

In cosmology, the equivalent of "two photos of the same person" is two simulations that share the same cosmological parameters (like the matter density Ω_m or the amplitude of fluctuations σ_8) but differ in their **baryonic physics** — the messy details of how gas, stars, and black holes behave inside galaxies. These differences are like lighting changes: real, but irrelevant to the underlying cosmology you're trying to measure.

![Figure 1](/iaifi-research-blog/figures/2308_09751/figure_1.png)

The team used a specific self-supervised algorithm called **VICReg** (Variance-Invariance-Covariance Regularization), which trains a neural network encoder to satisfy three objectives simultaneously:

- **Invariance**: Maps with the same cosmological parameters should produce similar summary vectors, regardless of baryonic details
- **Variance**: The summaries should spread out and use all available dimensions — no collapsed, uninformative representations
- **Covariance**: Different dimensions of the summary should carry independent information, not redundant copies

The data comes from the **CAMELS cosmological simulation suite**, a library of thousands of simulated universe snapshots spanning a grid of cosmological and astrophysical parameters. Each simulation produces a matter density map — a 2D or 3D snapshot of how mass is distributed across a patch of cosmic volume. Pairs of CAMELS simulations with matched cosmological parameters but different astrophysical parameters serve as positive training pairs: the cosmological analogue of "same face, different lighting."

![Figure 2](/iaifi-research-blog/figures/2308_09751/figure_1.png)

The compressed output is a low-dimensional vector — a handful of numbers — fed into a **simulation-based inference (SBI)** pipeline, a method for estimating parameter ranges without requiring an explicit mathematical formula for the likelihood of the data. The results are striking: the self-supervised summaries match or exceed a fully supervised neural network trained with explicit parameter labels, and dramatically outperform traditional power spectrum statistics.

![Figure 4](/iaifi-research-blog/figures/2308_09751/figure_2.png)

Perhaps most impressive is the method's robustness to systematics. By designing augmentations around baryonic variations, the team trained a version of the model that is nearly blind to astrophysical contamination. When supernova and AGN (active galactic nuclei — energetic winds driven by supermassive black holes at galaxy centers) feedback parameters were deliberately varied, the baryonic-invariant summaries barely flinched while still recovering cosmological parameters accurately. That's the equivalent of learning to see the skeleton of the universe through all the messy astrophysics layered on top.

## Why It Matters

Simulation-based inference has emerged as one of the most promising frameworks for next-generation cosmological analysis, because it sidesteps the need to write down an explicit likelihood function — a task that becomes essentially impossible when data is complex and non-Gaussian. But SBI's Achilles heel is the curse of dimensionality: the more numbers you feed it, the more simulations you need. Good compression isn't just convenient — it's existentially necessary.

Self-supervised methods offer compression schemes that scale with data complexity, can be deployed across diverse data types (density maps today, weak lensing shear fields or 21-cm maps tomorrow), and adapt in ways hand-crafted statistics never can. The simulation-based augmentation strategy is particularly elegant: compression is automatically informed by whatever systematics are included in the simulation library, with no new labels or manual feature engineering required. As simulation suites grow more sophisticated, the method effectively grows smarter with them.

Open questions remain. The current demonstrations use 2D projected maps; extending to full 3D cosmic volumes increases both the potential information gain and the computational challenge. The method also inherits whatever limitations exist in the underlying simulations — if the simulations miss important physics, the learned summaries may too. Bridging self-supervised compression with likelihood-free inference at survey scale will require careful validation on real observational data, not just simulations.

> **Bottom Line:** Self-supervised machine learning can automatically discover compressed cosmological summaries that are as informative as human-designed statistics — and far more systematic in handling astrophysical contamination — pointing toward a scalable, flexible framework for analyzing the next generation of cosmological surveys.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work pioneers contrastive self-supervised learning — a technique from computer vision — as a principled, physics-informed tool for cosmological data compression, directly connecting AI methodology to fundamental questions about the structure of the universe.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The team's simulation-based augmentation strategy offers a novel recipe for self-supervised learning in scientific domains where physical symmetries and model variations, rather than image transforms, define meaningful "views" of the data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling precise, systematic-robust inference of cosmological parameters from massive survey datasets, the method advances our ability to constrain dark matter, dark energy, and neutrino mass from upcoming experiments like Euclid and LSST.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work targets full 3D density fields, real observational data, and integration with sequential SBI pipelines; the paper is available at arXiv:2310.07042.</span></div></div>
</div>
