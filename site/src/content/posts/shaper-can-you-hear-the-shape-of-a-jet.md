---
abstract: The identification of interesting substructures within jets is an important
  tool for searching for new physics and probing the Standard Model at colliders.
  Many of these substructure tools have previously been shown to take the form of
  optimal transport problems, in particular the Energy Mover's Distance (EMD). In
  this work, we show that the EMD is in fact the natural structure for comparing collider
  events, which accounts for its recent success in understanding event and jet substructure.
  We then present a Shape Hunting Algorithm using Parameterized Energy Reconstruction
  (SHAPER), which is a general framework for defining and computing shape-based observables.
  SHAPER generalizes N-jettiness from point clusters to any extended, parametrizable
  shape. This is accomplished by efficiently minimizing the EMD between events and
  parameterized manifolds of energy flows representing idealized shapes, implemented
  using the dual-potential Sinkhorn approximation of the Wasserstein metric. We show
  how the geometric language of observables as manifolds can be used to define novel
  observables with built-in infrared-and-collinear safety. We demonstrate the efficacy
  of the SHAPER framework by performing empirical jet substructure studies using several
  examples of new shape-based observables.
arxivId: '2302.12266'
arxivUrl: https://arxiv.org/abs/2302.12266
authors:
- Demba Ba
- Akshunna S. Dogra
- Rikab Gambhir
- Abiy Tasissa
- Jesse Thaler
concepts:
- optimal transport
- jet physics
- energy mover's distance
- irc safety
- collider physics
- sinkhorn divergence
- manifold learning
- geometric deep learning
- event reconstruction
- clustering
- new physics searches
- loss function design
figures:
- /iaifi-research-blog/figures/2302_12266/figure_1.png
- /iaifi-research-blog/figures/2302_12266/figure_1.png
- /iaifi-research-blog/figures/2302_12266/figure_2.png
- /iaifi-research-blog/figures/2302_12266/figure_2.png
- /iaifi-research-blog/figures/2302_12266/figure_3.png
- /iaifi-research-blog/figures/2302_12266/figure_3.png
pdfUrl: https://arxiv.org/pdf/2302.12266v4
published: '2023-02-23T19:00:00+00:00'
theme: Theoretical Physics
title: 'SHAPER: Can You Hear the Shape of a Jet?'
wordCount: 1084
---

## The Big Picture

In 1966, mathematician Mark Kac posed a haunting question: "Can one hear the shape of a drum?" He wanted to know whether a drum's vibrational frequencies uniquely determine its geometry. Decades later, particle physicists at the LHC are asking a strikingly similar question about the debris from proton collisions: can you "hear" the shape of a jet?

Every time two protons smash together at the Large Hadron Collider, the collision spawns hundreds of particles that fan outward in narrow, focused streams called **jets**. These jets carry geometric fingerprints. A top quark — one of the heaviest known elementary particles, which rapidly decays into three lighter ones — leaves a distinctly different pattern than a gluon, the carrier of the strong nuclear force, which tends to spray out softer, more diffuse energy.

Identifying those shapes is crucial for finding new physics. But the tools physicists have relied on for decades are limited to rigid, preconceived geometric templates. If you don't know what shape to look for, you might miss it entirely.

A team from Harvard, MIT, and Tufts has built a framework called **SHAPER** — Shape Hunting Algorithm using Parameterized Energy Reconstruction — that can hunt for *any* geometric substructure within a jet: rings, ellipses, disks, or shapes physicists haven't named yet.

> **Key Insight:** SHAPER reframes jet substructure analysis as an optimal transport problem, proving that the "Earth Mover's Distance" is the *mathematically unique* distance measure that correctly respects collider detector geometry.

## How It Works

The foundation of SHAPER is the **Energy Mover's Distance (EMD)**. Think of each jet as a pile of dirt scattered across a detector, where height represents deposited energy. The EMD asks: what's the minimum work needed to reshape one pile into another? This is the classical "earth mover's distance" from computer vision, mathematically formalized as the **Wasserstein metric**.

The authors prove something deeper than mere usefulness: the Wasserstein metric is the *unique* metric on collision events satisfying two physical requirements simultaneously. It must be continuous — tiny momentum changes shouldn't cause wild jumps in an observable. And it must be **geometrically faithful**, meaning distances between events must respect the actual spatial layout of the detector. No other distance measure does both. This justifies why the EMD has appeared repeatedly in collider physics — it wasn't a lucky choice, it was inevitable.

![Figure 1](/iaifi-research-blog/figures/2302_12266/figure_1.png)

With this foundation, SHAPER defines a shape observable through a clean mathematical recipe:

1. **Parameterize an idealized shape** — describe a ring, ellipse, or disk as a probability distribution over the detector, controlled by parameters like radius, orientation, or eccentricity.
2. **Compute the EMD** between the actual jet and that idealized shape.
3. **Minimize over all parameters** — find the shape configuration that best matches the jet.
4. **Extract two outputs**: the minimum EMD value (how "shape-like" the jet is) and the optimal parameters (what the best-fit shape looks like).

The computational workhorse is the **Sinkhorn divergence**, a fast approximation of the Wasserstein metric that replaces the exact transport problem with a regularized version solvable by iterative matrix scaling. Crucially, Sinkhorn is differentiable — you can take gradients through it with respect to shape parameters, enabling GPU-accelerated optimization.

SHAPER handles **infrared-and-collinear (IRC) safety** automatically. IRC safety is a technical requirement in QCD (Quantum Chromodynamics, the theory of quarks and gluons): observables must be insensitive to very soft particles and near-identical particle splittings, otherwise they become incalculable with standard theoretical tools. Any shape built from smooth manifolds is automatically IRC safe.

The framework unlocks observables nobody could measure before. **N-Ringiness** asks how well a jet decomposes into N concentric rings. **N-Diskiness** measures how disk-like the energy deposit is. **N-Ellipsiness** extracts eccentricity and orientation event-by-event. In benchmarks on top quark versus QCD jets, top jets — which decay into three prongs — show measurably higher 2-Ringiness than QCD jets, because three-body decay creates ring-like energy deposits around the jet core.

![Figure 4](/iaifi-research-blog/figures/2302_12266/figure_2.png)

One particularly elegant application adds a "pileup" term to the shape model: instead of subtracting soft background radiation from other collisions, SHAPER absorbs it and mitigates it automatically.

![Figure 6](/iaifi-research-blog/figures/2302_12266/figure_3.png)

## Why It Matters

For particle physics, SHAPER is a new instrument. Where physicists previously had to commit to a specific geometric hypothesis before designing a search, they can now let the data speak. A jet that doesn't fit any known shape is immediately suspicious. Future collider experiments could use shape observables to flag boosted new particles, unusual color flows, or hypothetical exotic states — without knowing in advance what to look for.

For machine learning, this work demonstrates that mathematical rigor beats brute force. Rather than training a neural network on millions of jets and hoping it discovers geometric structure, SHAPER builds that structure into the observable by construction. The result is interpretable, theoretically grounded, and computationally efficient. The connection to optimal transport also points toward broader applications — galaxy morphology, medical imaging, protein conformations — anywhere structured distributions need to be compared, Wasserstein geometry could define principled shape observables.

Open questions remain. The Sinkhorn regularization introduces a smoothing parameter trading off accuracy against speed. Extending SHAPER to three-dimensional shapes for full-calorimetry detectors is an active frontier. And the theoretical question the title alludes to — whether jet shapes uniquely determine the underlying physics — remains beautifully open.

> **Bottom Line:** SHAPER proves that the Wasserstein metric is the mathematically natural language for comparing collider events, then delivers a computational framework that can measure *any* geometric structure within a jet — from rings to ellipses to arbitrary custom shapes — with built-in theoretical safety guarantees.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">SHAPER bridges optimal transport theory from mathematics and computer vision with collider jet physics, demonstrating that abstract Wasserstein geometry provides the rigorous foundation for a wide class of particle physics observables.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">By proving the Wasserstein metric's uniqueness for structured data on geometric spaces, this work justifies its use in machine learning tasks where spatial faithfulness matters, and introduces a differentiable shape-fitting framework suitable for end-to-end neural network training.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">SHAPER generalizes decades-old jet shape observables into a unified framework capable of measuring novel substructures like jet eccentricity and dynamic radii, opening new experimental handles for precision Standard Model tests and new physics searches at the LHC.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work includes extending shape manifolds to three-dimensional detector geometries and incorporating SHAPER observables as differentiable layers in jet tagging networks; the full framework is described in arXiv:2402.05300.</span></div></div>
</div>
