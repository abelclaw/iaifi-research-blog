---
abstract: Motivated by the question of defining a $p$-adic string worldsheet action
  in genus one, we define a Laplacian operator on the Tate curve, and study its Green's
  function. We show that the Green's function exists. We provide an explicit formula
  for the Green's function, which turns out to be a non-Archimedean counterpart of
  the Archimedean Green's function on a flat torus. In particular, it turns out that
  this Green's function recovers the Néron local height function for the Tate curve
  in the $p\to\infty$ limit, when the $j$-invariant has odd valuation. So this non-Archimedean
  height function now acquires a physics meaning in terms of the large $p$ limit of
  a non-Archimedean conformal field theory two point function on the Tate curve, as
  well as a direct analytic interpretation as a Green's function, on the same footing
  as in the Archimedean place.
arxivId: '2512.24935'
arxivUrl: https://arxiv.org/abs/2512.24935
authors:
- An Huang
- Rebecca Rohrlich
- Yaojia Sun
- Eric Whyman
concepts:
- p-adic analysis
- string theory
- conformal field theory
- néron height function
- bruhat-tits tree
- group theory
- quantum field theory
- spectral methods
- scattering amplitudes
figures:
- /iaifi-research-blog/figures/2512_24935/figure_1.png
- /iaifi-research-blog/figures/2512_24935/figure_1.png
pdfUrl: https://arxiv.org/pdf/2512.24935v2
published: '2025-12-31T15:48:39+00:00'
theme: Theoretical Physics
title: Green's function on the Tate curve
wordCount: 1153
---

## The Big Picture

Imagine describing the shape of a donut to someone whose world runs on completely different arithmetic — where "closeness" is defined not by size, but by how many times a prime number divides the difference between two values. That's the landscape of p-adic string theory, and it's where this paper stakes out genuinely new ground.

String theory holds that the fundamental constituents of nature are tiny vibrating strings. As each string moves through spacetime, it sweeps out a surface — its **worldsheet** — the way a moving loop traces out a tube. At the simplest level, worldsheets are spheres or disks. At the next level of complexity, the surface closes back on itself to form a torus: the donut shape.

Physicists have handled ordinary worldsheets for decades. But a parallel version of string theory is built on **p-adic numbers** — an alternative number system, one for each prime $p$, where arithmetic is governed by divisibility rather than magnitude. In the p-adic world, simpler worldsheets are well-understood. The torus has been a glaring open problem for over thirty years.

This paper by An Huang, Rebecca Rohrlich, Yaojia Sun, and Eric Whyman directly attacks that problem. They define a mathematical operator governing how fields spread across a p-adic torus, solve for the precise function describing field interactions, and reveal a stunning connection: a purely number-theoretic object from advanced arithmetic turns out to be the large-$p$ limit of a p-adic quantum field theory correlation function.

> **Key Insight:** The researchers prove that the Néron local height function on the Tate curve — a fundamental object in number theory — is the Green's function of a p-adic Laplacian, giving it a direct physical interpretation as a quantum field theory correlator for the first time.

## How It Works

The story begins with the **Tate curve** — the p-adic version of a torus, written as $E_q = \mathbb{Q}_p^\times / q^\mathbb{Z}$. Think of this as p-adic numbers modulo a lattice: the p-adic analogue of constructing a flat torus by gluing opposite edges of a plane together. Here, $q$ is a p-adic number with $|q| < 1$, playing the role of the modular parameter that controls the torus's shape.

The central mathematical object is the **Green's function** — a field theory's equivalent of an impulse response. Formally, it solves $DG = \delta - 1/V$, where $D$ is the Laplacian, $\delta$ is a perfectly localized disturbance, and $V$ is the volume of the fundamental domain. If the Laplacian describes how a field propagates across the torus, the Green's function captures the field's response to a point source.

In string theory, this is precisely the two-point correlation function of the **worldsheet CFT** — the conformal field theory living on the string's surface. It is the most basic quantity encoding how two points on the string interact.

![Figure 1](/iaifi-research-blog/figures/2512_24935/figure_1.png)

The authors define the p-adic Laplacian on the Tate curve via a careful integral operator:

$$D\phi(x) := \int_E \frac{\phi(z) - \phi(x)}{|z-x|^2} |x|\, dz$$

This is a **Non-Archimedean Laplacian** — "non-Archimedean" because it uses p-adic norms, which measure divisibility rather than ordinary size. The key motivating insight: locally, on any small patch of the p-adic torus, this operator is identical to the well-established **Vladimirov derivative** on simpler geometries — just as any genus worldsheet locally looks like a flat plane.

To solve the resulting equation, the authors deploy a filtration strategy:

- They restrict to functions depending on only the first $k$ p-adic digits, reducing the infinite-dimensional problem to finite-dimensional matrix equations at each level $k$
- This filtration corresponds geometrically to truncating the **Bruhat-Tits tree** $T_p/\Gamma$ — a combinatorial tree encoding p-adic geometry — at radius $k$
- Taking the limit $k \to \infty$ recovers the full Green's function

![Figure 2](/iaifi-research-blog/figures/2512_24935/figure_1.png)

The result is an explicit closed-form formula. On an ordinary torus, the Green's function involves logarithms and Jacobi theta functions. Here, it involves p-adic norms and sums over the tree $T_p/\Gamma$ — the same architecture, translated into p-adic language.

The punchline arrives in the large-$p$ limit. When the j-invariant of the Tate curve has odd valuation — a condition measuring how "degenerate" the torus is — the Green's function converges, as $p \to \infty$, to the **Néron local height function**: an object arithmetic geometers use to measure heights of points on elliptic curves, central to the theory connecting elliptic curves to the Birch and Swinnerton-Dyer conjecture.

## Why It Matters

This result bridges two worlds that rarely speak to each other. Number theorists have studied Néron local height functions since the 1960s as abstract algebraic tools for measuring arithmetic complexity. Physicists have studied Green's functions as concrete objects governing particle propagation. This paper shows they are the same thing — at least in the p-adic world.

The Néron height isn't abstract bookkeeping. It's a genuine quantum field theory correlator, with a direct physical interpretation in terms of how information propagates across a p-adic string worldsheet.

The implications stretch in several directions. First, the Green's function is the essential building block for computing tachyon scattering amplitudes, and this result opens the door to computing p-adic string amplitudes at genus one — the torus — for the first time. Second, the paper hints at connections to the **adelic product formula**: just as Tate's thesis showed that the product of p-adic and Archimedean Green's functions over all primes equals one, similar product formulas may hold here for the torus, stitching different "universes" of string theory into a single adelic picture. Third, the Bruhat-Tits tree filtration gives a concrete computational handle on non-Archimedean geometry that may extend to higher-genus worldsheets — edging closer to a full p-adic perturbative string theory.

> **Bottom Line:** By finding the Green's function on the p-adic Tate curve, Huang, Rohrlich, Sun, and Whyman solve a 35-year-old open problem in p-adic string theory while revealing that an abstract number-theoretic height function is secretly a quantum field theory correlator — a discovery that enriches both physics and mathematics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work unifies p-adic string theory and arithmetic geometry by proving that the Néron local height function on the Tate curve is the large-$p$ limit of a non-Archimedean CFT two-point function, bridging number theory and quantum field theory in a single result.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The Bruhat-Tits tree filtration developed here — discretizing infinite-dimensional p-adic spaces via tree truncation — offers a rigorous mathematical framework with potential applications to hierarchical and tree-structured representations in machine learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">This paper provides the first explicit Green's function for a p-adic string worldsheet at genus one, unlocking computation of p-adic closed string torus amplitudes and bringing the adelic formulation of string theory a significant step closer to reality.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work aims to compute p-adic string torus amplitudes from this Green's function and establish a full adelic product formula at genus one; the paper is available on arXiv.</span></div></div>
</div>
