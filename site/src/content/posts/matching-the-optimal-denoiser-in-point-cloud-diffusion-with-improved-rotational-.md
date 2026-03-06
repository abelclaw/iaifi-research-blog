---
abstract: Diffusion models are a popular class of generative models trained to reverse
  a noising process starting from a target data distribution. Training a diffusion
  model consists of learning how to denoise noisy samples at different noise levels.
  When training diffusion models for point clouds such as molecules and proteins,
  there is often no canonical orientation that can be assigned. To capture this symmetry,
  the true data samples are often augmented by transforming them with random rotations
  sampled uniformly over $SO(3)$. Then, the denoised predictions are often rotationally
  aligned via the Kabsch-Umeyama algorithm to the ground truth samples before computing
  the loss. However, the effect of this alignment step has not been well studied.
  Here, we show that the optimal denoiser can be expressed in terms of a matrix Fisher
  distribution over $SO(3)$. Alignment corresponds to sampling the mode of this distribution,
  and turns out to be the zeroth order approximation for small noise levels, explaining
  its effectiveness. We build on this perspective to derive better approximators to
  the optimal denoiser in the limit of small noise. Our experiments highlight that
  alignment is often a `good enough' approximation for the noise levels that matter
  most for training diffusion models.
arxivId: '2510.03335'
arxivUrl: https://arxiv.org/abs/2510.03335
authors:
- Ameya Daigavane
- YuQing Xie
- Bodhi P. Vani
- Saeed Saremi
- Joseph Kleinhenz
- Tess Smidt
concepts:
- diffusion models
- rotational alignment
- symmetry preservation
- matrix fisher distribution
- group theory
- loss function design
- laplace approximation
- equivariant neural networks
- geometric deep learning
- data augmentation
- generative models
- score-based models
figures:
- /iaifi-research-blog/figures/2510_03335/figure_1.png
- /iaifi-research-blog/figures/2510_03335/figure_2.png
- /iaifi-research-blog/figures/2510_03335/figure_3.png
pdfUrl: https://arxiv.org/pdf/2510.03335v1
published: '2025-10-02T05:55:22+00:00'
theme: Foundational AI
title: Matching the Optimal Denoiser in Point Cloud Diffusion with (Improved) Rotational
  Alignment
wordCount: 1028
---

## The Big Picture

Imagine you're trying to teach a computer to generate realistic 3D models of molecules. You show it a caffeine molecule, then a rotated caffeine molecule, then another rotation. The molecule is the same, but it looks different from every angle. The AI needs to understand that these are all the same thing. Making AI treat every rotation of an object as equally valid is the central challenge in generating molecular structures, protein conformations, and any 3D data represented as a collection of points in space.

**Diffusion models** have become the go-to tool for generating such structures. They work by learning to "un-blur" noisy data, starting from chaos and progressively denoising until a realistic structure emerges. But when your data has no preferred orientation in 3D space, a fundamental question arises: how do you train the AI to denoise correctly when any rotation of the answer is equally valid?

The standard fix has been surprisingly simple: rotate your training data randomly, then align the model's predictions back to the original orientation before measuring the error. Practically every major molecular generation system uses this trick. But until now, nobody had proven *why* it works, or whether something better was possible. A team from MIT and Genentech has now answered both questions.

> **Key Insight:** The standard alignment trick in point cloud diffusion is mathematically equivalent to the simplest possible approximation of the theoretically perfect denoising step, and the researchers have derived provably better approximations.

## How It Works

Two key players make the story work.

The first is the **Kabsch-Umeyama algorithm**, a classical method for finding the best rotation that aligns two sets of 3D points. When training a diffusion model on molecules, practitioners use this to rotate the model's prediction so it lines up as closely as possible with the ground-truth structure before computing the error. It's like grading a student's answer by first rotating it to match the answer key.

![Figure 1](/iaifi-research-blog/figures/2510_03335/figure_1.png)

The second is the **matrix Fisher distribution**, a probability distribution over rotations in 3D space. Think of it like a bell curve, but instead of describing how likely different numbers are, it describes how likely different orientations are. The more concentrated the distribution, the more confidently you can say which rotation is correct.

The paper's central result connects these two. The **optimal denoiser** (the theoretically perfect prediction at any given noise level) can be written as an average over the matrix Fisher distribution. Given a noisy point cloud, the ideal denoiser asks: "What rotation would most likely have produced this noisy observation?" It then averages over all plausible rotations, weighted by their probability.

Here's where alignment enters the picture:

- When you apply Kabsch-Umeyama to align a prediction to the ground truth, you're picking the single *most likely* rotation (the peak of the Fisher distribution).
- This is mathematically equivalent to a **zeroth-order Laplace approximation**: replacing the full average over all rotations with just the value at the peak.
- At high noise levels, many rotations are plausible and this approximation is crude. At low noise levels, the distribution becomes sharply peaked and the peak captures nearly everything.

This explains why alignment works at all: as noise decreases during denoising, the optimal rotation becomes more concentrated, and simple alignment becomes an increasingly accurate approximation of the true optimal answer.

![Figure 2](/iaifi-research-blog/figures/2510_03335/figure_2.png)

The researchers then pushed further, using **Laplace's method** (a classical technique for approximating integrals by expanding around their peaks) to derive correction terms beyond the zeroth-order approximation. These higher-order estimators capture the spread of the Fisher distribution around its peak, accounting for the range of plausible rotations rather than just the most likely one. These improved estimators add negligible computational cost: the correction terms are computed analytically, not through expensive Monte Carlo sampling (running thousands of random simulations to estimate an average).

![Figure 3](/iaifi-research-blog/figures/2510_03335/figure_3.png)

Experimentally, the corrected estimators showed reduced bias compared to plain alignment, especially at higher noise levels. The experiments also revealed something practically important: for the noise levels that dominate typical training loss, standard alignment is already quite accurate. The low-noise regime, where improved estimators matter most in theory, is also where the approximation error from plain alignment is already small.

## Why It Matters

This work matters at two levels. On the practical side, it gives molecular AI researchers a principled understanding of a technique they've been using somewhat blindly. Tools like AlphaFold 3 and molecular generation systems from Genentech use variants of rotational alignment during training. Knowing *why* it works (and precisely *when* it might fail) helps researchers make informed architectural decisions rather than relying on empirical folklore.

On the theoretical side, the connection to the matrix Fisher distribution opens a new mathematical language for thinking about symmetry in generative models. The framework isn't limited to Kabsch-Umeyama alignment: it applies broadly to any setting where data lacks a canonical orientation. As AI systems for drug discovery, materials science, and structural biology grow more ambitious, these theoretical foundations matter more.

> **Bottom Line:** Standard rotational alignment in point cloud diffusion is the zeroth-order approximation to the provably optimal denoiser. The researchers proved it, derived better approximations, and showed that for most practical training scenarios, the old trick works just fine. Now you know exactly why.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges mathematical physics (specifically, the theory of distributions over Lie groups like SO(3)) with modern deep learning, providing a rigorous foundation for a widely-used but poorly-understood training technique in molecular AI.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper delivers the first theoretical proof that rotational alignment in point cloud diffusion training corresponds to a zeroth-order approximation of the optimal denoiser, and derives provably better estimators via Laplace's method at no added computational cost.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By clarifying how symmetry constraints should be handled during diffusion model training, this work directly advances AI tools for predicting molecular and protein structures, key to understanding the fundamental interactions governing matter.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend these results to higher noise regimes and other physical symmetry groups. The preprint is available at [arXiv:2510.03335](https://arxiv.org/abs/2510.03335) (Daigavane, Xie, Vani, Saremi, Kleinhenz, Smidt, 2025).</span></div></div>
</div>
