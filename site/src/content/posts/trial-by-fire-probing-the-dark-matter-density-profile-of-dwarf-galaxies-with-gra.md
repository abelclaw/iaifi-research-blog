---
abstract: 'The Dark Matter (DM) distribution in dwarf galaxies provides crucial insights
  into both structure formation and the particle nature of DM. GraphNPE (Graph Neural
  Posterior Estimator), first introduced in Nguyen et al. (2023), is a novel simulation-based
  inference framework that combines graph neural networks and normalizing flows to
  infer the DM density profile from line-of-sight stellar velocities. Here, we apply
  GraphNPE to satellite dwarf galaxies in the FIRE-2 Latte simulation suite of Milky
  Way-mass halos, testing it against both Cold and Self-Interacting DM scenarios.
  Our method demonstrates superior precision compared to conventional Jeans-based
  approaches, recovering DM density profiles to within the 95% confidence level even
  in systems with as few as 30 tracers. Moreover, we present the first evaluation
  of mass modeling methods in constraining two key parameters from realistic simulations:
  the peak circular velocity, $V_\mathrm{max}$, and the peak virial mass, $M_\mathrm{200m}^\mathrm{peak}$.
  Using only line-of-sight velocities, GraphNPE can reliably recover both $V_\mathrm{max}$
  and $M_\mathrm{200m}^\mathrm{peak}$ within our quoted uncertainties, including those
  experiencing tidal effects ($\gtrsim$ 63% of systems are recovered with our 68%
  confidence intervals and $\gtrsim$ 92% within our 95% confidence intervals). The
  method achieves 10-20% accuracy in $V_\mathrm{max}$ recovery, while $M_\mathrm{200m}^\mathrm{peak}$
  is recovered to 0.1-0.4 dex accuracy. This work establishes GraphNPE as a robust
  tool for inferring DM density profiles in dwarf galaxies, offering promising avenues
  for constraining DM models. The framework''s potential extends beyond this study,
  as it can be adapted to non-spherical and disequilibrium models, showcasing the
  broader utility of simulation-based inference and graph-based learning in astrophysics.'
arxivId: '2503.03812'
arxivUrl: https://arxiv.org/abs/2503.03812
authors:
- Tri Nguyen
- Justin Read
- Lina Necib
- Siddharth Mishra-Sharma
- Claude-André Faucher-Giguère
- Andrew Wetzel
- Tjitske K Starkenburg
concepts:
- simulation-based inference
- dark matter
- graph neural networks
- normalizing flows
- posterior estimation
- cosmological simulation
- stellar kinematics inference
- bayesian inference
- uncertainty quantification
- inverse problems
- geometric deep learning
- density estimation
figures:
- /iaifi-research-blog/figures/2503_03812/figure_1.png
- /iaifi-research-blog/figures/2503_03812/figure_1.png
- /iaifi-research-blog/figures/2503_03812/figure_2.png
- /iaifi-research-blog/figures/2503_03812/figure_2.png
- /iaifi-research-blog/figures/2503_03812/figure_3.png
- /iaifi-research-blog/figures/2503_03812/figure_3.png
pdfUrl: https://arxiv.org/pdf/2503.03812v2
published: '2025-03-05T19:00:00+00:00'
theme: Astrophysics
title: 'Trial by FIRE: Probing the dark matter density profile of dwarf galaxies with
  GraphNPE'
wordCount: 1014
---

## The Big Picture

Imagine trying to weigh an invisible object by watching how visible objects orbit around it. That's what astronomers do when studying dark matter in dwarf galaxies: inferring the mass of something that emits no light by tracking the velocities of stars caught in its gravitational pull.

Dwarf galaxies orbiting the Milky Way are among the most dark-matter-dominated objects in the universe. They also happen to be extraordinary laboratories. They're small enough that exploding stars barely disturb their dark matter distribution, close enough that we can measure individual stellar velocities, and numerous enough to provide real statistical power.

The shape of the dark matter density profile carries a fingerprint of dark matter's particle nature. Does the density rise steeply toward the center (a "cusp") or flatten out (a "core")? Cold dark matter predicts cusps. Self-interacting dark matter predicts cores. Getting this measurement right is one of the defining tests of dark matter theory.

A team led by Tri Nguyen has now put a powerful new tool through a rigorous trial: applying **GraphNPE** (Graph Neural Posterior Estimator) to realistic simulated dwarf galaxies from the FIRE-2 simulation suite, and showing that machine learning can outperform classical methods at recovering dark matter properties, even from tiny stellar samples.

> **Key Insight:** GraphNPE recovers dark matter density profiles and key halo properties from as few as 30 stellar velocity measurements, outperforming traditional dynamical modeling while working across both cold and self-interacting dark matter scenarios.

## How It Works

The classical approach uses **Jeans modeling**, a century-old technique that relates the spread of stellar velocities to a galaxy's gravitational pull. Think of it like measuring gas pressure to infer temperature. It works, but it bakes in assumptions: spherical symmetry, dynamical equilibrium, and a particular mathematical form for the density profile. Real dwarf galaxies, yanked around by the Milky Way's gravity and shaped by billions of years of messy evolution, routinely violate these assumptions.

GraphNPE sidesteps this problem entirely. Instead of fitting a pre-specified model to the data, it uses **simulation-based inference**: a neural network trained on thousands of simulated galaxies learns the relationship between observable stellar kinematics and underlying dark matter structure. Two components do the heavy lifting:

- A **graph neural network** treats each observed star as a node, passing information between neighbors to extract collective kinematic patterns without assuming any particular geometry
- A **normalizing flow** converts those patterns into a full posterior distribution over dark matter density profiles consistent with the observations

![Figure 1](/iaifi-research-blog/figures/2503_03812/figure_1.png)

Training data comes from idealized mock observations where the ground-truth dark matter profile is known. The real test, though, uses satellite dwarf galaxies from the **FIRE-2 Latte simulations**: high-resolution cosmological models of a full Milky Way-sized galaxy and its satellites. These are messy systems experiencing tidal stripping (stars pulled away by the Milky Way's gravity), supernova feedback, and environmental interactions. Some have cusps, some have cores, and some have been structurally scrambled by close passages near the Milky Way.

![Figure 3](/iaifi-research-blog/figures/2503_03812/figure_2.png)

The results speak for themselves. GraphNPE recovers the dark matter density profile within its 95% confidence interval for the vast majority of systems, including heavily tidally disrupted ones. For peak circular velocity $V_\text{max}$, accuracy reaches 10–20%. For peak virial mass $M_{200m}^\text{peak}$, accuracy ranges from 0.1 to 0.4 dex (roughly a factor of 1.25 to 2.5). Over 92% of all systems fall within their 95% confidence intervals, meaning the uncertainty estimates are well-calibrated rather than just optimistically tight.

## Why It Matters

The core-cusp problem has haunted dark matter physics for three decades. Simulations of cold dark matter consistently predict steeply rising central density profiles, while observations of many dwarf galaxies suggest flatter cores. Is this evidence that dark matter self-interacts? Or do energetic outflows from star formation sculpt the profiles instead?

Answering that question requires a measurement tool that recovers density profiles without introducing its own systematic biases. Jeans modeling carries known systematics that can blur the distinction between cusps and cores.

GraphNPE offers a way around this. Because it trains on simulations that include realistic baryonic physics (the complex interplay of gas, stars, and supernovae), the method implicitly learns to handle deviations from idealized assumptions. This paper is the first rigorous benchmark of simulation-based inference for mass modeling against FIRE-2 simulations, tested across both cold and self-interacting dark matter scenarios. That it works well even for tidally disrupted systems, where classical methods often break down, matters a great deal: many of the most interesting Milky Way satellites live in exactly this regime.

![Figure 5](/iaifi-research-blog/figures/2503_03812/figure_3.png)

With next-generation surveys like the Rubin Observatory's LSST set to discover thousands of new dwarf galaxies and measure tens of thousands of stellar velocities, tools like GraphNPE will be needed to convert that flood of data into dark matter constraints.

> **Bottom Line:** GraphNPE passes its trial by FIRE: tested against realistic cosmological simulations, this graph neural network approach recovers dark matter halo properties with 10–20% accuracy from stellar velocities alone, making it a credible tool for distinguishing between competing dark matter models using the Milky Way's dwarf galaxy population.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work brings modern deep learning architectures (graph neural networks combined with normalizing flows) to bear on a foundational problem in observational cosmology. Simulation-based inference can now replace and outperform century-old dynamical modeling techniques for dark matter astrophysics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">GraphNPE treats sets of stellar observations as graphs rather than fixed-dimensional inputs, allowing it to handle variable sample sizes and irregular spatial distributions without hand-crafted features. This is a natural fit for astronomical datasets, where the number of observed stars varies widely from galaxy to galaxy.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By reliably distinguishing density profiles consistent with cold versus self-interacting dark matter, even in tidally disturbed systems, this method provides a new handle on the particle properties of dark matter from galactic-scale observations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions to non-spherical and disequilibrium models could open up constraints from a much wider range of dwarf galaxies. The paper is available at [arXiv:2503.03812](https://arxiv.org/abs/2503.03812), from the IAIFI collaboration at MIT and partner institutions.</span></div></div>
</div>
