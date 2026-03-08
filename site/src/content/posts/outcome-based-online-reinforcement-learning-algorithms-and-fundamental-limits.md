---
abstract: 'Reinforcement learning with outcome-based feedback faces a fundamental
  challenge: when rewards are only observed at trajectory endpoints, how do we assign
  credit to the right actions? This paper provides the first comprehensive analysis
  of this problem in online RL with general function approximation. We develop a provably
  sample-efficient algorithm achieving $\widetilde{O}({C_{\rm cov} H^3}/{ε^2})$ sample
  complexity, where $C_{\rm cov}$ is the coverability coefficient of the underlying
  MDP. By leveraging general function approximation, our approach works effectively
  in large or infinite state spaces where tabular methods fail, requiring only that
  value functions and reward functions can be represented by appropriate function
  classes. Our results also characterize when outcome-based feedback is statistically
  separated from per-step rewards, revealing an unavoidable exponential separation
  for certain MDPs. For deterministic MDPs, we show how to eliminate the completeness
  assumption, dramatically simplifying the algorithm. We further extend our approach
  to preference-based feedback settings, proving that equivalent statistical efficiency
  can be achieved even under more limited information. Together, these results constitute
  a theoretical foundation for understanding the statistical properties of outcome-based
  reinforcement learning.'
arxivId: '2505.20268'
arxivUrl: https://arxiv.org/abs/2505.20268
authors:
- Fan Chen
- Zeyu Jia
- Alexander Rakhlin
- Tengyang Xie
concepts:
- reinforcement learning
- outcome-based feedback
- credit assignment
- reward optimization
- coverability coefficient
- stochastic processes
- active learning
- scalability
- bayesian inference
figures: []
pdfUrl: https://arxiv.org/pdf/2505.20268v2
published: '2025-05-26T17:44:08+00:00'
theme: Foundational AI
title: 'Outcome-Based Online Reinforcement Learning: Algorithms and Fundamental Limits'
wordCount: 1291
---

## The Big Picture

Imagine you're a chess coach watching a student play a full game. At the end, you say "that was a great game," but never tell them which moves were brilliant or which were blunders. Could your student still improve?

Now imagine doing this for a robot learning to walk, or an AI learning to write poetry. You give it one thumbs up or thumbs down at the very end, nothing in between. How does it figure out which of its hundreds of decisions actually mattered?

This is the **credit assignment problem** in machine learning: the challenge of tracing a final outcome back to the individual decisions that caused it. It gets brutally hard when feedback only arrives at the end of an entire sequence of actions. And this is exactly how we train many real-world AI systems.

When humans rate a chatbot's response, they judge the whole output, not word by word. When clinical trials evaluate a treatment, they measure final patient outcomes, not moment-to-moment progress. Despite how common this situation is, the mathematical foundations for learning efficiently under endpoint-only feedback have stayed surprisingly underdeveloped.

A new paper from researchers at MIT and the University of Wisconsin–Madison gives the first complete mathematical treatment of **online reinforcement learning** with outcome-based feedback. In online RL, an agent learns by acting in an environment and observing the consequences. The results include provably efficient algorithms and a precise characterization of when this problem is tractable, and when it's exponentially hard.

> **Key Insight:** Learning from endpoint-only feedback is sometimes just as efficient as learning from per-step rewards, but for some problems, the difference is exponential. Knowing which case you're in is half the battle.

## How It Works

The problem is framed using **Markov Decision Processes (MDPs)**, the standard mathematical model for sequential decision-making. Think of it as a map of states the agent can be in, actions it can take, and rewards it collects along the way.

In standard reinforcement learning, the agent sees a reward after every action. In the outcome-based setting, it only sees a single number at the very end: the sum of all step-level rewards, collapsed into one signal. The **horizon** H is the total number of steps per episode.

The central challenge: this can't be reduced to a simpler problem where each decision is independent (what researchers call a **bandit problem**) because the number of possible action sequences grows exponentially with H. Instead of trying to reconstruct step-level rewards from the final outcome, the key insight is that you can still learn useful **value functions** (estimates of how good each state is, in terms of expected future reward) if the problem has the right structure.

The main algorithm achieves a **sample complexity** (the number of learning episodes needed to find a near-optimal **policy**, i.e., the agent's decision strategy) of:

**Õ(C_cov · H³ / ε²)**

Breaking this down:
- **ε** is how close to optimal you need to be
- **H** is the horizon length; cubic dependence is the price of not knowing step-level rewards
- **C_cov** is the **coverability coefficient**, a measure of how "explorable" the MDP is. A low value means a single policy can visit most relevant states; a high value means the state space is sprawling and hard to cover

The algorithm makes no assumptions about state space structure. It uses **general function approximation**, meaning value functions just need to be representable by appropriate function classes (neural networks, polynomials, decision trees). Prior work required linear reward functions, a restrictive assumption that fails in many real scenarios. This removes that limitation.

Two standard assumptions apply:
- **Realizability**: the true value functions lie within the chosen function class
- **Completeness**: the **Bellman backup** (the operation that propagates value estimates backwards through time), applied to any function in the class, stays within that class

For **deterministic MDPs**, where transitions are fixed rather than random, the completeness assumption can be dropped entirely. A simpler algorithm based on **Bellman residual minimization** (measuring and minimizing prediction error in value estimates) achieves similar theoretical guarantees while being more computationally tractable.

## Why It Matters

The most striking result isn't the algorithm itself. It's the **exponential separation theorem**. The researchers construct a specific MDP with known transitions, a horizon of just H = 2, and a d-dimensional generalized linear reward function. With per-step feedback, existing algorithms solve this in roughly O(d²/ε²) episodes. With outcome-based feedback only, they prove that e^Ω(d) samples are *necessary*. No algorithm, no matter how clever, can do better.

This tells practitioners something concrete: reward function structure matters enormously when designing systems that learn from end-of-sequence feedback. Outcome-based feedback can match step-level feedback in well-structured settings, but for certain problem geometries, the information loss is catastrophic and irreversible.

The paper also extends its framework to **preference-based feedback**, the setting used in reinforcement learning from human feedback (RLHF). Instead of a scalar reward, you get binary comparisons between trajectories ("this response was better than that one"). Under the **Bradley-Terry-Luce model** (a standard probabilistic model that converts pairwise preferences into probabilities), the same statistical efficiency can be achieved as with outcome rewards. This puts RLHF on firmer mathematical ground, tying the theory to how systems like ChatGPT are actually trained.

The open questions now sharpen: Can the H³ dependence be improved? Are there natural problem classes beyond deterministic MDPs where completeness can be relaxed? And can these algorithms be made computationally efficient enough to deploy at scale?

> **Bottom Line:** This paper establishes the first complete theoretical picture of outcome-based online RL with general function approximation, proving when endpoint feedback is enough to learn efficiently and when it creates an exponential barrier that no algorithm can overcome.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects abstract RL theory to the practical challenge of training large language models from human feedback, putting the mathematics behind RLHF on solid footing.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper delivers the first provably sample-efficient algorithm for outcome-based online RL with general function approximation, alongside a sharp exponential lower bound that defines the fundamental limits of the problem.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By characterizing when trajectory-level feedback is statistically equivalent to per-step feedback, the results offer concrete guidance for learning systems in scientific domains (clinical trials, experimental physics pipelines) where only final outcomes are observable.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will focus on tightening the horizon dependence, extending results to richer feedback models, and moving toward computationally practical implementations; the paper is available at [arXiv:2505.20268](https://arxiv.org/abs/2505.20268).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Outcome-Based Online Reinforcement Learning: Algorithms and Fundamental Limits</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2505.20268</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Fan Chen", "Zeyu Jia", "Alexander Rakhlin", "Tengyang Xie"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Reinforcement learning with outcome-based feedback faces a fundamental challenge: when rewards are only observed at trajectory endpoints, how do we assign credit to the right actions? This paper provides the first comprehensive analysis of this problem in online RL with general function approximation. We develop a provably sample-efficient algorithm achieving $\widetilde{O}({C_{\rm cov} H^3}/{ε^2})$ sample complexity, where $C_{\rm cov}$ is the coverability coefficient of the underlying MDP. By leveraging general function approximation, our approach works effectively in large or infinite state spaces where tabular methods fail, requiring only that value functions and reward functions can be represented by appropriate function classes. Our results also characterize when outcome-based feedback is statistically separated from per-step rewards, revealing an unavoidable exponential separation for certain MDPs. For deterministic MDPs, we show how to eliminate the completeness assumption, dramatically simplifying the algorithm. We further extend our approach to preference-based feedback settings, proving that equivalent statistical efficiency can be achieved even under more limited information. Together, these results constitute a theoretical foundation for understanding the statistical properties of outcome-based reinforcement learning.</span></div></div>
</div>
