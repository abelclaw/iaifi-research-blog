---
abstract: Compact symbolic expressions have been shown to be more efficient than neural
  network models in terms of resource consumption and inference speed when implemented
  on custom hardware such as FPGAs, while maintaining comparable accuracy~\cite{tsoi2023symbolic}.
  These capabilities are highly valuable in environments with stringent computational
  resource constraints, such as high-energy physics experiments at the CERN Large
  Hadron Collider. However, finding compact expressions for high-dimensional datasets
  remains challenging due to the inherent limitations of genetic programming, the
  search algorithm of most symbolic regression methods. Contrary to genetic programming,
  the neural network approach to symbolic regression offers scalability to high-dimensional
  inputs and leverages gradient methods for faster equation searching. Common ways
  of constraining expression complexity often involve multistage pruning with fine-tuning,
  which can result in significant performance loss. In this work, we propose $\tt{SymbolNet}$,
  a neural network approach to symbolic regression specifically designed as a model
  compression technique, aimed at enabling low-latency inference for high-dimensional
  inputs on custom hardware such as FPGAs. This framework allows dynamic pruning of
  model weights, input features, and mathematical operators in a single training process,
  where both training loss and expression complexity are optimized simultaneously.
  We introduce a sparsity regularization term for each pruning type, which can adaptively
  adjust its strength, leading to convergence at a target sparsity ratio. Unlike most
  existing symbolic regression methods that struggle with datasets containing more
  than $\mathcal{O}(10)$ inputs, we demonstrate the effectiveness of our model on
  the LHC jet tagging task (16 inputs), MNIST (784 inputs), and SVHN (3072 inputs).
arxivId: '2401.09949'
arxivUrl: https://arxiv.org/abs/2401.09949
authors:
- Ho Fung Tsoi
- Vladimir Loncar
- Sridhara Dasu
- Philip Harris
concepts:
- symbolic regression
- dynamic pruning
- sparse models
- model compression
- interpretability
- jet physics
- feature extraction
- scalability
- trigger systems
- regression
- loss function design
- collider physics
figures:
- /iaifi-research-blog/figures/2401_09949/figure_1.png
- /iaifi-research-blog/figures/2401_09949/figure_1.png
- /iaifi-research-blog/figures/2401_09949/figure_2.png
- /iaifi-research-blog/figures/2401_09949/figure_2.png
- /iaifi-research-blog/figures/2401_09949/figure_3.png
- /iaifi-research-blog/figures/2401_09949/figure_3.png
pdfUrl: https://arxiv.org/pdf/2401.09949v3
published: '2024-01-18T12:51:38+00:00'
theme: Foundational AI
title: 'SymbolNet: Neural Symbolic Regression with Adaptive Dynamic Pruning for Compression'
wordCount: 1009
---

## The Big Picture

Imagine you're a physicist at CERN, and a particle collision happens every 25 nanoseconds. Your detector must decide in real time whether to keep or discard that event — with the compute budget of a calculator, not a supercomputer. Deep learning models are too slow, too hungry. What you want is a compact formula written on a napkin.

**Symbolic regression** tries to find that formula automatically. Instead of fitting data to a pre-defined equation, it searches the space of all possible mathematical expressions — addition, multiplication, sine, square roots — to discover the one that fits best. It's a modern version of what Max Planck did in 1900: stare at data from glowing hot objects, find a formula that fits the curve, and accidentally invent quantum mechanics.

The problem? Classical symbolic regression algorithms choke when data has more than roughly ten input variables. Physics datasets at the LHC (the Large Hadron Collider, the world's most powerful particle accelerator) have hundreds or thousands.

SymbolNet is a new neural network framework that closes this gap. It performs symbolic regression on high-dimensional inputs while simultaneously pruning away unnecessary variables, operators, and connections — all in a single training run.

> **Key Insight:** SymbolNet treats symbolic regression as a compression problem, using adaptive dynamic pruning to simultaneously optimize model accuracy and expression compactness, scaling symbolic regression to thousands of input features for the first time.

## How It Works

The traditional approach to symbolic regression is **genetic programming (GP)** — an evolutionary algorithm that breeds and mutates mathematical formulas across generations, selecting the fittest survivors. It works for small problems but becomes intractably slow as input dimensionality grows. SymbolNet replaces the evolutionary search with a neural network whose architecture is specifically designed to produce human-readable symbolic expressions.

![Figure 1](/iaifi-research-blog/figures/2401_09949/figure_1.png)

Each neuron applies one function from a library of **activation functions** — operations like addition, multiplication, square, sine, and absolute value. The network learns which operators to keep and which to simplify. A complex sine function might collapse to a linear term if the data doesn't require it, automatically reducing complexity without human intervention. This is called **operator pruning**.

SymbolNet prunes three things simultaneously in a single training pass:

- **Model weights** — individual connection strengths, the standard form of network sparsity
- **Input features** — entire input variables, performing automatic feature selection
- **Mathematical operators** — complex functions downgraded to simpler arithmetic

Each prunable element carries a **trainable threshold** — a learned cutoff that determines what survives. A weight survives if its magnitude exceeds its threshold; otherwise it's masked to zero. This dynamic competition means the network continuously renegotiates what to keep based on impact on accuracy.

![Figure 2](/iaifi-research-blog/figures/2401_09949/figure_1.png)

To prevent the network from ignoring sparsity, SymbolNet adds a **self-adaptive regularization** term for each pruning type. This regularization adjusts its own strength during training: if the expression is still too complex, the penalty increases; if sparsity is already at target, it relaxes. The user specifies a desired sparsity ratio — keep only 10% of weights, for example — and training converges there automatically, without manual coefficient tuning.

## Why It Matters

SymbolNet was tested on three datasets spanning vastly different scales. For **LHC jet tagging** (16 inputs), it matched or outperformed baseline neural symbolic regression methods while producing significantly sparser expressions. On **MNIST** (784 pixel inputs) and binary **SVHN** (3,072 inputs — street house numbers from photographs), SymbolNet demonstrated something no prior symbolic regression tool has achieved: compact symbolic expressions for image-scale inputs.

![Figure 4](/iaifi-research-blog/figures/2401_09949/figure_2.png)

The payoff for compactness is speed. When the extracted expressions were synthesized onto an **FPGA** — a reconfigurable hardware chip used in LHC trigger systems — inference ran in nanoseconds with a fraction of the resource usage of a conventional neural network. For jet tagging, the FPGA implementation achieved latency comparable to hls4ml-compressed networks (a leading tool for converting neural networks into hardware-deployable form), but with a far simpler, auditable expression underneath.

![Figure 5](/iaifi-research-blog/figures/2401_09949/figure_3.png)

At the LHC, the first-level hardware trigger must process 40 million collisions per second and reduce that stream to a manageable size in microseconds. Every nanosecond counts, and every FPGA lookup table is a scarce resource shared across an entire detector.

SymbolNet's expressions are not just fast — they're transparent. A physicist can read the formula, check it against physical intuition, and trust it in a way that a 50-layer neural network simply cannot be. Symbolic regression has long been proposed as a path toward **AI-assisted scientific discovery** — machines uncovering physical laws directly from data, the way Planck or Kepler did by hand. The bottleneck has always been scalability.

SymbolNet's results on 3,072-dimensional image data suggest that neural symbolic regression is no longer confined to toy problems. Whether the expressions it finds on real physics datasets encode genuinely new physical insight remains an open question — and it's exactly the right question to be asking next.

> **Bottom Line:** SymbolNet makes symbolic regression practical for high-dimensional real-world datasets by combining neural networks with single-phase adaptive pruning, delivering compact mathematical expressions that run at nanosecond latency on FPGA hardware — a critical capability for physics experiments at the LHC and beyond.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">SymbolNet addresses a core bottleneck at the intersection of machine learning and experimental particle physics, translating neural symbolic regression into a hardware-deployable compression technique validated on LHC jet tagging tasks.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The adaptive dynamic pruning framework — simultaneously optimizing weights, input features, and operators with self-adjusting regularization — advances the state of the art in neural symbolic regression, scaling the approach to datasets with thousands of inputs.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling real-time symbolic inference on FPGAs at nanosecond latency, this work directly supports the LHC's hardware trigger pipeline, where ultra-fast and resource-efficient models are essential for capturing rare collision events.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work includes extending SymbolNet to multiclass tasks and exploring whether discovered expressions encode novel physical principles; the paper is available on arXiv as part of the IAIFI research portfolio.</span></div></div>
</div>
