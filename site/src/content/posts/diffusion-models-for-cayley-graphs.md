---
abstract: We review the problem of finding paths in Cayley graphs of groups and group
  actions, using the Rubik's cube as an example, and we list several more examples
  of significant mathematical interest. We then show how to formulate these problems
  in the framework of diffusion models. The exploration of the graph is carried out
  by the forward process, while finding the target nodes is done by the inverse backward
  process. This systematizes the discussion and suggests many generalizations. To
  improve exploration, we propose a ``reversed score'' ansatz which substantially
  improves over previous comparable algorithms.
arxivId: '2503.05558'
arxivUrl: https://arxiv.org/abs/2503.05558
authors:
- Michael R. Douglas
- Kit Fraser-Taliente
concepts:
- diffusion models
- group theory
- cayley graph navigation
- reversed score ansatz
- score-based models
- stochastic processes
- reinforcement learning
- geometric deep learning
- symmetry preservation
- inverse problems
- quantum computing
figures:
- /iaifi-research-blog/figures/2503_05558/figure_1.png
- /iaifi-research-blog/figures/2503_05558/figure_2.png
- /iaifi-research-blog/figures/2503_05558/figure_3.png
pdfUrl: https://arxiv.org/pdf/2503.05558v1
published: '2025-03-07T16:33:16+00:00'
theme: Foundational AI
title: Diffusion Models for Cayley Graphs
wordCount: 1034
---

## The Big Picture

Picture a Rubik's Cube sitting scrambled on your desk. You can make any of 12 moves (rotate a face clockwise or counterclockwise) and your goal is to reach the solved state from whatever chaos you started with. Simple to state. Fiendishly hard to solve.

This plastic toy is a window into one of the deep structures in mathematics: **group theory**, the study of symmetry and how operations combine and reverse.

Now imagine that instead of a toy, the puzzle is a system of equations where numbers cycle like a clock, wrapping around instead of growing forever. Or the problem of compiling an optimal quantum circuit. Or an open conjecture in algebra that has stumped mathematicians for decades.

These problems look completely different on the surface, but they share a common skeleton: they're all questions about finding short paths in a **Cayley graph**, a network where every node is a mathematical object and every edge represents a single allowed operation. Solving these puzzles is about navigation through an astronomically large space.

Researchers Michael R. Douglas and Kit Fraser-Taliente have shown that **diffusion models** (the same class of AI behind image generators like DALL-E and Stable Diffusion) give a unified framework for this entire family of navigation problems.

> **Key Insight:** The two phases of a diffusion model map perfectly onto the two phases of graph navigation: the noisy *forward* process explores the graph, while the learned *backward* process finds the path to the goal.

## How It Works

Every Cayley graph has a natural home base: the **identity element**, the group's "do nothing" state, the solved cube, the point every algorithm is trying to reach. Every sequence of moves from that starting point traces a path through the graph.

For the Rubik's Cube, the nodes are cube states and the edges are legal moves. The group $G_{\text{Rubik}}$ has roughly $4 \times 10^{19}$ elements, yet every scrambled position can be solved in at most 26 moves. The graph's **diameter** (the longest shortest path between any two nodes) is tiny relative to its size.

![Figure 1](figure:1)

Standard AI solvers, like DeepCubeA, train a neural network to estimate a **cost-to-go function**: how many steps are you from the goal? Training data comes from random walks *outward* from the solved state (scrambling the cube step by step) with each position labeled by the number of steps taken. The solver then runs *backward*, always preferring moves that decrease the distance estimate.

Douglas and Fraser-Taliente recognized that this two-phase structure (random diffusion outward, then guided reversal) is exactly what diffusion models do. In image generation, the forward process adds random noise until a picture becomes pure static; the backward process learns to denoise, reconstructing coherence. In graph navigation:

- **Forward process:** random walks from the identity, exploring the graph
- **Score function:** a learned model predicting what move most likely produced the current position
- **Backward process:** using the score function greedily to navigate back toward the goal

The score function is the key object. Previous work trained a predictor for the *last move* applied in a random walk, learning to read the "fingerprints" of how you got somewhere. Douglas and Fraser-Taliente systematize this as a diffusion model score function, then introduce their central innovation: the **reversed score ansatz**.

The idea is elegant. Instead of predicting the last move forward, you flip the logic: train the model on what move would be applied in a mirrored walk going *backward* from the goal. Since every move has a corresponding reverse move, you can construct this reversed walk and learn its score. The reversed score captures not just "where you came from" but "where you should go," and in experiments it substantially improved over comparable previous algorithms.

![Figure 2](figure:2)

## Why It Matters

The Rubik's Cube is just the most photogenic example. The group $SL_2(\mathbb{Z})$ (2×2 integer matrices with unit determinant) encodes problems related to the Euclidean algorithm. The group $SL_2(\mathbb{Z}_p)$ over finite fields generates **Ramanujan graphs**, the expander graph constructions underpinning modern error-correcting codes and cryptography.

The **Andrews-Curtis conjecture**, a 60-year-old open problem in combinatorial group theory, can be cast as a path-finding problem on a Cayley graph of group actions. **Quantum circuit compilation** (arranging gates to implement a target unitary) fits this template when the gate set generates a finite subgroup of the unitary group.

![Figure 3](figure:3)

What makes this more than a clever rebranding is the systematization it provides. By casting all these problems in the language of diffusion models, you gain access to a mature toolkit: score-based generative modeling, learned noise schedules, search algorithms like beam search, and deep connections to statistical physics. The paper outlines several generalizations: diffusion on Cayley graphs of group *actions*, connections to Monte Carlo methods, and the prospect of adapting techniques like classifier-free guidance to graph navigation.

The framework also clarifies *why* Cayley graphs are special. Their homogeneity (the fact that every node looks the same) is what makes exploration and inversion tractable in ways impossible for arbitrary graphs.

The work sits at a productive intersection: insights from physics (diffusion, score functions, statistical mechanics) applied to hard mathematical problems through modern AI. That feedback loop, math inspiring AI inspiring math, keeps producing results neither field could reach alone.

> **Bottom Line:** By recognizing that Cayley graph navigation is a diffusion problem in disguise, Douglas and Fraser-Taliente provide a unified framework connecting Rubik's Cube, quantum computing, and open conjectures in mathematics, while a new "reversed score" trick delivers measurable algorithmic gains.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects generative AI (diffusion models) with pure mathematics (group theory, Cayley graphs), showing that the same probabilistic framework powering image synthesis can tackle problems in algebra and combinatorics.

- **Impact on Artificial Intelligence:** The reversed score ansatz offers a concrete algorithmic improvement for learning-based graph navigation, with implications for any reinforcement learning problem with group symmetry structure.

- **Impact on Fundamental Interactions:** Quantum circuit compilation (a central challenge in quantum computing) fits the Cayley graph framework, meaning these methods could accelerate the design of efficient quantum hardware operations.

- **Outlook and References:** Future directions include applying this framework to the Andrews-Curtis conjecture and expander graph problems; preprint available at [arXiv:2503.05558](https://arxiv.org/abs/2503.05558).
