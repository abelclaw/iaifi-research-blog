---
abstract: Legged robots have the potential to expand the reach of autonomy beyond
  paved roads. In this work, we consider the difficult problem of locomotion on challenging
  terrains using a single forward-facing depth camera. Due to the partial observability
  of the problem, the robot has to rely on past observations to infer the terrain
  currently beneath it. To solve this problem, we follow the paradigm in computer
  vision that explicitly models the 3D geometry of the scene and propose Neural Volumetric
  Memory (NVM), a geometric memory architecture that explicitly accounts for the SE(3)
  equivariance of the 3D world. NVM aggregates feature volumes from multiple camera
  views by first bringing them back to the ego-centric frame of the robot. We test
  the learned visual-locomotion policy on a physical robot and show that our approach,
  which explicitly introduces geometric priors during training, offers superior performance
  than more naïve methods. We also include ablation studies and show that the representations
  stored in the neural volumetric memory capture sufficient geometric information
  to reconstruct the scene. Our project page with videos is https://rchalyang.github.io/NVM
  .
arxivId: '2304.01201'
arxivUrl: https://arxiv.org/abs/2304.01201
authors:
- Ruihan Yang
- Ge Yang
- Xiaolong Wang
concepts:
- neural volumetric memory
- equivariant neural networks
- geometric deep learning
- reinforcement learning
- representation learning
- visuomotor distillation
- transfer learning
- convolutional networks
- feature extraction
- self-supervised learning
figures:
- /iaifi-research-blog/figures/2304_01201/figure_1.png
- /iaifi-research-blog/figures/2304_01201/figure_1.png
- /iaifi-research-blog/figures/2304_01201/figure_2.png
- /iaifi-research-blog/figures/2304_01201/figure_2.png
- /iaifi-research-blog/figures/2304_01201/figure_3.png
- /iaifi-research-blog/figures/2304_01201/figure_3.png
pdfUrl: https://arxiv.org/pdf/2304.01201v1
published: '2023-04-03T17:59:56+00:00'
theme: Foundational AI
title: Neural Volumetric Memory for Visual Locomotion Control
wordCount: 1039
---

## The Big Picture

Imagine walking across a rocky field while only being allowed to look straight ahead. You can see what's coming, but by the time a rock is directly under your foot, it's already behind your field of view. You have to rely on what you remember seeing moments ago to place each step correctly. This is exactly the challenge facing legged robots navigating difficult terrain.

Robots controlled by cameras face a fundamental mismatch: vision looks forward, but feet need to know what's *beneath* them right now. Most existing approaches handle this with a clumsy trick called **frame-stacking**, where the robot saves the last few raw images and feeds them all into its control system at once.

The problem? As the robot moves and rotates, those saved frames become increasingly misleading. A staircase edge that was on the left three frames ago might be dead ahead now, and the software has to rediscover that geometry from scratch every time. It's like navigating by a pile of photographs taken at random angles rather than a coherent map.

Researchers at UC San Diego and MIT's IAIFI have a cleaner solution: **Neural Volumetric Memory (NVM)**, a geometric memory system that builds and maintains a 3D mental model of the robot's surroundings — and keeps it correctly oriented even as the robot turns and moves.

> **Key Insight:** Instead of stacking raw images (which ignore 3D geometry), NVM translates past observations into a consistent 3D map centered on the robot, giving it a persistent, spatially coherent picture of the terrain beneath its feet.

## How It Works

The NVM system has two interlocking components working in real time.

![Figure 2](/iaifi-research-blog/figures/2304_01201/figure_1.png)

First, a **2D-to-3D feature volume encoder** takes each incoming depth image and "lifts" it into a 3D voxel grid — a grid of 3D pixels, each storing learned information about the space it represents. Rather than treating the camera frame as a flat picture, this encoder builds a volumetric representation of the scene geometry: a miniature 3D map of what's in front of the robot at that instant.

Second, a **pose estimator network** — a small network that tracks exactly how far the robot has moved and which way it's turned — solves the critical alignment problem. When NVM incorporates an observation from two steps ago, it doesn't simply stack it on top. It applies the inverse of the robot's motion to shift and rotate that old 3D map back into the current perspective. In mathematical terms, this makes the memory **SE(3) equivariant**: it correctly handles any combination of rotation and translation in three-dimensional space, the same symmetry group that governs how rigid objects move in the physical world.

Deploying on real hardware uses a two-stage **teacher-student training** approach:

1. **Stage 1 — Teacher policy:** Train a "privileged" controller in simulation with access to a perfect elevation map and ground-truth velocity data. This policy learns to traverse stairs, gaps, and unstructured terrain robustly, but requires sensors unavailable on real hardware.
2. **Stage 2 — Visuomotor distillation:** Train the NVM-equipped student policy to mimic the teacher using only a forward-facing depth camera. ("Visuomotor" means the student learns to connect visual input directly to motor commands.) An optional self-supervised objective based on **novel-view synthesis** — where the model proves it understands the 3D scene by predicting what it would look like from a different angle — provides additional geometric grounding.

![Figure 3](/iaifi-research-blog/figures/2304_01201/figure_2.png)

The result is a single policy — no environment-specific fine-tuning — that transfers directly from simulation to a real UniTree A1 quadruped. The geometric alignment step costs little computationally but pays enormous dividends in sample efficiency and generalization: the network doesn't have to *learn* to account for camera motion because the architecture handles it by construction.

## Why It Matters

The leap from lab demo to real-world legged locomotion has historically required armies of hand-crafted heuristics — special-case code for stairs, rocks, uneven ground. The promise of **end-to-end learned policies** — where the robot learns everything from raw sensor data to motor commands with no hand-written rules in between — is that you train once and deploy anywhere. NVM moves that vision closer to reality.

![Figure 1](/iaifi-research-blog/figures/2304_01201/figure_1.png)

More broadly, the paper illustrates a powerful principle: when you know the physics of your problem — here, that the world is three-dimensional and objects don't warp when you move around them — bake that knowledge into the architecture rather than hoping the network learns it from data. SE(3) equivariance isn't a mathematical nicety; it's a hard constraint that makes the learning problem dramatically easier. The same logic underpins recent work across physics-informed machine learning, from molecular dynamics to gravitational wave detection. NVM is a clean demonstration that geometric priors pay dividends in robotics too.

Open questions remain. The current system uses a single forward-facing camera; lateral or downward-facing sensors could give the robot a fuller picture of its surroundings. The simulation-to-real gap, while impressively small here, still exists, and extending NVM to dynamic obstacles or deformable terrain would push the frontier further. But the core insight — that a robot's memory should respect the geometry of the world — is likely to shape visual locomotion research for years to come.

> **Bottom Line:** Neural Volumetric Memory gives legged robots a 3D geometric map that stays correctly oriented as they move, enabling a single learned policy to navigate stairs, rocks, gaps, and unstructured terrain on real hardware — no fine-tuning required.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges 3D computer vision and reinforcement learning by applying SE(3)-equivariant geometric representations — rooted in the symmetries of physical space — to real-world locomotion control.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">NVM demonstrates that explicitly encoding 3D geometric priors into a memory architecture yields dramatically better generalization than naïve frame-stacking, offering a scalable blueprint for vision-based robot control in unstructured environments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The SE(3) equivariance framework mirrors symmetry principles central to fundamental physics, showing how geometric invariances can be productively imported into machine learning architectures that reason about the physical world.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend NVM to richer sensor configurations and dynamic environments; the paper is available on arXiv and real-world deployment videos are at [rchalyang.github.io/NVM](https://rchalyang.github.io/NVM).</span></div></div>
</div>
