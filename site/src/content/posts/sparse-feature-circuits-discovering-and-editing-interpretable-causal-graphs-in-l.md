---
abstract: 'We introduce methods for discovering and applying sparse feature circuits.
  These are causally implicated subnetworks of human-interpretable features for explaining
  language model behaviors. Circuits identified in prior work consist of polysemantic
  and difficult-to-interpret units like attention heads or neurons, rendering them
  unsuitable for many downstream applications. In contrast, sparse feature circuits
  enable detailed understanding of unanticipated mechanisms. Because they are based
  on fine-grained units, sparse feature circuits are useful for downstream tasks:
  We introduce SHIFT, where we improve the generalization of a classifier by ablating
  features that a human judges to be task-irrelevant. Finally, we demonstrate an entirely
  unsupervised and scalable interpretability pipeline by discovering thousands of
  sparse feature circuits for automatically discovered model behaviors.'
arxivId: '2403.19647'
arxivUrl: https://arxiv.org/abs/2403.19647
authors:
- Samuel Marks
- Can Rager
- Eric J. Michaud
- Yonatan Belinkov
- David Bau
- Aaron Mueller
concepts:
- interpretability
- causal circuit discovery
- autoencoders
- sparse models
- feature attribution
- disentangled representations
- transformers
- feature extraction
- scalability
- attention mechanisms
- clustering
- anomaly detection
figures:
- /iaifi-research-blog/figures/2403_19647/figure_1.png
- /iaifi-research-blog/figures/2403_19647/figure_1.png
- /iaifi-research-blog/figures/2403_19647/figure_2.png
- /iaifi-research-blog/figures/2403_19647/figure_2.png
- /iaifi-research-blog/figures/2403_19647/figure_3.png
- /iaifi-research-blog/figures/2403_19647/figure_3.png
pdfUrl: https://arxiv.org/pdf/2403.19647v3
published: '2024-03-28T17:56:07+00:00'
theme: Foundational AI
title: 'Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs
  in Language Models'
wordCount: 1051
---

## The Big Picture

Imagine trying to understand why a car engine makes a strange noise by looking only at the whole engine block, never at individual pistons, valves, or fuel injectors. That's what AI interpretability researchers have been doing for years: explaining why a language model behaves a certain way by pointing to broad internal components with names like "attention head 7" or "layer 4." These components are like engine blocks. Too big, too tangled, and frustratingly vague.

The deeper problem is **polysemanticity**: individual processing units inside AI language models respond to dozens of unrelated concepts at the same time. A single unit might activate for "banana," "yellow objects," and "tropical countries" all at once. Trying to explain a model's behavior using these blurry units is like describing a symphony by pointing at sections of the orchestra. Technically accurate, but missing everything that matters.

A team from Northeastern University, MIT, and the Technion built a sharper tool. Their **sparse feature circuits**, published at ICLR 2025, reveal the fine-grained, human-interpretable causal pathways actually responsible for specific model behaviors. They also built a pipeline that discovers thousands of these circuits automatically.

> **Key Insight:** By replacing blurry processing units with sharp, meaningful "features" learned by a specially trained neural network, researchers can now trace exactly which concepts cause a language model to make a specific prediction, and surgically edit those pathways.

## How It Works

The method rests on two technical pillars.

The first is **sparse autoencoders (SAEs)**, neural networks trained to decompose a model's internal representations into interpretable building blocks. When a language model processes text, each layer produces a stream of numbers encoding what the model "knows" at that point. SAEs re-express those numbers as a combination of features, each corresponding to a single recognizable concept: "the word 'doctor' in a medical context" or "a plural subject in a relative clause." The researchers trained SAEs for every sublayer of Pythia-70M and used the publicly available Gemma Scope SAEs for Gemma-2-2B.

![Figure 1](/iaifi-research-blog/figures/2403_19647/figure_1.png)

The second pillar is **attribution patching**, a fast mathematical technique for estimating how much each feature causally contributes to a specific model output. Given a "clean" input ("The teacher...") and a "patch" input ("The teachers..."), attribution patching estimates how much each feature's difference shifts the model's probability of outputting "is" versus "are." Because the technique scores thousands of features in parallel, it scales.

Combining both pillars, the pipeline works like this:

1. **Define a behavior**, for example, subject-verb agreement on sentences with an intervening noun phrase.
2. **Run SAEs** on every sublayer to decompose activations into sparse features.
3. **Score features** using attribution patching to find which ones causally influence that behavior.
4. **Threshold and connect**: keep only the most important features and trace how they communicate across layers, forming a directed graph.

The result is a sparse feature circuit: a graph where nodes are interpretable features and edges represent causal influence.

![Figure 2](/iaifi-research-blog/figures/2403_19647/figure_1.png)

One honest touch: the **SAE error term** (the gap between what the SAE captured and what the model actually computed) gets its own node in the circuit. Researchers can see exactly how much of the model's behavior is explained by interpretable features versus unexplained residuals.

## Why It Matters

The most direct application is **SHIFT** (Sparse Human-Interpretable Feature Trimming), a technique for removing bias from AI classifiers by eliminating irrelevant features. The team tested it on a worst-case scenario: a model trained to predict profession where gender perfectly predicts the correct answer in training data.

Standard bias-removal methods require carefully curated examples where gender and profession are independent. SHIFT doesn't. A human examines the discovered circuit, identifies features clearly related to gender rather than profession, and removes them. The model's spurious gender sensitivity drops without any special data.

![Figure 4](/iaifi-research-blog/figures/2403_19647/figure_2.png)

Beyond debiasing, the team built a fully unsupervised pipeline that discovers thousands of narrow language model behaviors ("predicting 'to' as an infinitive object," "predicting commas in dates") using clustering, then automatically computes sparse feature circuits for all of them. Results are publicly browsable at feature-circuits.xyz. That scalability matters most here: interpretability no longer has to be a hand-crafted, one-behavior-at-a-time endeavor.

Open questions remain. Better SAEs will shrink the unexplained residual. Attribution patching is an approximation, so complex interactions between multiple features could be missed. And the method has so far been validated on smaller models; scaling to frontier systems is still ahead.

> **Bottom Line:** Sparse feature circuits give researchers a genuinely interpretable, causally grounded window into language model behavior, and a practical tool for editing that behavior without needing carefully curated datasets.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects mechanistic interpretability with the precision analysis familiar to physicists, tracing causal pathways through complex systems with minimal assumptions, much like tracking particle interactions through a detector.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Sparse feature circuits replace polysemantic, hard-to-interpret units with fine-grained, human-readable features. The unsupervised pipeline can discover thousands of interpretable causal explanations for language model behaviors without manual effort.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The SHIFT technique shows that interpretability tools can support targeted, principled edits to model behavior, a step toward AI systems whose internal workings can be read, understood, and responsibly modified.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will focus on improving SAE quality and scaling circuit discovery to larger frontier models. The paper is available at [arXiv:2403.19647](https://arxiv.org/abs/2403.19647), and code is released at github.com/saprmarks/feature-circuits.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2403.19647</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Samuel Marks", "Can Rager", "Eric J. Michaud", "Yonatan Belinkov", "David Bau", "Aaron Mueller"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We introduce methods for discovering and applying sparse feature circuits. These are causally implicated subnetworks of human-interpretable features for explaining language model behaviors. Circuits identified in prior work consist of polysemantic and difficult-to-interpret units like attention heads or neurons, rendering them unsuitable for many downstream applications. In contrast, sparse feature circuits enable detailed understanding of unanticipated mechanisms. Because they are based on fine-grained units, sparse feature circuits are useful for downstream tasks: We introduce SHIFT, where we improve the generalization of a classifier by ablating features that a human judges to be task-irrelevant. Finally, we demonstrate an entirely unsupervised and scalable interpretability pipeline by discovering thousands of sparse feature circuits for automatically discovered model behaviors.</span></div></div>
</div>
