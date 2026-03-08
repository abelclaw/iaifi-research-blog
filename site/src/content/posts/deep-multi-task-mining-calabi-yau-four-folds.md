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
wordCount: 1217
---

## The Big Picture

Imagine you're an architect trying to design a building, but instead of working in ordinary three-dimensional space, you're folding reality itself into hidden extra dimensions. The shape of those dimensions, their twists and holes and overall geometry, determines everything about the physics that comes out the other side: how many matter particles exist, what forces they feel, whether atoms and chemistry are even possible.

String theorists face exactly this challenge. The mathematical objects at the center of it are called **Calabi-Yau manifolds**, geometric spaces that string theory requires to be curled up at scales far too small for any microscope. To make predictions about physics (say, the number of generations of quarks and electrons), physicists need precise structural properties of these spaces called **Hodge numbers**. These are integers that count how many independent structural features a Calabi-Yau manifold has of different types.

But computing Hodge numbers is brutally hard. The catalog of four-dimensional Calabi-Yau spaces known as **CICY four-folds** contains nearly a million distinct configurations, and their Hodge number computation can be NP-hard. A team from MIT, CEA Paris-Saclay, and Uppsala University decided to let deep learning take a crack at it.

Their result: a single neural network called *CICYMiner* that learns all four independent Hodge numbers simultaneously and, with enough training data, achieves perfect accuracy.

> **Key Insight:** By treating Calabi-Yau geometry as a multi-task learning problem inspired by computer vision, the team hit 100% accuracy on two Hodge numbers and near-perfect results on the others. Deep learning can solve problems that have resisted algebraic geometry techniques for decades.

## How It Works

The raw input to the network is surprisingly visual. Each of the 921,497 CICY four-fold manifolds in the dataset is described by a **configuration matrix**, a rectangular grid of integers encoding how the manifold is built from polynomial equations in a high-dimensional mathematical space. Earlier work showed that treating these matrices as grayscale images and feeding them to a neural network worked well for simpler three-dimensional Calabi-Yau spaces. The same intuition carries over here.

![Figure 1](figure:1)

The team stacked **Inception modules**, the same building blocks behind Google's image recognition models, to process these mathematical matrices. An Inception module applies multiple convolutional filters of different sizes in parallel, then concatenates their outputs. This lets the network pick up on both local structure (individual matrix entries) and global patterns (relationships spanning the whole matrix) at the same time.

What sets CICYMiner apart is its **multi-task architecture**. Rather than training four separate networks, one for each Hodge number, CICYMiner branches at its top layers into four task-specific heads while sharing a common trunk of Inception modules. This **hard parameter sharing** forces all four prediction tasks to draw on the same learned internal representation. The network develops a single view of Calabi-Yau geometry, with each head specializing to extract a different invariant. There is physical motivation here too: all four Hodge numbers arise from the same underlying geometry, so a single model ought to capture them all. The shared representation also acts as a regularizer, reducing overfitting.

![Figure 3](figure:3)

Training had to contend with severe **class imbalance**. The distribution of Hodge numbers across the dataset is wildly skewed: a handful of values appear tens of thousands of times while others show up exactly once. The team treated prediction as a classification problem (which discrete value does each Hodge number take?) rather than regression, and tuned their loss functions to prevent the network from simply memorizing the most common classes.

The results came in strong:

- **h^(1,1):** 100% accuracy with just 30% training data
- **h^(2,1):** 97% with 30% data, 100% with 80%
- **h^(3,1):** 81% with 30% data, 96% with 80%
- **h^(2,2):** 49% with 30% data, 83% with 80%

The hardest number, h^(2,2), reflects genuinely richer geometric complexity. Its values span a much wider range and the dataset distribution is more spread out. But physics saves the day. The **Euler characteristic**, a single integer summarizing a manifold's overall topological shape, satisfies a linear formula tying all four Hodge numbers together. Since the Euler characteristic is easy to compute algebraically, you can plug it in as a constraint. Do that, and the model achieves **100% total accuracy** even where individual predictions were uncertain.

![Figure 5](figure:5)

## Why It Matters

The stakes go well beyond mathematical curiosity. String theory's most pressing practical problem is the **string landscape**: an estimated 10^272,000 possible vacuum configurations when compactifying on Calabi-Yau four-folds. Nobody can compute the properties of each one by hand. Machine learning tools that rapidly classify topological invariants may be the only viable way to navigate this enormous space and find configurations that reproduce the physics we actually observe.

The multi-task framing is interesting in its own right. When a single neural network learns all four Hodge numbers from one shared representation, it may be implicitly encoding a unified mathematical structure, one that could eventually be decoded into human-readable theorems. The authors raise this possibility: a unified model might yield closed-form formulas connecting configuration matrix structure directly to Hodge numbers, formulas that have eluded mathematicians working by hand. Extending the approach to non-standard vector bundles could also unlock predictions for matter spectra in realistic string compactifications.

> **Bottom Line:** CICYMiner shows that computer vision architectures adapted for abstract mathematical data can master Calabi-Yau geometry at scale. Combining multi-task learning with known physical constraints pushes accuracy to 100%, and the approach could help guide the search for physically realistic string vacua.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects state-of-the-art computer vision (Inception modules, multi-task learning) with one of the central mathematical challenges in string theory, showing that image-inspired architectures can extract deep geometric information from algebraic data.

- **Impact on Artificial Intelligence:** The paper treats CICY four-folds as a rigorous, large-scale benchmark for multi-task learning on structured mathematical inputs. Hard parameter sharing with task-specific heads significantly outperforms single-task baselines on highly imbalanced classification problems.

- **Impact on Fundamental Interactions:** By achieving near-perfect prediction of all four Hodge numbers of Calabi-Yau four-folds, the work provides a practical tool for rapidly characterizing string compactifications and sorting through the enormous space of possible vacuum configurations in F-theory.

- **Outlook and References:** Future work will extend CICYMiner to non-standard vector bundles whose cohomologies directly determine particle spectra in string phenomenology; the full paper and code are available at [arXiv:2108.02221](https://arxiv.org/abs/2108.02221) and on GitHub.

## Original Paper Details
- **Title:** Deep multi-task mining Calabi-Yau four-folds
- **arXiv ID:** 2108.02221
- **Authors:** ["Harold Erbin", "Riccardo Finotello", "Robin Schneider", "Mohamed Tamaazousti"]
- **Abstract:** We continue earlier efforts in computing the dimensions of tangent space cohomologies of Calabi-Yau manifolds using deep learning. In this paper, we consider the dataset of all Calabi-Yau four-folds constructed as complete intersections in products of projective spaces. Employing neural networks inspired by state-of-the-art computer vision architectures, we improve earlier benchmarks and demonstrate that all four non-trivial Hodge numbers can be learned at the same time using a multi-task architecture. With 30% (80%) training ratio, we reach an accuracy of 100% for $h^{(1,1)}$ and 97% for $h^{(2,1)}$ (100% for both), 81% (96%) for $h^{(3,1)}$, and 49% (83%) for $h^{(2,2)}$. Assuming that the Euler number is known, as it is easy to compute, and taking into account the linear constraint arising from index computations, we get 100% total accuracy.
