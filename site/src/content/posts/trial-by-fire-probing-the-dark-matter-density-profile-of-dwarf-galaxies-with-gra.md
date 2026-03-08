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
wordCount: 1087
---

## The Big Picture

Imagine trying to weigh an invisible object by watching how visible objects orbit around it. That's essentially what astronomers do when studying dark matter in dwarf galaxies — inferring the mass of something that emits no light and interacts with ordinary matter only through gravity. The stars in these tiny galaxies become the detectives, and their velocities tell the story.

Dwarf galaxies orbiting the Milky Way are among the most dark-matter-dominated objects in the universe. They're also extraordinary laboratories: small enough that exploding stars barely disturb their dark matter distribution, close enough to measure individual stellar velocities, and numerous enough to provide statistical power.

The shape of the dark matter density profile — whether it rises steeply toward the center (a "cusp") or flattens out (a "core") — carries a fingerprint of dark matter's fundamental nature. Cold dark matter predicts cusps; self-interacting dark matter predicts cores. Getting this measurement right is one of the key tests of dark matter theory.

A team led by Tri Nguyen has now put a powerful new tool to a rigorous trial: applying **GraphNPE** (Graph Neural Posterior Estimator) to realistic simulated dwarf galaxies from the FIRE-2 simulation suite — highly detailed computer models of galaxies — demonstrating that machine learning can outperform classical methods and recover dark matter properties with impressive precision, even from tiny stellar samples.

> **Key Insight:** GraphNPE recovers dark matter density profiles and key halo properties from as few as 30 stellar velocity measurements, outperforming traditional dynamical modeling while working across both cold and self-interacting dark matter scenarios.

## How It Works

The classical approach uses **Jeans modeling** — a century-old technique that relates the spread of stellar velocities to a galaxy's gravitational pull. Think of it like measuring gas pressure to infer temperature. Jeans modeling works, but it bakes in assumptions: spherical symmetry, dynamical equilibrium (the galaxy isn't being shaken by outside forces), and a particular mathematical profile. Real dwarf galaxies, yanked around by the Milky Way's gravity and shaped by billions of years of complex evolution, often violate these assumptions.

GraphNPE takes a fundamentally different approach. Rather than fitting a pre-specified mathematical model to the data, it uses **simulation-based inference** — training a neural network on thousands of simulated galaxies to learn the relationship between observable stellar kinematics and underlying dark matter structure. Two components do the heavy lifting:

- A **graph neural network** treats each observed star as a node, passing information between neighbors to extract collective kinematic patterns without assuming any particular geometry
- A **normalizing flow** — a tool that reshapes a simple probability distribution into a complex one — converts those patterns into a full posterior over which dark matter density profiles are most consistent with the observations

![Figure 1](/iaifi-research-blog/figures/2503_03812/figure_1.png)

The training data comes from idealized mock observations where the ground-truth dark matter profile is known. The researchers then tested GraphNPE on a much harder dataset: satellite dwarf galaxies from the **FIRE-2 Latte simulations**, high-resolution cosmological models of a full Milky Way-sized galaxy and its satellites in realistic detail. These are messy galaxies experiencing tidal stripping (stars pulled away by the Milky Way's gravity), supernova explosions, and environmental interactions. Some have cusps; some have cores; some have been structurally scrambled by close passages near the Milky Way.

![Figure 3](/iaifi-research-blog/figures/2503_03812/figure_2.png)

The results are striking. GraphNPE recovers the dark matter density profile within its 95% confidence interval for the vast majority of systems — including those heavily tidally disrupted. For peak circular velocity $V_\text{max}$, accuracy reaches 10–20%. For peak virial mass $M_{200m}^\text{peak}$ — the total mass the dark matter halo reached at its most massive point — accuracy ranges from 0.1 to 0.4 dex (roughly a factor of 1.25 to 2.5). Crucially, over 92% of all systems fall within their 95% confidence intervals, meaning the uncertainty estimates are well-calibrated, not just optimistically tight.

## Why It Matters

The core-cusp problem has haunted dark matter physics for three decades. Simulations of cold dark matter consistently predict steeply rising central density profiles, while observations of many dwarf galaxies suggest flatter cores. Is this evidence that dark matter self-interacts? Or are energetic outflows from star formation doing the sculpting?

Answering that question requires a measurement tool that recovers density profiles without introducing its own systematic biases. Jeans modeling carries known systematic errors that can blur the distinction between cusps and cores.

GraphNPE offers a path forward. By training on simulations that include realistic baryonic physics — the complex interplay of gas, stars, and supernova explosions — the method implicitly learns to account for deviations from idealized assumptions. This paper is the first rigorous benchmark of a simulation-based inference approach for mass modeling against FIRE-2 simulations, tested across both cold and self-interacting dark matter scenarios. The finding that it works well even for tidally disrupted systems — where classical methods often fail — is particularly valuable, since many of the most interesting Milky Way satellites are in exactly this regime.

![Figure 5](/iaifi-research-blog/figures/2503_03812/figure_3.png)

With next-generation surveys like the Rubin Observatory's LSST poised to discover thousands of new dwarf galaxies and measure tens of thousands of stellar velocities, tools like GraphNPE will be essential for converting that data into dark matter constraints.

> **Bottom Line:** GraphNPE passes its trial by FIRE: tested against realistic cosmological simulations, this graph neural network approach recovers dark matter halo properties with 10–20% accuracy from stellar velocities alone, establishing it as a credible tool for distinguishing between competing dark matter models using the Milky Way's dwarf galaxy population.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies modern deep learning architectures — graph neural networks combined with normalizing flows — to a foundational problem in observational cosmology, demonstrating that simulation-based inference can replace and outperform century-old dynamical modeling techniques in dark matter astrophysics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">GraphNPE advances the use of graph neural networks for astronomical data by treating sets of stellar observations as graphs rather than fixed-dimensional inputs, enabling the model to handle variable sample sizes and irregular spatial distributions without hand-crafted features.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By reliably distinguishing density profiles consistent with cold versus self-interacting dark matter — even in realistically complex, tidally disturbed systems — this method provides a new tool for constraining the particle properties of dark matter from galactic-scale observations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions to non-spherical and disequilibrium models could unlock constraints from a much wider range of dwarf galaxies; the paper is available on arXiv (submitted August 2025) from the IAIFI collaboration at MIT and partner institutions.</span></div></div>
</div>
