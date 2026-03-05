---
abstract: 'When training large-scale models, the performance typically scales with
  the number of parameters and the dataset size according to a slow power law. A fundamental
  theoretical and practical question is whether comparable performance can be achieved
  with significantly smaller models and substantially less data. In this work, we
  provide a positive and constructive answer. We prove that a generic permutation-invariant
  function of $d$ objects can be asymptotically compressed into a function of $\operatorname{polylog}
  d$ objects with vanishing error, which is proved to be the optimal compression rate.
  This theorem yields two key implications: (Ia) a large neural network can be compressed
  to polylogarithmic width while preserving its learning dynamics; (Ib) a large dataset
  can be compressed to polylogarithmic size while leaving the loss landscape of the
  corresponding model unchanged. Implication (Ia) directly establishes a proof of
  the dynamical lottery ticket hypothesis, which states that any ordinary network
  can be strongly compressed such that the learning dynamics and result remain unchanged.
  (Ib) shows that a neural scaling law of the form $L\sim d^{-α}$ can be boosted to
  an arbitrarily fast power law decay, and ultimately to $\exp(-α'' \sqrt[m]{d})$.'
arxivId: '2510.00504'
arxivUrl: https://arxiv.org/abs/2510.00504
authors:
- Hong-Yi Wang
- Di Luo
- Tomaso Poggio
- Isaac L. Chuang
- Liu Ziyin
concepts:
- symmetry preservation
- lottery ticket hypothesis
- polylogarithmic compression
- neural scaling laws
- scalability
- sparse models
- dimensionality reduction
- group theory
- loss function design
- attention mechanisms
figures:
- /iaifi-research-blog/figures/2510_00504/figure_1.png
- /iaifi-research-blog/figures/2510_00504/figure_2.png
- /iaifi-research-blog/figures/2510_00504/figure_3.png
pdfUrl: https://arxiv.org/pdf/2510.00504v2
published: '2025-10-01T04:35:23+00:00'
theme: Foundational AI
title: A universal compression theory for lottery ticket hypothesis and neural scaling
  laws
wordCount: 1138
---

## The Big Picture

Imagine learning to recognize cats. You don't need ten million examples — a few dozen will do. Yet today's largest AI language models train on roughly a trillion words to reach human-level fluency, while a child masters language after hearing perhaps a hundred million words by age ten. That's a ten-thousand-fold efficiency gap. Something fundamental is being wasted.

That waste shows up in **neural scaling laws** — the observed pattern that AI performance improves only as a slow, diminishing-returns curve as you add more data or computing power. To halve a language model's error, you typically need to multiply your dataset tenfold or more. It's a brutal tax on compute and energy, and until now no one had a principled explanation for whether it could be escaped.

A team from Princeton, MIT, Tsinghua, and UCLA now offers a mathematical proof that it can. Their theorem shows that any well-behaved function of d objects — data points or neurons — can be compressed to use only a tiny, slowly-growing fraction of those objects with negligible error. This simultaneously proves the **lottery ticket hypothesis** — the idea that large AI models secretly contain much smaller models that work just as well — and shows that the slow improvement rates governing AI training can be dramatically accelerated.

> **Key Insight:** The hidden symmetry in both neural networks and datasets means that most of their content is mathematically redundant — and this redundancy can be provably eliminated, shrinking a trillion-element system down to perhaps a million elements without changing what it computes.

## How It Works

The entire argument rests on one observation: **permutation symmetry** — the property that swapping any two elements leaves the result unchanged. When you measure how wrong a model is, you sum a penalty over every training example. Shuffle the data in any order and the total stays the same: the examples are interchangeable. Inside a neural network layer, swapping any two neurons (along with their weights) leaves the output identical.

![Figure 1](/iaifi-research-blog/figures/2510_00504/figure_1.png)

This symmetry unlocks compression. Any permutation-symmetric function has a **"deep set" representation**: each input passes through the same feature detector, all results are summed, then a final function reads out the answer — written compactly as h(Σ g(wᵢ)). Under this structure, the researchers prove a striking result: when d objects live in an m-dimensional space and the function is smooth, those objects inevitably **crowd together** as d grows large.

Dense clusters mean redundancy. You can prune redundant elements and the error shrinks to zero. The compression is constructive:

1. **Identify crowding**: As d → ∞, objects pack into a fixed bounded region, forming clusters by a pigeonhole argument.
2. **Select representatives**: Use a geometric covering to pick O(polylog d) representatives approximating every cluster.
3. **Reweight**: Assign each representative a weight proportional to its cluster size, preserving the function's value.
4. **Bound the error**: Because h and g are Taylor-expandable, error decays as exp(−α′ · d^(1/m)) — faster than any power law.

The team proves this compression rate is optimal.

## Why It Matters

**The dynamical lottery ticket hypothesis.** The original lottery ticket hypothesis (Frankle & Carlin, 2019) proposed that large networks contain small "winning ticket" subnetworks trainable in isolation to similar accuracy. The dynamical version is stronger: can you find a subnetwork that not only reaches the same final accuracy but follows the same *training trajectory* throughout?

The compression theorem says yes. A neural network's forward pass is permutation-symmetric in its neurons, so the theorem directly implies any network of width d can be compressed to width O(polylog d) — roughly, a trillion-neuron layer replaced by a few-million-neuron layer — with identical learning dynamics, not just identical final performance.

![Figure 2](/iaifi-research-blog/figures/2510_00504/figure_2.png)

**Turbocharging scaling laws.** Since the training loss is also permutation-symmetric in the data points, the same compression applies there: a dataset of d examples can be pruned to O(polylog d) **coreset** examples — a carefully reweighted subset that preserves the full shape of the loss landscape.

This doesn't just shift the scaling exponent — it changes the functional form entirely. A standard scaling law L ∝ d^(−α) becomes, after compression, L ∝ exp(−α′ · d^(1/m)). Exponential beats polynomial by an infinite margin. Numerically, the researchers confirm concrete gains: tasks that required millions of examples now converge with far fewer, losses dropping far faster than any power law predicts.

![Figure 3](/iaifi-research-blog/figures/2510_00504/figure_3.png)

The AI field has largely accepted power-law scaling as a fact of life, planning exaflop training runs and petabyte datasets accordingly. This work suggests that acceptance was premature — the slow power law reflects not a fundamental limit of learning, but a failure to exploit mathematical structure already present in every dataset and every network.

For physics-inspired AI, the result resonates deeply. Permutation symmetry is a physicist's bread and butter: it underlies Bose-Einstein statistics, identical-particle indistinguishability, and the symmetry principles organizing the Standard Model. The authors' framework — compressing symmetric functions by exploiting redundancy — is essentially the same logic physicists use when reducing a many-body problem to its irreducible representations. The bridge between statistical learning theory and symmetry-based physics runs both ways.

Open questions remain. The smoothness assumption formally excludes ReLU networks, though numerical experiments suggest the conclusions hold regardless. Extending the theory to non-smooth architectures, attention mechanisms, and finite (rather than asymptotic) d are natural next steps. Translating the theoretical coreset construction into a practical training algorithm — one that achieves exponential scaling on real benchmarks — is the grand challenge ahead.

> **Bottom Line:** By proving that permutation symmetry makes both neural networks and datasets compressible to polylogarithmic size, this work establishes the dynamical lottery ticket hypothesis and shows that the slow power laws governing AI scaling are not fundamental limits — they're an efficiency gap waiting to be closed.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work translates a physicist's intuition about symmetry and redundancy into a rigorous mathematical theory of neural network compression, demonstrating that the permutation symmetries omnipresent in both physics and machine learning are the key to dramatically improving data efficiency.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper provides the first proof of the dynamical lottery ticket hypothesis and a constructive theorem showing that neural scaling laws can be transformed from slow power-law decay into exponential decay, with direct implications for reducing the compute and data costs of training large models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The compression framework applies symmetry-reduction principles — familiar from the physics of identical particles and group theory — to neural network learning dynamics, forging a new mathematical connection between statistical physics and deep learning theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend the theory to non-smooth architectures and develop practical coreset-construction algorithms that realize exponential scaling on real-world benchmarks; the paper appears at ICLR 2026 (see arXiv for the full version with proofs).</span></div></div>
</div>
