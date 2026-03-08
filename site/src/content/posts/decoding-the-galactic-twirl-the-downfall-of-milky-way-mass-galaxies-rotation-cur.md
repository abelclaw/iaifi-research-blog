---
abstract: Recent measurements of the Milky Way rotation curve found a sharp decline
  at around $15$-$20$ kpc from the center of the Galaxy, suggesting that the Galactic
  dark matter halo is much less massive than predicted by other dynamical tracers.
  To address this tension, we study the validity of the assumptions made in calculating
  the Milky Way's rotation curve. To do so, we apply Jeans' equation, the current
  standard approach of measuring rotation curves, to three cosmological zoom-in simulations
  of Milky Way-like galaxies from the FIRE-2 Latte suite. Using synthetic Gaia surveys,
  we replicate the sample selection process and calculation employed in measuring
  the Milky Way rotation curve. We examine four failure modes of this calculation
  and find that the measured curves deviate from the true curve by $5$-$20\%$ rather
  than below $5\%$, as estimated by previous works. Interestingly, there is a large
  galaxy-to-galaxy variance, and different systematics dominate different galaxies.
  We rederive the Milky Way's dark matter density profile with the rotation curve
  while incorporating systematics from the simulations. The posterior distribution
  of the density profiles is consistent with a fiducial NFW profile when assuming
  a gNFW profile for dark matter. We find that the virial mass, $7.32^{+1.98}_{-1.53}\times10^{11}~M_{\odot}$,
  consistent with other probes of the Milky Way's mass. However, we recommend that
  the field moves away from relying solely on the rotation curve when studying the
  dark matter profile, and adopts methods that incorporate additional probes and/or
  do not heavily depend on assumptions described in this study.
arxivId: '2503.05877'
arxivUrl: https://arxiv.org/abs/2503.05877
authors:
- Xiaowei Ou
- Lina Necib
- Andrew Wetzel
- Anna Frebel
- Jeremy Bailin
- Micah Oeur
concepts:
- dark matter
- jeans equation
- cosmological simulation
- rotation curve systematics
- uncertainty quantification
- model validation
- bayesian inference
- posterior estimation
- nfw profile fitting
- simulation-based inference
- inverse problems
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2503_05877/figure_1.png
- /iaifi-research-blog/figures/2503_05877/figure_1.png
- /iaifi-research-blog/figures/2503_05877/figure_2.png
- /iaifi-research-blog/figures/2503_05877/figure_2.png
- /iaifi-research-blog/figures/2503_05877/figure_3.png
- /iaifi-research-blog/figures/2503_05877/figure_3.png
pdfUrl: https://arxiv.org/pdf/2503.05877v1
published: '2025-03-07T19:03:14+00:00'
theme: Astrophysics
title: 'Decoding the Galactic Twirl: The Downfall of Milky Way-mass Galaxies Rotation
  Curves in the FIRE Simulations'
wordCount: 1021
---

## The Big Picture

Imagine trying to weigh a room by measuring how fast a single ceiling fan spins. You'd get a number, but how confident could you really be? Astronomers face a version of this problem every time they try to measure the Milky Way's dark matter halo, and for decades, the rotation curve has been their fan.

The **rotation curve** plots how fast stars orbit the galactic center at different distances. It has been the gold standard for probing dark matter in galaxies for half a century. Stars in the outer disk orbit faster if there's more mass pulling on them, so a flat curve means dark matter keeps adding mass even far from the center.

But recently, something strange turned up. Multiple independent measurements found the Milky Way's rotation curve *dropping* sharply beyond about 50,000 to 65,000 light-years from the center, implying a dark matter halo far lighter than other techniques suggest. Those other techniques include tracking globular clusters, dwarf satellite galaxies, and stellar streams (the ribbons of stars left behind when a small galaxy gets torn apart). Something didn't add up.

A new study led by Xiaowei Ou and Lina Necib at MIT puts the measurement method itself on trial. Using high-fidelity cosmological simulations, they pin down exactly where the standard calculation goes wrong and by how much.

> **Key Insight:** The standard method for measuring galactic rotation curves can be off by 5–20%, not the sub-5% error previously assumed, meaning the Milky Way's apparent dark matter deficit may be a measurement artifact rather than a physical reality.

## How It Works

The researchers turned to the **FIRE-2 Latte simulations**, three high-resolution simulations of Milky Way-mass galaxies that concentrate their full computational power on a single galaxy while still tracking the surrounding cosmic environment. These evolve gas, stars, and dark matter from the early universe to the present day, capturing everything from star formation to shock waves from exploding stars. Unlike the real Milky Way, the researchers know exactly what the true rotation curve is for each simulated galaxy, so they can compare what the measurement *says* versus what's actually *there*.

![Figure 1](/iaifi-research-blog/figures/2503_05877/figure_1.png)

To mimic reality, the team built **synthetic Gaia surveys**: fake observations that replicate the selection biases, distance errors, and coverage gaps of the real Gaia mission, the European Space Agency's star-mapping satellite. They then applied the same **Jeans equation** pipeline used in actual Milky Way studies. The Jeans equation is a mathematical framework, borrowed from the physics of gases, that converts measured stellar velocities and densities into an inferred gravitational pull and ultimately a rotation curve. It works well in theory but rests on assumptions that crack under real-world conditions.

The team hunted down four failure modes:

1. **Asymmetric drift correction errors** — Stars don't orbit in perfectly circular paths; the Jeans method corrects for this, but those corrections are approximations that can go wrong.
2. **Observational selection effects** — Gaia doesn't see every star equally well. Biases in which stars get included distort the inferred velocity distributions.
3. **Axis asymmetry** — The Jeans equation assumes the galaxy is rotationally symmetric, like a perfect pinwheel. Real galaxies, battered by mergers and satellite interactions, often aren't.
4. **Dynamical disequilibrium** — If the galaxy hasn't settled into a stable, steady state, the equation's assumption of equilibrium breaks down entirely.

![Figure 2](/iaifi-research-blog/figures/2503_05877/figure_1.png)

Across all three simulated galaxies, the measured rotation curves deviated from the true curves by **5 to 20%**, far worse than the sub-5% systematic error assumed by previous Milky Way studies.

Different galaxies were dominated by different failure modes. One galaxy's curve was mostly corrupted by asymmetric drift errors; another's by lingering gravitational disturbances from a recently absorbed smaller galaxy. There is no single culprit, and no one-size-fits-all correction.

![Figure 4](/iaifi-research-blog/figures/2503_05877/figure_2.png)

## Why It Matters

With a calibrated model of how badly the measurement can go wrong, the team re-ran the inference of the Milky Way's dark matter profile using the Ou et al. 2024 rotation curve data, this time folding in their simulation-derived systematic error budget. When you allow for 5–20% measurement uncertainty, the Milky Way's dark matter halo is no longer anomalously light. The best-fit dark matter density profile now matches the standard **NFW profile**, the shape predicted by cold dark matter simulations, with a virial mass of **7.32 × 10¹¹ solar masses** (roughly three-quarters of a trillion suns). That's consistent with estimates from globular clusters and stellar streams.

![Figure 6](/iaifi-research-blog/figures/2503_05877/figure_3.png)

This isn't just a fix for one measurement. It exposes a real vulnerability in how the field approaches galactic dynamics. The galaxy-to-galaxy variation in failure modes also warns against over-interpreting any single measurement: what looks like a dark matter anomaly might just be a galaxy that went through a recent merger.

The implication is straightforward. The field should stop relying solely on rotation curves to characterize dark matter profiles. Future work should combine rotation curves with independent probes like stellar streams, satellite kinematics, and gravitational lensing, and use inference methods that don't assume a perfectly symmetric, perfectly calm galaxy.

> **Bottom Line:** The Milky Way's rotation curve may have been telling us more about the limits of our measurement tools than about a genuinely unusual dark matter halo. Fix those tools, and the Galaxy falls back in line with everything else we know about it.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies simulation-based systematic modeling and synthetic survey techniques to a classic astrophysics problem, showing how forward modeling can reveal hidden biases in observational inference pipelines.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The methodology of using synthetic observations to quantify failure modes in inference pipelines provides a blueprint for robustness testing across data-rich astronomical surveys.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By showing that the Milky Way's dark matter halo mass is consistent with NFW predictions once measurement systematics are properly accounted for, this work resolves a significant tension in our understanding of galactic dark matter structure.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work should combine rotation curves with complementary probes (stellar streams, satellite dynamics, and lensing) using methods that handle asymmetry and disequilibrium; the full analysis is available at [arXiv:2503.05877](https://arxiv.org/abs/2503.05877).</span></div></div>
</div>
