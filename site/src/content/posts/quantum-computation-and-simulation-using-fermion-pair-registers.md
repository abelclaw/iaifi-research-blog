---
abstract: We propose and analyze an approach to realize quantum computation and simulation
  using fermionic particles under quantum gas microscopes. Our work is inspired by
  a recent experimental demonstration of large-scale quantum registers, where tightly
  localized fermion pairs are used to encode qubits exhibiting long coherence time
  and robustness against laser intensity noise. We describe how to engineer the SWAP
  gate and high-fidelity controlled-phase gates by adjusting the fermion hopping as
  well as Feshbach interaction strengths. Combined with previously demonstrated single-qubit
  rotations, these gates establish the computational universality of the system. Furthermore,
  we show that 2D quantum Ising Hamiltonians with tunable transverse and longitudinal
  fields can be efficient simulated by modulating Feshbach interaction strengths.
  We present a sample-efficient protocol to characterize engineered gates and Hamiltonian
  dynamics based on an improved classical shadow process tomography that requires
  minimal experimental controls. Our work opens up new opportunities to harness existing
  ultracold quantum gases for quantum information sciences.
arxivId: '2306.03905'
arxivUrl: https://arxiv.org/abs/2306.03905
authors:
- Xiangkai Sun
- Di Luo
- Soonwon Choi
concepts:
- quantum computing
- quantum simulation
- fermion-pair qubits
- quantum states
- feshbach resonance
- entanglement
- hamiltonian systems
- shadow process tomography
- symmetry preservation
- experimental design
- phase transitions
figures:
- /iaifi-research-blog/figures/2306_03905/figure_1.png
- /iaifi-research-blog/figures/2306_03905/figure_2.png
- /iaifi-research-blog/figures/2306_03905/figure_3.png
pdfUrl: https://arxiv.org/pdf/2306.03905v1
published: '2023-06-06T17:59:08+00:00'
theme: Theoretical Physics
title: Quantum Computation and Simulation using Fermion-Pair Registers
wordCount: 1153
---

## The Big Picture

Imagine building a computer where the bits are individual atoms held in fragile quantum states — superpositions where each atom represents both 0 and 1 simultaneously — that collapse the instant anything disturbs them. That's the central challenge of quantum computing: the very properties that make these machines powerful also make them desperately fragile. Every vibration, every stray photon, every imperfection in a laser beam threatens to destroy the delicate states that carry information.

Physicists have spent decades hunting for qubit platforms that are simultaneously controllable and robust. Superconducting circuits are fast but require near-absolute-zero temperatures and custom-built chips. Trapped ions are precise but hard to scale. Now, researchers at MIT propose turning an existing laboratory tool — the **quantum gas microscope**, a device that traps and images individual atoms — into a universal quantum computer, using a surprisingly sturdy qubit: pairs of fermions, the fundamental category of quantum particles that includes electrons, protons, and certain atoms.

In a new theoretical paper, Xiangkai Sun, Di Luo, and Soonwon Choi describe how to achieve universal quantum computation and large-scale quantum simulation using **fermion-pair registers** — quantum memory units built from bound pairs of fermionic atoms — building on a recent experimental breakthrough showing these registers can hold quantum information for exceptionally long times without losing it to noise.

> **Key Insight:** By encoding qubits in the shared vibrational states of tightly bound fermion pairs — and exploiting fundamental quantum statistics for protection — this approach achieves inherent robustness against the laser noise that plagues most quantum computing platforms.

## How It Works

The starting point is a quantum gas microscope that uses tightly focused lasers to trap ultracold atoms in a grid called an **optical lattice**, with single-atom resolution. Instead of one atom per site, this system places exactly two fermionic atoms at every lattice site. These pairs serve as the qubits.

![Figure 1](/iaifi-research-blog/figures/2306_03905/figure_1.png)

The encoding is elegant. In each site, two atoms sit in a slightly anharmonic trap — like a bowl that's not quite parabolic. The qubit states |0⟩ and |1⟩ differ in how the pair distributes its vibrational energy: in |0⟩, both atoms occupy the first excited vibrational level; in |1⟩, one atom climbs to the second. Crucially, both states carry roughly the same total energy, so stray fluctuations in laser intensity — which shift all energy levels together — can't distinguish between them. The qubits are protected by their own structure.

Manipulating these qubits requires two physical controls:

- **Feshbach interaction strength (U):** Tuning a magnetic field near a **Feshbach resonance** dramatically amplifies atomic interactions. Modulating this field drives transitions between qubit states, implementing single-qubit rotations.
- **Nearest-neighbor hopping amplitude (J):** Atoms quantum-mechanically tunnel between adjacent lattice sites. Controlling this tunneling creates **quantum entanglement** — correlations between neighboring qubit pairs with no classical equivalent — the essential ingredient for quantum computation.

Together, these two knobs produce a complete set of **universal quantum gates**.

The **SWAP gate** is almost free. Without interaction (U = 0), atoms tunnel freely between neighboring sites. Let the system evolve for exactly t = π/(2J) and two qubits exchange their full quantum states. This isn't magic — it's quantum mechanics doing what it does naturally.

The harder part is the **controlled-phase (CPHASE) gate**, which creates the entanglement that makes quantum computers powerful. Here, both hopping and Feshbach interactions are activated simultaneously. Atoms briefly hop to neighboring sites and return in a rapid dance of virtual moves that leaves a permanent mark — a quantum phase shift whose value depends on the state of both qubits. By tuning the ratio U/J and the evolution time, any desired phase angle φ is achievable.

![Figure 2](/iaifi-research-blog/figures/2306_03905/figure_2.png)

Beyond gate-based computation, the system directly simulates a foundational physics model: the **2D quantum Ising model**, which describes quantum particles interacting like tiny magnets and captures phenomena from ordinary magnetism to abrupt quantum phase transitions. By varying the Feshbach interaction strength U(t) over time, the fermion-pair register naturally implements the Ising equations — with tunable effective magnetic fields in two directions — without decomposing the simulation into individual gates. The optical lattice geometry can be freely reconfigured, making this a programmable quantum simulator adaptable to different physical scenarios.

## Why It Matters

The practical challenge for any quantum computing platform isn't just building hardware — it's verifying it works. Quantum states can't be measured without destroying them, and full **quantum process tomography** — the standard method for characterizing what a quantum gate actually does — requires an exponentially large number of measurements.

The MIT team addresses this with an improved **classical shadow process tomography** protocol that requires minimal experimental overhead. Random measurements combined with classical post-processing reconstruct gate behavior with provably efficient sample complexity. For experimentalists working with quantum gas microscopes, this is invaluable: reliable gate characterization without redesigning experiments from scratch.

![Figure 3](/iaifi-research-blog/figures/2306_03905/figure_3.png)

The broader significance is convergence. Quantum gas microscopes were originally built to study how quantum particles behave collectively — exploring exotic states of matter, watching particles freeze in place due to quantum effects, probing strange transport phenomena. This paper shows those same instruments, with existing capabilities, can be repurposed for universal quantum computation.

The fermion-pair platform doesn't require the extreme isolation of trapped ions or the millikelvin temperatures of superconducting chips in specialized cryostats. It lives naturally in the ultracold physics ecosystem that already exists in laboratories worldwide. Any group with a quantum gas microscope is closer to a quantum computer than they may have realized.

Open questions remain. The paper focuses on two-qubit gates between nearest neighbors; longer-range connectivity — essential for many quantum algorithms — would require chains of SWAP operations. Decoherence from atom loss and other sources will set limits on circuit depth. Scaling to thousands of qubits will introduce new engineering challenges. But the theoretical foundation is now in place.

> **Bottom Line:** Fermion-pair registers, already demonstrated experimentally at scale, can implement universal quantum gates and quantum many-body simulations using nothing more than tunable atomic interactions and tunneling — turning quantum gas microscopes into a viable quantum computing platform.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges quantum information science and ultracold atomic physics, translating quantum gate mathematics directly into the physical controls — magnetic fields and laser-tuned tunneling — available in quantum gas microscope experiments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The classical shadow process tomography protocol developed here provides a provably sample-efficient method for characterizing quantum processes, a technique that could accelerate benchmarking and verification workflows across quantum computing platforms broadly.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The fermion-pair register architecture exploits fundamental fermionic exchange symmetry as a built-in error protection mechanism, advancing understanding of how intrinsic quantum statistics can be harnessed for robust quantum information storage.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will explore scaling to larger registers, implementing long-range entanglement, and benchmarking gate fidelities in experimental demonstrations; the full analysis appears on arXiv at 2306.03985.</span></div></div>
</div>
