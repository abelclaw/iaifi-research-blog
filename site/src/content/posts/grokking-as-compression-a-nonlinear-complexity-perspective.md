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
wordCount: 1095
---

## The Big Picture

Imagine teaching a child long division. For weeks, they memorize dozens of example problems by rote — matching inputs to outputs without grasping the underlying rule. Then one day, something clicks. They don't just know the answers anymore; they *understand division*. That moment of insight, delayed long after the initial memorization, is exactly what researchers call **grokking** in neural networks.

Since the phenomenon was first documented in 2022, AI researchers have been puzzled by it. A neural network trains on a small dataset, quickly achieving perfect accuracy on training examples — but fails completely on new data. Training continues. Nothing seems to happen. Then, thousands of steps later, the network suddenly generalizes: it starts getting the right answer on examples it has never seen before. What was it doing during all that seemingly wasted time?

A new paper from MIT and IAIFI researchers Ziming Liu, Ziqian Zhong, and Max Tegmark proposes a compelling answer: the network was *compressing*. And to prove it, they invented a new way to measure how complicated a neural network actually is — one that makes physical sense.

> **Key Insight:** Grokking happens because neural networks first find a complex, bloated memorization solution, then slowly compress toward a simpler, more elegant generalization solution — and a new metric called the Linear Mapping Number (LMN) tracks this compression precisely.

## How It Works

The standard tool for measuring neural network complexity has been the **L2 norm** — the total "weight" of a model's internal connections, calculated as the sum of their squared values. The intuition: smaller weights mean a simpler model. But the MIT team argues this is a poor proxy. A deep network can have enormous weights while computing only a single simple function. What matters isn't how large the numbers are — it's how many *distinct computations* the network performs.

Their alternative, **Linear Mapping Number (LMN)**, builds on a geometric insight. A **ReLU network** — a standard neural network architecture whose internal switches activate only when their input exceeds zero — doesn't compute one smooth function. It carves up the space of possible inputs into regions, behaving like a completely different linear function within each one.

Think of it like origami: you fold a flat sheet repeatedly and end up with a complex 3D shape. The number of flat facets is the number of linear regions — a direct measure of complexity.

![Figure 1](/iaifi-research-blog/figures/2310_05918/figure_1.png)

LMN generalizes this idea to networks with *any* **activation function** — the internal switching mechanism that determines how each neuron responds to its inputs, not just ReLU. The key trick: pick two input samples and draw a straight line between them, then watch what happens to that line after it passes through the network. If it stays straight, both samples are processed by the same internal rule. If it curves, they're not. The team defines a **linear connectivity matrix** L where each entry L_ij captures how "straight" the path between samples i and j remains.

Then they apply **Von Neumann entropy** — borrowed from quantum physics, it quantifies how spread out or concentrated information is across a system — to count how many effectively distinct linear mappings the matrix implies. That count is the LMN.

The computation breaks down into three steps:

1. For each pair of input samples, interpolate a path in input space and measure how curved the output path is (via R² of linear regression).
2. Stack all pairwise measurements into the N×N matrix L.
3. Compute the eigenvalue spectrum of L — its mathematical fingerprint — treat it as a probability distribution, and exponentiate the Shannon entropy (a classical measure of information spread) to get LMN.

## Why It Matters

The researchers tested LMN on three classic algorithmic tasks where grokking is known to occur: modular addition (clock arithmetic), the permutation group S5 (symmetry operations on five elements), and multi-digit XOR. The results were striking.

After a network finishes memorizing but before it generalizes, LMN drops steadily — and it drops in a straight line with the test loss, the standard measure of how wrong the network's predictions are on new data. The network is literally becoming simpler, computation by computation, as it discovers the underlying rule. L2 norm shows a correlation too, but a messy, nonlinear one that's hard to interpret.

![Figure 2](/iaifi-research-blog/figures/2310_05918/figure_1.png)

The XOR experiment revealed something unexpected. After grokking, instead of leveling off at a stable low value, LMN showed a *double-descent* — dropping, rising, then dropping again. The explanation: XOR admits two different generalization algorithms of nearly equal efficiency. The network oscillates between them. LMN made this invisible phenomenon visible. L2 norm showed nothing unusual at all.

This opens a larger door. The authors argue that LMN is a candidate for the **neural network version of Kolmogorov complexity** — the theoretical minimum description length of a computational object, a foundational concept in information theory. Kolmogorov complexity is notoriously uncomputable in general. LMN offers a practical, architecture-aware approximation: it counts how many distinct linear computations a network actually uses, aligning naturally with how modern AI systems operate.

The connection to physics at IAIFI is more than institutional. Tegmark and collaborators have long argued that the universe's laws are compressible — that deep regularities exist waiting to be discovered. A metric that measures how efficiently a network has compressed its knowledge maps directly onto questions about how physical systems represent information. If grokking is compression, and compression is what intelligence looks like, then understanding grokking quantitatively brings us closer to understanding intelligence itself.

> **Bottom Line:** LMN provides the first complexity metric that tracks neural network generalization cleanly and linearly, revealing that grokking is compression — and pointing toward a practical, physically interpretable version of Kolmogorov complexity for modern AI.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies Von Neumann entropy — a concept from quantum information theory — to characterize neural network complexity, exemplifying IAIFI's mission of transplanting ideas between physics and AI.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">LMN provides a new, interpretable complexity measure that outperforms the widely-used L2 norm for understanding generalization dynamics, with potential applications to regularization and model analysis beyond grokking.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By connecting neural network compression to Kolmogorov complexity, this work advances a physics-inspired view of learning as information compression, linking machine intelligence to fundamental principles of information theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may apply LMN to larger transformer architectures and use it as a training signal for improving generalization; the paper is available on arXiv as a preprint under review.</span></div></div>
</div>
