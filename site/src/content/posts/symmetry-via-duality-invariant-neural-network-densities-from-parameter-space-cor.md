---
abstract: Parameter-space and function-space provide two different duality frames
  in which to study neural networks. We demonstrate that symmetries of network densities
  may be determined via dual computations of network correlation functions, even when
  the density is unknown and the network is not equivariant. Symmetry-via-duality
  relies on invariance properties of the correlation functions, which stem from the
  choice of network parameter distributions. Input and output symmetries of neural
  network densities are determined, which recover known Gaussian process results in
  the infinite width limit. The mechanism may also be utilized to determine symmetries
  during training, when parameters are correlated, as well as symmetries of the Neural
  Tangent Kernel. We demonstrate that the amount of symmetry in the initialization
  density affects the accuracy of networks trained on Fashion-MNIST, and that symmetry
  breaking helps only when it is in the direction of ground truth.
arxivId: '2106.00694'
arxivUrl: https://arxiv.org/abs/2106.00694
authors:
- Anindita Maiti
- Keegan Stoner
- James Halverson
concepts:
- symmetry preservation
- parameter-function duality
- quantum field theory
- network correlation functions
- group theory
- stochastic processes
- kernel methods
- symmetry breaking
- density estimation
- equivariant neural networks
- bayesian inference
figures:
- /iaifi-research-blog/figures/2106_00694/figure_1.png
- /iaifi-research-blog/figures/2106_00694/figure_1.png
- /iaifi-research-blog/figures/2106_00694/figure_2.png
- /iaifi-research-blog/figures/2106_00694/figure_2.png
- /iaifi-research-blog/figures/2106_00694/figure_3.png
- /iaifi-research-blog/figures/2106_00694/figure_3.png
pdfUrl: https://arxiv.org/pdf/2106.00694v1
published: '2021-06-01T18:00:06+00:00'
theme: Theoretical Physics
title: 'Symmetry-via-Duality: Invariant Neural Network Densities from Parameter-Space
  Correlators'
wordCount: 1006
---

## The Big Picture

Imagine understanding a crowd's personality without observing every individual. You could study each person one by one — or you could look at collective behaviors to infer something deeper about shared nature. Physicists have used this trick for decades to uncover hidden symmetries of fundamental forces. Now, a team at IAIFI is applying it to neural networks.

Neural networks have a dirty secret: even though millions are trained every day, we understand remarkably little about the *population* of all possible networks — the full range of behaviors any network with a given design could exhibit. This distribution, called the **network density**, encodes everything about a network's possible behaviors before training begins. Knowing its symmetries — the transformations that leave it unchanged — would constrain predictions and guide better designs. The catch? The density is almost always unknown and impossible to calculate directly.

Researchers Anindita Maiti, Keegan Stoner, and James Halverson found a way around this. By borrowing **duality** from theoretical physics — the idea that the same object can be described in two different but equivalent ways — they can determine the symmetries of a neural network density *without ever computing it*.

> **Key Insight:** Symmetries of an unknown neural network density can be read off from correlation functions computed in the more tractable parameter space — a technique called symmetry-via-duality that connects quantum field theory with deep learning.

## How It Works

The central idea exploits a fundamental duality in how you can think about a neural network. On one side is **parameter space**: a network is a collection of weights and biases drawn from some underlying distribution. On the other is **function space**: the same network can be viewed as a randomly sampled function from all possible input-output behaviors the architecture allows. These are two frames for the same object — exactly the kind of duality physicists exploit in quantum field theory (QFT).

In QFT, physicists compute **n-point correlation functions** — averages measuring how multiple points in a field relate — to extract symmetry constraints without knowing the complete theory. Maiti, Stoner, and Halverson import this machinery directly. The n-point correlators of a network are:

$$G^{(n)}(x_1, \ldots, x_n) = \mathbb{E}[f(x_1) \cdots f(x_n)]$$

The key theorem is elegant: if these correlation functions are invariant under a transformation, the underlying density over functions *must also be invariant*. You don't need to know the density. The correlators tell you everything.

![Figure 1](/iaifi-research-blog/figures/2106_00694/figure_1.png)

The team applies this systematically across two symmetry types:
- **Input symmetries**: transformations of the network's inputs — translations, rotations, or other operations on data
- **Output symmetries**: transformations of the network's outputs — permuting output neurons, for instance

For each case, invariance of the correlation functions — computable directly from the parameter distribution — implies invariance of the functional density. Crucially, this holds even when no single network in the ensemble is equivariant. The density can be symmetric even if individual networks are not.

![Figure 2](/iaifi-research-blog/figures/2106_00694/figure_1.png)

The approach also extends beyond initialization. When networks train, their parameters become correlated — a challenge for most analytical tools. Symmetry-via-duality handles this: if the correlated parameter distribution preserves the relevant invariances, the symmetry carries through. The framework also applies to the **Neural Tangent Kernel (NTK)** — the mathematical object describing how a wide network's outputs shift during training — deriving its symmetry properties by the same mechanism.

In the infinite-width limit, the results recover known results from **Neural Network Gaussian Processes (NNGPs)** — the well-understood case where networks behave like Gaussian processes with especially clean mathematical properties. This serves as a consistency check: the new framework generalizes the known story to finite-width networks with richer, non-Gaussian behavior.

## Why It Matters

The practical stakes become clear in Fashion-MNIST experiments. The team constructs initialization distributions with varying amounts of symmetry — some highly symmetric, some with deliberately broken symmetry — and measures classification accuracy after training. The results sharpen an intuition that had been fuzzy: **more symmetry at initialization is not always better**. What matters is whether the symmetry breaking points toward the true structure of the data.

When it does, breaking symmetry helps. When it doesn't, it hurts.

![Figure 3](/iaifi-research-blog/figures/2106_00694/figure_2.png)

This has direct implications for network design. If you know the symmetry structure of your problem — rotational symmetry in a physics dataset, permutation symmetry in a particle physics task — you can engineer the initialization distribution to match or purposefully break it in the right directions. The symmetry-via-duality framework lets you verify that your chosen parameter distribution produces the desired functional symmetry, all without computing the density directly.

Looking further ahead, this work opens a door between two communities that have long talked past each other. QFT physicists have developed extraordinarily powerful tools for extracting symmetry constraints from correlation functions — tools that took decades to mature. Neural network theory is young enough that importing even the basic vocabulary of that framework could accelerate progress dramatically.

> **Bottom Line:** Symmetry-via-duality lets researchers determine the hidden symmetries of neural network densities using parameter-space correlation functions — no explicit density required — and demonstrates that initialization symmetry directly shapes trained network performance.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly transplants duality and correlation-function machinery from quantum field theory into neural network theory, establishing a rigorous bridge between fundamental physics formalism and deep learning foundations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Symmetry-via-duality provides a practical diagnostic for network initialization: by computing parameter-space correlators, researchers can verify or engineer the symmetry properties of a network density before training begins, with measurable effects on accuracy.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By recovering NNGP and NTK symmetry results as special cases and extending them to finite-width non-Gaussian regimes, the framework advances the QFT-inspired understanding of neural network densities underlying gauge-equivariant lattice field theory applications.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work can extend symmetry-via-duality to characterize how symmetry flows during gradient-descent training and to constrain non-Gaussian process models at finite width; the paper is available as an arXiv preprint from the IAIFI group at Northeastern University.</span></div></div>
</div>
