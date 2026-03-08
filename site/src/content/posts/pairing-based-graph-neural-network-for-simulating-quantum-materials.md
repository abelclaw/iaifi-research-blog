---
abstract: We develop a pairing-based graph neural network for simulating quantum many-body
  systems. Our architecture augments a BCS-type geminal wavefunction with a generalized
  pair amplitude parameterized by a graph neural network. Variational Monte Carlo
  with our neural network simultaneously provides an accurate, flexible, and scalable
  method for simulating many-electron systems. We apply this method to two-dimensional
  semiconductor electron-hole bilayers and obtain accurate results on a variety of
  interaction-induced phases, including the exciton Bose-Einstein condensate, electron-hole
  superconductor, and bilayer Wigner crystal. Our study demonstrates the potential
  of physically-motivated neural network wavefunctions for quantum materials simulations.
arxivId: '2311.02143'
arxivUrl: https://arxiv.org/abs/2311.02143
authors:
- Di Luo
- David D. Dai
- Liang Fu
concepts:
- graph neural networks
- quantum simulation
- monte carlo methods
- geminal wavefunction
- quantum states
- physics-informed neural networks
- neural network wavefunction
- phase transitions
- electron-hole bilayer
- symmetry preservation
- transfer learning
- scalability
figures:
- /iaifi-research-blog/figures/2311_02143/figure_1.png
- /iaifi-research-blog/figures/2311_02143/figure_1.png
- /iaifi-research-blog/figures/2311_02143/figure_2.png
- /iaifi-research-blog/figures/2311_02143/figure_2.png
- /iaifi-research-blog/figures/2311_02143/figure_3.png
- /iaifi-research-blog/figures/2311_02143/figure_3.png
pdfUrl: https://arxiv.org/pdf/2311.02143v2
published: '2023-11-03T17:12:29+00:00'
theme: Astrophysics
title: Pairing-based graph neural network for simulating quantum materials
wordCount: 1087
---

## The Big Picture

Imagine trying to predict the behavior of a crowd of thousands of people, where every person's movement depends on the simultaneous positions of everyone else. Now make those people quantum particles — each existing in a blur of possible states at once, mysteriously linked to all the others. That's roughly the challenge facing physicists who want to simulate quantum materials from scratch.

The math is exact. Schrödinger's equation describes how quantum particles behave, and physicists have known it for nearly a century. But simulating many electrons together is a different problem entirely: the number of variables grows exponentially with particle count, making exact computation impossible for anything larger than a handful of atoms.

For decades, physicists have attacked this exponential wall with clever approximations — Hartree-Fock theory, density functional theory, coupled cluster methods — each capturing some physics while sacrificing others. Systems where electrons interact too strongly to be treated independently have been especially stubborn: standard techniques either fail or give dangerously wrong answers.

Now, a team from MIT and Harvard has developed a new approach: a **pairing-based graph neural network wavefunction** that combines physics intuition with machine learning flexibility to simulate quantum materials with unprecedented accuracy and scalability. Their target is the **electron-hole bilayer** — a two-dimensional semiconductor sandwich where electrons and their positively charged counterparts (holes) interact across an atomically thin gap, producing exotic quantum states that conventional methods struggle to capture simultaneously.

> **Key Insight:** By encoding the physics of electron pairing directly into a graph neural network architecture, this approach achieves accurate, unbiased simulation of multiple competing quantum phases — exciton condensates, superconductors, and Wigner crystals — within a single unified framework.

## How It Works

The core innovation is **GemiNet** — a portmanteau of "geminal" (a quantum chemistry term for paired-particle wavefunctions) and "network." It builds on a classic piece of physics: the **BCS wavefunction**, originally developed to describe superconductors, where electrons pair up into Cooper pairs and condense into a superfluid.

In the BCS picture, the wavefunction is a determinant of pair amplitudes. This automatically enforces a fundamental quantum rule: electrons are **fermions**, meaning no two can ever occupy exactly the same state simultaneously. But the traditional BCS formula is a **mean-field approximation** — it averages out detailed particle interactions rather than tracking them — and it's tailored to describe only certain phases of matter.

GemiNet's key move is to replace the simple, hand-crafted pair amplitude with a **generalized pair amplitude parameterized by a graph neural network**. Here's how:

1. **Start with BCS structure.** The wavefunction is a determinant of electron-hole pair amplitudes — mathematically enforcing pairing physics and fermionic statistics from the outset.
2. **Generalize the pair amplitude.** Instead of a fixed functional form, the pair amplitude becomes a learnable function of all particle positions, computed by a graph neural network.
3. **Build the graph.** Electrons and holes become nodes; their interactions become edges. The GNN passes messages between nodes, letting each particle's effective wavefunction depend on its neighbors.
4. **Optimize with Variational Monte Carlo.** Network parameters are trained by minimizing the system's energy, sampling many random configurations of particle positions to estimate the answer.

![Figure 1](/iaifi-research-blog/figures/2311_02143/figure_1.png)

The elegance is that the physics is *built in*, not learned from scratch. The BCS skeleton ensures the network starts with sensible pairing structure; the GNN layers then learn corrections that capture strong correlations, spatial pattern formation, and other effects that the mean-field treatment misses.

![Figure 2](/iaifi-research-blog/figures/2311_02143/figure_1.png)

A crucial practical feature is **transfer learning across system sizes**. Because the GNN operates on local particle interactions, a network trained on a small system can initialize training on a larger one — a scalability advantage that purely data-driven approaches lack. The authors verify this works well, enabling simulation of bilayers with up to 30 electron-hole pairs.

## Why It Matters

The electron-hole bilayer is a remarkable laboratory for quantum phases. Depending on particle density and interlayer separation, the system can be an **exciton Bose-Einstein condensate** (tightly bound electron-hole pairs condensed into a superfluid), an **electron-hole superconductor** (loosely paired carriers in a BCS state), or a **bilayer Wigner crystal** (electrons and holes separately crystallizing into locked lattices). Probing all three phases with a single unbiased method has been a longstanding challenge.

![Figure 3](/iaifi-research-blog/figures/2311_02143/figure_2.png)

GemiNet delivers quantitatively accurate energies across the entire phase diagram, outperforming Hartree-Fock-Bogoliubov calculations especially in the intermediate-density regime where correlations matter most. It correctly captures the **BEC-BCS crossover** — the smooth evolution from tightly bound excitons to loosely paired superconducting carriers — as well as the crystalline Wigner phase at large separations and low densities. Because the network doesn't presuppose a particular phase, it detects which phase is energetically favored without methodological bias.

![Figure 4](/iaifi-research-blog/figures/2311_02143/figure_2.png)

The broader implications extend well beyond this system. Many of the most scientifically interesting materials — high-temperature superconductors, frustrated magnets, topological insulators — are strongly correlated systems where conventional methods fail. Physically motivated neural network wavefunctions offer a path to simulate these materials from first principles, without the biases baked into hand-crafted starting-point formulas.

![Figure 5](/iaifi-research-blog/figures/2311_02143/figure_3.png)

The success of GemiNet on the electron-hole bilayer suggests this strategy can extend to twisted bilayer graphene, moiré materials, and systems relevant to quantum computing hardware. Open questions remain: scalability to larger systems, handling of spin-orbit coupling and magnetic fields, and incorporating longer-range correlations into the GNN architecture — each a productive frontier.

![Figure 6](/iaifi-research-blog/figures/2311_02143/figure_3.png)

> **Bottom Line:** GemiNet demonstrates that fusing physics-motivated wavefunction structure with graph neural network flexibility enables accurate, scalable, and unbiased simulation of competing quantum phases — opening a powerful new route to understanding strongly correlated quantum materials from first principles.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work exemplifies the IAIFI mission by translating graph neural network architectures from machine learning into a physically motivated quantum wavefunction that outperforms traditional condensed matter methods on a challenging benchmark.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">GemiNet introduces a novel strategy for physics-informed neural network design, showing that encoding known physical structure — BCS pairing — into the architectural inductive bias dramatically improves sample efficiency, accuracy, and scalability over generic approaches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The method achieves accurate simulation of the full electron-hole bilayer phase diagram — spanning exciton BEC, BCS superconductor, and Wigner crystal phases — in a regime where mean-field theory fails, providing a new quantitative tool for understanding interaction-driven quantum phases in two-dimensional materials.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend GemiNet to twisted moiré systems, spin-orbit coupled materials, and real-time dynamics; the full paper is available at arXiv:2311.02610.</span></div></div>
</div>
