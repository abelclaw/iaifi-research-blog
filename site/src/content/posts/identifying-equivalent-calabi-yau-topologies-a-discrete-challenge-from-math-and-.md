---
abstract: We review briefly the characteristic topological data of Calabi--Yau threefolds
  and focus on the question of when two threefolds are equivalent through related
  topological data. This provides an interesting test case for machine learning methodology
  in discrete mathematics problems motivated by physics.
arxivId: '2202.07590'
arxivUrl: https://arxiv.org/abs/2202.07590
authors:
- Vishnu Jejjala
- Washington Taylor
- Andrew Turner
concepts:
- calabi-yau topology
- topological equivalence
- string theory
- triple intersection numbers
- classification
- group theory
- geometric deep learning
- interpretability
- representation learning
- kernel methods
figures:
- /iaifi-research-blog/figures/2202_07590/figure_1.png
- /iaifi-research-blog/figures/2202_07590/figure_1.png
- /iaifi-research-blog/figures/2202_07590/figure_2.png
- /iaifi-research-blog/figures/2202_07590/figure_2.png
- /iaifi-research-blog/figures/2202_07590/figure_3.png
- /iaifi-research-blog/figures/2202_07590/figure_3.png
pdfUrl: https://arxiv.org/pdf/2202.07590v1
published: '2022-02-15T17:26:13+00:00'
theme: Theoretical Physics
title: 'Identifying equivalent Calabi--Yau topologies: A discrete challenge from math
  and physics for machine learning'
wordCount: 1007
---

## The Big Picture

Imagine two different-looking maps of the same city, one using compass directions, the other a rotated coordinate system. The cities are identical, but proving it requires matching every feature across both representations. Now scale that problem to six-dimensional geometric spaces with hundreds of millions of variants, replace coordinate rotations with an infinite family of allowed mathematical rearrangements, and remove any known algorithm for solving it. That's the challenge facing physicists trying to classify the shapes of extra dimensions in string theory.

String theory requires ten dimensions, but we observe only four. The remaining six must be curled into an impossibly small geometry called a **Calabi-Yau threefold**, a class of six-dimensional shapes compatible with both general relativity and supersymmetry. The Kreuzer-Skarke database catalogs 473,800,776 such families. The catch: many "different" entries may actually describe the *same* geometry written in different mathematical coordinates.

Jejjala, Taylor, and Turner frame this identification challenge as a precise machine learning problem. They test the approach on a simpler, tractable analogue to see how well ML can actually solve it.

> **Key Insight:** Determining whether two Calabi-Yau geometries are the same shape requires testing equivalence under an infinite family of allowed transformations, a problem with no known algorithm. This makes it a natural and genuinely hard target for machine learning.

## How It Works

The **topology** of a Calabi-Yau threefold (the study of properties preserved under smooth stretching or bending, like the difference between a sphere and a donut) is encoded in a finite list of integers. By Wall's theorem, three pieces of data completely characterize it:

- **Hodge numbers** (h^{1,1} and h^{2,1}): count types of geometric "holes" in the space
- **Triple intersection numbers** C_{ijk}: a symmetric three-index tensor recording how divisors (complex codimension-one slices of the geometry) intersect each other
- **First Pontryagin class**: an integer-valued quantity encoding how the geometry curves on itself

![Figure 1](figure:1)

Two geometries are topologically equivalent if there exists an integer matrix Λ in SL(N,ℤ), the group of N×N integer matrices with determinant 1, that transforms one set of triple intersection numbers into the other via C'_{ijk} = Λ_{il} Λ_{jm} Λ_{kn} C_{lmn}. The problem is that SL(N,ℤ) is *infinite*. No finite-time algorithm is known. Some **topological invariants** exist (quantities unchanged under any such rearrangement, like the greatest common divisor of all C_{ijk} entries), but they're incomplete: matching invariants don't guarantee equivalence.

To test whether ML can make progress, the authors study a mathematically analogous but tractable problem: **unitary equivalence of complex matrices**. Two matrices A and B are unitarily equivalent if B = ΛAΛ† for some unitary Λ, a rotation-like transformation preserving lengths and angles. **Specht's theorem** gives a complete answer here: two matrices are equivalent if and only if all "word traces" Tr W(A, A†) agree, where W ranges over combinations built from A and its **adjoint** (the conjugate transpose, obtained by flipping across the diagonal and taking complex conjugates). For N×N matrices, only finitely many such combinations need checking.

![Figure 2](figure:2)

The team trained neural networks to predict whether matrix pairs are unitarily equivalent. The real question was whether the networks would learn Specht invariants or find something else entirely.

Networks distinguish equivalent from non-equivalent pairs with high accuracy. Probing what they actually compute reveals they are implicitly capturing the trace invariants that Specht's theorem prescribes. The ML system rediscovers the known mathematical structure from data alone.

![Figure 3](figure:3)

## Why It Matters

The connection to physics is direct. In **F-theory**, a twelve-dimensional framework generalizing string theory, the topology of Calabi-Yau threefolds determines the gauge group and matter content of the resulting four-dimensional physics. If two seemingly different geometries are actually identical, counting them separately inflates the string landscape. Resolving this overcounting is a prerequisite to understanding whether the string landscape is truly finite and to identifying which physical theories are genuinely distinct.

There is a broader ML lesson here too. Discrete mathematics problems where the symmetry group is infinite and no polynomial-time algorithm exists represent a genuinely hard frontier. Unlike continuous optimization, you can't gradient-descend your way to an exact equivalence check over ℤ.

The paper makes the case that this class of problems needs dedicated attention: not just applying existing architectures, but developing methods that can *discover* new algebraic invariants from data, the way mathematicians discovered Specht's theorem by hand. The analogy between matrix and tensor equivalence suggests a systematic ladder of increasingly hard problems that ML can climb toward the full Calabi-Yau case.

![Figure 4](figure:4)

> **Bottom Line:** Machine learning can detect topological equivalence in structured mathematical problems, and in the tractable matrix case it recovers known invariants from scratch. The full Calabi-Yau equivalence problem remains open, one of the hardest mathematical challenges the field can put in front of AI.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects algebraic geometry and machine learning by framing a long-standing unsolved problem in string theory compactification as a concrete ML benchmark, with rigorous mathematical grounding on both sides.

- **Impact on Artificial Intelligence:** The paper introduces a well-posed discrete equivalence problem, with known ground truth in the matrix case, as a demanding testbed for ML methods that go beyond continuous optimization and pattern matching.

- **Impact on Fundamental Interactions:** Solving the Calabi-Yau equivalence problem would directly reduce overcounting in the string landscape, clarifying which four-dimensional physical theories can genuinely arise from string compactification.

- **Outlook and References:** The authors call for ML approaches capable of discovering new algebraic invariants, not just classifying known equivalences. The work appears as [arXiv:2202.07590](https://arxiv.org/abs/2202.07590) and points toward a systematic ML attack on the full Kreuzer-Skarke database.

## Original Paper Details
- **Title:** Identifying equivalent Calabi--Yau topologies: A discrete challenge from math and physics for machine learning
- **arXiv ID:** 2202.07590
- **Authors:** ["Vishnu Jejjala", "Washington Taylor", "Andrew Turner"]
- **Abstract:** We review briefly the characteristic topological data of Calabi--Yau threefolds and focus on the question of when two threefolds are equivalent through related topological data. This provides an interesting test case for machine learning methodology in discrete mathematics problems motivated by physics.
