---
abstract: We demonstrate that any Euclidean-time quantum mechanical theory may be
  represented as a neural network, ensured by the Kosambi-Karhunen-Loève theorem,
  mean-square path continuity, and finite two-point functions. The additional constraint
  of reflection positivity, which is related to unitarity, may be achieved by a number
  of mechanisms, such as imposing neural network parameter space splitting or the
  Markov property. Non-differentiability of the networks is related to the appearance
  of non-trivial commutators. Neural networks acting on Markov processes are no longer
  Markov, but still reflection positive, which facilitates the definition of deep
  neural network quantum systems. We illustrate these principles in several examples
  using numerical implementations, recovering classic quantum mechanical results such
  as Heisenberg uncertainty, non-trivial commutators, and the spectrum.
arxivId: '2504.05462'
arxivUrl: https://arxiv.org/abs/2504.05462
authors:
- Christian Ferko
- James Halverson
concepts:
- reflection positivity
- stochastic processes
- neural network field theory
- spectral methods
- quantum field theory
- deep quantum systems
- quantum states
- physics-informed neural networks
- eigenvalue decomposition
- quantum simulation
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2504_05462/figure_1.png
- /iaifi-research-blog/figures/2504_05462/figure_1.png
- /iaifi-research-blog/figures/2504_05462/figure_2.png
- /iaifi-research-blog/figures/2504_05462/figure_2.png
- /iaifi-research-blog/figures/2504_05462/figure_3.png
- /iaifi-research-blog/figures/2504_05462/figure_3.png
pdfUrl: https://arxiv.org/pdf/2504.05462v1
published: '2025-04-07T19:54:00+00:00'
theme: Theoretical Physics
title: Quantum Mechanics and Neural Networks
wordCount: 1121
---

## The Big Picture

Imagine tracking a dust particle suspended in water — a jittering, unpredictable zigzag too jagged for any smooth description. Now imagine that buried inside that erratic motion is the complete mathematical structure of quantum mechanics: built-in uncertainty, discrete energy levels, and the rule that certain properties can't all be precisely pinned down at the same time. That's the claim at the heart of new work from Northeastern University's Christian Ferko and James Halverson: any quantum mechanical system can be represented as a neural network, and the weirdness of quantum theory emerges directly from the roughness of the network's paths.

Quantum mechanics and neural networks have been converging for years — researchers have used neural nets to solve quantum equations, accelerate simulations, and approximate quantum states. But Ferko and Halverson flip the question entirely. Instead of asking how AI can help us study quantum systems, they ask: are quantum systems already neural networks? The answer, they prove, is yes — in a mathematically precise sense.

The researchers show that every valid quantum mechanical theory, formulated in imaginary time (a mathematical technique that makes quantum calculations more tractable), can be written as a collection of neural networks with a specific probability distribution over their parameters. This isn't an approximation or a metaphor. It's a theorem.

> **Key Insight:** Any quantum mechanical theory in Euclidean time is mathematically equivalent to a neural network — meaning the entire structure of quantum mechanics, including unitarity and uncertainty, can be encoded in network architectures and parameter distributions.

## How It Works

The bridge runs through **stochastic processes** — mathematical descriptions of randomly evolving quantities, like that dust particle's position over time. In Euclidean quantum mechanics, a particle's trajectory through imaginary time looks like a random walk. The authors show this random walk satisfies the conditions for the **Kosambi-Karhunen-Loève (KKL) theorem**, a result from probability theory that decomposes any smoothly-varying random process into a structured sum of simpler building-block components.

That expansion is exactly a neural network. The network's neurons correspond to basis functions in the KKL decomposition, its weights to random coefficients, and the distribution over those weights defines the ensemble. Three conditions seal the deal:

- **Mean-square path continuity**: quantum paths don't jump discontinuously
- **Finite two-point functions**: quantum correlation functions are well-behaved
- **The Kállén-Lehmann spectral representation**: the energy spectrum is non-negative

These properties hold for every legitimate quantum mechanical system. Every quantum system already lives inside a neural network.

![Figure 1](/iaifi-research-blog/figures/2504_05462/figure_1.png)

Correlation functions computed in imaginary time must also satisfy **reflection positivity (RP)** to guarantee a valid real-time quantum theory — imaginary-time language for unitarity, the requirement that probabilities add up to one. How do you ensure a neural network has this property?

Ferko and Halverson identify two mechanisms. A **parameter splitting** method divides the network's parameter space into two halves — one for positive times, one for negative — and constrains their relationship, forcing reflection positivity into any architecture. More elegantly, **Markov processes** (random walks where only the current state matters) are automatically reflection positive. This opens a powerful door.

![Figure 2](/iaifi-research-blog/figures/2504_05462/figure_1.png)

### Deep Neural Network Quantum Mechanics

Take any Markov process and feed it through a neural network. The output loses the Markov property — the network introduces memory, mixing past and present — but remains reflection positive. You can stack neural networks on top of Markov processes and always stay within the space of valid quantum theories.

This prescription defines **deep neural network quantum mechanics (deep NN-QM)**: constructing vast families of quantum systems by composing neural networks on top of a base quantum process. Each layer transforms the quantum system into a new one while preserving unitarity.

The authors test this framework numerically using the **Ornstein-Uhlenbeck (OU) process** — a particle pulled back toward equilibrium by a restoring force, the random-walk equivalent of a mass on a spring — as their seed. Applying various architectures and computing observables directly from the resulting paths, they confirm:

- **Heisenberg uncertainty**: position-momentum uncertainty saturates the quantum lower bound
- **Non-trivial commutators**: $[x, p] = i\hbar$ arises because paths are *nowhere differentiable* — too rough to have well-defined slopes. This roughness is the mechanism by which non-commutativity enters the theory.
- **Energy spectrum**: reconstructed eigenvalues recover the correct harmonic oscillator spectrum

![Figure 3](/iaifi-research-blog/figures/2504_05462/figure_2.png)

Passing the OU process through increasingly complex architectures — deeper networks, different activation functions — produces genuinely different quantum systems. The machinery works.

![Figure 4](/iaifi-research-blog/figures/2504_05462/figure_2.png)

## Why It Matters

This result sits at the intersection of two powerful traditions in modern physics: the neural network field theory program, which interprets machine learning through the lens of quantum field theory, and constructive quantum mechanics, which asks what minimal conditions define a valid quantum theory. Ferko and Halverson show these aren't separate projects — they're two faces of the same structure.

The practical implications cut both ways. If every quantum system has a neural network representation, the full toolkit of machine learning — optimization algorithms, architecture search, expressivity theory — becomes available for studying quantum systems without ever writing down an action or Lagrangian. Conversely, insights from quantum theory about which network ensembles are physically meaningful could guide the design of better neural architectures.

Open directions include extending the framework to quantum field theories in higher dimensions, mapping specific architectures to classes of quantum systems, and understanding how training dynamics modify quantum properties.

![Figure 5](/iaifi-research-blog/figures/2504_05462/figure_3.png)

![Figure 6](/iaifi-research-blog/figures/2504_05462/figure_3.png)

For decades, physicists have used neural networks as tools to probe quantum systems. This paper argues the relationship is more intimate: quantum mechanics and neural networks are, in a precise mathematical sense, the same kind of object.

> **Bottom Line:** Ferko and Halverson prove that every quantum mechanical theory is a neural network, and every deep neural network built on a quantum seed defines a new quantum system — unifying two of the most powerful frameworks in modern science through a theorem about random paths and their roughness.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work establishes a rigorous mathematical equivalence between quantum mechanics and neural network ensembles, forging a direct and provable bridge between machine learning theory and the foundations of quantum physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Neural network architectures can systematically encode physical constraints like unitarity and reflection positivity, providing a principled route to building physics-respecting AI systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Deep neural networks define valid quantum systems, opening a new non-Lagrangian route to constructing and classifying quantum mechanical theories without traditional action-based methods.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending the framework to quantum field theories in higher dimensions and connecting network expressivity to the space of physically realizable quantum systems; the paper is available from Northeastern University's Department of Physics and IAIFI.</span></div></div>
</div>
