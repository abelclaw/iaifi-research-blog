---
abstract: We study the behavior of toric Landau-Ginzburg models under extremal contraction
  and minimal model program. We also establish a relation between the moduli space
  of toric Landau-Ginzburg models and the geography of central models. We conjecture
  that there is a correspondence between extremal contractions and minimal model program
  on Fano varieties, and degenerations of their associated toric Landau-Ginzburg models
  written explicitly. We prove the conjectures for smooth toric varieties, as well
  as general smooth Fano varieties in dimensions 2 and 3. As an application, we compute
  the elementary syzygies for smooth Fano threefolds.
arxivId: '2506.15427'
arxivUrl: https://arxiv.org/abs/2506.15427
authors:
- Yang He
- Artan Sheshmani
concepts:
- landau-ginzburg mirror symmetry
- mori minimal model program
- sarkisov program
- fano variety geometry
- threefold syzygies
- quantum field theory
- toric geometry
- moduli space
- string theory
- laurent polynomial mutations
- symmetry breaking
- inverse problems
figures:
- /iaifi-research-blog/figures/2506_15427/figure_1.png
pdfUrl: https://arxiv.org/pdf/2506.15427v2
published: '2025-06-18T13:02:22+00:00'
theme: Foundational AI
title: Geography of Landau-Ginzburg models and threefold syzygies
wordCount: 940
---

## The Big Picture

Imagine cataloging every route between two mountain ranges, not just direct paths, but every detour and shortcut that counts as "mathematically equivalent." That's the challenge algebraic geometers face with **birational maps**: transformations between complex geometric shapes that look different on the surface but are, in a precise mathematical sense, the same at their core.

For decades, the goal has been to break these maps into their simplest irreducible pieces, the way you factor a large number into primes.

The **Minimal Model Program (MMP)**, developed in the 1980s, gives mathematicians a systematic procedure for simplifying multidimensional shapes. Think of it as repeatedly smoothing wrinkles in fabric until you reach the flattest possible form. One of its key outputs: **Mori fibre spaces**, the irreducible building blocks.

But knowing the building blocks is only the beginning. You also need to understand how those connections *relate to each other*. These higher-order relations are called **syzygies**, and a useful analogy is grammar: not just vocabulary, but the laws governing how words combine into valid sentences.

A new paper by Yang He and Artan Sheshmani tackles this problem by borrowing tools from theoretical physics. By tracking how physical theories called **Landau-Ginzburg models** change when their associated geometric spaces transform, they build an explicit mirror dictionary that turns previously intractable computations into concrete calculations.

> **Key Insight:** Extremal contractions in the Minimal Model Program, the fundamental geometric surgeries on Fano varieties, correspond precisely to degenerations of their mirror Landau-Ginzburg models. This turns a hard algebraic problem into a tractable geometric one.

## How It Works

The foundation is **mirror symmetry**, one of the most surprising ideas to come out of string theory. Every **Fano variety** (a geometric space with positive curvature, like a sphere generalized to many dimensions) has a mirror partner: a Landau-Ginzburg model defined by a polynomial called a **superpotential**, essentially an equation encoding the energy landscape of the system. These two descriptions look completely different but encode equivalent mathematical information. Physicists discovered this duality; mathematicians have spent decades making it precise.

![Figure 1](/iaifi-research-blog/figures/2506_15427/figure_1.png)

He and Sheshmani ask a sharper question: what happens to the Landau-Ginzburg model when you *transform* its corresponding Fano variety? When the MMP performs an **extremal contraction**, a surgery that collapses certain curves or subspaces, how does the mirror respond? Their answer comes in three flavors:

- **Divisorial contractions** (collapsing a high-dimensional subspace) → straightforward degenerations of the superpotential
- **Mori fibre spaces** (the MMP's endpoint) → **Tyurin degenerations**, where the mirror splits into two distinct pieces
- **Flips and flops** (birational modifications preserving essential structure) → **wall-crossings** in the parameter space of LG models, where one description abruptly transitions to another

The authors first prove these correspondences for **toric varieties**, a class of shapes where all the geometry reduces to combinatorial data: arrays of numbers and geometric grids. Here everything is explicit. You can track exactly how the **Newton polytope** (a geometric shape whose vertices encode the terms of the superpotential) changes under contraction, making the correspondence checkable by hand.


For general smooth Fano surfaces and threefolds, the proof requires more machinery. The strategy is a local-to-global construction: establish the mirror correspondence locally near each contracted curve or fiber, then patch these local pictures together across the full moduli space of central models. He and Sheshmani prove the correspondence for all smooth toric varieties and all smooth Fano varieties in dimensions 2 and 3.

## Why It Matters

The immediate payoff is a complete computation of the **elementary syzygies** for all smooth Fano threefolds, organized by **Picard number** (roughly, the number of independent curve classes). For Picard numbers 1 through 4, He and Sheshmani enumerate every elementary relation between **Sarkisov links**, the fundamental atomic transformations from which all birational maps between Fano varieties are built. All 105 smooth Fano threefolds have been classified, so computing their syzygies fully characterizes the relational structure of their birational automorphism groups.


The deeper significance is conceptual. Prior work showed that the full syzygy hierarchy lives in a contractible CW complex built from central models. This paper adds a physical interpretation: the cells of that complex correspond to Landau-Ginzburg models, and the attaching maps correspond to degenerations under the MMP. Mirror symmetry, it turns out, encodes not just individual variety-theory pairs but the entire hierarchical structure of birational geometry.

For researchers applying machine learning to algebraic geometry, explicit structural results like these syzygies are useful ground truth: known invariants to train on, geometric intuitions to test, and organizing principles that suggest where ML exploration is most likely to turn up new patterns.

> **Bottom Line:** By proving that mirror symmetry precisely encodes the algebraic relations between birational building blocks, He and Sheshmani complete the syzygy computation for all smooth Fano threefolds, turning an open problem into an explicit, checkable table.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects string-theoretic mirror symmetry with the algebraic geometry of the Minimal Model Program, showing that physical Landau-Ginzburg models encode the deepest relational structure (syzygies) of Fano variety classifications.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The explicit, computable syzygy data for all smooth Fano threefolds provides structured ground truth for machine learning approaches to algebraic geometry and topological invariant computation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper gives a new, explicit form of the mirror symmetry dictionary in dimensions 2 and 3, proving that every move in the Minimal Model Program has a precise physical counterpart in Landau-Ginzburg degeneration theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Extensions to singular Fano threefolds and higher dimensions are now within reach using the contractible CW complex framework; the full paper is available at [arXiv:2506.15427](https://arxiv.org/abs/2506.15427).</span></div></div>
</div>
