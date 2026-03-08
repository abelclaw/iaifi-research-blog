---
abstract: We study the complex structure moduli dependence of the scalar Laplacian
  eigenmodes for one-parameter families of Calabi-Yau $n$-folds in P^{n+1}. It was
  previously observed that some eigenmodes get lighter while others get heavier as
  a function of these moduli, which leads to eigenvalue crossing. We identify the
  cause for this behavior for the torus. We then show that at points in a sublocus
  of complex structure moduli space where Laplacian eigenmodes cross, the torus has
  complex multiplication. We speculate that the generalization to arbitrary Calabi-Yau
  manifolds could be that level crossing is related to rank one attractor points.
  To test this, we compute the eigenmodes numerically for the quartic K3 and the quintic
  threefold, and match crossings to CM and attractor points in these varieties. To
  quantify the error of our numerical methods, we also study the dependence of the
  numerical spectrum on the quality of the Calabi-Yau metric approximation, the number
  of points sampled from the Calabi-Yau variety, the truncation of the eigenbasis,
  and the the distance from degeneration points in complex structure moduli space.
arxivId: '2304.00027'
arxivUrl: https://arxiv.org/abs/2304.00027
authors:
- Hamza Ahmed
- Fabian Ruehle
concepts:
- eigenvalue decomposition
- complex multiplication
- attractor points
- string theory
- calabi-yau moduli
- spectral methods
- group theory
- physics-informed neural networks
- symmetry preservation
- monte carlo methods
- conformal field theory
figures:
- /iaifi-research-blog/figures/2304_00027/figure_1.png
- /iaifi-research-blog/figures/2304_00027/figure_2.png
- /iaifi-research-blog/figures/2304_00027/figure_3.png
pdfUrl: https://arxiv.org/pdf/2304.00027v1
published: '2023-03-31T18:00:00+00:00'
theme: Theoretical Physics
title: Level Crossings, Attractor Points and Complex Multiplication
wordCount: 937
---

## The Big Picture

Imagine tuning a guitar, but as you tighten one string, another seemingly unrelated one shifts pitch in response. Now scale that up: the strings are vibrational patterns on a six-dimensional geometric space curled up at every point in the universe, and the tuning knob controls the shape of reality itself.

In string theory, the extra dimensions aren't empty space. They're folded into intricate geometric objects called **Calabi-Yau manifolds**, and the shapes of these spaces determine observable physics: particle masses, symmetries, the forces of nature.

As you vary the shape parameters (called **complex structure moduli**) of these spaces, the spectrum of vibrational frequencies changes. Sometimes two frequencies gradually approach each other and, at a precise moment, swap. This phenomenon, known as **level crossing**, had been observed numerically, but nobody knew why it happened or what made the crossing points special.

Ahmed and Ruehle set out to answer exactly that question. What they found connects abstract number theory to black hole physics in a way nobody had anticipated.

> **Key Insight:** Level crossings in Calabi-Yau Laplacian spectra occur at points in moduli space with a number-theoretic property called complex multiplication, the same special points that govern the behavior of extremal black holes in string theory.

## How It Works

The researchers started with the simplest case: a **torus** (a CY 1-fold, mathematically a cubic curve in projective space P²). Everything about the torus can be computed analytically, no approximations needed. That made it the right place to understand level crossings before moving to harder cases.

A torus's shape is encoded in a single complex number τ, its **complex structure modulus**. As τ varies, the eigenmodes of the **scalar Laplacian** (the differential operator governing wave behavior on the surface) shift their eigenvalues. The researchers tracked how each eigenmode transforms as the torus's algebraic description changes.

What they found: eigenmodes divide into symmetry classes called **irreducible representations**, distinct families of vibrations that don't normally mix. As τ changes, eigenvalues from different families can approach each other, and at specific values of τ, they cross.

![Figure 1](/iaifi-research-blog/figures/2304_00027/figure_1.png)

Those crossing points aren't random. They correspond to values of τ where the torus has **complex multiplication (CM)**, a special algebraic property where the endomorphism ring contains more than just the integers. In plain terms, the torus at these points carries an extra symmetry visible only through number theory. CM tori include familiar examples like τ = i (the square torus) and τ = e^(2πi/3) (the hexagonal torus).

With this analytic foundation in hand, the team moved to higher dimensions, where numerical computation becomes essential:

- **Quartic K3 surface** (CY 2-fold): A complex 2-dimensional surface where the Picard rank, a count of algebraic cycles, jumps from 19 to 20 at special CM points.
- **Quintic threefold** (CY 3-fold): A complex 3-dimensional manifold with 101 complex structure parameters. The paper studies the one-parameter subfamily with enhanced symmetry.

Analytic metrics don't exist for these cases. The team used **neural network-approximated Ricci-flat metrics**, building on work pioneered at IAIFI, to numerically compute the Laplacian eigenspectrum. They characterized numerical errors carefully, varying metric approximation quality, sampling density, eigenbasis truncation, and proximity to degeneration points.

![Figure 2](/iaifi-research-blog/figures/2304_00027/figure_2.png)

For the K3, crossings matched known CM points where the Picard rank jumps. For the quintic, they matched **rank one attractor points**, special moduli values where BPS black hole flows in string theory converge. This is the paper's most striking result: the same points governing the thermodynamics of extremal black holes in 4D supergravity also mark where vibrational modes on the compactification manifold exchange identity.

![Figure 3](/iaifi-research-blog/figures/2304_00027/figure_3.png)

## Why It Matters

Why should we care? Attractor points in Calabi-Yau moduli space are tied to BPS black hole stability and the structure of the string landscape (the vast space of possible string theory vacua). A direct spectral signature of these points creates a new way to find them: instead of hunting for attractor points through algebraic geometry, you could detect them through numerical spectroscopy of the Laplacian.

The work also pushes forward the use of machine learning for rigorous calculations in string theory. The careful error analysis across multiple approximation schemes shows that neural network-based metric approximations are accurate enough to identify subtle spectral phenomena.

Several open questions remain. Does the crossing-to-attractor connection hold for arbitrary multi-parameter Calabi-Yau families? Can spectral methods become a systematic tool for mapping out string vacua? The conjectured link to rank one attractor points, rather than CM points directly, still awaits a proof.

> **Bottom Line:** Level crossings in Calabi-Yau spectra are a spectral fingerprint of attractor points, extraordinary geometric locations tied to black hole physics and number theory alike. Ahmed and Ruehle turn a puzzling numerical observation into a precise conjecture, backed by analytic proof for the torus and strong numerical evidence for K3 and quintic geometries.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects algebraic geometry, number theory, black hole physics, and machine learning-based numerical methods, bringing together the kinds of cross-disciplinary tools that define IAIFI's research program.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper rigorously benchmarks neural network-approximated Ricci-flat metrics as a tool for detecting subtle spectral phenomena in curved geometry, demonstrating the reliability of ML methods for mathematical physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By connecting Laplacian level crossings to rank one attractor points and complex multiplication in Calabi-Yau manifolds, this work provides a new spectral probe of the string landscape and the geometry underlying 4D supergravity theories.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend this conjecture to multi-parameter Calabi-Yau families and provide a computational shortcut for locating attractor points; the full paper is available at [arXiv:2304.00027](https://arxiv.org/abs/2304.00027).</span></div></div>
</div>
