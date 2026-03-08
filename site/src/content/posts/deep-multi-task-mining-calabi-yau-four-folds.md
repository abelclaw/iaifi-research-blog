---
abstract: We continue earlier efforts in computing the dimensions of tangent space
  cohomologies of Calabi-Yau manifolds using deep learning. In this paper, we consider
  the dataset of all Calabi-Yau four-folds constructed as complete intersections in
  products of projective spaces. Employing neural networks inspired by state-of-the-art
  computer vision architectures, we improve earlier benchmarks and demonstrate that
  all four non-trivial Hodge numbers can be learned at the same time using a multi-task
  architecture. With 30% (80%) training ratio, we reach an accuracy of 100% for $h^{(1,1)}$
  and 97% for $h^{(2,1)}$ (100% for both), 81% (96%) for $h^{(3,1)}$, and 49% (83%)
  for $h^{(2,2)}$. Assuming that the Euler number is known, as it is easy to compute,
  and taking into account the linear constraint arising from index computations, we
  get 100% total accuracy.
arxivId: '2108.02221'
arxivUrl: https://arxiv.org/abs/2108.02221
authors:
- Harold Erbin
- Riccardo Finotello
- Robin Schneider
- Mohamed Tamaazousti
concepts:
- multi-task learning
- calabi-yau manifolds
- hodge number prediction
- string theory
- convolutional networks
- cicy dataset
- classification
- regression
- representation learning
- transfer learning
- scalability
- data augmentation
figures:
- /iaifi-research-blog/figures/2108_02221/figure_1.png
- /iaifi-research-blog/figures/2108_02221/figure_1.png
- /iaifi-research-blog/figures/2108_02221/figure_2.png
- /iaifi-research-blog/figures/2108_02221/figure_2.png
- /iaifi-research-blog/figures/2108_02221/figure_3.png
- /iaifi-research-blog/figures/2108_02221/figure_3.png
pdfUrl: https://arxiv.org/pdf/2108.02221v2
published: '2021-08-04T18:00:15+00:00'
theme: Theoretical Physics
title: Deep multi-task mining Calabi-Yau four-folds
wordCount: 1120
---

## The Big Picture

Imagine you're an architect trying to design a building, but instead of working in ordinary three-dimensional space, you're folding reality itself into hidden extra dimensions. The shape of those dimensions — their twists, holes, and overall geometry — determines everything about the physics that emerges: how many matter particles exist, what forces they feel, whether our universe could even support atoms and chemistry.

String theorists face exactly this challenge. The mathematical objects at the center of it all are called **Calabi-Yau manifolds** — exotic geometric spaces that string theory requires to be curled up at scales far smaller than any microscope can see.

To make predictions about physics — say, the number of generations of fundamental particles like quarks and electrons — physicists need precise structural properties of these spaces called **Hodge numbers**: a set of integers that encode the geometric complexity of a Calabi-Yau manifold, essentially counting how many independent structural features the space has of different types.

But computing Hodge numbers is brutally hard. The catalog of four-dimensional Calabi-Yau spaces known as **CICY four-folds** contains nearly a million distinct configurations, and classical computation of their Hodge numbers can be NP-hard — computationally intractable even for powerful modern computers. A team from MIT, CEA Paris-Saclay, and Uppsala University decided to let deep learning take a crack at it.

Their result: a single neural network called *CICYMiner* that learns all four independent Hodge numbers simultaneously — and with enough training data, achieves perfect accuracy.

> **Key Insight:** By treating Calabi-Yau geometry as a multi-task learning problem inspired by computer vision, researchers achieved 100% accuracy on two Hodge numbers and near-perfect results on the others — demonstrating that deep learning can crack problems that have stumped algebraic geometers for decades.

## How It Works

The raw input to the network is surprisingly visual. Each of the 921,497 CICY four-fold manifolds in the dataset is described by a **configuration matrix** — a rectangular grid of integers encoding how the manifold is built from polynomial equations embedded in a high-dimensional mathematical space. Earlier work showed that treating these matrices as grayscale images and feeding them to a neural network worked well for simpler three-dimensional Calabi-Yau spaces. The same intuition carries over here.

![Figure 1](/iaifi-research-blog/figures/2108_02221/figure_1.png)

The team's key architectural insight was to stack **Inception modules** — the same building blocks that power Google's computer vision models for recognizing objects in photos — to process these mathematical matrices. An Inception module applies multiple convolutional filters of different sizes in parallel, then concatenates their outputs. This lets the network pick up on both local structure (individual matrix entries) and global patterns (relationships across the whole matrix) simultaneously.

The real innovation is the **multi-task architecture**. Instead of training four separate networks — one for each Hodge number — CICYMiner branches at its top layers into four task-specific heads while sharing a common trunk of Inception modules. This **hard parameter sharing** forces all four prediction tasks to draw on the same learned internal representation, so the network develops a unified view of Calabi-Yau geometry, with each head specializing to extract a different invariant. Multi-task learning is known to regularize models and reduce overfitting; here it also carries a deeper physical meaning: all four Hodge numbers arise from the same underlying geometry, so a single model should capture them all.

![Figure 3](/iaifi-research-blog/figures/2108_02221/figure_2.png)

Training had to handle a major challenge: **class imbalance**. The distribution of Hodge numbers across the dataset is wildly skewed — a handful of values appear tens of thousands of times while others appear only once. The team treated this as a classification problem (predicting which discrete value each Hodge number takes) rather than regression, and carefully tuned their loss functions to prevent the network from simply memorizing the most common classes.

Results came in strong:

- **h^(1,1):** 100% accuracy with just 30% training data
- **h^(2,1):** 97% with 30% data, 100% with 80%
- **h^(3,1):** 81% with 30% data, 96% with 80%
- **h^(2,2):** 49% with 30% data, 83% with 80%

The hardest number, h^(2,2), reflects genuinely richer geometric complexity — its values span a much wider range and the dataset distribution is more spread out. But here physics saves the day: the **Euler characteristic** — a single integer that acts like a geometric fingerprint, summarizing a manifold's overall shape — satisfies a formula tying all four Hodge numbers together. The Euler characteristic is easy to compute algebraically. Plug it in as a known constraint, and the model achieves **100% total accuracy** even where individual predictions were uncertain.

![Figure 5](/iaifi-research-blog/figures/2108_02221/figure_3.png)

## Why It Matters

The stakes go well beyond mathematical curiosity. String theory's most pressing practical problem is the **landscape** — the estimated 10^272,000 possible vacuum configurations when compactifying on Calabi-Yau four-folds. Physicists cannot compute the properties of each one by hand. Machine learning tools that rapidly classify topological invariants are the only plausible way to navigate this vast terrain and identify configurations that might reproduce the physics of our observed universe.

The multi-task framing also opens a conceptual door. When a single neural network learns all four Hodge numbers from the same internal representation, it may be implicitly encoding a unified mathematical structure — one that could be decoded into human-readable theorems. The authors gesture at this possibility: a unified model could yield closed-form formulas connecting configuration matrix structure directly to Hodge numbers, formulas that have eluded mathematicians working by hand. Future extensions to non-standard vector bundles could unlock predictions relevant to computing matter spectra in realistic string compactifications.

> **Bottom Line:** CICYMiner proves that computer vision architectures adapted for abstract mathematical data can master Calabi-Yau geometry at scale — and combining multi-task learning with known physical constraints pushes accuracy to 100%, pointing toward a future where AI actively guides the search for physically realistic string vacua.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges state-of-the-art computer vision (Inception modules, multi-task learning) with one of the central mathematical challenges in string theory, demonstrating that image-inspired architectures can extract deep geometric information from algebraic data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper establishes CICY four-folds as a rigorous, large-scale benchmark for multi-task learning on structured mathematical inputs, showing that hard parameter sharing with task-specific heads dramatically outperforms single-task baselines on highly imbalanced classification problems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By achieving near-perfect prediction of all four Hodge numbers of Calabi-Yau four-folds, the research provides a practical tool for rapidly characterizing string compactifications and navigating the enormous landscape of possible vacuum configurations in F-theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work aims to apply CICYMiner to non-standard vector bundles whose cohomologies directly determine particle spectra in string phenomenology; the full paper and code are available on arXiv (arXiv:2108.13027) and GitHub.</span></div></div>
</div>
