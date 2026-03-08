---
abstract: Jet point cloud images are high dimensional data structures that needs to
  be transformed to a separable feature space for machine learning algorithms to distinguish
  them with simple decision boundaries. In this article, the authors focus on jet
  category separability by particle and jet feature extraction, resulting in more
  efficient training of a simple deep neural network, resulting in a computational
  efficient interpretable model for jet classification. The methodology is tested
  with three to five categories of jets from the JetNet benchmark jet tagging dataset,
  resulting in comparable performance to particle flow network. This work demonstrates
  that high dimensional datasets represented in separable latent spaces lead to simpler
  architectures for jet classification.
arxivId: '2407.03524'
arxivUrl: https://arxiv.org/abs/2407.03524
authors:
- Jairo Orozco Sandoval
- Vidya Manian
- Sudhir Malik
concepts:
- jet physics
- feature extraction
- classification
- convolutional networks
- point cloud classification
- attention mechanisms
- dimensionality reduction
- autoencoders
- embeddings
- collider physics
- event reconstruction
- interpretability
figures:
- /iaifi-research-blog/figures/2407_03524/figure_1.png
- /iaifi-research-blog/figures/2407_03524/figure_2.png
- /iaifi-research-blog/figures/2407_03524/figure_3.png
pdfUrl: https://arxiv.org/pdf/2407.03524v1
published: '2024-07-03T22:00:35+00:00'
theme: Foundational AI
title: A multicategory jet image classification framework using deep neural network
wordCount: 1034
---

## The Big Picture

Imagine standing at the edge of a fireworks display, trying to identify each shell by the shape of its burst — while thousands of explosions go off simultaneously, every second. That's roughly what physicists face at the Large Hadron Collider, where proton collisions spray cascades of particles outward at nearly the speed of light. These cascades, called **jets**, are the fingerprints of the fundamental particles that created them. But the fingerprints are messy, overlapping, and arriving faster than any human could ever read.

The LHC generates collision data at 40 million events per second. When the High Luminosity upgrade comes online, that torrent will swell to roughly 50 terabytes of raw particle data every second. Somewhere inside that flood are signals of top quarks, W bosons, Z bosons, gluons, and light quarks — different types of fundamental particles, each leaving a subtly different spray pattern in the detector. Some of those patterns look nearly identical to each other. Standard machine learning approaches either drown in the data's complexity or require enormous, power-hungry neural networks to untangle it.

Researchers at the University of Puerto Rico, Mayaguez, took a different approach. Rather than throwing a bigger model at the problem, they asked: what if you could reorganize the data first so that jets from different sources naturally separate — and then train a simpler network on that cleaner picture?

> **Key Insight:** By transforming raw jet data into a more "separable" feature space before classification, this framework achieves competitive accuracy with far simpler neural network architecture — proving that smarter data representation can substitute for raw computational power.

## How It Works

The raw material is a **point cloud** — a set of particles, each described by four numbers capturing its position in the detector, its direction of travel, its energy, and its mass. Think of it as a three-dimensional scatter plot of individual raindrops in a storm, where each drop also carries metadata about its energy and direction. Taken straight from the detector, these point clouds look like tangled blobs — jets from different source particles cluster in ways that make classification unreliable with simple models.

![Figure 1](/iaifi-research-blog/figures/2407_03524/figure_1.png)

The team built a two-track pipeline:

1. **Particle feature extraction** — A **point cloud transformer** with multihead attention — a mechanism that weighs how much each particle "pays attention" to every other particle in the jet — captures each particle's local relationships to its neighbors. This is the same mathematical machinery behind large language models, adapted here to encode how particles relate in terms of energies and trajectories.
2. **Jet feature extraction** — A **1D convolutional autoencoder** — a neural network that compresses data into a compact summary, where the middle layer retains the most important features — processes the whole jet's aggregate properties (type, total transverse momentum, pseudorapidity, and mass) into a compact learned representation.

After merging these two streams, the team added two engineered features: **particle density** (how tightly packed the jet's particles are) and **average intensity** (the mean energy deposition). These handcrafted additions push different jet categories further apart in the feature space before classification even begins.

![Figure 2](/iaifi-research-blog/figures/2407_03524/figure_2.png)

The payoff is visible in 3D plots of the embedded data. Before feature extraction, all five jet classes pile up in an undifferentiated mass. After embedding, the classes fan out into distinct clusters. Once the data is structured this way, a straightforward **deep neural network (DNN)** — not a massive transformer, not a graph network — can draw clean boundaries between classes.

## Why It Matters

The team tested their framework on the JetNet benchmark dataset: 250,000 jets across five categories, with an 80/20 train-test split. For the full five-class problem — top quark, W boson, Z boson, gluon, and light quark — the model reached **75.98% overall test accuracy**. Top quarks, W bosons, and Z bosons each classified above 80%. Gluons and light quarks came in at 65% and 68% respectively, reflecting a genuine physical similarity that even expert physicists struggle to resolve.

When the problem was reduced to four classes by removing one of that similar pair, accuracy jumped to **84.00%**, with top quarks hitting 88.91%. These numbers match the **Particle Flow Network (PFN)**, a well-established and considerably more complex benchmark — but with a simpler, more interpretable architecture.

![Figure 3](/iaifi-research-blog/figures/2407_03524/figure_3.png)

For physics, better jet tagging directly improves the LHC's ability to identify rare processes — including potential signatures of new particles beyond the Standard Model. Every percentage point of classification accuracy translates into sharper physics reach. At the HL-LHC, where data rates become almost incomprehensible, computational efficiency isn't just convenient — it's necessary.

For AI research, the deeper lesson is about **representation learning** — the idea that how you organize data before training can matter as much as the model itself. Investing in the feature space, using transformers for local particle relationships and autoencoders for global jet properties, can substitute for brute-force model scaling. A well-structured feature space enables interpretable models that researchers can actually interrogate — increasingly important as "black box" concerns face greater scrutiny.

> **Bottom Line:** By pairing a point cloud transformer with a CNN autoencoder to reorganize jet data before classification, this work matches state-of-the-art accuracy with a simpler, more interpretable model — a template for efficient AI at the extreme data rates of next-generation colliders.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges attention-based deep learning from NLP with the specific geometric structure of particle jets, showing that cross-domain architectural borrowing can yield efficient, physics-grounded solutions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The framework demonstrates that representation engineering — constructing a separable feature space through parallel transformer and autoencoder streams — can reduce model complexity without sacrificing classification performance, a broadly applicable principle for high-dimensional data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Improved jet tagging accuracy directly sharpens physicists' ability to identify rare particle decays and probe physics beyond the Standard Model, making each collision event more informationally valuable.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend the framework to finer-grained flavor tagging, anomaly detection for new physics searches, and real-time trigger integration at the HL-LHC; the full methodology is described in the authors' paper from the University of Puerto Rico, Mayaguez.</span></div></div>
</div>
