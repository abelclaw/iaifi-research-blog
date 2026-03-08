---
abstract: We lay out the phenomenological behavior of event-shape observables evaluated
  by solving optimal transport problems between collider events and reference geometries
  -- which we name 'manifold distances' -- to provide guidance regarding their use
  in future studies. This discussion considers several choices related to the metric
  used to quantify these distances. We explore the differences between the various
  options, using a combination of analytical studies and simulated minimum-bias and
  multi-jet events. Making judicious choices when defining the metric and reference
  geometry can improve sensitivity to interesting signal features and reduce sensitivity
  to non-perturbative effects in QCD. The goal of this article is to provide a 'field
  guide' that can inform how choices made when defining a manifold distance can be
  tailored for the analysis at-hand.
arxivId: '2409.13150'
arxivUrl: https://arxiv.org/abs/2409.13150
authors:
- Cari Cesarotti
- Matt LeBlanc
concepts:
- optimal transport
- manifold distances
- collider physics
- energy mover's distance
- jet physics
- event isotropy
- new physics searches
- monte carlo methods
- standard model
- symmetry preservation
- anomaly detection
figures:
- /iaifi-research-blog/figures/2409_13150/figure_1.png
- /iaifi-research-blog/figures/2409_13150/figure_2.png
- /iaifi-research-blog/figures/2409_13150/figure_3.png
pdfUrl: https://arxiv.org/pdf/2409.13150v2
published: '2024-09-20T01:29:20+00:00'
theme: Theoretical Physics
title: A Field Guide to Event-Shape Observables Using Optimal Transport
wordCount: 892
---

## The Big Picture

Every time protons smash together at the Large Hadron Collider, hundreds of particles spray outward in all directions. Physicists need to quantify how "messy" that spray is compared to some idealized geometry. Think of it like a warehouse problem: you've got a chaotic pile of cargo, and you want to know the minimum work needed to rearrange it into a perfectly organized layout. That minimum work is your measure of disorder.

The sprays, called **event shapes**, encode information about the fundamental forces at play. The geometry of energy flowing outward from a collision tells you whether you're looking at ordinary quantum chromodynamics (QCD) or something new: exotic particles, supersymmetric partners, maybe even mini black holes. Different physics produces different geometric signatures, and no single measurement captures all of them equally well.

Cari Cesarotti and Matt LeBlanc have written a field guide to a new family of event-shape measurements built on **optimal transport theory**, the same mathematics behind that warehouse analogy. By mapping collider events onto geometric reference templates, physicists can build observables sharply tuned to specific new-physics signatures while staying insensitive to the messy, hard-to-calculate effects of QCD. The guide gives experimentalists a toolkit for choosing the right configuration for any given analysis.

## How It Works

The mathematical core is the **Energy Mover's Distance (EMD)**, a particle-physics adaptation of the classical Earth Mover's Distance from computer vision and operations research. Each particle in a collision carries some energy, and the EMD measures how much "work" it would take to rearrange all that energy into a perfectly symmetric reference pattern. A single number summarizing how far a given collision sits from some ideal geometry.

![Figure 1](/iaifi-research-blog/figures/2409_13150/figure_1.png)

Cesarotti and LeBlanc call these EMD-based measurements **manifold distances**: they measure how far an event sits from a geometric manifold, a smooth surface of reference shapes. The paper focuses on two complementary reference geometries:

- **Isotropic (ring-like):** A uniform distribution of energy in all directions. This is the signature of exotic soft unclustered energy patterns (SUEPs), where particles spread evenly rather than forming distinct jets, or of collider-produced black holes.
- **Dipole (back-to-back):** Two jets fired in opposite directions, the classic signature of ordinary quark-antiquark or quark-gluon scattering.

The paper also varies the **ground-space distance metric**, the mathematical ruler used to measure how far apart two particles are in the detector's coordinate system. Angular distances, distances in the rapidity-azimuth plane (the standard grid for mapping particle directions at the LHC), and other options each have different sensitivities to particle kinematics.

The analysis combines analytical calculations with Monte Carlo simulations of two distinct event types: **minimum-bias events** (common, low-energy collisions that form background noise) and **multi-jet events** (high-energy collisions producing several distinct particle jets). Comparing distributions across these two populations isolates which choices make an observable more or less sensitive to specific physics.

![Figure 2](/iaifi-research-blog/figures/2409_13150/figure_2.png)

The results show real, practical differences. Choosing the right metric and reference geometry changes what you can see. Dipole-distance observables behave similarly to the classical thrust variable under certain metric choices, as the authors verify analytically. Ring-distance observables, by contrast, open sensitivity to spherical or isotropic events that thrust would miss entirely.

The paper also examines how different choices respond to **hadronization**, the process by which quarks and gluons bind together into the actual particles reaching the detector. Low hadronization sensitivity matters because it means the observable is measuring the underlying high-energy collision physics rather than hard-to-calculate binding effects.

![Figure 3](/iaifi-research-blog/figures/2409_13150/figure_3.png)

## Why It Matters

Physicists at ATLAS and CMS must decide in advance which observables they'll measure. A poor choice means missing a new-physics signal, not because it wasn't there, but because the wrong geometric ruler was used.

The ATLAS Collaboration has already measured event isotropy (the isotropic manifold distance) in high-pT multijet events, and CMS has measured it in minimum-bias events. This field guide arrives as both experiments look to expand their event-shape programs.

The EMD framework is closely related to Wasserstein distances used in generative adversarial networks and distribution comparison in machine learning. Bringing optimal transport into particle physics creates a principled design space for new observables that classical approaches never offered. Future colliders, including proposed lepton colliders and high-luminosity LHC upgrades, will benefit from having this vocabulary worked out now.

Manifold distances aren't just one new observable. They're an entire configurable family, and this field guide shows physicists how to pick the right configuration for any search, from SUEP hunters to QCD precision measurements.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies optimal transport theory, a mathematical framework with deep roots in AI and machine learning, to design a new class of physically motivated particle physics observables, connecting methods across AI and fundamental physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Wasserstein/Earth Mover's Distance methods, widely used in generative modeling and distribution comparison in AI, can be adapted into domain-specific scientific tools with tunable sensitivity to physical features. This work shows concretely how that transfer works.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The field guide gives concrete prescriptions for tailoring event-shape observables at the LHC to improve sensitivity to BSM physics signatures, including SUEPs, high-multiplicity final states, and isotropic new-physics signals, while suppressing QCD non-perturbative backgrounds.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work can extend this framework to three-dimensional geometries, additional reference manifolds, and next-generation collider environments. The full paper is available at [arXiv:2409.13150](https://arxiv.org/abs/2409.13150).</span></div></div>
</div>
