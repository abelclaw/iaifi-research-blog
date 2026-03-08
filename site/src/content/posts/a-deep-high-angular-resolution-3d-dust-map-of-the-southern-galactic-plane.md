---
abstract: We present a deep, high-angular resolution 3D dust map of the southern Galactic
  plane over $239^\circ < \ell < 6^\circ$ and $|b| < 10^\circ$ built on photometry
  from the DECaPS2 survey, in combination with photometry from VVV, 2MASS, and unWISE
  and parallaxes from Gaia DR3 where available. To construct the map, we first infer
  the distance, extinction, and stellar types of over 700 million stars using the
  brutus stellar inference framework with a set of theoretical MIST stellar models.
  Our resultant 3D dust map has an angular resolution of $1'$, roughly an order of
  magnitude finer than existing 3D dust maps and comparable to the angular resolution
  of the Herschel 2D dust emission maps. We detect complexes at the range of distances
  associated with the Sagittarius-Carina and Scutum-Centaurus arms in the fourth quadrant,
  as well as more distant structures out to a maximum reliable distance of $d \approx$
  10 kpc from the Sun. The map is sensitive up to a maximum extinction of roughly
  $A_V \approx 12$ mag. We publicly release both the stellar catalog and the 3D dust
  map, the latter of which can easily be queried via the Python package dustmaps.
  When combined with the existing Bayestar19 3D dust map of the northern sky, the
  DECaPS 3D dust map fills in the missing piece of the Galactic plane, enabling extinction
  corrections over the entire disk $|b| < 10^\circ$. Our map serves as a pathfinder
  for the future of 3D dust mapping in the era of LSST and Roman, targeting regimes
  accessible with deep optical and near-infrared photometry but often inaccessible
  with Gaia.
arxivId: '2503.02657'
arxivUrl: https://arxiv.org/abs/2503.02657
authors:
- Catherine Zucker
- Andrew K. Saydjari
- Joshua S. Speagle
- Edward F. Schlafly
- Gregory M. Green
- Robert Benjamin
- Joshua Peek
- Gordian Edenhofer
- Alyssa Goodman
- Michael A. Kuhn
- Douglas P. Finkbeiner
concepts:
- 3d dust mapping
- bayesian inference
- interstellar extinction
- posterior estimation
- stellar evolution
- inverse problems
- density estimation
- uncertainty quantification
- superresolution
- scalability
- monte carlo methods
- cosmic microwave background
figures:
- /iaifi-research-blog/figures/2503_02657/figure_1.png
- /iaifi-research-blog/figures/2503_02657/figure_1.png
- /iaifi-research-blog/figures/2503_02657/figure_2.png
- /iaifi-research-blog/figures/2503_02657/figure_2.png
- /iaifi-research-blog/figures/2503_02657/figure_3.png
- /iaifi-research-blog/figures/2503_02657/figure_3.png
pdfUrl: https://arxiv.org/pdf/2503.02657v2
published: '2025-03-04T14:17:09+00:00'
theme: Astrophysics
title: A Deep, High-Angular Resolution 3D Dust Map of the Southern Galactic Plane
wordCount: 1185
---

## The Big Picture

Imagine trying to read a book through smoke. Now imagine the smoke is layered in wisps and clumps at different distances, some thick, some thin, shifting across three dimensions. That's what astronomers face looking through the plane of our galaxy. Between us and distant stars lies an invisible obstacle course of interstellar dust — tiny particles of carbon and silicate that scatter and absorb light, rendering whole swaths of the Milky Way's interior frustratingly opaque.

For decades, astronomers worked with two-dimensional dust maps: flat photographs of the smoke, with no depth information. If you want to understand a star cluster embedded in a dust cloud 4,000 light-years away, knowing there's *some* dust between you and it isn't enough. You need to know exactly where it sits along the line of sight.

A new paper by Catherine Zucker, Andrew Saydjari, Joshua Speagle, and collaborators delivers exactly that: the deepest, sharpest three-dimensional dust map of the southern Galactic plane ever constructed — assembled from light measurements of over 700 million individual stars.

> **Key Insight:** By mapping how dust reddens the light of hundreds of millions of stars at known distances, this team has produced a 3D dust atlas of the southern Milky Way at 1 arcminute angular resolution — ten times finer than any previous 3D dust map — reaching structures as far as 10 kiloparsecs (about 32,000 light-years) from Earth.

## How It Works

The core idea is elegant: dust reddens starlight. Just as sunsets turn orange because blue light scatters away through the atmosphere, starlight reddened by interstellar dust shifts toward longer wavelengths. Measure how much a star's colors deviate from what they should be, and you can infer how much dust lies between you and that star. Do this for millions of stars at a range of distances, and you can reconstruct a 3D dust density map by asking: at what distance does the reddening jump?

![Figure 1](/iaifi-research-blog/figures/2503_02657/figure_1.png)

The team built their map on **photometry** — brightness measurements across multiple wavelengths — drawn from four major surveys:

- **DECaPS2** (Dark Energy Camera Plane Survey, second data release): a deep optical survey of the southern Galactic plane reaching stars far too faint for earlier all-sky catalogs
- **VVV** (VISTA Variables in the Vía Láctea): a ground-based deep-infrared sky survey
- **2MASS** (Two Micron All Sky Survey): a foundational full-sky infrared catalog
- **unWISE**: reprocessed data from NASA's WISE space telescope
- **Gaia DR3** distance measurements, where available, from the European Space Agency's satellite that tracks tiny positional shifts as Earth orbits the Sun

The multi-wavelength approach is critical. Different wavelengths probe dust differently, and combining optical with infrared data allows the team to pierce through heavier obscuration and constrain stellar types more precisely.

![Figure 2](/iaifi-research-blog/figures/2503_02657/figure_1.png)

The inference pipeline uses **brutus**, a Bayesian statistical framework fed with **MIST stellar models** (MESA Isochrones and Stellar Tracks — a library of computer simulations showing how stars of different masses, ages, and compositions should appear across the electromagnetic spectrum). For each of the 700+ million stars, brutus simultaneously estimates three entangled quantities:

- **Distance** — how far is this star?
- **Extinction** (AV) — how much dust dimming has its light suffered?
- **Stellar type** — what kind of star is this intrinsically?

A star can look faint because it's dim, far away, or heavily extincted. Brutus untangles these degeneracies by analyzing brightness across many wavelengths simultaneously, finding the combination that best explains all the observations at once.

![Figure 3](/iaifi-research-blog/figures/2503_02657/figure_2.png)

With stellar distances and extinctions in hand, the team tallies dust encountered along each line of sight and reconstructs a three-dimensional density map. The result covers galactic longitudes 239° to 6° — the entire southern Galactic plane — at 1 arcminute resolution. For comparison, the widely used **Bayestar19** map (which covers the northern sky) achieves 7–14 arcminute resolution. This new map is roughly ten times sharper.

![Figure 4](/iaifi-research-blog/figures/2503_02657/figure_2.png)

The map reaches reliably to ~10 kiloparsecs from the Sun and detects extinction up to AV ≈ 12 magnitudes, tracing dust through some of the galaxy's most obscured regions. Critically, the team identifies dust concentrations at distances consistent with two major spiral arms: the **Sagittarius-Carina arm** and the **Scutum-Centaurus arm** — physically coherent structures visible as dense clumps in the 3D density map.

## Why It Matters

The practical impact is immediate. Every astronomical observation through the Galactic plane must correct for dust extinction; failing to do so distorts distance estimates, luminosities, and color measurements. Surveys hunting for supernovae, variable stars, exoplanets, stellar clusters, and gravitational wave counterparts all depend on accurate extinction corrections.

![Figure 5](/iaifi-research-blog/figures/2503_02657/figure_3.png)

Before this work, the southern Galactic plane was a blind spot. Bayestar19 covered the north, but the south lacked a comparable 3D resource. By releasing both the stellar catalog and the dust map through the Python **dustmaps** package, the team enables the entire astronomical community to query extinction anywhere in the southern disk with unprecedented precision.

The deeper significance is structural. Mapping dust in 3D is equivalent to mapping the galaxy's interstellar medium in 3D — the gas, the molecular clouds, the sites of ongoing star formation all trace the same density enhancements that accumulate dust. This map provides a new observational anchor for models of Galactic spiral structure and the molecular cloud lifecycle.

It also serves as a direct pathfinder for the next generation of wide-field surveys. The **Vera Rubin Observatory** (LSST) and **Nancy Grace Roman Space Telescope** will push even deeper, imaging billions of stars in regimes where Gaia's parallaxes run out. The multi-band inference framework, spatial reconstruction pipeline, and public query tools developed here lay the groundwork for maps that will be orders of magnitude more complete.

![Figure 6](/iaifi-research-blog/figures/2503_02657/figure_3.png)

> **Bottom Line:** Zucker, Saydjari, Speagle, and collaborators have delivered the definitive 3D dust map of the southern Milky Way — 700 million stars, 1 arcminute resolution, 10 kiloparsec depth — completing the full-sky 3D picture of Galactic dust and opening a new window on the structure of our galaxy's interstellar medium.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses large-scale machine learning inference with fundamental astrophysics, using a Bayesian stellar parameter framework to convert raw photometry from hundreds of millions of stars into a physically interpretable 3D map of the Milky Way's dust distribution.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The brutus pipeline demonstrates how probabilistic deep learning — simultaneously fitting distance, extinction, and stellar type across 700+ million objects — can be deployed at industrial scale on heterogeneous multi-wavelength datasets, pushing the frontier of AI-driven catalog science.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The resulting 3D dust map resolves spiral arm dust concentrations at 1 arcminute angular resolution, providing a new observational baseline for models of Galactic structure, star formation, and the interstellar medium — and completing the full-sky extinction correction resource needed by the astronomical community.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future surveys including LSST and Roman will extend this approach to billions of stars at greater depths; the methods and public data releases here serve as direct infrastructure for the next generation of 3D Galactic cartography. The paper is available on arXiv at 2509.19431.</span></div></div>
</div>
