---
abstract: We explore unique considerations involved in fitting ML models to data with
  very high precision, as is often required for science applications. We empirically
  compare various function approximation methods and study how they scale with increasing
  parameters and data. We find that neural networks can often outperform classical
  approximation methods on high-dimensional examples, by auto-discovering and exploiting
  modular structures therein. However, neural networks trained with common optimizers
  are less powerful for low-dimensional cases, which motivates us to study the unique
  properties of neural network loss landscapes and the corresponding optimization
  challenges that arise in the high precision regime. To address the optimization
  issue in low dimensions, we develop training tricks which enable us to train neural
  networks to extremely low loss, close to the limits allowed by numerical precision.
arxivId: '2210.13447'
arxivUrl: https://arxiv.org/abs/2210.13447
authors:
- Eric J. Michaud
- Ziming Liu
- Max Tegmark
concepts:
- precision machine learning
- regression
- scalability
- loss function design
- modular structure discovery
- loss landscape geometry
- interpretability
- inverse problems
- sparse models
- surrogate modeling
- kernel methods
figures:
- /iaifi-research-blog/figures/2210_13447/figure_1.png
- /iaifi-research-blog/figures/2210_13447/figure_1.png
- /iaifi-research-blog/figures/2210_13447/figure_2.png
- /iaifi-research-blog/figures/2210_13447/figure_2.png
- /iaifi-research-blog/figures/2210_13447/figure_3.png
- /iaifi-research-blog/figures/2210_13447/figure_3.png
pdfUrl: https://arxiv.org/pdf/2210.13447v1
published: '2022-10-24T17:58:30+00:00'
theme: Foundational AI
title: Precision Machine Learning
wordCount: 1040
---

## The Big Picture

Imagine measuring the width of a human hair with a ruler designed for buildings. That's roughly the problem facing scientists who want to use machine learning for precision science — standard ML tools were never built to be precise enough. A chatbot doesn't need to know the next-word probability to seven decimal places. But a physicist trying to rediscover the laws of nature from data? They need to get things *exactly* right.

This is the world of **Precision Machine Learning (PML)** — where researchers ask not whether a neural network can learn a mathematical pattern, but whether it can do so with errors smaller than one part in a trillion. In science, a tiny difference in how wrong the model is can mean the difference between finding the exact formula and missing it entirely. Standard training methods, optimized for vision and language tasks, can fail spectacularly at this level of scrutiny.

Researchers at MIT's IAIFI set out to understand exactly *why* precision is hard, compare every major function-fitting method head-to-head, and develop new training techniques that push neural networks to the very edge of what computers can numerically represent.

> **Key Insight:** Neural networks auto-discover hidden modular structure in high-dimensional scientific functions, letting them outperform classical methods — but standard optimizers fall short in low dimensions, a fixable problem that requires rethinking how we train.

## How It Works

The team framed precision ML as a regression problem: given data from symbolic formulas drawn from the **Feynman Lectures on Physics**, how precisely can different methods recover the underlying function? These equations — covering everything from ideal gas laws to relativistic energy — make perfect test cases because they have no noise, possess genuine mathematical structure, and span a wide range of input dimensions.

![Figure 1](/iaifi-research-blog/figures/2210_13447/figure_1.png)

The researchers decomposed total error into four components: **optimization error** (how far the optimizer is from its best), **sampling luck** (statistical fluctuations), **generalization gap** (train vs. test performance), and **architecture error** (the best a given model type can ever achieve). In the high-precision regime, architecture error and optimization error dominate — the usual concerns about overfitting become secondary.

To compare architectures fairly, they tracked how error shrinks as parameters increase. The key metric is the **scaling exponent** *α*, where loss ∝ N^(−α) — a higher α means faster precision gains per parameter added:

- **Piecewise polynomial methods** (splines) have theoretically grounded scaling but degrade badly as dimension grows
- **Chebyshev polynomials and Fourier series** achieve high precision but only for smooth, low-dimensional functions
- **Neural networks with standard activations** (ReLU, tanh) scale better in higher dimensions by exploiting **computational modularity** — when a function is built from composable sub-parts like `sin(x + y²)`, networks learn each piece separately

![Figure 2](/iaifi-research-blog/figures/2210_13447/figure_1.png)

This modularity insight is central. Feynman equations are hierarchically structured — nested additions, multiplications, and simple nonlinearities. Neural networks spontaneously discover these building blocks and represent them efficiently, outperforming classical methods on 5- or 10-dimensional functions even at equal parameter counts.

But here's the catch. In *low-dimensional* cases, classical methods beat neural networks — not because of architecture limits, but because of **optimization failure**. The error landscapes in the high-precision regime are littered with flat regions, saddle points, and narrow valleys that standard gradient descent cannot navigate. The optimizer stalls before reaching the global minimum, even when that minimum theoretically exists.

![Figure 3](/iaifi-research-blog/figures/2210_13447/figure_2.png)

To fix this, the team developed targeted training techniques: aggressive **learning rate scheduling** (starting large and gradually shrinking), **second-order optimization** (using curvature information to navigate more intelligently than plain gradient descent), and precision-tuned **weight initialization**. They also found that cycling between optimizers at different training stages — a kind of optimizer annealing — helped escape local traps.

With these methods, they trained networks to relative RMSE losses of 10^(−14) and below, approaching the 10^(−16) floor imposed by 64-bit floating-point arithmetic — the hard limit of how precisely modern computers store numbers.

![Figure 4](/iaifi-research-blog/figures/2210_13447/figure_2.png)

## Why It Matters

The implications extend well beyond benchmarking. **Symbolic regression** — discovering exact mathematical formulas from data — is one of the most exciting frontiers in AI for science. Tools like PySR and Eureqa propose candidate formulas, but they depend on neural network components fitting intermediate representations with high fidelity. Imprecise function approximation breaks the symbolic discovery pipeline. Precision ML is the missing ingredient.

More broadly, this work exposes a gap in how the ML community thinks about optimization. Decades of research have been driven by tasks where error of 0.1 is acceptable and 0.01 is excellent. Adam, SGD with momentum, cosine schedules — these tools were never built for the high-precision game. The finding that standard training fails not due to architecture limits but due to *optimizer limits* is a call to action: as ML moves deeper into scientific applications, the field needs optimization methods designed for precision from the ground up.

![Figure 5](/iaifi-research-blog/figures/2210_13447/figure_3.png)

The work also raises an intriguing question: if neural networks are auto-discovering modular structure in high dimensions, can we *read out* that structure? Could precision training become a tool for scientific interpretability — not just fitting functions, but revealing their compositional anatomy?

![Figure 6](/iaifi-research-blog/figures/2210_13447/figure_3.png)

> **Bottom Line:** By pushing neural networks to the limits of floating-point precision, this work shows that the bottleneck in scientific ML is often the optimizer, not the architecture — and that fixing it unlocks a path toward discovering exact scientific laws from data.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges AI methodology and physics practice directly, using the Feynman Lectures as a benchmark to expose and fix fundamental limitations in how neural networks handle scientific data requiring ultra-high precision.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces a new training framework — optimizer annealing and precision-targeted scheduling — that enables neural networks to reach losses within an order of magnitude of the 64-bit floating-point floor, far beyond what standard training achieves.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By demonstrating that neural networks auto-discover modular structure in physics equations, the work lays groundwork for data-driven symbolic regression capable of recovering exact physical laws from experimental observations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend these techniques to noisy experimental data and multi-output scientific models; the full paper is available at arXiv:2210.13447.</span></div></div>
</div>
