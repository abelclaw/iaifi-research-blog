---
abstract: In state-of-the-art self-supervised learning (SSL) pre-training produces
  semantically good representations by encouraging them to be invariant under meaningful
  transformations prescribed from human knowledge. In fact, the property of invariance
  is a trivial instance of a broader class called equivariance, which can be intuitively
  understood as the property that representations transform according to the way the
  inputs transform. Here, we show that rather than using only invariance, pre-training
  that encourages non-trivial equivariance to some transformations, while maintaining
  invariance to other transformations, can be used to improve the semantic quality
  of representations. Specifically, we extend popular SSL methods to a more general
  framework which we name Equivariant Self-Supervised Learning (E-SSL). In E-SSL,
  a simple additional pre-training objective encourages equivariance by predicting
  the transformations applied to the input. We demonstrate E-SSL's effectiveness empirically
  on several popular computer vision benchmarks, e.g. improving SimCLR to 72.5% linear
  probe accuracy on ImageNet. Furthermore, we demonstrate usefulness of E-SSL for
  applications beyond computer vision; in particular, we show its utility on regression
  problems in photonics science. Our code, datasets and pre-trained models are available
  at https://github.com/rdangovs/essl to aid further research in E-SSL.
arxivId: '2111.00899'
arxivUrl: https://arxiv.org/abs/2111.00899
authors:
- Rumen Dangovski
- Li Jing
- Charlotte Loh
- Seungwook Han
- Akash Srivastava
- Brian Cheung
- Pulkit Agrawal
- Marin Soljačić
concepts:
- self-supervised learning
- contrastive learning
- representation learning
- equivariant neural networks
- equivariant pretext task
- data augmentation
- symmetry preservation
- group theory
- transfer learning
- multi-task learning
- regression
- scientific workflows
figures:
- /iaifi-research-blog/figures/2111_00899/figure_1.png
- /iaifi-research-blog/figures/2111_00899/figure_1.png
- /iaifi-research-blog/figures/2111_00899/figure_2.png
- /iaifi-research-blog/figures/2111_00899/figure_2.png
- /iaifi-research-blog/figures/2111_00899/figure_3.png
- /iaifi-research-blog/figures/2111_00899/figure_3.png
pdfUrl: https://arxiv.org/pdf/2111.00899v2
published: '2021-10-28T17:21:33+00:00'
theme: Foundational AI
title: Equivariant Contrastive Learning
wordCount: 897
---

## The Big Picture

Think about how you recognize a dog. Whether it's upright, flipped on its side, or rotated in a photo, you still know it's a dog. That's **invariance**: your brain ignores certain transformations. But imagine instead you're trying to figure out *which way* a dog is oriented. Now you need to actually *track* that rotation, not ignore it. That's a fundamentally different kind of knowledge, and a richer one.

Modern AI systems learn **representations** (compact internal summaries of what they observe) through **self-supervised learning**, a technique where a model trains itself on unlabeled data by solving cleverly designed puzzles. The dominant approach enforces invariance: treat a photo and its flipped, color-shifted version as identical. This produces powerful features. But a team at MIT asked: what if some transformations are too informative to throw away?

Their answer is **Equivariant Self-Supervised Learning (E-SSL)**, a framework that teaches models to be invariant to some transformations while staying *sensitive* to others in a structured, predictable way. The result is representations that outperform state-of-the-art methods on standard benchmarks and open up new applications in physics.

> **Key Insight:** Invariance is just a special case of a broader property called equivariance. By training models to *track* certain transformations rather than ignore them, E-SSL learns more informative representations, improving ImageNet accuracy and enabling new applications in photonics science.

## How It Works

The core idea rests on **equivariance**: when you transform an input, the representation transforms in a correspondingly predictable way. Invariance is the trivial case where the representation doesn't change at all. Non-trivial equivariance means the representation *moves* in a structured, knowable way.

The researchers started with a diagnostic experiment. They took SimCLR, a popular invariant SSL method, and tested what happened when they made it either invariant or sensitive to a second transformation on top of standard random cropping.

![Figure 1](/iaifi-research-blog/figures/2111_00899/figure_1.png)

The results split cleanly. For **horizontal flips** and **grayscale**, invariance helped. But for **four-fold rotations**, **vertical flips**, **2×2 jigsaws**, **four-fold Gaussian blurs**, and **color inversions**, invariance actively hurt, while sensitivity to those same transformations improved performance. The pattern: if invariance to a transformation is harmful, equivariance to it tends to help.

E-SSL captures this with a two-part training objective:

1. **Standard invariant SSL loss** (e.g., SimCLR's contrastive loss, a scoring function that rewards grouping different augmented views of the same image together): train the **encoder**, the network component that compresses an image into a representation, to produce similar outputs for different views of the same image.
2. **Equivariance prediction loss**: a lightweight prediction head that identifies *which transformation* was applied, forcing the encoder to retain transformation information rather than discard it.

No architectural overhaul required. The prediction head is a simple classifier over discrete transformation classes, such as which of four rotation angles was applied. Minimal overhead; significant impact on what the encoder learns.

![Figure 2](/iaifi-research-blog/figures/2111_00899/figure_1.png)

The team applied E-SSL to four popular SSL methods (SimCLR, BYOL, Barlow Twins, and VICReg) and found consistent gains. On **ImageNet**, a standard large-scale image classification benchmark, evaluated with a **linear probe** (a frozen representation tested with a single trainable layer on top), E-SSL pushed SimCLR to **72.5%** accuracy. In a field where gains come slowly, that's a meaningful improvement.

## Why It Matters

The deeper claim here is that human knowledge about transformations shouldn't just specify what to ignore; it should actively shape the structure of learned representations. The symmetries and near-symmetries of a problem are often its most informative features. E-SSL turns that intuition into a training signal.

![Figure 3](/iaifi-research-blog/figures/2111_00899/figure_2.png)

The photonics application makes this concrete. The team applied E-SSL to regression tasks in photonics science, predicting physical properties of materials from simulation data. Domain knowledge tells you which transformations preserve or predictably alter the output. Encoding those as equivariance targets rather than invariances improved regression performance. The framework transfers to scientific domains where labeled data is scarce and structure is rich.

Many scientific problems involve data with known symmetries, whether rotational, translational, or **gauge** symmetries (the abstract symmetries underlying the fundamental forces of nature), that current SSL methods either ignore or discard. E-SSL offers a recipe for converting that structural knowledge into a training signal. The natural next steps include molecular property prediction, cosmological field reconstruction, and any domain where the geometry of the data is partially understood but labels are expensive.

> **Bottom Line:** E-SSL shows that the best self-supervised representations come not from maximally ignoring transformations, but from being selective: staying blind to some while staying sharp on others. A simple idea with significant empirical payoff and a clear path into physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">E-SSL connects representation learning theory to physics by applying equivariance, a concept central to fundamental physics, as a practical SSL training objective, with direct demonstrations on photonics regression tasks.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">By generalizing invariant SSL to an equivariant framework, E-SSL improves linear probe accuracy on ImageNet and consistently boosts SimCLR, BYOL, Barlow Twins, and VICReg with minimal architectural changes.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Domain-specific transformation knowledge in photonics science can be encoded as equivariance targets, improving sample efficiency and prediction accuracy for physical property regression from simulation data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending E-SSL to continuous transformation groups and other scientific domains with known symmetry structure; the paper appeared at ICLR 2022 with code and pretrained models available at github.com/rdangovs/essl.</span></div></div>
</div>
