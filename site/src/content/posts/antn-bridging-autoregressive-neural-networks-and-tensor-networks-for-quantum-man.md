---
abstract: Quantum many-body physics simulation has important impacts on understanding
  fundamental science and has applications to quantum materials design and quantum
  technology. However, due to the exponentially growing size of the Hilbert space
  with respect to the particle number, a direct simulation is intractable. While representing
  quantum states with tensor networks and neural networks are the two state-of-the-art
  methods for approximate simulations, each has its own limitations in terms of expressivity
  and inductive bias. To address these challenges, we develop a novel architecture,
  Autoregressive Neural TensorNet (ANTN), which bridges tensor networks and autoregressive
  neural networks. We show that Autoregressive Neural TensorNet parameterizes normalized
  wavefunctions, allows for exact sampling, generalizes the expressivity of tensor
  networks and autoregressive neural networks, and inherits a variety of symmetries
  from autoregressive neural networks. We demonstrate our approach on quantum state
  learning as well as finding the ground state of the challenging 2D $J_1$-$J_2$ Heisenberg
  model with different systems sizes and coupling parameters, outperforming both tensor
  networks and autoregressive neural networks. Our work opens up new opportunities
  for quantum many-body physics simulation, quantum technology design, and generative
  modeling in artificial intelligence.
arxivId: '2304.01996'
arxivUrl: https://arxiv.org/abs/2304.01996
authors:
- Zhuo Chen
- Laker Newhouse
- Eddie Chen
- Di Luo
- Marin Soljačić
concepts:
- tensor networks
- quantum simulation
- autoregressive wavefunction
- quantum states
- neural network quantum states
- monte carlo methods
- variational ansatz
- entanglement
- generative models
- symmetry preservation
- density estimation
- recurrent networks
figures:
- /iaifi-research-blog/figures/2304_01996/figure_1.png
- /iaifi-research-blog/figures/2304_01996/figure_2.png
pdfUrl: https://arxiv.org/pdf/2304.01996v3
published: '2023-04-04T17:54:14+00:00'
theme: Theoretical Physics
title: 'ANTN: Bridging Autoregressive Neural Networks and Tensor Networks for Quantum
  Many-Body Simulation'
wordCount: 1202
---

## The Big Picture

Imagine describing the state of a single coin: heads or tails, easy enough. Now imagine 300 coins simultaneously, every one quantum-entangled with every other. The number of possible configurations isn't just large; it's 2³⁰⁰, a number exceeding the count of atoms in the observable universe. This is the fundamental difficulty of quantum many-body physics, and the reason simulating even modest quantum systems remains one of science's hardest problems.

Physicists have two powerful but imperfect weapons. **Tensor networks** exploit the fact that nearby particles correlate more strongly than distant ones, compressing an otherwise unmanageable description into something tractable. But they struggle in two or more dimensions, where correlations grow too complex to tame. **Neural network quantum states** bring raw representational power, but lack built-in physical intuition and run into stubborn difficulties managing the canceling positive and negative contributions that make quantum calculations especially tricky.

A team from MIT and Harvard's IAIFI has fused both approaches into a single architecture, the **Autoregressive Neural TensorNet (ANTN)**, that inherits the strengths of each while sidestepping their individual limitations.

> **Key Insight:** ANTN doesn't just combine two methods. It mathematically *generalizes* both. Any quantum state that either approach can represent, ANTN can represent too, and then some.

## How It Works

The central challenge in quantum simulation is representing a **wavefunction** (the complete mathematical description of a quantum system's state) in a form a computer can handle. A wavefunction assigns a complex number to every possible spin configuration of every particle. For 50 spins, that's over a quadrillion numbers. You need a smarter way.

![Figure 1](/iaifi-research-blog/figures/2304_01996/figure_1.png)

Tensor networks attack this by factoring the wavefunction into a network of smaller tensors, which are multi-dimensional tables of numbers, each capturing local correlations between neighboring particles. The most familiar variant, the **matrix product state (MPS)**, arranges these tables in a chain and works beautifully for one-dimensional systems. In 2D, which is more relevant to real materials, the correlations become too rich, and tensor networks hit a representational ceiling.

**Autoregressive neural networks (ARNNs)** take a different angle. They decompose the probability of observing a spin configuration using the **chain rule of probability**: the probability of the full sequence equals the probability of the first spin, times the probability of the second given the first, and so on. This guarantees exact, unbiased sampling, which is a major practical advantage. But ARNNs don't naturally encode the spatial structure physicists know should matter.

ANTN weaves these ideas together in a mathematically principled way. The core trick: treat the tensors not as fixed arrays, but as outputs of neural networks that observe the chain of previous spins. The **elementwise** variant multiplies the neural network output into each tensor element; the **blockwise** variant generates entire tensor blocks at each step.

The result is a hybrid that:

- Produces normalized wavefunctions automatically, without expensive normalization corrections
- Enables exact sampling from the learned distribution, critical for efficient variational optimization
- Inherits symmetries (spin-flip, translational invariance) from the ARNN component
- Strictly generalizes both parent architectures: fix the neural network contribution and you recover a tensor network; collapse the tensor structure and you recover an ARNN

## Why It Matters

The team tested ANTN on two benchmarks. First, **quantum state learning**: given measurement samples from a known quantum state, can ANTN reconstruct it faithfully? ANTN achieved higher quantum fidelity, a measure of overlap between the learned and true states, than either tensor networks or ARNNs alone.

![Figure 2](/iaifi-research-blog/figures/2304_01996/figure_2.png)

The harder test came from the **2D J₁-J₂ Heisenberg model**, a notorious benchmark in condensed matter physics. This model describes spins on a square lattice with two competing interactions: nearest-neighbor coupling J₁ and next-nearest-neighbor coupling J₂. When J₂ is large relative to J₁, the interactions frustrate each other (they can't both be satisfied simultaneously), creating a disordered **quantum spin liquid** phase that's exceptionally hard to simulate. Near J₂/J₁ ≈ 0.5 is where most methods falter.

Across multiple system sizes and coupling parameters, ANTN consistently found lower ground state energies than either baseline, with the advantage most pronounced in exactly the frustrated regime. The two variants offered a practical tradeoff: blockwise ANTN achieved better accuracy; elementwise ANTN was computationally cheaper.


The immediate payoff is a better trial wavefunction for quantum simulation, useful for studying exotic phases of matter, designing new quantum materials, and benchmarking quantum computers. The frustrated 2D Heisenberg model isn't just an academic exercise; its physics connects directly to high-temperature superconductors, topological materials, and quantum spin liquids that physicists hope to harness for quantum computing.

Beyond the numerical results, ANTN says something about the relationship between physics and machine learning. The architecture doesn't just borrow tricks from each field. It exposes the fact that tensor networks and autoregressive models share a common mathematical structure, with ANTN occupying a richer space above both. That structural insight could inform new architectures in generative modeling, sequence modeling, and any domain where hierarchical decomposition of probability distributions matters.

> **Bottom Line:** By constructing a rigorous bridge between tensor networks and autoregressive neural networks, ANTN achieves state-of-the-art results on one of quantum physics' hardest benchmarks, and suggests the boundary between physics-inspired computation and modern AI is blurrier than anyone thought.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">ANTN fuses tensor networks from quantum physics with autoregressive models from machine learning into a single unified architecture with provable mathematical properties bridging both fields.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Physics-inspired inductive biases can systematically improve generative model expressivity, with potential applications to sequence modeling and probabilistic inference beyond quantum systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">ANTN achieves lower ground state energies than existing methods on the frustrated 2D J₁-J₂ Heisenberg model, advancing simulation of quantum materials relevant to superconductivity and topological phases.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending ANTN to fermionic systems, continuous-variable quantum fields, and quantum chemistry; see [arXiv:2304.01996](https://arxiv.org/abs/2304.01996) for the full paper and theoretical proofs.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">ANTN: Bridging Autoregressive Neural Networks and Tensor Networks for Quantum Many-Body Simulation</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2304.01996</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Zhuo Chen", "Laker Newhouse", "Eddie Chen", "Di Luo", "Marin Soljačić"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Quantum many-body physics simulation has important impacts on understanding fundamental science and has applications to quantum materials design and quantum technology. However, due to the exponentially growing size of the Hilbert space with respect to the particle number, a direct simulation is intractable. While representing quantum states with tensor networks and neural networks are the two state-of-the-art methods for approximate simulations, each has its own limitations in terms of expressivity and inductive bias. To address these challenges, we develop a novel architecture, Autoregressive Neural TensorNet (ANTN), which bridges tensor networks and autoregressive neural networks. We show that Autoregressive Neural TensorNet parameterizes normalized wavefunctions, allows for exact sampling, generalizes the expressivity of tensor networks and autoregressive neural networks, and inherits a variety of symmetries from autoregressive neural networks. We demonstrate our approach on quantum state learning as well as finding the ground state of the challenging 2D $J_1$-$J_2$ Heisenberg model with different systems sizes and coupling parameters, outperforming both tensor networks and autoregressive neural networks. Our work opens up new opportunities for quantum many-body physics simulation, quantum technology design, and generative modeling in artificial intelligence.</span></div></div>
</div>
