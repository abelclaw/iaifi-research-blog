---
abstract: 'Recent advances on neural quantum states have shown that correlations between
  quantum particles can be efficiently captured by {\it attention} -- a foundation
  of modern neural architectures that enables neural networks to learn the relation
  between objects. In this work, we show that a general-purpose self-attention Fermi
  neural network is able to find chiral $p_x \pm i p_y$ superconductivity in an attractive
  Fermi gas by energy minimization, {\it without prior knowledge or bias towards pairing}.
  The superconducting state is identified from the optimized wavefunction by measuring
  various physical observables: the pair binding energy, the total angular momentum
  of the ground state, and off-diagonal long-range order in the two-body reduced density
  matrix. Our work paves the way for AI-driven discovery of unconventional and topological
  superconductivity in strongly correlated quantum materials.'
arxivId: '2509.03683'
arxivUrl: https://arxiv.org/abs/2509.03683
authors:
- Chun-Tse Li
- Tzen Ong
- Max Geier
- Hsin Lin
- Liang Fu
concepts:
- attention mechanisms
- chiral superconductivity
- transformers
- neural quantum states
- quantum states
- monte carlo methods
- topological quantum matter
- equivariant neural networks
- symmetry breaking
- quantum simulation
- phase transitions
- automated discovery
- materials discovery
figures:
- /iaifi-research-blog/figures/2509_03683/figure_1.png
- /iaifi-research-blog/figures/2509_03683/figure_2.png
- /iaifi-research-blog/figures/2509_03683/figure_3.png
pdfUrl: https://arxiv.org/pdf/2509.03683v1
published: '2025-09-03T20:06:39+00:00'
theme: Theoretical Physics
title: Attention is all you need to solve chiral superconductivity
wordCount: 1034
---

## The Big Picture

Imagine trying to find a hidden treasure without a map, any clues, or even knowing what the treasure looks like. A team of physicists at MIT, Academia Sinica, and USC just did something close to that. The treasure: one of the most exotic quantum states of matter, **chiral superconductivity**.

Superconductivity is already strange enough. Below certain temperatures, electrons in some materials pair up and flow without any electrical resistance. No energy wasted, no heat generated.

Chiral superconductivity is stranger still. The paired electrons carry angular momentum, rotating around each other like partners in a cosmic waltz. The state has a built-in handedness: run time backwards, and it looks different. Physicists call this **breaking time-reversal symmetry**.

Discovering such states from scratch has been a long-standing challenge. Traditional methods either fail when particles interact too strongly, or require physicists to tell the algorithm what to look for before it starts.

A team led by MIT researchers has now shown that a single general-purpose **transformer neural network**, the same architecture behind large language models, can find chiral *p_x ± ip_y* superconductivity entirely on its own. Starting from random weights and minimizing energy, the network discovered the answer without any hints about pairing or superconducting order.

> A self-attention neural network, given no information about pairing or superconductivity, independently discovers a topologically nontrivial chiral superconducting state. AI can uncover exotic quantum phases without human-imposed bias.

## How It Works

The researchers work with spin-polarized fermions in two dimensions, subject to an attractive Gaussian potential. The physics is clean and controlled, but solving it exactly is impossible: the number of quantum states grows exponentially with particle number. Brute-force approaches are hopeless for anything beyond toy systems.

Their solution uses **self-attention**, the mechanism at the heart of transformer models. In a language model, attention lets the network learn which words relate to which other words. Here, it learns which particles relate to which other particles, capturing the quantum correlations that define exotic phases of matter.

![Figure 1](/iaifi-research-blog/figures/2509_03683/figure_1.png)

The network's wavefunction is built on a **FermiNet-style architecture** that automatically satisfies the **Pauli exclusion principle**, the quantum rule forbidding two identical particles from occupying the same state. It does this by expressing the wavefunction as a sum of generalized Slater determinants, mathematical structures that enforce this rule by construction.

Particle coordinates enter as sine and cosine embeddings that respect the periodic boundary conditions of the simulation box. These "particle tokens" pass through multiple layers of multi-head self-attention and MLP blocks, then get projected into many-body orbital matrices whose determinants give the final wavefunction.

The network is initialized with random weights and optimized from scratch using **variational Monte Carlo (VMC)**: many random particle configurations are sampled, and the network's parameters are nudged to minimize expected energy. No pretraining, no warm-starting from BCS mean-field theory, no problem-specific modifications. The same architecture tested on electron gases, atoms, and molecules is applied here unmodified.

Once the network converges, three independent diagnostics confirm the result is a chiral topological superconductor:

- **Pair binding energy**, defined as *E(N) + E(N+2) − 2E(N+1)*, measures whether the system energetically prefers even or odd particle numbers. Conventional superconductors prefer even numbers (pairs). Topological chiral superconductors flip this: odd-*N* states are favored because an unpaired state sits below the Fermi level. The network reproduces exactly this reversed odd-even effect across a range of coupling strengths.
- **Total angular momentum**: chiral *p_x ± ip_y* pairing means the ground state carries net angular momentum. Measurements from the optimized wavefunction match the expected chiral quantum number.
- **Off-diagonal long-range order (ODLRO)**: the smoking gun of superconductivity, visible in the two-body reduced density matrix. The wavefunction shows the characteristic long-range correlations that define true superconducting order.

![Figure 2](/iaifi-research-blog/figures/2509_03683/figure_2.png)

All three diagnostics converge on the same conclusion across a broad range of interaction strengths, from weak coupling where BCS theory applies to strong coupling where it breaks down entirely. At strong coupling, the neural network goes beyond mean-field theory, capturing quantum fluctuation effects that perturbative methods miss.

![Figure 3](/iaifi-research-blog/figures/2509_03683/figure_3.png)

## Why It Matters

The topological character of the state, confirmed by the reversed odd-even binding energy signature, is particularly significant. **Topological superconductors** are predicted to host **Majorana zero modes**: exotic quasiparticles that are their own antiparticles and a leading candidate for fault-tolerant quantum computing. Finding them computationally, without prior bias, points toward a systematic AI-driven survey of which materials might harbor them.

Previous neural quantum state studies of superconductivity required modifying the wavefunction ansatz to include pairing structure by hand. The self-attention approach needs none of that scaffolding.


This points toward a future where AI acts as an unbiased explorer of the quantum phase diagram. Real materials (high-temperature superconductors, topological insulators, quantum spin liquids) are governed by strongly correlated Hamiltonians that have resisted decades of analytical and numerical effort. A general-purpose solver that can find exotic ground states without being told where to look could systematically map territory that has long been inaccessible.

The authors frame their result as a step toward AI-driven discovery of unconventional and topological superconductivity in real quantum materials. Given what their network pulled off here, that goal looks a good deal closer.

> By finding chiral *p_x ± ip_y* superconductivity from scratch, with no pairing ansatz and no mean-field warm-start, this work shows that self-attention neural networks are powerful enough to discover topological quantum phases without human guidance, opening a systematic path to AI-driven quantum materials discovery.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits squarely at the intersection of modern AI architecture and condensed matter physics, showing that transformer self-attention, developed for language, turns out to be a natural framework for quantum correlations between electrons.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">A single general-purpose self-attention wavefunction architecture generalizes across diverse quantum phases, including topologically nontrivial superconductors, without any problem-specific modifications.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">For the first time, chiral *p_x ± ip_y* superconductivity with its characteristic reversed odd-even binding energy signature has been obtained variationally from an unbiased neural network, surpassing BCS mean-field theory in the strong-coupling regime.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work targets strongly correlated electron materials where unconventional superconductivity remains poorly understood. The full paper is available at [arXiv:2509.03683](https://arxiv.org/abs/2509.03683).</span></div></div>
</div>
