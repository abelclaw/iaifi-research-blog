---
abstract: Employing equivariance in neural networks leads to greater parameter efficiency
  and improved generalization performance through the encoding of domain knowledge
  in the architecture; however, the majority of existing approaches require an a priori
  specification of the desired symmetries. We present a neural network architecture,
  Linear Group Networks (LGNs), for learning linear groups acting on the weight space
  of neural networks. Linear groups are desirable due to their inherent interpretability,
  as they can be represented as finite matrices. LGNs learn groups without any supervision
  or knowledge of the hidden symmetries in the data and the groups can be mapped to
  well known operations in machine learning. We use LGNs to learn groups on multiple
  datasets while considering different downstream tasks; we demonstrate that the linear
  group structure depends on both the data distribution and the considered task.
arxivId: '2305.18552'
arxivUrl: https://arxiv.org/abs/2305.18552
authors:
- Emmanouil Theodosis
- Karim Helwani
- Demba Ba
concepts:
- linear group learning
- equivariant neural networks
- group theory
- weight space symmetry
- symmetry preservation
- cyclic group construction
- geometric deep learning
- interpretability
- convolutional networks
- representation learning
- self-supervised learning
- sparse models
figures:
- /iaifi-research-blog/figures/2305_18552/figure_1.png
- /iaifi-research-blog/figures/2305_18552/figure_1.png
- /iaifi-research-blog/figures/2305_18552/figure_2.png
- /iaifi-research-blog/figures/2305_18552/figure_2.png
- /iaifi-research-blog/figures/2305_18552/figure_3.png
- /iaifi-research-blog/figures/2305_18552/figure_3.png
pdfUrl: https://arxiv.org/pdf/2305.18552v1
published: '2023-05-29T18:29:11+00:00'
theme: Foundational AI
title: Learning Linear Groups in Neural Networks
wordCount: 1120
---

## The Big Picture

Imagine designing a robot arm without knowing in advance how many joints it needs, then watching it figure out its own structure just by handling thousands of different objects. That's roughly the challenge at the heart of modern equivariant neural networks — and until recently, nobody had a clean solution.

Neural networks benefit enormously from **symmetry**. When a network "knows" that rotating an image of a cat still shows a cat, it can share what it learned across orientations, train faster, and generalize better. This concept — **equivariance**, meaning the network's output changes in a predictable, consistent way when its input is transformed — underlies everything from image recognition to cutting-edge physics simulators.

The catch: someone has to tell the network *which* symmetries matter. For images, it's obvious that shifting a photo left or right shouldn't change what's in it. For molecular dynamics, knowing a molecule looks the same from any angle helps. But for a novel dataset where the relevant symmetries are unknown? You're stuck guessing — or ignoring symmetry altogether and leaving performance on the table.

Researchers at Harvard and Amazon Web Services now have a different answer. Their framework, **Linear Group Networks (LGNs)**, lets a network discover its own symmetries directly from data, with no prior knowledge of what those symmetries might be — and the discovered symmetries are interpretable enough to recognize once found.

> **Key Insight:** LGNs automatically learn the symmetry structure hidden in a dataset by discovering elements of the *general linear group* acting on neural network weights — and the learned groups turn out to correspond to recognizable operations like rotations and median filtering.

## How It Works

The central idea starts with a mathematical object called the **general linear group**, GL_d(K) — the set of all invertible d×d matrices over a field K (think: square grids of numbers where every transformation can be undone). This is a deliberately expansive umbrella: rotations, reflections, shears, and many other transformations all live inside it as subgroups. Rather than picking a subgroup in advance, LGNs learn a single matrix generator and use it to build a **cyclic group** — a set of transformations obtained by repeatedly applying that generator.

Here's the concrete construction:

1. The network learns a matrix **A** (the group generator) alongside its normal weights.
2. A finite cyclic group is constructed as {I, A, A², A³, ..., A^(n-1)}, where A^n = I (the identity).
3. This group acts on the **weight space** of the network — the filters themselves, not the input data directly.
4. The result is a set of filters that are geometrically related to each other by the learned transformation.

![Figure 1](/iaifi-research-blog/figures/2305_18552/figure_1.png)

This **weight-space action** — applying the group transformation to the network's learned filters rather than to raw input images — is a deliberate design choice. Keeping the transformations in this moderate-dimensional space makes the network both interpretable and computationally efficient.

The authors use **unfolded networks** — architectures built by unrolling an iterative problem-solving algorithm into a fixed sequence of layers — because these networks reconstruct an approximation of the input at every layer. This keeps the filters tethered to the data space where human inspection is possible.

![Figure 2](/iaifi-research-blog/figures/2305_18552/figure_1.png)

Training is entirely self-supervised with respect to the group. The network simultaneously learns the weights and the group generator, with no labels indicating what symmetries are present. The only signal comes from the downstream task itself.

![Figure 3](/iaifi-research-blog/figures/2305_18552/figure_2.png)

What does the network actually discover? On natural image datasets, the learned group actions cluster into recognizable categories:

- **Skew-symmetric** actions — transformations with a strong rotational character.
- **Toeplitz** matrix structures — arising in convolution and sliding-window operations.
- **Multi-scale** actions — capturing coarse-to-fine structure reminiscent of wavelet decompositions.

Through ablation studies, the authors show that certain filter sets have group actions with high correlation to compositions of rotations and **median filtering**, the latter closely related to the pooling operations ubiquitous in modern deep learning.

![Figure 4](/iaifi-research-blog/figures/2305_18552/figure_2.png)

One of the paper's sharpest findings: the learned group structure depends on *both* the data distribution *and* the task. Training the same architecture on the same images for different objectives — reconstruction versus classification — produces different groups. Symmetry is not a fixed property of a dataset. It's a joint property of the data and what you're trying to do with it.

![Figure 5](/iaifi-research-blog/figures/2305_18552/figure_3.png)

## Why It Matters

The broader stakes extend well beyond image classification. Across scientific domains — particle physics, cosmology, protein folding, materials discovery — researchers embed known symmetries into neural architectures to improve sample efficiency and physical plausibility. But known symmetries are the easy case.

The harder, more common case is precisely the situation LGNs target: datasets where the relevant symmetry structure is unknown, approximate, or emergent from a combination of domain and measurement process. LGNs offer a path toward automatic symmetry discovery that produces interpretable results.

Because the learned groups are finite matrices, you can inspect them. You can correlate them with known operations. You can ask whether the symmetry the network found corresponds to something physically meaningful — and if it does, that's a genuine scientific insight, not just an engineering convenience.

The authors frame this explicitly: their goal isn't just to build a better architecture, but to use LGNs as a *probe* for understanding what symmetries matter in real-world data. Open questions remain — how to scale to very high-dimensional weight spaces, how to handle continuous rather than discrete groups, whether discovered symmetries transfer across datasets — but the foundation is laid.

![Figure 6](/iaifi-research-blog/figures/2305_18552/figure_3.png)

> **Bottom Line:** Linear Group Networks prove that neural networks can discover their own symmetries from scratch, and those symmetries are interpretable — mapping onto operations researchers already know and use. This reframes symmetry not as a design choice baked into architecture, but as something a sufficiently flexible model can learn to need.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges mathematical group theory and practical deep learning, showing that abstract algebraic structures — cyclic subgroups of GL_d — can be learned end-to-end and mapped onto physically interpretable operations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">LGNs remove a fundamental bottleneck in equivariant deep learning by enabling unsupervised discovery of symmetry groups, opening equivariant architectures to domains where symmetries are unknown in advance.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The framework provides a principled tool for probing hidden symmetries in scientific datasets, with direct applications to physics problems where the symmetry group of the data is itself an open question.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend LGNs to continuous groups and higher-dimensional weight spaces, enabling symmetry discovery in large-scale physics simulations; the paper is available on arXiv from Theodosis, Helwani, and Ba at Harvard University.</span></div></div>
</div>
