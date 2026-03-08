---
abstract: We compute masses of the two lightest glueballs from spectral reconstructions
  of timelike interaction channels of the four-gluon vertex in Landau gauge Yang-Mills
  theory. The Euclidean spacelike dressings of the vertex are calculated with the
  functional renormalisation group. For the spectral reconstruction of these Euclidean
  data, we employ Gaussian process regression. The glueball resonances can be identified
  straightforwardly and we obtain $m_{sc} = 1870(75)~$ MeV as well as $m_{ps} = 2700(120)~$
  MeV, in accordance with functional bound state and lattice calculations.
arxivId: '2212.01113'
arxivUrl: https://arxiv.org/abs/2212.01113
authors:
- Jan M. Pawlowski
- Coralie S. Schneider
- Jonas Turnwald
- Julian M. Urban
- Nicolas Wink
concepts:
- quantum field theory
- spectral methods
- glueball spectroscopy
- renormalization
- inverse problems
- functional renormalization group
- bayesian inference
- kallen-lehmann representation
- regression
- kernel methods
- uncertainty quantification
- lattice gauge theory
- lattice qcd
figures:
- /iaifi-research-blog/figures/2212_01113/figure_1.png
- /iaifi-research-blog/figures/2212_01113/figure_1.png
- /iaifi-research-blog/figures/2212_01113/figure_2.png
- /iaifi-research-blog/figures/2212_01113/figure_2.png
- /iaifi-research-blog/figures/2212_01113/figure_3.png
- /iaifi-research-blog/figures/2212_01113/figure_3.png
pdfUrl: https://arxiv.org/pdf/2212.01113v2
published: '2022-12-02T11:59:31+00:00'
theme: Theoretical Physics
title: Yang-Mills glueball masses from spectral reconstruction
wordCount: 1180
---

## The Big Picture

Imagine trying to find a ghost. Not the Halloween kind, but a particle so elusive that despite decades of searching, physicists have never definitively spotted one in a detector. That's the situation with **glueballs** — hypothetical particles made entirely of gluons, the force-carrying particles that bind quarks together inside protons and neutrons.

Gluons carry their own version of the charge that governs the strong nuclear force — physicists call it "color charge" — which means they can interact with each other directly, not just with quarks. In principle, they can form their own bound states: glueballs. The Standard Model predicts they exist. We just can't find them.

The problem isn't theoretical doubt — it's that glueballs look too much like ordinary particles. Every particle has a fingerprint: a set of properties like mass, spin, and symmetry behavior. Glueballs are expected to have fingerprints matching those of **mesons**, particles also made from quarks and gluons. Every experimental glueball candidate has a plausible conventional explanation.

To make progress, theorists need sharp, reliable mass predictions that experimentalists can actually hunt for — and that requires calculating from first principles, without approximations that sweep the hard physics under the rug. A new collaboration has done exactly that, combining quantum field theory techniques with a machine learning method borrowed from Bayesian statistics. They computed the masses of the two lightest glueballs — the scalar type at **1870 MeV** and the pseudo-scalar type at **2700 MeV** — using a self-consistent approach that sidesteps some of the trickiest obstacles in the field. (An MeV, or megaelectronvolt, is the standard unit of mass in particle physics; a proton weighs about 938 MeV.)

> **Key Insight:** By treating glueball masses as spectral peaks in the four-gluon interaction vertex and using Gaussian process regression to reconstruct real-time dynamics from imaginary-time calculations, the team extracted precise glueball masses without solving a bound-state equation directly.

## How It Works

The core challenge is a familiar one in theoretical physics: the equations governing the strong nuclear force are most tractable in **Euclidean space** — a mathematical trick where time is replaced by imaginary time, turning wild oscillatory integrals into well-behaved ones. But the physical masses of particles live in **Minkowski space**, the real spacetime of the universe.

Getting from one to the other requires inverting a mathematical transform that is famously ill-conditioned — small errors in the input can blow up into large errors in the output. The team's workflow navigates this in three stages:

1. **Compute Euclidean data with the functional renormalization group (fRG).** The **functional renormalization group** is a non-perturbative method — meaning it works even when the interaction strength is too large for standard approximation schemes — that computes how particles interact by integrating out quantum fluctuations scale by scale. The team used fRG results for the **four-gluon vertex** — the interaction amplitude describing four gluons meeting at a point — focusing on channels with the right symmetry properties to correspond to each glueball type.

2. **Identify the right tensor structures.** Different glueballs are distinguished by their **tensor structure** — the geometric shape of how gluon fields combine at the interaction point. For the scalar glueball ($J^{PC} = 0^{++}$, zero spin and symmetric under certain reflections), the natural arrangement of the four-gluon vertex suffices. For the pseudo-scalar ($J^{PC} = 0^{-+}$, which flips sign under those same reflections), the team employs a structure involving the antisymmetric tensor $\varepsilon_{\mu\nu\rho\sigma}$, chosen so the two channels stay orthogonal — they don't bleed into each other. Mixing channels would make spectral reconstruction exponentially harder.

![Figure 1](/iaifi-research-blog/figures/2212_01113/figure_1.png)

3. **Reconstruct the spectral function with Gaussian process regression (GPR).** This is where machine learning enters. **Gaussian process regression** is a Bayesian technique that treats the unknown **spectral function** — a mathematical object encoding all the frequencies at which a quantum field can vibrate, with peaks corresponding to real particles — as a random field with a prior encoding smoothness assumptions. Given the Euclidean data, GPR updates that prior to a posterior, yielding both a best estimate and rigorous uncertainty bands. It handles the ill-posed inversion gracefully: it doesn't claim to know more than the data support.

![Figure 2](/iaifi-research-blog/figures/2212_01113/figure_1.png)

Where the spectral function peaks, a resonance lives — and a resonance is a particle. The scalar glueball appears as a clean peak in the scalar channel; the pseudo-scalar appears in the pseudo-scalar channel.

![Figure 3](/iaifi-research-blog/figures/2212_01113/figure_2.png)

What makes this approach elegant is its self-consistency. Rather than solving a separate bound-state equation — the usual **Bethe-Salpeter approach**, which models two particles attracting each other into a composite state — the team extracts glueball masses directly from the same four-gluon correlation functions used throughout the fRG calculation. The glueballs are already hiding inside the vertex; you just need the right tool to see them.

![Figure 4](/iaifi-research-blog/figures/2212_01113/figure_2.png)

The final results are $m_{sc} = 1870 \pm 75$ MeV for the scalar glueball and $m_{ps} = 2700 \pm 120$ MeV for the pseudo-scalar. These agree well with independent lattice QCD calculations and with functional bound-state methods — a nontrivial consistency check across very different computational approaches.

![Figure 5](/iaifi-research-blog/figures/2212_01113/figure_3.png)

## Why It Matters

Glueball spectroscopy sits at the frontier of our understanding of the strong nuclear force. Finding experimental evidence for glueballs would confirm that gluons — not just quarks — can form stable bound states: a qualitatively new kind of matter. The GlueX experiment at Jefferson Lab and BESIII in Beijing are actively searching, and sharp theoretical mass predictions directly sharpen that hunt.

Beyond the specific physics, this work establishes Gaussian process regression as a serious tool for quantum field theory, not just a curiosity. The ability to extract spectral functions — with uncertainties — from Euclidean correlators is a persistent bottleneck in finite-temperature QCD, transport coefficient calculations, and heavy-ion physics. The team's framework could be applied to quark-gluon plasma properties, transport coefficients, or exotic hadron spectroscopy — anywhere real-time physics must be coaxed out of imaginary-time data.

> **Bottom Line:** By combining functional renormalization group calculations with Gaussian process regression, this work delivers precise, uncertainty-quantified glueball mass predictions that align with lattice results — and provides a blueprint for extracting real-time physics from Euclidean field theory data.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work demonstrates how Gaussian process regression — a tool from Bayesian statistics — solves a long-standing bottleneck in quantum field theory, bridging machine learning methodology and non-perturbative particle physics in a single calculation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Gaussian process regression proves to be a robust, uncertainty-aware method for solving ill-conditioned linear inverse problems in physics, expanding the spectral reconstruction toolkit beyond conventional maximum entropy and neural network approaches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The calculation yields precise masses for the two lightest Yang-Mills glueballs — $m_{sc} = 1870(75)$ MeV and $m_{ps} = 2700(120)$ MeV — providing sharp theoretical benchmarks for ongoing experimental searches at GlueX and BESIII.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions to full QCD, where quark mixing complicates glueball identification, represent the next frontier; this work is affiliated with MIT's IAIFI (NSF AI Institute for Artificial Intelligence and Fundamental Interactions).</span></div></div>
</div>
