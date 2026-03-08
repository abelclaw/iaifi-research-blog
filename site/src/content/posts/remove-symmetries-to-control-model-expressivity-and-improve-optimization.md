---
abstract: When symmetry is present in the loss function, the model is likely to be
  trapped in a low-capacity state that is sometimes known as a "collapse". Being trapped
  in these low-capacity states can be a major obstacle to training across many scenarios
  where deep learning technology is applied. We first prove two concrete mechanisms
  through which symmetries lead to reduced capacities and ignored features during
  training and inference. We then propose a simple and theoretically justified algorithm,
  syre, to remove almost all symmetry-induced low-capacity states in neural networks.
  When this type of entrapment is especially a concern, removing symmetries with the
  proposed method is shown to correlate well with improved optimization or performance.
  A remarkable merit of the proposed method is that it is model-agnostic and does
  not require any knowledge of the symmetry.
arxivId: '2408.15495'
arxivUrl: https://arxiv.org/abs/2408.15495
authors:
- Liu Ziyin
- Yizhou Xu
- Isaac Chuang
concepts:
- symmetry removal
- group theory
- symmetry breaking
- capacity collapse
- loss function design
- saddle point escape
- eigenvalue decomposition
- equivariant neural networks
- phase transitions
- geometric deep learning
- scalability
figures:
- /iaifi-research-blog/figures/2408_15495/figure_1.png
- /iaifi-research-blog/figures/2408_15495/figure_2.png
- /iaifi-research-blog/figures/2408_15495/figure_3.png
pdfUrl: https://arxiv.org/pdf/2408.15495v4
published: '2024-08-28T02:45:41+00:00'
theme: Foundational AI
title: Remove Symmetries to Control Model Expressivity and Improve Optimization
wordCount: 1076
---

## The Big Picture

Imagine training a world-class athlete who keeps gravitating back to the same comfortable corner — never pushing past it, never discovering what they're actually capable of. That's roughly what happens inside a neural network when the mathematical formula guiding its training has a certain kind of built-in balance. The network finds a perfectly stable, perfectly mediocre resting spot and stays there. Not because it can't do better, but because the mathematics actively pulls it back.

This phenomenon — called **collapse** — is one of the sneakiest failure modes in modern deep learning. It appears in self-supervised learning (where AI learns to recognize patterns without hand-labeled examples), in language models, in physics-informed networks (AI systems designed to respect known laws of physics), and in almost every corner of AI research.

A model collapses when it stops using significant parts of its problem-solving capacity: neurons go silent, features get ignored, performance plateaus well below potential. For years, practitioners have patched around it with tricks and heuristics. Nobody had a clean theoretical story for why it happens, let alone a principled fix.

Now, researchers at MIT and EPFL have done both. Liu Ziyin, Yizhou Xu, and Isaac Chuang prove exactly how symmetry causes collapse — and propose a one-line algorithm called **syre** that removes it.

> **Key Insight:** Symmetries in a neural network's loss function create low-capacity "traps" that gradient descent falls into naturally. Removing those symmetries breaks the traps — and the fix requires no knowledge of what the symmetry actually is.

## How It Works

The starting point is a mathematical observation that's both elegant and unsettling. Many standard training practices — adding weight decay, using certain architectures, designing particular loss functions — introduce **reflection symmetries** (mirror-image patterns where the training landscape looks identical from two opposite sides) into the loss landscape. Formally, if you apply a transformation $(I - 2P)\theta$ — a reflection through a subspace defined by projection matrix $P$ — the loss doesn't change.

![Figure 1](/iaifi-research-blog/figures/2408_15495/figure_1.png)

That sounds harmless. It isn't. The researchers prove two distinct mechanisms through which these symmetries damage training:

1. **Capacity reduction via gradient vanishing.** Near a symmetric solution — a point on the symmetry plane — the forces that normally push the network toward higher-capacity solutions become vanishingly small. The model can technically escape, but gradient descent (the algorithm that moves the network step by step toward better solutions) loses traction exactly where it needs it most.
2. **Weight decay coupling.** Standard **weight decay** — a regularization technique that discourages overly large parameter magnitudes — inadvertently makes things worse. The symmetric version of any parameter configuration always has a smaller magnitude than the original. So weight decay doesn't just regularize; it actively drags parameters toward symmetric, low-capacity solutions.

Together, these mechanisms mean the model is both attracted to collapse and unable to escape once it's close. The symmetric solutions are **saddle points** — mathematical traps where the terrain slopes favorably in some directions but not others — and particularly sticky ones.

The proposed fix, **syre** (SYmmetry REmoval), is almost disarmingly simple. Rather than identifying and enumerating symmetries — which in nonlinear networks can be hidden, high-dimensional, and practically infinite — syre breaks them all at once by adding a small asymmetric perturbation to the loss.

Specifically, it adds a term of the form $\lambda \|\theta - \theta_0\|^2_D$, where $D$ is a random positive definite matrix. Because $D$ is random and asymmetric, it shatters every reflection symmetry simultaneously. The researchers prove this rigorously: with probability one, a random $D$ breaks all reflection symmetries, including ones the practitioner doesn't know about.

![Figure 2](/iaifi-research-blog/figures/2408_15495/figure_2.png)

The elegance here is that you don't need to understand your network's symmetry structure. You don't need to audit the architecture or the loss function. You add one term, sample a random matrix, and the theoretical guarantees handle the rest.

## Why It Matters

Collapse is not a niche problem. It afflicts self-supervised methods like SimCLR and BYOL, degrades transformers trained with weight decay, and limits physics-informed neural networks that encode symmetries as built-in assumptions. Every one of these settings is now, in principle, addressable with a fix that works regardless of model type or the specific symmetries involved.

![Figure 3](/iaifi-research-blog/figures/2408_15495/figure_3.png)

For physics applications specifically, this work cuts close to something fundamental. Physicists love symmetry — they encode it into models deliberately, as a form of domain knowledge. But there's a tension: baking too much symmetry into a neural network can inadvertently create the very traps this paper describes. The syre framework offers a way to navigate that tension: use physics-informed symmetries as built-in assumptions, but selectively break the ones that threaten training stability.

The framework also connects to a deeper theme at the intersection of physics and machine learning: the geometry of parameter space, like the geometry of physical space, governs what dynamics are even possible.

The open questions are equally rich. Can syre be extended to continuous symmetries, not just discrete ones? How does it interact with equivariant architectures (networks specifically designed to preserve certain symmetries)? Can the random matrix $D$ be chosen adaptively — learned alongside the model — to yield even stronger guarantees? This paper doesn't close the door on symmetry in deep learning. It opens a much more precise one.

> **Bottom Line:** By proving that symmetry-induced collapse is both mechanistically inevitable and mathematically preventable, this work gives the field its first clean, principled handle on one of deep learning's most persistent failure modes — and the fix is a single line of code.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies the physicist's language of symmetry — reflection groups, invariant transformations, projection operators — to diagnose and cure a core failure mode in deep learning, demonstrating that fundamental physics concepts have direct, actionable consequences for AI optimization.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The syre algorithm provides the first provably correct, model-agnostic method for breaking symmetry-induced collapse in neural networks, with demonstrated improvements across self-supervised learning, language model fine-tuning, and graph neural networks.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By formalizing how symmetry governs the capacity and dynamics of learned representations, this work deepens the theoretical bridge between symmetry principles in physics and the geometry of neural network loss landscapes.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending the framework to continuous and Lie-group symmetries common in physics-informed networks; the paper by Liu Ziyin, Yizhou Xu, and Isaac Chuang (MIT and EPFL) was published at ICLR 2025.</span></div></div>
</div>
