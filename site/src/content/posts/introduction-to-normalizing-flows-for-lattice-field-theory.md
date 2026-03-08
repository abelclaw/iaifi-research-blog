---
abstract: This notebook tutorial demonstrates a method for sampling Boltzmann distributions
  of lattice field theories using a class of machine learning models known as normalizing
  flows. The ideas and approaches proposed in arXiv:1904.12072, arXiv:2002.02428,
  and arXiv:2003.06413 are reviewed and a concrete implementation of the framework
  is presented. We apply this framework to a lattice scalar field theory and to U(1)
  gauge theory, explicitly encoding gauge symmetries in the flow-based approach to
  the latter. This presentation is intended to be interactive and working with the
  attached Jupyter notebook is recommended.
arxivId: '2101.08176'
arxivUrl: https://arxiv.org/abs/2101.08176
authors:
- Michael S. Albergo
- Denis Boyda
- Daniel C. Hackett
- Gurtej Kanwar
- Kyle Cranmer
- Sébastien Racanière
- Danilo Jimenez Rezende
- Phiala E. Shanahan
concepts:
- normalizing flows
- lattice gauge theory
- equivariant neural networks
- monte carlo methods
- symmetry preservation
- quantum field theory
- coupling layers
- density estimation
- generative models
- lattice qcd
- bayesian inference
figures:
- /iaifi-research-blog/figures/2101_08176/figure_1.png
- /iaifi-research-blog/figures/2101_08176/figure_1.png
- /iaifi-research-blog/figures/2101_08176/figure_2.png
- /iaifi-research-blog/figures/2101_08176/figure_2.png
- /iaifi-research-blog/figures/2101_08176/figure_3.png
- /iaifi-research-blog/figures/2101_08176/figure_3.png
pdfUrl: https://arxiv.org/pdf/2101.08176v3
published: '2021-01-20T15:16:28+00:00'
theme: Theoretical Physics
title: Introduction to Normalizing Flows for Lattice Field Theory
wordCount: 1137
---

## The Big Picture

Imagine describing thousands of subatomic particles at once, not just tracking their positions but capturing every possible configuration they might be in, weighted by probability. In quantum field theory, the branch of physics governing how fundamental particles arise and interact, this is the actual problem physicists face every time they want to make a prediction.

The traditional tools are running out of road.

For decades, physicists have relied on **Markov Chain Monte Carlo (MCMC)**, a random walk through an enormous space of possible physical configurations, guided by the laws of physics. Picture a hiker mapping a vast, foggy mountain range one careful step at a time, always favoring more plausible terrain. It works, but it's slow.

Near **phase transitions**, the moments when matter changes its fundamental character, like water freezing into ice, MCMC gets stuck. The random walk takes exponentially longer to explore relevant configurations, a problem known as **critical slowing down**. The field has been searching for something faster.

A team from MIT, NYU, DeepMind, and Argonne National Laboratory has now written a detailed tutorial showing how **normalizing flows**, a class of machine learning models, can fill that role. Instead of a random walk, these models generate realistic field configurations directly, in a single step, on a computational **lattice** (a grid that discretizes space so the physics becomes computable). The researchers show how to encode **gauge symmetry**, the mathematical constraint that certain transformations leave the physics unchanged, directly into the model's architecture.

> **Key Insight:** Normalizing flows learn to map simple random noise directly into physically meaningful field configurations, bypassing the slow random walk of traditional MCMC, with gauge symmetry baked into the model's structure from the start.

## How It Works

Rather than stumbling through configuration space step by step, a normalizing flow learns a smooth transformation, a change of variables, that maps a simple, easy-to-sample distribution (like a Gaussian) into something matching the target physics.

Think of a rubber sheet. Start flat and featureless (your simple starting distribution). A normalizing flow stretches, compresses, and folds it until it matches the complicated shape of your target. Because the transformation is invertible and differentiable, you can track exactly how much any region gets stretched. That's the **Jacobian factor**, the mathematical measure of how volumes change under a transformation, and it lets you compute the exact probability density of any sample you draw.

![Figure 1](/iaifi-research-blog/figures/2101_08176/figure_1.png)

The practical challenge is building flows that are both expressive and computationally cheap. The answer here is **coupling layers**, a modular approach to constructing the flow in stages.

Split the field variables into two groups. One group passes through unchanged. The other gets transformed using functions of the first group, giving the whole layer's Jacobian a special triangular structure. Computing it then reduces to multiplying diagonal entries rather than performing a full matrix operation. Stack enough coupling layers and the composite flow can approximate arbitrarily complex distributions.

For scalar field theory on a 2D lattice, training proceeds in four steps:

1. Draw samples from a simple Gaussian prior.
2. Pass them through the normalizing flow to get candidate field configurations.
3. Compare the output distribution to the target **Boltzmann distribution**, the physics-derived probability law assigning lower probability to higher-energy configurations, using **KL divergence**, a measure of how far apart two distributions are.
4. Backpropagate through the entire flow to update its parameters.

After training, the flow generates independent, nearly correct samples in a single forward pass. Any residual errors get corrected by using the flow samples as proposals in a standard MCMC step, guaranteeing exact statistics even if the learned approximation isn't perfect.

![Figure 2](/iaifi-research-blog/figures/2101_08176/figure_1.png)

The gauge theory case raises a harder problem. For **U(1) gauge theory**, the simplest example of a theory with point-to-point symmetry, the field lives not on real numbers but on the circle (angles from 0 to 2π), and the physics must be invariant under local gauge transformations. A naive flow would ignore this structure entirely, wasting model capacity on configurations that are physically identical.

The solution is architectural. The paper introduces **gauge-equivariant coupling layers** that, by construction, always produce outputs respecting gauge symmetry regardless of their inputs. These layers build their transformations from **plaquettes**, the smallest closed loops on the lattice grid and the fundamental building blocks of gauge-invariant physics, so the learned distribution automatically respects gauge invariance. The model never needs to learn what gauge symmetry is; it comes for free.

![Figure 3](/iaifi-research-blog/figures/2101_08176/figure_2.png)

## Why It Matters

The stakes extend well beyond any single calculation. Lattice quantum chromodynamics (QCD), the theory of quarks and gluons governing the strong nuclear force, is the primary tool for first-principles predictions about protons, neutrons, and nuclear matter. Those calculations run on some of the world's largest supercomputers and are extraordinarily expensive.

If normalizing flows can replace or accelerate the sampling step, the payoff is large: faster calculations, access to parameter regimes where MCMC breaks down entirely, and the ability to study phenomena near phase transitions that are currently out of reach.

The tutorial format matters too. By releasing a working Jupyter notebook alongside the mathematical exposition, the authors lower the barrier for physicists to experiment with these methods, and for machine learning researchers to engage with the specific challenges of physical symmetry and gauge invariance. The explicit treatment of U(1) gauge theory lays groundwork for tackling SU(2) and SU(3), the more complex symmetry groups governing the strong force.

![Figure 4](/iaifi-research-blog/figures/2101_08176/figure_2.png)

Open questions remain. Current implementations work on small lattices; scaling to the large volumes needed for precision QCD is an unsolved engineering challenge. Training costs are high, and it's not yet clear how they compare to the gains at production scale. But the framework is in place, and the community now has a hands-on guide to building on it.

> **Bottom Line:** This tutorial makes normalizing flows accessible to the lattice field theory community, showing how machine learning models can generate field configurations that respect physical symmetries, a potential step change for some of the most computationally demanding calculations in particle physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits at the intersection of probabilistic machine learning and quantum field theory, embedding gauge symmetry constraints into neural network architectures to make ML-based samplers physically meaningful.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper advances normalizing flow methodology by showing how to encode continuous symmetry groups, specifically U(1) local gauge invariance, as hard architectural constraints rather than soft training objectives.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Flow-based sampling offers a path beyond critical slowing down in lattice QCD, potentially enabling first-principles calculations of hadronic properties at parameter regimes inaccessible to traditional MCMC.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will need to scale these methods to SU(3) gauge theory and larger lattice volumes; the foundational approaches are detailed in [arXiv:2101.08176](https://arxiv.org/abs/2101.08176) and prior works [arXiv:1904.12072](https://arxiv.org/abs/1904.12072), [arXiv:2002.02428](https://arxiv.org/abs/2002.02428), and [arXiv:2003.06413](https://arxiv.org/abs/2003.06413).</span></div></div>
</div>
