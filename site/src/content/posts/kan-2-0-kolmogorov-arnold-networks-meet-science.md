---
abstract: 'A major challenge of AI + Science lies in their inherent incompatibility:
  today''s AI is primarily based on connectionism, while science depends on symbolism.
  To bridge the two worlds, we propose a framework to seamlessly synergize Kolmogorov-Arnold
  Networks (KANs) and science. The framework highlights KANs'' usage for three aspects
  of scientific discovery: identifying relevant features, revealing modular structures,
  and discovering symbolic formulas. The synergy is bidirectional: science to KAN
  (incorporating scientific knowledge into KANs), and KAN to science (extracting scientific
  insights from KANs). We highlight major new functionalities in the pykan package:
  (1) MultKAN: KANs with multiplication nodes. (2) kanpiler: a KAN compiler that compiles
  symbolic formulas into KANs. (3) tree converter: convert KANs (or any neural networks)
  to tree graphs. Based on these tools, we demonstrate KANs'' capability to discover
  various types of physical laws, including conserved quantities, Lagrangians, symmetries,
  and constitutive laws.'
arxivId: '2408.10205'
arxivUrl: https://arxiv.org/abs/2408.10205
authors:
- Ziming Liu
- Pingchuan Ma
- Yixuan Wang
- Wojciech Matusik
- Max Tegmark
concepts:
- kolmogorov-arnold networks
- interpretability
- symbolic regression
- conservation laws
- lagrangian methods
- multiplicative nodes
- physics-informed neural networks
- symmetry preservation
- feature extraction
- modular structure discovery
- sparse models
- scientific workflows
figures:
- /iaifi-research-blog/figures/2408_10205/figure_1.png
- /iaifi-research-blog/figures/2408_10205/figure_2.png
- /iaifi-research-blog/figures/2408_10205/figure_3.png
pdfUrl: https://arxiv.org/pdf/2408.10205v1
published: '2024-08-19T17:59:04+00:00'
theme: Foundational AI
title: 'KAN 2.0: Kolmogorov-Arnold Networks Meet Science'
wordCount: 967
---

## The Big Picture

Imagine trying to describe a sunset using only mathematics. You could measure wavelengths, calculate scattering angles, model atmospheric optics, and end up with a precise, beautiful equation. Now imagine the reverse: you have a neural network that has somehow "learned" the sunset, and you want to extract that equation back out of it. That is the central challenge of AI-driven science discovery.

Modern AI is built on a simple but powerful idea: intelligence can emerge from vast webs of numbers, all tuned by exposure to data. Science runs on something different: clean equations, conservation laws, and mathematical structures that hold true everywhere in the universe. These two approaches are mismatched at a basic level. A deep neural network can predict the trajectory of a particle with high accuracy, yet the physics it has learned stays locked inside billions of opaque parameters, invisible to the physicist who needs to understand *why* it works.

A team at MIT and Caltech, led by Ziming Liu and Max Tegmark, wants to close that gap. In KAN 2.0, they extend Kolmogorov-Arnold Networks with new tools that let AI systems absorb prior scientific knowledge and actively reveal the symbolic laws hidden in their own learned representations.

> **Key Insight:** KAN 2.0 creates a two-way bridge between AI and science. Researchers can embed physical knowledge *into* a network, then extract symbolic laws *from* it, all within a single interpretable architecture.

## How It Works

At the core is the **Kolmogorov-Arnold Network (KAN)**, a neural architecture that differs from standard deep learning in one important way. Ordinary networks place fixed mathematical rules (activation functions) at each node. KANs place *learnable* versions of those rules on the *connections* between nodes. The network learns one-dimensional transformations along each link, which can later be matched to known mathematical functions like sine, exponential, or power laws.

![Figure 1](figure:1)

KAN 2.0's first major addition is **MultKAN**, an upgraded architecture that explicitly includes multiplication nodes alongside standard summation nodes. The mathematical theorem underlying KANs technically only requires addition and single-input functions, but that encoding is inefficient and hard to read. Native multiplication nodes make the network far more concise when the underlying physics involves products, like kinetic energy (`½mv²`) or gravitational force (`GMm/r²`).

![Figure 2](figure:2)

The team built three interoperating tools around this architecture:

- **kanpiler**: A compiler that translates a symbolic formula directly into a KAN, letting scientists inject known physics (say, Newton's law of gravity) as a structural prior rather than a soft penalty.
- **tree converter**: Converts any trained KAN, or any neural network, into a tree-structured graph, exposing the compositional structure of a learned function in a way that flat weight matrices never could.
- **Symbolic regression pipeline**: After training, individual activation functions on edges are matched to a library of known functions, progressively "freezing" the network into a readable mathematical formula.

The system operates at three levels of explanation, from coarse to fine: identifying *which inputs matter*, revealing *how those inputs combine*, and extracting *precise symbolic formulas*. Not every problem demands the deepest level. In chemistry or biology, knowing that two variables interact additively can already be a real discovery.

## Why It Matters

The results speak for themselves. KAN 2.0 successfully rediscovers **conserved quantities** (like energy and momentum) from trajectory data, identifies **Lagrangians** (the elegant functions from which classical mechanics derives equations of motion), and uncovers **symmetries** in physical systems. It also discovers **constitutive laws**, the empirical relationships like Hooke's Law or Ohm's Law that characterize how materials respond to forces.

![Figure 3](figure:3)

The deeper point goes beyond any single application. Science has always alternated between two modes: the grinding work of collecting data and fitting curves, and the sudden leap of recognizing that those curves encode something universal. KAN 2.0 is an attempt to accelerate the second mode.

If a network trained on protein dynamics could be tree-converted, symbolically regressed, and handed back to a biochemist as a set of interpretable equations, the gap between AlphaFold-style prediction and genuine physical understanding could shrink considerably. The authors invoke AlphaFold explicitly as a system that must have internalized important unknown physics, physics that currently remains hidden.

Open questions remain. Symbolic regression still relies on a predefined library of candidate functions; discovering truly novel mathematical structures requires either an enormous library or a different approach entirely. Scaling KANs to the parameter counts of frontier models is an active challenge. And the tree-conversion tool, while powerful, imposes a compositional structure that may not always reflect the true causal architecture of a phenomenon.

> **Bottom Line:** KAN 2.0 turns neural networks into two-way instruments for science. They are not just black-box predictors but interactive tools that can absorb prior knowledge and return interpretable physical laws.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work targets the fundamental tension between AI's connectionist foundations and science's symbolic language, proposing a unified approach that moves fluidly between data-driven learning and human-readable equations.

- **Impact on Artificial Intelligence:** The MultKAN architecture, kanpiler compiler, and tree converter form a new toolkit for interpretable machine learning, enabling any neural network to be analyzed for its underlying compositional and symbolic structure.

- **Impact on Fundamental Interactions:** KAN 2.0 automates the rediscovery of conserved quantities, Lagrangians, and symmetries, the core mathematical structures of fundamental physics, directly from observational data.

- **Outlook and References:** Future work will focus on scaling KANs to larger scientific datasets and extending symbolic discovery to chemistry and biology; the paper is available at [arXiv:2408.10205](https://arxiv.org/abs/2408.10205) and the open-source `pykan` package can be installed via `pip install pykan`.
