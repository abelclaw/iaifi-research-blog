---
abstract: We compute the gravitational action of a free massive Majorana fermion coupled
  to two-dimensional gravity on compact Riemann surfaces of arbitrary genus. The structure
  is similar to the case of the massive scalar. The small-mass expansion of the gravitational
  yields the Liouville action at zeroth order, and we can identify the Mabuchi action
  at first order. While the massive Majorana action is a conformal deformation of
  the massless Majorana CFT, we find an action different from the one given by the
  David-Distler-Kawai (DDK) ansatz.
arxivId: '2308.08342'
arxivUrl: https://arxiv.org/abs/2308.08342
authors:
- Corinne de Lacroix
- Harold Erbin
- Vincent Lahoche
concepts:
- majorana fermion
- quantum field theory
- liouville gravity
- conformal field theory
- spectral methods
- functional determinant
- mabuchi action
- renormalization
- symmetry breaking
- effective field theory
- string theory
figures: []
pdfUrl: https://arxiv.org/pdf/2308.08342v2
published: '2023-08-16T13:07:51+00:00'
theme: Theoretical Physics
title: Gravitational action for a massive Majorana fermion in 2d quantum gravity
wordCount: 1219
---

## The Big Picture

Imagine trying to understand the ocean by first mastering a swimming pool. That's roughly the strategy physicists use when studying quantum gravity in two dimensions: strip the problem down to something tractable, solve it completely, and extract lessons that might illuminate the full four-dimensional mystery. Gravity in 4D is ferociously hard. The equations spiral into uncontrollable infinities, and no one has found a fully consistent quantum version. Drop two dimensions, and the math becomes manageable.

In 2D, all the ways a geometry can vary collapse to a single adjustable field called the **Liouville field**, named after the 19th-century mathematician. The central question: how do quantum particles living on this flexible 2D surface respond to changes in its shape? That response is encoded in a formula called the **gravitational action**.

For the simplest particles, those whose behavior looks identical at every scale (a property called **conformal symmetry**), this was solved decades ago. But the real world contains massive particles, and mass breaks scale-invariance. A new paper by de Lacroix, Erbin, and Lahoche ([arXiv:2308.08342](https://arxiv.org/abs/2308.08342)) extends the story to the next-simplest case: a free massive **Majorana fermion**, a particle that is its own antiparticle.

What they find is surprising. A widely used recipe called the **DDK ansatz**, developed by David, Distler, and Kawai (an "ansatz" being a physicist's educated guess), gives the wrong answer. The exact result simply doesn't match.

> **Key Insight:** When a massive Majorana fermion couples to 2D quantum gravity, its gravitational action cannot be captured by the standard DDK construction, challenging a cornerstone assumption in how physicists handle non-conformal matter in 2D gravity.

## How It Works

The paper's central task is computing a **functional determinant**: the quantum mechanical product over all vibrational modes of the fermion field, evaluated on a curved surface. Think of it like computing the harmonic content of a drum's resonances, except the drum is a curved 2D surface, the vibrations are fermionic quantum fields, and the geometry itself is part of what you're solving for.

The starting point is the **Dirac operator**, the differential equation governing how fermions move on a curved surface, evaluated on a compact Riemann surface of arbitrary genus. These topological surfaces range from a sphere (genus 0) to a torus (genus 1) to more complex multi-handled shapes. The Majorana condition means the fermion carries half the degrees of freedom of a generic complex spinor, which makes the functional integral delicate to define correctly. The authors establish it rigorously through a careful mode expansion.

The step-by-step logic:

1. **Write the classical action** for a massive Majorana fermion on a curved surface with metric $g_{\mu\nu}$.
2. **Decompose the metric** into a fixed background $\hat{g}_{\mu\nu}$ and a conformal factor $e^{2\sigma}$, the Liouville field.
3. **Expand the fermion field** in eigenmodes of the Dirac operator. The functional integral becomes a product over eigenvalues, a zeta-regulated determinant.
4. **Track how this determinant changes** under Weyl transformations (rescalings of the geometry). This variation is the gravitational action.

The key technical tool is the **spectral zeta function** $\zeta(s)$, a generalization of the Riemann zeta function that regularizes the otherwise infinite product of eigenvalues. A critical complication arises from **zero-modes** of the Dirac operator: eigenstates with eigenvalue zero that represent field configurations costing no energy. These must be handled separately, and their count depends on surface topology through the **Atiyah-Singer index theorem**, a deep result linking quantum field theory to geometry.

For small but nonzero fermion mass $m$, the gravitational action admits a systematic expansion in powers of $m^2$. The zeroth-order term recovers the classic **Liouville action**, as expected since a massless Majorana fermion is a conformal field theory with central charge $c = 1/2$ (the Ising model universality class). The first-order term reveals the **Mabuchi action**, a geometric functional originally defined by mathematicians studying Kähler metrics. This same Mabuchi term had already appeared in the scalar field calculation. Its reappearance here suggests it's a universal feature of massive matter coupled to 2D gravity, not an artifact of bosonic fields.

## Why It Matters

The disagreement with the DDK ansatz is the headline result. Proposed in the late 1980s, the DDK ansatz offered a convenient recipe: when you deform a conformal field theory by adding a mass or coupling, write down the gravitational action by dressing the perturbation with a specific power of the Liouville field. This works beautifully for pure Liouville theory and its conformal bootstrap formulation. But the present calculation shows it fails for a massive Majorana fermion.

The deeper reason is worth understanding. The DDK construction assumes you can factorize the functional integral of the Liouville field from the matter integral, treating geometry and particles as independent. For a truly non-conformal theory, this assumption breaks down: geometry and matter fluctuations are entangled in a way the ansatz cannot capture.

The massive Majorana calculation makes this concrete with an exactly solvable model, providing a clean counterexample where the precise error can be diagnosed. This raises immediate questions. What systematic construction replaces the DDK recipe in the non-conformal regime? How general is the breakdown? The appearance of the Mabuchi action across multiple independent calculations hints at a deeper geometric structure, one potentially connecting mathematical results on optimal transport and Kähler geometry with physics on string worldsheets.

> **Bottom Line:** The gravitational action for a massive Majorana fermion in 2D quantum gravity differs from what the DDK ansatz predicts, exposing a fundamental limitation of that construction and pointing toward new mathematical structures, including the Mabuchi functional, that govern how massive matter couples to curved geometries.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects structures from complex geometry (the Mabuchi functional, Riemann surface theory, spectral zeta functions) with foundational questions in quantum gravity and string theory, sitting squarely at the intersection of mathematical physics and fundamental interactions that IAIFI is built to explore.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The spectral and geometric methods developed here, including zeta-function regularization and mode expansion on curved manifolds, have parallels in understanding the geometry of neural network parameter spaces and machine learning on curved feature manifolds.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper provides the first complete, exact gravitational action for a massive Majorana fermion on compact Riemann surfaces of arbitrary genus. It shows that the DDK ansatz fails for non-conformal matter and identifies the Mabuchi action as a universal correction at first order in mass.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending the computation to non-minimally coupled fermions, understanding the full resummation of the mass expansion, and investigating whether the Mabuchi action plays a systematic role across all massive matter theories. The paper is available at [arXiv:2308.08342](https://arxiv.org/abs/2308.08342).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Gravitational action for a massive Majorana fermion in 2d quantum gravity</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2308.08342</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Corinne de Lacroix", "Harold Erbin", "Vincent Lahoche"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We compute the gravitational action of a free massive Majorana fermion coupled to two-dimensional gravity on compact Riemann surfaces of arbitrary genus. The structure is similar to the case of the massive scalar. The small-mass expansion of the gravitational yields the Liouville action at zeroth order, and we can identify the Mabuchi action at first order. While the massive Majorana action is a conformal deformation of the massless Majorana CFT, we find an action different from the one given by the David-Distler-Kawai (DDK) ansatz.</span></div></div>
</div>
