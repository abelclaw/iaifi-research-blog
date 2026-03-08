---
abstract: 'Direct searches for new particles at colliders have traditionally been
  factorized into model proposals by theorists and model testing by experimentalists.
  With the recent advent of machine learning methods that allow for the simultaneous
  unfolding of all observables in a given phase space region, there is a new opportunity
  to blur these traditional boundaries by performing searches on unfolded data. This
  could facilitate a research program where data are explored in their natural high
  dimensionality with as little model bias as possible. We study how the information
  about physics beyond the Standard Model is preserved by full phase space unfolding
  using an important physics target at the Large Hadron Collider (LHC): exotic Higgs
  boson decays involving hadronic final states. We find that if the signal cross section
  is high enough, information about the new physics is visible in the unfolded data.
  We will show that in some cases, quantifiably all of the information about the new
  physics is encoded in the unfolded data. Finally, we show that there are still many
  cases when the unfolding does not work fully or precisely, such as when the signal
  cross section is small. This study will serve as an important benchmark for enhancing
  unfolding methods for the LHC and beyond.'
arxivId: '2105.09923'
arxivUrl: https://arxiv.org/abs/2105.09923
authors:
- Patrick Komiske
- W. Patrick McCormack
- Benjamin Nachman
concepts:
- unfolding
- new physics searches
- collider physics
- bsm unfolding fidelity
- classification
- simulation-based inference
- likelihood ratio
- signal detection
- anomaly detection
- standard model
- inverse problems
- event reconstruction
figures:
- /iaifi-research-blog/figures/2105_09923/figure_1.png
- /iaifi-research-blog/figures/2105_09923/figure_1.png
- /iaifi-research-blog/figures/2105_09923/figure_2.png
- /iaifi-research-blog/figures/2105_09923/figure_2.png
- /iaifi-research-blog/figures/2105_09923/figure_3.png
- /iaifi-research-blog/figures/2105_09923/figure_3.png
pdfUrl: https://arxiv.org/pdf/2105.09923v2
published: '2021-05-20T17:36:53+00:00'
theme: Theoretical Physics
title: Preserving New Physics while Simultaneously Unfolding All Observables
wordCount: 1105
---

## The Big Picture

Imagine trying to identify a rare flower in a dense forest using only a blurry photograph. That's roughly the situation physicists face at the Large Hadron Collider (LHC). Particle detectors don't record clean physics events. They record a smeared, distorted version of reality filtered through layers of hardware. The process of mathematically "unblurring" that image to recover the underlying physics is called **unfolding**, and for decades it has been a bottleneck in the search for new particles.

Traditional unfolding methods were designed for a world where we already know what we're looking for. They compress data into a handful of hand-selected measurements and use simulations of known physics (the Standard Model, our best theory of matter and forces) to correct for detector distortions. But if something genuinely new is hiding in the data, something whose detector signature differs from anything we've simulated, the standard approach could systematically erase exactly the signal we're trying to find.

A team from MIT and Lawrence Berkeley National Laboratory asked a sharp question: if you unfold *everything at once*, all particles, all their properties, the full shape of every collision event, can you preserve the fingerprint of new physics nobody was specifically looking for? Their answer, with important caveats, is yes.

> **Key Insight:** Machine learning-powered full phase space unfolding can preserve signatures of exotic new particles in LHC data. This opens the door to model-agnostic searches on corrected data rather than raw detector output, but only when those signals are strong enough to survive the procedure.

## How It Works

The central tool is **OmniFold**, a machine learning method that works differently from traditional approaches. Instead of sorting data into bins and inverting a correction table, OmniFold trains neural network classifiers to iteratively reweight simulated events until they match actual experimental data. The result is a corrected, detector-free snapshot of particle collisions, not for one measurement at a time, but for all measurements simultaneously.

![Figure 1](/iaifi-research-blog/figures/2105_09923/figure_1.png)

The OmniFold loop runs in two alternating steps:

1. **Step 1 — Match detector-level simulation to data:** Train a classifier to distinguish real detector data from simulated detector events. Use the classifier output as event weights, pushing the simulation to look like the data.
2. **Step 2 — Push weights back to particle level:** Apply those detector-level weights to the corresponding particle-level simulated events. Train a second classifier to make the unweighted particle-level simulation match the newly weighted version. These particle-level weights are the unfolded result.

Repeat. Iterate. Converge.

OmniFold can tackle the *full* phase space (the complete description of every particle produced in every collision) because it uses **particle cloud networks**: neural architectures built to process any number of particles in any order, exactly as they emerge from a collision. Every particle track, every **jet** (a spray of particles from a quark or gluon), every photon gets included. Nothing is discarded.

The benchmark physics target is deliberately tricky: exotic **Higgs boson** decays into a *Z* boson (carrier of the weak nuclear force) plus a light neutral particle that decays into ordinary matter. This produces a distinctive particle cluster buried under ordinary *Z*+jets production, the everyday process where a *Z* boson appears alongside jets. Simple bump-hunting in a one-dimensional mass spectrum would miss it.

![Figure 2](/iaifi-research-blog/figures/2105_09923/figure_1.png)

The team tested two variants. **MultiFold** processes the full event as a point cloud, treating each collision as a swarm of particles with no assumed structure, making it sensitive to complete event geometry. **OmniFold** operates on a compact numerical summary of the event, trading some information for computational tractability. Comparing the two reveals where information lives in high-dimensional event space.

## Why It Matters

The results are nuanced, which is part of what makes them useful. When the signal **cross section** (roughly, how often the exotic decay occurs relative to all collisions) is high enough, OmniFold successfully preserves the new physics information. The researchers quantify this using the **Fisher information**, a measure of how much a dataset "knows" about a particular parameter. In favorable cases, the Fisher information in the unfolded data matches the raw detector data: quantifiably, nothing is lost.

![Figure 4](/iaifi-research-blog/figures/2105_09923/figure_2.png)

But when the signal is rare, unfolding degrades. Classifiers trained overwhelmingly on Standard Model events don't correctly model the rare signal's detector response, and the corrected data can misrepresent the new physics in ways that are difficult to catch after the fact.

The team also tested what happens when new physics is included in the simulation used for unfolding, a more realistic scenario where physicists have some prior suspicion of what to look for. Including the signal in the generation step improves fidelity substantially. This suggests that hybrid strategies, part model-agnostic and part model-informed, may offer the best practical path forward.

![Figure 5](/iaifi-research-blog/figures/2105_09923/figure_3.png)

For most of the LHC's history, the workflow has been linear: theorists propose a model, experimentalists design a targeted analysis, and the two communities meet when results are published. Full phase space unfolding scrambles that workflow in the best possible way. Experimentalists could publish unfolded datasets that any theorist can analyze with any model, no access to raw detector data or proprietary simulation chains required.

The stakes are high. The LHC's High-Luminosity upgrade will produce data at rates that make exhaustive model-by-model searches increasingly impractical. Methods that preserve new physics information in a corrected, model-agnostic form could become the primary interface between raw collision data and the broader physics community. This paper provides an honest benchmark, failure modes included, that the field needs before deploying these methods at scale.

> **Bottom Line:** OmniFold-style full phase space unfolding can preserve exotic new physics signatures in LHC data when signals are strong, opening the door to model-agnostic searches on corrected data. Signal rarity remains a fundamental challenge that next-generation methods must address.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines deep learning (neural network classifiers and particle cloud architectures) with high-energy experimental physics, showing that AI-powered unfolding can connect theorist-designed models and experimentalist-driven searches at the LHC in ways that were previously impractical.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The study benchmarks how iterative neural reweighting methods preserve or lose information across a high-dimensional transformation, offering concrete guidance for designing better machine learning pipelines in scientific data analysis.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Full phase space unfolding can preserve signatures of exotic Higgs boson decays, expanding the LHC's capacity to search for physics beyond the Standard Model without committing to a specific signal model in advance.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will focus on improving unfolding fidelity at low signal cross sections and integrating these methods into real experimental analyses; the paper is available at [arXiv:2105.09923](https://arxiv.org/abs/2105.09923).</span></div></div>
</div>
