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
wordCount: 1249
---

## The Big Picture

Imagine tracking a dust particle suspended in water: a jittering, unpredictable zigzag too jagged for any smooth description. Now imagine that buried inside that erratic motion is the complete mathematical structure of quantum mechanics, with built-in uncertainty, discrete energy levels, and the rule that certain properties can't all be precisely pinned down at the same time. That's the claim at the heart of [new work](https://arxiv.org/abs/2504.05462) from Northeastern University's Christian Ferko and James Halverson. Any quantum mechanical system can be represented as a neural network, and the weirdness of quantum theory emerges directly from the roughness of the network's paths.

Quantum mechanics and neural networks have been converging for years. Researchers have used neural nets to solve quantum equations, accelerate simulations, and approximate quantum states. But Ferko and Halverson flip the question entirely. Instead of asking how AI can help us study quantum systems, they ask: are quantum systems already neural networks? The answer, they prove, is yes, in a mathematically precise sense.

The researchers show that every valid quantum mechanical theory, formulated in imaginary time (a mathematical technique that makes quantum calculations more tractable), can be written as a collection of neural networks with a specific probability distribution over their parameters. This isn't an approximation or a metaphor. It's a theorem.

> **Key Insight:** Any quantum mechanical theory in Euclidean time is mathematically equivalent to a neural network, meaning the entire structure of quantum mechanics, including unitarity and uncertainty, can be encoded in network architectures and parameter distributions.

## How It Works

The bridge runs through **stochastic processes**, mathematical descriptions of randomly evolving quantities like that dust particle's position over time. In Euclidean quantum mechanics, a particle's trajectory through imaginary time looks like a random walk. The authors show this random walk satisfies the conditions for the **Kosambi-Karhunen-Loève (KKL) theorem**, a result from probability theory that decomposes any smoothly-varying random process into a structured sum of simpler building-block components.

That expansion is exactly a neural network. The network's neurons correspond to basis functions in the KKL decomposition, its weights to random coefficients, and the distribution over those weights defines the ensemble. Three conditions seal the deal:

- **Mean-square path continuity**: quantum paths don't jump discontinuously
- **Finite two-point functions**: quantum correlation functions are well-behaved
- **The Kállén-Lehmann spectral representation**: the energy spectrum is non-negative

These properties hold for every legitimate quantum mechanical system. So every quantum system already lives inside a neural network.

![Figure 1](figure:1)

Correlation functions computed in imaginary time must also satisfy **reflection positivity (RP)** to guarantee a valid real-time quantum theory. Reflection positivity is the imaginary-time expression of unitarity, the requirement that probabilities add up to one. How do you ensure a neural network has this property?

Ferko and Halverson identify two mechanisms. A **parameter splitting** method divides the network's parameter space into two halves, one for positive times and one for negative, and constrains their relationship so that reflection positivity is forced into any architecture. A second, more elegant route: **Markov processes** (random walks where only the current state matters) are automatically reflection positive. This second route turns out to be especially productive.

![Figure 2](figure:2)

### Deep Neural Network Quantum Mechanics

Take any Markov process and feed it through a neural network. The output loses the Markov property (the network introduces memory, mixing past and present) but remains reflection positive. You can stack neural networks on top of Markov processes and always stay within the space of valid quantum theories.

This prescription defines **deep neural network quantum mechanics (deep NN-QM)**: constructing vast families of quantum systems by composing neural networks on top of a base quantum process. Each layer transforms the quantum system into a new one while preserving unitarity.

The authors test this framework numerically using the **Ornstein-Uhlenbeck (OU) process**, a particle pulled back toward equilibrium by a restoring force (the random-walk equivalent of a mass on a spring), as their seed. Applying various architectures and computing observables directly from the resulting paths, they confirm:

- **Heisenberg uncertainty**: position-momentum uncertainty saturates the quantum lower bound
- **Non-trivial commutators**: $[x, p] = i\hbar$ arises because paths are *nowhere differentiable*, too rough to have well-defined slopes. This roughness is the mechanism by which non-commutativity enters the theory.
- **Energy spectrum**: reconstructed eigenvalues recover the correct harmonic oscillator spectrum

![Figure 3](figure:3)

Passing the OU process through increasingly complex architectures (deeper networks, different activation functions) produces genuinely different quantum systems. The machinery works.

![Figure 4](figure:4)

## Why It Matters

This result sits at the intersection of two active programs in modern physics: the neural network field theory program, which interprets machine learning through the lens of quantum field theory, and constructive quantum mechanics, which asks what minimal conditions define a valid quantum theory. Ferko and Halverson show these aren't separate projects. They are two faces of the same structure.

The practical payoff runs in both directions. If every quantum system has a neural network representation, the full toolkit of machine learning (optimization algorithms, architecture search, expressivity theory) becomes available for studying quantum systems without ever writing down an action or Lagrangian. Going the other way, insights from quantum theory about which network ensembles are physically meaningful could guide the design of better neural architectures.

Open directions include extending the framework to quantum field theories in higher dimensions, mapping specific architectures to classes of quantum systems, and understanding how training dynamics modify quantum properties.

![Figure 5](figure:5)

![Figure 6](figure:6)

For decades, physicists have used neural networks as tools to probe quantum systems. This paper argues the relationship is more intimate: quantum mechanics and neural networks are, in a precise mathematical sense, the same kind of object.

> **Bottom Line:** Ferko and Halverson prove that every quantum mechanical theory is a neural network, and every deep neural network built on a quantum seed defines a new quantum system, unifying two of the most powerful frameworks in modern science through a theorem about random paths and their roughness.

---

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work proves a mathematical equivalence between quantum mechanics and neural network ensembles, connecting machine learning theory directly to the foundations of quantum physics.

- **Impact on Artificial Intelligence:** Neural network architectures can systematically encode physical constraints like unitarity and reflection positivity, giving a principled route to building physics-respecting AI systems.

- **Impact on Fundamental Interactions:** Deep neural networks define valid quantum systems, offering a new non-Lagrangian route to constructing and classifying quantum mechanical theories without traditional action-based methods.

- **Outlook and References:** Future directions include extending the framework to quantum field theories in higher dimensions and connecting network expressivity to the space of physically realizable quantum systems; see [arXiv:2504.05462](https://arxiv.org/abs/2504.05462).

## Original Paper Details
- **Title:** Quantum Mechanics and Neural Networks
- **arXiv ID:** [2504.05462](https://arxiv.org/abs/2504.05462)
- **Authors:** Christian Ferko, James Halverson
- **Abstract:** We demonstrate that any Euclidean-time quantum mechanical theory may be represented as a neural network, ensured by the Kosambi-Karhunen-Loève theorem, mean-square path continuity, and finite two-point functions. The additional constraint of reflection positivity, which is related to unitarity, may be achieved by a number of mechanisms, such as imposing neural network parameter space splitting or the Markov property. Non-differentiability of the networks is related to the appearance of non-trivial commutators. Neural networks acting on Markov processes are no longer Markov, but still reflection positive, which facilitates the definition of deep neural network quantum systems. We illustrate these principles in several examples using numerical implementations, recovering classic quantum mechanical results such as Heisenberg uncertainty, non-trivial commutators, and the spectrum.
