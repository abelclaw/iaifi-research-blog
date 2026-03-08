---
abstract: Emerging sampling algorithms based on normalizing flows have the potential
  to solve ergodicity problems in lattice calculations. Furthermore, it has been noted
  that flows can be used to compute thermodynamic quantities which are difficult to
  access with traditional methods. This suggests that they are also applicable to
  the density-of-states approach to complex action problems. In particular, flow-based
  sampling may be used to compute the density directly, in contradistinction to the
  conventional strategy of reconstructing it via measuring and integrating the derivative
  of its logarithm. By circumventing this procedure, the accumulation of errors from
  the numerical integration is avoided completely and the overall normalization factor
  can be determined explicitly. In this proof-of-principle study, we demonstrate our
  method in the context of two-component scalar field theory where the $O(2)$ symmetry
  is explicitly broken by an imaginary external field. First, we concentrate on the
  zero-dimensional case which can be solved exactly. We show that with our method,
  the Lee-Yang zeroes of the associated partition function can be successfully located.
  Subsequently, we confirm that the flow-based approach correctly reproduces the density
  computed with conventional methods in one- and two-dimensional models.
arxivId: '2203.01243'
arxivUrl: https://arxiv.org/abs/2203.01243
authors:
- Jan M. Pawlowski
- Julian M. Urban
concepts:
- normalizing flows
- density of states
- density estimation
- sign problem
- monte carlo methods
- quantum field theory
- lattice qcd
- symmetry breaking
- phase transitions
- likelihood estimation
- lee-yang zeros
- stochastic processes
figures:
- /iaifi-research-blog/figures/2203_01243/figure_1.png
- /iaifi-research-blog/figures/2203_01243/figure_1.png
- /iaifi-research-blog/figures/2203_01243/figure_2.png
- /iaifi-research-blog/figures/2203_01243/figure_2.png
- /iaifi-research-blog/figures/2203_01243/figure_3.png
- /iaifi-research-blog/figures/2203_01243/figure_3.png
pdfUrl: https://arxiv.org/pdf/2203.01243v2
published: '2022-03-02T17:05:50+00:00'
theme: Theoretical Physics
title: Flow-based density of states for complex actions
wordCount: 1066
---

## The Big Picture

Imagine trying to measure the temperature of a campfire with a thermometer that bursts into flames on contact. That's roughly the predicament facing physicists who study matter at extreme densities, from the interior of neutron stars to the early universe microseconds after the Big Bang.

The mathematical framework they use, **lattice QCD** (quantum chromodynamics computed on a discrete grid), involves what's called a **complex action**: a term in the governing equation that becomes imaginary in the mathematical sense. This makes standard probability-based sampling methods completely unusable. The resulting roadblock, the infamous **sign problem**, has stalled progress on some of the most important open questions in nuclear physics for decades.

One workaround is the **density-of-states (DoS) approach**, which sidesteps the sign problem by slicing the problem into manageable pieces. Instead of computing everything at once, you map out how often the system visits each possible value of the troublesome quantity. Once you have this map, the density of states, you reconstruct the full physics through a relatively simple integral.

The catch: building that map with traditional methods requires measuring how the density shifts from one slice to the next, then summing those changes. Every step accumulates numerical error, and controlling that error to the required precision is brutally expensive.

Researchers Jan Pawlowski (Heidelberg) and Julian Urban (MIT/IAIFI) now propose a cleaner route: use **normalizing flows**, a machine learning technique, to compute the density of states directly, skipping the error-prone reconstruction entirely.

> **Key Insight:** By training a normalizing flow to sample configurations restricted to slices of field space, the density of states can be read off directly from the model's probability, eliminating accumulated integration errors and fixing the overall normalization that conventional methods must set by hand.

## How It Works

**Normalizing flows** are generative models that learn to transform a simple, known distribution (like a Gaussian) into a complicated target through a sequence of invertible operations. Because the transformation is invertible and differentiable, you can compute the exact probability of any output point via the change-of-variables formula. Flows are unusual among machine learning models in this respect: they provide both sampling *and* density estimation for free.

The idea here is to use flows not to approximate the full field theory measure, but to target a *modified* distribution that keeps the system pinned near a specific value of the observable causing the sign problem.

![Figure 1](/iaifi-research-blog/figures/2203_01243/figure_1.png)

Here's the procedure:

1. **Slice the problem.** Define the density of states ρ(c) as the integral over all field configurations with a fixed value c of the problematic observable X(ϕ), a cross-section through configuration space at height c.
2. **Smooth the slice.** Replace the exact delta-function constraint with a narrow Gaussian, a standard trick that makes the restricted distribution tractable for sampling.
3. **Train a flow per slice.** For each target value c, train a normalizing flow using **affine coupling layers**, where one part of the input scales and shifts the other, with transformation parameters set by a neural network.
4. **Read off the density directly.** Once trained, the flow's learned probability density gives you ρ(c) at that slice point. No integration required. The normalization factor, which must be set by hand in conventional methods, emerges automatically.

The training objective is the **Kullback-Leibler (KL) divergence** between the flow's distribution and the target. Minimizing it also yields a variational bound on the **partition function** log Z, a key quantity encoding all thermodynamic information about the system.

![Figure 2](/iaifi-research-blog/figures/2203_01243/figure_1.png)

The authors test their method across three settings of increasing complexity. In the zero-dimensional case, a single-site model solvable exactly, the flow-based density matches the analytical result closely. The method also locates the **Lee-Yang zeroes** of the partition function: special complex values where the partition function vanishes, which are fingerprints of phase transitions. Identifying these requires extending the partition function into the complex plane (**analytic continuation**), something the DoS approach handles gracefully once ρ(c) is in hand.

![Figure 3](/iaifi-research-blog/figures/2203_01243/figure_2.png)

Moving to one- and two-dimensional lattice models, the flow-based density is compared against results from conventional restricted **MCMC** (Markov Chain Monte Carlo) calculations. Agreement is good across the tested parameter ranges, confirming the method scales beyond toy models.

![Figure 4](/iaifi-research-blog/figures/2203_01243/figure_2.png)

![Figure 5](/iaifi-research-blog/figures/2203_01243/figure_3.png)

The automatic normalization deserves attention. In conventional DoS calculations, the overall normalization of ρ(c) is a free parameter requiring additional constraints or separate measurement. Having it fall out of flow training removes one more source of systematic uncertainty.

![Figure 6](/iaifi-research-blog/figures/2203_01243/figure_3.png)

## Why It Matters

The sign problem is not a technical nuisance. It is a fundamental barrier between physicists and some of the most interesting physics in the universe. QCD at finite baryon density, which describes neutron star cores and the quark-gluon plasma produced in heavy-ion collisions, is inaccessible to standard lattice techniques precisely because of it. The density-of-states approach offers a path around this barrier, and this paper shows that machine learning can sharpen that path considerably.

The sign problem also appears in condensed matter physics (strongly correlated electrons, frustrated magnets), quantum gravity models, and real-time quantum dynamics. Any of these could benefit from flow-based DoS methods. More expressive architectures and extended training strategies could push the approach to larger lattices and more realistic theories. The current results are a proof of principle, but the principle is now established.

> **Bottom Line:** Normalizing flows can compute the density of states for complex-action lattice field theories directly and without integration error, reproducing exact results in zero dimensions and conventional MCMC results in higher dimensions, and opening a machine learning avenue into some of the hardest problems in theoretical physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines normalizing flow models with the density-of-states technique from lattice field theory, showing that the explicit probability tracking of generative models solves a structural problem (accumulated integration error) that has long limited conventional approaches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Normalizing flows can act as precise density estimators in high-dimensional physics applications, providing exact normalization constants and variational bounds on partition functions as built-in outputs of training.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling direct, error-free computation of the density of states for complex-action theories, this method expands the toolkit available to attack the sign problem, a decades-old barrier blocking lattice QCD calculations at finite density.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will target larger lattices, more realistic gauge theories, and more expressive flow architectures; the paper is available at [arXiv:2203.01243](https://arxiv.org/abs/2203.01243).</span></div></div>
</div>
