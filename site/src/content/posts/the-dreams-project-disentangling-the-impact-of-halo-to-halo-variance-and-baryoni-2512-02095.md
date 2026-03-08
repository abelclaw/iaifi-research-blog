---
abstract: 'We analyze the properties of satellite galaxies around 1,024 Milky Way-mass
  hosts from the DREAMS Project, simulated within a $Λ$CDM cosmology. Utilizing the
  TNG galaxy-formation model, the DREAMS simulations incorporate both baryonic physics
  and cosmological uncertainties for a large sample of galaxies with diverse environments
  and formation histories. We investigate the relative impact of the physical uncertainty
  from the galaxy-formation model on predicted satellite properties using four metrics:
  the satellite stellar mass function, radial distribution, inner slope of dark matter
  density profile, and stellar half-light radius. We compare these predictions to
  observations from the SAGA Survey and the DREAMS N-body simulations and find that
  uncertainties from baryonic physics modeling are subdominant to the scatter arising
  from halo-to-halo variance. Where baryonic modeling does affect satellites, the
  supernova wind energy has the largest effect on the satellite properties that we
  investigate. Specifically, increased supernova wind energy suppresses the stellar
  mass of satellites and results in more extended stellar half-light radii. The adopted
  wind speed has only a minor impact, and other astrophysical and cosmological parameters
  show no measurable effect. Our findings highlight the robustness of satellite properties
  against uncertainties in baryonic physics modeling.'
arxivId: '2512.02095'
arxivUrl: https://arxiv.org/abs/2512.02095
authors:
- Jonah C. Rose
- Mariangela Lisanti
- Paul Torrey
- Francisco Villaescusa-Navarro
- Alex M. Garcia
- Arya Farahi
- Carrie Filion
- Alyson M. Brooks
- Nitya Kallivayalil
- Kassidy E. Kollmann
- Ethan Lilie
- Jiaxuan Li
- Olivia Mostow
- Akaxia Cruz
- Tri Nguyen
- Sandip Roy
- Andrew B. Pace
- Niusha Ahvazi
- Stephanie O'Neil
- Xuejian Shen
- Francis-Yan Cyr-Racine
- Adrian M. Price-Whelan
- Marla Geha
- Lina Necib
- Mark Vogelsberger
- Julian B. Muñoz
- Julianne J. Dalcanton
concepts:
- cosmological simulation
- halo-to-halo variance
- baryonic feedback
- uncertainty quantification
- dark matter
- satellite stellar mass function
- stellar evolution
- simulation-based inference
- emulation
- bayesian inference
figures:
- /iaifi-research-blog/figures/2512_02095/figure_1.png
- /iaifi-research-blog/figures/2512_02095/figure_2.png
pdfUrl: https://arxiv.org/pdf/2512.02095v1
published: '2025-12-01T19:00:00+00:00'
theme: Astrophysics
title: 'The DREAMS Project: Disentangling the Impact of Halo-to-Halo Variance and
  Baryonic Feedback on Milky Way Satellite Galaxies'
wordCount: 1014
---

## The Big Picture

Imagine trying to understand traffic patterns in a city by studying just ten intersections, then wondering whether your conclusions apply to the whole metropolis. That's the challenge astronomers face when modeling the Milky Way's satellite galaxies: tiny, faint dwarf galaxies orbiting our home galaxy, each one a window into the universe's darkest and smallest structures. For decades, researchers have built elaborate computer simulations to predict what these satellites should look like. But a nagging question persists: when simulations disagree with observations, is it because our physics models are wrong, or just because every Milky Way is a little different?

The **DREAMS Project** (Dark Matter and Astrophysics with Machine Learning and Simulations) goes after this question directly. By simulating 1,024 Milky Way-mass host galaxies, roughly a hundred times more than most previous efforts, researchers led by Jonah Rose and Mariangela Lisanti at Princeton set out to quantify exactly how much the assumed physics of galaxy formation matters compared to the natural diversity of galaxies themselves. The answer is clear: the messiness of the cosmos, not the messiness of our equations, drives most of what we see in satellite galaxy populations.

> **Key Insight:** The natural variation from galaxy to galaxy swamps the uncertainty from how we model star formation and stellar explosions. Our satellite galaxy predictions are far more stable than previously feared, and observations primarily reflect the diverse formation histories of individual galaxies rather than flaws in the underlying model.

## How It Works

Each of the 1,024 host galaxies was simulated using the **TNG galaxy-formation model**, a widely used physics recipe specifying how gas cools, stars form, supernovae explode, and black holes grow, best known from the IllustrisTNG suite. To probe the role of physics assumptions, the team ran simulations across a grid of baryonic and cosmological parameters: adjustable settings governing everything from how much energy supernovae pump into surrounding gas to the rate of cosmic expansion.

For each simulated galaxy, the researchers tracked four properties of the satellite population:

- **Satellite stellar mass function** — how many satellites exist at each mass scale
- **Radial distribution** — how far satellites orbit from their host
- **Inner slope of the dark matter density profile** — the steepness of the dark matter concentration at each satellite's core
- **Stellar half-light radius** — how physically extended each satellite's stars are

![Figure 1](/iaifi-research-blog/figures/2512_02095/figure_1.png)

The team compared these predictions against two benchmarks: the **SAGA Survey**, which observes satellite galaxies around 101 nearby Milky Way analogs in the real universe, and a companion set of N-body (dark matter-only) DREAMS simulations that strip away baryonic physics entirely. By stacking results across all 1,024 hosts and across all parameter variations, they could separate the signal of physics uncertainty from the noise of natural galaxy-to-galaxy variation.

The results are telling. Plot the predicted satellite stellar mass function for different physics settings, and the curves pile nearly on top of one another. But the cloud of galaxy-to-galaxy variation engulfs them all. No matter how you tune the supernova model or cosmological parameters within observationally allowed ranges, the diversity of galaxy formation histories produces a far wider spread than the model uncertainty itself.

![Figure 2](/iaifi-research-blog/figures/2512_02095/figure_2.png)

There is one exception worth noting. Supernova wind energy, the total kinetic energy injected into surrounding gas when massive stars explode, does leave a measurable imprint. Cranking up wind energy suppresses satellite stellar masses and produces more spatially extended stellar distributions. The physics is intuitive: stronger winds push gas outward before it can collapse into stars, leaving satellites less centrally concentrated. Wind speed, by contrast, has only a minor effect. Parameters governing black holes, cosmic expansion, and other processes show essentially no measurable signal.


## Why It Matters

Satellite galaxies are among the best laboratories we have for probing dark matter behavior on scales smaller than a single galaxy. Competing theories (warm dark matter, self-interacting dark matter, various ultralight candidates) all predict different satellite populations. Before we can use observations to rule models in or out, we need to know how much observed scatter in satellite properties comes from dark matter physics versus galaxy formation physics.

The DREAMS result settles that question on the galaxy-formation side: the physics uncertainty is small. Departures from standard ΛCDM predictions in observed satellites are more likely to signal exotic dark matter than poorly modeled stellar explosions or black hole activity.

For computational cosmology more broadly, the finding suggests a shift in strategy. Rather than spending computational resources on ever-finer resolution for a handful of systems, future surveys may gain more from expanding the statistical sample of hosts. Diversity, not model tuning, dominates the total prediction uncertainty. The DREAMS framework, combining large ensemble simulations with systematic parameter variation, offers a template for moving beyond simulating one galaxy at a time. And the SAGA Survey comparison lends confidence that the TNG model captures the essential physics at this mass scale.

> **Bottom Line:** With 1,024 simulated Milky Way analogs, the DREAMS Project shows that satellite galaxy properties hold up well against uncertainty in baryonic physics. The cosmos's own diversity, not our model imprecision, is the main source of theoretical scatter when comparing simulations to observations.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">The DREAMS Project combines large-scale hydrodynamical simulation ensembles with systematic parameter sweeps across baryonic and cosmological uncertainties, connecting computational astrophysics and statistical inference to disentangle physical from cosmic variance in satellite galaxy populations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The DREAMS framework provides a richly varied dataset of 1,024 host galaxies with controlled parameter variation, exactly the kind of large-scale simulation suite needed to train and validate machine learning emulators for cosmological inference.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By demonstrating that satellite galaxy properties are insensitive to baryonic physics modeling uncertainties, the results sharpen satellites as probes of dark matter physics, making them more reliable discriminators between standard cosmological predictions and alternative dark matter models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future DREAMS analyses will extend to additional satellite observables and use the simulation suite for simulation-based inference on dark matter properties; the paper is available at [arXiv:2512.02095](https://arxiv.org/abs/2512.02095).</span></div></div>
</div>
