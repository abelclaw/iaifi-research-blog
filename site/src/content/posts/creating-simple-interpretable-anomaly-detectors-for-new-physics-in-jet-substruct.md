---
abstract: Anomaly detection with convolutional autoencoders is a popular method to
  search for new physics in a model-agnostic manner. These techniques are powerful,
  but they are still a "black box," since we do not know what high-level physical
  observables determine how anomalous an event is. To address this, we adapt a recently
  proposed technique by Faucett et al., which maps out the physical observables learned
  by a neural network classifier, to the case of anomaly detection. We propose two
  different strategies that use a small number of high-level observables to mimic
  the decisions made by the autoencoder on background events, one designed to directly
  learn the output of the autoencoder, and the other designed to learn the difference
  between the autoencoder's outputs on a pair of events. Despite the underlying differences
  in their approach, we find that both strategies have similar ordering performance
  as the autoencoder and independently use the same six high-level observables. From
  there, we compare the performance of these networks as anomaly detectors. We find
  that both strategies perform similarly to the autoencoder across a variety of signals,
  giving a nontrivial demonstration that learning to order background events transfers
  to ordering a variety of signal events.
arxivId: '2203.01343'
arxivUrl: https://arxiv.org/abs/2203.01343
authors:
- Layne Bradshaw
- Spencer Chang
- Bryan Ostdiek
concepts:
- anomaly detection
- autoencoders
- interpretability
- jet physics
- new physics searches
- knowledge distillation
- convolutional networks
- feature extraction
- out-of-distribution detection
- collider physics
- classification
- transfer learning
figures:
- /iaifi-research-blog/figures/2203_01343/figure_1.png
- /iaifi-research-blog/figures/2203_01343/figure_1.png
- /iaifi-research-blog/figures/2203_01343/figure_2.png
- /iaifi-research-blog/figures/2203_01343/figure_2.png
- /iaifi-research-blog/figures/2203_01343/figure_3.png
- /iaifi-research-blog/figures/2203_01343/figure_3.png
pdfUrl: https://arxiv.org/pdf/2203.01343v2
published: '2022-03-02T19:00:05+00:00'
theme: Theoretical Physics
title: Creating Simple, Interpretable Anomaly Detectors for New Physics in Jet Substructure
wordCount: 1070
---

## The Big Picture

Imagine you hire the world's best detective to find a criminal, and they succeed. But when you ask how they did it, they shrug and say "I just knew." That's the situation physicists face at the Large Hadron Collider when they deploy deep learning to search for exotic new particles. The AI finds something suspicious. But what, exactly, is it looking at?

At the LHC, protons collide billions of times per second, producing cascades of particles called **jets**: sprays of subatomic debris carrying fingerprints of the collision. Most jets come from ordinary processes described by the **Standard Model of particle physics**, the well-tested rulebook governing all known subatomic particles and forces. If something new exists (a hidden particle, an exotic decay) it might leave a distinctive pattern in the internal arrangement of that debris.

For years, physicists have used **convolutional autoencoders**, a type of neural network that learns to compress and reconstruct jet images, to flag unusual events as potentially exotic. The problem: nobody knows which physical features the autoencoder actually uses to call something anomalous. Bradshaw, Chang, and Ostdiek set out to crack open that black box and build a replacement physicists can actually understand.

> **Key Insight:** By mimicking a convolutional autoencoder's decisions using only six human-interpretable observables, the researchers built simpler anomaly detectors that match or outperform the original on seven out of eight exotic signal types, proving that interpretability doesn't have to cost performance.

## How It Works

The starting point is a **convolutional autoencoder (CAE)**, a neural network trained to compress jet images into a compact internal representation and then reconstruct them. Jets from ordinary background processes get reconstructed well; jets from rare or exotic processes don't. That reconstruction error becomes an anomaly score: high error means "this event looks weird."

But which features of the jet make it weird? The autoencoder operates on raw pixel-level jet images, thousands of numbers per event, and never reveals whether it's reacting to the jet's mass, its angular spread, or some subtle three-pronged substructure.

![Figure 1](/iaifi-research-blog/figures/2203_01343/figure_1.png)

To extract that hidden logic, the researchers adapted an interpretability technique originally designed for classifiers. Their approach uses **Energy Flow Polynomials (EFPs)** as a vocabulary: a mathematically complete set of measurements covering every physically meaningful way to characterize a jet's shape and energy distribution. Think of EFPs as a giant dictionary of jet properties. Some measure how "pronglike" a jet is; others capture its angular moments.

From this dictionary, the team built two competing mimicker networks:

1. **The High-Level Network (HLN):** Trained to replicate the autoencoder's anomaly score event by event, using a handful of EFPs as input.
2. **The Paired Neural Network (PNN):** Given two jet events, it learns to predict which one the autoencoder rated as *less* anomalous, turning it into a ranking task rather than a regression. It never sees signal events during training.

Both networks use an iterative selection procedure: start with one observable, find which EFP best improves agreement with the CAE, add it, repeat. Selection stops when additional observables provide diminishing returns.

![Figure 2](/iaifi-research-blog/figures/2203_01343/figure_1.png)

The result is striking. Both strategies independently converged on the **same six observables**, even though they approached the problem from completely different mathematical angles. The matched set includes the jet mass, multiplicity-related quantities, and specific EFPs capturing two- and three-body angular correlations. Two fundamentally different formulations of "what does the autoencoder care about?" reached the same answer. Both mimickers agreed with the autoencoder's event ordering about 83% of the time on ordinary background jets.

The real test: can mimickers trained only on ordinary jets detect exotic new physics they were never trained for?

![Figure 3](/iaifi-research-blog/figures/2203_01343/figure_2.png)

The researchers tested eight signal types: W bosons of four different masses, top quarks at two masses, and Higgs bosons at two masses. These span exotic jet shapes with two, three, and four distinct prongs of energy deposition. Performance was measured using **signal significance improvement (SSI)**, which quantifies how much better than random chance the detector isolates signal from background.

For seven out of eight signals, at least one mimicker matched or exceeded the autoencoder's performance. The lone exception was a very light W boson (59 GeV), where the jet substructure looks nearly identical to background, a hard case for every method. The interpretable networks also held their own against **Isolation Forests**, another popular anomaly detection approach.

![Figure 5](/iaifi-research-blog/figures/2203_01343/figure_3.png)

## Why It Matters

This result matters on two levels. The first is practical. Experimental collaborations at the LHC face enormous overhead when validating any new observable: checking it against detector effects, calibrating its measurement, accounting for systematic uncertainties. An anomaly detector depending on raw jet images requires that process for thousands of pixel values. One depending on six well-understood EFPs requires it for six. In real experimental deployments, that difference is enormous.

The second is conceptual. The fact that six high-level observables, things physicists can write down and measure cleanly, reproduce a complex autoencoder's behavior suggests the network isn't discovering mysterious jet features humans missed. It's learning a compact combination of known physics.

That's reassuring, but it also opens a question: is there a regime where deep networks genuinely exceed simple observables? If so, what does it look like? The iterative EFP selection method can be applied to other autoencoder architectures, other datasets, other signal hypotheses. And the deeper insight, that learning to order background events transfers to ordering signal events, may hold lessons for anomaly detection well beyond particle physics.

> **Bottom Line:** Six simple, human-readable jet observables can replicate what a convolutional autoencoder does when hunting for exotic particles, making anomaly detection at the LHC both more interpretable and more deployable without sacrificing sensitivity.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits squarely at the intersection of deep learning interpretability and experimental particle physics, adapting classifier mimicry methods to unsupervised anomaly detection in a way that produces physics-meaningful outputs.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Iterative knowledge distillation from a black-box neural network yielded compact, interpretable models that match performance on out-of-distribution data, a result relevant to explainable AI well beyond physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By revealing which jet substructure observables drive anomaly detection decisions, this work provides both practical tools and conceptual clarity for model-agnostic new physics searches at the LHC.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend this interpretability framework to other autoencoder architectures and higher-dimensional jet representations; the paper is available at [arXiv:2203.01343](https://arxiv.org/abs/2203.01343).</span></div></div>
</div>
