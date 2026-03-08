---
abstract: Perturbative, or effective field theory (EFT)-based, full-shape analyses
  of galaxy clustering data involve ``nuisance parameters'' to capture various observational
  effects such as the galaxy-dark matter connection (galaxy bias). We present an efficient
  approach to set informative physically motivated priors on these parameters. We
  extract these priors from simulated galaxy catalogs based on halo occupation distribution
  (HOD) models. First, we build a joint distribution between EFT galaxy bias and HOD
  parameters from a set of 10,500 HOD mock catalogs. We use the field level EFT technique
  that allows for cosmic variance cancellation, enabling a precision calibration of
  EFT parameters from computationally inexpensive small-volume simulations. Second,
  we use neural density estimators -- normalizing flows -- to model the marginal probability
  density of the EFT parameters, which can be used as a prior distribution in full
  shape analyses. As a first application, we use our HOD-based priors in a new analysis
  of galaxy power spectra and bispectra from the BOSS survey in the context of single
  field primordial non-Gaussianity. We find that our priors lead to a reduction of
  the posterior volume of bias parameters by an order of magnitude. We also find $f_{\rm
  NL}^{\rm equil} = 320\pm 300$ and $f_{\rm NL}^{\rm ortho} = 100\pm 130$ (at 68\%
  CL) in a combined two-template analysis, representing a $\approx 40\%$ improvement
  in constraints on single field primordial non-Gaussianity, equivalent to doubling
  the survey volume.
arxivId: '2402.13310'
arxivUrl: https://arxiv.org/abs/2402.13310
authors:
- Mikhail M. Ivanov
- Carolina Cuesta-Lazaro
- Siddharth Mishra-Sharma
- Andrej Obuljen
- Michael W. Toomey
concepts:
- effective field theory
- primordial non-gaussianity
- normalizing flows
- simulation-based inference
- galaxy bias calibration
- density estimation
- bayesian inference
- posterior estimation
- cosmological simulation
- dark matter
- surrogate modeling
- dark energy
figures:
- /iaifi-research-blog/figures/2402_13310/figure_2.png
- /iaifi-research-blog/figures/2402_13310/figure_2.png
pdfUrl: https://arxiv.org/pdf/2402.13310v2
published: '2024-02-20T19:00:00+00:00'
theme: Astrophysics
title: 'Full-shape analysis with simulation-based priors: constraints on single field
  inflation from BOSS'
wordCount: 1048
---

## The Big Picture

Imagine trying to weigh something on a scale that vibrates. You can still get a reading, but the wobble limits your precision. Now imagine you had a blueprint for exactly how that scale vibrates under different conditions, so you could subtract the noise. Your measurement suddenly gets much sharper.

A team from MIT, Harvard, and the University of Zurich has done something like this for one of the most ambitious measurements in modern cosmology: probing the physics of the Big Bang using the largest maps of galaxies ever built.

The problem: galaxies don't trace the underlying structure of matter in the universe perfectly. They form in preferred locations, dense knots of invisible dark matter, and the relationship between where galaxies sit and where matter actually is turns out to be messy and complicated. That messiness injects a "wobble" into any attempt to use galaxy maps to measure fundamental cosmic physics.

By training a neural network on 10,500 simulated galaxy catalogs, the researchers built a precise map of that wobble and used it as an intelligent correction, cutting measurement uncertainty by 40%.

> **Key Insight:** By replacing vague assumptions about galaxy bias with AI-learned priors from galaxy simulations, this team achieved the equivalent of doubling the volume of one of the world's premier galaxy surveys, without collecting a single new data point.

## How It Works

The core challenge: to extract cosmological signals from galaxy surveys like BOSS (the Baryon Oscillation Spectroscopic Survey), analysts use the **Effective Field Theory of Large-Scale Structure (EFT-LSS)**. This mathematical framework describes how galaxies cluster in space on large scales, building a rigorous description from simpler, well-understood components. EFT is fast (templates compute in under a second) and systematically improvable. But it comes with a price.

EFT requires **galaxy bias parameters**, numbers like *b*₁, *b*₂, and *bG*₂, that encode how galaxies trace the dark matter distribution. These capture messy small-scale physics: how galaxies form inside **dark matter halos** (the invisible gravitational scaffolding around which galaxies assemble) and how they respond to their surroundings.

Traditionally, analysts treat these as free parameters and marginalize over them using broad, uninformative priors, averaging over all plausible values. The result: significant dilution of the cosmological signals you're trying to measure. You're leaving the scale vibrating when you don't have to.

![Figure 1](/iaifi-research-blog/figures/2402_13310/figure_2.png)

The team's solution unfolds in two steps:

1. **Build the bias-from-simulations map.** They ran 10,500 mock galaxy catalogs using the **Halo Occupation Distribution (HOD)** model, a statistical recipe that populates dark matter halos with galaxies according to rules rooted in real observations. They extracted EFT bias parameters from these mocks using **field-level EFT**, a technique that exploits "cosmic variance cancellation": because the simulated and reference universes share the same large-scale structure, statistical noise cancels out, enabling precise measurements from computationally cheap small boxes.

2. **Learn the distribution with normalizing flows.** The 10,500 samples span a 14-dimensional parameter space (HOD parameters plus EFT bias parameters). Rather than fitting simple Gaussian approximations, the team used **normalizing flows**, a type of neural network that learns complex probability distributions by gradually transforming a simple shape (like a bell curve) into whatever shape the data requires.


The learned marginal distribution over EFT parameters then serves as a prior in the actual data analysis. It isn't a vague Gaussian guess. It knows, from thousands of simulations, which combinations of bias parameters are physically plausible for BOSS-like galaxies and rules out the vast swaths of parameter space that are physically unreasonable.

## Why It Matters

The immediate application is **primordial non-Gaussianity (PNG)**, subtle statistical patterns in the universe's earliest moments that reveal whether the initial density fluctuations were perfectly random or showed signs of more exotic physics. The team targets *equilateral* and *orthogonal* PNG templates, which probe how the **inflaton field** (the energy field thought to have driven the universe's rapid early expansion) interacted with itself. If inflation wasn't the simplest possible single-field model, PNG is where the fingerprints show up.

Using HOD-based priors on BOSS **power spectra and bispectra** (statistical summaries of how strongly galaxies cluster at different scales and in different geometric configurations), the team finds *f*_NL^equil = 320 ± 300 and *f*_NL^ortho = 100 ± 130 (68% confidence), with uncertainties roughly 40% smaller than conventional analyses. The **posterior volume** for galaxy bias parameters in each BOSS chunk shrank by an order of magnitude. That's not a marginal improvement; it's a qualitative leap in constraining inflation physics from galaxy surveys.


This matters for the future. Surveys like DESI, Euclid, and the Roman Space Telescope will map hundreds of millions of galaxies over the coming decade. The galaxy bias problem won't disappear. It will grow more acute as statistical power improves. The simulation-based prior approach transfers directly to these next-generation surveys.

The framework is modular, too: as HOD models improve and hydrodynamical simulations get more realistic, the priors sharpen, essentially for free.

There's a broader point worth making. Machine learning didn't replace physical modeling here; it amplified it. The normalizing flow didn't invent knowledge about galaxy bias. It compressed and organized knowledge already embedded in thousands of physically motivated simulations, making it usable in a rigorous Bayesian framework.

> **Bottom Line:** By combining 10,500 galaxy simulations with neural density estimators, this work turned galaxy bias from a constraint-killing nuisance into a well-characterized prior, delivering a 40% improvement in inflation constraints equivalent to doubling the BOSS survey volume, and setting a template for next-generation large-scale structure cosmology.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits squarely at the intersection of AI and cosmology, using normalizing flows to encode physically motivated knowledge from galaxy simulations into a Bayesian prior that enables sharper tests of inflationary physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Neural density estimators can extract and compress high-dimensional physical distributions from simulation ensembles at a scale (10,500 samples, 14-dimensional parameter space) that would be impractical without deep learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The improved constraints on equilateral and orthogonal primordial non-Gaussianity push closer to the theoretical thresholds that distinguish standard single-field inflation from models with exotic inflaton self-interactions or modified propagation speeds.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future application to DESI, Euclid, and Roman data, combined with improved HOD and hydrodynamical simulation models, could sharpen these constraints significantly. See [arXiv:2402.13310](https://arxiv.org/abs/2402.13310) for full details.</span></div></div>
</div>
