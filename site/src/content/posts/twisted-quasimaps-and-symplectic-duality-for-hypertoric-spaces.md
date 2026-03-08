---
abstract: We study moduli spaces of twisted quasimaps to a hypertoric variety $X$,
  arising as the Higgs branch of an abelian supersymmetric gauge theory in three dimensions.
  These parametrise general quiver representations whose building blocks are maps
  between rank one sheaves on $\mathbb{P}^1$, subject to a stability condition, associated
  to the quiver, involving both the sheaves and the maps. We show that the singular
  cohomology of these moduli spaces is naturally identified with the Ext group of
  a pair of holonomic modules over the `quantized loop space' of $X$, which we view
  as a Higgs branch for a related theory with infinitely many matter fields. We construct
  the coulomb branch of this theory, and find that it is a periodic analogue of the
  coulomb branch associated to $X$. Using the formalism of symplectic duality, we
  derive an expression for the generating function of twisted quasimap invariants
  in terms of the character of a certain tilting module on the periodic coulomb branch.
  We give a closed formula for this generating function when $X$ arises as the abelianisation
  of the $N$-step flag quiver.
arxivId: '2004.04508'
arxivUrl: https://arxiv.org/abs/2004.04508
authors:
- Michael McBreen
- Artan Sheshmani
- Shing-Tung Yau
concepts:
- symplectic duality
- hypertoric varieties
- quiver representations
- quantum field theory
- tilting modules
- koszul duality
- quantization
- enumerative geometry
- category o
- flag quivers
- symmetry breaking
- spectral methods
figures:
- /iaifi-research-blog/figures/2004_04508/figure_1.png
- /iaifi-research-blog/figures/2004_04508/figure_1.png
- /iaifi-research-blog/figures/2004_04508/figure_2.png
- /iaifi-research-blog/figures/2004_04508/figure_2.png
- /iaifi-research-blog/figures/2004_04508/figure_3.png
- /iaifi-research-blog/figures/2004_04508/figure_3.png
pdfUrl: https://arxiv.org/pdf/2004.04508v4
published: '2020-04-09T12:11:36+00:00'
theme: Foundational AI
title: Twisted Quasimaps and Symplectic Duality for Hypertoric Spaces
wordCount: 995
---

## The Big Picture

Imagine trying to understand a complex gemstone by studying only one face. You could catalog every facet, measure every angle, and still miss half the picture. Now imagine discovering that every gemstone has an invisible twin, and that counting the facets of one tells you something deep about the structure of the other.

That's roughly what **symplectic duality** does: it pairs each geometric space with a mathematical "mirror twin" and shows that deep properties of one can be read off the other. This idea drives the new work by McBreen, Sheshmani, and Yau.

The spaces they study are called **hypertoric varieties**, geometric objects built from layers of symmetry that arise where modern physics meets pure mathematics. They appear in supersymmetric gauge theories, representing the possible configurations of quantum fields. Mathematicians have spent decades building tools to probe their structure.

But a key question lingered: can you compute certain *shape-counting numbers*, quantities recording how maps can topologically wrap around these spaces, using purely algebraic data from the mirror twin? This paper answers yes, constructing an explicit dictionary and delivering a closed, computable formula.

> **Key Insight:** The counting function for maps wrapping around these geometric spaces can be decoded from a single algebraic object (a tilting module) living on the mirror "twin" space, converting a hard geometric problem into an explicit algebraic calculation.

## How It Works

The central objects of study are **twisted quasimaps**: maps from the projective line ℙ¹ into a hypertoric variety X. These are built from **line bundles** (geometric packages assigning a one-dimensional vector space to each point) connected by algebraic maps subject to a stability condition that rules out degenerate cases.

Counting these objects, weighted by topological class and cohomological degree, produces a **generating function** Υ^ref(z, τ). This single expression encodes infinitely many counting numbers at once, acting as a fingerprint for the geometry of X.

![Figure 1](figure:1)

Direct computation of this generating function is forbiddingly hard. The authors take a roundabout route, through symplectic duality, that transforms the problem into something tractable. Their strategy has three steps:

1. **Lift to a loop space.** They construct a symplectic ind-scheme LX̃, a rigorously defined infinite-dimensional space modeling all closed loops in X. The moduli of twisted quiver sheaves embeds into LX̃ as an **intersection of Lagrangians**, pairs of half-dimensional subspaces whose overlap captures exactly the quasimap data. This translates counting quasimaps into computing Ext groups over the quantized loop space of X.

2. **Apply symplectic duality.** The paper extends symplectic duality, the pairing between X and its algebraic mirror X^!, to the infinite-dimensional loop setting. The dual of LX̃ turns out to be a *periodic* analogue PX^! of the **Coulomb branch**, the partner space describing a different physical regime of the same theory. This finite-dimensional but infinite-type space carries an action of H₂(X, ℤ). First sketched in unpublished work by Hausel and Proudfoot, the periodic Coulomb branch here receives a rigorous construction equipped with the algebraic tools needed for computation.

3. **Read off the answer via Koszul duality.** The authors establish a **Koszul duality**, a fundamental algebraic correspondence exchanging two different module categories, between category O for LX̃ and PX^!. This is the first extension of such a duality to the loop setting for symplectically dual spaces. Through this correspondence, the Ext groups from step one translate directly into weight spaces of an indecomposable **tilting module** T^!_ν(α+)^∞ on the quantized periodic Coulomb branch.

![Figure 2](figure:2)

The payoff is Theorem 1.1: Υ^ref(z, τ) equals a graded trace of this tilting module. From that algebraic expression, the authors extract Theorem 1.2, an explicit closed formula indexed by torus fixed points of X^! and combinatorial data attached to them. For X arising as the abelianization of the N-step flag quiver, every ingredient becomes concrete and computable.

## Why It Matters

This work sits at a productive frontier where **enumerative geometry** (the discipline of counting geometric objects: curves, maps, configurations) meets quantum algebra and physics.

Symplectic duality has driven enormous mathematical progress since Braden, Licata, Proudfoot, and Webster formalized it, inspired by three-dimensional mirror symmetry in physics. But explicit, computable results connecting both sides of a dual pair remain rare. McBreen, Sheshmani, and Yau deliver one: a theorem that takes a geometric counting problem and resolves it through pure algebra on the dual side.

The periodic Coulomb branch PX^! opens up new directions. When X comes from a graph Γ, this space connects to the **compactified Jacobian**, a classical object recording all line bundles on a curve (including degenerate limiting cases) of a nodal curve with dual graph Γ. The authors' framework suggests that more general enumerative problems on loop spaces of symplectic resolutions should be tractable via similar periodic duality constructions.

The natural next target is extending these results beyond the hypertoric (abelian) setting to non-abelian gauge theories, where the geometry is richer and the combinatorics wilder.

> **Bottom Line:** By extending symplectic duality to loop spaces and constructing a periodic Coulomb branch, McBreen, Sheshmani, and Yau turn a hard geometric counting problem into an explicit algebraic formula, showing that duality works not just as a guiding principle but as a hands-on computational tool.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work forges a precise mathematical link between the enumerative geometry of supersymmetric gauge theories and representation theory, showing how physical intuition about mirror symmetry can drive rigorous mathematical advances.

- **Impact on Artificial Intelligence:** The algebraic structures developed here, including periodic analogues of Coulomb branches and extended Koszul duality, expand the geometric and algebraic toolkit with potential applications to AI methods for scientific discovery.

- **Impact on Fundamental Interactions:** By computing refined Donaldson-Thomas invariants for hypertoric spaces via symplectic duality, this paper advances the mathematical understanding of three-dimensional supersymmetric gauge theories and their Higgs/Coulomb branch structure.

- **Outlook and References:** The periodic Coulomb branch construction points toward analogous results for non-abelian gauge theories, with connections to compactified Jacobians and loop group geometry; the paper is available at [arXiv:2004.04508](https://arxiv.org/abs/2004.04508).
