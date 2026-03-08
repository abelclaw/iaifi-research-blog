---
abstract: Do neural networks, trained on well-understood algorithmic tasks, reliably
  rediscover known algorithms for solving those tasks? Several recent studies, on
  tasks ranging from group arithmetic to in-context linear regression, have suggested
  that the answer is yes. Using modular addition as a prototypical problem, we show
  that algorithm discovery in neural networks is sometimes more complex. Small changes
  to model hyperparameters and initializations can induce the discovery of qualitatively
  different algorithms from a fixed training set, and even parallel implementations
  of multiple such algorithms. Some networks trained to perform modular addition implement
  a familiar Clock algorithm; others implement a previously undescribed, less intuitive,
  but comprehensible procedure which we term the Pizza algorithm, or a variety of
  even more complex procedures. Our results show that even simple learning problems
  can admit a surprising diversity of solutions, motivating the development of new
  tools for characterizing the behavior of neural networks across their algorithmic
  phase space.
arxivId: '2306.17844'
arxivUrl: https://arxiv.org/abs/2306.17844
authors:
- Ziqian Zhong
- Ziming Liu
- Max Tegmark
- Jacob Andreas
concepts:
- interpretability
- mechanistic explanation
- algorithmic phase space
- phase transitions
- embeddings
- attention mechanisms
- transformers
- representation learning
- symmetry preservation
- group theory
- dimensionality reduction
figures:
- /iaifi-research-blog/figures/2306_17844/figure_1.png
- /iaifi-research-blog/figures/2306_17844/figure_1.png
- /iaifi-research-blog/figures/2306_17844/figure_2.png
- /iaifi-research-blog/figures/2306_17844/figure_2.png
- /iaifi-research-blog/figures/2306_17844/figure_3.png
- /iaifi-research-blog/figures/2306_17844/figure_3.png
pdfUrl: https://arxiv.org/pdf/2306.17844v2
published: '2023-06-30T17:59:13+00:00'
theme: Foundational AI
title: 'The Clock and the Pizza: Two Stories in Mechanistic Explanation of Neural
  Networks'
wordCount: 1066
---

## The Big Picture

If a meeting starts at 10 and lasts 3 hours, it ends at 1. You solved that using a clock — and so, apparently, does a neural network. When researchers trained small AI models called transformers to perform modular arithmetic (the kind of math that wraps around like a clock face), a 2022 study found something elegant: the networks spontaneously rediscovered the clockface approach. Numbers were encoded as angles, the angles were added, and out came the answer. A clean, geometric solution hiding inside the learned workings of a neural net.

But what happens when you tweak the design? Change how the model processes information, adjust its size, or shift its random starting point? The researchers behind this new paper did exactly that — and found something unexpected. Different networks learned completely different algorithms to solve the same problem. Not variations on the clock, but something else entirely. Something that looks less like a clock and more like a pizza.

The paper's central finding: for even the simplest well-defined algorithmic tasks, neural networks can land on a surprising diversity of internal solutions, and small design changes can push them across sharp boundaries between qualitatively different algorithms.

> **Key Insight:** Neural networks don't reliably rediscover a single "correct" algorithm for a task — even a simple one. The same training data can produce qualitatively different internal procedures, depending on architecture choices and initialization.

## How It Works

The researchers focused on **modular addition**: given two numbers *a* and *b*, compute *(a + b) mod p*, where *p* = 59. Think of it as arithmetic on a circle with 59 positions. They trained two model variants — **Model A**, a one-layer transformer with fixed (non-learned) attention, effectively a ReLU MLP, and **Model B**, a standard one-layer ReLU transformer with trainable attention.

The previously known **Clock algorithm** works like this:

1. Embed each input number as a point on a unit circle — number *a* becomes the angle *2πka/p* for some frequency *k*
2. Use the attention mechanism to multiply the trigonometric components and extract the angle *a + b*
3. Read off the answer by matching the resulting angle to the output embedding

Crucially, the Clock algorithm requires multiplication — and the transformer's attention mechanism provides it. Model B, with standard trainable attention, implements this cleanly.

![Figure 1](/iaifi-research-blog/figures/2306_17844/figure_1.png)

Model A is a different story. Without learnable attention, it can't multiply the same way. Two signs revealed this. First, the output scores (logits) for each possible answer showed perfect **gradient symmetry** — the network treated inputs *a* and *b* as completely interchangeable. The Clock algorithm breaks this symmetry, so whatever Model A was doing, it wasn't the Clock. Second, while both models learned circular embeddings, the intermediate computations diverged sharply.

What Model A discovered is the **Pizza algorithm** — named because it treats the circle not as a continuous angle-space but as something divided into sectors, like pizza slices:

1. Embed *a* and *b* as circular vectors, just like the Clock algorithm
2. Compute the **vector mean**: average the two input embeddings to get a midpoint vector
3. Apply an **absolute value nonlinearity** — a step that folds negative values to positive, extracting amplitude — yielding a quantity proportional to |cos(wk(a−b)/2)|, which encodes the difference between *a* and *b*
4. Combine amplitude and direction to reconstruct the sum *a + b*

The math works because the mean of two unit-circle vectors points in the direction of their angle average, and its magnitude encodes the angle difference. No multiplication required — just the absolute value step.

![Figure 2](/iaifi-research-blog/figures/2306_17844/figure_1.png)

What makes this striking are the **phase transitions**. Systematically varying model width and attention strength, the researchers found sharp boundaries where models flipped from Clock to Pizza. They also uncovered messier **non-circular algorithms** using line-like or Lissajous-curve embeddings (patterns traced by two overlapping oscillations, like a spirograph), and some models ran multiple imperfect Pizza copies in parallel, voting on the answer. The algorithmic landscape has structure — but far richer than anyone expected.

![Figure 4](/iaifi-research-blog/figures/2306_17844/figure_2.png)

## Why It Matters

A core assumption in interpretability research — sometimes stated, often tacit — is that identifying *one* algorithm a network uses to solve a task means you've understood something fundamental about how that task gets solved. This paper challenges that directly.

Same task, same training data, same basic architecture family: different algorithms. Not different implementations of the same idea, but different mathematical procedures with different computational signatures.

This means interpretability work needs to think in terms of **algorithmic phase spaces** — the full map of possible internal solutions — not single algorithmic solutions. Finding one clean story isn't enough. You need to characterize the full space of possible stories and understand what determines which story any given network will tell. That's a harder problem, but a more honest one.

It also connects to physics: transitions between algorithmic regimes look structurally similar to phase transitions in physical systems, and the tools physicists use to characterize phase diagrams may find a new home in neural network analysis.

> **Bottom Line:** Neural networks don't converge on a single algorithm for algorithmic tasks — they explore a phase space of solutions, and small architectural changes can trigger sharp transitions between qualitatively different approaches. Reliable interpretability tools will require mapping this phase space, not just finding one good story.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies the physics concept of phase transitions to neural network algorithms, showing that networks undergo sharp, qualitative shifts in their internal computational strategies as architectural parameters vary — a framework directly inspired by condensed matter physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The discovery of the Pizza algorithm and the characterization of algorithmic phase spaces challenges a foundational assumption in mechanistic interpretability: that networks reliably converge on known algorithms, motivating new tools for systematically mapping the full diversity of solutions neural networks can discover.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By demonstrating that mechanistic understanding of even simple learned systems is more complex than previously thought, this work urges caution when assuming a network has "learned" a known physical law or algorithm in scientific applications.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work should develop systematic methods for exploring algorithmic phase spaces across model families, transforming how researchers validate neural network solutions in scientific domains; the paper appeared at NeurIPS 2023 and is available on arXiv, with code at github.com/fjzzq2002/pizza.</span></div></div>
</div>
