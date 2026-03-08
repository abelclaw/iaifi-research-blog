---
abstract: Astrophysical searches for dark matter in the Milky Way require a reliable
  model for its density distribution, which in turn depends on the influence of baryonic
  feedback on the Galaxy. In this work, we utilize a new suite of Milky Way-mass halos
  from the DREAMS Project, simulated with Cold Dark Matter (CDM),to quantify the influence
  of baryon feedback and intrinsic halo-to-halo variance on dark matter density profiles.
  Our suite of 1024 halos varies over supernova and black hole feedback parameters
  from the IllustrisTNG model, as well as variations in two cosmological parameters.
  We find that Milky Way-mass dark matter density profiles in the IllustrisTNG model
  are largely insensitive to astrophysics and cosmology variations, with the dominant
  source of scatter instead arising from halo-to-halo variance. However, most of the
  (comparatively minor) feedback-driven variations come from the changes to supernova
  prescriptions. By comparing to dark matter-only simulations, we find that the strongest
  supernova wind energies are so effective at preventing galaxy formation that the
  halos are nearly entirely collisionless dark matter. Finally, regardless of physics
  variation, all the DREAMS halos are roughly consistent with a halo contracting adiabatically
  from the presence of baryons, unlike models that have bursty stellar feedback. This
  work represents a step toward assessing the robustness of Milky Way dark matter
  profiles, with direct implications for dark matter searches where systematic uncertainty
  in the density profile remains a major challenge.
arxivId: '2512.03132'
arxivUrl: https://arxiv.org/abs/2512.03132
authors:
- Alex M. Garcia
- Jonah C. Rose
- Paul Torrey
- Andrea Caputo
- Mariangela Lisanti
- Andrew B. Pace
- Hongwan Liu
- Abdelaziz Hussein
- Haozhe Liu
- Francisco Villaescusa-Navarro
- John Barry
- Ilem Leisher
- Belén Costanza
- Jonathan Kho
- Ethan Lilie
- Jiaxuan Li
- Niusha Ahvazi
- Aklant Bhowmick
- Tri Nguyen
- Stephanie O'Neil
- Xiaowei Ou
- Xuejian Shen
- Arya Farahi
- Nitya Kallivayalil
- Lina Necib
- Mark Vogelsberger
concepts:
- dark matter
- cosmological simulation
- baryonic feedback
- halo-to-halo variance
- uncertainty quantification
- adiabatic contraction
- simulation-based inference
- nfw profile
- model validation
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2512_03132/figure_1.png
- /iaifi-research-blog/figures/2512_03132/figure_2.png
- /iaifi-research-blog/figures/2512_03132/figure_3.png
pdfUrl: https://arxiv.org/pdf/2512.03132v1
published: '2025-12-02T19:00:00+00:00'
theme: Astrophysics
title: 'The DREAMS Project: Disentangling the Impact of Halo-to-Halo Variance and
  Baryonic Feedback on Milky Way Dark Matter Density Profiles'
wordCount: 1060
---

## The Big Picture

Imagine trying to find a book in a library where you don't know whether the shelves are organized alphabetically, by color, or at random. That's roughly the challenge facing physicists hunting for dark matter in our galaxy: to detect it, they need to know precisely how dark matter is spread across the Milky Way, how densely it packs at the center, how thinly it spreads at the edges. Scientists call this the **dark matter density profile**, and getting it right matters enormously.

The stakes are real. Experiments like direct detection searches and gamma-ray telescopes point toward the galactic center expecting the highest concentration of dark matter. But dark matter doesn't emit light, and its distribution depends on the messy, turbulent history of galaxy formation, billions of stellar explosions over cosmic time. If the assumed map is wrong, conclusions about dark matter's properties could be off by factors of ten or a hundred.

To untangle this, the DREAMS Project team ran 1,024 simulated Milky Way-mass galaxies, systematically varying the physics of stellar explosions and black hole growth, then measured how sensitive the dark matter density profiles were to each variable they changed. The answer upends a common assumption.

> **Key Insight:** The dominant source of uncertainty in dark matter density profiles is not the physics of how stars explode or black holes grow — it's the cosmic luck of which particular galaxy you happen to inhabit. Galaxy-to-galaxy variation swamps everything else.

## How It Works

The DREAMS Project (Dark Matter and Astrophysics with Machine Learning and Simulations) built its simulations on the **IllustrisTNG model**, one of the most widely used frameworks for galaxy formation. It treats dark matter, gas, stars, and supermassive black holes together in a fully self-consistent simulation.

The team varied four key parameters across all 1,024 runs:

- **Supernova wind speed** and **supernova wind energy**, controlling how aggressively stellar explosions blow gas out of galaxies
- **Black hole feedback efficiency** and **black hole accretion rate**, governing how actively galactic nuclei heat their surroundings
- Two **cosmological parameters** (the matter power spectrum amplitude and slope)

They sampled this space using a **Latin hypercube** strategy, a method for spreading test cases evenly across a multi-dimensional parameter space so no two simulations are clones of each other. Each simulation also started from a different random initial condition, capturing both physics variation and the intrinsic scatter built into the universe's structure.

![Figure 1](/iaifi-research-blog/figures/2512_03132/figure_1.png)

When researchers compared dark matter density profiles across the full sample, **halo-to-halo variance** consistently dominated over any systematic shift from varying the feedback parameters. Halo-to-halo variance is the natural scatter in how galaxies form, driven by different merger histories, proximity to galaxy clusters, and the randomness of structure formation.

Turn up the supernova winds. Turn down the black hole feedback. Tweak the cosmology. The profiles barely budge compared to how much they vary simply from halo to halo.

One exception stood out: when supernova wind energies were cranked to extreme values, feedback became so powerful it suppressed star formation almost entirely. The remaining halos were nearly **collisionless**, dominated almost entirely by dark matter, with almost no **baryons** (ordinary matter like gas, stars, and dust) left to influence the structure. These extreme halos are a regime where astrophysics genuinely matters, but they also fail to produce realistic Milky Way analogs.

![Figure 2](/iaifi-research-blog/figures/2512_03132/figure_2.png)

Then there's the shape of the inner density profile. A long-standing debate asks whether baryonic feedback creates a flat **dark matter core** (constant density at the center) or preserves the sharp **cusp** that dark matter-only simulations universally predict, where density rises steeply inward.

Some simulations with explosive, episodic "bursty" stellar feedback do create cores by repeatedly shaking the gravitational potential, causing rapid fluctuations that scour out the center. The DREAMS halos tell a different story: regardless of feedback variation, all 1,024 simulations are consistent with **adiabatic contraction**, a process where dark matter responds smoothly to the slow accumulation of baryons at the center. This makes the inner profile *denser* rather than hollow. IllustrisTNG's smooth feedback model simply doesn't generate the violent potential fluctuations needed to carve out a core.

![Figure 3](/iaifi-research-blog/figures/2512_03132/figure_3.png)

## Why It Matters

Every dark matter search using the Milky Way as its laboratory depends on two inputs: the **local dark matter density** (how much dark matter passes through a given volume near Earth) and the **velocity distribution** of dark matter particles near our solar system. For years, researchers have worried that uncertainties in baryonic feedback, notoriously hard to model, might be silently dominating the error budget in these searches.

The DREAMS results push back on that concern. For Milky Way-mass halos in the IllustrisTNG framework, feedback uncertainty is secondary. The bigger challenge is the irreducible halo-to-halo variance: our Milky Way is just one realization of a random process. That uncertainty can be addressed statistically, by building better priors over the population of Milky Way-like galaxies and incorporating observational constraints from stellar motions and satellite populations.

The work also raises a pointed question for the broader simulation community: do other widely-used models (FIRE, EAGLE, Simba) agree? If those models predict cores where DREAMS predicts cusps, reconciling them becomes essential before dark matter searches can claim any real confidence in their assumed density profiles.

> **Bottom Line:** Out of 1,024 simulated Milky Ways with widely varying physics, it's not the supernova prescription or the black hole model that most shapes the dark matter profile. It's simply which galaxy you are. This shifts the uncertainty problem for dark matter detection toward population-level statistical approaches.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">The DREAMS Project produced the largest suite of Milky Way-mass hydrodynamical simulations to date, combining cosmological simulation, systematic parameter exploration, and dark matter phenomenology to directly inform experimental dark matter searches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The Latin hypercube sampling design and simulation-based inference frameworks developed within DREAMS provide a reusable template for AI-accelerated sensitivity analysis across high-dimensional astrophysical parameter spaces.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By showing that adiabatic contraction, not core formation, characterizes IllustrisTNG Milky Way halos across all feedback variations, this work establishes a stronger theoretical baseline for interpreting direct and indirect dark matter detection experiments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future DREAMS work will extend to warm dark matter and self-interacting dark matter models, directly testing how non-CDM physics alters these conclusions; the paper is available at [arXiv:2512.03132](https://arxiv.org/abs/2512.03132).</span></div></div>
</div>
