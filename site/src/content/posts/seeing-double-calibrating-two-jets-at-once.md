---
abstract: Jet energy calibration is an important aspect of many measurements and searches
  at the LHC. Currently, these calibrations are performed on a per-jet basis, i.e.
  agnostic to the properties of other jets in the same event. In this work, we propose
  taking advantage of the correlations induced by momentum conservation between jets
  in order to improve their jet energy calibration. By fitting the $p_T$ asymmetry
  of dijet events in simulation, while remaining agnostic to the $p_T$ spectra themselves,
  we are able to obtain correlation-improved maximum likelihood estimates. This approach
  is demonstrated with simulated jets from the CMS Detector, yielding a $3$-$5\%$
  relative improvement in the jet energy resolution, corresponding to a quadrature
  improvement of approximately 35\%.
arxivId: '2402.14067'
arxivUrl: https://arxiv.org/abs/2402.14067
authors:
- Rikab Gambhir
- Benjamin Nachman
concepts:
- jet physics
- calibration
- likelihood estimation
- collider physics
- conservation laws
- dijet momentum asymmetry
- detector simulation
- uncertainty quantification
- bayesian inference
- event reconstruction
- regression
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2402_14067/figure_1.png
- /iaifi-research-blog/figures/2402_14067/figure_2.png
- /iaifi-research-blog/figures/2402_14067/figure_3.png
pdfUrl: https://arxiv.org/pdf/2402.14067v1
published: '2024-02-21T19:00:07+00:00'
theme: Experimental Physics
title: 'Seeing Double: Calibrating Two Jets at Once'
wordCount: 1145
---

## The Big Picture

Imagine trying to measure the weight of two people standing on a seesaw. You could weigh each person separately on a bathroom scale. But you could also use the seesaw itself: if it's perfectly balanced, you know both weights must be equal. Even if the seesaw isn't perfectly balanced, the *imbalance* tells you something you couldn't learn from either scale alone.

Physicists at the LHC have been using the bathroom scale approach for decades. This paper shows how to use the seesaw.

At particle accelerators like the Large Hadron Collider, protons smash together at nearly the speed of light, spraying out cascades of particles called **jets**: tight, cone-shaped showers of dozens to hundreds of particles emerging from a single quark or gluon. Measuring jet energies precisely matters for nearly every physics search, from hunting new particles to pinning down Higgs boson properties. But jets are messy. Detectors add noise, some particles get lost, and reconstructing the true energy from the raw detector signal is hard.

Researchers Rikab Gambhir (MIT) and Benjamin Nachman (Lawrence Berkeley National Lab) noticed something hiding in plain sight: the LHC produces enormous numbers of **dijet events**, collisions where exactly two jets fly out in opposite directions with nearly equal momentum. Momentum conservation links these jets at a fundamental level. That link had never been exploited to improve individual jet calibration. Until now.

> **Key Insight:** When two jets are born from the same collision, momentum conservation makes them correlated. Fitting the *imbalance* between them, rather than calibrating each jet in isolation, yields a measurably better energy estimate for both jets simultaneously.

## How It Works

In a dijet event, the two jets should carry equal and opposite transverse momentum (pT, the component of motion perpendicular to the beam). In practice, they don't balance perfectly. Some imbalance comes from real physics effects like stray radiation shed during the collision; some comes from detector noise.

The **pT asymmetry**, the normalized difference between the two measured jet pTs, follows a predictable distribution with characteristic width Λ. Standard **maximum likelihood estimation (MLE)** treats each jet as an independent measurement and ignores this correlation entirely. The authors construct a modified likelihood that folds in the constraint.

What makes this work is that the method doesn't care about the pT spectrum. It doesn't matter how many high-pT jets versus low-pT jets are in the dataset. The only thing that matters is the shape of the asymmetry distribution (the width Λ), which captures purely the *relationship* between the two jets, not their individual energy distributions.

The math works out cleanly. For a jet with ordinary resolution σ, the correlation-improved resolution gains by a factor scaling as σ²/(2Λ²). The tighter the momentum conservation constraint (small Λ), the bigger the improvement. If the two jets must balance, knowing one jet's energy constrains the other.

![Figure 1](/iaifi-research-blog/figures/2402_14067/figure_1.png)

The method handles two detector noise models:

- **Gaussian case**: The improved estimates shift each jet's pT slightly toward the midpoint of the two measurements, weighted by the relative magnitudes of σ and Λ.
- **Exponential case**: For heavier-tailed noise (more realistic for some detectors) the improvement is qualitatively similar with a different analytic form.

The authors tested this on simulated proton-collision dijet events from the CMS detector at CERN, using early Run 1 conditions. They fit asymmetry distributions in bins of jet pT and position in the detector, since both resolution and physics asymmetry depend on jet geometry and energy.

![Figure 2](/iaifi-research-blog/figures/2402_14067/figure_2.png)

The fits reveal a clear pattern: Λ is consistently *smaller* than σ across all pT ranges studied. That's exactly the regime where the correlation-improved method helps most.

![Figure 3](/iaifi-research-blog/figures/2402_14067/figure_3.png)

Across the full pT range, the method achieves a 3–5% relative improvement in jet energy resolution, corresponding to roughly a 35% reduction in the squared resolution. In experimental physics, where precision campaigns work for years to gain percent-level improvements, that's a real payoff from a simple modification. The improved estimates are also unbiased, verified in simulation to neither systematically over- nor under-estimate the true jet energy.

## Why It Matters

The correlation-improved MLE framework is general: it applies whenever you have multiple correlated measurements and some prior knowledge of how they're correlated, even without knowing their individual distributions. The authors already sketch an extension to **boosted resonances**, where a heavy particle like a Z boson or Higgs decays to two nearby jets. The same momentum conservation argument applies in a different energy and geometry regime.

LHC physics has increasingly turned to mining known physical constraints (conservation laws, symmetries, known particle properties) to extract information that naive jet-by-jet analysis misses. Machine learning has driven much of the recent progress in jet physics, but this paper shows that careful statistical reasoning, without any neural network, can still deliver meaningful gains. The method could also combine with ML-based calibrations, potentially stacking improvements.

On the practical side, the approach requires no exotic hardware, special data collection, or new training infrastructure. It builds on existing per-jet calibrations and adds a simple post-processing step, the kind of improvement large experimental collaborations can realistically adopt.

> **Bottom Line:** By treating two jets as a correlated system rather than independent measurements, this method extracts a free 3–5% improvement in jet energy resolution. No new hardware, no new data, just smarter use of momentum conservation.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies rigorous statistical inference (maximum likelihood estimation with explicit correlation structure) to a core challenge in experimental particle physics, showing how mathematical tools from statistics can directly improve LHC measurements.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The correlation-improved MLE framework is a general method for joint calibration of correlated measurements, with potential applications beyond particle physics wherever conservation laws constrain multi-object systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Improving jet energy resolution directly benefits Higgs boson measurements, new physics searches, and QCD studies at the LHC.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include applying this technique to boosted resonances and combining it with ML-based jet calibrations. The full method is available at [arXiv:2402.14067](https://arxiv.org/abs/2402.14067).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Seeing Double: Calibrating Two Jets at Once</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2402.14067</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Rikab Gambhir", "Benjamin Nachman"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Jet energy calibration is an important aspect of many measurements and searches at the LHC. Currently, these calibrations are performed on a per-jet basis, i.e. agnostic to the properties of other jets in the same event. In this work, we propose taking advantage of the correlations induced by momentum conservation between jets in order to improve their jet energy calibration. By fitting the $p_T$ asymmetry of dijet events in simulation, while remaining agnostic to the $p_T$ spectra themselves, we are able to obtain correlation-improved maximum likelihood estimates. This approach is demonstrated with simulated jets from the CMS Detector, yielding a $3$-$5\%$ relative improvement in the jet energy resolution, corresponding to a quadrature improvement of approximately 35\%.</span></div></div>
</div>
