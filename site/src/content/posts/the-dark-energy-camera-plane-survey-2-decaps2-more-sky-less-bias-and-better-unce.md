---
abstract: Deep optical and near-infrared imaging of the entire Galactic plane is essential
  for understanding our Galaxy's stars, gas, and dust. The second data release of
  the DECam Plane Survey (DECaPS2) extends the five-band optical and near-infrared
  survey of the southern Galactic plane to cover $6.5\%$ of the sky, |b| < 10° and
  6° > l > -124°, complementary to coverage by Pan-STARRS1. Typical single-exposure
  effective depths, including crowding effects and other complications, are 23.5,
  22.6, 22.1, 21.6, and 20.8 mag in $g$, $r$, $i$, $z$, and $Y$ bands, respectively,
  with around 1 arcsecond seeing. The survey comprises 3.32 billion objects built
  from 34 billion detections in 21.4 thousand exposures, totaling 260 hours open shutter
  time on the Dark Energy Camera (DECam) at Cerro Tololo. The data reduction pipeline
  features several improvements, including the addition of synthetic source injection
  tests to validate photometric solutions across the entire survey footprint. A convenient
  functional form for the detection bias in the faint limit was derived and leveraged
  to characterize the photometric pipeline performance. A new post-processing technique
  was applied to every detection to de-bias and improve uncertainty estimates of the
  flux in the presence of structured backgrounds, specifically targeting nebulosity.
  The images and source catalogs are publicly available at http://decaps.skymaps.info/.
arxivId: '2206.11909'
arxivUrl: https://arxiv.org/abs/2206.11909
authors:
- A. K. Saydjari
- E. F. Schlafly
- D. Lang
- A. M. Meisner
- G. M. Green
- C. Zucker
- I. Zelko
- J. S. Speagle
- T. Daylan
- A. Lee
- F. Valdes
- D. Schlegel
- D. P. Finkbeiner
concepts:
- photometric crowded-field deblending
- uncertainty quantification
- structured background estimation
- calibration
- model validation
- detection bias modeling
- scientific workflows
- inverse problems
- stellar evolution
- anomaly detection
- superresolution
figures:
- /iaifi-research-blog/figures/2206_11909/figure_1.png
- /iaifi-research-blog/figures/2206_11909/figure_2.png
- /iaifi-research-blog/figures/2206_11909/figure_3.png
pdfUrl: https://arxiv.org/pdf/2206.11909v2
published: '2022-06-23T18:00:01+00:00'
theme: Astrophysics
title: 'The Dark Energy Camera Plane Survey 2 (DECaPS2): More Sky, Less Bias, and
  Better Uncertainties'
wordCount: 1023
---

## The Big Picture

Imagine trying to census every person in a city, but you can only photograph it through a sandstorm, at night, with everyone standing shoulder-to-shoulder. That's roughly the challenge astronomers face when mapping the Milky Way's disk. The Galactic plane, the flat band of stars, gas, and dust that forms the body of our galaxy, is where most of the action is and the hardest place to see clearly. Dust absorbs and reddens starlight. Stars crowd so tightly their images blur and overlap. Glowing gas clouds smear irregular halos across every exposure.

The first DECam Plane Survey (DECaPS1) took a major step toward cracking this problem but left a quarter of the southern Galactic plane unmapped, missing the faint stars and dim features that only long, careful exposures reveal. DECaPS2 fills that gap and then some. The team didn't just add more sky; they rebuilt their data-processing pipeline from scratch, producing a catalog of **3.32 billion objects** covering 6.5% of the entire sky, with tighter error bounds and far fewer systematic distortions than its predecessor.

> **Key Insight:** DECaPS2 is not just a bigger catalog. It's a smarter one. By directly measuring and correcting two major error sources (a tendency to overestimate faint-object brightness and contamination from irregular gas clouds) the survey delivers measurements you can actually trust in the most chaotic regions of the Galaxy.

## How It Works

The survey used the **Dark Energy Camera (DECam)** on the 4-meter Víctor M. Blanco Telescope at Cerro Tololo Inter-American Observatory in Chile, a 570-megapixel wide-field imager originally built to map dark energy, now pointed at the densest star fields in the sky. Over 260 hours of observing time across 21,400 individual exposures, the team captured imaging in five bands spanning optical to near-infrared: *g*, *r*, *i*, *z*, and *Y*.

Processing those exposures required a pipeline built for extremes, centered on three ideas:

- **`crowdsource`**: A photometry code that simultaneously fits all detectable stars within each image rather than processing them in isolation. In crowded fields, fitting stars one at a time leads to terrible errors. Fitting them jointly properly apportions light between overlapping neighbors.
- **`CloudCovErr.jl`**: A post-processing module applied to every detection in the survey. Standard pipelines model image backgrounds as smooth, gradually varying surfaces, which works fine in sparse regions but falls apart when the "background" has sharp filaments and gradients at the same spatial scale as the stars being measured. For each source, `CloudCovErr.jl` estimates the local background covariance and uses that structure to correct measured brightness and recalculate realistic uncertainties.
- **Detection bias correction**: Faint objects near the detection threshold are systematically measured too bright, because you only catch them when random noise pushes them above the cutoff. The team derived a clean mathematical description of this bias and validated it with **synthetic source injection tests**: fake stars of known brightness were planted across the entire survey footprint, the pipeline was run on them, and recovery was measured directly.

![Figure 1](figure:1)

![Figure 2](figure:2)

**Photometric calibration** converts raw pixel counts into standardized brightness measurements comparable across instruments. Using reference data from Pan-STARRS1 and Gaia, combined with injection test results, the team characterized depth, completeness, and positional accuracy across wildly varying conditions, from sparse outer-disk fields to the blazing stellar density of the inner Galaxy.

## Why It Matters

The Milky Way is our home galaxy, but also the one we understand least. We're embedded in it, looking through layers of dust that block our view toward the center. Surveys like DECaPS2 are the backbone of nearly every branch of Galactic astronomy: mapping the three-dimensional dust distribution, measuring stellar populations across ages and compositions, hunting for variable stars and transients, and building training sets for machine learning classifiers that must sort billions of sources automatically.

![Figure 3](figure:3)

The survey's overlap with Pan-STARRS1 matters, too. PS1 covers the northern and equatorial sky well, but the southern Galactic plane, where the inner disk and bulge are most visible from Earth's southern hemisphere, was its blind spot. DECaPS2 fills that hole with comparable depth and better-understood systematics.

Together, these two surveys form the most complete deep optical and near-infrared census of the Galactic plane assembled to date. The 3.32 billion objects in this catalog, built from 34 billion individual detections across five bands, will serve as a reference resource for years. This is especially true as next-generation surveys like the Rubin Observatory's LSST begin operations and need reliable anchor points in exactly these challenging regions.

The improvements in uncertainty estimation have real consequences for science. **Color-magnitude diagrams** are plots of stellar brightness versus color that reveal populations, ages, and distances. Near nebulosity, measurement errors scatter stars to wrong positions in the diagram, making them unreliable. The team showed directly that `CloudCovErr.jl` sharpens these diagrams, cleaning up scatter from structured backgrounds and making globular clusters and stellar populations in previously garbled regions accessible to analysis.

> **Bottom Line:** DECaPS2 maps 3.32 billion objects across the most complex part of the sky, with systematic biases explicitly measured and corrected, giving astronomers a trustworthy foundation for understanding the structure, stellar populations, and dust of our own Galaxy.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** DECaPS2 shows how algorithmic advances from statistics and signal processing (covariance-aware background modeling, injection-test validation, bias-corrected detection statistics) can open up new astrophysical science in large-scale astronomical surveys.

- **Impact on Artificial Intelligence:** The survey's synthetic source injection framework gives astronomers a way to rigorously test photometric pipelines against ground truth, offering a template for benchmarking machine learning classifiers and regression models at population scale.

- **Impact on Fundamental Interactions:** A 3.32-billion-object catalog of the Galactic plane with well-characterized uncertainties enables precision measurements of the three-dimensional dust distribution and stellar populations needed to understand Galactic structure and evolution.

- **Outlook and References:** Future work will extend photometric and astrometric comparisons with Rubin/LSST and Roman Space Telescope observations. The full catalog and images are publicly available, and the paper is posted as [arXiv:2206.11909](https://arxiv.org/abs/2206.11909).

## Original Paper Details
- **Title:** The Dark Energy Camera Plane Survey 2 (DECaPS2): More Sky, Less Bias, and Better Uncertainties
- **arXiv ID:** [2206.11909](https://arxiv.org/abs/2206.11909)
- **Authors:** A. K. Saydjari, E. F. Schlafly, D. Lang, A. M. Meisner, G. M. Green, C. Zucker, I. Zelko, J. S. Speagle, T. Daylan, A. Lee, F. Valdes, D. Schlegel, D. P. Finkbeiner
- **Abstract:** Deep optical and near-infrared imaging of the entire Galactic plane is essential for understanding our Galaxy's stars, gas, and dust. The second data release of the DECam Plane Survey (DECaPS2) extends the five-band optical and near-infrared survey of the southern Galactic plane to cover 6.5% of the sky, |b| < 10° and 6° > l > -124°, complementary to coverage by Pan-STARRS1. Typical single-exposure effective depths, including crowding effects and other complications, are 23.5, 22.6, 22.1, 21.6, and 20.8 mag in g, r, i, z, and Y bands, respectively, with around 1 arcsecond seeing. The survey comprises 3.32 billion objects built from 34 billion detections in 21.4 thousand exposures, totaling 260 hours open shutter time on the Dark Energy Camera (DECam) at Cerro Tololo. The data reduction pipeline features several improvements, including the addition of synthetic source injection tests to validate photometric solutions across the entire survey footprint. A convenient functional form for the detection bias in the faint limit was derived and used to characterize the photometric pipeline performance. A new post-processing technique was applied to every detection to de-bias and improve uncertainty estimates of the flux in the presence of structured backgrounds, specifically targeting nebulosity. The images and source catalogs are publicly available at http://decaps.skymaps.info/.
