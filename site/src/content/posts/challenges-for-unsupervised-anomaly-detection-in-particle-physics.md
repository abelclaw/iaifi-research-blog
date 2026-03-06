---
abstract: Anomaly detection relies on designing a score to determine whether a particular
  event is uncharacteristic of a given background distribution. One way to define
  a score is to use autoencoders, which rely on the ability to reconstruct certain
  types of data (background) but not others (signals). In this paper, we study some
  challenges associated with variational autoencoders, such as the dependence on hyperparameters
  and the metric used, in the context of anomalous signal (top and $W$) jets in a
  QCD background. We find that the hyperparameter choices strongly affect the network
  performance and that the optimal parameters for one signal are non-optimal for another.
  In exploring the networks, we uncover a connection between the latent space of a
  variational autoencoder trained using mean-squared-error and the optimal transport
  distances within the dataset. We then show that optimal transport distances to representative
  events in the background dataset can be used directly for anomaly detection, with
  performance comparable to the autoencoders. Whether using autoencoders or optimal
  transport distances for anomaly detection, we find that the choices that best represent
  the background are not necessarily best for signal identification. These challenges
  with unsupervised anomaly detection bolster the case for additional exploration
  of semi-supervised or alternative approaches.
arxivId: '2110.06948'
arxivUrl: https://arxiv.org/abs/2110.06948
authors:
- Katherine Fraser
- Samuel Homiller
- Rashmish K. Mishra
- Bryan Ostdiek
- Matthew D. Schwartz
concepts:
- anomaly detection
- variational autoencoders
- optimal transport
- autoencoders
- jet physics
- new physics searches
- collider physics
- hyperparameter sensitivity
- out-of-distribution detection
- dimensionality reduction
- representation learning
- semi-supervised learning
figures:
- /iaifi-research-blog/figures/2110_06948/figure_1.png
- /iaifi-research-blog/figures/2110_06948/figure_2.png
- /iaifi-research-blog/figures/2110_06948/figure_3.png
pdfUrl: https://arxiv.org/pdf/2110.06948v1
published: '2021-10-13T18:00:04+00:00'
theme: Experimental Physics
title: Challenges for Unsupervised Anomaly Detection in Particle Physics
wordCount: 1172
---

## The Big Picture

Imagine you're a security guard at the world's busiest airport, tasked with spotting suspicious behavior — but you've never been told what suspicious looks like. You can only study the millions of ordinary travelers passing through each day, building up an intuition for "normal," and hope that anything truly unusual will stand out.

That's essentially the challenge physicists face at the Large Hadron Collider (LHC). Particle collisions produce an overwhelming flood of routine subatomic interactions — ordinary physics we already understand — and the hope is that exotic new physics will announce itself as different.

The LHC has found no clear evidence of new particles beyond the Standard Model — physicists' current best theory of all known matter and forces — despite years of searching. One reason may be that searches have been too narrowly tailored to specific hypothetical signals. A more flexible strategy is **unsupervised anomaly detection**: train an algorithm only on "boring" background events, then flag anything that looks unusual.

This "model-agnostic" approach requires no assumptions about what new physics looks like. But a new study from Harvard physicists at IAIFI reveals it faces deeper challenges than previously appreciated. The researchers — Katherine Fraser, Samuel Homiller, Rashmish Mishra, Bryan Ostdiek, and Matthew Schwartz — systematically probed why a class of neural networks called variational autoencoders struggle with particle physics anomaly detection, and uncovered a geometric insight that points toward better methods.

> **Key Insight:** The choices that best compress and represent background events are *not* necessarily the choices that best expose signal events as anomalies — a fundamental tension at the heart of unsupervised anomaly detection.

## How It Works

The workhorse of modern unsupervised anomaly detection in particle physics is the **variational autoencoder (VAE)** — a neural network that learns to compress data into a compact representation and then reconstruct it. Think of it like a lossy photo compressor: squeeze an image down, then expand it back. If the original was typical, the reconstruction will be faithful. If it was unusual, details get lost.

Train a VAE on background-only data, and it learns the structure of normal events. When a signal event appears, the VAE can't reconstruct it well, producing a high **reconstruction error** — the gap between the original and the network's best attempt — that serves as an anomaly score.

The team tested this on jets: the sprays of particles produced when quarks and gluons scatter at high energy. Their background consisted of ordinary QCD jets (the routine particle showers dominating most LHC collisions). Their signals were top quark jets and W boson jets, both with distinctive multi-pronged substructure compared to the smooth QCD baseline. Jets were represented as images — two-dimensional maps of energy deposits in the detector.

![Figure 1](/iaifi-research-blog/figures/2110_06948/figure_1.png)

Performance depends heavily on **hyperparameters**: tuning knobs set before training, including the size of the **latent space** (the compressed internal representation, analogous to the small file in the photo analogy), the relative weight of the reconstruction loss versus the **KL divergence** (a penalty that keeps the compressed representation organized), and the distance metric used to measure reconstruction error. Systematic variation of these choices revealed:

- Optimal settings for detecting top jets were often non-optimal for W jets
- Small changes in KL weight dramatically shifted performance, sometimes reversing which signal the network could best identify
- No single configuration worked best for all signals simultaneously

This is a fundamental problem for a model-agnostic tool. If tuning for one signal hurts sensitivity to another, the whole point is undermined.

While probing the VAE's internals, the researchers made a further striking observation: distances between events in the latent space were strongly correlated with **Wasserstein distances** — also called **optimal transport distances** — between the original jet images. Wasserstein distance has a clean physical intuition: it measures how much "work" it takes to rearrange the energy deposits in one jet image to match another, treating energy as dirt that needs to be moved.

![Figure 2](/iaifi-research-blog/figures/2110_06948/figure_2.png)

This connection suggests the VAE is essentially learning a compressed version of optimal transport geometry. That prompted a direct question: why use an autoencoder at all? The team developed **event-to-ensemble distance** — select a set of representative background events, then score each new event by its optimal transport distance to those representatives. No neural network training required; just a physically interpretable measure of deviation from typical background.

The results were striking. Direct optimal transport scoring matched the best VAE configurations in performance — and illuminated the same fundamental tension: the set of representative events that best *describes* the background is not the set that best *separates* signal from background.

![Figure 3](/iaifi-research-blog/figures/2110_06948/figure_3.png)

This echoes a deep statistical principle. The best density estimator concentrates resources on high-probability regions — the bulk of the background. But anomaly detection needs sensitivity at the edges, where rare signal events lurk. These goals pull in opposite directions.

## Why It Matters

These findings reframe how physicists should think about anomaly detection at the LHC. The autoencoder paradigm implicitly assumes that learning to represent background well will naturally make signal events stand out. This paper shows that assumption is fragile: the optimization target — reconstruction fidelity on background — isn't aligned with the goal of signal discovery.

The optimal transport connection offers a computationally lighter and more interpretable alternative to VAEs. You can understand exactly why an event gets flagged in terms of jet geometry. But it faces the same fundamental challenge. Both approaches are victims of the same tension between description and discrimination.

The most important takeaway is the case for **semi-supervised approaches** — methods that incorporate even weak or indirect information about what signals might look like — as a necessary complement to fully unsupervised searches. Hybrid strategies that combine the model-agnosticism of unsupervised methods with even minimal signal priors could chart the most promising path forward for new physics discovery at the LHC.

> **Bottom Line:** Variational autoencoders for particle physics anomaly detection are more sensitive to hyperparameter choices than previously recognized, and the optimal transport geometry they implicitly learn can be used directly — but no unsupervised method can fully escape the tension between modeling background and detecting signal, pointing toward semi-supervised approaches as the most promising path.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work forges a concrete mathematical link between VAE latent spaces and optimal transport geometry, connecting machine learning methodology with physically motivated jet metrics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The study shows that VAE latent geometry under MSE training encodes Wasserstein-like distances, and that direct optimal transport scoring matches autoencoder performance — providing a more interpretable, training-free anomaly detection baseline.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By systematically mapping the failure modes of unsupervised anomaly detection for QCD jets, this work sharpens the theoretical foundations for model-agnostic new physics searches at the LHC and motivates more robust semi-supervised strategies.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work should explore semi-supervised and hybrid methods that better align training objectives with signal discovery goals; the full analysis is available at arXiv:2107.11580.</span></div></div>
</div>
