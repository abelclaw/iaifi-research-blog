---
abstract: 'We present Neural Descriptor Fields (NDFs), an object representation that
  encodes both points and relative poses between an object and a target (such as a
  robot gripper or a rack used for hanging) via category-level descriptors. We employ
  this representation for object manipulation, where given a task demonstration, we
  want to repeat the same task on a new object instance from the same category. We
  propose to achieve this objective by searching (via optimization) for the pose whose
  descriptor matches that observed in the demonstration. NDFs are conveniently trained
  in a self-supervised fashion via a 3D auto-encoding task that does not rely on expert-labeled
  keypoints. Further, NDFs are SE(3)-equivariant, guaranteeing performance that generalizes
  across all possible 3D object translations and rotations. We demonstrate learning
  of manipulation tasks from few (5-10) demonstrations both in simulation and on a
  real robot. Our performance generalizes across both object instances and 6-DoF object
  poses, and significantly outperforms a recent baseline that relies on 2D descriptors.
  Project website: https://yilundu.github.io/ndf/.'
arxivId: '2112.05124'
arxivUrl: https://arxiv.org/abs/2112.05124
authors:
- Anthony Simeonov
- Yilun Du
- Andrea Tagliasacchi
- Joshua B. Tenenbaum
- Alberto Rodriguez
- Pulkit Agrawal
- Vincent Sitzmann
concepts:
- neural descriptor fields
- equivariant neural networks
- geometric deep learning
- pose descriptor fields
- representation learning
- self-supervised learning
- symmetry preservation
- few-shot manipulation
- embeddings
- autoencoders
- group theory
- transfer learning
figures:
- /iaifi-research-blog/figures/2112_05124/figure_1.png
- /iaifi-research-blog/figures/2112_05124/figure_1.png
- /iaifi-research-blog/figures/2112_05124/figure_2.png
- /iaifi-research-blog/figures/2112_05124/figure_2.png
- /iaifi-research-blog/figures/2112_05124/figure_3.png
- /iaifi-research-blog/figures/2112_05124/figure_3.png
pdfUrl: https://arxiv.org/pdf/2112.05124v1
published: '2021-12-09T18:57:15+00:00'
theme: Foundational AI
title: 'Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation'
wordCount: 1230
---

## The Big Picture

Imagine trying to teach someone to hang a mug on a rack, but they've never seen that particular mug before, and it's sitting at a completely random angle. You could spend hours showing them every possible orientation, or you could teach them something more fundamental: *what a mug handle looks like*, and *what it means* to hang something. Robots, until recently, have been firmly stuck in the first camp.

Current robotic systems are frustratingly brittle. Show a robot how to pick up a blue ceramic mug sitting handle-right, and it will struggle the moment you hand it a glass tumbler turned sideways. Reliably handling different objects across all possible 3D orientations, something a toddler does without thinking, has been a persistent bottleneck in robotic manipulation. The core issue isn't raw computation; it's *representation*, the internal model a robot builds of what an object is. Robots haven't had a way to understand objects that captures what matters for a task while staying indifferent to irrelevant variations like size, color, or rotation.

Researchers at MIT, Google Research, and the University of Toronto built exactly that. Their system, **Neural Descriptor Fields (NDFs)**, learns to represent objects in a way that is both task-aware and rotation-proof. A robot can learn a new manipulation skill from just five to ten demonstrations and then execute it on objects it has never seen, in orientations it has never encountered.

> **Key Insight:** NDFs encode not just what an object looks like, but the geometric *meaning* of spatial locations relative to task-relevant features. They do this in a mathematically principled way that guarantees generalization to any 3D orientation.

## How It Works

Instead of teaching a robot "grab this specific mug at these specific pixel coordinates," NDFs teach it something closer to: "grab the object at the location that *feels like* the rim of a mug." The system learns a continuous function that takes any 3D coordinate and maps it to a **spatial descriptor**, a compact geometric signature encoding how that location relates to the object's meaningful features.

![Figure 1](figure:1)

Think of it like smell. Every part of a freshly baked loaf has a scent, but the scent at the crust *means something different* from the scent at the soft interior. Two loaves from the same recipe will have matching scents at matching locations. NDFs do this for geometry: locations with the same structural role on different mugs get the same descriptor, regardless of size or orientation.

Training is self-supervised, with no human-labeled examples required. The network learns by solving a **3D auto-encoding** task: reconstructing 3D point clouds (collections of dots representing an object's surface) from partial observations. Geometric structure emerges on its own.

The architecture uses **SE(3)-equivariant convolutions**, mathematical operations built to respect the full symmetry of 3D space, including all rotations and translations. Rotating the input produces a correspondingly rotated output, not a scrambled one. Generalization to unseen orientations isn't a hopeful extrapolation. It's a provable consequence of the architecture.

At test time, the system works in three steps:

1. **Observe a demonstration**: A human shows the robot a task (e.g., hanging a mug on a rack) using one specific mug. The system records the SE(3) pose, the precise 3D position and orientation of the gripper relative to the mug.
2. **Build a pose descriptor**: That gripper pose is encoded as a set of feature descriptors evaluated at a cluster of query points around the gripper.
3. **Optimize on new instances**: Given a new mug in an arbitrary orientation, the system uses gradient-based optimization to find the transformation that makes the new object's descriptors best match those from the demonstration.

![Figure 2](figure:2)

The trick is treating the gripper pose itself as something to be matched in descriptor space, not in raw coordinate space. Small errors in localizing individual keypoints can compound into large errors for the overall transformation. This approach sidesteps that failure mode entirely.

## Why It Matters

With just five to ten demonstrations, NDFs successfully generalize pick-and-place and rack-hanging tasks to entirely new mug designs across arbitrary 6-DoF configurations (every possible combination of position and rotation in 3D space), including orientations completely absent from training. The system runs in both simulation and on a real robot, and it significantly outperforms a 2D descriptor baseline that works from flat images rather than 3D geometry. That baseline struggles because 2D representations can't handle the full complexity of 3D object pose variation.

![Figure 4](figure:4)

Beyond manipulation, NDFs offer a blueprint for representations that are simultaneously task-relevant and transformation-invariant, unaffected by how an object is rotated or positioned. Self-supervised training eliminates expensive annotation pipelines. The equivariance guarantee eliminates the need to collect examples at every possible rotation. Principled geometric structure plus data efficiency is looking like the recipe for embodied AI systems that can actually operate in the real world.

Open questions remain. Can NDFs handle articulated objects like scissors or bottles with caps? Can the pose descriptor concept extend to longer-horizon task sequences? The framework's treatment of demonstrations as queries into a continuous geometric field suggests natural paths toward both.

> **Bottom Line:** By encoding object geometry in a mathematically rotation-proof way and learning entirely without labeled keypoints, Neural Descriptor Fields let robots generalize manipulation skills from a handful of demonstrations to any object in any 3D orientation. That's a real step toward robots that adapt to the world rather than demanding the world adapt to them.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects geometric deep learning and robotic manipulation by applying SE(3)-equivariant neural architectures, rooted in physics symmetry principles, to the practical challenge of generalizable robotic grasping.

- **Impact on Artificial Intelligence:** NDFs show that mathematical symmetry guarantees, rather than brute-force data augmentation, can unlock generalization from just 5–10 demonstrations, a significant advance in data-efficient robot learning.

- **Impact on Fundamental Interactions:** SE(3)-equivariance directly encodes the rotational and translational symmetry group of 3D space into the neural representation, showing how symmetry principles from physics can be operationalized as inductive biases in learning systems.

- **Outlook and References:** Future work may extend NDFs to articulated and deformable objects and longer-horizon task sequences; the paper is available at [arXiv:2112.05124](https://arxiv.org/abs/2112.05124).

## Original Paper Details
- **Title:** Neural Descriptor Fields: SE(3)-Equivariant Object Representations for Manipulation
- **arXiv ID:** 2112.05124
- **Authors:** ["Anthony Simeonov", "Yilun Du", "Andrea Tagliasacchi", "Joshua B. Tenenbaum", "Alberto Rodriguez", "Pulkit Agrawal", "Vincent Sitzmann"]
- **Abstract:** We present Neural Descriptor Fields (NDFs), an object representation that encodes both points and relative poses between an object and a target (such as a robot gripper or a rack used for hanging) via category-level descriptors. We employ this representation for object manipulation, where given a task demonstration, we want to repeat the same task on a new object instance from the same category. We propose to achieve this objective by searching (via optimization) for the pose whose descriptor matches that observed in the demonstration. NDFs are conveniently trained in a self-supervised fashion via a 3D auto-encoding task that does not rely on expert-labeled keypoints. Further, NDFs are SE(3)-equivariant, guaranteeing performance that generalizes across all possible 3D object translations and rotations. We demonstrate learning of manipulation tasks from few (5-10) demonstrations both in simulation and on a real robot. Our performance generalizes across both object instances and 6-DoF object poses, and significantly outperforms a recent baseline that relies on 2D descriptors. Project website: https://yilundu.github.io/ndf/.
