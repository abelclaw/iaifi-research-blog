---
abstract: Path integral contour deformations have been shown to mitigate sign and
  signal-to-noise problems associated with phase fluctuations in lattice field theories.
  We define a family of contour deformations applicable to $SU(N)$ lattice gauge theory
  that can reduce sign and signal-to-noise problems associated with complex actions
  and complex observables. For observables, these contours can be used to define deformed
  observables with identical expectation value but different variance. As a proof-of-principle,
  we apply machine learning techniques to optimize the deformed observables associated
  with Wilson loops in two dimensional $SU(2)$ and $SU(3)$ gauge theory. We study
  loops consisting of up to 64 plaquettes and achieve variance reduction of up to
  4 orders of magnitude.
arxivId: '2101.12668'
arxivUrl: https://arxiv.org/abs/2101.12668
authors:
- William Detmold
- Gurtej Kanwar
- Henry Lamm
- Michael L. Wagman
- Neill C. Warrington
concepts:
- path integral contour deformations
- lattice gauge theory
- sign and signal-to-noise problems
- variance reduction
- monte carlo methods
- group theory
- wilson loops
- lattice qcd
- quantum field theory
- physics-informed neural networks
- symmetry preservation
figures:
- /iaifi-research-blog/figures/2101_12668/figure_1.png
- /iaifi-research-blog/figures/2101_12668/figure_1.png
- /iaifi-research-blog/figures/2101_12668/figure_2.png
- /iaifi-research-blog/figures/2101_12668/figure_2.png
- /iaifi-research-blog/figures/2101_12668/figure_3.png
- /iaifi-research-blog/figures/2101_12668/figure_3.png
pdfUrl: https://arxiv.org/pdf/2101.12668v1
published: '2021-01-29T16:14:50+00:00'
theme: Theoretical Physics
title: Path integral contour deformations for observables in $SU(N)$ gauge theory
wordCount: 1107
---

## The Big Picture

Imagine trying to measure the height of ocean waves during a storm — but your measuring stick keeps getting buffeted by the very waves you're measuring. The more precisely you want to measure, the worse the interference, until your data is buried in noise. This is roughly the predicament facing physicists who use Monte Carlo simulations — a technique that uses random sampling to crunch difficult mathematical calculations — to study the strong nuclear force, which holds quarks together inside protons and neutrons.

The problem has a name: the **signal-to-noise (StN) problem**. In **lattice QCD** — the computational framework physicists use to simulate quantum chromodynamics (the theory of the strong nuclear force) on a discrete spacetime grid — calculations involving protons, neutrons, or larger nuclear structures produce results whose signal degrades *exponentially* faster than the noise. More simulation time barely helps.

For calculations involving nuclear matter at extreme densities — inside neutron stars or produced in heavy-ion collisions — there's an even nastier variant: the **sign problem**. Here, the mathematical weights assigned to each simulated state become complex numbers (numbers with an imaginary component), making them impossible to interpret as ordinary probabilities.

A team from MIT, Fermilab, and the University of Washington has now demonstrated that machine learning can dramatically tame both problems — achieving up to **10,000-fold reductions in variance** for Wilson loop observables in two-dimensional SU(2) and SU(3) gauge theories.

> **Key Insight:** By deforming the mathematical integration path into complex space — guided by machine learning — researchers can compute the same physics with radically less statistical noise, without changing the answer.

## How It Works

The trick exploits a beautiful result from complex analysis. **Cauchy's integral theorem** guarantees that if you deform the contour of integration — the mathematical path along which an integral is computed — through a region where the integrand is complex-differentiable, the integral's value doesn't change. Think of it like routing water through a valley: you can change the path, but the same total volume flows through.

![Figure 1](/iaifi-research-blog/figures/2101_12668/figure_1.png)

The researchers apply this idea to **SU(N) lattice gauge theory** — a mathematical framework describing how force-carrying gluons interact on a grid-like representation of spacetime. The fundamental variables are abstract group elements representing the gauge field on each lattice link. Their key construction is a family of **contour deformations**: explicit mappings that push these variables into a "complexified" space where values can have both real and imaginary parts.

Crucially, the **Jacobian determinant** — the correction factor accounting for the stretching and squeezing that occurs when you change variables — has a special triangular structure. For triangular matrices, the determinant reduces to the product of the diagonal entries, so it can be computed in time that scales *linearly* with system size rather than exponentially. That's a major computational win.

For observables like **Wilson loops** — closed paths traced through the gauge field that encode information about quark confinement — the team uses the **deformed observable method**: they rewrite the observable so that it takes a different value on each individual field configuration, but the average over all configurations remains mathematically identical. The variance, however, can be made much smaller.

Here's the workflow:

1. Generate an ensemble of SU(N) gauge field configurations via standard Monte Carlo
2. Define a contour deformation parameterized by a neural network
3. Use the network to map each configuration into complexified field space
4. Reweight the observable using the Jacobian of the deformation
5. Train the network to minimize the variance of the resulting estimator

![Figure 2](/iaifi-research-blog/figures/2101_12668/figure_1.png)

The neural network learns the optimal deformation by gradient descent, tuning its parameters to squeeze out as much variance as possible while Cauchy's theorem guarantees the expectation value stays exact.

## Why It Matters

The team tested their approach on Wilson loops in (1+1)-dimensional SU(2) and SU(3) gauge theories — two-dimensional toy versions of real four-dimensional QCD. They studied loops spanning up to 64 plaquettes (elementary squares of the lattice), where the StN problem is most severe.

![Figure 3](/iaifi-research-blog/figures/2101_12668/figure_2.png)

The results are striking. For the largest loops at the finest lattice spacings, variance was reduced by factors between 1,000 and 10,000. To put that in perspective: a 10,000-fold variance reduction means you need 10,000 times fewer Monte Carlo samples to achieve the same statistical precision — the difference between a calculation that takes years and one that takes hours.

![Figure 4](/iaifi-research-blog/figures/2101_12668/figure_2.png)

The linear scaling of the Jacobian computation means the technique doesn't become exponentially more expensive as the system grows — a crucial requirement for real-world applicability.

![Figure 5](/iaifi-research-blog/figures/2101_12668/figure_3.png)

The researchers also derived exact analytical results for variances in (1+1)D gauge theory, providing a precise benchmark for their machine-learned improvements. In several cases, the optimized deformations essentially saturated the theoretical limit for variance reduction.

![Figure 6](/iaifi-research-blog/figures/2101_12668/figure_3.png)

The sign and signal-to-noise problems aren't mere technical inconveniences — they represent fundamental obstacles to precision nuclear physics. Calculations of nuclear binding energies, neutron matter properties, and dense-matter behavior in heavy-ion collisions all run headlong into these walls. Without solutions, entire regimes of the Standard Model remain computationally inaccessible.

This work occupies a distinctive niche within the growing body of ML-for-lattice-QCD research. Rather than using neural networks to generate better Monte Carlo samples, it uses them to find better *representations* of the same physics. The deformed observable method is complementary to sampling improvements and can in principle be combined with them for even greater gains.

> **Bottom Line:** Machine-learned path integral contour deformations achieve up to 10,000-fold variance reduction for Wilson loops in SU(N) gauge theory, pointing toward a practical route for taming the sign and signal-to-noise problems that have long blocked precision calculations in nuclear and particle physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges machine learning optimization with fundamental problems in quantum field theory, using neural networks to discover optimal contour deformations that are analytically guaranteed — via Cauchy's theorem — to preserve physical predictions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The approach demonstrates a principled use of ML in which the network learns geometrical deformations subject to an exact mathematical constraint, offering a template for integrating deep learning into rigorous scientific computation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Variance reductions of up to four orders of magnitude for Wilson loops in SU(2) and SU(3) gauge theory represent a significant step toward overcoming the signal-to-noise problem that has long limited lattice QCD calculations of nuclear systems and dense matter.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work aims to extend contour deformations to full (3+1)-dimensional lattice QCD, where the linear-scaling Jacobian computation makes the approach feasible at realistic system sizes; the preprint is available as FERMILAB-PUB-21-014-T / MIT-CTP/5270.</span></div></div>
</div>
