---
abstract: Correcting for detector effects in experimental data, particularly through
  unfolding, is critical for enabling precision measurements in high-energy physics.
  However, traditional unfolding methods face challenges in scalability, flexibility,
  and dependence on simulations. We introduce a novel approach to multidimensional
  object-wise unfolding using conditional Denoising Diffusion Probabilistic Models
  (cDDPM). Our method utilizes the cDDPM for a non-iterative, flexible posterior sampling
  approach, incorporating distribution moments as conditioning information, which
  exhibits a strong inductive bias that allows it to generalize to unseen physics
  processes without explicitly assuming the underlying distribution. Our results highlight
  the potential of this method as a step towards a "universal" unfolding tool that
  reduces dependence on truth-level assumptions, while enabling the unfolding of a
  wide range of measured distributions with improved adaptability and accuracy.
arxivId: '2406.01507'
arxivUrl: https://arxiv.org/abs/2406.01507
authors:
- Camila Pazos
- Shuchin Aeron
- Pierre-Hugues Beauchemin
- Vincent Croft
- Zhengyan Huan
- Martin Klassen
- Taritree Wongjirad
concepts:
- diffusion models
- unfolding
- posterior estimation
- inverse problems
- generative models
- distribution moment conditioning
- bayesian inference
- detector simulation
- collider physics
- event reconstruction
- transfer learning
- simulation-based inference
- new physics searches
figures:
- /iaifi-research-blog/figures/2406_01507/figure_1.png
- /iaifi-research-blog/figures/2406_01507/figure_1.png
- /iaifi-research-blog/figures/2406_01507/figure_2.png
- /iaifi-research-blog/figures/2406_01507/figure_2.png
- /iaifi-research-blog/figures/2406_01507/figure_3.png
- /iaifi-research-blog/figures/2406_01507/figure_3.png
pdfUrl: https://arxiv.org/pdf/2406.01507v3
published: '2024-06-03T16:34:50+00:00'
theme: Experimental Physics
title: Towards Universal Unfolding of Detector Effects in High-Energy Physics using
  Denoising Diffusion Probabilistic Models
wordCount: 1175
---

## The Big Picture

Imagine trying to photograph a hummingbird through a dirty, smudged window. The image you capture isn't the real bird; it's the bird *plus* all the distortions introduced by the glass. Your career depends on knowing the bird's true color, wing shape, and position, so you have to undo the window's effect mathematically. That's the situation physicists at the Large Hadron Collider face every time they run an experiment.

When protons smash together at nearly the speed of light, they explode into a spray of smaller particles rushing outward in all directions. Those particles don't reach the detectors cleanly. Every measurement gets blurred, shifted, and distorted by the detector itself: gaps in coverage, errors in energy measurement, and the sheer complexity of instruments that weigh thousands of tons. Mathematically "undoing" these distortions to recover what *actually* happened is called **unfolding**, and it's one of the most statistically tricky problems in experimental physics.

Do it wrong, and your precision measurement isn't precise at all. It's just a very confident mistake.

A team at Tufts University and IAIFI has built a new unfolding tool using **diffusion models**, the same class of AI that recently revolutionized image generation. Their approach doesn't just unfold one process; it can unfold *any* physics process, including ones the model has never seen before.

> **Key Insight:** By training a single diffusion model on diverse particle data and conditioning it on statistical moments of distributions, researchers can unfold detector effects in a way that generalizes to entirely new physics processes, a step toward a truly universal unfolding tool.

## How It Works

Unfolding is a classic **inverse problem**: you have an answer (messy detector data) but need to work backwards to find the question (what actually happened). You observe smeared, detector-level data and want to infer the pristine truth-level particle properties underneath. This requires sampling from a **posterior distribution**, the full probability landscape of what might truly have happened given what you measured.

Traditional methods like iterative Bayesian unfolding tackle this approximately, but they require data sorted into rigid bins, struggle when measuring multiple properties simultaneously, and carry built-in bias toward whatever physics was assumed upfront.

The Tufts team's approach uses a **conditional Denoising Diffusion Probabilistic Model (cDDPM)**. A diffusion model learns to reverse a noise-adding process. Start with pure Gaussian noise, completely random and structureless, and step by step the model strips that noise away to reveal a coherent output. Applied to unfolding, the model learns to reverse the blurring and distortion the detector introduces, producing samples from the posterior distribution of true particle properties.

![Figure 1](figure:1)

The conditioning strategy is where it gets interesting. Rather than conditioning on a fixed assumed physics process, the model takes **statistical moments** (mean, variance, skewness, kurtosis) of the measured data as input. These quantities describe the overall shape of a distribution compactly, without locking the model into any specific underlying physics.

So the model learns a strong **inductive bias** about how detectors systematically distort particles. It understands the *pattern* of distortion, not just what any one kind of collision looks like.

The team trained two variants:

- A **dedicated unfolder** trained for a specific process (W+jets production, collisions producing a W boson alongside jets of particles), which serves as a performance benchmark
- A **generalizable unfolder** trained on a diverse mix of physics processes simultaneously, conditioned only on distribution moments

![Figure 2](figure:2)

By training on multiple processes at once, and never encoding which process it's working on (only the statistical fingerprint of the data), the model develops the ability to unfold distributions from processes it was never explicitly trained on. The team tested this on a synthetic "unknown" process: a mixture of top-quark pair production, W+jets, and leptoquark events. The dedicated unfolder produced biased results. The generalizable unfolder handled it well.

## Why It Matters

The paper benchmarks against the precision that real experiments demand. ATLAS measurements of W+jets **differential cross-sections** (detailed measurements of how often specific particle types are produced at various energies and angles) carry total uncertainties on the order of 10–15%, with a few percent attributable to unfolding. The cDDPM-based generalizable unfolder achieves accuracy within this range.

It does so across key **kinematic observables**: transverse momentum (a particle's sideways kick relative to the beam), pseudorapidity (its forward angle), and azimuthal angle (its orientation around the beam axis).

![Figure 3](figure:3)

This unfolder operates **object-wise**, reconstructing properties of individual particles rather than sorting data into binned histograms. That preserves correlations between kinematic quantities that traditional binned methods fundamentally cannot capture. An electron's transverse momentum and pseudorapidity are correlated; object-wise unfolding keeps those correlations intact, which matters for multi-dimensional measurements.

![Figure 4](figure:4)

The approach is also **non-iterative**. Unlike classical methods that run many convergence cycles, the cDDPM produces posterior samples in a single forward pass, a practical advantage when processing the billions of events a collider experiment accumulates.

There's a bigger picture here, too. The High-Luminosity LHC will produce roughly ten times more collisions per year than the current run, and traditional unfolding methods are already strained. Right now, physicists design a new unfolding procedure for nearly every measurement, a painstaking, expert-intensive process that can take months. A model that generalizes across processes could lower that barrier considerably, freeing physicists to focus on physics rather than statistical plumbing. The method also reduces dependence on the specific Monte Carlo generator used to model the "true" distribution, shrinking a systematic uncertainty that haunts nearly every LHC measurement.

![Figure 5](figure:5)

Open questions remain. What's the right way to condition a generative model on distribution-level information when making event-by-event predictions? How do you ensure generalization to *truly* novel physics (a new particle, for instance) rather than interpolation between known processes? The authors acknowledge this as an open frontier; robustness to genuinely exotic signatures remains to be demonstrated.

> **Bottom Line:** By turning the unfolding problem into a diffusion model's natural habitat, posterior sampling from a noisy process, this Tufts/IAIFI team has built a flexible, generalizable tool that corrects detector distortions without assuming what physics you're looking for. It points toward a future where a single AI system handles unfolding across all of particle physics.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work brings state-of-the-art generative AI from computer vision directly into experimental particle physics, using the same diffusion model architecture behind modern image generators to tackle one of the field's most persistent statistical challenges.
- **Impact on Artificial Intelligence:** The conditioning strategy, using distribution moments as compact summary statistics, enables generative models to generalize across data-generating processes they were never explicitly trained on. This is a broadly applicable technique for domain-robust inference.
- **Impact on Fundamental Interactions:** By reducing systematic bias from prior assumptions and enabling multi-dimensional, object-wise unfolding, this approach improves the fidelity of precision measurements at colliders like the LHC, sharpening tests of the Standard Model and searches for new physics.
- **Outlook and References:** Future work will push toward robustness on genuinely exotic physics signatures and integration with real detector data from experiments like ATLAS; the paper is available at [arXiv:2406.01507](https://arxiv.org/abs/2406.01507).
