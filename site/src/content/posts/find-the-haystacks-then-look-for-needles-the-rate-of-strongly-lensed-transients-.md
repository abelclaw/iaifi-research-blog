---
abstract: The time delay between appearances of multiple images of a gravitationally
  lensed supernova (glSN) is sensitive to the Hubble constant, $H_0$. As well as time
  delays, a lensed host galaxy is needed to enable precise inference of $H_0$. In
  this work we investigate the connection between discoverable lensed transients and
  their host galaxies. We find that LSST will discover 88 glSNe per year, of which
  $54\%$ will also have a strongly lensed host. The rates can change by approximately
  30 percent uncertainty depending primarily on the choice of unlensed SN population
  and uncertainties in the redshift evolution of the deflector population, but the
  fraction of glSNe with a lensed host is consistently around a half. LSST will discover
  20 glSNe per year in systems that could plausibly have been identified by Euclid
  as galaxy-galaxy lenses before the discovery of the glSN. Such systems have preferentially
  longer time delays and therefore are well suited for cosmography. We define a golden
  sample of glSNe Ia with time delays over 10 days, image separations greater than
  0.8 arcseconds, and a multiply imaged host. For this golden sample, we find $91\%$
  occur in systems that should already be discoverable as galaxy-galaxy lenses in
  Euclid. For cosmology with glSNe, monitoring Euclid lenses is a plausible alternative
  to searching the entire LSST alert stream.
arxivId: '2407.04080'
arxivUrl: https://arxiv.org/abs/2407.04080
authors:
- Ana Sainz de Murieta
- Thomas E. Collett
- Mark R. Magee
- Justin D. R. Pierel
- Wolfgang J. R. Enzi
- Martine Lokken
- Alex Gagliano
- Dan Ryczanowski
concepts:
- gravitational lensing time delays
- strong gravitational lensing rates
- survey optimization
- cosmological simulation
- monte carlo methods
- supernova classification
- dark energy
- signal detection
- uncertainty quantification
- bayesian inference
- stochastic processes
figures:
- /iaifi-research-blog/figures/2407_04080/figure_1.png
- /iaifi-research-blog/figures/2407_04080/figure_1.png
- /iaifi-research-blog/figures/2407_04080/figure_2.png
- /iaifi-research-blog/figures/2407_04080/figure_2.png
- /iaifi-research-blog/figures/2407_04080/figure_3.png
- /iaifi-research-blog/figures/2407_04080/figure_3.png
pdfUrl: https://arxiv.org/pdf/2407.04080v1
published: '2024-07-04T17:41:49+00:00'
theme: Astrophysics
title: 'Find the haystacks, then look for needles: The rate of strongly lensed transients
  in galaxy-galaxy strong gravitational lenses'
wordCount: 1012
---

## The Big Picture

Imagine searching for a handful of needles scattered across every haystack in North America. That's roughly the challenge astronomers face when hunting for gravitationally lensed supernovae, exploding stars whose light has been bent and split into multiple images by a foreground galaxy's gravity. These events are extraordinarily rare and scientifically valuable. Finding even one could help resolve one of the deepest open problems in modern physics.

The problem is the **Hubble tension**: a stubborn disagreement between two independent measurements of how fast the universe is expanding. Local measurements using Cepheid stars and Type Ia supernovae give about 73 km/s/Mpc, meaning the universe expands 73 kilometers per second faster for every 3.26 million light-years of distance. Measurements from the **cosmic microwave background**, the faint afterglow of the Big Bang observed in light that traveled 13.8 billion years to reach us, land at 67 km/s/Mpc. That 9% gap shouldn't exist if our cosmological model is complete. Closing it requires an independent measurement that relies on neither method.

When a massive galaxy sits precisely between us and a distant exploding star, gravity bends the light into multiple images that arrive at slightly different times. That **time delay** encodes the Hubble constant directly. But finding these rare events in the flood of data from next-generation surveys, up to 10 million alerts per night from the Vera C. Rubin Observatory, is its own enormous challenge.

A new study by Ana Sainz de Murieta and collaborators offers a smarter strategy: find the haystacks first, then look for the needles inside them.

> **Key Insight:** Instead of scanning the entire night sky for lensed supernovae, monitoring a pre-identified catalog of galaxy-scale gravitational lenses could yield 91% of the most cosmologically valuable events, at a fraction of the search cost.

## How It Works

The team built a simulation pipeline to model the full population of discoverable **gravitationally lensed supernovae (glSNe)**. It incorporates realistic supernova rates, galaxy distributions, lens mass profiles, and the detection characteristics of both the **Vera C. Rubin Observatory's LSST** (Legacy Survey of Space and Time) and the **Euclid** space telescope.

![Figure 1](/iaifi-research-blog/figures/2407_04080/figure_1.png)

The core question: when LSST spots a lensed supernova, will that system already be catalogued as a known galaxy-galaxy lens? Answering this required modeling two populations independently, glSNe that LSST can detect and lens systems that Euclid can identify, then measuring their overlap.

The key steps:

1. **Simulate the glSN population**: Draw supernova host galaxies and lens galaxies from observed distributions, compute lensing cross-sections (a measure of how likely each galaxy is to bend background light), and apply LSST detection criteria for brightness, cadence, and image separation.
2. **Model the lensed host visibility**: Determine whether the host galaxy appears as a multiply-imaged arc, a distorted smear of light bent around the lens, which is critical for reconstructing lens geometry and measuring H₀ (the Hubble constant).
3. **Cross-match with Euclid lens catalogs**: Apply Euclid's detection criteria to identify which lens systems would already be catalogued before a supernova appears.

![Figure 2](/iaifi-research-blog/figures/2407_04080/figure_1.png)

The numbers are worth paying attention to. LSST should discover roughly 88 glSNe per year, with ~30% uncertainty driven mostly by assumptions about unlensed supernova rates. Of those, 54% will have a multiply-imaged host galaxy, the kind that helps astronomers reconstruct lens geometry and pin down H₀. That fraction stays stable across different modeling assumptions.

About 20 glSNe per year will occur in systems Euclid could plausibly have already catalogued as galaxy-galaxy lenses. These systems carry a built-in advantage: they tend to have longer time delays, making the delay measurements more precise.

![Figure 4](/iaifi-research-blog/figures/2407_04080/figure_2.png)

The team then defined a **golden sample**, events best suited for cosmology: Type Ia supernovae with time delays longer than 10 days, image separations larger than 0.8 arcseconds (roughly 1/4500 of a degree), and a multiply-imaged host. For this golden sample, 91% occur in systems already discoverable by Euclid as galaxy-galaxy lenses.

## Why It Matters

This result reframes how astronomers should approach the next decade of lensed-supernova science. Rather than building pipelines to sift millions of nightly transient alerts, a problem contaminated by ordinary supernovae, active galactic nuclei (supermassive black holes at galaxy centers that flare brightly), and variable stars, observatories could monitor a few thousand known lens systems instead. The signal-to-noise problem shrinks enormously.

The cosmological payoff is real. Each precisely measured time delay provides an independent H₀ measurement. With LSST operating for a decade, accumulating enough golden-sample events for percent-level precision on H₀ becomes plausible, potentially enough to determine whether the Hubble tension reflects systematic errors or genuinely new physics. Pre-identified lens catalogs make that accumulation tractable.

![Figure 5](/iaifi-research-blog/figures/2407_04080/figure_3.png)

Significant uncertainties remain. The ~30% rate uncertainty reflects genuine gaps in knowledge: how supernova rates evolve with **redshift** (a proxy for distance and look-back time, indicating how much the universe has expanded since the light was emitted), how lens galaxy populations change over cosmic time, and how well Euclid's actual performance matches simulations. As Euclid delivers its first lens catalogs and LSST comes online, these predictions will be tested in real time.

> **Bottom Line:** By monitoring Euclid's catalog of galaxy-galaxy lenses rather than searching the full LSST alert stream, astronomers can capture 91% of the best events for measuring the Hubble constant, turning an overwhelming needle-in-a-haystack problem into a focused, targeted campaign.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects gravitational astrophysics and large-scale survey science, developing simulation frameworks that link lens population statistics to observational discovery strategies.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The results have direct implications for how AI-driven transient classifiers for LSST should be designed. Targeted monitoring of known lens systems cuts the false-positive burden compared to blind all-sky searches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By quantifying the expected yield of cosmologically golden lensed supernovae, this work sets up independent H₀ measurements that could resolve the Hubble tension and point to physics beyond the standard cosmological model.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">With Euclid's lens catalogs now coming online and LSST first light approaching, these predictions will be tested within years; the paper is available at [arXiv:2407.04080](https://arxiv.org/abs/2407.04080).</span></div></div>
</div>
