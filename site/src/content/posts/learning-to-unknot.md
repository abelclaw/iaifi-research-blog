---
abstract: We introduce natural language processing into the study of knot theory,
  as made natural by the braid word representation of knots. We study the UNKNOT problem
  of determining whether or not a given knot is the unknot. After describing an algorithm
  to randomly generate $N$-crossing braids and their knot closures and discussing
  the induced prior on the distribution of knots, we apply binary classification to
  the UNKNOT decision problem. We find that the Reformer and shared-QK Transformer
  network architectures outperform fully-connected networks, though all perform well.
  Perhaps surprisingly, we find that accuracy increases with the length of the braid
  word, and that the networks learn a direct correlation between the confidence of
  their predictions and the degree of the Jones polynomial. Finally, we utilize reinforcement
  learning (RL) to find sequences of Markov moves and braid relations that simplify
  knots and can identify unknots by explicitly giving the sequence of unknotting actions.
  Trust region policy optimization (TRPO) performs consistently well for a wide range
  of crossing numbers and thoroughly outperformed other RL algorithms and random walkers.
  Studying these actions, we find that braid relations are more useful in simplifying
  to the unknot than one of the Markov moves.
arxivId: '2010.16263'
arxivUrl: https://arxiv.org/abs/2010.16263
authors:
- Sergei Gukov
- James Halverson
- Fabian Ruehle
- Piotr Sułkowski
concepts:
- knot theory
- braid word representation
- reinforcement learning
- transformers
- classification
- jones polynomial
- embeddings
- attention mechanisms
- reward optimization
- automated discovery
- interpretability
figures:
- /iaifi-research-blog/figures/2010_16263/figure_1.png
- /iaifi-research-blog/figures/2010_16263/figure_1.png
- /iaifi-research-blog/figures/2010_16263/figure_2.png
- /iaifi-research-blog/figures/2010_16263/figure_2.png
- /iaifi-research-blog/figures/2010_16263/figure_3.png
- /iaifi-research-blog/figures/2010_16263/figure_3.png
pdfUrl: https://arxiv.org/pdf/2010.16263v1
published: '2020-10-28T18:00:05+00:00'
theme: Theoretical Physics
title: Learning to Unknot
wordCount: 1214
---

## The Big Picture

Imagine handing a tangled ball of string to a mathematician and asking: "Is this actually knotted, or could you untangle it into a simple loop if you had enough patience?" This question, the **UNKNOT problem**, sits at the heart of one of mathematics' oldest open challenges. Easy to state, fiendishly hard to solve, and connected to the same technology powering your email autocomplete.

Knots appear throughout fundamental science: in protein folding, in the search for possible string theory universes, and in deep unsolved questions about four-dimensional geometry, including the famous smooth Poincaré conjecture. Existing algorithms scale explosively with complexity. Human intuition fails spectacularly for knots with many crossings.

A team from Caltech, Northeastern, CERN, Oxford, and Warsaw took a lateral approach: they taught a neural network to read knots like sentences, then trained a reinforcement learning agent to untangle them step by step. The result classifies knots with high accuracy and can prove a knot is trivial by showing you the moves.

> **Key Insight:** Knots encoded as braid words are formally equivalent to sentences in a language, and transformer neural networks trained on natural language turn out to be very good at detecting the unknot, with accuracy that *improves* as the knot gets more complex.

## How It Works

The key conceptual leap is representing knots as **braid words**, sequences of symbols like σ₁, σ₂⁻¹, σ₁, σ₂, where each symbol describes how strands cross over or under each other. Close the ends of a braid and you get a knot. A braid word is a sequence of characters drawn from a finite alphabet, which is exactly what language models were built to handle.

![Figure 1](figure:1)

The researchers generated N-crossing braids and balanced datasets of unknots and genuine knots, then trained several neural architectures on yes-or-no classification: given this braid word, is it the unknot?

- **Fully-connected networks**, the baseline, which performed well but not best
- **Shared-QK Transformers**, attention models where query and key matrices are tied together, reducing the number of parameters
- **Reformers**, a memory-efficient transformer variant that uses clever indexing shortcuts to handle long sequences without running out of memory

The Reformer and shared-QK Transformer both outperformed the baseline. What's less obvious: the longer the braid word, the *higher* the classification accuracy. More crossings should mean a harder problem, but longer braid words carry more redundancy and context, giving the attention mechanism more signal to work with.

![Figure 2](figure:2)

The team also found a deep connection between classifier confidence and the **Jones polynomial**, a knot invariant (a quantity that stays fixed under any deformation, as long as you don't cut the knot) introduced in 1984. Highly confident predictions correlated strongly with the degree of the Jones polynomial. The network didn't know about the Jones polynomial. It rediscovered this correlation from braid words alone.

**Unknotting as a Game**

Classification tells you *whether* a knot is trivial. Reinforcement learning tells you *how* to untangle it.

![Figure 3](figure:3)

The researchers formulated unknotting as a game. An RL agent observes the current braid and chooses from legal moves: **Markov moves** (which change the number of strands while preserving the underlying knot) and **braid relations** (local rewriting rules that simplify crossings without changing the knot type). The reward is simple: simplify the braid, earn points. Unknot it completely, and win.

Among several RL algorithms tested (PPO, A2C, random walkers), **Trust Region Policy Optimization (TRPO)** clearly dominated. TRPO constrains how much the policy can change per update, preventing catastrophic forgetting and enabling stable learning across a wide range of crossing numbers.

Looking at the agent's choices revealed something mathematically concrete: braid relations proved far more useful than one of the two Markov moves (stabilization), which was rarely helpful. This is a direct, actionable insight for mathematicians designing knot simplification algorithms.

![Figure 4](figure:4)

Unlike the classifier, the RL agent provides a *proof*. When it successfully unknots a braid, it hands you an explicit, mechanically verifiable sequence of moves, transforming a probabilistic prediction into a mathematical certificate.

## Why It Matters

The UNKNOT problem is believed to be decidable but not known to be in NP; its computational complexity remains open. Tools that rapidly classify or simplify knots help mathematicians probe this question. The Jones polynomial connection raises a natural follow-up: if networks are implicitly approximating this invariant, perhaps they can be reverse-engineered to discover new ones.

On the physics side, knots appear in string theory compactifications, lattice gauge theories, and topological quantum computing. The NLP framing also opens a broader door. Other mathematical structures with discrete symbolic representations (Lie algebras, Calabi-Yau manifolds, Diophantine equations) could be treated as languages and fed to transformers. This paper makes a concrete case for that entire research program.

> **Bottom Line:** By treating knots as sentences and unknotting as a game, this team showed that modern AI can both classify and actively solve one of mathematics' oldest topological puzzles, while uncovering an unexpected connection between neural networks and the Jones polynomial.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work sits at the intersection of topology, NLP, and reinforcement learning. Encoding knots as braid-word "sentences" and training transformer architectures and RL agents on them shows that AI tools developed for language can make real headway on problems in fundamental mathematics and physics.

- **Impact on Artificial Intelligence:** Attention-based architectures (Reformers, shared-QK Transformers) outperform fully-connected networks on combinatorial mathematical problems, and classification accuracy *increases* with sequence length, a counterintuitive result with implications for how transformers handle structured symbolic data.

- **Impact on Fundamental Interactions:** The RL agent's move analysis reveals that braid relations are more useful than one of the Markov moves for unknotting, and the classifier's confidence correlates with the degree of the Jones polynomial, connecting deep learning to one of knot theory's central invariants.

- **Outlook and References:** Future work could extend these methods to harder knot invariants, more complex topological problems, and other symbolic mathematical structures; the paper is available at [arXiv:2010.16263](https://arxiv.org/abs/2010.16263).

## Original Paper Details
- **Title:** Learning to Unknot
- **arXiv ID:** 2010.16263
- **Authors:** ["Sergei Gukov", "James Halverson", "Fabian Ruehle", "Piotr Sułkowski"]
- **Abstract:** We introduce natural language processing into the study of knot theory, as made natural by the braid word representation of knots. We study the UNKNOT problem of determining whether or not a given knot is the unknot. After describing an algorithm to randomly generate $N$-crossing braids and their knot closures and discussing the induced prior on the distribution of knots, we apply binary classification to the UNKNOT decision problem. We find that the Reformer and shared-QK Transformer network architectures outperform fully-connected networks, though all perform well. Perhaps surprisingly, we find that accuracy increases with the length of the braid word, and that the networks learn a direct correlation between the confidence of their predictions and the degree of the Jones polynomial. Finally, we utilize reinforcement learning (RL) to find sequences of Markov moves and braid relations that simplify knots and can identify unknots by explicitly giving the sequence of unknotting actions. Trust region policy optimization (TRPO) performs consistently well for a wide range of crossing numbers and thoroughly outperformed other RL algorithms and random walkers. Studying these actions, we find that braid relations are more useful in simplifying to the unknot than one of the Markov moves.
