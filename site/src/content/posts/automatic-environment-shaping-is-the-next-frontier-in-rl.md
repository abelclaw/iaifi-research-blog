---
abstract: Many roboticists dream of presenting a robot with a task in the evening
  and returning the next morning to find the robot capable of solving the task. What
  is preventing us from achieving this? Sim-to-real reinforcement learning (RL) has
  achieved impressive performance on challenging robotics tasks, but requires substantial
  human effort to set up the task in a way that is amenable to RL. It's our position
  that algorithmic improvements in policy optimization and other ideas should be guided
  towards resolving the primary bottleneck of shaping the training environment, i.e.,
  designing observations, actions, rewards and simulation dynamics. Most practitioners
  don't tune the RL algorithm, but other environment parameters to obtain a desirable
  controller. We posit that scaling RL to diverse robotic tasks will only be achieved
  if the community focuses on automating environment shaping procedures.
arxivId: '2407.16186'
arxivUrl: https://arxiv.org/abs/2407.16186
authors:
- Younghyo Park
- Gabriel B. Margolis
- Pulkit Agrawal
concepts:
- reinforcement learning
- environment shaping
- sim-to-real transfer
- reward optimization
- automated discovery
- scalability
- transfer learning
- automatic curriculum design
- loss function design
- surrogate modeling
- active learning
figures:
- /iaifi-research-blog/figures/2407_16186/figure_1.png
- /iaifi-research-blog/figures/2407_16186/figure_2.png
- /iaifi-research-blog/figures/2407_16186/figure_3.png
pdfUrl: https://arxiv.org/pdf/2407.16186v1
published: '2024-07-23T05:22:29+00:00'
theme: Foundational AI
title: Automatic Environment Shaping is the Next Frontier in RL
wordCount: 1001
---

## The Big Picture

Imagine handing a new intern a task at 5 PM and walking in the next morning to find it done perfectly. No hand-holding, no tweaking the instructions, no staying late to troubleshoot. That's the dream roboticists have been chasing for decades — and it turns out the obstacle isn't what most people think.

The conventional wisdom says we need better learning algorithms. Smarter optimization, more efficient trial-and-error, cleverer software designs. But a position paper from MIT's Improbable AI Lab argues this is the wrong place to look. The real bottleneck is something unglamorous: the enormous amount of human labor required to *set up the training environment* before learning even begins.

Before you can train a robot to load a dishwasher, someone has to define what it can observe, how it can move, what counts as success, and how the simulation should behave. That process — called **environment shaping** — is the hidden tax on every robotics AI project. The researchers' thesis: the field will only scale to truly general robotics if we automate environment shaping itself.

> **Key Insight:** Environment shaping — designing rewards, observations, actions, and simulation dynamics — is the primary bottleneck in scaling reinforcement learning to diverse robotic tasks, and the community should treat its automation as a first-class research priority.

## How It Works

The MIT team studies **reinforcement learning (RL)** — a method where a robot learns by trial and error inside a simulation, then transfers that behavior to the real world. They break this process into four stages:

1. **Sample environment modeling** — building a simulation: importing robot and asset models, placing objects in their default poses
2. **Environment shaping** — the human-intensive design work: crafting reward functions, defining observations, choosing action representations, specifying curricula
3. **RL training** — running the algorithm inside the shaped simulator
4. **Outer feedback loop** — evaluating the learned behavior and iterating

![Figure 1](/iaifi-research-blog/figures/2407_16186/figure_1.png)

Most research attention flows to stage three. But the paper argues that practitioners almost never tune the algorithm — they tune the environment.

A roboticist wrestling with a four-legged robot (a "quadruped") that won't learn to walk isn't tweaking the underlying learning equations. They're redesigning the reward function, restricting the action space, adjusting the difficulty of the terrain curriculum.

The paper defines environment shaping precisely: every design choice made to make training tractable that isn't strictly required to model the physics of the task. A reward function that penalizes falling is environment shaping. So is giving the robot access to its own joint velocities. So is starting training on flat ground before introducing stairs. None of these choices flow automatically from "teach the robot to walk" — a human expert has to invent them.

![Figure 2](/iaifi-research-blog/figures/2407_16186/figure_2.png)

The dishwasher example is instructive. Modeling the true distribution of real-world dishwashers — every brand, loading configuration, water pressure, soap residue — is intractable. So you pick a representative sample, call it a **reference environment**, and design your shaping choices to work on that. The problem: every new robot and every new task requires re-inventing these choices from scratch, with no principled way to transfer expertise across problems.

The paper catalogs where human effort concentrates: designing reward functions (often weeks of iteration), crafting observations that include the right signals, selecting action representations that make the problem tractable, and specifying **domain randomization** — intentionally varying simulation parameters like lighting, friction, and object weights so the robot learns to handle real-world variability. Each is a form of expert knowledge that currently lives in researchers' heads and doesn't generalize.

## Why It Matters

This is a position paper — it's making an argument, not presenting a new algorithm. And the argument lands hard.

The paper arrives at a moment when large language models have demonstrated that the right abstraction plus scale can dissolve problems that previously required painstaking hand-engineering. The same transition happened in computer vision (from manually coded rules about edges and corners to learned representations) and in language processing (from hand-built grammar rules to models that learn from vast text). The authors are betting robotics is next — but only if the community stops optimizing the RL algorithm and starts automating the scaffolding around it.

The concrete path forward involves treating environment shaping as a learnable, automatable process. LLMs already show early promise in generating reward functions from natural language task descriptions. Curriculum design can be framed as a **meta-learning** problem — where a system learns *how to set up learning tasks*, not just how to solve them. Domain randomization ranges can be inferred from real-world data.

Each of these is a research direction. The paper is a call to organize the community around them as a coherent program rather than isolated tricks. The long-term prize: a robot you can hand a task description in the evening and trust to figure out the rest.

> **Bottom Line:** The next breakthrough in robotics won't come from better RL algorithms — it'll come from automating the unglamorous work of environment design that currently requires expert human labor for every new task. This paper names that problem and makes the case that solving it is the field's most urgent priority.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges theoretical RL research and practical robotics deployment, identifying the human-in-the-loop bottleneck that prevents AI systems from autonomously acquiring physical skills at scale.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper reframes a longstanding assumption in RL research — that algorithmic advances are the primary lever — and argues that meta-level automation of training environment design is the more impactful frontier.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By targeting the scalability of sim-to-real transfer, this work addresses a core obstacle to deploying intelligent physical agents that interact robustly with the messy, variable structure of the real world.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The paper calls for systematic research into automated reward design, curriculum generation, and observation/action space optimization; the full position paper is available via ICML 2024 proceedings (arXiv: 2407.xxxxx, PMLR 235, 2024).</span></div></div>
</div>
