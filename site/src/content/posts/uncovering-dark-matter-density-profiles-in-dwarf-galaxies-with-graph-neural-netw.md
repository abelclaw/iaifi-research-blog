---
abstract: Dwarf galaxies are small, dark matter-dominated galaxies, some of which
  are embedded within the Milky Way. Their lack of baryonic matter (e.g., stars and
  gas) makes them perfect test beds for probing the properties of dark matter -- understanding
  the spatial dark matter distribution in these systems can be used to constrain microphysical
  dark matter interactions that influence the formation and evolution of structures
  in our Universe. We introduce a new method that leverages simulation-based inference
  and graph-based machine learning in order to infer the dark matter density profiles
  of dwarf galaxies from observable kinematics of stars gravitationally bound to these
  systems. Our approach aims to address some of the limitations of established methods
  based on dynamical Jeans modeling. We show that this novel method can place stronger
  constraints on dark matter profiles and, consequently, has the potential to weigh
  in on some of the ongoing puzzles associated with the small-scale structure of dark
  matter halos, such as the core-cusp discrepancy.
arxivId: '2208.12825'
arxivUrl: https://arxiv.org/abs/2208.12825
authors:
- Tri Nguyen
- Siddharth Mishra-Sharma
- Reuel Williams
- Lina Necib
concepts:
- graph neural networks
- simulation-based inference
- dark matter
- posterior estimation
- density estimation
- inverse problems
- normalizing flows
- core-cusp problem
- feature extraction
- bayesian inference
- cosmological simulation
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2208_12825/figure_1.png
- /iaifi-research-blog/figures/2208_12825/figure_2.png
- /iaifi-research-blog/figures/2208_12825/figure_3.png
pdfUrl: https://arxiv.org/pdf/2208.12825v1
published: '2022-08-26T18:00:04+00:00'
theme: Astrophysics
title: Uncovering dark matter density profiles in dwarf galaxies with graph neural
  networks
wordCount: 956
---

## The Big Picture

Imagine trying to weigh a ghost. You can't see it directly, but you can watch how its gravity tugs on nearby objects, and from those nudges you reconstruct the ghost's shape. That's what astrophysicists do when they study **dark matter** in dwarf galaxies. They watch stars move, and from those movements, they reverse-engineer the invisible scaffolding holding everything together.

Dwarf galaxies are a natural laboratory for this. These small, dim satellites of the Milky Way contain very little ordinary matter: few stars, almost no gas. But they are suffused with dark matter, which dominates their gravitational budget. That makes every stellar velocity measurement precious. Each one is a data point about the dark matter distribution hiding underneath.

The central puzzle in this field is called the **core-cusp discrepancy**. Cold dark matter simulations predict that each galaxy's dark matter halo should have a "cusp," a steep spike of density at the center. But observations of real dwarf galaxies often hint at a gentler, flat "core" instead.

Resolving this discrepancy could tell us something profound about dark matter's fundamental nature. A team of IAIFI-affiliated researchers have introduced a machine learning approach, using graph neural networks and simulation-based inference, that extracts more information from stellar kinematics than traditional methods can. The goal: sharpen our ability to finally answer whether dark matter halos have cusps or cores.

> **Key Insight:** By treating stellar positions and velocities as a graph and learning directly from simulations, this method extracts information that classical Jeans modeling discards, yielding tighter constraints on dark matter density profiles.

## How It Works

The workhorse of traditional dark matter inference in dwarf galaxies is **Jeans modeling**, a technique from stellar dynamics. It relates the **velocity dispersion** (the spread in how fast stars are moving) to the gravitational potential, inferring mass from motion.

It's powerful but limited. It assumes the galaxy is in perfect dynamical equilibrium and often requires assuming stellar orbits are isotropic. It uses only second moments of the velocity distribution, essentially the average of squared velocities, discarding the detailed shape of how velocities are distributed.

The new approach learns directly from simulated data in three stages:

1. **Forward model:** The researchers use `StarSampler` to generate 80,000 mock dwarf galaxies. Each simulation draws dark matter from a **generalized NFW (gNFW) profile**, a template named after Navarro, Frenk, and White that describes how dark matter density changes with radius. It is parameterized by a central density ρ₀, scale radius r_s, and slope γ that controls whether the center is cuspy or cored, plus a stellar light profile and velocity anisotropy.

2. **Graph neural network:** Rather than summarizing stars with statistics like velocity dispersion, each simulated observation is represented as a **graph**, a structure where each star is a node connected to nearby stars by edges. A graph neural network (GNN) learns to extract features that are maximally informative about the underlying dark matter profile. The representation is permutation-invariant (the result doesn't depend on the order stars are listed) and naturally handles datasets of varying size.

3. **Simulation-based inference:** The compressed graph features feed into a **neural posterior estimator**, a neural network that maps observations to a full probability distribution over model parameters. No explicit likelihood function is required. The simulator itself encodes all the physics.

![Figure 1](/iaifi-research-blog/figures/2208_12825/figure_1.png)

Given observed stellar positions and **line-of-sight velocities** (how fast each star is moving toward or away from Earth), the pipeline returns a full posterior distribution over the five dark matter profile parameters, including the slope γ that distinguishes cusps from cores.

![Figure 2](/iaifi-research-blog/figures/2208_12825/figure_2.png)

On test simulations, the GNN-based method consistently outperforms Jeans modeling. The posteriors are narrower, meaning tighter constraints on γ, and remain well-calibrated. Posterior estimation for a new observation takes seconds rather than hours.

## Why It Matters

The core-cusp discrepancy has nagged at cosmologists for decades. If halos are genuinely cored, it could mean dark matter self-interacts, or that baryonic feedback from supernovae and stellar winds reshapes halos in ways current simulations don't capture. Getting a definitive answer requires measurements precise enough to distinguish profiles that differ mainly in their innermost regions, where data is sparse.

![Figure 3](/iaifi-research-blog/figures/2208_12825/figure_3.png)

The machine learning approach here delivers that extra precision. The GNN uses the full spatial and kinematic picture of the stars, not just velocity dispersions, picking up information that Jeans modeling leaves on the table. As observational datasets grow (future surveys like the Vera Rubin Observatory will discover hundreds of new Milky Way satellites), methods like this become essential tools.

The current proof-of-concept assumes idealized, spherically symmetric, equilibrium galaxies. Extending to realistic systems with proper motion data and real-world measurement errors is the natural next step. More broadly, the approach reflects a shift in astrophysical inference: away from hand-crafted summary statistics and toward learned representations that let structure in the data do the heavy lifting.

> **Bottom Line:** Graph neural networks trained on simulated dwarf galaxies can infer dark matter density profiles with sharper constraints than classical Jeans modeling, bringing the resolution of the core-cusp puzzle measurably closer.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits at the intersection of simulation-based astrophysics and modern deep learning, replacing analytic summary statistics with learned graph representations to tackle one of cosmology's enduring puzzles.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The approach shows how graph neural networks and neural posterior estimators can jointly handle variable-size, unordered point-cloud datasets in a principled Bayesian inference framework.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Tighter constraints on dark matter density profiles in dwarf galaxies strengthen the search for non-gravitational dark matter interactions and help discriminate between competing cosmological models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions will incorporate non-equilibrium dynamics, proper motion data, and real observational uncertainties. The work is available at [arXiv:2208.12825](https://arxiv.org/abs/2208.12825).</span></div></div>
</div>
