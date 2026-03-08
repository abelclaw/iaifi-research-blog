---
abstract: We present optical photometry and spectroscopy of SN\,2019stc (=ZTF19acbonaa),
  an unusual Type Ic supernova (SN Ic) at a redshift of $z=0.117$. SN\,2019stc exhibits
  a broad double-peaked light curve, with the first peak having an absolute magnitude
  of $M_r=-20.0$ mag, and the second peak, about 80 rest-frame days later, $M_r=-19.2$
  mag. The total radiated energy is large, $E_{\rm rad}\approx 2.5\times 10^{50}$
  erg. Despite its large luminosity, approaching those of Type I superluminous supernovae
  (SLSNe), SN\,2019stc exhibits a typical SN Ic spectrum, bridging the gap between
  SLSNe and SNe Ic. The spectra indicate the presence of Fe-peak elements, but modeling
  of the first light curve peak with radioactive heating alone leads to an unusually
  high nickel mass fraction of $f_{\rm Ni}\approx 31\%$ ($M_{\rm Ni}\approx 3.2$ M$_\odot$).
  Instead, if we model the first peak with a combined magnetar spin-down and radioactive
  heating model we find a better match with $M_{\rm ej}\approx 4$ M$_\odot$, a magnetar
  spin period of $P_{\rm spin}\approx 7.2$ ms and magnetic field of $B\approx 10^{14}$
  G, and $f_{\rm Ni}\lesssim 0.2$ (consistent with SNe Ic). The prominent second peak
  cannot be naturally accommodated with radioactive heating or magnetar spin-down,
  but instead can be explained as circumstellar interaction with $\approx 0.7$ $M_\odot$
  of hydrogen-free material located $\approx 400$ AU from the progenitor. Including
  the remnant mass leads to a CO core mass prior to explosion of $\approx 6.5$ M$_\odot$.
  The host galaxy has a metallicity of $\approx 0.26$ Z$_\odot$, low for SNe Ic but
  consistent with SLSNe. Overall, we find that SN\,2019stc is a transition object
  between normal SNe Ic and SLSNe.
arxivId: '2103.02611'
arxivUrl: https://arxiv.org/abs/2103.02611
authors:
- Sebastian Gomez
- Edo Berger
- Griffin Hosseinzadeh
- Peter K. Blanchard
- Matt Nicholl
- V. Ashley Villar
concepts:
- supernova classification
- magnetar spin-down
- multi-peak light curves
- circumstellar interaction
- stellar evolution
- inverse problems
- bayesian inference
- anomaly detection
figures:
- /iaifi-research-blog/figures/2103_02611/figure_1.png
- /iaifi-research-blog/figures/2103_02611/figure_2.png
- /iaifi-research-blog/figures/2103_02611/figure_3.png
pdfUrl: https://arxiv.org/pdf/2103.02611v2
published: '2021-03-03T19:00:01+00:00'
theme: Astrophysics
title: 'The Luminous and Double-Peaked Type Ic Supernova 2019stc: Evidence for Multiple
  Energy Sources'
wordCount: 1116
---

## The Big Picture

Imagine watching a fireworks show where one explosive launches two distinct bursts of light, separated by nearly three months, each blazing as bright as billions of stars. That's roughly what astronomers witnessed when SN 2019stc ignited in late 2019 — a stellar death so strange it defied every standard explanation.

When massive stars exhaust their nuclear fuel, they collapse catastrophically, triggering supernova explosions. **Type Ic supernovae** — explosions from stars that shed their outer layers of hydrogen and helium before dying — are well-understood: they shine predictably, powered by radioactive nickel slowly decaying inside the expanding debris cloud.

SN 2019stc broke every rule. It blazed nearly 100 times brighter than a typical Type Ic event, yet its *spectrum* — the characteristic pattern of colors in its light, which reveals what chemical elements are present — looked completely ordinary. More baffling still, it produced two distinct brightness peaks separated by 80 days, something radioactive decay simply cannot explain.

A team of Harvard & Smithsonian astronomers, led by Sebastian Gomez and Edo Berger, tracked this extraordinary supernova across more than a year of observations and assembled a remarkable solution: SN 2019stc required not one, not two, but three distinct energy sources working in sequence.

> **Key Insight:** SN 2019stc is a cosmic Rosetta Stone — a single supernova that simultaneously displays the features of two entirely different explosion classes, revealing that the boundary between ordinary stripped-core supernovae and their ultra-luminous cousins may be far more permeable than astronomers assumed.

## How It Works

The team gathered brightness measurements in four color bands — optical filters labeled *g*, *r*, *i*, and *z* — using three telescopes: the 1.2-m FLWO and the 6.5-m Magellan and MMT observatories. These were supplemented by data from the **Zwicky Transient Facility (ZTF)**, the robotic sky survey that first spotted the transient on September 30, 2019.

![Figure 1](/iaifi-research-blog/figures/2103_02611/figure_1.png)

The light curve told an immediately puzzling story. The first peak hit an absolute magnitude of *M_r* = −20.0 — already approaching **Type I superluminous supernovae (SLSNe)**, the rarest and brightest class of stellar explosions known — with a total radiated energy of approximately 2.5 × 10^50 erg. Then, instead of fading gracefully as nickel decays into cobalt and iron, SN 2019stc *brightened again* 80 days later, peaking at *M_r* = −19.2.

The researchers tried the standard explanation first: pure **radioactive nickel heating**, the process by which nickel forged in the explosion releases energy as it decays, powering the supernova's glow over weeks. The math was brutal. Explaining the first peak with nickel alone would require 3.2 solar masses of nickel — 31% of the total ejected mass. Normal Type Ic events have nickel fractions of 5–30% at far lower absolute amounts. This scenario is physically implausible.

The better solution involved a **magnetar engine** — a newly-formed neutron star spinning hundreds of times per second, its rapid rotation bleeding energy into surrounding gas like a cosmic electromagnetic dynamo. Fitting the first peak with a combined magnetar-plus-nickel model produced far more reasonable results:

- Ejecta mass: ~4 solar masses
- Magnetar spin period: ~7.2 milliseconds
- Magnetic field strength: ~10^14 Gauss
- Nickel fraction: ≤20% — consistent with normal SNe Ic

This explained why the spectrum looked ordinary: the nickel content was actually normal. The magnetar was simply adding extra luminosity on top.

![Figure 2](/iaifi-research-blog/figures/2103_02611/figure_2.png)

The second peak still needed explaining. Neither radioactive decay nor magnetar spin-down naturally produces a delayed brightening of this magnitude. The team turned to a third mechanism: **circumstellar interaction (CSI)** — where debris blasted outward by the explosion slams into gas the dying star shed into surrounding space before it exploded. That collision converts kinetic energy into light, lighting a second lamp weeks or months after the main event.

The geometry fits strikingly. About 0.7 solar masses of hydrogen-free material sat roughly 400 AU from the progenitor — about 10 times the Earth-Sun distance. The ejecta, traveling at thousands of kilometers per second, took roughly 80 days to reach it. The collision produced a second peak nearly as bright as the first.

![Figure 3](/iaifi-research-blog/figures/2103_02611/figure_3.png)

Summing all mass components, the team inferred a carbon-oxygen core mass of approximately 6.5 solar masses just before explosion. The host galaxy's **metallicity** — the abundance of elements heavier than hydrogen and helium, a proxy for chemical enrichment — sits at ~0.26 solar metallicities: low for typical SNe Ic environments, but perfectly in line with where SLSNe prefer to occur.

## Why It Matters

SN 2019stc sits precisely in the luminosity gap between normal stripped supernovae and their superluminous cousins — a zone astronomers have barely mapped. Only a handful of events with peak magnitudes between −19 and −20 are known. Each one found there helps answer a fundamental question: are SLSNe a completely distinct population, or is there a continuous spectrum connecting them to ordinary core collapses?

SN 2019stc argues for the latter. The same progenitor — a stripped, moderately massive star in a low-metallicity galaxy — can apparently produce a normal SN Ic, a superluminous event, or something in between, depending on whether a magnetar forms and whether the star shed circumstellar material before dying. That reframes how astronomers should search for and classify transients with next-generation facilities like the Rubin Observatory's Legacy Survey of Space and Time, which will find thousands of supernovae per night. The intermediate zone where SN 2019stc lives may be far more populated than anyone expected.

> **Bottom Line:** SN 2019stc required a magnetar, radioactive nickel, *and* circumstellar interaction to explain its extraordinary double-peaked light curve — making it the clearest evidence yet that these explosion classes exist on a continuum, with profound implications for how we understand stripped stellar deaths across the universe.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines multi-facility observational astronomy with advanced physical modeling to decode a complex, multi-mechanism transient — demonstrating how systematic data analysis and first-principles theory together unlock phenomena inaccessible to either approach alone.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The FLEET program that flagged SN 2019stc for follow-up uses machine learning to identify luminous extragalactic transients in real time from ZTF data streams, showing how AI-assisted discovery pipelines accelerate the identification of rare astrophysical events.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">SN 2019stc reveals that magnetar formation, radioactive nucleosynthesis, and pre-explosion mass loss can operate simultaneously in a single stellar death, constraining the physical conditions governing the final stages of massive star evolution and the birth of neutron stars.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future time-domain surveys will likely uncover a population of similar transitional events; this paper provides the analytical framework for interpreting them. The full analysis is presented by Gomez et al. (2021) in *The Astrophysical Journal*.</span></div></div>
</div>
