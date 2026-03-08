---
abstract: Adiabaticity is a cornerstone of many promising approaches to quantum control,
  computing, and simulation. In practice, however, there is always a trade-off. Although
  the deleterious effects of noise can be diminished by running a control schedule
  more quickly, this benefit comes at the expense of nonadiabaticity. To put these
  two unwanted effects on the same theoretical footing, we analyze the nonadiabatic
  error in qubit control as a form of entropy production, examining the mechanism
  by which fine-grained information is effectively lost despite the dynamics being
  fundamentally unitary. A crucial issue here is the question of how to define equilibrium
  under a time-dependent Hamiltonian. Using the Landau--Zener protocol as a test case,
  we show that entropy increases nearly monotonically when equilibrium is defined
  with respect to the effective Hamiltonian in the optimal superadiabatic frame. We
  then consider single-passage Landau--Zener--Stückelberg--Majorana interferometry,
  in which the initial state of the qubit is arbitrary. Violations of the second law
  of thermodynamics are possible but require exquisite control to achieve deliberately.
arxivId: '2506.16570'
arxivUrl: https://arxiv.org/abs/2506.16570
authors:
- Pavel Zhelnin
- Lucas Johns
- Carlos A. Argüelles
concepts:
- nonadiabatic driving
- superadiabatic frame
- coarse-grained entropy
- quantum states
- hamiltonian systems
- quantum computing
- phase transitions
- stochastic processes
- quantum simulation
- quantum field theory
figures:
- /iaifi-research-blog/figures/2506_16570/figure_1.png
- /iaifi-research-blog/figures/2506_16570/figure_1.png
- /iaifi-research-blog/figures/2506_16570/figure_2.png
- /iaifi-research-blog/figures/2506_16570/figure_2.png
- /iaifi-research-blog/figures/2506_16570/figure_3.png
- /iaifi-research-blog/figures/2506_16570/figure_3.png
pdfUrl: https://arxiv.org/pdf/2506.16570v1
published: '2025-06-19T19:51:54+00:00'
theme: Theoretical Physics
title: 'Qubit thermodynamics: Entropy production from nonadiabatic driving'
wordCount: 989
---

## The Big Picture

Imagine trying to flip a coin — but instead of heads-to-tails, you need it to land perfectly balanced on its edge. Too slow, and a passing breeze knocks it over. Too fast, and violent spin sends it tumbling unpredictably. Quantum computers face a similar dilemma every time they manipulate qubits.

The textbook approach to quantum control is **adiabatic evolution**: driving a qubit so slowly and gently that it glides smoothly from one quantum state to another. But "slow" is the enemy of practical quantum computing. Leave a qubit sitting too long, and the environment corrupts it with noise, a process called **decoherence**.

Speed things up, though, and you trigger **nonadiabaticity**, moving faster than the quantum state can naturally follow. That causes unwanted quantum jumps that knock the system off course even when the hardware is running perfectly. Physicists have largely treated these two failure modes as separate problems.

A new study from Harvard and Los Alamos National Laboratory, led by Pavel Zhelnin, Lucas Johns, and Carlos Argüelles, takes a unified view. By reframing speed-induced errors as **entropy production**, a measure of how much useful order is lost borrowed from thermodynamics, they show that both failure modes sit on the same theoretical footing. The choice of mathematical "frame," or reference perspective, dramatically changes how that disorder behaves.

> **Key Insight:** In the right reference frame (the superadiabatic frame, which tracks the quantum state's natural motion) entropy builds up in a smooth, one-way ramp, much like a system warming against a hot reservoir. The second law of thermodynamics nearly holds, even for a perfectly isolated quantum system.

## How It Works

The starting point sounds almost too simple: a lone qubit, completely isolated from its environment, driven by a time-varying **Hamiltonian** (the mathematical recipe describing how the qubit's energy changes over time). Such evolution is **unitary**, perfectly reversible and information-preserving, so entropy strictly speaking never changes. How, then, can they talk about entropy production at all?

Through **coarse-graining**: the deliberate act of blurring out fine details. Examine only the average behavior of the qubit's quantum state over short time windows, ignoring rapid quantum-phase oscillations, and some information becomes effectively inaccessible. That lost information registers as entropy.

The specific mechanism is **dephasing**. The qubit's **Bloch vector**, a geometric arrow representing the qubit's state in a 3D picture whose length reflects how "pure" or well-defined that state is, precesses rapidly like a wobbly spinning top. Time-average that spinning arrow and it shrinks. A shorter Bloch vector means higher entropy.

![Figure 1](figure:1)

The researchers studied the **Landau-Zener protocol**, a textbook scenario where two energy levels (think of two rungs on a ladder) are swept through a crossing point at a finite rate. At the crossing, the system faces its highest chance of jumping between rungs. This protocol has an exact analytical solution and appears everywhere from quantum computing to neutrino physics.

Does entropy build up smoothly as you sweep through the crossing, or does it oscillate wildly? That depends entirely on the reference frame. The team examined two choices:

- **The adiabatic frame** (ordinary energy eigenstates of the lab-frame Hamiltonian): entropy production lurches up and down as quantum phases interfere, wildly non-monotonic.
- **The optimal superadiabatic frame**: entropy increases in a smooth, one-way ramp, mimicking gradual heat dissipation as a classical system approaches equilibrium.

![Figure 2](figure:2)

The superadiabatic frame incorporates a correction to the Hamiltonian that accounts for energy eigenstates moving in time. It's like switching from a stationary map to one that rotates with your compass; suddenly the view makes sense. In this frame, the effective equilibrium state is always well-defined, and the second law is obeyed far more faithfully.

## Why It Matters

The implications reach beyond quantum computing. The team also explored **Landau-Zener-Stückelberg-Majorana (LZSM) interferometry**, where the qubit starts in an arbitrary quantum state rather than the ground state. Here something unexpected shows up: nonadiabatic driving can actually *decrease* entropy, an apparent violation of the second law.

![Figure 3](figure:3)

Don't start building a perpetual motion machine just yet. These entropy-decreasing trajectories require extraordinarily precise initial conditions. Tiny errors in preparation wipe out the effect. The researchers carefully quantify how fine-tuned control must be, showing that deliberate second-law violations are thermodynamically possible but practically forbidding.

The deeper contribution is conceptual. Quantum thermodynamics usually focuses on systems coupled to thermal baths, tracking entropy that leaks out as waste heat. This paper extends that framework to a fundamentally different regime: a perfectly isolated quantum system whose "irreversibility" arises entirely from coarse-graining and observation. That distinction matters for how we think about information in quantum devices.

The same mathematical structure (Landau-Zener transitions, frame-dependent particle definitions, superadiabatic corrections) appears in wildly different physical contexts: particle production in an expanding universe, neutrino flavor oscillations in stellar interiors, quantum heat engines. A thermodynamic language that unifies nonadiabaticity and decoherence could prove useful across all of them.

![Figure 4](figure:4)

> **Bottom Line:** By treating nonadiabatic control errors as entropy production and identifying the superadiabatic frame as the natural thermodynamic reference, this work lays groundwork for a unified theory of quantum control fidelity, one where noise and speed finally speak the same language.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects quantum information theory, quantum thermodynamics, and quantum control by recasting nonadiabatic driving errors (a quantum computing problem) in the language of entropy production from statistical mechanics.

- **Impact on Artificial Intelligence:** The entropy-production framework provides a new theoretical tool for characterizing and minimizing errors in qubit control protocols, with direct relevance to optimizing adiabatic quantum computing and gate-based quantum algorithms.

- **Impact on Fundamental Interactions:** The analysis connects qubit thermodynamics to neutrino flavor evolution and cosmological particle production, exposing a structural parallel across seemingly unrelated domains of fundamental physics.

- **Outlook and References:** Future work could extend this framework to multi-qubit and open quantum systems, building a fully unified thermodynamic cost function for quantum error budgets; the paper is available at [arXiv:2506.16570](https://arxiv.org/abs/2506.16570).
