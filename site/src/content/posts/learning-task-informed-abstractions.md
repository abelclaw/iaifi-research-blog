---
abstract: Current model-based reinforcement learning methods struggle when operating
  from complex visual scenes due to their inability to prioritize task-relevant features.
  To mitigate this problem, we propose learning Task Informed Abstractions (TIA) that
  explicitly separates reward-correlated visual features from distractors. For learning
  TIA, we introduce the formalism of Task Informed MDP (TiMDP) that is realized by
  training two models that learn visual features via cooperative reconstruction, but
  one model is adversarially dissociated from the reward signal. Empirical evaluation
  shows that TIA leads to significant performance gains over state-of-the-art methods
  on many visual control tasks where natural and unconstrained visual distractions
  pose a formidable challenge.
arxivId: '2106.15612'
arxivUrl: https://arxiv.org/abs/2106.15612
authors:
- Xiang Fu
- Ge Yang
- Pulkit Agrawal
- Tommi Jaakkola
concepts:
- reinforcement learning
- representation learning
- task-informed mdp
- distractor separation
- disentangled representations
- reward optimization
- world models
- loss function design
- generative adversarial networks
- variational autoencoders
figures:
- /iaifi-research-blog/figures/2106_15612/figure_1.png
- /iaifi-research-blog/figures/2106_15612/figure_1.png
- /iaifi-research-blog/figures/2106_15612/figure_2.png
- /iaifi-research-blog/figures/2106_15612/figure_2.png
- /iaifi-research-blog/figures/2106_15612/figure_3.png
- /iaifi-research-blog/figures/2106_15612/figure_3.png
pdfUrl: https://arxiv.org/pdf/2106.15612v2
published: '2021-06-29T17:56:11+00:00'
theme: Foundational AI
title: Learning Task Informed Abstractions
wordCount: 995
---

## The Big Picture

Imagine handing a chess grandmaster a photograph of a game board and asking them to plan their next move — but the photo is taken in a crowded coffee shop, full of people, steam, and distracting signage. A human expert filters all of that out instantly. Their brain doesn't try to memorize every face in the background before deciding to move the knight. AI systems, however, are remarkably bad at this.

When you show a **reinforcement learning (RL)** agent — an AI that learns by trial and error, receiving rewards for good actions and penalties for bad ones — a complex visual scene, it dutifully tries to learn *everything* it sees: the robot arm, the target object, and every flickering pixel of irrelevant background scenery.

This is not a minor inconvenience. Real-world robots operate in messy environments with changing lighting, moving people, and reflective surfaces. If the AI spends its limited representational capacity modeling all of that irrelevance, it has less left for what actually matters: figuring out where the arm is and where it needs to go.

Researchers at MIT CSAIL and IAIFI tackled this directly by developing **Task Informed Abstractions (TIA)** — a method that explicitly teaches an AI to separate what matters from what doesn't, rather than hoping the distinction emerges on its own.

> **Key Insight:** TIA forces a learning system to build two separate internal models — one focused on task-relevant features, one dedicated to distractors — and pits them against each other so neither can cheat by mixing the two.

## How It Works

The starting point is a deceptively simple experiment. The team trained *Dreamer* — a leading **model-based RL** algorithm that builds an internal simulation of the world to plan ahead — on the classic *Cheetah Run* locomotion task: once with a clean background, once with complex natural video playing behind the running cheetah. They also varied model size: small (0.5×), medium (1×), and large (2×).

![Figure 1](/iaifi-research-blog/figures/2106_15612/figure_1.png)

The results were striking. With a clean background, even the smallest model performed well. With the complex background, performance collapsed across all model sizes, recovering only as capacity increased. Bigger models weren't learning *better* — they were buying extra capacity to absorb the irrelevant background and still have some room left for the actual task. Expensive and inelegant.

TIA introduces a formal structure called the **Task Informed MDP (TiMDP)**, which partitions the internal state representation into two explicit components:

- **s⁺ (task state):** Features correlated with reward — what the agent actually needs to maximize performance.
- **s⁻ (distractor state):** Everything else — background motion, irrelevant objects, visual noise.

![Figure 2](/iaifi-research-blog/figures/2106_15612/figure_1.png)

Two models work together in a cooperative-adversarial game. The **task model** learns s⁺ by predicting rewards — it must capture whatever features matter for success. The **distractor model** learns s⁻ through a competing mechanism: it is *explicitly penalized* for learning anything correlated with rewards, forcing it to absorb only the irrelevant residual.

The cooperative twist: both models must jointly reconstruct the full observed image. Neither can succeed alone. The task model handles the robot arm; the distractor model handles the moving trees in the background. Together they account for everything the camera captures.

This design threads a needle that previous methods missed. Pure reconstruction learning captures *too much* — the model must encode every pixel regardless of relevance. Pure reward prediction captures *too little* — knowing only the center of mass of a humanoid is sufficient to predict reward, but not to control it well. TIA uses reconstruction as a completeness check while using adversarial separation to keep the right features in the right sub-model.

## Why It Matters

The implications extend well beyond locomotion benchmarks. Any domain where an agent must learn from high-dimensional observations littered with irrelevant variation — medical robotics, scientific instrument control, autonomous vehicles — faces this exact challenge.

![Figure 4](/iaifi-research-blog/figures/2106_15612/figure_2.png)

TIA consistently outperforms state-of-the-art baselines across three distinct evaluation settings:

- The **DMControl benchmark**, a standard suite of robot control tasks with video distractors
- The custom **ManyWorld environment**, designed specifically to stress-test distraction robustness
- **Atari games**, where visual clutter takes a very different form

The gains are most dramatic precisely where distractions are hardest — the settings where prior methods struggle most. That's a meaningful sign that TIA is solving the right problem, not just tuning hyperparameters on easy cases.

The deeper insight in TIA is not a clever trick but a formalization of something humans do naturally: build mental models that are *selective*, not exhaustive. Open questions remain — Can TIA scale to real-world settings where the boundary between "relevant" and "irrelevant" is fuzzy? Can adversarial training stay stable as environments grow more complex? — but the foundation is principled.

> **Bottom Line:** TIA teaches AI agents to see like experts — filtering out visual noise not by brute-force capacity, but by explicitly learning what to ignore. It's a principled step toward RL agents that can handle the messy, distraction-filled real world.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">TIA applies information-theoretic principles — the physicist's instinct that a good model should capture only the minimal sufficient representation of a system — directly to deep reinforcement learning, connecting statistical mechanics intuition to practical AI agent design.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">By formalizing the TiMDP and introducing cooperative-adversarial training to separate task-relevant features from distractors, TIA sets a new state of the art on visual control benchmarks with natural distractions, with significant performance gains over leading model-based RL methods.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The distractor-separation framework opens pathways for scientific AI agents that must extract meaningful signals from noisy experimental data — a challenge directly analogous to isolating physical signals from environmental interference in particle physics or gravitational wave detection.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend TiMDP to continuous, time-varying distractor distributions and real robotic deployment; the full paper is available via the ICML 2021 proceedings, with the arXiv preprint at arXiv:2106.15612.</span></div></div>
</div>
