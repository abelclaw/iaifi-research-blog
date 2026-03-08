---
abstract: Machine learning offers an exciting opportunity to improve the calibration
  of nearly all reconstructed objects in high-energy physics detectors. However, machine
  learning approaches often depend on the spectra of examples used during training,
  an issue known as prior dependence. This is an undesirable property of a calibration,
  which needs to be applicable in a variety of environments. The purpose of this paper
  is to explicitly highlight the prior dependence of some machine learning-based calibration
  strategies. We demonstrate how some recent proposals for both simulation-based and
  data-based calibrations inherit properties of the sample used for training, which
  can result in biases for downstream analyses. In the case of simulation-based calibration,
  we argue that our recently proposed Gaussian Ansatz approach can avoid some of the
  pitfalls of prior dependence, whereas prior-independent data-based calibration remains
  an open problem.
arxivId: '2205.05084'
arxivUrl: https://arxiv.org/abs/2205.05084
authors:
- Rikab Gambhir
- Benjamin Nachman
- Jesse Thaler
concepts:
- calibration
- prior dependence
- jet physics
- collider physics
- gaussian ansatz
- robustness
- uncertainty quantification
- simulation-based inference
- regression
- event reconstruction
- density estimation
- loss function design
figures:
- /iaifi-research-blog/figures/2205_05084/figure_1.png
- /iaifi-research-blog/figures/2205_05084/figure_2.png
- /iaifi-research-blog/figures/2205_05084/figure_3.png
pdfUrl: https://arxiv.org/pdf/2205.05084v2
published: '2022-05-10T18:00:00+00:00'
theme: Experimental Physics
title: Bias and Priors in Machine Learning Calibrations for High Energy Physics
wordCount: 1151
---

## The Big Picture

Imagine you're trying to calibrate a thermometer, but every time you use it in a new environment, it gives slightly wrong readings. Not because it's broken, but because your calibration assumed a fixed temperature range. Deploy it somewhere hotter or colder, and you're off. Now imagine that thermometer costs a billion dollars and lives inside the Large Hadron Collider, the world's most powerful particle accelerator.

That's the challenge facing physicists who use machine learning to calibrate detectors at the LHC. Calibration ensures measurements are "correct on average," so that when you measure the energy of a **jet** (a narrow cone of particles spraying from a proton collision), you're getting the *true* energy, not a detector artifact.

Machine learning has raised hopes of transforming this process. But a new paper from MIT's Jesse Thaler, Rikab Gambhir, and Lawrence Berkeley's Benjamin Nachman sounds a clear warning: many promising ML calibration methods carry a hidden flaw that could corrupt the physics they're meant to protect.

The researchers lay out how **prior dependence**, the tendency of ML models to silently absorb assumptions baked into their training data, can bias calibrations. They argue for a specific approach that sidesteps this trap for one class of calibrations, while honestly flagging a genuine unsolved problem for the other.

> **Key Insight:** A machine learning calibration trained on one distribution of particle energies will give subtly wrong answers when applied to a different distribution, and collecting more data won't fix it.

## How It Works

The experimental pipeline goes roughly like this: particles collide, detectors record the resulting spray, and physicists infer what actually happened. The gap between what the detector records (**detector-level features**) and the underlying truth (**truth-level features**, like actual jet energy) has to be closed by calibration. Get it wrong, and every downstream measurement (Higgs boson properties, new-particle searches) inherits that error.

Two flavors of calibration are at play:

- **Simulation-based calibration** trains on (detector measurement, true value) pairs from detailed physics simulations, learning to map one to the other.
- **Data-based calibration** takes a different goal: it adjusts simulated distributions to match real experimental data, correcting for imperfections in the simulation itself.

![Figure 1](/iaifi-research-blog/figures/2205_05084/figure_1.png)

For simulation-based calibration, the standard approach trains a neural network to minimize **mean squared error (MSE)**, how far predictions stray from true values on average. Minimizing MSE drives the model toward the *conditional average* true value for each detector measurement. The problem: that average depends on the training distribution.

- The model learns *E[truth | detector measurement]* averaged over the **training sample**.
- Deploy it on a **different distribution** and the conditional average shifts, even if the detector's physical response is identical.

This isn't subtle. The paper shows with explicit Gaussian examples that a calibration derived from jets peaking at 100 GeV (gigaelectronvolts, the standard energy unit in particle physics) gives wrong answers on jets peaking at 200 GeV, even when the detector behaves identically at both energies.

![Figure 2](/iaifi-research-blog/figures/2205_05084/figure_2.png)

The authors then ask whether their **Gaussian Ansatz** approach fares better. Rather than learning a single average, this method models the full *shape* of the detector response, fitting it to a bell curve and extracting parameters directly. Because it captures the response shape rather than a sample-averaged statistic, it achieves **prior independence**: the calibration works regardless of what true-energy distribution you feed it. The answer is yes, with important caveats.

The situation for data-based calibration is grimmer. Here the goal is to learn **reweighting functions**, adjustments that upweight or downweight simulated events until the simulation matches real data. Recent ML proposals learn these weights from a specific event sample, but the weights break down on events drawn from different underlying distributions. The paper traces this to the same root cause. No prior-independent data-based calibration method exists yet.

![Figure 3](/iaifi-research-blog/figures/2205_05084/figure_3.png)

The authors ground these findings in a concrete jet energy study using simulated LHC data: train on one energy distribution, test on another. The biases are real and quantifiable. The Gaussian Ansatz substantially outperforms naive MSE-based calibration in the simulation-based case; data-based approaches show persistent prior-induced bias regardless of the ML method used.

## Why It Matters

Calibration is the invisible foundation of every measurement at the LHC. Experiments like ATLAS and CMS calibrate jet energies, muon momenta, electron energies, tau leptons, and heavy-flavor jet identification, and the field has been rushing to replace traditional methods with ML. If those ML methods are inherently prior-dependent, improvements in one context can silently create systematic errors in another. A new-physics search relying on a calibration derived from a control sample with different kinematics could be quietly, systematically wrong.

There is also a genuine theoretical gap here. Prior-independent simulation-based calibration is solvable, and the Gaussian Ansatz offers a practical path forward. Prior-independent data-based calibration (correcting for simulation imperfections across a wide range of physics processes) remains open. The authors are transparent about this precisely so the community can build better methods.

> **Bottom Line:** ML calibrations for particle physics detectors can secretly inherit the biases of their training data, corrupting downstream measurements. The fix exists for simulation-based calibration but remains an unsolved challenge for data-based methods.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies statistical ML theory to a central problem in experimental particle physics, showing how prior dependence (a well-known ML concept) creates concrete, measurable biases in LHC calibrations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper formalizes conditions under which regression-based ML models fail to generalize across distribution shifts, with implications for any scientific ML application where training and deployment distributions differ.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By identifying and partially solving the prior dependence problem in simulation-based jet energy calibration, this work protects the integrity of measurements behind searches for new physics at the LHC.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Prior-independent data-based calibration remains an open challenge the authors hope will motivate new approaches; the full paper is available as [arXiv:2205.05084](https://arxiv.org/abs/2205.05084).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Bias and Priors in Machine Learning Calibrations for High Energy Physics</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2205.05084](https://arxiv.org/abs/2205.05084)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Rikab Gambhir", "Benjamin Nachman", "Jesse Thaler"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Machine learning offers an exciting opportunity to improve the calibration of nearly all reconstructed objects in high-energy physics detectors. However, machine learning approaches often depend on the spectra of examples used during training, an issue known as prior dependence. This is an undesirable property of a calibration, which needs to be applicable in a variety of environments. The purpose of this paper is to explicitly highlight the prior dependence of some machine learning-based calibration strategies. We demonstrate how some recent proposals for both simulation-based and data-based calibrations inherit properties of the sample used for training, which can result in biases for downstream analyses. In the case of simulation-based calibration, we argue that our recently proposed Gaussian Ansatz approach can avoid some of the pitfalls of prior dependence, whereas prior-independent data-based calibration remains an open problem.</span></div></div>
</div>
