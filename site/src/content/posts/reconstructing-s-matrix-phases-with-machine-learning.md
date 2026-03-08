---
abstract: An important element of the $S$-matrix bootstrap program is the relationship
  between the modulus of an $S$-matrix element and its phase. Unitarity relates them
  by an integral equation. Even in the simplest case of elastic scattering, this integral
  equation cannot be solved analytically and numerical approaches are required. We
  apply modern machine learning techniques to studying the unitarity constraint. We
  find that for a given modulus, when a phase exists it can generally be reconstructed
  to good accuracy with machine learning. Moreover, the loss of the reconstruction
  algorithm provides a good proxy for whether a given modulus can be consistent with
  unitarity at all. In addition, we study the question of whether multiple phases
  can be consistent with a single modulus, finding novel phase-ambiguous solutions.
  In particular, we find a new phase-ambiguous solution which pushes the known limit
  on such solutions significantly beyond the previous bound.
arxivId: '2308.09451'
arxivUrl: https://arxiv.org/abs/2308.09451
authors:
- Aurélien Dersy
- Matthew D. Schwartz
- Alexander Zhiboedov
concepts:
- scattering amplitudes
- phase ambiguity
- inverse problems
- s-matrix bootstrap
- quantum field theory
- physics-informed neural networks
- loss function design
- loss landscape
- regression
- uncertainty quantification
figures:
- /iaifi-research-blog/figures/2308_09451/figure_1.png
- /iaifi-research-blog/figures/2308_09451/figure_2.png
- /iaifi-research-blog/figures/2308_09451/figure_3.png
pdfUrl: https://arxiv.org/pdf/2308.09451v1
published: '2023-08-18T10:29:26+00:00'
theme: Theoretical Physics
title: Reconstructing $S$-matrix Phases with Machine Learning
wordCount: 1000
---

## The Big Picture

Imagine listening to music through a wall. You can hear the volume of each note, how loud the bass, how strong the treble, but you've lost something crucial: the timing, the rhythm, the way notes relate to each other in time. That missing information is the *phase*.

In quantum particle physics, experimentalists face an almost identical problem. When two particles collide, detectors measure how many particles scatter in each direction, essentially the *magnitude* of the scattering. But the underlying quantum description is a complex number, carrying both a magnitude and a hidden rotation called the **phase**, invisible to detectors.

Recovering that hidden phase from measurable data is one of the oldest unsolved problems in theoretical physics. The full quantum description encodes everything about fundamental particle interactions, and without the phase, our picture remains incomplete. The problem is governed by the **unitarity constraint**, which enforces the requirement that all probabilities must add up to one, linking magnitude to phase through an integral equation with no known analytical solution even in the simplest two-particle case.

Now, researchers Aurélien Dersy, Matthew Schwartz, and Alexander Zhiboedov from Harvard and CERN have shown that modern machine learning can crack this problem with impressive accuracy, and do something even more surprising along the way.

> **Key Insight:** A machine learning algorithm can reconstruct the quantum phase from a given scattering magnitude, and its *failure* to do so reliably signals that no valid phase exists at all, turning the optimization itself into a diagnostic for physical consistency.

## How It Works

The central object of study is the **S-matrix**, the mathematical framework encoding all possible scattering outcomes between particles. At fixed energy, the scattering amplitude can be written as a magnitude times a complex phase factor. Unitarity imposes a strict relationship between the two through an integral equation. The question: given the magnitude, can you find the phase?

The ML approach frames this as an optimization problem with three steps:

1. **Represent** the unknown phase using a neural network, a flexible function approximator.
2. **Define** a loss function measuring how well the unitarity equation is satisfied.
3. **Minimize** the loss by iteratively adjusting the network's parameters until the equation is satisfied as well as possible.

The method works across a broad range of test cases: simple linear and quadratic magnitudes, as well as physically important **extremal amplitudes** that push right up against the theoretical limits of what's allowed.

![Figure 1](/iaifi-research-blog/figures/2308_09451/figure_1.png)

But the real payoff comes from what the loss value *itself* reveals. A low loss means the network successfully satisfied the constraint. A high loss strongly suggests no consistent phase exists. This makes the loss a practical **unitarity feasibility probe**, no new physics required, just a clever reuse of the optimization signal.

**Finding phase ambiguities.** Beyond reconstruction, the paper tackles a deeper question: can two completely different phases produce the *same* magnitude? This **phase ambiguity** problem has been studied since the 1970s, but progress stalled. For elastic scattering (where particles bounce without changing identity) with infinitely many partial waves, classical results showed that at most two phases could correspond to a given magnitude. Explicit examples of such pairs were rare.

To find phase-ambiguous solutions, the researchers added a **repulsive loss** term. Two networks run simultaneously, both trying to satisfy unitarity for the same magnitude, but penalized for converging to the same answer. This forces each network to explore different regions, hunting for distinct valid phases.

![Figure 2](/iaifi-research-blog/figures/2308_09451/figure_2.png)

For finitely many partial waves, where at most 2^L phases can exist for L partial waves, the method finds multiple solutions systematically. For the infinite partial wave case, the team discovered new phase-ambiguous solutions that push well beyond bounds established decades ago.

![Figure 3](/iaifi-research-blog/figures/2308_09451/figure_3.png)

The mathematical scaffolding comes from classical complex analysis: **Blaschke products**, which express scattering amplitudes using the locations of zeros of a complex-valued function. ML provides the numerical muscle to search through the vast space of possible solutions.

## Why It Matters

This work connects two of the most active frontiers in theoretical physics. The **S-matrix bootstrap** program tries to constrain quantum field theories purely from consistency conditions like unitarity, analyticity, and crossing symmetry, without assuming a specific underlying model. It has seen a major revival over the past decade.

Being able to rapidly test whether a given scattering amplitude is consistent with unitarity, and to find all consistent phases, directly accelerates this program. Problems that once required laborious analytical work can now be explored at scale.

On the AI side, the paper shows that physics-informed neural networks can go beyond approximating known solutions. They can probe whether solutions *exist* and whether they are *unique*. The loss-as-feasibility-probe idea is especially clean: it turns a failed optimization into information rather than a dead end.

Future directions include extending the method to inelastic scattering, applying it to realistic collider data, and mapping the full space of physically consistent S-matrices.

> **Bottom Line:** Machine learning doesn't just solve the decades-old phase reconstruction problem. It uncovers new phase-ambiguous solutions that push known theoretical bounds, opening a computational path into the S-matrix bootstrap program.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies modern neural network optimization to a foundational problem in theoretical particle physics, showing that machine learning can both solve and test the consistency of quantum mechanical constraints that have resisted analytical solution for over 50 years.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The repulsive loss technique, running two networks that penalize convergence to the same solution, offers a fresh strategy for finding multiple distinct solutions to nonlinear integral equations, with potential applications beyond physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The discovery of new phase-ambiguous S-matrix solutions extends known mathematical bounds on the unitarity phase problem, providing concrete benchmarks for the S-matrix bootstrap program and opening previously inaccessible regions of amplitude space.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions to inelastic scattering and direct application to experimental cross-section data could make phase reconstruction a practical tool for collider physics; the full paper is available at [arXiv:2308.09451](https://arxiv.org/abs/2308.09451).</span></div></div>
</div>
