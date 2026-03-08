---
abstract: The data-taking conditions expected in Run 3 of the LHCb experiment at CERN
  are unprecedented and challenging for the software and computing systems. Despite
  that, the LHCb collaboration pioneers the use of a software-only trigger system
  to cope with the increased event rate efficiently. The beauty physics programme
  of LHCb is heavily reliant on topological triggers. These are devoted to selecting
  beauty-hadron candidates inclusively, based on the characteristic decay topology
  and kinematic properties expected from beauty decays. The following proceeding describes
  the current progress of the Run 3 implementation of the topological triggers using
  Lipschitz monotonic neural networks. This architecture offers robustness under varying
  detector conditions and sensitivity to long-lived candidates, improving the possibility
  of discovering New Physics at LHCb.
arxivId: '2306.09873'
arxivUrl: https://arxiv.org/abs/2306.09873
authors:
- Nicole Schulte
- Blaise Raheem Delaney
- Niklas Nolte
- Gregory Max Ciezarek
- Johannes Albrecht
- Mike Williams
concepts:
- trigger systems
- lipschitz neural networks
- monotonic neural networks
- robustness
- new physics searches
- collider physics
- event reconstruction
- classification
- out-of-distribution detection
- particle tracking
- calibration
- ensemble methods
figures:
- /iaifi-research-blog/figures/2306_09873/figure_1.png
- /iaifi-research-blog/figures/2306_09873/figure_2.png
- /iaifi-research-blog/figures/2306_09873/figure_3.png
pdfUrl: https://arxiv.org/pdf/2306.09873v2
published: '2023-06-16T14:36:39+00:00'
theme: Experimental Physics
title: Development of the Topological Trigger for LHCb Run 3
wordCount: 1228
---

## The Big Picture

Imagine trying to find a single interesting conversation in a stadium packed with 30 million people, all talking at once, every single second. That's roughly the challenge facing physicists at CERN's LHCb experiment as it enters its third major data-taking run. Protons collide 30 million times per second inside the detector, and buried somewhere in that avalanche are the rare decays of **beauty particles**, exotic relatives of the proton and neutron that carry clues about why the universe is made of matter rather than antimatter.

LHCb can't store everything. That would require impossible amounts of disk space. Instead, it makes split-second decisions about which collisions are worth keeping, discarding the rest forever.

This real-time selection system is called a **trigger**, and getting it right is existential for the physics programme. In Run 3, LHCb went further than any major experiment before it: it ditched hardware filters entirely and ran a fully software-based trigger, processing every collision with intelligent algorithms on the fly.

A team from MIT, TU Dortmund, and CERN developed the centerpiece of that system, a neural network-based selection called the **topological trigger**. The name comes from the distinctive geometric arrangement of particle tracks that beauty decays leave in the detector.

> **Key Insight:** By using Lipschitz monotonic neural networks, the Run 3 topological trigger stays stable under messy real-world detector conditions while remaining sensitive to unknown new particles that weren't included in its training data.

## How It Works

Beauty hadrons, particles containing a bottom quark, have a telltale signature in LHCb's detector. They're produced at the collision point, travel a centimeter or two, and then decay into a spray of lighter particles. That gap between the **primary vertex** (where protons collide) and the **secondary vertex** (where the beauty particle decays) is the topological trigger's bread and butter.

The trigger reconstructs this signature on the fly by pairing up charged particle tracks, fitting a vertex to each pair, and computing a set of kinematic variables:

- **Momentum** — how energetically the particles are moving
- **Impact parameter** — how far a track misses the original collision point
- **Flight distance** — the separation between primary and secondary vertices
- **Vertex quality** — how cleanly the tracks converge at the decay point

Two versions run in parallel: one targeting two-body beauty decays and one targeting three-body decays. For the three-body algorithm, the two-body combination is treated as a single "super-particle" and a third track is attached. This hierarchical approach keeps the number of possible combinations manageable.

![Figure 1](/iaifi-research-blog/figures/2306_09873/figure_1.png)

In Run 2, the selection engine was a **boosted decision tree (BDT)**, a reliable workhorse delivering roughly 80% signal efficiency. For Run 3, the team upgraded to **Lipschitz monotonic neural networks**. The reasons come down to two things: engineering resilience and physics ambition.

The **Lipschitz constraint** guarantees that small changes to detector conditions (calibrations drifting, noise fluctuations, alignment shifts) can only change the network's output score by a bounded amount. Formally: given two input configurations *x* and *x'*, the outputs *M(x)* and *M(x')* can differ by no more than a fixed multiple of how different the inputs were. This keeps the trigger stable across a multi-year data-taking campaign and keeps measurement uncertainties under control for downstream analyses.

**Monotonicity** adds a second constraint, one with direct physical motivation. The network is built so that improving any input feature (higher momentum, better vertex quality, longer flight distance) can only increase the output score, never decrease it. A candidate that looks *more* like a beauty decay in every measurable way must score at least as high as a less extreme version.

![Figure 2](/iaifi-research-blog/figures/2306_09873/figure_2.png)

The physics payoff is concrete. If some exotic long-lived particle from beyond the Standard Model (BSM), physics' best current theory of fundamental particles and forces, appears in the detector, behaving like a "super-beauty" candidate in all measurable dimensions, the monotonic network won't accidentally reject it just because it falls outside the training distribution. Sensitivity to the unknown, baked into the architecture.

## Why It Matters

LHCb's Run 3 trigger architecture marks a real shift in how particle physics experiments are built. Every major previous experiment used hardware pre-filters, dedicated electronics that discard most collisions before software ever sees them. LHCb's decision to go fully software-based, processing 30 MHz of collisions and reducing them to 100 kHz using only intelligent algorithms, is a serious bet on machine learning. The topological trigger, which produces the largest output bandwidth of any selection algorithm in **HLT2** (the second-stage software filter that makes the final keep-or-discard decision), sits at the heart of that bet.

![Figure 3](/iaifi-research-blog/figures/2306_09873/figure_3.png)

The Lipschitz monotonic architecture also shows what it looks like to build ML systems for physics that are *interpretable by construction*, not just after the fact. The Lipschitz bound and monotonicity are hard mathematical guarantees, not post-hoc explanations. The trigger's response to particles with unexpectedly long lifetimes has been carefully characterized, making BSM sensitivity a first-class feature of the design rather than an afterthought.

As particle physics increasingly relies on neural networks for critical data-taking decisions, this approach (encoding physical intuitions directly into the network architecture) is a useful model. It shows that the constraints physicists care about can be structural properties of the network, not just things you hope the training process will learn.

> **Bottom Line:** The Run 3 LHCb topological trigger replaces a boosted decision tree with Lipschitz monotonic neural networks, delivering stability under shifting detector conditions and built-in sensitivity to undiscovered physics. It's a case where the ML architecture and the physics requirements are genuinely aligned.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work shows how principled ML architectures, specifically Lipschitz-constrained monotonic networks, can satisfy both engineering constraints (stability under detector drift) and physics goals (sensitivity to new particles) within a production system at a major experiment.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Lipschitz monotonic neural networks provide a concrete example of physics-motivated inductive biases improving ML stability. The architectural guarantees may transfer to other domains that need certified behavior under distribution shift.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The topological trigger enables LHCb's beauty physics programme at Run 3 luminosities and could open a window to long-lived BSM particles that prior trigger designs would have missed.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">As LHCb continues collecting data at record luminosity, the trigger's performance on real data and its sensitivity to specific BSM scenarios will be key benchmarks; this work is available at [arXiv:2306.09873](https://arxiv.org/abs/2306.09873).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Development of the Topological Trigger for LHCb Run 3</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2306.09873</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Nicole Schulte", "Blaise Raheem Delaney", "Niklas Nolte", "Gregory Max Ciezarek", "Johannes Albrecht", "Mike Williams"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">The data-taking conditions expected in Run 3 of the LHCb experiment at CERN are unprecedented and challenging for the software and computing systems. Despite that, the LHCb collaboration pioneers the use of a software-only trigger system to cope with the increased event rate efficiently. The beauty physics programme of LHCb is heavily reliant on topological triggers. These are devoted to selecting beauty-hadron candidates inclusively, based on the characteristic decay topology and kinematic properties expected from beauty decays. The following proceeding describes the current progress of the Run 3 implementation of the topological triggers using Lipschitz monotonic neural networks. This architecture offers robustness under varying detector conditions and sensitivity to long-lived candidates, improving the possibility of discovering New Physics at LHCb.</span></div></div>
</div>
