---
abstract: Dynamic Sparse Training (DST) methods achieve state-of-the-art results in
  sparse neural network training, matching the generalization of dense models while
  enabling sparse training and inference. Although the resulting models are highly
  sparse and theoretically less computationally expensive, achieving speedups with
  unstructured sparsity on real-world hardware is challenging. In this work, we propose
  a sparse-to-sparse DST method, Structured RigL (SRigL), to learn a variant of fine-grained
  structured N:M sparsity by imposing a constant fan-in constraint. Using our empirical
  analysis of existing DST methods at high sparsity, we additionally employ a neuron
  ablation method which enables SRigL to achieve state-of-the-art sparse-to-sparse
  structured DST performance on a variety of Neural Network (NN) architectures. Using
  a 90% sparse linear layer, we demonstrate a real-world acceleration of 3.4x/2.5x
  on CPU for online inference and 1.7x/13.0x on GPU for inference with a batch size
  of 256 when compared to equivalent dense/unstructured (CSR) sparse layers, respectively.
arxivId: '2305.02299'
arxivUrl: https://arxiv.org/abs/2305.02299
authors:
- Mike Lasby
- Anna Golubeva
- Utku Evci
- Mihai Nica
- Yani Ioannou
concepts:
- sparse models
- dynamic sparse training
- structured n:m sparsity
- neuron ablation
- scalability
- loss function design
- convolutional networks
- fine-tuning
- interpretability
- ensemble methods
figures:
- /iaifi-research-blog/figures/2305_02299/figure_1.png
- /iaifi-research-blog/figures/2305_02299/figure_1.png
- /iaifi-research-blog/figures/2305_02299/figure_2.png
pdfUrl: https://arxiv.org/pdf/2305.02299v4
published: '2023-05-03T17:48:55+00:00'
theme: Foundational AI
title: Dynamic Sparse Training with Structured Sparsity
wordCount: 1132
---

## The Big Picture

Imagine a library where most shelves are empty. In theory, you'd only need to visit a handful of spots to find every book. But if the books are scattered randomly, one here, three there, none in predictable locations, the librarian still has to check every shelf. The library is technically sparse, but finding anything takes as long as ever.

This paradox has dogged neural network compression for years. Researchers have gotten very good at training networks with 90% or more of their **weights** (the numerical values that determine how a model processes data) set to zero. This is called **sparse training**. Sparse models are theoretically cheaper to run: fewer calculations, less memory. But "theoretically cheaper" and "actually faster" are two different things.

When zero weights are scattered randomly, real hardware can't exploit the sparsity. CPUs and GPUs read data in orderly, predictable chunks. The library is mostly empty, but the librarian is still exhausted.

A team from the University of Calgary, MIT, Google DeepMind, and affiliated institutions has found a way to have it both ways. Their method, **Structured RigL (SRigL)**, trains neural networks that are both highly sparse *and* organized in a pattern hardware can actually exploit, with real-world speedups of up to 13x on GPU inference compared to conventional sparse formats.

> **Key Insight:** SRigL closes the gap between theoretical and practical efficiency by learning structured sparsity *during* training rather than imposing it afterward, letting the network adapt its weights to fit a hardware-friendly pattern.

## How It Works

SRigL builds on an existing algorithm called **RigL** (Rigged Lottery), a **Dynamic Sparse Training (DST)** method. Traditional pruning trains a full network first, then cuts weights. DST does it differently: sparsity is maintained throughout training. Weights are periodically pruned (smallest magnitude) and regrown (largest gradient magnitude), letting the network explore different sparse connectivity patterns over time. RigL consistently matches or beats dense models at 85–95% sparsity. The catch: its sparsity is *unstructured*, with surviving weights scattered at arbitrary positions.

SRigL adds one critical constraint, **constant fan-in**, meaning every neuron receives exactly the same number of incoming connections. Think of each neuron being allowed exactly 10 input wires, no more, no less. This creates fine-grained **N:M sparsity**: out of every M consecutive weights in a row, exactly N are nonzero. A GPU no longer hunts for random weight positions. It loads weights in predictable, contiguous blocks.

The training procedure runs in three stages:

1. **Sparse initialization**: The network starts with a random sparse mask satisfying constant fan-in.
2. **Dynamic mask updates**: At regular intervals, SRigL drops the smallest-magnitude weights per neuron and grows the largest-gradient-magnitude weights, always preserving fan-in.
3. **Neuron ablation**: Above ~90% sparsity, the authors discovered that standard RigL naturally kills entire neurons, zeroing all their incoming weights. SRigL makes this explicit, letting active neurons concentrate their fixed fan-in budget on the most useful connections.

![Figure 1](/iaifi-research-blog/figures/2305_02299/figure_1.png)

That third stage emerged from careful empirical analysis. At extreme sparsity, RigL was already doing neuron ablation, but implicitly and inefficiently. Making it explicit lets the algorithm lean into the behavior, and performance at extreme sparsity improved dramatically.

![Figure 2](/iaifi-research-blog/figures/2305_02299/figure_1.png)

There's a theoretical payoff too. The paper shows mathematically that constant fan-in layers have *lower variance in their output norms* compared to equally sparse but unstructured layers. Internal signals stay better-behaved during training, which contributes to more stable optimization.

## Why It Matters

The gap between algorithmic efficiency and real-world efficiency has long frustrated the compression community. Papers routinely report reductions in **FLOPs** (the basic arithmetic a model performs) that never translate to faster inference on actual hardware.

SRigL attacks this gap directly. On a 90% sparse linear layer, it achieves **3.4x speedup over dense** and **2.5x over unstructured sparse** on CPU for single-sample inference. On GPU with batch size 256, the gains are sharper: **1.7x over dense** and **13.0x over unstructured sparse**. These are wall-clock measurements, not theoretical FLOP counts.

![Figure 3](/iaifi-research-blog/figures/2305_02299/figure_2.png)

The practical stakes are growing. As AI models get larger and more expensive to deploy, techniques that make inference *genuinely* faster become essential. This is especially true for scientific applications like physics simulations, particle detector readouts, and gravitational wave analysis, where models must run at high throughput on constrained hardware. A method that delivers structured sparsity without sacrificing generalization opens doors that unstructured pruning has kept closed.

Open questions remain. The authors compare SRigL primarily on image classification; how constant fan-in transfers to transformers, diffusion models, or graph neural networks is still unexplored. The neuron ablation behavior at extreme sparsity also raises questions about what the surviving network topology represents, which could be worth investigating from an interpretability angle.

> **Bottom Line:** SRigL proves that structured sparsity doesn't require sacrificing accuracy. By learning structure and weights simultaneously, it delivers hardware-ready sparse networks with up to 13x real-world inference speedup over unstructured sparse formats.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">The work ties fundamental neural network theory (why constant fan-in reduces output-norm variance) to practical hardware engineering, connecting the kinds of questions that IAIFI's approach to AI for science is built around.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">SRigL sets a new bar for structured dynamic sparse training, showing that hardware-friendly sparsity patterns can be learned end-to-end without the accuracy penalty traditionally associated with structured pruning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Efficient sparse inference matters directly for physics experiments that need real-time AI on edge hardware, from trigger systems in particle detectors to fast gravitational wave classifiers where latency is mission-critical.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will likely extend constant fan-in structured sparsity to transformer architectures and probe theoretical connections between neuron ablation and network topology. The paper ([arXiv:2305.02299](https://arxiv.org/abs/2305.02299)) appeared as an ICLR 2024 conference paper.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Dynamic Sparse Training with Structured Sparsity</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2305.02299</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Mike Lasby", "Anna Golubeva", "Utku Evci", "Mihai Nica", "Yani Ioannou"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Dynamic Sparse Training (DST) methods achieve state-of-the-art results in sparse neural network training, matching the generalization of dense models while enabling sparse training and inference. Although the resulting models are highly sparse and theoretically less computationally expensive, achieving speedups with unstructured sparsity on real-world hardware is challenging. In this work, we propose a sparse-to-sparse DST method, Structured RigL (SRigL), to learn a variant of fine-grained structured N:M sparsity by imposing a constant fan-in constraint. Using our empirical analysis of existing DST methods at high sparsity, we additionally employ a neuron ablation method which enables SRigL to achieve state-of-the-art sparse-to-sparse structured DST performance on a variety of Neural Network (NN) architectures. Using a 90% sparse linear layer, we demonstrate a real-world acceleration of 3.4x/2.5x on CPU for online inference and 1.7x/13.0x on GPU for inference with a batch size of 256 when compared to equivalent dense/unstructured (CSR) sparse layers, respectively.</span></div></div>
</div>
