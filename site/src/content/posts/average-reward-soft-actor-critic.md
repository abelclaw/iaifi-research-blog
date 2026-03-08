---
abstract: The average-reward formulation of reinforcement learning (RL) has drawn
  increased interest in recent years for its ability to solve temporally-extended
  problems without relying on discounting. Meanwhile, in the discounted setting, algorithms
  with entropy regularization have been developed, leading to improvements over deterministic
  methods. Despite the distinct benefits of these approaches, deep RL algorithms for
  the entropy-regularized average-reward objective have not been developed. While
  policy-gradient based approaches have recently been presented for the average-reward
  literature, the corresponding actor-critic framework remains less explored. In this
  paper, we introduce an average-reward soft actor-critic algorithm to address these
  gaps in the field. We validate our method by comparing with existing average-reward
  algorithms on standard RL benchmarks, achieving superior performance for the average-reward
  criterion.
arxivId: '2501.09080'
arxivUrl: https://arxiv.org/abs/2501.09080
authors:
- Jacob Adamczyk
- Volodymyr Makarenko
- Stas Tiomkin
- Rahul V. Kulkarni
concepts:
- reinforcement learning
- average-reward mdp
- entropy regularization
- actor-critic framework
- reward optimization
- loss function design
- stochastic processes
- robustness
- scalability
- bayesian inference
- uncertainty quantification
figures:
- /iaifi-research-blog/figures/2501_09080/figure_1.png
- /iaifi-research-blog/figures/2501_09080/figure_2.png
- /iaifi-research-blog/figures/2501_09080/figure_3.png
pdfUrl: https://arxiv.org/pdf/2501.09080v2
published: '2025-01-15T19:00:46+00:00'
theme: Foundational AI
title: Average-Reward Soft Actor-Critic
wordCount: 1082
---

## The Big Picture

Imagine training a dog by rewarding every trick it performs today slightly more than tricks it might perform next week (discounting the future). The dog learns fast, but it becomes weirdly shortsighted, optimizing for the next few minutes rather than becoming a well-behaved companion over years. Most modern AI agents work exactly this way, and it creates subtle but serious problems.

In **reinforcement learning** (where AI agents learn by collecting rewards through trial and error), tasks often run indefinitely: a robot walking, a trading algorithm ticking, a game with no natural end. For these situations, researchers commonly apply a **discount factor** (γ), a mathematical trick that makes future rewards worth less than immediate ones. It's convenient, but it introduces an arbitrary knob that must be tuned carefully. Set γ too low and the agent becomes reckless. Set it slightly wrong and performance collapses entirely. Worse, the agent ends up optimizing a quantity nobody actually cares about, since practitioners ultimately measure performance by average reward over time anyway.

A cleaner alternative exists: optimize for the **average reward** directly, asking how much reward per timestep the agent can earn in the long run. Researchers at UMass Boston, San José State, and Texas Tech have combined this more principled objective with a technique that encourages agents to keep their options open rather than prematurely locking in on a single strategy, producing a new algorithm called **Average-Reward Soft Actor-Critic (AR-SAC)** that outperforms existing approaches while requiring minimal changes to existing codebases.

> **Key Insight:** By marrying average-reward optimization with entropy regularization, AR-SAC eliminates the need for discount factor tuning while producing policies that are naturally stochastic and varied, a combination that previously had no practical deep RL implementation.

## How It Works

The standard workhorse of modern deep RL is **Soft Actor-Critic (SAC)**, an algorithm that learns by maximizing both reward and the entropy of its policy. The **temperature parameter** (β⁻¹) acts as a dial controlling how strongly the agent is rewarded for staying flexible rather than committing to a single action. The result is **stochastic** policies (randomly varying rather than rigidly deterministic) that generalize better and handle unexpected situations more gracefully. SAC has become a gold standard in the discounted setting.

The challenge is that average-reward RL operates differently at a mathematical level. In discounted RL, value functions satisfy a clean recursive structure called the **Bellman equation**, which contracts toward a unique solution, a property that makes optimization stable. Remove discounting and this contraction disappears. The math gets messier, and most existing deep RL tools simply don't apply.

![Figure 1](/iaifi-research-blog/figures/2501_09080/figure_1.png)

The authors resolve this by reformulating SAC's core quantities for the average-reward setting. Instead of a standard Q-function estimating discounted future rewards, AR-SAC tracks the **differential Q-function**, measuring how much better or worse a state-action pair performs relative to the agent's average reward rate ρ. The Bellman update subtracts this running reward rate at every step, keeping value estimates bounded without discounting. Entropy regularization is folded into this modified objective consistently, producing what the authors call the **Entropy-Regularized Average-Reward (ERAR) MDP** (Markov Decision Process, the standard mathematical model for sequential decisions) framework.

The resulting algorithm follows a familiar actor-critic structure:

- A **critic** network estimates the differential Q-function, updated by minimizing a modified Bellman residual that tracks the average reward rate
- An **actor** network updates the policy to maximize both expected differential value and policy entropy
- The **reward rate** ρ is learned online, adapting as the agent improves
- The **temperature** β⁻¹ is tuned automatically via a dual optimization trick inherited from SAC

Implementing AR-SAC requires only modest changes to an existing SAC codebase: remove the γ multiplier from the Bellman backup, add the reward rate estimate, and adjust the entropy target. Researchers who already use SAC can adapt without rebuilding their infrastructure.

## Why It Matters

The immediate practical payoff is freedom from discount factor tuning. Standard SAC on the Swimmer-v5 MuJoCo environment (a widely used physics simulator for robot locomotion) fails completely at its default γ = 0.99, and only careful manual tuning unlocks good performance. AR-SAC sidesteps this entirely. Benchmarks across standard continuous-control tasks show AR-SAC achieving superior performance on the average-reward criterion compared to existing average-reward algorithms, including policy-gradient-based methods (which improve behavior by estimating how small changes in strategy affect total reward) that previously represented the state of the art.

![Figure 2](/iaifi-research-blog/figures/2501_09080/figure_2.png)

The deeper significance lies in what this opens up for physics-informed AI. Many real-world physical systems (thermal machines, biological motor control, particle accelerators in steady-state operation) are inherently continuing tasks where long-run average performance is the meaningful objective. The entropy regularization also has a natural interpretation in statistical physics: maximizing entropy corresponds to finding the least-biased probability distribution consistent with observed constraints, a concept central to thermodynamics and information theory. Combining these ideas in a working deep RL algorithm creates tools better matched to problems at the intersection of AI and physics than standard discounted methods.

Open questions remain. Theoretical convergence guarantees for average-reward deep RL are weaker than in the discounted case, a gap the community is still working to close. Extending AR-SAC to offline settings, multi-agent systems, and partial observability are natural next steps. The authors also note their formulation handles general KL-divergence regularization relative to arbitrary reference policies, not just the standard maximum-entropy case, opening doors to incorporating prior knowledge into policy structure.

> **Bottom Line:** AR-SAC delivers a principled, practical deep RL algorithm for long-horizon continuous control that beats the competition without requiring discount factor tuning, and the stability benefits of entropy regularization come built in.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges statistical physics and reinforcement learning by formalizing entropy-regularized average-reward optimization, a framework where maximum-entropy principles from thermodynamics directly shape how AI agents learn optimal long-run behavior.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">AR-SAC is the first deep RL algorithm combining entropy regularization with the average-reward objective, achieving state-of-the-art performance on continuous control benchmarks while eliminating the need to tune the discount factor hyperparameter.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Average-reward RL is naturally suited to physical systems in steady-state or ergodic regimes; AR-SAC provides a practical tool for applying modern deep RL to problems in physics where long-run average performance (not discounted returns) is the correct objective.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work includes extending AR-SAC to offline learning and multi-agent settings. The paper is by Jacob Adamczyk, Volodymyr Makarenko, Stas Tiomkin, and Rahul V. Kulkarni, published in *Reinforcement Learning Journal* (2025). [[arXiv:2501.09080](https://arxiv.org/abs/2501.09080)]</span></div></div>
</div>
