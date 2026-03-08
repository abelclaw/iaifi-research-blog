---
abstract: 'We set the strongest limits to-date on the velocity-independent dark matter
  (DM) - proton cross section $σ$ for DM masses $m = 10\,\mathrm{keV}$ to $100\,\mathrm{GeV}$,
  using large-scale structure traced by the Lyman-alpha forest: e.g., a 95% lower
  limit $σ< 6 \times 10^{-30}\,\mathrm{cm}^2$, for $m = 100\,\mathrm{keV}$. Our results
  complement direct detection, which has limited sensitivity to sub-GeV DM. We use
  an emulator of cosmological simulations, combined with data from the smallest cosmological
  scales used to-date, to model and search for the imprint of primordial DM-proton
  collisions. Cosmological bounds are improved by up to a factor of 25.'
arxivId: '2111.10386'
arxivUrl: https://arxiv.org/abs/2111.10386
authors:
- Keir K. Rogers
- Cora Dvorkin
- Hiranya V. Peiris
concepts:
- dark matter
- lyman-alpha forest constraints
- cosmological simulation
- emulation
- matter power spectrum suppression
- bayesian inference
- surrogate modeling
- simulation-based inference
- active learning
- monte carlo methods
- effective field theory
- cosmic microwave background
figures:
- /iaifi-research-blog/figures/2111_10386/figure_1.png
- /iaifi-research-blog/figures/2111_10386/figure_2.png
- /iaifi-research-blog/figures/2111_10386/figure_3.png
pdfUrl: https://arxiv.org/pdf/2111.10386v2
published: '2021-11-19T19:00:02+00:00'
theme: Astrophysics
title: New limits on light dark matter - proton cross section from the cosmic large-scale
  structure
wordCount: 1039
---

## The Big Picture

Imagine trying to find a ghost by looking for the shadows it casts, not directly, but across cosmic scales stretching hundreds of millions of light-years. That's what physicists do when hunting for dark matter. It bends light, shapes galaxies, and sculpts the vast web of filaments and voids that make up the universe's large-scale structure. But what it actually *is* remains unknown.

For decades, the most sensitive dark matter searches have relied on underground detectors, waiting patiently for a rare particle to knock into an atomic nucleus and deliver a measurable jolt. This works well for dark matter at or above a proton's mass, roughly 1 GeV.

For *light* dark matter, though, the approach hits a wall. Particles hundreds or thousands of times lighter than a proton don't carry enough momentum to leave a detectable signal. They pass through detectors like whispers through a hurricane.

A team led by Keir Rogers, Cora Dvorkin, and Hiranya Peiris took a different path: using the universe itself as a detector. By analyzing faint patterns in light from distant quasars, they've set the tightest constraints ever on how often dark matter can collide with protons, covering nearly the entire light dark matter mass range from 10 keV to 100 GeV.

> **Key Insight:** By reading the cosmic fossil record encoded in quasar light, this team improved existing dark matter bounds by up to a factor of 25, without building any new hardware.

## How It Works

The cosmic detector here is the **Lyman-alpha forest**, a thicket of absorption lines imprinted on quasar spectra as their light passes through intergalactic hydrogen gas. Each absorption dip marks a clump of hydrogen that swallowed a photon at a specific wavelength. Together, these dips trace matter structure across cosmic scales, turning quasar spectra into one-dimensional maps of the universe's density field.

![Figure 1](figure:1)

If dark matter collides with protons in the very early universe, those collisions dampen the growth of small-scale structure. Think of dark matter clumps trying to collapse under gravity while being buffeted by constant proton collisions, like a ball bearing falling through honey. The result is a smoothing-out of structure that leaves a permanent imprint, visible billions of years later in the Lyman-alpha forest.

The strength of this suppression depends on two things: the dark matter mass and the **cross section**, the probability that two particles interact when they meet. Smaller cross sections leave subtler imprints. Lighter particles leave larger ones.

Comparing real quasar data against theoretical predictions for every possible mass and cross section combination would be computationally impossible. So the team built a machine-learning emulator: a trained neural network that predicts the **1D flux power spectrum** (how much structure the forest shows at different size scales) at a fraction of a full simulation's cost. They trained it on a grid of hydrodynamical simulations tracking 512³ dark matter and gas particles in a volume roughly 45 million light-years across, then validated it against independent runs.

The statistical inference required careful handling of several systematic effects:

- **IGM thermal state:** The temperature and density of the intergalactic medium affect the forest independently of dark matter, so these parameters were fit simultaneously.
- **Photoionization rate uncertainty:** Ultraviolet radiation from quasars and galaxies ionizes intergalactic hydrogen, altering the forest. An optical depth correction accounted for this uncertain background.
- **Primordial power spectrum:** Density fluctuations from the Big Bang were treated as a free parameter to prevent the dark matter signal from being confused with inflation's imprint.
- **Model robustness:** Bayesian optimization, an active learning technique, identified corners of parameter space where the emulator might fail. Targeted additional simulations patched those gaps.

![Figure 2](figure:2)

## Why It Matters

The results push into territory no previous constraint has reached: a 95% upper limit of σ < 6 × 10⁻³⁰ cm² at 100 keV, with bounds across the full 10 keV–100 GeV mass range surpassing all prior cosmological constraints. At the most sensitive mass scales, limits improved by a factor of 25. No new telescope, no new underground lab, just smarter use of existing data.

From a particle physics perspective, these bounds rule out large regions of parameter space for motivated candidates, including dark matter with a magnetic dipole moment, well beyond the reach of any current or planned direct detection experiment. Sub-GeV dark matter is genuinely hard to catch with nuclear recoils. Cosmology is one of the only handles available.

For cosmology, the work shows what high-fidelity simulation emulators can do when paired with small-scale observational data. The sub-Mpc scales used here had never been tapped for dark matter constraints in this way. As next-generation quasar surveys come online and simulators improve, the same framework can extend to velocity-dependent cross sections, exotic IGM heating scenarios, and combinations with CMB damping tail measurements.

![Figure 3](figure:3)

> **Bottom Line:** Using the cosmic fossil record of intergalactic hydrogen as a dark matter detector, Rogers, Dvorkin, and Peiris set the world's strongest limits on light dark matter, improving previous cosmological bounds by up to 25× across eight decades of mass. The universe itself turns out to be our best dark matter experiment.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work sits at the intersection of machine learning and observational cosmology. A neural-network emulator of hydrodynamical simulations made it possible to run statistical inference on dark matter microphysics from quasar spectra, a task that would be intractable with traditional simulation approaches alone.

- **Impact on Artificial Intelligence:** The use of Bayesian optimization as an active learning strategy to adaptively improve emulator accuracy in poorly-sampled parameter regions is a methodological contribution that applies well beyond this specific problem, to any physics simulation surrogate.

- **Impact on Fundamental Interactions:** The paper sets the strongest constraints to date on the dark matter–proton cross section for masses between 10 keV and 100 GeV, closing off large swaths of parameter space for light dark matter candidates including magnetic dipole models.

- **Outlook and References:** Future surveys with higher quasar resolution and density will enable even tighter bounds using this forward-modeling framework; full details are available at [arXiv:2111.10386](https://arxiv.org/abs/2111.10386).
