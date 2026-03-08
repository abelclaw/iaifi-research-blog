---
abstract: In this paper, we present a method of embedding physics data manifolds with
  metric structure into lower dimensional spaces with simpler metrics, such as Euclidean
  and Hyperbolic spaces. We then demonstrate that it can be a powerful step in the
  data analysis pipeline for many applications. Using progressively more realistic
  simulated collisions at the Large Hadron Collider, we show that this embedding approach
  learns the underlying latent structure. With the notion of volume in Euclidean spaces,
  we provide for the first time a viable solution to quantifying the true search capability
  of model agnostic search algorithms in collider physics (i.e. anomaly detection).
  Finally, we discuss how the ideas presented in this paper can be employed to solve
  many practical challenges that require the extraction of physically meaningful representations
  from information in complex high dimensional datasets.
arxivId: '2208.05484'
arxivUrl: https://arxiv.org/abs/2208.05484
authors:
- Sang Eon Park
- Philip Harris
- Bryan Ostdiek
concepts:
- embeddings
- manifold learning
- dimensionality reduction
- anomaly detection
- optimal transport
- jet physics
- collider physics
- new physics searches
- representation learning
- volume-adjusted roc
- hyperbolic embedding
- metric distortion
- convolutional networks
- transformers
figures:
- /iaifi-research-blog/figures/2208_05484/figure_1.png
- /iaifi-research-blog/figures/2208_05484/figure_2.png
- /iaifi-research-blog/figures/2208_05484/figure_3.png
pdfUrl: https://arxiv.org/pdf/2208.05484v2
published: '2022-08-10T18:00:00+00:00'
theme: Experimental Physics
title: 'Neural Embedding: Learning the Embedding of the Manifold of Physics Data'
wordCount: 1270
---

## The Big Picture

Imagine trying to describe every possible way a jazz improvisation could sound. You could record every note, every beat, every subtle variation, but the resulting dataset would be enormous, and most of the "distance" between two performances would be buried in noise. What you really want is a map: a compact representation that preserves the musical relationships without drowning in irrelevant detail.

Physicists at the LHC face the same problem. When protons smash together at nearly the speed of light, they spray out cascades of particles called **jets**, chaotic-looking bursts of energy that carry deep structure from fundamental physics. A single collision event can involve dozens of particles with multiple properties, pushing raw data into spaces with hundreds of dimensions. The interesting structure, though, lives on a much lower-dimensional shape hiding inside that enormous space.

A team from MIT, Harvard, and IAIFI has built a neural network framework that finds that hidden shape and flattens it into something usable. Their method, **neural embedding**, learns to compress high-dimensional physics data into two or three dimensions while preserving the distances that physicists actually care about.

> **Key Insight:** By training a neural network to preserve physically meaningful distances between collider events, researchers can map complex jet data onto simple 2D maps and use the geometry of those maps to measure, for the first time, how broadly an anomaly detector actually searches.

## How It Works

The core idea starts with a way of measuring distance. Rather than working with raw particle lists, the team uses **Energy Mover's Distance (EMD)**, a metric borrowed from optimal transport theory. Think of it as measuring how much "work" it takes to rearrange one jet's energy pattern into another's. EMD captures genuine physical similarity: two jets that look different particle-by-particle but carry similar energy flows can still be close in EMD.

This is a richer distance than a pixel-by-pixel comparison, but it lives in a brutally high-dimensional space. With just 50 particles and 3 features each, the underlying geometry spans 150 dimensions.

The embedding pipeline works in three steps:

1. **Compute pairwise distances** between training events using EMD or another physics metric.
2. **Train a neural network** (either a CNN or Transformer, depending on the input representation) to map each event to a point in a low-dimensional target space, either Euclidean or Hyperbolic.
3. **Optimize the embedding** so that distances in the low-dimensional output match the original EMD distances as closely as possible, minimizing distortion.

![Figure 1](/iaifi-research-blog/figures/2208_05484/figure_1.png)

To test how faithfully the embedding preserves structure, the team built a "toy jet generator" with tunable parameters, a physics sandbox where the ground truth is known exactly. Jets could be 1-prong, 2-prong, or 4-prong (prongs are distinct energy clusters within a jet), with the parent particle's mass varied continuously. When embedded into 2D Euclidean space, jets with the same number of prongs clustered together naturally, and jets with similar masses sat near each other within each cluster. The network was never told about prong number or mass. It discovered these physical categories purely by learning the geometry.

Moving to realistic simulated LHC events (generated with Pythia and Delphes, standard particle physics simulation tools), the embedding continued to self-organize into physically meaningful regions. The team also explored **Hyperbolic embedding**, placing events in a curved, saddle-shaped space rather than a flat plane. The motivation is that jet showers have a hierarchical, tree-like structure, and hyperbolic geometry is well-suited to representing branching processes. The results confirmed that hyperbolic space captures jet structure with lower distortion in some regimes.

![Figure 2](/iaifi-research-blog/figures/2208_05484/figure_2.png)

## Why It Matters

The most significant application here isn't visualization. It's solving a long-standing measurement problem in collider physics. After decades of LHC operation, physicists have found nothing beyond the Higgs boson. The field is now betting heavily on **model-agnostic searches**, or anomaly detection: algorithms that flag unusual events without assuming what new physics should look like. But how do you evaluate an anomaly detector when you don't know what you're looking for?

Until now, there was no principled way to measure how broadly a given algorithm searches. The paper proposes a solution: the **area-adjusted ROC curve**. A standard ROC curve plots sensitivity against false-alarm rate; the area-adjusted version adds a geometric dimension by measuring coverage in embedded space. Once events are embedded in 2D, you can literally measure the area of the region an anomaly detector marks as "interesting."

An algorithm that flags only a tiny corner of the embedded event space has limited reach; one that covers a large area casts a wider net. The team showed this concretely by comparing two anomaly detection algorithms on the same dataset, revealing how their search regions differ in embedded space. Before this work, that comparison was impossible to quantify.

![Figure 3](/iaifi-research-blog/figures/2208_05484/figure_3.png)

There are practical advantages too. A single forward pass through the trained network produces an embedding, so it is embarrassingly parallel and fast enough to run inside an LHC trigger system, which must make keep-or-discard decisions on microsecond timescales. The compressed representation also enables data compression: reducing a 150-dimensional event to a 2D coordinate while retaining physically meaningful structure.

The comparison with off-the-shelf manifold learning methods like t-SNE and UMAP is worth spelling out. Those tools work well for exploration, but they don't produce a learned function that generalizes to new data. They must be re-run from scratch on every new batch. Neural embedding trains once and deploys continuously, a critical practical advantage at collider scale.

> **Bottom Line:** Neural embedding turns the abstract geometry of particle physics into literal geography, a 2D map where physical similarity becomes spatial proximity, and uses that map to solve the previously intractable problem of measuring how thoroughly an anomaly detector covers the space of possible new physics.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses representation learning from machine learning with optimal-transport metrics from theoretical physics, producing a tool that makes abstract geometric structures in collider data concretely visualizable and measurable.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The neural embedding framework shows that physics-informed distance metrics can supervise manifold learning more effectively than unsupervised methods like UMAP or t-SNE, with the added benefit of out-of-sample generalization.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By introducing the area-adjusted ROC curve, this paper provides the first quantitative framework for measuring the search reach of model-agnostic anomaly detection algorithms at the LHC, a foundational tool for the next era of new physics searches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include applying hyperbolic embeddings more broadly to jet substructure analysis and integrating real-time embedding into LHC trigger pipelines; the full paper is available at [arXiv:2208.05484](https://arxiv.org/abs/2208.05484).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Neural Embedding: Learning the Embedding of the Manifold of Physics Data</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2208.05484</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Sang Eon Park", "Philip Harris", "Bryan Ostdiek"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">In this paper, we present a method of embedding physics data manifolds with metric structure into lower dimensional spaces with simpler metrics, such as Euclidean and Hyperbolic spaces. We then demonstrate that it can be a powerful step in the data analysis pipeline for many applications. Using progressively more realistic simulated collisions at the Large Hadron Collider, we show that this embedding approach learns the underlying latent structure. With the notion of volume in Euclidean spaces, we provide for the first time a viable solution to quantifying the true search capability of model agnostic search algorithms in collider physics (i.e. anomaly detection). Finally, we discuss how the ideas presented in this paper can be employed to solve many practical challenges that require the extraction of physically meaningful representations from information in complex high dimensional datasets.</span></div></div>
</div>
