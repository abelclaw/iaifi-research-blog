---
abstract: 'We present extensive ultraviolet (UV), optical, and near-infrared (NIR)
  photometric and spectroscopic observations of the nearby hydrogen-poor superluminous
  supernova (SLSN-I) SN2024rmj at z = 0.1189. SN 2024rmj reached a peak absolute magnitude
  of Mg $\approx$ -21.9, placing it at the luminous end of the SLSN-I distribution.
  The light curve exhibits a pronounced pre-peak bump ($\approx$ 60 d before the main
  peak) and a post-peak bump ($\approx$ 55 d after the main peak). The bulk of the
  light curve is otherwise well fit by a magnetar spin-down model, with typical values
  (spin: $\approx$ 2.1 ms; magnetic field: $\approx$ 6 $\times$ 10$^{13}$ G; ejecta
  mass: $\approx$ 12 M$_\odot$). The optical spectra exhibit characteristic SLSN-I
  features and evolution, but with a relatively high velocity of $\approx$ 8,000 km
  s$^{-1}$ post-peak. Most significantly, we find a clear detection of helium in the
  NIR spectra at He I $λ$1.083 $μ$m and $λ$2.058 $μ$m, blueshifted by $\approx$ 15,000
  km s$^{-1}$ (13 d before peak) and $\approx$ 13,000 km s$^{-1}$ (40 d after peak),
  indicating that helium is confined to the outermost ejecta; based on these NIR detections,
  we also identify likely contribution from He I $λ$5876 Å in the optical spectra
  on a similar range of timescales. This represents the most definitive detection
  of helium in a bright SLSN-I to date, and indicates that progenitors with a thin
  helium layer can still explode as SLSNe.'
arxivId: '2506.06417'
arxivUrl: https://arxiv.org/abs/2506.06417
authors:
- Harsh Kumar
- Edo Berger
- Peter K. Blanchard
- Sebastian Gomez
- Daichi Hiramatsu
- Alex Gagliano
- Moira Andrews
- K. Azalee Bostroem
- Joseph Farah
- D. Andrew Howell
- Curtis McCully
concepts:
- signal detection
- supernova classification
- spectral methods
- magnetar spin-down
- stellar evolution
- ejecta velocity mapping
- regression
- light curve bumps
- uncertainty quantification
figures:
- /iaifi-research-blog/figures/2506_06417/figure_1.png
- /iaifi-research-blog/figures/2506_06417/figure_2.png
pdfUrl: https://arxiv.org/pdf/2506.06417v1
published: '2025-06-06T18:00:00+00:00'
theme: Astrophysics
title: A Detection of Helium in the Bright Superluminous Supernova SN 2024rmj
wordCount: 1364
---

## The Big Picture

Imagine a star so massive that when it dies, it briefly outshines its entire galaxy, not just for a moment, but for weeks or months. These are **superluminous supernovae**, the most energetic stellar explosions astronomers have ever catalogued. They radiate as much energy as the Sun will emit over its entire lifetime, yet despite decades of study, the stars that produce them remain poorly understood. A central mystery: what exactly are these stars made of when they explode?

One element has been particularly elusive: helium. Superluminous supernovae lack hydrogen; that much is clear from the light they emit. But helium, the universe's second most abundant element, has stubbornly refused to show up in most of these events. The explosions move so fast that helium's light signatures get smeared together with features from other elements, making identification nearly impossible.

Do these stars shed all their helium before exploding, or does some remain?

A new study of SN 2024rmj, one of the brightest superluminous supernovae ever observed in the nearby universe, gives the clearest answer yet. A team led by researchers at the Center for Astrophysics | Harvard & Smithsonian has made a definitive helium detection in a bright superluminous supernova, using infrared light that cuts through the spectral confusion.

> **Key Insight:** SN 2024rmj shows unambiguous helium signatures in its near-infrared spectra, proving that even the brightest superluminous supernovae can come from stars that retained a thin outer helium layer before exploding.

## How It Works

Detecting helium in a fast-moving explosion isn't straightforward. Helium's signature in visible light, near 5,876 Å (angstroms, a unit far smaller than a millimeter), is hopelessly blended with sodium, calcium, and carbon features. The solution is **near-infrared (NIR)** light, just beyond the red end of what human eyes can see, where helium has two cleaner spectral lines at 1.083 μm and 2.058 μm.

The 1.083 μm line can still pick up contamination from carbon and magnesium, but the 2.058 μm line is uniquely clean. No other common element produces a strong feature there. Even modest amounts of helium (as little as ~0.1 solar masses) generate a detectable signal. The catch: only supernovae close enough to us, at **redshifts** (a measure of cosmic distance; larger z means farther away) below roughly z = 0.15, allow ground-based telescopes to reach this wavelength. SN 2024rmj, at z = 0.1189, sits just inside that window.

![Figure 1](/iaifi-research-blog/figures/2506_06417/figure_1.png)

The research team ran an extensive campaign spanning UV, optical, and near-infrared wavelengths from August 2024 through February 2025, using Las Cumbres Observatory, the Fred Lawrence Whipple Observatory, and archival data from ZTF, ATLAS, and the Swift space telescope. The key detections came from NIR spectroscopy:

- **13 days before peak brightness**: He I at 1.083 μm and 2.058 μm, blueshifted by ~15,000 km/s
- **40 days after peak**: The same helium lines, now blueshifted by ~13,000 km/s
- The blueshift encodes velocity, with helium racing outward at roughly 5% of the speed of light

That velocity drop between the two epochs is telling. The helium sits in the **outermost ejecta** (the debris cloud blasted outward by the explosion, with material shed earliest moving the fastest). As the explosion evolves and deeper layers are exposed, the apparent helium velocity decreases. The inner ejecta lack helium entirely. This onion-skin structure pins down where helium lived inside the star before detonation.

![Figure 2](/iaifi-research-blog/figures/2506_06417/figure_2.png)

The **light curve**, how the explosion's brightness changed over time, adds another piece. SN 2024rmj reached a peak brightness of M_g ≈ −21.9 (on the logarithmic magnitude scale astronomers use, where more negative means brighter), placing it among the most luminous superluminous supernovae known. It also shows two unusual bumps, one roughly 60 days before peak, another about 55 days after, riding atop a smooth main peak.

The bulk of the light curve fits a **magnetar spin-down model**: the explosion leaves behind a **magnetar**, a rapidly rotating, ultra-magnetized neutron star that continuously pumps energy into the surrounding debris as it slows down. Best-fit parameters are physically plausible: a spin period of ~2.1 milliseconds, a magnetic field of ~6×10¹³ Gauss, and roughly 12 solar masses of ejected material.


## Why It Matters

The helium detection in a bright, magnetar-powered superluminous supernova upends a prevailing assumption. The most luminous of these explosions were thought to come from stars that had shed essentially all of their outer envelopes, first hydrogen, then helium, before detonating. SN 2024rmj shows that a thin helium shell can survive the violent winds and mass-loss episodes that precede the explosion, leaving a detectable fingerprint in the ejecta.

It also clarifies the classification boundaries between different classes of **stripped-envelope supernovae**, explosions from stars that lost their outer layers to varying degrees before death. Earlier helium detections in superluminous events came only from lower-luminosity objects near the boundary with ordinary core-collapse supernovae, leaving open the question of whether those events truly belonged to the superluminous class. SN 2024rmj's extreme brightness rules out that ambiguity. The progenitor was almost certainly magnetar-powered, and it still had helium.

Future NIR spectroscopic surveys of nearby superluminous supernovae will map how common this is, and whether helium abundance correlates with luminosity, host galaxy metallicity, or other properties.

> **Bottom Line:** By catching helium's infrared fingerprint in one of the brightest superluminous supernovae ever observed, astronomers have shown that even the most extreme stellar explosions can come from stars that didn't completely strip their outer layers, rewriting our picture of what these exotic progenitors look like.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines multi-wavelength observational astrophysics with detailed spectral modeling to resolve a long-standing question about superluminous supernova progenitors. Neither data collection nor physical modeling alone could have answered it; the two together reveal stellar physics that each approach misses on its own.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Discriminating faint helium signals from blended spectral features across a complex, fast-evolving explosion is exactly the kind of pattern-recognition challenge where machine-learning spectral classifiers are increasingly applied to transient surveys.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The helium detection in SN 2024rmj constrains the mass-loss history and envelope structure of massive star progenitors, informing theories of stellar evolution, core collapse, and the formation of magnetars as central engines of superluminous supernovae.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future facilities with wide-field NIR spectroscopic capabilities will systematically hunt for helium in large samples of nearby superluminous supernovae, testing whether SN 2024rmj is a rare outlier or a common subclass; the study is available at [arXiv:2506.06417](https://arxiv.org/abs/2506.06417) (Kumar et al. 2025).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">A Detection of Helium in the Bright Superluminous Supernova SN 2024rmj</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2506.06417</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Harsh Kumar", "Edo Berger", "Peter K. Blanchard", "Sebastian Gomez", "Daichi Hiramatsu", "Alex Gagliano", "Moira Andrews", "K. Azalee Bostroem", "Joseph Farah", "D. Andrew Howell", "Curtis McCully"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We present extensive ultraviolet (UV), optical, and near-infrared (NIR) photometric and spectroscopic observations of the nearby hydrogen-poor superluminous supernova (SLSN-I) SN2024rmj at z = 0.1189. SN 2024rmj reached a peak absolute magnitude of Mg $\approx$ -21.9, placing it at the luminous end of the SLSN-I distribution. The light curve exhibits a pronounced pre-peak bump ($\approx$ 60 d before the main peak) and a post-peak bump ($\approx$ 55 d after the main peak). The bulk of the light curve is otherwise well fit by a magnetar spin-down model, with typical values (spin: $\approx$ 2.1 ms; magnetic field: $\approx$ 6 $\times$ 10$^{13}$ G; ejecta mass: $\approx$ 12 M$_\odot$). The optical spectra exhibit characteristic SLSN-I features and evolution, but with a relatively high velocity of $\approx$ 8,000 km s$^{-1}$ post-peak. Most significantly, we find a clear detection of helium in the NIR spectra at He I $λ$1.083 $μ$m and $λ$2.058 $μ$m, blueshifted by $\approx$ 15,000 km s$^{-1}$ (13 d before peak) and $\approx$ 13,000 km s$^{-1}$ (40 d after peak), indicating that helium is confined to the outermost ejecta; based on these NIR detections, we also identify likely contribution from He I $λ$5876 Å in the optical spectra on a similar range of timescales. This represents the most definitive detection of helium in a bright SLSN-I to date, and indicates that progenitors with a thin helium layer can still explode as SLSNe.</span></div></div>
</div>
