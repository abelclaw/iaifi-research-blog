---
abstract: Knowledge of terrain's physical properties inferred from color images can
  aid in making efficient robotic locomotion plans. However, unlike image classification,
  it is unintuitive for humans to label image patches with physical properties. Without
  labeled data, building a vision system that takes as input the observed terrain
  and predicts physical properties remains challenging. We present a method that overcomes
  this challenge by self-supervised labeling of images captured by robots during real-world
  traversal with physical property estimators trained in simulation. To ensure accurate
  labeling, we introduce Active Sensing Motor Policies (ASMP), which are trained to
  explore locomotion behaviors that increase the accuracy of estimating physical parameters.
  For instance, the quadruped robot learns to swipe its foot against the ground to
  estimate the friction coefficient accurately. We show that the visual system trained
  with a small amount of real-world traversal data accurately predicts physical parameters.
  The trained system is robust and works even with overhead images captured by a drone
  despite being trained on data collected by cameras attached to a quadruped robot
  walking on the ground.
arxivId: '2311.01405'
arxivUrl: https://arxiv.org/abs/2311.01405
authors:
- Gabriel B. Margolis
- Xiang Fu
- Yandong Ji
- Pulkit Agrawal
concepts:
- self-supervised learning
- active terrain sensing
- reinforcement learning
- active learning
- proprioceptive state estimation
- sim-to-real transfer
- reward optimization
- representation learning
- inverse problems
- transfer learning
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2311_01405/figure_1.png
- /iaifi-research-blog/figures/2311_01405/figure_1.png
- /iaifi-research-blog/figures/2311_01405/figure_2.png
- /iaifi-research-blog/figures/2311_01405/figure_2.png
- /iaifi-research-blog/figures/2311_01405/figure_3.png
- /iaifi-research-blog/figures/2311_01405/figure_3.png
pdfUrl: https://arxiv.org/pdf/2311.01405v1
published: '2023-11-02T17:19:18+00:00'
theme: Foundational AI
title: Learning to See Physical Properties with Active Sensing Motor Policies
wordCount: 1046
---

## The Big Picture

Close your eyes and walk across a room. Even blind, you can tell carpet from tile, grass from ice — your feet feel it. Now imagine a robot trying to do the same thing, but needing to teach its *eyes* what its feet already know. That's exactly the problem a team at MIT's Improbable AI Lab set out to solve.

Legged robots today are surprisingly good at navigating complex terrain — stairs, sand, slopes, even ice. But most rely on depth sensors and body-position sensing, ignoring a rich source of information hiding in plain sight: color. A patch of wet grass *looks* different from dry concrete. Knowing that difference from a camera feed, before the robot takes a step, could make locomotion dramatically safer and more efficient.

The challenge is that nobody knows how to annotate terrain images with physical properties like slipperiness. You can't hire humans to measure and label every surface a robot might walk on.

The MIT team's answer: don't use human labels at all. Instead, teach the robot to generate its own ground truth by actively exploring terrain, then use those physical measurements to train a vision model that learns to *see* what the terrain *feels* like.

> **Key Insight:** By training a robot to move in ways that maximize physical sensing accuracy — learning to swipe its foot like a wine-taster swirling a glass — researchers built a self-labeling pipeline that turns the robot's physical experience into visual intuition about terrain physics.

## How It Works

The system unfolds in four interlocking stages, each feeding into the next.

![Figure 1](/iaifi-research-blog/figures/2311_01405/figure_1.png)

The foundation is **Active Sensing Motor Policies (ASMP)** — the paper's central contribution, and a new way of thinking about robot movement. Standard locomotion controllers are trained to move efficiently from A to B. ASMPs are trained to do something subtler: move in ways that *reveal* physical information about the ground.

Specifically, the policy receives an **estimation reward** — a bonus signal that grows when the robot's onboard **state estimator** (a software module, trained entirely in simulation, that infers hidden physical conditions from sensor readings) can accurately measure the terrain's slipperiness or roughness. The result is emergent, almost animal-like behavior: the quadruped learns on its own to drag a foot sideways to probe friction, or vary its gait to make roughness measurable. Nobody programmed that swiping motion. The robot discovered it because sliding a foot is simply the most informative thing it can do.

![Figure 2](/iaifi-research-blog/figures/2311_01405/figure_1.png)

Here's how the full pipeline chains together:

1. **Active traversal**: The ASMP walks across real terrain while the state estimator measures local slipperiness and roughness from joint torques, velocities, and contact patterns.
2. **Self-supervised labeling**: Every image frame from the onboard cameras is automatically tagged with the physical property estimate from that moment — no human annotators, no manual labels.
3. **Vision training**: A neural network built on a pretrained visual backbone learns to map image patches to per-pixel physical property values, supervised entirely by robot-generated labels.
4. **Cost-map planning**: Simulation rollouts with varied terrain parameters generate a cost function linking physical properties to performance metrics. Combined with the vision model's predictions, the robot computes a full cost map from a color image and plans paths accordingly.

The state estimator is trained in simulation with **domain randomization** — deliberately exposing it to a huge range of simulated conditions, from slick ice to rough gravel — so it generalizes to real surfaces it has never seen. This **sim-to-real transfer** is what makes the whole chain work: reliable physical estimates in the real world, derived entirely from simulated training.

## Why It Matters

The most striking result is generalization across viewpoints. The visual model trains exclusively on images from cameras mounted on a low-walking quadruped — a ground-level perspective. Yet when tested on overhead imagery from a drone, the model still predicts terrain properties accurately.

The reason: physical properties like slipperiness and roughness don't change with viewing angle. A slippery surface is slippery whether you're looking from 10 centimeters or 10 meters. Task-specific measures of terrain quality would not generalize the same way.

This points toward a more modular future for robotic perception. Prior terrain-aware locomotion work tends to bake task-specific assumptions into learned representations — a model trained to judge "is this good for fast running?" needs retraining for "is this good for dragging a sled?" By predicting raw physical parameters instead, this system creates a **digital twin** of terrain properties that any downstream planner can query for any task.

Swap in a new cost function from simulation, and the same vision model serves a completely new objective. That modularity is rare and opens the door to rapid adaptation as robots encounter new mission requirements.

Open questions remain. The current system focuses on two parameters — friction and roughness. Real terrain has more degrees of freedom: deformability, wetness, thermal properties. Extending active sensing to a richer parameter space, without making the robot's exploratory behavior too disruptive for normal operation, is a natural next frontier. There's also the question of how active sensing interacts with the primary locomotion objective — sometimes you need to move fast, not informatively.

> **Bottom Line:** By teaching a robot to move in physically revealing ways, MIT researchers built a self-labeling loop that transfers physical intuition from body to eye — and the resulting vision system generalizes across viewpoints that task-specific models cannot handle.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges robotics control theory, physics-based simulation, and computer vision, using physical parameter estimation as the connective tissue between a robot's bodily experience and its visual perception of the world.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The Active Sensing Motor Policy framework introduces a principled, emergent approach to active perception, where an agent learns what actions maximize informational value rather than having information-gathering behavior hand-designed.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The pipeline treats terrain as a dynamical system with measurable physical parameters — friction coefficients, roughness magnitudes — demonstrating that sim-to-real transfer of physics-based estimators can anchor real-world machine perception in genuine physical quantities.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend active sensing to richer terrain parameter spaces and multi-robot teaming scenarios; the paper appeared at CoRL 2023 and the project page is at gmargo11.github.io/active-sensing-loco.</span></div></div>
</div>
