---
abstract: Sparse Bayesian learning (SBL) is a powerful framework for tackling the
  sparse coding problem while also providing uncertainty quantification. The most
  popular inference algorithms for SBL exhibit prohibitively large computational costs
  for high-dimensional problems due to the need to maintain a large covariance matrix.
  To resolve this issue, we introduce a new method for accelerating SBL inference
  -- named covariance-free expectation maximization (CoFEM) -- that avoids explicit
  computation of the covariance matrix. CoFEM solves multiple linear systems to obtain
  unbiased estimates of the posterior statistics needed by SBL. This is accomplished
  by exploiting innovations from numerical linear algebra such as preconditioned conjugate
  gradient and a little-known diagonal estimation rule. For a large class of compressed
  sensing matrices, we provide theoretical justifications for why our method scales
  well in high-dimensional settings. Through simulations, we show that CoFEM can be
  up to thousands of times faster than existing baselines without sacrificing coding
  accuracy. Through applications to calcium imaging deconvolution and multi-contrast
  MRI reconstruction, we show that CoFEM enables SBL to tractably tackle high-dimensional
  sparse coding problems of practical interest.
arxivId: '2105.10439'
arxivUrl: https://arxiv.org/abs/2105.10439
authors:
- Alexander Lin
- Andrew H. Song
- Berkin Bilgic
- Demba Ba
concepts:
- bayesian inference
- covariance-free em
- sparse models
- uncertainty quantification
- posterior estimation
- scalability
- preconditioned conjugate gradient
- diagonal estimation
- inverse problems
- multi-task learning
figures:
- /iaifi-research-blog/figures/2105_10439/figure_1.png
- /iaifi-research-blog/figures/2105_10439/figure_1.png
- /iaifi-research-blog/figures/2105_10439/figure_2.png
pdfUrl: https://arxiv.org/pdf/2105.10439v2
published: '2021-05-21T16:20:07+00:00'
theme: Foundational AI
title: Covariance-Free Sparse Bayesian Learning
wordCount: 952
---

## The Big Picture

Imagine tracking a needle in a million-piece haystack — not just locating it, but quantifying exactly how uncertain you are about its position. That's the challenge facing scientists who use **sparse Bayesian learning (SBL)**: a technique for reconstructing a complete signal from incomplete, noisy data while rigorously accounting for uncertainty.

SBL appears across neuroscience and imaging, from reconstructing brain activity in MRI to inferring neural firing from calcium imaging to estimating radio signal directions. Its advantage over methods like LASSO is that it doesn't just return a single answer. It returns a full probability distribution over all possible answers. That honest accounting of uncertainty matters for downstream decisions.

The problem? SBL has a computational bottleneck baked into its core. Every update step requires working with a **covariance matrix**, a grid tracking how every unknown in your signal relates to every other. For *D* unknowns, this grid has *D²* entries and requires *O(D³)* operations to manipulate. Double the problem size, and computation becomes eight times slower. At real-world scales, a brain scan with tens of thousands of voxels, SBL grinds to a halt.

A team from Harvard and MIT built a fix: **CoFEM**.

> **Key Insight:** CoFEM eliminates the covariance matrix bottleneck entirely by *estimating* the statistics SBL needs via randomized numerical methods, achieving the same accuracy as full-covariance SBL while running up to thousands of times faster.

## How It Works

Standard SBL uses an **expectation-maximization (EM) algorithm**: a two-step cycle alternating between estimating the signal given current model parameters (the E-step) and updating those parameters (the M-step). The E-step is the bottleneck. It requires forming and inverting a *D × D* covariance matrix. At *D* = 10,000, that's 100 million entries. At *D* = 100,000, it's effectively impossible.

CoFEM's core insight: you don't need the whole matrix. You only need two quantities from it, the **posterior mean** (your best single-point estimate of the signal) and the **diagonal of the covariance** (a compact list of per-unknown uncertainties). Both can be estimated without ever constructing the full matrix.

Here's how:

1. **Solve linear systems instead of inverting matrices.** Rather than directly computing Σ = (Φᵀβ Φ + diag{α})⁻¹, CoFEM sets up *K* linear systems, each with a randomly drawn right-hand side, and solves them using **preconditioned conjugate gradient (CG)**. This iterative solver requires only matrix-vector products, never the full matrix.

2. **Estimate the diagonal via the Rademacher trick.** The **Rademacher diagonal estimator** works by averaging the outputs of random "probe" vectors fired through the system, yielding an unbiased estimate of the diagonal of the inverse covariance. CoFEM replaces an *O(D²)* impossibility with a statistical estimate that converges reliably.

3. **Parallelize across GPUs.** The *K* linear systems are independent, so they run simultaneously on GPU hardware. Most SBL competitors can't exploit this due to memory constraints.

![Figure 1](/iaifi-research-blog/figures/2105_10439/figure_1.png)

Per-iteration cost drops from *O(D³)* to *O(UKτD)*, where *τD* is one matrix-vector multiply and *U, K* are small fixed hyperparameters. Memory drops from *O(D²)* to *O(DK)*. For measurement matrices satisfying the **restricted isometry property (RIP)**, a standard condition in compressed sensing ensuring measurements capture the signal broadly, the authors prove *U* and *K* can stay fixed as *D* grows. More unknowns doesn't mean more probes.

![Figure 2](/iaifi-research-blog/figures/2105_10439/figure_1.png)

In simulations, CoFEM matches standard EM on sparse signal recovery while cutting runtime by hundreds to thousands of times. With GPU acceleration, computation that previously took hours shrinks to seconds.

## Why It Matters

SBL's ability to quantify uncertainty has always set it apart from LASSO and ℓ₁-regularized compressed sensing. But that ability was locked behind a computational wall for any problem at scale. CoFEM removes that wall.

![Figure 3](/iaifi-research-blog/figures/2105_10439/figure_2.png)

The paper tests this on two real applications. In **calcium imaging deconvolution**, where the goal is to infer neural spiking activity from fluorescence traces, CoFEM-equipped SBL recovers firing patterns with competitive accuracy while delivering the uncertainty estimates that purely deterministic methods cannot. In **multi-contrast MRI reconstruction**, the goal is to simultaneously reconstruct multiple tissue-contrast images from undersampled k-space data. CoFEM handles the enormous dimensionality of volumetric brain scans in practical compute times.

Both extensions (multi-task learning across MRI contrasts, non-negativity constraints for calcium signals) slot cleanly into the CoFEM framework, showing its flexibility beyond the baseline setting.


There's a broader template here. Many Bayesian methods remain confined to low-dimensional settings because their inference costs scale catastrophically. CoFEM shows a path forward: identify what you *actually* need from an expensive intermediate object, then estimate it cheaply using randomized numerical linear algebra. The same approach could extend to other scientific domains where uncertainty quantification matters but computational cost has been prohibitive.

> **Bottom Line:** CoFEM makes Sparse Bayesian Learning fast enough for high-dimensional real-world problems by replacing explicit covariance matrix inversion with randomized linear solvers, achieving thousands-fold speedups with no accuracy loss and opening the door to principled uncertainty quantification at scale.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects Bayesian statistics, numerical linear algebra, and signal processing, delivering a method applicable to scientific imaging (from MRI reconstruction to neural calcium imaging) where uncertainty quantification has genuine interpretive value.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">CoFEM shows that randomized numerical methods can dramatically accelerate Bayesian inference, reducing covariance-matrix EM from cubic to near-linear complexity, a major step for scalable probabilistic machine learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By making principled uncertainty quantification tractable in high-dimensional inverse problems, CoFEM offers a practical tool for physics-adjacent domains that share the same mathematical structure as sensing problems in fundamental physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending CoFEM to non-Gaussian priors, deeper integration with physics-informed forward models, and applications to large-scale inverse problems in astrophysics and particle physics; see [arXiv:2105.10439](https://arxiv.org/abs/2105.10439) for the full technical treatment.</span></div></div>
</div>
