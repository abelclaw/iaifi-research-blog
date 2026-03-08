---
abstract: 'We present a system for accurately predicting stable orientations for diverse
  rigid objects. We propose to overcome the critical issue of modelling multimodality
  in the space of rotations by using a conditional generative model to accurately
  classify contact surfaces. Our system is capable of operating from noisy and partially-observed
  pointcloud observations captured by real world depth cameras. Our method substantially
  outperforms the current state-of-the-art systems on a simulated stacking task requiring
  highly accurate rotations, and demonstrates strong sim2real zero-shot transfer results
  across a variety of unseen objects on a real world reorientation task. Project website:
  \url{https://richardrl.github.io/stable-reorientation/}'
arxivId: '2208.08962'
arxivUrl: https://arxiv.org/abs/2208.08962
authors:
- Richard Li
- Carlos Esteves
- Ameesh Makadia
- Pulkit Agrawal
concepts:
- contact plane registration
- variational autoencoders
- generative models
- rotation multimodality
- geometric deep learning
- classification
- sim2real transfer
- transfer learning
- monte carlo methods
- robustness
- loss function design
figures:
- /iaifi-research-blog/figures/2208_08962/figure_1.png
- /iaifi-research-blog/figures/2208_08962/figure_2.png
- /iaifi-research-blog/figures/2208_08962/figure_3.png
pdfUrl: https://arxiv.org/pdf/2208.08962v1
published: '2022-08-18T17:10:28+00:00'
theme: Foundational AI
title: Stable Object Reorientation using Contact Plane Registration
wordCount: 935
---

## The Big Picture

Imagine unpacking a box of oddly shaped items, a ceramic mug, a wrench, a toy dinosaur, and stacking them neatly. Without thinking, your brain computes how each object should sit: which face goes down, which edge provides stability. You don't memorize every object; you read its geometry and make a judgment call. For a robot, this same task is a surprisingly hard mathematical problem.

The challenge isn't just picking up an object. It's predicting the right *orientation*, the rotation in three-dimensional space that places an object stably on a surface. Robots operating in warehouses, kitchens, or laboratories need to do this constantly.

The mathematics of 3D rotation is treacherous. Small errors cause wildly wrong answers. Many objects have several equally correct orientations. Standard mathematical tools for describing rotation break down at certain edge cases. A robot that fumbles here can't reliably stack, sort, or hand off anything.

Researchers at MIT's Improbable AI Lab and Google Research have developed a new system that reframes the rotation problem entirely, achieving large improvements in both accuracy and real-world generalization.

> **Key Insight:** Instead of directly predicting a 3D rotation, the system asks a simpler question: *which surface of this object should touch the table?* Answering that well turns out to be sufficient to recover a precise, stable orientation.

## How It Works

Finding a stable resting orientation is really a two-step process: identify the **contact plane** (the flat face that should sit on the table), then compute the rotation needed to align it with gravity. This reformulation sidesteps the notorious difficulties of directly predicting rotations.

![Figure 1](/iaifi-research-blog/figures/2208_08962/figure_1.png)

The system operates in four stages:

1. **Point cloud input.** A depth camera captures a **point cloud**, a set of noisy, incomplete 3D coordinate measurements of the object's surface.
2. **Contact point prediction.** A neural network scores each point: how likely is it to belong to the contact surface, the "bottom" of the object before it's been flipped?
3. **Plane fitting with RANSAC.** **RANSAC** (Random Sample Consensus) is a technique for finding the best-fitting geometric shape in noisy data while automatically ignoring outliers. Here it fits a plane to the highest-density cluster of predicted contact points.
4. **Rotation computation.** Rodrigues' rotation formula converts the fitted plane's **normal vector** (the perpendicular direction pointing straight up from the face) into an exact 3D rotation aligned with gravity.

![Figure 2](/iaifi-research-blog/figures/2208_08962/figure_2.png)

This per-point classification approach generalizes well because contact point probabilities depend mainly on *local geometry*. Flat regions near the base of an object look geometrically similar regardless of whether you've seen that exact object before. Traditional approaches rely on tools like quaternions or Euler angles, compact mathematical encodings of rotation that become ambiguous or ill-conditioned at certain orientations. The network avoids those issues entirely: it votes on which surface points are in contact, not on what rotation to apply.

Objects can have multiple valid contact surfaces. A cube can rest stably on any of six faces. This is the **multimodality problem**: similar inputs can have very different correct outputs. The system handles it with a **CVAE** (Conditional Variational Autoencoder), a generative model that samples plausible hypotheses rather than averaging over all of them. Even when predicted probabilities spread across several valid contact regions, RANSAC selects the dominant cluster and ignores the rest.

![Figure 3](/iaifi-research-blog/figures/2208_08962/figure_3.png)

On a simulated block-stacking benchmark requiring high rotational precision, the method substantially outperforms previous state-of-the-art approaches. It also transfers directly from simulation to the real world **zero-shot**, with no real-world training data at all, successfully reorienting a diverse set of never-before-seen objects using only noisy point clouds from commodity RealSense depth cameras.

## Why It Matters

Object reorientation might sound narrow, but it is a linchpin of robotic manipulation. Virtually every downstream task (pick-and-place, assembly, tool use, surgical robotics) requires a robot to reason about how objects sit in space.

Systems that generalize poorly to new object shapes are effectively useless outside a controlled lab. The **sim-to-real gap**, the tendency for robots trained in simulation to fail in the messier real world, remains one of the biggest open problems in robotics. This work attacks both issues simultaneously.

The deeper contribution is methodological. Decomposing a hard rotation-prediction problem into a more tractable contact-classification problem shows that clever reformulation can outperform simply scaling up model capacity. Local geometric reasoning, the kind that transfers across shapes, is exactly the right prior for manipulation tasks. Open questions remain around non-planar contact surfaces, dynamics during contact, and deformable objects where stable orientations are harder to define.

> **Bottom Line:** By teaching a robot to ask "which face goes down?" instead of "what rotation is needed?", this system achieves accurate, generalizable object reorientation from real-world depth cameras, transferring from simulation to physical robots without any real-world training data.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects geometric deep learning and robotic manipulation, using physical reasoning about contact and gravity to structure a machine learning problem, reflecting IAIFI's AI-physics integration approach.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The contact plane reformulation offers a principled solution to the multimodality problem in SO(3) rotation prediction, combining conditional generative modeling with geometric estimation for stable, generalizable inference.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By grounding the learning problem in physical constraints (stable equilibria, contact mechanics, gravitational alignment), the method shows how physics priors can be embedded directly into neural architectures to improve generalization across object geometries.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions may address non-planar contact surfaces and dynamic manipulation; the sim-to-real framework also provides a template for training robotic systems without costly real-world data collection. Full paper by Li, Esteves, Makadia, and Agrawal: [arXiv:2208.08962](https://arxiv.org/abs/2208.08962).</span></div></div>
</div>
