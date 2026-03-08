---
abstract: Quantum computing promises to provide machine learning with computational
  advantages. However, noisy intermediate-scale quantum (NISQ) devices pose engineering
  challenges to realizing quantum machine learning (QML) advantages. Recently, a series
  of QML computational models inspired by the noise-tolerant dynamics on the brain
  have emerged as a means to circumvent the hardware limitations of NISQ devices.
  In this article, we introduce a quantum version of a recurrent neural network (RNN),
  a well-known model for neural circuits in the brain. Our quantum RNN (qRNN) makes
  use of the natural Hamiltonian dynamics of an ensemble of interacting spin-1/2 particles
  as a means for computation. In the limit where the Hamiltonian is diagonal, the
  qRNN recovers the dynamics of the classical version. Beyond this limit, we observe
  that the quantum dynamics of the qRNN provide it quantum computational features
  that can aid it in computation. To this end, we study a qRNN based on arrays of
  Rydberg atoms, and show that the qRNN is indeed capable of replicating the learning
  of several cognitive tasks such as multitasking, decision making, and long-term
  memory by taking advantage of several key features of this platform such as interatomic
  species interactions, and quantum many-body scars.
arxivId: '2111.10956'
arxivUrl: https://arxiv.org/abs/2111.10956
authors:
- Rodrigo Araiza Bravo
- Khadijeh Najafi
- Xun Gao
- Susanne F. Yelin
concepts:
- quantum reservoir computing
- recurrent networks
- hamiltonian systems
- rydberg atom arrays
- quantum computing
- many-body quantum scars
- quantum simulation
- entanglement
- stochastic processes
- multi-task learning
- phase transitions
figures:
- /iaifi-research-blog/figures/2111_10956/figure_1.png
- /iaifi-research-blog/figures/2111_10956/figure_1.png
- /iaifi-research-blog/figures/2111_10956/figure_2.png
- /iaifi-research-blog/figures/2111_10956/figure_2.png
- /iaifi-research-blog/figures/2111_10956/figure_3.png
- /iaifi-research-blog/figures/2111_10956/figure_3.png
pdfUrl: https://arxiv.org/pdf/2111.10956v4
published: '2021-11-22T02:45:18+00:00'
theme: Theoretical Physics
title: Quantum reservoir computing using arrays of Rydberg atoms
wordCount: 1172
---

## The Big Picture

Imagine trying to teach a noisy, imperfect orchestra to play a symphony perfectly. You can't force every musician to hit every note. The instruments drift out of tune, the timing falters, the hall reverberates unpredictably. But what if, instead of fighting the noise, you *composed for it*? What if the music you wanted emerged naturally from the chaos?

That's the central gamble behind quantum reservoir computing, and researchers at Harvard are now winning it with atoms.

Quantum computers could accelerate machine learning in ways we're only beginning to understand. But today's machines, the so-called **NISQ devices** (Noisy Intermediate-Scale Quantum), are messy. They're small, error-prone, and fragile: quantum bits lose their delicate state almost instantly, a problem called **decoherence**. Attempts to train these machines can hit dead ends called "barren plateaus," where the learning signal vanishes entirely.

Rodrigo Araiza Bravo and colleagues at Harvard have proposed a way through this impasse: build your quantum computer to think like a brain.

> **Key Insight:** By mapping a recurrent neural network onto the natural quantum dynamics of Rydberg atoms, the researchers created a quantum reservoir computer that learns cognitive tasks (multitasking, decision-making, long-term memory) without complex circuit training.

## How It Works

The core idea borrows from neuroscience. **Recurrent neural networks (RNNs)** feed signals back through themselves over time, making them powerful for sequential tasks like language or time-series prediction. The researchers define a **quantum RNN (qRNN)** by replacing classical binary neurons with quantum two-level systems, i.e. **qubits**.

Instead of hand-coded synaptic weights, connections between qubits are determined by the natural physics of the quantum system: its **Hamiltonian dynamics**, the built-in rules governing how energy flows through the system. The network's wiring isn't programmed by engineers. It's dictated by physics.

![Figure 1](/iaifi-research-blog/figures/2111_10956/figure_1.png)

This is the reservoir computing trick: instead of training the internal dynamics (which is hard and error-prone), you fix the quantum system's interactions and train only a simple linear readout layer. The richness of the quantum dynamics does the heavy lifting.

The platform of choice is **Rydberg atom arrays**, grids of neutral atoms trapped by tightly focused laser beams (optical tweezers) and excited to high-energy "Rydberg" states, where they interact strongly over surprisingly long distances. The platform is scalable, controllable, and offers coherence times that rival any quantum hardware available today.

What makes the Rydberg reservoir special:

- **Interspecies interactions**: Atoms excited to different energy levels (described by different principal quantum numbers) carry distinct interaction profiles. This naturally encodes *inhibitory* and *excitatory* connections, the same mix neuroscientists know is essential for cognitive flexibility and multitasking.
- **Quantum many-body scars**: Certain quantum states in Rydberg arrays resist the normal expectation that quantum systems rapidly scramble information. These non-thermalizing states persist over long timescales, acting as a built-in long-term memory written into the physics itself.

![Figure 2](/iaifi-research-blog/figures/2111_10956/figure_1.png)

The team numerically tested Rydberg reservoir computers on three cognitive benchmarks drawn from neuroscience: multitasking, decision-making, and long-term memory. With only a handful of atoms, the qRNN succeeded on all three.

![Figure 3](/iaifi-research-blog/figures/2111_10956/figure_2.png)

The researchers also show a theoretical advantage for simulating **stochastic dynamics**, random processes like a noisy signal or a molecule's random walk. A classical RNN must sample many trajectories to approximate a probability distribution. A qRNN, evolving through a superposition of all possible configurations simultaneously, accesses the full distribution directly. That speedup is rooted in quantum mechanics itself.

## Why It Matters

On one level, this work offers a practical path through the NISQ bottleneck. The reservoir computing framework sidesteps the training instabilities that plague **variational quantum circuits**, a common quantum ML approach in which circuit parameters are iteratively adjusted like tuning knobs. Because the quantum dynamics are fixed and only the output layer is trained classically, the system is inherently noise-tolerant. Much as the brain processes information reliably even when individual neurons misfire, the reservoir's collective dynamics smooth over errors.

![Figure 4](/iaifi-research-blog/figures/2111_10956/figure_2.png)

On another level, the paper clarifies *why* quantum hardware helps, not just *that* it does. The performance gains trace back to identifiable physical mechanisms: multitasking arises from interspecies Rydberg interactions; long-term memory arises from quantum many-body scars. That kind of mechanistic clarity can guide engineers building better quantum ML hardware, rather than hoping quantum systems help by accident.

The bigger question running beneath all of this: what does quantum mechanics actually buy you computationally, and how do you harness it in messy real-world devices? This paper carves out a concrete, experimentally accessible piece of that answer. And it suggests the path forward runs through physics, not around it.

> **Bottom Line:** Arrays of Rydberg atoms, wired by quantum physics rather than silicon, can learn the same cognitive tasks that challenge classical neural networks. Quantum many-body effects like scars and interspecies interactions aren't bugs in this system; they're features.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects quantum many-body physics and machine learning by showing how phenomena unique to Rydberg atom arrays (quantum many-body scars and interspecies interactions) directly enable cognitive computational capabilities, turning physics into AI architecture.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The quantum reservoir computing framework offers a noise-tolerant alternative to variational quantum circuits, providing a practical route to quantum-enhanced machine learning on near-term hardware without the training instabilities that plague current quantum ML approaches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The research shows that quantum many-body scars, exotic non-thermalizing quantum states, have a concrete computational function as a mechanism for long-term memory, giving these physically unusual states a new practical interpretation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include scaling to larger Rydberg arrays, exploring quantum tasks beyond classical cognitive benchmarks, and identifying further physical mechanisms that confer computational advantages; the full paper is available at [arXiv:2111.10956](https://arxiv.org/abs/2111.10956).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Quantum reservoir computing using arrays of Rydberg atoms</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2111.10956</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Rodrigo Araiza Bravo", "Khadijeh Najafi", "Xun Gao", "Susanne F. Yelin"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Quantum computing promises to provide machine learning with computational advantages. However, noisy intermediate-scale quantum (NISQ) devices pose engineering challenges to realizing quantum machine learning (QML) advantages. Recently, a series of QML computational models inspired by the noise-tolerant dynamics on the brain have emerged as a means to circumvent the hardware limitations of NISQ devices. In this article, we introduce a quantum version of a recurrent neural network (RNN), a well-known model for neural circuits in the brain. Our quantum RNN (qRNN) makes use of the natural Hamiltonian dynamics of an ensemble of interacting spin-1/2 particles as a means for computation. In the limit where the Hamiltonian is diagonal, the qRNN recovers the dynamics of the classical version. Beyond this limit, we observe that the quantum dynamics of the qRNN provide it quantum computational features that can aid it in computation. To this end, we study a qRNN based on arrays of Rydberg atoms, and show that the qRNN is indeed capable of replicating the learning of several cognitive tasks such as multitasking, decision making, and long-term memory by taking advantage of several key features of this platform such as interatomic species interactions, and quantum many-body scars.</span></div></div>
</div>
