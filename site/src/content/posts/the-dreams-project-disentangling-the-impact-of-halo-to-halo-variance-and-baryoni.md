---
abstract: Direct detection experiments require information about the local dark matter
  speed distribution to produce constraints on dark matter candidates, or infer their
  properties in the event of a discovery. In this paper, we analyze how the uncertainty
  in the dark matter speed distribution near the Sun is affected by baryonic feedback,
  halo-to-halo variance, and halo mass. To do so, we harness the statistical power
  of the new DREAMS Cold Dark Matter simulation suite, which is comprised of 1024
  zoom-in Milky Way-mass halos with varied initial conditions as well as cosmological
  and astrophysical parameters. Applying a normalizing flows emulator to these simulations,
  we find that the uncertainty in the local DM speed distribution is dominated by
  halo-to-halo variance and, to a lesser extent, uncertainty in host halo mass. Uncertainties
  in supernova and black hole feedback (from the IllustrisTNG model in this case)
  are negligible in comparison. Using the DREAMS suite, we present a state-of-the-art
  prediction for the DM speed distribution in the Milky Way. Although the Standard
  Halo Model is contained within the uncertainty of this prediction, individual galaxies
  may have distributions that differ from it. Lastly, we apply our DREAMS results
  to the XENON1T experiment and demonstrate that the astrophysical uncertainties are
  comparable to the experimental ones, solidifying previous results in the literature
  obtained with a smaller sample of simulated Milky Way-mass halos.
arxivId: '2512.04157'
arxivUrl: https://arxiv.org/abs/2512.04157
authors:
- Ethan Lilie
- Jonah C. Rose
- Mariangela Lisanti
- Alex M. Garcia
- Paul Torrey
- Kassidy E. Kollmann
- Jiaxuan Li
- Olivia Mostow
- Bonny Y. Wang
- Stephanie O'Neil
- Xuejian Shen
- Alyson M. Brooks
- Arya Farahi
- Nitya Kallivayalil
- Lina Necib
- Andrew B. Pace
- Mark Vogelsberger
concepts:
- dark matter
- cosmological simulation
- halo-to-halo variance
- normalizing flows
- uncertainty quantification
- emulation
- baryonic feedback
- simulation-based inference
- density estimation
- direct detection constraints
- bayesian inference
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2512_04157/figure_1.png
- /iaifi-research-blog/figures/2512_04157/figure_2.png
- /iaifi-research-blog/figures/2512_04157/figure_3.png
pdfUrl: https://arxiv.org/pdf/2512.04157v1
published: '2025-12-03T19:00:01+00:00'
theme: Astrophysics
title: 'The DREAMS Project: Disentangling the Impact of Halo-to-Halo Variance and
  Baryonic Feedback on Milky Way Dark Matter Speed Distributions'
wordCount: 1066
---

## The Big Picture

Imagine trying to catch a ghost by setting up detectors in your house, but you don't know how fast the ghost moves. That's roughly the situation physicists face when hunting for dark matter. Underground detectors like XENON1T wait patiently for a dark matter particle to collide with an atomic nucleus, producing a faint flash of light. How often that happens depends on how fast dark matter particles are moving through our Solar neighborhood. Get the speed distribution wrong, and you might conclude dark matter doesn't interact when it actually does, or vice versa.

For decades, physicists have relied on the **Standard Halo Model (SHM)**: a clean assumption that dark matter speeds follow a smooth bell curve, the same statistics that describe gas molecules bouncing around a room. It's a reasonable first guess.

But the Milky Way is not a simple system. It formed through billions of years of mergers, gas flows, exploding stars, and black holes swallowing surrounding matter. Why should its dark matter distribution be perfectly smooth?

The DREAMS project tackled this question head-on. The team simulated 1,024 Milky Way-like galaxies, delivering the most statistically powerful analysis yet of what dark matter in our cosmic backyard actually looks like.

> **Key Insight:** The biggest source of uncertainty in the local dark matter speed distribution isn't how we model exploding stars or black holes. It's simply the cosmic lottery of which particular galaxy the Milky Way happened to become.

## How It Works

The researchers built their analysis on the **DREAMS simulation suite**: 1,024 cosmological simulations, each zoomed in on a single galaxy-sized region of space and evolved to the present day from varied initial conditions. Unlike previous studies that used handfuls of simulated galaxies, this dataset provides real statistical muscle.

Each simulation tracks not just dark matter but also **baryonic feedback**, the physics of ordinary matter like gas and stars. When massive stars explode as supernovae, they blast gas outward. When supermassive black holes devour surrounding material, they release energy that reshapes the galaxy. These processes redistribute gas and, indirectly, dark matter. The DREAMS suite varies the strength of these mechanisms, drawing parameters from the **IllustrisTNG** model.

![Figure 1](figure:1)

Simulating 1,024 galaxies creates a practical challenge: how do you extract a smooth, well-characterized speed distribution from each one? The team trained a **normalizing flows** emulator on the simulation outputs. This type of neural network learns to transform simple probability distributions into complex ones, efficiently filling in gaps without running thousands of additional simulations.

The key question: which source of uncertainty matters most?

- **Halo-to-halo variance:** Each simulated galaxy has a unique merger history and internal structure, even with identical physical parameters. This is the "cosmic lottery" effect.
- **Host halo mass:** The Milky Way's total dark matter mass is uncertain by roughly a factor of two. Heavier halos pull dark matter faster.
- **Baryonic feedback parameters:** How strongly do supernovae and black holes shape the dark matter distribution?

The answer was unambiguous: halo-to-halo variance dominates. The spread between individual simulated galaxies swamps any effect from tweaking feedback physics. Host halo mass matters secondarily. Supernova and black hole feedback uncertainties? Negligible.

![Figure 2](figure:2)

On the reassuring side, imperfect models of stellar feedback won't dramatically bias dark matter detection predictions. But there's a harder problem: the Milky Way's particular formation history, something we can only partially reconstruct, introduces an irreducible uncertainty that no improvement in feedback physics can resolve.

The team also combined results across all 1,024 halos to produce a new prediction for the Milky Way's dark matter speed distribution. The Standard Halo Model falls within the uncertainty range, but that doesn't mean the SHM is right for any specific galaxy. Many individual simulated galaxies deviate significantly. The SHM survives as a statistical average, not a reliable description of any particular galaxy.

![Figure 3](figure:3)

## Why It Matters

The payoff shows up directly in detection science. Applied to XENON1T, one of the world's most sensitive dark matter detectors, the DREAMS results show that astrophysical uncertainties (what we don't know about dark matter's local speed distribution) are now comparable in magnitude to the experiment's own measurement uncertainties.

This confirms earlier estimates from smaller simulation samples: astrophysics is no longer a footnote in dark matter detection analyses. It is a co-equal source of uncertainty.

Observations of the Milky Way could narrow down which simulated halos actually resemble our own. How fast stars orbit at different distances, the structure of the diffuse cloud of old stars surrounding the disk, the orbits of companion galaxies: all of these carry information about our galaxy's dark matter halo. If matched against the DREAMS suite, the astrophysical uncertainties could shrink considerably.

Next-generation detectors like XENONnT and LUX-ZEPLIN will need even more precise astrophysical inputs to interpret their results. As detectors get sharper, the dark matter speed distribution goes from background assumption to front-line concern.

> **Bottom Line:** With 1,024 simulated Milky Ways and a machine learning emulator, the DREAMS project shows that the biggest wildcard in dark matter detection is the unique cosmic history of our own galaxy, not the physics of exploding stars, and that this astrophysical uncertainty is now large enough to matter for real experiments.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects cosmological simulation, machine learning, and particle physics, using a normalizing flows neural network to extract statistical predictions from 1,024 galaxy simulations and apply them directly to dark matter detector constraints.

- **Impact on Artificial Intelligence:** The normalizing flows emulator shows how generative machine learning models can characterize complex, high-dimensional probability distributions across large simulation suites, making astrophysical inference possible at a scale that brute-force simulation alone could not reach.

- **Impact on Fundamental Interactions:** By establishing that halo-to-halo variance dominates local dark matter speed uncertainty, DREAMS provides the most rigorous astrophysical input to date for interpreting direct detection experiments like XENON1T and its successors.

- **Outlook and References:** Future work will incorporate observational constraints to identify which simulated halos best match the Milky Way, potentially sharpening predictions for next-generation detectors; the paper is available at [arXiv:2512.04157](https://arxiv.org/abs/2512.04157).

## Original Paper Details
- **Title:** The DREAMS Project: Disentangling the Impact of Halo-to-Halo Variance and Baryonic Feedback on Milky Way Dark Matter Speed Distributions
- **arXiv ID:** 2512.04157
- **Authors:** ["Ethan Lilie", "Jonah C. Rose", "Mariangela Lisanti", "Alex M. Garcia", "Paul Torrey", "Kassidy E. Kollmann", "Jiaxuan Li", "Olivia Mostow", "Bonny Y. Wang", "Stephanie O'Neil", "Xuejian Shen", "Alyson M. Brooks", "Arya Farahi", "Nitya Kallivayalil", "Lina Necib", "Andrew B. Pace", "Mark Vogelsberger"]
- **Abstract:** Direct detection experiments require information about the local dark matter speed distribution to produce constraints on dark matter candidates, or infer their properties in the event of a discovery. In this paper, we analyze how the uncertainty in the dark matter speed distribution near the Sun is affected by baryonic feedback, halo-to-halo variance, and halo mass. To do so, we harness the statistical power of the new DREAMS Cold Dark Matter simulation suite, which is comprised of 1024 zoom-in Milky Way-mass halos with varied initial conditions as well as cosmological and astrophysical parameters. Applying a normalizing flows emulator to these simulations, we find that the uncertainty in the local DM speed distribution is dominated by halo-to-halo variance and, to a lesser extent, uncertainty in host halo mass. Uncertainties in supernova and black hole feedback (from the IllustrisTNG model in this case) are negligible in comparison. Using the DREAMS suite, we present a state-of-the-art prediction for the DM speed distribution in the Milky Way. Although the Standard Halo Model is contained within the uncertainty of this prediction, individual galaxies may have distributions that differ from it. Lastly, we apply our DREAMS results to the XENON1T experiment and demonstrate that the astrophysical uncertainties are comparable to the experimental ones, solidifying previous results in the literature obtained with a smaller sample of simulated Milky Way-mass halos.
