---
abstract: We review two algorithmic advances that bring us closer to reliable quantum
  simulations of model systems in high energy physics and beyond on noisy intermediate-scale
  quantum (NISQ) devices. The first method is the dimensional expressivity analysis
  of quantum circuits, which allows for constructing minimal but maximally expressive
  quantum circuits. The second method is an efficient mitigation of readout errors
  on quantum devices. Both methods can lead to significant improvements in quantum
  simulations, e.g., when variational quantum eigensolvers are used.
arxivId: '2110.03809'
arxivUrl: https://arxiv.org/abs/2110.03809
authors:
- Lena Funcke
- Tobias Hartung
- Karl Jansen
- Stefan Kühn
- Manuel Schneider
- Paolo Stornati
- Xiaoyang Wang
concepts:
- quantum simulation
- quantum computing
- variational quantum eigensolver
- readout error mitigation
- dimensional expressivity analysis
- hamiltonian systems
- lattice gauge theory
- symmetry preservation
- standard model
- tensor networks
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2110_03809/figure_1.png
- /iaifi-research-blog/figures/2110_03809/figure_1.png
- /iaifi-research-blog/figures/2110_03809/figure_2.png
- /iaifi-research-blog/figures/2110_03809/figure_2.png
- /iaifi-research-blog/figures/2110_03809/figure_3.png
- /iaifi-research-blog/figures/2110_03809/figure_3.png
pdfUrl: https://arxiv.org/pdf/2110.03809v1
published: '2021-10-07T22:13:37+00:00'
theme: Theoretical Physics
title: Towards Quantum Simulations in Particle Physics and Beyond on Noisy Intermediate-Scale
  Quantum Devices
wordCount: 1118
---

## The Big Picture

Imagine trying to simulate a hurricane on a 1970s calculator. That's roughly the situation physicists face when modeling quarks, gluons, and the strong force. Quantum chromodynamics — the theory governing these interactions — becomes mathematically intractable the moment you move beyond the simplest cases. Classical supercomputers choke on it.

And yet, the answers hidden in those equations could explain one of physics' deepest mysteries: why the universe contains any matter at all.

According to the Standard Model, matter and antimatter should have been created in equal amounts after the Big Bang and promptly annihilated each other. Yet here we are, made of matter. Something broke the symmetry — a phenomenon called **CP violation**, where particles and their antimatter counterparts don't behave in exact mirror-image ways.

Understanding that "something" requires simulating real-time quantum processes that classical computers fundamentally cannot handle. The culprit is the **sign problem**: when complex oscillating phases appear in quantum field theory calculations, the statistical sampling methods that normally tame these computations collapse catastrophically.

Quantum computers can sidestep the sign problem. They simulate quantum systems with quantum hardware, bypassing the statistical methods that fail when complex phases appear. But today's machines are noisy and error-prone — what researchers call **noisy intermediate-scale quantum (NISQ) devices**.

A team spanning MIT, DESY, the Cyprus Institute, and Peking University has now developed two algorithmic advances that make NISQ-era quantum simulations dramatically more reliable: a systematic way to build smarter quantum circuits, and a powerful method to correct for the errors those circuits inevitably produce.

> **Key Insight:** By combining a new technique for designing minimal yet maximally expressive quantum circuits with an efficient readout-error correction scheme, this team has made quantum simulations of particle physics measurably more reliable on today's noisy hardware.

## How It Works

The core workhorse for NISQ simulations is the **variational quantum eigensolver (VQE)** — a hybrid algorithm that splits computational labor between quantum and classical computers. The quantum device evaluates a cost function measuring how close the current state is to the target, while a classical optimizer adjusts circuit parameters to minimize it. Think of it as teaching a quantum computer to tune itself: the circuit is a machine with knobs, and the classical computer keeps turning them until the lowest-energy state is found.

Two critical problems lurk beneath the surface. First, how do you design the circuit itself? Before this work, circuit design was largely guesswork — borrowed from other contexts or built from generic templates (*ansätze*), with no principled way to know whether a given circuit could even represent the target quantum state. Second, every measurement is contaminated by readout errors — hardware misidentifying quantum states, turning 0s into 1s with distressing frequency.

![Figure 1](/iaifi-research-blog/figures/2110_03809/figure_1.png)

The team's first advance attacks circuit design with **dimensional expressivity analysis**. The key insight is geometric: the set of all quantum states reachable by a parameterized circuit forms a mathematical surface. If some parameters can be changed without affecting the output state, the circuit is wasting resources.

Expressivity analysis detects these redundancies by examining the **Jacobian** of the circuit's output — a mathematical tool measuring how sensitively each output changes when each parameter is nudged. Redundant parameters get removed. The result is a circuit that is simultaneously *minimal* (no unnecessary gates) and *maximally expressive* (it reaches every quantum state its architecture allows).

Fewer parameters mean a shallower circuit, which means less **decoherence** — the tendency of quantum states to degrade due to environmental noise. Applied to gauge theories relevant to particle physics, including formulations of quantum electrodynamics in lower dimensions, this approach reduced circuit depth without sacrificing computational power.

![Figure 2](/iaifi-research-blog/figures/2110_03809/figure_1.png)

The second advance targets readout errors with a technique that is both mathematically rigorous and practically efficient. **Readout error mitigation** works by characterizing a device's error pattern — building a map of how often hardware confuses each possible measurement outcome with another. This requires measuring the device on known states, then inverting the resulting error matrix to correct future measurements.

The computational challenge: for *n* qubits, there are 2ⁿ possible outcomes, making the full error matrix exponentially large. The team's solution exploits structure in real hardware. Readout errors on different qubits are often **approximately independent** — each qubit's confusion between 0 and 1 doesn't strongly correlate with its neighbors'. By measuring this independence and grouping correlated qubits, they build an approximate error model that is tractable to invert and accurate enough to produce significant improvements.

![Figure 3](/iaifi-research-blog/figures/2110_03809/figure_2.png)

The correction pipeline works in four steps:

- **Characterize**: Measure the device on single-qubit basis states to extract per-qubit error rates
- **Group**: Identify qubits whose errors are correlated and handle them jointly
- **Invert**: Construct an approximate inverse of the error matrix for each group
- **Correct**: Apply this inverse to raw measurement outcomes to recover cleaner probability distributions

The combination of leaner circuits and cleaner measurements produces results substantially closer to exact solutions, as validated against classical tensor network simulations — a well-established technique that serves as ground truth for small quantum systems.

## Why It Matters

Particle physics is the motivating application, but these techniques are general tools. Any VQE application — quantum chemistry, condensed matter physics, quantum optimization — benefits from circuits that are maximally efficient and measurements that are maximally accurate. The readout mitigation scheme is hardware-agnostic: it applies to any gate-based quantum computer, regardless of the underlying technology.

![Figure 4](/iaifi-research-blog/figures/2110_03809/figure_2.png)

Simulating full quantum chromodynamics in 3+1 dimensions remains far beyond current hardware. But algorithmic improvements accumulate. Better circuit design, better error mitigation, better classical validation — the community is building infrastructure that will eventually make such simulations possible. Each advance narrows the gap between what NISQ hardware *can* do and what particle physics *needs*, with rigorous benchmarks demonstrating real gains on real devices.

> **Bottom Line:** Dimensional expressivity analysis and structured readout error mitigation measurably improve the reliability of quantum simulations on today's noisy hardware, bringing particle physics phenomena one concrete step closer to quantum tractability.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges quantum information theory and high-energy physics, applying tools from differential geometry to the practical challenge of simulating gauge field theories on quantum hardware.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Dimensional expressivity analysis provides a principled, general framework for optimizing parameterized quantum circuits, with broad applications in quantum machine learning and variational algorithms beyond physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">More reliable quantum simulations of gauge theories open a computational path toward studying CP violation and matter-antimatter asymmetry in regimes inaccessible to classical Monte Carlo methods.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work aims to scale these techniques to larger systems and 3+1D gauge theories; full details appear in the preprint carrying MIT identifier MIT-CTP/5325.</span></div></div>
</div>
