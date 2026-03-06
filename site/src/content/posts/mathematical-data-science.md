---
abstract: 'Can machine learning help discover new mathematical structures? In this
  article we discuss an approach to doing this which one can call "mathematical data
  science". In this paradigm, one studies mathematical objects collectively rather
  than individually, by creating datasets and doing machine learning experiments and
  interpretations. After an overview, we present two case studies: murmurations in
  number theory and loadings of partitions related to Kronecker coefficients in representation
  theory and combinatorics.'
arxivId: '2502.08620'
arxivUrl: https://arxiv.org/abs/2502.08620
authors:
- Michael R. Douglas
- Kyu-Hwan Lee
concepts:
- mathematical data science
- automated discovery
- interpretability
- murmurations
- scientific workflows
- feature extraction
- kronecker coefficients
- regression
- classification
- hypothesis testing
- self-supervised learning
figures:
- /iaifi-research-blog/figures/2502_08620/figure_1.png
- /iaifi-research-blog/figures/2502_08620/figure_1.png
- /iaifi-research-blog/figures/2502_08620/figure_2.png
- /iaifi-research-blog/figures/2502_08620/figure_2.png
- /iaifi-research-blog/figures/2502_08620/figure_3.png
- /iaifi-research-blog/figures/2502_08620/figure_3.png
pdfUrl: https://arxiv.org/pdf/2502.08620v1
published: '2025-02-12T18:15:35+00:00'
theme: Theoretical Physics
title: Mathematical Data Science
wordCount: 1080
---

## The Big Picture

Imagine handing a master chef thousands of recipes and asking them not to cook a single dish, but to discover a new cuisine. That's roughly what a growing group of mathematicians are doing with machine learning — not solving individual problems, but feeding entire families of mathematical objects into neural networks and watching for patterns no human has ever noticed. This is **mathematical data science**, and it's quietly transforming how mathematicians discover new truths.

For centuries, math has been a discipline of lone geniuses wrestling with specific objects: this particular curved equation, that knot, a specific polynomial. The occasional pattern would emerge when someone computed enough examples by hand. But computation has exploded. Databases of millions of mathematical objects now exist, and the tools to search for hidden structure in them — tools perfected by the tech industry to recommend movies and translate languages — are now available to anyone with a laptop and a curiosity about abstract structures.

Physicists Michael R. Douglas and mathematician Kyu-Hwan Lee have written a clarifying manifesto for this emerging paradigm, demonstrating through two striking case studies that the approach isn't just plausible — it already works.

> **Key Insight:** By treating mathematical objects as data and applying machine learning, researchers can detect statistical patterns invisible to traditional analysis, generating precise new conjectures that humans can then rigorously prove.

## How It Works

The **mathematical data science (MDS) paradigm** breaks into four steps that are simple to state but deceptively subtle to execute:

1. **Generate a dataset** of mathematical objects — not one object, but thousands or millions, computed systematically.
2. **Apply ML tools** to find structure in that dataset, treating invariants (measurable properties) as features.
3. **Interpret the results** to understand what the patterns actually mean mathematically.
4. **Formulate conjectures and theorems** from the evidence.

Every step still requires human mathematicians. Choices about what to measure, how to sample, which patterns are interesting — none of this is automated. The computer is a powerful telescope, not an autonomous explorer.

A key conceptual contribution is the **"platonic dataset."** Most ML datasets are fuzzy — web-scraped text, photographs with inconsistent labels. A platonic dataset is mathematically precise: a well-defined set of objects, a function mapping each to measurable invariants, and a principled rule for choosing finite subsets to analyze. This precision means any conjecture the ML suggests can be stated in exact mathematical language — a prerequisite for eventually proving it.

![Figure 1](/iaifi-research-blog/figures/2502_08620/figure_1.png)

The paper's first case study involves **murmurations** — a striking phenomenon recently discovered in the statistics of elliptic curve *L*-functions. An *L*-function is a formula encoding deep arithmetic information about a mathematical object; in this case, an **elliptic curve**, a smooth curve defined by a simple cubic equation with surprisingly rich mathematical properties. Researchers had studied these functions one at a time for decades.

When Lee and collaborators looked at large collections of elliptic curves, sorting them by their **rank** (a number measuring how many independent solutions a curve has) and plotting average values of the *L*-functions, they found an unexpected oscillatory correlation — a murmuration pattern, named for the collective undulation of starling flocks. This structure is completely invisible when you study one curve at a time. It only emerges statistically, from the crowd.

![Figure 2](/iaifi-research-blog/figures/2502_08620/figure_1.png)

The second case study tackles **Kronecker coefficients** — numbers that appear throughout the mathematics of symmetry and have applications in quantum information theory. These coefficients are notoriously hard to compute, and harder still to understand conceptually.

The authors define a dataset of **integer partitions** (ways to write a number as an ordered sum — 4 can be expressed as 3+1, or 2+2, or 2+1+1) and compute associated **loadings** — numerical summaries capturing how Kronecker coefficients are distributed across the dataset. Machine learning experiments reveal patterns in how these loadings cluster, pointing toward combinatorial structure that pure theory had not predicted.

![Figure 3](/iaifi-research-blog/figures/2502_08620/figure_2.png)

## Why It Matters

The historical precedent is striking. The famous **Birch and Swinnerton-Dyer conjecture** — one of the Millennium Prize Problems, carrying a $1 million reward for its proof — originated from exactly this kind of computer experiment in the 1960s. Bryan Birch and Peter Swinnerton-Dyer generated elliptic curves by computer and performed linear regression on the results. They were doing mathematical data science before the term existed.

The authors acknowledge the central difficulty that distinguishes math from other data sciences: **interpretability**. In biology or medicine, a neural network that predicts outcomes accurately is already useful even if you can't explain why. In mathematics, a black-box prediction is nearly worthless without understanding. A pattern only becomes mathematically meaningful when it can be turned into a precise statement and, ultimately, a proof.

This tension — between the fluency of modern ML and the rigorous demands of mathematics — is where the field must grow. Tools like **attribution analysis**, which identify which input features drove a model's prediction, are crucial bridges between pattern and proof.

![Figure 4](/iaifi-research-blog/figures/2502_08620/figure_2.png)

The timing is auspicious. Mathematical databases like the LMFDB (L-functions and Modular Forms Database) and KnotInfo have matured. Computing power makes datasets of millions of objects routine. The most important development may be cultural: mathematicians and ML researchers are increasingly working together, as in the landmark 2021 DeepMind collaboration with Fields Medal–level experts that produced new theorems in knot theory and representation theory. Douglas and Lee's paper reads as an invitation to more such collaborations.

> **Bottom Line:** Mathematical data science is transforming how new conjectures get discovered — murmurations in number theory and structure in Kronecker coefficients show that collective analysis of mathematical objects reveals patterns no individual study could find, and the best is likely still ahead.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges AI methodology and pure mathematics, applying supervised and unsupervised machine learning to abstract mathematical datasets to discover new structures in number theory and representation theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces the "platonic dataset" framework — a principled standard for ML experiments where data has exact definitions rather than empirical noise, offering a template for rigorous ML-driven scientific discovery.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The murmuration phenomenon in *L*-functions of elliptic curves is a genuinely new statistical regularity in arithmetic objects, with deep implications for the Langlands program and connections to string theory and physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include automating more of the conjecture-generation pipeline and extending MDS to geometric and topological objects; the paper is available at arXiv:2407.07346.</span></div></div>
</div>
