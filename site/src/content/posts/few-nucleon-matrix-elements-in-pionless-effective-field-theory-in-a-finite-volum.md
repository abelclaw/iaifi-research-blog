---
abstract: Pionless effective field theory in a finite volume (FVEFT$_{π\!/}$) is investigated
  as a framework for the analysis of multi-nucleon spectra and matrix elements calculated
  in lattice QCD (LQCD). By combining FVEFT$_{π\!/}$ with the stochastic variational
  method, the spectra of nuclei with atomic number $A\in\{2,3\}$ are matched to existing
  finite-volume LQCD calculations at heavier-than-physical quark masses corresponding
  to a pion mass $m_π=806$ MeV, thereby enabling infinite-volume binding energies
  to be determined using infinite-volume variational calculations. Based on the variational
  wavefunctions that are constructed in this approach, the finite-volume matrix elements
  of various local operators are computed in FVEFT$_{π\!/}$ and matched to LQCD calculations
  of the corresponding QCD operators in the same volume, thereby determining the relevant
  one and two-body EFT counterterms and enabling an extrapolation of the LQCD matrix
  elements to infinite volume. As examples, the scalar, tensor, and axial matrix elements
  are considered, as well as the magnetic moments and the isovector longitudinal momentum
  fraction.
arxivId: '2102.04329'
arxivUrl: https://arxiv.org/abs/2102.04329
authors:
- W. Detmold
- P. E. Shanahan
concepts:
- finite-volume pionless eft
- effective field theory
- nuclear matrix elements
- lattice qcd
- finite-volume extrapolation
- stochastic variational method
- monte carlo methods
- renormalization
- quantum field theory
- inverse problems
- bayesian inference
figures:
- /iaifi-research-blog/figures/2102_04329/figure_1.png
- /iaifi-research-blog/figures/2102_04329/figure_1.png
- /iaifi-research-blog/figures/2102_04329/figure_2.png
- /iaifi-research-blog/figures/2102_04329/figure_2.png
- /iaifi-research-blog/figures/2102_04329/figure_3.png
- /iaifi-research-blog/figures/2102_04329/figure_3.png
pdfUrl: https://arxiv.org/pdf/2102.04329v1
published: '2021-02-08T16:34:00+00:00'
theme: Theoretical Physics
title: Few-nucleon matrix elements in pionless effective field theory in a finite
  volume
wordCount: 1050
---

## The Big Picture

Imagine trying to measure the weight of a fish, but you can only do it inside a tiny aquarium. The fish is cramped, its behavior is constrained by the walls, and the measurement you get isn't quite the same as what you'd find in the open ocean.

Now imagine the fish is a nucleus, the aquarium is a finite computational grid, and the "weight" is a fundamental nuclear property — like how strongly a nucleus responds to a magnetic field, or how the quarks inside it share momentum. That's exactly the problem facing physicists who use **Lattice Quantum Chromodynamics (LQCD)** — one of the most powerful tools for computing nuclear properties from first principles.

LQCD works by placing quarks (the tiny constituents of protons and neutrons) and gluons (the force-carriers that bind them) on a discrete spacetime grid and simulating their interactions directly. Every LQCD calculation lives in a finite box, and extracting real-world physics from that box requires careful theoretical bridges. For simple two-particle scattering, those bridges exist. For heavier nuclei and their matrix elements? Until now, the path was far murkier.

This paper by William Detmold and Phiala Shanahan at MIT's Center for Theoretical Physics and IAIFI takes a major step forward. They extend **finite-volume pionless effective field theory (FVEFT_π/)** to nuclear matrix elements for the first time. **Nuclear matrix elements** describe how nuclei respond to external forces — from magnetic fields to the weak nuclear force — and are essential for connecting QCD to experiment. This opens a systematic route from lattice calculations to real nuclear physics.

> **Key Insight:** By combining finite-volume effective field theory with a powerful variational optimization technique, the researchers can take cramped, finite-box LQCD calculations of nuclear properties and reliably extrapolate them to the infinite-volume limit that nature actually lives in.

## How It Works

The foundation is **pionless effective field theory (EFT_π/)**, a framework for nuclear physics at energies too low to produce pions — the lightest quark-composite particles. Rather than tracking every quark and gluon, EFT_π/ describes nucleons interacting through contact forces parameterized by **low-energy constants (LECs)** — numbers that encode all the short-distance physics we don't need to resolve explicitly.

The key idea: run this EFT *inside the same finite box* as the LQCD calculation. Finite-volume effects are long-range phenomena — arising from long-wavelength physics being cut off by the box walls — placing them squarely within EFT_π/'s domain of validity. Match the EFT to LQCD results in the box, fix the LECs, then run the EFT without a box to get infinite-volume predictions.

![Figure 1](/iaifi-research-blog/figures/2102_04329/figure_1.png)

The computational engine is the **stochastic variational method (SVM)**, a technique for building approximate wavefunctions of few-body systems. The SVM constructs trial quantum states as combinations of Gaussian basis functions, then iteratively adjusts them to minimize the system's energy — closely analogous to gradient descent in machine learning. For two- and three-nucleon systems, this yields highly accurate variational wavefunctions both inside the box and in infinite volume.

The workflow proceeds in two matched stages:

1. **Energy matching:** Two- and three-body LECs are tuned to reproduce finite-volume binding energies from NPLQCD collaboration LQCD calculations — computed across three lattice volumes (L ∈ {3.4, 4.5, 6.7} fm) at a pion mass of 806 MeV, roughly six times the physical value, which makes the simulations computationally tractable. With LECs fixed, infinite-volume binding energies follow directly.

2. **Matrix element matching:** Using wavefunctions from stage one, finite-volume matrix elements of external currents are computed within FVEFT_π/ and matched to LQCD calculations of the same operators. This fixes additional **two-body counterterms** — coupling constants encoding how nucleon pairs respond collectively to external probes, beyond what single-nucleon responses predict.

![Figure 3](/iaifi-research-blog/figures/2102_04329/figure_2.png)

The framework covers a wide range of nuclear properties: **scalar matrix elements** (sensitive to how nucleon mass arises from quark condensates), **tensor matrix elements** (related to quark spin distributions), **axial matrix elements** (tied to weak interactions and beta decay), magnetic moments, and the isovector longitudinal momentum fraction. A particularly important case is the axial matrix element, which governs proton-proton fusion in the sun and neutrino-nucleus scattering. Its two-body LEC, L₁,A, has been notoriously difficult to determine — exactly what this framework provides.

![Figure 5](/iaifi-research-blog/figures/2102_04329/figure_3.png)

## Why It Matters

Extrapolating LQCD matrix elements to infinite volume is not a technical footnote — it's a prerequisite for comparing LQCD predictions with experiment. Every finite-volume LQCD result carries contamination from the box walls. Without a systematic way to remove it, the extraordinary computational effort of LQCD cannot be fully translated into measurable physics.

FVEFT_π/ as developed here provides that translation for few-nucleon systems across a wide range of properties simultaneously. It's also more flexible than Lüscher's method — an established model-independent approach formally limited to two- and three-particle systems that doesn't naturally extend to matrix elements of heavier nuclei.

As LQCD calculations gradually approach physical quark masses and larger nuclei, this framework will be ready to interpret them. The immediate next step: applying this machinery at lighter quark masses, closer to physical reality, and extending it to larger nuclei and properties like electromagnetic polarizabilities.

> **Bottom Line:** Detmold and Shanahan have built the theoretical infrastructure to systematically extract infinite-volume nuclear matrix elements from finite-volume lattice QCD — a crucial bridge between first-principles computation and measurable nuclear physics, demonstrated here for scalar, tensor, axial, magnetic, and momentum-fraction properties of A = 2 and 3 nuclei.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges lattice QCD computation and nuclear effective field theory using the stochastic variational method — a technique from quantum chemistry — exemplifying IAIFI's mission of combining modern computational tools with fundamental physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The stochastic variational method applied here — iteratively optimizing basis functions to minimize energy in complex many-body systems — mirrors the variational strategies underlying modern machine learning, demonstrating concrete cross-pollination between nuclear theory and AI methodology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">For the first time, finite-volume pionless EFT is systematically applied to nuclear matrix elements, enabling reliable infinite-volume extrapolations of magnetic moments, axial charges, and other quantities governing weak nuclear processes including stellar fusion and neutrino-nucleus scattering.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend this framework to physical quark masses and larger nuclei as LQCD calculations continue to advance; the full methodology is detailed in arXiv:2101.10520.</span></div></div>
</div>
