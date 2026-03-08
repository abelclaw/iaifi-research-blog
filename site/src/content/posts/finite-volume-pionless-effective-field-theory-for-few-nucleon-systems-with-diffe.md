---
abstract: Finite-volume pionless effective field theory provides an efficient framework
  for the extrapolation of nuclear spectra and matrix elements calculated at finite
  volume in lattice QCD to infinite volume, and to nuclei with larger atomic number.
  In this work, it is demonstrated how this framework may be implemented via a set
  of correlated Gaussian wavefunctions optimised using differentiable programming
  and via solution of a generalised eigenvalue problem. This approach is shown to
  be significantly more efficient than a stochastic implementation of the variational
  method based on the same form of correlated Gaussian wavefunctions, yielding comparably
  accurate representations of the ground-state wavefunctions with an order of magnitude
  fewer terms. The efficiency of representation allows such calculations to be extended
  to larger systems than in previous work. The method is demonstrated through calculations
  of the binding energies of nuclei with atomic number $A\in\{2,3,4\}$ in finite volume,
  matched to lattice QCD calculations at quark masses corresponding to $m_π=806$ MeV,
  and infinite-volume effective field theory calculations of $A\in\{2,3,4,5,6\}$ systems
  based on this matching.
arxivId: '2202.03530'
arxivUrl: https://arxiv.org/abs/2202.03530
authors:
- Xiangkai Sun
- William Detmold
- Di Luo
- Phiala E. Shanahan
concepts:
- effective field theory
- variational wavefunction optimization
- finite-volume eft
- differentiable programming
- lattice qcd
- correlated gaussian wavefunctions
- eigenvalue decomposition
- physics-informed neural networks
- quantum field theory
- monte carlo methods
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2202_03530/figure_1.png
- /iaifi-research-blog/figures/2202_03530/figure_1.png
- /iaifi-research-blog/figures/2202_03530/figure_2.png
- /iaifi-research-blog/figures/2202_03530/figure_2.png
- /iaifi-research-blog/figures/2202_03530/figure_3.png
- /iaifi-research-blog/figures/2202_03530/figure_3.png
pdfUrl: https://arxiv.org/pdf/2202.03530v2
published: '2022-02-07T21:42:57+00:00'
theme: Theoretical Physics
title: Finite-Volume Pionless Effective Field Theory for Few-Nucleon Systems with
  Differentiable Programming
wordCount: 975
---

## The Big Picture

Imagine assembling a jigsaw puzzle where the pieces keep shifting shape. That's roughly what nuclear physicists face when computing how protons and neutrons bind from first principles. Quantum Chromodynamics (QCD) describes quarks and gluons with exquisite precision, but its equations become impossibly tangled at the energy scales where nuclei form.

The standard workaround is to discretize space and time into a grid — a "lattice" — and simulate physics on supercomputers. But lattice calculations are confined to tiny artificial boxes, and computational cost explodes as you add more nucleons.

A new paper from MIT's Center for Theoretical Physics and IAIFI offers a smarter path. Rather than brute-forcing larger lattice calculations, the researchers use a bridge theory — **pionless effective field theory**, a streamlined description that captures essential nuclear forces without tracking every quark and gluon — to translate small lattice results into predictions for bigger nuclei. And they made that bridge dramatically more efficient by replacing a slow, random search with a modern AI technique: differentiable programming.

The result achieves the same accuracy as previous methods with roughly ten times fewer terms, and extends nuclear predictions to systems previously out of reach.

> **Key Insight:** By applying differentiable programming — the mathematical engine behind neural network training — to nuclear wavefunction optimization, this work squeezes an order-of-magnitude efficiency improvement from the same underlying physics framework.

## How It Works

The strategy unfolds in two stages. First, run a lattice QCD calculation of a small nucleus inside an artificial box. Those results carry **finite-volume artifacts** — distortions caused by the fact that particles in a box behave differently than particles in infinite space. Second, deploy **finite-volume pionless effective field theory (FVEFT)** to model those same box calculations, pin down the theory's free parameters (called **low-energy constants**, or LECs — the adjustable dials controlling how strongly nucleons attract each other), then extrapolate to infinite volume and larger nuclei.

The tricky part is step two. FVEFT requires finding the **wavefunction** — a mathematical description of where all particles are likely to be — that gives the lowest possible energy. The standard approach, the **stochastic variational method (SVM)**, builds a trial wavefunction by randomly proposing Gaussian "blobs" one at a time, keeping each only if it improves the energy estimate. It works, but requires hundreds or thousands of terms.

![Figure 1](/iaifi-research-blog/figures/2202_03530/figure_1.png)

The new approach flips the script. **Differentiable programming (DP)** writes down a compact wavefunction using a fixed number of **correlated Gaussian** terms — multi-dimensional bell curves that encode how particles influence each other's positions — then computes how energy changes with respect to every parameter. Gradient descent simultaneously optimizes all parameters, steering the wavefunction toward the true ground state. It's the same mathematics that trains a neural network, applied to nuclear wavefunctions.

The key steps:

1. **Parameterize** the trial wavefunction as a sum of correlated Gaussians with adjustable widths, centers, and correlations.
2. **Compute the energy** as a differentiable function of those parameters using quantum mechanical expectation values.
3. **Backpropagate** — automatically calculate how each parameter nudges the energy — and update all parameters simultaneously via gradient descent.
4. **Stack multiple optimized states** and solve a **generalized eigenvalue problem (GEVP)** to extract the most accurate energy levels from overlapping approximate solutions.

![Figure 2](/iaifi-research-blog/figures/2202_03530/figure_1.png)

The payoff is dramatic. Where SVM needs hundreds of Gaussian terms to represent the helium-4 (⁴He) ground state, differentiable programming achieves comparable accuracy with roughly ten times fewer. That compactness matters: memory and compute scale badly with term count, so a 10× reduction opens calculations that were previously impossible.

![Figure 3](/iaifi-research-blog/figures/2202_03530/figure_2.png)

The team validated the method by computing binding energies for nuclei with A∈{2,3,4} inside finite-volume boxes, matching them to existing lattice QCD results at an artificially heavy pion mass of m_π = 806 MeV. With LECs pinned down, they extrapolated to infinite volume and pushed up to A∈{5,6} — helium-5 and lithium-6 — systems not previously reached with this framework.

![Figure 4](/iaifi-research-blog/figures/2202_03530/figure_2.png)

## Why It Matters

This work sits at the intersection of two grand challenges: making nuclear physics rigorous from first principles, and deploying AI-driven optimization beyond machine learning. The differentiable programming revolution — fueled by PyTorch and JAX — has already transformed computer vision, language modeling, and protein structure prediction. This paper shows it can do the same for quantum few-body physics.

Physicists can now extend the FVEFT matching procedure to A=5 and A=6 systems, building a longer bridge from lattice QCD toward the nuclear chart. As lattice QCD approaches physical quark masses and tightens its systematic uncertainties, this matching framework will be ready to absorb those results and propagate them to larger nuclei. The same differentiable variational approach could also target nuclear matrix elements relevant to neutrinoless double-beta decay searches, or other few-body quantum systems where compact wavefunction representations are prized.

> **Bottom Line:** Replacing random sampling with gradient-based optimization cuts nuclear wavefunction calculation costs by an order of magnitude, enabling first-principles-anchored predictions for A=5 and A=6 nuclei and setting the stage for a systematic bridge from lattice QCD to nuclear physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses differentiable programming — a cornerstone of modern AI — with pionless nuclear effective field theory, demonstrating that gradient-based optimization can directly accelerate rigorous quantum many-body calculations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper shows that differentiable programming is not just a neural network training trick but a general-purpose scientific optimization engine, achieving order-of-magnitude efficiency gains over stochastic methods in a demanding physics application.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By extending finite-volume EFT calculations to A=5 and A=6 nuclei matched to lattice QCD, this research advances the long-term goal of predicting nuclear properties directly from the Standard Model's quark-gluon dynamics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will target physical pion masses and larger nuclei as lattice QCD matures; the full methodology is detailed in arXiv:2407.07946.</span></div></div>
</div>
