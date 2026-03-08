---
abstract: An approach to field theory is studied in which fields are comprised of
  $N$ constituent random neurons. Gaussian theories arise in the infinite-$N$ limit
  when neurons are independently distributed, via the Central Limit Theorem, while
  interactions arise due to finite-$N$ effects or non-independently distributed neurons.
  Euclidean-invariant ensembles of neurons are engineered, with tunable two-point
  function, yielding families of Euclidean-invariant field theories. Some Gaussian,
  Euclidean invariant theories are reflection positive, which allows for analytic
  continuation to a Lorentz-invariant quantum field theory. Examples are presented
  that yield dual theories at infinite-$N$, but have different symmetries at finite-$N$.
  Landscapes of classical field configurations are determined by local maxima of parameter
  distributions. Predictions arise from mixed field-neuron correlators. Near-Gaussianity
  is exhibited at large-$N$, potentially explaining a feature of field theories in
  Nature.
arxivId: '2112.04527'
arxivUrl: https://arxiv.org/abs/2112.04527
authors:
- James Halverson
concepts:
- quantum field theory
- neural network qft
- reflection positivity
- stochastic processes
- large-n duality
- symmetry breaking
- group theory
- kernel methods
- renormalization
- effective field theory
- conformal field theory
- monte carlo methods
figures: []
pdfUrl: https://arxiv.org/pdf/2112.04527v1
published: '2021-12-08T19:05:36+00:00'
theme: Theoretical Physics
title: Building Quantum Field Theories Out of Neurons
wordCount: 1161
---

## The Big Picture

What if the universe is, in some deep sense, a neural network? That sounds like science fiction, but physicist James Halverson at Northeastern University has taken the question seriously and built a mathematical framework that puts quantum field theory and machine learning on the same footing. Not metaphorically. Literally.

**Quantum field theory (QFT)** is the language of modern physics. It describes electrons, photons, quarks, and the Higgs boson, every fundamental particle and force we've ever measured. Traditionally, physicists write down a **Lagrangian**, a recipe encoding how particles move and interact, and derive all physics from there. Choosing the right recipe feels like an art. Halverson asks: what if you could skip the recipe entirely and build a quantum field out of neurons instead?

The result is a construction called **neural network quantum field theory (NN-QFT)**. In the usual approach, quantum randomness comes from summing over all possible field configurations. In Halverson's version, randomness comes from the statistical properties of the neurons themselves. The construction can satisfy all the mathematical requirements of a QFT that respects the symmetries of special relativity.

> **Key Insight:** By building fields out of random neurons, the Central Limit Theorem does the work that Lagrangians usually do. Free theories emerge automatically at large N, while interactions arise from finite-N corrections and neuron correlations.

## How It Works

Start with a **scalar field** φ, which assigns a real number to every point in space. In Halverson's construction, this field is a sum of N random neurons:

φ(x) = a₁h₁(x) + a₂h₂(x) + ... + aₙhₙ(x)

Each neuron hᵢ is a randomly initialized function. The coefficients aᵢ are drawn from a distribution with variance σ²/N. No Lagrangian appears anywhere.

What happens next depends on two limits. When N → ∞ and neurons are independently distributed, the **Central Limit Theorem** kicks in. Just as averaging millions of coin flips produces a bell curve, summing millions of independent random neurons produces a **Gaussian theory**: the field-theory equivalent of a free particle. This mirrors a well-known result in machine learning called the **Neural Network Gaussian Process (NNGP) correspondence**, where infinitely wide neural networks behave like Gaussian processes.

Interactions enter in two ways:

- **Finite-N corrections**: at large but finite N, the CLT isn't exact, and the 4-point connected correlation function picks up contributions of order 1/N
- **Independence breaking**: if neurons are correlated with each other, interactions appear even at infinite N through a term called I⁽⁴⁾_IB

The CLT assumes independence. Break that assumption, and you get non-trivial physics.

Going from a Euclidean field theory to a genuine QFT requires satisfying the **Osterwalder-Schrader (OS) axioms**. These are mathematical conditions guaranteeing the theory can be analytically continued into real spacetime, with a well-defined Hilbert space and no ghost states that would break unitarity. The hardest condition to satisfy is **reflection positivity**: correlation functions must behave correctly under time reflection. For Gaussian NN-QFTs, Halverson shows this reduces to a constraint on the power spectrum G⁽²⁾(p), and he constructs explicit neuron architectures that satisfy it. These are the first concrete NN-QFTs.

The paper also turns up a result about **duality**. Different neuron architectures, with different internal symmetries and parameter distributions, can produce identical theories at N → ∞ but diverge at finite N. Think of it as the neural analog of known dualities in physics: two models that look identical from far away reveal their differences under a microscope.

Without an action to minimize, classical field configurations take on a new meaning. Classical solutions correspond to local maxima of the parameter distribution P(θ). The landscape of classical physics becomes the landscape of likely neuron parameters.

Predictions in NN-QFT come from **mixed field-neuron correlators**, quantities that involve both the output field φ and the constituent neurons hᵢ. Ordinary QFT has no "constituent" degrees of freedom to probe. Here, the internal structure of the field is directly accessible, connecting the macroscopic field to its microscopic building blocks.

## Why It Matters

For physics, NN-QFT offers a non-Lagrangian route into quantum field theory. That matters in regimes where writing down an action is hard: strongly coupled theories, exotic geometries, situations where the standard toolkit breaks down.

The near-Gaussianity of real-world quantum fields has always seemed like a coincidence. Most QFTs in nature are weakly coupled and nearly free. In the NN-QFT framework, there's a natural explanation: large-N suppression of non-Gaussian terms is baked into the architecture, just as it is in real neural networks.

For machine learning theory, the payoff runs deeper than analogy. There's a growing research program that imports QFT tools (Feynman diagrams, renormalization group flows) to understand how networks learn. Halverson's paper inverts that program: instead of applying QFT to neural networks, it uses neural networks to *build* QFTs. The two directions together point toward a tighter mathematical relationship between learning systems and physical theories than anyone had previously shown.

> **Bottom Line:** Neural networks can construct quantum field theories from scratch, no Lagrangian required. Gaussian theories emerge naturally at large N, and interactions arise from finite-N corrections. The framework offers both a new approach to QFT and a principled explanation for why real-world fields are nearly free.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work builds a two-way bridge between machine learning theory and quantum field theory, showing that the mathematical structures underlying neural networks (Gaussian processes, the CLT, parameter distributions) can directly constitute physical field theories satisfying the Osterwalder-Schrader axioms.

- **Impact on Artificial Intelligence:** The framework reinterprets the NNGP correspondence not just as an approximation tool, but as a constructive method for defining quantum field theories, pointing to new mathematical questions about what large neural networks actually compute.

- **Impact on Fundamental Interactions:** NN-QFTs provide a non-Lagrangian approach to constructing Lorentz-invariant quantum field theories, with built-in near-Gaussianity that explains why fundamental interactions are weakly coupled at accessible energies.

- **Outlook and References:** Future directions include constructing reflection-positive interacting NN-QFTs, mapping which architectures yield physically interesting models, and connecting NN-QFT dualities to known dualities in string theory and condensed matter. The paper is available at [arXiv:2112.04527](https://arxiv.org/abs/2112.04527).

## Original Paper Details
- **Title:** Building Quantum Field Theories Out of Neurons
- **arXiv ID:** 2112.04527
- **Authors:** ["James Halverson"]
- **Abstract:** An approach to field theory is studied in which fields are comprised of $N$ constituent random neurons. Gaussian theories arise in the infinite-$N$ limit when neurons are independently distributed, via the Central Limit Theorem, while interactions arise due to finite-$N$ effects or non-independently distributed neurons. Euclidean-invariant ensembles of neurons are engineered, with tunable two-point function, yielding families of Euclidean-invariant field theories. Some Gaussian, Euclidean invariant theories are reflection positive, which allows for analytic continuation to a Lorentz-invariant quantum field theory. Examples are presented that yield dual theories at infinite-$N$, but have different symmetries at finite-$N$. Landscapes of classical field configurations are determined by local maxima of parameter distributions. Predictions arise from mixed field-neuron correlators. Near-Gaussianity is exhibited at large-$N$, potentially explaining a feature of field theories in Nature.
