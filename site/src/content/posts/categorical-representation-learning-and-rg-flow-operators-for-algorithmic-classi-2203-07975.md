---
abstract: 'Following the earlier formalism of the categorical representation learning
  (arXiv:2103.14770) by the first two authors, we discuss the construction of the
  "RG-flow based categorifier". Borrowing ideas from theory of renormalization group
  flows (RG) in quantum field theory, holographic duality, and hyperbolic geometry,
  and mixing them with neural ODE''s, we construct a new algorithmic natural language
  processing (NLP) architecture, called the RG-flow categorifier or for short the
  RG categorifier, which is capable of data classification and generation in all layers.
  We apply our algorithmic platform to biomedical data sets and show its performance
  in the field of sequence-to-function mapping. In particular we apply the RG categorifier
  to particular genomic sequences of flu viruses and show how our technology is capable
  of extracting the information from given genomic sequences, find their hidden symmetries
  and dominant features, classify them and use the trained data to make stochastic
  prediction of new plausible generated sequences associated with new set of viruses
  which could avoid the human immune system. The content of the current article is
  part of the recent US patent application submitted by first two authors (U.S. Patent
  Application No.: 63/313.504).'
arxivId: '2203.07975'
arxivUrl: https://arxiv.org/abs/2203.07975
authors:
- Artan Sheshmani
- Yizhuang You
- Wenbo Fu
- Ahmadreza Azizi
concepts: []
figures:
- /iaifi-research-blog/figures/2203_07975/figure_1.png
- /iaifi-research-blog/figures/2203_07975/figure_2.png
pdfUrl: https://arxiv.org/pdf/2203.07975v1
published: '2022-03-15T15:04:51+00:00'
theme: Foundational AI
title: Categorical Representation Learning and RG flow operators for algorithmic classifiers
wordCount: 1065
---

## The Big Picture

Imagine trying to understand a city from a satellite photo. Zoom out too fast, and you lose the street-level detail that explains why neighborhoods function the way they do; zoom in too close, and the sheer number of buildings overwhelms any sense of pattern. What you really want is a systematic way to move between scales, preserving what matters at each level while compressing what doesn't. Physicists have been doing exactly this for decades with a technique called the **renormalization group**, and now a team at IAIFI and UCSD has turned that same machinery into a new kind of AI architecture.

The **renormalization group (RG)** is one of theoretical physics' most powerful ideas. It explains how the laws of physics change depending on the scale at which you observe a system, and it shows up everywhere: phase transitions (water turning to steam), the behavior of quarks inside protons, critical phenomena in condensed matter. But until recently, that mathematical machinery sat largely untouched by the machine learning community. The new paper by Artan Sheshmani, Yizhuang You, Wenbo Fu, and Ahmadreza Azizi changes that, constructing an architecture called the **RG-flow categorifier** that encodes how information flows across scales as its core operating principle.

The payoff isn't just theoretical. The team applied their architecture to one of the hardest problems in modern biology: predicting how influenza viruses evolve to evade the human immune system.

> **Key Insight:** By embedding the mathematical structure of renormalization group flows directly into a neural network, the researchers built a classifier that can not only recognize genomic patterns, but generate new, biologically plausible viral sequences that might escape immune detection.

## How It Works

The starting point is an analogy between physics and data. In statistical mechanics, a many-body system (billions of interacting spins in a magnet, say) is too complex to analyze directly. RG solves this through **coarse-graining**: iteratively grouping small-scale variables into effective large-scale ones, building a hierarchy of descriptions that zooms out step by step. A genomic sequence has the same structure: many tokens at the microscopic level, coherent meaning only emerging at higher scales.

![Figure 1](/iaifi-research-blog/figures/2203_07975/figure_1.png)

Here's the catch: in physics, humans define the coarse-graining rules. For real-world data like protein sequences, those rules aren't obvious. The team's solution borrows from **holographic duality**, the idea from string theory that a physical system in flat space can be equivalently described by a theory on a higher-dimensional curved surface.

In the RG context, the optimal coarse-graining transformation maps flat data space into a **hyperbolic geometry**, a curved, saddle-shaped space that naturally organizes information by hierarchy. Features at different length scales become disentangled in this curved space, and short-range correlations in the interior represent long-range correlations in the original data.

To make this invertible and trainable, the researchers combine three ingredients:

- **Neural ODEs**: Network depth becomes a continuous parameter governed by a differential equation. The network flows smoothly through scales rather than jumping in discrete steps, with RG "flow time" as the governing variable.
- **Flow-based generative models**: Bijective (reversible, one-to-one) transformations that let the network both classify data and generate new samples by running the same process forwards or backwards.
- **Hyperbolic space embedding**: Hierarchical structure is encoded in the geometry itself, with features organized by relevance at each scale.

![Figure 2](/iaifi-research-blog/figures/2203_07975/figure_2.png)

The algorithm separates **relevant fields** (features that dominate at large scales) from **irrelevant fields** (microscopic fluctuations that wash out under coarse-graining). An objective function maximizes the disentanglement between the two, mirroring the physical intuition of RG flows converging toward **fixed points**, stable configurations where scale-invariance holds.


The experiments focused on flu virus genomics. Trained on hemagglutinin protein sequences (the surface proteins that determine strain identity and immune response), the model first learned the statistical distribution of amino acid residues at each position along the sequence. It then moved to full sequence distribution learning, capturing correlations across the entire chain. The most impressive result came from the **viral escape mutation** task: given sequences known to evade immune detection, the trained model generated new, statistically plausible sequences with similar escape properties, none of which appeared in the training data.


## Why It Matters

The connection between RG theory and deep learning has floated around the theoretical ML community for years. Researchers have noted that convolutional networks seem to implement something like coarse-graining, and that network depth parallels a physical system's flow toward large-scale behavior. But these analogies had remained informal.


This paper makes them precise, embedding the RG transformation directly into the architecture with rigorous grounding in differential geometry (specifically Ricci flow theory, the same mathematical framework behind Perelman's proof of the Poincaré conjecture) and holographic duality.

The biomedical angle is worth spelling out. Predicting viral evolution, not just classifying known strains but generating hypothetical future variants, is exactly the kind of problem where current ML tools struggle. Because the generative model is grounded in the physics of information flow across scales, the RG categorifier has a structural advantage: it doesn't memorize training sequences. It learns the hierarchical structure that generates them. The same framework could extend to protein folding, drug design, or any sequential data where multi-scale structure matters.


> **Bottom Line:** The RG-flow categorifier translates one of quantum field theory's most powerful conceptual tools into a working AI architecture and demonstrates it by generating new flu virus sequences that could evade immune detection, opening a new direction in both AI research and pandemic preparedness.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects renormalization group theory, a pillar of quantum field theory and statistical physics, with neural network architecture design, translating holographic duality and hyperbolic geometry into a concrete, trainable machine learning system.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The RG-flow categorifier introduces an architecture capable of both classification and generation at all network layers, built on a physically motivated, invertible coarse-graining framework using neural ODEs and flow-based generative models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper shows how RG flow operators can be constructed on moduli spaces of smooth maps, bringing together Ricci flow geometry, nonlinear sigma models, and holographic duality in a single algorithmic framework.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include scaling the architecture to larger genomic datasets and extending the holographic mapping to two-dimensional data such as images. The full paper is available at [arXiv:2203.07975](https://arxiv.org/abs/2203.07975), with related foundational work at [arXiv:2103.14770](https://arxiv.org/abs/2103.14770).</span></div></div>
</div>
