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
wordCount: 1150
---

## The Big Picture

Imagine cataloging every possible way a soap bubble can form inside a larger container — not just the stable final shapes, but all the in-between states, the quivers and distortions that arise during formation. Classical geometry handles the stable endpoints. But modern physics, especially string theory, demands something richer: a catalog that tracks the entire history of how those shapes come to be. That's the challenge at the heart of this paper by Dennis Borisov, Ludmil Katzarkov, and Artan Sheshmani.

The objects under study are **Quot-schemes** — classical geometric structures that act as master inventories, listing every possible way to "cut down" one mathematical object by another. Introduced decades ago, Quot-schemes are workhorses of algebraic geometry — the branch of mathematics studying shapes defined by polynomial equations — encoding the "space of all possible configurations" in a precise, computable form.

The problem is that classical Quot-schemes are too rigid. They record only final configurations — the stable bubble shapes — but miss the rich information about *how* shapes deform and transform into one another. This deformation history is exactly what physicists need when studying string theory on **Calabi-Yau manifolds**, the six-dimensional curved spaces central to modern theoretical physics.

Borisov, Katzarkov, and Sheshmani prove that **derived Quot-stacks** — upgraded versions of Quot-schemes that track full deformation history — can be captured by concrete objects called **dg manifolds of finite type**. "Representable" means the abstract catalog isn't just a useful fiction: it corresponds to a specific, tangible geometric object that mathematicians can work with and compute on directly.

> **Key Insight:** The derived Quot-stack, which encodes all higher-order geometric data about quotients of sheaves, is not just a formal abstraction — it can be represented by a differential graded manifold, a concrete geometric object that is computationally tractable and structurally rigid.

## How It Works

The proof strategy is elegant. The authors begin with a simple example: a one-dimensional vector space *N* sitting inside a larger space *M*, with a group action that scales *N*. You can "divide out" by this symmetry in three ways:

- An **algebraic quotient** — abstract, coordinate-free
- A **geometric quotient** — the classical picture
- A **partial quotient** — the total space of a line bundle over projective space

All three are **weakly equivalent** — they encode identical underlying geometric information, the way a map and a satellite photo of the same city contain the same data in different forms. This toy example seeds the entire proof.

The core construction proceeds in three steps:

1. For each finite stretch [a, t], construct a **dg manifold** W[a,t] — a smooth scheme enhanced by a differential graded structure — that solves the derived moduli problem over that stretch.
2. As t grows, these dg manifolds form a sequence connected by **fibrations** (maps that behave like fiber bundle projections).
3. The derived Quot-scheme is the **homotopy limit** of this sequence — the mathematical destination that all approximations converge toward, like a numerical sequence approaching a fixed point.

The catch: the morphisms between the W[a,t] are **projective** (involving ratios, like coordinates on a sphere) rather than **affine** (involving direct coordinates, like ordinary Cartesian space). This makes taking the limit inside the category of dg manifolds impossible.

The authors' key move is to reformulate the problem. Instead of starting with Grassmannians — which produce projective morphisms — they begin with **affine deformation problems** derived via **Koszul duality**, a technique that translates between two equivalent encodings of the same geometric structure, applied here to **dg Lie algebras** that capture the infinitesimal symmetries of a space.

The critical technical lemma — Proposition 2 — shows that injectivity of the module map N → M in a sufficiently long stretch [a, b] automatically forces injectivity everywhere once the **Maurer-Cartan equations** (the governing equations of deformation theory) are satisfied. A finite amount of data controls an infinite structure.

With this, the authors construct a parallel sequence of dg schemes using algebraic (affine) quotients that is weakly equivalent to the original sequence but now admits a limit inside the category of dg manifolds. The three quotient types form a triangle of weak equivalences, and the authors navigate between them to extract exactly the representability they need.

The result: the homotopy limit is not merely a derived stack in some abstract sense, but is concretely represented by a dg manifold of **finite type** — built from finitely many pieces, each a smooth classical space with a finite-dimensional differential graded enhancement.

## Why It Matters

This result lives at a crossroads of mathematics with deep implications for theoretical physics. **Shifted symplectic structures** — a far-reaching generalization of classical symplectic geometry developed by Pantev, Toën, Vaquié, and Vezzosi — are known to exist on derived moduli spaces of sheaves on Calabi-Yau manifolds. These structures are the mathematical backbone of topological quantum field theories and string theory compactifications. But to work with them computationally, you need the moduli spaces represented by concrete geometric objects, not just abstract stacks.

This paper provides exactly that foundation for Quot-type moduli. The distinction matters: any dg manifold defines a derived scheme, but not vice versa. A dg manifold of finite type is a far stronger, more tractable object. Proving the derived Quot-stack satisfies this — requiring, as the authors note, a "strict embedding into projective space" — is genuinely non-trivial.

Future work, building directly on this foundation, aims to construct shifted symplectic structures explicitly on these dg manifolds, connecting to enumerative invariants — the counts of geometric objects that appear in string theory as physical observables.

> **Bottom Line:** Borisov, Katzarkov, and Sheshmani prove that derived Quot-schemes, the homotopically enriched moduli spaces central to modern mathematical physics, are concretely representable by dg manifolds of finite type — opening the door to explicit computation of shifted symplectic structures on Calabi-Yau moduli spaces.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges advanced algebraic geometry (derived algebraic geometry, dg manifolds) with the mathematical foundations of string theory and quantum field theory, providing tools necessary for computing invariants on Calabi-Yau manifolds relevant to fundamental physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The structural results here — particularly the use of Koszul duality and A∞-algebra to tame infinite-dimensional problems via finite approximations — offer conceptual frameworks relevant to how AI systems might represent and reason about continuous, high-dimensional moduli spaces.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By establishing that derived Quot-stacks are representable by concrete dg manifolds, this work provides the rigorous geometric foundation needed to compute shifted symplectic structures on sheaf moduli spaces, which are directly tied to topological invariants in string theory compactifications.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The next step is to explicitly construct shifted symplectic forms on these dg manifold representatives, connecting to enumerative geometry and Donaldson-Thomas theory; the full program is detailed in the companion paper and this work (see arXiv for the series by Borisov, Katzarkov, and Sheshmani).</span></div></div>
</div>
