---
abstract: Recent work has proposed that language models perform computation by manipulating
  one-dimensional representations of concepts ("features") in activation space. In
  contrast, we explore whether some language model representations may be inherently
  multi-dimensional. We begin by developing a rigorous definition of irreducible multi-dimensional
  features based on whether they can be decomposed into either independent or non-co-occurring
  lower-dimensional features. Motivated by these definitions, we design a scalable
  method that uses sparse autoencoders to automatically find multi-dimensional features
  in GPT-2 and Mistral 7B. These auto-discovered features include strikingly interpretable
  examples, e.g. circular features representing days of the week and months of the
  year. We identify tasks where these exact circles are used to solve computational
  problems involving modular arithmetic in days of the week and months of the year.
  Next, we provide evidence that these circular features are indeed the fundamental
  unit of computation in these tasks with intervention experiments on Mistral 7B and
  Llama 3 8B, and we examine the continuity of the days of the week feature in Mistral
  7B. Overall, our work argues that understanding multi-dimensional features is necessary
  to mechanistically decompose some model behaviors.
arxivId: '2405.14860'
arxivUrl: https://arxiv.org/abs/2405.14860
authors:
- Joshua Engels
- Eric J. Michaud
- Isaac Liao
- Wes Gurnee
- Max Tegmark
concepts:
- multi-dimensional features
- representation learning
- circular representations
- autoencoders
- interpretability
- sparse models
- transformers
- modular arithmetic circuits
- dimensionality reduction
- disentangled representations
- clustering
- embeddings
figures:
- /iaifi-research-blog/figures/2405_14860/figure_2.png
- /iaifi-research-blog/figures/2405_14860/figure_2.png
- /iaifi-research-blog/figures/2405_14860/figure_3.png
pdfUrl: https://arxiv.org/pdf/2405.14860v3
published: '2024-05-23T17:59:04+00:00'
theme: Foundational AI
title: Not All Language Model Features Are One-Dimensionally Linear
wordCount: 1244
---

## The Big Picture

Imagine trying to understand a foreign language by assuming every word is a single note, a simple "yes" or "no" signal. That's essentially what researchers have been doing with AI language models. For years, a leading theory held that these systems think by activating clean, isolated signals: one signal dedicated to "royalty," another to "France," another to "past tense." Elegant. Tidy. And possibly incomplete.

A team of researchers from MIT and the Institute for AI and Fundamental Interactions (IAIFI) just showed that some of what's happening inside large language models is fundamentally more complex. When a language model thinks about Monday, Tuesday, Wednesday, it doesn't just toggle a single switch. It traces a *circle*.

The paper, published at ICLR 2025, challenges the dominant **linear representation hypothesis**, the idea that every concept a language model handles corresponds to a single, isolated signal. The researchers found that certain concepts require inherently multi-dimensional structure (think a shape, not a point) and they built tools to find these structures automatically.

> **Key Insight:** Language models like GPT-2 and Mistral 7B internally represent cyclical concepts, such as days of the week and months of the year, as *circles* in their activation space. These circles are the actual computational machinery the models use to reason about time.

## How It Works

The central question sounds simple: when can a representation *not* be broken down into simpler pieces? The team formalized this with a rigorous definition of **irreducible multi-dimensional features**, representations that genuinely require multiple dimensions and can't be split into either independent simpler parts or parts that never co-occur.

To find these features automatically, the researchers used **sparse autoencoders (SAEs)**, a technique that decomposes a model's internal signals into a large dictionary of basic building blocks, like decomposing a musical chord into individual notes. SAEs have become a core tool of **mechanistic interpretability** research, the field trying to reverse-engineer how neural networks actually work. Rather than treating each dictionary element as standalone, the team looked for *clusters* of elements that light up together in structured patterns.

The pipeline:

1. Train sparse autoencoders on the internal signals (activations) of GPT-2-small and Mistral 7B.
2. Compute how often each pair of SAE features lights up together across a large text corpus.
3. Cluster the co-activation graph to find tight groups of features.
4. Apply a statistical test, comparing actual cluster variance against what independent features would produce, to flag irreducible multi-dimensional candidates.

The results were hard to ignore.

![Figure 1](/iaifi-research-blog/figures/2405_14860/figure_2.png)

Visualizing the discovered clusters using PCA (a standard technique for collapsing complex data to its most important dimensions), the days of the week formed a perfect circle in a two-dimensional subspace of layer 7 in GPT-2-small. Monday through Sunday, spiraling in order. Months of the year made the same shape. Even years of the 20th century traced a circular arc. These weren't visualization artifacts. The geometry was genuinely present in the model's internals.

Finding a pretty picture is one thing, though. The harder question is whether these circles *matter* for computation. The researchers designed careful **activation patching** experiments, surgically replacing the circular representation mid-computation, to test causal necessity.

Ask a language model "If today is Thursday, what day is it in four days?" and it must compute (4 + 4) mod 7 = 1, which is Monday. Modular arithmetic, the kind that wraps around, is geometrically natural on a circle. When the team patched in the circular representation for a different starting day in Mistral 7B and Llama 3 8B, the model's answer changed in exactly the way the circle's geometry predicts. The circle isn't decorative; it's the actual variable the model passes through its circuits to solve the problem.

![Figure 3](/iaifi-research-blog/figures/2405_14860/figure_3.png)

Erasing the full circular feature degraded performance far more than erasing any single one-dimensional component of it. The whole is genuinely more than the sum of its parts. When text referred to "early Monday" versus "late Monday," the model's representation shifted continuously around the circle, treating time as a smooth, analog quantity rather than discrete buckets. The model has apparently learned something like a continuous clock.

## Why It Matters

If some model behaviors are controlled by multi-dimensional features, then tools built around single isolated signals will systematically miss them. Sparse autoencoders trained to find one-dimensional building blocks will, at best, carve a circle into disconnected fragments that look meaningless in isolation. The researchers are pointing at a genuine blind spot in the field's current toolkit.

This connects to a core challenge in AI safety and alignment: can we fully understand what a model is doing? If the true computational units include geometric objects like circles, **tori** (donut shapes), or stranger curved surfaces, then interpretability requires a richer mathematical vocabulary than a list of labeled signals. What other shapes might be lurking? Helices, grids, fractals? Whether complex reasoning tasks require fundamentally multi-dimensional internal representations that current tools don't capture remains an open question.

> **Bottom Line:** Language models encode cyclical concepts like days and months as literal geometric circles in their activation space, and these circles are the actual variables driving modular arithmetic computations, not a byproduct of training. Understanding AI's internal geometry may require going well beyond the linear feature paradigm.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work imports ideas from physics and geometry, specifically the topology of circles and continuous symmetry, into mechanistic interpretability. AI models spontaneously learn representations that physicists would recognize as compact manifolds.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper challenges the dominant linear representation hypothesis and introduces scalable tools for discovering irreducible multi-dimensional features in large language models, revealing a class of internal structure that prior interpretability methods systematically miss.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The discovery that neural networks represent periodic quantities using circular geometry mirrors how physicists encode cyclic symmetries in physical theories, pointing to structural parallels between learned AI representations and the mathematical objects that describe nature.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will need to map the full zoo of possible feature geometries, beyond circles to tori, helices, and beyond, to build complete mechanistic accounts of complex model behaviors; the paper is available at [arXiv:2405.14860](https://arxiv.org/abs/2405.14860).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Not All Language Model Features Are One-Dimensionally Linear</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2405.14860</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Joshua Engels", "Eric J. Michaud", "Isaac Liao", "Wes Gurnee", "Max Tegmark"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Recent work has proposed that language models perform computation by manipulating one-dimensional representations of concepts ("features") in activation space. In contrast, we explore whether some language model representations may be inherently multi-dimensional. We begin by developing a rigorous definition of irreducible multi-dimensional features based on whether they can be decomposed into either independent or non-co-occurring lower-dimensional features. Motivated by these definitions, we design a scalable method that uses sparse autoencoders to automatically find multi-dimensional features in GPT-2 and Mistral 7B. These auto-discovered features include strikingly interpretable examples, e.g. circular features representing days of the week and months of the year. We identify tasks where these exact circles are used to solve computational problems involving modular arithmetic in days of the week and months of the year. Next, we provide evidence that these circular features are indeed the fundamental unit of computation in these tasks with intervention experiments on Mistral 7B and Llama 3 8B, and we examine the continuity of the days of the week feature in Mistral 7B. Overall, our work argues that understanding multi-dimensional features is necessary to mechanistically decompose some model behaviors.</span></div></div>
</div>
