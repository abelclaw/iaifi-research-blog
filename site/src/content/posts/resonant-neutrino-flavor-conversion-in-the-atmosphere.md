---
abstract: Neutrinos produced in the atmosphere traverse a column density of air before
  being detected at neutrino observatories like IceCube or KM3NeT. In this work, we
  extend the neutrino flavor evolution in the {nuSQuIDS} code accounting for the varying
  height of neutrino production and the variable air density in the atmosphere. These
  effects can lead to sizeable spectral distortions in standard neutrino oscillations
  and are crucial to accurately describe some new physics scenarios. As an example,
  we study a model of quasi-sterile neutrinos that induce resonant flavor conversions
  at neutrino energies of ${O}(300)\text{ MeV}$ in matter densities of $1 \text{ g/cm}^3$.
  In atmospheric air densities, the same resonance is then realized at neutrino energies
  of ${O}(300- 700)$~GeV. We find that the new resonance can deplete the $ν_μ+ \overlineν_μ$
  flux at the IceCube Neutrino Observatory by as much as $10\%$ in the direction of
  the horizon.
arxivId: '2405.12140'
arxivUrl: https://arxiv.org/abs/2405.12140
authors:
- Connor Sponsler
- Matheus Hostert
- Ivan Martinez-Soler
- Carlos A. Argüelles
concepts:
- msw resonance
- atmospheric neutrino oscillations
- neutrino detection
- quasi-sterile neutrinos
- new physics searches
- spectral distortions
- effective field theory
- signal detection
- monte carlo methods
- standard model
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2405_12140/figure_1.png
- /iaifi-research-blog/figures/2405_12140/figure_1.png
pdfUrl: https://arxiv.org/pdf/2405.12140v1
published: '2024-05-20T16:02:55+00:00'
theme: Experimental Physics
title: Resonant Neutrino Flavor Conversion in the Atmosphere
wordCount: 1162
---

## The Big Picture

Imagine shining a flashlight through a fog bank. The light that reaches you isn't quite what went in: the fog has scattered, filtered, and changed it. Now replace the flashlight with a particle accelerator, the fog with Earth's atmosphere, and the light with neutrinos, subatomic particles that barely interact with ordinary matter. What you get is one of the strangest transformations in physics: neutrinos literally changing identity as they travel.

This shape-shifting is called **neutrino oscillation**. Neutrinos come in three "flavors" (electron, muon, and tau), and quantum mechanics allows them to spontaneously switch between these identities as they travel through space or matter.

When matter is involved, the switching can become **resonant**, locked into a feedback loop that dramatically amplifies the conversion rate. Think of a tuning fork vibrating most powerfully at exactly the right frequency. This phenomenon, known as the **Mikheev-Smirnov-Wolfenstein (MSW) effect**, explains why neutrinos streaming from the Sun arrive at Earth having swapped into a different flavor than the one they started with.

A team of physicists has now pushed this physics into new territory. They've shown that Earth's atmosphere, the thin shell of air clinging to our planet, can itself act as a resonance chamber for exotic neutrino flavor conversion. The result would be a detectable dip in the rate of muon-type neutrinos arriving at giant observatories like IceCube.

> **Key Insight:** If a new type of neutrino resonance occurs at ~300 MeV in dense laboratory matter, the same resonance will appear at ~300–700 GeV in the low-density air of Earth's atmosphere, and IceCube could see it as a 10% dip in the muon neutrino flux near the horizon.

## How It Works

The story begins with cosmic rays: high-energy protons and nuclei raining down from space. When they slam into atmospheric nuclei, they produce a shower of short-lived particles called pions and kaons, which decay into muon neutrinos. These atmospheric neutrinos are produced not at a single altitude but spread across a range of heights, from roughly 10 to 40 kilometers above the surface.

![Figure 1](/iaifi-research-blog/figures/2405_12140/figure_1.png)

That spread matters more than physicists had previously accounted for. The team upgraded **nuSQuIDS** (Neutrino Simple Quantum Integro-Differential Solver), a publicly available code for computing neutrino flavor evolution, to model the atmosphere as a proper three-dimensional spherical shell rather than an infinitely thin surface. When you track neutrinos produced at different heights traveling through air of varying density, the odds of a neutrino changing flavor shift and smear in ways that are observationally significant.

![Figure 2](/iaifi-research-blog/figures/2405_12140/figure_1.png)

The real payoff comes when you introduce **quasi-sterile neutrinos**, hypothetical particles immune to the weak nuclear force but still capable of affecting ordinary matter through some undiscovered interaction. The key physics unfolds in three steps:

- In dense laboratory matter (~1 g/cm³), quasi-sterile neutrinos would induce resonant flavor conversion at energies around **300 MeV**.
- Resonant conversion depends on the ratio of neutrino energy to background matter density. The atmosphere is roughly 1,000 times less dense than liquid water.
- Scaling up the energy to compensate for lower density, the **same resonance reappears at 300–700 GeV** in atmospheric air.

So would this resonance actually survive the journey? The atmosphere isn't uniform; it's warm and dense at low altitudes, thin and cold higher up. For a resonance to fully develop, it must remain narrow enough not to wash out, and neutrinos must be produced at high enough altitudes to traverse the resonance region. Both conditions hold, but only for neutrinos arriving from near the **horizon**, not from directly overhead or below.


## Why It Matters

On the practical side, this work delivers the first publicly available neutrino flavor evolution code that properly accounts for the extended geometry of the atmosphere. Even for ordinary three-neutrino oscillations, ignoring the height distribution of neutrino production introduces errors. Those corrections become mandatory when searching for new physics, and any future atmospheric neutrino analysis should incorporate them.

There's also a direct connection to long-standing anomalies in particle physics. Experiments like MiniBooNE and LSND have observed hints of muon-to-electron neutrino conversions at short distances that the standard three-neutrino picture cannot explain. Quasi-sterile neutrinos are one class of proposed solutions.

IceCube, the world's largest neutrino detector buried in a cubic kilometer of Antarctic ice, can test these models independently. The signature: a 10% deficit in the muon neutrino flux along the horizon. That's a smoking-gun signal with a distinctive angular pattern that would be very hard to fake with conventional physics.


This search would complement, not duplicate, existing sterile neutrino searches at IceCube. Those look for neutrinos coming up through the Earth, where the planet's core provides the dense matter needed for resonance. This new search looks sideways, along the horizon, where the atmosphere provides the resonance. Different geometry, different energy scale, different new-physics sensitivity.

> **Bottom Line:** By upgrading neutrino simulation software to treat the atmosphere as the extended, varying-density shell it actually is, this team revealed that exotic neutrino physics visible at short-baseline accelerator experiments would leave a distinctive 10% dip in the GeV-to-TeV muon neutrino flux at IceCube, a new handle on particle physics' most stubborn anomalies.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects computational particle physics with observational neutrino astronomy, upgrading open-source simulation tools (nuSQuIDS) to link short-baseline laboratory anomalies to signals in a cubic-kilometer Antarctic ice detector.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The improved nuSQuIDS framework enables more accurate training data and likelihood calculations for machine-learning-based neutrino event classification and new-physics inference at IceCube and KM3NeT.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The atmospheric air column acts as a resonance chamber for quasi-sterile neutrino conversion at 300–700 GeV, offering a geometry-distinct probe of beyond-Standard-Model neutrino interactions motivated by the MiniBooNE and LSND anomalies.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work can implement this framework in full IceCube likelihood analyses to set constraints on, or discover, quasi-sterile neutrino mixing; the study is available at [arXiv:2405.12140](https://arxiv.org/abs/2405.12140).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Resonant Neutrino Flavor Conversion in the Atmosphere</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2405.12140</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Connor Sponsler", "Matheus Hostert", "Ivan Martinez-Soler", "Carlos A. Argüelles"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Neutrinos produced in the atmosphere traverse a column density of air before being detected at neutrino observatories like IceCube or KM3NeT. In this work, we extend the neutrino flavor evolution in the {nuSQuIDS} code accounting for the varying height of neutrino production and the variable air density in the atmosphere. These effects can lead to sizeable spectral distortions in standard neutrino oscillations and are crucial to accurately describe some new physics scenarios. As an example, we study a model of quasi-sterile neutrinos that induce resonant flavor conversions at neutrino energies of ${O}(300)\text{ MeV}$ in matter densities of $1 \text{ g/cm}^3$. In atmospheric air densities, the same resonance is then realized at neutrino energies of ${O}(300- 700)$~GeV. We find that the new resonance can deplete the $ν_μ+ \overlineν_μ$ flux at the IceCube Neutrino Observatory by as much as $10\%$ in the direction of the horizon.</span></div></div>
</div>
