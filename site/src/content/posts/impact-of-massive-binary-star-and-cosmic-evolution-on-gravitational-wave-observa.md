---
abstract: 'Making the most of the rapidly increasing population of gravitational-wave
  detections of black hole (BH) and neutron star (NS) mergers requires comparing observations
  with population synthesis predictions. In this work we investigate the combined
  impact from the key uncertainties in population synthesis modelling of the isolated
  binary evolution channel: the physical processes in massive binary-star evolution
  and the star formation history as a function of metallicity, $Z$, and redshift $z,
  \mathcal{S}(Z,z)$. Considering these uncertainties we create 560 different publicly
  available model realizations and calculate the rate and distribution characteristics
  of detectable BHBH, BHNS, and NSNS mergers. We find that our stellar evolution and
  $\mathcal{S}(Z,z)$ variations can impact the predicted intrinsic and detectable
  merger rates by factors $10^2$-$10^4$. We find that BHBH rates are dominantly impacted
  by $\mathcal{S}(Z,z)$ variations, NSNS rates by stellar evolution variations and
  BHNS rates by both. We then consider the combined impact from all uncertainties
  considered in this work on the detectable mass distribution shapes (chirp mass,
  individual masses and mass ratio). We find that the BHNS mass distributions are
  predominantly impacted by massive binary-star evolution changes. For BHBH and NSNS
  we find that both uncertainties are important. We also find that the shape of the
  delay time and birth metallicity distributions are typically dominated by the choice
  of $\mathcal{S}(Z,z)$ for BHBH, BHNS and NSNS. We identify several examples of robust
  features in the mass distributions predicted by all 560 models, such that we expect
  more than 95% of BHBH detections to contain a BH $\gtrsim 8\,\rm{M}_{\odot}$ and
  have mass ratios $\lesssim 4$. Our work demonstrates that it is essential to consider
  a wide range of allowed models to study double compact object merger rates and properties.'
arxivId: '2112.05763'
arxivUrl: https://arxiv.org/abs/2112.05763
authors:
- Floor S. Broekgaarden
- Edo Berger
- Simon Stevenson
- Stephen Justham
- Ilya Mandel
- Martyna Chruślińska
- Lieke A. C. van Son
- Tom Wagg
- Alejandro Vigna-Gómez
- Selma E. de Mink
- Debatri Chattopadhyay
- Coenraad J. Neijssel
concepts:
- gravitational waves
- stellar evolution
- binary population synthesis
- compact object mergers
- uncertainty quantification
- cosmological simulation
- chirp mass distribution
- monte carlo methods
- ensemble methods
- simulation-based inference
- bayesian inference
figures:
- /iaifi-research-blog/figures/2112_05763/figure_1.png
- /iaifi-research-blog/figures/2112_05763/figure_3.png
pdfUrl: https://arxiv.org/pdf/2112.05763v2
published: '2021-12-10T19:00:00+00:00'
theme: Astrophysics
title: 'Impact of Massive Binary Star and Cosmic Evolution on Gravitational Wave Observations
  II: Double Compact Object Rates and Properties'
wordCount: 1048
---

## The Big Picture

Imagine trying to reconstruct a recipe by tasting only the final dish. You can detect sweetness, acidity, heat, but tracing each flavor back to a specific ingredient requires knowing how cooking transforms everything. Gravitational wave astronomy faces the same puzzle: when LIGO (a detector sensitive enough to measure ripples in spacetime smaller than an atomic nucleus) picks up two black holes spiraling together a billion light-years away, what does that collision actually tell us about the massive stars that lived and died to create them?

Predicting what detectors should see requires threading two needles simultaneously. First, you need to model the complicated physics of two massive stars evolving together: how they shed mass through outflows called **stellar winds**, how they swap material back and forth, how one star's explosive death kicks its companion. Second, you need to know the history of star formation across the universe. Where and when were stars forming, and how chemically enriched were those stellar nurseries?

That last point matters more than it might seem. In astronomy, "metal-rich" means formed from gas already containing heavy elements like carbon and iron, leftovers from earlier stellar generations. Metal-rich stars shed more mass before dying and collapse into lighter black holes. Metal-poor stars hold on to more mass and leave heavier ones. Get either ingredient wrong, and the recipe fails.

A team led by Floor Broekgaarden at the Center for Astrophysics at Harvard & Smithsonian tackled both uncertainties head-on, constructing 560 distinct model universes and asking: across all of them, what can we still reliably predict about gravitational wave sources?

> **Key Insight:** Predicted merger rates for black holes and neutron stars can vary by factors of 10,000 depending on which physical assumptions you make. But even amid that chaos, certain features remain predictable across every model the team tested.

## How It Works

The researchers focused on the **isolated binary evolution channel**, the pathway where two massive stars are born as companions, evolve together over millions of years, and eventually both collapse into **compact objects** (black holes or neutron stars) that inspiral and merge. This is currently the leading explanation for the black hole mergers LIGO and Virgo detect.

To map out the uncertainty, the team varied two interconnected sets of parameters:

- **Massive binary star evolution physics**: wind mass-loss rates; **common envelope evolution** (a dramatic phase where one star's outer layers balloon outward and engulf its companion, and the pair must then shed those layers or spiral into a single object); **natal kick velocities** (the recoil a neutron star receives at birth, which can break up a binary entirely); and **mass transfer stability criteria** (whether mass flowing between stars proceeds steadily or catastrophically)
- **S(Z,z), the metallicity-dependent star formation rate density**: how star formation varied across cosmic time and chemical enrichment, which matters because low-metallicity stars lose less mass to winds and can form heavier black holes

![Figure 1](/iaifi-research-blog/figures/2112_05763/figure_1.png)

Combining variations across both dimensions yielded 560 model realizations. For each, the team ran rapid **population synthesis** simulations (fast numerical codes tracking millions of binary systems using simplified mathematical recipes for each physical process) and calculated predicted rates and properties for three types of **double compact object (DCO)** mergers: black hole–black hole (BHBH), black hole–neutron star (BHNS), and neutron star–neutron star (NSNS).

The rate variations are staggering. Across 560 models, predicted merger rates span two to four orders of magnitude, a factor of 10,000 between the most and least optimistic assumptions. This isn't a minor calibration uncertainty. Without accounting for both families of unknowns, any rate prediction is essentially unconstrained.

Different merger types respond differently to different uncertainties. BHBH rates are primarily driven by S(Z,z), because black hole masses are exquisitely sensitive to how much mass stars shed, which depends heavily on metallicity. NSNS rates are dominated by stellar evolution physics, particularly supernova kicks that can disrupt fragile neutron star binaries. BHNS mergers feel both effects roughly equally.

![Figure 2](/iaifi-research-blog/figures/2112_05763/figure_3.png)

## Why It Matters

The real prize isn't just cataloging the uncertainty but identifying what remains predictable despite it. Scanning across all 560 models, the team found several persistent features in the mass distributions that hold regardless of physical assumptions. More than 95% of detected BHBH mergers should contain at least one black hole heavier than 8 solar masses, and their mass ratios should be less than 4:1. These aren't model-dependent predictions. They're constraints that survive every combination of assumptions the team explored.


This has immediate practical value. As LIGO, Virgo, and KAGRA continue adding events to their catalogs, comparisons between observed distributions and theoretical predictions can progressively rule out corners of this vast model space. The team's 560 models are publicly available, giving the community a ready-made toolkit for exactly this kind of inference.

With larger observed samples, gravitational wave detectors become cosmic laboratories for massive star physics. The inverse problem turns tractable: instead of asking what mergers the stars produce, you ask what stars the mergers imply.

> **Bottom Line:** Predicting gravitational wave merger rates from first principles requires simultaneously modeling uncertain stellar physics and uncertain cosmic star formation history. Getting both wrong can mislead you by a factor of 10,000. By mapping that entire range across 560 models, the team reveals which features of the merger population we can trust no matter which assumptions we make.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects computational astrophysics with observational gravitational wave science, using large-scale population synthesis to link fundamental stellar physics with the rapidly growing catalog of LIGO/Virgo detections.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The systematic approach of building 560 model realizations and identifying stable predictions across parameter space parallels modern machine learning practices for uncertainty quantification; the publicly released model grids provide a foundation for future AI-driven Bayesian inference on gravitational wave populations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By disentangling how BHBH, BHNS, and NSNS merger rates each respond differently to stellar evolution versus cosmic star formation uncertainties, the analysis sharpens our ability to extract fundamental physics (compact object masses, supernova mechanisms, common envelope evolution) from gravitational wave observations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future gravitational wave observing runs, combined with these 560 publicly available model realizations, will progressively constrain the currently unconstrained stages of massive binary star evolution; see [arXiv:2112.05763](https://arxiv.org/abs/2112.05763) for the full analysis.</span></div></div>
</div>
