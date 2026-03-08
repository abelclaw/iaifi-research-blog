---
abstract: Mechanistic Interpretability (MI) promises a path toward fully understanding
  how neural networks make their predictions. Prior work demonstrates that even when
  trained to perform simple arithmetic, models can implement a variety of algorithms
  (sometimes concurrently) depending on initialization and hyperparameters. Does this
  mean neuron-level interpretability techniques have limited applicability? We argue
  that high-dimensional neural networks can learn low-dimensional representations
  of their training data that are useful beyond simply making good predictions. Such
  representations can be understood through the mechanistic interpretability lens
  and provide insights that are surprisingly faithful to human-derived domain knowledge.
  This indicates that such approaches to interpretability can be useful for deriving
  a new understanding of a problem from models trained to solve it. As a case study,
  we extract nuclear physics concepts by studying models trained to reproduce nuclear
  data.
arxivId: '2405.17425'
arxivUrl: https://arxiv.org/abs/2405.17425
authors:
- Ouail Kitouni
- Niklas Nolte
- Víctor Samuel Pérez-Díaz
- Sokratis Trifinopoulos
- Mike Williams
concepts:
- interpretability
- representation learning
- mechanistic interpretability
- dimensionality reduction
- disentangled representations
- embeddings
- latent space topography
- manifold learning
- nuclear magic numbers
- eigenvalue decomposition
- feature extraction
- surrogate modeling
figures: []
pdfUrl: https://arxiv.org/pdf/2405.17425v1
published: '2024-05-27T17:59:35+00:00'
theme: Experimental Physics
title: 'From Neurons to Neutrons: A Case Study in Interpretability'
wordCount: 1211
---

## The Big Picture

Imagine handing a student a massive table of measurements, thousands of rows of numbers describing atomic nuclei, and asking them to find the patterns. No textbook, no hints, no physics curriculum. Now imagine that student not only learns to predict new measurements accurately, but spontaneously invents concepts that took physicists decades to discover. That's essentially what researchers at IAIFI found when they peered inside neural networks trained on nuclear data.

**Mechanistic interpretability** asks a deceptively simple question: when a neural network makes a prediction, *how* does it actually do it? Prior work showed that networks trained on basic arithmetic can invent surprising internal algorithms, sometimes multiple different ones, depending on the accident of how training began. This raised an uncomfortable possibility: maybe neural network internals are too unpredictable to tell us anything useful about the real world. This paper argues the opposite.

A team of physicists and ML researchers trained networks to reproduce nuclear experimental data, then dissected what those networks had learned. What they found wasn't arbitrary computational machinery. It was nuclear physics, reconstructed from scratch.

> **Key Insight:** Neural networks trained on nuclear data spontaneously learn internal representations that mirror the conceptual structures physicists use to understand atomic nuclei, suggesting interpretability tools can extract genuine scientific knowledge, not just predict outputs.

## How It Works

The researchers begin with a warm-up: **modular arithmetic**, the math of clock faces and remainders. When a small neural network (an MLP, or multi-layer perceptron) learns to add numbers in this system, its **embeddings** (the internal vectors the network uses to represent each number) arrange themselves in a perfect circle. The network computes a sum by averaging two points on the circle and reading off which "slice" the midpoint falls in.

Nobody imposed this circular structure. It emerges purely from training. And it matches how humans naturally teach modular arithmetic, a convergence worth pausing on.


This circular example establishes the key method: **latent space topography (LST)**. Rather than inspecting individual neurons, the researchers project the network's high-dimensional internal representations down to their first two or three **principal components (PCs)**. These are the directions that capture the most variation in the data, like scatter plot axes oriented to reveal maximum structure. The researchers then map what the network "thinks" across that compressed space. Think of it as a topographic survey of a mountain range, sampling elevation at a grid of points to reconstruct the terrain.

With that technique validated, they turn to nuclear physics. The setup: train a neural network to predict properties of atomic nuclei, including **binding energies** (the energy holding a nucleus together; higher means more stable), given only the number of protons (Z) and neutrons (N). No shell models, no magic numbers, no physics prior. Just data.

They extract the learned embeddings for each neutron number and project them onto the first three principal components.


Out comes a helix. The embeddings spiral through three-dimensional space in a corkscrew pattern that encodes layers of nuclear structure simultaneously. When the researchers repeat the experiment on synthetic data generated by an established human-derived theory (the liquid drop model with shell corrections), the same helix emerges. The two spirals are structurally identical.

The helix isn't decorative. Its geometry encodes specific physical concepts:

- **Nuclear shells:** Nuclei with certain "magic numbers" of protons or neutrons (2, 8, 20, 28, 50, 82, 126) are unusually stable, much like filled electron shells in chemistry. These appear as distinctive kinks or clustering patterns along the helix.
- **Pairing effects:** Nuclei with even numbers of neutrons are more stable than odd-neutron nuclei, a quantum effect from nucleon pairing. This shows up as a systematic wobble in the helix.
- **Bulk nuclear matter:** The overall scale of the helix encodes the dominant contribution to binding energy, the same term that anchors the liquid drop model physicists derived decades ago.

None of these concepts were given to the network. They emerged from fitting the data.

## Why It Matters

The standard story about neural network interpretability is cautionary: networks can implement wildly different algorithms depending on how they were initially set up, making it hard to extract universal lessons. For *scientific* data, generated by real physical laws, the situation looks different. Physical laws constrain what representations are useful, and networks trained on that data tend to converge on representations that reflect the underlying physics, not idiosyncratic computational choices.

This opens up a new use for interpretability tools. Rather than asking only "how does this model make predictions?", researchers can ask "what does this model's internal structure reveal about the data?" In domains where human understanding is incomplete (exotic nuclei far from stability, novel materials, poorly understood particle interactions), a trained network could become something like an oracle, its internal representations pointing toward concepts that human theorists haven't yet articulated.

There's also a practical message here for AI researchers: high-dimensional networks, even when trained on messy real-world data rather than clean arithmetic problems, can learn low-dimensional representations that are both accurate and interpretable. This supports the **manifold hypothesis**, the idea that natural data concentrates near low-dimensional surfaces in high-dimensional space. Not just as a mathematical nicety, but as a practical guide to what networks actually learn.

> **Bottom Line:** Applying mechanistic interpretability to nuclear physics reveals that neural networks can autonomously rediscover established scientific knowledge encoded in data, turning interpretability from a tool for auditing AI into a tool for doing science.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">The work connects mechanistic interpretability with nuclear structure physics, showing that analytical tools developed to understand arithmetic-solving networks can extract established physical concepts from data-driven models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper expands mechanistic interpretability beyond algorithmic toy problems. Latent space topography and PCA-based analysis reveal scientifically meaningful low-dimensional structure in networks trained on real experimental data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By recovering nuclear shell structure, magic numbers, and pairing effects from learned representations, without any physics prior, the work validates a new pathway for using neural networks as hypothesis-generating tools in nuclear and particle physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include applying this framework to domains where human theory is incomplete, such as exotic nuclei and strongly coupled systems. The paper is available as [arXiv:2405.17425](https://arxiv.org/abs/2405.17425).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">From Neurons to Neutrons: A Case Study in Interpretability</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2405.17425</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Ouail Kitouni", "Niklas Nolte", "Víctor Samuel Pérez-Díaz", "Sokratis Trifinopoulos", "Mike Williams"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Mechanistic Interpretability (MI) promises a path toward fully understanding how neural networks make their predictions. Prior work demonstrates that even when trained to perform simple arithmetic, models can implement a variety of algorithms (sometimes concurrently) depending on initialization and hyperparameters. Does this mean neuron-level interpretability techniques have limited applicability? We argue that high-dimensional neural networks can learn low-dimensional representations of their training data that are useful beyond simply making good predictions. Such representations can be understood through the mechanistic interpretability lens and provide insights that are surprisingly faithful to human-derived domain knowledge. This indicates that such approaches to interpretability can be useful for deriving a new understanding of a problem from models trained to solve it. As a case study, we extract nuclear physics concepts by studying models trained to reproduce nuclear data.</span></div></div>
</div>
