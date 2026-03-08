---
abstract: 'In a recent work arXiv:2008.08601, Halverson, Maiti and Stoner proposed
  a description of neural networks in terms of a Wilsonian effective field theory.
  The infinite-width limit is mapped to a free field theory, while finite $N$ corrections
  are taken into account by interactions (non-Gaussian terms in the action). In this
  paper, we study two related aspects of this correspondence. First, we comment on
  the concepts of locality and power-counting in this context. Indeed, these usual
  space-time notions may not hold for neural networks (since inputs can be arbitrary),
  however, the renormalization group provides natural notions of locality and scaling.
  Moreover, we comment on several subtleties, for example, that data components may
  not have a permutation symmetry: in that case, we argue that random tensor field
  theories could provide a natural generalization. Second, we improve the perturbative
  Wilsonian renormalization from arXiv:2008.08601 by providing an analysis in terms
  of the nonperturbative renormalization group using the Wetterich-Morris equation.
  An important difference with usual nonperturbative RG analysis is that only the
  effective (IR) 2-point function is known, which requires setting the problem with
  care. Our aim is to provide a useful formalism to investigate neural networks behavior
  beyond the large-width limit (i.e.~far from Gaussian limit) in a nonperturbative
  fashion. A major result of our analysis is that changing the standard deviation
  of the neural network weight distribution can be interpreted as a renormalization
  flow in the space of networks. We focus on translations invariant kernels and provide
  preliminary numerical results.'
arxivId: '2108.01403'
arxivUrl: https://arxiv.org/abs/2108.01403
authors:
- Harold Erbin
- Vincent Lahoche
- Dine Ousmane Samary
concepts:
- renormalization
- nn-qft correspondence
- quantum field theory
- functional renormalization group
- effective field theory
- kernel methods
- phase transitions
- tensor field theory
- symmetry breaking
- stochastic processes
- interpretability
figures:
- /iaifi-research-blog/figures/2108_01403/figure_1.png
- /iaifi-research-blog/figures/2108_01403/figure_2.png
- /iaifi-research-blog/figures/2108_01403/figure_3.png
pdfUrl: https://arxiv.org/pdf/2108.01403v2
published: '2021-08-03T10:36:04+00:00'
theme: Theoretical Physics
title: Nonperturbative renormalization for the neural network-QFT correspondence
wordCount: 1135
---

## The Big Picture

Imagine you're trying to understand why a crowded city functions the way it does. You could track every person's movements — every coffee run, every commute — or you could zoom out and describe the city using traffic patterns, density flows, and aggregate behavior. This second approach, ignoring microscopic details to reveal large-scale structure, is exactly what physicists do with the **renormalization group** — a mathematical framework for systematically zooming out from small-scale details to large-scale behavior. Now a team of theoretical physicists has applied this technique to neural networks themselves, revealing a deep connection between machine learning and **quantum field theory** (the mathematical language of fundamental particles and forces).

The puzzle at the heart of this work: neural networks are notoriously opaque. They work, often brilliantly, but we struggle to explain *why* or how to systematically improve them. A promising route emerged from a 2020 result showing that infinitely wide neural networks are mathematically equivalent to the simplest possible quantum field theories — ones with no interactions, where outputs follow a tidy, predictable bell-curve pattern.

But "infinite-width" is a physicist's fantasy. Real networks are finite, messy, and far from that clean limit. Erbin, Lahoche, and Ousmane Samary set out to bridge that gap using some of the most sophisticated tools in theoretical physics. Their central achievement is a **nonperturbative renormalization group analysis** of neural networks — an approach that works even when networks are far from the well-behaved infinite-width regime, capturing behaviors that simpler approximations miss.

> **Key Insight:** Changing the standard deviation of a neural network's weight distribution is mathematically equivalent to flowing along a renormalization group trajectory through the space of possible networks — connecting mundane design choices directly to the physics of phase transitions.

## How It Works

The foundation is the **NN-QFT correspondence**: a neural network's statistical behavior, encoded in its **correlation functions** (measurements of how different outputs relate to each other), maps onto the mathematical structure of a quantum field theory. In the infinite-width limit, this is a *free* field theory — equivalent to saying the network outputs follow a **Gaussian process**, a statistical model where outputs form a symmetric bell curve fully described by a mean and a variance.

Add finite-width corrections and you get **interaction terms** — the non-Gaussian parts that make the theory, and the network, genuinely complex and interesting.

The previous state of the art used **Wilsonian perturbative renormalization**: a systematic expansion treating interaction terms as small corrections, building up a solution layer by layer — like approximating a complicated curve with a polynomial. It works near the Gaussian limit. Many interesting network behaviors, however, live far from this limit, where the expansion breaks down.

The team's solution: deploy the **Wetterich-Morris equation**, a cornerstone of **nonperturbative RG (NPRG)**. Rather than assuming interactions are small, NPRG tracks exactly how a theory's effective behavior changes as you gradually integrate out finer and finer details, scale by scale.

![Figure 1](/iaifi-research-blog/figures/2108_01403/figure_1.png)

There's a crucial twist. In standard NPRG applications — condensed matter, particle physics — you know the microscopic theory and derive the macroscopic one. With neural networks, the situation is inverted: only the **infrared (IR) 2-point function** (the large-scale correlation between any two network outputs, essentially the fingerprint of the Gaussian process) is known. This required the authors to reformulate the problem with boundary conditions at the large-scale end rather than the small-scale end.

The analysis distinguishes two flavors of RG flow:

- **Passive RG**: flowing through the space of field theories, integrating out momentum modes — the standard physics picture
- **Active RG**: flowing through the space of neural networks themselves, where changing hyperparameters like weight standard deviation moves you along a trajectory in network space

The active RG is the conceptually striking result. When you tune a network's weight initialization — a routine practical choice — you are, in a precise mathematical sense, performing a renormalization group transformation.

![Figure 2](/iaifi-research-blog/figures/2108_01403/figure_2.png)

The team focuses on **translation-invariant kernels**, which allow momentum-space methods to apply cleanly, and works through the **local potential approximation (LPA)** — a controlled simplification of the full effective action that preserves essential physics while keeping the equations tractable. They analyze both the symmetric phase and symmetry-broken phases, tracking fixed points and flows numerically.

![Figure 3](/iaifi-research-blog/figures/2108_01403/figure_3.png)

The paper also addresses a subtle issue: **locality** in standard QFT means fields interact only at the same spacetime point, rooted in causality. Neural network inputs are arbitrary vectors with no natural spacetime structure, so that constraint doesn't apply. The RG itself generates a natural notion of locality — modes organized by their eigenvalues under the kernel rather than spacetime position. When input data lacks permutation symmetry, the authors argue that **random tensor field theories** offer the right generalization, pointing toward a richer mathematical framework.

## Why It Matters

The practical stakes are significant. If weight initialization standard deviation corresponds to a position in theory space, then finding good initializations becomes a question about the geometry of that space — which fixed points are stable, which flows lead to networks that learn well. The renormalization group could, in principle, provide systematic guidance for hyperparameter selection, architecture design, and generalization.

More broadly, this work pushes the NN-QFT correspondence beyond the comfortable Gaussian regime into genuinely nonperturbative territory. The techniques developed here — reformulating NPRG with IR rather than UV boundary conditions, distinguishing passive and active RG flows — expand the methodological toolkit for any system where only coarse-grained information is available at the outset.

The suggestion that tensor field theories might describe networks processing structured data opens a further direction: connecting the flourishing field of tensor models, used in quantum gravity and combinatorics, to machine learning.

> **Bottom Line:** By applying the Wetterich-Morris nonperturbative renormalization group to neural networks, this work transforms a deep mathematical analogy into a precise, computable framework — revealing that tuning a network's weight distribution is literally a renormalization flow, and extending the NN-QFT correspondence far beyond its well-studied infinite-width origins.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges quantum field theory and machine learning by extending the NN-QFT correspondence into the nonperturbative regime, establishing that neural network hyperparameter choices have precise counterparts in RG flow equations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The framework provides a principled, physics-based formalism for analyzing neural network behavior beyond the Gaussian limit, potentially informing systematic approaches to initialization, generalization, and architecture design.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper adapts the Wetterich-Morris exact RG equation to a novel setting where only IR data is available, advancing nonperturbative QFT methods and connecting them to tensor field theories relevant to quantum gravity.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending beyond the local potential approximation, incorporating derivative corrections, and applying tensor field theory methods to networks with structured inputs; the paper is available as arXiv:2108.01403.</span></div></div>
</div>
