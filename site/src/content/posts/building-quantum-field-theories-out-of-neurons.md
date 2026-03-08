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
wordCount: 1082
---

## The Big Picture

What if the universe is, in some deep sense, a neural network? That sounds like science fiction, but physicist James Halverson at Northeastern University has taken the question seriously — and built a rigorous mathematical framework that puts quantum field theory and machine learning on the same footing. Not metaphorically. Literally.

**Quantum field theory (QFT)** is the language of modern physics. It describes electrons, photons, quarks, and the Higgs boson — every fundamental particle and force we've ever measured. Traditionally, physicists write down a **Lagrangian** — a recipe encoding how particles move and interact — and derive all physics from there. Choosing the right recipe feels like an art. Halverson asks: what if you could skip the recipe entirely and build a quantum field out of neurons instead?

The result is a new construction called a **neural network quantum field theory (NN-QFT)**. In the usual approach, quantum randomness comes from averaging over all possible field configurations — summing over every conceivable way the universe could arrange itself. In Halverson's construction, randomness comes from the statistical properties of the neurons themselves. The paper shows this construction can satisfy all mathematical requirements for a legitimate QFT that obeys the symmetries of special relativity.

> **Key Insight:** By building fields out of random neurons, the Central Limit Theorem does the work that Lagrangians usually do — free theories emerge automatically at large N, while interactions arise from finite-N corrections and neuron correlations.

## How It Works

Start with a **scalar field** φ, which assigns a real number to every point in space. In Halverson's construction, this field is literally a sum of N random neurons:

φ(x) = a₁h₁(x) + a₂h₂(x) + ... + aₙhₙ(x)

Each **neuron** hᵢ is a randomly initialized function. The coefficients aᵢ are drawn from a distribution with variance σ²/N. No Lagrangian appears anywhere.

The magic happens in two limits. When N → ∞ and neurons are **independently distributed** — each chosen at random with no relationship to the others — the **Central Limit Theorem** kicks in. Just as averaging millions of coin flips produces a bell curve, summing millions of independent random neurons produces a **Gaussian theory**: the field-theory equivalent of a free particle. This mirrors a famous result in machine learning, the **Neural Network Gaussian Process (NNGP) correspondence**, which shows that infinitely wide neural networks behave like Gaussian processes — essentially free field theories.

Interactions enter in two ways:

- **Finite-N corrections** — at large but finite N, the CLT isn't exact, and the 4-point connected correlation function receives contributions of order 1/N
- **Independence breaking** — if neurons are correlated with each other, interactions appear even at infinite N through a term called I⁽⁴⁾_IB

The CLT assumes independence. Break that assumption, and you get non-trivial physics.

Getting from a Euclidean field theory to a genuine QFT requires satisfying the **Osterwalder-Schrader (OS) axioms** — mathematical conditions guaranteeing the theory can be translated into real spacetime, with a well-defined space of quantum states and no unphysical "ghost" particles that would violate probability conservation. The critical condition is **reflection positivity**: the theory's correlation functions must behave sensibly under time reflection. Halverson shows that for Gaussian NN-QFTs, reflection positivity reduces to a condition on the power spectrum G⁽²⁾(p), and constructs explicit neuron architectures that satisfy it. These are the first concrete NN-QFTs.

One striking result involves **duality**. Different neuron architectures — different internal symmetries, different parameter distributions — can yield identical theories at N → ∞ but diverge at finite N. This is the neural analog of well-known dualities in physics like electric-magnetic duality, now arising from the geometry of neuron parameter space rather than from deep symmetry principles. Two models that look identical from far away reveal their differences under a microscope.

The framework also redefines **classical field configurations**. With no action to minimize, classical solutions correspond to local maxima of the parameter distribution P(θ). The landscape of classical physics is literally the landscape of likely neuron parameters.

Finally, **predictions** in NN-QFT come from **mixed field-neuron correlators** — quantities involving both the output field φ and the constituent neurons hᵢ. In ordinary QFT there are no "constituent" degrees of freedom to correlate with. Here, the internal structure of the field is accessible, encoding how the macroscopic field emerges from its microscopic components.

## Why It Matters

For physics, this work opens a non-Lagrangian route into quantum field theory — valuable in regimes where writing down an action is hard, such as strongly coupled theories or exotic geometries.

The near-Gaussianity of real-world quantum fields has always seemed like a lucky accident — most QFTs in nature are weakly coupled and nearly free. Here it has a natural explanation: large-N suppression of non-Gaussian terms is built into the architecture from the start, just as it is in real neural networks.

For machine learning theory, the connection runs deeper than analogy. The growing field of "field theory of neural networks" imports QFT tools — Feynman diagrams, renormalization group flows — to understand how networks learn. Halverson's paper inverts this: instead of applying QFT to neural networks, it uses neural networks to *build* QFTs. Together, these directions suggest a much tighter mathematical unity between learning systems and physical theories than previously established.

> **Bottom Line:** Neural networks can construct quantum field theories from scratch — no Lagrangian required — with Gaussian theories emerging naturally at large N and interactions arising from finite-N corrections, offering both a new route into QFT and a principled explanation for why real-world fields are nearly free.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work establishes a rigorous two-way bridge between machine learning theory and quantum field theory, showing that the mathematical structures underlying neural networks — Gaussian processes, the CLT, parameter distributions — can literally *constitute* physical field theories satisfying the Osterwalder-Schrader axioms.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The framework reinterprets the NNGP correspondence not merely as an approximation tool, but as a constructive method for defining quantum field theories, opening new mathematical directions for understanding what large neural networks actually compute.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">NN-QFTs provide a non-Lagrangian approach to constructing Lorentz-invariant quantum field theories, with built-in near-Gaussianity offering a principled explanation for why fundamental interactions are weakly coupled at accessible energies.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include constructing reflection-positive interacting NN-QFTs, mapping the landscape of architectures that yield physically interesting models, and connecting NN-QFT dualities to known dualities in string theory and condensed matter; the paper is available at arXiv:2110.02965.</span></div></div>
</div>
