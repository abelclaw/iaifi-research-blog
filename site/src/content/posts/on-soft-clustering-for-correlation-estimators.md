---
abstract: Properly estimating correlations between objects at different spatial scales
  necessitates $\mathcal{O}(n^2)$ distance calculations. For this reason, most widely
  adopted packages for estimating correlations use clustering algorithms to approximate
  local trends. However, methods for quantifying the error introduced by this clustering
  have been understudied. In response, we present an algorithm for estimating correlations
  that is probabilistic in the way that it clusters objects, enabling us to quantify
  the uncertainty caused by clustering simply through model inference. These soft
  clustering assignments enable correlation estimators that are theoretically differentiable
  with respect to their input catalogs. Thus, we also build a theoretical framework
  for differentiable correlation functions and describe their utility in comparison
  to existing surrogate models. Notably, we find that repeated normalization and distance
  function calls slow gradient calculations and that sparse Jacobians destabilize
  precision, pointing towards either approximate or surrogate methods as a necessary
  solution to exact gradients from correlation functions. To that end, we close with
  a discussion of surrogate models as proxies for correlation functions. We provide
  an example that demonstrates the efficacy of surrogate models to enable gradient-based
  optimization of astrophysical model parameters, successfully minimizing a correlation
  function output. Our numerical experiments cover science cases across cosmology,
  from point spread function (PSF) modeling efforts to gravitational simulations to
  galaxy intrinsic alignment (IA).
arxivId: '2504.06174'
arxivUrl: https://arxiv.org/abs/2504.06174
authors:
- Edward Berman
- Sneh Pandya
- Jacqueline McCleary
- Marko Shuntov
- Caitlin Casey
- Nicole Drakos
- Andreas Faisst
- Steven Gillman
- Ghassem Gozaliasl
- Natalie Hogg
- Jeyhan Kartaltepe
- Anton Koekemoer
- Wilfried Mercier
- Diana Scognamiglio
- COSMOS-Web
- ':'
- The JWST Cosmic Origins Survey
concepts:
- clustering
- uncertainty quantification
- soft clustering assignments
- surrogate modeling
- differentiable correlation functions
- bayesian inference
- monte carlo methods
- inverse problems
- cosmological simulation
- posterior estimation
- dark energy
- rho statistics
figures:
- /iaifi-research-blog/figures/2504_06174/figure_1.png
- /iaifi-research-blog/figures/2504_06174/figure_1.png
- /iaifi-research-blog/figures/2504_06174/figure_2.png
- /iaifi-research-blog/figures/2504_06174/figure_2.png
- /iaifi-research-blog/figures/2504_06174/figure_3.png
- /iaifi-research-blog/figures/2504_06174/figure_3.png
pdfUrl: https://arxiv.org/pdf/2504.06174v3
published: '2025-04-08T16:18:39+00:00'
theme: Astrophysics
title: On Soft Clustering For Correlation Estimators
wordCount: 1265
---

## The Big Picture

Imagine measuring how galaxies cluster across the cosmos. To do it perfectly, you'd need to compare every galaxy to every other, a trillion calculations for a catalog of a million objects. Astronomers solved this decades ago with a clever trick: group nearby objects into representative clusters first, then measure distances between clusters instead of individual points. Fast, well-tested, and usually reliable.

But nobody has been asking what happens when you don't have millions of galaxies to work with.

This is the problem facing researchers using the James Webb Space Telescope's COSMOS-Web survey, one of JWST's largest programs. In those deep-field images, the number of usable stars for calibrating how the telescope smears a pinpoint of light into a tiny blurred spot (what astronomers call the **point spread function**, or PSF) sometimes numbers in the hundreds, not millions.

At that scale, the assumption that small grouping errors cancel out breaks down completely. A single misassigned galaxy can shift a measurement by an entire distance bin, badly biasing the correlation functions astronomers depend on to map the structure of the universe.

Edward Berman and colleagues tackled this by rethinking clustering at its foundation, replacing rigid, all-or-nothing assignments with probabilistic ones that carry their own built-in uncertainty. The result is a framework for **soft clustering** that improves statistical estimates and makes them *differentiable*, meaning you can calculate precisely how a change in input ripples through to the output. That opens up new ways of fitting astrophysical models that weren't previously accessible.

> **Key Insight:** By treating cluster assignments as probabilities rather than hard decisions, the team can quantify the *epistemic uncertainty* introduced by clustering itself, a source of error that cosmological analyses have largely overlooked.

## How It Works

Traditional correlation estimators like TreeCorr use hard clustering: each data point gets assigned to exactly one cluster center, period. Points that sit between two centers get arbitrarily assigned to one, introducing epistemic uncertainty, the kind that arises from the model's limitations rather than from the data itself.

Soft clustering replaces that with probability distributions. Instead of asking "which cluster does this galaxy belong to?", the algorithm asks "what's the probability this galaxy belongs to each cluster?" Run the analysis multiple times with those distributions and you get a spread of answers. That spread *is* the clustering uncertainty, quantified for free.

The paper tests this across three experiments:

- **Model uncertainty:** Repeat soft clustering many times and measure the standard deviation of the resulting correlation functions.
- **Differentiability:** Forward-model a gravitational simulation and compute gradients through the correlation estimator.
- **Surrogate modeling:** Train a neural network to emulate the full estimator, then use that differentiable proxy for fast Bayesian inference.

![Figure 1](figure:1)

The differentiability result is the most technically ambitious. The **Landy-Szalay estimator**, the classic statistic for measuring how galaxy positions correlate across the sky, involves counting galaxy pairs in angular distance bins. With soft assignments, those bin counts become smooth functions, and in principle you can take gradients all the way back to the input catalog.

In practice, serious obstacles arise. Repeated distance calculations slow gradient computation dramatically. The Jacobian (the table tracking how every output value changes when you nudge every input) turns out sparse and poorly behaved numerically. Exact automatic differentiation through correlation functions is theoretically possible but practically brutal.

## Why It Matters

The practical payoff comes from surrogate models. Rather than differentiating through the full correlation estimator, the team trains a neural network to emulate its behavior. Neural networks are differentiable by construction, so once you have a good surrogate, gradients come essentially for free.

They demonstrate this on **galaxy intrinsic alignment (IA)**, the subtle tendency of galaxies to orient themselves with the large-scale structure around them. IA is a major systematic in weak gravitational lensing surveys. Model it incorrectly and your measurements of dark energy and dark matter shift. A trained surrogate successfully recovers IA parameters via Hamiltonian Monte Carlo, a sampling algorithm that requires gradients to work efficiently.

![Figure 2](figure:2)

The framework applies across multiple science cases:
- **PSF modeling** for JWST/NIRCam, where small star counts make clustering errors non-negligible
- **N-body simulations**, where forward models connect initial conditions to observable clustering statistics
- **Galaxy intrinsic alignment**, where surrogates enable gradient-based posterior sampling

As JWST pushes to deeper fields and smaller samples, the assumption that clustering errors wash out no longer holds. Every JWST deep-field survey faces this challenge.

And as the field moves toward differentiable pipelines and simulation-based inference, uncertainty-aware correlation estimators become essential infrastructure. Making classical statistical estimators differentiable means the full machinery of modern deep learning, from gradient descent to automatic differentiation to Hamiltonian Monte Carlo, becomes available the moment you can compute gradients through your science pipeline. The paper's honest accounting of where exact gradients fail and where surrogates succeed lays out a practical path forward.

> **Bottom Line:** Soft clustering gives astronomers a principled way to quantify an overlooked source of error in correlation measurements. The differentiable framework it enables, best accessed through surrogate models, makes gradient-based optimization available for astrophysical inference that would otherwise require brute-force sampling.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects probabilistic machine learning (soft clustering and surrogate neural networks) with observational cosmology, building uncertainty-aware statistical tools for the small-sample regime that JWST deep-field surveys increasingly face.

- **Impact on Artificial Intelligence:** The paper develops a theoretical framework for differentiable correlation functions and shows how neural network surrogates can step in as practical gradient proxies when exact automatic differentiation proves numerically unstable.

- **Impact on Fundamental Interactions:** Rigorous epistemic uncertainty quantification in two-point correlation functions improves PSF modeling, weak gravitational lensing, and galaxy intrinsic alignment measurements, all of which feed directly into cosmological constraints on dark energy and dark matter.

- **Outlook and References:** Future directions include extending the surrogate framework to three-point correlation functions and integrating soft clustering into production pipelines for upcoming surveys. The paper is available at [arXiv:2504.06174](https://arxiv.org/abs/2504.06174), and the code is open-source at github.com/EdwardBerman/cosmo-corr.

## Original Paper Details
- **Title:** On Soft Clustering For Correlation Estimators
- **arXiv ID:** 2504.06174
- **Authors:** ["Edward Berman", "Sneh Pandya", "Jacqueline McCleary", "Marko Shuntov", "Caitlin Casey", "Nicole Drakos", "Andreas Faisst", "Steven Gillman", "Ghassem Gozaliasl", "Natalie Hogg", "Jeyhan Kartaltepe", "Anton Koekemoer", "Wilfried Mercier", "Diana Scognamiglio", "COSMOS-Web", ":", "The JWST Cosmic Origins Survey"]
- **Abstract:** Properly estimating correlations between objects at different spatial scales necessitates $\mathcal{O}(n^2)$ distance calculations. For this reason, most widely adopted packages for estimating correlations use clustering algorithms to approximate local trends. However, methods for quantifying the error introduced by this clustering have been understudied. In response, we present an algorithm for estimating correlations that is probabilistic in the way that it clusters objects, enabling us to quantify the uncertainty caused by clustering simply through model inference. These soft clustering assignments enable correlation estimators that are theoretically differentiable with respect to their input catalogs. Thus, we also build a theoretical framework for differentiable correlation functions and describe their utility in comparison to existing surrogate models. Notably, we find that repeated normalization and distance function calls slow gradient calculations and that sparse Jacobians destabilize precision, pointing towards either approximate or surrogate methods as a necessary solution to exact gradients from correlation functions. To that end, we close with a discussion of surrogate models as proxies for correlation functions. We provide an example that demonstrates the efficacy of surrogate models to enable gradient-based optimization of astrophysical model parameters, successfully minimizing a correlation function output. Our numerical experiments cover science cases across cosmology, from point spread function (PSF) modeling efforts to gravitational simulations to galaxy intrinsic alignment (IA).
