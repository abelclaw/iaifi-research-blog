---
abstract: In this paper, we conduct a data-scientific investigation of Maass forms.
  We find that averaging the Fourier coefficients of Maass forms with the same Fricke
  sign reveals patterns analogous to the recently discovered "murmuration" phenomenon,
  and that these patterns become more pronounced when parity is incorporated as an
  additional feature. Approximately 43% of the forms in our dataset have an unknown
  Fricke sign. For the remaining forms, we employ Linear Discriminant Analysis (LDA)
  to machine learn their Fricke sign, achieving 96% (resp. 94%) accuracy for forms
  with even (resp. odd) parity. We apply the trained LDA model to forms with unknown
  Fricke signs to make predictions. The average values based on the predicted Fricke
  signs are computed and compared to those for forms with known signs to verify the
  reasonableness of the predictions. Additionally, a subset of these predictions is
  evaluated against heuristic guesses provided by Hejhal's algorithm, showing a match
  approximately 95% of the time. We also use neural networks to obtain results comparable
  to those from the LDA model.
arxivId: '2501.02105'
arxivUrl: https://arxiv.org/abs/2501.02105
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
- maass forms
- classification
- murmuration phenomenon
- feature extraction
- semi-supervised learning
- l-functions
- spectral methods
- interpretability
- clustering
- dimensionality reduction
figures:
- /iaifi-research-blog/figures/2501_02105/figure_1.png
- /iaifi-research-blog/figures/2501_02105/figure_2.png
- /iaifi-research-blog/figures/2501_02105/figure_3.png
pdfUrl: https://arxiv.org/pdf/2501.02105v2
published: '2025-01-03T21:22:29+00:00'
theme: Theoretical Physics
title: Learning Fricke signs from Maass form Coefficients
wordCount: 941
---

## The Big Picture

Imagine you're a librarian cataloging a vast archive of mathematical objects, each with a hidden label that determines its fundamental behavior. You've correctly labeled about half the collection, but the other half remains a mystery because the labeling process is so computationally difficult that even the best algorithms struggle. Then someone walks in and asks: "What if we could teach a machine to read the labels without doing the hard calculation?" That's exactly what a team of nine mathematicians and data scientists just did.

The objects in question are **Maass forms**, a special class of mathematical functions central to number theory. Each carries a hidden binary label called a **Fricke sign** (either +1 or −1) that encodes how the form behaves under a specific transformation. Computing this sign rigorously requires knowing the form's numerical fingerprint to extraordinary precision, a task so demanding that nearly half of all Maass forms in the world's largest mathematical database remain unlabeled.

Using machine learning, the team achieved over 96% accuracy predicting Fricke signs from that fingerprint alone, then applied their model to fill in thousands of missing labels.

> **Key Insight:** Machine learning can recover a fundamental number-theoretic invariant that conventional computation struggles to determine, by treating the entire dataset collectively rather than analyzing each object in isolation.

## How It Works

The data comes from the **LMFDB** (L-functions and Modular Forms Database), a community-built repository containing 35,416 Maass forms. Roughly 15,423 of them, about 43%, lack rigorously computed Fricke signs. The researchers trained their models on the ~20,000 forms with known signs.

The first discovery came before any machine learning. When the team averaged the **Fourier coefficients** (the sequence of numbers encoding each Maass form's essential structure) grouped by Fricke sign, a subtle but real pattern emerged. This mirrors the **"murmuration" phenomenon** first observed in elliptic curves: individual coefficients look noisy, but averaged across thousands of forms grouped by sign, they begin to oscillate in sync. Think of starlings in a flock. Each bird moves chaotically, but the flock as a whole exhibits breathtaking coordination.

![Figure 1](/iaifi-research-blog/figures/2501_02105/figure_1.png)

The patterns sharpened when the team incorporated **parity**, whether the form is symmetric (even) or antisymmetric (odd) under negation of its inputs. Parity and Fricke sign together carve out meaningful structure in the coefficient data.

With that insight, the team applied **Linear Discriminant Analysis (LDA)**, a classical statistical technique that finds the linear combination of features best separating two groups. Their pipeline:

1. **Input features:** Fourier coefficients $a_n$ for small primes and integers, plus the **spectral parameter** $R$ (a number characterizing each form's oscillation rate)
2. **Labels:** Known Fricke signs (+1 or −1), split by parity
3. **Training:** LDA fitted on the labeled subset
4. **Result:** 96% accuracy for even-parity forms, 94% for odd-parity forms

![Figure 2](/iaifi-research-blog/figures/2501_02105/figure_2.png)

Could the model be exploiting a shortcut? On **squarefree levels**, where the defining parameter $N$ has no repeated prime factors, the coefficient $a_N$ directly encodes the Fricke sign. A lazy classifier could just memorize this. The team explicitly ruled it out, showing that LDA extracts genuinely richer information from the coefficient data.

They also trained **neural networks** on the same data and achieved comparable accuracy. Agreement between a linear statistical method and a nonlinear deep model strengthens the conclusion: the signal is real.

![Figure 3](/iaifi-research-blog/figures/2501_02105/figure_3.png)

The researchers then predicted Fricke signs for all 15,423 unlabeled forms. Comparison against **Hejhal's algorithm**, a numerical method that heuristically estimates Fricke signs without rigorous guarantees, yielded a ~95% match rate. Both methods appear to be tracking the same underlying mathematical structure.

## Why It Matters

Maass forms are closely tied to **automorphic representations**, mathematical structures encoding deep symmetries at the heart of the Langlands program, one of the most ambitious unifying frameworks in modern mathematics. The Fricke sign controls the **functional equation** of the associated L-function, governing its symmetry and determining whether it vanishes at a special central point. Whether or not that zero exists connects to the **Birch and Swinnerton-Dyer conjecture**, one of the Millennium Prize Problems.

Beyond the specific application, the paper makes a broader methodological point: treating a mathematical database *collectively* reveals structure invisible to case-by-case computation. The murmuration connection, originally discovered through machine learning on elliptic curves, hints at a unifying statistical principle operating across different classes of automorphic forms.

Unsupervised methods like **k-means clustering** failed where supervised LDA succeeded. The Fricke sign is learnable from coefficients but not spontaneously discoverable without labels. Future work will focus on *interpreting* the classifiers; understanding which coefficients matter most may yield new mathematical theorems.

> **Bottom Line:** By treating ~35,000 mathematical objects as a dataset rather than isolated problems, this team predicted a notoriously hard-to-compute quantity with >96% accuracy and uncovered new statistical structure in Maass forms that mathematicians are only beginning to understand.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies modern data science (Linear Discriminant Analysis and neural networks) to one of the hardest open computational problems in analytic number theory, showing that AI can complement and extend traditional mathematical methods.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Classical linear classifiers match neural networks in structured mathematical domains, and parity-constrained features dramatically improve classification of binary invariants previously thought resistant to general-purpose machine learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Predicting Fricke signs for thousands of Maass forms expands the effective scope of the LMFDB and advances understanding of L-function symmetries central to the Langlands program and its connections to quantum physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will focus on interpretability, identifying which Fourier coefficients drive the classifier, potentially yielding new theoretical insights into Fricke signs; the paper is available at [arXiv:2501.02105](https://arxiv.org/abs/2501.02105) (Bieri et al., 2025).</span></div></div>
</div>
