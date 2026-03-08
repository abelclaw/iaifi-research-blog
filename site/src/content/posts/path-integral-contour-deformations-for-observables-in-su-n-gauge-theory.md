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
pdfUrl: https://arxiv.org/pdf/2101.12668v1
published: '2021-01-29T16:14:50+00:00'
theme: Theoretical Physics
title: Path integral contour deformations for observables in $SU(N)$ gauge theory
wordCount: 1025
---

## The Big Picture

Imagine trying to measure the height of ocean waves during a storm, but your measuring stick keeps getting buffeted by the very waves you're measuring. The more precisely you want to measure, the worse the interference, until your data is buried in noise. This is roughly the predicament facing physicists who use Monte Carlo simulations to study the strong nuclear force, which holds quarks together inside protons and neutrons.

The problem has a name: the **signal-to-noise (StN) problem**. In **lattice QCD**, the computational framework for simulating quantum chromodynamics on a discrete spacetime grid, calculations involving protons, neutrons, or larger nuclear structures produce results whose signal degrades *exponentially* faster than the noise. Throwing more simulation time at it barely helps.

For calculations involving nuclear matter at extreme densities, whether inside neutron stars or produced in heavy-ion collisions, there's an even nastier variant: the **sign problem**. The mathematical weights assigned to each simulated state become complex numbers, making them impossible to interpret as ordinary probabilities.

A team including researchers from MIT and Fermilab has now shown that machine learning can dramatically tame both problems, achieving up to 10,000-fold reductions in variance for Wilson loop observables in two-dimensional SU(2) and SU(3) gauge theories.

> **Key Insight:** By deforming the mathematical integration path into complex space, guided by machine learning, researchers can compute the same physics with radically less statistical noise without changing the answer.

## How It Works

The trick exploits a beautiful result from complex analysis. **Cauchy's integral theorem** guarantees that if you deform the contour of integration through a region where the integrand is complex-differentiable, the integral's value doesn't change. Think of it like routing water through a valley: you can change the path, but the same total volume flows through.

![Figure 1](/iaifi-research-blog/figures/2101_12668/figure_1.png)

The researchers apply this idea to **SU(N) lattice gauge theory**, a mathematical framework describing how force-carrying gluons interact on a grid-like representation of spacetime. The fundamental variables are abstract group elements on each lattice link. The key construction is a family of **contour deformations**: explicit mappings that push these variables into a "complexified" space where values can have both real and imaginary parts.

The **Jacobian determinant**, the correction factor for the stretching and squeezing that occurs when you change variables, turns out to have a special triangular structure. For triangular matrices the determinant is just the product of the diagonal entries, so it can be computed in time that scales *linearly* with system size rather than exponentially. That's a major computational win.

For observables like **Wilson loops**, closed paths traced through the gauge field that encode information about quark confinement, the team uses what they call the **deformed observable method**. They rewrite the observable so that it takes a different value on each individual field configuration, but the average over all configurations remains mathematically identical. The variance, however, can be made much smaller.

Here's the workflow:

1. Generate an ensemble of SU(N) gauge field configurations via standard Monte Carlo
2. Define a contour deformation parameterized by a neural network
3. Use the network to map each configuration into complexified field space
4. Reweight the observable using the Jacobian of the deformation
5. Train the network to minimize the variance of the resulting estimator

![Figure 2](/iaifi-research-blog/figures/2101_12668/figure_1.png)

The neural network learns the optimal deformation by gradient descent, tuning its parameters to squeeze out as much variance as possible. Cauchy's theorem guarantees the expectation value stays exact throughout.

## Why It Matters

The team tested their approach on Wilson loops in (1+1)-dimensional SU(2) and SU(3) gauge theories, two-dimensional versions of full four-dimensional QCD. They studied loops spanning up to 64 plaquettes (elementary squares of the lattice), where the StN problem is most severe.

![Figure 3](/iaifi-research-blog/figures/2101_12668/figure_2.png)

The results speak for themselves. For the largest loops at the finest lattice spacings, variance dropped by factors between 1,000 and 10,000. To put that in perspective: a 10,000-fold variance reduction means you need 10,000 times fewer Monte Carlo samples to hit the same statistical precision. That's the difference between a calculation that takes years and one that finishes in hours.


Because the Jacobian computation scales linearly, the technique doesn't become exponentially more expensive as the system grows. That's a hard requirement for any method that hopes to work on realistic lattice sizes.


The researchers also derived exact analytical results for variances in (1+1)D gauge theory, giving them a precise benchmark. In several cases, the optimized deformations essentially saturated the theoretical limit for variance reduction.


The sign and signal-to-noise problems aren't mere technical inconveniences. They block calculations of nuclear binding energies, neutron matter properties, and dense-matter behavior in heavy-ion collisions. Without solutions, entire regimes of the Standard Model stay computationally out of reach.

What sets this approach apart from other ML-for-lattice-QCD work is its target. Rather than using neural networks to generate better Monte Carlo samples, it uses them to find better *representations* of the same physics. The deformed observable method complements sampling improvements and could in principle be combined with them.

> **Bottom Line:** Machine-learned path integral contour deformations achieve up to 10,000-fold variance reduction for Wilson loops in SU(N) gauge theory, opening a practical route toward solving the sign and signal-to-noise problems that have long blocked precision calculations in nuclear and particle physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Interdisciplinary Achievement</strong><br/><span style="color:#374151;">This work connects machine learning optimization with open problems in quantum field theory, using neural networks to discover optimal contour deformations that Cauchy's theorem analytically guarantees will preserve physical predictions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Impact on AI</strong><br/><span style="color:#374151;">The approach shows a principled use of ML where the network learns geometrical deformations subject to an exact mathematical constraint, a model for integrating deep learning into rigorous scientific computation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Variance reductions of up to four orders of magnitude for Wilson loops in SU(2) and SU(3) gauge theory mark real progress on the signal-to-noise problem that has long limited lattice QCD calculations of nuclear systems and dense matter.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Outlook</strong><br/><span style="color:#374151;">Future work targets extending contour deformations to full (3+1)-dimensional lattice QCD, where the linear-scaling Jacobian computation makes the approach viable at realistic system sizes. The preprint is available at [arXiv:2101.12668](https://arxiv.org/abs/2101.12668).</span></div></div>
</div>
