---
abstract: A strictification result is proved for isotropic distributions on derived
  schemes equipped with negatively shifted homotopically closed $2$-forms. It is shown
  that any derived scheme over $\mathbb{C}$ equipped with a $-2$-shifted symplectic
  structure, and having a Hausdorff space of classical points, admits a globally defined
  Lagrangian distribution as a dg $\mathbb{C}^{\infty}$-manifold.
arxivId: '1908.00651'
arxivUrl: https://arxiv.org/abs/1908.00651
authors:
- Dennis Borisov
- Ludmil Katzarkov
- Artan Sheshmani
- Shing-Tung Yau
concepts:
- shifted symplectic structures
- derived algebraic geometry
- lagrangian methods
- moduli spaces of sheaves
- group theory
- string theory
- quantum field theory
- symmetry preservation
- hamiltonian systems
- inverse problems
figures: []
pdfUrl: https://arxiv.org/pdf/1908.00651v3
published: '2019-08-01T22:47:10+00:00'
theme: Theoretical Physics
title: Strictification and gluing of Lagrangian distributions on derived schemes with
  shifted symplectic forms
wordCount: 1221
---

## The Big Picture

Imagine trying to flatten a crumpled piece of paper. Locally, in any small patch, you can iron out the wrinkles. But if the paper is folded into a sphere, no amount of local flattening produces a single smooth, flat sheet. This tension between local and global structure runs through both mathematics and physics.

Now imagine the "paper" is a mathematical space encoding all solutions to a system of equations, and "flattening" means imposing a consistent organizing structure across the whole space at once. That is what this research accomplishes.

The paper by Dennis Borisov, Ludmil Katzarkov, Artan Sheshmani, and Shing-Tung Yau tackles a deep problem in **derived algebraic geometry**, a branch of modern mathematics that handles spaces built from equations with hidden symmetries and higher-order structure. The central question: can you always find a globally consistent **Lagrangian distribution** on such a space, a coherent way of splitting it into two complementary halves, like separating positions from momenta in classical physics? The technical engine is a **shifted symplectic structure**, a generalization of the mathematical form encoding that position-momentum pairing. Under natural conditions, the answer is yes.

The stakes are high. These geometric structures appear naturally on **moduli spaces of sheaves on Calabi-Yau 4-folds**, mathematical catalogs of all possible field configurations in certain string-theoretic settings. Proving that globally consistent Lagrangian distributions exist unlocks new tools for computing invariants of these spaces (counting geometric objects rigorously and with correct signs), with direct implications for Donaldson-Thomas theory and the mathematics of Spin(7)-instantons.

> **Key Insight:** The authors prove that any derived scheme carrying a -2-shifted symplectic structure, under mild topological conditions on its classical points, admits a globally defined Lagrangian distribution, solving a problem that previously had only local solutions.

## How It Works

In classical mechanics, **phase space** tracks all possible positions and momenta of a physical system. It carries a **symplectic form**: a mathematical structure pairing each position coordinate with its corresponding momentum. A **Lagrangian subspace** is a "half-dimensional" subspace on which this pairing vanishes, like fixing all positions while letting momenta vary freely. In physics, Lagrangian submanifolds encode solutions to equations of motion.

**Derived schemes** generalize ordinary geometric spaces defined by polynomial equations by incorporating higher-order homotopy information. They show up naturally when intersecting spaces or studying moduli problems where objects carry automorphisms. On these derived spaces, the symplectic form gets "shifted": instead of being an ordinary 2-form, it lives in a degree shifted by an integer, and the conditions of being closed and non-degenerate hold only up to homotopy. The relevant case here, a **-2-shifted symplectic structure**, appears on moduli spaces of sheaves on Calabi-Yau 4-folds.

The central challenge is that shifted symplectic forms are inherently "floppy": defined up to higher homotopies, with different local representations that may not obviously fit together globally. The 2016 local Darboux theorem of Brav, Bussi, and Joyce established that any negatively shifted symplectic form can be locally **strictified**, rewritten in canonical coordinates where the homotopies disappear, analogous to the standard $dq \wedge dp$ form from classical mechanics. But that result was inherently local.

The new paper addresses the global question through two interlocking results:

1. **Local strictification of isotropic distributions.** The authors work with purely derived foliations, distributions confined entirely to the higher-order, non-classical part of the geometry. For such distributions equipped with an isotropic structure (the Lagrangian condition formulated up to homotopy), they prove that one can always find an equivalent distribution in a canonical strict form locally.

2. **Gluing via partition of unity.** The global result assembles these local pieces by showing that the sheaf of purely derived Lagrangian foliations is a **soft sheaf**. In topology, a sheaf is soft when its local sections can always be patched together globally using partitions of unity, which is precisely what guarantees global sections exist.

The Hausdorff condition on the space of classical points is doing real work here: it ensures the topological machinery for constructing partitions of unity applies.

One nice feature of the approach is that the strictification result works for homotopically closed forms that aren't necessarily symplectic. When passing from a derived scheme to a derived stack (say, by quotienting by a group action) the symplectic structure lives on the quotient while the scheme underneath carries only a homotopically closed form. The authors' framework handles this intermediate situation, which is what makes the result applicable to the physically relevant case of moduli spaces defined as quotient stacks.

## Why It Matters

The motivating application comes from the geometry of **Calabi-Yau 4-folds**: complex 4-dimensional manifolds with vanishing first Chern class, the setting for certain compactifications in string theory. Donaldson and Thomas proposed using the top holomorphic form on such a manifold to define anti-self-dual instantons, discarding some curvature conditions to obtain a determined elliptic system. The moduli spaces of SU(4)-connections and Spin(7)-instantons (the latter using octonionic geometry) turn out to be set-theoretically isomorphic.

The program initiated by Dominic Joyce aims to replicate this correspondence in algebraic geometry, obtaining compactified moduli spaces with **virtual fundamental classes**, the tools needed to define enumerative invariants that count instantons rigorously with correct signs. The -2-shifted symplectic structure is central to this program. A globally defined Lagrangian distribution means the relevant moduli space can be written as a derived critical locus of a degree -1 potential globally, not just locally. That is the algebraic-geometric analog of the gauge-theoretic structure making Spin(7) instanton theory tractable.

This opens a concrete path toward computing Donaldson-Thomas type invariants for Calabi-Yau 4-folds, a problem at the frontier of both mathematics and mathematical physics. It also shows how homotopy-algebraic techniques can resolve genuinely global geometric problems that classical methods cannot touch.

> **Bottom Line:** By proving that Lagrangian distributions on -2-shifted symplectic derived schemes are globally constructible, this work provides the geometric foundation needed to rigorously define and compute instanton invariants on Calabi-Yau 4-folds, a major step in the Joyce program connecting algebraic geometry to gauge theory.

## IAIFI Research Highlights

- **Interdisciplinary Achievement:** This work connects modern derived algebraic geometry with the physics of string compactifications, translating gauge-theoretic constructions involving Spin(7)-instantons into the language of homotopy algebra and shifted symplectic structures.

- **Impact on Artificial Intelligence:** The strictification and gluing techniques developed here, reconciling locally-defined homotopy-coherent data into globally consistent structures, address a mathematical problem that has structural analogues in machine learning, where locally trained representations must be unified into coherent global models.

- **Impact on Fundamental Interactions:** The results build out the mathematical infrastructure for defining Donaldson-Thomas invariants on Calabi-Yau 4-folds, contributing to the mathematical foundations of string theory and the geometry of moduli spaces in high-energy physics.

- **Outlook and References:** Future work will apply these global Lagrangian distributions to construct virtual fundamental classes for Spin(7)-instanton moduli spaces in algebraic geometry, completing the correspondence with gauge-theoretic invariants; see the full paper [arXiv:1908.00651](https://arxiv.org/abs/1908.00651).

## Original Paper Details
- **Title:** Strictification and gluing of Lagrangian distributions on derived schemes with shifted symplectic forms
- **arXiv ID:** [1908.00651](https://arxiv.org/abs/1908.00651)
- **Authors:** Dennis Borisov, Ludmil Katzarkov, Artan Sheshmani, Shing-Tung Yau
- **Abstract:** A strictification result is proved for isotropic distributions on derived schemes equipped with negatively shifted homotopically closed $2$-forms. It is shown that any derived scheme over $\mathbb{C}$ equipped with a $-2$-shifted symplectic structure, and having a Hausdorff space of classical points, admits a globally defined Lagrangian distribution as a dg $\mathbb{C}^{\infty}$-manifold.
