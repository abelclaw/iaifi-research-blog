---
abstract: Partial differential equations (PDEs) are instrumental for modeling dynamical
  systems in science and engineering. The advent of neural networks has initiated
  a significant shift in tackling these complexities though challenges in accuracy
  persist, especially for initial value problems. In this paper, we introduce the
  $\textit{Time-Evolving Natural Gradient (TENG)}$, generalizing time-dependent variational
  principles and optimization-based time integration, leveraging natural gradient
  optimization to obtain high accuracy in neural-network-based PDE solutions. Our
  comprehensive development includes algorithms like TENG-Euler and its high-order
  variants, such as TENG-Heun, tailored for enhanced precision and efficiency. TENG's
  effectiveness is further validated through its performance, surpassing current leading
  methods and achieving $\textit{machine precision}$ in step-by-step optimizations
  across a spectrum of PDEs, including the heat equation, Allen-Cahn equation, and
  Burgers' equation.
arxivId: '2404.10771'
arxivUrl: https://arxiv.org/abs/2404.10771
authors:
- Zhuo Chen
- Jacob McCarran
- Esteban Vizcaino
- Marin Soljačić
- Di Luo
concepts:
- natural gradient optimization
- sequential-in-time optimization
- time-dependent variational principle
- neural operators
- loss function design
- surrogate modeling
- physics-informed neural networks
- sparse models
- hamiltonian systems
- inverse problems
- stochastic processes
figures:
- /iaifi-research-blog/figures/2404_10771/figure_1.png
pdfUrl: https://arxiv.org/pdf/2404.10771v2
published: '2024-04-16T17:55:31+00:00'
theme: Theoretical Physics
title: 'TENG: Time-Evolving Natural Gradient for Solving PDEs With Deep Neural Nets
  Toward Machine Precision'
wordCount: 1209
---

## The Big Picture

Imagine trying to predict the weather by snapping photographs every few minutes and guessing what comes next, but each guess inherits all the error from every previous guess, until your forecast is nothing but noise. That is the challenge facing scientists who use neural networks to solve **partial differential equations** (PDEs): the equations governing how heat spreads, fluids churn, and materials transform. Small inaccuracies compound over time, and what starts as a promising simulation drifts away from reality.

PDEs are the mathematical backbone of modern science. From the fluid dynamics of jet engines to the quantum evolution of exotic materials, these equations describe how things change in space and time.

Traditional numerical solvers have served scientists well for decades, but they struggle when problems become too complex or involve too many interacting variables. Neural networks offer an appealing alternative: adaptable computational tools that can handle complexity traditional methods can't. The catch? Accuracy, especially over time, has been hard to achieve.

A team of researchers at MIT and Harvard, affiliated with the NSF AI Institute for Artificial Intelligence and Fundamental Interactions (IAIFI), set out to fix that. Their method, **Time-Evolving Natural Gradient (TENG)**, doesn't just improve on existing neural PDE solvers. It hits *machine precision*: the limit of what a computer can represent numerically.

> **Key Insight:** TENG combines ideas from quantum physics, differential geometry, and optimization theory to solve PDEs with neural networks at a level of accuracy that rivals traditional high-precision numerical methods, a first for this class of approaches.

## How It Works

To understand TENG, it helps to know the two older approaches it builds on. The first, **time-dependent variational principle (TDVP)**, projects the PDE's dynamics directly onto the geometry of the neural network. Think of it like casting a shadow: take the "true" direction the solution should evolve, then find the nearest direction the network can actually move. The second, **optimization-based time integration (OBTI)**, treats each time step as a fresh optimization problem, finding the network parameters that best match where the solution should be after a small step forward in time.

Both approaches have real strengths, but both hit a ceiling on accuracy. TDVP accumulates projection errors; OBTI can settle into imprecise solutions. TENG asks: what if you combined the geometric intuition of TDVP with the optimization power of OBTI, and then used **natural gradient** methods?

![Figure 1](/iaifi-research-blog/figures/2404_10771/figure_1.png)

Natural gradient, originally developed by Shun-ichi Amari in 1998, is a smarter way of adjusting a neural network's internal settings. Standard optimization takes the shortest apparent path toward a better solution, but that path ignores the actual shape of the terrain, sometimes leading into poorly-suited valleys. Instead of this naive approach, natural gradient accounts for how the network's *outputs* actually respond to changes in its *parameters*, choosing more informed steps. This matters especially when the terrain is highly contorted, which is exactly the situation you face when fitting a neural network to a rapidly changing PDE solution.

Here's how TENG works, step by step:

1. **Initialize:** Fit the neural network to the initial condition of the PDE.
2. **Project:** At each time step, define a loss function in the space of *functions* (not parameters), measuring how well the current network matches where the solution should be.
3. **Optimize with natural gradient:** Iteratively update the network parameters using natural gradient steps, nudging the network toward the desired change, constrained to what the network can actually express.
4. **Advance:** Move forward in time and repeat.

The team developed two concrete algorithms from this framework. **TENG-Euler** is the basic first-order variant, fast and already far more accurate than competing methods. **TENG-Heun** goes further, evaluating the gradient at intermediate steps in the same way that Runge-Kutta methods improve accuracy by taking carefully placed intermediate measurements before committing to a full step. To keep the method tractable for large networks, the authors also developed a sparse update strategy that targets only the most informative parameters at each step, cutting computational cost substantially.

## Why It Matters

Across three benchmark PDEs (the **heat equation**, the **Allen-Cahn equation**, and **Burgers' equation**), TENG achieves errors at or near the limits of floating-point arithmetic. Compared to OBTI and PINN with energy natural gradient, TENG reduces errors by orders of magnitude. This isn't a marginal improvement; it's a qualitative leap into a new accuracy regime.


For physics, high-precision neural PDE solvers open the door to studying complex quantum systems, turbulent flows, and other phenomena where both accuracy and scalability matter. Traditional solvers often scale poorly to high dimensions. Neural networks handle that more gracefully.

For AI, TENG shows that combining ideas from physics (variational principles, information geometry) with machine learning can produce capabilities that neither field achieves alone. The natural gradient connection, originally developed for statistical learning, turns out to be exactly the right mathematical tool for navigating the function-space geometry of time-evolving PDEs.


Open questions remain. Can TENG scale to the high-dimensional PDEs that arise in quantum many-body physics or climate modeling? How does it handle PDEs with discontinuous solutions or sharp fronts, where accuracy is hardest to maintain? And can the sparse update strategies be pushed further, making TENG competitive on problems where even current neural solvers are computationally prohibitive?

> **Bottom Line:** TENG achieves machine-precision accuracy in neural network PDE solving by fusing natural gradient optimization with sequential time integration, outperforming all current state-of-the-art methods by orders of magnitude.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">TENG directly bridges ideas from quantum physics (time-dependent variational principles), differential geometry (natural gradient optimization), and deep learning to produce a new class of PDE solvers that neither field could have developed alone.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">TENG sets a new benchmark for neural network-based PDE solving, showing that machine-precision accuracy is achievable and providing a blueprint for high-order, geometry-aware optimization in scientific machine learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling accurate, scalable neural PDE solvers, TENG expands the tools available for simulating complex physical systems, from phase transitions in materials science to dynamical quantum systems relevant to fundamental physics research.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend TENG to high-dimensional quantum and classical PDEs where traditional methods fail; the full paper is available on [arXiv:2404.10771](https://arxiv.org/abs/2404.10771) and was published at ICML 2024 (proceedings PMLR 235, 2024).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">TENG: Time-Evolving Natural Gradient for Solving PDEs With Deep Neural Nets Toward Machine Precision</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2404.10771](https://arxiv.org/abs/2404.10771)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">Zhuo Chen, Jacob McCarran, Esteban Vizcaino, Marin Soljačić, Di Luo</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Partial differential equations (PDEs) are instrumental for modeling dynamical systems in science and engineering. The advent of neural networks has initiated a significant shift in tackling these complexities though challenges in accuracy persist, especially for initial value problems. In this paper, we introduce the Time-Evolving Natural Gradient (TENG), generalizing time-dependent variational principles and optimization-based time integration, leveraging natural gradient optimization to obtain high accuracy in neural-network-based PDE solutions. Our comprehensive development includes algorithms like TENG-Euler and its high-order variants, such as TENG-Heun, tailored for enhanced precision and efficiency. TENG's effectiveness is further validated through its performance, surpassing current leading methods and achieving machine precision in step-by-step optimizations across a spectrum of PDEs, including the heat equation, Allen-Cahn equation, and Burgers' equation.</span></div></div>
</div>
