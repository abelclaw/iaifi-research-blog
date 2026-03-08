---
abstract: What are the symmetries of a dataset? Whereas the symmetries of an individual
  data element can be characterized by its invariance under various transformations,
  the symmetries of an ensemble of data elements are ambiguous due to Jacobian factors
  introduced while changing coordinates. In this paper, we provide a rigorous statistical
  definition of the symmetries of a dataset, which involves inertial reference densities,
  in analogy to inertial frames in classical mechanics. We then propose SymmetryGAN
  as a novel and powerful approach to automatically discover symmetries using a deep
  learning method based on generative adversarial networks (GANs). When applied to
  Gaussian examples, SymmetryGAN shows excellent empirical performance, in agreement
  with expectations from the analytic loss landscape. SymmetryGAN is then applied
  to simulated dijet events from the Large Hadron Collider (LHC) to demonstrate the
  potential utility of this method in high energy collider physics applications. Going
  beyond symmetry discovery, we consider procedures to infer the underlying symmetry
  group from empirical data.
arxivId: '2112.05722'
arxivUrl: https://arxiv.org/abs/2112.05722
authors:
- Krish Desai
- Benjamin Nachman
- Jesse Thaler
concepts:
- generative adversarial networks
- symmetry discovery
- group theory
- inertial reference density
- automated discovery
- density estimation
- collider physics
- likelihood ratio
- data augmentation
- equivariant neural networks
- simulation-based inference
- anomaly detection
figures:
- /iaifi-research-blog/figures/2112_05722/figure_1.png
- /iaifi-research-blog/figures/2112_05722/figure_1.png
- /iaifi-research-blog/figures/2112_05722/figure_2.png
- /iaifi-research-blog/figures/2112_05722/figure_2.png
- /iaifi-research-blog/figures/2112_05722/figure_3.png
- /iaifi-research-blog/figures/2112_05722/figure_3.png
pdfUrl: https://arxiv.org/pdf/2112.05722v2
published: '2021-12-10T18:25:53+00:00'
theme: Theoretical Physics
title: 'SymmetryGAN: Symmetry Discovery with Deep Learning'
wordCount: 1172
---

## The Big Picture

Imagine you have a photograph of a snowflake. You can immediately see its sixfold rotational symmetry: rotate it 60 degrees, and it looks identical. Now imagine you have a thousand photographs of different snowflakes. What are the symmetries *of that collection*?

That question turns out to be surprisingly subtle, and answering it rigorously matters for everything from particle physics to machine learning.

Symmetries are the skeleton of physics. They determine which quantities stay constant, shape how physical systems evolve, and reveal hidden patterns in data. Physicists have long known how to exploit symmetries once found, but *finding* them has remained a largely human endeavor, guided by intuition and prior knowledge. What if a neural network could do it instead?

That's what Jesse Thaler (MIT/IAIFI), Benjamin Nachman, and Krish Desai set out to do. Their paper introduces **SymmetryGAN**, a deep learning framework that automatically discovers the symmetries lurking in a dataset, with no prior physics knowledge required.

> **Key Insight:** The symmetries of a statistical dataset are fundamentally different from the symmetries of individual data points, and correctly defining them requires an "inertial reference density," a conceptual move borrowed directly from classical mechanics.

## How It Works

The first challenge is definitional. When you transform a single data point (say, rotating a vector), the symmetry condition is straightforward: does it look the same afterward?

But when you have a *distribution* of data points, a whole cloud of measurements, the problem gets trickier. Transforming the coordinate system introduces **Jacobian factors**, mathematical correction terms that account for how much space gets stretched or compressed by the transformation. These factors change the apparent density of the data, so a transformation can *appear* to preserve your dataset simply by compressing or stretching space in clever ways. That's not a real symmetry. It's a coordinate trick.

![Figure 1](figure:1)

To solve this, the researchers borrow a concept from physics: the **inertial frame**, a vantage point that isn't accelerating, where physical laws take their simplest form. They introduce an *inertial reference density*, a fixed reference distribution that anchors what counts as a genuine symmetry transformation versus a mere reparametrization. A transformation qualifies as a true symmetry only if it maps the target dataset to itself *and* maps the reference density to itself, ruling out Jacobian cheats.

With this definition in hand, the paper turns to the learning framework. SymmetryGAN repurposes the machinery of **Generative Adversarial Networks (GANs)**, the familiar two-player game where a *generator* tries to produce outputs indistinguishable from real data while a *discriminator* tries to tell real from fake.

In a standard GAN, the generator maps random noise to realistic data. SymmetryGAN flips this: the generator maps *the dataset to itself*. A well-trained generator that successfully fools the discriminator has learned a transformation that makes the data statistically indistinguishable from the original, which is precisely what it means to be a symmetry.

Training proceeds in three stages:

1. The **generator** _g_ applies a parameterized transformation to samples from the target dataset.
2. The **discriminator** _d_ tries to distinguish transformed samples from real ones.
3. The inertial constraint forces _g_ to also map the reference density back to itself, preventing trivial solutions.

## Why It Matters

The researchers first validated SymmetryGAN on controlled examples using **Gaussian distributions**, bell-curve-shaped probability clouds where the correct symmetry answers are known analytically. A one-dimensional Gaussian is symmetric under reflection; SymmetryGAN finds it. A circular two-dimensional Gaussian is symmetric under all rotations (the **SO(2) group**), and SymmetryGAN recovers the full rotation group. Gaussian mixtures with discrete symmetries are also correctly identified.

The team also derived analytic expressions for the loss landscape that the network navigates during training and showed that empirical behavior matches theoretical predictions. That kind of interpretability is rare in deep learning.

![Figure 2](figure:2)

The real test came from particle physics. The researchers applied SymmetryGAN to simulated **dijet events** from the Large Hadron Collider, collisions that produce two back-to-back jets of particles, analyzed in a high-dimensional space of jet properties. SymmetryGAN searched for symmetries within a subspace parameterized by SO(2) × SO(2) transformations and identified the symmetry structure without being told what to look for.

The paper also sketches a path toward **symmetry inference**: not just finding invariant transformations, but identifying which formal mathematical group they belong to. The authors are upfront that this remains an open problem, but they outline concrete first steps.

![Figure 3](figure:3)

What does this buy you? On the physics side, automated symmetry discovery could accelerate the search for hidden structure in experimental data, whether from LHC collisions, condensed matter systems, or cosmological surveys. Symmetries that nobody thought to look for might surface directly from measurements.

On the machine learning side, importing concepts like inertial frames, Jacobian factors, and group theory into algorithm design makes these methods more principled. Discovered symmetries can augment training data, inform **equivariant architectures** (neural networks built to respect known symmetries), and compress generative models.

> **Bottom Line:** SymmetryGAN turns symmetry discovery into a learning problem, using GANs to find the mathematical transformations that leave a dataset statistically unchanged, with rigorous theoretical grounding and successful application to particle physics data.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** SymmetryGAN imports the physics concept of inertial reference frames into machine learning, creating a rigorous bridge between statistical learning theory and the group-theoretic language of fundamental physics.
- **Impact on Artificial Intelligence:** The paper establishes a differentiable, GAN-based framework for unsupervised symmetry discovery that is more general and theoretically grounded than prior reinforcement learning approaches, with analytic understanding of its loss landscape.
- **Impact on Fundamental Interactions:** SymmetryGAN was applied to LHC dijet event data, showing it can discover hidden symmetry structure in high-energy physics datasets without prior assumptions about the underlying physics.
- **Outlook and References:** Future work will focus on scaling symmetry inference to identify specific symmetry groups from data and extending the method to higher-dimensional and continuous symmetry spaces; the paper is available at [arXiv:2112.05722](https://arxiv.org/abs/2112.05722).

## Original Paper Details
- **Title:** SymmetryGAN: Symmetry Discovery with Deep Learning
- **arXiv ID:** 2112.05722
- **Authors:** ["Krish Desai", "Benjamin Nachman", "Jesse Thaler"]
- **Abstract:** What are the symmetries of a dataset? Whereas the symmetries of an individual data element can be characterized by its invariance under various transformations, the symmetries of an ensemble of data elements are ambiguous due to Jacobian factors introduced while changing coordinates. In this paper, we provide a rigorous statistical definition of the symmetries of a dataset, which involves inertial reference densities, in analogy to inertial frames in classical mechanics. We then propose SymmetryGAN as a novel and powerful approach to automatically discover symmetries using a deep learning method based on generative adversarial networks (GANs). When applied to Gaussian examples, SymmetryGAN shows excellent empirical performance, in agreement with expectations from the analytic loss landscape. SymmetryGAN is then applied to simulated dijet events from the Large Hadron Collider (LHC) to demonstrate the potential utility of this method in high energy collider physics applications. Going beyond symmetry discovery, we consider procedures to infer the underlying symmetry group from empirical data.
