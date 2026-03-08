---
abstract: Value approximation using deep neural networks is at the heart of off-policy
  deep reinforcement learning, and is often the primary module that provides learning
  signals to the rest of the algorithm. While multi-layer perceptron networks are
  universal function approximators, recent works in neural kernel regression suggest
  the presence of a spectral bias, where fitting high-frequency components of the
  value function requires exponentially more gradient update steps than the low-frequency
  ones. In this work, we re-examine off-policy reinforcement learning through the
  lens of kernel regression and propose to overcome such bias via a composite neural
  tangent kernel. With just a single line-change, our approach, the Fourier feature
  networks (FFN) produce state-of-the-art performance on challenging continuous control
  domains with only a fraction of the compute. Faster convergence and better off-policy
  stability also make it possible to remove the target network without suffering catastrophic
  divergences, which further reduces TD}(0)'s estimation bias on a few tasks.
arxivId: '2206.04672'
arxivUrl: https://arxiv.org/abs/2206.04672
authors:
- Ge Yang
- Anurag Ajay
- Pulkit Agrawal
concepts:
- reinforcement learning
- fourier feature networks
- kernel methods
- spectral methods
- neural tangent kernel
- feature extraction
- representation learning
- td learning stability
- reward optimization
- scalability
- loss function design
figures:
- /iaifi-research-blog/figures/2206_04672/figure_1.png
- /iaifi-research-blog/figures/2206_04672/figure_1.png
- /iaifi-research-blog/figures/2206_04672/figure_2.png
- /iaifi-research-blog/figures/2206_04672/figure_2.png
- /iaifi-research-blog/figures/2206_04672/figure_3.png
- /iaifi-research-blog/figures/2206_04672/figure_3.png
pdfUrl: https://arxiv.org/pdf/2206.04672v1
published: '2022-06-09T17:59:57+00:00'
theme: Foundational AI
title: Overcoming the Spectral Bias of Neural Value Approximation
wordCount: 1092
---

## The Big Picture

Imagine tuning a radio receiver that only picks up bass frequencies. You'd catch the rhythm, maybe some melody — but the high-pitched details that make music rich and distinctive would be a blur. Now imagine this is your brain learning chess: you can grasp broad strategic ideas, but the subtle tactical patterns that separate a grandmaster from a club player remain perpetually fuzzy, no matter how long you study.

This is the problem haunting neural networks in reinforcement learning. When an AI agent learns to play a game or control a robot, it builds a **value function** — an internal map assigning scores to every possible situation, telling the agent how favorable its position is. Deep neural networks approximate this function across vast, continuous spaces. But a subtle flaw undermines them: they learn smooth, slowly-varying patterns quickly while sharp, high-frequency details — the distinctions that matter most — take exponentially more training steps to acquire, and sometimes never get learned at all.

Researchers at MIT's CSAIL and the NSF AI Institute for Artificial Intelligence and Fundamental Interactions (IAIFI) identified this tendency — called **spectral bias** — as a root cause of inefficiency in deep reinforcement learning. Their fix requires a single line of code.

> **Key Insight:** Standard neural networks are systematically biased toward low-frequency value functions, causing them to miss critical high-frequency structure. Replacing the input layer with random Fourier features reshapes this learning dynamic across the full frequency spectrum, enabling dramatically faster and more stable value approximation.

## How It Works

The theoretical backbone comes from **neural tangent kernel (NTK) theory**, a framework that precisely characterizes what kinds of patterns a neural network learns efficiently and which it struggles with. The core finding: training via **gradient descent** doesn't learn all patterns at the same rate. Low-frequency components — gradual, broad trends — converge quickly. High-frequency components — sharp, rapid variations — converge exponentially slowly.

For value functions, this is a serious problem. Value functions tend to be complex and jagged due to the recursive structure of **Bellman equations**, the mathematical rules governing how an agent's value estimates feed into one another.

![Figure 1](/iaifi-research-blog/figures/2206_04672/figure_1.png)

Toy experiments make this concrete. A standard 4-layer **multi-layer perceptron (MLP)** trained with **fitted Q-iteration** produces a smoothed-out, blurry approximation of the true value function. Making the network three times deeper or training five times longer doesn't fix it — the architecture is constitutionally biased against the sharp value landscapes agents need.

![Figure 2](/iaifi-research-blog/figures/2206_04672/figure_1.png)

The solution borrows from computer graphics, where researchers discovered identical problems when neural networks tried to represent fine 3D scene details. The fix there — and here — is to first transform raw inputs through **random Fourier features**: sinusoidal functions at randomly sampled frequencies that lift low-dimensional inputs into a higher-dimensional space rich with oscillatory structure. Mathematically, this transforms the network's learning profile from a broad low-pass filter into a **composite kernel** tunable across a wide frequency range.

The resulting architecture — **Fourier Feature Networks (FFN)** — works as follows:

1. Take the state (and action) as input
2. Apply a fixed random Fourier feature embedding: $\gamma(\mathbf{x}) = [\sin(\mathbf{B}\mathbf{x}), \cos(\mathbf{B}\mathbf{x})]$, where $\mathbf{B}$ is a matrix of randomly sampled frequencies
3. Feed the embedded input into a standard MLP
4. Train with the same off-policy RL algorithm as before

The embedding is fixed — it doesn't train — so there's no added computational cost during forward passes. Yet the effect on learning dynamics is profound. The network gains **localized support**: gradient updates for one state-action pair no longer bleed over and corrupt estimates for distant ones, dramatically stabilizing training.

## Why It Matters

The performance gains are striking. On continuous control benchmarks — physics-simulated locomotion and manipulation tasks that stress-test modern RL algorithms — FFN achieves state-of-the-art results with a fraction of the compute. Faster convergence means the agent reaches the same performance level in fewer environment interactions, directly reducing training time and real-world sample requirements.

![Figure 3](/iaifi-research-blog/figures/2206_04672/figure_2.png)

The most surprising finding is what becomes possible once learning stabilizes: the **target network can be removed**. Target networks — a second, slowly-updated copy of the value network used to generate stable training targets — have been a standard fixture in deep RL since the original DQN paper in 2013. They exist because training with neural networks tends to spiral into catastrophic divergence without them. With FFN's improved stability, the authors demonstrate successful training without this crutch on several tasks. Eliminating the target network also removes a source of **estimation bias** — a systematic distortion the target network inevitably introduces — improving accuracy further.

The implications extend well beyond the specific algorithms tested. Spectral bias is a fundamental property of how neural networks learn, not an artifact of any particular RL algorithm. Any system using neural value approximation — from robotics to game-playing to financial optimization — potentially suffers from it. The Fourier feature fix is cheap, principled, and compatible with essentially any existing RL framework.

Open questions remain: How should one choose the frequency distribution for the Fourier features? Random Gaussian sampling works well, but a learned or adaptive distribution might do better. And while removing the target network succeeds on some tasks, understanding exactly when it's safe remains an active area.

> **Bottom Line:** A single-line fix — replacing the input layer of a value network with random Fourier features — overcomes a fundamental bias that has quietly hampered deep reinforcement learning for years, delivering state-of-the-art performance at reduced compute while enabling training regimes previously too unstable to attempt.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work imports theoretical tools from machine learning theory (neural tangent kernels) and practical techniques from computer graphics (Fourier feature embeddings) to solve a core problem in reinforcement learning — a direct example of the cross-domain synthesis IAIFI was designed to catalyze.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Fourier Feature Networks achieve state-of-the-art performance on continuous control benchmarks with dramatically reduced compute, while enabling stable training without the long-standard target network — advancing both efficiency and theoretical understanding of neural value approximation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By providing a more principled framework for neural function approximation, this work strengthens the toolkit available for physics-motivated AI applications, including those used to model complex dynamical systems in fundamental physics research.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will explore adaptive frequency selection and broader applications across RL domains; the paper appeared at ICLR 2022 and code is available at geyang.github.io/ffn, with the theoretical analysis laying groundwork for ongoing research into neural kernel methods in sequential decision-making.</span></div></div>
</div>
