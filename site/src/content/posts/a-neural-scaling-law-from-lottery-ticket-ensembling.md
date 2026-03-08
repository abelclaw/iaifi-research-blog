---
abstract: 'Neural scaling laws (NSL) refer to the phenomenon where model performance
  improves with scale. Sharma & Kaplan analyzed NSL using approximation theory and
  predict that MSE losses decay as $N^{-α}$, $α=4/d$, where $N$ is the number of model
  parameters, and $d$ is the intrinsic input dimension. Although their theory works
  well for some cases (e.g., ReLU networks), we surprisingly find that a simple 1D
  problem $y=x^2$ manifests a different scaling law ($α=1$) from their predictions
  ($α=4$). We opened the neural networks and found that the new scaling law originates
  from lottery ticket ensembling: a wider network on average has more "lottery tickets",
  which are ensembled to reduce the variance of outputs. We support the ensembling
  mechanism by mechanistically interpreting single neural networks, as well as studying
  them statistically. We attribute the $N^{-1}$ scaling law to the "central limit
  theorem" of lottery tickets. Finally, we discuss its potential implications for
  large language models and statistical physics-type theories of learning.'
arxivId: '2310.02258'
arxivUrl: https://arxiv.org/abs/2310.02258
authors:
- Ziming Liu
- Max Tegmark
concepts:
- neural scaling laws
- lottery ticket ensembling
- ensemble methods
- variance reduction
- interpretability
- scalability
- sparse models
- stochastic processes
- regression
- phase transitions
figures:
- /iaifi-research-blog/figures/2310_02258/figure_1.png
- /iaifi-research-blog/figures/2310_02258/figure_1.png
- /iaifi-research-blog/figures/2310_02258/figure_2.png
- /iaifi-research-blog/figures/2310_02258/figure_2.png
- /iaifi-research-blog/figures/2310_02258/figure_3.png
- /iaifi-research-blog/figures/2310_02258/figure_3.png
pdfUrl: https://arxiv.org/pdf/2310.02258v2
published: '2023-10-03T17:58:33+00:00'
theme: Foundational AI
title: A Neural Scaling Law from Lottery Ticket Ensembling
wordCount: 1037
---

## The Big Picture

Every time AI researchers train a larger model, something almost magical happens: the model gets better at its task, following a precise mathematical law. Double the number of **parameters** — the adjustable numerical settings inside a neural network — and prediction error drops by a predictable amount. These **neural scaling laws** have become one of the most important empirical facts in modern AI, driving billion-dollar investments in ever-larger models. But we still don't fully understand *why* they hold.

The standard explanation, developed by Sharma and Kaplan, treats neural networks as tools for fitting mathematical patterns to data. Pack in more parameters, and you can describe that data with finer precision — like drawing a smoother curve through a cloud of points. The math predicts that prediction error should shrink as N^(-4/d), where N is the number of parameters and d reflects how many variables describe a typical data point. Clean. Elegant. And sometimes completely wrong.

MIT physicists Ziming Liu and Max Tegmark stumbled onto this problem while studying something almost embarrassingly simple: training a neural network to learn y = x². Their results revealed a hidden mechanism behind scaling laws — one that has nothing to do with fitting functions to data and everything to do with what happens when lucky sub-networks work together.

> **Key Insight:** When neural networks scale up, they don't just get better at approximating functions — they accumulate more "lottery ticket" sub-networks that pool their estimates, and the resulting variance reduction follows the same statistics as averaging coin flips.

## How It Works

The experimental setup is deliberately stripped-down. Liu and Tegmark trained two-layer networks with a single hidden layer of width N to fit y = x² on the interval [-2, 2], testing two common activation functions:

- **ReLU** — a piecewise-linear function that outputs zero for negative inputs and passes positive values through unchanged
- **SiLU** — a smoother variant with curved transitions, increasingly popular in modern architectures

Across 1,000 random starting configurations per width, they recorded the median prediction error.

![Figure 1](/iaifi-research-blog/figures/2310_02258/figure_1.png)

Standard fitting theory predicts loss should decay as N^(-4) for ReLU networks — since d=1 in this one-dimensional problem, the exponent α = 4/d = 4. For small N, ReLU networks obey this law. But as networks grow wider, the scaling slows dramatically, eventually settling near N^(-1). For SiLU networks, the N^(-1) slope holds from the very start, skipping the N^(-4) phase entirely. Something other than fitting precision is driving performance at scale.

To understand why, the researchers did something increasingly rare in deep learning: they opened the networks and looked inside. Examining an extremely wide network (N=10,000 SiLU neurons), they found a striking pattern in the learned weights and biases: **symmetric neurons** — pairs that are exact mirror images of each other. For nearly every neuron with parameters (w, b), a corresponding neuron existed with parameters (-w, b). This symmetry guarantees the network represents an even function, which is exactly what y = x² is.

![Figure 2](/iaifi-research-blog/figures/2310_02258/figure_1.png)

Next, they trained 1,000 tiny networks with just N=2 neurons. Instead of a smooth spread of outcomes, the results showed discrete peaks — evidence that small networks converge to only a handful of distinct internal "algorithms." The lowest-loss peak corresponded to networks that found the symmetric neuron configuration.

Liu and Tegmark called these successful configurations **lottery tickets**: sub-networks that can solve the problem well on their own. As a network grows wider, it contains proportionally more lottery tickets (n ∝ N). Each produces an independent estimate of the true function, and the network's output is effectively an average over all of them. This is **lottery ticket ensembling** — not a designed strategy, but an emergent behavior that falls out of training.

Elementary statistics then takes over: average n independent estimates of the same quantity, and variance shrinks as 1/n. Since n grows with N, the loss shrinks as N^(-1). This is the **central limit theorem** — the principle explaining why averaging many independent estimates always converges toward the truth — now operating inside neural networks.

## Why It Matters

This work identifies a regime where the standard function-fitting explanation for scaling laws breaks down. The ReLU results are particularly telling: fitting theory governs early scaling, but the mechanism switches at larger widths. If large language models operate in a similar regime, the N^(-4/d) predictions may get the scaling exponent entirely wrong — either underestimating the gains from further scale, or missing the dominant effect altogether.

![Figure 3](/iaifi-research-blog/figures/2310_02258/figure_2.png)

The statistical-physics framing opens a deeper conceptual door. The central limit theorem is one of the most universal results in mathematics — it describes why averages of random things converge, regardless of the specific distribution. Finding it lurking inside neural scaling laws hints at something profound: macroscopic scaling laws may emerge from the collective statistics of microscopic computational sub-structures, much as temperature and pressure emerge from the collective behavior of individual molecules.

The theory still needs refinement — the authors say as much. But the empirical scaffolding is solid, and the conceptual picture is compelling enough to pursue seriously.

> **Bottom Line:** A surprisingly simple experiment — teaching a neural network to square a number — revealed that "bigger networks work better" sometimes has nothing to do with better approximation and everything to do with averaging over lucky sub-networks. The central limit theorem, not function approximation, may govern scaling in many practical regimes.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly applies statistical physics reasoning — ensemble averaging and the central limit theorem — to explain a fundamental empirical pattern in deep learning, exemplifying IAIFI's mission to unify physics and AI.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper identifies a new mechanism for neural scaling laws that operates independently of approximation theory, challenging prevailing models for why larger networks consistently outperform smaller ones.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By treating neural networks as physical systems where macroscopic laws emerge from microscopic statistics, this work contributes to statistical physics-style theories of learning and complexity.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will test whether lottery ticket ensembling governs scaling in large language models and other high-dimensional settings; the paper is available at arXiv (Liu & Tegmark, MIT/IAIFI).</span></div></div>
</div>
