---
abstract: The Gaia satellite will observe the positions and velocities of over a billion
  Milky Way stars. In the early data releases, the majority of observed stars do not
  have complete 6D phase-space information. In this Letter, we demonstrate the ability
  to infer the missing line-of-sight velocities until more spectroscopic observations
  become available. We utilize a novel neural network architecture that, after being
  trained on a subset of data with complete phase-space information, takes in a star's
  5D astrometry (angular coordinates, proper motions, and parallax) and outputs a
  predicted line-of-sight velocity with an associated uncertainty. Working with a
  mock Gaia catalog, we show that the network can successfully recover the distributions
  and correlations of each velocity component for stars that fall within ~5 kpc of
  the Sun. We also demonstrate that the network can accurately reconstruct the velocity
  distribution of a kinematic substructure in the stellar halo that is spatially uniform,
  even when it comprises a small fraction of the total star count.
arxivId: '2103.14039'
arxivUrl: https://arxiv.org/abs/2103.14039
authors:
- Adriana Dropulic
- Bryan Ostdiek
- Laura J. Chang
- Hongwan Liu
- Timothy Cohen
- Mariangela Lisanti
concepts:
- stellar phase-space inference
- regression
- uncertainty quantification
- inverse problems
- density estimation
- semi-supervised learning
- loss function design
- cosmological simulation
- anomaly detection
- dark matter
- transfer learning
figures:
- /iaifi-research-blog/figures/2103_14039/figure_1.png
- /iaifi-research-blog/figures/2103_14039/figure_2.png
- /iaifi-research-blog/figures/2103_14039/figure_3.png
pdfUrl: https://arxiv.org/pdf/2103.14039v2
published: '2021-03-25T18:00:00+00:00'
theme: Astrophysics
title: 'Machine Learning the 6th Dimension: Stellar Radial Velocities from 5D Phase-Space
  Correlations'
wordCount: 1202
---

## The Big Picture

Imagine trying to reconstruct the full motion of a billion cars on a highway, but your camera can only capture four pieces of information per car: its position on the grid, how fast it's moving left-right, how fast it's moving up-down, and how far away it is. The one thing you can't directly measure? How fast each car is moving toward or away from you. Now scale that up to a billion stars, each hurtling through the Milky Way at hundreds of kilometers per second, and you start to understand the challenge facing modern astrophysicists.

The European Space Agency's *Gaia* satellite is the most ambitious stellar census ever attempted, mapping over a billion stars with extraordinary precision. To fully describe a star's motion through space, you need six numbers: three for position, three for velocity. *Gaia*'s early data releases delivered five of those numbers reliably. The sixth, the **line-of-sight velocity** (the component of motion directly toward or away from us), requires a completely different kind of observation called spectroscopy.

Spectroscopy measures how starlight shifts in color depending on whether a star is approaching or receding. It's the same principle behind the rising-and-falling pitch of a passing ambulance siren, applied to light instead of sound. In the early *Gaia* data releases, fewer than 1% of observed stars had this measurement.

A team of researchers from Princeton, Harvard, New York University, and the University of Oregon found a clever workaround: train a neural network to infer the missing sixth dimension from the five that *Gaia* already provides.

> **Key Insight:** Physical correlations in stellar kinematics are strong enough that a neural network can predict a star's missing line-of-sight velocity from its other measured properties, and honestly assess its own uncertainty when it can't.

## How It Works

Stars don't move randomly. They orbit the galaxy, stream through the disk, and cluster in kinematic groups that share common origins. A star's position and its sideways velocity components carry real statistical information about how fast it's moving toward or away from us. The network learns those correlations.

The team built their training dataset from a mock *Gaia* catalog, a simulation of roughly 75 million stars with complete position and velocity data in all three dimensions, drawn from the Besançon Galactic model. It encodes the structure of the bulge, thin disk, thick disk, and stellar halo. They also injected a population of stars mimicking **Gaia Enceladus**, the remnant of a dwarf galaxy that merged with the Milky Way billions of years ago, to test whether the network could detect real substructure.

![Figure 1](/iaifi-research-blog/figures/2103_14039/figure_1.png)

Instead of a single network outputting one number, the team built a **compound feedforward network**: two parallel halves sharing the same structure but diverging at the final layer. One half predicts the line-of-sight velocity; the other predicts the *uncertainty* on that prediction. For stars whose kinematics fall neatly within learned patterns, the uncertainty is small. For outliers or stars in sparse regions of phase space, the network flags its own low confidence.

Training used seven million stars with confirmed full 6D information, tested against ten million stars spanning a broader range of magnitudes and temperatures. The inputs were five *Gaia* observables:

- Two **angular coordinates** (the star's location on the sky)
- Two **proper motions** (how fast it moves across the sky plane)
- **Parallax** (a proxy for distance, derived from the star's apparent shift in position as Earth orbits the Sun)

## Why It Matters

The network successfully recovers full velocity distributions for stars within roughly 5 kiloparsecs (about 16,000 light-years) of the Sun. Not just rough averages: the detailed statistical shapes of how stars move in each direction, including the correlations between velocity components that encode the dynamical structure of the galaxy.

![Figure 2](/iaifi-research-blog/figures/2103_14039/figure_2.png)

The most telling test involves **kinematic substructure**, groupings of stars that share distinctive movement patterns but are invisible to ordinary sky searches. Gaia Enceladus stars are spatially spread out; you can't find them by position alone. Their signature lives purely in velocity space.

Even when these stars represent only about 0.5% of the training set, the network accurately reconstructs their distinct velocity distribution. That's a strong sign that machine learning can pull its weight in the search for the Milky Way's ancient merger history.

![Figure 3](/iaifi-research-blog/figures/2103_14039/figure_3.png)

This work arrives at a specific moment in *Gaia*'s development. Future data releases will steadily expand the number of stars with spectroscopic measurements, but that process takes years. In the interim, neural network inference offers a statistically rigorous way to extract more science from data already in hand, working alongside spectroscopic surveys like APOGEE, GALAH, and LAMOST rather than replacing them.

The idea generalizes. Any time a dataset is systematically missing one kind of measurement, correlated variables may let a well-designed network fill the gap with calibrated uncertainty rather than false confidence. That template applies well beyond *Gaia*.

> **Bottom Line:** By training on known correlations in stellar kinematics, this team predicts *Gaia*'s missing sixth dimension, line-of-sight velocity, for millions of stars, complete with honest uncertainty estimates. The network recovers kinematic substructures invisible to purely geometric searches.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">Modern deep learning applied to a core problem in observational astrophysics, turning incomplete phase-space data into statistically rigorous velocity predictions for galactic dynamics research.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The compound dual-output network, which simultaneously predicts a value and its own uncertainty, provides a practical architecture for uncertainty-aware regression in scientific domains where calibrated confidence matters as much as the prediction itself.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Recovering full 6D phase-space information for millions of stars expands the usable dataset for measuring the Milky Way's gravitational potential, mapping dark matter density, and identifying remnants of ancient galaxy mergers like Gaia Enceladus.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will apply this approach to real *Gaia* data releases and extend coverage as spectroscopic surveys expand the training set; the method and code are available on GitHub, and the paper is archived at [arXiv:2103.14039](https://arxiv.org/abs/2103.14039).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Machine Learning the 6th Dimension: Stellar Radial Velocities from 5D Phase-Space Correlations</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2103.14039</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Adriana Dropulic", "Bryan Ostdiek", "Laura J. Chang", "Hongwan Liu", "Timothy Cohen", "Mariangela Lisanti"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">The Gaia satellite will observe the positions and velocities of over a billion Milky Way stars. In the early data releases, the majority of observed stars do not have complete 6D phase-space information. In this Letter, we demonstrate the ability to infer the missing line-of-sight velocities until more spectroscopic observations become available. We utilize a novel neural network architecture that, after being trained on a subset of data with complete phase-space information, takes in a star's 5D astrometry (angular coordinates, proper motions, and parallax) and outputs a predicted line-of-sight velocity with an associated uncertainty. Working with a mock Gaia catalog, we show that the network can successfully recover the distributions and correlations of each velocity component for stars that fall within ~5 kpc of the Sun. We also demonstrate that the network can accurately reconstruct the velocity distribution of a kinematic substructure in the stellar halo that is spatially uniform, even when it comprises a small fraction of the total star count.</span></div></div>
</div>
