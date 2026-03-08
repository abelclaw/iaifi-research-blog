---
abstract: Current and upcoming cosmological surveys will produce unprecedented amounts
  of high-dimensional data, which require complex high-fidelity forward simulations
  to accurately model both physical processes and systematic effects which describe
  the data generation process. However, validating whether our theoretical models
  accurately describe the observed datasets remains a fundamental challenge. An additional
  complexity to this task comes from choosing appropriate representations of the data
  which retain all the relevant cosmological information, while reducing the dimensionality
  of the original dataset. In this work we present a novel framework combining scale-dependent
  neural summary statistics with normalizing flows to detect model misspecification
  in cosmological simulations through Bayesian evidence estimation. By conditioning
  our neural network models for data compression and evidence estimation on the smoothing
  scale, we systematically identify where theoretical models break down in a data-driven
  manner. We demonstrate a first application to our approach using matter and gas
  density fields from three CAMELS simulation suites with different subgrid physics
  implementations.
arxivId: '2508.05744'
arxivUrl: https://arxiv.org/abs/2508.05744
authors:
- Aizhan Akhmetzhanova
- Carolina Cuesta-Lazaro
- Siddharth Mishra-Sharma
concepts:
- normalizing flows
- out-of-distribution detection
- scale-dependent inference
- cosmological simulation
- model validation
- simulation-based inference
- bayesian inference
- density estimation
- anomaly detection
- dimensionality reduction
- likelihood estimation
- dark energy
figures:
- /iaifi-research-blog/figures/2508_05744/figure_1.png
- /iaifi-research-blog/figures/2508_05744/figure_2.png
- /iaifi-research-blog/figures/2508_05744/figure_3.png
pdfUrl: https://arxiv.org/pdf/2508.05744v1
published: '2025-08-07T18:00:09+00:00'
theme: Astrophysics
title: Detecting Model Misspecification in Cosmology with Scale-Dependent Normalizing
  Flows
wordCount: 1270
---

## The Big Picture

Imagine you're a doctor reading an X-ray with a machine trained only on healthy patients. The machine might flag a fracture, or it might confidently declare everything normal because the shadow it sees doesn't match any pattern in its training data.

Now scale that problem up to the entire Universe. Cosmologists build elaborate theoretical models of how matter and energy should be distributed across cosmic scales, run millions of computer simulations, and match those models against galaxy survey observations. But what happens when the model is quietly wrong? Not wrong in an obvious, catastrophic way, but subtly wrong at a specific scale, in a specific regime, due to physics we haven't quite nailed down.

This is the challenge of **model misspecification**: a theoretical framework that looks plausible on the surface but silently fails in some corner of its domain. We already know something is off. The Hubble tension pits early-Universe measurements of the expansion rate against late-Universe ones by a stubborn, statistically significant margin. The DESI collaboration has hinted that dark energy might be evolving over time rather than remaining constant, as Einstein's cosmological constant predicts. Are these genuine cracks in fundamental physics, or symptoms of models that break down at certain scales?

Researchers Aizhan Akhmetzhanova, Carolina Cuesta-Lazaro, and Siddharth Mishra-Sharma have built a framework that goes after this question directly: a scale-dependent, neural-network-driven approach that identifies *where* and *at what spatial scales* theoretical models start to fail, without assuming in advance what the anomaly looks like.

> **Key Insight:** By training a neural network to compress cosmological data at multiple spatial scales and estimating how well a model fits each scale separately, this framework can pinpoint precisely where a theoretical model breaks down, without assuming any particular form for the discrepancy.

## How It Works

The framework has two interlocking pieces, each powered by neural networks, and both made scale-dependent by conditioning on a smoothing parameter.

![Figure 1](/iaifi-research-blog/figures/2508_05744/figure_1.png)

The first piece is a **neural data compressor**: a network that takes a high-dimensional cosmological field (a 3D density map of matter across a slice of the Universe, with millions of pixels) and squeezes it into a compact set of numbers called **neural summary statistics**. Raw cosmological fields are far too high-dimensional for direct statistical tests, so this compression step is essential. The compressor is trained to be maximally informative about cosmological parameters, ensuring no relevant information gets thrown away.

The second piece is a **normalizing flow**, a generative model that learns to estimate probability distributions. Here it calculates the **Bayesian model evidence**: a single number quantifying how well a theoretical model explains an observation, averaged across all plausible parameter values. High evidence means the model fits. Low evidence signals a problem.

What sets the approach apart is scale conditioning. Both the compressor and the flow receive an additional input: a smoothing scale σ. By blurring fields at different scales before training, the framework produces a *curve* of evidence values as a function of scale, not just a single number. If a model fits at large scales but fails at small ones, the evidence plummets as σ decreases. That drop-off is a precise, data-driven fingerprint of where the physics goes wrong.

The training procedure:
1. Draw simulated cosmological fields from a baseline simulation suite
2. Smooth each field at a randomly sampled scale σ
3. Train the neural compressor to extract summary statistics sensitive to cosmological parameters
4. Train the normalizing flow to estimate evidence, conditioned on the same σ
5. At test time, feed in a field from a *different* simulation and watch how the evidence curve deviates

## Why It Matters

The team tested their framework using the **CAMELS** (Cosmology and Astrophysics with Machine Learning Simulations) suite, a dataset of thousands of simulations run with different **subgrid physics** implementations. Subgrid physics captures processes below simulation resolution: star formation, supernova feedback, black hole heating. Different simulation codes (IllustrisTNG, SIMBA, Astrid) make different assumptions about these processes, producing subtly different density fields even with identical cosmological parameters.

![Figure 2](/iaifi-research-blog/figures/2508_05744/figure_2.png)

Treating one simulation suite as the baseline and another as "observed" data, the scale-dependent evidence curves told a clear story. At large spatial scales, where gravity dominates and **baryonic feedback** (the way exploding stars and growing black holes push and heat surrounding gas) is relatively weak, different suites looked statistically consistent. As the smoothing scale decreased and finer structure came into view, evidence dropped sharply. Small scales are where the model breaks down.

![Figure 3](/iaifi-research-blog/figures/2508_05744/figure_3.png)

Gas density fields, more sensitive to baryonic physics than matter density, showed this breakdown at larger scales, exactly as physical intuition predicts.

This matters for next-generation surveys. Instruments like Euclid and the Vera Rubin Observatory's LSST will map large-scale structure with extraordinary precision, probing scales where baryonic physics complicates theoretical predictions. The standard approach is either to avoid small scales entirely (discarding information) or to apply uncertain corrections (risking hidden biases). A method that diagnoses exactly where a model fails gives cosmologists a principled way to know where they can trust their inferences.

The framework also fills a gap in **simulation-based inference**, the practice of comparing thousands of simulations statistically against real observations rather than solving equations analytically. Traditional goodness-of-fit tools like the χ² statistic assume Gaussian errors and linear relationships, assumptions that fall apart in modern cosmological analyses. Bayesian evidence estimated from learned neural summaries is far more flexible.

> **Bottom Line:** This scale-dependent normalizing flow framework gives cosmologists a new diagnostic tool, one that automatically identifies at which spatial scales a theoretical model fails and enables more reliable inference from next-generation cosmic surveys.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work brings together machine learning (normalizing flows and neural data compression) with cosmological forward modeling to create a diagnostic tool that neither field could have produced alone, a direct expression of IAIFI's mission.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The scale-conditioning strategy for simultaneously training neural density estimators and summary statistic networks across multiple spatial scales offers a broadly applicable template for out-of-distribution detection wherever data has natural multiscale structure.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By providing a model-agnostic way to detect misspecification in cosmological simulations, this framework could help distinguish genuine new physics, such as evolving dark energy or modified gravity, from artifacts of poorly modeled baryonic processes at small scales.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could apply this framework to observed galaxy survey data and weak lensing maps, potentially clarifying current cosmological tensions. The full methodology and results are available at [arXiv:2508.05744](https://arxiv.org/abs/2508.05744).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Detecting Model Misspecification in Cosmology with Scale-Dependent Normalizing Flows</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2508.05744</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Aizhan Akhmetzhanova", "Carolina Cuesta-Lazaro", "Siddharth Mishra-Sharma"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Current and upcoming cosmological surveys will produce unprecedented amounts of high-dimensional data, which require complex high-fidelity forward simulations to accurately model both physical processes and systematic effects which describe the data generation process. However, validating whether our theoretical models accurately describe the observed datasets remains a fundamental challenge. An additional complexity to this task comes from choosing appropriate representations of the data which retain all the relevant cosmological information, while reducing the dimensionality of the original dataset. In this work we present a novel framework combining scale-dependent neural summary statistics with normalizing flows to detect model misspecification in cosmological simulations through Bayesian evidence estimation. By conditioning our neural network models for data compression and evidence estimation on the smoothing scale, we systematically identify where theoretical models break down in a data-driven manner. We demonstrate a first application to our approach using matter and gas density fields from three CAMELS simulation suites with different subgrid physics implementations.</span></div></div>
</div>
