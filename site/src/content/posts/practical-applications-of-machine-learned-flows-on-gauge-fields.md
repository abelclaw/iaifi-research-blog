---
abstract: Normalizing flows are machine-learned maps between different lattice theories
  which can be used as components in exact sampling and inference schemes. Ongoing
  work yields increasingly expressive flows on gauge fields, but it remains an open
  question how flows can improve lattice QCD at state-of-the-art scales. We discuss
  and demonstrate two applications of flows in replica exchange (parallel tempering)
  sampling, aimed at improving topological mixing, which are viable with iterative
  improvements upon presently available flows.
arxivId: '2404.11674'
arxivUrl: https://arxiv.org/abs/2404.11674
authors:
- Ryan Abbott
- Michael S. Albergo
- Denis Boyda
- Daniel C. Hackett
- Gurtej Kanwar
- Fernando Romero-López
- Phiala E. Shanahan
- Julian M. Urban
concepts:
- normalizing flows
- lattice qcd
- lattice gauge theory
- parallel tempering
- monte carlo methods
- topological freezing
- density estimation
- equivariant neural networks
- simulation-based inference
- stochastic processes
- transfer learning
figures:
- /iaifi-research-blog/figures/2404_11674/figure_1.png
pdfUrl: https://arxiv.org/pdf/2404.11674v1
published: '2024-04-17T18:17:14+00:00'
theme: Theoretical Physics
title: Practical applications of machine-learned flows on gauge fields
wordCount: 1076
---

## The Big Picture

Imagine trying to map every possible configuration of a city's traffic by randomly sampling routes, but discovering that your sampling algorithm keeps getting stuck in the same neighborhoods, missing entire districts. That's roughly the problem physicists face when simulating the quantum vacuum of the strong nuclear force.

At the finest scales needed for precision physics, their tools hit a wall called **topological freezing**: the simulation traps itself in one family of field configurations and can't escape to explore others. Like a map with entire regions left forever blank.

**Lattice QCD** (quantum chromodynamics on a discrete spacetime grid) is the gold standard for computing properties of protons, neutrons, and the strong force from first principles. But as researchers push to finer lattice spacings, essential for higher precision, standard sampling algorithms slow to a crawl. They take exponentially longer between each genuinely independent sample. This isn't a technical footnote. It's the difference between testing the Standard Model at precision sufficient to detect new physics, and being stuck.

Machine learning has entered this arena with **normalizing flows**, generative models that learn to transform one collection of random samples into another through a perfectly reversible process. The question this paper asks is pointed: not "can flows eventually replace traditional samplers?" but "how can flows we have *right now* already make things better?"

> **Key Insight:** Rather than waiting for perfect flow models, this work shows how imperfect flows can already provide real computational gains when combined with existing parallel tempering techniques, by bridging nearby theories or repairing action defects.

## How It Works

The core object is a **flow**, a learned invertible transformation *f* that maps gauge field configurations from one probability distribution to another. The map is reversible and its **Jacobian determinant** (the "stretch factor" measuring how much the transformation locally compresses or expands probability) is computable, so the flow provides an exact accounting of where samples came from and how likely they are.

![Figure 1](/iaifi-research-blog/figures/2404_11674/figure_1.png)

The researchers work in pure-gauge SU(3) with the Wilson gauge action, using a residual flow architecture with 16 coupling layers. Each layer updates half the lattice links conditioned on the frozen ones, a design ensuring invertibility while keeping the Jacobian tractable. The real novelty isn't the architecture; it's *how* the flows get deployed.

The paper demonstrates two distinct strategies, both built around **replica exchange** (parallel tempering), a technique where multiple simulations at different parameters run in parallel and periodically swap configurations:

- **Transformed Replica Exchange (T-REX):** Instead of swapping raw configurations between replicas, a flow transforms configurations before proposing swaps. It bridges two nearby theories, making proposed swaps far more likely to be accepted. Topological mixing improves across the entire replica ladder, and even simulations far from the flow's training target benefit indirectly.

- **Defect Repair:** A deliberately unphysical "defect" action lowers barriers between topological sectors, letting a separate replica mix freely across them. A flow then maps configurations from this defect theory back to the physical theory. These repaired configurations inject topological diversity into the physical replica that standard sampling couldn't achieve alone.


Both strategies share one feature that matters: they don't require perfect flows. An approximate flow simply reduces acceptance rates without biasing results. Exact statistics are recovered via the Metropolis acceptance step. Imperfect flows become useful *components* in exact sampling machinery, rather than needing to replace it wholesale.


Training uses **reverse KL self-training with path gradients**: the flow generates its own training samples, compares them to the target distribution, and uses gradients traced back through the sampling process to reduce noise. The base distributions are already gauge theories at positive coupling, which makes training harder but more relevant to real applications.

## Why It Matters

Topological freezing is one of the most concrete obstacles between current lattice QCD capabilities and the precision physics the field needs. Experiments at the Large Hadron Collider and future facilities will push hadronic measurements to sub-percent precision, but theoretical predictions lag because simulations can't reach fine enough lattice spacings without prohibitive cost. The strategies here offer a viable path forward without waiting for a fully generative flow model of QCD, a target still years away.

The prevailing narrative has been "flows as replacements for MCMC," a demanding goal requiring near-perfect models. This paper makes a case for "flows as accelerators *inside* MCMC," which is far more achievable in the near term.

The two strategies are complementary and composable, both with each other and with future improvements. As flow expressiveness grows through better architectures, larger models, or transfer learning across volumes, both strategies benefit automatically.

> **Bottom Line:** Machine-learned normalizing flows can already improve lattice QCD sampling through clever integration with parallel tempering, even at current model quality, turning an aspirational long-term goal into a practical near-term tool for resolving topological freezing.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects state-of-the-art generative ML with a core computational challenge in particle physics, showing that machine learning can enhance established Monte Carlo methods in lattice QCD rather than merely replacing them.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper establishes a practical framework for deploying approximate generative models as exact-sampling components via Metropolis correction. This broadens the utility of normalizing flows well beyond the "perfect model" regime where most demonstrations have focused.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By demonstrating viable strategies to mitigate topological freezing, a long-standing barrier to fine-lattice QCD simulations, this work opens a path toward higher-precision theoretical predictions for the strong nuclear force, needed for testing the Standard Model.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend these strategies to full QCD with dynamical fermions, scaling to larger volumes as flow architectures improve. Full methodology is detailed in the companion publication ([arXiv:2307.11913](https://arxiv.org/abs/2307.11913)), with this proceedings contribution from Lattice 2023.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Practical applications of machine-learned flows on gauge fields</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2404.11674](https://arxiv.org/abs/2404.11674)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">Ryan Abbott, Michael S. Albergo, Denis Boyda, Daniel C. Hackett, Gurtej Kanwar, Fernando Romero-López, Phiala E. Shanahan, Julian M. Urban</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Normalizing flows are machine-learned maps between different lattice theories which can be used as components in exact sampling and inference schemes. Ongoing work yields increasingly expressive flows on gauge fields, but it remains an open question how flows can improve lattice QCD at state-of-the-art scales. We discuss and demonstrate two applications of flows in replica exchange (parallel tempering) sampling, aimed at improving topological mixing, which are viable with iterative improvements upon presently available flows.</span></div></div>
</div>
