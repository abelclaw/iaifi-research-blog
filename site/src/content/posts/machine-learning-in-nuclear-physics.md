---
abstract: "Advances in machine learning methods provide tools that have broad applicability\
  \ in scientific research. These techniques are being applied across the diversity\
  \ of nuclear physics research topics, leading to advances that will facilitate scientific\
  \ discoveries and societal applications.\n  This Review gives a snapshot of nuclear\
  \ physics research which has been transformed by machine learning techniques."
arxivId: '2112.02309'
arxivUrl: https://arxiv.org/abs/2112.02309
authors:
- Amber Boehnlein
- Markus Diefenthaler
- Cristiano Fanelli
- Morten Hjorth-Jensen
- Tanja Horn
- Michelle P. Kuchera
- Dean Lee
- Witold Nazarewicz
- Kostas Orginos
- Peter Ostroumov
- Long-Gang Pang
- Alan Poon
- Nobuo Sato
- Malachi Schram
- Alexander Scheinker
- Michael S. Smith
- Xin-Nian Wang
- Veronique Ziegler
concepts:
- bayesian inference
- uncertainty quantification
- surrogate modeling
- lattice qcd
- monte carlo methods
- classification
- inverse problems
- effective field theory
- regression
- anomaly detection
- particle tracking
- simulation-based inference
- experimental design
figures:
- /iaifi-research-blog/figures/2112_02309/figure_1.png
- /iaifi-research-blog/figures/2112_02309/figure_1.png
- /iaifi-research-blog/figures/2112_02309/figure_2.png
- /iaifi-research-blog/figures/2112_02309/figure_2.png
- /iaifi-research-blog/figures/2112_02309/figure_3.png
- /iaifi-research-blog/figures/2112_02309/figure_3.png
pdfUrl: https://arxiv.org/pdf/2112.02309v2
published: '2021-12-04T11:26:00+00:00'
theme: Theoretical Physics
title: Machine Learning in Nuclear Physics
wordCount: 1077
---

## The Big Picture

Imagine trying to solve a jigsaw puzzle with a trillion pieces, where every piece connects to every other piece in ways governed by quantum mechanics. That is, roughly speaking, what nuclear physicists face every day.

The atomic nucleus — a tiny bundle of protons and neutrons crammed into a space millions of times smaller than a single atom — is one of the most complex physical systems in the universe. Predicting how nuclei behave, how they smash together at high energies, or how they decay requires calculations of staggering difficulty. Classical computational methods strain under the load.

Now, a landmark review co-authored by researchers spanning Jefferson Lab, MIT, Michigan State, Lawrence Berkeley, and a dozen other institutions offers a sweeping panorama of how machine learning is transforming this centuries-old field. From designing particle detectors to taming a long-standing mathematical obstacle that makes certain quantum calculations nearly impossible, the paper catalogs a revolution already underway.

This is not a promise of future breakthroughs. It is a field already transformed.

> **Key Insight:** Machine learning is not just accelerating calculations in nuclear physics — it is enabling entirely new classes of problems to be solved that were previously intractable, from predicting nuclear structure properties to reconstructing particle collisions in real time.

## How It Works

The authors organize ML applications into four major pillars: **nuclear theory**, **experimental methods**, **accelerator science**, and **nuclear data**. Each pillar uses different architectures to address fundamentally different problems.

![Figure 1](/iaifi-research-blog/figures/2112_02309/figure_1.png)

Start with nuclear theory. **Low-energy nuclear theory** — the study of how forces between protons and neutrons determine nuclear structure — has long been limited by quantum-mechanical complexity. With even moderate nuclei containing dozens of interacting particles, exact solutions are computationally forbidden. ML now provides surrogate models that predict nuclear masses, binding energies, and decay rates orders of magnitude faster than traditional methods.

Researchers have applied **Gaussian processes** (statistical techniques that express predictions as probability distributions rather than single values), **Bayesian neural networks** (which track uncertainty alongside predictions), and deep feedforward networks to interpolate and extrapolate nuclear properties across the chart of nuclides — the periodic-table-like map of all known atomic nuclei.

In **Lattice QCD** — the leading computational approach to solving the theory of quarks and gluons — ML tackles two of the hardest outstanding problems. The **sign problem** arises because the mathematical weight assigned to each possible field configuration can become a complex number rather than a simple positive one, causing catastrophic cancellations when summing millions of contributions. ML-based flow models now generate configurations that avoid the worst of these cancellations.

Separately, **normalizing flows** and **generative models** — techniques that learn to sample from complex probability distributions — produce independent lattice field configurations far more efficiently than traditional Markov-chain Monte Carlo methods, which generate configurations one laborious step at a time. This could cut the cost of a single lattice calculation by orders of magnitude.

On the experimental side, the challenges are different but equally brutal:

- **Charged particle tracking** in detectors produces millions of hits per second; ML-based graph neural networks reconstruct particle trajectories in real time with accuracy rivaling hand-tuned algorithms
- **Calorimetry** uses convolutional neural networks to extract energies and positions from pixel-level detector readout
- **Particle identification** and **event classification** use boosted decision trees and deep networks to distinguish signal from noise in flooded data environments
- **Streaming detector readout** poses a data-volume problem that ML-based trigger systems address by compressing and filtering data on the fly, before it can be written to disk

![Figure 2](/iaifi-research-blog/figures/2112_02309/figure_1.png)

Accelerator science adds another dimension. Modern accelerators are impossibly complex machines with thousands of coupled parameters. **ML-based surrogate models** — trained on simulation data — replace expensive physics-based models during real-time optimization, enabling feedback loops fast enough to correct beam instabilities as they emerge. **Adaptive ML** handles the additional wrinkle that accelerator systems are non-stationary: components age, conditions drift, and a model trained yesterday may fail today.

## Why It Matters

What makes this review particularly significant is not any single technique but the convergence it documents. Nuclear physics spans roughly fifteen orders of magnitude in energy scale — from nuclear binding energies of a few MeV (million electron volts) to quark-gluon plasma temperatures exceeding a trillion Kelvin. Experiments at CERN, Jefferson Lab, and RHIC (the Relativistic Heavy Ion Collider) each generate petabytes of data annually.

The theoretical models that interpret this data are among the most computationally expensive in all of science. Machine learning is not just a convenience here — it is becoming infrastructure.

The implications extend well beyond nuclear physics. Techniques developed for this field — uncertainty quantification in neural networks, equivariant architectures that respect physical symmetries, flow-based samplers for quantum field theory — are feeding back into ML research itself. Nuclear physicists are becoming ML innovators, and tools built for hadron spectroscopy (classifying subatomic particles by quark content) or accelerator control are shaping how the broader community thinks about physics-informed machine learning.

Open questions remain sharp. How do we rigorously propagate uncertainties through deep neural networks used as theory emulators? Can generative models ever fully solve the sign problem, or only alleviate it? How do we ensure that ML-based event reconstruction does not introduce subtle biases that corrupt precision measurements? The authors do not shy away from these tensions — the review is honest about both the promise and the open methodological challenges.

> **Bottom Line:** Machine learning has already reshaped nuclear physics across theory, experiment, and infrastructure — this review provides the definitive map of that transformation, revealing a field not waiting for AI but actively co-developing it.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This review, co-authored by MIT IAIFI affiliate Cristiano Fanelli, documents how nuclear physics and machine learning are developing in genuine partnership — with physics problems driving new ML methodology and ML capabilities opening physically inaccessible regimes of nuclear science.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Nuclear physics applications have pioneered physics-informed generative models, uncertainty-aware Bayesian networks, and equivariant architectures that enforce fundamental symmetries — contributions now influencing ML research broadly.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">ML techniques are cracking open previously intractable problems in nuclear structure, lattice QCD at finite density, and real-time detector reconstruction, enabling precision measurements of the fundamental forces governing matter.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The paper anticipates that ML will become standard infrastructure in nuclear science over the next decade, particularly for accelerator control and lattice field theory; see arXiv:2112.02309 for the full review.</span></div></div>
</div>
