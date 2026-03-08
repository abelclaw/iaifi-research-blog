---
abstract: We introduce a new multivariate statistical problem that we refer to as
  the Ensemble Inverse Problem (EIP). The aim of EIP is to invert for an ensemble
  that is distributed according to the pushforward of a prior under a forward process.
  In high energy physics (HEP), this is related to a widely known problem called unfolding,
  which aims to reconstruct the true physics distribution of quantities, such as momentum
  and angle, from measurements that are distorted by detector effects. In recent applications,
  the EIP also arises in full waveform inversion (FWI) and inverse imaging with unknown
  priors. We propose non-iterative inference-time methods that construct posterior
  samplers based on a new class of conditional generative models, which we call ensemble
  inverse generative models. For the posterior modeling, these models additionally
  use the ensemble information contained in the observation set on top of single measurements.
  Unlike existing methods, our proposed methods avoid explicit and iterative use of
  the forward model at inference time via training across several sets of truth-observation
  pairs that are consistent with the same forward model, but originate from a wide
  range of priors. We demonstrate that this training procedure implicitly encodes
  the likelihood model. The use of ensemble information helps posterior inference
  and enables generalization to unseen priors. We benchmark the proposed method on
  several synthetic and real datasets in inverse imaging, HEP, and FWI. The codes
  are available at https://github.com/ZhengyanHuan/The-Ensemble-Inverse-Problem--Applications-and-Methods.
arxivId: '2601.22029'
arxivUrl: https://arxiv.org/abs/2601.22029
authors:
- Zhengyan Huan
- Camila Pazos
- Martin Klassen
- Vincent Croft
- Pierre-Hugues Beauchemin
- Shuchin Aeron
concepts:
- inverse problems
- generative models
- ensemble inverse learning
- posterior estimation
- unfolding
- simulation-based inference
- bayesian inference
- normalizing flows
- collider physics
- diffusion models
- density estimation
- full waveform inversion
figures:
- /iaifi-research-blog/figures/2601_22029/figure_1.png
- /iaifi-research-blog/figures/2601_22029/figure_2.png
- /iaifi-research-blog/figures/2601_22029/figure_3.png
pdfUrl: https://arxiv.org/pdf/2601.22029v1
published: '2026-01-29T17:34:41+00:00'
theme: Foundational AI
title: 'The Ensemble Inverse Problem: Applications and Methods'
wordCount: 1004
---

## The Big Picture

Imagine trying to reconstruct a signal from a broken radio transmission. You have the crackling, distorted output — but the radio itself is a black box. You can't peer inside it, can't run it backwards, and you only get one shot at each transmission.

Now imagine the "radio" is a multi-billion-dollar particle detector, and the "signals" are fundamental particles colliding at nearly the speed of light.

This is the daily reality of physicists at colliders like the LHC. Detectors smear, blur, and corrupt the true physics. To learn what actually happened in a collision — what particles' true speeds and angles were — physicists must *undo* the detector's distortions. The same mathematical challenge appears in earthquake seismology and medical imaging. All three fields have developed their own solutions, often in isolation, each requiring expensive repeated simulations of the very process they're trying to undo.

Researchers at Tufts University and IAIFI have now unified these scattered problems under a single framework — the **Ensemble Inverse Problem** — and proposed a family of machine learning methods that solve them faster, more flexibly, and without ever re-running the physical process they're trying to invert.

> **Key Insight:** By treating collections of measurements as a group rather than solving each one in isolation, an AI model can learn to invert complex physical processes without simulating them at deployment — and can generalize to distributions it has never seen before.

## How It Works

The core observation is simple: in practice, you never receive just one measurement. A particle physics experiment logs millions of collision events. A seismologist records waveforms across a dense sensor array. These collections — **ensembles** — carry information that no single measurement can.

Traditional approaches treat each measurement independently: given one blurry detector readout, invert the physics to recover the truth. The EIP framework asks something different: given the *whole set* of observations together, what underlying distribution of true physics must have generated them?

The researchers formalize two related problems:

- **EIP-I** asks for the **prior distribution** — the natural spread of true physical quantities before any particular observation is taken into account.
- **EIP-II** asks for the **posterior**: given a specific observation *and* the full ensemble context, what was the most likely true value for *that particular event*? This is a refined best-guess that combines one measurement with everything the ensemble reveals about the broader physics.

EIP-I is the coarser target; EIP-II is more precise. Solving EIP-II automatically gives you EIP-I, but not vice versa — you can approximate EIP-I with wrong posteriors that happen to integrate correctly, as Figure 1 illustrates.

![Figure 1](figure:1)

Their solution is a new class of models called **ensemble inverse generative models**, trained with a three-step recipe:

1. Collect many datasets, each generated by a *different* prior distribution fed through the *same* **forward model** — the physical process being inverted, whether detector response, seismic wave equations, or an imaging system.
2. Train a **conditional generative model** that takes both a single observation *and* the full ensemble as inputs.
3. The model learns to sample from the posterior, conditioned on all available context.

This training procedure implicitly encodes the forward model's behavior into the network's weights. At inference time, you never run the forward model again — no expensive simulations, no iterative loops. One forward pass through the trained network, and you have your answer.

## Why It Matters

The practical stakes are high across multiple fields. In particle physics, **unfolding** — the standard name for this inverse problem — is a prerequisite for nearly every precision measurement. If the LHC is to detect subtle deviations from the Standard Model, physicists need to strip away detector artifacts without introducing biases.

Current state-of-the-art methods like OmniFold require iterative reweighting of simulated events — computationally expensive and dependent on explicit access to the forward model. The EIP framework sidesteps this entirely.

![Figure 2](figure:2)

In seismology, full waveform inversion already demands supercomputers running physics simulations for days. A method that learns the forward model implicitly — and inverts instantly for new observations — could transform how geoscientists image the Earth's interior. The authors demonstrate this isn't hypothetical: they benchmark against real FWI datasets alongside synthetic tests and particle physics benchmarks, showing competitive or superior performance across all three domains. The ensemble context proves especially powerful for generalizing to distributions the model never encountered during training.

The work also connects to an emerging thread in AI research: **in-context learning** — the ability of AI systems to pick up new tasks from examples provided at query time, without any retraining. Large language models demonstrate this: show them a few examples in the prompt, and they adapt on the fly. The EIP framework formalizes an analogous capability for physical inverse problems, using the ensemble as a kind of context that lets the model adapt to a new prior without modification.

![Figure 3](figure:3)

> **Bottom Line:** The Ensemble Inverse Problem gives a unified mathematical home to inverse challenges across physics, geoscience, and imaging — and the proposed generative model approach solves them without forward-model simulations at inference time, while generalizing to distributions never seen during training.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work formally unifies particle physics unfolding, seismic full waveform inversion, and inverse imaging under a single statistical framework, enabling shared methodological progress across fields that have historically solved these problems in isolation.

- **Impact on Artificial Intelligence:** The ensemble inverse generative model introduces a new class of conditional generative models that use observation-set context to enable prior generalization — a capability with implications for in-context learning and scalable Bayesian inference beyond physics.

- **Impact on Fundamental Interactions:** By eliminating the need for explicit forward-model simulation at inference time, the method could significantly accelerate precision measurements at particle colliders, reducing a key computational bottleneck in Standard Model tests and new-physics searches.

- **Outlook and References:** Future work could explore scaling to higher-dimensional physics observables and tighter integration with LHC data pipelines; the paper is available on arXiv as [2602.09093](https://arxiv.org/abs/2602.09093).
