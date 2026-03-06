---
abstract: Maximizing the discovery potential of increasingly precise neutrino experiments
  will require an improved theoretical understanding of neutrino-nucleus cross sections
  over a wide range of energies. Low-energy interactions are needed to reconstruct
  the energies of astrophysical neutrinos from supernovae bursts and search for new
  physics using increasingly precise measurement of coherent elastic neutrino scattering.
  Higher-energy interactions involve a variety of reaction mechanisms including quasi-elastic
  scattering, resonance production, and deep inelastic scattering that must all be
  included to reliably predict cross sections for energies relevant to DUNE and other
  accelerator neutrino experiments. This white paper discusses the theoretical status,
  challenges, required resources, and path forward for achieving precise predictions
  of neutrino-nucleus scattering and emphasizes the need for a coordinated theoretical
  effort involved lattice QCD, nuclear effective theories, phenomenological models
  of the transition region, and event generators.
arxivId: '2203.09030'
arxivUrl: https://arxiv.org/abs/2203.09030
authors:
- L. Alvarez Ruso
- A. M. Ankowski
- S. Bacca
- A. B. Balantekin
- J. Carlson
- S. Gardiner
- R. Gonzalez-Jimenez
- R. Gupta
- T. J. Hobbs
- M. Hoferichter
- J. Isaacson
- N. Jachowicz
- W. I. Jay
- T. Katori
- F. Kling
- A. S. Kronfeld
- S. W. Li
- H. -W. Lin
- K. -F. Liu
- A. Lovato
- K. Mahn
- J. Menendez
- A. S. Meyer
- J. Morfin
- S. Pastore
- N. Rocco
- M. Sajjad Athar
- T. Sato
- A. Schwenk
- P. E. Shanahan
- L. E. Strigari
- M. Wagman
- X. Zhang
- Y. Zhao
- B. Acharya
- L. Andreoli
- C. Andreopoulos
- J. L. Barrow
- T. Bhattacharya
- V. Brdar
- Z. Davoudi
- C. Giusti
- Y. Hayato
- A. N. Khan
- D. Kim
- Y. F. Li
- M. Lin
- P. Machado
- M. Martini
- K. Niewczas
- P. Pandey
- A. Papadopoulou
- R. Plestid
- M. Roda
- I. Ruiz Simo
- J. N. Simone
- R. S. Sufian
- J. Tena-Vidal
- O. Tomalak
- Y. -D. Tsai
- J. M. Udias
concepts:
- neutrino-nucleus cross sections
- lattice qcd
- effective field theory
- nuclear many-body theory
- coherent elastic neutrino scattering
- monte carlo methods
- neutrino detection
- standard model
- new physics searches
- scattering amplitudes
- simulation-based inference
figures:
- /iaifi-research-blog/figures/2203_09030/figure_1.png
- /iaifi-research-blog/figures/2203_09030/figure_1.png
- /iaifi-research-blog/figures/2203_09030/figure_2.png
- /iaifi-research-blog/figures/2203_09030/figure_2.png
- /iaifi-research-blog/figures/2203_09030/figure_3.png
- /iaifi-research-blog/figures/2203_09030/figure_3.png
pdfUrl: https://arxiv.org/pdf/2203.09030v2
published: '2022-03-17T02:08:42+00:00'
theme: Theoretical Physics
title: 'Theoretical tools for neutrino scattering: interplay between lattice QCD,
  EFTs, nuclear physics, phenomenology, and neutrino event generators'
wordCount: 1079
---

## The Big Picture

Imagine trying to catch a ghost. Neutrinos — the universe's most abundant massive particles — pass through entire planets without so much as a nudge. Detecting them at all is a triumph of engineering. But detecting them *precisely enough* to answer fundamental questions about the cosmos? That's where things get genuinely hard. And it turns out, the bottleneck isn't the detectors. It's the math.

Next-generation experiments like DUNE — which will fire neutrino beams 1,300 kilometers through bedrock from Fermilab to a detector in South Dakota — aim to settle some of the deepest open questions in physics: Why does matter dominate the universe? What are the actual neutrino masses? Do exotic new particles lurk in the neutrino sector? Answering these questions requires knowing, with precision, exactly how neutrinos interact with atomic nuclei. Right now, those theoretical predictions fall embarrassingly short of what experiments demand.

A collaboration of over 70 physicists — particle theorists, nuclear physicists, astrophysicists, and software engineers — has produced a landmark white paper mapping out what needs to be done to fix this. Their roadmap links the most sophisticated theoretical machinery in physics, charting a coordinated path toward reliable predictions of neutrino-nucleus interactions across a staggering range of energies.

> **Key Insight:** The single biggest obstacle to unlocking new physics with neutrino experiments isn't detector sensitivity — it's theoretical uncertainty in how neutrinos scatter off nuclei. This white paper lays out the coordinated theoretical program needed to solve that problem.

## How It Works

When a neutrino enters a detector, it smashes into a nucleus — a tightly bound clump of protons and neutrons. Physicists must trace the collision's debris backward to reconstruct what the incoming neutrino was doing. That reconstruction requires knowing the probability of every possible interaction across many orders of magnitude in energy: the **cross section**. Computing it accurately is fiendishly difficult.

The white paper organizes the theoretical toolkit into four interconnected layers:

- **Lattice QCD** — numerical simulations of the strong nuclear force (the force that binds quarks into protons and neutrons) on a discrete spacetime grid — provides the most fundamental inputs: how quarks and gluons respond to a neutrino's weak-force kick. Key targets include the **axial form factor** of the nucleon (which governs how quark spins inside a proton or neutron respond to a neutrino interaction) and **two-body currents** (corrections arising when a neutrino interacts with a correlated pair of nucleons rather than just one).

- **Nuclear effective field theories (EFTs)** translate those quark-level inputs into a language applicable to multi-nucleon systems — the actual nuclei inside detectors — systematically accounting for the complex dance of nucleons interacting through the strong force.

- **Nuclear many-body theory** applies these EFTs to real nuclei like argon-40 (the DUNE target) and carbon-12 (used in many test detectors). Methods like **Green's function Monte Carlo** and **coupled cluster theory** compute how the full nucleus absorbs and reemits energy across different reaction channels.

- **Neutrino event generators** — the simulation software (GENIE, NuWro, NEUT, GiBUU) that experiments use to predict detector signals — synthesize all theoretical inputs into coherent, fast simulations running over millions of events.

![Figure 1](/iaifi-research-blog/figures/2203_09030/figure_1.png)

The energy landscape splits the problem into distinct regimes. At tens of MeV (the energy scale of nuclear physics) — the range relevant for supernova neutrinos — theorists must compute exclusive processes down to specific nuclear excited states. Get this wrong, and you lose the astrophysical information needed to reconstruct how neutron stars form.

At GeV energies (the scale of accelerator experiments) relevant for DUNE, the picture fragments further. **Quasi-elastic scattering**, **pion production**, and **deep inelastic scattering** all overlap in a messy transition region no single framework handles cleanly. The paper gives particular attention to **quark-hadron duality** — the empirical observation that averaging over many particle resonances often reproduces predictions from the fundamental theory of the strong force — as a potential bridge across this transition zone.

![Figure 3](/iaifi-research-blog/figures/2203_09030/figure_2.png)

The white paper is frank about event generators: they often incorporate theoretical models inconsistently, and improving them requires sustained, funded collaboration between generator developers and the broader theory community — something the field has historically struggled to sustain.

## Why It Matters

The stakes are concrete. DUNE's primary goal — measuring **CP violation in the lepton sector** (a subtle asymmetry between how neutrinos and antineutrinos behave, which could explain why matter dominates the universe) — depends on comparing oscillation probabilities at the 1–2% level.

If cross section predictions carry 5–10% uncertainties, as they currently do in parts of the relevant energy range, the CP measurement becomes statistically hopeless. The theoretical work outlined here isn't academic overhead. It's prerequisite.

The same machinery reaches beyond DUNE. **Coherent elastic neutrino-nucleus scattering (CEvNS)** — first observed in 2017 and now measured with growing precision — provides a clean window into the weak nuclear charge of nuclei and potentially into new physics. Its cross section depends sensitively on the nuclear form factor and on radiative corrections computed from lattice QCD and nuclear theory. For astrophysical neutrinos, next-generation detectors could capture thousands of events from a Milky Way supernova — but only if theorists supply the cross sections needed to unfold the neutrino energy spectrum from raw detector data.

> **Bottom Line:** Neutrino physics is entering a precision era where theoretical uncertainties, not detector limitations, are the binding constraint on discovery. This white paper charts the coordinated program — linking lattice QCD, nuclear EFTs, many-body theory, and event generators — that the field must execute to realize its full scientific potential.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This white paper exemplifies the computational-theoretical synthesis at IAIFI's core, connecting first-principles lattice QCD calculations with large-scale nuclear many-body simulations and event generators that translate theory into experimental predictions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Machine learning methods are increasingly being applied to accelerate the lattice QCD and nuclear many-body techniques described here, with IAIFI researchers developing equivariant neural networks and normalizing flows to speed up configuration sampling and hadronic matrix element extraction.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The work directly enables measurements of CP violation at DUNE, precise characterization of coherent elastic neutrino-nucleus scattering, and reconstruction of supernova neutrino spectra — all windows into physics beyond the Standard Model.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The roadmap set out here will guide the field's theoretical investments through the DUNE era and beyond; the full white paper is available at arXiv:2203.09030, submitted to the Snowmass 2021 Community Study on the Future of Particle Physics.</span></div></div>
</div>
