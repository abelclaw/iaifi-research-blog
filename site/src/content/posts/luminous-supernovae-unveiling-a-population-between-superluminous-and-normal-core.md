---
abstract: 'Stripped-envelope core-collapse supernovae can be divided into two broad
  classes: the common Type Ib/c supernovae (SNe Ib/c), powered by the radioactive
  decay of $^{56}$Ni, and the rare superluminous supernovae (SLSNe), most likely powered
  by the spin-down of a magnetar central engine. Up to now, the intermediate regime
  between these two populations has remained mostly unexplored. Here, we present a
  comprehensive study of 40 \textit{luminous supernovae} (LSNe), SNe with peak magnitudes
  of $M_r = -19$ to $-20$ mag, bound by SLSNe on the bright end and by SNe Ib/c on
  the dim end. Spectroscopically, LSNe appear to form a continuum between Type Ic
  SNe and SLSNe. Given their intermediate nature, we model the light curves of all
  LSNe using a combined magnetar plus radioactive decay model and find that they are
  indeed intermediate, not only in terms of their peak luminosity and spectra, but
  also in their rise times, power sources, and physical parameters. We sub-classify
  LSNe into distinct groups that are either as fast-evolving as SNe Ib/c or as slow-evolving
  as SLSNe, and appear to be either radioactively or magnetar powered, respectively.
  Our findings indicate that LSNe are powered by either an over-abundant production
  of $^{56}$Ni or by weak magnetar engines, and may serve as the missing link between
  the two populations.'
arxivId: '2204.08486'
arxivUrl: https://arxiv.org/abs/2204.08486
authors:
- Sebastian Gomez
- Edo Berger
- Matt Nicholl
- Peter K. Blanchard
- Griffin Hosseinzadeh
concepts:
- supernova classification
- light curve modeling
- magnetar central engine
- radioactive decay power
- bayesian inference
- stellar evolution
- monte carlo methods
- clustering
- regression
- anomaly detection
figures:
- /iaifi-research-blog/figures/2204_08486/figure_1.png
- /iaifi-research-blog/figures/2204_08486/figure_3.png
pdfUrl: https://arxiv.org/pdf/2204.08486v1
published: '2022-04-18T18:00:02+00:00'
theme: Astrophysics
title: 'Luminous Supernovae: Unveiling a Population Between Superluminous and Normal
  Core-collapse Supernovae'
wordCount: 1235
---

## The Big Picture

Imagine you're sorting a music collection and discover a genre that doesn't fit anywhere: too loud for classical, too structured for jazz, but not quite rock either. For decades, astrophysicists faced a similar puzzle with exploding stars.

Some massive stars shed their outer gas layers before they die, stripped bare by stellar winds or a companion star. When they finally explode, the resulting supernovae come in dramatically different flavors. The most common type, called **Type Ib/c supernovae**, are relatively dim and fade within weeks. At the far extreme, a rare breed called **superluminous supernovae (SLSNe)** can blaze up to 100 times brighter and linger for months.

Between them? A gap, and a nagging question about what lived there.

A team led by Sebastian Gomez at the Space Telescope Science Institute and Harvard's Center for Astrophysics has now filled that gap. By systematically mining supernova catalogs, they assembled 40 **luminous supernovae (LSNe)**, a distinct population sitting between the common and the extraordinary. These aren't slightly unusual Type Ib/c supernovae or slightly faint SLSNe. They appear to be a genuine intermediate class, with their own physics and their own power sources.

> **Key Insight:** Luminous supernovae connect ordinary stripped-envelope supernovae to their far more brilliant cousins. Powered either by unusually abundant radioactive nickel or by weak magnetar engines, they reveal that stellar death doesn't come in just two sizes.

## How It Works

The researchers started with 315 stripped-envelope supernovae drawn from public databases including the Open Supernova Catalog, the Transient Name Server, and WISeREP. They identified LSNe using a brightness criterion based on **absolute magnitude**, a standardized scale where more negative numbers mean intrinsically brighter objects. The cut required peak values of **M_r = −19 to −20 mag** in the red band, placing LSNe squarely between ordinary Type Ib/c supernovae (around −17.7 mag) and SLSNe (around −21.7 mag).

![Figure 1](/iaifi-research-blog/figures/2204_08486/figure_1.png)

Of the 40 objects in the sample, 25 earned a **"Gold"** designation for having well-sampled light curves and confirmed stripped-envelope spectra. The remaining 15 were labeled **"Silver"** for adequate but incomplete data. This quality tiering matters because modeling stellar explosions demands good measurements.

To figure out what powers these explosions, the team fit a **combined magnetar plus radioactive decay model** to every light curve. The two energy sources work like this:

- **Radioactive decay**: Standard Type Ib/c supernovae shine because nickel-56 (⁵⁶Ni) synthesized in the explosion decays to cobalt and then iron, releasing gamma rays that heat the expanding gas.
- **Magnetar spin-down**: SLSNe are thought to be lit from within by a **magnetar**, a rapidly spinning neutron star left behind by the explosion. It converts rotational energy into radiation as it gradually slows down.
- **Combined model**: LSNe draw from both wells simultaneously. Fitting both components to each light curve yields physical parameters: ejecta mass, nickel mass, magnetar spin period, and magnetic field strength.

**Spectroscopy** told a consistent story. LSNe show no sharp divide from either neighboring class. Their spectra form a continuous bridge from ordinary Type Ic features to the W-shaped oxygen absorption lines that mark young SLSNe. As LSNe cool, they look more and more like normal Type Ic supernovae, exactly as aging SLSNe do.

![Figure 2](/iaifi-research-blog/figures/2204_08486/figure_3.png)

LSNe also split into two sub-groups. The first evolves quickly, rising and falling on timescales comparable to ordinary Type Ib/c supernovae. These events appear driven primarily by **over-abundant ⁵⁶Ni**: more radioactive nickel than a typical Type Ic produces, but not enough to require an exotic energy source. Think ordinary supernovae with the volume turned up.

The second group stretches over weeks to months, like SLSNe. These appear powered by **weak magnetar engines**: neutron stars spinning down and depositing energy, but with less punch than the magnetars behind true SLSNe. Their physical parameters sit between the two established classes in ejecta mass, magnetic field strength, and spin period.


Event rates reinforce this picture. SLSNe represent less than 1% of the Type Ib/c volumetric rate. LSNe occupy an intermediate niche, which suggests magnetar engines don't suddenly switch on at some luminosity threshold. Instead, they span a continuum of power.

## Why It Matters

The old picture of two distinct classes separated by a yawning gap is giving way to something more interesting: a spectrum of explosions, with different energy sources contributing at different points along the way.

Filling this gap does more than tidy up a catalog. It constrains the underlying physics. How often do neutron stars form as millisecond magnetars? How much nickel can a collapsing star produce before something else takes over? What determines whether a dying star produces a weak magnetar or an overabundance of nickel: the progenitor's mass, its rotation rate, or its metallicity?

The LSNe in this sample give theorists new anchor points for models connecting progenitor properties to explosion outcomes. Future wide-field surveys like the Rubin Observatory's LSST will discover hundreds of these events, turning today's 40-object sample into something statistically powerful.

> **Bottom Line:** Luminous supernovae are real, they connect two previously isolated populations, and they show that stellar explosions span a continuum of power sources, from radioactive decay to magnetar spin-down, rather than jumping between them.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">Systematic catalog mining, quality-tiered sample selection, and multi-component physical modeling revealed a hidden population in existing astrophysical datasets, putting data-intensive methods at the heart of the discovery.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The combined magnetar-plus-radioactive-decay fitting framework applied to 40 light curves shows how physically motivated parametric models can extract astrophysical parameters at scale, informing machine learning approaches to transient classification.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Identifying luminous supernovae as a genuine intermediate population constrains neutron star formation physics and the conditions under which millisecond magnetars form, probing the fundamental interactions that govern compact object birth.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future surveys will dramatically expand LSNe samples, enabling statistical tests of rates and progenitor properties; the full analysis is available at [arXiv:2204.08486](https://arxiv.org/abs/2204.08486).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Luminous Supernovae: Unveiling a Population Between Superluminous and Normal Core-collapse Supernovae</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2204.08486</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Sebastian Gomez", "Edo Berger", "Matt Nicholl", "Peter K. Blanchard", "Griffin Hosseinzadeh"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Stripped-envelope core-collapse supernovae can be divided into two broad classes: the common Type Ib/c supernovae (SNe Ib/c), powered by the radioactive decay of $^{56}$Ni, and the rare superluminous supernovae (SLSNe), most likely powered by the spin-down of a magnetar central engine. Up to now, the intermediate regime between these two populations has remained mostly unexplored. Here, we present a comprehensive study of 40 \textit{luminous supernovae} (LSNe), SNe with peak magnitudes of $M_r = -19$ to $-20$ mag, bound by SLSNe on the bright end and by SNe Ib/c on the dim end. Spectroscopically, LSNe appear to form a continuum between Type Ic SNe and SLSNe. Given their intermediate nature, we model the light curves of all LSNe using a combined magnetar plus radioactive decay model and find that they are indeed intermediate, not only in terms of their peak luminosity and spectra, but also in their rise times, power sources, and physical parameters. We sub-classify LSNe into distinct groups that are either as fast-evolving as SNe Ib/c or as slow-evolving as SLSNe, and appear to be either radioactively or magnetar powered, respectively. Our findings indicate that LSNe are powered by either an over-abundant production of $^{56}$Ni or by weak magnetar engines, and may serve as the missing link between the two populations.</span></div></div>
</div>
