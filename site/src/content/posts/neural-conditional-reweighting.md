---
abstract: There is a growing use of neural network classifiers as unbinned, high-dimensional
  (and variable-dimensional) reweighting functions. To date, the focus has been on
  marginal reweighting, where a subset of features are used for reweighting while
  all other features are integrated over. There are some situations, though, where
  it is preferable to condition on auxiliary features instead of marginalizing over
  them. In this paper, we introduce neural conditional reweighting, which extends
  neural marginal reweighting to the conditional case. This approach is particularly
  relevant in high-energy physics experiments for reweighting detector effects conditioned
  on particle-level truth information. We leverage a custom loss function that not
  only allows us to achieve neural conditional reweighting through a single training
  procedure, but also yields sensible interpolation even in the presence of phase
  space holes. As a specific example, we apply neural conditional reweighting to the
  energy response of high-energy jets, which could be used to improve the modeling
  of physics objects in parametrized fast simulation packages.
arxivId: '2107.08979'
arxivUrl: https://arxiv.org/abs/2107.08979
authors:
- Benjamin Nachman
- Jesse Thaler
concepts:
- conditional reweighting
- likelihood ratio
- simulation-based inference
- detector simulation
- loss function design
- classification
- jet physics
- phase space interpolation
- collider physics
- surrogate modeling
- monte carlo methods
- density estimation
figures:
- /iaifi-research-blog/figures/2107_08979/figure_1.png
- /iaifi-research-blog/figures/2107_08979/figure_2.png
- /iaifi-research-blog/figures/2107_08979/figure_3.png
pdfUrl: https://arxiv.org/pdf/2107.08979v2
published: '2021-07-19T15:55:41+00:00'
theme: Experimental Physics
title: Neural Conditional Reweighting
wordCount: 1082
---

## The Big Picture

Imagine assembling the world's most accurate city map using two imperfect tools: a satellite image that blurs street-level details, and a sketch map that captures ground-level texture but gets distances wrong. Neither alone is what you want — you need to borrow the accuracy from each without letting their individual flaws contaminate the result.

That's the challenge physicists face when simulating particle collisions at ATLAS and CMS — the giant detectors at CERN. Producing realistic collision data requires two chained steps: a **physics simulator** modeling the underlying particle interactions, and a **detector simulator** modeling how particles register in the hardware. Running the most precise versions of both is computationally brutal.

So physicists mix and match — using fast, approximate simulators and applying statistical corrections called **reweighting** to make the output statistically match the expensive, precise version. Reweighting assigns each simulated event a numerical weight: boost some events, suppress others, until the fast simulation mimics the expensive one.

Until now, those corrections treated the physics model and the detector model as inseparable. Benjamin Nachman and Jesse Thaler have introduced a cleaner approach: **neural conditional reweighting**, which separates detector corrections from physics corrections and applies them independently using a neural network smart enough to handle gaps in the data.

> **Key Insight:** Instead of averaging a detector correction over all possible particle energies, neural conditional reweighting computes the correction *for each specific particle energy* — making simulation improvements far more portable and precise.

## How It Works

The standard approach, **marginal reweighting**, trains a neural network to distinguish events from two simulation samples. Because the optimal classifier is mathematically equivalent to the **likelihood ratio** — a measure of how much more probable one distribution is than the other at any given point — its output directly gives the reweighting function. Simple and powerful, but it averages over everything you're not explicitly modeling. Apply a correction derived from jets (collimated sprays of particles) peaked at 500 GeV to a sample peaked at 1 TeV, and you've baked in an energy-dependence you can't separate.

![Figure 1](/iaifi-research-blog/figures/2107_08979/figure_1.png)

Conditional reweighting instead computes the ratio of **conditional probability densities**: *q(x|x′) / p(x|x′)*. Here:

- *x* is the detector-level observable (like reconstructed jet energy)
- *x′* is the particle-level truth — the "true" energy before detector smearing
- *q(x|x′)* means "the probability of observing *x* given that the true value is *x′*"

Instead of one correction number per detector observable, you get a correction that depends on both the detector output *and* the particle-level input — a surface rather than a curve.

The naive approach would require two separate classifiers: one for the **joint distribution** (how *x* and *x′* vary together) and one for the **marginal distribution** (how *x′* behaves on its own, ignoring *x*). You'd then divide them. Nachman and Thaler instead derive a **custom loss function** that achieves conditional reweighting in a *single* training run.

The real payoff appears in handling **phase space holes** — regions of parameter space where no training data exists. Standard likelihood-ratio approaches go haywire in these gaps. The new loss function forces the network to produce physically sensible interpolated values across empty regions by leveraging information from neighboring populated areas — crucial for realistic physics where complete coverage is never guaranteed.

**Validation on Gaussians and Jets.** On controlled Gaussian examples with overlapping distributions, the conditional reweighter recovers the correct weight function without bias. More impressively, in an interpolation test where training data exists only at discrete energies (100 GeV and 200 GeV), the model correctly interpolates the detector correction at 150 GeV — a region it never saw during training.

![Figure 2](/iaifi-research-blog/figures/2107_08979/figure_2.png)

The flagship application targets **jet energy response**. Jet energy is notoriously hard to simulate: the detector smears and distorts the true energy in ways that depend on the jet's own energy, direction, and surrounding collision environment. The authors construct three datasets using Pythia and Herwig (widely-used physics event generators) with Delphes (a fast detector simulation package) and a parametrized full simulation playing the roles of coarse and precise detectors.

Neural conditional reweighting successfully learns the detector response correction conditioned on particle-level jet energy — and the trained model applies to an entirely different generator (Herwig instead of Pythia) without refitting, because the detector correction has been cleanly separated from the generator-level physics.

![Figure 3](/iaifi-research-blog/figures/2107_08979/figure_3.png)

## Why It Matters

This work slots into a rapidly maturing ecosystem of machine-learning tools for particle physics simulation. Fast packages like Delphes are widely used but imperfect; the goal is to automatically "upgrade" their outputs to match expensive full simulations. Neural conditional reweighting provides a principled, efficient component for that pipeline — not replacing full simulation, but correcting fast simulation deficiencies in a way that generalizes across different physics scenarios.

The portability is the key practical gain. Because detector corrections no longer bake in assumptions about the underlying physics distribution, a single trained model can serve multiple generator configurations — cutting the computational overhead of maintaining separate correction models for every scenario.

The technique extends naturally to **signal interpolation in new physics searches**. When full simulation exists only at a handful of signal mass benchmarks, conditional reweighting interpolates the detector response across the gaps, extending coverage without running expensive new simulations. Any domain with a "coarse" and "precise" version of a process — where portable corrections matter — is a natural fit.

> **Bottom Line:** Neural conditional reweighting lets physicists correct detector simulations for specific particle energies rather than averaging over all of them, making corrections portable across physics models and enabling sensible extrapolation into data-sparse regions — a practical leap for the field of fast simulation.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges modern machine learning — classifier-based density ratio estimation — with a core challenge in experimental particle physics: making fast simulations accurate enough for precision measurements without running full Geant4 simulations for every physics scenario.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces a custom loss function that achieves conditional density ratio estimation in a single neural network training, with robust interpolation through data-sparse regions — a general-purpose ML tool applicable well beyond physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Neural conditional reweighting enables more accurate and portable detector corrections for collider experiments, directly improving the fidelity of physics object modeling in LHC analyses and new physics searches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include applying this technique to full LHC datasets and integrating it into standard fast simulation workflows; the work is available at arXiv:2107.08979.</span></div></div>
</div>
