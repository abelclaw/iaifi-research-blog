---
abstract: 'Machine learning frameworks for physical problems must capture and enforce
  physical constraints that preserve the structure of dynamical systems. Many existing
  approaches achieve this by integrating physical operators into neural networks.
  While these methods offer theoretical guarantees, they face two key limitations:
  (i) they primarily model local relations between adjacent time steps, overlooking
  longer-range or higher-level physical interactions, and (ii) they focus on forward
  simulation while neglecting broader physical reasoning tasks. We propose the Denoising
  Hamiltonian Network (DHN), a novel framework that generalizes Hamiltonian mechanics
  operators into more flexible neural operators. DHN captures non-local temporal relationships
  and mitigates numerical integration errors through a denoising mechanism. DHN also
  supports multi-system modeling with a global conditioning mechanism. We demonstrate
  its effectiveness and flexibility across three diverse physical reasoning tasks
  with distinct inputs and outputs.'
arxivId: '2503.07596'
arxivUrl: https://arxiv.org/abs/2503.07596
authors:
- Congyue Deng
- Brandon Y. Feng
- Cecilia Garraffo
- Alan Garbarz
- Robin Walters
- William T. Freeman
- Leonidas Guibas
- Kaiming He
concepts:
- hamiltonian systems
- neural operators
- denoising physical trajectories
- diffusion models
- conservation laws
- physics-informed neural networks
- transformers
- inverse problems
- symmetry preservation
- multi-task learning
- superresolution
- disentangled representations
figures:
- /iaifi-research-blog/figures/2503_07596/figure_1.png
- /iaifi-research-blog/figures/2503_07596/figure_3.png
pdfUrl: https://arxiv.org/pdf/2503.07596v1
published: '2025-03-10T17:57:01+00:00'
theme: Foundational AI
title: Denoising Hamiltonian Network for Physical Reasoning
wordCount: 974
---

## The Big Picture

Imagine watching a pendulum swing. A physicist from three centuries ago could predict its position tomorrow, not by tracking every moment, but by invoking a single elegant principle: energy is conserved. You don't need to follow each tick of the clock. You can leap directly from the starting point to the answer using global laws.

Modern AI has largely forgotten this lesson. Most AI systems trained to respect physics work like careful accountants, tallying up each time step one by one: feed them the current state of a system, and they'll tell you the state one moment later. This approach works, but it ignores the sweeping, global reasoning that made classical physics so powerful in the first place. It also means these models can only do one thing: simulate forward. Ask them to fill in a gap in a trajectory, or infer a pendulum's mass from scattered observations, and they're stuck.

A team from MIT, Stanford, Harvard-Smithsonian, and Northeastern has built something better. Their **Denoising Hamiltonian Network (DHN)** takes the mathematical skeleton of **Hamiltonian mechanics** (the 19th-century framework that describes physical systems entirely through their total energy) and stretches it into a flexible architecture that handles a whole menu of physical reasoning tasks at once.

> **Key Insight:** DHN extends the energy-based rules of Hamiltonian mechanics into a neural network that reasons across the full sweep of a trajectory, not just from one moment to the next, while using a denoising process to stay physically grounded even as predictions grow complex.

## How It Works

In a Hamiltonian system, knowing the energy function lets you derive the equations of motion exactly. Energy conservation links distant points in a trajectory without requiring you to trace every step in between.

Earlier **Hamiltonian Neural Networks (HNNs)**, AI architectures that embedded this energy-based structure, did encode Hamiltonian rules, but they were essentially glorified one-step integrators. DHN breaks out of that box in three ways.

**First: treating trajectories as sequences, not chains.** Instead of passing a single state from step to step, DHN groups states into **tokens** and processes them with a **transformer**, a neural network architecture originally developed for language modeling that excels at finding relationships across long sequences. This lets the network attend to the full temporal context, the way a reader understands a sentence by weighing the whole passage, not just the preceding word.

![Figure 1](/iaifi-research-blog/figures/2503_07596/figure_1.png)

**Second: a denoising objective.** Inspired by **diffusion models** (the AI systems behind image generators like DALL-E and Stable Diffusion), DHN doesn't just predict trajectories: it learns to *denoise* them. During training, the network sees corrupted versions of physical trajectories and learns to recover the clean, physically valid path underneath. The payoff is better stability over long forecasting horizons and a built-in mechanism for handling sparse, noisy, or incomplete data. Different noise patterns unlock different tasks: the same trained model can complete a partial trajectory, infer system parameters, or interpolate sparse observations just by changing the conditioning structure.

![Figure 2](/iaifi-research-blog/figures/2503_07596/figure_3.png)

**Third: global conditioning for multi-system modeling.** Most HNNs model one physical system at a time. Pendulums of different lengths require separate models. DHN solves this with a **global latent code**, a learned embedding that encodes system-specific properties like mass or length. A single DHN generalizes across physically distinct systems without abandoning the underlying Hamiltonian structure.

The researchers tested this across three genuinely different tasks:

- **Trajectory prediction and completion:** given a partial trajectory, predict the rest
- **Physical parameter inference:** given scattered observations, infer the system's physical properties (mass, length)
- **Sparse super-resolution:** given coarsely sampled data, fill in fine-grained dynamics

Each task has different inputs and outputs. A single DHN handles all three, something standard HNNs simply can't do.


## Why It Matters

The deeper significance here isn't just better simulation. Physics-informed machine learning has raced toward increasingly elaborate integrations of differential equations into neural architectures. DHN suggests a different path: instead of hard-coding the *local* machinery of differential equations step by step, encode the *global* symmetries and conservation laws that give Hamiltonian mechanics its power, then let the neural network fill in the rest.

This matters far beyond toy pendulums. Reconstructing particle trajectories from detector hits, inferring stellar masses from sparse photometric data, modeling molecular dynamics from incomplete observations: these are fundamentally problems of working backward from data, not simulating forward. A framework that handles all of them under one roof, with physical guarantees baked in, is genuinely useful infrastructure for scientific AI.

The connection to diffusion models is worth watching. Borrowing the denoising objective from generative AI and injecting it into a physics-constrained architecture is a creative fusion. It suggests that the toolkit of modern deep learning (transformers, diffusion, learned context encodings) can be grafted onto the formal skeleton of classical mechanics without losing the physics. That's a design pattern with legs.

> **Bottom Line:** DHN shows that physical rigor and generative flexibility aren't mutually exclusive: a single framework that reasons across time, handles diverse tasks, and doesn't need a separate model for every system it studies.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses Hamiltonian mechanics (one of physics' most elegant formalisms) with transformer architectures and denoising diffusion objectives, showing that classical physical structure and modern deep learning are deeply compatible.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">DHN introduces a principled way to extend physics-constrained networks from narrow forward simulation to general physical reasoning, including inference, interpolation, and super-resolution, within a single unified framework.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By encoding global conservation laws rather than local integration steps, DHN opens a path toward AI tools that reason about physical systems the way physicists actually do: through global principles, not step-by-step calculation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include scaling DHN to higher-dimensional real-world systems and deeper integration with observational data pipelines. The paper is available at [arXiv:2503.07596](https://arxiv.org/abs/2503.07596).</span></div></div>
</div>
