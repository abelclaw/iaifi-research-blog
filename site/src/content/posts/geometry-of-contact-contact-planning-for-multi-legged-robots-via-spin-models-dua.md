---
abstract: Contact planning is crucial in locomoting systems.Specifically, appropriate
  contact planning can enable versatile behaviors (e.g., sidewinding in limbless locomotors)
  and facilitate speed-dependent gait transitions (e.g., walk-trot-gallop in quadrupedal
  locomotors). The challenges of contact planning include determining not only the
  sequence by which contact is made and broken between the locomotor and the environments,
  but also the sequence of internal shape changes (e.g., body bending and limb shoulder
  joint oscillation). Most state-of-art contact planning algorithms focused on conventional
  robots (e.g.biped and quadruped) and conventional tasks (e.g. forward locomotion),
  and there is a lack of study on general contact planning in multi-legged robots.
  In this paper, we show that using geometric mechanics framework, we can obtain the
  global optimal contact sequence given the internal shape changes sequence. Therefore,
  we simplify the contact planning problem to a graph optimization problem to identify
  the internal shape changes. Taking advantages of the spatio-temporal symmetry in
  locomotion, we map the graph optimization problem to special cases of spin models,
  which allows us to obtain the global optima in polynomial time. We apply our approach
  to develop new forward and sidewinding behaviors in a hexapod and a 12-legged centipede.
  We verify our predictions using numerical and robophysical models, and obtain novel
  and effective locomotion behaviors.
arxivId: '2302.03019'
arxivUrl: https://arxiv.org/abs/2302.03019
authors:
- Baxi Chong
- Di Luo
- Tianyu Wang
- Gabriel Margolis
- Juntao He
- Pulkit Agrawal
- Marin Soljačić
- Daniel I. Goldman
concepts:
- contact sequence optimization
- geometric mechanics
- geometric deep learning
- spin model duality
- group theory
- symmetry preservation
- phase transitions
- graph neural networks
- surrogate modeling
- optimal transport
- reinforcement learning
figures:
- /iaifi-research-blog/figures/2302_03019/figure_1.png
- /iaifi-research-blog/figures/2302_03019/figure_1.png
- /iaifi-research-blog/figures/2302_03019/figure_2.png
- /iaifi-research-blog/figures/2302_03019/figure_2.png
- /iaifi-research-blog/figures/2302_03019/figure_3.png
- /iaifi-research-blog/figures/2302_03019/figure_3.png
pdfUrl: https://arxiv.org/pdf/2302.03019v2
published: '2023-02-06T18:57:04+00:00'
theme: Theoretical Physics
title: 'Geometry of contact: contact planning for multi-legged robots via spin models
  duality'
wordCount: 1130
---

## The Big Picture

Watch a centipede navigate a cluttered forest floor. Twenty-four legs, each touching and lifting in a rippling wave, somehow coordinating into seamless forward motion. Now imagine trying to program that.

Which leg touches down first? When? In what order do the joints bend? The number of possible combinations is enormous, and yet evolution solved it. Roboticists are still catching up.

For engineers building multi-legged robots, **contact planning** (deciding exactly when each limb should push against the ground and when it should swing free) is one of the hardest unsolved problems in locomotion. Most algorithms work well for bipeds and quadrupeds moving forward. Scaling to six, twelve, or more legs moving in arbitrary directions turns a manageable problem into a computational nightmare. The number of possible stepping combinations grows exponentially with the number of legs.

A team spanning Georgia Tech, MIT, and Harvard's IAIFI found an unexpected shortcut. By borrowing a framework from **statistical physics**, the branch of physics that studies how large-scale behaviors like magnetism emerge from countless tiny interactions, they can map the entire contact planning problem onto a **spin model**: the same mathematical structure used to describe magnets at the atomic scale. Better still, they can solve it in **polynomial time**, meaning the computation stays fast as the number of legs grows rather than blowing up.

> **Key Insight:** Locomotion symmetry turns contact planning into a physics-style spin model. This lets researchers find globally optimal gaits for hexapods and centipedes without exhaustive search.

## How It Works

The approach begins with **geometric mechanics**, a mathematical framework that describes how a robot's body moves as a consequence of its internal shape changes: the bending of joints, the swinging of limbs. The central object is the **local connection matrix** A(**r**), which encodes how a given pattern of ground contact translates joint-movement speed into whole-body displacement. Think of it as a gear ratio that depends on which feet are touching the ground.

![Figure 1](figure:1)

Once you fix the sequence of internal shape changes, the optimal contact sequence (which feet should be on the ground at each moment) can be derived directly from the geometry. That collapses one half of the problem entirely.

The remaining half, finding the best internal shape sequence, is still a hard combinatorial search. But locomotion gaits have **spatio-temporal symmetry**: the pattern of motion repeats across legs and across gait cycles. The researchers exploited this structure by reformulating the search as a graph optimization problem. Each node represents a candidate sequence of joint movements; edges connect mutually compatible sequences. The goal is the combination with the lowest total cost.

![Figure 2](figure:2)

Then comes the physics trick. That graph optimization maps exactly onto special cases of **spin models**, mathematical models from statistical physics where variables (tiny atomic magnets) interact with neighbors and settle naturally into the lowest-energy arrangement. Finding the optimal gait is equivalent to finding the **ground state**, the lowest-energy configuration, of the spin system. These particular spin models can be solved exactly and efficiently, in polynomial time rather than exponential.

The full workflow:
1. **Set up the geometric model**: define joint angles and use Resistive Force Theory to compute contact forces from the ground's push-back on moving legs.
2. **Enumerate candidate shape sequences**: exploit spatio-temporal symmetry to keep this set manageable.
3. **Map to a spin model**: encode the optimization objective as interaction energies between spin variables.
4. **Solve for the ground state**: find the globally optimal gait in polynomial time.
5. **Read back the contact sequence**: geometric mechanics delivers the optimal footfall pattern automatically.

## Why It Matters

The team tested their framework on two robots. For a hexapod, they recovered known gaits like the **alternating tripod**, where three legs move together while the other three are planted, and discovered new sidewinding behaviors. Sidewinding is a motion mode typically associated with snakes, now adapted to a six-legged platform. For a **12-legged centipede robot**, they identified effective forward gaits in a regime where prior methods had no systematic approach at all.

![Figure 4](figure:4)

The predictions weren't just theoretical. The researchers built purpose-built test robots and ran them through the predicted gaits. Agreement between model predictions and actual robot behavior was strong, validating the entire pipeline from spin model to rolling machine.

The framework requires no real-time sensors and no onboard computation during locomotion. Planning happens offline; the robot executes the pre-computed gait open-loop, following the plan without checking sensor feedback along the way. This makes it well-suited for cheap robots, small robots, or robots operating in sensor-degraded environments like search-and-rescue missions.

What's unusual here is the way physics pays off in robotics, not through simulation or neural networks, but through the structural mathematics physicists use to understand magnets and phase transitions. The spin model duality isn't just a computational trick. It tells us something about locomotion geometry itself: optimal gaits are, in a precise mathematical sense, ground states of a physical system.

The approach scales where prior methods fail. A hexapod already strains conventional contact planning; a 12-legged centipede is essentially out of reach. Polynomial-time spin model optimization opens the door to robots with even more legs: myriapod machines, modular snake-like systems, or distributed soft robots where the combinatorial space of gaits is otherwise intractable. How the framework handles unpredictable terrain, where the substrate changes the local connection matrix in real time, remains an open question and a natural next step.

> **Bottom Line:** The team turned a hard robotics problem into a solvable physics problem, mapping optimal gait design for multi-legged robots onto spin models. The result is globally optimal contact planning in polynomial time and new locomotion behaviors that brute-force methods couldn't find.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects statistical physics and robotics by showing that contact planning optimization for multi-legged locomotors is mathematically dual to spin model ground-state problems, a connection that produces both theoretical insight and practical algorithms.
- **Impact on Artificial Intelligence:** The framework provides a principled, geometry-driven alternative to data-hungry reinforcement learning for robot locomotion, achieving globally optimal gait design without onboard sensing or real-time computation.
- **Impact on Fundamental Interactions:** By applying geometric mechanics and spin model physics to locomotion, the work exposes structural connections between the symmetry of physical motion and the mathematical formalisms of condensed matter physics.
- **Outlook and References:** Future work may extend this framework to adaptive terrain-aware locomotion and robots with even higher leg counts; the full paper is available at [arXiv:2302.03019](https://arxiv.org/abs/2302.03019).
