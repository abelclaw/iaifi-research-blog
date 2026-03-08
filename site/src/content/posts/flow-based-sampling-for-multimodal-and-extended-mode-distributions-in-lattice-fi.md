---
abstract: Recent results have demonstrated that samplers constructed with flow-based
  generative models are a promising new approach for configuration generation in lattice
  field theory. In this paper, we present a set of training- and architecture-based
  methods to construct flow models for targets with multiple separated modes (i.e.~vacua)
  as well as targets with extended/continuous modes. We demonstrate the application
  of these methods to modeling two-dimensional real and complex scalar field theories
  in their symmetry-broken phases. In this context we investigate different flow-based
  sampling algorithms, including a composite sampling algorithm where flow-based proposals
  are occasionally augmented by applying updates using traditional algorithms like
  HMC.
arxivId: '2107.00734'
arxivUrl: https://arxiv.org/abs/2107.00734
authors:
- Daniel C. Hackett
- Chung-Chun Hsieh
- Sahil Pontula
- Michael S. Albergo
- Denis Boyda
- Jiunn-Wei Chen
- Kai-Feng Chen
- Kyle Cranmer
- Gurtej Kanwar
- Phiala E. Shanahan
concepts:
- normalizing flows
- monte carlo methods
- lattice qcd
- mode collapse
- quantum field theory
- symmetry breaking
- composite mcmc
- phase transitions
- equivariant neural networks
- density estimation
- mixture flow models
- flow matching
- symmetry preservation
figures:
- /iaifi-research-blog/figures/2107_00734/figure_1.png
- /iaifi-research-blog/figures/2107_00734/figure_1.png
- /iaifi-research-blog/figures/2107_00734/figure_2.png
- /iaifi-research-blog/figures/2107_00734/figure_2.png
- /iaifi-research-blog/figures/2107_00734/figure_3.png
- /iaifi-research-blog/figures/2107_00734/figure_3.png
pdfUrl: https://arxiv.org/pdf/2107.00734v2
published: '2021-07-01T20:22:10+00:00'
theme: Theoretical Physics
title: Flow-based sampling for multimodal and extended-mode distributions in lattice
  field theory
wordCount: 1154
---

## The Big Picture

Imagine trying to map a mountain range when you can only wander on foot and thick fog limits your vision. You might stumble into one valley and, unable to see the others, convince yourself you've explored everything — when in reality, you've missed most of the terrain. This is essentially the crisis facing physicists who compute the properties of fundamental particles.

**Quantum Chromodynamics (QCD)** — the theory describing how quarks and gluons bind together inside protons and neutrons — is too mathematically complex for direct calculation. Physicists instead use **lattice field theory**: they carve space and time into a fine grid, then use statistical sampling to estimate the answers they need.

The trouble is that the probability landscape they must sample can split into disconnected islands. Think of a terrain map with two separate peaks and an impassable valley between them — each peak representing a distinct valid quantum state. Standard algorithms like **Hybrid Monte Carlo (HMC)** tend to get stranded on one peak and never visit the other. Physicists call this **topological freezing**, and it causes calculations to return subtly wrong results.

A promising class of methods uses **normalizing flows** — neural networks that learn to generate samples matching a target probability landscape — to escape this trap by jumping freely between peaks. But these models carry their own failure mode: **mode collapse**, where the model quietly learns to ignore entire regions of the landscape, pretending certain peaks don't exist.

A team from MIT, Harvard, Fermilab, National Taiwan University, the University of Wisconsin–Madison, and the University of Edinburgh has developed a comprehensive toolkit of architectural and training strategies to tackle exactly this problem, demonstrating that flow-based sampling can be made robust against mode collapse — and that hybridizing it with traditional methods produces something better than either alone.

> **Key Insight:** Flow-based generative models can be engineered to correctly represent all modes of a multimodal quantum field theory distribution, and when combined with HMC, the two methods compensate for each other's respective weaknesses.

## How It Works

The core technology is a **normalizing flow**: a neural network that learns a smooth, invertible transformation mapping a simple distribution (e.g., a Gaussian) to a complicated target distribution. You train the flow to approximate the probability distribution over all possible field configurations, draw samples independently, then accept or reject them via a **Metropolis-Hastings** correction step — guaranteeing exact results in the long run while bypassing HMC's slow random walk.

The problem emerges in **symmetry-broken phases**, where multiple distinct ground states coexist. Self-training procedures — which refine the flow using its own samples — catastrophically amplify any initial imbalance: if the model slightly undersamples one mode early on, it generates fewer training samples from that region, learns even less about it, and eventually ignores it entirely. The flow looks fine by some metrics but systematically misses half the physics.

![Figure 1](/iaifi-research-blog/figures/2107_00734/figure_1.png)

To fight mode collapse, the researchers assembled two categories of approaches:

**Architectural approaches** bake in knowledge of the mode structure directly:
- **Equivariant flows** constrain the network to respect the target's symmetries (e.g., Z₂), forcing equal weighting of all modes by construction
- **Topology matching** preprocesses the base distribution to mirror the topological structure of the target
- **Mixture models** explicitly combine multiple sub-flows, each targeting different modes, with either separate networks or symmetrized sampling

**Training approaches** modify the loss function or training schedule:
- **Forwards KL training** uses samples drawn from the actual target distribution rather than self-generated samples, breaking the feedback loop that produces collapse
- **Adiabatic retraining** slowly anneals the model from a simpler distribution to the full multimodal target
- **Flow-distance regularization** adds a penalty that discourages the model from concentrating probability mass too tightly

![Figure 3](/iaifi-research-blog/figures/2107_00734/figure_2.png)

The team tested these methods on two-dimensional real scalar field theory (Z₂ symmetry, discrete modes) and complex scalar field theory (U(1) symmetry, a continuous ring of modes — an **extended mode**). They tracked quality using the **effective sample size** — a measure of how many independent, usable samples the flow-plus-Metropolis procedure produces per forward pass.

The verdict: no single method dominates universally, but equivariant flows combined with forwards KL training consistently produced the most reliable results. Mixture models with adaptive weighting also performed well when the symmetry structure wasn't known in advance.

![Figure 5](/iaifi-research-blog/figures/2107_00734/figure_3.png)

The team's most practically powerful contribution is their **composite sampling algorithm**. Rather than committing entirely to flow-based or HMC sampling, it interleaves HMC steps between flow proposals. The logic is elegant: flow models excel at jumping between modes (something HMC almost never manages once topological freezing sets in), while HMC excels at exploring within a mode (something the flow may do imprecisely if it undersamples regions between modes). Together, they patch each other's blind spots.

## Why It Matters

Lattice field theory is currently the only systematic, non-perturbative method for calculating nuclear physics from first principles. Calculations of quantities like the proton's internal structure, the neutron's electric dipole moment, and the masses of exotic hadrons all depend on efficiently sampling field configurations. As physicists push toward finer lattices and more realistic quark masses, topological freezing becomes so severe that even state-of-the-art supercomputer runs can fail to sample all topological sectors — rendering results subtly wrong.

![Figure 6](/iaifi-research-blog/figures/2107_00734/figure_3.png)

This paper does not yet solve full QCD — the authors frame their 2D scalar field demonstrations as testbeds, not production tools. But the methods are general and modular. The architectural tricks (equivariance, topology matching, mixtures) and training tricks (forwards KL, adiabatic annealing, flow-distance regularization) are all applicable to more complex theories.

The composite sampling framework offers a particularly pragmatic path: rather than waiting for flows that perfectly model QCD, physicists can deploy partially-trained flows to accelerate HMC right now, gaining benefits even when the flow is imperfect.

> **Bottom Line:** By systematically cataloguing and benchmarking strategies to prevent mode collapse in flow-based samplers, this work lays essential groundwork for applying machine-learning-enhanced sampling to full QCD — potentially unlocking calculations that are computationally out of reach today.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits at the exact intersection of IAIFI's mission, applying cutting-edge generative modeling techniques directly to the sampling problems that bottleneck nuclear and particle physics calculations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper contributes novel architectural and training strategies for flow-based generative models in multimodal settings — including forwards KL self-training and flow-distance regularization — with broad applicability to any domain where mode collapse is a concern.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By demonstrating reliable flow-based sampling in symmetry-broken phases of scalar field theories, the work takes a concrete step toward solving topological freezing in lattice QCD, a longstanding obstacle to precision nuclear and hadron physics predictions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include scaling these composite and equivariant methods to gauge theories like QCD and developing automated mode-discovery for cases where the symmetry structure is unknown; the full paper is available at arXiv:2111.02989.</span></div></div>
</div>
