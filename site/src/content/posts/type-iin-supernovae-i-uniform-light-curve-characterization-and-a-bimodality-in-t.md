---
abstract: 'We present the largest uniform study to date of Type IIn supernovae (SNe
  IIn), focusing in this first paper on the multi-band optical light curves of $487$
  SNe IIn. The sample, constructed from multiple surveys, extends to $z \approx 0.8$,
  with the majority of events at $z \lesssim 0.3$. We construct uniform multi-band
  and bolometric light curves using Gaussian process regression, and determine key
  observed properties in the rest-frame (e.g., peak luminosity, timescales, radiated
  energy). We find that SNe IIn span broad ranges in peak luminosity ($\sim 10^{42}-10^{44}$
  erg s$^{-1}$) and timescales ($\sim 20-300$ days above 50% of peak luminosity),
  but the sample divides into two clear groups in the luminosity-timescale phase-space
  around the median peak luminosity ($\approx 10^{43}$ erg s$^{-1}$): faint-fast and
  luminous-slow groups. This leads to a strong bimodality in the radiated energy distribution,
  with peaks at $\sim 10^{49}$ and $\sim 2\times10^{50}$ erg, with the latter events
  having a characteristic timescale of $\sim 100$ days, and the former appearing to
  bifurcate into two branches with timescales of $\sim 40$ and $\sim 70$ days. Therefore,
  SNe IIn exhibit at least two dominant groupings, and perhaps three, which are likely
  reflective of different progenitor and/or circumstellar medium formation pathways.
  We do not find any obvious transition in SN IIn properties at the arbitrary cut-off
  of $\approx -20$ mag used for the designation "Type II Superluminous Supernovae",
  and we argue that this classification should be abandoned. The absence of SNe IIn
  with timescales of $\lesssim 14$ days defines the region occupied by fast transients
  with evidence for interaction with hydrogen-poor circumstellar medium.'
arxivId: '2411.07287'
arxivUrl: https://arxiv.org/abs/2411.07287
authors:
- Daichi Hiramatsu
- Edo Berger
- Sebastian Gomez
- Peter K. Blanchard
- Harsh Kumar
- Wasundara Athukoralalage
concepts:
- supernova classification
- bimodal energy distribution
- circumstellar interaction
- regression
- photometric survey analysis
- clustering
- stochastic processes
- stellar evolution
- hypothesis testing
- anomaly detection
figures:
- /iaifi-research-blog/figures/2411_07287/figure_1.png
- /iaifi-research-blog/figures/2411_07287/figure_1.png
- /iaifi-research-blog/figures/2411_07287/figure_2.png
- /iaifi-research-blog/figures/2411_07287/figure_2.png
- /iaifi-research-blog/figures/2411_07287/figure_3.png
- /iaifi-research-blog/figures/2411_07287/figure_3.png
pdfUrl: https://arxiv.org/pdf/2411.07287v1
published: '2024-11-11T19:00:01+00:00'
theme: Astrophysics
title: Type IIn Supernovae. I. Uniform Light Curve Characterization and a Bimodality
  in the Radiated Energy Distribution
wordCount: 976
---

## The Big Picture

Imagine sorting a pile of fireworks by brightness and burn time. Most would cluster naturally — quick sparklers on one end, long-lasting roman candles on the other. Now imagine discovering that the universe's most dramatic stellar explosions follow the same pattern, hidden in plain sight for decades.

Type IIn supernovae (SNe IIn) are among the most spectacular stellar deaths in the cosmos. Unlike typical supernovae, which fade as expanding debris cools, SNe IIn are powered by collision — the explosion slams into dense gas the star shed before it died, converting kinetic energy into brilliant light.

Their telltale signature is "narrow" hydrogen lines in their spectra: slow-moving gas surrounding the dying star that hasn't yet been swept up by the blast. What baffles astronomers is the sheer variety. Some IIn supernovae outshine entire galaxies for months; others flicker and fade in weeks. Why?

A team from the Center for Astrophysics at Harvard & Smithsonian and IAIFI has assembled the largest uniform study of these events ever attempted — 487 confirmed SNe IIn — and found that this apparent chaos has hidden structure. The explosions don't vary randomly. They fall into distinct groups, suggesting nature has only a few preferred ways to make a Type IIn supernova.

> **Key Insight:** Type IIn supernovae exhibit a strong bimodality in radiated energy, splitting into at least two — and possibly three — distinct populations that likely reflect fundamentally different stellar progenitors and mass-loss histories.

## How It Works

The challenge was data quality. Supernova surveys produce light curves measured in different filters, at different cadences, from different telescopes. Combining them into a coherent sample requires careful standardization — otherwise you're comparing apples to oranges across cosmic distances.

The team solved this with **Gaussian process regression (GPR)**, a statistical technique that fits smooth, flexible curves through noisy, irregularly-sampled data without assuming a fixed functional form. Think of it as drawing the most natural-looking curve through a scatter of points while rigorously tracking uncertainty. Applied across all 487 events, GPR allowed the team to reconstruct consistent **bolometric light curves** — total energy output across all wavelengths — and extract reliable measurements of peak luminosity, duration, and total radiated energy for each explosion.

![Figure 1](/iaifi-research-blog/figures/2411_07287/figure_1.png)

The sample spanned multiple surveys from 2016–2023, reaching redshift z ≈ 0.8 (roughly 7 billion light-years). Every candidate was spectroscopically verified — each explosion's light broken into individual wavelengths and checked against the IIn fingerprint. Sixty-five imposters with broad hydrogen lines were filtered out, leaving a clean, uniformly characterized dataset unlike anything previously available.

The results were striking. When plotted in peak luminosity versus timescale space, the 487 SNe IIn divided cleanly into two camps around a median peak luminosity of ~10⁴³ erg/s (about 10 billion times the Sun's total output):

- **Faint-fast events**: lower luminosity, shorter durations (~20–100 days at half-peak brightness)
- **Luminous-slow events**: higher luminosity, longer durations often exceeding 100 days

![Figure 2](/iaifi-research-blog/figures/2411_07287/figure_1.png)

This separation translates into a dramatic **bimodality in radiated energy**. The faint-fast group radiates roughly 10⁴⁹ ergs total; the luminous-slow group radiates about 2×10⁵⁰ ergs — twenty times more. Intriguingly, the faint-fast group itself may split into two sub-branches with characteristic timescales of ~40 and ~70 days, suggesting at least three distinct flavors of Type IIn supernovae.

![Figure 3](/iaifi-research-blog/figures/2411_07287/figure_2.png)

## Why It Matters

The bimodality isn't a statistical curiosity — it's a physical fingerprint. A luminous blue variable — a massive, unstable star prone to dramatic eruptions — that erupted repeatedly in its final centuries would leave behind a thick shell of gas, producing long-duration, high-luminosity interaction. A more modest red supergiant shedding wind-driven mass would produce a thinner cocoon and a shorter, fainter event.

The clear groupings suggest that IIn supernovae don't arise from a continuous distribution of stellar properties, but from a small number of distinct progenitor pathways — only a handful of stellar life histories lead to this type of explosion.

The team also delivers a pointed challenge to existing classification conventions. Astronomers have long labeled events brighter than roughly –20 magnitudes as "Type II Superluminous Supernovae" (SLSNe-II) — a threshold roughly equivalent to outshining a small galaxy. But the new data show no physical discontinuity there. Bright and faint populations blend continuously across that line, making the cutoff arbitrary. The authors argue this classification should be abandoned, a provocative but well-supported position that will likely reshape how the community catalogs these events.

The absence of any IIn events with timescales shorter than ~14 days is equally significant, cleanly demarcating the boundary between IIn supernovae and the separate class of fast transients interacting with hydrogen-poor gas.

> **Bottom Line:** The largest uniform survey of Type IIn supernovae reveals a striking bimodality in radiated energy — these explosions fall into at least two distinct groups, exposing hidden structure in one of astronomy's most chaotic stellar death categories and pointing toward a small number of preferred progenitor channels in nature.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work demonstrates how statistical machine learning tools like Gaussian process regression, applied uniformly at scale, can reveal physical structure in messy, heterogeneous astronomical datasets — bridging data science methodology with fundamental questions about stellar evolution.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">GPR enabled principled interpolation and uncertainty quantification across 487 sparsely and irregularly sampled multi-band light curves, showcasing how probabilistic ML methods handle real-world scientific data at population scale.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The discovery of a bimodal energy distribution in SNe IIn provides the clearest observational evidence to date that these explosions arise from distinct progenitor channels and circumstellar medium formation pathways, with direct implications for massive star physics and stellar mass loss.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future papers in this series will model individual events analytically, analyze CSM-shock interaction spectra, and study host galaxies to further constrain progenitor populations; the study is available at arXiv:2411.14181.</span></div></div>
</div>
