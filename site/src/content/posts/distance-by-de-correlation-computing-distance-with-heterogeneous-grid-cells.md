---
abstract: Encoding the distance between locations in space is essential for accurate
  navigation. Grid cells, a functional class of neurons in medial entorhinal cortex,
  are believed to support this computation. However, existing theories of how populations
  of grid cells code distance rely on complex coding schemes, with assumptions that
  may not be met by anatomical constraints. Inspired by recent work finding grid cells
  to have small, but robust heterogeneity in their grid properties, we hypothesize
  that distance coding can be achieved by a simple de-correlation of population activity.
  We develop a mathematical theory for describing this de-correlation in one-dimension,
  showing that its predictions are consistent with simulations of noisy grid cells.
  Our simulations highlight a non-intuitive prediction of such a distance by de-correlation
  framework. Namely, that some further distances are better encoded than some nearer
  distances. We find evidence of this "sweet spot" in previously published rodent
  behavioral experiments and demonstrate that a decoder which estimates distance from
  the de-correlation of populations of simulated noisy grid cells leads to a similar
  pattern of errors. Finally, by simulating noisy grid cells in two-dimensions, we
  find that there exists a trade-off between the range of distances that can be encoded
  by de-correlation of population activity and the distinguishability of different
  distances, which is controlled by the amount of variability in grid properties.
  We show that the previously observed average amount of grid property variability
  strikes a balance between the two, enabling the encoding of distances up to several
  meters. Our work provides new insight on how grid cells can underlie the coding
  of distance, without the assumptions previously needed, and why grid cells may have
  small amounts of heterogeneity in their grid properties.
arxivId: '2511.08292'
arxivUrl: https://arxiv.org/abs/2511.08292
authors:
- Pritipriya Dasbehera
- Akshunna S. Dogra
- William T. Redman
concepts:
- grid cell coding
- population vector correlation
- neural heterogeneity
- stochastic processes
- representation learning
- spectral methods
- inverse problems
- monte carlo methods
- interpretability
- manifold learning
figures: []
pdfUrl: https://arxiv.org/pdf/2511.08292v1
published: '2025-11-11T14:25:13+00:00'
theme: Foundational AI
title: 'Distance by de-correlation: Computing distance with heterogeneous grid cells'
wordCount: 1275
---

## The Big Picture

Close your eyes and imagine walking from your front door to the corner store. You don't consciously count your steps, yet your brain somehow knows — roughly — how far you've traveled. Now imagine doing this without sight, smell, or landmarks. Just the raw sense of distance, computed on the fly. For decades, neuroscientists have been puzzled by exactly how.

The leading candidate for the brain's internal odometer is a class of neurons called **grid cells**, found in a small region called the medial entorhinal cortex (MEC), a navigation hub tucked near the hippocampus. These neurons fire in a repeating hexagonal pattern as an animal moves through space — think of a sheet of graph paper overlaid on the environment, where each intersection is a firing field. The prevailing theory held that to encode distances beyond a meter or so, the brain needed to combine signals from multiple grid cell clusters (modules), each tuned to a different scale — a kind of neural arithmetic where reading the combination of scales tells you how far you've gone. It worked in theory, but it assumed an unrealistically tidy neural architecture, and it was never clear how downstream brain regions could actually decode the signal.

Researchers Pritipriya Dasbehera, Akshunna Dogra, and William Redman now propose a far simpler alternative: the brain doesn't need that elaborate multi-module machinery at all. A single module of grid cells, with just a tiny sprinkle of natural variability in their firing patterns, can encode distance through a mechanism as elegant as it is unexpected — plain statistical **de-correlation**, where neural activity patterns gradually become less similar to each other the farther apart two locations are.

> **Key Insight:** When grid cells within a single module have small but real differences in their grid spacing, the similarity between neural activity patterns decreases monotonically with distance — giving the brain a clean, readable odometer that requires no complex cross-module decoding.

## How It Works

The core idea hinges on a mathematical property of populations of oscillating neurons. Start with a perfectly uniform grid module — every cell fires with the exact same spacing and orientation, just offset in phase. When you compare the **population vector** (the collective pattern of activity across all cells) at two locations separated by exactly one grid spacing, the correlation — a measure of how similar the two activity patterns are, from 0 (nothing in common) to 1 (identical) — snaps back to 1.

It's déjà vu, built into the math. The neural code has no memory of how far you've come; it only knows where you are within the repeating grid.

Now add a small dose of heterogeneity: let each cell's grid spacing vary slightly around a common mean, as recent experiments confirmed actually happens in real brains. The code changes fundamentally:

- The quasi-periodic "snapping back" breaks down
- Population vector correlations no longer return to 1 at integer multiples of the grid spacing
- Instead, correlations **decay monotonically with distance** — smaller correlation reliably means greater distance
- A single grid module, with modest variability, now acts as a true odometer

The team developed a formal mathematical theory for this one-dimensional case, showing how correlations behave as a function of distance and variability in grid spacing. Simulations of noisy synthetic grid cells matched the theoretical predictions cleanly.

The simulations also revealed something stranger. One might expect a simple rule: the farther you go, the harder to encode distance precisely. Instead, the model predicts a non-monotonic pattern — encoding fidelity decreases, then increases, then decreases again as distance grows. There is a mid-range sweet spot where some longer distances are actually encoded *more* reliably than shorter ones immediately preceding them.

This sounds like a bug. It turns out it might be a feature already hiding in the literature. The team found exactly this pattern in published rodent behavioral experiments: mice performed better on certain intermediate distances than on shorter ones. When the researchers ran their decoder on simulated grid cell populations, it produced a strikingly similar error profile. The framework didn't just explain existing data; it predicted a specific, counterintuitive pattern that was already there in the numbers, waiting to be noticed.

Navigation in the real world is two-dimensional. Extending to 2D simulations, the same basic principle holds — but with an important wrinkle. There is a trade-off between two things you'd want from a distance code:

- **Range**: how far a distance you can encode before the correlation signal becomes too flat to read
- **Distinguishability**: how well the code separates nearby distances from each other

The amount of variability in grid properties controls where you land on this trade-off curve. Too little: no usable de-correlation. Too much: the code loses structure, and nearby distances become hard to tell apart.

The researchers found that the average observed heterogeneity in real rodent grid cells (roughly 10–20% variability in grid spacing) lands almost exactly at the balance point. It's a Goldilocks result: enough variability to produce a clean, monotonic distance signal, not so much that the code becomes indistinguishable noise. This optimal level enables encoding of distances up to several meters — precisely the right scale for a rat navigating a real environment.

## Why It Matters

This work belongs to a growing class of research that asks a deceptively simple question: *why does biological neural architecture look the way it does?* Random variation in neural properties is typically treated as noise to be tolerated, not a feature to be explained. Dasbehera, Dogra, and Redman's framework turns that assumption on its head. The heterogeneity of grid cells isn't a biological imperfection — it may be the precise, tuned ingredient that makes distance coding possible without the complexity of multi-module integration.

For AI and computational neuroscience, the implications go further. Current GPS-inspired theories of spatial cognition — which often invoke elaborate, hierarchical multi-scale codes — may be solving a harder problem than the brain actually solves. A simple de-correlation principle, applied to a single heterogeneous population, achieves the same goal with fewer moving parts. That's an insight worth carrying into the design of spatial representations in artificial systems, from navigation algorithms to memory architectures in neural networks.

The work also opens sharp empirical questions. Can the de-correlation signal be directly measured in MEC recordings during active navigation? Do grid cells with more variability cluster in regions associated with longer-range navigation? And how does this mechanism interact with the place cells downstream that actually guide behavior?

> **Bottom Line:** A single grid module with naturally observed levels of variability encodes distance through simple statistical de-correlation — no complex multi-module machinery required — and the resulting sweet spot in encoding fidelity matches real rodent behavior, offering a cleaner and more biologically plausible theory of spatial navigation.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges computational neuroscience and mathematical physics, developing a formal theory of neural population statistics that connects directly to behavioral experiments in rodents — a rare loop from abstract math to measured biology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The de-correlation framework offers a new design principle for spatial representations in AI systems, suggesting that heterogeneous, single-module populations can achieve robust distance encoding without hierarchical multi-scale complexity.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By showing that observed grid cell heterogeneity is precisely tuned to an optimal range-vs-distinguishability trade-off, the work provides a principled computational explanation for why biological neural circuits maintain small but nonzero variability in their properties.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will test whether de-correlation signals can be directly observed in electrophysiological recordings during active navigation; the full paper is available at [arXiv:2511.08292](https://arxiv.org/abs/2511.08292).</span></div></div>
</div>
