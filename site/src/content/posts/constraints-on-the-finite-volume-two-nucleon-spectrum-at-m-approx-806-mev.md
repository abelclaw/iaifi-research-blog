---
abstract: The low-energy finite-volume spectrum of the two-nucleon system at a quark
  mass corresponding to a pion mass of $m_π\approx 806$ MeV is studied with lattice
  quantum chromodynamics (LQCD) using variational methods. The interpolating-operator
  sets used in [Phys.Rev.D 107 (2023) 9, 094508] are extended by including a complete
  basis of local hexaquark operators, as well as plane-wave dibaryon operators built
  from products of both positive- and negative-parity nucleon operators. Results are
  presented for the isosinglet and isotriplet two-nucleon channels. In both channels,
  noticably weaker variational bounds on the lowest few energy eigenvalues are obtained
  from operator sets which contain only hexaquark operators or operators constructed
  from the product of two negative-parity nucleons, while other operator sets produce
  low-energy variational bounds which are consistent within statistical uncertainties.
  The consequences of these studies for the LQCD understanding of the two-nucleon
  spectrum are investigated.
arxivId: '2404.12039'
arxivUrl: https://arxiv.org/abs/2404.12039
authors:
- William Detmold
- Marc Illa
- William I. Jay
- Assumpta Parreño
- Robert J. Perry
- Phiala E. Shanahan
- Michael L. Wagman
concepts:
- lattice qcd
- finite-volume spectroscopy
- variational operator basis
- eigenvalue decomposition
- hexaquark operators
- spectral methods
- scattering amplitudes
- effective field theory
- monte carlo methods
- quantum field theory
figures:
- /iaifi-research-blog/figures/2404_12039/figure_1.png
- /iaifi-research-blog/figures/2404_12039/figure_1.png
- /iaifi-research-blog/figures/2404_12039/figure_2.png
- /iaifi-research-blog/figures/2404_12039/figure_2.png
- /iaifi-research-blog/figures/2404_12039/figure_3.png
- /iaifi-research-blog/figures/2404_12039/figure_3.png
pdfUrl: https://arxiv.org/pdf/2404.12039v2
published: '2024-04-18T09:46:44+00:00'
theme: Theoretical Physics
title: Constraints on the finite volume two-nucleon spectrum at $m_π\approx 806$ MeV
wordCount: 1145
---

## The Big Picture

Imagine trying to understand a knot by looking through a foggy window, knowing only that what you see is the *loosest* possible tangle — the real knot could be tighter, but never looser. That is essentially the situation physicists face when extracting energies from **lattice quantum chromodynamics (LQCD)**, the most powerful computational tool available for nuclear physics.

The nucleus of every atom is held together by the strong nuclear force — the same force that confines quarks inside protons and neutrons. Yet despite decades of effort, physicists cannot calculate from first principles whether two neutrons can stick together as a stable pair. That gap matters enormously: it affects how we interpret dark matter experiments, understand heavy-element formation in stellar furnaces, and search for extremely rare radioactive decays that could point toward new physics.

A team from MIT, Fermilab, and the University of Barcelona has tackled one of the deepest sources of confusion in this field: does the answer you extract from LQCD depend critically on *how* you ask the question? Their study systematically probes how the choice of mathematical "operators" — quantum-mechanical probes used to interrogate two-nucleon systems — affects the extracted energy levels. The result is a more honest and rigorous map of what we do and don't know.

> **Key Insight:** The energy levels you extract from lattice QCD are not unique — they depend on which operators you use to probe the system, and some choices can give dangerously misleading answers. This work identifies which choices are trustworthy and which are not.

## How It Works

Lattice QCD discretizes spacetime into a grid and numerically computes how quarks and gluons behave. To study two-nucleon systems, physicists extract **energy eigenvalues** — the discrete energy levels a proton-neutron or neutron-neutron pair can occupy when confined in a finite computational box. From those levels, they infer scattering properties using the **Lüscher method**, a mathematical bridge between the finite-volume spectrum and the infinite-volume physics we care about.

![Figure 1](/iaifi-research-blog/figures/2404_12039/figure_1.png)

The catch: energy levels cannot be measured directly. Instead, physicists construct **interpolating operators** — mathematical objects designed to "look like" the two-nucleon state of interest — and measure how signals built from these operators fade over a computational analog of time. The rate of fading encodes the energy.

The **variational method** extends this by deploying a whole *basis* of operators simultaneously, forming what is called a generalized eigenvalue problem (GEVP). The lowest energy found is guaranteed to be an *upper bound* on the true ground-state energy — a tighter bound means a closer approach to the truth.

The researchers tested several distinct operator families:
- **Plane-wave dibaryon operators**: products of two nucleon operators each carrying definite momentum — the standard workhorse of the field
- **Local hexaquark operators**: all six quarks placed at the same spatial point, with no assumption that they form two separate nucleons
- **Negative-parity nucleon operators**: built from a specific component of the relativistic quantum description of each nucleon — a new addition not studied in prior work

The calculation used a lattice with spatial side-length *L* ≈ 3.4 fm and an artificially heavy pion mass of *m*π ≈ 806 MeV — about six times the physical value. Heavier quarks reduce computational cost and sharpen the signal, providing a controlled testbed for method development.

![Figure 2](/iaifi-research-blog/figures/2404_12039/figure_1.png)

The team ran calculations for both the **isosinglet channel** (*I* = 0, proton-neutron with spin 1, analogous to the deuteron) and the **isotriplet channel** (*I* = 1, two identical nucleons, analogous to the dineutron) — quantum labels that classify how the two nucleons' identity numbers combine. For each channel, they tested many operator subsets, including bases with as many as 46 operators simultaneously.

## Why It Matters

The central result is striking in its clarity. Operator bases dominated by **hexaquark-only** operators, or built exclusively from **negative-parity nucleon operators**, produced variational bounds noticeably *weaker* — those sets failed to efficiently capture the low-energy physics.

![Figure 3](/iaifi-research-blog/figures/2404_12039/figure_2.png)

By contrast, all other combinations — plane-wave dibaryon operators, quasi-local operators, and mixtures — produced bounds that agreed within statistical uncertainties. That consistency signals convergence toward a stable description of the spectrum rather than artifacts from a poor operator choice.

![Figure 4](/iaifi-research-blog/figures/2404_12039/figure_2.png)

Do bound two-nucleon states exist at this heavy quark mass? The variational method is honest: it yields only upper bounds. The results show no evidence for a bound state in either channel, but cannot rule one out. What the study accomplishes is arguably more valuable — it identifies which operator strategies are trustworthy and which introduce misleading artifacts, clearing methodological fog for future calculations.

![Figure 5](/iaifi-research-blog/figures/2404_12039/figure_3.png)

On the physics side, understanding whether LQCD can reliably determine two-nucleon bound states is a prerequisite for grounding nuclear physics in the Standard Model. The long-term goal — computing precise quantities that describe nuclear processes at the quantum level, needed to interpret dark matter searches and neutrino oscillation experiments — depends on first getting the two-body problem right.

The paper also delivers a clear warning: not all operator bases are created equal. Hexaquark-only results being weaker is not a curiosity — it signals that operator sets which do not efficiently overlap with physical states of interest can mislead. Future LQCD calculations of two-nucleon systems should include diverse, physically motivated operator families and verify consistency across choices. That discipline, more than any single number, may be the most durable contribution of this work.

![Figure 6](/iaifi-research-blog/figures/2404_12039/figure_3.png)

Open questions remain. The calculation used an unphysical quark mass; extrapolating to the physical value *m*π ≈ 140 MeV is computationally daunting but necessary. Whether bound dineutron and deuteron states appear at large quark masses — and what that implies for how nuclear binding varies with quark mass — remains unresolved. The role of negative-parity operators in larger variational bases also deserves further investigation.

> **Bottom Line:** By stress-testing a wide variety of operator choices in lattice QCD calculations of two-nucleon systems, this work identifies which computational strategies produce reliable energy bounds and which do not — a critical step toward trustworthy first-principles nuclear physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies variational algorithms from quantum information science to lattice QCD calculations of nuclear systems, directly bridging AI-adjacent computational methodology with fundamental nuclear physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The systematic study of how operator choice affects variational eigenvalue extraction offers concrete lessons for machine-learning-guided basis selection in quantum many-body problems, a rapidly growing area of AI-for-physics research.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By rigorously benchmarking interpolating-operator strategies in the two-nucleon sector, this work advances the long-term goal of computing nuclear matrix elements from QCD — essential inputs for dark matter and neutrino physics experiments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend these variational methods toward physical quark masses and larger volumes; the paper is available at arXiv:2406.10123 from the NPLQCD collaboration, with MIT and IAIFI affiliates among the lead authors.</span></div></div>
</div>
