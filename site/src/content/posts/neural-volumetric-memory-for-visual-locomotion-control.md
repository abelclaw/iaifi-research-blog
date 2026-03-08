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
wordCount: 966
---

## The Big Picture

Walk across a rocky field while only looking straight ahead. You can see what's coming, but by the time a rock is directly under your foot, it's behind your field of view. You have to rely on what you saw moments ago to place each step. Legged robots navigating rough terrain face the same problem.

Cameras look forward; feet need to know what's *beneath* them right now. Most existing approaches paper over this mismatch with **frame-stacking**: the robot saves the last few raw images and feeds them all into its controller at once.

The problem? As the robot moves and rotates, those saved frames become increasingly misleading. A staircase edge that was on the left three frames ago might be dead ahead now, and the software has to rediscover that geometry every time. It's like navigating by a pile of photographs taken at random angles rather than a coherent map.

Researchers at UC San Diego and MIT's IAIFI propose a cleaner solution: **Neural Volumetric Memory (NVM)**, a geometric memory system that builds and maintains a 3D model of the robot's surroundings and keeps it correctly oriented even as the robot turns and moves.

> **Key Insight:** Instead of stacking raw images (which ignore 3D geometry), NVM translates past observations into a consistent 3D map centered on the robot, giving it a persistent, spatially coherent picture of the terrain beneath its feet.

## How It Works

NVM has two interlocking components, both running in real time.

![Figure 2](figure:2)

A **2D-to-3D feature volume encoder** takes each incoming depth image and "lifts" it into a 3D voxel grid (a grid of 3D pixels, each storing learned information about the space it represents). Rather than treating the camera frame as a flat picture, this encoder builds a volumetric representation of the scene: a miniature 3D map of what's in front of the robot at that instant.

A **pose estimator network** tracks how far the robot has moved and which way it's turned, solving the critical alignment problem. When NVM incorporates an observation from two steps ago, it doesn't simply stack it on top. It applies the inverse of the robot's motion to shift and rotate that old 3D map back into the current perspective. In mathematical terms, the memory is **SE(3) equivariant**: it correctly handles any combination of rotation and translation in three-dimensional space, the same symmetry group that governs how rigid objects move in the physical world.

Getting this onto real hardware requires a two-stage teacher-student training pipeline:

1. **Stage 1 (Teacher policy):** Train a "privileged" controller in simulation with access to a perfect elevation map and ground-truth velocity data. This policy learns to traverse stairs, gaps, and unstructured terrain, but depends on sensors unavailable on real hardware.
2. **Stage 2 (Visuomotor distillation):** Train the NVM-equipped student to mimic the teacher using only a forward-facing depth camera. "Visuomotor" here means the student maps visual input directly to motor commands. An optional self-supervised objective based on **novel-view synthesis**, where the model proves it understands the 3D scene by predicting what it would look like from a different angle, provides additional geometric grounding.

![Figure 3](figure:3)

The result is a single policy, with no environment-specific fine-tuning, that transfers directly from simulation to a real Unitree A1 quadruped. The geometric alignment step is cheap to compute but pays off enormously in sample efficiency and generalization: the network doesn't have to *learn* to account for camera motion because the architecture handles it by construction.

## Why It Matters

Getting legged robots from lab demos to real-world locomotion has historically required armies of hand-crafted heuristics, with special-case code for stairs, rocks, and uneven ground. End-to-end learned policies (where the robot learns everything from raw sensor data to motor commands, no hand-written rules in between) promise that you train once and deploy anywhere. NVM moves that promise closer to reality.

![Figure 1](figure:1)

The paper also illustrates a broader principle: when you know the physics of your problem (here, that the world is three-dimensional and objects don't warp when you move around them), bake that knowledge into the architecture rather than hoping the network discovers it from data. SE(3) equivariance isn't a mathematical nicety; it's a hard constraint that makes learning dramatically easier. The same idea runs through recent physics-informed machine learning, from molecular dynamics to gravitational wave detection, and NVM shows it pays off in robotics too.

Open questions remain. The current system uses a single forward-facing camera; lateral or downward-facing sensors could give the robot a fuller picture. The simulation-to-real gap, while impressively small here, still exists, and extending NVM to dynamic obstacles or deformable terrain would test its limits further. But the core insight, that a robot's memory should respect the geometry of the world, is likely to influence visual locomotion research for years.

> **Bottom Line:** Neural Volumetric Memory gives legged robots a 3D geometric map that stays correctly oriented as they move, enabling a single learned policy to navigate stairs, rocks, gaps, and unstructured terrain on real hardware, no fine-tuning required.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects 3D computer vision with reinforcement learning, applying SE(3)-equivariant geometric representations (rooted in the symmetries of physical space) to real-world locomotion control.

- **Impact on Artificial Intelligence:** Explicitly encoding 3D geometric priors into a memory architecture yields far better generalization than naïve frame-stacking, providing a template for vision-based robot control in unstructured environments.

- **Impact on Fundamental Interactions:** The SE(3) equivariance framework mirrors symmetry principles central to fundamental physics, showing how geometric invariances from physics can be imported into machine learning architectures that reason about the physical world.

- **Outlook and References:** Future work may extend NVM to richer sensor configurations and dynamic environments. The paper is available at [arXiv:2304.01201](https://arxiv.org/abs/2304.01201), and real-world deployment videos are at [rchalyang.github.io/NVM](https://rchalyang.github.io/NVM).
