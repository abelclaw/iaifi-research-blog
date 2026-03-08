---
abstract: "We build a theoretical range for the Milky Way's (MW) inner dark matter\
  \ (DM) distribution informed by the FIRE-2, Auriga, VINTERGATAN-GM, and TNG50 simulation\
  \ suites assuming the canonical cold dark matter (CDM) model. The DM density profiles\
  \ in Auriga, VINTERGATAN-GM, and TNG50 can be approximately modeled using the adiabatic\
  \ contraction prescription of Gnedin et al. 2004, while FIRE-2 has stronger baryonic\
  \ feedback, leading to a departure from the adiabatic contraction model. The simulated\
  \ halos that are adiabatically contracted are close to spherical (axis ratio $q\
  \ \\in [0.75-0.9]$ at $5^\\circ$), whereas halos that experience strong baryonic\
  \ feedback are oblate ($q \\in [0.5-0.7]$). Using the adiabatic contraction and\
  \ strong baryonic feedback models, along with the observed stellar distribution\
  \ of the MW, the inner logarithmic density slope for CDM in the MW is predicted\
  \ to range from $ -0.5$ to $-1.3$. The $J$-factor, which determines the DM-annihilation\
  \ flux, averaged over a solid angle of $5^\\circ$ ($10^\\circ$) is predicted to\
  \ span the range $0.8$-$30$ ($0.6$-$10$) $\\times 10^{23} \\rm{GeV}^2/\\rm{cm}^5$.\
  \ The $D$-factor, which determines the flux due to DM decay, is predicted to be\
  \ in the range $0.6$-$2$ ($0.5-1$) $\\times10^{23} \\rm{GeV}/\\rm{cm}^2$.\n  GitHub:\
  \ The results for this work can be found at https://github.com/abdelazizhussein/MW-Inner-DM-Profile."
arxivId: '2501.14868'
arxivUrl: https://arxiv.org/abs/2501.14868
authors:
- Abdelaziz Hussein
- Lina Necib
- Manoj Kaplinghat
- Stacy Y. Kim
- Andrew Wetzel
- Justin I. Read
- Martin P. Rey
- Oscar Agertz
concepts:
- dark matter
- cosmological simulation
- adiabatic contraction
- baryonic feedback
- simulation-based inference
- j-factor and d-factor
- surrogate modeling
- density estimation
- bayesian inference
- monte carlo methods
- inverse problems
figures:
- /iaifi-research-blog/figures/2501_14868/figure_1.png
- /iaifi-research-blog/figures/2501_14868/figure_1.png
- /iaifi-research-blog/figures/2501_14868/figure_2.png
- /iaifi-research-blog/figures/2501_14868/figure_2.png
- /iaifi-research-blog/figures/2501_14868/figure_3.png
- /iaifi-research-blog/figures/2501_14868/figure_3.png
pdfUrl: https://arxiv.org/pdf/2501.14868v1
published: '2025-01-24T19:00:01+00:00'
theme: Astrophysics
title: Theoretical Predictions for the Inner Dark Matter Distribution in the Milky
  Way Informed by Simulations
wordCount: 1321
---

## The Big Picture

Imagine trying to find something you've never seen, hiding inside a room so crowded with furniture that you can barely move, and the lights are off. That's roughly the challenge facing astronomers trying to map dark matter in the heart of our own galaxy.

The Milky Way's center is one of the most extreme environments in the universe. Dust chokes out visible light, billions of stars blur together in tight clusters, and ordinary matter dominates so thoroughly that the dark matter signal is nearly impossible to tease out.

Dark matter makes up roughly 85% of all matter in the universe, yet we've never detected it directly. We know it's there because its gravity shapes galaxies, bends light, and drives cosmic structure. But *where exactly* it sits, especially deep in the core of our own galaxy, remains stubbornly uncertain.

That uncertainty has real consequences. Searches for signals produced when dark matter particles collide or decay depend on knowing how much dark matter is packed into the galactic center. A factor of 10 uncertainty in density translates directly to a factor of 100 uncertainty in the expected signal.

A team led by Abdelaziz Hussein and Lina Necib at MIT took a new approach. Instead of measuring the dark matter distribution directly (which tracking individual stellar motions can barely constrain within about 20,000 light-years of the center), they bracketed the plausible range using four simulation suites of galaxy formation, anchored to what we actually observe about the Milky Way's stars.

> **Key Insight:** By using the physics of how ordinary matter reshapes dark matter halos, through either gravitational contraction or explosive stellar feedback, the team established a theoretically grounded range for the Milky Way's inner dark matter profile. This narrows the uncertainty space for detection experiments from "anything goes" to a principled window.

## How It Works

When stars form in a galactic center, what happens to the dark matter? Two competing forces reshape the **dark matter halo**, the extended, roughly spherical cloud of dark matter enveloping a galaxy:

- **Adiabatic contraction (AC):** As ordinary matter accumulates in the galactic center, its gravity drags dark matter inward, creating a denser, sharper concentration called a **cusp**. This is what you'd expect absent any violent disruption.
- **Baryonic feedback:** Supernovae, stellar winds, and **AGN** (active galactic nuclei, supermassive black holes in their energetic phase) drive repeated gas outflows. The gravitational potential fluctuates rapidly, flinging dark matter outward and carving out a shallower **core** instead.

The team analyzed six Milky Way-mass galaxies drawn from four simulation suites: Auriga, VINTERGATAN-GM, TNG50, and FIRE-2. Each implements these physical processes differently. Three suites (Auriga, VINTERGATAN-GM, TNG50) produce dark matter profiles that closely match the adiabatic contraction prescription of Gnedin et al. 2004. Stellar feedback in those models isn't strong enough to disrupt the contraction. FIRE-2 is the outlier: its stronger feedback drives the inner dark matter distribution outward, puffing up the halo.

![Figure 1](/iaifi-research-blog/figures/2501_14868/figure_1.png)

The ratio shown above tells the story. In FIRE-2, dark matter mass in the inner regions consistently falls below the AC prediction; feedback has won. In the other three suites, the ratio stays near 1.0, meaning AC dominates. These two regimes define the bookends of the team's theoretical range.

With these simulation-calibrated models in hand, the researchers plugged in the *observed* stellar distribution of the actual Milky Way. They didn't use simulated galaxies as direct stand-ins. Instead, they used them to calibrate the physics, then applied that physics to real observations. The result is a predicted **inner density slope**, how steeply dark matter density rises toward the galactic center, ranging from **−0.5** (a shallow, feedback-scoured core) to **−1.3** (a steep, adiabatically contracted cusp). The classic **NFW profile** (a standard theoretical baseline for how dark matter density varies with radius) has a slope of −1 at small radii, so the range spans shallower to slightly steeper than this benchmark.

The team also characterized the *shape* of the halo. Adiabatically contracted halos are nearly spherical, with axis ratios q (where 1.0 is perfectly round) in the range [0.75–0.9] at 5° from the galactic center. FIRE-2-like halos are oblate, squashed along the disk axis, with q in [0.5–0.7]. This morphological difference matters for indirect detection searches, which routinely assume spherical symmetry.

![Figure 2](/iaifi-research-blog/figures/2501_14868/figure_1.png)

## Why It Matters

The **J-factor**, which governs how bright a signal from annihilating dark matter particles would appear from the galactic center, spans nearly two orders of magnitude across the team's range: from 0.8 to 30 × 10²³ GeV²/cm⁵ when averaged over a 5° cone. The **D-factor**, governing signals from dark matter decay, ranges from 0.6 to 2 × 10²³ GeV/cm². These aren't free parameters. They're theoretically motivated bounds derived from simulations anchored to real stellar data.

This reframes how the community should approach inner dark matter constraints. Current analyses with gamma-ray searches from Fermi-LAT, neutrino surveys, and planned future experiments routinely assume a specific profile shape and optimize for signal strength. Hussein and colleagues show that the shape itself is a major source of theoretical uncertainty, and that this uncertainty is physically meaningful. Telling apart the two feedback regimes isn't just an academic exercise; it's a prerequisite for interpreting any claimed detection or upper limit from the galactic center.

Future surveys measuring stellar motions with unprecedented precision, combined with higher-resolution simulations, could eventually pin down which regime our galaxy actually inhabits.

> **Bottom Line:** The Milky Way's inner dark matter profile remains uncertain by a factor of ~40 in J-factor, but that uncertainty is now bracketed by physics rather than parametric freedom, giving dark matter hunters a principled target window.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines cosmological simulation analysis, observational stellar data, and analytical dark matter physics to produce theoretically grounded predictions, bridging astrophysics and particle physics in a way characteristic of IAIFI's mission.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The framework treats simulation suites as physical emulators, calibrating complex subgrid physics models against observations. This approach of learning physical relationships from simulations and transferring them to real data is becoming a standard tool in AI-assisted scientific inference.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By bounding the J- and D-factors with physically motivated models, this work sharpens targets for indirect dark matter detection across gamma rays, neutrinos, and cosmic rays.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future high-resolution stellar kinematic surveys and next-generation simulations may discriminate between the adiabatic contraction and strong feedback regimes in the actual Milky Way; the paper is available at [arXiv:2501.14868](https://arxiv.org/abs/2501.14868).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Theoretical Predictions for the Inner Dark Matter Distribution in the Milky Way Informed by Simulations</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2501.14868</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Abdelaziz Hussein", "Lina Necib", "Manoj Kaplinghat", "Stacy Y. Kim", "Andrew Wetzel", "Justin I. Read", "Martin P. Rey", "Oscar Agertz"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We build a theoretical range for the Milky Way's (MW) inner dark matter (DM) distribution informed by the FIRE-2, Auriga, VINTERGATAN-GM, and TNG50 simulation suites assuming the canonical cold dark matter (CDM) model. The DM density profiles in Auriga, VINTERGATAN-GM, and TNG50 can be approximately modeled using the adiabatic contraction prescription of Gnedin et al. 2004, while FIRE-2 has stronger baryonic feedback, leading to a departure from the adiabatic contraction model. The simulated halos that are adiabatically contracted are close to spherical (axis ratio $q \in [0.75-0.9]$ at $5^\circ$), whereas halos that experience strong baryonic feedback are oblate ($q \in [0.5-0.7]$). Using the adiabatic contraction and strong baryonic feedback models, along with the observed stellar distribution of the MW, the inner logarithmic density slope for CDM in the MW is predicted to range from $ -0.5$ to $-1.3$. The $J$-factor, which determines the DM-annihilation flux, averaged over a solid angle of $5^\circ$ ($10^\circ$) is predicted to span the range $0.8$-$30$ ($0.6$-$10$) $\times 10^{23} \rm{GeV}^2/\rm{cm}^5$. The $D$-factor, which determines the flux due to DM decay, is predicted to be in the range $0.6$-$2$ ($0.5-1$) $\times10^{23} \rm{GeV}/\rm{cm}^2$.
  GitHub: The results for this work can be found at https://github.com/abdelazizhussein/MW-Inner-DM-Profile.</span></div></div>
</div>
