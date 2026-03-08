---
abstract: 'We attribute grokking, the phenomenon where generalization is much delayed
  after memorization, to compression. To do so, we define linear mapping number (LMN)
  to measure network complexity, which is a generalized version of linear region number
  for ReLU networks. LMN can nicely characterize neural network compression before
  generalization. Although the $L_2$ norm has been a popular choice for characterizing
  model complexity, we argue in favor of LMN for a number of reasons: (1) LMN can
  be naturally interpreted as information/computation, while $L_2$ cannot. (2) In
  the compression phase, LMN has linear relations with test losses, while $L_2$ is
  correlated with test losses in a complicated nonlinear way. (3) LMN also reveals
  an intriguing phenomenon of the XOR network switching between two generalization
  solutions, while $L_2$ does not. Besides explaining grokking, we argue that LMN
  is a promising candidate as the neural network version of the Kolmogorov complexity
  since it explicitly considers local or conditioned linear computations aligned with
  the nature of modern artificial neural networks.'
arxivId: '2310.05918'
arxivUrl: https://arxiv.org/abs/2310.05918
authors:
- Ziming Liu
- Ziqian Zhong
- Max Tegmark
concepts:
- linear mapping number
- grokking
- eigenvalue decomposition
- interpretability
- spectral methods
- nonlinear complexity
- clustering
- regression
- loss function design
- sparse models
figures:
- /iaifi-research-blog/figures/2310_05918/figure_1.png
- /iaifi-research-blog/figures/2310_05918/figure_1.png
- /iaifi-research-blog/figures/2310_05918/figure_2.png
- /iaifi-research-blog/figures/2310_05918/figure_2.png
- /iaifi-research-blog/figures/2310_05918/figure_3.png
- /iaifi-research-blog/figures/2310_05918/figure_3.png
pdfUrl: https://arxiv.org/pdf/2310.05918v1
published: '2023-10-09T17:59:18+00:00'
theme: Foundational AI
title: 'Grokking as Compression: A Nonlinear Complexity Perspective'
wordCount: 1187
---

## The Big Picture

Imagine teaching a child long division. For weeks, they memorize dozens of example problems by rote, matching inputs to outputs without grasping the underlying rule. Then one day, something clicks: they don't just know the answers; they *understand division*.

That delayed moment of insight is exactly what researchers call **grokking** in neural networks. A network trains on a small dataset, quickly achieving perfect accuracy on training examples, but failing completely on new data. Training continues. Nothing seems to happen. Thousands of steps later, the network suddenly generalizes, getting the right answer on examples it has never seen.

What was it doing during all that seemingly wasted time?

A [new paper](https://arxiv.org/abs/2310.05918) from MIT and IAIFI researchers Ziming Liu, Ziqian Zhong, and Max Tegmark proposes an answer: the network was *compressing*. To prove it, they invented a new way to measure how complicated a neural network actually is, one that makes physical sense.

> **Key Insight:** Grokking happens because neural networks first find a complex, bloated memorization solution, then slowly compress toward a simpler, more elegant generalization solution. A new metric called the **Linear Mapping Number** (LMN) tracks this compression precisely.

## How It Works

The standard tool for measuring neural network complexity has been the **L2 norm**, the total "weight" of a model's internal connections, calculated as the sum of their squared values. Smaller weights, the thinking goes, mean a simpler model.

The MIT team argues this is a poor proxy. A deep network can have enormous weights while computing only a single simple function. What matters isn't how large the numbers are; it's how many *distinct computations* the network performs.

Their alternative, the **Linear Mapping Number** (LMN), builds on a geometric insight. A **ReLU network** (a standard architecture whose internal switches activate only when their input exceeds zero) doesn't compute one smooth function. It carves up the space of possible inputs into regions, behaving like a completely different linear function within each one.

Think of it like origami: you fold a flat sheet repeatedly and end up with a complex 3D shape. The number of flat facets is the number of linear regions, a direct measure of complexity.

![Figure 1](figure:1)

LMN generalizes this idea to networks with *any* **activation function** (the internal switching mechanism that determines how each neuron responds to its inputs), not just ReLU. The trick: pick two input samples and draw a straight line between them, then watch what happens to that line after it passes through the network. If it stays straight, both samples are processed by the same internal rule. If it curves, they're not.

The team defines a **linear connectivity matrix** L where each entry L_ij captures how "straight" the path between samples i and j remains. They then compute the eigenvalue spectrum of L, treat it as a probability distribution, and apply **Von Neumann entropy** (borrowed from quantum information theory) to count how many effectively distinct linear mappings the matrix encodes. That count is the LMN.

In practice, three steps:

1. For each pair of input samples, interpolate a path in input space and measure how curved the output path is (via R² of linear regression).
2. Stack all pairwise measurements into the N×N matrix L.
3. Compute the eigenvalue spectrum of L, treat it as a probability distribution, and exponentiate the entropy to get LMN.

## Why It Matters

The researchers tested LMN on three classic algorithmic tasks where grokking is known to occur: modular addition (clock arithmetic), the permutation group S5 (symmetry operations on five elements), and multi-digit XOR.

After a network finishes memorizing but before it generalizes, LMN drops steadily, and it drops in a straight line with the test loss. The network is literally becoming simpler, computation by computation, as it discovers the underlying rule. L2 norm shows a correlation too, but a messy, nonlinear one.

![Figure 2](figure:2)

The XOR experiment turned up something unexpected. After grokking, instead of leveling off at a stable low value, LMN showed a *double-descent*: dropping, rising, then dropping again. XOR admits two different generalization algorithms of nearly equal efficiency, and the network oscillates between them. LMN made this invisible phenomenon visible. L2 norm showed nothing.

Beyond grokking, the authors argue that LMN is a candidate for a neural network analogue of **Kolmogorov complexity**, the theoretical minimum description length of a computational object. Kolmogorov complexity is uncomputable in general. LMN offers a practical approximation that counts how many distinct linear computations a network actually uses, aligning with how modern neural networks operate.

The connection to physics runs deeper than the institutional affiliation. Tegmark and collaborators have long argued that the universe's laws are compressible, that deep regularities exist waiting to be discovered. A metric that measures how efficiently a network compresses its knowledge maps onto the same questions physicists ask about how nature represents information. If grokking is compression, measuring it precisely is a step toward understanding why neural networks generalize at all.

> **Bottom Line:** LMN provides the first complexity metric that tracks neural network generalization cleanly and linearly, revealing that grokking is compression and pointing toward a practical, physically interpretable version of Kolmogorov complexity for modern AI.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work applies Von Neumann entropy, a concept from quantum information theory, to characterize neural network complexity. It's a clean example of what IAIFI does best: moving ideas between physics and AI.

- **Impact on Artificial Intelligence:** LMN provides a new, interpretable complexity measure that outperforms the widely-used L2 norm for tracking generalization dynamics, with potential applications to regularization and model selection beyond grokking.

- **Impact on Fundamental Interactions:** By connecting neural network compression to Kolmogorov complexity, this work reinforces the idea that learning is fundamentally about information compression, tying machine intelligence back to core principles of information theory.

- **Outlook and References:** Future work may extend LMN to larger transformer architectures and use it as a training signal for improving generalization. The paper is available as [arXiv:2310.05918](https://arxiv.org/abs/2310.05918).

## Original Paper Details
- **Title:** Grokking as Compression: A Nonlinear Complexity Perspective
- **arXiv ID:** [2310.05918](https://arxiv.org/abs/2310.05918)
- **Authors:** Ziming Liu, Ziqian Zhong, Max Tegmark
- **Abstract:** We attribute grokking, the phenomenon where generalization is much delayed after memorization, to compression. To do so, we define linear mapping number (LMN) to measure network complexity, which is a generalized version of linear region number for ReLU networks. LMN can nicely characterize neural network compression before generalization. Although the $L_2$ norm has been a popular choice for characterizing model complexity, we argue in favor of LMN for a number of reasons: (1) LMN can be naturally interpreted as information/computation, while $L_2$ cannot. (2) In the compression phase, LMN has linear relations with test losses, while $L_2$ is correlated with test losses in a complicated nonlinear way. (3) LMN also reveals an intriguing phenomenon of the XOR network switching between two generalization solutions, while $L_2$ does not. Besides explaining grokking, we argue that LMN is a promising candidate as the neural network version of the Kolmogorov complexity since it explicitly considers local or conditioned linear computations aligned with the nature of modern artificial neural networks.
