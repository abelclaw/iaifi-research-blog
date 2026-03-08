---
abstract: We generalize the auxiliary field deformations of the principal chiral model
  (PCM) introduced in arXiv:2405.05899 and arXiv:2407.16338 to sigma models whose
  target manifolds are symmetric or semi-symmetric spaces, including a Wess-Zumino
  term in the latter case. This gives rise to a new infinite family of classically
  integrable $\mathbb{Z}_2$ and $\mathbb{Z}_4$ coset models of the form which are
  of interest in applications of integrability to worldsheet string theory and holography.
  We demonstrate that every theory in this infinite class admits a zero-curvature
  representation for its equations of motion by exhibiting a Lax connection.
arxivId: '2409.05704'
arxivUrl: https://arxiv.org/abs/2409.05704
authors:
- Daniele Bielli
- Christian Ferko
- Liam Smith
- Gabriele Tartaglino-Mazzucchelli
concepts:
- integrable deformations
- lax connection
- string theory
- wess-zumino term
- quantum field theory
- lagrangian methods
- group theory
- symmetry breaking
- conformal field theory
figures: []
pdfUrl: https://arxiv.org/pdf/2409.05704v2
published: '2024-09-09T15:14:31+00:00'
theme: Theoretical Physics
title: Auxiliary Field Deformations of (Semi-)Symmetric Space Sigma Models
wordCount: 1229
---

## The Big Picture

Imagine you're trying to solve a puzzle, but the pieces keep changing shape. Most physical theories work this way: the equations are so complex that exact solutions are essentially impossible. Now imagine a special class of puzzles where, no matter how you twist and deform the pieces, they always snap together perfectly. That's what makes **integrable theories** special, a rare breed of mathematical models that physicists can solve exactly rather than approximately.

**Sigma models** are a family of equations physicists use to describe how fields evolve across space and time. Think of a "field" as something like temperature, a value assigned to every point in space, but more abstract, encoding which state a physical system is in at each location. When the space of possible states has special geometric symmetry, these equations show up everywhere: in materials science, in particle physics, and in the mathematics of vibrating strings thought to underlie quantum gravity.

The trouble is that adding complexity to match real physics usually destroys the mathematical structure that makes these models tractable. A team of physicists from Northeastern University, the University of Queensland, and Chulalongkorn University has now shown that a powerful deformation technique, originally developed for a simpler class of models, extends to a much broader and more physically relevant family. The result is an infinite collection of new integrable theories directly applicable to string theory and **holography** (the idea that a theory of gravity can be exactly equivalent to a simpler theory living on its boundary).

> **Key Insight:** By introducing auxiliary fields (extra mathematical variables that reshape the equations without adding new physical particles) into sigma models on symmetric and semi-symmetric spaces, the researchers construct an infinite family of deformed theories that all remain classically integrable. Each one comes with an explicit Lax connection, a mathematical certificate of solvability.

## How It Works

At the foundation sits the **principal chiral model (PCM)**, a classic integrable sigma model where the field's target space is a Lie group, a mathematical object encoding continuous symmetry (like rotations) in a precise algebraic way. In earlier work, the same team introduced a clever trick: add auxiliary vector fields, extra variables that don't propagate independently but reshape the dynamics when you eliminate them algebraically. The interaction between physical and auxiliary fields is controlled by an arbitrary function, creating not just one deformed theory but an entire family parameterized by your choice of function.

The key question this paper addresses: does this auxiliary field trick work beyond the PCM? The researchers focus on two more general classes of sigma models:

- **Symmetric space sigma models (SSSM):** The target manifold is a coset G/H, a curved space built by "dividing out" a larger symmetry group G by a subgroup H, where a Z₂ symmetry relates the two roles of the group. These arise in string theory on symmetric backgrounds; the sphere S⁵ inside AdS₅ × S⁵ is a classic example.
- **Semi-symmetric space sigma models (sSSSM):** A further generalization with Z₄ symmetry, relevant for the full superstring on anti-de Sitter backgrounds. These models can also carry a **Wess-Zumino (WZ) term**, a topological contribution to the action measuring how the string's worldsheet (the two-dimensional surface it sweeps out as it moves) wraps around the target space.

The construction mirrors the PCM approach but demands more careful handling of the geometry. The group element g takes values in the coset G/H, and the current j = g⁻¹dg decomposes according to the grading of the Lie algebra. Auxiliary fields couple to the graded components, with the deformed action controlled by an arbitrary function E(ν₂, ..., νₙ) of several Lorentz invariants (quantities unchanged under boosts or rotations) built from those auxiliary fields.

The central technical achievement is proving that integrability survives this deformation. In integrable theories, the hallmark of exact solvability is a **Lax connection**: a pair of matrices L±(λ) depending on a free complex parameter λ (the spectral parameter) whose zero-curvature condition is exactly equivalent to the equations of motion. It works like a master key. Exhibit a Lax connection, and you've proven the theory is exactly solvable.

For both the SSSM and the sSSSM with WZ term, the authors explicitly construct Lax connections for the deformed theories. The connection takes the form familiar from undeformed models, with original current components replaced by modified versions depending on the auxiliary fields. Verifying that the zero-curvature condition reproduces the equations of motion requires careful algebra (detailed calculations fill two substantial appendices) but the structure works out cleanly in both cases.

## Why It Matters

The direct application is to string theory. Many string backgrounds relevant to the **AdS/CFT correspondence**, the duality between string theory in curved spacetime and gauge theories on its boundary, are described by exactly the class of sigma models studied here.

The superstring on AdS₅ × S⁵ is a Z₄ coset model with a WZ term. So is the string on AdS₄ × CP³ and AdS₃ × S³ × T⁴. The new infinite family of integrable deformations gives theorists a vast toolbox: a collection of exactly solvable models neighboring the physically important ones, useful for understanding how integrability works, what observables depend on it, and how spectra change under deformation.

There's a broader structural lesson here too. The auxiliary field approach is turning out to be a surprisingly universal language for integrable deformations. It already subsumes the **TT̄ deformation** (driven by the product of stress-energy tensor components) and higher-spin generalizations. Each choice of function E gives a different deformed theory, and the whole infinite family is integrable simultaneously. Connecting this framework to Yang-Baxter deformations, lambda deformations, and T-duality is an active frontier. This paper's extension to semi-symmetric spaces opens those questions directly in the string theory context.

> **Bottom Line:** Auxiliary field deformations, once confined to the simplest integrable sigma models, now extend to the full class of coset models describing superstrings on anti-de Sitter backgrounds, creating an infinite new collection of exactly solvable theories with direct relevance to quantum gravity and holography.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects mathematical physics, string theory, and algebra, using geometric symmetry principles to engineer exactly solvable models with implications for holography and quantum gravity.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper constructs an infinite new family of classically integrable Z₂ and Z₄ coset models with explicit Lax representations, directly expanding the toolkit for studying superstrings on AdS backgrounds and the AdS/CFT correspondence.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending these deformations to full quantum integrability, connecting them to Yang-Baxter and lambda deformations, and probing the spectrum of deformed string theories. The paper is available at [arXiv:2409.05704](https://arxiv.org/abs/2409.05704).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Auxiliary Field Deformations of (Semi-)Symmetric Space Sigma Models</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2409.05704</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Daniele Bielli", "Christian Ferko", "Liam Smith", "Gabriele Tartaglino-Mazzucchelli"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We generalize the auxiliary field deformations of the principal chiral model (PCM) introduced in arXiv:2405.05899 and arXiv:2407.16338 to sigma models whose target manifolds are symmetric or semi-symmetric spaces, including a Wess-Zumino term in the latter case. This gives rise to a new infinite family of classically integrable $\mathbb{Z}_2$ and $\mathbb{Z}_4$ coset models of the form which are of interest in applications of integrability to worldsheet string theory and holography. We demonstrate that every theory in this infinite class admits a zero-curvature representation for its equations of motion by exhibiting a Lax connection.</span></div></div>
</div>
