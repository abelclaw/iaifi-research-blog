---
abstract: Lattice quantum field theory calculations may potentially combine the advantages
  of Hamiltonian formulations with the scalability and control of conventional Lagrangian
  frameworks. However, such hybrid approaches need to consider (1) the differences
  in renormalized coupling values between the two formulations, and (2) finite-volume
  and discretization effects when the Hamiltonian component of the calculation is
  characterized by a smaller volume or coarser lattice spacing than the Lagrangian
  component. This work investigates the role of both factors in the application of
  Hamiltonian-optimized interpolating operator constructions for the conventional
  Lagrangian framework. The numerical investigation is realized for the pseudoscalar
  meson in the Schwinger model, using tensor-network and Monte-Carlo calculations.
  It is demonstrated that tensor-network-optimized constructions are robust to both
  (1) and (2). In particular, accurate optimized constructions for the pseudoscalar
  meson can be obtained from calculations with a smaller number of Hamiltonian lattice
  sites, even when the meson mass itself receives significant finite-volume corrections.
  To the extent that these results generalize to theories with more complicated spectra,
  the method holds promise for near-term applications in large-scale calculations
  of lattice quantum field theory.
arxivId: '2411.02185'
arxivUrl: https://arxiv.org/abs/2411.02185
authors:
- Artur Avkhadiev
- Lena Funcke
- Karl Jansen
- Stefan Kühn
- Phiala E. Shanahan
concepts:
- lattice gauge theory
- interpolating operator optimization
- quantum field theory
- tensor networks
- hamiltonian systems
- hybrid lattice approach
- monte carlo methods
- lagrangian methods
- finite-volume corrections
- renormalization
- quantum states
- quantum simulation
figures:
- /iaifi-research-blog/figures/2411_02185/figure_1.png
- /iaifi-research-blog/figures/2411_02185/figure_1.png
- /iaifi-research-blog/figures/2411_02185/figure_2.png
- /iaifi-research-blog/figures/2411_02185/figure_2.png
- /iaifi-research-blog/figures/2411_02185/figure_3.png
- /iaifi-research-blog/figures/2411_02185/figure_3.png
pdfUrl: https://arxiv.org/pdf/2411.02185v1
published: '2024-11-04T15:39:30+00:00'
theme: Theoretical Physics
title: Small-scale Hamiltonian optimization of interpolating operators for Lagrangian
  lattice quantum field theory
wordCount: 1242
---

## The Big Picture

Imagine trying to find a specific person in a massive crowd using a megaphone. The key is how you call out: you need a signal the right person responds to strongly, while everyone else stays quiet. Particle physicists face a similar challenge when extracting particle properties from lattice quantum field theory calculations.

The "megaphone" is called an **interpolating operator**, a mathematical construction that excites the particle you want to study while suppressing noise from everything else. Getting these operators right makes or breaks the calculation. Poorly tuned operators force physicists to wait for a faint signal to emerge from a storm of noise, and supercomputer time doesn't come cheap.

Two broad approaches exist. The first uses **Monte Carlo** methods, statistical sampling across an enormous number of quantum field configurations. This scales to large, realistic systems and forms the backbone of today's biggest lattice physics computations. The second works directly with quantum states, making it a natural fit for quantum computers and for **tensor networks**, mathematical tools that efficiently compress the staggering complexity of quantum states into something computable.

A natural dream is to combine them: use small, efficient quantum-state calculations to craft better operators, then hand those operators to the Monte Carlo machinery. A team from MIT, DESY, and the University of Bonn has now shown this is achievable. Operators optimized using tensor networks stay accurate even when the quantum-state calculation uses a coarser, smaller grid than the full Monte Carlo simulation.

> **Key Insight:** Tensor networks can optimize interpolating operators on a small, cheap quantum-state simulation, and those optimized operators remain accurate when transplanted into large-scale Monte Carlo calculations, even when the two approaches differ significantly in simulation parameters, physical volume, and grid resolution.

## How It Works

The central object is the **correlation function**, a quantity computed on the lattice to extract particle masses and energies. You insert an interpolating operator at one point in simulated time and another at a later time, then watch how the signal decays. The decay rate encodes the particle's energy. A perfect operator produces a clean exponential decay; a bad one drowns the signal in excited-state noise.

The hybrid strategy works in four steps:

1. **Parameterize the operator.** Write it as a weighted sum over a basis of simpler operators (smeared quark fields, spatially averaged to reduce noise) with tunable coefficients.
2. **Optimize on the Hamiltonian side.** Use a tensor-network calculation on a small lattice to find the coefficient weights that make the resulting quantum state as close as possible to the target particle.
3. **Transfer the coefficients.** Plug those optimized coefficients directly into the Monte Carlo calculation.
4. **Check robustness.** Verify that the transferred construction actually improves statistical precision, despite differences between the two approaches.

![Figure 1](/iaifi-research-blog/figures/2411_02185/figure_1.png)

The team tested this in the **Schwinger model**, quantum electrodynamics reduced to one spatial dimension plus time. Their target was the **pseudoscalar meson**, a quark-antiquark bound state analogous to the pion. This model is a standard proving ground: solvable enough to cross-check, yet complex enough to be nontrivial.

Two mismatches between the approaches could potentially wreck the transfer. First, the renormalized coupling constants (the numbers setting interaction strength once quantum fluctuations are accounted for) differ between the quantum-state and Monte Carlo versions of the same physical theory. This happens because the Hamiltonian formulation treats time as continuous while the Lagrangian (Monte Carlo) approach discretizes both time and space. Second, any practical small-scale quantum-state calculation uses a smaller volume or coarser lattice spacing than the full Monte Carlo simulation.

![Figure 2](/iaifi-research-blog/figures/2411_02185/figure_1.png)

The researchers found that coupling mismatches alone do not significantly degrade the transferred operators. Coarsening the Hamiltonian lattice spacing by a large factor at fixed physical volume eventually hurts accuracy, but reducing physical volume at fixed lattice spacing, which directly cuts computational cost, does not. Here's the surprise: even when the meson mass itself receives large finite-volume corrections in the small Hamiltonian calculation, the optimized operator construction remains accurate. The particle in the box is distorted, but the fingerprint the operator learns is still good.

![Figure 4](/iaifi-research-blog/figures/2411_02185/figure_2.png)

## Why It Matters

Lattice QCD, the gold standard for calculating properties of hadrons like protons, neutrons, and pions, requires enormous computational resources. Better interpolating operators can mean the difference between months and years of supercomputer time. The hybrid approach targets exactly this bottleneck.

The near-term implication has to do with quantum hardware. Tensor-network and quantum-computer calculations are currently limited to small system sizes. The results here show that *small is enough*: a quantum or tensor-network device doesn't need to simulate the full physical volume to deliver useful operator improvements for a large classical calculation. The two technologies can cooperate rather than compete, each doing what it does best.

![Figure 5](/iaifi-research-blog/figures/2411_02185/figure_3.png)

Open questions remain. The Schwinger model is simpler than QCD: a single flavor, no confinement in the usual sense. Whether this robustness extends to theories with richer spectra, where excited states crowd closer together and operator optimization becomes harder, is the real test. The authors flag this explicitly as future work.

> **Bottom Line:** Tensor-network-optimized interpolating operators survive the translation from small Hamiltonian lattices to large Monte Carlo calculations. That opens a practical path toward hybrid quantum-classical lattice field theory, letting small quantum devices punch above their weight in precision physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work builds a direct bridge between tensor-network quantum information methods and conventional Monte Carlo lattice field theory, showing that the two paradigms can cooperate on a single calculation without sacrificing accuracy.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Tensor networks, the same family of algorithms used in many modern AI compression and simulation methods, serve here as optimization engines for physics calculations, with practical value beyond purely machine-learning contexts.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The results point to a near-term pathway for improving the statistical precision of large-scale lattice QCD calculations relevant to nuclear and high-energy physics, including hadronic structure and flavor observables.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will test this hybrid approach in theories with more complex spectra such as QCD; the paper is available as [arXiv:2411.02185](https://arxiv.org/abs/2411.02185), part of the MIT Center for Theoretical Physics preprint series (MIT-CTP/5745).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Small-scale Hamiltonian optimization of interpolating operators for Lagrangian lattice quantum field theory</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[arXiv:2411.02185](https://arxiv.org/abs/2411.02185)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">Artur Avkhadiev, Lena Funcke, Karl Jansen, Stefan Kühn, Phiala E. Shanahan</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Lattice quantum field theory calculations may potentially combine the advantages of Hamiltonian formulations with the scalability and control of conventional Lagrangian frameworks. However, such hybrid approaches need to consider (1) the differences in renormalized coupling values between the two formulations, and (2) finite-volume and discretization effects when the Hamiltonian component of the calculation is characterized by a smaller volume or coarser lattice spacing than the Lagrangian component. This work investigates the role of both factors in the application of Hamiltonian-optimized interpolating operator constructions for the conventional Lagrangian framework. The numerical investigation is realized for the pseudoscalar meson in the Schwinger model, using tensor-network and Monte-Carlo calculations. It is demonstrated that tensor-network-optimized constructions are robust to both (1) and (2). In particular, accurate optimized constructions for the pseudoscalar meson can be obtained from calculations with a smaller number of Hamiltonian lattice sites, even when the meson mass itself receives significant finite-volume corrections. To the extent that these results generalize to theories with more complicated spectra, the method holds promise for near-term applications in large-scale calculations of lattice quantum field theory.</span></div></div>
</div>
