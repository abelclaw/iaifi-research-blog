---
abstract: Equivariant neural networks (ENNs) have been shown to be extremely effective
  in applications involving underlying symmetries. By construction ENNs cannot produce
  lower symmetry outputs given a higher symmetry input. However, symmetry breaking
  occurs in many physical systems and we may obtain a less symmetric stable state
  from an initial highly symmetric one. Hence, it is imperative that we understand
  how to systematically break symmetry in ENNs. In this work, we propose a novel symmetry
  breaking framework that is fully equivariant and is the first which fully addresses
  spontaneous symmetry breaking. We emphasize that our approach is general and applicable
  to equivariance under any group. To achieve this, we introduce the idea of symmetry
  breaking sets (SBS). Rather than redesign existing networks, we design sets of symmetry
  breaking objects which we feed into our network based on the symmetry of our inputs
  and outputs. We show there is a natural way to define equivariance on these sets,
  which gives an additional constraint. Minimizing the size of these sets equates
  to data efficiency. We prove that minimizing these sets translates to a well studied
  group theory problem, and tabulate solutions to this problem for the point groups.
  Finally, we provide some examples of symmetry breaking to demonstrate how our approach
  works in practice. The code for these examples is available at \url{https://github.com/atomicarchitects/equivariant-SBS}.
arxivId: '2402.02681'
arxivUrl: https://arxiv.org/abs/2402.02681
authors:
- YuQing Xie
- Tess Smidt
concepts:
- equivariant neural networks
- symmetry breaking
- symmetry breaking sets
- group theory
- normalizer constraint
- geometric deep learning
- point group symmetry
- symmetry preservation
- phase transitions
- crystal structure
figures:
- /iaifi-research-blog/figures/2402_02681/figure_1.png
- /iaifi-research-blog/figures/2402_02681/figure_1.png
- /iaifi-research-blog/figures/2402_02681/figure_2.png
- /iaifi-research-blog/figures/2402_02681/figure_2.png
- /iaifi-research-blog/figures/2402_02681/figure_3.png
- /iaifi-research-blog/figures/2402_02681/figure_3.png
pdfUrl: https://arxiv.org/pdf/2402.02681v3
published: '2024-02-05T02:35:11+00:00'
theme: Astrophysics
title: Equivariant Symmetry Breaking Sets
wordCount: 1082
---

## The Big Picture

Imagine a perfectly symmetric snowflake melting and refreezing into a lopsided crystal. The laws governing water molecules are completely symmetric — they don't prefer any direction — yet nature routinely produces structures that break that symmetry. This is one of the deepest puzzles in physics, and it turns out it's a serious problem for some of the most powerful AI tools scientists use today.

A special class of AI called **equivariant neural networks (ENNs)** has become essential in computational physics and chemistry. They're built with a clever guarantee: rotate your molecule, and the network's predictions rotate with it. Feed in a crystal structure, and the output respects the same spatial symmetries. This property — called **equivariance** — means the network needs far less training data, because it never has to rediscover the same physics twice from different orientations.

The catch? That guarantee becomes a straitjacket. By construction, an ENN *cannot* predict an output with lower symmetry than its input. You can't get a lopsided crystal from a perfectly symmetric starting configuration — not because the physics forbids it, but because the math of the network does.

MIT researchers YuQing Xie and Tess Smidt have cracked this problem open. In a paper published in *Transactions on Machine Learning Research*, they introduce **symmetry breaking sets (SBS)** — a mathematically rigorous, fully equivariant framework for teaching neural networks to break symmetry without abandoning the elegance that makes ENNs work.

> **Key Insight:** You don't need to redesign your neural network to handle symmetry breaking. Instead, design a carefully chosen set of "symmetry breaking objects" as additional inputs — and the math of group theory tells you exactly how to pick them.

## How It Works

The paper draws a sharp distinction between two flavors of symmetry breaking. **Explicit symmetry breaking** happens when the underlying laws themselves are asymmetric. **Spontaneous symmetry breaking** is trickier and more physically fundamental: the laws are perfectly symmetric, but the system settles into one of several equally valid low-symmetry states.

Think of a ball balanced atop a hill shaped like a Mexican hat — perfectly symmetric around the peak, but the ball must fall *somewhere*, rolling into one of infinitely many equivalent positions around the rim. This is the regime that broke earlier approaches.

![Figure 1](/iaifi-research-blog/figures/2402_02681/figure_1.png)

Rather than tinkering with the internals of an existing equivariant network, Xie and Smidt propose feeding the network additional "symmetry breaking objects" alongside the original input. These objects carry just enough asymmetry to nudge the network toward one valid low-symmetry output. The trick is designing them so the whole input — original data plus symmetry breaker — still transforms correctly whenever the system is rotated, reflected, or reoriented.

Here's what "correctly" means in practice:

- **The set must be closed under the normalizer.** When you rotate or reorient the input, the symmetry-breaking objects must rearrange themselves in a matching way. The **normalizer** of a symmetry group is the set of all transformations that preserve the group's structure — all the ways you can reorient data without changing its symmetry type.
- **Minimizing set size maximizes data efficiency.** A smaller SBS means fewer symmetry-breaking copies of your data to process. The authors prove that finding the minimum-size equivariant SBS is mathematically equivalent to finding **complements** of subgroups — the minimal extra structure needed to complete a partial symmetry into a full one.
- **Counterintuitive bonus:** Sometimes it's more efficient to break *more* symmetry than strictly necessary. Breaking all symmetry of the input can yield a smaller, cleaner SBS than carefully preserving some symmetries.

![Figure 2](/iaifi-research-blog/figures/2402_02681/figure_1.png)

The researchers tabulate concrete solutions for all **point groups** — the symmetry groups describing molecules and crystals. This is the kind of reference table computational physicists will actually use: pick your input symmetry, pick your desired output symmetry, look up the table, and you have your SBS recipe.

![Figure 3](/iaifi-research-blog/figures/2402_02681/figure_2.png)

To demonstrate the framework, the paper walks through crystal distortions from high- to low-symmetry phases, ground states that break Hamiltonian symmetry, and fluid dynamics simulations where symmetric flows spontaneously develop asymmetric Kármán vortex streets. In each case, a standard equivariant network produces the full set of valid lower-symmetry outputs — something previously impossible.

## Why It Matters

Spontaneous symmetry breaking is not an edge case — it's central to some of the most important phenomena in the universe. The Higgs mechanism, which gives fundamental particles their mass, is a spontaneous symmetry breaking event. Phase transitions in materials — from ferromagnetism to superconductivity — involve it. So does the formation of large-scale structure in the early universe.

As machine learning becomes increasingly central to physics research, the inability to handle spontaneous symmetry breaking is a genuine scientific obstacle. The SBS framework removes it — and it's plug-and-play: researchers don't need to discard existing equivariant models or retrain from scratch. They simply augment their inputs using the tabulated SBS designs. The code is open-source.

This low barrier to adoption means the framework could quickly reach molecular dynamics, crystal structure prediction, quantum chemistry, and PDE solvers (software for simulating fluid flow, heat transfer, and other physical processes) — anywhere that equivariant networks are already deployed and symmetry breaking lurks.

> **Bottom Line:** Xie and Smidt have solved the spontaneous symmetry breaking problem for equivariant neural networks — not by breaking the networks, but by giving them the right extra information. The result is a general, mathematically rigorous, and practically usable framework grounded in classical group theory.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work translates a classical mathematical concept — subgroup complements — into a concrete engineering recipe for AI systems that model physical symmetry breaking, sitting at the precise intersection of abstract group theory and practical machine learning for physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The symmetry breaking set framework is the first fully equivariant solution to spontaneous symmetry breaking in neural networks, enabling ENNs to model a class of physical phenomena previously beyond their reach without sacrificing their core mathematical guarantees.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling AI models to correctly handle spontaneous symmetry breaking — the mechanism behind the Higgs field, phase transitions, and crystal distortions — this work removes a fundamental barrier to deploying machine learning in quantum chemistry, condensed matter physics, and particle physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work includes extending the framework to continuous groups and infinite-dimensional symmetries; the full tabulation of point group solutions is available in the paper (*Transactions on Machine Learning Research*, October 2024; code at github.com/atomicarchitects/equivariant-SBS).</span></div></div>
</div>
