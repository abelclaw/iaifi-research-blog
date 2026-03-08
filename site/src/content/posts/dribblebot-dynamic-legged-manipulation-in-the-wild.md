---
abstract: DribbleBot (Dexterous Ball Manipulation with a Legged Robot) is a legged
  robotic system that can dribble a soccer ball under the same real-world conditions
  as humans (i.e., in-the-wild). We adopt the paradigm of training policies in simulation
  using reinforcement learning and transferring them into the real world. We overcome
  critical challenges of accounting for variable ball motion dynamics on different
  terrains and perceiving the ball using body-mounted cameras under the constraints
  of onboard computing. Our results provide evidence that current quadruped platforms
  are well-suited for studying dynamic whole-body control problems involving simultaneous
  locomotion and manipulation directly from sensory observations.
arxivId: '2304.01159'
arxivUrl: https://arxiv.org/abs/2304.01159
authors:
- Yandong Ji
- Gabriel B. Margolis
- Pulkit Agrawal
concepts:
- reinforcement learning
- transfer learning
- legged locomotion
- whole-body control
- reward optimization
- robustness
- domain randomization
- multi-task learning
- data augmentation
- convolutional networks
- feature extraction
figures:
- /iaifi-research-blog/figures/2304_01159/figure_1.png
- /iaifi-research-blog/figures/2304_01159/figure_1.png
- /iaifi-research-blog/figures/2304_01159/figure_2.png
- /iaifi-research-blog/figures/2304_01159/figure_2.png
- /iaifi-research-blog/figures/2304_01159/figure_3.png
- /iaifi-research-blog/figures/2304_01159/figure_3.png
pdfUrl: https://arxiv.org/pdf/2304.01159v1
published: '2023-04-03T17:26:09+00:00'
theme: Foundational AI
title: 'DribbleBot: Dynamic Legged Manipulation in the Wild'
wordCount: 932
---

## The Big Picture

Picture a golden retriever chasing a ball across a muddy field, instinctively adjusting its stride as paws sink into wet earth, eyes locked on that bouncing target. Now imagine programming a machine to do the same: not on a polished gym floor with overhead cameras and a supercomputer in the corner, but outside, on sand and snow and gravel, using only the sensors it carries on its back.

That's the challenge at the heart of legged robots that must move and manipulate objects simultaneously in uncontrolled environments. It's the difference between a robot arm bolted to a factory floor and a machine that can actually *do things* in the messy world we live in.

Past attempts at robotic soccer relied on indoor arenas, external motion-capture cameras, or robots that simply pushed a ball with their body. Real dribbling, kicking while running while balancing while tracking a moving target, remained unsolved.

Researchers at MIT's Improbable AI Lab built DribbleBot, a quadruped robot that dribbles a soccer ball across sand, gravel, mud, and snow using only onboard cameras and computing. No external infrastructure required.

> **Key Insight:** By training entirely in simulation and carefully transferring the learned behavior to reality, DribbleBot shows that current off-the-shelf robot hardware is already capable of dynamic whole-body coordination tasks previously considered out of reach.

## How It Works

The robot is a Unitree Go1, a small quadruped standing just 40 cm tall, roughly the height of a beagle. It carries two wide-angle fisheye cameras (each with a 210-degree field of view), two onboard NVIDIA Jetson Xavier NX computers, and a size-3 soccer ball as its permanent partner.

![Figure 1](figure:1)

The core strategy is **sim-to-real transfer**: train the control policy inside a physics simulator, then deploy it on real hardware. This sidesteps the painful problem of collecting millions of physical robot trials, which would destroy the hardware, by letting the robot practice virtually. The team used NVIDIA's Isaac Gym running on a single RTX 3090 GPU.

Simulation alone isn't enough, though. Three specific engineering challenges had to be solved:

1. **Variable ball dynamics.** A soccer ball rolling across pavement behaves nothing like one rolling through mud. The researchers added a custom **ball drag model** to the simulator, a mathematical description of how surface friction slows the ball, and randomized those friction parameters so the policy learned to handle the full spectrum of real-world conditions.

2. **Onboard visual perception.** Conventional robot cameras have narrow fields of view, which fails when the ball is directly in front of the robot's feet. The team switched to fisheye cameras and trained a separate **ball detection module** using a finetuned YOLOv7 model, accelerated with TensorRT to run at 30 Hz on the Jetson hardware. The dribbling policy never sees raw images; it only receives the estimated ball position. This separation keeps the policy lightweight and sidesteps the notoriously hard problem of visual sim-to-real transfer.

3. **Fall recovery.** Rough terrain will occasionally trip the robot. The team trained a dedicated **recovery policy** optimized for harsh falling conditions, enabling the robot to stand back up autonomously and resume dribbling.

![Figure 3](figure:3)

The dribbling policy takes **proprioceptive sensor data** (joint angles, speeds, and foot contact forces) plus the estimated ball position and a commanded ball velocity. It outputs target positions for all 12 motors at 50 Hz.

Training used **Proximal Policy Optimization (PPO)**, a standard reinforcement learning algorithm that refines behavior after each batch of simulated experience. The environment randomized the robot's starting orientation, leg positions, ball location (anywhere within 2 meters), and target velocity, forcing the policy to learn omnidirectional dribbling rather than a single narrow maneuver.

## Why It Matters

DribbleBot matters well beyond the novelty of a robot playing soccer. It's a proof of concept for a broad class of problems: any scenario where a robot must move through the real world while simultaneously manipulating an object. Think carrying packages over uneven ground, shepherding objects in search-and-rescue, or operating where fixed camera infrastructure doesn't exist.

The fact that this was achieved on consumer-grade hardware (the Go1 costs far less than research-grade platforms) with commodity compute (Jetson NX units, not server racks) is telling. It suggests the bottleneck in this kind of robot control is increasingly algorithmic, not hardware.

The modular design, separating perception, dribbling control, and fall recovery into distinct trained components, also points toward a tractable architecture for more complex tasks. Future work could extend this framework to humanoid platforms, non-spherical objects, or multi-robot coordination where the stakes are higher than a soccer match.

> **Bottom Line:** Sim-to-real reinforcement learning, combined with careful engineering of terrain dynamics and onboard perception, can unlock dynamic whole-body manipulation in the wild using hardware and compute that already exist today.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work sits at the intersection of robotics, computer vision, and physics-based simulation, combining reinforcement learning with custom terrain dynamics modeling to solve a real-world control problem that no single discipline could address alone.

- **Impact on Artificial Intelligence:** DribbleBot advances sim-to-real transfer by showing how separating perception and control, combined with domain randomization over physical parameters, enables deployment on hardware with severe computational constraints.

- **Impact on Fundamental Interactions:** The custom ball drag model captures the physics of rolling contact across different surface types, providing a concrete example of how accurate physical modeling in simulation directly determines whether a learned policy succeeds in the real world.

- **Outlook and References:** Future directions include extending whole-body dribbling to bipedal platforms and tackling multi-object manipulation; the paper is available as [arXiv:2304.01159](https://arxiv.org/abs/2304.01159) from MIT's Improbable AI Lab.
