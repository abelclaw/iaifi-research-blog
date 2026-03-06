---
abstract: The pseudoscalar meson light-cone distribution amplitudes (LCDAs) are essential
  non-perturbative inputs for a range of high-energy exclusive processes in quantum
  chromodynamics. In this proceedings, progress towards a determination of the low
  Mellin moments of the pion and kaon LCDAs by the HOPE Collaboration is reported.
arxivId: '2503.12198'
arxivUrl: https://arxiv.org/abs/2503.12198
authors:
- S. -P. Alex Chang
- William Detmold
- Anthony V. Grebe
- Issaku Kanamori
- C. -J. David Lin
- Robert J. Perry
- Yong Zhao
concepts:
- hope method
- light-cone distribution amplitudes
- lattice qcd
- effective field theory
- mellin moments
- renormalization
- quantum field theory
- monte carlo methods
- regression
- eigenvalue decomposition
figures:
- /iaifi-research-blog/figures/2503_12198/figure_1.png
- /iaifi-research-blog/figures/2503_12198/figure_1.png
- /iaifi-research-blog/figures/2503_12198/figure_2.png
- /iaifi-research-blog/figures/2503_12198/figure_2.png
- /iaifi-research-blog/figures/2503_12198/figure_3.png
- /iaifi-research-blog/figures/2503_12198/figure_3.png
pdfUrl: https://arxiv.org/pdf/2503.12198v1
published: '2025-03-15T16:35:44+00:00'
theme: Theoretical Physics
title: Extracting the distribution amplitude of pseudoscalar mesons using the HOPE
  method
wordCount: 1089
---

## The Big Picture

Imagine a pion — one of the most common particles in the universe — zipping along at nearly the speed of light. Inside it, a quark and an antiquark are locked together by the strong nuclear force, sharing momentum in some proportion. If you could freeze that particle mid-flight and ask "who's carrying how much of the momentum right now?", the answer would follow a probability distribution called the **light-cone distribution amplitude**, or LCDA. That distribution is an essential ingredient in calculating the outcomes of high-energy collisions at facilities like the Large Hadron Collider.

The problem: this distribution is fiendishly hard to compute from first principles. The strong force — described by **quantum chromodynamics (QCD)** — behaves very differently at different energy scales. At high energies, step-by-step approximation techniques work well. At the lower energies governing a pion's internal structure, they break down entirely.

Physicists have long relied on **lattice QCD**, which discretizes spacetime onto a grid for numerical computation on supercomputers. But there's a fundamental mismatch: LCDAs are defined along a *light-like* direction — a path traveling at the speed of light — and lattice calculations work in a mathematical framework where such paths don't exist.

The HOPE Collaboration, spanning MIT, Fermilab, RIKEN, Argonne, and institutions in Taiwan and Spain, has developed an ingenious workaround. They report progress computing the low **Mellin moments** — statistical averages that quantify the shape of the distribution — of the LCDAs for pions and kaons, using the **Heavy-Quark Operator Product Expansion (HOPE)** method.

> **Key Insight:** By introducing a fictitious heavy quark as a mathematical probe, the HOPE method converts an incalculable light-like quantity into ordinary lattice QCD correlation functions — making the unmeasurable measurable.

## How It Works

The HOPE method sidesteps the light-like operator entirely. Instead of computing the LCDA directly, researchers calculate a quantity involving two axial-vector currents built from light quarks *and* a fictional heavy quark that doesn't exist in nature. This fictitious particle — a mathematical scaffold, not a real constituent — allows the team to probe a meson's internal structure using currents that can be placed at standard lattice spacetime separations.

The connection back to the LCDA comes through the **Operator Product Expansion (OPE)** — a technique that simplifies the product of two field operators when they are close together in spacetime, expressing it as a sum of simpler terms with calculable coefficients. When the heavy quark is sufficiently massive, the two-current matrix element (a quantity encoding the meson's internal structure as probed by those currents) can be written as a sum over **Gegenbauer moments** — a mathematical decomposition of the LCDA's shape — weighted by perturbatively calculable coefficients.

In practice, the calculation proceeds in three steps:

1. **Compute correlation functions on the lattice.** The team calculates two-point and three-point correlation functions using lattice QCD, employing the **Generalized Eigenvalue Problem (GEVP)** — a linear-algebra technique for disentangling contributions from multiple quantum states — to construct an optimized operator that suppresses excited-state contamination.

2. **Extract the hadronic matrix element.** By forming a ratio of three-point to two-point correlators at large time separations, the researchers isolate the hadronic tensor $R_M^{\mu\nu}(t^-, p, q)$ — a structured object encoding how the meson responds to the two current insertions — as a function of momentum and current separation.

3. **Fit to the HOPE formula.** The extracted matrix element is fit to the one-loop HOPE expression, which predicts its dependence on kinematic variables in terms of the Gegenbauer moments $\phi_{M,n}$.

![Figure 1](/iaifi-research-blog/figures/2503_12198/figure_1.png)

The fitting procedure uses both the $t^-$-even and $t^-$-odd components of the hadronic matrix element — two independent observables providing complementary sensitivity to the distribution's moments. These Gegenbauer moments convert to **Mellin moments** $\langle\xi^n\rangle_M$, representing the average value of $\xi^n$ (where $\xi$ is the momentum fraction imbalance between quark and antiquark) weighted by the LCDA.

![Figure 3](/iaifi-research-blog/figures/2503_12198/figure_2.png)

The team applied this procedure to both the pion and the kaon using lattice ensembles with physical or near-physical quark masses. The kaon is particularly interesting: it contains a strange quark paired with an up or down antiquark, creating a **flavor asymmetry**. This means the kaon's LCDA is not symmetric around $\xi = 0$, and its odd Mellin moments are nonzero — a direct signature of SU(3) flavor-symmetry breaking with real phenomenological consequences.

![Figure 5](/iaifi-research-blog/figures/2503_12198/figure_3.png)

Systematic uncertainties are carefully tracked throughout, including higher-twist contamination (corrections from subleading OPE terms), renormalization scale dependence (sensitivity to the energy scale at which coupling constants are defined), and discretization artifacts from the finite lattice spacing.

## Why It Matters

LCDAs enter directly into predictions for **exclusive processes** — precisely measured reactions where specific particles go in and specific particles come out, such as the pion electromagnetic form factor, B-meson decays, and transition form factors relevant to Standard Model tests. Many tensions between theory and experiment in flavor physics hinge on the precise values of these non-perturbative quantities. Without accurate distribution amplitudes, theoretical predictions lose interpretive power, and experimental signals can't be confidently read as evidence for new physics.

The HOPE method is one of several recently developed approaches to circumventing the light-cone problem in lattice QCD — a family that includes quasi-LCDAs, pseudo-LCDAs, and the Compton amplitude method. What distinguishes HOPE is its systematic use of heavy-quark expansion technology, providing a rigorous theoretical framework with clearly defined power corrections. As lattice simulations improve and computing resources scale up, methods like HOPE will become indispensable for supplying the non-perturbative inputs that high-energy experiments need to push toward the energy frontier.

> **Bottom Line:** The HOPE Collaboration has demonstrated a working, systematically controlled method for extracting pion and kaon distribution amplitudes from lattice QCD — bringing precision QCD predictions for exclusive processes meaningfully closer to reality.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges lattice QCD, heavy-quark effective theory, and perturbative QCD, requiring tight integration across computational physics, quantum field theory, and high-performance computing.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The sophisticated fitting and statistical analysis infrastructure — handling correlated multi-dimensional data with systematic uncertainties — mirrors core challenges in machine learning and could inform data-driven approaches to extracting structure functions more broadly.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">First-principles extraction of pion and kaon light-cone distribution amplitudes removes a longstanding non-perturbative bottleneck in QCD, sharpening theoretical predictions for exclusive decay processes central to Standard Model tests.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend these results to the continuum and physical quark mass limits with improved statistics and finer lattice spacings; this proceedings summarizes results presented at LATTICE2024, with the full analysis forthcoming.</span></div></div>
</div>
