---
abstract: Photometric pipelines struggle to estimate both the flux and flux uncertainty
  for stars in the presence of structured backgrounds such as filaments or clouds.
  However, it is exactly stars in these complex regions that are critical to understanding
  star formation and the structure of the interstellar medium. We develop a method,
  similar to Gaussian process regression, which we term local pixelwise infilling
  (LPI). Using a local covariance estimate, we predict the background behind each
  star and the uncertainty on that prediction in order to improve estimates of flux
  and flux uncertainty. We show the validity of our model on synthetic data and real
  dust fields. We further demonstrate that the method is stable even in the crowded
  field limit. While we focus on optical-IR photometry, this method is not restricted
  to those wavelengths. We apply this technique to the 34 billion detections in the
  second data release of the Dark Energy Camera Plane Survey (DECaPS2). In addition
  to removing many $>3σ$ outliers and improving uncertainty estimates by a factor
  of $\sim 2-3$ on nebulous fields, we also show that our method is well-behaved on
  uncrowded fields. The entirely post-processing nature of our implementation of LPI
  photometry allows it to easily improve the flux and flux uncertainty estimates of
  past as well as future surveys.
arxivId: '2201.07246'
arxivUrl: https://arxiv.org/abs/2201.07246
authors:
- Andrew K. Saydjari
- Douglas P. Finkbeiner
concepts:
- photometric infilling
- regression
- uncertainty quantification
- structured background subtraction
- kernel methods
- local covariance estimation
- calibration
- bayesian inference
- stochastic processes
- model validation
- inverse problems
- signal detection
figures:
- /iaifi-research-blog/figures/2201_07246/figure_1.png
- /iaifi-research-blog/figures/2201_07246/figure_2.png
- /iaifi-research-blog/figures/2201_07246/figure_3.png
pdfUrl: https://arxiv.org/pdf/2201.07246v1
published: '2022-01-18T19:00:01+00:00'
theme: Astrophysics
title: 'Photometry on Structured Backgrounds: Local Pixelwise Infilling by Regression'
wordCount: 1282
---

## The Big Picture

Imagine trying to measure the brightness of a single candle on a table covered with a crumpled, glowing tablecloth. The candle is easy enough to spot, but how much light reaching you comes from the candle versus the shifting glow beneath it? This is roughly the challenge astronomers face measuring stars nestled in cosmic clouds of gas and dust near the Galactic plane.

Traditional astronomical software pipelines (the automated tools that process raw telescope images into usable catalogs) are built for cleaner situations: stars against relatively smooth, dark skies. When a star sits atop a filament of glowing interstellar gas or a wisp of dust cloud, those tools systematically misattribute background glow to the star itself. Worse, they fail to quantify how uncertain the measurement is. These stars aren't a fringe concern. They're precisely the ones most relevant to understanding star formation and the interstellar medium, the diffuse gas and dust that fills the space between stars.

Andrew Saydjari and Douglas Finkbeiner at Harvard developed a new technique called **Local Pixelwise Infilling (LPI)** that reconstructs what the background would look like *if the star weren't there*, then uses that reconstruction to produce cleaner brightness measurements and more honest error bars.

> **Key Insight:** By statistically predicting the background hidden beneath each star using its local neighborhood of pixels, LPI produces both corrected brightness measurements and reliable uncertainty estimates, something previous background-subtraction approaches fundamentally couldn't do.

## How It Works

The core idea behind LPI comes from a branch of statistics called **Gaussian Process Regression (GPR)**, a method that predicts unknown values by exploiting the fact that nearby measurements tend to resemble each other. Pixels in astronomical images behave this way, especially in smoothly varying dust clouds: knowing the surrounding pixels lets you estimate what a hidden pixel's value should be.

![Figure 1](/iaifi-research-blog/figures/2201_07246/figure_1.png)

Here's the LPI workflow in practice:

1. **Mask the star.** For each detected source, the algorithm identifies which pixels are contaminated by starlight, based on the telescope's **Point Spread Function** (the characteristic blurred halo that starlight spreads into through any real optical system).
2. **Estimate local covariance.** Using surrounding unmasked pixels, LPI builds a local statistical model of how background brightness varies. **Covariance** captures how strongly neighboring pixels tend to rise and fall in brightness together, essentially the texture of the dust or gas in that region.
3. **Infill the hidden pixels.** With this covariance model, the algorithm predicts what the background beneath the star should have been, along with how uncertain that prediction is.
4. **Correct the flux and error.** The predicted background is subtracted from the measured brightness, yielding a cleaner stellar flux. The infill uncertainty propagates directly into the reported error bar.

What sets this apart from classical GPR is flexibility. Standard GPR requires choosing a specific functional form for the covariance, an exponential decay or a Matérn kernel (a formula describing how correlation fades with distance), then fitting its parameters. LPI sidesteps this by estimating covariance nonparametrically: directly from the data, no formula assumed, using only a local neighborhood of pixels. Since astronomical images are pixelized grids, covariance is sampled at fixed pixel separations, keeping the calculation manageable.

The team validated LPI on synthetic images with known ground-truth backgrounds, then on real dust fields, and showed it holds up even in crowded fields, regions where stars overlap and photometric pipelines notoriously struggle.

## Why It Matters

The scale of the application puts real weight behind the method. Saydjari and Finkbeiner applied LPI to the full second data release of the **Dark Energy Camera Plane Survey (DECaPS2)**, a dataset containing 34 billion individual detections.

On nebulous fields, LPI eliminated large numbers of statistically anomalous measurements flagged as greater than 3σ outliers (readings more than three standard deviations from expected values, a standard red flag for unreliable data). Uncertainty estimates improved by a factor of roughly 2 to 3. That's not marginal: error bars that were previously half the size they should have been now reflect reality.

![Figure 2](/iaifi-research-blog/figures/2201_07246/figure_2.png)

What makes LPI most useful in practice is that it works as a post-processing step, applied after a standard light-measuring pipeline has already run. It doesn't require rebuilding complex data reduction infrastructure. It can retroactively improve archival survey data and slot into future surveys like the Legacy Survey of Space and Time (LSST) at the Vera C. Rubin Observatory, which will observe billions of Galactic-plane stars over its decade-long run.

![Figure 3](/iaifi-research-blog/figures/2201_07246/figure_3.png)

The method isn't limited to optical or infrared wavelengths. Any survey with pixelized images and spatially correlated backgrounds (radio, submillimeter, X-ray) could benefit from the same approach.

Reliable uncertainty estimates matter more than they might seem. Most of what astronomers care about, from distances and ages to compositions of stars and maps of interstellar dust, comes from statistical inferences built on brightness catalogs. Feed those inferences with error bars that are too small, and every downstream conclusion becomes overconfident. LPI makes the data tell the truth about its own limitations.

> **Bottom Line:** LPI is a statistically grounded, scalable, post-processing method that corrects stellar brightness measurements on complex backgrounds and produces honest uncertainty estimates, improving catalog quality across 34 billion measurements and opening the door to better science from both archival and future sky surveys.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work takes Gaussian process-inspired statistical machine learning and applies it directly to a core problem in observational astrophysics, using nonparametric covariance estimation to connect raw pixel data to precise stellar measurements.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">LPI shows how principled uncertainty quantification, a longstanding challenge for neural network-based approaches, can be built into a regression-based infilling framework. The approach offers a practical model for reliable, interpretable uncertainty estimation in scientific imaging tasks.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By improving photometric accuracy for stars embedded in interstellar gas and dust, the method sharpens our ability to map the structure of the interstellar medium and trace the environments where star formation occurs.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future surveys like LSST at the Vera C. Rubin Observatory and the Nancy Grace Roman Space Telescope will produce datasets where structured backgrounds are the rule rather than the exception, making methods like LPI essential; see [arXiv:2201.07246](https://arxiv.org/abs/2201.07246) for the full paper.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Photometry on Structured Backgrounds: Local Pixelwise Infilling by Regression</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2201.07246</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Andrew K. Saydjari", "Douglas P. Finkbeiner"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Photometric pipelines struggle to estimate both the flux and flux uncertainty for stars in the presence of structured backgrounds such as filaments or clouds. However, it is exactly stars in these complex regions that are critical to understanding star formation and the structure of the interstellar medium. We develop a method, similar to Gaussian process regression, which we term local pixelwise infilling (LPI). Using a local covariance estimate, we predict the background behind each star and the uncertainty on that prediction in order to improve estimates of flux and flux uncertainty. We show the validity of our model on synthetic data and real dust fields. We further demonstrate that the method is stable even in the crowded field limit. While we focus on optical-IR photometry, this method is not restricted to those wavelengths. We apply this technique to the 34 billion detections in the second data release of the Dark Energy Camera Plane Survey (DECaPS2). In addition to removing many $>3σ$ outliers and improving uncertainty estimates by a factor of $\sim 2-3$ on nebulous fields, we also show that our method is well-behaved on uncrowded fields. The entirely post-processing nature of our implementation of LPI photometry allows it to easily improve the flux and flux uncertainty estimates of past as well as future surveys.</span></div></div>
</div>
