---
abstract: In this paper, we present a general framework for quantum many-body simulations
  called the operator learning renormalization group (OLRG). Inspired by machine learning
  perspectives, OLRG is a generalization of Wilson's numerical renormalization group
  and White's density matrix renormalization group, which recursively builds a simulatable
  system to approximate a target system of the same number of sites via operator maps.
  OLRG uses a loss function to minimize the error of a target property directly by
  learning the operator map in lieu of a state ansatz. This loss function is designed
  by a scaling consistency condition that also provides a provable bound for real-time
  evolution. We implement two versions of the operator maps for classical and quantum
  simulations. The former, which we call the Operator Matrix Map, can be implemented
  via neural networks on classical computers. The latter, which we call the Hamiltonian
  Expression Map, generates device pulse sequences to leverage the capabilities of
  quantum computing hardware. We illustrate the performance of both maps for calculating
  time-dependent quantities in the quantum Ising model Hamiltonian.
arxivId: '2403.03199'
arxivUrl: https://arxiv.org/abs/2403.03199
authors:
- Xiu-Zhe Luo
- Di Luo
- Roger G. Melko
concepts:
- renormalization
- operator map learning
- quantum simulation
- scaling consistency condition
- loss function design
- tensor networks
- quantum computing
- neural operators
- hamiltonian expression map
- physics-informed neural networks
- phase transitions
figures:
- /iaifi-research-blog/figures/2403_03199/figure_1.png
- /iaifi-research-blog/figures/2403_03199/figure_2.png
- /iaifi-research-blog/figures/2403_03199/figure_3.png
pdfUrl: https://arxiv.org/pdf/2403.03199v2
published: '2024-03-05T18:37:37+00:00'
theme: Theoretical Physics
title: Operator Learning Renormalization Group
wordCount: 1080
---

## The Big Picture

Imagine you're trying to understand how an ocean behaves, but you can only afford a fish tank. You'd need some clever trick to connect what you can simulate to what you actually want to know. Quantum physicists face exactly this problem, scaled to the extreme.

Quantum systems of even a few dozen interacting particles are impossible to simulate on ordinary computers. The information required grows exponentially with system size. The universe doesn't care about your memory limits.

For decades, physicists have fought back with **renormalization group** (RG) methods, techniques that let you zoom in or out on a system, keeping only the most important features at each scale. Think of it as deliberately blurring a photograph in a controlled way: you lose fine detail but preserve large-scale structure. Wilson's Numerical Renormalization Group and White's Density Matrix Renormalization Group (DMRG) stand as two of the great algorithmic achievements of 20th-century physics.

But these methods rely on a simplification: they represent quantum states using fixed linear transformations. Elegant and manageable, yes, but limiting for high-dimensional systems and real-time dynamics.

Now, a team from MIT, Harvard's IAIFI, and the Perimeter Institute has asked: what if you replaced that rigid assumption with machine learning? Their answer is the **Operator Learning Renormalization Group** (OLRG), a framework that lets an algorithm learn *how to transform operators* from smaller to larger systems, rather than relying on a fixed mathematical template.

> **Key Insight:** OLRG reframes quantum simulation as a machine learning problem, directly learning operator maps that minimize error in your target physical property rather than approximating quantum states through linear algebra.

## How It Works

Classical RG methods work by a recursive trick: take a small system, compress it into a compact representation, attach another piece, compress again, and repeat until you've built up to the scale you care about. The compression step is where physics lives. You decide what to keep and what to discard.

In NRG and DMRG, that compression is a linear transformation, a rotation into a low-energy subspace represented by a matrix. OLRG replaces this fixed linear map with an arbitrary **operator map**: any function that takes a small system's physical descriptions and outputs a compact representation useful for simulating a larger one. Neural networks are the natural candidate.

![Figure 1](/iaifi-research-blog/figures/2403_03199/figure_1.png)

The core algorithmic loop:

1. Start with a simulatable *n*-site system and its operators.
2. Apply the operator map to compress those operators into a virtual representation.
3. Grow the system by one site and feed the compressed operators forward.
4. Repeat recursively until you reach the target system size.
5. Compute the observable of interest and measure error against the true value.

What guides the learning? Instead of minimizing spectral error (a mismatch in the system's energy levels), OLRG defines a loss function tied directly to the **target property**: the actual physical quantity you want to predict, whether magnetization, correlation functions, or time evolution. This end-to-end approach, borrowed from deep learning, removes intermediate approximation steps that can bias results.

The team also proves a rigorous theoretical result: a **scaling consistency condition** for systems where particles only interact with their immediate neighbors (technically, *geometrically local Hamiltonians*) under real-time evolution. A Hamiltonian is the equation governing how a quantum system evolves, the full rulebook for its physics. The condition provides a provable error bound: the simulated system's time evolution approximates the target system's evolution with controlled accuracy. Not empirical hand-waving, but a mathematical guarantee.

The researchers implement two concrete versions of the operator map. The **Operator Matrix Map** (OMM) represents operators as matrices and learns compression using a neural network on classical hardware. The **Hamiltonian Expression Map** (HEM) goes further: instead of representing operators as matrices, it maps the problem Hamiltonian directly to a *device Hamiltonian*, generating pulse sequences that run on real quantum hardware. This makes OLRG a natural fit for near-term quantum devices that aren't yet fully fault-tolerant.

![Figure 2](/iaifi-research-blog/figures/2403_03199/figure_2.png)

Both approaches are tested on the **Transverse Field Ising Model** (TFIM), a standard test problem describing spins on a chain interacting with a transverse magnetic field. The team focuses on two-point correlation functions under real-time dynamics, a notoriously difficult quantity to compute. DMRG struggles here because **entanglement** (quantum correlations linking distant particles) grows rapidly over time, outpacing what linear methods can track. Both OMM and HEM recover accurate time-dependent correlations, with the neural-network OMM providing faithful classical simulation and HEM pointing toward quantum hardware acceleration.

![Figure 3](/iaifi-research-blog/figures/2403_03199/figure_3.png)

## Why It Matters

DMRG's limitations have long been known: it excels at one-dimensional ground states but falters for real-time dynamics and higher-dimensional systems. The reason is its reliance on Matrix Product States (MPS), a representation built from chains of matrices that can't efficiently capture the entanglement building up as a quantum system evolves.

OLRG doesn't claim to have solved quantum simulation (that's a provably hard problem). But it opens a new design space. By decoupling the structure of the approximation from linear algebra, it makes room for richer representations tuned to the actual problem at hand.

The dual-track design is worth watching. As quantum devices improve, algorithms that translate naturally between classical and quantum representations will be essential for hybrid workflows. HEM is a concrete step in that direction, generating physically meaningful pulse sequences rather than abstract quantum circuits.

There's also an echo of broader ideas from machine learning: optimizing directly for what you want, rather than a proxy, tends to yield better results. That principle applies just as well in physics as it does in language modeling.

> **Bottom Line:** OLRG is a principled fusion of renormalization group theory and machine learning that unlocks richer operator representations for quantum simulation, with provable bounds on real-time dynamics and a direct path to quantum hardware implementation.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects modern machine learning (end-to-end optimization and neural network function approximation) with one of the foundational computational frameworks of condensed matter physics, the renormalization group.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">OLRG shows that learning task-specific representations end-to-end can replace hand-crafted linear ansatzes in physics simulations, opening a new class of physics-inspired learning algorithms.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By providing provable error bounds for real-time quantum evolution and implementing operator maps on quantum hardware, OLRG advances the practical simulation of quantum many-body systems beyond what standard DMRG can achieve.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending OLRG to higher-dimensional systems, ground-state problems, and larger quantum hardware; the work is available at [arXiv:2403.03199](https://arxiv.org/abs/2403.03199).</span></div></div>
</div>
