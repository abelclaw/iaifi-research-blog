---
abstract: Ab-initio simulations of multiple heavy quarks propagating in a Quark-Gluon
  Plasma are computationally difficult to perform due to the large dimension of the
  space of density matrices. This work develops machine learning algorithms to overcome
  this difficulty by approximating exact quantum states with neural network parametrisations,
  specifically Neural Density Operators. As a proof of principle demonstration in
  a QCD-like theory, the approach is applied to solve the Lindblad master equation
  in the 1+1d lattice Schwinger Model as an open quantum system. Neural Density Operators
  enable the study of in-medium dynamics on large lattice volumes, where multiple-string
  interactions and their effects on string-breaking and recombination phenomena can
  be studied. Thermal properties of the system at equilibrium can also be probed with
  these methods by variationally constructing the steady state of the Lindblad master
  equation. Scaling of this approach with system size is studied, and numerical demonstrations
  on up to 32 spatial lattice sites and with up to 3 interacting strings are performed.
arxivId: '2402.06607'
arxivUrl: https://arxiv.org/abs/2402.06607
authors:
- Joshua Lin
- Di Luo
- Xiaojun Yao
- Phiala E. Shanahan
concepts:
- neural density operators
- lindblad dynamics
- open quantum systems
- lattice gauge theory
- quantum simulation
- quantum states
- monte carlo methods
- quantum field theory
- hamiltonian systems
- symmetry breaking
- phase transitions
- tensor networks
figures:
- /iaifi-research-blog/figures/2402_06607/figure_1.png
pdfUrl: https://arxiv.org/pdf/2402.06607v2
published: '2024-02-09T18:36:17+00:00'
theme: Theoretical Physics
title: Real-time Dynamics of the Schwinger Model as an Open Quantum System with Neural
  Density Operators
wordCount: 1337
---

## The Big Picture

Imagine tracking a handful of billiard balls ricocheting inside a room. Hard enough. Now imagine the balls are quantum particles, and the room grows exponentially more complex every time you add another one. That's roughly the challenge facing physicists who want to simulate what happens when quarks (the subatomic building blocks of protons and neutrons) plow through the scorching plasma of free quarks and gluons that briefly existed microseconds after the Big Bang, and that colliders like the LHC recreate today.

This extreme state of matter, called the **Quark-Gluon Plasma (QGP)**, leaves a telltale fingerprint: it suppresses the production of bound quark pairs called **quarkonia**, heavier cousins of the hydrogen atom built from quarks instead of a proton and electron. Quantifying this suppression from first principles means simulating quantum systems that constantly exchange energy with a scorching thermal environment, what physicists call **open quantum systems**.

The mathematical object describing such a system is a **density matrix**: a table of numbers encoding all possible quantum states and their probabilities. Its size blows up exponentially with the number of particles. For more than a couple of quarks, exact simulation becomes completely intractable on classical computers.

Researchers at MIT and the University of Washington have shown that neural networks can cut through this exponential wall. Their framework, **Neural Density Operators (NDOs)**, simulates the real-time dynamics of a QCD-like theory on lattices with up to 32 sites and three interacting quark strings.

> **Key Insight:** By parametrizing quantum density matrices with neural networks, the researchers sidestep the exponential cost of exact simulation, making ab-initio calculations of quark dynamics in the Quark-Gluon Plasma a realistic target.

## How It Works

The team's testbed is the **Schwinger Model**, a one-dimensional quantum field theory. It shares two key features with full **QCD (Quantum Chromodynamics)**, the theory of the strong nuclear force: **confinement** (quarks can't exist as isolated free particles) and **chiral symmetry breaking** (a quantum effect that shapes particle masses and distinguishes matter from its mirror image). It's simpler than QCD but captures the essential physics, making it an ideal proving ground.

The dynamics are governed by the **Lindblad master equation**, a differential equation for how a quantum system's density matrix evolves when coupled to a thermal reservoir. Think of it as Schrödinger's equation with an extra noise term modeling the environment constantly nudging the system. Solving it exactly requires storing and evolving the full density matrix, which doubles in size with every added lattice site.

![Figure 1](/iaifi-research-blog/figures/2402_06607/figure_1.png)

Instead of storing the exact density matrix, the team approximates it with a compact neural network. A **Neural Density Operator** represents the density matrix using an architecture inspired by **restricted Boltzmann machines** (layered networks of interconnected nodes, similar to those used in image recognition). The network's parameters are far fewer than the matrix entries themselves, so instead of storing an exponentially large object, you store the network weights and sample from it using **Monte Carlo methods** (repeated random sampling that builds statistical estimates of otherwise intractable quantities).

To evolve the system forward in time, the researchers use **time-dependent Variational Monte Carlo (tVMC)**:

1. Express the Lindblad equation as an optimization problem over the NDO parameters
2. At each time step, compute how the parameters must change to best approximate the true evolution
3. Update the parameters and repeat, effectively steering the neural network to track the quantum state as it evolves

One practical challenge: you need a good starting point. The team developed bootstrapping algorithms that initialize NDOs trained on small lattices and transfer them to larger ones, cutting the cost of scaling to bigger systems.

## Why It Matters

In the Schwinger Model, quarks are connected by **flux tubes**, strings of electric field that confine them together. When these strings interact, they can break (the string snaps, producing new particle-antiparticle pairs) or recombine (two strings swap partners, like a square dance among quarks).


On lattices up to 32 spatial sites with up to three interacting strings, the NDO simulations tracked these dynamics in real time. Results agree with exact calculations on small lattices, validating the approach, while pushing into regimes where exact methods fail entirely. The team also studied thermal equilibrium properties by variationally finding the Lindblad steady state, showing the framework can probe thermodynamics as well as dynamics.


The scaling advantage is stark. The exact density matrix grows as $4^L$ for $L$ lattice sites; the neural network parametrization grows only polynomially, making 32-site simulations feasible where exact methods would need astronomical resources.

The suppression of quarkonia in heavy-ion collisions at RHIC (the **Relativistic Heavy Ion Collider**) and the LHC is one of the clearest experimental signatures of QGP formation, but a quantitative first-principles account has remained out of reach. This is the first time neural network methods have handled the multi-string, open-system dynamics needed for such calculations in a QCD-like theory. The path from the Schwinger Model to full 3+1 dimensional QCD is long, but the authors lay out how their methods could, in principle, be extended.

The work also connects machine learning with quantum many-body physics in a concrete way. Neural quantum states have already reshaped the simulation of closed quantum systems: ground states, spin models, molecular systems. Extending them to open Lindblad systems is harder, because density matrices are more complex objects than wave functions. The results here show that the extension works and is practically useful, bringing a new class of physical problems within reach of neural-network-based simulation.

Open questions remain. How well do NDOs perform as the number of strings grows beyond three? Can the approach handle 3+1 dimensional geometries? Can it be combined with quantum hardware to push even further?

> **Bottom Line:** Neural Density Operators crack open a computational bottleneck that has blocked first-principles simulations of quark dynamics in hot nuclear matter. On a QCD-like testbed, neural networks can now track the full real-time, dissipative quantum evolution of up to three interacting quark strings on lattices of 32 sites.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses machine learning architecture design with quantum field theory simulation, developing neural-network parametrizations of density matrices that solve a core obstacle in nuclear physics without exponential blowup.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The Neural Density Operator framework extends variational Monte Carlo methods to open quantum systems, showing that neural networks can efficiently represent and time-evolve mixed quantum states, a nontrivial generalization beyond neural quantum states for closed systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By simulating multi-string Lindbladian dynamics and string-breaking/recombination in the Schwinger Model, this work brings ab-initio calculations of heavy quarkonia suppression in the Quark-Gluon Plasma meaningfully closer to feasibility in realistic QCD settings.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions toward 3+1 dimensional QCD simulations and larger quark multiplicities are the key next steps; the full paper is available at [arXiv:2402.06607](https://arxiv.org/abs/2402.06607).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Real-time Dynamics of the Schwinger Model as an Open Quantum System with Neural Density Operators</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2402.06607](https://arxiv.org/abs/2402.06607)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">Joshua Lin, Di Luo, Xiaojun Yao, Phiala E. Shanahan</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Ab-initio simulations of multiple heavy quarks propagating in a Quark-Gluon Plasma are computationally difficult to perform due to the large dimension of the space of density matrices. This work develops machine learning algorithms to overcome this difficulty by approximating exact quantum states with neural network parametrisations, specifically Neural Density Operators. As a proof of principle demonstration in a QCD-like theory, the approach is applied to solve the Lindblad master equation in the 1+1d lattice Schwinger Model as an open quantum system. Neural Density Operators enable the study of in-medium dynamics on large lattice volumes, where multiple-string interactions and their effects on string-breaking and recombination phenomena can be studied. Thermal properties of the system at equilibrium can also be probed with these methods by variationally constructing the steady state of the Lindblad master equation. Scaling of this approach with system size is studied, and numerical demonstrations on up to 32 spatial lattice sites and with up to 3 interacting strings are performed.</span></div></div>
</div>
