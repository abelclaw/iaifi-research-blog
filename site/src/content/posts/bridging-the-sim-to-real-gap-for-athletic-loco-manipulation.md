---
abstract: 'Achieving athletic loco-manipulation on robots requires moving beyond traditional
  tracking rewards - which simply guide the robot along a reference trajectory - to
  task rewards that drive truly dynamic, goal-oriented behaviors. Commands such as
  "throw the ball as far as you can" or "lift the weight as quickly as possible" compel
  the robot to exhibit the agility and power inherent in athletic performance. However,
  training solely with task rewards introduces two major challenges: these rewards
  are prone to exploitation (reward hacking), and the exploration process can lack
  sufficient direction. To address these issues, we propose a two-stage training pipeline.
  First, we introduce the Unsupervised Actuator Net (UAN), which leverages real-world
  data to bridge the sim-to-real gap for complex actuation mechanisms without requiring
  access to torque sensing. UAN mitigates reward hacking by ensuring that the learned
  behaviors remain robust and transferable. Second, we use a pre-training and fine-tuning
  strategy that leverages reference trajectories as initial hints to guide exploration.
  With these innovations, our robot athlete learns to lift, throw, and drag with remarkable
  fidelity from simulation to reality.'
arxivId: '2502.10894'
arxivUrl: https://arxiv.org/abs/2502.10894
authors:
- Nolan Fey
- Gabriel B. Margolis
- Martin Peticco
- Pulkit Agrawal
concepts:
- reinforcement learning
- sim-to-real transfer
- fine-tuning
- transfer learning
- actuator dynamics modeling
- reward optimization
- surrogate modeling
- robustness
- whole-body loco-manipulation
- loss function design
- self-supervised learning
figures:
- /iaifi-research-blog/figures/2502_10894/figure_1.png
pdfUrl: https://arxiv.org/pdf/2502.10894v1
published: '2025-02-15T20:18:37+00:00'
theme: Foundational AI
title: Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation
wordCount: 1226
---

## The Big Picture

Imagine teaching someone to throw a javelin by telling them to precisely copy an Olympic athlete's arm angles frame by frame. They might reproduce the motion reasonably well, but they'd never discover the small adjustments that let the best athletes hurl the spear farther than anyone thought possible. The same tension haunts robotics.

Most approaches to training robots for dynamic motion force them to mimic a **reference trajectory** (a pre-recorded sequence of exact body positions to follow), stifling the discovery of genuinely athletic strategies. What happens when you let the robot figure it out on its own?

That question drives a new paper from MIT's Improbable AI Lab. The challenge is **loco-manipulation** (locomotion plus manipulation): tasks that demand a robot simultaneously move around *and* manipulate objects using its full body, the way a human lifts a heavy barbell by driving through the legs and hips, not just the arms.

For a 60-kilogram four-legged robot with a robotic arm mounted on its back, "throw the ball as far as you can" is a wildly different command than "follow this joint angle sequence." The former demands creativity and power; the latter demands compliance. The researchers wanted the former.

The result is a training pipeline that teaches a robot to lift, throw, and drag with what the authors call "remarkable fidelity." Not by copying humans, but by learning physics-grounded strategies in simulation that actually transfer to the real world.

> **Key Insight:** The biggest obstacle to giving robots true athletic freedom isn't the learning algorithm. It's the gap between simulated physics and reality. Fix the simulation, and the robot can discover its own winning strategies.

## How It Works

**Reward hacking** (where a robot finds sneaky shortcuts that boost its score without actually completing the task) is the central headache in reinforcement learning (RL), the trial-and-error method where an agent learns by receiving rewards for good outcomes. And it's largely a symptom of a bad simulation.

When you tell a robot to maximize the distance of a thrown ball, its learned strategy (called a *policy*) will exploit flaws in the simulated physics. The arm might snap to an impossible configuration, or the gripper might release at a moment that looks great in simulation but causes the robot to tumble in reality.

The standard fix is to add extra penalty terms and tracking objectives. But that brings you right back to the imitation problem.

![Figure 1](/iaifi-research-blog/figures/2502_10894/figure_1.png)

The MIT team's first innovation addresses the simulation problem directly. They introduce the **Unsupervised Actuator Net (UAN)**, a learned corrective model for actuator dynamics: a neural network that teaches the simulator how the real robot's motors actually behave.

The robot uses harmonic drive actuators, gear systems notorious for **non-linear friction**, **hysteresis** (a lag where a motor responds differently depending on whether it's speeding up or slowing down), and response lag. These behaviors are nearly impossible to capture with hand-tuned physics parameters.

Previous approaches required torque sensors (devices that measure the twisting force a motor actually delivers) to record what the actuator was doing. UAN sidesteps this entirely. Instead of measuring torques, it learns to predict **corrective torques**, small adjustments δ**τ** that nudge the simulated actuator to behave like the real one. The training signal is simply the discrepancy between simulated and real joint encoder readings (position and velocity), which any robot can provide.

The UAN runs as an RL agent inside the simulator, minimizing the mismatch between simulated and real transition dynamics. The result: a simulator that behaves like the actual hardware, without a single torque sensor.


A better simulator is only half the battle. The team's second challenge: **guided exploration**. Pure task rewards give the robot enormous freedom but almost no direction. The solution is to use reference trajectories not as strict commands, but as *hints* that warm-start exploration.

Training unfolds in two sub-phases:

1. **Pre-training**: The **whole-body controller (WBC)** (the system coordinating all 19 joints simultaneously) learns to track arbitrary base velocity and end-effector pose commands. ("End-effector" refers to the tip of the arm: the part that grabs and moves objects.) This builds a general motion prior without any specific task in mind.
2. **Fine-tuning**: For each athletic task (throwing, lifting, snatching a dumbbell, dragging a sled), the policy initializes from a reference trajectory. Reasonable performance comes for free. But the reward signal is the *task outcome*, not trajectory adherence, so the policy actively learns when to deviate from the reference to do better.

The reference trajectory isn't a leash. It's a suggestion. The robot uses it to bootstrap, then discards or modifies whatever parts it finds suboptimal.


The robot is a Unitree B2 quadruped (65 centimeters tall, 60 kilograms) carrying a modified Unitree Z1 Pro arm with 6 degrees of freedom (six independent ways the arm can rotate and extend). All 19 actuated joints must coordinate simultaneously during tasks like a dumbbell snatch, where the legs drive into the ground while the arm explosively lifts a weight overhead. That's a coordination problem that would challenge most robots running conventional controllers.

## Why It Matters

The implications stretch beyond impressive robot videos. The **sim-to-real gap** (the mismatch between how a robot behaves in simulation versus the physical world) has been one of the most persistent barriers to deploying learned behaviors in real environments.

**Domain randomization** (the standard approach of training across randomly varied physics parameters to build robustness) assumes you know what to randomize. For complex actuators with hysteresis and lag, those assumptions often fail silently. UAN offers a more principled path: measure the discrepancy directly and learn to close it, without expensive sensing infrastructure.

The pre-training and fine-tuning strategy also points toward a future where robots accumulate motion skills the way humans do. A child learning to throw a baseball draws on years of general movement experience, not a blank slate. A robot with a strong motion prior, fine-tuned for specific athletic tasks, follows that same developmental arc. The same framework could extend to contact-rich manipulation, parkour, or any task where the optimal strategy is genuinely hard to specify in advance.

Open questions remain. UAN currently learns a single corrective model per robot; whether it generalizes across different hardware configurations or wear states is unclear. And reference trajectory hints still require an initial demonstration. Automating that seeding process would bring the approach closer to fully autonomous skill acquisition.

> **Bottom Line:** By learning to close the simulation-reality gap for complex actuators (without torque sensors) and treating reference motions as hints rather than mandates, this approach lets robots discover genuinely athletic behaviors that transfer reliably from simulation to the real world.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects reinforcement learning and physical robotics through data-driven actuator modeling, tackling a problem at the intersection of machine learning, control theory, and actuator mechanics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">UAN shows that learning corrective dynamics models from encoder data alone, with no torque sensing required, can enable sim-to-real transfer for high-dimensional, contact-rich control tasks.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By accurately modeling non-linear friction, hysteresis, and lag in harmonic drive actuators, this research advances our understanding of how physical transmission mechanisms can be faithfully represented in learned simulation environments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending UAN to cross-platform generalization and automating reference trajectory generation. The full paper is available at [arXiv:2502.10894](https://arxiv.org/abs/2502.10894).</span></div></div>
</div>
