---
abstract: We present a technique for translating a black-box machine-learned classifier
  operating on a high-dimensional input space into a small set of human-interpretable
  observables that can be combined to make the same classification decisions. We iteratively
  select these observables from a large space of high-level discriminants by finding
  those with the highest decision similarity relative to the black box, quantified
  via a metric we introduce that evaluates the relative ordering of pairs of inputs.
  Successive iterations focus only on the subset of input pairs that are misordered
  by the current set of observables. This method enables simplification of the machine-learning
  strategy, interpretation of the results in terms of well-understood physical concepts,
  validation of the physical model, and the potential for new insights into the nature
  of the problem itself. As a demonstration, we apply our approach to the benchmark
  task of jet classification in collider physics, where a convolutional neural network
  acting on calorimeter jet images outperforms a set of six well-known jet substructure
  observables. Our method maps the convolutional neural network into a set of observables
  called energy flow polynomials, and it closes the performance gap by identifying
  a class of observables with an interesting physical interpretation that has been
  previously overlooked in the jet substructure literature.
arxivId: '2010.11998'
arxivUrl: https://arxiv.org/abs/2010.11998
authors:
- Taylor Faucett
- Jesse Thaler
- Daniel Whiteson
concepts:
- interpretability
- decision ordering metric
- jet physics
- convolutional networks
- energy flow polynomials
- classification
- feature extraction
- collider physics
- dimensionality reduction
- surrogate modeling
- model validation
- sparse models
figures:
- /iaifi-research-blog/figures/2010_11998/figure_1.png
- /iaifi-research-blog/figures/2010_11998/figure_2.png
pdfUrl: https://arxiv.org/pdf/2010.11998v2
published: '2020-10-22T19:18:19+00:00'
theme: Experimental Physics
title: Mapping Machine-Learned Physics into a Human-Readable Space
wordCount: 1026
---

## The Big Picture

Imagine hiring a chess grandmaster to improve your game, but instead of explaining strategy, they just silently win every match. Their results are undeniable. You've learned nothing you can use yourself.

This is the situation physicists face when deploying deep neural networks to analyze particle collision data. The machine wins. The physicists scratch their heads.

At the Large Hadron Collider, neural networks classify **jets** (sprays of particles produced when fundamental matter collides at nearly the speed of light) with impressive accuracy. But that accuracy comes with a frustrating asterisk: nobody knows exactly *how* the machine does it. The network ingests thousands of detector readings and produces a classification through layers of opaque mathematics. Physicists need to validate that the machine is using real physical information, not artifacts of the training data. They need to estimate systematic uncertainties. They need to understand the physics.

Taylor Faucett, Jesse Thaler, and Daniel Whiteson built a systematic method to crack open that black box, not by peering inside, but by finding simple, human-readable quantities that make the same decisions as the neural network.

> **Key Insight:** Rather than interpreting the neural network directly, the researchers use it as a guide to discover which human-understandable physical quantities capture the same information, closing the performance gap while revealing overlooked physics.

## How It Works

The core challenge is defining what "makes the same decisions" means mathematically. The team introduces a metric called **Average Decision Ordering (ADO)**, inspired by classical rank-correlation statistics. Instead of asking whether two classifiers assign the same numerical score to each event, ADO asks a subtler question: for any pair of events, do the two classifiers agree on which one is *more* signal-like? This pairwise comparison measures agreement in ranking order, independent of absolute scores.

![Figure 1](/iaifi-research-blog/figures/2010_11998/figure_1.png)

With ADO as their compass, the researchers build an iterative search algorithm:

1. Start with a large library of candidate high-level physics observables
2. Find the single observable with the highest ADO relative to the neural network
3. Add it to the working set and combine them into a new classifier
4. Identify the event pairs the current set still *misorients* compared to the neural network
5. Repeat, focusing only on those remaining misoriented pairs

This focus on "hard cases" is what makes the search efficient. The algorithm doesn't waste iterations on pairs already handled correctly; it drives directly toward the gaps.

The case study is **boosted W boson classification**: distinguishing jets from W bosons (particles carrying the weak nuclear force, which decay into two visible particle streams) versus jets from ordinary quarks and gluons that produce just one stream. The black box is a convolutional neural network trained on 37×37 pixel calorimeter images. The human-readable candidates are **Energy Flow Polynomials (EFPs)**, a mathematically complete set of collider observables that remain physically well-defined even when soft or nearly collinear particles are present.

The team applies their method in two modes. In *supplementation mode*, the algorithm starts from six well-known jet substructure observables and searches for what's missing. It quickly identifies a seventh, a specific EFP with a "triangle" graph topology that the jet substructure community had not previously considered for this task. Adding it nearly closes the performance gap between the human-engineered approach and the CNN. Physically, this EFP encodes a three-particle angular correlation matching the geometry expected from a W boson's two-pronged decay.

![Figure 2](/iaifi-research-blog/figures/2010_11998/figure_2.png)

In *from-scratch mode*, starting only from raw jet image inputs, the algorithm iteratively assembles a set of EFPs that matches CNN performance within statistical uncertainty. The selected EFPs tell a coherent physical story about what distinguishes W jets from QCD jets.


The black-box guided search also far outperforms both brute-force search and "truth-label guiding," where the known particle labels serve as the guide instead of the neural network. The black box turns out to be a *better* teacher than the ground truth itself, because it encodes decision boundaries tuned to the actual structure of the data, not just the labels.

## Why It Matters

Neural networks and interpretability are in tension throughout particle physics. The networks win the performance contest, but physics requires more than winning.

Results must be validated against physical models. Systematic uncertainties must be estimated and reported. Theoretical predictions must be tested. None of that is straightforward when your classifier is 40 layers of convolutions.

Faucett, Thaler, and Whiteson's method sidesteps the tradeoff. Train the powerful network first and let it find the optimal decision boundary. Then use it as a guide to find the simplest human-readable approximation of that boundary. You end up with a compact set of physically interpretable observables that can be individually calibrated, theoretically predicted, and experimentally validated, while capturing essentially all the discriminating power of the original machine.

The technique generalizes beyond jet physics to anywhere a black-box ML system operates on high-dimensional data but a human-readable summary would be more useful. Medical imaging, climate modeling, materials discovery: if understanding the *reason* behind a prediction matters, not just the prediction itself, the same iterative search could apply.

> **Bottom Line:** By treating a neural network as a guide rather than an oracle, this work translates black-box classification into discoverable physics, and in doing so, uncovers a jet substructure observable that physicists had overlooked for years.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects machine learning and experimental particle physics by developing Average Decision Ordering, a mathematical framework that translates opaque neural network decisions into physically interpretable observables grounded in collider phenomenology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The black-box guided search strategy is a general interpretability technique applicable beyond physics, providing a principled way to approximate any high-dimensional classifier with a compact, human-readable model without sacrificing performance.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Applied to jet substructure at colliders, the method recovered all discriminating power of a CNN while identifying a previously overlooked three-particle angular correlation observable, opening new directions in the theoretical understanding of jet formation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend this framework to more complex tasks such as full event reconstruction or flavor tagging, and to larger EFP libraries; the full paper is available at [arXiv:2010.11998](https://arxiv.org/abs/2010.11998).</span></div></div>
</div>
