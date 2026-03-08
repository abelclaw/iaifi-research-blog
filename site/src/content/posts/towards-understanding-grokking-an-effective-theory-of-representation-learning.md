---
abstract: 'We aim to understand grokking, a phenomenon where models generalize long
  after overfitting their training set. We present both a microscopic analysis anchored
  by an effective theory and a macroscopic analysis of phase diagrams describing learning
  performance across hyperparameters. We find that generalization originates from
  structured representations whose training dynamics and dependence on training set
  size can be predicted by our effective theory in a toy setting. We observe empirically
  the presence of four learning phases: comprehension, grokking, memorization, and
  confusion. We find representation learning to occur only in a "Goldilocks zone"
  (including comprehension and grokking) between memorization and confusion. We find
  on transformers the grokking phase stays closer to the memorization phase (compared
  to the comprehension phase), leading to delayed generalization. The Goldilocks phase
  is reminiscent of "intelligence from starvation" in Darwinian evolution, where resource
  limitations drive discovery of more efficient solutions. This study not only provides
  intuitive explanations of the origin of grokking, but also highlights the usefulness
  of physics-inspired tools, e.g., effective theories and phase diagrams, for understanding
  deep learning.'
arxivId: '2205.10343'
arxivUrl: https://arxiv.org/abs/2205.10343
authors:
- Ziming Liu
- Ouail Kitouni
- Niklas Nolte
- Eric J. Michaud
- Max Tegmark
- Mike Williams
concepts:
- representation learning
- grokking
- effective field theory
- phase transitions
- embeddings
- learning phase diagrams
- interpretability
- transformers
- group theory
- loss function design
- scalability
figures:
- /iaifi-research-blog/figures/2205_10343/figure_1.png
- /iaifi-research-blog/figures/2205_10343/figure_1.png
- /iaifi-research-blog/figures/2205_10343/figure_2.png
- /iaifi-research-blog/figures/2205_10343/figure_2.png
- /iaifi-research-blog/figures/2205_10343/figure_3.png
- /iaifi-research-blog/figures/2205_10343/figure_3.png
pdfUrl: https://arxiv.org/pdf/2205.10343v2
published: '2022-05-20T17:56:17+00:00'
theme: Foundational AI
title: 'Towards Understanding Grokking: An Effective Theory of Representation Learning'
wordCount: 1290
---

## The Big Picture

Imagine studying for an exam by memorizing answers without understanding the concepts behind them. You ace every practice test, but when the real exam asks a slightly different question, you're lost. Then, weeks later, something clicks: you finally *understand* the material. That's roughly what happens inside a neural network during a phenomenon called **grokking**: the model memorizes training data almost instantly, seems stuck, and then, sometimes thousands of training steps later, abruptly figures out the actual rule.

Grokking was discovered in 2021 and immediately puzzled the machine learning community. Why would a model that has already memorized its training data bother learning to generalize, to apply learned rules to examples it has never seen before? And why does it sometimes take so long?

These aren't just theoretical curiosities. They cut to the heart of how and why neural networks learn anything at all. A team from MIT's Institute for AI and Fundamental Interactions attacked the problem with an unlikely toolkit: the methods of theoretical physics.

Their result is a surprisingly crisp story. Generalization isn't magic; it's geometry. And the timing of when it happens depends on where a model sits in a **phase diagram**, a map of possible learning behaviors similar to those physicists use to show when water becomes ice or steam.

> **Key Insight:** Grokking happens when a neural network is forced to discover structured, geometric representations of its input. Delayed generalization occurs because the network is trapped in a "memorization" phase before finding that structure.

## How It Works

The researchers built their analysis in two layers: a microscopic view using what physicists call an **effective theory**, and a macroscopic view using phase diagrams. Both converge on the same story.

![Figure 1](figure:1)

Start with the microscopic picture. The team studied a toy model learning modular addition: given two numbers *a* and *b*, predict *a + b* mod *p*. Each number gets a learnable **embedding vector**, a point in some geometric space, and a small network called a *decoder* reads off the sum from those points.

What do those embeddings look like when a model generalizes versus when it memorizes? In the memorization regime, embeddings are scattered randomly. Each number gets an arbitrary point in space, and the decoder learns to look up answers from a giant internal table. When the model generalizes, the embeddings snap into a structured representation: they form parallelograms.

If the embedding of 3 plus the embedding of 5 equals the embedding of 2 plus the embedding of 6 (since 3 + 5 = 2 + 6 = 8), the geometry enforces the arithmetic. For modular addition, the structure is even more specific: the embeddings arrange themselves on a circle.

![Figure 2](figure:2)

The researchers formalized this with a **Representation Quality Index (RQI)** measuring how parallelogram-like the embeddings are. An RQI near zero signals memorization; near one signals generalization. They then derived an effective theory, a physicist's technique of replacing a complicated system with a simpler model that captures the same essential behavior, that accurately predicts how RQI evolves during training and how much data is needed to force the model into structured representations.

Now the macroscopic picture. By running a grid search over **hyperparameters** (the settings that control how a network trains, such as learning rate and weight decay), the team mapped out a phase diagram with four distinct learning phases:

- **Comprehension**: The model generalizes quickly and efficiently.
- **Grokking**: The model eventually generalizes, but only after a long detour through memorization.
- **Memorization**: The model fits training data but never generalizes.
- **Confusion**: The model fails even to fit the training data.

Structured representation learning only occurs in what the authors call the **Goldilocks zone**, the region covering comprehension and grokking, sandwiched between memorization and confusion. **Regularization** (techniques that discourage a network from fitting training data too literally) is the key control knob. Too little, and the network takes the easy path of memorization. Too much, and it can't even do that.

The grokking phase sits right at the edge of the memorization phase. Generalization is delayed precisely because the model is barely nudged away from pure memorization; it takes a long time for training to push it across the boundary into genuine understanding.

## Why It Matters

The paper borrows an analogy from biology: "intelligence from starvation," inspired by Darwinian evolution. When resources are scarce, organisms are forced toward efficient solutions. When training data is constrained and regularization applies gentle pressure, a neural network is similarly forced to discover compact, structured rules rather than memorize individual examples. The Goldilocks zone is where this pressure works: enough to prevent lazy memorization, not so much that learning fails entirely.

This has practical consequences. The researchers show that grokking can be *de-delayed*, moved from the slow grokking phase into the fast comprehension phase, by navigating the phase diagram with informed hyperparameter choices. Understanding why grokking happens tells practitioners how to train models that generalize faster.

The paper also makes a case that physics-inspired tools (effective theories, phase diagrams, representation analysis) are underused in machine learning research. The same methods physicists apply to phase transitions in magnets or quantum materials turn out to work well for understanding phase transitions in learning dynamics.

Open questions remain. The effective theory works cleanly in the toy setting; extending it to full transformers and real-world tasks requires further work. The precise mechanisms by which regularization pushes embeddings toward structured configurations are still being mapped out.

> **Bottom Line:** Grokking isn't a mystery anymore. It's a phase transition in representation space, and the theoretical tools now exist to predict when it happens, why it's delayed, and how to make it faster.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work applies two foundational tools from theoretical physics, effective theories and phase diagrams, to decode a core puzzle in deep learning. Methods from condensed matter physics translate naturally to neural network dynamics.

- **Impact on Artificial Intelligence:** The study explains grokking's delayed generalization through the lens of representation learning and provides a principled framework for navigating hyperparameter space to achieve faster, more reliable generalization.

- **Impact on Fundamental Interactions:** By formalizing how structured geometric representations emerge during learning and linking this to phase transitions and symmetry in embedding space, the work connects physics and the theory of intelligence in a concrete way.

- **Outlook and References:** Future work will extend the effective theory to larger transformer architectures and real-world tasks; the full paper is available at [arXiv:2205.10343](https://arxiv.org/abs/2205.10343).

## Original Paper Details
- **Title:** Towards Understanding Grokking: An Effective Theory of Representation Learning
- **arXiv ID:** 2205.10343
- **Authors:** ["Ziming Liu", "Ouail Kitouni", "Niklas Nolte", "Eric J. Michaud", "Max Tegmark", "Mike Williams"]
- **Abstract:** We aim to understand grokking, a phenomenon where models generalize long after overfitting their training set. We present both a microscopic analysis anchored by an effective theory and a macroscopic analysis of phase diagrams describing learning performance across hyperparameters. We find that generalization originates from structured representations whose training dynamics and dependence on training set size can be predicted by our effective theory in a toy setting. We observe empirically the presence of four learning phases: comprehension, grokking, memorization, and confusion. We find representation learning to occur only in a "Goldilocks zone" (including comprehension and grokking) between memorization and confusion. We find on transformers the grokking phase stays closer to the memorization phase (compared to the comprehension phase), leading to delayed generalization. The Goldilocks phase is reminiscent of "intelligence from starvation" in Darwinian evolution, where resource limitations drive discovery of more efficient solutions. This study not only provides intuitive explanations of the origin of grokking, but also highlights the usefulness of physics-inspired tools, e.g., effective theories and phase diagrams, for understanding deep learning.
