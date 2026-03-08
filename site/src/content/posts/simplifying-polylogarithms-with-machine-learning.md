---
abstract: Polylogrithmic functions, such as the logarithm or dilogarithm, satisfy
  a number of algebraic identities. For the logarithm, all the identities follow from
  the product rule. For the dilogarithm and higher-weight classical polylogarithms,
  the identities can involve five functions or more. In many calculations relevant
  to particle physics, complicated combinations of polylogarithms often arise from
  Feynman integrals. Although the initial expressions resulting from the integration
  usually simplify, it is often difficult to know which identities to apply and in
  what order. To address this bottleneck, we explore to what extent machine learning
  methods can help. We consider both a reinforcement learning approach, where the
  identities are analogous to moves in a game, and a transformer network approach,
  where the problem is viewed analogously to a language-translation task. While both
  methods are effective, the transformer network appears more powerful and holds promise
  for practical use in symbolic manipulation tasks in mathematical physics.
arxivId: '2206.04115'
arxivUrl: https://arxiv.org/abs/2206.04115
authors:
- Aurélien Dersy
- Matthew D. Schwartz
- Xiaoyuan Zhang
concepts:
- transformers
- polylogarithm identities
- reinforcement learning
- symbolic computation
- scattering amplitudes
- symbol calculus
- quantum field theory
- inverse problems
- automated discovery
- attention mechanisms
figures:
- /iaifi-research-blog/figures/2206_04115/figure_3.png
- /iaifi-research-blog/figures/2206_04115/figure_3.png
pdfUrl: https://arxiv.org/pdf/2206.04115v1
published: '2022-06-08T18:20:21+00:00'
theme: Theoretical Physics
title: Simplifying Polylogarithms with Machine Learning
wordCount: 1140
---

## The Big Picture

Imagine you're trying to solve a jigsaw puzzle where every piece can morph into multiple shapes depending on which pieces surround it. That's roughly what physicists face when simplifying the sprawling mathematical expressions that emerge from quantum field theory calculations. These expressions are built from **polylogarithms**, a family of functions that includes the familiar logarithm and extends into increasingly exotic territory with the dilogarithm, trilogarithm, and beyond. The catch: these functions obey dozens of tangled **algebraic identities** (rules that let you rewrite one expression as a secretly equivalent, simpler one), and knowing which identity to apply, and when, is more art than science.

When physicists compute something like the probability of an electron scattering off a photon, they evaluate **Feynman integrals**, mathematical objects that sum over all the quantum paths a particle can take. These integrals routinely produce enormous polylogarithmic expressions: pages of terms that, in principle, collapse to something much simpler, but only if you apply the right sequence of transformations. Getting from raw output to a clean result can take experienced researchers days, and no systematic algorithm guarantees success.

A team at Harvard's Department of Physics and IAIFI wanted to know whether machine learning could crack this bottleneck. It turns out a transformer network, the architecture behind modern language models, can simplify polylogarithmic expressions surprisingly well.

> **Key Insight:** Simplifying polylogarithms is structurally identical to translating between languages, and transformer networks, trained to do exactly that, turn out to be powerful symbolic mathematicians.

## How It Works

The researchers framed the simplification problem in two very different ways and pitted the approaches against each other:

- **Reinforcement learning (RL):** A trial-and-error strategy where each algebraic identity (reflection, duplication, inversion, and others) becomes a legal "move." The agent learns to play the game of simplification by trying sequences of moves and receiving a reward when the expression shrinks. Like a chess engine learning sacrifices that pay off three moves later, the RL agent must tolerate short-term complexity to reach long-term simplicity.
- **Sequence-to-sequence translation:** A **transformer network**, the same architecture used in large language models, treats simplification as a translation task. The input is a messy polylogarithmic expression written as a sequence of tokens; the output is the simplified form. The model never explicitly reasons about which identities to apply. It learns, from millions of training examples, what simplified expressions look like and how to get there.

![Figure 1](/iaifi-research-blog/figures/2206_04115/figure_3.png)

To generate training data, the team ran the simplification process in reverse: they started from simple, canonical expressions and applied identities *forward* to produce complex ones, creating (complex → simple) pairs without needing to solve the hard direction first. Generating hard instances from easy ones is always tractable, a clever inversion that sidesteps the core difficulty.

One important tool in both approaches is the **symbol**, an algebraic object that encodes the "skeleton" of a polylogarithmic function. For the dilogarithm (written Li₂(x)), the symbol is (1−x) ⊗ x, a compact expression that strips away lower-order terms and exposes the function's core structure. The symbol satisfies a simple product rule, making it easier to manipulate than the full function. Both the RL agent and the transformer can work on the full polylogarithmic expression or its symbol, and the paper tests all combinations.

![Figure 2](/iaifi-research-blog/figures/2206_04115/figure_3.png)

The results clearly favor the transformer. Operating on symbolic expressions, it achieves high simplification rates across a range of complexity levels, including cases requiring many nested identity applications. The RL approach works, but it struggles as expressions grow larger and the search space explodes. The transformer generalizes; the RL agent grinds.


There is also an elegant secondary finding: the transformer trained on symbols can often reconstruct the full polylogarithmic form from the symbol alone, essentially solving an inverse problem with no known algorithmic solution. Given the "French" (the symbol), the model recovers the "English" (the polylogarithm).

## Why It Matters

The immediate payoff is practical. Simplifying polylogarithmic expressions is a genuine bottleneck in high-energy physics calculations. Two-loop scattering amplitudes, needed for precision predictions at colliders like the LHC, routinely produce exactly the kind of sprawling output this system can tame. A reliable ML-assisted simplification tool could compress days of expert work into seconds, opening the door to calculations that are currently out of reach.

But the implications go further. The transformer's success hints at something about mathematical physics itself: that symbolic simplification, long thought to require human intuition, may be learnable from data. This connects to a growing body of work using neural networks for symbolic mathematics, from integrating functions to discovering identities in representation theory. What sets this paper apart is its focus on a problem where *no complete algorithmic solution exists*. The machine learning approach isn't just faster; it's qualitatively different from anything currently available.

> **Bottom Line:** Transformer networks can learn to simplify complex polylogarithmic expressions that arise in particle physics, a task with no known complete algorithm, suggesting that machine learning may become a standard tool in theoretical physics computation.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies transformer-based language modeling, a core AI technique, directly to one of the most stubborn bottlenecks in theoretical particle physics, showing that symbolic simplification is a learnable task.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper shows that transformers can solve inverse symbolic problems (reconstructing functions from their algebraic skeletons) where no algorithmic inverse is known, pushing the boundaries of neural symbolic reasoning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Automating polylogarithm simplification could unlock higher-order Feynman integral calculations needed for precision predictions at colliders, feeding directly into tests of the Standard Model.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend these methods to multiple polylogarithms and functions of several variables, which appear in more complex scattering amplitude calculations; the paper is available at [arXiv:2206.04115](https://arxiv.org/abs/2206.04115).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Simplifying Polylogarithms with Machine Learning</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2206.04115</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Aur\u00e9lien Dersy", "Matthew D. Schwartz", "Xiaoyuan Zhang"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Polylogrithmic functions, such as the logarithm or dilogarithm, satisfy a number of algebraic identities. For the logarithm, all the identities follow from the product rule. For the dilogarithm and higher-weight classical polylogarithms, the identities can involve five functions or more. In many calculations relevant to particle physics, complicated combinations of polylogarithms often arise from Feynman integrals. Although the initial expressions resulting from the integration usually simplify, it is often difficult to know which identities to apply and in what order. To address this bottleneck, we explore to what extent machine learning methods can help. We consider both a reinforcement learning approach, where the identities are analogous to moves in a game, and a transformer network approach, where the problem is viewed analogously to a language-translation task. While both methods are effective, the transformer network appears more powerful and holds promise for practical use in symbolic manipulation tasks in mathematical physics.</span></div></div>
</div>
