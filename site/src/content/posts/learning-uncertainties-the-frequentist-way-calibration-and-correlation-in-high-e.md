---
abstract: Calibration is a common experimental physics problem, whose goal is to infer
  the value and uncertainty of an unobservable quantity Z given a measured quantity
  X. Additionally, one would like to quantify the extent to which X and Z are correlated.
  In this paper, we present a machine learning framework for performing frequentist
  maximum likelihood inference with Gaussian uncertainty estimation, which also quantifies
  the mutual information between the unobservable and measured quantities. This framework
  uses the Donsker-Varadhan representation of the Kullback-Leibler divergence -- parametrized
  with a novel Gaussian Ansatz -- to enable a simultaneous extraction of the maximum
  likelihood values, uncertainties, and mutual information in a single training. We
  demonstrate our framework by extracting jet energy corrections and resolution factors
  from a simulation of the CMS detector at the Large Hadron Collider. By leveraging
  the high-dimensional feature space inside jets, we improve upon the nominal CMS
  jet resolution by upwards of 15%.
arxivId: '2205.03413'
arxivUrl: https://arxiv.org/abs/2205.03413
authors:
- Rikab Gambhir
- Benjamin Nachman
- Jesse Thaler
concepts:
- calibration
- uncertainty quantification
- gaussian ansatz
- mutual information
- likelihood ratio
- jet physics
- collider physics
- event reconstruction
- density estimation
- loss function design
- regression
- feature extraction
figures:
- /iaifi-research-blog/figures/2205_03413/figure_1.png
pdfUrl: https://arxiv.org/pdf/2205.03413v4
published: '2022-05-06T18:00:00+00:00'
theme: Experimental Physics
title: 'Learning Uncertainties the Frequentist Way: Calibration and Correlation in
  High Energy Physics'
wordCount: 995
---

## The Big Picture

Imagine you're trying to figure out how hard it's raining by listening to drops hit a tin roof. The rain itself, the actual intensity, is the truth you can't directly see. The sound is your measurement. Your job is to estimate the rain from the noise, and to know *how confident* you should be in that estimate. This is calibration, one of the most persistent challenges in experimental physics.

At the Large Hadron Collider, physicists face this constantly. When protons smash together at near-light speed, they spray out cascades of particles called **jets**, tightly focused sprays of subatomic particles that leave complex signatures across thousands of detector elements. The true energy of a jet is unobservable; what physicists record is a smeared, distorted signal filtered through layers of electronics and material. Recovering the truth, with real uncertainties and not just best guesses, is essential for every physics result that follows.

A team from MIT and Lawrence Berkeley National Laboratory has built a machine learning framework that solves this problem the right way: extracting calibrated values, their uncertainties, and a precise measure of how much information is actually recoverable, all in a single training run.

> **Key Insight:** By combining the MINE mutual information estimator with a novel "Gaussian Ansatz," this framework performs frequentist calibration that is independent of the training prior and improved CMS jet energy resolution by more than 15%.

## How It Works

The foundation is the **Donsker-Varadhan representation (DVR)**, a mathematical theorem that converts the **Kullback-Leibler (KL) divergence** (a measure of how different two probability distributions are) into something a neural network can directly optimize. When the KL divergence is maximized over a family of test functions, the optimal function encodes the **log-likelihood ratio**: how much more probable the data is under one hypothesis compared to another. This is the key quantity for **frequentist inference**, drawing conclusions directly from the data without assuming prior beliefs about the answer.

This is the core of **MINE** (Mutual Information Neural Estimator). The new idea here is the **Gaussian Ansatz**, an interpretable structure imposed on the neural network. ("Ansatz" is a physicist's term for an educated guess about the mathematical form of a solution.)

- Standard MINE trains a generic network T(x, z) that encodes the log-likelihood in principle, but extracting the maximum or width of that function requires expensive post-hoc optimization.
- The Gaussian Ansatz constrains T(x, z) to the form of a bell curve in z, with mean μ(x) and width σ(x) as direct network outputs.
- The calibrated value and its uncertainty pop out immediately after training. No secondary optimization needed.

The result is a framework that delivers four things at once: a prior-independent maximum likelihood estimate z-hat(x) that doesn't depend on what distribution the training samples were drawn from, a Gaussian resolution σ(x) around that estimate, the log-likelihood ratio for hypothesis testing, and the **mutual information** I(X; Z) between measured and true quantities.

![Figure 1](figure:1)

The team tested this on jet energy calibration at the CMS detector. Rather than relying on the handful of standard jet-level variables used in nominal CMS calibrations, they fed the network the full high-dimensional feature space inside the jet: the detailed structure of **particle flow candidates** (composite particle signals built by combining information from multiple sub-detectors), their energies, positions, and types. The network learned to exploit subtle correlations invisible to simpler methods.

The payoff was concrete. Compared to the official CMS jet energy resolution, the Gaussian Ansatz framework achieved improvements of upward of 15%. In a field where systematic uncertainties dominate many measurements, a 15% resolution improvement can be the difference between seeing a new effect and missing it entirely.

## Why It Matters

The prior-dependence of standard ML regression is a genuine problem in particle physics. When you train a network to regress a quantity, it implicitly learns the distribution of the training samples. If that distribution doesn't match your target dataset, your calibration is wrong in ways that are hard to diagnose. This framework sidesteps the problem entirely by targeting the likelihood function rather than the **posterior** (the Bayesian probability estimate that is sensitive to prior assumptions baked into the simulation), producing results valid regardless of what prior went into the simulation.

The mutual information output is useful in its own right. In the LHC context, knowing the exact information content of a jet measurement tells analysts how much resolution improvement is physically possible, a fundamental limit that separates detector effects from irreducible physics smearing. Mutual information also captures nonlinear relationships that standard linear correlation measures miss entirely.

Any calibration problem in neutrino physics, gravitational wave astronomy, or medical imaging that involves inferring an unobservable quantity from a high-dimensional measurement could benefit from this approach.

> **Bottom Line:** By pairing the MINE mutual information estimator with a physics-motivated Gaussian Ansatz, this framework delivers frequentist calibration with quantified uncertainties in a single training, free of prior dependence and post-hoc optimization, with a 15%+ gain in jet energy resolution at CMS.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects statistical learning theory and experimental particle physics, turning abstract information-theoretic tools (the Donsker-Varadhan representation and mutual information estimation) into a working calibration framework for LHC experiments.

- **Impact on Artificial Intelligence:** The Gaussian Ansatz shows that physics-motivated architectural constraints can produce cleaner, more tractable inference than black-box approaches, offering a principled route to uncertainty quantification in neural networks.

- **Impact on Fundamental Interactions:** Prior-independent jet energy calibration with quantified resolution is directly relevant to precision measurements at the LHC, from Higgs coupling measurements to searches for new particles decaying into jets.

- **Outlook and References:** Future work could extend the Gaussian Ansatz to non-Gaussian likelihoods and higher-dimensional target variables, with applications across neutrino experiments and beyond. The paper is available at [arXiv:2205.03413](https://arxiv.org/abs/2205.03413).
