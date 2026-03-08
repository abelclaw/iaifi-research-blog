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
wordCount: 947
---

## The Big Picture

Imagine two different-looking maps of the same city — one using compass directions, the other a rotated coordinate system. The cities are identical, but proving it requires matching every feature across both representations. Now scale that problem to six-dimensional geometric spaces with hundreds of millions of variants, replace coordinate rotations with an infinite family of allowed mathematical rearrangements, and remove any known algorithm for solving it. That's the challenge facing physicists trying to classify the shapes of extra dimensions in string theory.

String theory requires ten dimensions, but we observe only four. The remaining six must be curled into an impossibly small geometry — a **Calabi-Yau threefold**, a class of six-dimensional shapes compatible with both general relativity and supersymmetry. The Kreuzer-Skarke database catalogs 473,800,776 such families. The catch: many "different" entries may actually describe the *same* geometry written in different mathematical coordinates.

This paper, by Jejjala, Taylor, and Turner, frames this identification challenge as a precise machine learning problem — and uses a simpler, tractable analogue to test how well ML can actually solve it.

> **Key Insight:** Determining whether two Calabi-Yau geometries are the same shape requires testing equivalence under an infinite family of allowed transformations — a problem with no known algorithm, making it a natural and genuinely hard target for machine learning.

## How It Works

The **topology** of a Calabi-Yau threefold — the study of properties preserved under smooth stretching or bending, like the difference between a sphere and a donut — is encoded in a finite list of integers. By Wall's theorem, three pieces of data completely characterize it:

- **Hodge numbers** (h^{1,1} and h^{2,1}): count types of geometric "holes" in the space
- **Triple intersection numbers** C_{ijk}: a symmetric three-index tensor recording how divisors — complex codimension-one slices of the geometry — intersect each other
- **First Pontryagin class**: an integer-valued quantity encoding how the geometry curves on itself

![Figure 1](/iaifi-research-blog/figures/2202_07590/figure_1.png)

Two geometries are topologically equivalent if there exists an integer matrix Λ in SL(N,ℤ) — the group of N×N integer matrices with determinant 1 — that transforms one set of triple intersection numbers into the other via C'_{ijk} = Λ_{il} Λ_{jm} Λ_{kn} C_{lmn}. The problem: SL(N,ℤ) is *infinite*. No finite-time algorithm is known. Some **topological invariants** — quantities unchanged under any such rearrangement, like the greatest common divisor of all C_{ijk} entries — exist, but they're incomplete: matching invariants don't guarantee equivalence.

To test whether ML can make progress, the authors study a mathematically analogous but tractable problem: **unitary equivalence of complex matrices**. Two matrices A and B are unitarily equivalent if B = ΛAΛ† for some unitary Λ — a rotation-like transformation preserving lengths and angles. For this case, **Specht's theorem** gives a complete answer: two matrices are equivalent if and only if all "word traces" Tr W(A, A†) agree, where W ranges over combinations built from A and its **adjoint** (the conjugate transpose, obtained by flipping across the diagonal and taking complex conjugates). For N×N matrices, only finitely many such combinations need checking.

![Figure 2](/iaifi-research-blog/figures/2202_07590/figure_1.png)

The researchers trained neural networks to predict whether matrix pairs are unitarily equivalent. The key question: would networks learn Specht invariants, or find something else?

The results are instructive. Networks distinguish equivalent from non-equivalent pairs with high accuracy, and probing what they actually compute reveals they are implicitly capturing the trace invariants Specht's theorem prescribes. The ML system rediscovers the known mathematical structure from data alone.

![Figure 3](/iaifi-research-blog/figures/2202_07590/figure_2.png)

## Why It Matters

The connection to physics is direct. In **F-theory** — a twelve-dimensional framework generalizing string theory — the topology of Calabi-Yau threefolds determines the gauge group and matter content of the resulting four-dimensional physics. If two seemingly different geometries are actually identical, counting them separately artificially inflates the landscape. Resolving this overcounting is prerequisite to understanding whether the string landscape is truly finite, and to identifying which physical theories are genuinely distinct.

The broader ML lesson is equally sharp. Discrete mathematics problems — where the symmetry group is infinite and no polynomial-time algorithm exists — represent a genuinely hard frontier. Unlike continuous optimization, you can't gradient-descend your way to an exact equivalence check over ℤ.

The paper argues this class of problems deserves dedicated attention: not just applying existing architectures, but developing methods that can *discover* new algebraic invariants from data, the way physicists discovered Specht's theorem by hand. The analogy between matrix and tensor equivalence suggests a systematic ladder of increasingly hard problems that ML can climb toward the full Calabi-Yau case.

![Figure 4](/iaifi-research-blog/figures/2202_07590/figure_2.png)

> **Bottom Line:** Machine learning can detect topological equivalence in structured mathematical problems, and in the tractable matrix case it recovers known invariants from scratch — but the full Calabi-Yau equivalence problem remains open, representing one of the most mathematically deep challenges the field can offer AI.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges algebraic geometry and machine learning by framing a century-old unsolved problem in string theory compactification as a concrete ML benchmark, with rigorous mathematical grounding on both sides.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces a well-posed discrete equivalence problem — with known ground truth in the matrix case — as a demanding testbed for ML methods that go beyond continuous optimization and pattern matching.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Solving the Calabi-Yau equivalence problem would directly reduce overcounting in the string landscape, sharpening our understanding of which four-dimensional physical theories can genuinely arise from string compactification.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The authors call for ML approaches capable of discovering new algebraic invariants, not just classifying known equivalences; the work appears as arXiv:2202.12887 and points toward a systematic ML attack on the full Kreuzer-Skarke database.</span></div></div>
</div>
