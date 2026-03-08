---
abstract: We present an efficient algorithm for computing the prepotential in compactifications
  of type II string theory on mirror pairs of Calabi-Yau threefolds in toric varieties.
  Applying this method, we exhibit the first systematic computation of genus-zero
  Gopakumar-Vafa invariants in compact threefolds with many moduli, including examples
  with up to 491 vector multiplets.
arxivId: '2303.00757'
arxivUrl: https://arxiv.org/abs/2303.00757
authors:
- Mehmet Demirtas
- Manki Kim
- Liam McAllister
- Jakob Moritz
- Andres Rios-Tascon
concepts:
- calabi-yau geometry
- gopakumar-vafa invariants
- string theory
- picard-fuchs equations
- symmetry preservation
- toric geometry
- quantum field theory
- scattering amplitudes
- inverse problems
- surrogate modeling
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2303_00757/figure_1.png
- /iaifi-research-blog/figures/2303_00757/figure_1.png
- /iaifi-research-blog/figures/2303_00757/figure_2.png
- /iaifi-research-blog/figures/2303_00757/figure_2.png
- /iaifi-research-blog/figures/2303_00757/figure_3.png
- /iaifi-research-blog/figures/2303_00757/figure_3.png
pdfUrl: https://arxiv.org/pdf/2303.00757v2
published: '2023-03-01T19:00:00+00:00'
theme: Theoretical Physics
title: Computational Mirror Symmetry
wordCount: 1189
---

## The Big Picture

Imagine trying to count the number of ways a rubber band can wrap around a donut, but the donut exists in six extra dimensions, is twisted by quantum mechanics, and you have 491 different ways to deform it. That, roughly, is the challenge at the heart of this paper.

In string theory, the universe has more than the four dimensions we observe. The extra six are curled up into tiny geometric shapes called **Calabi-Yau spaces**. The precise shape of these spaces determines the physics we observe, so characterizing their geometry is fundamental to string theory. One powerful way to do that is through **Gopakumar-Vafa (GV) invariants**: integers that count the different ways strings can wrap around curves inside these spaces, each wrapping making a distinct quantum contribution to the physics. For decades, computing these invariants in realistic, large-scale examples has been essentially impossible, not for lack of mathematical theory, but for lack of computational tools powerful enough to handle the complexity.

**Mirror symmetry** offers a spectacular shortcut. Physicists discovered in the early 1990s that every Calabi-Yau space has a "mirror twin," a completely different geometric shape that somehow encodes the same physics. Quantum effects that are extremely hard to compute on one space become straightforward classical calculations on its mirror. It's like discovering that a fiendishly hard differential equation is equivalent to measuring the area under a much simpler curve.

Even this shortcut breaks down for spaces with many **moduli**, the parameters that control the shape of the extra dimensions. With more than a handful of such parameters, the translation procedure between a space and its mirror becomes a computational nightmare: the required calculations grow exponentially.

A team of researchers from Northeastern, MIT, and Cornell has cracked this problem. They present an efficient algorithm that finally makes this mirror-translation tractable for Calabi-Yau spaces of any complexity, including the largest known examples, with up to 491 moduli.

> By solving two long-standing mathematical bottlenecks (handling non-simplicial Mori cones and exponentially large lattice sums), this work makes possible the first systematic computation of Gopakumar-Vafa invariants in compact Calabi-Yau threefolds with hundreds of moduli.

## How It Works

The core goal is to compute the **prepotential**, a single mathematical function that encodes all the physics of the particle sector emerging from a string compactification. In type IIA string theory, the prepotential receives quantum corrections from **worldsheet instantons**: stringy loops that wrap around curves in the Calabi-Yau geometry. These corrections are precisely what the GV invariants count, curve class by curve class.

Mirror symmetry converts this quantum problem into a classical one. On the mirror Calabi-Yau, the prepotential can be read off from **periods**, integrals of a special geometric quantity over a set of three-dimensional surfaces within the space. These are classical geometric quantities, governed by differential equations called the **Picard-Fuchs system**. The strategy: solve those equations, extract the periods, apply the mirror map (the translation between the two geometries), and decode the GV invariants from the resulting expansion.

![Figure 1](/iaifi-research-blog/figures/2303_00757/figure_1.png)

Three obstacles have historically blocked this approach for large Calabi-Yau spaces:

1. **Computing intersection numbers** of a threefold with many Kähler moduli (the parameters describing how the space curves in different directions), solved in prior work by the software package `CYTools`.
2. **Non-simplicial Mori cones**: the standard HKTY method, a classical algorithm for connecting a Calabi-Yau to its mirror, requires the Mori cone (the space of effective curve classes) to be *simplicial*, meaning it has as many generating directions as its dimension. This condition almost never holds when the number of moduli is large. The authors solve this by generalizing the HKTY construction to arbitrary Mori cones.
3. **Exponential lattice sums**: extracting GV invariants requires scanning lattice points in the Mori cone, and the number of such points grows exponentially with the number of moduli. The authors develop a consistent truncation strategy, proving that contributions from curve classes above a certain degree threshold can be safely ignored. This makes the sum finite and manageable.

![Figure 3](/iaifi-research-blog/figures/2303_00757/figure_2.png)

The truncation idea is especially clean. Rather than summing infinitely many contributions, the authors show that GV invariants for curves that are "too big" cannot contribute to the prepotential at any given order in the expansion. This lets them prune the search space systematically and dramatically.

For Calabi-Yau geometries with non-simplicial Mori cones, the team introduces an extension of the fundamental period (a power series whose coefficients encode the topology of the mirror space) along with a corresponding generalization of the Picard-Fuchs equations. Previously known only in the simplicial case, extending this construction is the paper's central mathematical contribution.

## Why It Matters

The string landscape, the vast space of possible extra-dimensional geometries, contains an astronomically large number of Calabi-Yau threefolds, most of them with large numbers of moduli. Computing GV invariants in these spaces isn't just a mathematical exercise. These invariants feed into our understanding of how quantum corrections shape the effective physical theories derived from string compactifications, including potential connections to particle physics and cosmology. Without tools like this, the landscape remains largely opaque.

![Figure 5](/iaifi-research-blog/figures/2303_00757/figure_3.png)

Mirror symmetry also sits at a crossroads of physics, mathematics, and computation. The GV invariants computed here are objects of pure mathematics (enumerative invariants studied by algebraic geometers), but they are most efficiently computed using physics-inspired methods. This work extends those methods into previously inaccessible territory, opening a new computational frontier in enumerative geometry.

Future directions include extending the algorithm to complete intersection Calabi-Yau spaces, computing higher-genus invariants, and integrating these tools with large-scale surveys to understand patterns across the string landscape.

> This paper delivers the first algorithm capable of computing Gopakumar-Vafa invariants in compact Calabi-Yau threefolds with hundreds of moduli, a computational milestone that makes a vast swath of the string landscape newly accessible to quantitative analysis.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects algebraic geometry, string theory, and computational mathematics, turning abstract mirror symmetry into a practical algorithm that runs on a laptop for spaces previously considered computationally intractable.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">While not directly an AI paper, the efficient lattice enumeration and symbolic period computation developed here are the kind of algorithmic advances that AI-physics collaborations at IAIFI work to systematize and accelerate.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The algorithm enables the first systematic calculation of genus-zero Gopakumar-Vafa invariants in compact Calabi-Yau threefolds with up to 491 vector multiplets, making quantitative study of quantum corrections across the string landscape possible for the first time.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend these methods to higher-genus invariants and more general Calabi-Yau geometries, with direct applications to string landscape surveys; the paper is available at [arXiv:2303.00757](https://arxiv.org/abs/2303.00757).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Computational Mirror Symmetry</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2303.00757</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Mehmet Demirtas", "Manki Kim", "Liam McAllister", "Jakob Moritz", "Andres Rios-Tascon"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We present an efficient algorithm for computing the prepotential in compactifications of type II string theory on mirror pairs of Calabi-Yau threefolds in toric varieties. Applying this method, we exhibit the first systematic computation of genus-zero Gopakumar-Vafa invariants in compact threefolds with many moduli, including examples with up to 491 vector multiplets.</span></div></div>
</div>
