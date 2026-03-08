---
abstract: 'Agile maneuvers such as sprinting and high-speed turning in the wild are
  challenging for legged robots. We present an end-to-end learned controller that
  achieves record agility for the MIT Mini Cheetah, sustaining speeds up to 3.9 m/s.
  This system runs and turns fast on natural terrains like grass, ice, and gravel
  and responds robustly to disturbances. Our controller is a neural network trained
  in simulation via reinforcement learning and transferred to the real world. The
  two key components are (i) an adaptive curriculum on velocity commands and (ii)
  an online system identification strategy for sim-to-real transfer leveraged from
  prior work. Videos of the robot''s behaviors are available at: https://agility.csail.mit.edu/'
arxivId: '2205.02824'
arxivUrl: https://arxiv.org/abs/2205.02824
authors:
- Gabriel B Margolis
- Ge Yang
- Kartik Paigwar
- Tao Chen
- Pulkit Agrawal
concepts:
- reinforcement learning
- adaptive curriculum
- transfer learning
- multi-task learning
- domain randomization
- online system identification
- reward optimization
- robustness
- scalability
figures:
- /iaifi-research-blog/figures/2205_02824/figure_1.png
- /iaifi-research-blog/figures/2205_02824/figure_1.png
- /iaifi-research-blog/figures/2205_02824/figure_2.png
- /iaifi-research-blog/figures/2205_02824/figure_2.png
- /iaifi-research-blog/figures/2205_02824/figure_3.png
- /iaifi-research-blog/figures/2205_02824/figure_3.png
pdfUrl: https://arxiv.org/pdf/2205.02824v1
published: '2022-05-05T17:55:11+00:00'
theme: Foundational AI
title: Rapid Locomotion via Reinforcement Learning
wordCount: 999
---

## The Big Picture

Picture a cheetah and how it moves. It doesn't run fast because someone programmed every muscle twitch and paw placement. It runs fast because millions of years of trial and error shaped instincts that adapt on the fly to every patch of slick grass, every uneven rock. Now imagine giving a robot that same fluid, instinctive speed.

Legged robots have long promised to go where wheeled robots can't: uneven terrain, stairs, the messy real environments that humans navigate daily. But moving fast changes everything.

At walking speeds, small modeling errors are forgiving. At sprinting speeds, the physics becomes unforgiving. Turning too quickly builds up outward forces that can topple the robot, motors hit their physical limits, and the impact of each footfall spikes sharply. The gap between a careful walk and an all-out sprint isn't just about going faster; it's a harder control problem in a qualitative sense.

Researchers at MIT's Improbable AI Lab and IAIFI have pushed past this barrier. Their single neural network controller drives the MIT Mini Cheetah to 3.9 m/s (a record for the platform) across natural terrains from grass to ice, trained entirely in simulation.

> **Key Insight:** By combining an adaptive training schedule with real-time terrain sensing, an AI trained through trial and error can learn to sprint and spin on natural terrain without ever practicing on real ground.

## How It Works

The core idea is **reinforcement learning** (RL), a training paradigm where an agent learns by trying things, collecting rewards for good outcomes, and gradually improving. Here, the agent is a neural network that watches sensor data (just a gyroscope and joint encoders) and outputs joint position commands 50 times per second. No cameras, no LiDAR, no explicit terrain model. Just raw sensor readings mapped to leg movements.

![Figure 1](figure:1)

Training happens entirely in simulation. The researchers randomize everything that might differ between virtual and real: ground friction (from near-frictionless ice to sticky rubber), ground restitution, payload mass, motor strength, even the robot's center of mass. This technique, called **domain randomization**, forces the policy to develop strategies that work across a wide range of conditions, not just the idealized simulation.

Earlier approaches hit a wall here, though. When you ask an RL agent to learn the full range of speeds at once (slow walking through a full sprint) training collapses. The high-speed tasks are too hard to get reward on from the start, so the agent never makes progress. The fix is straightforward:

1. **Start narrow.** Begin training with only low-speed, easily achievable velocity commands.
2. **Expand dynamically.** As the agent masters those tasks, the curriculum automatically widens the commanded speed range, but only to velocities the agent is nearly ready to handle.
3. **Respect physics.** The curriculum tracks which combinations of linear speed and turning rate are actually achievable given the robot's dynamics, never wasting training on physically impossible targets.

This **adaptive velocity curriculum** is one half of the approach. The other is **online system identification**: inferring the robot's properties and terrain conditions in real time while it moves.

The implementation uses a teacher-student setup. During simulation training, a "teacher" policy has access to privileged information: exact terrain parameters, true friction coefficients, precise mass. A "student" policy learns to mimic the teacher using only the limited sensor suite available on the real robot.

The student also includes an **adaptation module**, a small network that reads recent sensor history and infers a compact representation of terrain and robot properties on the fly.

![Figure 2](figure:2)

The result is a policy that, when dropped onto real-world terrain it has never physically experienced, figures out what kind of ground it's on and adjusts within milliseconds. No fine-tuning after deployment.

## Why It Matters

The numbers are striking: 3.9 m/s sustained sprint, 3.4 m/s average over a 10-meter outdoor dash through grass, 5.7 rad/s spinning, all from a single neural network running on an onboard computer with nothing but a gyroscope and leg encoders. But beyond the benchmark, this work carries a deeper message about how to build capable robots.

Look at what the researchers *didn't* design. They didn't hand-engineer gait patterns or specify when legs should lift or how to compensate for ice. The policy developed these strategies entirely on its own and produced emergent behaviors nobody explicitly programmed: automatic recovery from tripping, real-time compensation for a malfunctioning motor. These aren't edge cases added to the reward function. They're behaviors that arose because the RL framework found them useful.

The scalable path to capable robots runs through richer simulation and smarter training regimes, not increasingly elaborate hand-coded rules.

The minimal sensing requirement also matters in practice. Because the controller needs only standard onboard sensors already present on most quadrupeds, the techniques transfer well beyond one expensive prototype. Agile locomotion could become a software upgrade for commercially available robots.

> **Bottom Line:** A neural network trained entirely in simulation, using an adaptive speed curriculum and on-the-fly terrain inference, breaks the speed record for the MIT Mini Cheetah and runs reliably on grass, ice, and gravel. RL can deliver agile, adaptable locomotion that was once thought to require hand-crafted physics models.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects reinforcement learning and classical mechanics by encoding physical constraints (centrifugal force limits, actuator dynamics, contact force regulation) directly into the training curriculum, turning physical laws into a guide for AI learning rather than a barrier to it.

- **Impact on Artificial Intelligence:** The adaptive velocity curriculum and teacher-student architecture provide broadly applicable strategies for multi-task RL in settings where task difficulty is physically constrained and not known in advance.

- **Impact on Fundamental Interactions:** Zero-shot sim-to-real transfer at record agility levels shows that learned models can faithfully capture and exploit real-world physical dynamics without direct physical experience.

- **Outlook and References:** Future work may extend these techniques to more complex morphologies, richer sensing, and higher-level navigation; the full system and videos are documented at [arXiv:2205.02824](https://arxiv.org/abs/2205.02824) alongside the IROS 2022 proceedings.
