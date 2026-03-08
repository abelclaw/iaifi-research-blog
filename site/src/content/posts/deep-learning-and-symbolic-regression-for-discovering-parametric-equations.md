---
abstract: Symbolic regression is a machine learning technique that can learn the governing
  formulas of data and thus has the potential to transform scientific discovery. However,
  symbolic regression is still limited in the complexity and dimensionality of the
  systems that it can analyze. Deep learning on the other hand has transformed machine
  learning in its ability to analyze extremely complex and high-dimensional datasets.
  We propose a neural network architecture to extend symbolic regression to parametric
  systems where some coefficient may vary but the structure of the underlying governing
  equation remains constant. We demonstrate our method on various analytic expressions,
  ODEs, and PDEs with varying coefficients and show that it extrapolates well outside
  of the training domain. The neural network-based architecture can also integrate
  with other deep learning architectures so that it can analyze high-dimensional data
  while being trained end-to-end. To this end we integrate our architecture with convolutional
  neural networks to analyze 1D images of varying spring systems.
arxivId: '2207.00529'
arxivUrl: https://arxiv.org/abs/2207.00529
authors:
- Michael Zhang
- Samuel Kim
- Peter Y. Lu
- Marin Soljačić
concepts:
- symbolic regression
- parametric equation learning
- interpretability
- sparse models
- automated discovery
- inverse problems
- convolutional networks
- regression
- hypernetwork
- scalability
- physics-informed neural networks
- scientific workflows
figures:
- /iaifi-research-blog/figures/2207_00529/figure_1.png
- /iaifi-research-blog/figures/2207_00529/figure_1.png
- /iaifi-research-blog/figures/2207_00529/figure_2.png
- /iaifi-research-blog/figures/2207_00529/figure_2.png
- /iaifi-research-blog/figures/2207_00529/figure_3.png
- /iaifi-research-blog/figures/2207_00529/figure_3.png
pdfUrl: https://arxiv.org/pdf/2207.00529v2
published: '2022-07-01T16:25:59+00:00'
theme: Foundational AI
title: Deep Learning and Symbolic Regression for Discovering Parametric Equations
wordCount: 1092
---

## The Big Picture

Imagine trying to decode the rules of a game by watching thousands of rounds, except the rules keep changing slightly between rounds. The core logic stays the same, but key parameters shift in ways you can't directly observe. That's the challenge facing scientists who want to discover governing equations of physical systems with varying coefficients. A wave propagating through different materials, electricity flowing through a non-uniform conductor, an atom cloud responding to an external field: all obey equations whose structure is constant, but whose coefficients shift in complex ways.

**Symbolic regression** is the branch of machine learning that rediscovers actual mathematical formulas from data, rather than fitting a black-box model that predicts accurately but can't explain why. Feed in measurements, get back an interpretable equation. But existing approaches hit a wall when data comes from parametric systems, where an equation's coefficients depend on context. Standard tools either ignore the variation, average over it, or fail entirely.

Researchers at MIT have proposed a neural network framework that extends symbolic regression to parametric systems while integrating with other neural network components. The result: a system that can autonomously discover scientific laws from complex, high-dimensional data.

> **Key Insight:** By embedding symbolic regression inside a neural network that learns how coefficients vary, this approach recovers not just *an* equation but the *parametric family* of equations governing an entire class of physical systems.

## How It Works

The foundation is the **Equation Learner (EQL) network**, developed in prior work. Ordinary neural networks use opaque internal functions like ReLU activations. The EQL swaps those out for recognizable mathematical operations: sin, cos, multiplication, division, addition. The network's learned weights become the actual coefficients in a symbolic expression. When training converges, you don't have a black box. You read the equation directly from the network structure.

![Figure 1](figure:1)

The standard EQL handles only fixed equations. To tackle parametric systems, the team introduces two new variants:

- **SEQL (Stacked EQL):** Two EQL networks run in parallel. One processes input variables; the other processes the varying parameters. Their outputs are combined so the coefficient-predicting network can modulate the equation-learning network in real time.
- **HEQL (Hyper EQL):** Borrowing from **hypernetworks**, where a small meta-network generates the weights of a larger one, a compact network learns to *produce the weights* of the main EQL as a function of the varying parameters. It doesn't learn fixed weights; it learns how weights should change.

![Figure 2](figure:2)

Both architectures are differentiable end-to-end, so the entire system trains via standard gradient-based learning and can plug into other neural network components. The team shows this by attaching a **convolutional encoder** to the front of the HEQL, using it to analyze 1D images of oscillating spring systems. The image network extracts physical state from raw pixels; the HEQL then discovers the underlying equation. The full pipeline trains jointly, with no manual feature engineering.

Training uses **L1 regularization** to encourage sparsity, pushing small, irrelevant weights to exactly zero. Think of it as a built-in Occam's Razor. A progressive masking strategy prunes weights below a threshold mid-training, gradually sculpting the network toward a clean symbolic expression.

![Figure 3](figure:3)

On analytic benchmark expressions and partial differential equations with spatially or temporally varying coefficients, both SEQL and HEQL recover the correct equation structure. This includes nonlinear systems. The models also extrapolate well outside of the training domain, something black-box networks are notoriously bad at. A model that has truly learned a governing law, rather than memorizing statistical patterns, should generalize beyond its training data. These architectures do.

![Figure 4](figure:4)

## Why It Matters

Partial differential equations with varying coefficients aren't a niche curiosity. They show up everywhere in modern physics. Light and electromagnetic waves in materials with uneven properties (Maxwell's equations). Quantum particles moving through non-uniform environments (the Schrödinger equation). Fluids flowing through heterogeneous media. All demand exactly the kind of parametric equation discovery this work enables. Previous approaches assumed coefficient variation was simple or linear. This framework imposes far fewer constraints.

The integration with convolutional networks opens a broader door. Many experimental datasets arrive as raw images or high-dimensional sensor readings. Piping such data directly into a symbolic regression system, with the full stack trained jointly, means scientists could point this tool at experimental measurements and receive interpretable equations with minimal preprocessing. The spring-system demonstration shows it's achievable today, even if it's not yet routine.

Future extensions could tackle turbulence modeling, materials discovery, or biological dynamical systems where governing equations remain poorly understood.

> **Bottom Line:** This work teaches neural networks to discover the *parametric family of laws* governing physical systems, and to do so from raw, high-dimensional inputs.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work bridges machine learning methodology with physics equation discovery, designing neural architectures to handle the parametric complexity inherent in real physical systems, including PDEs with spatially varying coefficients.

- **Impact on Artificial Intelligence:** The SEQL and HEQL architectures extend symbolic regression to a new class of problems and show that end-to-end training with CNNs on high-dimensional data is practical, advancing interpretable machine learning.

- **Impact on Fundamental Interactions:** The framework enables automated discovery of governing equations for systems including the nonlinear Schrödinger equation and Maxwell's equations with varying material properties, both central to quantum mechanics and electrodynamics.

- **Outlook and References:** Future work may extend these architectures to higher-dimensional PDEs and noisier experimental datasets; the paper is available as [arXiv:2207.00529](https://arxiv.org/abs/2207.00529).

## Original Paper Details
- **Title:** Deep Learning and Symbolic Regression for Discovering Parametric Equations
- **arXiv ID:** 2207.00529
- **Authors:** ["Michael Zhang", "Samuel Kim", "Peter Y. Lu", "Marin Soljačić"]
- **Abstract:** Symbolic regression is a machine learning technique that can learn the governing formulas of data and thus has the potential to transform scientific discovery. However, symbolic regression is still limited in the complexity and dimensionality of the systems that it can analyze. Deep learning on the other hand has transformed machine learning in its ability to analyze extremely complex and high-dimensional datasets. We propose a neural network architecture to extend symbolic regression to parametric systems where some coefficient may vary but the structure of the underlying governing equation remains constant. We demonstrate our method on various analytic expressions, ODEs, and PDEs with varying coefficients and show that it extrapolates well outside of the training domain. The neural network-based architecture can also integrate with other deep learning architectures so that it can analyze high-dimensional data while being trained end-to-end. To this end we integrate our architecture with convolutional neural networks to analyze 1D images of varying spring systems.
