---
abstract: Large-time correlation functions have a pivotal role in extracting particle
  masses from Euclidean lattice field theory calculations, however little is known
  about the statistical properties of these quantities. In this work, the asymptotic
  form of the distributions of the correlation functions at vanishing momentum is
  determined for bosonic interacting lattice field theories with a unique gapped vacuum.
  It is demonstrated that the deviations from the asymptotic form at large Euclidean
  times can be utilized to determine the spectrum of the theory.
arxivId: '2210.15789'
arxivUrl: https://arxiv.org/abs/2210.15789
authors:
- Cagin Yunus
- William Detmold
concepts:
- quantum field theory
- correlation function distributions
- signal-to-noise problem
- lattice qcd
- stochastic processes
- monte carlo methods
- uncertainty quantification
- spectral methods
- eigenvalue decomposition
- effective field theory
figures:
- /iaifi-research-blog/figures/2210_15789/figure_1.png
- /iaifi-research-blog/figures/2210_15789/figure_1.png
- /iaifi-research-blog/figures/2210_15789/figure_2.png
- /iaifi-research-blog/figures/2210_15789/figure_2.png
- /iaifi-research-blog/figures/2210_15789/figure_3.png
- /iaifi-research-blog/figures/2210_15789/figure_3.png
pdfUrl: https://arxiv.org/pdf/2210.15789v2
published: '2022-10-27T22:19:08+00:00'
theme: Theoretical Physics
title: Large-time correlation functions in bosonic lattice field theories
wordCount: 1067
---

## The Big Picture

Imagine trying to measure the weight of a single grain of sand on a beach — using only a bathroom scale buried under an avalanche of noise. That's roughly the challenge physicists face when extracting particle masses from **lattice quantum field theory** (LQFT) — a technique that models the subatomic world on a discrete mathematical grid, and the most powerful numerical method we have for studying strongly interacting particles like protons and neutrons. The deeper you probe, the more the signal drowns in statistical noise.

To find the mass of a particle, physicists compute **correlation functions** — measurements that track how a disturbance in a quantum field at one point in spacetime influences the field at another point, much later. A **quantum field** is an invisible quantity filling all of space, like temperature but governed by quantum rules; a correlation function is essentially a measure of how long the "memory" of a disturbance persists.

At long times, the correlation function decays exponentially toward the particle mass. But statistical noise decays more *slowly* than the signal, causing the signal-to-noise ratio to collapse exponentially. This mismatch — the **Parisi-Lepage problem**, named for the physicists who first described it in the 1980s — has plagued lattice calculations for decades.

Now, MIT physicists Cagin Yunus and William Detmold have done something deceptively simple: they figured out exactly *what kind of statistical animal* these long-time correlation functions actually are. By deriving the full probability distribution of correlation functions at large times, they've turned an empirical headache into a tool that can itself reveal the **particle spectrum** — the catalogue of all particles and their masses in the theory.

> **Key Insight:** The statistical fluctuations in lattice correlation functions aren't just noise to be beaten down — their precise mathematical form encodes physical information about the energy spectrum of the theory.

## How It Works

The researchers began in the simplest possible setting: a **free real scalar field theory** on a lattice. A scalar field is the simplest type of quantum field — a number assigned to every point in spacetime, like temperature in a room, but quantum mechanical. In this controlled sandbox, they computed the **characteristic function** of the correlation function's probability distribution — a mathematical transform that completely characterizes the shape of the distribution.

The key result is elegant. The correlation function $C(t) = \phi(t)\phi(0)$ turns out to follow a distribution determined by just two parameters, $\omega_+$ and $\omega_-$, derived from the inverse of the lattice operator. These parameters are directly tied to the particle masses in the theory.

![Figure 1](/iaifi-research-blog/figures/2210_15789/figure_1.png)

The distribution takes the form of a **modified Bessel function** — a classical mathematical function that precisely characterizes how correlation function values are spread around their average. The real payoff comes at *large* times: as $t \to \infty$, the distribution approaches an asymptotic form, and the *deviations* from that form are controlled by exponentials carrying information about excited states — the heavier particles sitting above the ground state.

The argument extends to the **interacting case** through a chain of reasoning:

- At large enough times, the dominant path-integral contribution comes from the lightest state overlapping with the operator
- The interacting theory's correlation function maps onto an effective free-field description at large times
- Deviations from the asymptotic form are suppressed by factors of $e^{-(m_1 - m_0)t}$, where $m_0$ and $m_1$ are the ground and first excited state masses

![Figure 2](/iaifi-research-blog/figures/2210_15789/figure_1.png)

By analyzing *how* an empirical distribution deviates from the predicted asymptotic form, one can read off the **mass gap** — the difference between the ground state and first excited state masses.

![Figure 3](/iaifi-research-blog/figures/2210_15789/figure_2.png)

The paper grounds this in a concrete lattice discretization using the standard Klein-Gordon operator, deriving exact expressions for the distribution parameters in terms of the bare lattice mass and coupling. At any finite time, the distribution can be computed analytically, and the approach to the asymptotic form tracked precisely.

## Why It Matters

The implications reach into the heart of nuclear and particle physics. **Lattice QCD** — the numerical study of the strong nuclear force — relies on extracting particle masses from exactly these exponentially decaying correlation functions. The Parisi-Lepage noise problem has long forced practitioners to either accept large statistical errors or hunt for clever variance-reduction tricks. This work offers something different: a principled statistical framework that says, here is exactly what the distribution *should* look like, and here is what departures from that form are telling you.

In practice, physicists collect thousands of **Monte Carlo samples** — independent snapshots of the quantum system generated by a random-sampling algorithm — of correlation functions. Checking whether those samples behaved as expected previously required rough heuristics or expensive bootstrap resampling. The analytical distributions derived here provide exact predictions against which empirical samples can be tested, revealing whether a calculation has reached the asymptotic regime or is still contaminated by excited-state contributions.

![Figure 4](/iaifi-research-blog/figures/2210_15789/figure_2.png)

The connection to machine learning is tantalizing. Modern lattice calculations increasingly deploy **normalizing flows** — generative models that learn to sample from complex probability distributions — to improve Monte Carlo efficiency. Knowing the precise statistical structure of the target distributions could inform better generative model design, improving sampling efficiency precisely where noise is hardest to control.

> **Bottom Line:** By deriving the exact probability distributions of large-time lattice correlation functions, Yunus and Detmold transform the notorious signal-to-noise problem from a statistical obstacle into a diagnostic tool — one that extracts particle masses from the shape of the fluctuations themselves.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses rigorous probability theory with non-perturbative quantum field theory, using characteristic function techniques to characterize the noise structure of nuclear physics calculations — a genuine bridge between mathematical disciplines.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The derived analytical distributions provide exact benchmarks for machine learning methods in lattice QFT, enabling principled evaluation of normalizing flows and generative models used to accelerate Monte Carlo sampling in strongly-coupled theories.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Lattice QCD practitioners gain a new analytical handle on the signal-to-noise problem — both as a statistical diagnostic for simulation quality and as a spectroscopy method that reads mass gaps directly from distributional deviations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend these results to fermionic theories and multi-hadron systems, where the Parisi-Lepage problem is most severe; the paper is available on arXiv (MIT-CTP-5465) by Cagin Yunus and William Detmold.</span></div></div>
</div>
