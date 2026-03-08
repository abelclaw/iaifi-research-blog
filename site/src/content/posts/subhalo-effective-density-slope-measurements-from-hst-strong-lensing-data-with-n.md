---
abstract: Examining the properties of subhalos with strong gravitational lensing images
  can shed light on the nature of dark matter. From upcoming large-scale surveys,
  we expect to discover orders of magnitude more strong lens systems that can be used
  for subhalo studies. To optimally extract information from a large number of strong
  lensing images, machine learning provides promising avenues for efficient analysis
  that is unachievable with traditional analysis methods, but application of machine
  learning techniques to real observations is still limited. We build upon previous
  work, which uses a neural likelihood-ratio estimator, to constrain the effective
  density slopes of subhalos and demonstrate the feasibility of this method on real
  strong lensing observations. To do this, we implement significant improvements to
  the forward simulation pipeline and undertake careful model evaluation using simulated
  images. Ultimately, we use our trained model to predict the effective subhalo density
  slope from combining a set of strong lensing images taken by the \textit{Hubble
  Space Telescope}. We found the subhalo slope measurement of this set of observations
  to be steeper than the slope predictions of cold dark matter subhalos. Our result
  adds to several previous works that also measured high subhalo slopes in observations.
  Although a possible explanation for this is that subhalos with steeper slopes are
  easier to detect due to selection effects and thus contribute to statistical bias,
  our result nevertheless points to the need for careful analysis of more strong lensing
  observations from future surveys.
arxivId: '2308.09739'
arxivUrl: https://arxiv.org/abs/2308.09739
authors:
- Gemma Zhang
- Atınç Çağan Şengül
- Cora Dvorkin
concepts:
- dark matter
- simulation-based inference
- strong gravitational lensing
- likelihood ratio
- subhalo density slope
- inverse problems
- posterior estimation
- cosmological simulation
- convolutional networks
- model validation
- bayesian inference
- calibration
figures:
- /iaifi-research-blog/figures/2308_09739/figure_1.png
- /iaifi-research-blog/figures/2308_09739/figure_1.png
- /iaifi-research-blog/figures/2308_09739/figure_2.png
- /iaifi-research-blog/figures/2308_09739/figure_2.png
- /iaifi-research-blog/figures/2308_09739/figure_3.png
- /iaifi-research-blog/figures/2308_09739/figure_3.png
pdfUrl: https://arxiv.org/pdf/2308.09739v2
published: '2023-08-18T18:00:01+00:00'
theme: Astrophysics
title: Subhalo effective density slope measurements from HST strong lensing data with
  neural likelihood-ratio estimation
wordCount: 1054
---

## The Big Picture

Imagine trying to weigh a ghost by watching how it bends light around it. That's essentially what astrophysicists do when they study dark matter, the invisible substance making up roughly 85% of all matter in the universe. Dark matter doesn't emit, absorb, or reflect light. It reveals itself only through gravity, and detecting its smallest clumps requires both the sharpest eyes in astronomy and some of the most sophisticated algorithms in machine learning.

Strong gravitational lensing offers one of the best windows into dark matter's structure. When a massive galaxy sits between Earth and a distant light source, it warps spacetime enough to bend and distort the background light into arcs, rings, and multiple images. Buried in those distortions are subtle fingerprints left by dark matter **subhalos**, small clumps of dark matter gravitationally bound to larger galaxies.

Different dark matter theories predict subhalos with different shapes. Cold dark matter predicts dense, sharply peaked clumps (like a spike rising steeply toward the center), while warmer or self-interacting dark matter predicts more diffuse, plateau-shaped ones. Measuring how steeply a subhalo's density rises toward its center is therefore a direct test of dark matter's fundamental nature.

Traditional analysis is brutally slow. Modeling a single subhalo in a lens system can consume enormous computational resources, and upcoming surveys like Euclid and the Rubin Observatory will deliver thousands of lens systems. Gemma Zhang, Atınç Çağan Şengül, and Cora Dvorkin have now shown that a neural network can do this job on real Hubble Space Telescope data, turning a machine learning method loose on actual observations for the first time rather than just simulations.

> **Key Insight:** For the first time, a machine learning technique has successfully extracted dark matter subhalo density slope measurements from real strong lensing images, a proof-of-concept for analyzing the coming flood of data from next-generation surveys.

## How It Works

The core tool is a **neural likelihood-ratio estimator (NLRE)**, a neural network trained not to predict a single answer, but to compare how likely a lensing image is under two competing hypotheses. Think of it like a trained sommelier who can't tell you the exact vintage, but can confidently say whether a wine is more consistent with 2010 or 2015.

![Figure 1](/iaifi-research-blog/figures/2308_09739/figure_1.png)

Here's the pipeline, step by step:

1. **Forward simulation.** The team generates thousands of synthetic lensing images using `lenstronomy`. Each simulated image is 100×100 pixels at 0.04 arcseconds per pixel, precisely matching HST's post-drizzling configuration. The images include a source galaxy, a foreground lens galaxy, a population of subhalos, and line-of-sight halos (dark matter clumps floating between the telescope and the background source, unbound to any galaxy).

2. **Realistic complexity.** The team added layers of realism that previous work skipped: realistic source galaxy morphologies drawn from actual HST cutouts, a lens light model, correlated noise based on real HST noise maps, and point spread function effects (the blurring introduced by the telescope's optics). Training simulations must look like real data, or the model will fail on deployment.

3. **Training the estimator.** The NLRE learns to output a likelihood ratio: given a lensing image, how does the probability of observing it change as you vary the **effective subhalo density slope**, the parameter describing how sharply dark matter density rises toward a subhalo's center? A steeper slope means a more concentrated, "cuspy" subhalo.

4. **Combining observations.** The trained model is applied to a set of real HST lensing images. Because the NLRE produces likelihood ratios, individual measurements can be combined by multiplying them, a statistically rigorous way to pool evidence across multiple lens systems.

![Figure 3](/iaifi-research-blog/figures/2308_09739/figure_2.png)

The team also invested in careful **model evaluation**, testing the network on simulated images with known ground-truth slope values before ever touching real data. This calibration step, often skipped in earlier ML lensing work, is what makes the real-data results credible.

## Why It Matters

Applied to the HST observations, the trained model measured a subhalo density slope steeper than cold dark matter predicts. This isn't an isolated result. It echoes several earlier studies by independent groups, all finding higher-than-expected subhalo concentrations in real observations.

The team is careful about interpretation. Steeper subhalos are easier to detect in lensing images, so selection effects could bias the sample toward unusually concentrated objects. But the consistency across methods is hard to dismiss.

![Figure 5](/iaifi-research-blog/figures/2308_09739/figure_3.png)

What matters most here is the machinery itself. Euclid, the Vera C. Rubin Observatory, and the Nancy Grace Roman Space Telescope will discover thousands of strong lens systems where today we have dozens. Traditional subhalo modeling cannot scale to that volume. Neural likelihood-ratio estimation can. The paper shows the approach works not just on idealized simulations but on the messy reality of actual telescope data, closing the gap between proof-of-concept and operational science tool.

Whether the steep slopes reflect genuine physics (perhaps subhalos stripped of outer layers by tidal forces), systematic effects in the modeling pipeline, or selection bias remains an open question. Answering it requires the larger samples that future surveys will provide, and the ML tools to analyze them efficiently.

> **Bottom Line:** Zhang, Şengül, and Dvorkin applied a neural likelihood-ratio estimator to real Hubble Space Telescope data and measured dark matter subhalo density slopes steeper than cold dark matter predicts. This is the first successful deployment of this ML approach on actual observations, laying the groundwork for the survey era of dark matter science.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits squarely at the intersection of simulation-based inference and observational astrophysics. The authors show that neural likelihood-ratio estimators trained on physically motivated forward models can extract meaningful dark matter constraints from real telescope data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The study pushes simulation-based inference forward by rigorously evaluating model calibration and handling distribution shift between training simulations and real observations, a general challenge relevant far beyond astrophysics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By measuring subhalo density slopes steeper than cold dark matter predictions in real HST observations, the results add to a growing body of evidence that demands careful scrutiny of dark matter models on subgalactic scales.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">With Euclid and Rubin set to deliver thousands of new lens systems, this pipeline is positioned to provide the first statistically powerful population-level constraints on dark matter's small-scale structure; the paper is available at [arXiv:2308.09739](https://arxiv.org/abs/2308.09739).</span></div></div>
</div>
