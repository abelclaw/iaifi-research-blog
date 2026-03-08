---
abstract: Diffusion models generate high-quality images but require dozens of forward
  passes. We introduce Distribution Matching Distillation (DMD), a procedure to transform
  a diffusion model into a one-step image generator with minimal impact on image quality.
  We enforce the one-step image generator match the diffusion model at distribution
  level, by minimizing an approximate KL divergence whose gradient can be expressed
  as the difference between 2 score functions, one of the target distribution and
  the other of the synthetic distribution being produced by our one-step generator.
  The score functions are parameterized as two diffusion models trained separately
  on each distribution. Combined with a simple regression loss matching the large-scale
  structure of the multi-step diffusion outputs, our method outperforms all published
  few-step diffusion approaches, reaching 2.62 FID on ImageNet 64x64 and 11.49 FID
  on zero-shot COCO-30k, comparable to Stable Diffusion but orders of magnitude faster.
  Utilizing FP16 inference, our model generates images at 20 FPS on modern hardware.
arxivId: '2311.18828'
arxivUrl: https://arxiv.org/abs/2311.18828
authors:
- Tianwei Yin
- Michaël Gharbi
- Richard Zhang
- Eli Shechtman
- Fredo Durand
- William T. Freeman
- Taesung Park
concepts:
- diffusion models
- distribution matching distillation
- score-based models
- one-step generation
- fake score estimation
- loss function design
- generative models
- fine-tuning
- scalability
- likelihood estimation
- generative adversarial networks
- transfer learning
figures:
- /iaifi-research-blog/figures/2311_18828/figure_1.png
- /iaifi-research-blog/figures/2311_18828/figure_1.png
- /iaifi-research-blog/figures/2311_18828/figure_2.png
- /iaifi-research-blog/figures/2311_18828/figure_2.png
- /iaifi-research-blog/figures/2311_18828/figure_3.png
- /iaifi-research-blog/figures/2311_18828/figure_3.png
pdfUrl: https://arxiv.org/pdf/2311.18828v4
published: '2023-11-30T18:59:20+00:00'
theme: Foundational AI
title: One-step Diffusion with Distribution Matching Distillation
wordCount: 1138
---

## The Big Picture

Imagine hiring a master chef to prepare a meal. She spends two hours layering flavors, tasting, adjusting, reducing sauces. The result is extraordinary. Now imagine you could bottle her intuition about what makes a dish work and teach a short-order cook to nail the same dish in thirty seconds. That's the problem researchers at MIT and Adobe Research set out to solve for image generation.

Diffusion models, the engines behind Stable Diffusion, DALL·E, and Midjourney, produce high-quality images by starting with pure random noise and progressively cleaning it up through dozens of processing steps. Each step asks the model: what should this image look like with a little less noise? Multiply that by fifty steps, and you're waiting seconds per image. For creative workflows, interactive design tools, or real-time applications, that's an eternity.

The team behind **Distribution Matching Distillation (DMD)** found a way to collapse that entire iterative process into a single step, without giving up image quality. Rather than replicating every step of the teacher's process, DMD trains a faster model to produce the same *range* of images, matching the statistical signature of what the full diffusion process would generate.

> **Key Insight:** DMD doesn't teach a student model to mimic the step-by-step denoising *process*. It teaches the student to match the final *distribution* of images that diffusion produces. That's a different objective entirely, and a much more powerful one.

## How It Works

Previous distillation methods tried to directly imitate the teacher's behavior at each step. Give the student a noisy image, and it should predict what the teacher would predict. That's like asking the short-order cook to replicate every knife stroke of the master chef. DMD doesn't care about the process, only the outcome.

![Figure 2](figure:2)

To enforce distribution-level matching, the team minimizes an approximate **KL divergence** (a measure of how different two probability distributions are). The rate of change of this divergence can be expressed as the difference between two score functions, mathematical objects that point any given image in the direction of higher likelihood under some target distribution:

- A **real score function**: a diffusion model trained on real data, pointing images toward higher realism
- A **fake score function**: a diffusion model trained on outputs from the one-step generator, pointing images toward "more fake"

The difference between these two directions tells the one-step generator exactly how to adjust: move toward real, move away from fake. The idea extends **Variational Score Distillation**, previously used for 3D object optimization, to training an entire generative model from scratch.

Distribution matching alone can produce images that are statistically plausible but structurally incoherent. So DMD adds a **regression loss** that anchors the one-step generator to the large-scale structure of multi-step diffusion outputs. The team pre-computes noise-image pairs from the teacher and enforces an **LPIPS perceptual similarity loss** (a standard measure of visual similarity as perceived by humans) between the student's outputs and those references. This regularizer keeps the model honest without being overly constraining.

Two complementary objectives result. Distribution matching ensures outputs *feel* like real diffusion at a statistical level. Regression loss ensures they *look* like what the teacher would have produced.

The numbers back this up. On ImageNet 64×64, DMD achieves a **FID of 2.62** (lower is better), outperforming all published few-step diffusion approaches, including Consistency Models. On the zero-shot text-to-image benchmark COCO-30k at 512×512, DMD scores **11.49 FID**, competitive with full Stable Diffusion while using orders of magnitude fewer neural network evaluations.

![Figure 1](figure:1)

The speed gap speaks for itself. Stable Diffusion takes 2,590 milliseconds per image. DMD takes 90 milliseconds, fast enough for **20 frames per second** with FP16 inference. That crosses the threshold into real-time generation.

## Why It Matters

Real-time generative models open up qualitatively new application categories: live image editing that responds to brush strokes, design tools that show previews as you type, visualization pipelines that generate thousands of candidate images per second.

Diffusion models are increasingly used as surrogate models in physics and scientific computing, serving as fast approximations of expensive simulations. Distilling these surrogates into single-step generators could speed up workflows in particle physics, cosmology, and materials science, where generating large candidate sets is routine. DMD's framework is architecture-agnostic: it applies to any diffusion model with deterministic sampling and drops into existing scientific pipelines without redesigning the underlying model.

There are real open questions, too. Maintaining two separate critic diffusion models (one real, one fake) adds training complexity and cost. Future work might share parameters between them or reduce the upfront cost of pre-computing the regression reference set. And whether DMD's distribution-matching approach extends to video diffusion, where the state space is orders of magnitude larger, is still an unsolved problem.

> **Bottom Line:** DMD turns a 2,590ms image generation pipeline into a 90ms one, with comparable quality, by teaching a one-step generator to match distributions rather than mimic processes. It's not just a speed trick; it's a different way of thinking about distillation entirely.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** DMD draws on information-theoretic tools (KL divergence and score functions) to solve a practical engineering challenge, connecting AI methodology with foundational mathematical concepts.
- **Impact on Artificial Intelligence:** DMD sets a new state of the art for one-step image generation, outperforming all prior few-step diffusion methods and enabling 20 FPS inference for real-time generative AI applications.
- **Impact on Fundamental Interactions:** Single-step diffusion generators could serve as ultra-fast surrogate models for physics simulations, enabling rapid generation of candidate configurations in particle physics, cosmology, and materials science.
- **Outlook and References:** Future directions include extending DMD to video generation and reducing the dual-critic training overhead; code and additional results are available at tianweiy.github.io/dmd.

## Original Paper Details
- **Title:** One-step Diffusion with Distribution Matching Distillation
- **arXiv ID:** [arXiv:2311.18828](https://arxiv.org/abs/2311.18828)
- **Authors:** Tianwei Yin, Michaël Gharbi, Richard Zhang, Eli Shechtman, Frédo Durand, William T. Freeman, Taesung Park
- **Abstract:** Diffusion models generate high-quality images but require dozens of forward passes. We introduce Distribution Matching Distillation (DMD), a procedure to transform a diffusion model into a one-step image generator with minimal impact on image quality. We enforce the one-step image generator match the diffusion model at distribution level, by minimizing an approximate KL divergence whose gradient can be expressed as the difference between 2 score functions, one of the target distribution and the other of the synthetic distribution being produced by our one-step generator. The score functions are parameterized as two diffusion models trained separately on each distribution. Combined with a simple regression loss matching the large-scale structure of the multi-step diffusion outputs, our method outperforms all published few-step diffusion approaches, reaching 2.62 FID on ImageNet 64x64 and 11.49 FID on zero-shot COCO-30k, comparable to Stable Diffusion but orders of magnitude faster. Utilizing FP16 inference, our model generates images at 20 FPS on modern hardware.
