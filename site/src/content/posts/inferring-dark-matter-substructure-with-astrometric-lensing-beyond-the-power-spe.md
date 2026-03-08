---
abstract: Astrometry -- the precise measurement of positions and motions of celestial
  objects -- has emerged as a promising avenue for characterizing the dark matter
  population in our Galaxy. By leveraging recent advances in simulation-based inference
  and neural network architectures, we introduce a novel method to search for global
  dark matter-induced gravitational lensing signatures in astrometric datasets. Our
  method based on neural likelihood-ratio estimation shows significantly enhanced
  sensitivity to a cold dark matter population and more favorable scaling with measurement
  noise compared to existing approaches based on two-point correlation statistics.
  We demonstrate the real-world viability of our method by showing it to be robust
  to non-trivial modeled as well as unmodeled noise features expected in astrometric
  measurements. This establishes machine learning as a powerful tool for characterizing
  dark matter using astrometric data.
arxivId: '2110.01620'
arxivUrl: https://arxiv.org/abs/2110.01620
authors:
- Siddharth Mishra-Sharma
concepts:
- dark matter
- simulation-based inference
- likelihood ratio
- astrometric lensing
- convolutional networks
- equivariant neural networks
- signal detection
- bayesian inference
- inverse problems
- cosmological simulation
- spectral methods
- robustness
figures:
- /iaifi-research-blog/figures/2110_01620/figure_1.png
- /iaifi-research-blog/figures/2110_01620/figure_2.png
- /iaifi-research-blog/figures/2110_01620/figure_3.png
pdfUrl: https://arxiv.org/pdf/2110.01620v2
published: '2021-10-04T18:00:00+00:00'
theme: Astrophysics
title: Inferring dark matter substructure with astrometric lensing beyond the power
  spectrum
wordCount: 1023
---

## The Big Picture

Imagine trying to find invisible rocks by watching how they bend light around them. That's what dark matter hunters do, except the "rocks" could be clumps of matter the size of small galaxies, and the light comes from objects billions of light-years away. **Dark matter subhalos**, invisible clumps too small to ever form a visible galaxy, leave only the faintest traces: subtle tugs on the apparent positions of distant objects as they drift past.

We've known for decades that dark matter shapes the universe on grand scales. Its gravitational fingerprints show up in how galaxies rotate faster than their visible matter can explain, in the large-scale web-like structure of the cosmos, and in the faint afterglow of the Big Bang. Below the scale of a single galaxy, though, things get murkier. Subhalos lighter than about a billion solar masses don't attract enough ordinary matter to glow, making them effectively invisible. The only way to find them is through their gravitational pull on things we *can* see.

Siddharth Mishra-Sharma at IAIFI has developed a new method that uses machine learning to squeeze far more information from stellar motion data than was previously possible, with direct consequences for how we probe dark matter's small-scale structure.

> **Key Insight:** By replacing traditional statistical summaries with a spherical convolutional neural network trained to estimate likelihood ratios, this approach achieves substantially better sensitivity to dark matter substructure and handles real-world measurement noise more gracefully than existing techniques.

## How It Works

The technique uses **astrometric lensing**: tiny deflections in the apparent velocities of background objects caused by a passing dark matter clump. When a subhalo drifts between us and a field of distant **quasars** (extremely bright galactic cores near the edge of the observable universe), its gravity subtly shifts those quasars' apparent positions, imprinting a coherent, correlated pattern across the sky. The signal is weak, but it's real.

Previous methods detected this signal using the **angular power spectrum**, a mathematical summary that measures how signal strength varies across different angular scales on the sky. Think of identifying a piece of music by analyzing only its average volume at different frequencies, ignoring melody and rhythm entirely. It works, but it throws away a lot of information, especially for clumpy dark matter distributions whose statistics can't be captured by simple averages and spreads.

The new approach feeds the full velocity map directly into a **spherical convolutional neural network**, built specifically for data living on the surface of a sphere like the celestial sky. Its pyramid-like architecture captures both fine local patterns and large-scale correlations.

![Figure 1](figure:1)

The network works as a **parameterized classifier**, trained on millions of simulated sky maps each generated with a different amount of dark matter substructure. It estimates the **likelihood ratio**: given this map of stellar velocities, how much more probable is it that a cold dark matter population with subhalo fraction *f_sub* exists versus none at all? This **simulation-based inference** approach sidesteps the impossibly complex task of writing down an explicit mathematical likelihood.

The method's key components:
- **Velocity maps** pixelized into 49,152 equal-area sky tiles using the **HEALPix** scheme (`nside=64`)
- **Simulation-based training** across a wide range of *f_sub* values, the fraction of the Milky Way's mass in subhalos spanning 10⁻⁶ to 10¹⁰ solar masses
- **Neural likelihood-ratio estimation** producing direct, calibrated constraints on dark matter substructure without hand-crafted summary statistics

## Why It Matters

The performance gains are striking. Compared to the power spectrum approach, the neural method puts significantly tighter constraints on the subhalo fraction. It needs fewer sources, or equivalently, it can detect smaller signals. And as astrometric precision improves with next-generation surveys, the neural method's advantage grows rather than shrinks.

![Figure 2](figure:2)

The method also holds up against the messy complications of real astronomical data. **Gaia**, the European Space Agency's satellite that has precisely mapped the positions and motions of over a billion stars, doesn't deliver clean velocity maps. Neither will future surveys like the Square Kilometer Array and the Roman Space Telescope. They all carry complicated noise patterns, gaps in sky coverage, and position-dependent systematic effects.

![Figure 3](figure:3)

The paper tests against both modeled noise (like uneven source distributions across the sky, checked against actual Gaia quasar catalogs) and unmodeled noise. A method that works on clean simulations but breaks on real data is useless. The neural likelihood-ratio estimator degrades gracefully under messy conditions, suggesting it can be applied directly to current surveys.

These tools aren't limited to dark matter, either. Spherical neural networks combined with simulation-based inference form a general toolkit for any signal-on-the-sphere problem: directional patterns in cosmic rays, the polarization of the Big Bang's afterglow, gravitational wave backgrounds. Machine learning can outperform traditional statistics on the celestial sphere, and do it reliably.

> **Bottom Line:** Neural likelihood-ratio estimation with spherical convolutional networks outperforms all existing power-spectrum-based approaches for astrometric dark matter searches, and its graceful handling of real-world noise makes it ready for deployment on current Gaia data.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work applies modern deep learning (spherical convolutional networks and simulation-based inference) directly to a fundamental astrophysics problem, achieving sensitivity beyond what purely statistical approaches can match. It's a clear example of the IAIFI mission in action.

- **Impact on Artificial Intelligence:** Neural networks designed to respect the symmetry structure of the data domain can replace hand-crafted summary statistics in high-dimensional inference, providing a template for ML-driven analysis in complex physical systems.

- **Impact on Fundamental Interactions:** By enabling more sensitive searches for dark matter subhalos below 10⁹ solar masses, this method can test small-scale structure predictions of cold dark matter models, potentially distinguishing between competing candidates that differ in their sub-galactic clustering.

- **Outlook and References:** With next-generation surveys like the Roman Space Telescope and SKA set to deliver orders-of-magnitude gains in astrometric precision, this method's favorable noise-scaling makes it a natural tool for dark matter characterization in the coming decade; see [arXiv:2110.01620](https://arxiv.org/abs/2110.01620).

## Original Paper Details
- **Title:** Inferring dark matter substructure with astrometric lensing beyond the power spectrum
- **arXiv ID:** 2110.01620
- **Authors:** ["Siddharth Mishra-Sharma"]
- **Abstract:** Astrometry -- the precise measurement of positions and motions of celestial objects -- has emerged as a promising avenue for characterizing the dark matter population in our Galaxy. By leveraging recent advances in simulation-based inference and neural network architectures, we introduce a novel method to search for global dark matter-induced gravitational lensing signatures in astrometric datasets. Our method based on neural likelihood-ratio estimation shows significantly enhanced sensitivity to a cold dark matter population and more favorable scaling with measurement noise compared to existing approaches based on two-point correlation statistics. We demonstrate the real-world viability of our method by showing it to be robust to non-trivial modeled as well as unmodeled noise features expected in astrometric measurements. This establishes machine learning as a powerful tool for characterizing dark matter using astrometric data.
