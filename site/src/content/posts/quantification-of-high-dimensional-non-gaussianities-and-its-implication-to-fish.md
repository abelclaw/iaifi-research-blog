---
abstract: It is well known that the power spectrum is not able to fully characterize
  the statistical properties of non-Gaussian density fields. Recently, many different
  statistics have been proposed to extract information from non-Gaussian cosmological
  fields that perform better than the power spectrum. The Fisher matrix formalism
  is commonly used to quantify the accuracy with which a given statistic can constrain
  the value of the cosmological parameters. However, these calculations typically
  rely on the assumption that the likelihood of the considered statistic follows a
  multivariate Gaussian distribution. In this work we follow Sellentin & Heavens (2017)
  and use two different statistical tests to identify non-Gaussianities in different
  statistics such as the power spectrum, bispectrum, marked power spectrum, and wavelet
  scatering transform (WST). We remove the non-Gaussian components of the different
  statistics and perform Fisher matrix calculations with the \textit{Gaussianized}
  statistics using Quijote simulations. We show that constraints on the parameters
  can change by a factor of $\sim 2$ in some cases. We show with simple examples how
  statistics that do not follow a multivariate Gaussian distribution can achieve artificially
  tight bounds on the cosmological parameters when using the Fisher matrix formalism.
  We think that the non-Gaussian tests used in this work represent a powerful tool
  to quantify the robustness of Fisher matrix calculations and their underlying assumptions.
  We release the code used to compute the power spectra, bispectra, and WST that can
  be run on both CPUs and GPUs.
arxivId: '2204.05435'
arxivUrl: https://arxiv.org/abs/2204.05435
authors:
- Core Francisco Park
- Erwan Allys
- Francisco Villaescusa-Navarro
- Douglas P. Finkbeiner
concepts:
- fisher information matrix
- hypothesis testing
- likelihood estimation
- uncertainty quantification
- cosmological simulation
- spectral methods
- wavelet scattering transform
- bayesian inference
- dimensionality reduction
- monte carlo methods
- dark energy
- dark matter
figures:
- /iaifi-research-blog/figures/2204_05435/figure_1.png
- /iaifi-research-blog/figures/2204_05435/figure_2.png
- /iaifi-research-blog/figures/2204_05435/figure_3.png
pdfUrl: https://arxiv.org/pdf/2204.05435v1
published: '2022-04-11T23:09:27+00:00'
theme: Astrophysics
title: Quantification of high dimensional non-Gaussianities and its implication to
  Fisher analysis in cosmology
wordCount: 1024
---

## The Big Picture

Imagine you're trying to measure the weight of a package, but the scale reads differently depending on whether you're weighing heavy or light objects. You'd get a precise-looking number, but it wouldn't mean what you think.

That's the problem tackled in a new paper from researchers at Harvard, ENS Paris, the Flatiron Institute, and Princeton. Cosmologists have been using the **Fisher matrix**, a mathematical forecasting tool, to predict how precisely future galaxy surveys can pin down the fundamental parameters of our universe. But that tool carries a hidden assumption. When it breaks, the forecast can be dangerously optimistic.

The universe's matter isn't spread out smoothly. Gravity has sculpted it into a cosmic web of filaments, voids, and dense clusters, a pattern that doesn't follow a simple, symmetric bell curve. That complexity makes it harder to describe with standard mathematical tools.

Cosmologists have known for years that the **power spectrum**, the standard tool for summarizing how matter clusters across different scales, throws away information precisely because it can't capture this complexity. More sophisticated statistics have been proposed as upgrades. But here's the twist: when you use the Fisher matrix to evaluate these tools, you're still assuming that *they* behave like bell curves, even if the underlying field doesn't.

Park, Allys, Villaescusa-Navarro, and Finkbeiner set out to systematically test that assumption and found it fails, sometimes badly enough to change parameter constraints by a factor of two.

> **Key Insight:** When cosmological statistics violate the Gaussian assumption baked into Fisher matrix forecasts, the resulting parameter constraints can be artificially tight, meaning we might think a future survey is twice as powerful as it actually is.

## How It Works

The **Fisher matrix formalism** answers the question: "Given a statistic and a set of parameters, how precisely can we measure those parameters?" It doesn't require actual data, just simulations and derivatives. The catch is that it assumes the probability distribution of your chosen statistic looks like a bell curve, even in high-dimensional space. The authors asked what happens when it doesn't.

To test this, they used the **Quijote simulations**, a suite of 44,100 gravity-only computer simulations built for Fisher matrix calculations. From these, they computed four statistics for the matter density field:

- **Power spectrum** — the standard tool for measuring how matter clusters across different length scales, using techniques from signal processing
- **Bispectrum** — a three-point generalization that captures some of the non-bell-curve complexity in the matter field
- **Marked power spectrum** — a cleverly weighted version that gives extra weight to underdense regions, making it sensitive to different physics
- **Wavelet Scattering Transform (WST)** — a deep-learning-inspired multi-scale representation with strong cosmological information content

For each statistic, they applied two Gaussianity tests (following Sellentin & Heavens 2017) that quantify whether the distribution of a statistic across many simulations actually looks like a bell curve in high dimensions. Even the humble power spectrum fails, and more exotic statistics can fail harder.

![Figure 1](figure:1)

They then developed a procedure to Gaussianize the statistics: identify the mathematical directions in which the data varies in a skewed or irregular way, then remove them. What remains is a cleaned, bell-curve-safe version. They reran Fisher matrix calculations on both raw and Gaussianized versions and compared the results.

The differences are substantial. For some statistics and cosmological parameters, constraints shift by roughly a factor of two. The non-Gaussian dimensions were quietly inflating or deflating the apparent information content, and the Fisher matrix couldn't tell the difference.

![Figure 2](figure:2)

A toy example drives the point home. Apply a monotonic transformation to a statistic that carries *zero* new cosmological information, and the Fisher matrix still produces different, often tighter, constraints. A statistic shouldn't get credit for information it doesn't have just because its probability distribution has a funny shape.

![Figure 3](figure:3)

The released code, which runs on both CPUs and GPUs, computes power spectra, bispectra, and WST, making these non-Gaussianity tests available to the broader cosmology community.

## Why It Matters

Upcoming surveys like DESI, Euclid, and the Rubin Observatory represent billions of dollars of investment and will map hundreds of millions of galaxies. Cosmologists are counting on advanced statistics to unlock measurements of neutrino masses, dark energy, and the universe's geometry at new levels of precision. Fisher matrix forecasts are what justify those bets. If those forecasts are systematically biased by violated Gaussianity assumptions, we could be building survey strategies around promises the data can't keep.

None of this means the new statistics are useless. It means the process of *evaluating* them needs a sanity check. The non-Gaussianity tests developed here do just that: they let you audit whether a Fisher forecast is trustworthy before committing to it. Applying these tests routinely could become standard practice, much like checking for numerical convergence in derivative estimates.

> **Bottom Line:** Fisher matrix forecasts can overestimate or underestimate parameter constraints by up to a factor of two when the underlying statistics aren't Gaussian. This paper provides the tools to catch and correct that error before it misleads survey design.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects machine-learning-inspired statistics, like the Wavelet Scattering Transform drawn from deep learning, with classical cosmological inference tools, stress-testing AI-adjacent methods against the statistical assumptions embedded in physics pipelines.
- **Impact on Artificial Intelligence:** High-dimensional non-Gaussianity tests turn out to be essential for validating any data-driven statistic used in scientific inference, a lesson that applies directly to AI/ML methods being imported into cosmology and beyond.
- **Impact on Fundamental Interactions:** By exposing and correcting a systematic bias in Fisher matrix forecasts, this work sharpens our ability to extract reliable measurements of fundamental cosmological parameters, including neutrino masses and dark energy properties, from large-scale structure surveys.
- **Outlook and References:** Future work should apply these Gaussianity audits to field-level inference methods and neural compression schemes as they enter the cosmological toolkit; the paper and its GPU-accelerated code are available at [arXiv:2204.05435](https://arxiv.org/abs/2204.05435).

## Original Paper Details
- **Title:** Quantification of high dimensional non-Gaussianities and its implication to Fisher analysis in cosmology
- **arXiv ID:** 2204.05435
- **Authors:** ["Core Francisco Park", "Erwan Allys", "Francisco Villaescusa-Navarro", "Douglas P. Finkbeiner"]
- **Abstract:** It is well known that the power spectrum is not able to fully characterize the statistical properties of non-Gaussian density fields. Recently, many different statistics have been proposed to extract information from non-Gaussian cosmological fields that perform better than the power spectrum. The Fisher matrix formalism is commonly used to quantify the accuracy with which a given statistic can constrain the value of the cosmological parameters. However, these calculations typically rely on the assumption that the likelihood of the considered statistic follows a multivariate Gaussian distribution. In this work we follow Sellentin & Heavens (2017) and use two different statistical tests to identify non-Gaussianities in different statistics such as the power spectrum, bispectrum, marked power spectrum, and wavelet scatering transform (WST). We remove the non-Gaussian components of the different statistics and perform Fisher matrix calculations with the \textit{Gaussianized} statistics using Quijote simulations. We show that constraints on the parameters can change by a factor of $\sim 2$ in some cases. We show with simple examples how statistics that do not follow a multivariate Gaussian distribution can achieve artificially tight bounds on the cosmological parameters when using the Fisher matrix formalism. We think that the non-Gaussian tests used in this work represent a powerful tool to quantify the robustness of Fisher matrix calculations and their underlying assumptions. We release the code used to compute the power spectra, bispectra, and WST that can be run on both CPUs and GPUs.
