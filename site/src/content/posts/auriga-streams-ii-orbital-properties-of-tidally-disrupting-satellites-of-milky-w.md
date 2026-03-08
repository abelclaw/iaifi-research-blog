---
abstract: Galaxies like the Milky Way are surrounded by complex populations of satellites
  at all stages of tidal disruption. In this paper, we present a dynamical study of
  the disrupting satellite galaxies in the Auriga simulations that are orbiting 28
  distinct Milky Way-mass hosts across three resolutions. We find that the satellite
  galaxy populations are highly disrupted. The majority of satellites that remain
  fully intact at present day were accreted recently without experiencing more than
  one pericentre ($n_{\rm peri} \lesssim 1$) and have large apocentres ($r_{\rm apo}
  \gtrsim 200$ kpc) and pericentres ($r_{\rm peri} \gtrsim 50$ kpc). The remaining
  satellites have experienced significant tidal disruption and, given full knowledge
  of the system, would be classified as stellar streams. We find stellar streams in
  Auriga across the range of pericentres and apocentres of the known Milky Way dwarf
  galaxy streams and, interestingly, overlapping significantly with the Milky Way
  intact satellite population. We find no significant change in satellite orbital
  distributions across resolution. However, we do see substantial halo-to-halo variance
  of $(r_\text{peri}, r_\text{apo})$ distributions across host galaxies, as well as
  a dependence of satellite orbits on host halo mass - systems disrupt at larger pericentres
  and apocentres in more massive hosts. Our results suggest that either cosmological
  simulations (including, but not limited to, Auriga) are disrupting satellites far
  too readily, or that the Milky Way's satellites are more disrupted than current
  imaging surveys have revealed. Future observing facilities and careful mock observations
  of these systems will be key to revealing the nature of this apparent discrepancy.
arxivId: '2410.09143'
arxivUrl: https://arxiv.org/abs/2410.09143
authors:
- Nora Shipp
- Alexander H. Riley
- Christine M. Simpson
- Rebekka Bieri
- Lina Necib
- Arpit Arora
- Francesca Fragkoudi
- Facundo A. Gómez
- Robert J. J. Grand
- Federico Marinacci
concepts:
- cosmological simulation
- tidal disruption
- stellar streams
- satellite orbital dynamics
- halo-to-halo variance
- galaxy classification
- dark matter
- model validation
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2410_09143/figure_1.png
- /iaifi-research-blog/figures/2410_09143/figure_1.png
- /iaifi-research-blog/figures/2410_09143/figure_2.png
- /iaifi-research-blog/figures/2410_09143/figure_2.png
- /iaifi-research-blog/figures/2410_09143/figure_3.png
- /iaifi-research-blog/figures/2410_09143/figure_3.png
pdfUrl: https://arxiv.org/pdf/2410.09143v1
published: '2024-10-11T18:00:00+00:00'
theme: Astrophysics
title: 'Auriga Streams II: orbital properties of tidally disrupting satellites of
  Milky Way-mass galaxies'
wordCount: 1009
---

## The Big Picture

Imagine the Milky Way as a slow cosmic shredder. Every galaxy that wanders too close gets stretched, pulled apart, and eventually dissolved into ghostly streams of stars, rivers of light tracing paths of systems that no longer exist as galaxies. Our own galaxy is surrounded by this wreckage: a graveyard of former satellites at every stage of dismemberment. Some survive intact. Some trail long stellar streamers. Some have dissolved so completely they're nearly impossible to find.

Astronomers have catalogued over 50 surviving satellite galaxies around the Milky Way and more than 100 candidate stellar streams, the scattered remnants of smaller systems torn apart by the Milky Way's gravity. But when researchers run computer simulations of Milky Way-like galaxies, the numbers don't match reality. Simulated galaxies tear their satellites apart far more aggressively than what we observe. Is something wrong with the simulations? Or have we simply missed most of the destruction happening around our own galaxy?

A new study led by Nora Shipp at the University of Washington attacks this question head-on, using the Auriga simulations (one of the most detailed cosmological models of Milky Way-mass galaxies ever run) to catalog the orbital histories of disrupting satellites across 28 different simulated galaxies.

> **Key Insight:** Simulations may be shredding satellite galaxies too aggressively, or our surveys of the Milky Way may be missing vast numbers of already-disrupted systems. Future telescopes may finally tell us which.

## How It Works

The Auriga simulations model the formation and evolution of 28 Milky Way-mass galaxies from cosmic dawn to today. They capture the full **baryonic physics** of ordinary matter: gas cooling into clouds, star formation, stellar explosions that push gas around, even magnetic fields. The team ran them at three different numerical resolutions to verify that their conclusions don't depend on simulation granularity.

![Figure 1](figure:1)

The first task was sorting every accreted system around each simulated host into three categories:

- **Intact satellites** — still gravitationally bound, roughly spherical
- **Stellar streams** — elongated tidal debris with a surviving progenitor core
- **Phase-mixed systems** — satellites so thoroughly dissolved that their stars blend invisibly into the surrounding stellar halo, like a drop of dye dispersed in water

This classification required full knowledge of each star's origin, information unavailable to observers but accessible to simulators.

The results were striking. The vast majority of satellites that look "intact" today were accreted very recently:

- Most surviving intact satellites have made fewer than one **pericentre passage**, meaning they haven't yet swung close enough to the host to feel its full tidal force
- They orbit at large distances, with apocentres (farthest orbital points) beyond 200 kiloparsecs and pericentres (closest approaches) above 50 kiloparsecs
- Any satellite that has made multiple close passes has already been shredded into a stream

The team then compared the orbital properties of simulated streams against known Milky Way stellar streams and intact dwarf galaxies. The discrepancy is vivid. Simulated streams cluster at larger orbits than Milky Way streams but overlap heavily with the orbits of Milky Way *intact* satellites. In simulations, those orbital zones are dominated by debris. In reality, they're occupied by galaxies that appear healthy.

![Figure 2](figure:2)

Resolution doesn't drive the discrepancy. Running the same galaxy at different numerical resolutions produces nearly identical orbital distributions, ruling out coarse simulations as the culprit. There is, however, substantial variation from one simulated galaxy to another. More massive hosts disrupt their satellites at systematically larger orbital distances, consistent with their stronger tidal fields.

## Why It Matters

This sharpens a genuine mystery at the heart of galaxy formation. The **ΛCDM cosmological model**, our standard framework for how structure forms in the universe, predicts that Milky Way-mass galaxies should be swimming in disrupted satellite remnants. Either those remnants exist and we haven't found them, or the simulations are wrong about how easily satellites get destroyed.

If simulations are over-disrupting satellites, it points to missing physics, perhaps in how dark matter halos respond to tidal forces, or how the galactic disk shocks orbiting systems. If the Milky Way really hosts many hidden streams, then current surveys like DES and SDSS have been missing them, likely because they're too faint or diffuse to detect. The upcoming Rubin Observatory's LSST could resolve this directly by reaching the surface brightness depths needed to reveal ultra-faint tidal structures.

The study also makes a case for multi-halo statistical approaches. By spanning 28 distinct Milky Way-mass hosts, Shipp and collaborators reveal that halo-to-halo variation is enormous. Drawing conclusions from any single simulated galaxy, however carefully constructed, is risky.

> **Bottom Line:** Milky Way-mass galaxies in current simulations disrupt their satellites far more thoroughly than observations suggest. Either our models have a flaw, or a vast hidden population of stellar streams is waiting to be discovered.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects high-performance cosmological simulation with observational survey science, using the Auriga suite to generate testable predictions about stellar stream populations that next-generation telescopes like the Rubin Observatory can directly probe.

- **Impact on Artificial Intelligence:** Classifying simulated satellites into intact, stream, and phase-mixed categories across tens of thousands of accreted systems is exactly the kind of large-scale population analysis that machine learning methods are increasingly built to handle, in both simulation and observational contexts.

- **Impact on Fundamental Interactions:** The results expose a tension in ΛCDM cosmology: either the physics governing tidal disruption of dark matter subhalos is incorrectly modeled, or current photometric surveys are blind to a substantial population of dissolved Milky Way satellites.

- **Outlook and References:** Future mock observations of Auriga streams at realistic survey depths will be critical for distinguishing simulation artifacts from observational incompleteness; the paper is available at [arXiv:2410.09143](https://arxiv.org/abs/2410.09143).
