---
abstract: In this paper, we study the vanishing order of rational $L$-functions from
  a data scientific perspective. Each $L$-function is represented in our data by finitely
  many Dirichlet coefficients, the normalisation of which depends on the context.
  We observe murmuration-like patterns in averages across our dataset, find that PCA
  clusters rational $L$-functions by their vanishing order, and record that LDA and
  neural networks may accurately predict this quantity.
arxivId: '2502.10360'
arxivUrl: https://arxiv.org/abs/2502.10360
authors:
- Joanna Bieri
- Giorgi Butbaia
- Edgar Costa
- Alyson Deines
- Kyu-Hwan Lee
- David Lowry-Duda
- Thomas Oliver
- Yidi Qi
- Tamara Veenstra
concepts:
- l-function vanishing order
- classification
- arithmetic l-functions
- dimensionality reduction
- clustering
- murmuration patterns
- convolutional networks
- feature extraction
- transfer learning
- spectral methods
- interpretability
figures:
- /iaifi-research-blog/figures/2502_10360/figure_1.png
- /iaifi-research-blog/figures/2502_10360/figure_1.png
- /iaifi-research-blog/figures/2502_10360/figure_2.png
- /iaifi-research-blog/figures/2502_10360/figure_2.png
- /iaifi-research-blog/figures/2502_10360/figure_3.png
- /iaifi-research-blog/figures/2502_10360/figure_3.png
pdfUrl: https://arxiv.org/pdf/2502.10360v1
published: '2025-02-14T18:42:06+00:00'
theme: Theoretical Physics
title: Machine learning the vanishing order of rational L-functions
wordCount: 1029
---

## The Big Picture

Imagine trying to predict the size of a hidden treasure chest by studying only the ripples it makes on the surface of a vast mathematical ocean. That's roughly the challenge of determining the **rank** of an **elliptic curve**, one of the deepest unsolved problems in number theory.

An elliptic curve isn't the oval you might picture. It's a family of equations of the form y² = x³ + ax + b whose solutions form a curve with rich algebraic structure. The rank counts how many fundamentally independent solutions exist using only fractions (what mathematicians call **rational points**). Computing it directly is notoriously difficult.

So mathematicians study a proxy: an **L-function**, an infinite formula built from the curve's coefficients that encodes its arithmetic secrets. Think of it as a fingerprint, a structured sequence of numbers carrying hidden information about the original curve.

The link between rank and L-functions is captured by the **Birch and Swinnerton-Dyer (BSD) conjecture**, one of the Millennium Prize Problems. BSD predicts that the rank equals the **vanishing order** of the L-function at a special input called the central point: how many times the function "touches zero" there. Vanishing order zero means finitely many rational points; higher orders mean more. But computing this vanishing order requires delicate analytic techniques.

What if a machine could learn to read it directly from the raw coefficients?

A team of nine researchers set out to test exactly that, and their results suggest machine learning can crack this code across a collection of 248,359 rational L-functions.

> **Key Insight:** Neural networks and classical ML methods can accurately predict the vanishing order of rational L-functions from their Dirichlet coefficients alone, a result with direct implications for BSD.

## How It Works

The researchers built a dataset called `RAT`, drawing from the **L-functions and Modular Forms Database (LMFDB)**. It spans five families of mathematical objects:

- **ECQ** — elliptic curves over Q
- **ECNF** — elliptic curves over number fields
- **CMF** — classical modular forms
- **DIR** — Dirichlet characters
- **G2Q** — genus 2 curves

In total: 248,359 L-functions with root analytic conductor below 4, a complexity measure that keeps the dataset balanced across origins.

Each L-function arrives as a sequence of **Dirichlet coefficients** $\{a_n\}$, numbers associated with each prime that capture how the underlying mathematical object behaves locally. The team fed these sequences directly into their models as feature vectors, working in the arithmetic normalization where coefficients are whole-number-like algebraic quantities and the functional equation takes a clean symmetric form.

![Figure 1](/iaifi-research-blog/figures/2502_10360/figure_1.png)

Before training any neural network, the team probed for structure with simpler tools.

**Principal Component Analysis (PCA)** compresses high-dimensional data down to its most informative directions. Projecting coefficient vectors onto their top two components revealed something unexpected: L-functions naturally clustered by vanishing order, with no labels required. The geometry of coefficient space itself separates rank-0 from rank-1 from rank-2 curves.

**Linear Discriminant Analysis (LDA)**, a supervised method that maximizes separation between labeled classes, achieved strong classification accuracy. This confirmed the PCA clusters carry genuine predictive signal. Feed-forward and convolutional neural networks pushed accuracy further still, learning nonlinear features from coefficient sequences that LDA missed.

![Figure 2](/iaifi-research-blog/figures/2502_10360/figure_1.png)

Then there are the **murmurations**. First observed in 2022 in elliptic curves over Q, the phenomenon is named after the coordinated flight of starling flocks. When you average the Dirichlet coefficients of many L-functions at the same prime, organized by root analytic conductor, the averages don't wash out to zero. They exhibit coherent oscillating patterns that differ systematically between vanishing orders.

The team found murmuration-like signatures across all five sub-datasets, suggesting the phenomenon is far more universal than originally suspected.

![Figure 3](/iaifi-research-blog/figures/2502_10360/figure_2.png)

The researchers also tested **transfer learning**: training a model on one sub-dataset and applying it to another. This probes whether the learned representations capture something universal about L-functions or something specific to one mathematical family. Transfer learning worked to a meaningful degree, hinting that the networks pick up on genuine analytic structure shared across all rational L-functions.

![Figure 4](/iaifi-research-blog/figures/2502_10360/figure_2.png)

## Why It Matters

The BSD conjecture and its generalizations, the **Beilinson-Bloch-Kato conjectures**, sit at the heart of modern number theory, connecting the analytic properties of L-functions to deep algebraic invariants. Proving BSD remains one of the hardest open problems in mathematics.

The information needed to determine vanishing order (essentially, the rank) is already present, in machine-readable form, in the first few hundred Dirichlet coefficients. That's not a proof of BSD, but it is strong empirical evidence that the conjecture is correct and that the structure it predicts is detectable.

The murmuration phenomenon itself was first spotted by researchers who noticed a pattern in averages before anyone had a theoretical explanation. By scaling up to a quarter million L-functions spanning multiple degrees and origins, this team has shown that machine learning generalizes across mathematical families in ways that may guide future theoretical work. The patterns these networks learn could suggest new conjectures about which arithmetic invariants control vanishing order.

![Figure 5](/iaifi-research-blog/figures/2502_10360/figure_3.png)

> **Bottom Line:** Machine learning doesn't just classify L-functions. It reveals that the rank of an arithmetic object is already encoded as detectable geometric structure in the first few hundred terms of its associated L-function. This is empirical evidence for one of number theory's deepest conjectures, delivered by a neural network.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects AI methodology (PCA, LDA, convolutional neural networks, transfer learning) with one of the deepest open problems in number theory, detecting algebraic invariants from analytic data across 248,359 L-functions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper advances transfer learning and representation learning in pure mathematics, showing that neural networks trained on one family of mathematical objects generalize meaningfully to structurally different families.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By showing that vanishing order is encoded in Dirichlet coefficients across diverse L-function families, the work provides a new empirical lens on the Birch–Swinnerton-Dyer conjecture and its generalizations to higher-dimensional arithmetic varieties.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending the dataset to larger conductors and applying interpretability methods to extract new conjectures; the paper is available at [arXiv:2502.10360](https://arxiv.org/abs/2502.10360) (supported in part by NSF grant PHY-2019786 to the IAIFI).</span></div></div>
</div>
