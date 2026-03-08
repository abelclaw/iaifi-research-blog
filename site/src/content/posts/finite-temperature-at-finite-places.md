---
abstract: This paper studies AdS/CFT in its $p$-adic version (at the ``finite place")
  in the setting where the bulk geometry is made up of the Tate curve, a discrete
  quotient of the Bruhat-Tits tree. Generalizing a classic result due to Zabrodin,
  the boundary dual of the free massive bulk theory is explicitly derived. Introducing
  perturbative interactions, the Wittens diagrams for the two-point and three-point
  correlators are computed for generic scaling dimensions at one-loop and tree level
  respectively. The answers obtained demonstrate how $p$-adic AdS/CFT on the Tate
  curve provides a useful toy model for real CFTs at finite temperature.
arxivId: '2408.04199'
arxivUrl: https://arxiv.org/abs/2408.04199
authors:
- An Huang
- Christian Baadsgaard Jepsen
concepts:
- conformal field theory
- p-adic ads/cft
- tate curve
- quantum field theory
- bruhat-tits tree
- scattering amplitudes
- renormalization
- string theory
- phase transitions
figures:
- /iaifi-research-blog/figures/2408_04199/figure_1.png
- /iaifi-research-blog/figures/2408_04199/figure_2.png
- /iaifi-research-blog/figures/2408_04199/figure_3.png
pdfUrl: https://arxiv.org/pdf/2408.04199v2
published: '2024-08-08T03:49:31+00:00'
theme: Theoretical Physics
title: Finite Temperature at Finite Places
wordCount: 1043
---

## The Big Picture

Imagine trying to understand a hurricane by first studying a simpler storm on a different planet, one where the physics is cleaner, the math collapses to manageable forms, and the essential features still show up. That's the strategy behind a new paper from Brandeis University and the Korea Institute for Advanced Study.

The researchers applied **AdS/CFT**, a framework linking gravity inside a curved region of spacetime to a different type of physics on that region's surface, in a radically simplified mathematical universe built on **p-adic numbers**. Think of AdS/CFT as decoding the interior of a snow globe by studying only its glass shell. P-adic numbers are an alternative number system where "closeness" works differently than on the real number line: two numbers can be "nearby" even when they appear far apart by ordinary arithmetic.

The target: **finite-temperature CFTs**. A conformal field theory (CFT) is a mathematical model for physical systems (like materials at the edge of a phase transition) that look statistically the same at every scale. At zero temperature, the math stays manageable. Switch on a temperature, and contributions from every type of excitation pile on. The math gets ugly fast.

The researchers showed that p-adic AdS/CFT, built on a discrete tree-like geometry called the **Tate curve**, provides a tractable toy model that reproduces the qualitative structure of real finite-temperature CFTs, with computations that actually close.

> **Key Insight:** By replacing continuous curved space with a discrete tree structure and real numbers with p-adic numbers, this paper makes the notoriously hard problem of finite-temperature CFT correlators suddenly computable. The answers parallel the real-world formulas in ways that are hard to dismiss as coincidence.

## How It Works

At the foundation sits the **Bruhat-Tits tree**, the p-adic analog of Anti-de Sitter (AdS) space. In ordinary AdS/CFT, the bulk is a smooth hyperbolic space and the boundary hosts a conformal field theory. In the p-adic version, the bulk is an infinite tree: each vertex connects to p+1 neighbors, branching outward forever, with the "boundary" living at the tree's infinite ends. This discrete structure eliminates derivative operators entirely (a huge technical simplification) while preserving the essential holographic logic.

To introduce temperature, you compactify a direction: wrap one dimension into a finite loop, the way rolling a strip of paper into a cylinder creates a circle. In real AdS/CFT, a thermal CFT lives on a cylinder S¹ × ℝ, and the bulk dual involves a black hole geometry. In the p-adic world, the analogous construction is the Tate curve. You take the Bruhat-Tits tree and glue vertices together using a discrete symmetry, wrapping the tree around a finite thermal cycle. What you get is a central loop (the thermal cycle) with branches hanging off each vertex.

![Figure 1](/iaifi-research-blog/figures/2408_04199/figure_1.png)

The paper proceeds in two stages:

1. **Free theory.** The authors solved the **Dirichlet problem** on the Tate curve, determining how a free massive scalar field in the bulk influences the boundary. The boundary **two-point function** (a measure of how strongly two points are correlated) takes a form that directly parallels its real-place counterpart, with real-number norms replaced by p-adic norms throughout.

2. **Interacting theory.** They turned on perturbative interactions and computed **Witten diagrams**, Feynman-like diagrams encoding boundary correlators. At tree level, they computed the three-point function for operators with generic **scaling dimensions** (quantum numbers characterizing how operators transform under scale changes). At one-loop, they computed the two-point function. Both calculations exploit the discrete Tate curve structure to reduce intractable integrals into manageable sums.

The one-loop two-point result stands out. In real finite-temperature CFTs, one-loop corrections involve complicated sums over operator dimensions from the **OPE** (operator product expansion, a technique describing what happens when two quantum operators are brought close together). The Tate curve produces the same structure, but the p-adic setting strips away the analytic complexity, leaving a clean sum that converges and can be evaluated explicitly for generic scaling dimensions.

![Figure 2](/iaifi-research-blog/figures/2408_04199/figure_2.png)

The paper also carefully tracks a non-thermal limit: as the thermal circle grows large (low temperature), the Tate curve reduces back to the ordinary Bruhat-Tits tree and correlators match zero-temperature p-adic AdS/CFT results. The construction is internally consistent.

## Why It Matters

Finite-temperature CFT is a bottleneck in theoretical physics. The toolkit that makes zero-temperature calculations tractable (conformal blocks, OPE decompositions, Witten diagrams) breaks down or becomes intractably complex once temperature enters. New toy models are needed, especially as experimentalists probe quantum critical phenomena in real materials where temperature effects are unavoidable.

The p-adic setting has a strong track record. Results computed first in p-adic string theory later guided real string theory calculations. Holographic conformal blocks for five- and six-point functions were worked out p-adically before anyone could do the real-place versions. This paper extends that track record to finite-temperature physics, establishing a concrete framework where thermal OPE data, conformal block decompositions at finite temperature, and higher-point thermal correlators are all computable. The natural next step is to use this toy model to conjecture structures for real finite-temperature CFTs, then verify them at the real place.

![Figure 3](/iaifi-research-blog/figures/2408_04199/figure_3.png)

> **Bottom Line:** The Tate curve gives p-adic AdS/CFT a thermal sector, and this paper delivers its complete one-loop and tree-level correlator toolkit: a working laboratory for finite-temperature physics where the hard parts are actually solvable.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects abstract number theory (specifically the arithmetic geometry of p-adic numbers and Tate curves) with quantum gravity and conformal field theory, showing that tools from pure mathematics can unlock computationally intractable problems in theoretical physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The discrete, tree-structured geometries central to p-adic AdS/CFT have informed research on tensor networks and holographic codes relevant to quantum information and AI architectures; this extension to finite temperature opens new directions in that connection.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper delivers explicit, closed-form Witten diagram results for thermal two- and three-point correlators with generic scaling dimensions, providing a concrete toy model for finite-temperature CFT that can guide calculations relevant to quantum phase transitions and strongly coupled systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work can use this framework to compute higher-point thermal correlators and conformal block decompositions in the p-adic setting, with results expected to inform analogous real-place calculations. The paper is available at [arXiv:2408.04199](https://arxiv.org/abs/2408.04199).</span></div></div>
</div>
