---
abstract: 'Grokking, the unusual phenomenon for algorithmic datasets where generalization
  happens long after overfitting the training data, has remained elusive. We aim to
  understand grokking by analyzing the loss landscapes of neural networks, identifying
  the mismatch between training and test losses as the cause for grokking. We refer
  to this as the "LU mechanism" because training and test losses (against model weight
  norm) typically resemble "L" and "U", respectively. This simple mechanism can nicely
  explain many aspects of grokking: data size dependence, weight decay dependence,
  the emergence of representations, etc. Guided by the intuitive picture, we are able
  to induce grokking on tasks involving images, language and molecules. In the reverse
  direction, we are able to eliminate grokking for algorithmic datasets. We attribute
  the dramatic nature of grokking for algorithmic datasets to representation learning.'
arxivId: '2210.01117'
arxivUrl: https://arxiv.org/abs/2210.01117
authors:
- Ziming Liu
- Eric J. Michaud
- Max Tegmark
concepts:
- grokking
- lu mechanism
- representation learning
- interpretability
- weight norm dynamics
- loss function design
- embeddings
- scalability
- classification
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2210_01117/figure_1.png
- /iaifi-research-blog/figures/2210_01117/figure_1.png
- /iaifi-research-blog/figures/2210_01117/figure_2.png
- /iaifi-research-blog/figures/2210_01117/figure_2.png
- /iaifi-research-blog/figures/2210_01117/figure_3.png
- /iaifi-research-blog/figures/2210_01117/figure_3.png
pdfUrl: https://arxiv.org/pdf/2210.01117v2
published: '2022-10-03T17:58:04+00:00'
theme: Foundational AI
title: 'Omnigrok: Grokking Beyond Algorithmic Data'
wordCount: 964
---

## The Big Picture

Imagine studying for an exam by cramming thousands of practice problems. You ace every practice test — perfect score, every time. But then you sit for the real exam and fail completely.

You keep studying, weeks pass, and then one day something clicks. Suddenly you understand the material *deeply*, and your score skyrockets. That's bizarre behavior, and it's exactly what researchers discovered neural networks were doing.

This phenomenon, dubbed **grokking**, was first observed in 2022 when networks trained on arithmetic tasks would memorize training examples almost immediately, without learning any underlying rules, then stall for thousands of training steps before suddenly cracking the pattern and generalizing perfectly. The original discovery raised two questions: *Why* does this happen, and *is it unique* to toy arithmetic puzzles? A team at MIT's IAIFI set out to find out.

The answer comes down to a simple geometric picture of how neural networks navigate the space of possible solutions. Grokking isn't some quirk of arithmetic datasets. It shows up in image recognition, sentiment analysis, and molecular property prediction too.

> **Key Insight:** Grokking is caused by a mismatch between how training loss and test loss behave as a function of model weight norm. By understanding this "LU mechanism," researchers can both *induce* and *eliminate* grokking across virtually any machine learning task.

## How It Works

The central idea starts with a reframing: instead of watching how a network's errors change over *training steps*, what if you watch how they change as a function of how *large* the model's weights are?

When you plot things this way, two distinct shapes appear. The **training loss** (how wrong the model is on examples it has already seen) traces an **L-shape**: it drops steeply then flattens, meaning many different weight sizes can fit the training data equally well. The **test loss** (how wrong the model is on *new*, unseen examples) traces a **U-shape**: there's a Goldilocks zone where weights must be just the right size for the model to truly generalize.

![Figure 1](figure:1)

The team calls this the **LU mechanism**, named after those two curves. It explains grokking's strange dynamics:

1. A network initializes with large weights, sitting in the flat bottom of the L-curve.
2. It quickly memorizes the training data. Training loss hits near-zero, but the model fails on new examples.
3. **Regularization**, a technique that penalizes large weights to nudge the model toward simpler solutions, slowly pushes the weight norm down toward the Goldilocks zone.
4. When regularization is weak, this drift takes forever, producing the dramatic delay we call grokking.
5. When **weight decay** finally brings the network into the Goldilocks zone, generalization suddenly snaps into place.

The math is precise: if the weight decay coefficient is γ and the initial weight norm is w₀, generalization time scales as ln(w₀/wc)/γ. Halving the weight decay doubles the grokking delay.

![Figure 2](figure:2)

To test this, the team used a **teacher-student setup**, a controlled experiment where a small "student" network learns to copy the outputs of a fixed, pre-trained "teacher." This stripped-down environment let them manipulate every variable and watch exactly how the LU landscape governed training dynamics. Large initializations caused grokking, small initializations caused fast generalization, and tuning regularization moved the network's trajectory through the landscape exactly as predicted.

## Why It Matters

With the LU mechanism in hand, the team induced grokking where nobody had seen it before. They deliberately inflated initialization weight norms and triggered grokking on MNIST image classification, IMDb sentiment analysis, and QM9 molecular property prediction. Real-world datasets, real-world architectures, full grokking, on demand.

![Figure 3](figure:3)

They also ran the movie backward: for algorithmic datasets where grokking is normally dramatic, constraining the weight norm during training almost entirely eliminated the delay. Grokking isn't inevitable. It's a consequence of specific geometric conditions that can be engineered away.

The paper also clarifies *why* algorithmic tasks produce such extreme grokking compared to image classification. On image tasks, there is essentially one Goldilocks zone: the network's internal representations don't fundamentally shift as training progresses. But on algorithmic tasks, there are *two* distinct zones, one for memorization-based representations and one for generalizing ones.

The "good" zone sits at a smaller weight norm. A network starting at standard initialization overshoots it entirely, forcing regularization to work twice as hard, and grokking becomes twice as dramatic. This connection to **representation learning** (how networks internally organize and encode information) raises new questions. Any task where generalizing representations require fundamentally different weight configurations than memorizing ones will be prone to severe grokking. Understanding which tasks have this property, and designing training procedures that navigate around it, could change how practitioners approach generalization in deep learning.

> **Bottom Line:** The LU mechanism provides a unified geometric explanation for grokking, and by extending it to images, text, and molecules, this work shows grokking is a universal feature of neural network training, not an algorithmic curiosity.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work applies geometric analysis rooted in physics intuition (examining loss landscapes as surfaces with characteristic shapes) to explain a foundational puzzle in machine learning, showing how a physicist's toolkit can untangle complex AI phenomena.

- **Impact on Artificial Intelligence:** By identifying the LU mechanism, the paper gives practitioners a principled handle on grokking: the ability to predict when it will occur, induce it experimentally, and eliminate it by constraining weight norm during training.

- **Impact on Fundamental Interactions:** The Goldilocks zone framework connects to broader questions about the geometry of solution spaces in physical systems and how neural networks used in physics simulations find generalizing solutions.

- **Outlook and References:** Future work may investigate which real-world tasks have multi-zone loss landscapes and develop training algorithms that efficiently navigate to the good representation zone; the full paper is available at [arXiv:2210.01117](https://arxiv.org/abs/2210.01117).
