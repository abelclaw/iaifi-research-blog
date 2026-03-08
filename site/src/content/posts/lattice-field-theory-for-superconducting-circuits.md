---
abstract: Large superconducting quantum circuits have a number of important applications
  in quantum computing. Accurately predicting the performance of these devices from
  first principles is challenging, as it requires solving the many-body Schrödinger
  equation. This work introduces a new, general ab-initio method for analyzing large
  quantum circuits based on lattice field theory, a tool commonly applied in nuclear
  and particle physics. This method is competitive with state-of-the-art techniques
  such as tensor networks, but avoids introducing systematic errors due to truncation
  of the infinite-dimensional Hilbert space associated with superconducting phases.
  The approach is applied to fluxonium, a specific many-component superconducting
  qubit with favorable qualities for quantum computation. A systematic study of the
  influence of impedance on fluxonium is conducted that parallels previous experimental
  studies, and ground capacitance effects are explored. The qubit frequency and charge
  noise dephasing rate are extracted from statistical analyses of charge noise, where
  thousands of instantiations of charge disorder in the Josephson junction array of
  a fixed fluxonium qubit are explicitly averaged over at the microscopic level. This
  is difficult to achieve with any other existing method.
arxivId: '2512.05851'
arxivUrl: https://arxiv.org/abs/2512.05851
authors:
- Joshua Lin
- Max Hays
- Stephen Sorokanich
- Julian Bender
- Phiala E. Shanahan
- Neill C. Warrington
concepts:
- lattice gauge theory
- quantum field theory
- monte carlo methods
- fluxonium qubit
- path integral formulation
- quantum computing
- charge noise dephasing
- tensor networks
- quantum simulation
- phase transitions
- effective field theory
- bayesian inference
figures:
- /iaifi-research-blog/figures/2512_05851/figure_2.png
- /iaifi-research-blog/figures/2512_05851/figure_2.png
pdfUrl: https://arxiv.org/pdf/2512.05851v1
published: '2025-12-05T16:26:18+00:00'
theme: Theoretical Physics
title: Lattice field theory for superconducting circuits
wordCount: 1138
---

## The Big Picture

Imagine predicting the behavior of a symphony orchestra by modeling every musician, every instrument, every vibrating string and resonating chamber, all at once, from first principles. That's roughly the challenge facing engineers who want to understand large superconducting quantum circuits. These devices, the backbone of quantum computers built by Google, IBM, and others, can contain hundreds of interconnected quantum components. Simulating them all together, precisely, is a combinatorial nightmare.

The standard workaround has been approximation. Fluxonium qubits (a promising design known for holding quantum states for unusually long periods before errors disrupt them) are built from hundreds of **Josephson junctions**, the tiny quantum switches at the heart of these circuits. Physicists typically collapse all those junctions into a single simplified element called a **superinductance**. It works in many cases. But it misses physics that matters, especially when the circuit operates at high electrical resistance, where strange collective quantum effects called **coherent quantum phase slips** begin to dominate. These are coordinated quantum tunneling events that can propagate through the circuit and cause trouble.

Researchers at MIT have now borrowed a powerful computational framework from nuclear and particle physics, **lattice field theory**, and retooled it to simulate superconducting circuits from scratch, without approximation. Their approach handles what no other method handles cleanly: thousands of complete qubit simulations, all at the microscopic level, without discarding any quantum complexity.

> **Key Insight:** By treating a superconducting circuit as a lattice field theory and using Monte Carlo sampling over the full quantum phase space, this method computes qubit properties without the systematic errors that plague existing approaches, giving direct access to many-body quantum effects in real hardware.

## How It Works

The core idea sounds almost playful in its audacity: take the mathematical machinery physicists use to study quarks and gluons inside protons, and apply it to a circuit etched onto a silicon chip. The connection is deeper than analogy.

![Figure 1](/iaifi-research-blog/figures/2512_05851/figure_2.png)

In **circuit QED**, the detailed microscopic theory of superconducting devices, each superconducting island carries a **phase variable**: a quantum degree of freedom that lives on a circle (technically, a U(1) variable). An array of 100 Josephson junctions means 100 such variables, all quantum-mechanically entangled. The governing equation is, in general, unsolvable by brute force.

Lattice field theory offers a route around this. The method proceeds in four steps:

1. **Formulate dynamics as a path integral.** Instead of solving for quantum wavefunctions directly, quantum amplitudes are expressed as sums over all possible histories of the system, a Feynman path integral reformulated in imaginary (Euclidean) time. Standard in particle physics; new in this context.
2. **Discretize the time direction.** Continuous Euclidean time is replaced by a finite lattice of time slices. The circuit's spatial structure (its network of capacitors, inductors, and junctions) is already discrete, making this a natural fit.
3. **Sample with Monte Carlo.** The path integral is evaluated by randomly sampling configurations of the phase variables, directly over the full circular U(1) space without truncating it. This sidesteps the systematic errors other methods incur.
4. **Extract the spectrum from correlators.** Qubit energies and matrix elements are recovered from how quantum correlations decay across Euclidean time slices. This is exactly how particle physicists extract hadron masses from lattice QCD.

![Figure 2](/iaifi-research-blog/figures/2512_05851/figure_2.png)

The key advantage over **tensor network (TN)** methods, currently the state of the art for many-body circuit simulation, lies in step three. Tensor networks must choose a finite basis to represent each junction's quantum state space, which is technically infinite-dimensional. That introduces truncation errors requiring careful justification. The lattice method keeps variables on their natural domain and avoids the problem entirely.

There's also a practical bonus. After computing one device, a technique called **reweighting** lets researchers simulate nearby devices in fabrication space at almost no additional cost. For hardware design, where you want to explore many parameter choices, that matters a lot.

## Why It Matters

The team applies their method to fluxonium, a qubit built from a single small Josephson junction shunted by an array of 100 or more larger junctions. The array functions as a superinductor, an element with unusually high electrical inductance, giving fluxonium its exceptional resistance to environmental noise. But the array also hosts collective quantum excitations called **array modes**, and at high impedance, coherent phase slips can propagate through it and disrupt the qubit's quantum coherence.


The team simulates thousands of individual fluxonium qubits, each with a different random realization of charge disorder across the Josephson junction array. This kind of exhaustive microscopic statistical study, explicitly averaging over disorder at the circuit level, is essentially impossible with any other existing method. From it, they extract the **charge noise dephasing rate** as a function of impedance, finding deviations from existing analytic formulas. At very high impedances, they observe signatures of multiple simultaneous phase slip events, effects that lie beyond the reach of current analytic theories.


There's also a surprise involving ground capacitance. Every circuit element has some small capacitance to the chip's ground plane; these stray capacitances are usually ignored. The lattice calculations show that ground capacitances actually *reduce* charge noise. That's counterintuitive, and it has direct implications for hardware design. It also goes beyond what tensor network methods have so far achieved for fluxonium.

The method generalizes to any superconducting circuit with capacitors, inductors, and Josephson junctions. Next-generation qubit designs like the 0-π qubit, blochnium, bifluxon, and harmonium all rely on long Josephson junction arrays where many-body effects matter. As quantum processors scale toward **fault-tolerant quantum computing**, where errors can be detected and corrected reliably, having a method that predicts device behavior without approximation is not a luxury. It is a necessity.


> **Bottom Line:** Borrowing tools from nuclear physics for quantum hardware design, this work delivers the first lattice field theory approach to superconducting circuits, simulating thousands of realistic fluxonium qubits at the microscopic level and revealing many-body physics invisible to every other existing technique.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly transplants lattice quantum field theory, a computational framework from nuclear and particle physics, into quantum hardware engineering, creating a rigorous bridge between two previously separate fields.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The method enables precise, first-principles simulation of the superconducting qubits at the core of near-term quantum computers, potentially accelerating the design of more coherent and reliable processors for quantum AI applications.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By treating a superconducting circuit as an instantiation of a lattice field theory with U(1) phase variables, the work reveals collective quantum phenomena (coherent phase slips, array mode coupling) that emerge from the full many-body description and are missed by effective field theory approximations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend the method to qubit-qubit interactions in full quantum processors and to next-generation qubit architectures; the paper is available at [arXiv:2512.05851](https://arxiv.org/abs/2512.05851).</span></div></div>
</div>
