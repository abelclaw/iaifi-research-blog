---
abstract: 'Extracting scientific understanding from particle-physics experiments requires
  solving diverse learning problems with high precision and good data efficiency.
  We propose the Lorentz Geometric Algebra Transformer (L-GATr), a new multi-purpose
  architecture for high-energy physics. L-GATr represents high-energy data in a geometric
  algebra over four-dimensional space-time and is equivariant under Lorentz transformations,
  the symmetry group of relativistic kinematics. At the same time, the architecture
  is a Transformer, which makes it versatile and scalable to large systems. L-GATr
  is first demonstrated on regression and classification tasks from particle physics.
  We then construct the first Lorentz-equivariant generative model: a continuous normalizing
  flow based on an L-GATr network, trained with Riemannian flow matching. Across our
  experiments, L-GATr is on par with or outperforms strong domain-specific baselines.'
arxivId: '2405.14806'
arxivUrl: https://arxiv.org/abs/2405.14806
authors:
- Jonas Spinner
- Victor Bresó
- Pim de Haan
- Tilman Plehn
- Jesse Thaler
- Johann Brehmer
concepts:
- equivariant neural networks
- geometric deep learning
- geometric algebra
- transformers
- flow matching
- attention mechanisms
- group theory
- normalizing flows
- generative models
- scattering amplitudes
- collider physics
- surrogate modeling
- jet physics
figures:
- /iaifi-research-blog/figures/2405_14806/figure_1.png
- /iaifi-research-blog/figures/2405_14806/figure_1.png
- /iaifi-research-blog/figures/2405_14806/figure_2.png
- /iaifi-research-blog/figures/2405_14806/figure_2.png
- /iaifi-research-blog/figures/2405_14806/figure_3.png
- /iaifi-research-blog/figures/2405_14806/figure_3.png
pdfUrl: https://arxiv.org/pdf/2405.14806v3
published: '2024-05-23T17:15:41+00:00'
theme: Foundational AI
title: Lorentz-Equivariant Geometric Algebra Transformers for High-Energy Physics
wordCount: 1031
---

## The Big Picture

Imagine teaching a student physics by making them memorize every possible outcome of every possible experiment — without ever mentioning symmetry. They'd eventually learn that dropping a ball in Paris gives the same result as dropping one in Tokyo, but only after seeing both. Now imagine teaching them instead that the laws of physics don't care about location. Suddenly, one observation generalizes everywhere. That's the power of building symmetry directly into the learning process.

At the Large Hadron Collider, protons smash together at nearly the speed of light, generating roughly a petabyte of raw data every second. Finding the Higgs boson, hunting for new particles, testing the Standard Model — all of it requires machine learning at every step. But most ML architectures were designed for images or language, not relativistic particle collisions. They can learn the relevant symmetries eventually, but only through brute-force pattern-matching across enormous datasets. In high-energy physics, data is expensive.

A team from Heidelberg University, MIT, IAIFI, and Qualcomm AI Research has built a smarter alternative: the **Lorentz Geometric Algebra Transformer (L-GATr)**, a neural network that speaks the language of special relativity natively.

> **Key Insight:** By encoding Lorentz symmetry directly into the network architecture, L-GATr learns from particle physics data more efficiently and more accurately than architectures that must discover symmetry on their own.

## How It Works

The architecture rests on three interlocking ideas, each addressing a different gap in existing tools.

![Figure 1](/iaifi-research-blog/figures/2405_14806/figure_1.png)

The first is **Lorentz equivariance** — the property that the network's outputs transform predictably when you shift reference frames. In special relativity, all physical laws obey this rule: the mass of a particle doesn't change whether you measure from a stationary lab or a moving train. Most neural networks violate this implicitly, forcing the model to approximate it from data. L-GATr bakes it in mathematically, so the guarantee is exact by construction. The paper also handles **symmetry-breaking inputs**, accommodating real-world cases where detector geometry or beam direction disrupts perfect Lorentz symmetry.

The second idea is the representation. Rather than feeding the network plain four-vectors — the energy and momentum coordinates describing each particle — L-GATr encodes everything in the **geometric algebra** (also called Clifford algebra) over four-dimensional spacetime. Think of this as upgrading from speaking only in nouns to having a full grammar: scalars, vectors, **bivectors** (quantities describing oriented areas in spacetime), and higher-grade objects all live in one unified algebraic structure. This gives the network richer building blocks while keeping every computation Lorentz-equivariant — naturally capturing invariant masses, decay angles, and other quantities physicists care about.

The third piece is the Transformer backbone. Transformers compute **pairwise attention** between all inputs — here, all particles in a collision event — making them natural fits for variable-length particle lists. They also support optimized backends like Flash Attention, so L-GATr inherits years of engineering work on large-scale training.

To make this work, the authors developed several new layers from scratch:
- A **maximally expressive Lorentz-equivariant linear map** for mixing geometric algebra components
- A **Lorentz-equivariant attention mechanism** replacing standard dot-product attention
- **Lorentz-equivariant layer normalization** — a subtle challenge, since naive normalization breaks the symmetry

![Figure 2](/iaifi-research-blog/figures/2405_14806/figure_1.png)

Beyond classification and regression, the paper introduces something genuinely new: the first Lorentz-equivariant generative model. The authors build a **continuous normalizing flow** on top of L-GATr and train it with **Riemannian flow matching** — a method that respects the curved geometry of particle-physics phase space. This lets the model hard-code the sharp probability boundaries arising from detector cuts and kinematic constraints, rather than learning them laboriously from data.

## Why It Matters

The three benchmark tasks span very different parts of the LHC analysis chain. Amplitude surrogates ask the network to mimic complex quantum field theory calculations — a precision regression problem. Top quark tagging is a well-established classification benchmark, distinguishing jets produced by top quarks from those produced by other processes. Generative modeling of reconstructed particles attacks the simulation bottleneck that limits nearly every LHC analysis.

That L-GATr matches or outperforms specialized baselines across all three tasks makes the core argument: a single general-purpose equivariant architecture can replace a collection of task-specific tools.

The broader implication is architectural philosophy. Domain-specific models built for one task can't easily transfer. L-GATr is a single backbone that plugs into the entire analysis pipeline. As collider experiments grow more demanding — the High-Luminosity LHC upgrade will increase collision rates fivefold — the demand for data-efficient, versatile architectures will only intensify. Building Lorentz symmetry in from the start is not just elegant; it's a practical engineering advantage.

![Figure 4](/iaifi-research-blog/figures/2405_14806/figure_2.png)

Natural extensions are already visible. The current architecture handles the Lorentz group but not the full **Poincaré group**, which also includes spacetime translations. Long-lived particles that travel measurable distances before decaying would require tracking absolute positions — an extension straightforward in principle. The framework could also extend to other symmetry groups relevant to particle physics: SU(3) color symmetry governs the strong force and remains largely untouched by equivariant ML.

> **Bottom Line:** L-GATr proves that encoding special relativity's symmetry directly into a Transformer is both achievable and worth it — matching or beating specialized tools across regression, classification, and generative modeling, while remaining a single flexible backbone that slots into every stage of LHC analysis.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">L-GATr directly bridges geometric deep learning and relativistic particle physics, translating the mathematical structure of special relativity into a practical neural network backbone deployed across multiple stages of LHC data analysis.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces new Lorentz-equivariant attention mechanisms, linear maps, and layer normalization techniques, along with the first equivariant generative model trained with Riemannian flow matching — concrete additions to the toolkit of geometric deep learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By building Lorentz equivariance into a general-purpose architecture, L-GATr improves data efficiency across high-energy physics tasks from quantum amplitude regression to particle-level simulation, directly addressing the computational bottlenecks of LHC science.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend the architecture to the full Poincaré group and gauge symmetries of the Standard Model; the paper and implementation are available at arXiv and the Heidelberg HEP ML group repository.</span></div></div>
</div>
