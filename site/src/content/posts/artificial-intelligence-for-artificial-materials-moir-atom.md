---
abstract: Moiré engineering in atomically thin van der Waals heterostructures creates
  artificial quantum materials with designer properties. We solve the many-body problem
  of interacting electrons confined to a moiré superlattice potential minimum (the
  moiré atom) using a 2D fermionic neural network. We show that strong Coulomb interactions
  in combination with the anisotropic moiré potential lead to striking ``Wigner molecule"
  charge density distributions observable with scanning tunneling microscopy.
arxivId: '2303.08162'
arxivUrl: https://arxiv.org/abs/2303.08162
authors:
- Di Luo
- Aidan P. Reddy
- Trithep Devakul
- Liang Fu
concepts:
- fermionic neural network
- moiré superlattice
- quantum states
- wigner molecule
- symmetry preservation
- monte carlo methods
- quantum simulation
- effective field theory
- phase transitions
- materials discovery
- tensor networks
figures:
- /iaifi-research-blog/figures/2303_08162/figure_1.png
- /iaifi-research-blog/figures/2303_08162/figure_2.png
- /iaifi-research-blog/figures/2303_08162/figure_3.png
pdfUrl: https://arxiv.org/pdf/2303.08162v2
published: '2023-03-14T18:21:50+00:00'
theme: Theoretical Physics
title: 'Artificial intelligence for artificial materials: moiré atom'
wordCount: 1207
---

## The Big Picture

Imagine stacking two sheets of graphene, each just one atom thick, and twisting one ever so slightly. A subtle interference pattern emerges across the surface, like the shimmer you see when two window screens overlap. This creates an entirely new periodic structure called a **moiré superlattice**: a slower, larger-scale pattern layered over the underlying atomic lattice.

Electrons moving through this twisted terrain experience a world unlike anything in ordinary materials. The interference creates tiny energy dips spaced nanometers apart, each capable of trapping a handful of electrons like a miniature artificial atom. These **moiré atoms** are laboratories where exotic quantum physics can be dialed in by adjusting the twist angle or applying a voltage.

The problem is that understanding what electrons actually *do* inside these traps is fiendishly hard. Quantum mechanics demands tracking all electrons simultaneously, accounting for how each one electrically repels every other. Add the warped, asymmetric shape of the moiré potential well (not a simple bowl, but a potential with hexagonal or triangular symmetry) and conventional methods buckle.

Exact diagonalization computes the right answer by brute force, but only for tiny systems. Hartree-Fock and density functional theory, the standard workhorses of physics and chemistry, either ignore the subtle correlations that make moiré physics interesting or break down in the low-density regime where interactions dominate.

A team from MIT and Harvard has cut through this complexity using a 2D fermionic neural network, an AI architecture trained to represent quantum wavefunctions. They found that multi-electron moiré atoms develop geometric charge distributions called **Wigner molecules** that should be directly visible under a scanning tunneling microscope.

> **Key Insight:** By training a neural network to encode the full many-body quantum wavefunction, the researchers solved a problem that conventional methods couldn't, revealing that moiré atoms form crystalline electron arrangements whose shapes encode deep physics about interactions and symmetry.

## How It Works

The starting point is a deceptively clean model. In semiconductor moiré heterostructures (layered combinations like WSe₂ on WS₂, or twisted molybdenum diselenide bilayers) electrons feel two things: a gently varying periodic potential with the periodicity of the moiré lattice, and the electrical repulsion of every other electron. The **continuum Hamiltonian**, the equation describing all forces on the electrons, is essentially the old "jellium model" of electron gases, now living in a potential with crystal symmetry rather than in flat space.

![Figure 1](/iaifi-research-blog/figures/2303_08162/figure_1.png)

The researchers focused on a single moiré potential minimum, one isolated atom. They expanded the moiré potential around its minimum up to sixth order in distance from the center, yielding a harmonic oscillator core plus higher-order **moiré crystal field** corrections. These corrections warp the bowl into hexagonal or triangular shapes depending on a phase parameter φ, which is controlled by the choice of material.

For **transition metal dichalcogenide (TMD) heterobilayers**, a family of layered semiconductors pairing metals like molybdenum or tungsten with chalcogen atoms like sulfur or selenium, φ ranges from near 0° to 45°. This makes it experimentally tunable across material choices. The team focused on φ = 30°, V₀ = 20 meV, and dielectric constant ε = 10: realistic values for actual TMD devices.

With the Hamiltonian defined, solving the many-body Schrödinger equation for N interacting electrons is the hard part. The team used a **2D fermionic neural network** built on the FermiNet architecture. Unlike grid or basis-set methods, whose cost explodes exponentially with particle number, FermiNet parameterizes a neural network in continuous real space whose outputs automatically obey the antisymmetry rule of fermionic quantum mechanics: the wavefunction must flip sign whenever two electrons are exchanged (the Pauli exclusion principle). Key features of the approach:

- The network represents the full many-body wavefunction, not a mean-field approximation
- Training minimizes the variational energy, so the network learns the ground state by optimizing itself
- Antisymmetry (Pauli exclusion) is built directly into the architecture, not imposed after the fact
- The 2D adaptation handles the specific geometry and interaction structure of moiré systems

The calculation's output is the **electron charge density**, the probability of finding an electron at each point in space, for moiré atoms holding one to several electrons.

## Why It Matters

For a single electron, the charge density hugs the bottom of the potential well in a roughly symmetric cloud. Add more electrons, and something dramatic happens.

Electrical repulsion fights confinement, and the electrons arrange into geometric patterns (triangles, squares, pentagons) like charges evenly distributed on a tiny two-dimensional cage. These are **Wigner molecules**, named for Eugene Wigner, who predicted that strongly interacting electrons would crystallize into ordered arrangements. Wigner molecules were already known in semiconductor quantum dots, but the moiré setting adds a twist: the crystal field breaks rotational symmetry and locks the Wigner molecule's orientation to the underlying lattice, making each pattern a fingerprint of the material's symmetry.

![Figure 2](/iaifi-research-blog/figures/2303_08162/figure_2.png)

This isn't just theory. Scanning tunneling microscopy (STM) can image electron density at atomic resolution, and modern STM experiments on moiré systems have already resolved individual trapped electrons. The charge density patterns predicted by the neural network, whether triangular or hexagonal depending on φ, should be directly observable.

That means you could measure the charge density shape in a known TMD heterostructure and infer the interaction strength and crystal field symmetry, effectively using the moiré atom as a quantum sensor for its own physics.

![Figure 3](/iaifi-research-blog/figures/2303_08162/figure_3.png)

The payoff runs in two directions. For condensed matter physics, neural networks can now solve strongly-correlated continuum models without the approximations that held back earlier methods: no band truncation, no self-interaction error, no neglected quantum correlations. For machine learning, neural network quantum states have arrived as practical tools for real materials problems, not just toy models.

FermiNet was first developed for quantum chemistry of real atoms. Now it extends to engineered "artificial atoms" with qualitatively different physics. Open questions remain. How do Wigner molecule states evolve as more electrons are added, approaching the regime of moiré Mott insulators and anomalous Hall states? Can the method scale to coupled moiré atoms, a moiré "molecule" or full lattice? And can it resolve ongoing debates about strongly correlated phases in twisted bilayer graphene and TMD systems?

> **Bottom Line:** A fermionic neural network solved a quantum many-body problem that defeated conventional methods, predicting Wigner molecule electron arrangements in moiré atoms. This is a concrete, testable prediction for STM experiments and a proof of concept for AI-driven study of artificial quantum materials.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work brings neural network quantum state methods together with the physics of moiré heterostructures, showing that machine learning architectures can directly address open problems in strongly-correlated condensed matter.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">FermiNet-style fermionic neural networks now extend into 2D materials physics, achieving accuracies beyond exact diagonalization, Hartree-Fock, and density functional theory in the relevant parameter regime.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By predicting observable Wigner molecule charge density profiles in moiré atoms, the research connects the abstract many-body Coulomb problem to a measurable STM signature, establishing moiré atoms as a tunable system for studying strong electron correlations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend this approach to coupled moiré atom arrays and finite-temperature dynamics, with potential to guide the design of engineered quantum phases; full results appear at [arXiv:2303.08162](https://arxiv.org/abs/2303.08162).</span></div></div>
</div>
