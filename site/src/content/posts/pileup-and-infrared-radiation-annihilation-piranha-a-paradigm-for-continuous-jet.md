---
abstract: Jet grooming is an important strategy for analyzing relativistic particle
  collisions in the presence of contaminating radiation. Most jet grooming techniques
  introduce hard cutoffs to remove soft radiation, leading to discontinuous behavior
  and associated experimental and theoretical challenges. In this paper, we introduce
  Pileup and Infrared Radiation Annihilation (PIRANHA), a paradigm for continuous
  jet grooming that overcomes the discontinuity and infrared sensitivity of hard-cutoff
  grooming procedures. We motivate PIRANHA from the perspective of optimal transport
  and the Energy Mover's Distance and review Apollonius Subtraction and Iterated Voronoi
  Subtraction as examples of PIRANHA-style grooming. We then introduce a new tree-based
  implementation of PIRANHA, Recursive Subtraction, with reduced computational costs.
  Finally, we demonstrate the performance of Recursive Subtraction in mitigating sensitivity
  to soft distortions from hadronization and detector effects, and additive contamination
  from pileup and the underlying event.
arxivId: '2305.00989'
arxivUrl: https://arxiv.org/abs/2305.00989
authors:
- Samuel Alipour-Fard
- Patrick T. Komiske
- Eric M. Metodiev
- Jesse Thaler
concepts:
- jet physics
- continuous jet grooming
- optimal transport
- collider physics
- energy mover's distance
- pileup mitigation
- quantum field theory
- unfolding
- monte carlo methods
- effective field theory
- anomaly detection
figures:
- /iaifi-research-blog/figures/2305_00989/figure_2.png
pdfUrl: https://arxiv.org/pdf/2305.00989v3
published: '2023-05-01T18:00:00+00:00'
theme: Experimental Physics
title: 'Pileup and Infrared Radiation Annihilation (PIRANHA): A Paradigm for Continuous
  Jet Grooming'
wordCount: 1045
---

## The Big Picture

Imagine trying to photograph a hummingbird in a rainstorm. The bird is what you care about, fast and precise and full of information, but the rain muddies every frame.

Particle physicists face the same problem every time the Large Hadron Collider fires up. When protons smash together at nearly the speed of light, the collisions produce **jets**, tight sprays of subatomic debris carrying fingerprints of the fundamental forces at play. But those jets don't travel through vacuum. They're surrounded by a constant drizzle of unwanted radiation: detector noise, overlapping collisions called **pileup**, and background particle activity from the collision remnants (the **underlying event**). Separating signal from noise is the job of **jet grooming**, algorithms that clean up jets before physicists analyze them.

Most grooming tools today are blunt instruments. They apply hard cutoffs: if a particle carries less than some fraction *z*_cut of the jet's energy, it gets discarded. That sounds reasonable, but it creates a nasty artifact. A tiny energy fluctuation can flip a grooming decision and reshape the entire jet. This discontinuity isn't just aesthetically unpleasant. It complicates correcting raw detector data for detector effects and makes theoretical calculations harder.

A team from MIT and IAIFI has now introduced **PIRANHA** (Pileup and Infrared Radiation Annihilation), a new grooming paradigm that replaces hard cutoffs with a continuous, mathematically principled approach rooted in optimal transport theory.

> **Key Insight:** Instead of binary cutoffs that cause abrupt, unphysical jumps in groomed jet shapes, PIRANHA continuously redistributes and removes soft radiation in a way that varies smoothly with the event, making groomed jets far more stable under small perturbations.

## How It Works

The mathematical backbone is the **Energy Mover's Distance (EMD)**, a measure of how different two collider events are, borrowed from **optimal transport** (the mathematics of moving distributions as efficiently as possible). Picture each event as a pile of dirt spread across the detector. The EMD is the minimum work needed to rearrange one pile into another. Jets that look similar physically should have a small EMD between them, and any grooming procedure that respects this geometry should map similar inputs to similar outputs.

PIRANHA turns this intuition into an algorithm. Rather than removing particles below a threshold, it *subtracts* energy from particles in a way that minimizes transport cost, the "effort" to redistribute that energy into a hypothetical background. The result:

- No particle is sharply excluded based on a single threshold
- Outputs respond smoothly as soft particles are added, removed, or shifted
- The geometric structure of the jet is preserved while contamination is removed

![Figure 1](/iaifi-research-blog/figures/2305_00989/figure_2.png)

The paper presents three concrete implementations. **Apollonius Subtraction (P-AS)** assigns each particle a region of influence based on an **Apollonius diagram**, a generalization of the **Voronoi tessellation** (dividing space into nearest-neighbor regions) that also accounts for particle energy, then subtracts background within each region. It's continuous but computationally expensive. **Iterated Voronoi Subtraction (P-IVS)** approximates P-AS using standard Voronoi regions applied iteratively, trading some precision for speed. Both were introduced in earlier work.

The new contribution is **Recursive Subtraction (P-RS)**, specifically **P-RSF** (Recursive Subtraction with a Fraction *f*). P-RSF operates on the **clustering tree**, the hierarchical branching structure that jet-finding algorithms already produce. At each branch point, it subtracts a fraction *f* of the softer branch's energy from the harder branch, then propagates upward. This is dramatically cheaper to compute and slots naturally into existing pipelines. The special case *f* = 1/2 is the only fully **soft-continuous** variant, producing no abrupt jumps as low-energy particles come and go, and it's the focus throughout the paper.


## Why It Matters

The authors test Recursive Subtraction against several contamination sources: hadronization (the process by which quarks and gluons bind into detectable particles), charged-only versus full-particle reconstruction, pileup from overlapping collisions, and the underlying event. In each case, P-RSF shows smaller sensitivity than traditional groomers like Soft Drop. For the practically important task of measuring *W* boson and top quark jet masses (crucial benchmarks at the LHC), Recursive Subtraction delivers cleaner mass peaks with less smearing from pileup.


The paper also provides a rigorous perturbative analysis tracing exactly why hard-cutoff groomers suffer from discontinuities and how PIRANHA avoids them. The authors distinguish **soft discontinuities** (sensitivity to changes in particle energies) from **angular discontinuities** (sensitivity to changes in particle directions), then locate each type precisely in the mathematics of different algorithms. An appendix pushes toward a full resummed perturbative calculation, systematically accounting for cumulative quantum corrections, for Recursive Subtraction. This opens the door to precision QCD (Quantum Chromodynamics, the theory of the strong force) predictions with PIRANHA-groomed observables.

Optimal transport has been reshaping machine learning over the past decade, and by grounding jet grooming in EMD, PIRANHA inherits both a rigorous mathematical toolkit and a natural interface with modern data analysis. As collider physics increasingly incorporates machine learning for anomaly detection, classification, and precision measurements, grooming procedures that speak the same geometric language could enable tighter integration with AI-based approaches.

Open questions remain. Angular discontinuities in P-RSF are suppressed but not eliminated; future variants may resolve them fully. Extending the resummation calculations to higher accuracy is another frontier. The PIRANHA paradigm itself may inspire algorithms optimized for boosted object tagging, heavy ion collisions, or future collider environments.

> **Bottom Line:** PIRANHA replaces the blunt, discontinuous cutoffs of traditional jet grooming with a continuous, transport-theory-inspired framework, making LHC measurements more stable, detector corrections easier, and theoretical predictions more tractable.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work imports optimal transport theory, a cornerstone of modern machine learning, into high-energy experimental physics, grounding jet grooming algorithms in geometric probability theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">PIRANHA shows how AI-adjacent tools like the Earth Mover's Distance can be put to work in physics pipelines, offering a concrete model for how ML geometry can inform algorithm design in data-intensive science.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By eliminating hard-cutoff discontinuities in jet grooming, PIRANHA reduces systematic uncertainties in LHC measurements of QCD, electroweak bosons, and top quarks, directly improving the precision of fundamental physics extractions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work includes extending the resummation framework to higher logarithmic accuracy and developing continuous implementations that fully eliminate angular discontinuities; see [arXiv:2305.00989](https://arxiv.org/abs/2305.00989) for the full paper.</span></div></div>
</div>
