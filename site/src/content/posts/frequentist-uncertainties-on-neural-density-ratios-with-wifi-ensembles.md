---
abstract: We introduce wifi ensembles as a novel framework to obtain asymptotic frequentist
  uncertainties on density ratios, with a particular focus on neural ratio estimation
  in the context of high-energy physics. When the density ratio of interest is a likelihood
  ratio conditioned on parameters, wifi ensembles can be used to perform simulation-based
  inference on those parameters. After training the basis functions f_i(x), uncertainties
  on the weights w_i can be straightforwardly propagated to the estimated parameters
  without requiring extraneous bootstraps. To demonstrate this approach, we present
  an application in quantum chromodynamics at the Large Hadron Collider, using wifi
  ensembles to estimate the likelihood ratio between generated quark and gluon jets.
  We use this learned likelihood ratio to estimate the quark fraction in a synthetic
  mixed quark/gluon sample, showing that the resultant uncertainties empirically satisfy
  the desired coverage properties.
arxivId: '2506.00113'
arxivUrl: https://arxiv.org/abs/2506.00113
authors:
- Sean Benevedes
- Jesse Thaler
concepts:
- likelihood ratio
- uncertainty quantification
- wifi ensembles
- ensemble methods
- simulation-based inference
- density estimation
- frequentist coverage
- calibration
- collider physics
- jet physics
- hypothesis testing
- classification
figures:
- /iaifi-research-blog/figures/2506_00113/figure_1.png
- /iaifi-research-blog/figures/2506_00113/figure_1.png
- /iaifi-research-blog/figures/2506_00113/figure_2.png
- /iaifi-research-blog/figures/2506_00113/figure_2.png
- /iaifi-research-blog/figures/2506_00113/figure_3.png
- /iaifi-research-blog/figures/2506_00113/figure_3.png
pdfUrl: https://arxiv.org/pdf/2506.00113v2
published: '2025-05-30T18:00:00+00:00'
theme: Experimental Physics
title: Frequentist Uncertainties on Neural Density Ratios with wifi Ensembles
wordCount: 1012
---

## The Big Picture

Imagine you're a detective reconstructing a crime scene. You have two sets of footprints, one from the suspect and one from someone else, but you don't know the exact shoe sizes. You can compare the prints to figure out which footprint probably belongs to whom. But how confident are you? Can you quantify that confidence in a rigorous, statistically honest way?

Physicists at the Large Hadron Collider face the same kind of problem every day. Deep inside the detector, billions of proton collisions spray out cascades of particles called **jets**, and sorting those jets into types (quarks vs. gluons, signal vs. background) requires comparing probability distributions that nobody can write down explicitly.

The standard approach, **density ratio estimation (DRE)**, trains neural networks to approximate the ratio between two distributions. It answers the question: "How much more likely is this particle pattern under one scenario than the other?" But nobody had a principled way to put reliable uncertainty bars on that ratio itself.

Sean Benevedes and Jesse Thaler at MIT's Center for Theoretical Physics have now addressed this problem with a framework they call **wifi ensembles**, a method that produces statistically guaranteed error bars on neural density ratios without expensive repeated retraining.

> **Key Insight:** By modeling a density ratio as a weighted sum of neural network basis functions, wifi ensembles convert unquantifiable model error into quantifiable statistical uncertainty, giving physicists honest error bars on machine-learned quantities for the first time.

## How It Works

Instead of training a single neural network and hoping it's right, wifi ensembles split the job into two stages.

**Stage 1: Train an ensemble of basis functions.** You train several neural networks f₁(x), f₂(x), ..., fₙ(x), each a candidate approximation of the log-density-ratio. Think of these as multiple detectives, each with their own theory of how the footprints differ.

**Stage 2: Fit the weights statistically.** Rather than averaging outputs naively, wifi ensembles introduce scalar weights w₁, w₂, ..., wₙ, one per basis function, fit using the training data:

log r̃(x|w) = Σ wᵢ fᵢ(x)

The wᵢ are treated as **M-estimators**, a class of estimators with well-established mathematical guarantees. From there, the authors derive asymptotic confidence intervals (error bars that provably improve as more data is collected) directly from classical statistics. No retraining. No bootstrapping. Just matrix algebra.

![Figure 1](/iaifi-research-blog/figures/2506_00113/figure_1.png)

Once you have uncertainties on the weights, you propagate them forward. If the density ratio is a likelihood ratio conditioned on some physics parameter (say, the quark fraction in a sample), the **Gong-Samaniego theorem** translates weight uncertainties into parameter uncertainties. The pipeline is computationally cheap.

There's a distinction here worth spelling out: mismodeling vs. uncertainty. Mismodeling is when no set of weights can reproduce the true distribution. It's fundamentally unquantifiable, and more data won't fix it. Uncertainty, on the other hand, shrinks as data grows and can be rigorously bounded. wifi ensembles convert one into the other by design: adding basis functions reduces mismodeling in exchange for a larger but *honest* uncertainty budget.

**Validation.** The team first confirmed the method on a Gaussian example where the true density ratio is known analytically, verifying that confidence intervals achieve correct frequentist coverage (a 68% interval contains the true value 68% of the time).

![Figure 2](/iaifi-research-blog/figures/2506_00113/figure_1.png)

Then came the real test: quark/gluon jet discrimination using QCD simulations. Quark and gluon jets look similar but differ subtly. Gluons spray more particles; quarks are more collimated. The team trained wifi ensembles on simulated jet data, learned the likelihood ratio between jet types, and inferred the quark fraction in a synthetic mixed sample.

![Figure 4](/iaifi-research-blog/figures/2506_00113/figure_2.png)

The inferred fractions matched ground truth, and uncertainty intervals showed proper frequentist coverage across a range of true quark fractions, all without the computationally expensive Neyman construction that traditional bootstrapping requires.

- **Faster:** No retraining needed for uncertainty quantification once basis functions are fixed.
- **Principled:** Uncertainties are asymptotically correct by construction, not empirically tuned.
- **Propagable:** Parameter uncertainties flow naturally from density ratio uncertainties via established theorems.

## Why It Matters

The implications go well beyond quark-gluon sorting. Simulation-based inference (SBI) is now one of the central tools of modern physics, used to measure the strong coupling constant, the top quark mass, and dozens of other fundamental parameters. All of these measurements rest on density ratio estimates. Until now, the uncertainty on the ratio itself was a known blind spot, handled with expensive heuristics or simply ignored.

wifi ensembles fill that hole. By giving physicists a principled, computationally efficient way to put honest error bars on neural density ratios, this work makes the entire SBI pipeline more trustworthy. The framework generalizes to detector unfolding, simulation reweighting, anomaly detection, and any other DRE application.

Open questions remain. The method assumes the model is well-specified, meaning that some combination of basis functions can actually represent the true ratio. Diagnosing violations of that assumption is an active research area. Extending wifi ensembles to handle genuine model misspecification would be a natural next step.

> **Bottom Line:** wifi ensembles give high-energy physicists statistically rigorous, frequentist uncertainty bars on machine-learned density ratios, without the computational cost of bootstrapping, demonstrated on real quark/gluon jet data at the LHC.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work brings together frequentist statistics, M-estimator theory, and neural network ensembles to solve a fundamental uncertainty quantification problem in high-energy physics, connecting ML methodology directly to LHC data analysis.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">wifi ensembles advance uncertainty quantification for neural density ratio estimation by converting unquantifiable model error into statistically rigorous frequentist confidence intervals using the Gong-Samaniego theorem, a new application of classical statistics to deep learning ensembles.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By providing principled uncertainty estimates on learned likelihood ratios, this framework strengthens simulation-based inference for precision measurements of QCD parameters and could improve the reliability of LHC analyses across jet physics and beyond.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend wifi ensembles to handle model misspecification and higher-dimensional parameter estimation, with potential applications across cosmology, neutrino physics, and any field relying on SBI; the paper is available at [arXiv:2506.00113](https://arxiv.org/abs/2506.00113).</span></div></div>
</div>
