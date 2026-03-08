---
abstract: 'When two AI models are trained on the same scientific task, do they learn
  the same theory or two different theories? Throughout history of science, we have
  witnessed the rise and fall of theories driven by experimental validation or falsification:
  many theories may co-exist when experimental data is lacking, but the space of survived
  theories become more constrained with more experimental data becoming available.
  We show the same story is true for AI scientists. With increasingly more systems
  provided in training data, AI scientists tend to converge in the theories they learned,
  although sometimes they form distinct groups corresponding to different theories.
  To mechanistically interpret what theories AI scientists learn and quantify their
  agreement, we propose MASS, Hamiltonian-Lagrangian neural networks as AI Scientists,
  trained on standard problems in physics, aggregating training results across many
  seeds simulating the different configurations of AI scientists. Our findings suggests
  for AI scientists switch from learning a Hamiltonian theory in simple setups to
  a Lagrangian formulation when more complex systems are introduced. We also observe
  strong seed dependence of the training dynamics and final learned weights, controlling
  the rise and fall of relevant theories. We finally demonstrate that not only can
  our neural networks aid interpretability, it can also be applied to higher dimensional
  problems.'
arxivId: '2504.02822'
arxivUrl: https://arxiv.org/abs/2504.02822
authors:
- Xinghong Fu
- Ziming Liu
- Max Tegmark
concepts:
- hamiltonian systems
- lagrangian methods
- ai scientist agreement
- interpretability
- physics-informed neural networks
- theory space convergence
- automated discovery
- seed dependence
- representation learning
- conservation laws
- ensemble methods
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2504_02822/figure_1.png
- /iaifi-research-blog/figures/2504_02822/figure_2.png
- /iaifi-research-blog/figures/2504_02822/figure_3.png
pdfUrl: https://arxiv.org/pdf/2504.02822v1
published: '2025-04-03T17:58:44+00:00'
theme: Foundational AI
title: Do Two AI Scientists Agree?
wordCount: 956
---

## The Big Picture

Imagine two physicists locked in separate rooms, handed the same experimental data. They work independently for months. When they emerge, do they present the same theory? History says the answer is complicated: Newton and Leibniz both invented calculus, arriving at equivalent but noticeably different notations. The question grows stranger when those "physicists" are neural networks.

That's what researchers Xinghong Fu, Ziming Liu, and Max Tegmark at MIT's IAIFI set out to probe. When two AI models are trained independently on identical physics problems, do they discover the same underlying laws, or diverge into competing frameworks? As AI systems take on larger roles in scientific discovery, their tendency to agree (or disagree) could shape which theories humanity ends up pursuing.

The answer mirrors the history of science itself. AI scientists trained on sparse data fragment into competing camps. Feed them richer, more complex data, and they converge, but not arbitrarily. They converge on the *same* framework that physicists spent centuries wrestling to identify.

> **Key Insight:** AI scientists independently trained on classical mechanics problems preferentially learn either Hamiltonian or Lagrangian descriptions. With enough data complexity, they overwhelmingly converge on the Lagrangian formulation, mirroring how scientific consensus emerges through experimental pressure.

## How It Works

The team built **MASS** (Multi-physics AI Scalar Scientist), a neural network architecture that learns simultaneously from multiple physical systems. Rather than predicting specific outputs, MASS learns a single mathematical expression: either a **Hamiltonian** (a formula for total energy that yields equations of motion) or a **Lagrangian** (a formula capturing the difference between kinetic and potential energy that yields the same equations via a different mathematical path). Both approaches are equivalent for standard problems, which is exactly what makes their competition interesting.

![Figure 2](figure:2)

Here's how the experiment works:

1. **Train many independent networks** on the same physical problem, varying only the random seed, the neural-network equivalent of giving two scientists different personal histories and intuitions.
2. **Probe what each network learned** by analyzing its internal signals to identify whether it has internalized a Hamiltonian or Lagrangian representation.
3. **Measure agreement** across all trained networks, asking whether the "scientific community" of AI models has reached consensus.
4. **Scale up complexity** by introducing harder problems (the double pendulum, the Kepler problem, synthetic potentials) and watch which theory takes over.

On simple systems like a single pendulum, the results are striking in their diversity. Different training seeds produce networks that land in distinct theoretical camps: some learn Hamiltonian descriptions, others Lagrangian. Neither is wrong. Both accurately describe a swinging pendulum. But they represent genuinely different internal pictures of reality.

![Figure 1](figure:1)

Then comes data pressure. As MASS encountered increasingly complex systems, with nonstandard potentials and higher-dimensional dynamics, Hamiltonian-trained networks began to fail. The Lagrangian formulation generalizes more readily to exotic physics beyond the textbook canon. Networks that had learned Hamiltonian representations either adapted toward Lagrangian or fell behind. The AI scientific community converged, not by vote, but by survival.

The team also documented something subtler and more unsettling: **seed dependence** (how much a network's random starting conditions shape which theory it learns) is enormous. Two networks with identical architectures and identical training data, differing only in initial weights, can arrive at fundamentally different physical frameworks. It's a computational analogue of path dependence in science: the accidents of early training shaping which paradigm a researcher adopts.

## Why It Matters

This research asks not just "can AI do physics?" but "what physics will AI do, and will different AIs agree?" The distinction matters as autonomous AI research systems grow more capable. If ten independent AI labs train models on the same cosmological dataset, will they propose the same theory of dark energy, or fragment into schools, as human physicists sometimes do?

That Lagrangian dynamics emerges as the "singular accurate family of descriptions" in a rich theory space will come as no surprise to physicists, who have long favored Lagrangian and Hamiltonian approaches not just for elegance but for generalizability. What's striking is that MASS rediscovers this preference from scratch, through pure data pressure, with no human hand guiding it toward those frameworks.

![Figure 3](figure:3)

The framework opens harder questions. Can AI scientists discover genuinely *new* frameworks that generalize even beyond the Lagrangian? What happens when training data contains noise or systematic errors, as real experimental data always does? And can seed dependence be tamed, or does it represent an irreducible randomness in how intelligent systems carve nature at its joints?

MASS also has practical value as a tool for learning dynamical systems in higher dimensions, extending beyond what traditional **symbolic regression** (finding mathematical formulas that fit data) can handle.

> **Bottom Line:** AI scientists, like human ones, fragment when data is scarce and converge under experimental pressure, and they independently rediscover the Lagrangian formulation as the most generalizable framework in classical mechanics. Scientific consensus, it seems, isn't purely a social phenomenon.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work fuses the epistemology of scientific theory formation with neural network training dynamics, using physics's canonical frameworks as a testbed for studying how AI systems discover laws from data.
- **Impact on Artificial Intelligence:** MASS introduces a unified architecture subsuming both Hamiltonian and Lagrangian neural networks, providing a new tool for learning dynamical systems in higher-dimensional settings beyond the reach of prior approaches.
- **Impact on Fundamental Interactions:** The study provides empirical evidence that the Lagrangian formulation is not merely a human convention but an emergent preference in data-driven theory discovery, reinforcing its privileged status in fundamental physics.
- **Outlook and References:** Future work may probe whether MASS can discover genuinely novel physical formalisms in domains where no established theory exists; the paper is available at [arXiv:2504.02822](https://arxiv.org/abs/2504.02822) and code is released at github.com/shinfxh/ai-scientists.
