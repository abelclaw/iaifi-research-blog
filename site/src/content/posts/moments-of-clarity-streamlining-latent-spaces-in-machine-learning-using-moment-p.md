---
abstract: Many machine learning applications involve learning a latent representation
  of data, which is often high-dimensional and difficult to directly interpret. In
  this work, we propose "Moment Pooling", a natural extension of Deep Sets networks
  which drastically decrease latent space dimensionality of these networks while maintaining
  or even improving performance. Moment Pooling generalizes the summation in Deep
  Sets to arbitrary multivariate moments, which enables the model to achieve a much
  higher effective latent dimensionality for a fixed latent dimension. We demonstrate
  Moment Pooling on the collider physics task of quark/gluon jet classification by
  extending Energy Flow Networks (EFNs) to Moment EFNs. We find that Moment EFNs with
  latent dimensions as small as 1 perform similarly to ordinary EFNs with higher latent
  dimension. This small latent dimension allows for the internal representation to
  be directly visualized and interpreted, which in turn enables the learned internal
  jet representation to be extracted in closed form.
arxivId: '2403.08854'
arxivUrl: https://arxiv.org/abs/2403.08854
authors:
- Rikab Gambhir
- Athis Osathapan
- Jesse Thaler
concepts:
- moment pooling
- dimensionality reduction
- representation learning
- interpretability
- jet physics
- energy flow networks
- collider physics
- classification
- deep sets
- feature extraction
- effective latent dimension
- symmetry preservation
figures:
- /iaifi-research-blog/figures/2403_08854/figure_2.png
- /iaifi-research-blog/figures/2403_08854/figure_3.png
pdfUrl: https://arxiv.org/pdf/2403.08854v2
published: '2024-03-13T18:00:01+00:00'
theme: Theoretical Physics
title: 'Moments of Clarity: Streamlining Latent Spaces in Machine Learning using Moment
  Pooling'
wordCount: 1127
---

## The Big Picture

Imagine trying to understand how a master chef decides whether a dish needs more salt, but instead of watching them cook, you can only see a thousand numbers streaming out of their brain in real time. That's roughly the situation physicists face when neural networks sort the particle sprays produced when protons collide inside the Large Hadron Collider. The networks work brilliantly. But *why* they work is hidden inside thousands of learned internal numbers that no human can directly read.

This opacity isn't just philosophically unsatisfying. When a model's internal logic is inscrutable, it's harder to trust predictions on new data and harder to extract the physical intuition the network may have quietly learned. Particle physicists have long suspected their networks are discovering real, meaningful patterns, ones that might correspond to known physics observables. But with hundreds of tangled internal variables, finding those patterns is like searching for a melody inside a full orchestra recording.

Researchers Rikab Gambhir, Athis Osathapan, and Jesse Thaler at MIT and IAIFI have found a way to turn that orchestra into a solo instrument: compressing the network's internal code down to a single dimension without sacrificing performance, then reading off the physics in closed form.

> **Key Insight:** By replacing the standard summation step in particle-physics neural networks with a richer statistical operation called Moment Pooling, the team achieved the same classification accuracy with a latent space 4× smaller, small enough to visualize directly and identify as a known physical observable.

## How It Works

The starting point is the **Energy Flow Network (EFN)**, an architecture built for jet physics that respects the fundamental symmetries of high-energy collisions. (Jets are the cone-shaped particle sprays produced when quarks and gluons fly apart after a proton-proton collision.) An EFN works in two stages: a function Φ maps each particle to an *L*-dimensional latent representation (a list of *L* numbers encoding that particle's properties), then a second function *F* acts on the *average* of those representations across all particles in the jet. That average is the bottleneck through which all information must pass.

The core innovation: why stop at the average? Statisticians routinely characterize distributions using not just their mean but also their variance, skewness, and kurtosis (the second, third, and fourth statistical moments, capturing a distribution's spread, lopsidedness, and tail weight). **Moment Pooling** applies exactly this logic. Instead of feeding *F* only the mean of Φ, a Moment EFN of order *k* feeds it all moments up to order *k*.

![Figure 1](/iaifi-research-blog/figures/2403_08854/figure_2.png)

The payoff is a big jump in effective latent dimensionality, meaning how much information actually passes through the bottleneck. With a latent dimension of *L* = 1 and moments up to order *k* = 4, the model passes *k* numbers through the bottleneck, giving it the same effective information capacity as an ordinary EFN with *L* = 4. But the *learned* latent space is still one-dimensional, so it can be plotted as a simple curve.

On the standard task of distinguishing quark-initiated jets from gluon-initiated jets (measured by area under the ROC curve):

- A standard EFN with *L* = 4 achieves a strong baseline classification accuracy
- A Moment EFN with *L* = 1 and *k* = 4 matches that performance almost exactly
- Moment EFNs consistently match or beat ordinary EFNs across a range of *L* and *k* values

## Why It Matters

With *L* = 1, the researchers can simply *plot* what the network learned: the function Φ that maps each particle's detector position to a number. And when they did, something jumped out.

![Figure 2](/iaifi-research-blog/figures/2403_08854/figure_3.png)

The learned Φ takes an almost perfectly simple mathematical form. After fitting it with analytic functions, the team found it corresponds closely to a **log angularity**, an observable that weights particles by their energy and by the logarithm of their angular distance from the jet center. Jet angularities are a family of observables physicists have studied theoretically for decades. The machine, trained only to maximize classification accuracy, had independently discovered a quantity that humans already knew was physically meaningful.

They pushed further, constraining the *F* network to be linear at *L* = 1. The learned observable became even more interpretable: essentially a weighted sum of the moments of the log angularity, which are themselves established theoretical objects. The network wasn't just finding *a* good observable; it was organizing the physics into a form that humans had already found compelling.


At *L* = 2, the picture remains tractable. The model learns a second latent function alongside the log angularity, and the two-dimensional latent space can be visualized as a scatter plot, still graspable by human eyes in a way that a 16-dimensional space never could be.

All of this connects to a bigger goal: building AI systems whose reasoning humans can actually follow. In particle physics, where the underlying theory is **Quantum Chromodynamics** (the precise mathematical description of how quarks and gluons interact), interpretability has a special edge. A model's internal representation can be compared directly against theoretical predictions. If a neural network learns something close to a jet angularity, that's not just a curiosity. It's evidence the observable captures the right physics, and it opens the door to computing analytic corrections, studying the observable at different collision energies, and designing better measurements.

Moment Pooling is not specific to particle physics, either. Any application using **Deep Sets**, a general framework for processing unordered collections such as point clouds, molecular structures, or graph-structured data, could benefit from the same trick: replace the pooling step with higher-order moments, shrink the latent dimension, and gain interpretability without sacrificing accuracy.

> **Bottom Line:** Moment Pooling lets physicists shrink neural network latent spaces from dozens of dimensions down to one, without losing accuracy, and then read off the learned physics in plain mathematical language. A black box becomes a transparent equation.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work puts IAIFI's core mission into practice, using machine learning theory (moment statistics and Deep Sets) to extract physically meaningful observables from jet data. It directly connects neural network architecture design to QCD phenomenology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Moment Pooling provides a general, architecture-agnostic technique for reducing latent dimensionality in set-based networks while maintaining or improving performance, offering a practical interpretability gain for any Deep Sets application.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The method reveals that a well-trained jet classifier independently discovers log angularities, a family of theoretically well-motivated QCD observables, providing a new data-driven route to identifying physically significant jet substructure quantities.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending Moment Pooling to molecular modeling, graph-structured data, and other collider tasks, as well as using the extracted analytic observables to compute perturbative QCD corrections; the full paper is available at [arXiv:2403.08854](https://arxiv.org/abs/2403.08854).</span></div></div>
</div>
