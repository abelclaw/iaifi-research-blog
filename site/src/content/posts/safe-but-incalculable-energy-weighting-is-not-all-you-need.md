---
abstract: Infrared and collinear (IRC) safety has long been used a proxy for robustness
  when developing new jet substructure observables. This guiding philosophy has been
  carried into the deep learning era, where IRC-safe neural networks have been used
  for many jet studies. For graph-based neural networks, the most straightforward
  way to achieve IRC safety is to weight particle inputs by their energies. However,
  energy-weighting by itself does not guarantee that perturbative calculations of
  machine-learned observables will enjoy small non-perturbative corrections. In this
  paper, we demonstrate the sensitivity of IRC-safe networks to non-perturbative effects,
  by training an energy flow network (EFN) to maximize its sensitivity to hadronization.
  We then show how to construct Lipschitz Energy Flow Networks (L-EFNs), which are
  both IRC safe and relatively insensitive to non-perturbative corrections. We demonstrate
  the performance of L-EFNs on generated samples of quark and gluon jets, and showcase
  fascinating differences between the learned latent representations of EFNs and L-EFNs.
arxivId: '2311.07652'
arxivUrl: https://arxiv.org/abs/2311.07652
authors:
- Samuel Bright-Thonney
- Benjamin Nachman
- Jesse Thaler
concepts:
- jet physics
- irc safety
- non-perturbative corrections
- lipschitz constraint
- optimal transport
- robustness
- graph neural networks
- representation learning
- collider physics
- spectral methods
- classification
figures:
- /iaifi-research-blog/figures/2311_07652/figure_1.png
- /iaifi-research-blog/figures/2311_07652/figure_2.png
- /iaifi-research-blog/figures/2311_07652/figure_3.png
pdfUrl: https://arxiv.org/pdf/2311.07652v2
published: '2023-11-13T19:00:02+00:00'
theme: Theoretical Physics
title: 'Safe but Incalculable: Energy-weighting is not all you need'
wordCount: 1082
---

## The Big Picture

Imagine designing a ruler to measure something incredibly small — say, the width of a single atom. You craft it carefully, but the ruler itself bends unpredictably due to unavoidable quantum effects. Your measurement is technically valid, but the answer is dominated by noise you can't calculate or control. That's essentially the problem particle physicists face when deploying certain AI tools to study jets at the Large Hadron Collider.

At the LHC, quarks and gluons scatter at nearly the speed of light and spray out cascades of particles called **jets**. Physicists have developed mathematical tools called **observables** to extract useful information from these sprays. One prized property is **IRC safety** (infrared and collinear safety): the guarantee that a measurement doesn't blow up when you add a very soft particle or split one particle into two nearly-identical ones.

IRC-safe observables can be calculated from first principles using **perturbation theory** — a systematic method where physicists compute increasingly precise corrections to their predictions. When deep learning arrived in particle physics, researchers naturally wanted IRC-safe neural networks, achieved through a clever trick: weight every particle's contribution by its share of the jet's total energy, so that tiny or nearly-identical particles barely influence the result.

But a team from Cornell, Lawrence Berkeley National Laboratory, and MIT has shown that energy weighting, while necessary, is not sufficient. An IRC-safe neural network can still be catastrophically sensitive to **non-perturbative effects** — the incalculable physics of how quarks bind into **hadrons** (composite particles like protons that detectors actually observe). Their fix, **Lipschitz Energy Flow Networks (L-EFNs)**, adds a geometric constraint that tames this sensitivity, producing networks that are both safe *and* calculable.

> **Key Insight:** A neural network can be infrared-and-collinear safe yet still be dominated by incalculable non-perturbative corrections — making it "safe but incalculable." The remedy lies not in how you weight inputs, but in how steeply your network is allowed to respond to changes in them.

## How It Works

The standard **Energy Flow Network (EFN)** processes a jet in three steps:

1. Each particle's angular position is mapped by a learned function into an abstract, high-dimensional representation.
2. Those representations are summed with energy-fraction weights — the IRC safety guarantee, since soft or collinear particles carry negligible weight.
3. A second learned function maps the summed representation to a final output.

The paper's key insight is that IRC safety only constrains what happens at the *edges* of particle space — very soft or very collinear configurations. It says nothing about how violently a network can respond to the physics separating **parton-level events** (quarks and gluons before binding) from **hadron-level events** (the particles a detector sees after **hadronization**). Non-perturbative corrections scale with how sensitive an observable is to energy rearrangement within a jet — and an unconstrained network can be exquisitely sensitive to exactly that.

To prove this dramatically, the authors trained a standard EFN to *maximize* its ability to distinguish parton-level from hadron-level jet samples. The result: the EFN became extraordinarily good at detecting hadronization despite remaining IRC safe — the "safe but incalculable" regime, where theoretical predictions formally exist but are swamped by non-perturbative effects.

![Figure 1](/iaifi-research-blog/figures/2311_07652/figure_1.png)

The L-EFN resolves this by imposing a **Lipschitz constraint** on both learned functions. A function is L-Lipschitz if it can never change its output by more than L times the change in its input — a global bound on steepness. The authors enforce this via **spectral normalization**: at each training step, each layer's weights are rescaled so no single layer amplifies input changes beyond a fixed limit. This is computationally cheap and slots directly into standard gradient-based training.

The mathematical motivation comes from the **Energy Mover's Distance (EMD)**, which quantifies how much "work" it takes to rearrange one jet's energy distribution into another's. A key result — the Kantorovich-Rubinstein theorem — shows that any 1-Lipschitz function acting on particle distributions is automatically bounded by the EMD between those distributions. Since the EMD between parton-level and hadron-level jets is small, a 1-Lipschitz network's output difference is *also* small — provably, by construction.

## Why It Matters

![Figure 2](/iaifi-research-blog/figures/2311_07652/figure_2.png)

The researchers tested L-EFNs on generated quark and gluon jets, the canonical benchmark in jet substructure physics. L-EFNs are somewhat less powerful discriminators than unconstrained EFNs — the Lipschitz constraint limits expressiveness — but they pay this modest accuracy cost with drastically reduced hadronization sensitivity.

![Figure 3](/iaifi-research-blog/figures/2311_07652/figure_3.png)

Visualizing the learned internal representations reveals that the two architectures organize jet information in qualitatively different ways. Constrained networks learn smoother, more physically interpretable representations of jet structure — a sign that the geometric constraint is doing genuine physics, not merely regularizing.

This work opens a door the jet physics community has largely left closed: a rigorous, trainable framework for controlling non-perturbative corrections in machine-learned observables. The immediate next step is developing full theoretical calculations for L-EFN outputs — something the bounded Lipschitz norm now makes plausible for the first time.

The approach generalizes: any particle-cloud or graph-based network using energy weighting could potentially be upgraded with spectral normalization to gain the same calculability guarantees. As ML becomes ever more central to LHC analysis, the question of whether network outputs can be trusted against first-principles QCD — not just on simulations — grows urgent. L-EFNs are a concrete step toward networks that can be genuinely compared with analytic calculations.

> **Bottom Line:** Energy weighting makes a neural network IRC safe, but Lipschitz constraints are what make it *calculable* — and this paper delivers both in a single, trainable architecture that could redefine how the field thinks about trustworthy machine learning for collider physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits at the precise intersection of quantum field theory and modern deep learning, using geometric constraints from optimal transport mathematics to make neural networks compatible with the calculability requirements of perturbative QCD.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces spectral normalization as a physics-motivated architectural constraint, demonstrating that Lipschitz regularization can encode domain-specific robustness guarantees into learned behavior — not just stabilize training.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By showing that IRC safety alone is insufficient for reliable perturbative calculations, this work reframes a foundational assumption in jet physics and provides a constructive path toward machine-learned observables that are analytically tractable in QCD.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work includes computing full fixed-order predictions for L-EFN outputs and extending the Lipschitz framework to more expressive graph neural network architectures; the paper is available at arXiv:2309.03501.</span></div></div>
</div>
