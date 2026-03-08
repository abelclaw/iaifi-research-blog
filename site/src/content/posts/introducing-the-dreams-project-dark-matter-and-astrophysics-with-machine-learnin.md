---
abstract: We introduce the DREAMS project, an innovative approach to understanding
  the astrophysical implications of alternative dark matter models and their effects
  on galaxy formation and evolution. The DREAMS project will ultimately comprise thousands
  of cosmological hydrodynamic simulations that simultaneously vary over dark matter
  physics, astrophysics, and cosmology in modeling a range of systems -- from galaxy
  clusters to ultra-faint satellites. Such extensive simulation suites can provide
  adequate training sets for machine-learning-based analyses. This paper introduces
  two new cosmological hydrodynamical suites of Warm Dark Matter, each comprised of
  1024 simulations generated using the Arepo code. One suite consists of uniform-box
  simulations covering a $(25~h^{-1}~{\rm M}_\odot)^3$ volume, while the other consists
  of Milky Way zoom-ins with sufficient resolution to capture the properties of classical
  satellites. For each simulation, the Warm Dark Matter particle mass is varied along
  with the initial density field and several parameters controlling the strength of
  baryonic feedback within the IllustrisTNG model. We provide two examples, separately
  utilizing emulators and Convolutional Neural Networks, to demonstrate how such simulation
  suites can be used to disentangle the effects of dark matter and baryonic physics
  on galactic properties. The DREAMS project can be extended further to include different
  dark matter models, galaxy formation physics, and astrophysical targets. In this
  way, it will provide an unparalleled opportunity to characterize uncertainties on
  predictions for small-scale observables, leading to robust predictions for testing
  the particle physics nature of dark matter on these scales.
arxivId: '2405.00766'
arxivUrl: https://arxiv.org/abs/2405.00766
authors:
- Jonah C. Rose
- Paul Torrey
- Francisco Villaescusa-Navarro
- Mariangela Lisanti
- Tri Nguyen
- Sandip Roy
- Kassidy E. Kollmann
- Mark Vogelsberger
- Francis-Yan Cyr-Racine
- Mikhail V. Medvedev
- Shy Genel
- Daniel Anglés-Alcázar
- Nitya Kallivayalil
- Bonny Y. Wang
- Belén Costanza
- Stephanie O'Neil
- Cian Roche
- Soumyodipta Karmakar
- Alex M. Garcia
- Ryan Low
- Shurui Lin
- Olivia Mostow
- Akaxia Cruz
- Andrea Caputo
- Arya Farahi
- Julian B. Muñoz
- Lina Necib
- Romain Teyssier
- Julianne J. Dalcanton
- David Spergel
concepts:
- dark matter
- cosmological simulation
- warm dark matter models
- baryonic feedback
- emulation
- convolutional networks
- simulation-based inference
- uncertainty quantification
- surrogate modeling
- bayesian inference
- galaxy classification
- dark energy
figures:
- /iaifi-research-blog/figures/2405_00766/figure_1.png
- /iaifi-research-blog/figures/2405_00766/figure_1.png
- /iaifi-research-blog/figures/2405_00766/figure_2.png
- /iaifi-research-blog/figures/2405_00766/figure_2.png
- /iaifi-research-blog/figures/2405_00766/figure_3.png
- /iaifi-research-blog/figures/2405_00766/figure_3.png
pdfUrl: https://arxiv.org/pdf/2405.00766v1
published: '2024-05-01T18:00:00+00:00'
theme: Astrophysics
title: 'Introducing the DREAMS Project: DaRk mattEr and Astrophysics with Machine
  learning and Simulations'
wordCount: 1355
---

## The Big Picture

Imagine trying to identify a single spice in a complex dish when you don't know how much salt, pepper, or garlic was added. That's the challenge physicists face when trying to detect dark matter through its influence on galaxies. Dark matter shapes how galaxies form and grow, but so does the messy, turbulent physics of exploding stars and feeding black holes. Separating these signals has been one of astrophysics' most stubborn problems.

Dark matter makes up roughly 27% of the universe's total energy content, yet we've never directly detected a single particle of it. Our best clue is how it sculpts the universe at small scales: the number of tiny satellite galaxies orbiting the Milky Way, the density of galactic cores, the structure of vast filaments connecting galaxies across space. Different dark matter models predict different structures.

Exploding stars blast gas out of small galaxies, erasing the very structures dark matter built. Supermassive black holes at galactic centers belch radiation that heats and scatters surrounding material. These processes can produce the same patterns we'd expect from certain types of dark matter. You can't identify your suspect if they're wearing someone else's disguise.

A new collaboration called the DREAMS project, short for **DaRk mattEr and Astrophysics with Machine learning and Simulations**, is building the toolkit to untangle these effects. The idea: run thousands of cosmological simulations, vary everything simultaneously, and let machine learning find the patterns.

> **Key Insight:** By running over 2,000 simulations that vary both dark matter properties and astrophysical feedback together, DREAMS gives machine learning models enough data to separate dark matter signatures from the noise of ordinary physics.

## How It Works

Rather than running a handful of carefully chosen simulations, the DREAMS team built entire **simulation suites**, massive collections where each run uses a different combination of dark matter and ordinary-matter physics parameters. This paper introduces two such suites, each containing 1,024 simulations, all targeting **Warm Dark Matter (WDM)**, a dark matter variant where particles move fast enough to smooth out small-scale structure.

![Figure 1](/iaifi-research-blog/figures/2405_00766/figure_1.png)

The simulations use **Arepo**, a moving-mesh hydrodynamics code, paired with the **IllustrisTNG** galaxy formation model. Within each simulation, the team varies four parameters simultaneously:

- The **WDM particle mass** (ranging from values indistinguishable from cold dark matter down to particles warm enough to erase dwarf galaxies)
- The strength of **supernova feedback**, how vigorously exploding stars push gas out of galaxies
- The efficiency of **AGN feedback**, how powerfully supermassive black holes heat their surroundings
- The **initial density field**, the random seed for where matter clumps first form

That last one matters more than it might seem. A single parameter combination run with just one initial condition can be a statistical fluke. Running 1,024 simulations across the parameter space means machine learning models train on genuine trends rather than cosmic accidents.

The two suites serve different scientific purposes. The **uniform-box suite** simulates a 25 Mpc/h cube, a region roughly 100 million light-years across, capturing the large-scale statistics of galaxy populations. The **Milky Way zoom-in suite** focuses computational power on a single galaxy-sized halo, resolving the faint satellite galaxies most sensitive to warm dark matter's suppression of small-scale structure.

![Figure 3](/iaifi-research-blog/figures/2405_00766/figure_2.png)

The team then demonstrates two machine learning applications. First, they build an **emulator**: a neural network that learns to predict galaxy statistics as a smooth function of the input parameters, acting as a fast surrogate for expensive simulations. Second, they deploy a **Convolutional Neural Network (CNN)**, a type of AI that finds patterns in images, trained to infer the WDM particle mass directly from synthetic images of satellite galaxy populations.

In both cases, the test is whether the ML models correctly attribute observed features to dark matter rather than stellar or black hole physics. The answer is yes, but only when training data spans the full uncertainty in both.

![Figure 5](/iaifi-research-blog/figures/2405_00766/figure_3.png)

## Why It Matters

The next decade will bring a flood of small-scale observational data. The Vera Rubin Observatory will discover thousands of new ultra-faint dwarf galaxies. The Roman Space Telescope will image stellar streams in extraordinary detail. 21-cm surveys will map the cosmic web at new resolution. All of these observations carry potential dark matter fingerprints, but extracting those fingerprints requires exactly the kind of simulation-trained inference machinery that DREAMS is building.

The project's architecture is deliberately extensible. Warm dark matter is just the first target. The same framework can accommodate **Self-Interacting Dark Matter (SIDM)**, **fuzzy dark matter**, **dark photon models**, and whatever else theorists conjure. Each new dark matter model becomes another axis in the parameter space, another suite of simulations, another training set for new ML models.

There's a broader lesson here for astrophysics. Historically, simulation campaigns have been designed to match known observations. DREAMS inverts this: design the simulations to train models that can then *make* predictions and *test* theories. It's a shift from confirmation to discovery, and it works because machine learning can extract signal from parameter spaces too large for any human analyst to navigate by hand.

> **Bottom Line:** DREAMS delivers the first large-scale simulation suite purpose-built for machine learning inference of dark matter properties, showing that you can separate dark matter physics from baryonic uncertainty, but only if you vary both simultaneously and at scale.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">DREAMS sits at the intersection of particle physics theory, cosmological simulation, and modern machine learning, building training datasets specifically designed for neural network inference of fundamental dark matter properties from astrophysical observables.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Emulators and CNNs trained on diverse, multi-parameter simulation suites can disentangle correlated physical effects, a template for simulation-based inference in any domain where ground truth is expensive to compute.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By varying dark matter particle mass alongside baryonic feedback across 2,048 hydrodynamic simulations, DREAMS provides the theoretical infrastructure needed to turn observations of dwarf galaxies and satellite populations into genuine constraints on dark matter's particle nature.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future DREAMS suites will expand to cold dark matter, self-interacting models, and galaxy cluster targets, with public data releases planned; the paper is available at [arXiv:2405.00766](https://arxiv.org/abs/2405.00766).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Introducing the DREAMS Project: DaRk mattEr and Astrophysics with Machine learning and Simulations</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2405.00766</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Jonah C. Rose", "Paul Torrey", "Francisco Villaescusa-Navarro", "Mariangela Lisanti", "Tri Nguyen", "Sandip Roy", "Kassidy E. Kollmann", "Mark Vogelsberger", "Francis-Yan Cyr-Racine", "Mikhail V. Medvedev", "Shy Genel", "Daniel Anglés-Alcázar", "Nitya Kallivayalil", "Bonny Y. Wang", "Belén Costanza", "Stephanie O'Neil", "Cian Roche", "Soumyodipta Karmakar", "Alex M. Garcia", "Ryan Low", "Shurui Lin", "Olivia Mostow", "Akaxia Cruz", "Andrea Caputo", "Arya Farahi", "Julian B. Muñoz", "Lina Necib", "Romain Teyssier", "Julianne J. Dalcanton", "David Spergel"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We introduce the DREAMS project, an innovative approach to understanding the astrophysical implications of alternative dark matter models and their effects on galaxy formation and evolution. The DREAMS project will ultimately comprise thousands of cosmological hydrodynamic simulations that simultaneously vary over dark matter physics, astrophysics, and cosmology in modeling a range of systems -- from galaxy clusters to ultra-faint satellites. Such extensive simulation suites can provide adequate training sets for machine-learning-based analyses. This paper introduces two new cosmological hydrodynamical suites of Warm Dark Matter, each comprised of 1024 simulations generated using the Arepo code. One suite consists of uniform-box simulations covering a $(25~h^{-1}~{\rm M}_\odot)^3$ volume, while the other consists of Milky Way zoom-ins with sufficient resolution to capture the properties of classical satellites. For each simulation, the Warm Dark Matter particle mass is varied along with the initial density field and several parameters controlling the strength of baryonic feedback within the IllustrisTNG model. We provide two examples, separately utilizing emulators and Convolutional Neural Networks, to demonstrate how such simulation suites can be used to disentangle the effects of dark matter and baryonic physics on galactic properties. The DREAMS project can be extended further to include different dark matter models, galaxy formation physics, and astrophysical targets. In this way, it will provide an unparalleled opportunity to characterize uncertainties on predictions for small-scale observables, leading to robust predictions for testing the particle physics nature of dark matter on these scales.</span></div></div>
</div>
