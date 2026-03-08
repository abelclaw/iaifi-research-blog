---
abstract: We investigate the central density structure of dark matter halos in cold
  dark matter (CDM) and self-interacting dark matter (SIDM) models using simulations
  that are part of the Feedback In Realistic Environments (FIRE) project. For simulated
  halos of dwarf galaxy scale ($M_{\rm halo}(z=0)\approx 10^{10}\,M_\odot$), we study
  the central structure in both dissipationless simulations and simulations with full
  FIRE-2 galaxy formation physics. As has been demonstrated extensively in recent
  years, both baryonic feedback and self-interactions can convert central cusps into
  cores, with the former process doing so in a manner that depends sensitively on
  stellar mass at fixed $M_{\rm halo}$. Whether the two processes (baryonic feedback
  and self-interactions) are distinguishable, however, remains an open question. Here
  we demonstrate that, compared to feedback-induced cores, SIDM-induced cores transition
  more quickly from the central region of constant density to the falling density
  at larger radial scales. This result holds true even when including identical galaxy
  formation modeling in SIDM simulations as is used in CDM simulations, since self-interactions
  dominate over galaxy formation physics in establishing the central structure of
  SIDM halos in this mass regime. The change in density profile slope as a function
  of radius therefore holds the potential to discriminate between self-interactions
  and galaxy formation physics as the driver of core formation in dwarf galaxies.
arxivId: '2501.16602'
arxivUrl: https://arxiv.org/abs/2501.16602
authors:
- Maria C. Straight
- Michael Boylan-Kolchin
- James S. Bullock
- Philip F. Hopkins
- Xuejian Shen
- Lina Necib
- Alexandres Lazar
- Andrew S. Graus
- Jenna Samuel
concepts:
- dark matter
- cosmological simulation
- self-interacting dark matter
- cusp-core transformation
- baryonic feedback
- density profile slope
- simulation-based inference
- model validation
- monte carlo methods
- dark energy
- regression
figures:
- /iaifi-research-blog/figures/2501_16602/figure_1.png
- /iaifi-research-blog/figures/2501_16602/figure_1.png
- /iaifi-research-blog/figures/2501_16602/figure_2.png
- /iaifi-research-blog/figures/2501_16602/figure_2.png
- /iaifi-research-blog/figures/2501_16602/figure_3.png
- /iaifi-research-blog/figures/2501_16602/figure_3.png
pdfUrl: https://arxiv.org/pdf/2501.16602v2
published: '2025-01-28T00:31:29+00:00'
theme: Astrophysics
title: Central densities of dark matter halos in FIRE-2 simulations of low-mass galaxies
  with cold dark matter and self-interacting dark matter
wordCount: 991
---

## The Big Picture

Imagine trying to solve a mystery where two completely different culprits leave nearly identical crime scenes. That's the situation astrophysicists face when studying the hearts of small galaxies. The dark matter at the center of dwarf galaxies looks suspiciously "fluffy," with lower density than our best theories predict. Two very different explanations could account for it.

The leading cosmological model, **cold dark matter (CDM)**, predicts that galaxies should have dense, sharply rising "cusps" of dark matter at their centers. But observations of dwarf galaxies consistently reveal something softer: flat, constant-density "cores." Two suspects have competed for decades to explain this discrepancy.

**Stellar feedback** (the energetic winds and explosions from dying stars) can violently rattle a galaxy's gravitational grip on its dark matter, gradually pushing the center outward into a flat, low-density core. **Self-interacting dark matter (SIDM)**, an exotic variant in which dark matter particles actually collide with each other, redistributes energy from the outside inward until the center smooths out.

A new study using the FIRE-2 simulation suite has found a subtle but potentially decisive fingerprint that could tell these two mechanisms apart: the *shape* of the transition between a galaxy's core and its outer halo.

> **Key Insight:** SIDM-induced cores have a sharper, more abrupt boundary where flat central density gives way to steeply falling outer density. Stellar feedback cannot replicate this shape fingerprint, even when both processes produce the same overall core size.

## How It Works

The team ran cosmological simulations targeting dwarf galaxies with halo masses around **10¹⁰ solar masses** (roughly ten billion times the mass of our Sun). This is a scale where both stellar feedback and SIDM are highly effective at carving out cores, making them the hardest to distinguish. They compared four scenarios side by side:

1. **Dark matter only (CDM)** — gravity alone, no stars or gas
2. **Dark matter only (SIDM)** — same, but dark matter particles collide with a cross section of σ/m ~ 2 cm² g⁻¹ (a measure of how likely two dark matter particles are to scatter off each other)
3. **CDM with full FIRE-2 physics** — star formation, supernova feedback, stellar winds, and gas dynamics
4. **SIDM with full FIRE-2 physics** — everything from scenario 3, but with self-interacting dark matter

By holding the star and gas physics constant across CDM and SIDM runs, any remaining difference in outcomes must come from the dark matter physics itself.

![Figure 1](/iaifi-research-blog/figures/2501_16602/figure_1.png)

The key diagnostic isn't just central density. It's the **logarithmic slope of the density profile**, which measures how quickly density falls off as you move outward from a galaxy's center. Think of the dark matter distribution as a hill: the slope tells you how steep the hill is at each point, and whether that steepness changes gradually or snaps abruptly.

In feedback-driven CDM cores, the transition from flat to steep is gradual, spread across a wide range of radii. In SIDM halos, the transition is sharper and more compressed. The core just *ends*.

![Figure 3](/iaifi-research-blog/figures/2501_16602/figure_2.png)

The researchers quantified this by comparing two characteristic radii: where the density slope reaches −1 (density begins falling noticeably) versus where it reaches −2 (density falls steeply). In SIDM halos, these radii sit much closer together, producing a tight, compact transition zone. In feedback-shaped CDM halos, the same transition is smeared out over larger scales.

Even when full stellar physics was added to the SIDM simulations, self-interactions still dominated the central structure. Stellar feedback did not wash out the SIDM signature. The shape of the SIDM core remained distinctly different from its CDM counterpart, suggesting this fingerprint holds up against the messiness of real galaxy formation.

## Why It Matters

The "cusp-core problem" has haunted cosmology for thirty years. If we can't tell CDM-plus-feedback from SIDM by looking at galaxy centers, we lose one of our best handles on whether dark matter particles have exotic properties. SIDM would require physics beyond the Standard Model, with new fundamental forces acting among dark matter particles but not on ordinary matter.

![Figure 5](/iaifi-research-blog/figures/2501_16602/figure_3.png)

This study points toward a concrete observational strategy. Next-generation instruments like the Vera C. Rubin Observatory, the Nancy Grace Roman Space Telescope, and powerful radio arrays will deliver unprecedentedly detailed maps of how stars and gas move inside dwarf galaxies. The slope transition signature identified here is exactly the kind of subtle profile shape that those instruments could resolve.

The paper also raises questions about even lower stellar masses, where feedback becomes ineffective and CDM and SIDM predictions should diverge more sharply.

Caveats remain. The simulations used a single, fixed SIDM cross section; real SIDM models often feature velocity-dependent cross sections that produce a wider variety of core shapes. This is a proof of concept, demonstrating that the shape difference *exists* and *persists* in realistic simulations, rather than a definitive prediction across all possible SIDM models.

> **Bottom Line:** The shape of a dwarf galaxy's dark matter core, not just its size, may be the key to solving one of cosmology's longest-running mysteries. SIDM leaves a characteristically sharper core boundary that survives even when realistic galaxy physics is included.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines computational astrophysics with fundamental particle physics, using the FIRE-2 galaxy formation framework to probe whether dark matter's microphysical properties leave detectable imprints in galaxy-scale structure.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Extracting subtle morphological signatures from noisy simulation outputs is a pattern-recognition challenge where AI-driven analysis tools are increasingly being applied to large astrophysical simulation databases.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By identifying an observational signature distinguishing SIDM from CDM in dwarf galaxies, this research opens a new avenue for constraining whether dark matter particles experience fundamental non-gravitational forces, directly testing physics beyond the Standard Model.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work with velocity-dependent SIDM cross sections and high-resolution kinematic data from Rubin and Roman could turn this theoretical signature into a definitive observational test. The paper is available as [arXiv:2501.16602](https://arxiv.org/abs/2501.16602).</span></div></div>
</div>
