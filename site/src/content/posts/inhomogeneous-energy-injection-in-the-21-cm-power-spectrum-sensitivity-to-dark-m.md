---
abstract: 'The 21-cm signal provides a novel avenue to measure the thermal state of
  the universe during cosmic dawn and reionization (redshifts $z\sim 5-30$), and thus
  to probe energy injection from decaying or annihilating dark matter (DM). These
  DM processes are inherently inhomogeneous: both decay and annihilation are density
  dependent, and furthermore the fraction of injected energy that is deposited at
  each point depends on the gas ionization and density, leading to further anisotropies
  in absorption and propagation. In this work, we develop a new framework for modeling
  the impact of spatially inhomogeneous energy injection and deposition during cosmic
  dawn, accounting for ionization and baryon density dependence, as well as the attenuation
  of propagating photons. We showcase how this first completely inhomogeneous treatment
  affects the predicted 21-cm power spectrum in the presence of exotic sources of
  energy injection, and forecast the constraints that upcoming HERA measurements of
  the 21-cm power spectrum will set on DM decays to photons and to electron/positron
  pairs. These projected constraints considerably surpass those derived from CMB and
  Lyman-$α$ measurements, and for decays to electron/positron pairs they exceed all
  existing constraints in the sub-GeV mass range, reaching lifetimes of $\sim 10^{28}\,\mathrm{s}$.
  Our analysis demonstrates the unprecedented sensitivity of 21-cm cosmology to exotic
  sources of energy injection during the cosmic dark ages. Our code, $\mathtt{DM21cm}$,
  includes all these effects and is publicly available in an accompanying release.'
arxivId: '2312.11608'
arxivUrl: https://arxiv.org/abs/2312.11608
authors:
- Yitian Sun
- Joshua W. Foster
- Hongwan Liu
- Julian B. Muñoz
- Tracy R. Slatyer
concepts:
- dark matter
- 21-cm power spectrum
- inhomogeneous energy injection
- cosmological simulation
- reionization modeling
- signal detection
- simulation-based inference
- cosmic microwave background
- bayesian inference
- emulation
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2312_11608/figure_1.png
- /iaifi-research-blog/figures/2312_11608/figure_1.png
- /iaifi-research-blog/figures/2312_11608/figure_2.png
- /iaifi-research-blog/figures/2312_11608/figure_2.png
- /iaifi-research-blog/figures/2312_11608/figure_3.png
- /iaifi-research-blog/figures/2312_11608/figure_3.png
pdfUrl: https://arxiv.org/pdf/2312.11608v1
published: '2023-12-18T19:00:00+00:00'
theme: Astrophysics
title: 'Inhomogeneous Energy Injection in the 21-cm Power Spectrum: Sensitivity to
  Dark Matter Decay'
wordCount: 1126
---

## The Big Picture

Imagine finding a ghost by watching how it disturbs the fog around it. You can't see the ghost directly, but if you know exactly how fog behaves, how it swirls and thins in response to invisible disturbances, you can infer the ghost's presence with startling accuracy. That's what a team of MIT and collaborating researchers are doing with dark matter, using the faint radio glow of hydrogen gas from the universe's teenage years as their cosmic fog machine.

The universe between roughly 100 million and a billion years old sits in a peculiar observational blind spot. Too late for the **cosmic microwave background (CMB)**, the faint afterglow of the Big Bang, to probe well. Too early for conventional galaxy surveys. This era, called **cosmic dawn**, is when the first stars lit up and triggered **reionization**: the transformation of the universe from a fog of neutral hydrogen into the transparent sea of charged particles we observe today. Threaded through all of this is dark matter, which makes up 27% of the universe's energy budget but has never been directly detected. If dark matter particles decay or annihilate, they release energy that heats and ionizes the surrounding hydrogen gas in distinctive ways.

The team built a new simulation framework called `DM21cm` that, for the first time, models these dark matter energy injections accounting for effects that vary from place to place rather than smearing everything into a single average. The result: projected sensitivity to dark matter lifetimes that crushes all previous constraints.

> **Key Insight:** By treating dark matter energy injection as spatially variable rather than uniform, the researchers tapped the full discriminating power of 21-cm cosmology. Their forecasted constraints on dark matter lifetimes surpass the CMB, Lyman-α, and all existing sub-GeV measurements combined.

## How It Works

The **21-cm signal** is produced by neutral hydrogen atoms flipping the spin orientation of their electron, a quantum mechanical quirk that releases a radio photon at 21 centimeters wavelength. As the universe expands, this signal gets **redshifted** (stretched to longer wavelengths by cosmic expansion), encoding both time and spatial information. Upcoming radio interferometers like **HERA** (Hydrogen Epoch of Reionization Array) will measure the **21-cm power spectrum**: a statistical map of how the 21-cm signal varies across the sky at different cosmic epochs.

Dark matter makes this picture richer. When a dark matter particle decays into photons or electron-positron pairs (a matter-antimatter pair that immediately annihilates), those products scatter through the **intergalactic medium**, the sparse gas filling the vast spaces between galaxies, depositing their energy unevenly depending on:

- **Local gas density**: denser regions absorb more energy
- **Local ionization state**: partially ionized gas interacts differently than neutral gas
- **Propagation distance**: high-energy photons travel farther before being absorbed

Previous work averaged these effects over large volumes, assuming dark matter heats everything uniformly. DM21cm throws out that assumption. The team coupled `21cmFAST`, the standard simulator for 21-cm cosmology, with `DarkHistory`, a code that tracks energy deposition physics in the early universe. Together, these codes evolve gas temperature, ionization fraction, and the 21-cm signal jointly across a three-dimensional grid of the cosmos.

![Figure 1](figure:1)

The **lightcone** comparison in Figure 1 makes the difference plain. A lightcone maps properties across both space and cosmic time simultaneously, and here a 1 keV dark matter particle decaying to photons produces very different spatial patterns in the 21-cm **brightness temperature** (the strength of the radio signal as measured by astronomers) depending on whether you use the inhomogeneous treatment or the old homogenized approximation. In the inhomogeneous case, heating and ionization track the underlying dark matter distribution, creating spatial structure that the power spectrum can latch onto.

![Figure 2](figure:2)

## Why It Matters

The payoff is in the projected constraints. The team used their simulations to forecast what HERA's upcoming measurements could reveal about dark matter decaying to two final states: photons (γγ) and electron-positron pairs (e+e-).

For decays to photons, projected HERA constraints surpass CMB bounds across a wide mass range. For decays to electron-positron pairs, the results are even more dramatic: projected constraints exceed *all existing constraints* in the sub-GeV mass range, probing dark matter lifetimes as long as ~10²⁸ seconds. The age of the universe is about 4 × 10¹⁷ seconds. HERA could potentially detect the decay of particles that live roughly 25 billion times longer than the cosmos has existed.

The spatial treatment matters quantitatively, not just visually. Different regions respond differently to dark matter energy injection, so the power spectrum carries additional information that the homogeneous approximation throws away. The full inhomogeneous calculation captures correlations between dark matter density, gas density, and ionization state, sharpening the predicted signal shape and breaking degeneracies with uncertain astrophysical parameters like the X-ray luminosity of early galaxies.

![Figure 4](figure:4)

What this really means is that 21-cm cosmology is growing into a precision dark matter probe. The CMB has long been the gold standard for early-universe constraints on exotic physics. These projections show that HERA, and eventually the **Square Kilometre Array (SKA)**, could become the dominant tool for probing dark matter in the sub-GeV mass range, where collider experiments lose sensitivity and direct detection faces fundamental background challenges.

The `DM21cm` code is publicly available and built for flexibility. It can accommodate arbitrary energy injection processes, not just dark matter decay. Future researchers could plug in annihilation channels, primordial black holes, or other speculative physics using the same infrastructure. Extending the framework to annihilating dark matter, where the signal scales as density squared and amplifies inhomogeneity effects further, is the natural next step.

> **Bottom Line:** DM21cm delivers the first fully inhomogeneous treatment of dark matter energy injection in 21-cm simulations. The projected HERA constraints it forecasts would set unprecedented bounds on sub-GeV dark matter lifetimes, making radio cosmology one of our sharpest tools for hunting dark matter.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects computational cosmology, particle physics, and radio astronomy by coupling state-of-the-art simulation tools into a unified framework that translates microphysical dark matter models into observable radio signatures across cosmic time.

- **Impact on Artificial Intelligence:** The DM21cm framework shows how combining physics-informed simulation codes can dramatically extend theoretical reach; the publicly released code enables rapid parameter-space exploration that would be computationally prohibitive with full hydrodynamic simulations.

- **Impact on Fundamental Interactions:** By developing the first completely inhomogeneous treatment of exotic energy injection in 21-cm cosmology, this work produces projected constraints on dark matter lifetimes that exceed all existing bounds in the sub-GeV mass range, reaching lifetimes of ~10²⁸ seconds.

- **Outlook and References:** HERA is already collecting data, making these forecasts immediately actionable, with the Square Kilometre Array promising even deeper reach in the coming decade; the full analysis and DM21cm code are described in [arXiv:2312.11608](https://arxiv.org/abs/2312.11608).
