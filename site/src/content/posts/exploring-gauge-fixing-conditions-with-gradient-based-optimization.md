---
abstract: Lattice gauge fixing is required to compute gauge-variant quantities, for
  example those used in RI-MOM renormalization schemes or as objects of comparison
  for model calculations. Recently, gauge-variant quantities have also been found
  to be more amenable to signal-to-noise optimization using contour deformations.
  These applications motivate systematic parameterization and exploration of gauge-fixing
  schemes. This work introduces a differentiable parameterization of gauge fixing
  which is broad enough to cover Landau gauge, Coulomb gauge, and maximal tree gauges.
  The adjoint state method allows gradient-based optimization to select gauge-fixing
  schemes that minimize an arbitrary target loss function.
arxivId: '2410.03602'
arxivUrl: https://arxiv.org/abs/2410.03602
authors:
- William Detmold
- Gurtej Kanwar
- Yin Lin
- Phiala E. Shanahan
- Michael L. Wagman
concepts:
- lattice gauge theory
- adjoint state method
- differentiable gauge fixing
- loss function design
- renormalization
- signal-to-noise optimization
- inverse problems
- monte carlo methods
- physics-informed neural networks
- normalizing flows
figures:
- /iaifi-research-blog/figures/2410_03602/figure_1.png
- /iaifi-research-blog/figures/2410_03602/figure_1.png
- /iaifi-research-blog/figures/2410_03602/figure_2.png
- /iaifi-research-blog/figures/2410_03602/figure_2.png
- /iaifi-research-blog/figures/2410_03602/figure_3.png
- /iaifi-research-blog/figures/2410_03602/figure_3.png
pdfUrl: https://arxiv.org/pdf/2410.03602v1
published: '2024-10-04T17:01:41+00:00'
theme: Theoretical Physics
title: Exploring gauge-fixing conditions with gradient-based optimization
wordCount: 1133
---

## The Big Picture

Imagine trying to photograph a spinning top. The top is real, with definite shape and angular momentum, but your choice of shutter speed, angle, and lighting determines what you actually capture. Some choices make the blur worse. Others freeze the motion perfectly. The underlying object never changes, but how well you can measure it depends enormously on *how* you choose to look.

Physicists studying the strong nuclear force face an analogous problem. Quantum chromodynamics (QCD), the theory governing quarks and gluons, possesses a mathematical symmetry called **gauge invariance** (the equations look identical after certain transformations of the underlying fields, much like rotational symmetry in a spinning top). To do practical calculations, physicists simulate QCD on a **lattice**, a discrete grid of spacetime points, like pixels in a computational snapshot of the universe.

Gauge invariance is useful in many contexts, but it becomes a headache when measuring quantities needed for **renormalization**, the mathematical process of subtracting infinities and extracting clean physical predictions from quantum field theory. Before computing these quantities, you must "fix the gauge": pick a specific mathematical perspective and stick to it.

For decades, physicists have made these choices by convention, defaulting to schemes like Landau gauge or Coulomb gauge. A new paper from researchers at MIT, Fermilab, and collaborating institutions asks a question that hasn't gotten enough attention: what if, instead of choosing a gauge by convention, you let a computer *learn* the best gauge for your specific problem?

> **Key Insight:** By treating gauge-fixing as a differentiable optimization problem, researchers can now systematically search for gauge-fixing schemes that minimize any target quantity, allowing data-driven exploration of gauge choices in lattice QCD calculations.

## How It Works

The method rests on one observation. Most common gauge-fixing schemes, including Landau gauge, Coulomb gauge, and **maximal tree gauges** (schemes that fix a spanning set of links to the identity matrix), can all be written as minimizing one functional:

$$E = -\frac{1}{N_d N_V} \sum_{x,\mu} \text{Re Tr}\, p_\mu(x)\, U_\mu^g(x)$$

Here, $U_\mu^g(x)$ are the gauge-transformed links and the coefficients $p_\mu(x)$ are real numbers assigned to each link. The magic is in those coefficients: set them all to 1 and you get Landau gauge; set them to 1 only for spatial links and you recover Coulomb gauge; make them binary over a tree structure and you have a maximal tree gauge.

This parameterization turns a discrete zoo of gauge choices into a continuous family, and a continuous family is something you can *differentiate through*.

![Figure 1](/iaifi-research-blog/figures/2410_03602/figure_1.png)

The key computational challenge: given a gauge-fixing algorithm that minimizes $E$ for a set of $p_\mu(x)$ coefficients, how do you compute the gradient of a downstream loss $\ell$ with respect to those coefficients? Running automatic differentiation through all the solver iterations is numerically unstable.

The team's solution is the **adjoint state method**, a classical technique from optimal control theory. Rather than differentiating through the iterative solver, it treats the gauge-fixing condition as a constraint and solves a single linear system to extract gradients exactly. The solver becomes a black box. Swap in any algorithm you like, and the gradient computation stays stable and efficient.

The workflow proceeds in three steps:

1. **Fix the gauge**: Run a standard iterative minimizer to find the gauge transformation $g^*(x)$ satisfying the gauge condition for your current $p_\mu(x)$.
2. **Solve the adjoint problem**: Compute Lagrange multipliers $\lambda_c(z)$ by solving a linear system involving the Hessian of $E$ at the fixed-gauge solution.
3. **Update the scheme parameters**: Use the adjoint variables to compute $d\ell/dp_\mu(x)$ and take a gradient step.

For the maximal tree subfamily (where $p_\mu(x)$ should ideally be binary), the team introduces a **temperature regulator**: a smooth interpolation that relaxes the discrete constraint and lets gradient descent explore continuously before annealing toward a binary solution.

## Why It Matters

![Figure 2](/iaifi-research-blog/figures/2410_03602/figure_1.png)

This work addresses a problem that has historically been treated as folklore: physicists know that gauge choice affects statistical noise in their calculations, but have had no principled way to search for better ones. The new framework provides a systematic tool for exactly that search.

Recent discoveries that gauge-variant quantities can dramatically reduce statistical noise through **contour deformations** (a technique for improving the signal-to-noise ratio in Monte Carlo calculations) make this especially timely. The framework lets researchers directly optimize their gauge scheme to minimize noise, rather than guessing.

![Figure 3](/iaifi-research-blog/figures/2410_03602/figure_2.png)

The broader significance is what this paper represents methodologically. It shows how modern machine learning infrastructure, including differentiable programming, gradient-based optimization, and automatic differentiation, can be applied to the constrained, discrete problems at the heart of lattice field theory. The adjoint state method has long been used in fluid dynamics and engineering optimization; its application here connects two fields that don't usually talk to each other.

Future extensions could incorporate richer parameterizations such as maximal Abelian gauges, or couple gauge optimization directly with the normalizing-flow samplers used in lattice QCD sampling. Whether learned gauge schemes will generalize across different lattice spacings and physical parameters remains an open question, one that mirrors familiar generalization challenges in deep learning.

> **Bottom Line:** By making gauge-fixing differentiable, this work transforms an ancient convention into a learnable design choice, giving lattice QCD practitioners a new knob to turn in the quest for cleaner, cheaper calculations of fundamental physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Interdisciplinary Achievement</strong><br/><span style="color:#374151;">This work imports adjoint state methods from optimal control into lattice gauge theory, creating a differentiable framework that unifies disparate gauge-fixing schemes under a single parameterization and enables gradient-based optimization over them.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Machine Learning Connection</strong><br/><span style="color:#374151;">The approach shows how differentiable programming and gradient-based optimization, core tools of modern ML, can be applied to discrete, constrained physics problems through continuous relaxation and stable adjoint-state gradients.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The framework gives lattice QCD practitioners a principled method to optimize gauge-fixing schemes for specific tasks, including noise reduction via contour deformations and precision RI-MOM renormalization.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Outlook</strong><br/><span style="color:#374151;">Future work could extend this approach to richer gauge functionals and integrate learned schemes with normalizing-flow samplers. This preprint (MIT-CTP/5786) was presented at LATTICE2024 in Liverpool. [[arXiv:2410.03602](https://arxiv.org/abs/2410.03602)]

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Exploring gauge-fixing conditions with gradient-based optimization</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[arXiv:2410.03602](https://arxiv.org/abs/2410.03602)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["William Detmold", "Gurtej Kanwar", "Yin Lin", "Phiala E. Shanahan", "Michael L. Wagman"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Lattice gauge fixing is required to compute gauge-variant quantities, for example those used in RI-MOM renormalization schemes or as objects of comparison for model calculations. Recently, gauge-variant quantities have also been found to be more amenable to signal-to-noise optimization using contour deformations. These applications motivate systematic parameterization and exploration of gauge-fixing schemes. This work introduces a differentiable parameterization of gauge fixing which is broad enough to cover Landau gauge, Coulomb gauge, and maximal tree gauges. The adjoint state method allows gradient-based optimization to select gauge-fixing schemes that minimize an arbitrary target loss function.</span></div></div>
</div>
