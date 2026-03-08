---
abstract: We investigate the structure of confining and deconfining phases in SU(2)
  lattice gauge theory via persistent homology, which gives us access to the topology
  of a hierarchy of combinatorial objects constructed from given data. Specifically,
  we use filtrations by traced Polyakov loops, topological densities, holonomy Lie
  algebra fields, as well as electric and magnetic fields. This allows for a comprehensive
  picture of confinement. In particular, topological densities form spatial lumps
  which show signatures of the classical probability distribution of instanton-dyons.
  Signatures of well-separated dyons located at random positions are encoded in holonomy
  Lie algebra fields, following the semi-classical temperature dependence of the instanton
  appearance probability. Debye screening discriminating between electric and magnetic
  fields is visible in persistent homology and pronounced at large gauge coupling.
  All employed constructions are gauge-invariant without a priori assumptions on the
  configurations under study. This work showcases the versatility of persistent homology
  for statistical and quantum physics studies, barely explored to date.
arxivId: '2208.03955'
arxivUrl: https://arxiv.org/abs/2208.03955
authors:
- Daniel Spitz
- Julian M. Urban
- Jan M. Pawlowski
concepts:
- persistent homology
- lattice gauge theory
- phase transitions
- instanton-dyons
- topology-based observables
- monte carlo methods
- quantum field theory
- symmetry breaking
- debye screening
- stochastic processes
- renormalization
figures:
- /iaifi-research-blog/figures/2208_03955/figure_1.png
- /iaifi-research-blog/figures/2208_03955/figure_1.png
- /iaifi-research-blog/figures/2208_03955/figure_2.png
- /iaifi-research-blog/figures/2208_03955/figure_2.png
- /iaifi-research-blog/figures/2208_03955/figure_3.png
- /iaifi-research-blog/figures/2208_03955/figure_3.png
pdfUrl: https://arxiv.org/pdf/2208.03955v2
published: '2022-08-08T07:49:58+00:00'
theme: Theoretical Physics
title: Confinement in non-Abelian lattice gauge theory via persistent homology
wordCount: 1222
---

## The Big Picture

Imagine trying to pull a single quark out of a proton. No matter how hard you yank, the force between quarks doesn't weaken with distance. They're connected by something like a rubber band that gets stronger as you stretch it. Eventually the band snaps, but instead of freeing a quark, it creates a new quark-antiquark pair. Physicists call this **confinement**, and it has been a puzzle for decades. We know it happens. We still don't fully understand *why*.

The mathematical framework governing quarks, **quantum chromodynamics (QCD)**, is notoriously hard to solve exactly. To make progress, physicists divide spacetime into a fine grid and simulate the theory numerically, a computationally intensive approach called **lattice gauge theory**. Even then, extracting clean signals from the quantum noise requires elaborate tricks: fixing a reference frame in the math, smoothing out fluctuations, projecting onto specific structures. Each assumption can color the results.

A team of physicists has brought a tool from data science, **persistent homology**, to bear on the confinement phase transition. Persistent homology extracts topological shape information from complex datasets, and it turns out to work cleanly on raw lattice data with no gauge-fixing required.

> **Key Insight:** Persistent homology acts as a gauge-invariant probe of the hidden topological structures governing confinement, picking up signatures of instanton-dyons and Debye screening directly from unprocessed lattice data.

## How It Works

The researchers work with **SU(2) lattice gauge theory**, a simpler cousin of full QCD that captures the essential mathematics of the strong force (its "non-Abelian" nature, meaning the order in which transformations are applied matters) while remaining computationally manageable. They simulate the theory on a 32³ × 8 Euclidean spacetime lattice, with three spatial dimensions plus a compact temporal dimension whose size encodes temperature, using the Hybrid Monte Carlo algorithm to sample quantum field configurations.

The central tool is persistent homology. Rather than examining field values directly, the method builds a sequence of geometric objects, called **cubical complexes**, by progressively including lattice sites based on the value of some field quantity. This step-by-step inclusion process is called a **filtration**. As you lower the threshold, topological features (connected regions, loops, voids) appear and disappear. Persistent homology tracks *how long* each feature survives. Long-lived features are real; short-lived ones are noise.

![Figure 1](figure:1)

The team constructs filtrations from five gauge-invariant observables:

1. **Traced Polyakov loops** — measures of how a quark's quantum state transforms as it travels through the full temporal extent of the simulation; the standard diagnostic for confinement
2. **Topological densities** — local measures of how the gauge field twists through topological configurations
3. **Holonomy Lie algebra fields** — a projection of the Polyakov loop encoding the local geometry of the gauge field
4. **Electric and magnetic field strengths** — split components of the gauge field energy density

Each filtration illuminates a different facet of the confinement physics.

![Figure 2](figure:2)

The topological density filtration yields the most revealing results. In the confined phase, the topological density organizes into spatial **lumps** rather than string-like structures. The persistence diagrams (scatter plots where each dot represents a topological feature with its birth and death threshold) show a distribution matching the expected signature of **instanton-dyons**.

These are semi-classical objects, sitting at the boundary between quantum and classical physics, that many theorists believe drive confinement. Think of them as localized knots of field energy arising at finite temperature. The lumps survive cooling, a procedure that smooths quantum fluctuations while preserving classical structures. That they persist confirms their near-classical nature.

![Figure 3](figure:3)

The holonomy field filtration adds another layer. It encodes signatures of well-separated dyons at random positions, and their abundance declines with rising temperature in a way that matches theoretical predictions. As the system crosses from confined to deconfined, the persistent homology signal changes qualitatively. No fitting, no modeling, just a clean signature of the phase transition.

![Figure 4](figure:4)

The electric and magnetic field filtrations produce what may be the most satisfying result. In a deconfined plasma, **Debye screening** operates asymmetrically: electric fields decay exponentially with distance while magnetic fields do not. This asymmetry is a hallmark of deconfinement.

Above the critical temperature, the persistent homology of the two field types diverges sharply. Electric fields show markedly different topological structure than magnetic fields, an effect especially pronounced at large gauge coupling.

![Figure 5](figure:5)

## Why It Matters

Persistent homology detects signatures of instanton-dyons, objects previously accessible only through computationally expensive cooling and fermion overlap techniques, directly from unsmoothed, unfixed gauge configurations. The method is entirely gauge-invariant and makes no prior assumptions about what classical objects might be hiding in the data. That opens a path to studying topological structure in full QCD without the procedural baggage that has historically complicated interpretation.

The implications go beyond lattice gauge theory. Persistent homology sits at the crossroads of pure mathematics, data science, and computational physics. Here, topological data analysis tools developed largely in machine learning contexts turn out to be precision instruments for quantum field theory. Future directions include larger lattice geometries, different gauge groups, and the inclusion of dynamical fermions. As quantum computing matures, quantum algorithms for persistent homology could push these analyses to scales currently out of reach.

![Figure 6](figure:6)

> **Bottom Line:** By applying persistent homology to SU(2) lattice gauge theory, this work reveals the topological fingerprints of instanton-dyons and Debye screening without any gauge-fixing or smoothing, establishing topological data analysis as an underexplored but potent tool for quantum field theory.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects topological data analysis, a mathematical framework developed partly for machine learning, with non-perturbative quantum field theory. Data science tools yield genuinely new physical insights into confinement.

- **Impact on Artificial Intelligence:** The study establishes persistent homology as an interpretable feature-extraction method for high-dimensional physical field configurations, expanding the toolkit of physics-informed ML and topological machine learning.

- **Impact on Fundamental Interactions:** The research provides gauge-invariant, assumption-free evidence for instanton-dyon signatures and Debye screening in SU(2) lattice gauge theory, advancing understanding of the topological mechanisms driving the confinement-deconfinement phase transition.

- **Outlook and References:** Future work will extend this approach to larger lattices, full QCD with dynamical fermions, and gauge groups with trivial center; the paper is available at [arXiv:2208.03955](https://arxiv.org/abs/2208.03955).

## Original Paper Details
- **Title:** Confinement in non-Abelian lattice gauge theory via persistent homology
- **arXiv ID:** 2208.03955
- **Authors:** ["Daniel Spitz", "Julian M. Urban", "Jan M. Pawlowski"]
- **Abstract:** We investigate the structure of confining and deconfining phases in SU(2) lattice gauge theory via persistent homology, which gives us access to the topology of a hierarchy of combinatorial objects constructed from given data. Specifically, we use filtrations by traced Polyakov loops, topological densities, holonomy Lie algebra fields, as well as electric and magnetic fields. This allows for a comprehensive picture of confinement. In particular, topological densities form spatial lumps which show signatures of the classical probability distribution of instanton-dyons. Signatures of well-separated dyons located at random positions are encoded in holonomy Lie algebra fields, following the semi-classical temperature dependence of the instanton appearance probability. Debye screening discriminating between electric and magnetic fields is visible in persistent homology and pronounced at large gauge coupling. All employed constructions are gauge-invariant without a priori assumptions on the configurations under study. This work showcases the versatility of persistent homology for statistical and quantum physics studies, barely explored to date.
