---
abstract: 'Deep learning techniques have been increasingly applied to the natural
  sciences, e.g., for property prediction and optimization or material discovery.
  A fundamental ingredient of such approaches is the vast quantity of labelled data
  needed to train the model; this poses severe challenges in data-scarce settings
  where obtaining labels requires substantial computational or labor resources. Here,
  we introduce surrogate- and invariance-boosted contrastive learning (SIB-CL), a
  deep learning framework which incorporates three ``inexpensive'''' and easily obtainable
  auxiliary information sources to overcome data scarcity. Specifically, these are:
  1)~abundant unlabeled data, 2)~prior knowledge of symmetries or invariances and
  3)~surrogate data obtained at near-zero cost. We demonstrate SIB-CL''s effectiveness
  and generality on various scientific problems, e.g., predicting the density-of-states
  of 2D photonic crystals and solving the 3D time-independent Schrodinger equation.
  SIB-CL consistently results in orders of magnitude reduction in the number of labels
  needed to achieve the same network accuracies.'
arxivId: '2110.08406'
arxivUrl: https://arxiv.org/abs/2110.08406
authors:
- Charlotte Loh
- Thomas Christensen
- Rumen Dangovski
- Samuel Kim
- Marin Soljacic
concepts:
- contrastive learning
- self-supervised learning
- surrogate modeling
- data-scarce learning
- transfer learning
- symmetry preservation
- representation learning
- semi-supervised learning
- fine-tuning
- data augmentation
- embeddings
- inverse problems
figures:
- /iaifi-research-blog/figures/2110_08406/figure_1.png
- /iaifi-research-blog/figures/2110_08406/figure_1.png
- /iaifi-research-blog/figures/2110_08406/figure_2.png
- /iaifi-research-blog/figures/2110_08406/figure_2.png
- /iaifi-research-blog/figures/2110_08406/figure_3.png
- /iaifi-research-blog/figures/2110_08406/figure_3.png
pdfUrl: https://arxiv.org/pdf/2110.08406v1
published: '2021-10-15T23:08:24+00:00'
theme: Theoretical Physics
title: Surrogate- and invariance-boosted contrastive learning for data-scarce applications
  in science
wordCount: 1050
---

## The Big Picture

Imagine trying to teach a child to recognize dogs with only three photographs. Three examples won't cut it — the child needs hundreds before the concept clicks. Now scale that problem to physics: you want a neural network to predict the quantum properties of a material, but each calculation takes days of supercomputer time. You can afford, say, 50 labeled examples. That's it.

This is the brutal reality facing researchers applying deep learning to fundamental science. Unlike computer vision, where millions of labeled images can be crowdsourced from the internet, generating labeled data in physics means running expensive simulations or conducting painstaking experiments. Every data point costs real time and money.

A team at MIT's departments of Electrical Engineering, Computer Science, and Physics has developed **SIB-CL** (Surrogate- and Invariance-Boosted Contrastive Learning) — a framework that slashes the number of labeled examples needed to train accurate models by orders of magnitude.

> **Key Insight:** SIB-CL exploits three cheap, readily-available information sources — unlabeled data, physical symmetries, and approximate "surrogate" calculations — to teach neural networks about physical systems using a tiny fraction of the labeled data otherwise required.

## How It Works

The core insight is that even when precise labels are scarce, science problems are rarely information-starved. They come packaged with rich structural knowledge that conventional supervised learning ignores entirely. SIB-CL is designed to consume all of it.

![Figure 1](/iaifi-research-blog/figures/2110_08406/figure_1.png)

The framework draws on three auxiliary information sources:

1. **Unlabeled data** — raw inputs (say, the geometry of a photonic crystal) that haven't been paired with expensive computed outputs. These are essentially free to generate.
2. **Invariances and symmetries** — prior knowledge that certain transformations leave the label unchanged. If rotating a crystal by 90° doesn't change its optical properties, the model should know that upfront rather than learning it from scratch across thousands of examples.
3. **Surrogate data** — approximate labels computed using faster, cheaper methods. Not perfectly accurate, but capturing the essential structure at a fraction of the cost.

SIB-CL fuses these sources through a two-stage training pipeline. In the first stage, the network undergoes **contrastive pre-training** — a self-supervised technique where the model learns useful internal representations without any labeled answers. The specific method is **SimCLR**.

The model sees two differently-transformed versions of the same input and learns to place them close together in a shared representational space, while pushing representations of different inputs far apart. Crucially, the transformations aren't arbitrary — they're chosen to reflect the actual physical symmetries of the problem. A rotation that leaves a crystal's properties invariant becomes a principled training signal. The physics does the work.

![Figure 2](/iaifi-research-blog/figures/2110_08406/figure_1.png)

Interleaved with this contrastive step is **surrogate transfer learning**: the model pre-trains on the cheaper approximate dataset before fine-tuning on the small, precious set of high-fidelity labels. This gives the network's **encoder** — the component that transforms raw inputs into a compact internal representation — a meaningful head start. It arrives at fine-tuning already understanding the structure of the problem, even if the surrogate's answers aren't exact.

The final stage is conventional fine-tuning: a prediction head is attached to the pre-trained encoder and trained on the available accurate labels. Because the encoder already carries rich, physics-aware representations, it needs far fewer expensive examples to converge.

The team validated SIB-CL on two demanding test cases. First, predicting the **density-of-states (DOS)** of 2D photonic crystals — materials that control light propagation through periodic structure, with applications in lasers and optical computing. The input is the geometry of the crystal's unit cell (its smallest repeating structural building block); the output is a complex spectral function requiring full electromagnetic simulation to compute accurately.

Second, solving the **3D time-independent Schrödinger equation** for quantum systems — a central problem in quantum chemistry and materials design. In both cases, SIB-CL matched the accuracy of standard supervised learning while using orders of magnitude fewer labeled examples.

![Figure 3](/iaifi-research-blog/figures/2110_08406/figure_2.png)

## Why It Matters

The immediate practical payoff is real. Tasks that would require thousands of expensive simulations might now be feasible with dozens. That's the difference between a project taking months versus days, and between being accessible to a well-funded group versus a broader research community.

The deeper significance is conceptual. SIB-CL operationalizes a principle that physicists have always relied on but machine learning has historically ignored: science problems are not naked datasets. They come embedded in a web of known structure — symmetries, conservation laws, approximate solutions, limiting cases.

Every physics student learns that when you can't solve a hard problem, you solve an easier one first and work outward. SIB-CL formalizes exactly that strategy for neural networks. As AI becomes central to material discovery, drug design, and quantum simulation, frameworks like SIB-CL point toward a future where labeled-data scarcity no longer gates which scientific questions are computationally tractable.

Open questions remain. The current demonstrations focus on well-defined problems where symmetries are known analytically. Extending SIB-CL to messier domains — experimental data from telescopes or particle detectors — will require creative thinking about how to define useful invariances when the underlying symmetry group isn't clean. The approach also inherits contrastive learning's sensitivity to batch size and augmentation strategy.

> **Bottom Line:** SIB-CL shows that the rich structural knowledge embedded in physics problems — symmetries, approximate models, unlabeled structure — can be systematically harvested to reduce labeled-data requirements by orders of magnitude, making deep learning viable for some of science's most expensive computational problems.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits squarely at the AI-physics interface, translating principles from contrastive self-supervised learning into a framework that explicitly encodes physical symmetries and exploits the hierarchical structure of approximate versus exact scientific calculations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">SIB-CL advances the self-supervised learning toolkit by demonstrating that domain-specific invariances can substitute for generic image augmentations, yielding dramatically more data-efficient pre-training when those invariances are physically grounded.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By making accurate property prediction tractable with far fewer labeled simulations, the framework directly accelerates research in photonics and quantum mechanics — domains where simulation cost has long constrained what questions researchers can ask computationally.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will likely extend SIB-CL to experimental datasets and to problems where invariances must be discovered rather than specified; the full paper is available at arXiv:2203.01343.</span></div></div>
</div>
