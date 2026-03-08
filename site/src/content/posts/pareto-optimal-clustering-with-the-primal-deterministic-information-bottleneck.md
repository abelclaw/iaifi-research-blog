---
abstract: 'At the heart of both lossy compression and clustering is a trade-off between
  the fidelity and size of the learned representation. Our goal is to map out and
  study the Pareto frontier that quantifies this trade-off. We focus on the optimization
  of the Deterministic Information Bottleneck (DIB) objective over the space of hard
  clusterings. To this end, we introduce the primal DIB problem, which we show results
  in a much richer frontier than its previously studied Lagrangian relaxation when
  optimized over discrete search spaces. We present an algorithm for mapping out the
  Pareto frontier of the primal DIB trade-off that is also applicable to other two-objective
  clustering problems. We study general properties of the Pareto frontier, and we
  give both analytic and numerical evidence for logarithmic sparsity of the frontier
  in general. We provide evidence that our algorithm has polynomial scaling despite
  the super-exponential search space, and additionally, we propose a modification
  to the algorithm that can be used where sampling noise is expected to be significant.
  Finally, we use our algorithm to map the DIB frontier of three different tasks:
  compressing the English alphabet, extracting informative color classes from natural
  images, and compressing a group theory-inspired dataset, revealing interesting features
  of frontier, and demonstrating how the structure of the frontier can be used for
  model selection with a focus on points previously hidden by the cloak of the convex
  hull.'
arxivId: '2204.02489'
arxivUrl: https://arxiv.org/abs/2204.02489
authors:
- Andrew K. Tan
- Max Tegmark
- Isaac L. Chuang
concepts:
- clustering
- information bottleneck
- pareto frontier mapping
- lossy compression
- representation learning
- dimensionality reduction
- loss function design
- sparse models
- interpretability
- group theory
- scalability
figures:
- /iaifi-research-blog/figures/2204_02489/figure_1.png
- /iaifi-research-blog/figures/2204_02489/figure_1.png
- /iaifi-research-blog/figures/2204_02489/figure_2.png
- /iaifi-research-blog/figures/2204_02489/figure_2.png
- /iaifi-research-blog/figures/2204_02489/figure_3.png
- /iaifi-research-blog/figures/2204_02489/figure_3.png
pdfUrl: https://arxiv.org/pdf/2204.02489v2
published: '2022-04-05T21:08:45+00:00'
theme: Foundational AI
title: Pareto-optimal clustering with the primal deterministic information bottleneck
wordCount: 1117
---

## The Big Picture

Imagine you're packing for a long trip, but your suitcase has a strict weight limit. You can't bring everything, so you make choices: keep the essentials, ditch the rest. But how do you *optimally* decide what "essential" means? That question sits at the heart of one of the deepest problems in information theory — and, it turns out, in machine learning too.

The core challenge is a fundamental tension: the more you compress data, the less information you retain. Squeeze too hard, and details blur. Hold too loosely, and you're not compressing at all. For decades, researchers have studied this trade-off mathematically, but most approaches only revealed a partial picture — a smooth curve that obscured rich, discrete structure hiding beneath.

A new paper from MIT and IAIFI researchers Andrew Tan, Max Tegmark, and Isaac Chuang maps that hidden terrain in full, revealing a landscape far more intricate — and more useful — than previously known. Their central contribution: a new algorithmic framework for mapping out the complete set of best possible trade-offs — called the **Pareto frontier** — between compression and information retention. Think of it as every balance point where you can't squeeze data any harder without losing something meaningful, and you can't preserve any more without giving up compression.

The framework is applied to a formalism called the **Deterministic Information Bottleneck (DIB)** — a mathematical approach to finding the most informative way to group inputs into clusters — and demonstrated on tasks ranging from compressing the English alphabet to classifying color in natural images.

> **Key Insight:** By solving the clustering problem directly — keeping both competing objectives separate rather than blending them into a single number — researchers reveal a much richer set of optimal clusterings that are completely invisible to conventional approaches.

## How It Works

To understand what makes this work distinctive, you need to grasp the difference between two ways of formulating the same optimization problem.

The standard approach to the **Information Bottleneck (IB)** — and its deterministic variant, DIB — takes two competing objectives (how much information you preserve, how simple your encoding is) and combines them into a single score using a trade-off parameter β. This is called the **Lagrangian relaxation**: pick β, optimize, get one point on the frontier. Sweep β across values and you trace a curve. Simple — but with a critical blind spot.

The Lagrangian approach only finds solutions on the **convex hull** of the feasible solution space — think of it as the outermost skin stretched tightly around all possible solutions, missing everything tucked inside. In discrete problems, where encodings are hard assignments of inputs to clusters, many optimal solutions live *inside* the convex hull — geometrically unreachable by any choice of β. These hidden solutions are Pareto optimal — you can't improve one objective without sacrificing the other — but the Lagrangian method can't find them.

![Figure 1](/iaifi-research-blog/figures/2204_02489/figure_1.png)

The figure above makes this vivid. On the left, the Lagrangian DIB frontier looks sparse and smooth. On the right, the primal DIB frontier — solved directly — reveals a staircase of discrete optimal clusterings, most of which lie inside the convex hull and are completely invisible to the Lagrangian approach.

The authors address this with the **primal DIB problem**: instead of combining objectives into a single scalar, keep them separate and seek clusterings that genuinely maximize preserved information for a given entropy constraint. Solving this directly is computationally daunting — the search space grows super-exponentially with input size. Their solution is **Pareto Mapper**, an ε-greedy agglomerative search that proceeds as follows:

1. Start with the "identity clustering" — every input in its own cluster.
2. Iteratively consider all pairwise merges of existing clusters.
3. Evaluate each merge on both objectives: entropy reduction and mutual information with the target.
4. Add Pareto-optimal points to a maintained frontier; probabilistically explore near-Pareto points using the ε-greedy acceptance criterion.
5. Continue until the queue is exhausted.

The ε parameter controls exploration: high ε chases leads far from the current frontier, useful when sampling noise is significant; low ε keeps the search tight. The result is an approximate Pareto frontier discovered in polynomial time, despite a super-exponential search space — a computational efficiency the authors support with empirical scaling experiments.

![Figure 2](/iaifi-research-blog/figures/2204_02489/figure_1.png)

## Why It Matters

**Model selection** — choosing the right number of clusters or compression level — is typically done by picking a single β and solving. But this hides structure.

The primal frontier reveals natural "corners": sharp bends in the Pareto curve where a small increase in entropy yields a large gain in information retention. These corners are robust, meaningful, and often correspond to the right number of clusters for a given dataset. The Lagrangian approach, by flattening the frontier onto a convex hull, obscures precisely these decision-relevant features.

Three application domains show how broadly this matters. When compressing the English alphabet — mapping 26 letters to fewer clusters based on co-occurrence statistics — the primal frontier reveals linguistically meaningful groupings. For natural image color classification, it shows how color categories emerge at different compression levels. And for a group theory-inspired synthetic dataset with mathematically known structure, the frontier's shape aligns with the algebraic structure of the data, validating the approach against ground truth.

One particularly striking theoretical result: Pareto-optimal frontiers are **logarithmically sparse** — the number of distinct optimal clusterings grows only as the logarithm of the total number of possible encodings. This explains why Pareto Mapper can work at all: the needle of optimality is rare, but the haystack shrinks faster than you'd expect.

> **Bottom Line:** By tackling the Pareto frontier of clustering directly rather than through convex relaxation, this work unlocks a richer map of the compression-information trade-off — revealing hidden optimal solutions and providing a principled new toolkit for model selection in machine learning.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies information-theoretic tools from physics — entropy, mutual information, rate-distortion theory — directly to machine learning clustering, showing how concepts central to statistical mechanics illuminate the structure of learning algorithms.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The Pareto Mapper algorithm provides a principled, computationally efficient method for discovering the full frontier of any two-objective hard clustering problem, enabling better model selection by surfacing optimal solutions hidden from standard Lagrangian approaches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper demonstrates that the structure of learned representations — even for abstract tasks like alphabet compression — reflects deep information-theoretic principles, pointing toward a more fundamental understanding of what makes representations meaningful.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending primal DIB analysis to soft clusterings and higher-dimensional objective spaces; the full paper is available at arXiv:2204.08096.</span></div></div>
</div>
