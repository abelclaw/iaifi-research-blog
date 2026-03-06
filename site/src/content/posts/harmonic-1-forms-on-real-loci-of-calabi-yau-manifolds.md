---
abstract: 'We numerically study whether there exist nowhere vanishing harmonic $1$-forms
  on the real locus of some carefully constructed examples of Calabi-Yau manifolds,
  which would then give rise to potentially new examples of $G_2$-manifolds and an
  explicit description of their metrics. We do this in two steps: first, we use a
  neural network to compute an approximate Calabi-Yau metric on each manifold. Second,
  we use another neural network to compute an approximately harmonic $1$-form with
  respect to the approximate metric, and then inspect the found solution. On two manifolds
  existence of a nowhere vanishing harmonic $1$-form can be ruled out using differential
  geometry. The real locus of a third manifold is diffeomorphic to $S^1 \times S^2$,
  and our numerics suggest that when the Calabi-Yau metric is close to a singular
  limit, then it admits a nowhere vanishing harmonic $1$-form. We explain how such
  an approximate solution could potentially be used in a numerically verified proof
  for the fact that our example manifold must admit a nowhere vanishing harmonic $1$-form.'
arxivId: '2405.19402'
arxivUrl: https://arxiv.org/abs/2405.19402
authors:
- Michael R. Douglas
- Daniel Platt
- Yidi Qi
- Rodrigo Barbosa
concepts:
- calabi-yau metric learning
- g2-manifold construction
- physics-informed neural networks
- string theory
- monte carlo methods
- surrogate modeling
- inverse problems
- equivariant neural networks
- computer-assisted proof
- geometric deep learning
- quantum field theory
figures:
- /iaifi-research-blog/figures/2405_19402/figure_1.png
- /iaifi-research-blog/figures/2405_19402/figure_2.png
- /iaifi-research-blog/figures/2405_19402/figure_3.png
pdfUrl: https://arxiv.org/pdf/2405.19402v2
published: '2024-05-29T18:00:01+00:00'
theme: Theoretical Physics
title: Harmonic $1$-forms on real loci of Calabi-Yau manifolds
wordCount: 1113
---

## The Big Picture

Imagine mapping territory so complex that no formula could describe it. The terrain exists — mathematicians proved that decades ago — but every attempt to write down its coordinates fails. This is the situation physicists face with **Calabi-Yau manifolds**: elegant, curled-up geometric spaces central to string theory, whose defining shape is provably real yet impossible to express analytically. Now imagine that probing one slice of such territory might unlock a new class of even stranger spaces that matter deeply to the leading candidate for a "theory of everything." That's exactly the challenge a team from Harvard, Northeastern, and Imperial College London decided to attack with neural networks.

At stake is a rare object called a **G₂-manifold**: a seven-dimensional curved space with a special geometric structure. These matter because M-theory — the most ambitious framework for unifying all fundamental forces — requires the universe to have extra dimensions too small to observe. Those hidden dimensions must curl into a specific shape, and G₂-manifolds are prime candidates. They are so scarce that mathematicians can count known construction methods on one hand.

A 2021 blueprint by Joyce and Karigiannis showed how to build new G₂-manifolds from Calabi-Yau manifolds — but only if the Calabi-Yau's **real locus** admits a special mathematical object. The real locus is the three-dimensional "shadow" cast by the six-dimensional manifold when restricted to real coordinates. The required object is a **nowhere-vanishing harmonic 1-form**: a smooth vector field pointing in some direction at every point, satisfying a natural equilibrium condition, with no zeros anywhere. Checking whether this can exist requires knowing the Calabi-Yau's geometry precisely — the very thing no one can write down.

This paper uses two stacked neural networks to do what analytic methods cannot: numerically approximate both the geometry and the desired vector field, then use those approximations to detect whether the real thing can exist.

> **Key Insight:** By training neural networks to approximate elusive Calabi-Yau metrics and harmonic 1-forms simultaneously, the authors find numerical evidence for a new conjectural G₂-manifold — only the second such candidate in the literature.

## How It Works

The pipeline has two stages, each powered by a neural network, applied to four carefully chosen example manifolds.

**Stage one: approximating the Calabi-Yau metric.** The team builds on the *bihomogeneous neural network* approach — an architecture designed to respect the symmetries of spaces defined by polynomial equations. A correction to the **Fubini-Study metric** (a natural baseline on projective space) is parametrized and trained to satisfy the **complex Monge-Ampère equation**, whose solution is the true Calabi-Yau metric. This produces a **Ricci-flat** geometry — no intrinsic curvature of its own, like a soap film settling into minimal-energy shape. For **complete intersection manifolds** — spaces carved out by multiple polynomial equations in a higher-dimensional ambient space — the authors extend this approach to handle the more constrained higher-codimension setting.

**Stage two: finding the harmonic 1-form.** A separate network targets the real locus L ⊂ M. Harmonicity on L means the form is both **closed** (zero variation around any loop — no "curl") and **co-closed** (zero divergence), both measured with respect to the pulled-back approximate metric. The network represents the 1-form using a **polynomial basis** restricted to L and minimizes a combined loss using Monte Carlo integration — random sampling of points across the manifold.

The four test cases span a range of topologies:

- **Fermat quintic** — real locus has first Betti number b₁ = 0; no non-trivial 1-forms exist. A control.
- **Quintic** — b₁ = 1, so a harmonic 1-form exists in principle, but classical 3-manifold geometry guarantees it must vanish somewhere. Another control.
- **CICY1 and CICY2** — complete intersections of a quadric and a quartic in ℙ⁵. Real loci are topologically S¹ × S², with b₁ = 1 and no topological obstruction to a nowhere-vanishing 1-form.

![Figure 1](/iaifi-research-blog/figures/2405_19402/figure_1.png)

The critical mathematical contribution is **Corollary 3.8**: if a nowhere-vanishing 1-form exists for an *approximate* metric sufficiently close to solving Monge-Ampère, then a genuine nowhere-vanishing harmonic 1-form for the *true* metric must exist nearby. This transforms a numerical finding into a potential pathway toward a computer-assisted proof.

## Why It Matters

The results validate the approach on both controls. On the Fermat quintic and Quintic, the approximate 1-forms are either identically near-zero or clearly develop zeros — confirming the network isn't inventing structure that isn't there.

On CICY2, something striking emerges: the approximate harmonic 1-form is approximately constant along the S¹ direction and approximately zero along S². This is exactly the pattern expected for a true nowhere-vanishing 1-form on S¹ × S², where the natural candidate is simply the differential of the S¹ coordinate.

![Figure 2](/iaifi-research-blog/figures/2405_19402/figure_2.png)

The authors also observe that the Calabi-Yau metric develops **long necks** near singular limits — regions where the geometry stretches thin as parameters vary. This behavior is analytically guaranteed for hypersurfaces by a 2019 theorem, but was previously unknown for higher-codimension manifolds like CICYs. The neural network simulations provide the first evidence it occurs there too.

![Figure 3](/iaifi-research-blog/figures/2405_19402/figure_3.png)

This work lives at a productive frontier: machine learning not replacing rigorous proof, but guiding mathematical discovery and laying groundwork for **computer-assisted proofs**. The authors are explicit that their approximations are not yet accurate enough to complete a formal proof — but Corollary 3.8 is already in place to make that possible.

As training improves — more compute, better architectures, higher-order polynomial bases — the gap between "numerically suggestive" and "rigorously certified" could close. The result would be the first verified new G₂-manifold construction in years, with direct implications for M-theory compactifications and the landscape of possible extra-dimensional geometries.

> **Bottom Line:** Neural networks can probe Calabi-Yau geometry well enough to find new conjectural G₂-manifolds that classical methods cannot reach — and a rigorous mathematical theorem already shows that sufficiently accurate approximations could become genuine proofs.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses differential geometry, algebraic topology, and deep learning into a single computational framework, using neural networks trained on physical constraints to answer open questions in pure mathematics about G₂-manifolds.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper extends neural network approximation of Calabi-Yau metrics from hypersurfaces to complete intersections of higher codimension, and introduces a polynomial-basis network for computing harmonic differential forms on curved manifolds.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The results provide the second conjectural example in the literature of a Calabi-Yau manifold whose real locus supports a nowhere-vanishing harmonic 1-form — a key ingredient for constructing new seven-dimensional G₂-manifolds relevant to M-theory compactifications.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work with higher-accuracy approximations could transform this numerical evidence into a computer-assisted proof via Corollary 3.8; see arXiv:2501.14048 and the accompanying code at github.com/yidiq7/MLHarmonic-1-form.</span></div></div>
</div>
