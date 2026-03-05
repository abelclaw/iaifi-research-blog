---
abstract: 'The simplification and reorganization of complex expressions lies at the
  core of scientific progress, particularly in theoretical high-energy physics. This
  work explores the application of machine learning to a particular facet of this
  challenge: the task of simplifying scattering amplitudes expressed in terms of spinor-helicity
  variables. We demonstrate that an encoder-decoder transformer architecture achieves
  impressive simplification capabilities for expressions composed of handfuls of terms.
  Lengthier expressions are implemented in an additional embedding network, trained
  using contrastive learning, which isolates subexpressions that are more likely to
  simplify. The resulting framework is capable of reducing expressions with hundreds
  of terms - a regular occurrence in quantum field theory calculations - to vastly
  simpler equivalent expressions. Starting from lengthy input expressions, our networks
  can generate the Parke-Taylor formula for five-point gluon scattering, as well as
  new compact expressions for five-point amplitudes involving scalars and gravitons.
  An interactive demonstration can be found at https://spinorhelicity.streamlit.app
  .'
arxivId: '2408.04720'
arxivUrl: https://arxiv.org/abs/2408.04720
authors:
- Clifford Cheung
- Aurélien Dersy
- Matthew D. Schwartz
concepts:
- scattering amplitudes
- spinor-helicity formalism
- transformers
- symbolic expression simplification
- contrastive learning
- embeddings
- representation learning
- quantum field theory
- attention mechanisms
- self-supervised learning
- interpretability
figures:
- /iaifi-research-blog/figures/2408_04720/figure_1.png
- /iaifi-research-blog/figures/2408_04720/figure_2.png
- /iaifi-research-blog/figures/2408_04720/figure_3.png
pdfUrl: https://arxiv.org/pdf/2408.04720v2
published: '2024-08-08T18:36:43+00:00'
theme: Theoretical Physics
title: Learning the Simplicity of Scattering Amplitudes
wordCount: 1064
---

## The Big Picture

Imagine writing a proof that fills fifty pages, only to discover it fits on a napkin. That's essentially what happens in theoretical particle physics — routinely.

When physicists calculate how particles scatter off each other, they use **Feynman diagrams** — a set of diagram-based rules that generate the underlying math. The diagrams are powerful, but the intermediate algebra can sprawl into hundreds or thousands of terms. Yet the final answer is often shockingly compact.

One famous example: the collision of five **gluons** — the particles that carry the strong force binding quarks inside protons — produces, via Feynman diagrams, a calculation hundreds of lines long. The actual answer, discovered by Parke and Taylor in 1986, is a single elegant fraction. The mess was never real. It was an artifact of how we were looking at the problem.

Finding these hidden simplifications matters beyond aesthetics. When physicists have spotted them in the past, they've unlocked entirely new frameworks — from string theory connections to the "amplituhedron," a geometric object encoding particle interactions without any reference to space or time.

The obstacle: getting from a complicated expression to its simplest form requires searching through astronomically many possible rearrangements. No known algorithm reliably finds the shortest form. You either get lucky, or you spend years staring at equations.

A team from Caltech, Harvard, and IAIFI — Clifford Cheung, Aurélien Dersy, and Matthew D. Schwartz — decided to teach a machine to do the staring. Their result: a machine learning framework that takes particle physics expressions containing hundreds of terms and compresses them into their simplest known forms, including autonomously rediscovering the Parke-Taylor formula.

> **Key Insight:** A transformer network trained to recognize mathematical simplicity can compress particle physics expressions spanning hundreds of terms down to single compact formulas — revealing hidden structure that took human physicists decades to find.

## How It Works

The mathematical language of this work is the **spinor-helicity formalism** — a compact notation where each particle's state is encoded as a pair of complex numbers called spinors. The building blocks are angle brackets ⟨ij⟩ and square brackets [ij], representing relationships between pairs of particles. **Amplitudes** — the quantities that determine how likely different collision outcomes are — are elegant in this notation once simplified, but bewilderingly messy before.

The same physical quantity can be expressed in countless equivalent ways through identities like the **Schouten identity**, a rule that lets you rewrite any expression involving three spinors in endless equivalent forms. This creates an astronomically large algebraic search space with no obvious path to simplicity.

The researchers built their system in two layers, each tackling a different scale of complexity.

![Figure 1](/iaifi-research-blog/figures/2408_04720/figure_1.png)

The first is a standard **encoder-decoder transformer** — the same architectural family underlying modern language models — trained on pairs of messy input expressions and their known simplified outputs. For expressions up to around a dozen terms, this "one-shot" network reads the full expression and outputs the simplified version directly, token by token. On moderate-length expressions, it achieves impressive simplification rates.

The harder problem is expressions with hundreds of terms. Feeding the entire thing to a transformer is computationally intractable — processing cost grows prohibitively with length. The researchers' solution was to mimic how a human expert would approach the problem:

1. **Scan** the expression and identify which terms are likely to combine
2. **Group** those terms into a smaller subset
3. **Simplify** the subset using the trained transformer
4. **Repeat** until nothing remains to simplify

The key to step one is an **embedding network** trained with **contrastive learning** — a technique from computer vision where similar items are pulled together in a shared mathematical space and dissimilar items pushed apart. Here, "similar" means "likely to cancel or combine under spinor-helicity identities." The network learns to place terms close together if they tend to simplify when grouped, and far apart if they don't. Clustering in this space guides which terms to feed into the simplification transformer at each step.

![Figure 2](/iaifi-research-blog/figures/2408_04720/figure_2.png)

This sequential pipeline — embed, cluster, simplify, repeat — enables the system to tackle full-scale expressions from real quantum field theory calculations.

## Why It Matters

Starting from Feynman-diagram outputs containing hundreds of terms, the system independently derives the Parke-Taylor formula for five-point gluon scattering. It also produces new compact expressions for five-point amplitudes involving scalars and gravitons — cases where no simple closed-form was previously known. These aren't numerical approximations; the outputs are exact symbolic expressions, verifiable by direct calculation.

![Figure 3](/iaifi-research-blog/figures/2408_04720/figure_3.png)

The deeper significance lies in what compact forms unlock. Every time physicists have found a simple amplitude, they've eventually understood *why* it's simple — and that understanding has revealed new theoretical structure. The amplituhedron, celestial holography, the double-copy relationship between gravity and gauge theory: all emerged from staring at compact expressions and asking what geometric or algebraic principle they encoded. If machine learning can now systematically produce those compact forms, it becomes a tool not just for calculation but for discovery.

The contrastive learning approach also generalizes: the same strategy for learning which subexpressions simplify together could apply to loop-level amplitudes, string theory calculations, and other domains where symbolic simplification matters.

> **Bottom Line:** By combining transformer-based symbolic translation with contrastive-learning-guided search, this framework compresses particle physics calculations by orders of magnitude — and in doing so, may help physicists discover the hidden structures that make the universe computable.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly applies modern deep learning architectures — transformers and contrastive learning — to a central technical challenge in theoretical high-energy physics, demonstrating that ML can serve as a genuine tool for symbolic mathematical discovery, not just numerical approximation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The contrastive learning strategy for guiding symbolic simplification — learning which subexpressions are likely to simplify together — offers a broadly applicable template for using learned representations to navigate combinatorially complex algebraic search spaces.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The system autonomously rediscovers the Parke-Taylor formula for five-point gluon amplitudes and produces new compact expressions for scalar and graviton amplitudes, opening a path toward systematically uncovering hidden simplicity in quantum field theory at higher multiplicity and loop order.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending the approach to loop-level amplitudes and more complex theories; an interactive demonstration is available at [spinorhelicity.streamlit.app](https://spinorhelicity.streamlit.app). The paper is available on arXiv as CALT-TH 2024-031.</span></div></div>
</div>
