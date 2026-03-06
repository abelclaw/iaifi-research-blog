---
abstract: When analyzing real-world data it is common to work with event ensembles,
  which comprise sets of observations that collectively constrain the parameters of
  an underlying model of interest. Such models often have a hierarchical structure,
  where "local" parameters impact individual events and "global" parameters influence
  the entire dataset. We introduce practical approaches for frequentist and Bayesian
  dataset-wide probabilistic inference in cases where the likelihood is intractable,
  but simulations can be realized via a hierarchical forward model. We construct neural
  estimators for the likelihood(-ratio) or posterior and show that explicitly accounting
  for the model's hierarchical structure can lead to significantly tighter parameter
  constraints. We ground our discussion using case studies from the physical sciences,
  focusing on examples from particle physics and cosmology.
arxivId: '2306.12584'
arxivUrl: https://arxiv.org/abs/2306.12584
authors:
- Lukas Heinrich
- Siddharth Mishra-Sharma
- Chris Pollard
- Philipp Windischhofer
concepts:
- simulation-based inference
- hierarchical forward model
- posterior estimation
- likelihood ratio
- bayesian inference
- event ensemble learning
- normalizing flows
- density estimation
- attention mechanisms
- uncertainty quantification
- collider physics
- dark matter
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2306_12584/figure_1.png
- /iaifi-research-blog/figures/2306_12584/figure_2.png
- /iaifi-research-blog/figures/2306_12584/figure_3.png
pdfUrl: https://arxiv.org/pdf/2306.12584v2
published: '2023-06-21T21:50:42+00:00'
theme: Theoretical Physics
title: Hierarchical Neural Simulation-Based Inference Over Event Ensembles
wordCount: 1094
---

## The Big Picture

Imagine you're a detective trying to identify a suspect, but you're only allowed to interview witnesses one at a time — and you can't compare notes. You'd get clues, but you'd miss the pattern that emerges when all the testimony is viewed together: the consistency that confirms a story, or the contradiction that blows it apart. Now imagine the crime scene is a particle collider, the witnesses are individual collision events, and the suspect is a fundamental parameter of the universe. That's the situation physicists face every day — and a new set of machine learning methods is finally letting scientists compare notes.

Scientists analyzing particle physics data or astronomical observations routinely work with **event ensembles** — large collections of individual measurements that, taken together, constrain some underlying physical model. These models have a layered structure: some parameters are "global," shaping every event in a dataset, while others are "local," relevant only to a single measurement. Traditional approaches often treat each event in isolation before combining results, a shortcut that can severely underestimate the power of the full dataset.

Compounding the challenge, the **likelihood functions** physicists use to calculate how probable a dataset is under a given theory are often impossible to compute exactly for complex simulations. You can run the simulation and observe the output, but you can't write down its probability in closed form.

Researchers from TU Munich, MIT, IAIFI, and the University of Chicago have built a practical framework for doing this inference properly — using neural networks that explicitly respect the model's layered structure to extract dramatically tighter parameter constraints.

> **Key Insight:** By training neural networks on entire event ensembles while explicitly respecting the hierarchical structure of the underlying physics model, the authors achieve dramatically tighter parameter constraints than methods that analyze events one by one.

## How It Works

The core challenge is **simulation-based inference (SBI)**: a paradigm for learning about a model when you can run simulations but can't compute exact probabilities. Traditional SBI trains a neural network to estimate likelihoods from single observations. The problem? Real physics datasets don't come as isolated points — they come as ensembles of many events, jointly constrained by the same global parameters.

The authors formalize the layered structure mathematically. Every dataset is governed by global parameters *θ* — things like a particle interaction cross-section or dark matter mass — and per-event local parameters *z_i*, specific to each individual measurement. A naive approach handles local parameters one event at a time, then multiplies the results. The authors prove this is only valid under specific conditions, and that violating them leads to systematically wrong or miscalibrated results.

![Figure 1](/iaifi-research-blog/figures/2306_12584/figure_1.png)

Their solution comes in two flavors:

- **Frequentist approach:** They build a neural network that directly estimates the **profile likelihood ratio** — a score comparing how well two competing hypotheses explain the full dataset, after optimizing over unknown nuisance parameters — across an entire ensemble at once. This is the first end-to-end frequentist SBI method designed specifically for hierarchical set-valued data.
- **Bayesian approach:** They train networks to estimate the full **posterior distribution** — a probability map showing which parameter values are most consistent with the observed data — over global parameters, given a whole set of events simultaneously. The network sees *sets* of observations as input, not individual points.

To handle sets of variable size, the architecture uses **permutation-invariant networks**: models that treat an unordered collection of inputs the same regardless of how you shuffle them. The network aggregates information across events using learned summary statistics, then maps that aggregate to a parameter estimate.

![Figure 2](/iaifi-research-blog/figures/2306_12584/figure_2.png)

The team validates these methods across three progressively complex case studies. First, a toy Gaussian mixture model where the correct answer is known analytically. Then a particle physics scenario involving a **marked Poisson process** — a collider model where the number of events itself carries information about a signal rate. Finally, the hardest test: **strong gravitational lensing**, where telescope images of galaxies distorted by a foreground mass must be analyzed to infer properties of that mass.

Each case study confirms the same pattern: hierarchy-aware inference produces substantially tighter, better-calibrated constraints than naive event-by-event combination.

![Figure 3](/iaifi-research-blog/figures/2306_12584/figure_3.png)

In the gravitational lensing application, the hierarchical approach yields posterior distributions that are meaningfully narrower — translating directly into better science per photon collected. The method is also substantially faster than **Markov Chain Monte Carlo** sampling — a standard but computationally intensive technique for exploring complex probability spaces — even when the likelihood is tractable. It also enables a compelling bonus: **streaming inference**, where the posterior updates in real time as new observations arrive, without reanalyzing old data.

## Why It Matters

Physics has always demanded rigorous statistical inference under complex models; machine learning has recently provided powerful tools for approximating intractable functions. But the real gains come from marrying these two properly — not just attaching a neural network to an existing pipeline, but redesigning inference to respect the model's actual structure.

The implications extend well beyond particle physics and cosmology. Any domain with layered data-generating processes — population genetics, epidemiology, exoplanet surveys, gravitational wave astronomy — could benefit from the same approach. As simulation-based inference matures, the principle here will likely become standard practice: learn from ensembles as ensembles, not as collections of individuals.

Open questions remain, particularly around scaling to truly enormous datasets and handling cases where the layered structure is itself uncertain or misspecified. But the foundation is now solid.

> **Bottom Line:** By building neural estimators that treat entire event ensembles as first-class inputs and explicitly exploit hierarchical model structure, this work delivers significantly tighter physics constraints — faster than MCMC and without requiring a tractable likelihood.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges modern machine learning — specifically permutation-invariant neural networks and amortized inference — with the statistical needs of large-scale physics experiments, demonstrating the power of AI tools designed with physics structure in mind.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces the first end-to-end frequentist simulation-based inference method for hierarchical set-valued data, advancing the SBI literature with architectures that generalize to variable-cardinality inputs and enable real-time streaming posterior updates.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling tighter, properly calibrated parameter constraints from particle collider data and gravitational lensing images, the methods directly improve the sensitivity of searches for new physics and dark matter signatures.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include scaling to higher-dimensional parameter spaces and datasets from next-generation experiments like the Vera Rubin Observatory; the full methodology is available at arXiv:2306.05676.</span></div></div>
</div>
