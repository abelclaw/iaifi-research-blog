---
abstract: The connection between galaxies and their host dark matter (DM) halos is
  critical to our understanding of cosmology, galaxy formation, and DM physics. To
  maximize the return of upcoming cosmological surveys, we need an accurate way to
  model this complex relationship. Many techniques have been developed to model this
  connection, from Halo Occupation Distribution (HOD) to empirical and semi-analytic
  models to hydrodynamic. Hydrodynamic simulations can incorporate more detailed astrophysical
  processes but are computationally expensive; HODs, on the other hand, are computationally
  cheap but have limited accuracy. In this work, we present NeHOD, a generative framework
  based on variational diffusion model and Transformer, for painting galaxies/subhalos
  on top of DM with an accuracy of hydrodynamic simulations but at a computational
  cost similar to HOD. By modeling galaxies/subhalos as point clouds, instead of binning
  or voxelization, we can resolve small spatial scales down to the resolution of the
  simulations. For each halo, NeHOD predicts the positions, velocities, masses, and
  concentrations of its central and satellite galaxies. We train NeHOD on the TNG-Warm
  DM suite of the DREAMS project, which consists of 1024 high-resolution zoom-in hydrodynamic
  simulations of Milky Way-mass halos with varying warm DM mass and astrophysical
  parameters. We show that our model captures the complex relationships between subhalo
  properties as a function of the simulation parameters, including the mass functions,
  stellar-halo mass relations, concentration-mass relations, and spatial clustering.
  Our method can be used for a large variety of downstream applications, from galaxy
  clustering to strong lensing studies.
arxivId: '2409.02980'
arxivUrl: https://arxiv.org/abs/2409.02980
authors:
- Tri Nguyen
- Francisco Villaescusa-Navarro
- Siddharth Mishra-Sharma
- Carolina Cuesta-Lazaro
- Paul Torrey
- Arya Farahi
- Alex M. Garcia
- Jonah C. Rose
- Stephanie O'Neil
- Mark Vogelsberger
- Xuejian Shen
- Cian Roche
- Daniel Anglés-Alcázar
- Nitya Kallivayalil
- Julian B. Muñoz
- Francis-Yan Cyr-Racine
- Sandip Roy
- Lina Necib
- Kassidy E. Kollmann
concepts:
- diffusion models
- dark matter
- emulation
- galaxy-halo connection
- generative models
- cosmological simulation
- point cloud modeling
- transformers
- surrogate modeling
- simulation-based inference
- posterior estimation
- scalability
figures:
- /iaifi-research-blog/figures/2409_02980/figure_1.png
- /iaifi-research-blog/figures/2409_02980/figure_1.png
- /iaifi-research-blog/figures/2409_02980/figure_2.png
- /iaifi-research-blog/figures/2409_02980/figure_2.png
- /iaifi-research-blog/figures/2409_02980/figure_3.png
- /iaifi-research-blog/figures/2409_02980/figure_3.png
pdfUrl: https://arxiv.org/pdf/2409.02980v1
published: '2024-09-04T18:00:00+00:00'
theme: Astrophysics
title: 'How DREAMS are made: Emulating Satellite Galaxy and Subhalo Populations with
  Diffusion Models and Point Clouds'
wordCount: 1022
---

## The Big Picture

Imagine understanding traffic patterns in a city. You could deploy sensors everywhere, run a full physics simulation of every car, or use a statistical model trained on real data to generate realistic flows in seconds. Cosmologists face a similar problem: they need to know how galaxies cluster around **dark matter halos** (vast, invisible clumps of dark matter that act as gravitational scaffolding), but the most accurate tool available, **hydrodynamic simulations**, burns through computing resources at a staggering rate. These are supercomputer programs that model the full physics of gas, stars, and dark matter simultaneously.

The stakes are real. Rubin Observatory, the Roman Space Telescope, and DESI will soon deliver data on billions of galaxies. To extract physics from those observations, theorists need fast, accurate models of how galaxies populate dark matter halos. The gap between "fast but crude" and "accurate but slow" has been a stubborn bottleneck.

A team led by Tri Nguyen at MIT, with collaborators across IAIFI, Princeton, Harvard, and Flatiron, has built something that breaks that tradeoff: **NeHOD**, a neural network that generates realistic galaxy populations with hydrodynamic fidelity at a fraction of the computational cost.

> **Key Insight:** NeHOD uses a diffusion model and Transformer to generate satellite galaxy populations as point clouds, achieving hydrodynamic-level accuracy while remaining as fast as traditional statistical models.

## How It Works

The traditional workhorse for placing galaxies in simulations is the **Halo Occupation Distribution (HOD)**, a set of statistical rules that say, roughly, "a halo of this mass probably hosts this many galaxies." It's fast, but it ignores spatial detail and the influence of **baryonic physics**, processes involving ordinary matter like supernova explosions blowing gas out of galaxies. At the other extreme, hydrodynamic simulations solve full fluid dynamics equations for gas, stars, and dark matter all at once. Beautiful physics, but a single run can take millions of CPU hours.

NeHOD sits between these extremes. It learns the mapping from dark matter halo properties to galaxy populations by training on 1,024 high-resolution **zoom-in simulations** from the **DREAMS project** (the TNG-Warm DM suite). Zoom-in simulations concentrate computing power on a single halo, and in this case they all model Milky Way-mass halos while varying two key parameters: warm dark matter particle mass and astrophysical feedback strength.

![Figure 1](/iaifi-research-blog/figures/2409_02980/figure_1.png)

The architecture has two interlocking pieces:

1. **A Transformer encoder** reads the dark matter halo as a cloud of particle positions and compresses it into a compact summary of the halo's structure, mass profile, and shape.
2. **A variational diffusion model** generates the satellite galaxy population conditioned on that summary and the simulation parameters. It learns to turn random noise into structured data step by step, iteratively refining a set of points into realistic galaxy positions, velocities, stellar masses, and concentration parameters.

Treating galaxies as a **point cloud** (individual points in space rather than values on a fixed grid) lets NeHOD avoid the resolution limits that constrain grid-based approaches. It resolves spatial scales down to the simulation's native resolution, which is critical for studying small satellite galaxies orbiting close to their host.

![Figure 3](/iaifi-research-blog/figures/2409_02980/figure_2.png)

NeHOD correctly reproduces the key statistics of satellite galaxy populations: the **subhalo mass function**, the **stellar-to-halo mass relation**, the **concentration-mass relation**, and **spatial clustering statistics**, all as a function of the simulation parameters. When warm dark matter is lighter and suppresses small-scale structure, NeHOD generates fewer low-mass satellites. When feedback parameters change, it adjusts stellar masses accordingly.

The model also captures correlations between properties that simpler models miss. In a real galaxy system, a satellite's position, velocity, mass, and concentration all co-evolved under the same gravitational and baryonic forces. The diffusion model learns these joint distributions implicitly, with no need for the researcher to specify them by hand.

![Figure 5](/iaifi-research-blog/figures/2409_02980/figure_3.png)

The computational payoff is large: populating a halo with NeHOD takes seconds on a GPU. The equivalent hydrodynamic simulation takes months on a supercomputer cluster.

## Why It Matters

This work connects two major efforts in modern cosmology. Surveys like SAGA and ELVES are already cataloging satellite galaxies around Milky Way analogs, with Rubin and Roman set to expand that census by orders of magnitude. At the same time, physicists are hunting for signatures of **warm dark matter**, a hypothetical variant whose fast-moving particles would smooth out small clumps and leave detectable gaps in satellite galaxy counts. Detecting that signal requires running thousands of forward models across wide parameter spaces, and only a fast emulator like NeHOD makes that feasible.

Accurate subhalo populations also open doors for **strong gravitational lensing** studies, where a massive galaxy bends light from a distant source into arcs or rings. The exact pattern depends on the detailed matter distribution, including small satellites. They matter equally for **satellite kinematics**, using dwarf galaxy motions to infer the mass profile of their host halo. The authors flag both as target applications.

There is a broader lesson here too. Point-cloud diffusion models, borrowed from machine learning's work on 3D object generation, turn out to be a natural fit for astrophysical structures that are inherently sparse and irregular in space.

> **Bottom Line:** NeHOD delivers hydrodynamic-quality galaxy populations at HOD-level speed, unlocking fast, parameter-spanning exploration of dark matter physics and galaxy formation with a neural generative model trained on the DREAMS simulation suite.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges modern deep learning (variational diffusion models and Transformers from computer vision and NLP) with astrophysical simulation, showing that point-cloud generative models can emulate complex hydrodynamic outputs with high fidelity.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">NeHOD introduces a novel application of conditional variational diffusion models to scientific data, showing that the architecture can learn correlated, multi-property distributions over variable-size point sets conditioned on physical parameters.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling fast, accurate emulation of satellite galaxy populations across warm dark matter and baryonic parameter spaces, this framework accelerates the search for observational signatures of dark matter's particle nature.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions could apply NeHOD to larger cosmological volumes, additional dark matter models, or observational mock catalogs for upcoming surveys like Rubin LSST. The paper is available at [arXiv:2409.02980](https://arxiv.org/abs/2409.02980).</span></div></div>
</div>
