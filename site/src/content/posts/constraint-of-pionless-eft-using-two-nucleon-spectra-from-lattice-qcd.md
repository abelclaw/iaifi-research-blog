---
abstract: Finite-volume pionless effective field theory (FVEFT$_{ π\!/ }$) at next-to-leading
  order (NLO) is used to analyze the two-nucleon lattice QCD spectrum of Ref.~\cite{Amarasinghe:2021lqa},
  performed at quark masses corresponding to a pion mass of approximately $800 $ MeV.
  Specifically, the effective theory is formulated in finite volume, and variational
  sets of wave functions are optimized using differential programming. Using these
  wave functions projected to the appropriate finite-volume symmetry group, variational
  bounds from FVEFT$_{π\!/ }$ are obtained for the ground state, as well as excited
  states. By comparison with the lattice QCD GEVP spectrum, different low energy constants
  (LECs) are constrained. Relativistic corrections are incorporated, allowing for
  the extractions of NLO LECs, as well as the leading $s$-$d$-wave mixing term in
  the deuteron channel.
arxivId: '2305.06313'
arxivUrl: https://arxiv.org/abs/2305.06313
authors:
- William Detmold
- Fernando Romero-López
- Phiala E. Shanahan
concepts:
- lattice qcd
- effective field theory
- finite-volume eft
- hamiltonian systems
- variational wave functions
- group theory
- eigenvalue decomposition
- differential programming
- lagrangian methods
- renormalization
- bayesian inference
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2305_06313/figure_1.png
- /iaifi-research-blog/figures/2305_06313/figure_2.png
- /iaifi-research-blog/figures/2305_06313/figure_3.png
pdfUrl: https://arxiv.org/pdf/2305.06313v1
published: '2023-05-10T17:01:10+00:00'
theme: Theoretical Physics
title: Constraint of pionless EFT using two-nucleon spectra from lattice QCD
wordCount: 1177
---

## The Big Picture

Imagine trying to understand how a skyscraper stands without being able to study its steel beams directly — you can only watch the building sway in the wind. Nuclear physicists face something analogous every day. The theory called **Quantum Chromodynamics (QCD)** describes the strong nuclear force, which binds tiny particles called quarks together into protons and neutrons, and then binds those into atomic nuclei. But the math is so ferociously complicated that even calculating how two protons interact from scratch pushes supercomputers to their limits. So physicists build bridges.

One of those bridges is called **pionless effective field theory** — a simplified description of nuclear forces that deliberately sets aside certain short-range particles called pions and focuses only on what matters at low energies. Think of it like replacing an intricate gear mechanism with a simple spring: you lose some details, but you gain the ability to actually calculate something useful. The challenge is figuring out how stiff that spring should be — determining the fundamental constants that make the theory accurate. That requires comparing predictions against hard numerical data from full QCD simulations.

A team from MIT's Center for Theoretical Physics and IAIFI has now demonstrated a powerful new pipeline for exactly this calibration. They used **lattice QCD** — a method that simulates the strong force on a discrete grid of space-time points, like pixels in a photograph — together with **differential programming**, an optimization technique borrowed from machine learning, to pin down nuclear force parameters at a new level of precision.

> **Key Insight:** By directly matching a finite-volume effective theory to lattice QCD energy spectra — including excited states — and optimizing variational wave functions with machine learning tools, the researchers extracted next-to-leading order nuclear force parameters that were previously inaccessible.

## How It Works

The story begins with a dataset: a detailed two-nucleon **energy spectrum** — a map of all the distinct energy levels that two nucleons (protons or neutrons) can occupy together — computed in a previous lattice QCD simulation. That simulation used artificially heavy quark masses, corresponding to a pion mass of roughly **800 MeV** (megaelectronvolts; about five times the physical value). Heavier quarks make simulations cheaper while still allowing the methodology to be validated. The spectrum includes ground states, **excited states** (higher-energy configurations), and states with nonzero total momentum — giving the theory many more data points to fit against.

The researchers formulate **finite-volume pionless EFT (FVEFTπ/)** directly inside the simulation box — matching the same finite, discrete space used by the lattice QCD calculation. This is a key architectural choice. Rather than extrapolating lattice results to infinite volume first and then matching to the EFT, they work entirely within the finite volume at every stage, eliminating a source of uncertainty.

![Figure 1](/iaifi-research-blog/figures/2305_06313/figure_1.png)

The EFT includes interactions up to **next-to-leading order (NLO)** — going beyond the simplest possible interactions to include terms with up to two derivatives, capturing more subtle distance-dependent effects. The theory contains several **low energy constants (LECs)**: numbers encoding the strength of nuclear interactions that must be determined by matching to data. The full set includes:

- Leading-order constants for the **deuteron** (spin-1 proton-neutron bound state) and **dineutron** (two-neutron system) channels
- NLO derivative corrections and relativistic corrections to the kinetic energy
- A term controlling **s-d wave mixing** in the deuteron — a subtle quantum effect where the nucleons carry a small admixture of angular momentum-2

The methodological centerpiece is a **variational approach** powered by differential programming. In a variational approach, you make an educated guess at the shape of a quantum wave function — the mathematical object describing how likely the particles are to be found in any configuration — and then systematically improve that guess until you reach the lowest possible energy. The team builds trial wave functions from **correlated Gaussians**, flexible multi-parameter functions that capture complex spatial correlations between the two nucleons.

Rather than tuning these by hand, they use automatic differentiation — the same algorithmic backbone as deep learning — to efficiently minimize the energy and find optimal wave function parameters for each set of LECs.

![Figure 2](/iaifi-research-blog/figures/2305_06313/figure_2.png)

The full workflow runs as follows:

1. Start with a candidate set of LECs
2. Optimize correlated Gaussian wave functions using differential programming to get variational energy bounds
3. Project those wave functions onto the appropriate **irreducible representations** of the cubic symmetry group — translating them into the limited set of rotations possible within a cube-shaped box, rather than in open space
4. Compare the resulting energy levels against the lattice QCD spectrum
5. Adjust the LECs until the match is optimized

By fitting simultaneously to ground states, excited states, and multiple symmetry sectors, the team disentangles effects that would be degenerate with fewer data points. The excited-state spectrum is particularly valuable: different NLO operators shift different energy levels in distinct ways, allowing each LEC to be separately constrained.

![Figure 3](/iaifi-research-blog/figures/2305_06313/figure_3.png)

## Why It Matters

The immediate physics payoff is a set of well-constrained NLO LECs for pionless EFT at these heavy quark masses — including the first variational bound on the s-d mixing parameter in the deuteron channel. But the deeper significance is methodological. This work shows that the finite-volume EFT approach can serve as a genuine alternative to the conventional **quantization condition** formalism — a standard mathematical technique that relates energy levels to scattering amplitudes, but which grows cumbersome for coupled channels and higher partial waves.

The differential programming framework also opens a door. As lattice QCD computations inch closer to physical quark masses — where simulations are more expensive but results more directly applicable to real nuclei — the optimization machinery scales naturally. The same pipeline could absorb richer lattice spectra, higher-order EFT corrections, and eventually three-nucleon systems, feeding parameters into nuclear structure calculations of heavier nuclei. Each calibrated EFT parameter is one more link in the chain from quarks and gluons to the structure of atomic nuclei.

> **Bottom Line:** By pairing lattice QCD spectra with machine-learning-optimized variational wave functions, this work pushes nuclear EFT calibration to next-to-leading order precision and establishes a scalable framework for connecting QCD simulations to the structure of real nuclei.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work exemplifies the IAIFI mission by applying differential programming — a tool from machine learning — directly to the calibration of nuclear effective field theory against first-principles QCD data, creating a seamless bridge between computational physics and AI methodology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The use of automatic differentiation for variational wave-function optimization demonstrates how deep learning infrastructure can accelerate precision calculations in quantum many-body physics well beyond neural-network-based approaches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The study extracts next-to-leading order low energy constants and places the first variational bound on s-d wave mixing in the two-nucleon system, advancing the program of deriving nuclear forces directly from QCD.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend this framework to physical pion masses and three-nucleon systems, with the potential to inform nuclear structure calculations across the periodic table; the paper is available at arXiv:2408.00082.</span></div></div>
</div>
