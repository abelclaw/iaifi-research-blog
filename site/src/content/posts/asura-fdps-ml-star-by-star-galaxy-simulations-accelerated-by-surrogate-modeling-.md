---
abstract: We introduce new high-resolution galaxy simulations accelerated by a surrogate
  model that reduces the computation cost by approximately 75 percent. Massive stars
  with a Zero Age Main Sequence mass of more than about 10 $\mathrm{M_\odot}$ explode
  as core-collapse supernovae (CCSNe), which play a critical role in galaxy formation.
  The energy released by CCSNe is essential for regulating star formation and driving
  feedback processes in the interstellar medium (ISM). However, the short integration
  timesteps required for SNe feedback have presented significant bottlenecks in astrophysical
  simulations across various scales. Overcoming this challenge is crucial for enabling
  star-by-star galaxy simulations, which aim to capture the dynamics of individual
  stars and the inhomogeneous shell's expansion within the turbulent ISM. To address
  this, our new framework combines direct numerical simulations and surrogate modeling,
  including machine learning and Gibbs sampling. The star formation history and the
  time evolution of outflow rates in the galaxy match those obtained from resolved
  direct numerical simulations. Our new approach achieves high-resolution fidelity
  while reducing computational costs, effectively bridging the physical scale gap
  and enabling multi-scale simulations.
arxivId: '2410.23346'
arxivUrl: https://arxiv.org/abs/2410.23346
authors:
- Keiya Hirashima
- Kana Moriwaki
- Michiko S. Fujii
- Yutaka Hirai
- Takayuki R. Saitoh
- Junnichiro Makino
- Ulrich P. Steinwandel
- Shirley Ho
concepts:
- surrogate modeling
- cosmological simulation
- emulation
- stellar evolution
- multi-scale simulation
- ism turbulence feedback
- scalability
- monte carlo methods
- regression
- transfer learning
- physics-informed neural networks
figures:
- /iaifi-research-blog/figures/2410_23346/figure_1.png
- /iaifi-research-blog/figures/2410_23346/figure_1.png
- /iaifi-research-blog/figures/2410_23346/figure_2.png
- /iaifi-research-blog/figures/2410_23346/figure_2.png
- /iaifi-research-blog/figures/2410_23346/figure_3.png
- /iaifi-research-blog/figures/2410_23346/figure_3.png
pdfUrl: https://arxiv.org/pdf/2410.23346v2
published: '2024-10-30T18:00:02+00:00'
theme: Astrophysics
title: 'ASURA-FDPS-ML: Star-by-star Galaxy Simulations Accelerated by Surrogate Modeling
  for Supernova Feedback'
wordCount: 1223
---

## The Big Picture

Imagine trying to simulate the entire history of a galaxy — billions of stars, vast clouds of gas, and the explosive deaths of massive suns — but every time a star explodes, your computer grinds to a near-halt. That's not a hypothetical problem. It's the central challenge that has bottlenecked galaxy simulations for decades.

Supernovae — the catastrophic deaths of stars more than ten times the mass of our Sun — release an almost incomprehensible burst of energy: about 10⁵¹ ergs, roughly equivalent to what our Sun will emit over its entire ten-billion-year lifetime, compressed into seconds. To capture that explosion faithfully in a simulation, you have to shrink your **computational time-step** — the slice of simulated time the computer calculates in each cycle — down to mere hundreds of years. Meanwhile, the rest of the galaxy ticks along on timescales millions of times longer. Reconciling those two clocks is brutally expensive.

The physics matters enormously. Supernovae don't just make pretty light shows. They regulate whether gas clumps together to form new stars, drive powerful winds that blow material out of galaxies entirely, and seed the cosmos with the heavy elements that eventually make planets and people.

Get the supernova physics wrong — or skip it to save compute time — and your simulated galaxy drifts from reality in ways that compound over billions of years. The field has been stuck in a painful tradeoff: high-resolution fidelity or tractable computation, but rarely both.

A team of researchers from the University of Tokyo, the Flatiron Institute, Kobe University, and collaborating institutions has now broken that tradeoff. Their new framework, **ASURA-FDPS-ML**, combines machine learning surrogate modeling with traditional direct simulations to cut computational costs by roughly 75% — without sacrificing the physical accuracy that makes high-resolution galaxy simulations worth running.

> **Key Insight:** By training a neural network to predict supernova blast wave outcomes and replacing the most expensive direct simulation steps with those predictions, the team achieved star-by-star galaxy simulations that match full-resolution results at a fraction of the cost.

## How It Works

The core bottleneck isn't the explosion itself — it's the **Sedov-Taylor phase**, the earliest stage of a supernova remnant's expansion when the blast wave is still moving fast and hot. Capturing this phase correctly requires time-steps on the order of hundreds of years, three orders of magnitude shorter than the typical flow of gas in galaxy simulations. Even particles far from the explosion have to slow their clocks to keep pace. The result: thousands of tiny steps per supernova event, multiplied across thousands of stellar deaths in a single dwarf galaxy simulation.

![Figure 1](/iaifi-research-blog/figures/2410_23346/figure_1.png)

The ASURA-FDPS-ML approach attacks this with a two-stage strategy:

1. **Training phase:** The team ran a suite of high-resolution **direct numerical simulations** — calculations that compute the physics from first principles, with no shortcuts — of isolated supernova explosions inside **turbulent molecular clouds**, the dense, swirling gas clouds where stars are born. These reference simulations fully resolve the Sedov-Taylor phase and capture how the blast wave evolves depending on local gas density, temperature, and turbulence.

2. **Surrogate model:** A machine learning surrogate learns from those reference simulations to predict the final state of a supernova blast wave given its local environment. Instead of grinding through hundreds of tiny time-steps, the surrogate jumps ahead and directly outputs the resulting momentum and energy deposited into surrounding gas particles.

3. **Gibbs sampling for stochasticity:** Real supernova environments are turbulent and chaotic. To preserve this statistical richness, the team incorporated **Gibbs sampling** — a technique that randomly draws outcomes from the full range of possibilities the model has learned, rather than always returning the most likely result. Each surrogate-modeled explosion still reflects the natural scatter of blast wave behavior; the simulation doesn't become artificially uniform.

The surrogate plugs directly into the **ASURA-FDPS** simulation code — a **smoothed particle hydrodynamics** framework that models gas as a collection of fluid particles rather than a fixed grid — which already tracks individual stars. When a massive star reaches the end of its life, instead of triggering a full expensive integration, the code queries the surrogate, gets a physically plausible outcome, and moves on.

![Figure 2](/iaifi-research-blog/figures/2410_23346/figure_1.png)

The validation results are striking. Comparing surrogate-accelerated simulations against fully resolved direct simulations of the same dwarf galaxy — identical initial conditions, same physics, different supernova solvers — the **star formation histories** match closely, as do the **outflow rates**, the measure of how much material supernovae blast out of the galaxy over time. These are precisely the quantities most sensitive to getting supernova feedback right.

![Figure 4](/iaifi-research-blog/figures/2410_23346/figure_2.png)

The 75% reduction in computation cost reflects the specific bottleneck being eliminated. In direct simulations, supernova time-step constraints dominate total wall-clock time. Replacing those constraints with fast surrogate evaluations removes the tax that individual explosions impose on the entire simulation.

## Why It Matters

**Star-by-star galaxy simulations** — models that track individual stellar masses rather than treating stars as statistical populations — represent the frontier of galaxy formation modeling. But computational cost has kept these simulations confined to small, isolated systems run for short durations.

In principle, such simulations capture effects that coarser models miss entirely: the clustering of supernovae in space and time, the chemical enrichment patterns imprinted by specific stellar generations, and the way feedback from a single massive star cluster can reshape the shape and structure of a small galaxy. Until now, the price tag was prohibitive.

The ASURA-FDPS-ML framework changes the economics. A 75% cost reduction isn't just a speedup — it's the difference between a simulation that takes a year and one that takes three months, or between a run you can afford once and one you can sweep across varied parameters, enabling real statistical studies. As surrogate models improve and training datasets grow richer, this approach could scale to larger galaxies and longer timescales. The methodology itself — pairing ML surrogates with probabilistic sampling to preserve stochasticity — offers a template for attacking similar time-step bottlenecks throughout computational astrophysics.

> **Bottom Line:** ASURA-FDPS-ML demonstrates that machine learning surrogates can replace the most computationally expensive physics in galaxy simulations without degrading the results that matter most — opening a path toward high-fidelity, star-by-star simulations of galaxy formation at scales previously out of reach.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges machine learning and astrophysical simulation, using data-driven surrogate modeling and probabilistic sampling to solve a fundamental computational bottleneck in galaxy formation physics — demonstrating that AI methods can be embedded faithfully within first-principles numerical frameworks.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper advances surrogate modeling for multi-scale physical simulations, showing that Gibbs sampling can preserve stochastic variability in ML-accelerated physics — a technique applicable beyond astrophysics to any domain where fast approximations must replicate the statistical texture of expensive solvers.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling accurate star-by-star galaxy simulations at reduced cost, this framework unlocks study of how individual supernova explosions collectively shape galaxy structure, chemical evolution, and outflow dynamics — fundamental questions in how the universe assembles the galaxies we observe today.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend the surrogate approach to larger galaxy masses, longer cosmic timescales, and additional feedback channels such as stellar winds and radiation pressure; the paper is available at arXiv as the ASURA-FDPS-ML preprint (Hirashima et al. 2025).</span></div></div>
</div>
