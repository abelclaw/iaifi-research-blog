---
abstract: It is proved that derived Quot-schemes, as defined by Ciocan-Fontanine and
  Kapranov, are represented by dg manifolds of finite type. This is the second part
  if a work aimed to analyze shifted symplectic structures on moduli spaces of coherent
  sheaves on Calabi--Yau manifolds. The first part related dg manifolds to derived
  schemes as defined by Toën and Vezzosi.
arxivId: '2312.02815'
arxivUrl: https://arxiv.org/abs/2312.02815
authors:
- Dennis Borisov
- Ludmil Katzarkov
- Artan Sheshmani
concepts:
- derived algebraic geometry
- moduli spaces of sheaves
- dg lie algebras
- maurer-cartan equations
- homotopy limit
- koszul duality
- manifold learning
- group theory
- quantum field theory
- string theory
figures: []
pdfUrl: https://arxiv.org/pdf/2312.02815v1
published: '2023-12-05T14:57:22+00:00'
theme: Foundational AI
title: Shifted symplectic structures on derived Quot-stacks II -- Derived Quot-schemes
  as dg manifolds
wordCount: 1078
---

## The Big Picture

Imagine cataloging every possible way a soap bubble can form inside a larger container. Not just the stable final shapes, but all the in-between states, the quivers and distortions during formation. Classical geometry handles the stable endpoints. Modern physics, especially string theory, demands something richer: a catalog that tracks the entire history of how those shapes come to be.

The objects under study are **Quot-schemes**, classical geometric structures that act as master inventories, listing every possible way to "cut down" one mathematical object by another. Introduced decades ago, Quot-schemes are workhorses of algebraic geometry (the branch of mathematics studying shapes defined by polynomial equations), encoding the space of all possible configurations in a precise, computable form.

But classical Quot-schemes are too rigid. They record only final configurations and miss the information about *how* shapes deform and transform into one another. This deformation history is exactly what physicists need when studying string theory on **Calabi-Yau manifolds**, the six-dimensional curved spaces at the center of modern theoretical physics.

In this paper ([arXiv:2312.02815](https://arxiv.org/abs/2312.02815)), Borisov, Katzarkov, and Sheshmani prove that **derived Quot-stacks**, upgraded versions of Quot-schemes that track full deformation history, can be captured by concrete objects called **dg manifolds of finite type**. "Representable" here means the abstract catalog isn't a useful fiction: it corresponds to a specific geometric object you can work with and compute on directly.

> **Key Insight:** The derived Quot-stack, which encodes all higher-order geometric data about quotients of sheaves, is not just a formal abstraction. It can be represented by a differential graded manifold, a concrete geometric object that is computationally tractable and structurally rigid.

## How It Works

The authors start with a toy example: a one-dimensional vector space *N* sitting inside a larger space *M*, with a group action that scales *N*. You can "divide out" by this symmetry in three ways:

- An **algebraic quotient**, abstract and coordinate-free
- A **geometric quotient**, the classical picture
- A **partial quotient**, the total space of a line bundle over projective space

All three are **weakly equivalent**: they encode identical underlying geometric information, the way a map and a satellite photo of the same city contain the same data in different forms. This toy example seeds the entire proof.

The core construction has three steps. First, for each finite stretch [a, t], construct a **dg manifold** W[a,t], a smooth scheme enhanced by a differential graded structure that solves the derived moduli problem over that stretch. Second, as t grows, these dg manifolds form a sequence connected by **fibrations** (maps that behave like fiber bundle projections). Third, the derived Quot-scheme is the **homotopy limit** of this sequence, the mathematical destination that all approximations converge toward, like a numerical sequence approaching a fixed point.

Here's the catch: the morphisms between the W[a,t] are **projective** (involving ratios, like coordinates on a sphere) rather than **affine** (involving direct coordinates, like ordinary Cartesian space). That makes taking the limit inside the category of dg manifolds impossible.

The authors' solution is to reformulate the problem. Instead of starting with Grassmannians, which produce projective morphisms, they begin with **affine deformation problems** derived via **Koszul duality**, a technique that translates between two equivalent encodings of the same geometric structure. Here it is applied to **dg Lie algebras** that capture the infinitesimal symmetries of a space.

The critical technical lemma (Proposition 2) shows that injectivity of the module map N → M in a sufficiently long stretch [a, b] automatically forces injectivity everywhere once the **Maurer-Cartan equations** are satisfied. A finite amount of data controls an infinite structure.

With this in hand, the authors construct a parallel sequence of dg schemes using algebraic (affine) quotients. This new sequence is weakly equivalent to the original but now admits a limit inside the category of dg manifolds. The three quotient types form a triangle of weak equivalences, and the authors navigate between them to extract the representability they need.

The payoff: the homotopy limit is not merely a derived stack in some abstract sense, but is concretely represented by a dg manifold of **finite type**, built from finitely many pieces, each a smooth classical space with a finite-dimensional differential graded enhancement.

## Why It Matters

**Shifted symplectic structures**, a far-reaching generalization of classical symplectic geometry developed by Pantev, Toën, Vaquié, and Vezzosi, are known to exist on derived moduli spaces of sheaves on Calabi-Yau manifolds. These structures are the mathematical backbone of topological quantum field theories and string theory compactifications. But to actually compute with them, you need the moduli spaces represented by concrete geometric objects, not just abstract stacks.

This paper supplies that foundation for Quot-type moduli. The distinction matters: any dg manifold defines a derived scheme, but not vice versa. A dg manifold of finite type is a far stronger, more tractable object. Proving the derived Quot-stack has this property requires, as the authors note, a "strict embedding into projective space," and the argument is non-trivial.

The next step in the program is to construct shifted symplectic structures explicitly on these dg manifolds, connecting to enumerative invariants, the counts of geometric objects that appear in string theory as physical observables.

> **Bottom Line:** Borisov, Katzarkov, and Sheshmani prove that derived Quot-schemes, the homotopically enriched moduli spaces at the center of modern mathematical physics, are concretely representable by dg manifolds of finite type. This clears the path toward explicit computation of shifted symplectic structures on Calabi-Yau moduli spaces.

---

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects advanced algebraic geometry (derived algebraic geometry, dg manifolds) with the mathematical foundations of string theory and quantum field theory, producing tools needed to compute invariants on Calabi-Yau manifolds relevant to fundamental physics.

- **Impact on Artificial Intelligence:** The structural results here, particularly the use of Koszul duality and A∞-algebra to tame infinite-dimensional problems via finite approximations, offer conceptual frameworks for how AI systems might represent and reason about continuous, high-dimensional moduli spaces.

- **Impact on Fundamental Interactions:** By establishing that derived Quot-stacks are representable by concrete dg manifolds, this work provides the rigorous geometric foundation needed to compute shifted symplectic structures on sheaf moduli spaces, which are tied to topological invariants in string theory compactifications.

- **Outlook and References:** The next step is to explicitly construct shifted symplectic forms on these dg manifold representatives, connecting to enumerative geometry and Donaldson-Thomas theory. The full program is detailed in the companion paper and this work; see [arXiv:2312.02815](https://arxiv.org/abs/2312.02815) for the series by Borisov, Katzarkov, and Sheshmani.
