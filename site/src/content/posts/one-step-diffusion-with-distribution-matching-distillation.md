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
wordCount: 1008
---

## The Big Picture

Imagine hiring a master chef to prepare a meal. She spends two hours layering flavors, tasting, adjusting, reducing sauces. The result is extraordinary. Now imagine you could bottle the *essence* of her expertise — her intuition about what makes a dish work — and teach a short-order cook to nail the same dish in thirty seconds. That's the challenge researchers at MIT and Adobe Research set out to solve for image generation.

Diffusion models — the engines behind Stable Diffusion, DALL·E, and Midjourney — produce stunning images by starting with pure random noise and progressively cleaning it up through dozens of processing steps.

Each step asks the model: what should this image look like with a little less noise? Multiply that by fifty steps, and you're waiting seconds per image. For creative workflows, interactive design tools, or real-time applications, that's an eternity.

The MIT and Adobe team behind **Distribution Matching Distillation (DMD)** found a way to collapse that entire iterative process into a single step — without sacrificing quality. Rather than replicating every step of the teacher's process, DMD trains a faster model to produce the same *range* of high-quality images, matching the statistical signature of what the full diffusion process would generate.

> **Key Insight:** Instead of teaching a student model to mimic the step-by-step denoising *process*, DMD teaches it to match the final *distribution* of images that diffusion produces — a fundamentally different and far more powerful objective.

## How It Works

The key conceptual shift is subtle but profound. Previous distillation methods tried to directly imitate the teacher's behavior at each step — if you give the student a noisy image, it should predict what the teacher would predict. That's like asking the short-order cook to replicate every knife stroke of the master chef. DMD doesn't care about the process, only the outcome.

![Figure 2](/iaifi-research-blog/figures/2311_18828/figure_1.png)

To enforce distribution-level matching, the team minimizes an approximate **KL divergence** — a measure of how different two probability distributions are. The rate of change of this divergence can be expressed as the difference between two score functions — mathematical guides that, for any given image, point in the direction that makes it look more like its training data:

- A **real score function**: a diffusion model trained on real data, pointing images toward higher realism
- A **fake score function**: a diffusion model trained on outputs from the one-step generator, pointing images toward "more fake"

The difference between these two directions tells the one-step generator exactly how to adjust: move toward real, move away from fake. This idea extends **Variational Score Distillation** — previously used for 3D object optimization — to training an entire generative model from scratch.

Distribution matching alone, however, can produce images that are statistically plausible but structurally incoherent. So DMD adds a **regression loss** — a training penalty measuring how far the student's outputs deviate from reference examples — that anchors the one-step generator to the large-scale structure of multi-step diffusion outputs. The team pre-computes noise-image pairs from the teacher and enforces an **LPIPS perceptual similarity loss** (a standard measure of visual similarity to human eyes) between the student's outputs and those references. This regularizer keeps the model honest without being overly constraining.

Two complementary objectives result: distribution matching ensures outputs *feel* like real diffusion at a statistical level; regression loss ensures they *look* like what the teacher would have produced.

The numbers bear this out. On ImageNet 64×64, DMD achieves an **FID of 2.62** — lower is better — a 2.4× improvement over the previous best one-step method, Consistency Models. On the zero-shot text-to-image benchmark COCO-30k at 512×512, DMD scores **11.49 FID**, competitive with full Stable Diffusion while using 100× fewer neural network evaluations.

![Figure 1](/iaifi-research-blog/figures/2311_18828/figure_1.png)

The speed difference is visceral. Stable Diffusion takes 2,590 milliseconds per image. DMD takes 90 milliseconds — fast enough for **20 frames per second** with FP16 inference, crossing the threshold into real-time generation.

## Why It Matters

Real-time generative models open qualitatively new application categories: live image editing that responds to brush strokes, design tools that show previews as you type, interactive visualization pipelines that generate thousands of candidate images per second for downstream analysis.

For physics and scientific computing, diffusion models are increasingly used as surrogate models — fast approximations of expensive simulations. Distilling these surrogates into single-step generators could dramatically accelerate workflows in particle physics, cosmology, and materials science, where generating large candidate sets is routine. DMD's framework is architecture-agnostic: it applies to any diffusion model with deterministic sampling and drops into existing scientific pipelines without redesigning the underlying model.

The open questions are equally interesting. Maintaining two separate critic diffusion models — one real, one fake — adds training complexity and cost. Future work might share parameters between them or reduce the upfront cost of pre-computing the regression reference set. Whether DMD's distribution-matching philosophy extends to video diffusion models, where the state space is orders of magnitude larger, remains an open and tantalizing problem.

> **Bottom Line:** DMD turns a 2,590ms image generation pipeline into a 90ms one — without sacrificing quality — by teaching a one-step generator to match distributions rather than mimic processes. It's not just a speed trick; it's a fundamentally different way of thinking about distillation.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">DMD's framework draws on information-theoretic tools — KL divergence and score functions — to solve a practical engineering challenge, reflecting IAIFI's mission of connecting AI methodology with foundational scientific concepts.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">DMD sets a new state of the art for one-step image generation, outperforming all prior few-step diffusion methods and enabling 20 FPS inference for real-time generative AI applications previously out of reach.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Single-step diffusion generators could serve as ultra-fast surrogate models for physics simulations, enabling rapid generation of candidate configurations in particle physics, cosmology, and materials science.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending DMD to video generation and reducing the dual-critic training overhead; code and additional results are available at tianweiy.github.io/dmd.</span></div></div>
</div>
