---
abstract: Controlling contact forces during interactions is critical for locomotion
  and manipulation tasks. While sim-to-real reinforcement learning (RL) has succeeded
  in many contact-rich problems, current RL methods achieve forceful interactions
  implicitly without explicitly regulating forces. We propose a method for training
  RL policies for direct force control without requiring access to force sensing.
  We showcase our method on a whole-body control platform of a quadruped robot with
  an arm. Such force control enables us to perform gravity compensation and impedance
  control, unlocking compliant whole-body manipulation. The learned whole-body controller
  with variable compliance makes it intuitive for humans to teleoperate the robot
  by only commanding the manipulator, and the robot's body adjusts automatically to
  achieve the desired position and force. Consequently, a human teleoperator can easily
  demonstrate a wide variety of loco-manipulation tasks. To the best of our knowledge,
  we provide the first deployment of learned whole-body force control in legged manipulators,
  paving the way for more versatile and adaptable legged robots.
arxivId: '2405.01402'
arxivUrl: https://arxiv.org/abs/2405.01402
authors:
- Tifanny Portela
- Gabriel B. Margolis
- Yandong Ji
- Pulkit Agrawal
concepts:
- reinforcement learning
- contact force regulation
- whole-body loco-manipulation
- sim-to-real transfer
- reward optimization
- transfer learning
- impedance control
- loss function design
- multi-task learning
figures:
- /iaifi-research-blog/figures/2405_01402/figure_1.png
- /iaifi-research-blog/figures/2405_01402/figure_1.png
- /iaifi-research-blog/figures/2405_01402/figure_2.png
- /iaifi-research-blog/figures/2405_01402/figure_2.png
- /iaifi-research-blog/figures/2405_01402/figure_3.png
- /iaifi-research-blog/figures/2405_01402/figure_3.png
pdfUrl: https://arxiv.org/pdf/2405.01402v2
published: '2024-05-02T15:53:43+00:00'
theme: Foundational AI
title: Learning Force Control for Legged Manipulation
wordCount: 1089
---

## The Big Picture

Imagine trying to thread a needle while wearing oven mitts. That's roughly the challenge facing most robot arms when they interact with the physical world: they know where to move, but they have no intuitive sense of *how hard* to push. Too little force and the task fails. Too much, and something breaks — or someone gets hurt. For four-legged robots like quadrupeds, this problem compounds dramatically, because every step the legs take ripples through the entire body and changes the forces at the arm's tip.

Researchers at MIT's Improbable AI Lab have cracked open a new approach. Most robot controllers today achieve forceful interactions only as a side effect of position commands — they keep moving the arm until it reaches a target location, with force being whatever happens to result from that motion. What this team built instead is a controller that can be directly *told* how hard to push, coordinating the robot's entire body — all four legs and the arm together — to hit that target precisely.

The result is a four-legged robot with an arm that feels the world the way a skilled human technician does: with calibrated, controllable touch.

> **Key Insight:** By training a reinforcement learning policy to track explicit force commands — without any dedicated force sensors — the researchers unlocked compliant, whole-body manipulation on a quadruped robot, making it intuitive for humans to teleoperate and opening the door to safer, more versatile robotic assistants.

## How It Works

The core innovation lives in how the team reframed the learning problem. Standard **sim-to-real reinforcement learning (RL)** — training a robot policy in a physics simulation, then deploying it in the real world — has become the dominant paradigm for legged locomotion. But those policies typically learn to achieve positions, not forces. The MIT team added a force-tracking objective directly into the training loop.

![Figure 2](/iaifi-research-blog/figures/2405_01402/figure_1.png)

Here's the clever part: rather than equipping the robot with expensive **wrist force-torque sensors**, the policy learns to estimate contact forces entirely from **proprioception** — the robot's internal sense of its own joint positions, velocities, and motor torques. No additional hardware required. The policy infers how hard the gripper is pushing from the same signals a human feels as muscle tension and joint resistance.

Training happens in a carefully designed simulation environment. The researchers place the robot in a virtual "potential field" — a simulated spring pulling the gripper toward a randomized target point. This forces the policy to push against varying resistances and learn what different force magnitudes feel like proprioceptively. The policy receives three types of commands simultaneously:

- A **base velocity command** telling the body where to walk
- An **end-effector position command** telling the arm where to place the gripper (the end-effector is the tool at the tip of the arm)
- A **force command** specifying how hard to press at the gripper

The learned **whole-body controller** — a single neural network coordinating all four legs and the arm at once — executes all of these simultaneously. When the arm needs to push harder, the legs automatically shift weight and reposition the torso to provide a stable mechanical foundation. The human teleoperator doesn't manage any of this; they simply command "push with 10 Newtons" and the robot handles the rest.

![Figure 1](/iaifi-research-blog/figures/2405_01402/figure_1.png)

This architecture unlocks two classical control behaviors that roboticists have prized for decades. **Gravity compensation** makes the arm feel weightless when a human physically guides it — the robot cancels out its own arm's mass so a person can guide it through tasks by hand, as if it weighed nothing. **Impedance control** lets the operator set the gripper's effective stiffness: dial it up for precise positioning, dial it down for compliant contact with fragile or irregular surfaces. Both behaviors emerge from the same learned force controller, simply by changing the commanded force profile.

## Why It Matters

This work sits at a critical junction in robotics: the gap between "robots that can move" and "robots that can *do things*." Legged robots have become remarkably capable at locomotion — running, jumping, navigating rubble, recovering from falls. Manipulation robots have mastered dexterous grasping and assembly. But combining both, with the finesse to interact safely with humans and fragile environments, has remained stubbornly difficult.

Force control is the missing ingredient for a wide class of real-world tasks. Think of a robot that needs to wipe a surface without scratching it, tighten a bolt to a specific torque, or help an elderly person stand without jerking. All of these require not just knowing *where* to move, but *how hard* to push at every instant.

The fact that the MIT team achieved this without force sensors matters enormously for deployment. Sensors add cost, fragility, and failure modes. A robot that infers forces from its own proprioception is more robust and cheaper to build.

The teleoperation angle is particularly significant. By making force a first-class commanded quantity, the researchers made it easy for a single human operator to demonstrate complex manipulation tasks — pulling open drawers, handling objects with varying weights, applying sustained pressure. That demonstrated data becomes fuel for the next generation of imitation learning systems, potentially accelerating the path toward robots that learn manipulation from human demonstrations at scale.

> **Bottom Line:** MIT researchers trained a quadruped robot to directly control the forces it applies — without force sensors — by learning from simulation alone. The result is the first legged robot to deploy learned whole-body force control in the real world, enabling compliant, intuitive manipulation that could transform how robots assist humans in unstructured environments.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges reinforcement learning theory with classical robotics concepts like impedance control and gravity compensation, demonstrating that learned neural policies can recover principled force-regulation behaviors without explicit physics-based programming.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The research advances sim-to-real RL by introducing explicit force-tracking objectives and proprioceptive force estimation, expanding the expressivity of learned policies beyond position control into compliant physical interaction.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By modeling contact mechanics through a potential-field training environment and proprioceptive feedback, the work deepens our understanding of how physical interaction forces can be represented and regulated in learned dynamical systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend this framework to tasks requiring precise force profiles — such as surgical assistance or material testing — and integration with tactile sensing could yield even richer contact feedback; see arXiv for the full paper by Portela, Margolis, Ji, and Agrawal.</span></div></div>
</div>
