---
abstract: Cosmological surveys must correct their observations for the reddening of
  extragalactic objects by Galactic dust. Existing dust maps, however, have been found
  to have spatial correlations with the large-scale structure of the Universe. Errors
  in extinction maps can propagate systematic biases into samples of dereddened extragalactic
  objects and into cosmological measurements such as correlation functions between
  foreground lenses and background objects and the primordial non-gaussianity parameter
  $f_{NL}$. Emission-based maps are contaminated by the cosmic infrared background,
  while maps inferred from stellar-reddenings suffer from imperfect removal of quasars
  and galaxies from stellar catalogs. Thus, stellar-reddening based maps using catalogs
  without extragalactic objects offer a promising path to making dust maps with minimal
  correlations with large-scale structure. We present two high-latitude integrated
  extinction maps based on stellar reddenings, with a point spread function of full-width
  half-maximum 6.1' and 15'. We employ a strict selection of catalog objects to filter
  out galaxies and quasars and measure the spatial correlation of our extinction maps
  with extragalactic structure. Our galactic extinction maps have reduced spatial
  correlation with large scale structure relative to most existing stellar-reddening
  based and emission-based extinction maps.
arxivId: '2212.04514'
arxivUrl: https://arxiv.org/abs/2212.04514
authors:
- Nayantara Mudur
- Core Francisco Park
- Douglas P Finkbeiner
concepts:
- dust extinction mapping
- large-scale structure contamination
- bayesian inference
- stellar catalog cleaning
- posterior estimation
- galaxy classification
- inverse problems
- regression
- calibration
- kernel methods
- anomaly detection
figures:
- /iaifi-research-blog/figures/2212_04514/figure_1.png
- /iaifi-research-blog/figures/2212_04514/figure_2.png
- /iaifi-research-blog/figures/2212_04514/figure_3.png
pdfUrl: https://arxiv.org/pdf/2212.04514v1
published: '2022-12-08T19:00:03+00:00'
theme: Astrophysics
title: Stellar Reddening Based Extinction Maps for Cosmological Applications
wordCount: 1346
---

## The Big Picture

Imagine trying to photograph a distant city through a foggy window. You can wipe down your side of the glass, but you can't control the fog itself. If the fog isn't evenly distributed, your photos will be systematically skewed in ways that are hard to correct later. Cosmologists face exactly this problem. The Milky Way is full of interstellar dust, and every observation of a distant galaxy or supernova must pass through this dusty "fog" before reaching our telescopes.

To do science, astronomers must subtract the dust's effect. But that correction is only as good as the maps they use.

The best dust maps we have are subtly contaminated. They're not just measuring dust; they're also picking up faint signals from distant galaxies, the very objects cosmologists are trying to study. Use a contaminated dust map to "clean" your galaxy survey, and you'll inadvertently imprint a fingerprint of that contamination onto your results.

For next-generation surveys like DESI and the Rubin Observatory's LSST, which aim to measure the universe's properties at the sub-percent level, even tiny biases like this can ruin the science.

Nayantara Mudur, Core Francisco Park, and Douglas Finkbeiner at Harvard have built two new dust extinction maps designed to break this vicious cycle. Their maps are less entangled with the distant galaxies they're supposed to be blind to, and the difference is measurable.

> **Key Insight:** The most widely used dust maps inadvertently contain signals from distant galaxies, creating a circular contamination problem. By rigorously filtering stellar catalogs to remove extragalactic sources, Mudur et al. produce cleaner maps that introduce fewer systematic biases into cosmological analyses.

## How It Works

The researchers focused on stellar-reddening based maps, which work by measuring how much redder stars appear compared to their known type. Think of it like checking whether a white streetlight looks orange, then using that color shift to infer how much atmosphere you're looking through. For each star, the reddening reveals how much dust lies between us and that star.

The problem: real stellar catalogs aren't perfectly clean. Galaxies and quasars sometimes sneak in, masquerading as stars. When a map-maker mistakes a galaxy for a star, the reddening inferred at its position is wrong. And since galaxies cluster together, this contaminates the dust map with exactly the galaxy-clustering signal you want to avoid.

The team's core strategy was strict, multi-pronged filtering:

- **Gaia astrometry cuts**: Gaia is the European Space Agency's star-mapping satellite. Objects with parallax (the tiny apparent position shift as Earth orbits the Sun, essentially zero for distant galaxies) or proper motion (a star's slow drift across the sky) inconsistent with being a distant star were removed.
- **Morphology cuts**: Extended sources, which tend to be galaxies, were rejected using Pan-STARRS shape measurements.
- **Color-based QSO rejection**: Quasars have distinctive optical and near-infrared colors; suspicious combinations triggered exclusion.
- **External catalog cross-matching**: Known quasar catalogs provided additional veto lists.

With the cleaned stellar sample in hand, photometry from Pan-STARRS1 (a wide-field optical sky survey spanning five wavelength bands from 490–964 nm) and 2MASS (the Two Micron All Sky Survey, covering three near-infrared bands), plus Gaia parallaxes, were fed into the **Bayestar** stellar inference framework. Bayestar models each star's distance and reddening simultaneously, producing a per-star estimate of the probable range of reddening and distance values. Integrating these along each line of sight produces a 2D extinction map.

![Figure 1](/iaifi-research-blog/figures/2212_04514/figure_1.png)

The result: two maps with angular resolutions of 6.1 arcminutes and 15 arcminutes full-width half-maximum. (For scale, the full Moon spans about 30 arcminutes, so 6.1 arcminutes is quite fine.) The maps cover the high galactic latitudes where cosmological surveys operate. The finer map matches the SFD (Schlegel-Finkbeiner-Davis 1998) map in resolution, but with substantially less contamination from the background universe.

![Figure 2](/iaifi-research-blog/figures/2212_04514/figure_2.png)

To measure success, the team computed angular cross-correlations between their extinction maps and tracers of cosmic structure, specifically quasar samples that probe the universe's web of galaxies. The question is simple: do the bright spots on the dust map tend to line up with the bright spots on the galaxy map? A well-behaved dust map should show zero such alignment. The new maps outperform most existing stellar-reddening and emission-based maps on this metric, showing significantly reduced spurious correlations across a range of angular scales.

![Figure 3](/iaifi-research-blog/figures/2212_04514/figure_3.png)

## Why It Matters

Two cosmological measurements are especially sensitive to dust map contamination.

The first is magnification bias and lensing cross-correlations. These measurements use the way foreground galaxies bend and amplify light from background objects to map how matter is distributed throughout the universe. Any spurious correlation between the dust map and galaxy positions distorts these signals directly.

The second application is measuring **fNL**, the primordial non-Gaussianity parameter, a number encoding information about cosmic inflation and the earliest moments of the universe's existence. Detecting a nonzero fNL is one of the grand goals of modern cosmology and requires picking out an incredibly subtle pattern in how galaxies cluster across the largest scales. Dust contamination that correlates with galaxy positions is precisely the kind of systematic that can mimic or mask this signal.

As Gaia's astrometric catalog matures and photometric surveys push deeper, stellar catalogs will only improve. More precise parallaxes mean cleaner star-galaxy separation, which means even less contaminated maps.

The two-map design (6.1' and 15') is itself deliberate. The coarser map sacrifices resolution for better noise properties in sparse regions, giving analysts a choice of tool depending on the science. The authors also note that combining their maps with neutral hydrogen (HI) maps, which trace dust through a completely different physical channel, could offer a valuable independent cross-check.

> **Bottom Line:** By carefully cleaning stellar catalogs of galaxies and quasars before building dust maps, this work delivers extinction maps with measurably lower spurious correlations with cosmic structure. For upcoming surveys trying to squeeze precision cosmology from billions of galaxy observations, that kind of improvement matters.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits at the intersection of astrophysical data science and precision cosmology, applying statistical inference and multi-survey catalog engineering to a systematic bias problem that threatens next-generation cosmological measurements.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The Bayestar framework is a case study in scaling probabilistic machine learning to real scientific infrastructure. It models per-star posteriors over reddening and distance for millions of stars and feeds them into map-making pipelines where accuracy has direct scientific consequences.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Cleaner dust maps directly improve prospects for detecting primordial non-Gaussianity fNL, a signal encoding information about inflationary physics and the fundamental interactions governing the universe's earliest moments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future improvements from Gaia's full mission data and deeper photometric surveys will further sharpen star-galaxy separation at the heart of this approach; the paper is available at [arXiv:2212.04514](https://arxiv.org/abs/2212.04514).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Stellar Reddening Based Extinction Maps for Cosmological Applications</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2212.04514</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Nayantara Mudur", "Core Francisco Park", "Douglas P Finkbeiner"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Cosmological surveys must correct their observations for the reddening of extragalactic objects by Galactic dust. Existing dust maps, however, have been found to have spatial correlations with the large-scale structure of the Universe. Errors in extinction maps can propagate systematic biases into samples of dereddened extragalactic objects and into cosmological measurements such as correlation functions between foreground lenses and background objects and the primordial non-gaussianity parameter $f_{NL}$. Emission-based maps are contaminated by the cosmic infrared background, while maps inferred from stellar-reddenings suffer from imperfect removal of quasars and galaxies from stellar catalogs. Thus, stellar-reddening based maps using catalogs without extragalactic objects offer a promising path to making dust maps with minimal correlations with large-scale structure. We present two high-latitude integrated extinction maps based on stellar reddenings, with a point spread function of full-width half-maximum 6.1' and 15'. We employ a strict selection of catalog objects to filter out galaxies and quasars and measure the spatial correlation of our extinction maps with extragalactic structure. Our galactic extinction maps have reduced spatial correlation with large scale structure relative to most existing stellar-reddening based and emission-based extinction maps.</span></div></div>
</div>
