---
abstract: Many materials properties depend on higher-order derivatives of the potential
  energy surface, yet machine learned interatomic potentials (MLIPs) trained with
  a standard loss on energy, force, and stress errors can exhibit error in curvature,
  degrading the prediction of vibrational properties. We introduce phonon fine-tuning
  (PFT), which directly supervises second-order force constants of materials by matching
  MLIP energy Hessians to DFT-computed force constants from finite displacement phonon
  calculations. To scale to large supercells, PFT stochastically samples Hessian columns
  and computes the loss with a single Hessian-vector product. We also use a simple
  co-training scheme to incorporate upstream data to mitigate catastrophic forgetting.
  On the MDR Phonon benchmark, PFT improves Nequix MP by 55% on average across phonon
  thermodynamic properties and achieves state-of-the-art accuracy among models trained
  on Materials Project trajectories. PFT also generalizes to improve properties beyond
  second-derivatives, improving thermal conductivity predictions that rely on third-order
  derivatives of the potential energy.
arxivId: '2601.07742'
arxivUrl: https://arxiv.org/abs/2601.07742
authors:
- Teddy Koker
- Abhijeet Gangan
- Mit Kotak
- Jaime Marian
- Tess Smidt
concepts:
- interatomic potentials
- phonon properties
- fine-tuning
- hessian supervision
- loss function design
- transfer learning
- scalability
- thermal conductivity
- surrogate modeling
- multi-task learning
- equivariant neural networks
- crystal structure
figures:
- /iaifi-research-blog/figures/2601_07742/figure_2.png
- /iaifi-research-blog/figures/2601_07742/figure_3.png
pdfUrl: https://arxiv.org/pdf/2601.07742v3
published: '2026-01-12T17:20:09+00:00'
theme: Foundational AI
title: 'PFT: Phonon Fine-tuning for Machine Learned Interatomic Potentials'
wordCount: 1192
---

## The Big Picture

Imagine trying to teach someone to play piano by only grading whether they hit the right notes. You never check their timing, dynamics, or how smoothly they transition between chords. They'd pass the test but sound awful in a real performance. That's roughly the problem facing some of the most powerful AI tools in materials science.

**Machine learned interatomic potentials (MLIPs)** are AI models that predict how atoms push and pull on each other inside a material. They're a fast, cheap alternative to quantum physics calculations that would otherwise take hours on supercomputers.

But standard MLIPs are trained to predict energies, forces, and stresses. That sounds thorough, and yet it misses something important: many physical properties depend not on the energy itself but on its *curvature*, how sharply the energy changes as atoms wiggle around their resting positions. Get the curvature wrong, and predictions of how a material conducts heat, stores energy, or vibrates fall apart.

A team of MIT and UCLA researchers has introduced **Phonon Fine-Tuning (PFT)**, a targeted training technique that directly teaches AI models to get the curvature right. The result: a 55% average improvement in vibrational property accuracy at a fraction of the original training cost.

> **Key Insight:** Standard MLIP training only indirectly shapes the curvature of the energy landscape, leaving systematic errors in vibrational properties. PFT fixes this by directly supervising that curvature, and the gains carry over into more complex properties like thermal conductivity.

## How It Works

The curvature that matters here is encoded in **phonons**, the quantum mechanical vibrations of atoms in a crystal lattice. Phonons govern how heat flows through a material, how it expands when warmed, and whether it can become a superconductor. Calculating phonon properties requires the **force constant matrix** (also called the **Hessian**): a grid encoding how the force on every atom changes when any other atom is nudged. This matrix is the mathematical fingerprint of curvature.

![Figure 1](/iaifi-research-blog/figures/2601_07742/figure_2.png)

The standard approach is a **finite displacement calculation**: take a supercell (a tiled copy of the crystal's repeating unit, large enough that edge effects vanish), nudge each atom, measure forces using **density functional theory (DFT)**, and numerically differentiate. DFT computes electron-atom interactions from first principles, and it's slow. Supercells can contain hundreds or thousands of atoms, and the full Hessian for *N* atoms has 3*N* × 3*N* entries. Training directly on that matrix is computationally ruinous.

PFT sidesteps this with three ideas:

- **Stochastic column sampling:** At each training step, randomly select a small subset of Hessian entries rather than computing the full matrix.
- **Hessian-vector products:** Each sample is extracted via **automatic differentiation** (the same technique that makes neural networks trainable), reducing per-step cost from quadratic to linear in system size.
- **Co-training:** Phonon datasets are small compared to MLIP pretraining data. Fine-tuning on phonon data alone risks **catastrophic forgetting**, where the model loses previously learned abilities. PFT interleaves pretraining batches alongside phonon data, improving phonon accuracy while degrading less than 1% on general stability benchmarks.

The loss function penalizes the gap between the MLIP's predicted force constants and DFT-computed reference values, giving the model direct feedback on the quantity it was previously getting wrong.

## Why It Matters

The researchers applied PFT to Nequix MP, a state-of-the-art foundation model pretrained on the Materials Project trajectory dataset, and benchmarked it on the MDR Phonon dataset, a held-out set of DFT calculations covering a wide range of crystal chemistries.

The results:

- **55% average improvement** across four phonon thermodynamic metrics: maximum phonon frequency, vibrational entropy, Helmholtz free energy, and heat capacity
- **State-of-the-art accuracy** among all models trained on Materials Project trajectories
- Thermal conductivity improved from 0.446 to **0.306 κ SRME** on Matbench Discovery, also state-of-the-art in its class

That last result is worth pausing on. PFT targets second derivatives of the potential energy. Yet it also improved predictions that depend on *third-order* derivatives. Better curvature supervision seems to teach the model something more general about the shape of the energy landscape, a lesson that carries upward through higher-order properties.

![Figure 2](/iaifi-research-blog/figures/2601_07742/figure_3.png)

The materials science community has invested enormous resources building "universal" MLIPs, trained on millions of DFT calculations spanning the periodic table. These models are increasingly used as drop-in replacements for DFT in high-throughput screening workflows. But if they systematically misrepresent energy-surface curvature, anything vibrational becomes unreliable.

PFT offers a lightweight fix: a fine-tuning pass that costs a fraction of pretraining yet corrects the specific blind spot that matters most for thermal and vibrational applications. The team also demonstrated it on a second base model trained on the larger OMat24 dataset and observed consistent gains, confirming the technique is modular and not tied to any particular architecture or training history.

Open questions remain. The phonon training set, while broad, is small relative to the full diversity of possible crystals. Expanding it and testing PFT at larger scales, or extending direct derivative supervision to third-order force constants, are natural next steps.

> **Bottom Line:** By teaching AI interatomic potentials to match the *curvature* of quantum energy surfaces, not just the surface itself, PFT achieves a 55% improvement in phonon property accuracy and sets a new state of the art for thermodynamic predictions in AI-driven materials discovery.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects equivariant neural network architectures from machine learning with the phonon formalism from condensed matter physics, using automatic differentiation to directly supervise quantum mechanical force constants during AI training.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">PFT introduces a scalable Hessian-vector product sampling strategy that makes second-derivative supervision tractable for large systems, expanding the toolkit for training physics-informed neural networks on higher-order properties.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By improving AI predictions of phonon dispersions and thermal conductivity, PFT makes computational screening of thermoelectric, superconducting, and thermally functional materials far more reliable.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend direct derivative supervision to third-order force constants and larger phonon datasets; the full paper is available at [arXiv:2601.07742](https://arxiv.org/abs/2601.07742) (Koker et al., *PFT: Phonon Fine-tuning for Machine Learned Interatomic Potentials*).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">PFT: Phonon Fine-tuning for Machine Learned Interatomic Potentials</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2601.07742</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Teddy Koker", "Abhijeet Gangan", "Mit Kotak", "Jaime Marian", "Tess Smidt"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Many materials properties depend on higher-order derivatives of the potential energy surface, yet machine learned interatomic potentials (MLIPs) trained with a standard loss on energy, force, and stress errors can exhibit error in curvature, degrading the prediction of vibrational properties. We introduce phonon fine-tuning (PFT), which directly supervises second-order force constants of materials by matching MLIP energy Hessians to DFT-computed force constants from finite displacement phonon calculations. To scale to large supercells, PFT stochastically samples Hessian columns and computes the loss with a single Hessian-vector product. We also use a simple co-training scheme to incorporate upstream data to mitigate catastrophic forgetting. On the MDR Phonon benchmark, PFT improves Nequix MP by 55% on average across phonon thermodynamic properties and achieves state-of-the-art accuracy among models trained on Materials Project trajectories. PFT also generalizes to improve properties beyond second-derivatives, improving thermal conductivity predictions that rely on third-order derivatives of the potential energy.</span></div></div>
</div>
