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
wordCount: 1061
---

## The Big Picture

Imagine trying to understand the structure of a distant city by listening to echoes. A single echo tells you something, but comparing multiple echoes together tells you far more. That's roughly the situation cosmologists face when studying the **Lyman-alpha forest**: the imprint of hydrogen gas scattered across billions of light-years, recorded as a pattern of dark absorption lines in quasar spectra.

For decades, astronomers have extracted cosmic information from the Lyman-alpha forest by measuring how pairs of points in the signal relate to each other. Powerful, but incomplete. Gravity has sculpted the cosmic web into filaments, voids, and clusters, and pairwise comparisons can't capture these complex shapes.

Unlocking that hidden information requires statistics that compare three or more points at a time, sensitive to the asymmetries baked into cosmic structure. The most important is the **bispectrum**, the three-point analog of the **power spectrum** (which measures how strongly the signal fluctuates at different scales). The problem: computing the full bispectrum depends on the shape of every possible triangle you can draw between three points in the signal. That's orders of magnitude more expensive than the power spectrum.

A team from MIT, UC Berkeley, and Lawrence Berkeley National Laboratory has found a shortcut. By extending a compression technique called **skew spectra** to the three-dimensional Lyman-alpha forest, they've built a practical way to extract bispectrum information from current and future surveys, including DESI, which is collecting quasar spectra right now.

> **Key Insight:** Skew spectra compress the bispectrum into a set of cross-power spectra that depend on only a single wavenumber, nearly as cheap to compute as the power spectrum itself, while retaining most of the cosmological information the full bispectrum provides.

## How It Works

Instead of computing the bispectrum directly, you compute **cross-spectra** between the original field and a set of quadratic operators applied to that field. These cross-spectra capture how squared or mixed combinations of the field correlate with the field itself, which is exactly the non-Gaussian signal the bispectrum encodes.

For the Lyman-alpha forest, the relevant quantity is the **transmitted flux fraction**, how much quasar light passes through the hydrogen gas at each point. The researchers:

1. Derived the **tree-level bispectrum** (the leading-order three-point statistic, valid on large scales where fluctuations are small) using the **Effective Field Theory of Large-Scale Structure (EFT-LSS)**, a perturbative framework built on symmetry principles.
2. Worked directly in **redshift space**, accounting for gas velocities that distort apparent positions along the line of sight, a phenomenon called **redshift-space distortions**.
3. Identified all quadratic operators in the bispectrum expansion and measured cross-spectra between each and the original flux field, yielding **26 skew spectra**.

![Figure 1](figure:1)

The theory is validated against two mock datasets. The first uses synthetic 3D Lyman-alpha fields generated with second-order perturbation theory, a controlled test where the theory is known to apply. The second uses large-volume mocks built from **AbacusSummit**, a suite of N-body simulations that accurately models gravitational clustering across cosmic time.

With idealized three-dimensional Gaussian smoothing at R = 10 Mpc/h, the team finds agreement at the 1–2 sigma level between theoretical predictions and measured skew spectra for both the monopole and quadrupole multipoles, up to k ≤ 0.17 h/Mpc.

![Figure 3](figure:3)

But real data introduces a complication. The Lyman-alpha forest is observed as individual one-dimensional spectra along lines of sight to quasars, not as a fully sampled three-dimensional volume. DESI will collect up to one million quasar spectra over its lifetime, but standard 3D smoothing can't be applied. So the team invented a new variant: **shifted skew spectra**.

## The Shifted Solution

Instead of squaring the field locally, shifted skew spectra displace one copy of the field in the radial (line-of-sight) direction before computing the product. A fixed displacement of 40 Mpc/h lets the statistic probe **non-squeezed bispectrum triangles** (where all three sides have comparable length) while requiring only line-of-sight smoothing at 10 Mpc/h.

![Figure 5](figure:5)

For the case of correlating the squared-and-displaced field with the original field, the team derives an **analytic window function treatment**, essential for applying any statistic to real survey data with irregular geometry and completeness masks. This forward modeling makes the shifted skew spectra directly applicable to DESI data without approximation.

Even with conservative line-of-sight-only smoothing, the new statistic achieves agreement with theoretical predictions comparable to the idealized 3D case.

![Figure 4](figure:4)

## Why It Matters

The Lyman-alpha forest occupies a unique cosmological sweet spot. It probes redshifts z = 2–5, an epoch when the universe was actively building its large-scale structure but perturbation theory still works. Galaxy surveys struggle to reach these redshifts. The Lyman-alpha forest does not.

Higher-order statistics like the bispectrum can break degeneracies that plague two-point analyses. The mean flux of the forest and the power spectrum amplitude are notoriously hard to separate using the power spectrum alone, but the bispectrum responds differently to each. Skew spectra give us a computationally affordable way in.

With DESI currently taking data and future surveys like WEAVE-QSO, the Prime Focus Spectrograph, and 4MOST on the horizon, the field is entering an era of data abundance. The compressed bispectrum framework developed here positions cosmologists to extract non-Gaussian information from these surveys at minimal computational cost. The underlying methodology (EFT-based bispectrum compression via skew spectra) also applies naturally to other tracers of large-scale structure.

> **Bottom Line:** By deriving 26 skew spectra from the Lyman-alpha forest bispectrum and validating them against N-body simulations, this work opens a computationally affordable route to extracting non-Gaussian cosmological information from DESI and future surveys.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects theoretical cosmology and observational data science by building an analytic EFT framework, grounded in fundamental physics symmetries, that is directly deployable on the world's largest ongoing spectroscopic survey.

- **Impact on Artificial Intelligence:** The skew spectrum compression strategy illustrates a broader data science principle: rather than computing expensive full statistics, find low-dimensional projections that preserve the most information. The same idea appears throughout scientific machine learning.

- **Impact on Fundamental Interactions:** Extending higher-order statistics to the three-dimensional Lyman-alpha forest opens new ways to constrain neutrino masses, dark matter properties, and primordial non-Gaussianity at redshifts inaccessible to current galaxy surveys.

- **Outlook and References:** The analytic window function treatment makes shifted skew spectra immediately applicable to DESI data, with extensions to future Stage-V spectroscopic surveys planned. The full methodology is detailed in [arXiv:2510.23597](https://arxiv.org/abs/2510.23597).
