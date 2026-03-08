---
abstract: In Monte Carlo calculations of expectation values in lattice quantum field
  theories, the stochastic variance of the sampling procedure that is used defines
  the precision of the calculation for a fixed number of samples. If the variance
  of an estimator of a particular quantity is formally infinite, or in practice very
  large compared to the square of the mean, then that quantity can not be reliably
  estimated using the given sampling procedure. There are multiple scenarios in which
  this occurs, including in Lattice Quantum Chromodynamics, and a particularly simple
  example is given by the Gross-Neveu model where Monte Carlo calculations involve
  the introduction of auxiliary bosonic variables through a Hubbard-Stratonovich (HS)
  transformation. Here, it is shown that the variances of HS estimators for classes
  of operators involving fermion fields are divergent in this model and an even simpler
  zero-dimensional analogue. To correctly estimate these observables, two alternative
  sampling methods are proposed and numerically investigated.
arxivId: '2205.01001'
arxivUrl: https://arxiv.org/abs/2205.01001
authors:
- Cagin Yunus
- William Detmold
concepts:
- monte carlo methods
- infinite variance sampling
- quantum field theory
- hubbard-stratonovich transformation
- lattice qcd
- lattice gauge theory
- sequential reweighting
- uncertainty quantification
- stochastic processes
- eigenvalue decomposition
figures:
- /iaifi-research-blog/figures/2205_01001/figure_1.png
- /iaifi-research-blog/figures/2205_01001/figure_1.png
- /iaifi-research-blog/figures/2205_01001/figure_2.png
- /iaifi-research-blog/figures/2205_01001/figure_2.png
- /iaifi-research-blog/figures/2205_01001/figure_3.png
- /iaifi-research-blog/figures/2205_01001/figure_3.png
pdfUrl: https://arxiv.org/pdf/2205.01001v1
published: '2022-05-02T15:58:47+00:00'
theme: Theoretical Physics
title: Infinite Variance in Monte Carlo Sampling of Lattice Field Theories
wordCount: 1054
---

## The Big Picture

Imagine measuring the average height of people in a room, but every so often, a giant walks in — someone ten thousand feet tall — destroying your running average. You could take a million measurements and still never get a reliable answer. This is the statistical nightmare physicists face when calculating certain properties of the subatomic world using **Monte Carlo sampling** — a method that uses random numbers to numerically estimate quantities too complex to solve analytically.

In quantum field theory, the mathematical language describing particles and forces at their most fundamental level, physicists can't solve equations on a whiteboard. Instead, they chop spacetime into a discrete grid called a **lattice**, then use Monte Carlo sampling to estimate physical quantities numerically.

It works beautifully in many cases. But sometimes the very structure of the theory causes the variance of the estimator — the spread in your answers — to be formally *infinite*. When that happens, no amount of computing power gives a reliable result. You can run your simulation forever and never converge.

Researchers Cagin Yunus and William Detmold at MIT's Center for Theoretical Physics have diagnosed exactly *why* this infinite-variance problem arises in specific theories, particularly the Gross-Neveu model and, more broadly, Lattice QCD — and proposed two concrete fixes.

> **Key Insight:** In certain lattice field theories, standard Monte Carlo estimators for fermion-field operators have formally infinite variance — not because of numerical errors, but because of the mathematical structure of the sampling procedure itself. This renders any finite number of samples statistically meaningless.

## How It Works

The problem starts with how physicists handle **fermions** — particles like quarks and electrons governed by the Pauli exclusion principle, which forbids two fermions from occupying the same quantum state. Fermions are notoriously difficult to simulate directly. The standard workaround is the **Hubbard-Stratonovich (HS) transformation**: introduce an auxiliary **bosonic** field — a fictional particle type without the Pauli restriction — that replaces complicated four-fermion interaction terms with simpler two-way ones. Mathematically exact, but it changes what you're sampling over.

In the **Gross-Neveu model** — a 2D quantum field theory sharing key structural features with QCD (Quantum Chromodynamics, the theory of the strong nuclear force) and widely used as a theoretical laboratory — this HS transformation introduces a continuous auxiliary field. Monte Carlo then samples configurations of this field.

The trouble: when the **Dirac operator** (the matrix governing fermion behavior) has **eigenvalues** close to zero — "exceptional configurations" — the estimator for fermion propagators blows up. Yunus and Detmold prove this rigorously: for operators built from fermion fields, the HS estimators have *divergent second moments*, meaning variance is not merely large but formally infinite. The consequences are stark:

- The **Central Limit Theorem** no longer applies — sample averages don't converge to true means
- Sample variance doesn't stabilize; it keeps growing with each new sample
- No finite number of Monte Carlo samples yields a statistically reliable result

![Figure 1](/iaifi-research-blog/figures/2205_01001/figure_1.png)

To build intuition, the authors first study a zero-dimensional toy model — no spacetime, just the algebraic structure — before tackling the full 2D Gross-Neveu model. The toy model is analytically tractable, letting them verify results against exact calculations before testing two proposed solutions.

**Solution 1: Discrete Hubbard-Stratonovich.** Replace the continuous auxiliary field with one taking only a finite set of values. Variance is manifestly finite by construction — no single sample can produce an infinite contribution. The cost: configurations grow exponentially with system size, limiting scalability. For small systems, it works well.

![Figure 2](/iaifi-research-blog/figures/2205_01001/figure_1.png)

**Solution 2: Sequential Reweighting.** For physical quantities that are always zero or positive — covering many observables in these theories — write the mean of a high-variance quantity as a *product* of means of lower-variance quantities. Instead of estimating one wildly fluctuating number directly, decompose it into a chain: estimate the first factor, use those results to estimate the second conditioned on the first, and so on. Each factor has finite variance, even when the direct estimate would not.

![Figure 3](/iaifi-research-blog/figures/2205_01001/figure_2.png)

Sequential reweighting proves particularly powerful in numerical tests — correctly recovering exact answers where the standard HS estimator fails completely, even when that estimator's sample variance appears, misleadingly, well-behaved.

![Figure 4](/iaifi-research-blog/figures/2205_01001/figure_2.png)

## Why It Matters

This isn't abstract. Lattice QCD — governing the strong nuclear force that binds protons and neutrons — faces related infinite-variance problems from zero-modes of the Dirac operator. Nuclear correlation functions built from large numbers of quark fields, essential for understanding atomic nuclei from first principles, hit exactly this wall. The more quarks involved, the worse the problem gets.

The issue is structural: whenever you use a continuous HS transformation to handle fermionic interactions, you potentially introduce infinite-variance estimators. That spans condensed matter physics (the Hubbard model, central to theories of high-temperature superconductivity) and particle physics alike. Sequential reweighting is general enough to apply far beyond the Gross-Neveu model, offering a practical path forward where discrete HS transformations become computationally infeasible.

![Figure 5](/iaifi-research-blog/figures/2205_01001/figure_3.png)

Open questions remain. The discrete HS approach needs a way to scale to larger volumes — perhaps through importance sampling within the discrete space. Both methods need testing in full 4D lattice QCD, where computational stakes are highest.

![Figure 6](/iaifi-research-blog/figures/2205_01001/figure_3.png)

> **Bottom Line:** Yunus and Detmold have rigorously identified a fundamental statistical failure mode in Monte Carlo simulations of lattice field theories and offered two workable remedies. Their sequential reweighting method points toward reliable first-principles calculations of fermion observables that were previously beyond reach.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges rigorous statistical theory with lattice quantum field theory, using tools from probability and stochastic analysis to diagnose and fix a fundamental computational problem in nuclear and particle physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The sequential reweighting framework offers a general strategy for taming infinite-variance estimators in Monte Carlo methods — with potential applications wherever importance sampling and stochastic estimation face similar breakdown modes, including machine learning contexts.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By characterizing and resolving infinite-variance failures in the Gross-Neveu model and outlining the path to Lattice QCD, this work directly advances prospects for reliable first-principles calculations of hadronic and nuclear observables from the strong force.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend these methods to larger spacetime volumes and full 4D lattice QCD; the paper is available at arXiv:2501.01496.</span></div></div>
</div>
