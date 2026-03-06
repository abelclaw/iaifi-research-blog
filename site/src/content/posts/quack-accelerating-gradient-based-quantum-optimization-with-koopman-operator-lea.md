---
abstract: Quantum optimization, a key application of quantum computing, has traditionally
  been stymied by the linearly increasing complexity of gradient calculations with
  an increasing number of parameters. This work bridges the gap between Koopman operator
  theory, which has found utility in applications because it allows for a linear representation
  of nonlinear dynamical systems, and natural gradient methods in quantum optimization,
  leading to a significant acceleration of gradient-based quantum optimization. We
  present Quantum-circuit Alternating Controlled Koopman learning (QuACK), a novel
  framework that leverages an alternating algorithm for efficient prediction of gradient
  dynamics on quantum computers. We demonstrate QuACK's remarkable ability to accelerate
  gradient-based optimization across a range of applications in quantum optimization
  and machine learning. In fact, our empirical studies, spanning quantum chemistry,
  quantum condensed matter, quantum machine learning, and noisy environments, have
  shown accelerations of more than 200x speedup in the overparameterized regime, 10x
  speedup in the smooth regime, and 3x speedup in the non-smooth regime. With QuACK,
  we offer a robust advancement that harnesses the advantage of gradient-based quantum
  optimization for practical benefits.
arxivId: '2211.01365'
arxivUrl: https://arxiv.org/abs/2211.01365
authors:
- Di Luo
- Jiayu Shen
- Rumen Dangovski
- Marin Soljačić
concepts:
- koopman operator learning
- quantum computing
- variational quantum algorithms
- scalability
- quantum simulation
- quantum natural gradient
- hamiltonian systems
- surrogate modeling
- eigenvalue decomposition
- spectral methods
- kernel methods
- stochastic processes
figures:
- /iaifi-research-blog/figures/2211_01365/figure_1.png
- /iaifi-research-blog/figures/2211_01365/figure_1.png
- /iaifi-research-blog/figures/2211_01365/figure_2.png
- /iaifi-research-blog/figures/2211_01365/figure_2.png
- /iaifi-research-blog/figures/2211_01365/figure_3.png
- /iaifi-research-blog/figures/2211_01365/figure_3.png
pdfUrl: https://arxiv.org/pdf/2211.01365v3
published: '2022-11-02T17:59:25+00:00'
theme: Theoretical Physics
title: 'QuACK: Accelerating Gradient-Based Quantum Optimization with Koopman Operator
  Learning'
wordCount: 963
---

## The Big Picture

Imagine you're hiking through a vast mountain range, searching for the lowest valley. Each step requires consulting an expensive GPS device — and the more peaks surrounding you, the more measurements you need. Now imagine someone hands you a map predicting where the valley lies, so you only need to check the GPS occasionally. That's what QuACK does for quantum computers optimizing complex physics problems.

Quantum computers promise to revolutionize how we simulate molecules, design materials, and solve problems that classical machines can't touch. But there's a painful bottleneck: computing **gradients** — the measurements that tell an optimizer which direction to improve. Training a **Variational Quantum Algorithm (VQA)** — where you fine-tune a quantum circuit's adjustable settings until it finds the best solution — requires calculating how the score changes with each setting. The cost scales *linearly* with the number of settings: add more, pay more, every single iteration.

A team from MIT, Harvard, and the University of Illinois has cracked this with **QuACK** (Quantum-circuit Alternating Controlled Koopman Operator Learning), achieving speedups of up to 200x by borrowing a mathematical tool from dynamical systems theory developed nearly a century ago.

> **Key Insight:** QuACK uses Koopman operator theory to learn a linear model of the nonlinear optimization dynamics, then predicts future parameter updates without running expensive quantum gradient computations — slashing circuit evaluations by orders of magnitude.

## How It Works

The core idea: reframe quantum optimization as a **dynamical system** — one whose state evolves step by step according to fixed rules, like a planet tracing its orbit. Rather than asking "what's the gradient right now?", QuACK asks "can we learn the rules governing how parameters evolve, then extrapolate forward?"

**Koopman operator theory** makes this possible. Developed in the 1930s, it offers something remarkable: even for wildly nonlinear systems, there exists a linear operator — acting on an infinite-dimensional space of measurable quantities — that captures all the dynamics exactly. In practice, you approximate this with a finite set of measurements. The result: a linear representation of nonlinear behavior, immensely powerful for prediction.

![Figure 1](/iaifi-research-blog/figures/2211_01365/figure_1.png)

QuACK's pipeline breaks into four stages:

1. **Quantum optimization runs** — parameterized quantum circuits evaluate the loss via measurements, and a classical optimizer computes parameter updates using quantum gradients (the expensive part)
2. **Data acquisition** — the optimization history forms a time series; each step costs resources proportional to the number of parameters
3. **Koopman operator learning** — an alternating algorithm learns an embedding space where the dynamics become approximately linear
4. **Prediction** — QuACK uses the learned operator to predict *many future parameter updates at once*, checking the actual quantum circuit only periodically to keep the model honest

The "alternating" in the name refers to the core optimization scheme: the algorithm alternates between updating the Koopman embedding and updating the linear operator, converging efficiently to a stable representation. The authors analyze **spectral stability** — ensuring predicted dynamics don't blow up — and extend the approach to handle nonlinear corrections via sliding windows and neural network enhancements.

![Figure 2](/iaifi-research-blog/figures/2211_01365/figure_1.png)

The connection to **quantum natural gradient** is particularly elegant. The natural gradient accounts for the geometry of quantum state space — treating the optimization landscape as curved rather than flat — and is captured by the **quantum Fisher information metric**, a measure of how distinguishable nearby quantum states are. The authors show Koopman learning in this geometric setting is theoretically well-posed. Overparameterized circuits — those with more parameters than strictly needed — are especially amenable, because their loss landscapes are smoother and the dynamics more predictable.

## Why It Matters

The numbers speak for themselves. In the overparameterized regime, QuACK delivers over **200x speedup** compared to standard gradient-based methods. In the smooth regime, it achieves **10x speedup**. Even in non-smooth settings — notoriously difficult for any optimizer — QuACK still manages **3x speedup**. The team validated these results across quantum chemistry, many-body spin systems, quantum machine learning tasks, and noisy environments mimicking real hardware.

![Figure 3](/iaifi-research-blog/figures/2211_01365/figure_2.png)

This matters far beyond benchmarks. The gradient bottleneck has been one of the most stubborn practical obstacles to deploying VQAs on near-term hardware. Quantum computers are expensive to run, noisy, and time-limited. A 200x reduction in required circuit evaluations could be the difference between a feasible experiment and an impossible one.

QuACK is also *complementary* to meta-learning and other acceleration strategies — it layers on top of existing approaches rather than replacing them. The Koopman framework opens further doors: studying optimization landscapes theoretically, understanding not just *whether* gradient methods converge but *why* and *how fast*. Extensions to larger qubit systems, more complex noise models, and hybrid classical-quantum architectures all seem within reach.

> **Bottom Line:** QuACK proves that a century-old mathematical theory — Koopman operator learning — can slash quantum optimization costs by up to 200x, potentially making gradient-based VQAs practical on real quantum hardware for the first time.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work forges a principled connection between Koopman dynamical systems theory, quantum natural gradient methods, and overparameterization theory — bridging pure mathematics, quantum physics, and machine learning in a single algorithmic framework.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">QuACK establishes a new class of optimization accelerator for variational quantum algorithms, demonstrating that machine-learned surrogate models of gradient dynamics can replace expensive quantum measurements across a wide range of quantum ML tasks.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling practical gradient-based optimization at scale, QuACK advances the ability to simulate quantum chemistry and many-body condensed matter systems — problems central to understanding fundamental physical interactions at the quantum level.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend QuACK to larger qubit systems, more realistic noise models, and integration with meta-learning pipelines; the paper is available on arXiv and was presented at NeurIPS 2023.</span></div></div>
</div>
