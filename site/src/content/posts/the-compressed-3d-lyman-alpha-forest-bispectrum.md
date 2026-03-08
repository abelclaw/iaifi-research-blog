---
abstract: Cosmological studies of the Lyman-Alpha (Lya) forest typically constrain
  parameters using two-point statistics. However, higher-order statistics, such as
  the three-point function (or its Fourier counterpart, the bispectrum) offer additional
  information and help break the degeneracy between the mean flux and power spectrum
  amplitude, albeit at a significant computational cost. To address this, we extend
  an existing highly informative compression of the bispectrum, the skew spectra,
  to the Lya forest. We derive the tree-level bispectrum of Lya forest fluctuations
  in the framework of effective field theory (EFT) directly in redshift space and
  validate our methodology on synthetic Lya forest data. We measure the anisotropic
  cross-spectra between the transmitted flux fraction and all quadratic operators
  arising in the bispectrum, yielding a set of 26 skew spectra. Using idealized 3D
  Gaussian smoothing (R=10 Mpc/h), we find good agreement (1-2 sigma level based on
  the statistical errors of the mocks) with the theoretical tree-level bispectrum
  prediction for monopole and quadrupole up to k <= 0.17 h/Mpc. To enable the cosmological
  analysis of Lya forest data from the currently observing Dark Energy Spectroscopic
  Instrument (DESI), where we cannot do 3D smoothing, we use a line-of-sight smoothing
  and introduce a new statistic, the shifted skew spectra. These probe non-squeezed
  bispectrum triangles and avoid locally applying quadratic operators to the field
  by displacing one copy of the field in the radial direction. Using a fixed displacement
  of 40 Mpc/h (and line-of-sight smoothing of 10 Mpc/h) yields a similar agreement
  with the theory prediction. For the special case of correlating the squared (and
  displaced) field with the original one, we analytically forward model the window
  function making this approach readily applicable to DESI data.
arxivId: '2510.23597'
arxivUrl: https://arxiv.org/abs/2510.23597
authors:
- Roger de Belsunce
- James M. Sullivan
- Patrick McDonald
concepts:
- skew spectra
- lyman-alpha forest
- effective field theory
- spectral methods
- shifted skew spectra
- cosmological simulation
- surrogate modeling
- dark energy
- bayesian inference
- monte carlo methods
- simulation-based inference
figures:
- /iaifi-research-blog/figures/2510_23597/figure_1.png
- /iaifi-research-blog/figures/2510_23597/figure_1.png
- /iaifi-research-blog/figures/2510_23597/figure_2.png
- /iaifi-research-blog/figures/2510_23597/figure_2.png
- /iaifi-research-blog/figures/2510_23597/figure_3.png
- /iaifi-research-blog/figures/2510_23597/figure_3.png
pdfUrl: https://arxiv.org/pdf/2510.23597v1
published: '2025-10-27T17:58:09+00:00'
theme: Theoretical Physics
title: The Compressed 3D Lyman-Alpha Forest Bispectrum
wordCount: 1148
---

## The Big Picture

Imagine trying to understand the structure of a distant city by listening to echoes. Each echo carries information, but a single echo tells you far less than comparing multiple echoes together. That's roughly the situation cosmologists face when studying the **Lyman-alpha forest**: the ghostly imprint of hydrogen gas scattered across billions of light-years, recorded as a distinctive pattern of dark absorption lines in the light from quasars — some of the brightest objects in the universe.

For decades, astronomers have extracted cosmic information from the Lyman-alpha forest by measuring how pairs of points in the signal relate to each other. This is powerful, but incomplete. Gravity has sculpted the cosmic web into filaments, voids, and clusters — complex patterns that pairwise comparisons cannot capture.

To unlock this hidden information, researchers need statistics that compare three or more points at a time, sensitive to the shapes and asymmetries baked into cosmic structure. The most important of these is the **bispectrum**, the three-point analog of the **power spectrum** (which measures how strongly the signal fluctuates at different scales). The catch: computing the full bispectrum is computationally brutal, depending on the shape of every possible triangle you can draw between three points in the signal — orders of magnitude more expensive than the power spectrum.

Now, a team from MIT, UC Berkeley, and Lawrence Berkeley National Laboratory has found a shortcut. By extending a clever compression technique called **skew spectra** to the three-dimensional Lyman-alpha forest, they've built a practical pathway to extracting bispectrum information from current and future surveys — including DESI, which is collecting quasar spectra right now.

> **Key Insight:** Skew spectra compress the bispectrum into a set of cross-power spectra that depend on only a single wavenumber — nearly as cheap to compute as the power spectrum itself — while retaining most of the cosmological information the full bispectrum provides.

## How It Works

The core idea is elegant: instead of computing the bispectrum directly, you compute **cross-spectra** — measurements of how two different versions of the signal correlate with each other — between the original field and a set of quadratic operators applied to that field. These cross-spectra capture how squared or mixed combinations of the field correlate with the field itself, which is exactly the non-Gaussian signal the bispectrum measures.

For the Lyman-alpha forest, the relevant quantity is the **transmitted flux fraction** — how much quasar light passes through the hydrogen gas at each point. The researchers:

1. Derived the **tree-level bispectrum** — the leading-order three-point statistic, valid on large scales where fluctuations are small — using the **Effective Field Theory of Large-Scale Structure (EFT-LSS)**, a rigorous perturbative framework grounded in symmetry principles.
2. Worked directly in **redshift space**, accounting for the fact that gas velocities distort apparent positions along the line of sight — a phenomenon called **redshift-space distortions**.
3. Identified all quadratic operators in the bispectrum expansion and measured cross-spectra between each and the original flux field, yielding **26 skew spectra**.

![Figure 1](/iaifi-research-blog/figures/2510_23597/figure_1.png)

The theory is validated against two mock datasets. The first uses synthetic 3D Lyman-alpha fields generated with second-order perturbation theory — a controlled test where the theory is known to apply. The second uses large-volume mocks built from **AbacusSummit**, a state-of-the-art suite of N-body simulations that accurately models gravitational clustering across cosmic time.

With idealized three-dimensional Gaussian smoothing at R = 10 Mpc/h, the team finds good agreement — at the 1–2 sigma level — between theoretical predictions and measured skew spectra for both the monopole and quadrupole multipoles, up to k ≤ 0.17 h/Mpc.

![Figure 3](/iaifi-research-blog/figures/2510_23597/figure_2.png)

There's a crucial complication for real data. The Lyman-alpha forest is observed as individual one-dimensional spectra along lines of sight to quasars, not as a fully sampled three-dimensional volume. DESI, which will collect up to one million quasar spectra over its lifetime, cannot apply standard 3D smoothing. So the team invented a new variant: **shifted skew spectra**.

## The Shifted Solution

Instead of squaring the field locally, shifted skew spectra displace one copy of the field in the radial (line-of-sight) direction before computing the product. This fixed displacement — 40 Mpc/h — allows the statistic to probe **non-squeezed bispectrum triangles** (where all three sides have comparable length) while requiring only line-of-sight smoothing at 10 Mpc/h.

![Figure 5](/iaifi-research-blog/figures/2510_23597/figure_3.png)

For the key case of correlating the squared-and-displaced field with the original field, the team derives an **analytic window function treatment** — essential for applying any statistic to real survey data with irregular geometry and completeness masks. This forward modeling makes the shifted skew spectra directly applicable to DESI data without approximation.

The results are striking: even with conservative line-of-sight-only smoothing, the new statistic achieves agreement with theoretical predictions comparable to the idealized 3D case.

![Figure 4](/iaifi-research-blog/figures/2510_23597/figure_2.png)

## Why It Matters

The Lyman-alpha forest occupies a unique cosmological sweet spot. It probes redshifts z = 2–5 — an epoch when the universe was actively building its large-scale structure, but perturbation theory still works. Galaxy surveys struggle to reach these redshifts; the Lyman-alpha forest does not.

Higher-order statistics like the bispectrum can break degeneracies that hamper two-point analyses. The mean flux of the forest and the power spectrum amplitude are notoriously hard to separate using the power spectrum alone — but the bispectrum responds differently to each. Skew spectra provide a practical route to exploiting this.

With DESI currently taking data and future surveys like WEAVE-QSO, the Prime Focus Spectrograph, and 4MOST on the horizon, the cosmological community is entering an era of data abundance. The compressed bispectrum framework developed here positions the field to extract non-Gaussian information from these surveys at minimal computational cost. Beyond Lyman-alpha, the underlying methodology — EFT-based bispectrum compression via skew spectra — continues to prove its versatility across different tracers of large-scale structure.

> **Bottom Line:** By deriving 26 skew spectra from the Lyman-alpha forest bispectrum and validating them against realistic N-body simulations, this work opens a practical, computationally affordable route to extracting non-Gaussian cosmological information from DESI and future surveys.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges theoretical cosmology and observational data science by building an analytic EFT framework — grounded in fundamental physics symmetries — that is directly deployable on the world's largest ongoing spectroscopic survey.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The skew spectrum compression strategy exemplifies a broader data science principle: rather than computing expensive full statistics, identify low-dimensional projections that preserve the most information — an approach with direct applications in scientific machine learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Extending higher-order statistics to the three-dimensional Lyman-alpha forest creates new tools for probing neutrino masses, dark matter properties, and primordial non-Gaussianity at redshifts inaccessible to current galaxy surveys.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The analytic window function treatment makes shifted skew spectra immediately applicable to DESI data, with extensions to future Stage-V spectroscopic surveys planned; the full methodology is detailed in arXiv:2503.03812.</span></div></div>
</div>
