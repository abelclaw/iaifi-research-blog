---
abstract: Power counting is a systematic strategy for organizing collider observables
  and their associated theoretical calculations. In this paper, we use power counting
  to characterize a class of jet substructure observables called energy flow polynomials
  (EFPs). EFPs provide an overcomplete linear basis for infrared-and-collinear safe
  jet observables, but it is known that in practice, a small subset of EFPs is often
  sufficient for specific jet analysis tasks. By applying power counting arguments,
  we obtain linear relationships between EFPs that hold for quark and gluon jets to
  a specific order in the power counting. We test these relations in the parton shower
  generator Pythia, finding excellent agreement. Power counting allows us to truncate
  the basis of EFPs without affecting performance, which we corroborate through a
  study of quark-gluon tagging and regression.
arxivId: '2205.06818'
arxivUrl: https://arxiv.org/abs/2205.06818
authors:
- Pedro Cal
- Jesse Thaler
- Wouter J. Waalewijn
concepts:
- jet physics
- energy flow polynomials
- power counting
- collider physics
- effective field theory
- infrared-collinear safety
- classification
- regression
- sparse models
- feature extraction
- graph neural networks
figures:
- /iaifi-research-blog/figures/2205_06818/figure_1.png
- /iaifi-research-blog/figures/2205_06818/figure_1.png
- /iaifi-research-blog/figures/2205_06818/figure_2.png
- /iaifi-research-blog/figures/2205_06818/figure_2.png
- /iaifi-research-blog/figures/2205_06818/figure_3.png
- /iaifi-research-blog/figures/2205_06818/figure_3.png
pdfUrl: https://arxiv.org/pdf/2205.06818v2
published: '2022-05-13T18:00:00+00:00'
theme: Theoretical Physics
title: Power Counting Energy Flow Polynomials
wordCount: 1056
---

## The Big Picture

Imagine trying to identify a person in a crowd using every possible facial measurement — the distance between each pair of freckles, every angle of every feature. You'd drown in data. Now imagine a physicist's version of that problem, applied to the chaos of particle collisions at the Large Hadron Collider.

Every time protons smash together at CERN, the resulting debris sprays into tight, narrow streams of particles called **jets**. The internal patterns of these jets — their **substructure** — carry fingerprints of the fundamental interactions that created them.

For decades, physicists have built specialized measurements to read those fingerprints. More recently, the field has pushed toward complete mathematical toolkits: collections of measurements that, in principle, capture *everything* about a jet. One such toolkit — **energy flow polynomials (EFPs)** — is mathematically guaranteed to be complete. Think of EFPs as a systematically organized family of measurements, each probing a different combination of angular relationships between particles in the jet, arranged by their complexity.

But completeness comes at a steep price. By degree six — the sixth level of complexity — there are 314 distinct EFPs. Using all of them is computationally painful and conceptually murky.

This paper by Pedro Cal, Jesse Thaler, and Wouter J. Waalewijn cuts through that excess. Using a classical physics technique called **power counting**, they show that the EFP toolkit contains enormous redundancy for realistic jets — and that a dramatically smaller subset performs just as well.

> **Key Insight:** By applying power counting arguments appropriate for quark and gluon jets, the authors reduce the EFP basis by more than a factor of six at degree six (from 212 down to 22 elements), without sacrificing machine learning performance.

## How It Works

EFPs are built from a beautiful idea: represent each observable as a graph. Each node corresponds to a particle in the jet; each edge encodes an angular correlation between particles. The **degree** of an EFP — the number of edges — controls how many angular correlations it probes. Computing all EFPs up to degree six means evaluating 314 such graphs over every particle pair, triplet, or quartet in a jet. Computational cost scales steeply with graph complexity.

**Power counting** is a tool borrowed from **effective field theory** — a physics framework that describes complex systems by focusing only on effects that matter at a given scale, systematically ignoring the rest. The core idea: not all contributions are equally important. By identifying what's "big" and what's "small" in typical jet configurations, you can organize observables by relative importance and discard subleading terms. The authors apply three power counting schemes:

- **Strongly-ordered expansion**: Assumes jet emissions are hierarchically ordered in both energy and angle — a realistic approximation for leading-logarithmic calculations.
- **1-collinear expansion**: Keeps one energetic **collinear** emission (a particle flying nearly parallel to the jet axis) with full angular information, expanding around that configuration.
- **2-collinear expansion**: Extends to two energetic collinear emissions, capturing next-to-leading logarithmic physics — a finer level of precision.

![Figure 1](/iaifi-research-blog/figures/2205_06818/figure_1.png)

Within each scheme, power counting reveals linear relationships between EFPs. Two graphically distinct EFPs may be numerically equivalent — to the precision of the approximation — once you account for how jets actually form. The authors derive these relations analytically, then test them on millions of simulated jets from **Pythia**, a widely used program that simulates particle emergence and scattering after high-energy collisions.

The results are striking. For the strongly-ordered basis, the degree-six EFP count drops from 212 to just 22. The 2-collinear basis needs 37 elements — richer, because it retains more angular information — but still tiny compared to the full set.

The predicted linear relations hold up in Pythia with excellent numerical agreement.

![Figure 3](/iaifi-research-blog/figures/2205_06818/figure_2.png)

## Why It Matters

The immediate payoff is practical. The authors run quark/gluon tagging — distinguishing jets initiated by quarks from those initiated by gluons — using logistic regression on both the full EFP set and their reduced bases. The reduced bases match full-set performance using a fraction of the inputs. For regression tasks predicting continuous jet properties, the story is the same.

But there's a deeper gain. EFPs were always intended as a complete basis, but completeness without structure is just a list. Power counting gives that list a hierarchy — it tells you which observables matter most, and for which physics.

This is understanding that machine learning alone can't provide. A neural network might implicitly learn to ignore redundant EFPs; power counting explains *why* they're redundant and *when* that redundancy breaks down.

There's also a computational bonus in the 1-collinear case. Naively, computing an N-point EFP on M particles costs O(M^N) — the computation balloons exponentially as both particle count and observable complexity grow. Power counting lets the authors "cut open" high-complexity graphs and express them as products of simpler ones, reducing the **tree-width** (a graph-theory measure of computational complexity) of the underlying computation. Fewer floating-point operations per jet matters enormously at the LHC, where jets are reconstructed millions of times per second.

Looking forward, the approach raises natural questions: Can power counting extend to multi-prong jets from top quarks or W bosons? Can the basis reductions inform better neural network architectures for jet physics? The authors focus on single-prong quark and gluon jets here, flagging multi-prong extension as explicit future work.

![Figure 5](/iaifi-research-blog/figures/2205_06818/figure_3.png)

> **Bottom Line:** Power counting transforms the EFP basis from an unwieldy 314-element list into a compact, physically motivated toolkit of ~22–70 elements — enabling faster computation, cleaner interpretability, and undiminished machine learning performance on jet classification tasks.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges effective field theory techniques from high-energy physics with modern machine learning approaches to jet substructure, showing that physics-informed basis reduction outperforms brute-force completeness.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Principled physical reasoning compresses high-dimensional feature spaces by over 6x without performance loss, offering a reusable template for physics-guided feature selection in scientific machine learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Power counting reveals previously hidden linear dependencies among jet observables, providing new analytic insight into the structure of infrared-and-collinear safe observables at the LHC — directly relevant to precision QCD calculations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions to multi-prong jets (top quarks, W/Z bosons) could dramatically expand the scope of this framework; the full paper is available at arXiv:2205.02824.</span></div></div>
</div>
