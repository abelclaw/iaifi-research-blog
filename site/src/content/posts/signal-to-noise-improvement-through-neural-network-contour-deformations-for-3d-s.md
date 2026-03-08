---
abstract: Complex contour deformations of the path integral have been demonstrated
  to significantly improve the signal-to-noise ratio of observables in previous studies
  of two-dimensional gauge theories with open boundary conditions. In this work, new
  developments based on gauge fixing and a neural network definition of the deformation
  are introduced, which enable an effective application to theories in higher dimensions
  and with generic boundary conditions. Improvements of the signal-to-noise ratio
  by up to three orders of magnitude for Wilson loop measurements are shown in $SU(2)$
  lattice gauge theory in three spacetime dimensions.
arxivId: '2309.00600'
arxivUrl: https://arxiv.org/abs/2309.00600
authors:
- William Detmold
- Gurtej Kanwar
- Yin Lin
- Phiala E. Shanahan
- Michael L. Wagman
concepts:
- lattice gauge theory
- signal-to-noise improvement
- complex contour deformation
- wilson loops
- monte carlo methods
- quantum field theory
- equivariant neural networks
- symmetry preservation
- normalizing flows
- stochastic processes
figures:
- /iaifi-research-blog/figures/2309_00600/figure_1.png
pdfUrl: https://arxiv.org/pdf/2309.00600v1
published: '2023-09-01T17:42:32+00:00'
theme: Theoretical Physics
title: Signal-to-noise improvement through neural network contour deformations for
  3D $SU(2)$ lattice gauge theory
wordCount: 1181
---

## The Big Picture

Imagine trying to hear a whisper in a hurricane. That's roughly the challenge facing physicists who simulate the quantum world on a computer: the signal they care about gets buried under an avalanche of statistical noise, and the problem grows exponentially worse the more ambitious the question.

In **lattice quantum field theory**, the laws of physics are discretized onto a grid so that supercomputers can solve them step by step. The **signal-to-noise problem** has blocked progress on fundamental questions about matter and forces for decades.

The issue runs deep. When physicists want to understand **confinement** (why quarks are permanently locked inside protons and neutrons, never seen alone) they need to measure objects called **Wilson loops**. Think of a Wilson loop as a measuring tape stretched across space and time: it captures the energy cost of holding two particles apart, revealing how the force between them behaves.

The catch: the signal-to-noise ratio of these measurements decays *exponentially* with loop size. Double the area you're probing, and your computational cost doesn't double. It explodes. You need exponentially more samples to learn exponentially less.

A team from MIT, IAIFI, the University of Bern, and Fermilab has now shown a way to beat back this problem using neural networks to reshape the mathematical space over which the calculation is performed. In 3D SU(2) lattice gauge theory, a simplified but physically meaningful cousin of the theory describing the real strong nuclear force, they achieved signal-to-noise improvements of up to **three orders of magnitude** for Wilson loop measurements.

> **Key Insight:** By training neural networks to intelligently deform the integration contour of the path integral (the sum over all possible histories of a quantum system) physicists can measure the same physical quantities with vastly less statistical noise, without any approximation.

## How It Works

The core trick comes from classical complex analysis. In quantum field theory, expectation values are computed as integrals over all possible field configurations, weighted by the **Boltzmann factor**, a term encoding how probable each configuration is. It's analogous to how temperature determines which states a system tends to occupy.

If the integrand is **holomorphic** (complex-analytic), a classical result called **Cauchy's theorem** guarantees you can deform the integration contour without changing the answer. Move the path over which you sum, and the total sum stays the same. The physics doesn't change, but the noise properties of any specific estimator can change dramatically.

Previous work by some of the same authors showed this approach works in two-dimensional gauge theories, using a change of variables from **gauge links** (mathematical objects on each lattice edge encoding how particles transform as they move through space) to **plaquettes**, the elementary four-link building blocks of the lattice. But that trick requires open boundary conditions: a lattice with edges, like a sheet of graph paper. Real calculations use periodic boundaries (a lattice that wraps around, like a torus) in 3D or 4D. This paper gets past that wall.

The new approach works directly on the gauge link degrees of freedom, using two key innovations:

1. **Gauge fixing:** Before deforming, the team fixes a gauge (specifically, temporal gauge) to remove redundant degrees of freedom. In gauge theories, many different field configurations describe the exact same physical situation. Gauge fixing picks one representative from each family, which dramatically reduces the dimensionality of what the neural network must learn.
2. **Neural network deformation map:** A neural network learns the optimal deformation, a map that nudges each real-valued field configuration into the complex plane, by minimizing the variance of the deformed observable. It finds the sweet spot where signal survives and noise cancels.

The SU(2) gauge links are matrices encoding the symmetry of the strong force, expressed using the **Bronzan parametrization**: each matrix written in terms of three angles. Allowing those angles to become complex is what moves the calculation into the complex plane. The network outputs small shifts to these angles, producing deformed configurations that integrate to the correct expectation value but with far less variance.

![Figure 1](/iaifi-research-blog/figures/2309_00600/figure_1.png)

Training proceeds by gradient descent: the loss function is the variance of the deformed estimator, and the network learns to push the integration contour toward regions where noise is suppressed. Because the **Jacobian** of the map (a factor correcting for how volumes stretch and compress under the change of variables) can be computed exactly, there is no approximation anywhere in the pipeline.

## Why It Matters

A three-orders-of-magnitude improvement in signal-to-noise is the difference between a calculation being feasible or impossible. Lattice QCD calculations that currently require millions of CPU-hours could become tractable with thousands. Problems that have been entirely off-limits (larger Wilson loops, more complex operators, higher-dimensional theories) suddenly enter reach.

The implications run in two directions. For fundamental physics, the path toward reliable first-principles calculations of confinement, hadronic structure, and nuclear forces becomes much clearer. For machine learning, the work shows that neural networks can do something genuinely new in physics: not just fit data or speed up simulation, but *optimize the mathematical structure of the calculation itself*.

The neural network isn't approximating the physics. It's finding the best possible mathematical vantage point from which to observe it exactly.

> **Bottom Line:** Neural networks can now guide physicists through the complex plane to dramatically quieter measurements, achieving 1000x noise reduction for Wilson loops in 3D SU(2) gauge theory, with a clear path to the 4D theories that describe the real world.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses lattice field theory with modern machine learning, using neural networks not to approximate physics but to optimize the mathematical contour of exact path integral calculations in higher-dimensional gauge theories.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The neural networks here act as variational optimizers for integration contours in complex mathematical spaces, opening a new class of problems where learned maps reduce Monte Carlo variance without introducing bias.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By extending complex contour deformation to 3D SU(2) gauge theory with periodic boundary conditions, this work provides a scalable route toward solving the signal-to-noise problem in lattice QCD, a key obstacle to first-principles calculations of nuclear and hadronic physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The authors identify 4D SU(N) theories and full QCD as the natural next step; the work was presented at Lattice 2023 and is available as [arXiv:2309.00600](https://arxiv.org/abs/2309.00600).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Signal-to-noise improvement through neural network contour deformations for 3D $SU(2)$ lattice gauge theory</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2309.00600</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["William Detmold", "Gurtej Kanwar", "Yin Lin", "Phiala E. Shanahan", "Michael L. Wagman"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Complex contour deformations of the path integral have been demonstrated to significantly improve the signal-to-noise ratio of observables in previous studies of two-dimensional gauge theories with open boundary conditions. In this work, new developments based on gauge fixing and a neural network definition of the deformation are introduced, which enable an effective application to theories in higher dimensions and with generic boundary conditions. Improvements of the signal-to-noise ratio by up to three orders of magnitude for Wilson loop measurements are shown in $SU(2)$ lattice gauge theory in three spacetime dimensions.</span></div></div>
</div>
