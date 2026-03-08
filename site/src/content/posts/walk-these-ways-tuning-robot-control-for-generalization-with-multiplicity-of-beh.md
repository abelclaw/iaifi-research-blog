---
abstract: 'Learned locomotion policies can rapidly adapt to diverse environments similar
  to those experienced during training but lack a mechanism for fast tuning when they
  fail in an out-of-distribution test environment. This necessitates a slow and iterative
  cycle of reward and environment redesign to achieve good performance on a new task.
  As an alternative, we propose learning a single policy that encodes a structured
  family of locomotion strategies that solve training tasks in different ways, resulting
  in Multiplicity of Behavior (MoB). Different strategies generalize differently and
  can be chosen in real-time for new tasks or environments, bypassing the need for
  time-consuming retraining. We release a fast, robust open-source MoB locomotion
  controller, Walk These Ways, that can execute diverse gaits with variable footswing,
  posture, and speed, unlocking diverse downstream tasks: crouching, hopping, high-speed
  running, stair traversal, bracing against shoves, rhythmic dance, and more. Video
  and code release: https://gmargo11.github.io/walk-these-ways/'
arxivId: '2212.03238'
arxivUrl: https://arxiv.org/abs/2212.03238
authors:
- Gabriel B Margolis
- Pulkit Agrawal
concepts:
- multiplicity of behavior
- reinforcement learning
- robustness
- sim-to-real transfer
- multi-task learning
- behavior parameterization
- transfer learning
- reward optimization
- disentangled representations
- out-of-distribution detection
- loss function design
figures:
- /iaifi-research-blog/figures/2212_03238/figure_1.png
- /iaifi-research-blog/figures/2212_03238/figure_1.png
- /iaifi-research-blog/figures/2212_03238/figure_2.png
- /iaifi-research-blog/figures/2212_03238/figure_2.png
- /iaifi-research-blog/figures/2212_03238/figure_3.png
- /iaifi-research-blog/figures/2212_03238/figure_3.png
pdfUrl: https://arxiv.org/pdf/2212.03238v1
published: '2022-12-06T18:59:34+00:00'
theme: Foundational AI
title: 'Walk These Ways: Tuning Robot Control for Generalization with Multiplicity
  of Behavior'
wordCount: 1019
---

## The Big Picture

Imagine teaching someone to walk by only ever practicing on a gym floor. The moment they step outside onto gravel, ice, or a flight of stairs, they freeze. Nothing in their training prepared them for that. This is the central frustration of modern robot locomotion. Researchers spend months training a four-legged robot to walk, only to find that the slightest deviation from the training environment sends it stumbling. A slippery patch, an unexpected step, a shove from behind: any of these can be fatal to a carefully learned gait.

The conventional fix is painstaking. Redesign the scoring rules that tell the robot what counts as good behavior. Tweak the simulation. Retrain from scratch. Test in the real world. Repeat. Adjustments that help the robot climb stairs often hurt its performance on slippery ground. There's no free lunch.

Gabriel Margolis and Pulkit Agrawal at MIT's Improbable AI Lab took a different approach. Rather than searching for one perfect walking strategy, they asked: what if a single trained policy (the robot's learned decision-making program) contained *many* strategies, all equally valid during training, but each performing differently on unfamiliar terrain? The result is **Multiplicity of Behavior (MoB)** and an open-source controller called *Walk These Ways*.

> **Key Insight:** A robot policy doesn't have to commit to one way of walking. By encoding a structured family of behaviors into a single policy, you can tune robot locomotion in real time for new environments, no retraining required.

## How It Works

The driving observation behind MoB is **under-specification**: many different locomotion strategies can equally solve a training task. Walking on flat ground constrains only one thing, the robot's overall forward velocity. It says nothing about how high the feet should lift, how wide the stance should be, how the torso should angle, or how fast the legs should cycle.

Two robots walking at the same speed with completely different gaits both "succeed" during training. But on ice, one slips while the other holds firm. On stairs, one stumbles while the other clears each step cleanly.

![Figure 1](figure:1)

MoB exploits this deliberately. Instead of training a policy that locks onto one solution, the researchers train a policy that takes as additional inputs a small set of **behavior parameters**: variables specifying aspects of the gait like foot clearance height, body posture, gait frequency, and foot contact timing. At training time, these parameters are randomized across a wide range of combinations, forcing the policy to learn not one walk but a whole *family* of walks. At deployment time, a human operator or higher-level controller can dial these parameters in real time. No retraining, no reward engineering.

![Figure 2](figure:2)

The technical implementation pairs **reinforcement learning** (a training method where the robot improves by trial and error, guided by rewards for good behavior) with a timing-based gait parameterization that encodes precisely when each foot should be on the ground and when it should swing. The policy receives behavior parameters alongside standard sensory observations like joint angles, velocities, and orientation estimates. It then learns to produce the joint forces that realize the requested movement. With the right timing parameters, the controller executes classical structured gaits: trotting, bounding, pacing, and pronking (a springy leap where all four feet leave the ground simultaneously).

The training setup is deliberately minimal. Flat ground only. No stairs, no rough terrain, no external disturbances. Yet by encoding a rich behavioral repertoire, the same policy, with manually tuned parameters, successfully handles:

- **Stair traversal** with a low-frequency gait and high foot clearance
- **Slippery terrain sprinting** using a high-frequency, low-clearance gait
- **Resistance to external shoves** through a wide stance and low swing height
- **Crouching under obstacles** via a low-body-height posture mode
- **High-speed running, hopping, and rhythmic dance** through direct gait parameter control

The parameters are interpretable. A human can look at a new environment, reason about what kind of gait it demands, and adjust accordingly, far faster than redesigning a reward function and waiting hours for retraining.

## Why It Matters

This work addresses a persistent problem in robotics: the **sim-to-real gap**. Robots trained in simulation always face a world slightly different from what they practiced on. More and better simulation will never fully close that gap. MoB offers a complementary strategy. Instead of simulating every possible scenario, simulate *diversity of behavior*, and let humans or higher-level algorithms select the right behavior at deployment time.

The principle extends beyond locomotion. Any reinforcement learning setting where the training task under-specifies the solution (which is most real-world tasks) could benefit from MoB. The researchers frame this as a general approach to out-of-distribution generalization, where behavioral diversity hedges against an unpredictable world.

The *Walk These Ways* controller also works well as a practical building block. Its interpretable control interface makes it easy to use as the low-level foundation for higher-level task planners, demonstration collection systems, or learned behavior selectors.

> **Bottom Line:** *Walk These Ways* proves that a single robot policy, trained only on flat ground, can handle stairs, ice, shoves, and dance moves. The trick isn't better simulation. It's encoding a structured family of behaviors tunable in real time. Behavioral diversity turns out to be a powerful tool for generalization.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects reinforcement learning theory, specifically the concept of under-specification in policy learning, with hands-on robotics engineering. The takeaway is that theoretical insights about solution multiplicity have direct, practical consequences for real-world deployment.

- **Impact on Artificial Intelligence:** MoB introduces a principled framework for encoding behavioral diversity into a single learned policy, offering a fresh angle on out-of-distribution generalization that complements domain randomization and meta-learning approaches.

- **Impact on Fundamental Interactions:** By reducing dependence on accurate physics simulation for out-of-distribution scenarios, this work moves closer to deploying AI-controlled physical systems in environments where ground-truth dynamics are unknown or hard to model.

- **Outlook and References:** Future work could explore automated parameter selection, having a learned system choose behaviors on the fly, and extend MoB to manipulator arms or other physical systems. The paper is available at [arXiv:2212.03238](https://arxiv.org/abs/2212.03238) and the open-source controller at https://gmargo11.github.io/walk-these-ways/.
