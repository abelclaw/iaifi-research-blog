---
abstract: "As large language models have evolved, it has become crucial to distinguish\
  \ between process supervision and outcome supervision -- two key reinforcement learning\
  \ approaches to complex reasoning tasks. While process supervision offers intuitive\
  \ advantages for long-term credit assignment, the precise relationship between these\
  \ paradigms has remained an open question. Conventional wisdom suggests that outcome\
  \ supervision is fundamentally more challenging due to the trajectory-level coverage\
  \ problem, leading to significant investment in collecting fine-grained process\
  \ supervision data.\n  In this paper, we take steps towards resolving this debate.\
  \ Our main theorem shows that, under standard data coverage assumptions, reinforcement\
  \ learning through outcome supervision is no more statistically difficult than through\
  \ process supervision, up to polynomial factors in horizon. At the core of this\
  \ result lies the novel Change of Trajectory Measure Lemma -- a technical tool that\
  \ bridges return-based trajectory measure and step-level distribution shift. Furthermore,\
  \ for settings with access to a verifier or a rollout capability, we prove that\
  \ any policy's advantage function can serve as an optimal process reward model,\
  \ providing a direct connection between outcome and process supervision. These findings\
  \ suggest that the empirically observed performance gap -- if any -- between outcome\
  \ and process supervision likely stems from algorithmic limitations rather than\
  \ inherent statistical difficulties, potentially transforming how we approach data\
  \ collection and algorithm design for reinforcement learning."
arxivId: '2502.10581'
arxivUrl: https://arxiv.org/abs/2502.10581
authors:
- Zeyu Jia
- Alexander Rakhlin
- Tengyang Xie
concepts:
- reinforcement learning
- outcome vs process supervision
- reward optimization
- process reward modeling
- credit assignment
- stochastic processes
- fine-tuning
- scalability
- test-time scaling
- interpretability
figures: []
pdfUrl: https://arxiv.org/pdf/2502.10581v2
published: '2025-02-14T22:21:56+00:00'
theme: Foundational AI
title: Do We Need to Verify Step by Step? Rethinking Process Supervision from a Theoretical
  Perspective
wordCount: 1020
---

## The Big Picture

Imagine teaching a student to solve math problems. One approach: stand over their shoulder, correcting every line of algebra. Another: hand back only the final grade. Common sense says the first approach must be better. How can a student learn *where* they went wrong if you only tell them the final answer was right or wrong?

This intuition has shaped how the AI community trains large language models. For years, researchers have invested enormous effort (and money) in **process supervision** data: human annotators painstakingly marking each step of a model's reasoning chain as correct or incorrect. The alternative, **outcome supervision**, feels risky.

If a model produces a long chain of thought that reaches the wrong answer, which step derailed the reasoning? This is the **credit assignment problem**, and it seemed to make outcome supervision fundamentally harder, perhaps even impossible to solve reliably for long reasoning chains.

A new theoretical paper from MIT's Zeyu Jia, Alexander Rakhlin, and Tengyang Xie challenges that intuition head-on. Their conclusion is striking: mathematically, outcome supervision is *not* harder than process supervision. The performance gap we sometimes observe is a problem with our algorithms, not with the data.

> **Key Insight:** Under standard statistical assumptions, reinforcement learning from outcome supervision is no more difficult than from process supervision, suggesting that costly step-by-step annotation may not be as fundamental as the field has assumed.

## How It Works

In the language of **Markov Decision Processes (MDPs)**, a mathematical framework modeling decision-making as a sequence of choices and their consequences, an agent works through a **trajectory**: a complete sequence of reasoning steps from start to finish. With process supervision, the agent gets a reward signal at *every step*. With outcome supervision, it gets only a single reward at the *end*.

The conventional worry: if you only see rewards at the end, you cannot easily figure out how much credit each step deserves. One bad step early in a long reasoning chain might corrupt everything that follows, yet the final reward gives no direct pointer to that step. This is the **trajectory-level coverage problem**, the concern that outcome-supervised data can't adequately cover all the individual step-level distributions needed to learn a good policy.

The paper's central theorem demolishes this concern. The key technical move is what the authors call the **Change of Trajectory Measure Lemma**:

- Any dataset of trajectories with only final rewards can be *reweighted* to behave like a dataset with per-step rewards.
- The cost of this transformation scales with **state-action concentrability**, a measure of how well the data covers the state-action space, step by step.
- This is the *same* coverage requirement that process supervision already demands. Good step-level coverage is necessary either way.

The practical upshot: take any algorithm designed for process supervision, feed it outcome-supervised data transformed via this reweighting, and performance degrades by at most a polynomial factor in the horizon, not an exponential collapse. The hardness is essentially the same.

A second major result concerns a popular practical trick: using **Q-functions or advantage functions** as surrogate process reward models to extract step-level signals from outcome data. Many recent systems (including DeepSeek's work) do exactly this. The paper gives this practice rigorous theoretical backing, but with an important nuance.

The **advantage function**, which measures how much *better* a particular step is compared to the model's typical behavior, is provably an optimal process reward model. The **Q-function**, which measures the absolute expected reward from a given step onward, is *not*. Using it can lead to systematically suboptimal results. This distinction has real implications for which quantities practitioners should be estimating.

The analysis extends to **preference-based RL**, the framework behind methods like Direct Preference Optimization (DPO). When humans compare pairs of model outputs, the resulting data implicitly encodes outcome-level preferences across entire trajectories. The paper shows that DPO's data requirements scale with state-action concentrability coefficients, potentially an *exponential* improvement over previous analyses that relied on trajectory-level concentrability.

## Why It Matters

If outcome supervision is statistically equivalent to process supervision, then the field's massive investment in fine-grained human annotation (labeling every step of a model's chain of thought) may be solving the wrong problem. The bottleneck isn't in the *type* of data; it's in the *algorithms* used to learn from it. Future work should focus on closing the algorithmic gap, not on collecting ever more expensive step-level labels.

This also reframes recent empirical successes. Systems like DeepSeek-R1, which achieve strong reasoning performance using outcome-supervised RL, no longer look like lucky exceptions to a theoretical rule. They start to look like early confirmations of this theorem in action. The paper provides the theoretical scaffolding to understand *why* those systems work, and what limits might still exist.

The open questions now center on algorithm design: what specific algorithmic properties explain the performance differences we *do* see in practice, and can they be fixed?

> **Bottom Line:** A new theorem proves that outcome supervision is statistically no harder than process supervision for RL training, meaning the field's heavy investment in step-by-step annotation reflects algorithmic limitations, not mathematical necessity, pointing toward a richer theory of learning from sparse rewards.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies the rigorous mathematical toolkit of statistical learning theory (concentrability coefficients, change-of-measure arguments, MDP theory) to resolve a foundational question about how modern AI systems learn to reason, connecting pure mathematics and large-scale AI practice.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper provides the first formal proof that outcome supervision is statistically equivalent to process supervision up to polynomial factors, potentially redirecting how the field designs data collection pipelines and RL algorithms for language model training.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By establishing that the advantage function constitutes an optimal process reward model, the work provides a principled foundation for self-improvement methods, where models bootstrap process supervision from their own rollouts, that are increasingly central to frontier AI development.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work should focus on identifying the algorithmic sources of observed performance gaps and tightening the polynomial-in-horizon factors in the main theorem; the paper is available at [arXiv:2502.10581](https://arxiv.org/abs/2502.10581) (Jia, Rakhlin, Xie, 2025).</span></div></div>
</div>
