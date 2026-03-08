---
abstract: Neutrino telescopes are gigaton-scale neutrino detectors comprised of individual
  light-detection units. Though constructed from simple building blocks, they have
  opened a new window to the Universe and are able to probe center-of-mass energies
  that are comparable to those of collider experiments. \prometheus{} is a new, open-source
  simulation tailored for this kind of detector. Our package, which is written in
  a combination of \texttt{C++} and \texttt{Python} provides a balance of ease of
  use and performance and allows the user to simulate a neutrino telescope with arbitrary
  geometry deployed in ice or water. \prometheus{} simulates the neutrino interactions
  in the volume surrounding the detector, computes the light yield of the hadronic
  shower and the out-going lepton, propagates the photons in the medium, and records
  their arrival times and position in user-defined regions. Finally, \prometheus{}
  events are serialized into a \texttt{parquet} file, which is a compact and interoperational
  file format that allows prompt access to the events for further analysis.
arxivId: '2304.14526'
arxivUrl: https://arxiv.org/abs/2304.14526
authors:
- Jeffrey Lazar
- Stephan Meighen-Berger
- Christian Haack
- David Kim
- Santiago Giner
- Carlos A. Argüelles
concepts:
- detector simulation
- neutrino detection
- open-source neutrino simulator
- monte carlo methods
- photon propagation
- cherenkov light modeling
- event reconstruction
- scientific workflows
- simulation-based inference
- emulation
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2304_14526/figure_1.png
- /iaifi-research-blog/figures/2304_14526/figure_2.png
pdfUrl: https://arxiv.org/pdf/2304.14526v1
published: '2023-04-27T20:48:22+00:00'
theme: Experimental Physics
title: 'Prometheus: An Open-Source Neutrino Telescope Simulation'
wordCount: 931
---

## The Big Picture

Imagine trying to catch a ghost. Not just any ghost, but one that can pass through the entire Earth without leaving a single trace. Very occasionally, though, it doesn't. That's the challenge of neutrino astronomy.

Neutrinos are the most abundant massive particles in the universe, yet they interact so rarely with matter that detecting them requires building detectors the size of mountains out of water or ice. And before you can build one, you need to simulate it.

Neutrino telescopes like the IceCube Neutrino Observatory (a cubic kilometer of Antarctic ice peppered with over 5,000 light sensors) work by waiting for a neutrino to slam into a water molecule and produce a cascade of charged particles. Those particles, hurtling faster than light travels through ice, emit a blue glow called **Cherenkov radiation**. Reconstructing the original neutrino's direction and energy from that faint flash of light is detective work at the quantum scale, and doing it well requires very detailed simulations.

The problem: every major neutrino telescope collaboration has historically built its own simulation software from scratch, in isolation. A team at Harvard, MIT, and collaborating institutions has now changed that with **Prometheus**, an open-source, general-purpose neutrino telescope simulation that works for any detector geometry, in both ice and water.

> **Key Insight:** Prometheus provides the first open-source, end-to-end simulation framework for neutrino telescopes that works across detector designs, enabling cross-experiment comparisons that weren't practical before.

## How It Works

The simulation pipeline follows a neutrino's journey from deep space to detector, breaking it into four physical stages.

![Figure 1](/iaifi-research-blog/figures/2304_14526/figure_1.png)

1. **Injection.** Prometheus selects where a neutrino interacts, choosing an interaction vertex (the point in space where the collision occurs) within a simulation volume surrounding the detector. The injection geometry is weighted to efficiently sample the interactions that matter most. This step builds on LeptonInjector, the open-source neutrino event generator released by IceCube.

2. **Final state propagation.** The neutrino interaction produces a hadronic shower, a brief, violent spray of particles created when the neutrino smashes into an atomic nucleus, along with an outgoing lepton such as a muon or electron. The lepton then travels through the medium, shedding energy through ionization (knocking electrons off atoms) and bremsstrahlung radiation (light emitted when the charged particle rapidly decelerates). Prometheus uses PROPOSAL, a well-established muon and tau propagator built for neutrino telescopes, to handle this step with full physics detail.

3. **Light yield.** Every energy loss along the lepton's track, and every particle in the hadronic shower, produces photons. A module called Fennel converts these into actual photon counts using parameterizations derived from detailed GEANT4 simulations, covering both electromagnetic and hadronic showers in water and ice.

4. **Photon propagation.** In ice, Prometheus uses PPC (Photon Propagation Code), the same ray tracer IceCube relies on. In water, the team developed their own module, Hyperion, tuned for water's distinct optical properties. Both modules track photons until they're absorbed or reach a sensor.

The entire output is serialized into **Parquet files**, a compact, column-oriented format optimized for fast access and directly compatible with modern machine learning pipelines. That format choice is deliberate.

## Why It Matters

We're in a boom time for neutrino telescope construction. KM3NeT is building two detectors in the Mediterranean. Baikal-GVD is taking shape in a Siberian lake. P-ONE will be deployed off Vancouver Island, and TRIDENT is planned for the South China Sea. IceCube itself is planning a major expansion. Every one of these projects needs simulation software, and until now, every one would have had to build it independently.

![Figure 2](/iaifi-research-blog/figures/2304_14526/figure_2.png)

Prometheus makes something new possible: **cross-experiment reconstruction algorithms**. A machine learning model trained on Prometheus simulations of one detector geometry could, in principle, be adapted for another without starting from scratch. This is a big deal for the growing role of deep learning in neutrino astronomy, where neural networks reconstruct particle directions and energies from raw photon arrival patterns. The shared output format also means analysis techniques developed for IceCube can be benchmarked directly against a KM3NeT configuration.

There's a democratization angle too. Neutrino telescope simulation software has traditionally lived inside large collaborations, accessible only to members. A graduate student designing a novel detector or a machine learning researcher developing new reconstruction methods can now reach for the same simulation quality as the major experiments.


The paper includes benchmark checks validating Prometheus output against known results, plus performance evaluations showing it balances speed and physical accuracy well. The C++/Python architecture keeps computationally intensive steps fast while the user-facing interface stays approachable.

> **Bottom Line:** Prometheus turns neutrino telescope simulation from a per-collaboration effort into shared infrastructure, lowering the barrier to entry for new detectors and making it possible to build ML algorithms that work across experiments.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">Prometheus sits at the intersection of high-energy astrophysics and computational physics, providing simulation infrastructure for developing and benchmarking machine learning reconstruction techniques across different neutrino telescope experiments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The Parquet output format and geometry-agnostic design make Prometheus a natural data source for ML-based event reconstruction, allowing neural networks trained on one detector to be transferred and tested on others.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By unifying simulation for ice- and water-based neutrino telescopes, including IceCube, KM3NeT, Baikal-GVD, P-ONE, and TRIDENT, Prometheus accelerates our ability to study astrophysical neutrinos at energies that probe fundamental interactions at the TeV scale and beyond.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future development will focus on extending Prometheus to upcoming detector designs and tighter integration with ML-based analysis frameworks; the paper is available at [arXiv:2304.14526](https://arxiv.org/abs/2304.14526).</span></div></div>
</div>
