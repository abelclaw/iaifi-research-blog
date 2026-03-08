---
abstract: The structure factor is a useful observable for probing charge density correlations
  in real materials, and its long-wavelength behavior encapsulated by ``quantum weight''
  has recently gained prominence in the study of quantum geometry and topological
  phases of matter. Here we employ the static structure factor, S(q), to explore the
  phase diagram of twisted transition metal dichalcogenides (TMDs), specifically tMoTe2,
  at filling factors n=1/3, 2/3 under varying displacement fields. Our results reveal
  a topological phase transition between a fractional Chern insulator (FCI) and a
  generalized Wigner crystal (GWC). This transition is marked by the appearance of
  Bragg peaks at charge-density-wave vectors, and simultaneously, large decrease of
  S(q) at small q which lowers the interaction energy. We further calculate the quantum
  weight of various FCI states, verifying the universal topological bound. Our findings
  provide new insights into the phase diagram of twisted TMDs and establish a general
  framework for characterizing topological phases through structure factor analysis.
arxivId: '2411.03496'
arxivUrl: https://arxiv.org/abs/2411.03496
authors:
- Timothy Zaklama
- Di Luo
- Liang Fu
concepts:
- fractional chern insulator
- quantum weight
- phase transitions
- moiré quantum geometry
- quantum states
- symmetry breaking
- spectral methods
- eigenvalue decomposition
- effective field theory
- quantum computing
figures:
- /iaifi-research-blog/figures/2411_03496/figure_3.png
- /iaifi-research-blog/figures/2411_03496/figure_3.png
pdfUrl: https://arxiv.org/pdf/2411.03496v2
published: '2024-11-05T20:20:08+00:00'
theme: Theoretical Physics
title: Structure factor and topological bound of twisted bilayer semiconductors at
  fractional fillings
wordCount: 1106
---

## The Big Picture

Imagine tuning a radio. Most of the time you hear static or a clear station, but at certain frequencies you catch the moment of transition, where the signal flickers between two completely different broadcasts. Physicists face a similar problem with exotic quantum materials: how do you pinpoint the moment a material switches between radically different quantum phases?

In twisted bilayer semiconductors (sheets of atomically thin material stacked at a slight angle) electrons organize into very different states depending on experimental conditions. At specific **fractional fillings**, corresponding to simple fractions like 1/3 or 2/3 of available quantum states, the system tips into one of two phases. It either becomes a **fractional Chern insulator** (FCI), a fluid-like state where electrons collectively mimic exotic quasiparticles, or a **generalized Wigner crystal** (GWC), where electrons lock into a rigid, periodic arrangement like atoms frozen in a solid. Telling these two apart has been a major experimental challenge.

Researchers at MIT (Timothy Zaklama, Di Luo, and Liang Fu) found a direct diagnostic: the **structure factor**, a quantity that measures how charge clumps and spreads across a material at different length scales, accessible via X-ray or electron scattering. They used it to map the complete phase diagram of twisted molybdenum ditelluride (tMoTe₂) and, in doing so, verified a universal law linking quantum geometry to a topological integer that stays constant even as other conditions vary.

> **Key Insight:** The structure factor reveals a sharp phase transition between topological and crystalline states in twisted semiconductors, and its long-wavelength behavior obeys a universal bound tied directly to the material's topological invariant.

## How It Works

The **static structure factor** S(**q**) measures the likelihood of charge density fluctuations at a given spatial wavelength **q** in the material's ground state. In a crystal, S(**q**) shows sharp **Bragg peaks** at specific wavevectors, spikes that act as a crystallographic fingerprint revealing the regular spacing of charges. In a topological liquid, those peaks are absent, but the small-**q** behavior tells a different story.

The central quantity here is **quantum weight** K, the coefficient describing how fast S(**q**) grows as **q** approaches zero. Quantum weight connects directly to optical conductivity, charge fluctuations, and **many-body quantum geometry**: a measure of how the collective electron quantum state shifts when boundary conditions change.

A recently proven theorem establishes a universal lower bound: K ≥ |C|, where C is the **many-body Chern number**, the integer-valued topological invariant classifying quantum Hall-like states. This bound is saturated in idealized quantum Hall states under strong magnetic fields. The open question was whether it holds for the more complex, field-free FCIs found in moiré materials.

![Figure 1](/iaifi-research-blog/figures/2411_03496/figure_3.png)

To answer this, the team used **band-projected exact diagonalization (ED)**, solving the full quantum many-body problem exactly within the low-energy bands relevant to the physics. They modeled tMoTe₂ at filling fractions ν = 1/3 and 2/3, systematically varying the displacement field D, an electric field perpendicular to the layers that controls the material's topology. At low fields, the relevant bands carry Chern number C = 1, placing electrons in a topological phase. At large fields, the bands become trivial (C = 0).

Their workflow followed three steps:

1. Construct the single-particle continuum model for spin-1/2 holes in the twisted bilayer
2. Diagonalize the full interacting Hamiltonian (including Coulomb repulsion) for small finite-size systems at fixed filling
3. Compute S(**q**) across all momenta and extract quantum weight K from the small-**q** behavior

![Figure 2](/iaifi-research-blog/figures/2411_03496/figure_3.png)

At ν = 1/3 and low displacement fields, S(**q**) shows no Bragg peaks, the hallmark of an FCI liquid. Quantum weight stays firmly above the topological bound. As the displacement field increases past a critical value, the picture changes abruptly.


Bragg peaks suddenly appear at charge-density-wave vectors, momenta corresponding to a crystalline charge pattern that signals electrons settling into a periodic arrangement to minimize mutual repulsion. This is the GWC forming. At the same time, S(**q**) at small **q** drops sharply, falling *below* the topological bound K ≥ |C|. The drop is self-consistent: the GWC has C = 0, so the bound no longer applies. But the discontinuity marks the topological phase transition clearly and quantitatively.


At ν = 2/3, the FCI-to-GWC transition is even sharper. The team also identified a specific twist angle where the FCI's quantum weight nearly saturates the topological bound, meaning the material is as geometrically tight as possible. At larger twist angles, the bound still holds but K significantly exceeds |C|. This echoes the well-known magic angles in twisted bilayer graphene, where flat bands and strong correlations coincide.


The bound held across every computed FCI state, at both 1/3 and 2/3 filling, across all tested twist angles and displacement fields. This provides the first numerical confirmation of the universal inequality for strongly interacting fractional quantum Hall-like systems.


## Why It Matters

This work gives experimentalists a concrete, measurable signature to distinguish topological from crystalline phases in moiré materials without measuring transport or Hall conductivity directly. X-ray scattering and electron energy-loss spectroscopy can probe S(**q**) in real samples, making the framework immediately applicable to ongoing experiments on tMoTe₂ and related systems.

Verifying K ≥ |C| for interacting FCIs is also a foundational result in its own right. It places quantum weight, rooted in many-body quantum geometry, on the same footing as topological invariants. The structure factor becomes a probe of quantum geometry wherever traditional topological diagnostics are difficult or inaccessible.

The approach extends naturally to other fractional fillings, other moiré platforms, and potentially other symmetry classes or dimensions. Open questions remain. Can bound saturation be achieved experimentally? What happens at Jain-sequence fillings like ν = 2/5 or 3/7?

> **Bottom Line:** By computing the structure factor across the tMoTe₂ phase diagram, researchers pinpointed the topological-to-crystalline phase transition and confirmed a universal law linking quantum geometry to topology, giving experimentalists a new tool to read the quantum fingerprints of exotic matter.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects quantum topology, condensed matter experiment, and many-body computation, using a measurable scattering observable to diagnose and characterize exotic quantum phases in moiré semiconductors.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The exact diagonalization framework advances computational methods for strongly correlated quantum systems, with relevance to quantum machine learning and simulation of complex many-body Hamiltonians.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">This paper provides the first numerical verification of the universal topological bound K ≥ |C| for interacting fractional Chern insulators, a foundational result in the theory of topological quantum matter.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend this structure factor framework to other moiré systems and fractional fillings; the paper is available at [arXiv:2411.03496](https://arxiv.org/abs/2411.03496).</span></div></div>
</div>
