---
abstract: We present UV/optical/NIR observations and modeling of supernova (SN) 2024ggi,
  a type II supernova (SN II) located in NGC 3621 at 7.2 Mpc. Early-time ("flash")
  spectroscopy of SN 2024ggi within +0.8 days of discovery shows emission lines of
  H I, He I, C III, and N III with a narrow core and broad, symmetric wings (i.e.,
  IIn-like) arising from the photoionized, optically-thick, unshocked circumstellar
  material (CSM) that surrounded the progenitor star at shock breakout. By the next
  spectral epoch at +1.5 days, SN 2024ggi showed a rise in ionization as emission
  lines of He II, C IV, N IV/V and O V became visible. This phenomenon is temporally
  consistent with a blueward shift in the UV/optical colors, both likely the result
  of shock breakout in an extended, dense CSM. The IIn-like features in SN 2024ggi
  persist on a timescale of $t_{\rm IIn} = 3.8 \pm 1.6$ days at which time a reduction
  in CSM density allows the detection of Doppler broadened features from the fastest
  SN material. SN 2024ggi has peak UV/optical absolute magnitudes of $M_{\rm w2} =
  -18.7$ mag and $M_{\rm g} = -18.1$ mag that are consistent with the known population
  of CSM-interacting SNe II. Comparison of SN 2024ggi with a grid of radiation hydrodynamics
  and non-local thermodynamic equilibrium (nLTE) radiative-transfer simulations suggests
  a progenitor mass-loss rate of $\dot{M} = 10^{-2}$M$_{\odot}$ yr$^{-1}$ ($v_w$ =
  50 km/s), confined to a distance of $r < 5\times 10^{14}$ cm. Assuming a wind velocity
  of $v_w$ = 50 km/s, the progenitor star underwent an enhanced mass-loss episode
  in the last ~3 years before explosion.
arxivId: '2404.19006'
arxivUrl: https://arxiv.org/abs/2404.19006
authors:
- W. V. Jacobson-Galán
- K. W. Davis
- C. D. Kilpatrick
- L. Dessart
- R. Margutti
- R. Chornock
- R. J. Foley
- P. Arunachalam
- K. Auchettl
- C. R. Bom
- R. Cartier
- D. A. Coulter
- G. Dimitriadis
- D. Dickinson
- M. R. Drout
- A. T. Gagliano
- C. Gall
- B. Garretson
- L. Izzo
- D. O. Jones
- N. LeBaron
- H. -Y. Miao
- D. Milisavljevic
- Y. -C. Pan
- A. Rest
- C. Rojas-Bravo
- A. Santos
- H. Sears
- B. M. Subrayan
- K. Taggart
- S. Tinyanont
concepts:
- flash spectroscopy
- csm interaction
- shock breakout
- stellar evolution
- simulation-based inference
- inverse problems
- surrogate modeling
- supernova classification
- signal detection
- spectral methods
figures:
- /iaifi-research-blog/figures/2404_19006/figure_1.png
- /iaifi-research-blog/figures/2404_19006/figure_2.png
- /iaifi-research-blog/figures/2404_19006/figure_3.png
pdfUrl: https://arxiv.org/pdf/2404.19006v3
published: '2024-04-29T18:00:03+00:00'
theme: Astrophysics
title: 'SN 2024ggi in NGC 3621: Rising Ionization in a Nearby, CSM-Interacting Type
  II Supernova'
wordCount: 1064
---

## The Big Picture

Imagine a star roughly ten times the mass of our Sun has been quietly shedding its outer layers for years, a slow stellar wind, like a cosmic exhale. Then, in an instant, its core collapses and a titanic explosion rips outward. The shockwave slams into that previously shed material, and for a few fleeting days, the collision lights up like nothing else in the universe. That brief, violent glow carries a complete record of the star's final years, if you can catch it in time.

That's exactly what happened with SN 2024ggi, a Type II supernova discovered in April 2024 in the galaxy NGC 3621, about 23 million light-years away. Type II supernovae are triggered when a massive star's core collapses under its own gravity. Astronomers caught this one within less than a day of discovery, and what they found rewrote the story of how this star died. The surrounding gas wasn't just illuminated; it underwent a dramatic shift in chemistry within hours, revealing a star that had been frantically shedding mass in the years before its death.

A large international team led by W. V. Jacobson-Galán used rapid follow-up observations across ultraviolet, optical, and near-infrared wavelengths, combined with detailed computer simulations, to reconstruct the dying star's final chapter. They measured its mass-loss rate, the extent of shed material, and the timeline of its demise.

> **Key Insight:** SN 2024ggi captured a real-time "ionization rise," a spectral fingerprint never before seen so clearly, proving that the progenitor star underwent an intense mass-loss episode in the roughly three years before it exploded.

## How It Works

The technique behind this discovery is **flash spectroscopy**: grabbing a spectrum of a supernova within hours of discovery, before the initial radiation burst fades. When the explosion's leading edge first tears free of the star (an event called **shock breakout**, or SBO), it floods surrounding material with X-rays and ultraviolet light. For a brief window, that material glows with distinctive emission lines, a chemical fingerprint of what the star shed before dying.

![Figure 1](/iaifi-research-blog/figures/2404_19006/figure_1.png)

Within 0.8 days of discovery, the team detected emission lines of hydrogen, helium, carbon, and nitrogen, all characteristic of **circumstellar material (CSM)**: the gas cloud the star had shed into surrounding space. These lines had a distinctive shape, a narrow core with broad, symmetric wings produced by electron scattering. Astronomers call this profile "IIn-like."

Then came the surprise. By 1.5 days, less than 17 hours later, the spectrum had transformed. New, higher-ionization lines appeared: He II, C IV, N IV/V, and O V. These are highly energized forms of helium, carbon, nitrogen, and oxygen, each stripped of more electrons than before. Creating these ions requires more energetic photons, signaling that the gas had been hit by an even more intense radiation burst.

![Figure 2](/iaifi-research-blog/figures/2404_19006/figure_2.png)

The team interprets this rising ionization as evidence that the shockwave broke out not from the star's surface, but from deep within an extended, dense CSM cloud. The explosion had to punch through extra material before light could escape freely.

The IIn-like features persisted for roughly 3.8 days (±1.6 days), then faded as the fastest-moving ejecta became visible beneath. This timescale directly constrains how far the CSM extended and how dense it was.

To extract physical parameters, the team ran a grid of **radiation hydrodynamics** simulations (computer models that track how an explosion's energy heats, ionizes, and drives gas outward) combined with **non-local thermodynamic equilibrium (nLTE) radiative-transfer** calculations using the code CMFGEN, which models how light moves through gas not in simple equilibrium. The best-fit models yielded:

- A mass-loss rate of ~0.01 solar masses per year (10⁻² M☉ yr⁻¹)
- A wind velocity of ~50 km/s
- CSM confined within ~5 × 10¹⁴ cm (~33 astronomical units, roughly Neptune's orbital distance) of the star's center
- Enhanced mass loss beginning roughly 3 years before explosion

![Figure 3](/iaifi-research-blog/figures/2404_19006/figure_3.png)

SN 2024ggi peaked at absolute magnitude −18.7 in the ultraviolet and −18.1 in the optical, consistent with the broader population of CSM-interacting Type II supernovae.


## Why It Matters

Red supergiants, the aging, bloated massive stars that precede Type II supernovae, shouldn't be shedding mass this quickly in their final years. Standard stellar evolution models predict relatively modest winds throughout a massive star's life. Yet SN 2024ggi adds to a growing body of evidence that something dramatic happens just before core collapse. Stars appear to enter a period of enhanced, eruptive mass loss that no current theory fully explains.

The proximity of SN 2024ggi (23 million light-years), combined with its rapid discovery and multi-wavelength coverage, made it one of the best-observed examples of this phenomenon to date. Future supernovae caught within minutes to hours of explosion could reveal whether this mass-loss surge is universal among Type II progenitors or specific to certain stellar masses and compositions.

Wide-field survey telescopes coming online soon, along with automated alert systems and machine-learning classifiers that flag young transients (newly exploded stars) in real time, will be essential for catching these critical early moments. Why massive stars convulse so violently just before core collapse remains an open question, one with implications for stellar feedback, galaxy evolution, and the neutron stars and black holes supernovae leave behind.


> **Bottom Line:** SN 2024ggi gave astronomers a rare, real-time window into a star's death throes, revealing furious mass loss in the progenitor's final years that challenges standard stellar models and points toward a violent, still-unexplained instability at the end of massive stellar evolution.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects observational astronomy, stellar physics, and high-performance computational modeling, using nLTE radiative-transfer simulations alongside multi-wavelength photometric and spectroscopic data to decode the final years of a massive star's life.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">SN 2024ggi's discovery relied on automated transient-detection pipelines and rapid-classification tools that increasingly incorporate machine learning. AI-assisted survey astronomy is becoming essential for time-critical science on timescales of hours.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By measuring the progenitor's mass-loss rate, wind velocity, and CSM geometry from first principles, this study provides direct empirical constraints on the poorly understood physics driving enhanced mass loss in red supergiants immediately before core collapse.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future facilities and real-time ML classifiers promise to catch more supernovae within minutes of shock breakout, further unlocking fleeting ionization signatures; the full study is available at [arXiv:2404.19006](https://arxiv.org/abs/2404.19006) (Jacobson-Galán et al. 2024).</span></div></div>
</div>
