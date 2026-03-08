---
abstract: Classical and quantum annealing are computing paradigms that have been proposed
  to solve a wide range of optimization problems. In this paper, we aim to enhance
  the performance of annealing algorithms by introducing the technique of degeneracy
  engineering, through which the relative degeneracy of the ground state is increased
  by modifying a subset of terms in the objective Hamiltonian. We illustrate this
  novel approach by applying it to the example of $\ell_0$-norm regularization for
  sparse linear regression, which is in general an NP-hard optimization problem. Specifically,
  we show how to cast $\ell_0$-norm regularization as a quadratic unconstrained binary
  optimization (QUBO) problem, suitable for implementation on annealing platforms.
  As a case study, we apply this QUBO formulation to energy flow polynomials in high-energy
  collider physics, finding that degeneracy engineering substantially improves the
  annealing performance. Our results motivate the application of degeneracy engineering
  to a variety of regularized optimization problems.
arxivId: '2205.10375'
arxivUrl: https://arxiv.org/abs/2205.10375
authors:
- Eric R. Anschuetz
- Lena Funcke
- Patrick T. Komiske
- Serhii Kryhin
- Jesse Thaler
concepts:
- degeneracy engineering
- sparse models
- qubo encoding
- quantum computing
- regression
- collider physics
- physics-motivated optimization
- monte carlo methods
- loss function design
- jet physics
- interpretability
figures:
- /iaifi-research-blog/figures/2205_10375/figure_1.png
- /iaifi-research-blog/figures/2205_10375/figure_1.png
pdfUrl: https://arxiv.org/pdf/2205.10375v2
published: '2022-05-20T18:00:00+00:00'
theme: Theoretical Physics
title: 'Degeneracy Engineering for Classical and Quantum Annealing: A Case Study of
  Sparse Linear Regression in Collider Physics'
wordCount: 1121
---

## The Big Picture

Imagine searching for a needle in a haystack, blindfolded, feeling your way through. Now imagine someone secretly replaced that single needle with a hundred needles scattered throughout. Your odds of success skyrocket, even though the fundamental problem hasn't changed.

Quantum annealing and its classical cousin, simulated annealing, mimic the physics of cooling. Just as metal slowly cools into a stable crystalline structure, these algorithms gradually home in on the best answer to a problem. The challenge is that complex optimization problems are riddled with false solutions and dead ends, with only a handful of correct answers scattered across a vast solution space. Annealing can easily get trapped before finding the right one.

Researchers at MIT and IAIFI have introduced **degeneracy engineering**, a systematic way to reshape the optimization landscape so the correct answer is far easier to find, without changing what that answer is. They demonstrated this on a particularly hard problem: using sparse regression to decode particle collider data.

> **Key Insight:** By deliberately encoding problems with redundant bits, you can make the correct answer (the ground state) appear many more times in the solution space, dramatically improving the odds that an annealing algorithm finds it.

## How It Works

The paper tackles **sparse linear regression with ℓ₀-norm regularization**: given a huge library of candidate functions for describing collider data, find the smallest subset that still fits well. Unlike ridge regression (ℓ₂) or lasso (ℓ₁), which penalize large coefficients, the ℓ₀ penalty directly counts nonzero terms. That makes it powerful but NP-hard.

The first step is translating this into a **QUBO (Quadratic Unconstrained Binary Optimization)**, the native language of annealing hardware. Each real-valued coefficient is encoded in binary, and the ℓ₀ penalty (which asks "is this coefficient nonzero?") is rewritten using **ancilla** bits, extra redundant bits that make the penalty expressible as a simple product of two binary variables.

Two encoding strategies behave very differently in practice:

- **Single ancilla encoding:** Each "zero coefficient" solution maps to exactly one bit-string configuration.
- **Double ancilla encoding:** Multiple distinct bit-strings all represent the same zero-coefficient solution. They are degenerate.

This degeneracy is the whole point. The relative degeneracy, meaning correct-solution configuration count divided by first-excited-state configuration count, grows substantially when one extra ancilla is added. When an annealing algorithm explores the solution space, a more degenerate ground state is a bigger target. The algorithm doesn't need to find one specific needle; any one of many equivalent needles will do. Mathematically, this enlarges the energy gap between the correct solution and all nearby wrong ones, a property both classical and quantum annealing exploit to converge reliably.

![Figure 1](/iaifi-research-blog/figures/2205_10375/figure_1.png)

To stress-test degeneracy engineering, the team used **Energy Flow Polynomials (EFPs)**, a rich linear basis for describing particle jets. Jets are the sprays of particles produced when protons collide at experiments like the Large Hadron Collider. EFPs are indexed by graph topologies, each encoding a specific pattern of energy correlations among particles in a jet. Certain linear relations among EFPs are known analytically (for example, the square of a degree-1 EFP exactly equals a specific degree-2 EFP), which means regression problems can be constructed with known ground truth. That gives an absolute benchmark most optimization test cases lack.

![Figure 2](/iaifi-research-blog/figures/2205_10375/figure_1.png)

The results were unambiguous. The single-ancilla encoding performed poorly; the annealer consistently missed the known optimal solution. The double-ancilla encoding found the correct sparse solution far more reliably across all tested problems. The paper also introduces two "refined regression" heuristics that warm-start annealing from classical ℓ₁ or ℓ₂ solutions, using fast classical methods to identify a promising region and then annealing to refine. These hybrid approaches point toward practical strategies for near-term quantum hardware.


## Why It Matters

Sparse ℓ₀ regression could unlock more efficient jet classification and observable discovery at colliders. If a handful of EFPs can do the job that thousands currently do, that's both computationally cleaner and physically more interpretable.

From the quantum computing angle, degeneracy engineering is general-purpose. Any optimization problem cast as a QUBO can potentially benefit from identifying redundant encodings that increase ground-state degeneracy. It's a new design axis, complementary to existing approaches like penalty term tuning and embedding optimization. As quantum annealing hardware scales and competition with classical solvers intensifies, principled methods for steering the optimization landscape toward correct solutions will matter more, not less.

Open questions remain. The simulations used PIMC (Path Integral Monte Carlo) as a proxy for quantum annealing, not physical hardware; performance on devices like D-Wave is untested. How degeneracy engineering interacts with hardware noise and connectivity constraints is an important direction for future work.

> **Bottom Line:** Degeneracy engineering, deliberately adding redundant bits to make the correct answer a bigger target in solution space, substantially improves annealing performance on hard optimization problems. The authors demonstrate this concretely on sparse regression tasks in collider physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects quantum computing algorithm design with high-energy collider physics, using analytically known EFP relations to rigorously benchmark a novel optimization technique applicable across both fields.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Degeneracy engineering provides a general tool for formulating hard combinatorial optimization problems as QUBOs, with demonstrated improvements in annealing performance for NP-hard sparse regression.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Sparse ℓ₀-norm regression over Energy Flow Polynomials offers a computationally tractable path to identifying minimal, interpretable sets of collider observables for jet classification and reconstruction tasks.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will target implementation on physical quantum annealing hardware and extension to larger EFP bases; the full paper is available at [arXiv:2205.10375](https://arxiv.org/abs/2205.10375).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Degeneracy Engineering for Classical and Quantum Annealing: A Case Study of Sparse Linear Regression in Collider Physics</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2205.10375</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Eric R. Anschuetz", "Lena Funcke", "Patrick T. Komiske", "Serhii Kryhin", "Jesse Thaler"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Classical and quantum annealing are computing paradigms that have been proposed to solve a wide range of optimization problems. In this paper, we aim to enhance the performance of annealing algorithms by introducing the technique of degeneracy engineering, through which the relative degeneracy of the ground state is increased by modifying a subset of terms in the objective Hamiltonian. We illustrate this novel approach by applying it to the example of $\ell_0$-norm regularization for sparse linear regression, which is in general an NP-hard optimization problem. Specifically, we show how to cast $\ell_0$-norm regularization as a quadratic unconstrained binary optimization (QUBO) problem, suitable for implementation on annealing platforms. As a case study, we apply this QUBO formulation to energy flow polynomials in high-energy collider physics, finding that degeneracy engineering substantially improves the annealing performance. Our results motivate the application of degeneracy engineering to a variety of regularized optimization problems.</span></div></div>
</div>
