---
abstract: X-space schemes are gauge-invariant, regulator-independent renormalization
  schemes that are defined by requiring position-space correlation functions of gauge
  invariant operators to be equal to their noninteracting values at particular kinematic
  points. These schemes can be used to nonperturbatively renormalize composite operators
  in Lattice Quantum Chromodynamics (LQCD), and by computing matching coefficients
  between the X-space scheme and MSbar in the dimensionally-regulated continuum, matrix
  elements calculated with LQCD can be converted to MSbar-renormalized matrix elements.
  Using X-space schemes for Heavy Quark Effective Theory (HQET) operators has the
  additional benefit that appropriate ratios of position-space correlation functions
  cancel the power divergent static-quark self-energy of Lattice HQET nonperturbatively.
  This work presents the O($α_S$) matching coefficients between X-space renormalized
  four-quark flavor-nonsinglet HQET operators relevant for the lifetimes of charm-
  and bottom-hadrons, and four-quark HQET operators relevant for mixing between neutral
  mesons containing a heavy quark, such as B-Bbar mixing.
arxivId: '2404.16191'
arxivUrl: https://arxiv.org/abs/2404.16191
authors:
- Joshua Lin
- William Detmold
- Stefan Meinel
concepts:
- renormalization
- x-space renormalization
- lattice qcd
- effective field theory
- lattice gauge theory
- b-meson mixing
- static quark power divergence
- quantum field theory
- standard model
figures: []
pdfUrl: https://arxiv.org/pdf/2404.16191v1
published: '2024-04-24T20:27:24+00:00'
theme: Theoretical Physics
title: Position-space renormalization schemes for four-quark operators in HQET
wordCount: 1069
---

## The Big Picture

Imagine trying to weigh something, but your scale gives a different reading depending on whether you're measuring in kilograms or pounds, and the conversion factors are only approximately known. That's roughly the situation facing physicists who want to extract precise predictions from lattice QCD calculations about the lifetimes of heavy particles and their quantum behavior.

Lattice QCD simulates the strong nuclear force by modeling spacetime as a discrete 4D grid. It's powerful, but translating grid-based numbers into testable predictions requires a calibration step called **renormalization**. Think of it as adjusting a thermometer against known reference temperatures before trusting it for real measurements.

This calibration becomes especially tricky for **Heavy Quark Effective Theory (HQET)**, which simplifies calculations involving bottom and charm quarks by treating them as essentially stationary. The simplification works well but introduces a mathematical landmine: an enormous spurious term that buries the physical signal unless cancelled with extraordinary precision.

A new paper from researchers at MIT and the University of Arizona solves a key part of this puzzle. They've calculated the full set of translation factors, called **matching coefficients**, that allow lattice results to be converted into the standard notation used when comparing theory with experiment. The payoff: more precise predictions for B meson lifetimes and their oscillation between matter and antimatter.

> **Key Insight:** By defining renormalization conditions entirely in position space using gauge-invariant operators, this approach sidesteps the gauge-fixing headaches of momentum-space schemes and automatically cancels HQET's power divergences, with no extra tuning required.

## How It Works

The workhorse here is the **X-space scheme**, a renormalization recipe that works in position space. It tracks how quantum operators behave at specific physical locations rather than in the abstract momentum domain. This avoids the main pitfall of the most common alternative, **RI-(S)MOM**, which requires "fixing the gauge," a procedure that introduces ghost-like mathematical fields, ambiguities, and contamination from unphysical operators.

X-space sidesteps all of this with a simple condition: the position-space correlation function (how strongly two quantum operators influence each other at fixed separation *x*) must match its free-field value at that separation. Set that ratio to one and you've defined your scheme. No gauge-fixing needed.


For HQET specifically, the scheme gets even cleverer. The heavy quark propagator in the static limit naturally lives in position space as a Wilson line extending in the time direction. The power-divergent self-energy, which would otherwise require a precisely tuned subtraction, cancels automatically when you form appropriate ratios of three-point to two-point correlation functions. The divergence appears identically in numerator and denominator and drops out exactly, nonperturbatively, with no approximation.

The paper treats two distinct operator classes:

- **ΔQ = 0 operators**: flavor-nonsinglet four-quark operators of the form *(Q̄Γq)(q̄Γ'Q)*, controlling the lifetimes of charm and bottom hadrons through the Heavy Quark Expansion
- **ΔQ = 2 operators**: these drive **B–B̄ mixing**, the quantum oscillation between a B meson and its antimatter partner, sensitive to the CKM matrix element |V_td| and to potential new physics


For each class, the authors calculate the O(αS) matching coefficients, the first-order quantum corrections that translate X-space renormalized matrix elements into the **MS̄ scheme** (the standard notation for comparing theory with experiment). This involves evaluating Feynman diagrams in dimensional regularization and tracking operator mixing structure, since some operators mix under renormalization and require matrix-valued matching. Results are checked against known simpler cases.

The calculation builds up from simpler heavy-light bilinear and trilinear operators to the four-quark case. Ratios of decay constants, computable on the lattice, enter the renormalization conditions in a way that makes the scheme self-contained within HQET.


## Why It Matters

Lattice QCD groups running HQET calculations for B-physics phenomenology now have the perturbative matching coefficients they need to convert results into MS̄ and compare directly with experiment. B–B̄ mixing has been measured to sub-percent precision, and theoretical uncertainties currently limit extraction of fundamental parameters like |V_td/V_ts|.

Beyond B physics, this work extends the X-space toolkit in a direction that matters for precision flavor physics more broadly. Gauge invariance, nonperturbative power-divergence cancellation, and clean perturbative matching make X-space schemes an appealing alternative to RI-SMOM for a growing class of operators. As lattice calculations push toward finer discretizations and more physical quark masses, having multiple independently validated renormalization pathways strengthens control over systematic uncertainties.

> **Bottom Line:** This paper delivers the one-loop matching coefficients needed to connect lattice HQET calculations directly to phenomenology using a gauge-invariant, power-divergence-free renormalization scheme, providing a needed technical ingredient for high-precision predictions of B-meson mixing and heavy-hadron lifetimes.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects computational lattice field theory with analytic effective field theory, developing renormalization tools that bridge numerical simulation and perturbative phenomenology, reflecting the kind of cross-disciplinary approach pursued at IAIFI.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The X-space framework's reliance on position-space correlators is well-suited to lattice analysis workflows, and the matching coefficients produced here can be incorporated into data analysis pipelines for lattice QCD calculations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The one-loop matching coefficients for four-quark HQET operators enable more precise determinations of B–B̄ mixing parameters and heavy-hadron lifetimes, directly improving tests of the Standard Model's flavor sector and sensitivity to new physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend these results to higher orders in αS and apply them in full nonperturbative lattice HQET calculations; the paper is available at [arXiv:2404.16191](https://arxiv.org/abs/2404.16191).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Position-space renormalization schemes for four-quark operators in HQET</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2404.16191</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Joshua Lin", "William Detmold", "Stefan Meinel"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">X-space schemes are gauge-invariant, regulator-independent renormalization schemes that are defined by requiring position-space correlation functions of gauge invariant operators to be equal to their noninteracting values at particular kinematic points. These schemes can be used to nonperturbatively renormalize composite operators in Lattice Quantum Chromodynamics (LQCD), and by computing matching coefficients between the X-space scheme and MSbar in the dimensionally-regulated continuum, matrix elements calculated with LQCD can be converted to MSbar-renormalized matrix elements. Using X-space schemes for Heavy Quark Effective Theory (HQET) operators has the additional benefit that appropriate ratios of position-space correlation functions cancel the power divergent static-quark self-energy of Lattice HQET nonperturbatively. This work presents the O($α_S$) matching coefficients between X-space renormalized four-quark flavor-nonsinglet HQET operators relevant for the lifetimes of charm- and bottom-hadrons, and four-quark HQET operators relevant for mixing between neutral mesons containing a heavy quark, such as B-Bbar mixing.</span></div></div>
</div>
