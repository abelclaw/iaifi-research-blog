---
abstract: 'The homogeneous electron gas is a cornerstone of quantum condensed matter
  physics, providing the foundation for developing density functional theory and understanding
  electronic phases in semiconductors. However, theoretical understanding of strongly-correlated
  electrons in realistic semiconductor systems remains limited. In this work, we develop
  a neural network based variational approach to study quantum wells in three dimensional
  geometry for a variety of electron densities and well thicknesses. Starting from
  first principles, our unbiased AI-powered method reveals metallic and crystalline
  phases with both monolayer and bilayer charge distributions. In the emergent bilayer,
  we discover a new quantum phase of matter: the electronic quasicrystal.'
arxivId: '2512.10909'
arxivUrl: https://arxiv.org/abs/2512.10909
authors:
- Filippo Gaggioli
- Pierre-Antoine Graham
- Liang Fu
concepts:
- electronic quasicrystal
- monte carlo methods
- neural network variational monte carlo
- attention mechanisms
- quantum states
- phase transitions
- quantum simulation
- hamiltonian systems
- crystal structure
- quantum well bilayer
- automated discovery
- symmetry preservation
figures:
- /iaifi-research-blog/figures/2512_10909/figure_1.png
- /iaifi-research-blog/figures/2512_10909/figure_1.png
- /iaifi-research-blog/figures/2512_10909/figure_2.png
- /iaifi-research-blog/figures/2512_10909/figure_2.png
- /iaifi-research-blog/figures/2512_10909/figure_3.png
- /iaifi-research-blog/figures/2512_10909/figure_3.png
pdfUrl: https://arxiv.org/pdf/2512.10909v1
published: '2025-12-11T18:39:04+00:00'
theme: Theoretical Physics
title: 'Electronic crystals and quasicrystals in semiconductor quantum wells: an AI-powered
  discovery'
wordCount: 1172
---

## The Big Picture

Imagine billions of electrons trapped inside a thin slice of semiconductor, not moving freely, not frozen in place, but hovering somewhere in between. For decades, physicists have tried to predict what patterns these electrons form when crammed together and cooled to near absolute zero.

The math is brutally hard. Each electron interacts with every other, and the complexity multiplies exponentially with every electron added. Standard theoretical tools either miss the physics entirely or grind to a halt.

Now a team from MIT has cracked open this problem with a neural network and found something nobody expected. In wide semiconductor quantum wells (thin slabs of material that trap electrons in a flat, confined layer), interacting electrons don't just form metals or ordinary crystals. In the right conditions, they spontaneously arrange themselves into a **quasicrystal**: a structure with precise global order but no repeating unit cell, like a Penrose tiling etched in electron density. This is a new quantum phase of matter, a way electrons can organize at the lowest possible energy that no one had predicted in this setting.

Filippo Gaggioli, Pierre-Antoine Graham, and Liang Fu built an AI-powered simulation of electrons from scratch, with no assumptions about what phases they'd find. What emerged from that unbiased search rewrote the known map of how electrons arrange themselves in quantum wells.

> **Key Insight:** Using an attention-based neural network to represent quantum many-body wavefunctions, the MIT team discovered that electrons in wide semiconductor quantum wells can form an electronic quasicrystal, a phase with no classical analogue, stabilized purely by quantum fluctuations.

## How It Works

The core challenge in strongly correlated electron physics is this: writing down the quantum state of N electrons requires tracking every possible combination of their positions simultaneously. For even a few dozen electrons in continuous space, this exponentially large **wavefunction** (the mathematical object fully describing a quantum system) is impossible to store or compute directly.

The MIT team's solution is **neural network variational Monte Carlo (NN-VMC)**. The method works in three steps:

1. **Represent** the wavefunction as a deep neural network. The network takes electron positions as input and outputs a value encoding the quantum weight of that configuration.
2. **Sample** random electron configurations according to the probability distribution encoded by the network.
3. **Optimize** the network's millions of adjustable weights by nudging them downhill until the total energy is minimized.

Their architecture is attention-based, similar in spirit to transformer models. Each "token" is an electron, and the attention mechanism captures how each electron's quantum state depends on all the others. The network also enforces **antisymmetry**: swapping any two electrons flips the mathematical sign of the wavefunction. This is the quantum mechanical fingerprint of electrons as **fermions**, identical particles fundamentally forbidden from occupying the same state.

The team studied spin-polarized electrons confined in a GaAs-like quantum well, scanning across two key parameters: electron density (*r_s*, the ratio of interparticle spacing to effective Bohr radius) and well thickness *d*. By letting the neural network find the lowest-energy state at each point, they built a complete phase diagram with no preconceptions required.

![Figure 1](figure:1)

## Phases Emerge from First Principles

At narrow well thicknesses, the physics is familiar. At low density (*r_s* around 30), electrons crystallize into a **Wigner crystal**, a perfectly triangular lattice locked in place by electrical repulsion. At higher density, they form a **Fermi liquid**, an ordinary metal-like conducting state.

Widen the well, and something new happens. Higher energy levels become accessible, and electrons spread out along the depth of the well, spontaneously splitting into two layers even though the well itself has no physical divider. The **Fermi surface** (the boundary in momentum space separating occupied from empty electron states) splits from one circular surface into two distinct ones.

![Figure 2](figure:2)

In the bilayer regime at low density, crystalline phases appear. But the bilayer geometry introduces a frustration problem: two triangular lattices stacked on top of each other can't simultaneously minimize all their interlayer repulsions. The triangular crystal isn't always the winner.

![Figure 3](figure:3)

What wins instead, in a specific range of densities and well widths, is the **quantum quasicrystal**. The simulations reveal a phase with 12-fold rotational symmetry, a pattern that tiles the plane with two different shapes, never repeating, yet never disordered. This dodecagonal order appears in the **structure factor** (a mathematical fingerprint of how electron density is organized in space) with sharp peaks no ordinary crystal can produce.

![Figure 4](figure:4)

The quasicrystal isn't a classical effect. By computing the **zero-point quantum fluctuations**, the irreducible quantum jitter electrons retain even at absolute zero, the team showed these fluctuations actually *stabilize* the quasicrystal relative to competing crystal phases. Remove quantum mechanics, and the quasicrystal disappears.

![Figure 5](figure:5)

![Figure 6](figure:6)

## Why It Matters

Electronic quasicrystals have been theorized and hinted at in moiré systems (twisted stacks of atomically thin materials like graphene on boron nitride), but this work delivers one of the clearest theoretical predictions of a quasicrystalline electron phase stabilized by quantum mechanics alone. That distinction matters. Classical quasicrystals, like the aluminum-manganese alloys behind Dan Shechtman's 2011 Nobel Prize, are metastable: not the true lowest-energy state, but patterns frozen in during cooling. A true quantum quasicrystal is a genuine ground state, the lowest-energy configuration at zero temperature.

The predictions are directly testable. GaAs quantum wells of the relevant thickness and electron density are already fabricated in laboratories. The quasicrystal's 12-fold diffraction pattern and anomalous transport properties should be visible in existing experimental setups. The same physics may appear in **van der Waals heterostructures** (atomically thin layers of different materials stacked like sheets of paper), where layer thickness and density can be tuned with extraordinary precision.

Beyond the specific prediction, the approach itself is the point. The neural network didn't start with a quasicrystal as an assumed answer. It found one. AI-powered first-principles simulations have reached the stage where they can discover new physics, not just compute known answers faster.

> **Bottom Line:** MIT researchers used a neural network to simulate strongly interacting electrons in semiconductor quantum wells from first principles and discovered a new quantum phase of matter: the electronic quasicrystal, stabilized entirely by quantum fluctuations. The prediction is testable in real materials today.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work fuses transformer-style deep learning with quantum many-body physics to discover a new phase of matter, showing AI can function as a genuine discovery tool in condensed matter physics.
- **Impact on Artificial Intelligence:** The attention-based NN-VMC method scales to continuous three-dimensional quantum systems with strong correlations, a regime where conventional methods fail, pushing the frontier of neural quantum state methods.
- **Impact on Fundamental Interactions:** The discovery reveals that Coulomb interactions combined with quantum zero-point fluctuations can produce electronic order with no classical analogue, adding a new entry to the catalog of quantum phases of matter.
- **Outlook and References:** This work motivates direct experimental searches for quasicrystalline charge order in wide GaAs quantum wells and van der Waals heterostructures; see [arXiv:2512.10909](https://arxiv.org/abs/2512.10909) for full details and supplementary methods.
