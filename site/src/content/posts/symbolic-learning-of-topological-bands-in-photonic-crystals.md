---
abstract: Topological photonic crystals (PhCs) that support disorder-resistant modes,
  protected degeneracies, and robust transport have recently been explored for applications
  in waveguiding, optical isolation, light trapping, and lasing. However, designing
  PhCs with prescribed topological properties remains challenging because of the highly
  nonlinear mapping from the continuous real-space design of PhCs to the discrete
  output space of band topology. Here, we introduce a machine learning approach to
  address this problem, employing Kolmogorov--Arnold networks (KANs) to predict and
  inversely design the band symmetries of two-dimensional PhCs with two-fold rotational
  (C2) symmetry. We show that a single-hidden-layer KAN, trained on a dataset of C2-symmetric
  unit cells, achieves high accuracy in classifying the topological classes of the
  lowest lying bands. We use the symbolic regression capabilities of KANs to extract
  algebraic formulas that express the topological classes directly in terms of the
  Fourier components of the dielectric function. These formulas not only retain the
  full predictive power of the network but also provide novel insights and enable
  deterministic inverse design. Using this approach, we generate photonic crystals
  with target topological bands, achieving high accuracy even for high-contrast, experimentally
  realizable structures beyond the training domain.
arxivId: '2505.10485'
arxivUrl: https://arxiv.org/abs/2505.10485
authors:
- Ali Ghorashi
- Sachin Vaidya
- Ziming Liu
- Charlotte Loh
- Thomas Christensen
- Max Tegmark
- Marin Soljačić
concepts:
- kolmogorov-arnold networks
- interpretability
- symbolic regression
- inverse problems
- topological photonic crystals
- classification
- band topology
- symmetry preservation
- group theory
- spectral methods
- crystal structure
- phase transitions
figures:
- /iaifi-research-blog/figures/2505_10485/figure_1.png
- /iaifi-research-blog/figures/2505_10485/figure_1.png
- /iaifi-research-blog/figures/2505_10485/figure_2.png
- /iaifi-research-blog/figures/2505_10485/figure_2.png
- /iaifi-research-blog/figures/2505_10485/figure_3.png
- /iaifi-research-blog/figures/2505_10485/figure_3.png
pdfUrl: https://arxiv.org/pdf/2505.10485v2
published: '2025-05-15T16:38:19+00:00'
theme: Experimental Physics
title: Symbolic Learning of Topological Bands in Photonic Crystals
wordCount: 1077
---

## The Big Picture

Imagine designing a stained-glass window where the color of each pane isn't about pigment but a hidden mathematical property of the glass, one that determines whether light flows through in a protected, one-way channel. Change the shape of a single tile and the whole character of the system can flip. That is the challenge facing physicists who work with **topological photonic crystals**: materials engineered at the microscopic scale to guide light with unusual resistance to flaws and disorder.

These aren't science fiction. Photonic crystals, materials with a repeating microscopic structure that governs how light moves, already appear in lasers, optical isolators, and waveguides. The topological varieties add something extra: channels of light that refuse to bounce backward when they hit a scratch, impurity, or defect. This robustness comes not from physical toughness but from abstract mathematical properties of the material's structure, properties that act like a guarantee written in geometry.

Designing a photonic crystal with exactly this kind of protected behavior has been brutally hard. The relationship between a crystal's physical shape and its topological properties is wildly unpredictable. Change one geometric parameter and the topology can shift in ways no simple rule anticipates. Traditional approaches amount to expensive guesswork: sweep through design parameters, run computationally intensive simulations, and hope you land somewhere useful.

A team at MIT, with collaborators at Yale and DTU and affiliated with IAIFI, has now cracked this problem open. They didn't just build a machine learning model that predicts topology. They made the model explain itself in the form of explicit, human-readable algebraic formulas.

> **Key Insight:** By training Kolmogorov-Arnold Networks on photonic crystal datasets, the researchers extracted compact mathematical formulas directly linking crystal geometry to band topology, enabling deterministic inverse design without any black-box guesswork.

## How It Works

The team focused on two-dimensional photonic crystals with **C₂ symmetry**, meaning the structure looks identical after a 180-degree rotation. This symmetry restricts how light can behave at four special locations in the crystal's **momentum space** (the mathematical "wave space" where the repeating structure most strongly shapes light): the Γ, B, Y, and A points.

At each of these landmark points, every light mode picks up a label of +1 or −1, depending on how it transforms under that rotation. The pattern of labels determines whether the crystal's lowest energy band is topologically ordinary or **topologically nontrivial**, hosting protected features like **Dirac points** (where two energy bands touch and light behaves like a massless particle) or edge states that survive small imperfections.

![Figure 1](figure:1)

Each crystal's geometry enters through the **dielectric function** ε(r), a map describing how strongly each point in the repeating unit cell interacts with light. The trick is to represent this map as a **Fourier series**: a sum of sinusoidal waves at different spatial scales, each with its own amplitude. Instead of feeding a raw image of the crystal into a neural network, each crystal is described by its Fourier coefficients, a compact, physics-informed fingerprint that captures what actually matters about the geometry.

Rather than a standard deep neural network, the researchers chose **Kolmogorov-Arnold Networks (KANs)**, a recently developed architecture that replaces fixed activation functions at neurons with learnable functions on connections. The payoff: KANs are naturally suited to **symbolic regression**, meaning they can be "read" after training to yield algebraic expressions rather than an opaque grid of weights. The team trained a single-hidden-layer KAN on C₂-symmetric unit cells, augmenting the dataset fourfold by exploiting shifts between **Wyckoff positions**, the special high-symmetry sites defined by a crystal's repeating structure.

![Figure 2](figure:2)

The KAN achieved greater than 99% accuracy in classifying topological classes. But the real prize came from symbolic regression on the trained network, which revealed something clean: **only the smallest Fourier components, the lowest-frequency spatial harmonics, actually determine band topology**. Higher Fourier modes are essentially irrelevant. This is consistent with degenerate perturbation theory, a standard technique for predicting how symmetry-related changes shift energy levels, now confirmed and quantified by machine learning on real crystallographic data.

From these extracted formulas, the team built an inverse design pipeline:

1. **Choose a target topology**: bands hosting Dirac points, a specific Chern number, or protected edge states.
2. **Apply the algebraic formula** to identify which Fourier components are required.
3. **Generate crystal geometries** satisfying those constraints, deterministically, with no optimization loop.

The formulas work even for high-contrast, two-tone photonic crystals outside the training distribution, structures directly realizable with standard fabrication techniques.

![Figure 3](figure:3)

## Why It Matters

The photonics application is compelling on its own. But the deeper significance lies in what interpretable machine learning can do for materials design. Most AI-driven design tools in physics are black boxes: they predict well but explain nothing. Here, the machine didn't just learn the answer. It learned the *rule*, expressed in language a physicist can immediately use and extend.

The combination of KANs with topological band theory creates a template that reaches well past photonic crystals. Topological classification problems arise across condensed matter physics, acoustic metamaterials, and mechanical systems. Anywhere a complex geometric design maps to a discrete topological output, this approach (parameterize by Fourier modes, train a KAN, extract symbolic formulas) offers a path to both prediction and interpretable inverse design.

That the formulas generalize beyond the training domain is the part worth paying attention to. The model didn't memorize; it found the underlying physics.

![Figure 4](figure:4)

> **Bottom Line:** KANs don't just predict which photonic crystals are topological — they hand you the formula to design them, achieving deterministic inverse design of experimentally realizable structures with over 99% accuracy and interpretable algebraic rules.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work fuses topological condensed matter theory, photonic crystal engineering, and interpretable machine learning, using IAIFI's blend of AI and fundamental physics to extract human-readable laws from complex physical systems.

- **Impact on Artificial Intelligence:** The paper shows that Kolmogorov-Arnold Networks can perform symbolic regression on real physics datasets to yield compact, generalizable algebraic formulas, making the case for interpretable AI as a genuine scientific discovery tool and not just a prediction engine.

- **Impact on Fundamental Interactions:** By uncovering that only the lowest Fourier harmonics of the dielectric function govern band topology, the work establishes new analytical design principles for topological photonic systems, allowing deterministic engineering of disorder-resistant light transport.

- **Outlook and References:** Future directions include extending the KAN-based symbolic approach to higher-symmetry photonic crystals and to electronic topological materials; the work is available at [arXiv:2505.10485](https://arxiv.org/abs/2505.10485).
