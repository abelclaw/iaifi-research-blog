---
abstract: Autoencoders have been proposed as a powerful tool for model-independent
  anomaly detection in high-energy physics. The operating principle is that events
  which do not belong to the space of training data will be reconstructed poorly,
  thus flagging them as anomalies. We point out that in a variety of examples of interest,
  the connection between large reconstruction error and anomalies is not so clear.
  In particular, for data sets with nontrivial topology, there will always be points
  that erroneously seem anomalous due to global issues. Conversely, neural networks
  typically have an inductive bias or prior to locally interpolate such that undersampled
  or rare events may be reconstructed with small error, despite actually being the
  desired anomalies. Taken together, these facts are in tension with the simple picture
  of the autoencoder as an anomaly detector. Using a series of illustrative low-dimensional
  examples, we show explicitly how the intrinsic and extrinsic topology of the dataset
  affects the behavior of an autoencoder and how this topology is manifested in the
  latent space representation during training. We ground this analysis in the discussion
  of a mock "bump hunt" in which the autoencoder fails to identify an anomalous "signal"
  for reasons tied to the intrinsic topology of $n$-particle phase space.
arxivId: '2102.08380'
arxivUrl: https://arxiv.org/abs/2102.08380
authors:
- Joshua Batson
- C. Grace Haaf
- Yonatan Kahn
- Daniel A. Roberts
concepts:
- autoencoders
- anomaly detection
- topological obstructions
- manifold learning
- phase space topology
- dimensionality reduction
- new physics searches
- representation learning
- out-of-distribution detection
- inductive bias interpolation
- collider physics
- signal detection
- jet physics
figures:
- /iaifi-research-blog/figures/2102_08380/figure_1.png
- /iaifi-research-blog/figures/2102_08380/figure_1.png
- /iaifi-research-blog/figures/2102_08380/figure_2.png
- /iaifi-research-blog/figures/2102_08380/figure_2.png
- /iaifi-research-blog/figures/2102_08380/figure_3.png
- /iaifi-research-blog/figures/2102_08380/figure_3.png
pdfUrl: https://arxiv.org/pdf/2102.08380v2
published: '2021-02-16T19:00:00+00:00'
theme: Theoretical Physics
title: Topological Obstructions to Autoencoding
wordCount: 1115
---

## The Big Picture

Imagine trying to flatten a map of the Earth. No matter how clever your projection, you'll always distort something. Greenland balloons to the size of Africa, Antarctica stretches impossibly wide, and the poles become lines instead of points. This isn't a flaw in your technique; it's a mathematical fact about representing a curved, closed surface on a flat plane.

Now imagine building a machine to find rare, exotic particles in a collider experiment. You'd probably reach for an autoencoder, a neural network that compresses data into a compact representation, then reconstructs it. Train it on ordinary "background" physics events, and when something weird shows up, the autoencoder will fail to reconstruct it cleanly, flagging it as an anomaly. Physicists have used this approach in searches for new particles, hoping to spot signals that defy the Standard Model.

There's just one problem. The same mathematics that ruins your flat map also ruins your autoencoder. The authors of this paper show that the *shape* of physics data (how it curves and connects in mathematical space, not just how many dimensions it has) creates unavoidable obstructions to autoencoder-based anomaly detection.

> **Key Insight:** When your data lives on a curved, closed surface in mathematical space (like a sphere), an autoencoder is mathematically forced to either distort the data or misclassify perfectly normal events as anomalies. No architecture trick fixes this.

## How It Works

The paper identifies a deep tension in how physicists use autoencoders. **Phase space**, the mathematical space of all possible particle momenta and energies in a collision, isn't flat. For $n$ final-state particles, it has the topology of a sphere, $S^{3n-4}$: a curved, closed surface, not a simple box in $\mathbb{R}^k$.

An autoencoder works by squeezing data through a narrow **latent space** (think of summarizing a detailed city map with just a handful of coordinates) then expanding it back out. If training data lives on a sphere, the autoencoder must map points on that sphere into a flat latent space and back. But you can't continuously map a sphere onto a line without tearing it somewhere. The autoencoder, as a composition of continuous functions, is bound by the same topological laws that plague mapmakers.

![Figure 1](figure:1)

The authors make this concrete through a sequence of increasingly complex examples. The simplest is the unit circle $S^1$, every point at exactly distance 1 from a center, like the rim of a wheel. A single angle $\phi$ labels every point, but $\phi$ and $\phi + 2\pi$ are the same point: the angle wraps around.

When an autoencoder compresses the circle onto a line, it must "cut" the circle somewhere. Points near that cut are genuine neighbors on the circle but end up far apart in latent space, so the autoencoder flags them as badly reconstructed outliers. These are false positives, plain and simple.

![Figure 2](figure:2)

The researchers trained actual autoencoders on these toy problems and watched this failure unfold. On a circle dataset, the network reliably produces a "dead zone" where reconstruction error spikes, not because those points are rare, but purely because of topology. The dead zone shifts with random initialization but never disappears.

The problems get worse in higher dimensions:

- **The 2-sphere** ($S^2$) exhibits the same mapping failure, now with a larger distorted region around the "pole" of the projection.
- **The double cone** (two sheets joined at a point) shows how sharp geometric features and non-uniform sampling further confuse the autoencoder.
- **3-body phase space**, directly relevant to collider physics, inherits spherical topology and displays all the same pathologies.

![Figure 3](figure:3)

There's a second failure mode cutting in the opposite direction. Neural networks have a strong **inductive bias** toward local interpolation: they excel at smoothly filling gaps between nearby training examples. If an anomaly signal is a rare but localized cluster of events (like Higgs decays concentrated at a specific **invariant mass**), the autoencoder may reconstruct those events *too well*. It interpolates across the gap, treating the signal as a natural extension of the background, and assigns a low reconstruction error. That's exactly the wrong answer.

![Figure 4](figure:4)

The paper illustrates this with a mock **bump hunt**, a standard search technique where physicists look for an unexpected spike in event counts at a particular energy, potentially signaling an unknown particle. The autoencoder fails to flag the signal because the signal events live on a topologically equivalent submanifold that the network confidently interpolates over.

![Figure 5](figure:5)

## Why It Matters

This is a precise, mathematically grounded critique of a popular class of tools. Autoencoders have been applied broadly in particle physics, from jet substructure studies to new-physics searches, often with the implicit assumption that high reconstruction error means "anomalous event." The topological analysis here shows that assumption breaks in predictable, systematic ways depending on the shape of the data manifold, not on sample size or network capacity.

The same tension shows up wherever data lives on a non-Euclidean manifold: molecular conformations in drug discovery, directional data in geophysics, orientation spaces in robotics. The paper points toward several remedies. **Variational autoencoders** with latent-space priors shaped to match the data topology could help. So could topology-aware anomaly scores that account for expected distortion, or combining autoencoders with density estimation methods less sensitive to global manifold structure.

Plenty of questions remain. How much does this failure mode affect real LHC searches currently underway? Can one systematically map the "dead zones" for specific physics processes before running a search? The authors' framework of studying low-dimensional examples carefully, then extrapolating to full phase space, gives a concrete way to start answering these.

> **Bottom Line:** Autoencoders can't escape topology. The same mathematics that prevents a perfect flat map of Earth prevents autoencoders from faithfully representing curved data manifolds. Physicists searching for new particles with these tools may be chasing topological artifacts or missing real signals hiding in plain sight.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work applies algebraic topology and differential geometry to diagnose neural network failure modes in particle physics, building a rigorous bridge between pure mathematics, machine learning theory, and experimental high-energy physics.

- **Impact on Artificial Intelligence:** The paper identifies a fundamental, architecture-independent limitation of autoencoder-based anomaly detection when data has non-trivial topology, and provides a principled diagnostic framework using low-dimensional examples to anticipate these failures at scale.

- **Impact on Fundamental Interactions:** By showing that $n$-particle phase space has spherical topology that systematically undermines autoencoder anomaly detection, this research challenges model-independent new-physics searches at colliders and motivates topologically informed analysis strategies.

- **Outlook and References:** Future work should explore topology-aware latent representations and anomaly scores that hold up under manifold geometry; the full analysis is available at [arXiv:2102.08380](https://arxiv.org/abs/2102.08380) (MIT-CTP/5264).
