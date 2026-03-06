---
abstract: Optical computing often employs tailor-made hardware to implement specific
  algorithms, trading generality for improved performance in key aspects like speed
  and power efficiency. An important computing approach that is still missing its
  corresponding optical hardware is probabilistic computing, used e.g. for solving
  difficult combinatorial optimization problems. In this study, we propose an experimentally
  viable photonic approach to solve arbitrary probabilistic computing problems. Our
  method relies on the insight that coherent Ising machines composed of coupled and
  biased optical parametric oscillators can emulate stochastic logic. We demonstrate
  the feasibility of our approach by using numerical simulations equivalent to the
  full density matrix formulation of coupled optical parametric oscillators.
arxivId: '2406.04000'
arxivUrl: https://arxiv.org/abs/2406.04000
authors:
- Michael Horodynski
- Charles Roques-Carmes
- Yannick Salamin
- Seou Choi
- Jamison Sloan
- Di Luo
- Marin Soljačić
concepts:
- optical parametric oscillators
- probabilistic computing
- stochastic processes
- coherent ising machines
- hamiltonian systems
- phase transitions
- inverse problems
- simulation-based inference
- monte carlo methods
- bayesian inference
figures:
- /iaifi-research-blog/figures/2406_04000/figure_1.png
- /iaifi-research-blog/figures/2406_04000/figure_2.png
- /iaifi-research-blog/figures/2406_04000/figure_3.png
pdfUrl: https://arxiv.org/pdf/2406.04000v1
published: '2024-06-06T12:19:55+00:00'
theme: Theoretical Physics
title: Stochastic logic in biased coupled photonic probabilistic bits
wordCount: 955
---

## The Big Picture

Imagine solving a puzzle where thousands of pieces must fit together simultaneously, not one at a time, but all at once. Classical computers tackle such problems sequentially, which becomes impossibly slow as the puzzle grows. Nature, however, solves similar problems all the time: atoms in magnets spontaneously arrange into minimum-energy configurations without trying every combination. What if we could build a computer that worked the same way, using light?

That's the promise of **probabilistic computing**, an approach where individual bits don't hold fixed 0s and 1s but fluctuate randomly between both states, like a coin spinning in mid-air. String enough of these "probabilistic bits" together and the whole system naturally gravitates toward solutions to hard optimization problems. The catch: nobody had built a fully functional optical version. Until now.

Researchers at MIT and Stanford have shown that networks of coupled laser-like devices, guided by carefully injected beams of light, can carry out any kind of probabilistic logic operation. This transforms existing optical hardware (machines already used to search for optimal solutions to complex problems) into a general-purpose probabilistic computer, a key missing piece in the optical computing puzzle.

> **Key Insight:** By injecting a small coherent bias field into each node of an optical parametric oscillator network, researchers can implement the full Ising Hamiltonian, including the previously missing "Zeeman term," enabling any probabilistic logic circuit to run on optical hardware.

## How It Works

The paper introduces a three-step recipe for converting any computational problem into something a photonic network can solve natively.

![Figure 1](/iaifi-research-blog/figures/2406_04000/figure_1.png)

1. **Write the truth table.** Every logic gate (AND, OR, XOR) can be described by a table listing all possible input-output combinations.

2. **Map to an Ising model.** The truth table gets translated into an **Ising Hamiltonian**, the physics framework describing how a collection of interacting binary elements (magnetic spins pointing either up or down) settles into its lowest-energy state. This Hamiltonian has two components: a **coupling matrix J** (how spins interact) and a **Zeeman vector h** (a local field pushing each spin toward 0 or 1). Previous optical Ising machines handled only the coupling part. A simple AND gate *requires* a nonzero Zeeman term; without it, general probabilistic logic is impossible.

3. **Build the OPO network.** **Optical parametric oscillators (OPOs)** are laser-like devices where a powerful pump drives a specially designed optical cavity. Above a threshold pump power, each OPO spontaneously settles into one of two output phases (+1 or -1), chosen randomly. That binary, random choice is exactly what a probabilistic bit does.

The innovation is the **bias field**: a weak beam injected into each OPO cavity at the signal frequency. This nudges the cavity's internal state, tilting the odds of landing in +1 versus -1. Tune the bias field strength and you tune the probability, the optical equivalent of a magnetic field nudging a spin.

The team derived this behavior from the **density matrix formulation** of quantum optics, the most complete framework for describing quantum systems, capturing both quantum uncertainty and classical randomness simultaneously. They showed it's equivalent to a set of **stochastic differential equations** tracking how probabilities evolve over time.

By expanding the OPO's in-phase amplitude in powers of the coupling/bias strength ε, they proved analytically that the network's steady state minimizes the full Ising energy, Zeeman term included. The photon decay rate Γ plays the role of the energy landscape: the network settles where Γ is minimized, which corresponds exactly to the Ising ground state.

Numerical simulations confirmed the theory. Networks implementing AND, OR, and other stochastic logic gates reproduced the correct probabilistic truth tables, matching predictions from p-bit theory exactly.

## Why It Matters

Probabilistic computing has already shown promise across a range of applications: solving combinatorial optimization problems that defeat classical algorithms, running Bayesian inference, accelerating quantum Monte Carlo simulations, and training restricted Boltzmann machines. Building dedicated hardware for each application is expensive and slow. A general-purpose photonic p-computer could tackle all of these on the same physical substrate.

![Figure 2](/iaifi-research-blog/figures/2406_04000/figure_2.png)

The timing matters too. Moore's law is stalling. Neural network accelerators are proliferating. Optical hardware is maturing rapidly. What's been missing is a viable optical approach to probabilistic computing, one that requires no exotic new components, just clever use of existing OPO technology augmented with bias fields.

The path from proposal to experimental hardware is short: OPO networks already exist in labs, and injecting coherent bias fields is technically straightforward. Next steps involve scaling to larger networks and benchmarking against electronic **p-bit** (probabilistic bit) implementations on real optimization problems.

![Figure 3](/iaifi-research-blog/figures/2406_04000/figure_3.png)

> **Bottom Line:** By adding a simple bias field to optical parametric oscillator networks, this MIT/Stanford team unlocks fully general probabilistic computing in the optical domain, turning coherent Ising machines into all-purpose stochastic logic engines that could eventually outpace electronic alternatives in speed and energy efficiency.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges quantum optics and computer science, mapping probabilistic computing frameworks onto the physics of nonlinear optical cavities. The stochastic behavior of quantum optical systems turns out to be a computational resource, not just noise.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Photonic probabilistic computing could dramatically accelerate AI workloads like Bayesian inference and restricted Boltzmann machine training by exploiting the natural randomness of optical systems rather than simulating it expensively in software.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper provides a rigorous density-matrix-level derivation linking OPO quantum dynamics to Ising Hamiltonians with nonzero Zeeman terms, deepening the theoretical foundations connecting quantum optical physics to computational complexity.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The proposed platform is experimentally viable with current OPO technology, and scaling to larger networks could enable optical solutions to NP-hard optimization problems. Full derivations and simulation results are in the paper: [arXiv:2406.04000](https://arxiv.org/abs/2406.04000)</span></div></div>
</div>
