---
abstract: These notes are based on lectures I gave at TASI 2024 on Physics for Machine
  Learning. The focus is on neural network theory, organized according to network
  expressivity, statistics, and dynamics. I present classic results such as the universal
  approximation theorem and neural network / Gaussian process correspondence, and
  also more recent results such as the neural tangent kernel, feature learning with
  the maximal update parameterization, and Kolmogorov-Arnold networks. The exposition
  on neural network theory emphasizes a field theoretic perspective familiar to theoretical
  physicists. I elaborate on connections between the two, including a neural network
  approach to field theory.
arxivId: '2408.00082'
arxivUrl: https://arxiv.org/abs/2408.00082
authors:
- Jim Halverson
concepts:
- quantum field theory
- neural tangent kernel
- stochastic processes
- neural network field theory
- kernel methods
- kolmogorov-arnold networks
- feature extraction
- maximal update parameterization
- symmetry preservation
- renormalization
- scalability
figures:
- /iaifi-research-blog/figures/2408_00082/figure_1.png
- /iaifi-research-blog/figures/2408_00082/figure_2.png
- /iaifi-research-blog/figures/2408_00082/figure_3.png
pdfUrl: https://arxiv.org/pdf/2408.00082v1
published: '2024-07-31T18:00:22+00:00'
theme: Theoretical Physics
title: TASI Lectures on Physics for Machine Learning
wordCount: 1128
---

## The Big Picture

Imagine you're a theoretical physicist dropped into the 1960s, just as experimentalists are discovering dozens of new particles—pions, kaons, sigma baryons—faster than anyone can make sense of them. The theory hasn't caught up. The experimentalists are running laps around the theorists.

Sound familiar? That's precisely the situation in machine learning today. Neural networks beat world champions at Go, fold proteins, and generate images indistinguishable from photographs, yet the theoretical understanding of *why* they work remains frustratingly incomplete. At TASI 2024, one of the most prestigious summer schools in theoretical physics, Jim Halverson of Northeastern University delivered lectures designed to close that gap using physics' most powerful conceptual tools: equations describing how forces spread through space, mathematics for handling vast systems of interacting parts, and the trick of asking what happens as a system grows infinitely large.

The result is a framework for understanding neural networks from first principles, organized around three fundamental questions: what can a network *express*, what does it *look like statistically*, and how does it *evolve* during training?

> **Key Insight:** Neural networks and quantum field theories share deep mathematical structure, and exploiting that connection gives physicists a powerful new lens for understanding why deep learning works.

## How It Works

Halverson structures the entire framework around a deceptively simple object: a neural network as a function mapping inputs to outputs through adjustable parameters. (Mathematically, *ϕ_θ: ℝᵈ → ℝ* means the network takes a *d*-dimensional input and produces a single number.) The central question of what that network actually predicts is complicated by two intertwined problems:

- **Statistics:** Parameters are initialized randomly, so the network is a random function.
- **Dynamics:** Training changes those parameters over time.

These two pillars, plus a third on expressivity, form the architecture of the lectures.

**Expressivity** asks what functions a network can represent at all. The classic answer is the **Universal Approximation Theorem**: a sufficiently wide single-hidden-layer network can approximate any continuous function to arbitrary accuracy. Halverson also covers the **Kolmogorov-Arnold Theorem**, a result about decomposing multivariate functions into compositions of simpler ones. That connection recently inspired an entirely new architecture called Kolmogorov-Arnold Networks (KANs), which replace fixed activation functions with learnable ones placed on the network's edges rather than nodes.

![Figure 1](/iaifi-research-blog/figures/2408_00082/figure_1.png)

**Statistics** is where the physics perspective really shines. When you initialize a neural network with random parameters, the resulting function is itself a random object. In the infinite-width limit, Halverson shows it converges to a **Gaussian Process**, a probability distribution over *functions* (rather than individual numbers) that's completely characterized by its mean and covariance. The covariance function is called the **kernel**, and this result is the **NNGP (Neural Network/Gaussian Process) correspondence**.

Finite-width networks are non-Gaussian, and Halverson develops the machinery to handle the corrections: a perturbative expansion in 1/width, visualized using **Feynman diagrams** (the same loop-diagram bookkeeping from particle physics, repurposed to track neural network interactions). These non-Gaussian corrections encode the network's capacity to learn *features*, internal representations of the data, rather than simply fitting a fixed kernel.

**Dynamics** brings in the **Neural Tangent Kernel (NTK)**: in the infinite-width limit, gradient descent doesn't change the kernel at all. Parameters move, but the geometry of function space stays frozen. This makes training exactly solvable (it becomes a linear ODE in function space) and corresponds to **lazy learning**, where the network essentially performs **kernel regression**, fitting a smooth curve through training data using the fixed kernel as a similarity measure between inputs.

![Figure 2](/iaifi-research-blog/figures/2408_00082/figure_2.png)

The more interesting regime is **feature learning**, captured by the **maximal update parameterization (μP)**, a specific way of scaling weights so that hidden layers update by order-one amounts during training rather than shrinking toward zero as the network grows wider. Here, hidden layers actually learn internal representations that adapt to the data. The contrast between NTK and μP is one of the sharpest conceptual distinctions in modern neural network theory, with direct practical consequences for how large models should be scaled and initialized.

## Why It Matters

The deepest section of the lectures is the **NN-FT correspondence**: a formal map between neural network theory and quantum field theory (QFT). In QFT, the central object is a path integral, a weighted sum over all possible field configurations. In neural network theory, the analogous object is an integral over all possible parameter configurations, weighted by the initialization distribution. The two frameworks share the same mathematical skeleton.

Halverson shows explicitly how *ϕ⁴* theory (a workhorse of particle physics built around a field raised to the fourth power) emerges from the neural network perturbative expansion, with the quartic coupling playing the role of the non-Gaussian correction. This isn't mere analogy. It opens a bidirectional research program: physicists can apply **renormalization group** methods, tools for tracking how a theory's behavior changes with scale, to understand neural network scaling, while ML researchers can use neural networks as computational tools for field theory calculations.

Open questions include whether renormalization group flow of neural networks corresponds to something meaningful about learning, and what the "phases" of neural network behavior look like in hyperparameter space.

![Figure 3](/iaifi-research-blog/figures/2408_00082/figure_3.png)

For the broader ML community, this perspective brings clarity to questions that have felt empirically murky: Why do wider networks generalize better in some regimes? Why does parameterization choice matter so much at scale? Why do certain data symmetries get automatically respected by trained networks? These aren't philosophical questions; they have engineering consequences for how we design, train, and scale the next generation of AI systems.

> **Bottom Line:** By translating neural network theory into the language of quantum field theory, Halverson provides theoretical physicists with both a new research frontier and a rigorous foundation for understanding why deep learning works, with implications ranging from architecture design to the fundamental physics of information processing.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work establishes a rigorous mathematical correspondence between neural network theory and quantum field theory, creating a shared language that allows techniques from particle physics, including Feynman diagrams, perturbative expansions, and renormalization group methods, to be applied directly to understanding machine learning systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The lectures provide a unified theoretical framework covering expressivity, statistics, and dynamics of neural networks, including the neural tangent kernel and maximal update parameterization, offering principled guidance for architecture design and large-scale model training.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The NN-FT correspondence opens a new avenue for computing in quantum field theory, with neural networks used as flexible function approximators for path integrals and field configurations on manifolds including Calabi-Yau spaces relevant to string theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include applying renormalization group techniques to understand neural network scaling laws and using the μP feature-learning regime to probe phase transitions in learning; the full lecture notes are available at [arXiv:2408.00082](https://arxiv.org/abs/2408.00082).</span></div></div>
</div>
