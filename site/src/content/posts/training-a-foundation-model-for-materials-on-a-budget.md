---
abstract: Foundation models for materials modeling are advancing quickly, but their
  training remains expensive, often placing state-of-the-art methods out of reach
  for many research groups. We introduce Nequix, a compact E(3)-equivariant potential
  that pairs a simplified NequIP design with modern training practices, including
  equivariant root-mean-square layer normalization and the Muon optimizer, to retain
  accuracy while substantially reducing compute requirements. Nequix has 700K parameters
  and was trained in 100 A100 GPU-hours. On the Matbench-Discovery and MDR Phonon
  benchmarks, Nequix ranks third overall while requiring a 20 times lower training
  cost than most other methods, and it delivers two orders of magnitude faster inference
  speed than the current top-ranked model. We release model weights and fully reproducible
  codebase at https://github.com/atomicarchitects/nequix.
arxivId: '2508.16067'
arxivUrl: https://arxiv.org/abs/2508.16067
authors:
- Teddy Koker
- Mit Kotak
- Tess Smidt
concepts:
- equivariant neural networks
- interatomic potentials
- materials discovery
- scalability
- budget-conscious training
- graph neural networks
- geometric deep learning
- molecular dynamics
- phonon properties
- symmetry preservation
- dynamic batching
- transfer learning
figures:
- /iaifi-research-blog/figures/2508_16067/figure_1.png
- /iaifi-research-blog/figures/2508_16067/figure_2.png
pdfUrl: https://arxiv.org/pdf/2508.16067v2
published: '2025-08-22T03:38:06+00:00'
theme: Foundational AI
title: Training a Foundation Model for Materials on a Budget
wordCount: 1112
---

## The Big Picture

Imagine trying to predict the properties of every possible material in the universe — how it conducts heat, whether it stays stable under pressure, how atoms vibrate within its crystal lattice. For decades, physicists relied on quantum mechanical calculations so computationally expensive that simulating a single material could take days on a supercomputer cluster. AI models that learn to predict how atoms interact — called interatomic potentials — promised to change that, making accurate predictions thousands of times faster. But there's a catch: training these AI models has become a competition for computing resources that only the biggest labs can afford to enter.

The latest generation of "foundation models" for materials — AI systems trained on vast databases of atomic structures — can cost tens of thousands of GPU-hours (hours of processing time on specialized graphics chips) to train. That's a barrier that shuts out most university research groups, national labs on tight budgets, and scientists in less-resourced parts of the world. The implicit assumption has been that better performance requires more compute. A team at MIT decided to challenge that assumption directly.

Researchers Teddy Koker, Mit Kotak, and Tess Smidt built **Nequix**: a compact AI model for predicting materials properties that achieves near-state-of-the-art accuracy at a fraction of the cost. It ranks third on major community benchmarks while requiring 20 times less compute than its competitors and running 100 times faster when making predictions.

> **Key Insight:** By combining a streamlined neural network architecture with modern optimization tricks borrowed from the machine learning speedrunning community, Nequix proves that efficiency and accuracy don't have to be in tension — and that cutting-edge materials science AI doesn't require a supercomputer budget.

## How It Works

The foundation of Nequix is an architecture called **E(3)-equivariant neural networks** — networks built with a mathematical guarantee that their predictions don't change when you rotate or reflect the input atomic structure. This is physically essential: a crystal of iron has the same energy whether you orient it north-south or east-west. The team built Nequix as a streamlined version of NequIP, an established equivariant architecture, stripping away complexity while preserving the physics that matters.

![Figure 1](/iaifi-research-blog/figures/2508_16067/figure_1.png)

The architecture changes are surgical. Two simplifications from recent literature reduced parameter count without sacrificing expressiveness: replacing species-specific self-connection layers with a single linear layer, and discarding unused non-scalar representations from the final layer. The team then added **equivariant RMSNorm** — a stabilizing technique that normalizes the network's internal signals, adapted to handle the directional quantities (vectors and tensors) that physics-aware networks must track. This stabilizes training and, crucially, plays well with the new optimizer they chose.

That optimizer is where things get interesting. Instead of the standard Adam optimizer used in virtually every deep learning workflow, the team adopted **Muon** — a recently proposed optimizer inspired by researchers who compete to train neural networks on benchmarks as fast as possible. Muon uses an algorithm from numerical linear algebra to ensure each weight update points in a unique direction, encouraging different neurons to learn genuinely distinct features. The result: Nequix reaches equivalent accuracy to Adam-trained models in just 60–70% of the training epochs, with a 7% reduction in energy prediction error.

The efficiency gains stack across the full pipeline:

- **Dynamic batching** fills each GPU batch to memory capacity rather than using fixed-size batches, keeping hardware utilization high even when atomic structures vary wildly in size
- **Custom CUDA kernels** — low-level GPU programs written specifically for Nequix — fuse the expensive equivariant tensor product operation with message-passing into a single step, eliminating costly intermediate memory allocations
- **100 training epochs on MPtrj** (a database of ~1.5 million quantum chemistry calculations), completed on just two A100 GPUs in 50 hours — 100 GPU-hours total

The final model has 700,000 parameters. Large language models routinely exceed 70 billion. Nequix is tiny — and that's the point.

## Why It Matters

The Matbench-Discovery benchmark is the field's most demanding test for materials AI: it asks models to screen 257,000 candidate crystal structures for thermodynamic stability, predicting which will survive synthesis and which will fall apart. Nequix ranks third among compliant models — those trained only on MPtrj for a fair comparison. It also ranks third on the MDR Phonon benchmark, which tests predictions of lattice vibrations relevant to thermal conductivity.

![Figure 2](/iaifi-research-blog/figures/2508_16067/figure_2.png)

Third place while spending one-twentieth the compute budget of any competitor is not a consolation prize. It's a different kind of result entirely.

The field has been climbing a scaling curve: well-funded institutions train ever-larger models on ever-larger datasets, with the implicit message that a massive compute budget is the price of admission to frontier research. Nequix suggests there's a parallel path worth taking — one focused on architectural efficiency, smarter optimization, and democratized access. When a model can be trained for the cost of a few hundred dollars in cloud compute, a graduate student at a small university can reproduce and build on frontier research. That changes the sociology of the field, not just the benchmarks.

Open questions remain. Nequix was trained on MPtrj, a dataset dominated by inorganic crystalline solids; how well the approach generalizes to molecules, surfaces, or disordered materials is unresolved. The Muon optimizer is new enough that its behavior across different problem domains isn't fully characterized. But the reproducible codebase and released model weights mean the community can start answering these questions immediately.

> **Bottom Line:** Nequix demonstrates that a 700K-parameter model trained in 100 GPU-hours can compete with the best materials AI on the planet — a proof of concept that democratizes access to foundation model-quality predictions and challenges the assumption that better materials science requires bigger compute budgets.

## IAIFI Research Highlights

**Interdisciplinary Research Achievement:** Nequix directly bridges modern deep learning optimization techniques — including the Muon optimizer from the ML speedrunning community — with the geometric symmetry constraints fundamental to physical chemistry, producing a model that is both computationally lean and physically principled.

**Impact on Artificial Intelligence:** The work demonstrates that equivariant RMSNorm combined with the Muon optimizer can dramatically accelerate convergence in physics-constrained neural networks, offering a training recipe that could benefit equivariant models across scientific domains beyond materials.

**Impact on Fundamental Interactions:** By making accurate interatomic potential prediction accessible at low computational cost, Nequix lowers the barrier for ab initio-quality materials screening — accelerating the discovery of stable new materials relevant to energy storage, superconductivity, and quantum technologies.

**Outlook and References:** Future work will likely explore extending Nequix-style efficiency to larger and more diverse training datasets, as well as applying these optimization strategies to other equivariant architectures; the model and code are available at github.com/atomicarchitects/nequix (arXiv preprint, 2025).