---
abstract: 'It has been an open question in deep learning if fault-tolerant computation
  is possible: can arbitrarily reliable computation be achieved using only unreliable
  neurons? In the grid cells of the mammalian cortex, analog error correction codes
  have been observed to protect states against neural spiking noise, but their role
  in information processing is unclear. Here, we use these biological error correction
  codes to develop a universal fault-tolerant neural network that achieves reliable
  computation if the faultiness of each neuron lies below a sharp threshold; remarkably,
  we find that noisy biological neurons fall below this threshold. The discovery of
  a phase transition from faulty to fault-tolerant neural computation suggests a mechanism
  for reliable computation in the cortex and opens a path towards understanding noisy
  analog systems relevant to artificial intelligence and neuromorphic computing.'
arxivId: '2202.12887'
arxivUrl: https://arxiv.org/abs/2202.12887
authors:
- Alexander Zlokapa
- Andrew K. Tan
- John M. Martyn
- Ila R. Fiete
- Max Tegmark
- Isaac L. Chuang
concepts:
- robustness
- fault-tolerant neural computation
- phase transitions
- grid code error correction
- analog fault tolerance
- quantum computing
- stochastic processes
- uncertainty quantification
- ensemble methods
- scalability
figures:
- /iaifi-research-blog/figures/2202_12887/figure_1.png
- /iaifi-research-blog/figures/2202_12887/figure_1.png
- /iaifi-research-blog/figures/2202_12887/figure_2.png
- /iaifi-research-blog/figures/2202_12887/figure_2.png
- /iaifi-research-blog/figures/2202_12887/figure_3.png
- /iaifi-research-blog/figures/2202_12887/figure_3.png
pdfUrl: https://arxiv.org/pdf/2202.12887v3
published: '2022-02-25T18:55:46+00:00'
theme: Foundational AI
title: Fault-Tolerant Neural Networks from Biological Error Correction Codes
wordCount: 1028
---

## The Big Picture

Imagine trying to build a reliable calculator from components that randomly malfunction. Every switch occasionally flips the wrong way, every wire sometimes drops its signal. It sounds impossible. For a long time, it was an open question whether it even *could* be done.

The answer turned out to be yes: with clever redundancy and error correction, you can build trustworthy machines from untrustworthy parts. That insight is behind every computer and smartphone on the planet.

Now ask the same question about the brain. Neurons are noisy. They fire at the wrong time, drop signals, and add random static to every message they send. Yet the brain performs reliable calculations. How? And can we steal that trick for artificial intelligence?

A team of researchers from MIT and IAIFI has done exactly that. By borrowing an error correction strategy discovered in grid cells (neurons in mammals that encode spatial location) they have proven, for the first time, that neural networks can achieve **universal fault-tolerant computation**: arbitrarily accurate results, even when every single neuron is noisy.

> **Key Insight:** Biological error correction codes found in the brain's grid cells don't just protect memories. They can protect *computations*, enabling reliable neural networks from unreliable components, provided noise stays below a sharp threshold.

## How It Works

The story starts with a result from the dawn of computer science. In 1956, John von Neumann showed that you could build a reliable logical circuit from faulty gates, as long as each gate's failure probability *p* stays below some threshold *p₀*. His trick was the **repetition code**: copy your data three times, run majority voting, and even if one vote is wrong, the other two win. Apply this repeatedly, and errors stay bounded no matter how long the computation runs.

![Figure 1](figure:1)

That works for digital errors, where a gate either fails or it doesn't. But neurons don't fail digitally. They suffer from two messier problems:

- **Synaptic failure**: a connection randomly drops out, sending zero instead of a signal. This is a discrete, on/off error.
- **Analog noise**: a neuron's output is corrupted by continuous Gaussian noise with standard deviation σ. Majority voting can't fix a continuous smear of randomness.

The first problem yields to an extension of von Neumann's repetition code. The second is where biology steps in.

In the entorhinal cortex, **grid cells** fire in hexagonal patterns as an animal navigates space. These cells encode position using a **grid code**, an analog error correction scheme that represents a continuous value as a combination of signals at multiple scales, like nested ruler ticks. This encoding is hard to corrupt: small perturbations to any individual cell barely shift the decoded value, because the information is spread across many cells at many resolutions.

The team adapted this biological code for computation. Instead of storing a continuous value in a single noisy neuron, it's encoded across a population using the grid code. When noise perturbs some neurons, the decoder reconstructs the original value from redundant information at multiple scales. The computations themselves, including the nonlinear operations that make neural networks powerful, are also performed *within* the encoded representation, using faulty neurons throughout.

![Figure 2](figure:2)

The formal result is what the authors call **Neural Network Fault-Tolerance**: any Boolean formula of *N* gates can be simulated by a faulty neural network using only *O*(*N* polylog(*N/ε*)) neurons to achieve error probability at most *ε*. The thresholds *p₀* for synaptic failure and *σ₀* for analog noise are both nonzero, so fault-tolerance is genuinely achievable, not just an unreachable theoretical limit.

When the researchers estimated where real biological neurons fall on this map, noisy neurons in the brain land *below* the fault-tolerance threshold.

![Figure 4](figure:4)

Biology has, apparently, already solved this problem.

## Why It Matters

This result sits at the intersection of three fields that rarely talk to each other: theoretical computer science, neuroscience, and machine learning. The fault-tolerance threshold behaves like a **phase transition**, the kind familiar from physics, where systems abruptly shift behavior at a critical parameter. Water turns to ice at exactly 0°C; neural computation flips from unreliable to reliable at a critical noise level. That kind of clean, universal behavior is exactly what physicists love to find in unexpected places.

Consider **neuromorphic chips**, hardware designed to mimic neural architecture for energy-efficient AI. These chips have long struggled with component failures and manufacturing variability. This work gives them a theoretical foundation: there exists a regime where noise doesn't matter, and the grid code shows how to reach it. For deep learning more broadly, robustness to weight noise and hardware imprecision becomes tractable once you have a formal framework for what fault-tolerance means in the analog setting.

The paper also reframes a longstanding puzzle in neuroscience. Grid cells have been celebrated for spatial navigation, but their error-correcting properties seemed almost incidental. Maybe those properties are *the point*, or at least they serve a dual function. Reliable computation in the brain may depend on grid-code-like representations not just for storing location, but for executing computations on noisy hardware.

> **Bottom Line:** Neurons are noisy, but noise doesn't have to mean unreliability. The brain figured this out first. This paper proves that fault-tolerant neural computation is possible using the same error correction codes found in mammalian grid cells, connecting biological neural architecture to the theoretical foundations of reliable computation.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects theoretical computer science, neuroscience, and machine learning by proving that biologically-inspired analog error correction codes enable universal fault-tolerant neural networks.

- **Impact on Artificial Intelligence:** The paper provides the first formal proof that analog neural networks can achieve fault-tolerant computation below a sharp noise threshold, opening a theoretical path for noise-resilient neuromorphic hardware and AI systems.

- **Impact on Fundamental Interactions:** The discovery of a phase transition between faulty and fault-tolerant neural computation introduces physics-style critical phenomena into neural computation theory, with universal behavior analogous to phase transitions in physical systems.

- **Outlook and References:** Future work can explore whether other biological neural codes exhibit similar fault-tolerance properties, and whether the grid-code construction can be practically implemented in neuromorphic chips; the paper is available at [arXiv:2202.12887](https://arxiv.org/abs/2202.12887).
