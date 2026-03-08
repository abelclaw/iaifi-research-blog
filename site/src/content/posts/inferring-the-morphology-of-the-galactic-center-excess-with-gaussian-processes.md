---
abstract: Descriptions of the Galactic Center using Fermi gamma-ray data have so far
  modeled the Galactic Center Excess (GCE) as a template with fixed spatial morphology
  or as a linear combination of such templates. Although these templates are informed
  by various physical expectations, the morphology of the excess is a priori unknown.
  For the first time, we describe the GCE using a flexible, non-parametric machine
  learning model -- the Gaussian process (GP). We assess our model's performance on
  synthetic data, demonstrating that the model can recover the templates used to generate
  the data. We then fit the \Fermi data with our model in a single energy bin from
  2-20 GeV (leaving a spectral GP analysis of the GCE for future work) using a variety
  of template models of diffuse gamma-ray emission to quantify our fits' systematic
  uncertainties associated with diffuse emission modeling. We interpret our best-fit
  GP in terms of GCE templates consisting of an NFW squared template and a bulge component
  to determine which bulge models can best describe the fitted GP and to what extent
  the best-fit GP is described better by an NFW squared template versus a bulge template.
  The best-fit GP contains morphological features that are typically not associated
  with traditional GCE studies. These include a localized bright source at around
  $(\ell,b) = (20^{\circ}, 0^{\circ})$ and a diagonal arm extending Northwest from
  the Galactic Center. In spite of these novel features, the fitted GP is explained
  best by a template-based model consisting of the bulge presented in Coleman et al.
  (2020) and a squared NFW component. Our results suggest that the physical interpretation
  of the GCE in terms of stellar bulge and NFW-like components is highly sensitive
  to the assumed morphologies, background models, and the region of the sky used for
  inference.
arxivId: '2410.21367'
arxivUrl: https://arxiv.org/abs/2410.21367
authors:
- Edward D. Ramirez
- Yitian Sun
- Matthew R. Buckley
- Siddharth Mishra-Sharma
- Tracy R. Slatyer
concepts:
- stochastic processes
- galactic center excess
- bayesian inference
- posterior estimation
- dark matter
- uncertainty quantification
- sparse variational inference
- kernel methods
- scalability
- signal detection
- nfw profile
- model validation
- inverse problems
figures:
- /iaifi-research-blog/figures/2410_21367/figure_1.png
- /iaifi-research-blog/figures/2410_21367/figure_1.png
- /iaifi-research-blog/figures/2410_21367/figure_2.png
pdfUrl: https://arxiv.org/pdf/2410.21367v1
published: '2024-10-28T18:00:00+00:00'
theme: Astrophysics
title: Inferring the Morphology of the Galactic Center Excess with Gaussian Processes
wordCount: 1415
---

## The Big Picture

Imagine trying to identify a faint glow hidden inside a fireworks display. That's roughly the challenge astronomers face when studying the heart of our galaxy. The Milky Way's center blazes with gamma rays produced by cosmic rays slamming into gas clouds, remnants of exploded stars, and thousands of compact objects. Buried in that chaos is an extra glow that nobody fully understands.

Since 2009, scientists analyzing data from NASA's *Fermi* gamma-ray space telescope have noticed an unexplained surplus of gamma rays from the Galactic Center, known as the **Galactic Center Excess (GCE)**. It's not subtle: by some estimates, it accounts for roughly 10% of all gamma-ray light from the inner galaxy outside the flat disk of the Milky Way.

Two explanations have battled for dominance. One says dark matter particles are annihilating each other, consistent with a particle about 100 times the mass of a proton and with properties that theory predicts for dark matter left over from the early universe. The other says millions of rapidly spinning dead stars called **millisecond pulsars (MSPs)**, individually too faint to resolve, are collectively producing that telltale glow.

The catch? Answering this question requires knowing the *shape* of the excess, and every analysis so far has assumed that shape rather than measured it freely.

A team from Rutgers, McGill, MIT, and Harvard's IAIFI took a different approach: instead of assuming a fixed shape, they let the data speak for itself. Their tool is a **Gaussian process**, a machine learning technique that maps the structure of the GCE with minimal built-in assumptions about what the answer should look like.

> **Key Insight:** By replacing fixed morphological templates with a flexible Gaussian process model, the researchers found unexpected structural features in the Galactic Center Excess and showed that the physical interpretation of the excess depends far more on modeling assumptions than previously appreciated.

## How It Works

The standard approach works like a paint-by-numbers kit. Astronomers construct **templates** (spatial maps predicting where different gamma-ray sources should be) and fit those templates to *Fermi* data. The GCE template is usually an **NFW-squared profile**, the expected shape from dark matter annihilation, or a **bulge template** tracing old stars near the galactic center. Both approaches bake in an assumption about the answer before the analysis begins.

The Gaussian process approach is different in kind. A GP is a **non-parametric probabilistic model**: it can take any shape, is locked into no specific form, and encodes only smoothness assumptions. Think of it as handing an artist a photograph and asking them to paint what they see, rather than asking them to trace a pre-drawn outline. The GP assigns flux values to every pixel and allows them to vary continuously, constrained only by the expectation that nearby pixels should have similar values.

![Figure 1](/iaifi-research-blog/figures/2410_21367/figure_1.png)

Fitting a GP to sky maps with thousands of pixels is computationally brutal. The team made it tractable with two techniques:

- **Stochastic variational inference (SVI):** Recasts Bayesian inference (normally a slow statistical search over possible solutions) as an optimization problem, making it practical where traditional Markov Chain Monte Carlo sampling would be hopelessly slow.
- **Sparse GP approximations:** Uses a smaller set of "inducing points" to represent the full spatial field, scaling computation to the ~10³ spatial bins in the region of interest.

The analysis covered a 20-degree circle around the Galactic Center in a single energy bin from 2–20 GeV, with an outer annulus (30–40 degrees) used to calibrate background templates without GCE contamination.

Before touching real data, the team validated their method on synthetic datasets. Fake gamma-ray skies generated from known templates confirmed that the GP could recover the input morphologies. The method proved stable across different kernel functions, numbers of inducing points, and GCE assumptions. A final stress test checked robustness to deliberately mismodeled diffuse emission, since background mismodeling is the field's perennial nemesis.

![Figure 2](/iaifi-research-blog/figures/2410_21367/figure_1.png)

Once validated, they fit the model to actual *Fermi* data using multiple independent diffuse emission models to quantify systematic uncertainty. This step is essential given how strongly conclusions in this field depend on background assumptions.

## Why It Matters

The best-fit GP does not look like a clean NFW-squared distribution. It contains two unexpected features: a localized bright source near galactic coordinates (ℓ, b) = (20°, 0°), and a diagonal arm extending northwest from the Galactic Center. Neither structure appears in standard GCE analyses.

Whether they represent real astrophysical sources, artifacts of background mismodeling, or something stranger remains an open question.

![Figure 3](/iaifi-research-blog/figures/2410_21367/figure_2.png)

When the team decomposed their best-fit GP into familiar template components, the winner was a combination of the **Coleman et al. (2020) stellar bulge template** plus an NFW-squared component. Not purely dark matter, and not purely MSPs. This hints at a baryonic (stellar) contribution to the GCE. But the sensitivity of this conclusion to background model choice and sky region means the dark matter interpretation cannot be ruled out.

The implications go beyond the GCE debate itself. Flexible ML models can be embedded directly into gamma-ray likelihood analyses at scale, opening a path toward template-free morphological inference in astrophysics more broadly. The authors point to a full spectral GP analysis as the natural next step: simultaneous fitting across energy bins could break remaining degeneracies between the GCE and background components.


> **Bottom Line:** The first Gaussian process analysis of the Galactic Center Excess reveals unexpected structure and shows that the dark-matter-vs-pulsars debate depends on modeling choices more than anyone realized.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work uses Gaussian processes with stochastic variational inference as the core analysis engine for a fundamental physics question, showing how AI methods can replace rigid physical assumptions with data-driven flexibility in gamma-ray astrophysics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper advances scalable probabilistic inference for spatial fields. Sparse variational GP approximations, it turns out, can be reliably applied to astronomical sky maps with thousands of pixels while maintaining calibrated uncertainty quantification.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By mapping the GCE morphology without fixed templates, the analysis reveals that interpreting the excess as dark matter annihilation or stellar emission is far more sensitive to background model choices and sky region than previous studies acknowledged, changing how the community should approach this long-standing puzzle.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend this GP framework to a full spectral analysis across energy bins, potentially providing sharper discrimination between dark matter and astrophysical explanations; the paper is available at [arXiv:2410.21367](https://arxiv.org/abs/2410.21367) with code at github.com/edwarddramirez/gce-gp.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Inferring the Morphology of the Galactic Center Excess with Gaussian Processes</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2410.21367](https://arxiv.org/abs/2410.21367)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">Edward D. Ramirez, Yitian Sun, Matthew R. Buckley, Siddharth Mishra-Sharma, Tracy R. Slatyer</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Descriptions of the Galactic Center using Fermi gamma-ray data have so far modeled the Galactic Center Excess (GCE) as a template with fixed spatial morphology or as a linear combination of such templates. Although these templates are informed by various physical expectations, the morphology of the excess is a priori unknown. For the first time, we describe the GCE using a flexible, non-parametric machine learning model -- the Gaussian process (GP). We assess our model's performance on synthetic data, demonstrating that the model can recover the templates used to generate the data. We then fit the Fermi data with our model in a single energy bin from 2-20 GeV (leaving a spectral GP analysis of the GCE for future work) using a variety of template models of diffuse gamma-ray emission to quantify our fits' systematic uncertainties associated with diffuse emission modeling. We interpret our best-fit GP in terms of GCE templates consisting of an NFW squared template and a bulge component to determine which bulge models can best describe the fitted GP and to what extent the best-fit GP is described better by an NFW squared template versus a bulge template. The best-fit GP contains morphological features that are typically not associated with traditional GCE studies. These include a localized bright source at around (ℓ,b) = (20°, 0°) and a diagonal arm extending Northwest from the Galactic Center. In spite of these novel features, the fitted GP is explained best by a template-based model consisting of the bulge presented in Coleman et al. (2020) and a squared NFW component. Our results suggest that the physical interpretation of the GCE in terms of stellar bulge and NFW-like components is highly sensitive to the assumed morphologies, background models, and the region of the sky used for inference.</span></div></div>
</div>
