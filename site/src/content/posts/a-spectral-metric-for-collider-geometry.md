---
abstract: By quantifying the distance between two collider events, one can triangulate
  a metric space and reframe collider data analysis as computational geometry. One
  popular geometric approach is to first represent events as an energy flow on an
  idealized celestial sphere and then define the metric in terms of optimal transport
  in two dimensions. In this paper, we advocate for representing events in terms of
  a spectral function that encodes pairwise particle angles and products of particle
  energies, which enables a metric distance defined in terms of one-dimensional optimal
  transport. This approach has the advantage of automatically incorporating obvious
  isometries of the data, like rotations about the colliding beam axis. It also facilitates
  first-principles calculations, since there are simple closed-form expressions for
  optimal transport in one dimension. Up to isometries and event sets of measure zero,
  the spectral representation is unique, so the metric on the space of spectral functions
  is a metric on the space of events. At lowest order in perturbation theory in electron-positron
  collisions, our metric is simply the summed squared invariant masses of the two
  event hemispheres. Going to higher orders, we present predictions for the distribution
  of metric distances between jets in fixed-order and resummed perturbation theory
  as well as in parton-shower generators. Finally, we speculate on whether the spectral
  approach could furnish a useful metric on the space of quantum field theories.
arxivId: '2305.03751'
arxivUrl: https://arxiv.org/abs/2305.03751
authors:
- Andrew J. Larkoski
- Jesse Thaler
concepts:
- spectral emd
- optimal transport
- spectral methods
- collider physics
- jet physics
- collider event geometry
- symmetry preservation
- manifold learning
- quantum field theory
- renormalization
- monte carlo methods
- geometric deep learning
figures:
- /iaifi-research-blog/figures/2305_03751/figure_1.png
- /iaifi-research-blog/figures/2305_03751/figure_2.png
pdfUrl: https://arxiv.org/pdf/2305.03751v2
published: '2023-05-05T18:00:01+00:00'
theme: Theoretical Physics
title: A Spectral Metric for Collider Geometry
wordCount: 1110
---

## The Big Picture

Imagine comparing two snowflakes by measuring how much "stuff" you'd need to move to transform one into the other. Physicists do something analogous when comparing particle collision events at the Large Hadron Collider, except instead of snowflakes, they're comparing showers of subatomic particles exploding outward at nearly the speed of light, recorded across hundreds of detector dimensions.

When a proton smashes into another proton at the LHC, the resulting spray of particles can vary in hundreds of different ways. Making sense of this requires more than a checklist of particle energies. It requires a *geometry*. Define a *distance* between any two collision events and you can map the data, find clusters and outliers, and discover patterns that simpler methods would miss.

The **Energy Mover's Distance (EMD)**, introduced several years ago, took exactly this approach: treat each collision event as a pile of "dirt" spread around the detector, and define the distance as the minimum cost to rearrange one pile into the other. It works, but it requires solving a complex mathematical optimization problem in two dimensions. That's computationally expensive and hard to analyze on paper.

Larkoski and Thaler have now proposed a smarter alternative. By compressing the full event into a one-dimensional **spectral function**, a compact fingerprint of all pairwise relationships between particles, they unlock a distance measure with exact closed-form solutions that automatically respects collider symmetries and still captures the full event structure. This is not a lossy shortcut: it is a complete representation that's simply easier to work with.

> **Key Insight:** By encoding collider events as spectral functions of pairwise particle angles, the authors reduce metric distances to one-dimensional optimal transport, yielding closed-form expressions and built-in rotational symmetry without sacrificing any physical information.

## How It Works

The starting point is a deceptively simple question: what information in a collision event is both physically meaningful and **rotationally invariant**, unchanged when you rotate the whole picture? The answer is pairwise geometry: the angles between each pair of particles, and the products of their energies.

Larkoski and Thaler package this into the spectral function. For every pair of particles *i* and *j*, multiply their energies and record the contribution at the angular separation between them. Sum over all pairs, and you get a one-dimensional distribution over angles: a compact fingerprint of the event.

The spectral function is unique up to rotations about the beam axis and reflections. Two events that differ only by a rotation will have identical spectral functions, so the symmetry is baked in automatically. The authors prove (Appendix A) that, aside from these trivial geometric equivalences and a negligibly small set of edge cases, the spectral function retains the full event information. Nothing is lost.

![Figure 1](/iaifi-research-blog/figures/2305_03751/figure_1.png)

With events represented as one-dimensional distributions, the **Spectral EMD** between two events becomes the cost of optimal transport in 1D. And in one dimension, optimal transport has a clean closed-form solution: sort both distributions from smallest to largest, pair them up point by point, and integrate the difference. No iterative solver needed.

The team applied this framework across increasing levels of approximation:

- **Leading order (one particle per jet):** No pairs, no spectral function. The distance is zero.
- **Next-to-leading order (two-particle jets):** The Spectral EMD reduces to a simple formula involving the inter-particle angle and energy fraction, computable in closed form.
- **Second order (three-particle jets):** More complex, but still tractable. The authors work through the relevant optimal transport plans explicitly.

At the simplest approximation, in electron-positron collisions, the Spectral EMD between two jets equals the sum of the squared **invariant masses** of the two event hemispheres. (Invariant mass is the effective mass of a particle cluster, computed in a frame-independent way.) That's a physically intuitive result: the distance between two simple events is captured by how "heavy" each half of the collision looks.

## Why It Matters

![Figure 2](/iaifi-research-blog/figures/2305_03751/figure_2.png)

The authors computed Spectral EMD distributions between quark jets and gluon jets using both fixed-order perturbative QCD at next-to-leading order and parton-shower Monte Carlo generators. Quark-gluon separation turns out to be controlled by the sum of their **quadratic color Casimirs** (C_F for quarks, C_A for gluons), mirroring what was found with the original EMD. The new metric measures the same real physics, from a more convenient mathematical angle.

They also found that non-perturbative hadronization effects, the messy process by which quarks and gluons bind into observable hadrons, are smaller than naive estimates would suggest. A metric less sensitive to poorly-understood non-perturbative physics is one that experimentalists can actually trust at the LHC.


The most speculative application sits at the end of the paper: can the spectral approach define a metric not just on events, but on the space of **quantum field theories** themselves? The authors sketch how spectral functions associated with energy-energy correlators could quantify distances between entire theoretical frameworks, covering different QFTs, coupling regimes, and UV completions. It's a long-range vision, pointing toward using collider geometry to map out fundamental physics at a structural level.

The connection to machine learning is implicit but real. Geometric tools (metrics, distances, manifold structure) are exactly what modern ML methods use to cluster, classify, and generate data. A metric that's analytically computable, symmetry-respecting, and physically grounded is a far better foundation for ML-based collider analysis than raw high-dimensional particle lists. As LHC data accumulates and future colliders are planned, tools like the Spectral EMD will sit at the core of how physicists make sense of what their detectors record.

> **Bottom Line:** The Spectral EMD gives physicists a mathematically cleaner way to measure distances between particle collision events, one that is analytically tractable, automatically symmetric, and experimentally relevant. It opens doors to better collider data analysis and a deeper geometric understanding of quantum field theory itself.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies optimal transport theory, a mathematical framework central to modern machine learning, to fundamental particle physics. It defines a geometric structure on collider event space that connects data science and quantum field theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The Spectral EMD provides a computationally tractable, symmetry-respecting distance metric with closed-form expressions, making it a natural foundation for geometry-aware machine learning methods applied to high-dimensional collider data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The framework enables first-principles perturbative QCD calculations of metric distance distributions between jets, yielding physically interpretable results and revealing that quark-gluon separation is governed by quadratic color Casimirs.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending the spectral metric to proton-proton collisions at the LHC and exploring whether spectral functions can define a useful metric on the space of quantum field theories; the paper is available as [arXiv:2305.03751](https://arxiv.org/abs/2305.03751).</span></div></div>
</div>
