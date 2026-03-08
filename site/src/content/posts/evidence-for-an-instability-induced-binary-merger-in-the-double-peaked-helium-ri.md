---
abstract: We present ultraviolet to infrared observations of the extraordinary Type
  IIn supernova 2023zkd (SN 2023zkd). Photometrically, it exhibits persistent and
  luminous precursor emission spanning $\sim$4 years preceding discovery ($M_r\approx-15$
  mag, 1,500~days in the observer frame), followed by a secondary stage of gradual
  brightening in its final year. Post-discovery, it exhibits two photometric peaks
  of comparable brightness ($M_r\lesssim-18.7$ mag and $M_r\approx-18.4$ mag, respectively)
  separated by 240 days. Spectroscopically, SN 2023zkd exhibits highly asymmetric
  and multi-component Balmer and He I profiles that we attribute to ejecta interaction
  with fast-moving ($1,\!000-2,\!000\;\mathrm{km}\;\mathrm{s}^{-1}$) He-rich polar
  material and slow-moving ($\sim$$400\;\mathrm{km}\;\mathrm{s}^{-1}$) equatorially-distributed
  H-rich material. He II features also appear during the second light curve peak and
  evolve rapidly. Shock-driven models fit to the multi-band photometry suggest that
  the event is powered by interaction with $\sim$$5-6\;M_{\odot}$ of CSM, with $2-3\;M_{\odot}$
  associated with each light curve peak, expelled during mass-loss episodes $\sim$$3-4$
  and $\sim$$1-2$ years prior to explosion. The observed precursor emission, combined
  with the extreme mass-loss rates required to power each light curve peak, favors
  either super-Eddington accretion onto a black hole or multiple long-lived eruptions
  from a massive star to luminosities that have not been previously observed. We consider
  multiple progenitor scenarios for SN 2023zkd, and find that the brightening optical
  precursor and inferred explosion properties are most consistent with a massive ($M_{\mathrm{ZAMS}}\geq30\;M_{\odot}$)
  and partially-stripped He star undergoing an instability-induced merger with a black
  hole companion.
arxivId: '2502.19469'
arxivUrl: https://arxiv.org/abs/2502.19469
authors:
- A. Gagliano
- V. A. Villar
- T. Matsumoto
- D. O. Jones
- C. L. Ransome
- A. E. Nugent
- D. Hiramatsu
- K. Auchettl
- D. Tsuna
- Y. Dong
- S. Gomez
- P. D. Aleo
- C. Angus
- T. de Boer
- K. A. Bostroem
- K. C. Chambers
- D. A. Coulter
- K. W. Davis
- J. R. Fairlamb
- J. Farah
- D. Farias
- R. J. Foley
- C. Gall
- H. Gao
- E. P. Gonzalez
- D. A. Howell
- M. E. Huber
- C. D. Kilpatrick
- C. -C. Lin
- M. E. MacLeod
- E. A. Magnier
- C. McCully
- P. Minguez
- G. Narayan
- M. Newsome
- K. C. Patra
- A. Rest
- S. Rest
- S. Smartt
- K. W. Smith
- G. Terreran
- R. J. Wainscoat
- Q. Wang
- S. K. Yadavalli
- Y. Zenati
concepts:
- circumstellar material interaction
- stellar evolution
- binary merger progenitor
- supernova classification
- precursor emission
- inverse problems
- signal detection
- regression
- bayesian inference
- anomaly detection
figures:
- /iaifi-research-blog/figures/2502_19469/figure_1.png
- /iaifi-research-blog/figures/2502_19469/figure_1.png
- /iaifi-research-blog/figures/2502_19469/figure_2.png
- /iaifi-research-blog/figures/2502_19469/figure_2.png
- /iaifi-research-blog/figures/2502_19469/figure_3.png
- /iaifi-research-blog/figures/2502_19469/figure_3.png
pdfUrl: https://arxiv.org/pdf/2502.19469v1
published: '2025-02-26T19:00:00+00:00'
theme: Astrophysics
title: Evidence for an Instability-Induced Binary Merger in the Double-Peaked, Helium-Rich
  Type IIn Supernova 2023zkd
wordCount: 1124
---

## The Big Picture

Imagine a star so massive it could swallow thirty suns, locked in a death spiral with a black hole. For years, the doomed star bleeds gas into space, a slow luminous hemorrhage visible across billions of light-years. Then, in its final moments, the merger triggers a catastrophic explosion. Not one explosion. Two.

That is the story astronomers now believe explains one of the most bizarre stellar deaths ever recorded: **SN 2023zkd**, a supernova that broke nearly every rule about how stars are supposed to die.

Type IIn supernovae (named for a distinctive narrow spike in their hydrogen signal) are already known for theatrical death scenes, with exploding stars crashing into shells of previously ejected gas. But SN 2023zkd took the drama to a new extreme: four years of pre-explosion fireworks, two separate brightness peaks eight months apart, and light signatures pointing to a wildly lopsided, chemically layered explosion environment.

The team, led by Alexander Gagliano at the NSF AI Institute for Artificial Intelligence and Fundamental Interactions (IAIFI) and the Center for Astrophysics | Harvard & Smithsonian, assembled an ultraviolet-to-infrared portrait of this event and concluded that no ordinary stellar death can explain it. Their best answer: a runaway orbital collapse between a massive helium star (one that had already shed its outer hydrogen layers) and its black hole companion.

> **Key Insight:** SN 2023zkd's double-peaked light curve, four-year optical precursor, and asymmetric helium-rich spectral features together point to a progenitor system unlike anything previously confirmed — a massive helium star spiraling into a black hole before exploding as a supernova.

## How It Works

The discovery story began before anyone knew there was anything to discover. Archival imaging from the **Zwicky Transient Facility (ZTF)** and the **Young Supernova Experiment (YSE)** revealed that the site of SN 2023zkd had been glowing for roughly 1,500 days before the explosion was catalogued. That is about four years of persistent, unexplained light.

This **precursor emission** (a long-lived glow at the explosion site before the blast) reached an absolute magnitude of about −15, making it extraordinarily luminous for pre-explosion activity and comparable to the faintest supernovae. In its final year, the source brightened further, accelerating toward collapse.

![Figure 1](/iaifi-research-blog/figures/2502_19469/figure_1.png)

After explosion, the light curve held another surprise. Rather than fading smoothly after a single peak, SN 2023zkd brightened to a first maximum around magnitude −18.7, faded, then climbed again to nearly −18.4. The two peaks sat 240 days apart. Shock-driven models fitted to the multi-band photometry indicate the explosion interacted with roughly **5–6 solar masses of circumstellar material (CSM)**, gas expelled by the progenitor before it died, with 2–3 solar masses powering each peak separately.

The spectroscopy told an equally strange story. Emission lines of hydrogen and helium showed **asymmetric, multi-component profiles**: light from different parts of the explosion arrived at very different speeds and intensities, rather than blending into a single smooth signal. Fast-moving helium-rich material raced outward at 1,000–2,000 km/s at the poles, while slower hydrogen-rich gas (around 400 km/s) spread along the equatorial plane.

This geometry, a **bipolar-plus-toroidal CSM structure** (two jets firing from the top and bottom of the star, surrounded by a thick equatorial ring), requires the star to have shed mass in at least two distinct episodes. The first occurred roughly 3–4 years before explosion, the second about 1–2 years before, each through geometrically different mechanisms.

![Figure 2](/iaifi-research-blog/figures/2502_19469/figure_1.png)

The team ruled out explanations one by one:

- **Standard stellar wind mass loss** cannot account for the extreme mass-loss rates required, which exceed known values by orders of magnitude
- **A single giant eruption** cannot explain two separated photometric peaks
- **Pair-instability pulsations** (violent eruptions driven by spontaneous matter-antimatter pair creation deep in the stellar core) are disfavored by the chemical composition and light curve shape
- **Super-Eddington accretion onto a black hole** (matter falling faster than the theoretical maximum rate) remains plausible but struggles to explain the precursor's multi-year duration and final-year brightening

What fits best is a massive helium star, born with at least 30 solar masses, in a close binary orbit with a black hole. As it evolved and swelled, it began transferring mass onto the black hole, triggering runaway accretion. An instability eventually caused the two objects to spiral together in a **common-envelope merger**, where the black hole plunges so deep into the companion that both share the same outer layers. The merger ejected material in two successive episodes along different geometries before triggering core collapse.

![Figure 3](/iaifi-research-blog/figures/2502_19469/figure_2.png)

## Why It Matters

Binary stellar evolution has long been invoked to explain supernova diversity, but direct observational evidence linking a specific explosion to a specific binary progenitor is rare. SN 2023zkd is one of the most compelling cases yet for **instability-driven binary mergers**, a channel theorists have predicted but observers have struggled to confirm.

Four years of pre-explosion data across multiple wide-field surveys gave the team an unusually detailed view of a star in its final act. As the **Vera C. Rubin Observatory** comes fully online and monitors the entire southern sky every few nights, events like SN 2023zkd won't be one-off curiosities. They'll be a statistical sample.

That raises a set of concrete questions: how common are merger-driven explosions? What fraction of Type IIn supernovae hide a black hole companion? What does the diversity of pre-explosion activity reveal about the final years of massive stellar evolution?

The tools to answer them (machine learning classifiers, automated alert brokers, simulation-based inference frameworks) are already in active development, many at IAIFI and affiliated institutions. SN 2023zkd is both a scientific result and a proof of concept for that pipeline.

![Figure 4](/iaifi-research-blog/figures/2502_19469/figure_2.png)

> **Bottom Line:** SN 2023zkd reveals a new pathway to stellar death — a massive helium star merging with a black hole companion, producing years of pre-explosion flaring and a unique double-peaked explosion — and sets the stage for a statistical census of such events with next-generation surveys.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines wide-field time-domain astronomy, spectroscopic modeling, and shock-interaction physics to decode an extraordinary transient, showing how multi-wavelength datasets can constrain exotic binary progenitor scenarios.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The detection and characterization of SN 2023zkd relied on automated survey pipelines and photometric classification tools increasingly powered by machine learning, highlighting AI's expanding role in identifying rare astrophysical events in real time.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By identifying an instability-induced black hole–helium star merger as the likely progenitor, this study provides a new observational handle on the end states of massive binary stellar evolution and the formation channels of compact object remnants.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future observations with Rubin Observatory and next-generation spectroscopic surveys will determine how common merger-driven supernovae are; the full study is available at [arXiv:2502.19469](https://arxiv.org/abs/2502.19469).</span></div></div>
</div>
