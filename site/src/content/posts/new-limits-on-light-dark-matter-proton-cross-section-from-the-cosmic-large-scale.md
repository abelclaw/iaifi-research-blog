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

Imagine trying to find a ghost by looking for the shadows it casts — not directly, but across cosmic scales stretching hundreds of millions of light-years. That's essentially what physicists do when hunting for dark matter. We know it's there: it bends light, shapes galaxies, and sculpts the vast web of filaments and voids making up the large-scale structure of the universe. But its fundamental nature — what it's made of, how it interacts with ordinary matter — remains one of science's deepest mysteries.

For decades, the most sensitive dark matter searches have relied on underground detectors, waiting patiently for a rare particle to knock into an atomic nucleus and deliver a measurable jolt. This works brilliantly for dark matter at or above a proton's mass — roughly 1 GeV.

But for *light* dark matter — particles hundreds or thousands of times lighter than a proton — the approach hits a wall. Lightweight particles don't carry enough momentum to leave a detectable signal. They pass through detectors like whispers through a hurricane.

A team led by Keir Rogers, Cora Dvorkin, and Hiranya Peiris has charted a fundamentally different path: using the universe itself as a detector. By analyzing faint patterns in light from distant quasars, they've set the tightest constraints ever on how often dark matter can collide with protons — across nearly the entire light dark matter mass range, from 10 keV to 100 GeV.

> **Key Insight:** By reading the cosmic fossil record encoded in quasar light, this team improved existing dark matter bounds by up to a factor of 25 — without building any new hardware.

## How It Works

The researchers' cosmic detector is the **Lyman-alpha forest** — a thicket of absorption lines imprinted on quasar spectra as their light passes through intergalactic hydrogen gas. Each absorption dip marks a clump of hydrogen that swallowed a photon at a specific wavelength. Collectively, these dips trace matter structure across cosmic scales, turning quasar spectra into one-dimensional maps of the universe's density field.

![Figure 1](/iaifi-research-blog/figures/2111_10386/figure_1.png)

If dark matter collides with protons in the very early universe, those collisions dampen the growth of small-scale structure. Picture dark matter clumps trying to collapse under gravity while being buffeted by constant proton collisions — like a ball bearing falling through honey. The result is a smoothing-out of structure that leaves a permanent imprint, visible billions of years later in the Lyman-alpha forest.

The strength of this suppression depends on two things: the dark matter mass and the **cross section** — the probability that two particles interact when they meet. Smaller cross sections leave subtler imprints; lighter particles leave larger ones.

Comparing real quasar data against theoretical predictions for every possible mass and cross section combination would be computationally impossible. The team's solution: a **machine-learning emulator**, a trained neural network that predicts the **1D flux power spectrum** — how much structure the forest shows at different size scales — at a fraction of a full simulation's cost. The emulator was trained on a grid of hydrodynamical simulations tracking 512³ dark matter and gas particles in a volume roughly 45 million light-years across, then validated against independent runs.

The statistical inference required careful handling of several systematic effects:

- **IGM thermal state:** The temperature and density of the intergalactic medium (IGM) — the thin gas between galaxies — affects the forest independently of dark matter, so it was fit simultaneously.
- **Photoionization rate uncertainty:** Ultraviolet radiation from quasars and galaxies ionizes intergalactic hydrogen, altering the forest. An optical depth correction accounted for this uncertain background.
- **Primordial power spectrum:** Density fluctuations from the Big Bang were treated as a free parameter, preventing the dark matter signal from being confused with inflation's imprint.
- **Model robustness:** **Bayesian optimization** — an active learning technique — identified corners of parameter space where the emulator might fail, prompting targeted additional simulations to patch those gaps.

![Figure 2](/iaifi-research-blog/figures/2111_10386/figure_2.png)

## Why It Matters

The results push into territory no previous constraint has reached: a 95% upper limit of σ < 6 × 10⁻³⁰ cm² at 100 keV, with bounds across the full 10 keV–100 GeV mass range surpassing all prior cosmological constraints. At the most sensitive mass scales, limits improved by a factor of 25 — no new telescope, no new underground lab, just smarter use of existing data.

The significance runs in two directions. For particle physics, these bounds constrain a range of motivated candidates — including dark matter with a magnetic dipole moment — beyond the reach of any current or planned direct detection experiment. Sub-GeV dark matter is genuinely hard to catch with nuclear recoils; cosmology remains one of the only handles available.

For cosmology, this work demonstrates what becomes possible when high-fidelity simulation emulators meet small-scale observational data. The sub-Mpc scales exploited here had never been used for dark matter constraints this way. As next-generation quasar surveys come online and simulators improve, the same framework can extend to velocity-dependent cross sections, exotic IGM heating scenarios, and combinations with CMB damping tail measurements.

![Figure 3](/iaifi-research-blog/figures/2111_10386/figure_3.png)

> **Bottom Line:** Using the cosmic fossil record of intergalactic hydrogen as a dark matter detector, Rogers, Dvorkin, and Peiris set the world's strongest limits on light dark matter — improving previous cosmological bounds by up to 25× across eight decades of mass, proving that the universe itself is our best dark matter experiment.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges machine learning and observational cosmology, deploying a neural-network emulator of hydrodynamical simulations to enable statistical inference on dark matter microphysics from quasar spectra — a task intractable with traditional simulation approaches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Using Bayesian optimization as an active learning strategy to adaptively improve emulator fidelity in poorly-sampled parameter regions represents a methodological advance applicable to any physics simulation surrogate.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper delivers the strongest-ever constraints on the dark matter–proton cross section for masses between 10 keV and 100 GeV, closing off large swaths of parameter space for light dark matter candidates including magnetic dipole models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future surveys with higher quasar resolution and density will enable even tighter bounds using this forward-modeling framework; full details are available at arXiv:2204.07633.</span></div></div>
</div>
