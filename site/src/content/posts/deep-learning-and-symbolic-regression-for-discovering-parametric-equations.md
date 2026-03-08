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
wordCount: 974
---

## The Big Picture

Imagine trying to decode the rules of a game by watching thousands of rounds — but the rules keep changing slightly between rounds. The core logic stays the same, yet key parameters shift in ways you can't directly observe. This is the challenge facing scientists who want to discover the governing equations of physical systems with **varying coefficients** — the specific numbers that determine an equation's behavior. A wave propagating through different materials, electricity flowing through a non-uniform conductor, or an atom cloud responding to an external field: all obey equations whose *structure* is constant, but whose coefficients shift in complex ways.

**Symbolic regression** is the branch of machine learning that rediscovers actual mathematical formulas from data, rather than fitting a black-box model — one that predicts accurately but can't explain why. It's a powerful idea: feed in measurements, get back an interpretable equation. But existing approaches hit a wall when data comes from parametric systems, where an equation's coefficients depend on context. Standard tools either ignore the variation, average over it, or fail entirely.

Researchers at MIT have proposed a neural network framework that cracks this problem open, extending symbolic regression to parametric systems while integrating seamlessly with other AI components — a step toward machines that can autonomously discover scientific laws from complex, high-dimensional data.

> **Key Insight:** By embedding symbolic regression inside a neural network that learns how coefficients vary, this approach recovers not just *an* equation but the *parametric family* of equations governing an entire class of physical systems.

## How It Works

The foundation is the **Equation Learner (EQL) network**, developed in prior work. Unlike ordinary neural networks — which use opaque internal functions like ReLU activations — the EQL swaps those out for recognizable mathematical operations: sin, cos, multiplication, division, addition. The network's learned weights become the actual coefficients in a symbolic expression. When training converges, you don't have a black box; you read the equation directly from the network structure.

![Figure 1](/iaifi-research-blog/figures/2207_00529/figure_1.png)

The standard EQL handles only fixed equations. To tackle parametric systems, the MIT team introduces two new variants:

- **SEQL (Stacked EQL):** Two EQL networks run in parallel. One processes input variables; the other processes the varying parameters. Their outputs are combined so the coefficient-predicting network can modulate the equation-learning network in real time.
- **HEQL (Hyper EQL):** Inspired by **hypernetworks** — where a small meta-network generates the weights of a larger one — a compact network learns to *produce the weights* of the main EQL as a function of the varying parameters. Instead of learning fixed weights, it learns how weights should change.

![Figure 2](/iaifi-research-blog/figures/2207_00529/figure_1.png)

Both architectures are differentiable end-to-end: the entire system trains via standard gradient-based learning and can be connected to other AI components. The team demonstrates this by attaching a **convolutional encoder** — an image-processing neural network — to the front of the HEQL to analyze 1D images of oscillating spring systems. The image network extracts physical state from raw pixels; the HEQL then discovers the underlying equation. The full pipeline trains jointly, with no manual feature engineering.

Training applies **L1 regularization** to encourage sparsity — pushing small, irrelevant weights to exactly zero, mimicking Occam's Razor. A progressive masking strategy prunes weights below a threshold mid-training, gradually sculpting the network toward a clean symbolic expression.

![Figure 3](/iaifi-research-blog/figures/2207_00529/figure_2.png)

The results are striking. On analytic benchmark expressions and partial differential equations with spatially or temporally varying coefficients — including nonlinear systems — both SEQL and HEQL recover the correct equation structure. The models also **extrapolate well outside the training domain**, a property black-box networks notoriously lack. A model that has truly learned a governing law, rather than memorizing statistical patterns, should generalize beyond its training data — and these architectures do.

![Figure 4](/iaifi-research-blog/figures/2207_00529/figure_2.png)

## Why It Matters

Partial differential equations (PDEs) with varying coefficients aren't a niche curiosity — they're central to modern physics. How light and electromagnetic waves behave in materials with uneven properties (Maxwell's equations), how quantum particles move through non-uniform environments (the Schrödinger equation), how fluids flow through heterogeneous media — all demand exactly the kind of parametric equation discovery this work enables. Previous approaches required strong assumptions about coefficient variation, such as assuming they change in simple, linear ways. This framework imposes far fewer constraints.

The integration with convolutional networks opens a broader door. Many experimental datasets arrive as raw images or high-dimensional sensor readings. Piping such data directly into a symbolic regression system — with the full stack trained jointly — means scientists could, in principle, point this tool at experimental measurements and receive back interpretable equations with minimal preprocessing.

That's not yet routine, but the spring-system demonstration shows it's achievable today. Future extensions could tackle turbulence modeling, materials discovery, or biological dynamical systems where governing equations remain poorly understood.

> **Bottom Line:** This work teaches neural networks to discover the *parametric family of laws* governing physical systems — and to do so from raw, high-dimensional inputs. It's a meaningful step toward machines that can genuinely participate in scientific discovery.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges machine learning methodology with physics equation discovery, designing neural architectures specifically to handle the parametric complexity inherent in real physical systems — including PDEs with spatially varying coefficients.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The SEQL and HEQL architectures extend symbolic regression to a new class of problems and demonstrate seamless end-to-end training with CNNs on high-dimensional data, advancing the frontier of interpretable machine learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The framework enables automated discovery of governing equations for systems including the nonlinear Schrödinger equation and Maxwell's equations with varying material properties — central tools in quantum mechanics and electrodynamics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend these architectures to higher-dimensional PDEs and noisier experimental datasets; the paper is available as arXiv:2207.09408.</span></div></div>
</div>
