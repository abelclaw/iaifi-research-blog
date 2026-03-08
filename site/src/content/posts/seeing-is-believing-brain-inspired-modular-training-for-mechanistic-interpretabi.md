---
abstract: We introduce Brain-Inspired Modular Training (BIMT), a method for making
  neural networks more modular and interpretable. Inspired by brains, BIMT embeds
  neurons in a geometric space and augments the loss function with a cost proportional
  to the length of each neuron connection. We demonstrate that BIMT discovers useful
  modular neural networks for many simple tasks, revealing compositional structures
  in symbolic formulas, interpretable decision boundaries and features for classification,
  and mathematical structure in algorithmic datasets. The ability to directly see
  modules with the naked eye can complement current mechanistic interpretability strategies
  such as probes, interventions or staring at all weights.
arxivId: '2305.08746'
arxivUrl: https://arxiv.org/abs/2305.08746
authors:
- Ziming Liu
- Eric Gan
- Max Tegmark
concepts:
- interpretability
- modular training
- loss function design
- locality regularization
- sparse models
- geometric deep learning
- neuron swapping
- representation learning
- regression
- classification
- transformers
- group theory
figures:
- /iaifi-research-blog/figures/2305_08746/figure_1.png
- /iaifi-research-blog/figures/2305_08746/figure_1.png
- /iaifi-research-blog/figures/2305_08746/figure_2.png
- /iaifi-research-blog/figures/2305_08746/figure_2.png
- /iaifi-research-blog/figures/2305_08746/figure_3.png
- /iaifi-research-blog/figures/2305_08746/figure_3.png
pdfUrl: https://arxiv.org/pdf/2305.08746v3
published: '2023-05-04T17:56:42+00:00'
theme: Foundational AI
title: 'Seeing is Believing: Brain-Inspired Modular Training for Mechanistic Interpretability'
wordCount: 981
---

## The Big Picture

Imagine trying to understand how a radio works by staring at a tangled pile of wires, resistors, and capacitors jumbled together in a box. You could trace every connection, but you'd never *see* the radio. Now imagine the same components laid out on a workbench, logically grouped: the tuner here, the amplifier there, the speaker output neatly separated. The structure becomes obvious.

That's the problem facing researchers studying modern neural networks. A typical trained network is the tangled pile: billions of weights connecting millions of neurons in ways that seem almost deliberately opaque. Researchers have developed clever approaches, from testing individual neurons with targeted inputs to making controlled changes to internal activity to poring over raw connection strengths. These techniques work, but they demand enormous effort for modest payoff. What if you could simply *look* at a network and see its modules?

A team at MIT's IAIFI (Ziming Liu, Eric Gan, and Max Tegmark) has done exactly that. Their method, **Brain-Inspired Modular Training (BIMT)**, borrows a trick from biology to make neural networks physically self-organize into visible, interpretable components during training.

> **Key Insight:** By penalizing long-range connections the way evolution penalizes long axons in the brain, BIMT causes neural networks to spontaneously reorganize into compact, visible modules, making interpretability as easy as looking at a picture.

## How It Works

The core observation is almost too simple: brains are modular, artificial neural networks aren't, and the reason may come down to *geometry*. In a standard network, the training objective doesn't care where neurons live. You can shuffle neurons within a layer in any order and get identical behavior.

Brains work differently. Long neural connections consume more energy and space, so evolution pressured brains to keep related computations close together. Modularity emerged as a consequence.

BIMT recreates this pressure artificially with three ingredients:

1. **Geometric embedding** — Neurons are placed in a 2D (or 3D) Euclidean space. Neurons in the same layer sit at the same height, evenly spaced horizontally. Every connection now has a measurable physical length.
2. **Locality regularization** — The training loss gains a new term: the sum of each connection's length multiplied by the absolute value of its weight. Short, strong connections are cheap; long, strong connections are expensive. This generalizes standard L1 regularization, which produces sparse networks, by adding the geometric pressure that makes BIMT novel.
3. **Neuron swapping** — Gradient descent can get stuck. A neuron might be in the wrong position, making all its connections expensive, but no weight update will move it. BIMT periodically swaps pairs of neurons within a layer when doing so reduces the locality cost. Since swapping doesn't change what the network computes, only where it computes it, this step is purely about layout.

![Figure 1](figure:1)

Where a vanilla network trained on the same task produces a dense tangle, a BIMT-trained network snaps into compact clusters you can literally see by drawing the connectivity graph. The swap step turns out to matter a lot: without it, neurons get stuck in bad positions and locality regularization alone can't rescue them.

![Figure 2](figure:2)

BIMT was tested across a range of tasks. For **symbolic regression** (finding a mathematical formula that fits a dataset), BIMT discovered independence, with two input variables handled by entirely separate pathways. It revealed compositionality, where a formula like *f(g(x), h(y))* splits into identifiable sub-networks. And it exposed feature sharing, with multiple outputs reusing the same intermediate computation.

For **classification**, BIMT produced interpretable decision boundaries and human-recognizable feature detectors. For **algorithmic tasks** like modular arithmetic, it revealed tree-like connectivity graphs matching theoretical predictions about group representations (mathematical structures that describe symmetry) and uncovered a surprising "voting" mechanism where parallel modules collectively determine the output.

## Why It Matters

Current mechanistic interpretability relies heavily on **probing** (training auxiliary classifiers to detect concepts in activations), **activation patching** (surgically replacing activations to test causal influence), and raw weight analysis. These methods are powerful but slow. They work after the network is trained and require significant expertise to apply.

BIMT takes a different approach: interpretability *by design*, baked in during training. The module structure isn't reverse-engineered from a black box; it falls out directly from how the network was trained.

There are real connections to fundamental physics here too. The locality penalty is mathematically analogous to the **principle of least action**, nature's tendency to follow paths that minimize a cost accumulated over an entire trajectory. The researchers note that BIMT generalizes beyond fully connected networks to transformers and image architectures, which suggests it could scale to the models that matter most for AI safety and alignment research.

Open questions remain. Can BIMT handle truly large-scale models? What's the right geometric embedding for non-Euclidean structures like graphs or sequences? And does the modularity BIMT discovers always align with the modularity humans would identify by hand?

> **Bottom Line:** BIMT makes neural networks self-organize into visible modules by penalizing long connections, a simple, physics-inspired trick that turns interpretability from a painstaking reverse-engineering problem into something you can see with your own eyes.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work applies biological and physical intuitions (the metabolic cost of long axons, the principle of locality) directly to the engineering of interpretable AI, putting physics thinking to work inside deep learning.

- **Impact on Artificial Intelligence:** BIMT provides a practical training-time method for producing modular neural networks without requiring prior knowledge of problem structure, complementing existing post-hoc interpretability tools like probes and activation patching.

- **Impact on Fundamental Interactions:** By revealing compositional and group-theoretic structures in networks trained on algorithmic tasks, BIMT offers a new lens for discovering mathematical structure in learned representations, with direct applications to scientific AI.

- **Outlook and References:** Future work will test BIMT at the scale of large language models and deepen its connections to formal theories of neural modularity; the paper is available at [arXiv:2305.08746](https://arxiv.org/abs/2305.08746).
