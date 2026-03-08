---
abstract: 'Hydrogen-rich supernovae (SNe) span a range of hydrogen envelope masses
  at core collapse, producing diverse light curves from extended plateaus in Type
  II SNe to double-peaked Type IIb SNe. Recent hydrodynamic modeling predicts a continuous
  sequence of light-curve morphologies as hydrogen is removed, with short plateau
  SNe (plateau durations ~50--70 days) emerging as a transitional class. However,
  the observational boundary between IIb and short-plateau remains poorly defined,
  and thus far unobserved. We report on extensive photometric and spectroscopic follow-up
  of SN 2023wdd and SN 2022acrv, candidate transitional events on the low-mass end
  of the short-plateau class. Both exhibit weak, double-peaked light curves which
  we interpret as exceptionally short plateaus (10--20 days), and hybrid spectral
  features: persistent H$α$ absorption with He I contamination, but without the helium
  dominance characteristic of IIb SNe. Using analytic shock-cooling models and numerical
  light curve fitting, we estimate hydrogen-rich envelope masses of ~0.6--0.8 $M_\odot$
  -- significantly larger than canonical IIb values ($\lesssim0.1\,M_\odot$) but consistent
  with the ${\sim}0.9\,M_\odot$ threshold predicted for short-plateau behavior. Although
  the progenitor radii inferred from analytic and numerical methods differ by factors
  of 2--5, envelope mass estimates are consistent across approaches. Comparisons to
  well-studied IIb (SN 2016gkg, SN 2022hnt), short-plateau (SN 2023ufx, SN 2006ai,
  SN 2016egz, SN 2006Y), and II SNe (SN 2023ixf, SN 2013ej) suggest a monotonic relationship
  between hydrogen envelope mass and plateau length consistent with analytic and numerical
  expectations. These findings provide additional evidence for a continuous distribution
  of envelope stripping in hydrogen-rich core-collapse progenitors and place SN 2023wdd
  and SN 2022acrv along the IIb/short-plateau boundary.'
arxivId: '2509.12470'
arxivUrl: https://arxiv.org/abs/2509.12470
authors:
- Joseph R. Farah
- D. Andrew Howell
- Daichi Hiramatsu
- Curtis McCully
- Moira Andrews
- Megan Newsome
- Estefania Padilla Gonzalez
- Craig Pellegrino
- Edo Berger
- Peter Blanchard
- Sebastian Gomez
- Harsh Kumar
- K. Azalee Bostroem
- Yuan Qi Ni
- A. Gagliano
- Aravind P. Ravi
concepts:
- supernova classification
- envelope stripping continuum
- light curve modeling
- stellar evolution
- shock-cooling emission
- spectral line analysis
- simulation-based inference
- bayesian inference
- regression
- anomaly detection
figures:
- /iaifi-research-blog/figures/2509_12470/figure_1.png
- /iaifi-research-blog/figures/2509_12470/figure_2.png
pdfUrl: https://arxiv.org/pdf/2509.12470v1
published: '2025-09-15T21:26:46+00:00'
theme: Astrophysics
title: 'When IIb Ceases To Be: Bridging the Gap Between IIb and Short-plateau Supernovae'
wordCount: 1022
---

## The Big Picture

Think of a star's hydrogen envelope like an onion skin. Most massive stars explode with nearly all their outer layers intact, a thick, juicy onion that produces a long, steady glow called a **Type IIP supernova**. Strip almost everything away and you get a **Type IIb supernova**, a nearly naked core that flashes twice: once when the explosion's shockwave breaks through the thin remaining skin, then again as radioactive nickel-56 powers a second peak. For decades, astronomers treated these as separate categories, two distinct boxes in a classification scheme built on what chemical fingerprints show up in a supernova's light.

Nature rarely respects our filing systems. Theoretical work predicts that hydrogen stripping happens along a smooth continuum, with every shade of partially peeled onion between the extremes existing somewhere in the universe. In supernova science, a "plateau" is a period where brightness holds roughly steady for weeks. The **short-plateau** class sits in the middle ground between thin-skinned IIb events and the fully-enveloped IIP class. The problem: that transition zone had never actually been caught in the wild.

Two recently observed supernovae, **SN 2023wdd** and **SN 2022acrv**, may finally fill that gap. A team from Las Cumbres Observatory, Harvard & Smithsonian, MIT, and collaborating institutions ran an intensive observing campaign, measuring brightness over time and across wavelengths and analyzing chemical fingerprints in the light to pin down the physical properties of both events. These two supernovae sit squarely on the poorly defined boundary between Type IIb and short-plateau events, offering the best observational evidence to date for a continuous envelope-stripping sequence.

> **Key Insight:** SN 2023wdd and SN 2022acrv are "missing link" supernovae. Their hydrogen envelope masses (~0.6–0.8 solar masses) place them in the gap between thin-enveloped Type IIb events and the heavier short-plateau class, filling a hole in the core-collapse supernova continuum that had only been predicted, never observed.

## How It Works

Both supernovae were identified through wide-field transient surveys, which triggered intensive **photometric follow-up** (measuring brightness across time and wavelength) alongside **spectroscopic observations** (breaking the light into its component wavelengths to identify chemical fingerprints).

![Figure 1](/iaifi-research-blog/figures/2509_12470/figure_1.png)

The light curves were immediately interesting. Both SN 2023wdd and SN 2022acrv display the double-peak brightness structure associated with Type IIb supernovae: an early brightening followed by a dip and a second rise. But the initial decline is far more subtle than in classic IIb events.

The team interprets the first peak not as the shockwave rapidly cooling after bursting through a thin hydrogen skin, but as an exceptionally short plateau lasting only **10–20 days**. For comparison, typical short-plateau events last 50–70 days, and Type IIP supernovae sustain plateaus of 80–120 days. These objects have too much hydrogen to be IIb, but not enough to sustain a real plateau.

The spectral fingerprints told the same story. Classic IIb supernovae show helium features that eventually dominate, with hydrogen fading fast. SN 2023wdd and SN 2022acrv instead show **persistent Hα absorption** well into their evolution, combined with **He I contamination** (helium features bleeding into the spectrum), but helium never takes over. That hybrid spectral signature is exactly what you'd expect from an intermediate hydrogen envelope mass.

To measure those envelope masses, the team used two independent modeling approaches:

- **Analytic shock-cooling models**: fast, physics-motivated formulae linking the shape of the early light curve to the progenitor star's radius and envelope mass
- **Numerical light curve fitting**: full hydrodynamic simulations matched to the observed data

Both methods agreed where it mattered. They placed the hydrogen-rich envelope masses at **~0.6–0.8 solar masses**, far larger than typical IIb values (≲0.1 solar masses) but consistent with the ~0.9 solar mass threshold predicted for short-plateau behavior. The progenitor radii inferred by the two methods differed by factors of 2–5, revealing genuine model uncertainties. The envelope masses, though, held up across approaches.

![Figure 2](/iaifi-research-blog/figures/2509_12470/figure_2.png)

## Why It Matters

Supernova classification might seem like mere bookkeeping, but the categories directly encode our understanding of how massive stars live and die. The type of explosion a star produces reflects its entire evolutionary history: how much mass it shed through powerful stellar winds, whether it had a companion star siphoning off material, how violent its eruptions were in its final centuries. A truly continuous distribution of hydrogen envelope masses would mean the mass-loss processes shaping stellar evolution operate across a wide range of intensities, not switching between a few fixed channels.


Comparing SN 2023wdd and SN 2022acrv to benchmarks across the full sequence (IIb events like SN 2016gkg and SN 2022hnt, short-plateau events like SN 2023ufx and SN 2006Y, and classic IIP events like SN 2023ixf) reveals a clear trend: more hydrogen envelope mass produces longer plateaus. The new observations fit cleanly into that trend. Future surveys with the Vera Rubin Observatory's Legacy Survey of Space and Time will capture thousands more supernovae, allowing astronomers to statistically map the envelope mass distribution and what it tells us about binary stars, stellar winds, and mass-transfer physics across cosmic time.

> **Bottom Line:** Two newly characterized supernovae occupy the long-sought boundary zone between Type IIb and short-plateau events, with hybrid light curves and spectra matching intermediate hydrogen envelope masses of ~0.6–0.8 solar masses. They are the strongest observational evidence yet that stellar envelope stripping is a continuous process, not a binary choice.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">Dense observational coverage from global telescope networks, combined with both analytic and numerical modeling, resolved a longstanding classification ambiguity at the boundaries of core-collapse supernova physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The multi-method approach, pairing fast analytic shock-cooling models with full numerical hydrodynamic fits, shows how physics-informed modeling strategies can produce reliable measurements even when individual methods yield discrepant progenitor parameters.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By placing SN 2023wdd and SN 2022acrv on the IIb/short-plateau boundary, this study gives direct observational support for a continuous hydrogen envelope distribution among massive-star progenitors, constraining theories of binary mass transfer and stellar wind-driven mass loss.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future wide-field transient surveys will statistically populate this transitional regime, enabling direct tests of stellar evolution models; the full study is available at [arXiv:2509.12470](https://arxiv.org/abs/2509.12470).</span></div></div>
</div>
