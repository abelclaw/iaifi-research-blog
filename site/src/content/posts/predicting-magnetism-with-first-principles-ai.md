---
abstract: Computational discovery of magnetic materials remains challenging because
  magnetism arises from the competition between kinetic energy and Coulomb interaction
  that is often beyond the reach of standard electronic-structure methods. Here we
  tackle this challenge by directly solving the many-electron Schrödinger equation
  with neural-network variational Monte Carlo, which provides a highly expressive
  variational wavefunction for strongly correlated systems. Applying this technique
  to transition metal dichalcogenide moiré semicondutors, we predict itinerant ferromagnetism
  in WSe$_2$/WS$_2$ and an antiferromagnetic insulator in twisted $Γ$-valley homobilayer,
  using the same neural network without any physics input beyond the microscopic Hamiltonian.
  Crucially, both types of magnetic states are obtained from a single calculation
  within the $S_z=0$ sector, removing the need to compute and compare multiple $S_z$
  sectors. This significantly reduces computational cost and paves the way for faster
  and more reliable magnetic material design.
arxivId: '2602.09093'
arxivUrl: https://arxiv.org/abs/2602.09093
authors:
- Max Geier
- Liang Fu
concepts:
- neural wavefunction
- quantum states
- equivariant neural networks
- itinerant magnetism
- symmetry preservation
- transformers
- phase transitions
- hamiltonian systems
- moiré heterostructures
- materials discovery
- quantum simulation
figures:
- /iaifi-research-blog/figures/2602_09093/figure_1.png
- /iaifi-research-blog/figures/2602_09093/figure_2.png
- /iaifi-research-blog/figures/2602_09093/figure_3.png
pdfUrl: https://arxiv.org/pdf/2602.09093v1
published: '2026-02-09T19:00:01+00:00'
theme: Theoretical Physics
title: Predicting magnetism with first-principles AI
wordCount: 1062
---

## The Big Picture

Imagine trying to find the lowest point in a vast mountain range while blindfolded. You can only feel the ground immediately beneath your feet, and the landscape has millions of peaks and valleys. That's roughly the challenge facing physicists who want to predict whether a new material will be magnetic.

Magnetism seems deceptively simple — stick a magnet to your refrigerator and it just works. But at the quantum level, magnetism emerges from a delicate tug-of-war between two competing forces: the kinetic energy that wants electrons to roam freely, and the electrical repulsion that makes electrons push each other apart.

These forces operate at vastly different energy scales, and the magnetic state a material settles into is often a whisper atop a roar — nearly impossible to resolve with standard computational methods. Techniques like **density functional theory** — a widely used approach that handles electron interactions only approximately — routinely fail to predict whether a material is actually magnetic.

Now, MIT physicists Max Geier and Liang Fu have turned to neural networks to cut through this complexity, directly solving the quantum equations that govern electrons in real materials — and predicting two completely different kinds of magnetism, from scratch, without any physics assumptions baked in.

> **Key Insight:** A single neural network, trained by pure energy minimization with no prior physics knowledge, can spontaneously discover whether a material is magnetic — and what kind of magnet it will be.

## How It Works

The approach centers on **neural-network variational Monte Carlo (NN-VMC)**, a technique that encodes the quantum wavefunction — the mathematical object describing all possible states of every electron simultaneously — inside a neural network. Instead of approximating electron-electron interactions, NN-VMC confronts them head-on.

![Figure 1](/iaifi-research-blog/figures/2602_09093/figure_1.png)

Here's the basic workflow:

1. **Define the Hamiltonian.** Write down the microscopic equations governing the electrons — their kinetic energy, mutual repulsion, and the periodic potential of the crystal lattice. (The Hamiltonian is the formal expression for the system's total energy.) No assumptions about spin ordering, no physics-informed initialization.
2. **Parameterize the wavefunction.** Represent the many-electron wavefunction as a sum of determinants — a structure that correctly enforces the quantum rule that no two electrons can occupy the same state — whose orbitals are computed by a **transformer neural network**, the same architecture powering modern language models, here repurposed as a universal approximator of quantum states.
3. **Minimize the energy.** Train the network to find the lowest possible energy. It learns the ground state organically, guided only by the equations of quantum mechanics.
4. **Read off the magnetism.** Compute the total spin ⟨S²⟩ and **staggered magnetization** — a measure of whether neighboring atoms have parallel or opposing spins — from the trained wavefunction. If ⟨S²⟩ > 0, you have a magnet; the spatial pattern reveals whether it's ferromagnetic or antiferromagnetic.

The critical technical trick involves the **Sz = 0 sector** — a constraint that keeps up-spin and down-spin electrons equal, so the system appears overall non-magnetic going in. Conventional methods compute the ground state in each spin sector separately and compare energies, which is expensive and error-prone.

Geier and Fu recognized that all possible magnetization values can in principle be accessed from a single calculation in this sector. Remarkably, the network can find a magnetically ordered state — spins spontaneously aligning in the x-y plane — starting from this apparently non-magnetic configuration, purely by following the energy gradient downhill.

The materials studied are **moiré semiconductors**: atomically thin crystals stacked with a slight twist or lattice mismatch, creating a long-wavelength interference pattern that fundamentally alters how electrons behave. These systems have become a hotbed for exotic quantum phases because their properties can be tuned electrically. The specific systems were WSe₂/WS₂ heterobilayers and twisted Γ-valley homobilayers of WS₂, MoS₂, and MoSe₂.

![Figure 2](/iaifi-research-blog/figures/2602_09093/figure_2.png)

For WSe₂/WS₂, NN-VMC predicts **itinerant ferromagnetism** — a metallic state where electrons remain delocalized but collectively align their spins, the same phenomenon behind iron's magnetism. For the homobilayer system, it finds an **antiferromagnetic insulator**, where electrons localize and neighboring sites develop opposing spin orientations. Two completely different magnetic phases, from the same framework, from the same fundamental equations.

## Why It Matters

The stakes extend well beyond academic curiosity. Powerful permanent magnets — the kind driving electric motors and wind turbines — currently depend on rare-earth elements like neodymium and samarium. These materials are geopolitically sensitive and environmentally costly to mine. Finding rare-earth-free alternatives requires understanding what makes a material magnetic before synthesizing it, which demands exactly the kind of reliable predictive theory that has so far eluded computational physics.

![Figure 3](/iaifi-research-blog/figures/2602_09093/figure_3.png)

More broadly, this work demonstrates that neural networks trained purely on first-principles physics can discover qualitatively different ground states without human guidance. The same network that finds ferromagnetism in one material finds antiferromagnetism in another — not because it was told to, but because the energy landscape demanded it. As moiré systems continue to reveal new quantum phases — superconductivity, Mott insulators, Wigner crystals — tools that can navigate that landscape reliably will become indispensable. Working within the Sz = 0 sector alone makes this method significantly more practical for screening candidate materials at scale.

> **Bottom Line:** By combining transformer neural networks with variational quantum mechanics, Geier and Fu have built a first-principles compass for magnetic materials — one that finds the right answer without being told what to look for, and does it more efficiently than any prior method.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses transformer architectures from machine learning with the variational Monte Carlo formalism from quantum many-body physics, demonstrating that AI tools developed for language can solve fundamental equations of quantum mechanics in real materials.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">A single neural network autonomously identifies qualitatively distinct quantum phases — ferromagnetic and antiferromagnetic — purely through energy minimization, establishing neural-network wavefunctions as a general-purpose solver for strongly correlated electron systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By directly solving the many-electron Schrödinger equation in moiré semiconductors without approximation, the method bypasses longstanding failures of density functional theory and Hartree-Fock in predicting magnetic order driven by subtle exchange-correlation effects.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work can extend this framework to screen rare-earth-free permanent magnet candidates and probe other correlated phases in moiré heterostructures; the full paper is available on arXiv (submitted February 2026) from the Liang Fu group at MIT.</span></div></div>
</div>
