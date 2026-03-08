---
abstract: Topological materials present unconventional electronic properties that
  make them attractive for both basic science and next-generation technological applications.
  The majority of currently known topological materials have been discovered using
  methods that involve symmetry-based analysis of the quantum wavefunction. Here we
  use machine learning to develop a simple-to-use heuristic chemical rule that diagnoses
  with a high accuracy whether a material is topological using only its chemical formula.
  This heuristic rule is based on a notion that we term topogivity, a machine-learned
  numerical value for each element that loosely captures its tendency to form topological
  materials. We next implement a high-throughput procedure for discovering topological
  materials based on the heuristic topogivity-rule prediction followed by ab initio
  validation. This way, we discover new topological materials that are not diagnosable
  using symmetry indicators, including several that may be promising for experimental
  observation.
arxivId: '2202.05255'
arxivUrl: https://arxiv.org/abs/2202.05255
authors:
- Andrew Ma
- Yang Zhang
- Thomas Christensen
- Hoi Chun Po
- Li Jing
- Liang Fu
- Marin Soljačić
concepts:
- materials discovery
- classification
- interpretability
- automated discovery
- topological invariants
- crystal structure
- feature extraction
- topological semimetals
- surrogate modeling
- sparse models
- symmetry preservation
- phase transitions
figures:
- /iaifi-research-blog/figures/2202_05255/figure_1.png
- /iaifi-research-blog/figures/2202_05255/figure_2.png
- /iaifi-research-blog/figures/2202_05255/figure_3.png
pdfUrl: https://arxiv.org/pdf/2202.05255v3
published: '2022-02-10T18:57:17+00:00'
theme: Astrophysics
title: 'Topogivity: A Machine-Learned Chemical Rule for Discovering Topological Materials'
wordCount: 1077
---

## The Big Picture

Imagine identifying every poisonous plant on Earth not by testing each one in a lab, but by glancing at the leaf shape and guessing. That sounds reckless for botany. But for the quantum world of topological materials, researchers at MIT just pulled off something similar: a rule so simple you could compute it by hand that predicts, with roughly 80% accuracy, whether a material harbors exotic quantum properties, using nothing more than its chemical formula.

**Topological materials** are a strange class of matter. Their electrons are governed by a mathematical property called topology, the same branch of geometry that distinguishes a donut from a sphere. Once you know the shape, you know which behaviors are possible, no matter how you deform the material without tearing it.

This topology produces striking behaviors: electrical currents that flow along surfaces and resist disruption by defects or impurities, electrons that behave like massless particles, and phenomena that could power quantum computers and next-generation electronics.

Finding these materials has been laborious. The dominant approach analyzes **quantum wavefunctions** (mathematical descriptions of electron behavior) through the lens of a crystal's geometric symmetry. It demands substantial computing power and goes blind for materials whose atomic arrangements lack the right kind of symmetry, leaving an entire class of candidates invisible.

A team led by physicists Andrew Ma, Yang Zhang, and Marin Soljačić changed the search. Using machine learning, they derived a single interpretable number for each chemical element, a quantity they call **topogivity**, and showed that a simple weighted average predicts topological character across the periodic table.

> **Key Insight:** Topogivity assigns each element a learned score capturing its tendency to join topological compounds; the weighted average of a material's elements' topogivities reveals whether that material is likely topological or trivial, no quantum calculation required.

## How It Works

The starting point is a labeled dataset from existing first-principles databases, collections of materials whose quantum-mechanical properties have been computed from scratch. The dataset covers non-magnetic, three-dimensional compounds with fixed elemental ratios, and each entry is classified as either "topological" or "trivial."

The researchers deliberately chose an interpretable ML model. Not a deep neural network, but something far simpler, because their goal wasn't just prediction accuracy. They wanted insight.

![Figure 1](figure:1)

The heuristic rule works like this:

1. **Assign a topogivity value** (τ) to each element in the periodic table, a single machine-learned number encoding how strongly that element tends to appear in topological compounds.
2. **Compute the weighted average** of the constituent elements' topogivities, weighted by their stoichiometric ratios (the proportions in which each element appears in the formula). For compound AB: ½τ_A + ½τ_B. For AC₃: ¼τ_A + ¾τ_C.
3. **Read the sign:** a positive result predicts topologically nontrivial; negative predicts trivial. Magnitude gives a rough confidence estimate.

This napkin-computable rule achieves roughly 80% classification accuracy, even though it ignores crystal structure, symmetry, and electronic wavefunctions entirely.

The ML model distilled a chemical intuition: certain elements, especially heavy atoms with large **spin-orbit coupling** (a quantum interaction between an electron's spin and its orbital motion that grows stronger in heavier elements), tend to promote topological behavior, while others suppress it. Topogivity makes that intuition quantitative.

Where this really earns its keep is in what it can *see* that conventional methods cannot. **Symmetry indicators**, the dominant computational tool for detecting topological character, work by finding mathematical patterns in electron behavior that mirror a crystal's geometric symmetry. They go blind for materials with low crystal symmetry or topological properties that don't couple to symmetry at all. That includes **Chern insulators** and **time-reversal-invariant Z₂ topological insulators**, two classes defined by topological invariants that symmetry analysis simply cannot detect. The first experimentally confirmed Weyl semimetal, tantalum arsenide (TaAs), is non-symmetry-diagnosable. Topogivity has no such blind spot.

The team built a high-throughput discovery pipeline around this idea: screen a large candidate space with the fast topogivity rule, then validate survivors with expensive **density functional theory (DFT)** calculations, a standard method that computes electronic structure from quantum-mechanical first principles. This two-stage funnel reserves DFT only for promising candidates, cutting the computational burden by a wide margin. The pipeline turned up new topological materials that are non-symmetry-diagnosable, materials that standard database searches would have missed entirely.

## Why It Matters

This work sits at a productive tension in modern materials science: interpretability versus power. Most ML breakthroughs in materials discovery involve deep networks that are accurate but opaque. They find patterns without explaining them. By insisting on interpretability, the MIT team extracted a *principle* rather than just a prediction engine.

The analogy to **electronegativity** is deliberate. Electronegativity is itself a heuristic, not a rigorous quantum observable, yet it shapes vast swaths of chemical intuition. Topogivity is after the same conceptual niche: a quick, reliable gut-check before committing to heavier calculation.

Topogivity is a hypothesis about the chemical origins of electronic topology, now testable and refinable by the broader community. As ML becomes standard in materials discovery, what models *understand* (not just predict) grows more urgent. A machine-learned number that slots into the same framework as electronegativity offers a template: using AI not to replace chemical intuition, but to quantify it in regimes where human intuition runs out.

Open questions remain. Topogivity operates only on stoichiometry, ignoring crystal structure, a significant abstraction that limits precision. Future extensions might incorporate structural motifs or learn separate topogivities conditioned on bonding environment. Whether analogous heuristics exist for magnetic topological materials, excluded from the current framework, is an open challenge.

> **Bottom Line:** By distilling the quantum complexity of electronic topology into a single number per element, topogivity makes materials discovery faster, broader, and, for the first time, chemically intuitive, uncovering topological materials invisible to every prior method.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** Machine learning can extract human-interpretable chemical rules from quantum-mechanical databases, directly connecting AI-driven pattern recognition with the physics of electronic band topology.
- **Impact on Artificial Intelligence:** Prioritizing interpretable over black-box ML models can yield transferable scientific principles, a template for using AI to generate insight, not just predictions.
- **Impact on Fundamental Interactions:** Topogivity provides the first broadly applicable chemical heuristic for identifying topological insulators and semimetals, including non-symmetry-diagnosable materials inaccessible to all existing symmetry-based approaches.
- **Outlook and References:** Future work could extend topogivity to magnetic materials and structure-conditioned variants; full methodology and discovered candidates are detailed in [arXiv:2202.05255](https://arxiv.org/abs/2202.05255).

## Original Paper Details
- **Title:** Topogivity: A Machine-Learned Chemical Rule for Discovering Topological Materials
- **arXiv ID:** 2202.05255
- **Authors:** ["Andrew Ma", "Yang Zhang", "Thomas Christensen", "Hoi Chun Po", "Li Jing", "Liang Fu", "Marin Soljačić"]
- **Abstract:** Topological materials present unconventional electronic properties that make them attractive for both basic science and next-generation technological applications. The majority of currently known topological materials have been discovered using methods that involve symmetry-based analysis of the quantum wavefunction. Here we use machine learning to develop a simple-to-use heuristic chemical rule that diagnoses with a high accuracy whether a material is topological using only its chemical formula. This heuristic rule is based on a notion that we term topogivity, a machine-learned numerical value for each element that loosely captures its tendency to form topological materials. We next implement a high-throughput procedure for discovering topological materials based on the heuristic topogivity-rule prediction followed by ab initio validation. This way, we discover new topological materials that are not diagnosable using symmetry indicators, including several that may be promising for experimental observation.
