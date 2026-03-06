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

Imagine trying to find invisible rocks by watching how they bend light around them. That's essentially what dark matter hunters do — except the "rocks" could be clumps of matter the size of small galaxies, and the light comes from objects billions of light-years away. The challenge is that **dark matter subhalos** — invisible clumps too small to ever form a visible galaxy — leave only the faintest whispers of evidence: subtle tugs on the apparent positions of distant objects as they drift past.

Astronomers have known for decades that dark matter shapes the universe on grand scales — its gravitational fingerprints appear in how galaxies rotate faster than their visible matter alone can explain, in the large-scale web-like structure of the cosmos, and in the faint afterglow of the Big Bang. At scales smaller than a single galaxy, though, things get murkier. Subhalos below roughly a billion solar masses don't attract enough ordinary matter to glow, making them effectively invisible. The only way to find them is through their gravitational effects on things we *can* see.

Siddharth Mishra-Sharma at IAIFI has developed a new method that uses machine learning to squeeze far more information from stellar motion data than previously possible — potentially opening a new window into dark matter's small-scale structure.

> **Key Insight:** By replacing traditional statistical summaries with a spherical convolutional neural network trained to estimate likelihood ratios, this approach achieves dramatically better sensitivity to dark matter substructure and handles real-world measurement noise more gracefully than any existing technique.

## How It Works

The technique exploits **astrometric lensing** — tiny deflections in the apparent velocities of background objects caused by a passing dark matter clump. When a subhalo drifts between us and a field of distant **quasars** (extremely bright galactic cores near the edge of the observable universe), its gravity subtly tugs those quasars' apparent positions, imprinting a coherent, correlated pattern across the sky. The signal is weak, but it's real.

Previous methods detected this signal using the **angular power spectrum** — a mathematical summary measuring how signal strength varies across different angular scales on the sky. Think of identifying a piece of music by analyzing only its average volume at different frequencies, ignoring melody and rhythm entirely. It works, but it discards substantial information, especially for clumpy dark matter distributions whose statistics can't be captured by simple averages and spreads.

The new approach feeds the full velocity map directly into a **spherical convolutional neural network** — designed specifically for data on the surface of a sphere, like the celestial sky. Its pyramid-like architecture captures both fine local patterns and large-scale correlations across the whole sky.

![Figure 1](/iaifi-research-blog/figures/2110_01620/figure_1.png)

The network operates as a **parameterized classifier** — a pattern-recognizer trained on millions of simulated sky maps, each generated with a different amount of dark matter substructure. It estimates the **likelihood ratio**: given this map of stellar velocities, how much more probable is it that a cold dark matter population with subhalo fraction *f_sub* exists versus none at all? This **simulation-based inference** approach sidesteps the impossibly complex task of writing down an explicit mathematical likelihood.

The method's key components:
- **Velocity maps** pixelized into 49,152 equal-area sky tiles using the **HEALPix** scheme (`nside=64`)
- **Simulation-based training** across a wide range of *f_sub* values — the fraction of the Milky Way's mass in subhalos spanning 10⁻⁶ to 10¹⁰ solar masses
- **Neural likelihood-ratio estimation** producing direct, calibrated constraints on dark matter substructure without hand-crafted summary statistics

## Why It Matters

The performance gains are striking. Compared to the power spectrum approach, the neural method achieves significantly tighter constraints on the subhalo fraction — it requires fewer sources, or equivalently can detect smaller signals. As astrometric precision improves with next-generation surveys, the neural method's advantage grows rather than shrinks.

![Figure 2](/iaifi-research-blog/figures/2110_01620/figure_2.png)

The method also proves robust to the messy complications of real astronomical data. **Gaia** — the European Space Agency's satellite that has precisely mapped the positions and motions of over a billion stars — and future surveys like the Square Kilometer Array and the Roman Space Telescope don't deliver clean velocity maps. They carry complicated noise patterns, gaps in sky coverage, and position-dependent systematic effects.

![Figure 3](/iaifi-research-blog/figures/2110_01620/figure_3.png)

The paper demonstrates robustness against both *modeled* noise (like uneven source distributions across the sky, tested against actual Gaia quasar catalogs) and *unmodeled* noise. A method that works on clean simulations but breaks on real data is useless. The neural likelihood-ratio estimator degrades gracefully when confronted with messy reality — suggesting it can be applied directly to current surveys with confidence.

The broader implications reach well beyond dark matter. Spherical neural networks combined with simulation-based inference form a general toolkit for any signal-on-the-sphere problem: directional patterns in cosmic rays, the polarization of the Big Bang's afterglow, gravitational wave backgrounds. This work is a proof of concept that machine learning can outperform traditional statistics on the celestial sphere — and do it reliably.

> **Bottom Line:** Neural likelihood-ratio estimation with spherical convolutional networks outperforms all existing power-spectrum-based approaches for astrometric dark matter searches, and its robustness to real-world noise makes it ready for deployment on current Gaia data.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work exemplifies the IAIFI mission by applying modern deep learning — spherical convolutional networks and simulation-based inference — directly to a fundamental astrophysics problem, achieving sensitivity beyond what purely statistical approaches can match.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper demonstrates that neural networks designed to respect the symmetry structure of the data domain can replace hand-crafted summary statistics in high-dimensional inference, offering a blueprint for ML-driven inference in complex physical systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling more sensitive searches for dark matter subhalos below 10⁹ solar masses, this method can probe small-scale structure predictions of cold dark matter models, potentially distinguishing between competing candidates that differ in their sub-galactic clustering.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">With next-generation surveys like the Roman Space Telescope and SKA set to deliver orders-of-magnitude gains in astrometric precision, this method's favorable noise-scaling positions it as a key tool for dark matter characterization in the coming decade; see arXiv:2110.01632.</span></div></div>
</div>
