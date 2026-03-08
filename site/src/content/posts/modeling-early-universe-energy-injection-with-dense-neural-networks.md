---
abstract: We show that Dense Neural Networks can be used to accurately model the cooling
  of high-energy particles in the early universe, in the context of the public code
  package DarkHistory. DarkHistory self-consistently computes the temperature and
  ionization history of the early universe in the presence of exotic energy injections,
  such as might arise from the annihilation or decay of dark matter. The original
  version of DarkHistory uses large pre-computed transfer function tables to evolve
  photon and electron spectra in redshift steps, which require a significant amount
  of memory and storage space. We present a light version of DarkHistory that makes
  use of simple Dense Neural Networks to store and interpolate the transfer functions,
  which performs well on small computers without heavy memory or storage usage. This
  method anticipates future expansion with additional parametric dependence in the
  transfer functions without requiring exponentially larger data tables.
arxivId: '2207.06425'
arxivUrl: https://arxiv.org/abs/2207.06425
authors:
- Yitian Sun
- Tracy R. Slatyer
concepts:
- surrogate modeling
- transfer function interpolation
- dark matter
- emulation
- scalability
- regression
- cosmological simulation
- cosmic microwave background
- loss function design
- neural operators
- effective field theory
figures:
- /iaifi-research-blog/figures/2207_06425/figure_1.png
- /iaifi-research-blog/figures/2207_06425/figure_2.png
- /iaifi-research-blog/figures/2207_06425/figure_3.png
pdfUrl: https://arxiv.org/pdf/2207.06425v1
published: '2022-07-13T18:00:00+00:00'
theme: Astrophysics
title: Modeling early-universe energy injection with Dense Neural Networks
wordCount: 1125
---

## The Big Picture

Imagine trying to trace every ripple in a pond after throwing a stone. Not just the first splash, but every secondary wave bouncing off every edge, for billions of years. That's roughly the challenge physicists face when modeling the early universe. If dark matter (the invisible substance making up most of the universe's mass) occasionally transforms into bursts of high-energy particles, those particles slam into the hot, charged gas that filled the young cosmos, triggering cascades of secondary particles that ripple through cosmic history.

Understanding those cascades could unlock clues about dark matter's identity. But the computational cost of tracking them has long been a bottleneck.

The code package `DarkHistory` was built to handle this problem. It computes how the temperature and electrical state of the gas between galaxies (the **intergalactic medium**, or IGM) evolve when dark matter injects energy it wouldn't under standard physics. But the original version carries a heavy price: roughly 18 gigabytes of pre-computed lookup tables that must sit in memory during every simulation. For researchers without access to powerful lab computers, that's a serious obstacle.

Yitian Sun and Tracy Slatyer at MIT found a smarter way to store all that information. They trained compact neural networks to replace the tables entirely, shrinking the memory footprint by a factor of roughly 400 without meaningfully sacrificing accuracy.

> **Key Insight:** Dense Neural Networks can replace multi-gigabyte physics lookup tables in cosmological simulations, achieving comparable accuracy at a fraction of the storage and memory cost, and making advanced dark matter research accessible on a laptop.

## How It Works

The heart of `DarkHistory` is a set of **transfer functions**: mathematical objects that take an input bundle of particles (say, a burst of photons from annihilating dark matter) and output the secondary particles produced after one step of cosmic evolution. Think of them as detailed recipes. Given this mix of energetic particles at this moment in cosmic history, here's what you get after the universe expands a little further. The problem is storage: each transfer function table runs about 1.5 gigabytes, and a standard run needs 12 loaded simultaneously.

![Figure 1](figure:1)

Sun and Slatyer's approach is clean. Instead of storing a giant pre-computed matrix, they train a **Dense Neural Network (DNN)**, a standard multi-layer network where every unit connects to every unit in adjacent layers, to *learn* each transfer function as a smooth mathematical mapping.

The network takes five inputs: the energy of the incoming particle, the energy of the outgoing particle, the current **redshift** (a measure of how much the universe has expanded, used as a proxy for cosmic time), the fraction of hydrogen atoms that have lost their electrons, and the equivalent fraction for helium. It outputs a single number: the log of the transfer function value at that point. To reconstruct the full matrix, you evaluate the DNN across the grid of relevant energies.

The training process:

1. Generate a dense grid of training data from the original high-fidelity tables
2. Train separate DNNs for each transfer function type (photon-to-photon, electron-to-photon, etc.)
3. Validate against held-out data, confirming that temperature and ionization histories reproduce the original results to within a few percent

The DNN-based `DarkHistory` reproduces the hydrogen ionization history and IGM temperature to sub-percent accuracy in the regions that matter most (when species are more than 10% ionized) and to within a few percent everywhere else.

The approach also reproduces subtle distortions in the **CMB** (Cosmic Microwave Background, the faint glow of ancient light still detectable today), matching the original to within 10%. Current experimental uncertainties from CMB observations are themselves larger, so the approximation is more than adequate for real science.

![Figure 2](figure:2)

There's a bonus baked into the neural network approach: **automatic interpolation**. The original tables were defined on a fixed grid, and values between grid points required manual interpolation. DNNs are continuous functions. They return sensible values at any parameter combination within the training range. Future versions of `DarkHistory` could work with flexible binning schemes or sparse training data, opening doors that rigid lookup tables keep shut.

## Why It Matters

The practical payoff is immediate: a researcher with a standard laptop can now run `DarkHistory` without loading 18 gigabytes into RAM. But the deeper point is about scalability.

The original table-based approach has a fundamental flaw. Adding a new physical parameter (say, a dependence on helium temperature or the density of ordinary matter) requires multiplying the table size by the number of steps in that new parameter. Storage demands explode exponentially.

Neural networks don't work that way. Adding a new input increases the network's complexity only modestly, roughly a constant-size increase in neurons regardless of how finely you sample the new parameter. That's the difference between a method that scales and one that hits a wall.

![Figure 3](figure:3)

This work fits into a broader wave of machine learning applications in theoretical physics, where neural networks increasingly stand in for expensive computations: full simulations of particle collisions, galaxy formation, and more. Sun and Slatyer aren't using AI to find new patterns in observations. They're compressing and generalizing hard-won physical knowledge so more scientists can use it. Future extensions of `DarkHistory`, from dark matter decaying into multiple channels to position-dependent energy injection, now have a clear computational path forward.

> **Bottom Line:** By swapping 18 GB of lookup tables for a handful of compact neural networks, this work makes dark matter cosmology simulations far more accessible while laying the groundwork for a scalable `DarkHistory` that can handle more complex physics without exponentially growing storage demands.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects machine learning and early-universe cosmology, using Dense Neural Networks as physics emulators that compress complex particle-cascade physics into lightweight, portable models deployable on consumer hardware.

- **Impact on Artificial Intelligence:** Simple fully-connected DNNs serve as accurate, continuously interpolating surrogates for high-dimensional physical lookup tables, a generalizable approach applicable to any simulation that relies on pre-computed transfer matrices.

- **Impact on Fundamental Interactions:** By making `DarkHistory` accessible without heavy computing infrastructure, this work lowers the barrier to probing dark matter annihilation and decay constraints from the CMB and IGM temperature history, directly advancing the search for physics beyond the Standard Model.

- **Outlook and References:** Future work will extend the DNN transfer functions to include additional parametric dependencies, such as helium temperature or other IGM conditions, without the exponential storage costs of conventional tables; see [arXiv:2207.06425](https://arxiv.org/abs/2207.06425) for the full paper.

## Original Paper Details
- **Title:** Modeling early-universe energy injection with Dense Neural Networks
- **arXiv ID:** 2207.06425
- **Authors:** ["Yitian Sun", "Tracy R. Slatyer"]
- **Abstract:** We show that Dense Neural Networks can be used to accurately model the cooling of high-energy particles in the early universe, in the context of the public code package DarkHistory. DarkHistory self-consistently computes the temperature and ionization history of the early universe in the presence of exotic energy injections, such as might arise from the annihilation or decay of dark matter. The original version of DarkHistory uses large pre-computed transfer function tables to evolve photon and electron spectra in redshift steps, which require a significant amount of memory and storage space. We present a light version of DarkHistory that makes use of simple Dense Neural Networks to store and interpolate the transfer functions, which performs well on small computers without heavy memory or storage usage. This method anticipates future expansion with additional parametric dependence in the transfer functions without requiring exponentially larger data tables.
