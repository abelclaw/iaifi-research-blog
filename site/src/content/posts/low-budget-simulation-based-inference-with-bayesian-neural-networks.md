---
abstract: Simulation-based inference methods have been shown to be inaccurate in the
  data-poor regime, when training simulations are limited or expensive. Under these
  circumstances, the inference network is particularly prone to overfitting, and using
  it without accounting for the computational uncertainty arising from the lack of
  identifiability of the network weights can lead to unreliable results. To address
  this issue, we propose using Bayesian neural networks in low-budget simulation-based
  inference, thereby explicitly accounting for the computational uncertainty of the
  posterior approximation. We design a family of Bayesian neural network priors that
  are tailored for inference and show that they lead to well-calibrated posteriors
  on tested benchmarks, even when as few as $O(10)$ simulations are available. This
  opens up the possibility of performing reliable simulation-based inference using
  very expensive simulators, as we demonstrate on a problem from the field of cosmology
  where single simulations are computationally expensive. We show that Bayesian neural
  networks produce informative and well-calibrated posterior estimates with only a
  few hundred simulations.
arxivId: '2408.15136'
arxivUrl: https://arxiv.org/abs/2408.15136
authors:
- Arnaud Delaunoy
- Maxence de la Brassinne Bonardeaux
- Siddharth Mishra-Sharma
- Gilles Louppe
concepts:
- simulation-based inference
- bayesian inference
- uncertainty quantification
- calibration
- posterior estimation
- bnn weight priors
- epistemic uncertainty
- density estimation
- monte carlo methods
- ensemble methods
- cosmological simulation
- model validation
figures:
- /iaifi-research-blog/figures/2408_15136/figure_1.png
- /iaifi-research-blog/figures/2408_15136/figure_2.png
- /iaifi-research-blog/figures/2408_15136/figure_3.png
pdfUrl: https://arxiv.org/pdf/2408.15136v1
published: '2024-08-27T15:19:07+00:00'
theme: Foundational AI
title: Low-Budget Simulation-Based Inference with Bayesian Neural Networks
wordCount: 1036
---

## The Big Picture

Imagine solving a cosmic puzzle with only a handful of clues. A detective with ten clues might crack the case, or might jump to a wildly wrong conclusion if those clues happen to be misleading. In science, this problem is everywhere: you have an expensive computer simulation of how dark matter clusters in the universe, you can only afford to run it a few dozen times, and you need to extract reliable conclusions from those precious runs. Getting it wrong isn't just wasteful. It can seed false discoveries that ripple through the field.

This is the challenge of **simulation-based inference (SBI)**, a family of methods that uses machine learning to learn the relationship between simulation inputs (physical parameters) and outputs (observed data). Standard SBI trains a neural network on thousands of simulation runs to approximate a **posterior distribution**, a probability map showing which physical settings best explain your observation and how confident we should be in each answer.

The problem: when simulations are scarce, the neural network has too little to go on. Many different internal configurations (think of these as different "theories" the network could hold about how the world works) fit the limited training data equally well, yet each makes different predictions on new observations. The network becomes confident not because it's right, but because it doesn't know what it doesn't know.

Researchers at the University of Liège and MIT's IAIFI have a principled fix: equip the neural network with uncertainty about its own internal settings, and design that uncertainty carefully from the start.

> **Key Insight:** By treating neural network weights as probability distributions rather than fixed numbers, and designing those distributions specifically for the inference task, Bayesian neural networks can deliver reliable, well-calibrated posteriors even when only a handful of simulations are available.

## How It Works

The idea builds on **Bayesian deep learning**, a framework that replaces the usual single "best-fit" set of network weights with a full probability distribution over all plausible weight configurations. Instead of asking "what are the right weights?", a **Bayesian neural network (BNN)** asks "given our data, how confident are we about any particular set of weights?" When making predictions, it averages over all plausible networks, a procedure called **Bayesian model averaging**, rather than committing to just one.

![Figure 1](figure:1)

The ingredient that makes this work, and where the paper makes its main contribution, is the **prior** over neural network weights. A prior encodes beliefs about the weights before seeing any training data. Most BNN applications use vague, generic priors: Gaussians centered at zero, chosen for mathematical convenience. But this choice matters enormously when data is limited.

With very few simulations, the prior dominates the posterior over weights. A prior that conveys the wrong beliefs will produce a miscalibrated inference network from the start.

The team's solution is to design priors *tailored for inference*. They construct priors that enforce a specific desirable property: when no training data is available, the network outputs a **uniform (flat) distribution** over parameters, the most honest and conservative answer possible. As training data accumulates, the network smoothly updates toward more informative posteriors.

This behavior is baked into the prior itself, not enforced by post-hoc correction. The authors build a family of such priors and analyze their properties both theoretically and empirically across a suite of benchmarks.

What do they find?

- With as few as **O(10) simulations**, the BNN with tailored priors produces well-calibrated posteriors on standard benchmarks
- Standard neural SBI methods produce overconfident posteriors at the same simulation budgets; they think they know more than they do
- Ensemble methods (training many independent networks and averaging) help somewhat, but BNNs with principled priors beat them, especially in the most extreme low-data regime

## Why It Matters

![Figure 2](figure:2)

The cosmology application makes the stakes concrete. A single simulation of large-scale structure, modeling how galaxies and dark matter are distributed across the cosmos, can require substantial compute. Running thousands of such simulations to train a standard inference network isn't practical. Running a few hundred might be feasible. The authors show their BNN approach produces informative, well-calibrated posterior estimates of cosmological parameters with only a few hundred simulations.

The work also matters for how the field handles uncertainty in machine learning-based science more broadly. The distinction between **aleatoric uncertainty** (genuine randomness in the data) and **epistemic uncertainty** (ignorance due to limited training data) is often glossed over in applied ML. In scientific inference, where the goal is to make reliable claims about nature, conflating the two can be catastrophic. The BNN framework here offers a template for handling epistemic uncertainty honestly, not just in cosmology but wherever simulations are expensive: particle physics, climate modeling, drug discovery, materials science.

![Figure 3](figure:3)

Open questions remain. Sampling from a BNN's weight posterior costs more than training a standard network, and scaling these methods to very high-dimensional parameter spaces is an active area of research. Optimal prior design for different problem structures also needs more work. But the core point holds: acknowledging what a network doesn't know is just as important as what it does know.

> **Bottom Line:** Bayesian neural networks with inference-tailored priors can perform reliable simulation-based inference with as few as ten simulations, making rigorous scientific inference feasible for problems where running the simulator is genuinely expensive.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects Bayesian statistics, deep learning theory, and observational cosmology, developing principled ML tools motivated by and validated on real problems in fundamental physics.

- **Impact on Artificial Intelligence:** The paper provides a theoretically grounded framework for designing BNN priors that enforce calibration by construction, advancing uncertainty quantification in neural density estimation.

- **Impact on Fundamental Interactions:** By enabling reliable inference with only hundreds of cosmological simulations, this method makes Bayesian parameter estimation tractable for computationally expensive simulators of large-scale structure and other physical systems.

- **Outlook and References:** Future work includes scaling to higher-dimensional problems and more complex simulators. The paper is available at [arXiv:2408.15136](https://arxiv.org/abs/2408.15136) and code is open-sourced at github.com/ADelau/low_budget_sbi_with_bnn.

## Original Paper Details
- **Title:** Low-Budget Simulation-Based Inference with Bayesian Neural Networks
- **arXiv ID:** 2408.15136
- **Authors:** ["Arnaud Delaunoy", "Maxence de la Brassinne Bonardeaux", "Siddharth Mishra-Sharma", "Gilles Louppe"]
- **Abstract:** Simulation-based inference methods have been shown to be inaccurate in the data-poor regime, when training simulations are limited or expensive. Under these circumstances, the inference network is particularly prone to overfitting, and using it without accounting for the computational uncertainty arising from the lack of identifiability of the network weights can lead to unreliable results. To address this issue, we propose using Bayesian neural networks in low-budget simulation-based inference, thereby explicitly accounting for the computational uncertainty of the posterior approximation. We design a family of Bayesian neural network priors that are tailored for inference and show that they lead to well-calibrated posteriors on tested benchmarks, even when as few as $O(10)$ simulations are available. This opens up the possibility of performing reliable simulation-based inference using very expensive simulators, as we demonstrate on a problem from the field of cosmology where single simulations are computationally expensive. We show that Bayesian neural networks produce informative and well-calibrated posterior estimates with only a few hundred simulations.
