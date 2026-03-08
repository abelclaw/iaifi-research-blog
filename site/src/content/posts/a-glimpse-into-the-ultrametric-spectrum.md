---
abstract: The non-relativistic string spectrum is built from integer-spaced energy
  quanta in such a way that the high-temperature asymptotics, via the Hardy-Ramanujan
  formula for integer partitions, reduces to standard two-dimensional thermodynamics.
  Here we explore deformed realizations of this behavior motivated by $p$-adic string
  theory and Lorentzian versions thereof with a non-trivial spectrum. We study the
  microstate scaling that results on associating quantum harmonic oscillators to the
  normal modes of tree-graphs rather than string graphs and observe that Hardy-Ramanujan
  scaling is not realized. But by computing the eigenvalues of the derivative operator
  on the $p$-adic circle and by determining the eigenspectrum of the Neumann-to-Dirichlet
  operator, we uncover a spectrum of exponentially growing energies but with exponentially
  growing degeneracies balanced in such a way that Hardy-Ramanujan scaling is realized,
  but modulated with log-periodic fluctuations.
arxivId: '2601.03738'
arxivUrl: https://arxiv.org/abs/2601.03738
authors:
- An Huang
- Christian B. Jepsen
concepts:
- ultrametric spectrum
- string theory
- p-adic string theory
- spectral methods
- eigenvalue decomposition
- log-periodic fluctuations
- quantum field theory
- conformal field theory
- phase transitions
figures:
- /iaifi-research-blog/figures/2601_03738/figure_1.png
- /iaifi-research-blog/figures/2601_03738/figure_2.png
- /iaifi-research-blog/figures/2601_03738/figure_3.png
pdfUrl: https://arxiv.org/pdf/2601.03738v1
published: '2026-01-07T09:27:25+00:00'
theme: Theoretical Physics
title: A glimpse into the Ultrametric spectrum
wordCount: 1389
---

## The Big Picture

Imagine measuring distance not by how far apart two cities are on a map, but by how many levels up a family tree you have to climb to find a common ancestor. That strange alternative geometry, called an **ultrametric**, treats things as "close" when they share deep common ancestry, not when they happen to sit near each other in space.

This idea is the mathematical heart of a decades-old proposal for reinventing string theory from the ground up. Two theorists have now taken a serious step toward making that proposal work, uncovering a hidden spectrum that behaves, against all odds, just like ordinary strings.

String theory's most famous prediction is an infinite tower of vibrating states, each successive mode heavier than the last, arranged with mathematical regularity. That regularity has a thermodynamic consequence: the number of ways to pack a given amount of energy into string vibrations follows a formula Hardy and Ramanujan proved over a century ago. It's an entropy fingerprint, a signature that distinguishes string theory from nearly everything else.

The question An Huang and Christian Jepsen set out to answer: can you reconstruct that fingerprint in a world built not on ordinary numbers, but on ***p*-adic numbers**? In this alternative number system, "closeness" is measured by divisibility rather than size, producing a universe with a naturally tree-like, hierarchical structure.

Their answer is yes, but with a twist. The ultrametric string spectrum does reproduce Hardy-Ramanujan scaling, but it pulses with rhythmic **log-periodic fluctuations**, repeating oscillations that appear each time the energy increases by a fixed multiplicative factor. These have no counterpart in the ordinary string.

> **Key Insight:** Exponentially growing energy levels and exponentially growing degeneracies in the *p*-adic string spectrum cancel each other out to preserve the thermodynamic signature of ordinary string theory, but leave a distinctive oscillating imprint.

## How It Works

The researchers built their analysis around a central analogy. A string, discretized into a chain of beads, is mathematically equivalent to an infinite path graph, a chain where every interior vertex has exactly two neighbors. The **Bruhat-Tits tree** (also known as the Bethe lattice) is the natural *p*-adic analog: a branching tree where every vertex has *p*+1 neighbors. Picture an infinite family tree where every member has exactly the same number of descendants, forever. The question is whether quantizing vibrations on this tree-graph produces the same thermodynamic behavior as quantizing vibrations on a string.

The first answer is no. When Huang and Jepsen associated quantum harmonic oscillators to the **normal modes** (the independent vibration patterns of the whole system, like the distinct notes a plucked guitar string can ring out) of finite tree-graphs, the results depended critically on boundary conditions:

- **Neumann boundary conditions** (free ends) produce a non-trivial spectrum with exponentially spaced modes, each with exponentially growing degeneracy.
- **Dirichlet boundary conditions** (fixed ends) produce an infinitely large gap at the bottom, useless for building a continuous tower of states.
- **Periodic boundary conditions** essentially can't be taken to the infinite-size limit for trees with *p* > 1, because no suitable infinite Moore graph exists.

So the simple tree approach fails. But the Neumann case hinted at something: even though the overall scaling is wrong, the spectrum has exponentially spaced levels with exponentially growing degeneracies. Could these two effects balance?

![Figure 1](figure:1)

The real breakthrough came when the authors shifted focus from tree-graphs to the ***p*-adic circle**, written U*p*. This is the set of *p*-adic numbers with unit norm, the hierarchical world's equivalent of the ordinary unit circle that underlies standard string quantization. The relevant operator is the **Vladimirov derivative**, the *p*-adic analog of ordinary differentiation: a mathematically rigorous way to measure how quickly functions change in an ultrametric space. Computing its eigenvalues on U*p* yields concrete spectra for small primes:

- *p* = 2: energies 2, 5, 11, 23, 47, 95, … with degeneracies 1, 2, 4, 8, 16, 32, …
- *p* = 3: energies 1, 5, 17, 53, 161, 485, … with degeneracies 1, 4, 12, 36, 108, 324, …

The pattern jumps out. Energies grow roughly like *p*^*n*, while degeneracies grow like (*p*−1)·*p*^(*n*−1). The ratio stays controlled in just the right way.

![Figure 2](figure:2)

To extract the thermodynamics, the researchers computed the **partition function**, the fundamental accounting tool of statistical mechanics that tallies all possible states weighted by their thermal probability. Getting the high-temperature asymptotics right required care: both energies and degeneracies grow exponentially, so standard approximation schemes break down. The authors developed a systematic expansion showing that entropy scales as the square root of energy, exactly as in the ordinary non-relativistic string.

But the entropy doesn't simply scale like √*E*. It oscillates. The leading behavior is Hardy-Ramanujan-like, modulated by log-periodic fluctuations that repeat every time the energy increases by a fixed multiplicative factor. This is a hallmark of **discrete scale invariance**: the ultrametric world is hierarchical by construction, and that hierarchy leaves its mark on the thermodynamics.

![Figure 3](figure:3)

The same spectrum also arises as the eigenspectrum of the **Neumann-to-Dirichlet operator** on U*p*, a boundary-value operator that maps how steeply a function slopes at an edge to the function's value there. This connection gives an independent derivation of the ultrametric string spectrum, confirming its mathematical naturality.

## Why It Matters

*P*-adic string theory has been discussed since the 1980s, but the original Freund-Olson formulation contained only a single state, the tachyon, making it phenomenologically barren. Huang and Jepsen's construction points toward a richer ultrametric string theory with a genuine tower of states, bringing it much closer to the real thing.

The log-periodic fluctuations are not a bug. Such oscillations appear in critical phenomena on hierarchical lattices, in systems near catastrophic failure, and in certain quantum gravity models. Their presence in the ultrametric string entropy reflects a concrete mathematical fact: discrete scale invariance leaves oscillatory fingerprints wherever it goes. Future work will need to address whether these oscillations survive in a fully Lorentz-covariant setting, and whether they carry observable consequences.

There is also an experimental angle. Within the past five years, researchers have engineered spin systems that interpolate between ordinary linear order and *p*-adic (2-adic) hierarchical order. As experimental control of ultrametric systems improves, the thermodynamic signatures described here may become directly testable.

> **Bottom Line:** By computing the *p*-adic analog of the string's vibrational spectrum, Huang and Jepsen show that ultrametric string theory can reproduce the hallmark thermodynamic scaling of ordinary strings, opening a new path toward a hierarchical reformulation of string theory with a rich state tower.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects number theory (*p*-adic analysis, the Vladimirov derivative) with theoretical physics (string thermodynamics, the Hardy-Ramanujan formula), showing that tools from pure mathematics can reveal deep structure in candidate quantum gravity theories.

- **Impact on Artificial Intelligence:** The log-periodic fluctuations and discrete scale invariance uncovered here are mathematically related to patterns that appear in hierarchical machine learning models and in the analysis of neural network loss landscapes on tree-structured data.

- **Impact on Fundamental Interactions:** The paper provides the first concrete example of an ultrametric string spectrum with a non-trivial tower of states that reproduces Hardy-Ramanujan entropy scaling, advancing the long-standing goal of constructing a *p*-adic string theory with genuine string-like physics.

- **Outlook and References:** Future work will explore Lorentz-covariant generalizations and the role of log-periodic oscillations in full quantum ultrametric string theory; the paper is available at [arXiv:2601.03738](https://arxiv.org/abs/2601.03738).

## Original Paper Details
- **Title:** A glimpse into the Ultrametric spectrum
- **arXiv ID:** 2601.03738
- **Authors:** ["An Huang", "Christian B. Jepsen"]
- **Abstract:** The non-relativistic string spectrum is built from integer-spaced energy quanta in such a way that the high-temperature asymptotics, via the Hardy-Ramanujan formula for integer partitions, reduces to standard two-dimensional thermodynamics. Here we explore deformed realizations of this behavior motivated by $p$-adic string theory and Lorentzian versions thereof with a non-trivial spectrum. We study the microstate scaling that results on associating quantum harmonic oscillators to the normal modes of tree-graphs rather than string graphs and observe that Hardy-Ramanujan scaling is not realized. But by computing the eigenvalues of the derivative operator on the $p$-adic circle and by determining the eigenspectrum of the Neumann-to-Dirichlet operator, we uncover a spectrum of exponentially growing energies but with exponentially growing degeneracies balanced in such a way that Hardy-Ramanujan scaling is realized, but modulated with log-periodic fluctuations.
