---
abstract: Optimal extraction of the non-Gaussian information encoded in the Large-Scale
  Structure (LSS) of the universe lies at the forefront of modern precision cosmology.
  We propose achieving this task through the use of the Wavelet Scattering Transform
  (WST), which subjects an input field to a layer of non-linear transformations that
  are sensitive to non-Gaussianity in spatial density distributions through a generated
  set of WST coefficients. In order to assess its applicability in the context of
  LSS surveys, we apply the WST on the 3D overdensity field obtained by the Quijote
  simulations, out of which we extract the Fisher information in 6 cosmological parameters.
  It is subsequently found to deliver a large improvement in the marginalized errors
  on all parameters, ranging between $1.2-4\times$ tighter than the corresponding
  ones obtained from the regular 3D cold dark matter + baryon power spectrum, as well
  as a $50 \%$ improvement over the neutrino mass constraint given by the marked power
  spectrum. Through this first application on 3D cosmological fields, we demonstrate
  the great promise held by this novel statistic and set the stage for its future
  application to actual galaxy observations.
arxivId: '2108.07821'
arxivUrl: https://arxiv.org/abs/2108.07821
authors:
- Georgios Valogiannis
- Cora Dvorkin
concepts:
- wavelet scattering transform
- non-gaussian statistics
- cosmological simulation
- feature extraction
- bayesian inference
- spectral methods
- simulation-based inference
- neutrino detection
- dark matter
- convolutional networks
- dark energy
- dimensionality reduction
figures:
- /iaifi-research-blog/figures/2108_07821/figure_1.png
- /iaifi-research-blog/figures/2108_07821/figure_2.png
- /iaifi-research-blog/figures/2108_07821/figure_3.png
pdfUrl: https://arxiv.org/pdf/2108.07821v2
published: '2021-08-17T18:00:04+00:00'
theme: Astrophysics
title: Towards an Optimal Estimation of Cosmological Parameters with the Wavelet Scattering
  Transform
wordCount: 1255
---

## The Big Picture

Imagine trying to understand a sculpture by only measuring its weight. You'd miss the curves, the texture, the fine details that make it what it is. That's roughly the situation cosmologists face when using the **power spectrum** to analyze the large-scale structure of the universe.

The power spectrum summarizes how matter is clustered at different scales, essentially a count of how many lumps of various sizes appear across the cosmos. But it compares only pairs of points at a time. Gravity is nonlinear. It has spent billions of years building far richer structure (filaments, voids, knots of dark matter) that no pairwise comparison can fully capture.

The stakes are high. Surveys like DESI, the Vera Rubin Observatory, and Euclid are mapping the 3D distribution of galaxies across cosmic history with extraordinary precision. Hidden in those maps is information about neutrino masses, the nature of dark energy, and the physics of the early universe. If our statistical tools can only read part of the message, we leave science on the table.

The question isn't whether better statistics exist. It's whether they're practical.

Georgios Valogiannis and Cora Dvorkin at Harvard answer with a clear yes. They apply the **Wavelet Scattering Transform** (WST) to three-dimensional cosmological density fields for the first time, showing that it extracts dramatically more information from the same simulations than the standard power spectrum, all without the interpretability headaches of a neural network.

> **Key Insight:** The Wavelet Scattering Transform acts like a neural network with fixed, mathematically well-understood filters. It captures the complex clustering patterns that gravity builds over billions of years and delivers up to 4× tighter cosmological parameter constraints than the conventional power spectrum.

## How It Works

The WST borrows intuition from deep learning while keeping its hands tied in a principled way. A **convolutional neural network** (CNN) learns arbitrary filters during training, making it powerful but opaque: a black box that scientists distrust when applied to real survey data. The WST makes a different trade. It uses fixed wavelets, convolution operations, and modulus nonlinearities arranged in layers. No training, no learned weights, no mystery.

The recipe:

1. **Convolve** the 3D density field with a bank of wavelets tuned to different scales and orientations. Each wavelet is a solid harmonic wavelet, a mathematical probe sensitive to a specific size and direction in space.
2. **Take the modulus** of each convolved field. This nonlinear step makes the output invariant to small translations while preserving clustering information.
3. **Average spatially** to produce S₁ coefficients, one number per (scale, angular order) combination summarizing how much structure exists at that scale.
4. **Repeat** the convolution-modulus-average chain on the modulus fields from step 2 to get S₂ coefficients, which capture correlations *between* scales, encoding information up to the four-point function.

![Figure 1](/iaifi-research-blog/figures/2108_07821/figure_1.png)

The authors implement this using the KYMATIO package, applying WST coefficients to the 3D overdensity field from the **Quijote N-body simulations**, a large suite of cosmological simulations spanning a grid in parameter space. From these, they compute a Fisher matrix: a formal measure of how much information each statistic contains about each cosmological parameter.

Six parameters are under scrutiny: matter density (Ωm), baryon density (Ωb), amplitude of primordial fluctuations (σ₈), spectral index (ns), the Hubble constant (h), and the hardest nut in modern cosmology, the sum of neutrino masses (Mν).

![Figure 2](/iaifi-research-blog/figures/2108_07821/figure_2.png)

Across all six parameters, WST delivers 1.2 to 4× tighter constraints than the standard 3D power spectrum from the same simulations. The gains are largest for parameters most sensitive to nonlinear structure.

For neutrino masses specifically, WST beats the marked power spectrum (a recent competitor that up-weights underdense regions to amplify neutrino signatures) by 50%. That's not a marginal improvement. For a single-dataset analysis, that kind of gain changes what questions you can answer.

![Figure 3](/iaifi-research-blog/figures/2108_07821/figure_3.png)

## Why It Matters

Neutrino mass is one of the big open questions in fundamental physics. We know neutrinos have mass, since neutrino oscillation experiments proved it, but laboratory experiments can't yet pin down the absolute scale. Cosmology offers a complementary probe: massive neutrinos suppress structure growth on small scales, leaving a subtle but measurable imprint on the cosmic web.

That imprint is small. It's buried in complex clustering patterns the power spectrum can barely see. A statistic that extracts 50% more neutrino information from the same survey data could be the difference between a detection and an upper bound.

Beyond neutrinos, this work makes a strong case for squeezing more out of next-generation surveys. The analysis uses the dark matter density field directly, the pristine theoretical quantity, rather than the observed galaxy field, which is an imperfect proxy tangled with astrophysical uncertainties. The authors are explicit: this is step one.

Applying WST to galaxy catalogs will require modeling survey geometry, selection effects, and observational systematics. But having shown the statistical power on clean simulations, the motivation to build that pipeline is hard to argue with. The WST's mathematical transparency helps here too. When a statistic constrains a parameter, astronomers need to understand *why*, and with WST that question is tractable in ways that deep learning is not.

> **Bottom Line:** The Wavelet Scattering Transform extracts up to four times more cosmological information than the standard power spectrum from the same 3D density field. It is mathematically transparent, requires no training, and offers a practical route to getting the full science return from galaxy surveys.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work imports a signal-processing tool developed for image recognition and molecular modeling into precision cosmology, showing that wavelet scattering's mathematical structure transfers effectively across physical domains.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The WST sits at a useful middle ground between classical statistics and opaque neural networks: a fixed-weight, interpretable architecture that captures nonlinear structure without requiring labeled training data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By achieving up to 4× tighter constraints on cosmological parameters and a 50% improvement on neutrino mass bounds over the marked power spectrum, this method could make definitive measurements of absolute neutrino mass possible with upcoming galaxy surveys.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend WST to the biased galaxy field and explore custom wavelets designed for cosmological symmetries; the full analysis is available at [arXiv:2108.07821](https://arxiv.org/abs/2108.07821).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Towards an Optimal Estimation of Cosmological Parameters with the Wavelet Scattering Transform</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2108.07821</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Georgios Valogiannis", "Cora Dvorkin"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Optimal extraction of the non-Gaussian information encoded in the Large-Scale Structure (LSS) of the universe lies at the forefront of modern precision cosmology. We propose achieving this task through the use of the Wavelet Scattering Transform (WST), which subjects an input field to a layer of non-linear transformations that are sensitive to non-Gaussianity in spatial density distributions through a generated set of WST coefficients. In order to assess its applicability in the context of LSS surveys, we apply the WST on the 3D overdensity field obtained by the Quijote simulations, out of which we extract the Fisher information in 6 cosmological parameters. It is subsequently found to deliver a large improvement in the marginalized errors on all parameters, ranging between $1.2-4\times$ tighter than the corresponding ones obtained from the regular 3D cold dark matter + baryon power spectrum, as well as a $50 \%$ improvement over the neutrino mass constraint given by the marked power spectrum. Through this first application on 3D cosmological fields, we demonstrate the great promise held by this novel statistic and set the stage for its future application to actual galaxy observations.</span></div></div>
</div>
