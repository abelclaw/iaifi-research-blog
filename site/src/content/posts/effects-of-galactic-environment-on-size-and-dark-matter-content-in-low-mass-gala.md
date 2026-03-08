---
abstract: We utilize the cosmological volume simulation, FIREbox, to investigate how
  a galaxy's environment influences its size and dark matter content. Our study focuses
  on approximately 1,200 galaxies (886 central and 332 satellite halos) in the low-mass
  regime, with stellar masses between $10^6$ to $10^9$ $M_{\odot}$. We analyze the
  size-mass relation ($r_{50} - M_{\star}$), inner dark matter mass-stellar mass ($M^{50}_{\rm
  DM} - M_{\star}$) relation, and the halo mass-stellar mass ($M_{\rm halo} - M_{\star}$)
  relation. At fixed stellar mass, we find the galaxies experiencing stronger tidal
  influences, indicated by higher Perturbation Indices (PI $>$ 1) are generally larger
  and have lower masses relative to their counterparts with lower Perturbation Indices
  (PI $<$ 1). Applying a Random Forest regression model, we show that both the environment
  (PI) and halo mass ($M_{rm halo}$) are significant predictors of a galaxy's relative
  size and dark matter content. Notably, because $M_{\rm halo}$ is also strongly affected
  by the environment, our findings indicate that environmental conditions not only
  influence galactic sizes and relative inner dark matter content directly, but also
  indirectly through their impact on halo mass. Our results highlight a critical interplay
  between environmental factors and halo mass in shaping galaxy properties, affirming
  the environment as a fundamental driver in galaxy formation and evolution.
arxivId: '2501.04084'
arxivUrl: https://arxiv.org/abs/2501.04084
authors:
- Francisco J. Mercado
- Jorge Moreno
- Robert Feldmann
- Marckie Zeender
- Jose A. Benavides
- Joanna M. Piotrowska
- Courtney Klein
- Coral Wheeler
- Lina Necib
- James S. Bullock
- Philip F. Hopkins
concepts:
- cosmological simulation
- dark matter
- galaxy size-mass relation
- halo mass-stellar mass relation
- regression
- tidal stripping
- ensemble methods
- galaxy classification
- stellar feedback
- bayesian inference
figures:
- /iaifi-research-blog/figures/2501_04084/figure_2.png
- /iaifi-research-blog/figures/2501_04084/figure_2.png
- /iaifi-research-blog/figures/2501_04084/figure_3.png
pdfUrl: https://arxiv.org/pdf/2501.04084v2
published: '2025-01-07T19:00:01+00:00'
theme: Astrophysics
title: Effects of galactic environment on size and dark matter content in low-mass
  galaxies
wordCount: 1141
---

## The Big Picture

Imagine two people with identical genetics raised in completely different neighborhoods. Despite identical starting points, their lives unfold differently, shaped by forces beyond their control. Galaxies face a strikingly similar fate. Two dwarf galaxies born with the same stellar mass can end up radically different — one puffy and stretched, the other compact and dense — simply because of where they formed in the cosmic web.

Why small galaxies look so different from one another has puzzled astronomers for decades. Dwarf galaxies, the universe's most abundant type, range wildly in size and dark matter content. Some are ghostly, diffuse wisps barely held together. Others are tight, dark-matter-packed systems. Scientists have long suspected that a galaxy's neighborhood plays a role, but disentangling environmental influence from intrinsic properties has been notoriously difficult.

A team led by Francisco Mercado has used the FIREbox cosmological simulation to directly quantify how environment sculpts dwarf galaxy size and dark matter content, deploying machine learning to separate the tangled threads of cause and effect.

> **Key Insight:** The gravitational push-and-pull a galaxy feels from its neighbors doesn't merely nudge its properties. It reshapes how large a galaxy grows and how much dark matter it retains, both directly and by eroding the dark matter halo (the invisible cloud of dark matter that surrounds and gravitationally holds a galaxy together) that governs everything else.

## How It Works

The researchers turned to **FIREbox**, a cosmological simulation from the Feedback In Realistic Environments (FIRE) project that tracks galaxy formation across a cube of space roughly 22 megaparsecs on a side. Unlike zoom-in simulations that study single galaxies in extreme detail, FIREbox captures a statistical sample of about 1,200 low-mass galaxies: 886 "central" galaxies sitting at the heart of their own dark matter halos and 332 "satellites" orbiting inside larger host halos. All have stellar masses between one million and one billion times the mass of our Sun.

![Figure 1](/iaifi-research-blog/figures/2501_04084/figure_2.png)

To measure each galaxy's gravitational stress from its surroundings, the team introduced the **Perturbation Index (PI)**, a single number capturing the cumulative tidal force a galaxy feels from all its neighbors, weighted by their mass and proximity. Tidal force is the stretching force that arises when gravity pulls harder on one side of an object than the other. It's the same effect that drives Earth's ocean tides, here operating at cosmic scales. A galaxy with PI > 1 is significantly tugged by its environment; PI < 1 means it's relatively undisturbed. This metric lets researchers slice their sample into disturbed and undisturbed groups and compare properties at fixed stellar mass.

The results were clear. At the same stellar mass, high-PI galaxies are systematically larger, sometimes dramatically so, and carry significantly less dark matter in their central regions than more isolated counterparts. Environmental harassment puffs galaxies up while stripping away their dark matter.

To disentangle causation, the team trained a **Random Forest regression model** to predict each galaxy's relative size and dark matter content. Random Forest is an ensemble technique that builds hundreds of decision trees, each a flowchart of yes/no questions about the data, and averages their predictions. Inputs included the Perturbation Index, total halo mass, and stellar mass. By examining which variables the model relied on most heavily (its **feature importance** scores), the researchers could rank the drivers of galaxy structure.

![Figure 2](/iaifi-research-blog/figures/2501_04084/figure_2.png)

Both environment (PI) and halo mass emerged as significant predictors. But halo mass is itself strongly shaped by environment: galaxies in high-tidal-force regions tend to have their dark matter halos stripped, reducing total halo mass. So environment operates on two tracks simultaneously. There's a direct track that physically distorts and inflates a galaxy, and an indirect track that erodes the dark matter halo governing everything else.

The team examined three key scaling relations:
- **Size-mass relation** (half-light radius vs. stellar mass): High-PI galaxies sit systematically above the median at fixed stellar mass. The half-light radius is the distance from a galaxy's center enclosing half its total light.
- **Inner dark matter mass-stellar mass relation** (dark matter within the half-mass radius vs. stellar mass): High-PI galaxies are dark-matter-poor relative to low-PI counterparts.
- **Halo mass-stellar mass relation**: High-PI galaxies occupy systematically lower-mass halos, consistent with tidal stripping of the outer dark matter envelope.


## Why It Matters

The Vera C. Rubin Observatory, currently coming online in Chile, will soon deliver a census of millions of faint dwarf galaxies across all cosmic environments. The Nancy Grace Roman Space Telescope will push even deeper. For the first time, astronomers will have statistical samples spanning the full range of environments, from isolated voids to dense galaxy clusters.

Interpreting that data requires a theoretical framework for understanding what drives dwarf galaxy diversity. Mercado and colleagues provide exactly that. Their finding that environment shapes dwarf galaxies through both direct tidal distortion *and* indirect halo mass erosion means any model explaining the observed zoo of dwarf galaxies must account for both pathways at once. This matters most for the extreme cases: **ultra-diffuse galaxies (UDGs)**, ghostly, spread-out systems that seem to contain far too little dark matter for their size. The team's results support the idea that tidal processes in dense environments can naturally inflate galaxies into UDG territory, no exotic physics required.

The machine learning component here does real scientific work. Random Forest feature importance gives a principled, data-driven way to rank the causes of galaxy diversity in a complex simulation. As cosmological simulations grow more sophisticated and data-rich, these interpretability tools will become standard equipment for extracting physical insight from computational experiments.

> **Bottom Line:** Where a galaxy lives in the cosmic web isn't background scenery. It's an active sculptor that stretches galaxies larger and strips them of dark matter, through both direct tidal forces and the slow erosion of the dark matter halos that galaxies depend on for their very structure.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects cosmological simulation science with interpretable machine learning, using a Random Forest model to disentangle the competing roles of environment and halo mass in shaping dwarf galaxy structure, a question that purely statistical or analytical approaches struggle to resolve.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Applying Random Forest feature importance to high-dimensional astrophysical simulation data shows how ensemble ML methods can function as causal inference tools, ranking physical drivers in complex systems where controlled experiments are impossible.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By quantifying how tidal forces reshape the size and dark matter content of low-mass galaxies, this study sharpens our picture of how large-scale cosmic structure governs the smallest, most common galaxies within it.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">As Rubin Observatory and the Roman Space Telescope begin delivering vast samples of observed dwarf galaxies, this simulation-based framework will be key for interpreting the full diversity of low-mass galaxy populations; the full study is available at [arXiv:2501.04084](https://arxiv.org/abs/2501.04084).</span></div></div>
</div>
