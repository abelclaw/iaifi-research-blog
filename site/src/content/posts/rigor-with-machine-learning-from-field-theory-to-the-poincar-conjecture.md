---
abstract: Machine learning techniques are increasingly powerful, leading to many breakthroughs
  in the natural sciences, but they are often stochastic, error-prone, and blackbox.
  How, then, should they be utilized in fields such as theoretical physics and pure
  mathematics that place a premium on rigor and understanding? In this Perspective
  we discuss techniques for obtaining rigor in the natural sciences with machine learning.
  Non-rigorous methods may lead to rigorous results via conjecture generation or verification
  by reinforcement learning. We survey applications of these techniques-for-rigor
  ranging from string theory to the smooth $4$d Poincaré conjecture in low-dimensional
  topology. One can also imagine building direct bridges between machine learning
  theory and either mathematics or theoretical physics. As examples, we describe a
  new approach to field theory motivated by neural network theory, and a theory of
  Riemannian metric flows induced by neural network gradient descent, which encompasses
  Perelman's formulation of the Ricci flow that was utilized to resolve the $3$d Poincaré
  conjecture.
arxivId: '2402.13321'
arxivUrl: https://arxiv.org/abs/2402.13321
authors:
- Sergei Gukov
- James Halverson
- Fabian Ruehle
concepts:
- neural network field theory
- quantum field theory
- conjecture generation
- reinforcement learning
- ricci flow
- string theory
- automated discovery
- interpretability
- kernel methods
- renormalization
- optimal transport
- bayesian inference
figures:
- /iaifi-research-blog/figures/2402_13321/figure_2.png
pdfUrl: https://arxiv.org/pdf/2402.13321v1
published: '2024-02-20T19:00:59+00:00'
theme: Theoretical Physics
title: Rigor with Machine Learning from Field Theory to the Poincaré Conjecture
wordCount: 1190
---

## The Big Picture

Imagine hiring a brilliant but unreliable assistant. Brilliant enough to solve problems that stump experts, but prone to inventing facts, changing answers on a whim, and incapable of explaining its reasoning. That's the situation mathematicians and theoretical physicists face with modern machine learning.

The tension runs deep. In pure mathematics and theoretical physics, there are no approximations. A theorem is either proven or it isn't. An equation either holds or it doesn't. These standards, refined over centuries, leave little room for tools that are stochastic by nature and opaque by design.

So when ML started outperforming humans across science (protein folding, game-playing, materials discovery), physicists and mathematicians faced a real question: can we harness this power without sacrificing rigor?

Sergei Gukov, James Halverson, and Fabian Ruehle argue the answer is yes. Working across Caltech, Northeastern, and IAIFI, they lay out a framework for deploying ML in mathematics and theoretical physics, not as a replacement for proof, but as a partner to it.

> ML doesn't need to be rigorous itself to produce rigorous results. It can generate conjectures for humans to prove, or play mathematical games whose winning moves *are* formal proofs.

## How It Works

The authors identify two distinct pathways from probabilistic ML to proven mathematics.

**Conjecture generation.** Neural networks are universal function approximators. Given enough data, they learn to predict one property of a mathematical object from another. When a network makes such predictions reliably, it hints that a deep relationship exists, even if the network can't explain why.

Human experts can then:
1. Interrogate the model using interpretable AI techniques (such as attribution methods that identify which input features matter most)
2. Distill that hint into a precise mathematical conjecture
3. Prove the conjecture by conventional means

This pipeline has already produced real theorems. In knot theory, ML-assisted conjecture generation turned up new connections between algebraic properties and geometric invariants that mathematicians hadn't previously suspected. Similar methods have uncovered structure in the string theory landscape and in algebraic geometry involving **mirror symmetry**, where two geometrically different spaces turn out to be physically equivalent, like two different maps of the same territory.

![Figure 1](/iaifi-research-blog/figures/2402_13321/figure_2.png)

**Reinforcement learning as proof search.** Some mathematical problems can be recast as games. Design a game where winning requires demonstrating a mathematical fact, train an RL agent to play, and any winning strategy constitutes a rigorous proof, because the rules of the game *encode the logic of the problem*.

The authors highlight a striking application: the smooth four-dimensional Poincaré conjecture. The original conjecture (that any simply-connected closed 3-manifold is topologically equivalent to a 3-sphere) was solved by Grigori Perelman using Ricci flow. The smooth 4d version remains open, with hundreds of proposed counterexamples in the form of exotic knots.

An RL program trained to test the **ribbonness** of knots, a geometric property whose presence rules out a knot as a counterexample, systematically eliminated hundreds of candidates. It performed far beyond typical human expert ability. Every win was a theorem.

## Why It Matters

The paper goes further than applied strategies. It draws direct connections between neural network theory and fundamental physics.

The **NN-FT correspondence** (Neural Network–Field Theory correspondence) establishes a formal parallel between neural networks and quantum field theories, the mathematical language of particles and forces. At initialization, a sufficiently wide neural network defines a Gaussian process that corresponds precisely to a free quantum field theory. During training, interactions turn on, deforming the free theory into an interacting one.

The authors show that *ϕ*⁴ theory, a cornerstone of particle physics, can be explicitly realized as a neural network field theory, with the potential to provide a non-perturbative continuum definition of QFT. That's one of the field's long-standing open challenges.


The second bridge involves **metric flows**, tools describing how a space's geometry changes continuously over time. Represent a Riemannian metric as a neural network and train it with gradient descent: the resulting dynamics define a flow on the space of metrics. Using **neural tangent kernel** theory, which describes how infinitely wide networks evolve during training, the authors derive a general theory of such flows.

This framework turns out to encompass Perelman's formulation of Ricci flow as a gradient flow, the very tool that proved the 3d Poincaré conjecture. The mathematics of deep learning and the mathematics of topology's greatest triumph are the same mathematics.

We are at an inflection point. ML is already transforming science, but its adoption in mathematics and theoretical physics has been cautious, because rigor matters. The paper doesn't argue that ML should replace proof. It argues that ML and proof can be deeply integrated, each strengthening the other.

Open questions remain. Can the NN-FT correspondence yield new non-perturbative results in particle physics? Can metric flow theory find new applications in geometry? Can RL programs crack the smooth 4d Poincaré conjecture itself?

> Gukov, Halverson, and Ruehle show that ML's lack of inherent rigor is no barrier to rigorous results, and that the deepest connections between neural network theory and fundamental physics may still be waiting to be found.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work builds precise mathematical connections between neural network theory, quantum field theory, and differential geometry, showing that machine learning is itself a source of new mathematical structures, not merely a computational tool.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper presents a framework for deploying ML in high-stakes scientific domains, combining interpretable AI, conjecture generation, and reinforcement learning into a pipeline that converts probabilistic predictions into verified theorems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The NN-FT correspondence offers a potential non-perturbative continuum definition of quantum field theory, while the neural-network-induced metric flow theory recovers Perelman's Ricci flow, linking deep learning dynamics to the proof of the 3d Poincaré conjecture.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">This Perspective opens a research agenda that could reshape how theoretical physics and pure mathematics use AI; the full paper is available at [arXiv:2402.13321](https://arxiv.org/abs/2402.13321) and represents ongoing work at IAIFI at the frontier of AI and fundamental science.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Rigor with Machine Learning from Field Theory to the Poincaré Conjecture</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[arXiv:2402.13321](https://arxiv.org/abs/2402.13321)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Sergei Gukov", "James Halverson", "Fabian Ruehle"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Machine learning techniques are increasingly powerful, leading to many breakthroughs in the natural sciences, but they are often stochastic, error-prone, and blackbox. How, then, should they be utilized in fields such as theoretical physics and pure mathematics that place a premium on rigor and understanding? In this Perspective we discuss techniques for obtaining rigor in the natural sciences with machine learning. Non-rigorous methods may lead to rigorous results via conjecture generation or verification by reinforcement learning. We survey applications of these techniques-for-rigor ranging from string theory to the smooth $4$d Poincaré conjecture in low-dimensional topology. One can also imagine building direct bridges between machine learning theory and either mathematics or theoretical physics. As examples, we describe a new approach to field theory motivated by neural network theory, and a theory of Riemannian metric flows induced by neural network gradient descent, which encompasses Perelman's formulation of the Ricci flow that was utilized to resolve the $3$d Poincaré conjecture.</span></div></div>
</div>
