---
abstract: Deep ensembles (DE) have been successful in improving model performance
  by learning diverse members via the stochasticity of random initialization. While
  recent works have attempted to promote further diversity in DE via hyperparameters
  or regularizing loss functions, these methods primarily still rely on a stochastic
  approach to explore the hypothesis space. In this work, we present Multi-Symmetry
  Ensembles (MSE), a framework for constructing diverse ensembles by capturing the
  multiplicity of hypotheses along symmetry axes, which explore the hypothesis space
  beyond stochastic perturbations of model weights and hyperparameters. We leverage
  recent advances in contrastive representation learning to create models that separately
  capture opposing hypotheses of invariant and equivariant functional classes and
  present a simple ensembling approach to efficiently combine appropriate hypotheses
  for a given task. We show that MSE effectively captures the multiplicity of conflicting
  hypotheses that is often required in large, diverse datasets like ImageNet. As a
  result of their inherent diversity, MSE improves classification performance, uncertainty
  quantification, and generalization across a series of transfer tasks.
arxivId: '2303.02484'
arxivUrl: https://arxiv.org/abs/2303.02484
authors:
- Charlotte Loh
- Seungwook Han
- Shivchander Sudalairaj
- Rumen Dangovski
- Kai Xu
- Florian Wenzel
- Marin Soljacic
- Akash Srivastava
concepts:
- ensemble methods
- contrastive learning
- equivariant neural networks
- hypothesis space diversity
- symmetry preservation
- representation learning
- uncertainty quantification
- transfer learning
- self-supervised learning
- group theory
- data augmentation
figures:
- /iaifi-research-blog/figures/2303_02484/figure_1.png
- /iaifi-research-blog/figures/2303_02484/figure_1.png
- /iaifi-research-blog/figures/2303_02484/figure_2.png
- /iaifi-research-blog/figures/2303_02484/figure_2.png
- /iaifi-research-blog/figures/2303_02484/figure_3.png
- /iaifi-research-blog/figures/2303_02484/figure_3.png
pdfUrl: https://arxiv.org/pdf/2303.02484v2
published: '2023-03-04T19:11:54+00:00'
theme: Foundational AI
title: 'Multi-Symmetry Ensembles: Improving Diversity and Generalization via Opposing
  Symmetries'
wordCount: 1135
---

## The Big Picture

Imagine you're teaching someone to recognize dogs. You'd probably want them to notice that a dog flipped upside-down is still a dog. But you'd also want them to know that *orientation* matters — a dog lying on its side looks different from one standing at attention, and that difference carries real information.

Now imagine you're teaching them to recognize flowers. For flowers, orientation is almost irrelevant — a rose rotated 90 degrees is still unmistakably a rose. These two lessons are in fundamental tension. And that tension is at the heart of one of the most persistent challenges in machine learning.

When researchers build ensembles of neural networks — collections of models that vote together on predictions — they typically rely on randomness to create diversity. Each model starts from a different random configuration and, through the chaos of training, lands somewhere different in the solution space.

But this approach has a ceiling. No matter how many randomly initialized models you combine, they'll cluster around the same basic assumption about how the world works. They're like a team of people who all attended the same school: diverse in small ways, shaped by the same core beliefs.

A team of researchers from MIT, MIT-IBM Watson AI Lab, and collaborating institutions have built something better. Their framework, **Multi-Symmetry Ensembles (MSE)**, doesn't shuffle the deck randomly — it deliberately trains models that hold *opposing views* about the geometric structure of the world, then combines their strengths.

> **Key Insight:** MSE builds diverse ensembles by pairing models that treat the same transformations — like rotations — in fundamentally opposite ways: one ignoring the transformation (invariant), one tracking it precisely (equivariant). This structured opposition creates diversity that random initialization simply cannot.

## How It Works

The central concept is the distinction between **invariance** and **equivariance** — two ways a model can respond to geometric transformations like rotation, reflection, or flipping.

![Figure 1](/iaifi-research-blog/figures/2303_02484/figure_1.png)

An **invariant** model, shown a rotated image, produces the same output regardless of rotation — it has learned to ignore the change entirely. An **equivariant** model tracks the rotation, its output changing *in sync with* how the input changed, preserving orientation information. Neither approach is universally better.

For flowers, invariance wins. For dogs with characteristic postures, equivariance wins. In a massive dataset like ImageNet — containing both flowers and dogs, plus a thousand other categories — both assumptions are simultaneously correct, for different slices of the data. Traditional ensembles can't navigate this. Even a large ensemble of equivariant models remains fundamentally equivariant; you can't average your way to invariance.

MSE solves this by deliberately constructing the ensemble from both camps. Here's how:

1. **Contrastive pretraining with opposing symmetries.** The team leverages recent advances in self-supervised learning — where models learn from unlabeled data by comparing examples against each other — specifically a method called Equivariant Self-Supervised Learning (E-SSL). This allows them to pretrain separate models that explicitly encode invariant versus equivariant representations, training one model to be agnostic to rotations and another to be sensitive to them.

2. **Task-agnostic diversity.** This diversity is baked into the *representations* — the internal features a model learns — before any task-specific training. This matters enormously for transfer learning, where a model trained on one dataset is later applied to a new task. Geometric assumptions shape everything downstream, so getting them right at the representation level pays dividends across many tasks.

3. **Greedy ensembling.** Once diverse members are trained, the researchers use a greedy selection strategy to combine them. Rather than blindly averaging all models, they select combinations that maximize validation performance, efficiently identifying which symmetry assumptions help for a given task.

![Figure 2](/iaifi-research-blog/figures/2303_02484/figure_1.png)

The team tested MSE on ImageNet classification, uncertainty calibration (how well a model knows when it doesn't know), and a battery of transfer tasks. The results reveal something striking: combining a high-accuracy equivariant model with a *weaker* invariant model can outperform an ensemble of multiple high-accuracy equivariant models. The weaker model isn't a drag — it's carrying information the stronger model fundamentally cannot represent. Diversity, not raw accuracy, drives ensemble performance.

![Figure 3](/iaifi-research-blog/figures/2303_02484/figure_2.png)

MSE also extends beyond rotational symmetry. The framework generalizes to other symmetry groups — horizontal flipping, color jitter, and more — and combining models with opposing hypotheses across *multiple* symmetry axes yields further gains. The geometry of the hypothesis space is rich, and MSE systematically explores it.

## Why It Matters

For AI researchers, MSE reframes the diversity problem. Instead of asking "how do we make models more randomly different," it asks "what are the *structurally distinct* ways of understanding this data, and can we explicitly represent each?" This connects ensemble theory to the physics of symmetry groups and opens the door to far richer ensemble designs.

For the broader intersection of AI and physical reasoning, the work highlights something profound: geometric symmetry isn't just a mathematical nicety. It's a hypothesis about how the world works, and real-world datasets are full of objects that *disagree* about which symmetries apply. A model forced to commit to one geometric worldview will always be blind to the others.

MSE's structured pluralism — holding multiple, conflicting geometric hypotheses simultaneously — is closer to how physicists themselves think. Different physical regimes obey different symmetries; the art is knowing which applies when.

Open questions abound. Can MSE extend to more exotic symmetry groups relevant to physics — gauge symmetries, Lorentz invariance? Can the greedy ensembling approach become fully adaptive at inference time, routing different inputs to the most appropriate ensemble member? As models grow larger and pretraining more expensive, can MSE's diversity gains be achieved at lower computational cost?

> **Bottom Line:** Multi-Symmetry Ensembles show that the best path to diverse, reliable neural networks isn't more randomness — it's structured geometric disagreement. By pairing models with opposing symmetry hypotheses, MSE achieves classification, calibration, and transfer performance that purely stochastic ensembles cannot match.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly imports concepts from physics — symmetry groups, invariance, and equivariance — into the engineering of machine learning systems, demonstrating that the mathematical language of fundamental physics provides actionable design principles for AI.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">MSE establishes a new paradigm for ensemble diversity, showing that structured symmetry-based disagreement between models outperforms stochastic diversity alone, with measurable gains in classification accuracy, uncertainty quantification, and cross-dataset transfer.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By demonstrating that large visual datasets contain inherently conflicting symmetry hypotheses, this work formalizes an observation familiar to physicists — that the correct symmetry group depends on context — and builds models that respect this multiplicity.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend MSE to symmetry groups central to physics (gauge invariance, Lorentz symmetry) and to adaptive inference-time ensemble routing; the paper is available at arXiv and the code at github.com/clott3/multi-sym-ensem.</span></div></div>
</div>
