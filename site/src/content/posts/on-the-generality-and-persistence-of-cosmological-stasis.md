---
abstract: Hierarchical decays of $N$ matter species to radiation may balance against
  Hubble expansion to yield stasis, a new phase of cosmological evolution with constant
  matter and radiation abundances. We analyze stasis with various machine learning
  techniques on the full $2N$-dimensional space of decay rates and abundances, which
  serve as inputs to the system of Boltzmann equations that governs the dynamics.
  We construct a differentiable Boltzmann solver to maximize the number of stasis
  $e$-folds $\mathcal{N}$. High-stasis configurations obtained by gradient ascent
  motivate log-uniform distributions on rates and abundances to accompany power-law
  distributions of previous works. We demonstrate that random configurations drawn
  from these families of distributions regularly exhibit many $e$-folds of stasis.
  We additionally use them as priors in a Bayesian analysis conditioned on stasis,
  using stochastic variational inference with normalizing flows to model the posterior.
  All three numerical analyses demonstrate the generality of stasis and point to a
  new model in which the rates and abundances are exponential in the species index.
  We show that the exponential model solves the exact stasis equations, is an attractor,
  and satisfies $\mathcal{N}\propto N$, exhibiting inflation-level $e$-folding with
  a relatively low number of species. This is contrasted with the $\mathcal{N}\propto
  \log(N)$ scaling of power-law models. Finally, we discuss implications for the emergent
  string conjecture and string axiverse.
arxivId: '2408.00835'
arxivUrl: https://arxiv.org/abs/2408.00835
authors:
- James Halverson
- Sneh Pandya
concepts:
- cosmological stasis
- normalizing flows
- bayesian inference
- differentiable boltzmann solver
- posterior estimation
- simulation-based inference
- string theory
- density estimation
- monte carlo methods
- dark energy
- effective field theory
- stochastic processes
figures:
- /iaifi-research-blog/figures/2408_00835/figure_1.png
- /iaifi-research-blog/figures/2408_00835/figure_1.png
- /iaifi-research-blog/figures/2408_00835/figure_2.png
- /iaifi-research-blog/figures/2408_00835/figure_2.png
- /iaifi-research-blog/figures/2408_00835/figure_3.png
- /iaifi-research-blog/figures/2408_00835/figure_3.png
pdfUrl: https://arxiv.org/pdf/2408.00835v3
published: '2024-08-01T18:00:03+00:00'
theme: Astrophysics
title: On the Generality and Persistence of Cosmological Stasis
wordCount: 1103
---

## The Big Picture

Imagine the universe as a giant balancing act. As the cosmos expands, different forms of energy — matter, radiation, dark energy — thin out and fade at different rates. Matter dilutes faster than radiation; radiation fades faster than dark energy. The standard story of cosmic evolution is one of constant change, with each component's share of the total energy budget shifting relentlessly over time.

But what if the universe could get stuck? What if matter and radiation could lock into a cosmic standoff, each holding its ground against the relentless thinning of expansion?

That's the premise of **cosmological stasis**, a surprising phase of cosmic evolution first proposed just a few years ago. In stasis, a sequence of unstable matter particles — arranged in a hierarchy from heaviest to lightest — decay one after another into radiation. The rate of those decays balances almost exactly against the universe's expansion, which would otherwise dilute everything away.

The result: a universe that, for an extended stretch, looks frozen in terms of its energy composition. Matter holds its share. Radiation holds its share. Everything freezes — not in temperature, but in *ratio*.

Now, James Halverson and Sneh Pandya at Northeastern University have used a battery of machine learning tools to ask how easy stasis actually is to achieve. Their answer is striking — stasis is not a fragile fluke but a remarkably robust phenomenon, and a newly discovered **exponential model** can sustain it for durations rivaling cosmic inflation, the brief but extraordinarily rapid expansion believed to have occurred in the universe's first split second.

> **Key Insight:** Cosmological stasis — where matter and radiation abundances remain constant during cosmic expansion — turns out to be surprisingly generic, and a new exponential model of particle decay rates achieves far longer stasis than previously known, scaling linearly with the number of species rather than logarithmically.

## How It Works

The stasis system is governed by **Boltzmann equations** — coupled differential equations, meaning equations all linked together, each tracking how the energy carried by one particle species changes over time while influencing the others. With N species, each carrying an initial abundance Ω_ℓ and a decay rate Γ_ℓ, the full parameter space is 2N-dimensional. Previous work studied specific 8-parameter "power-law" models. Halverson and Pandya wanted to explore the full space — and for that, they needed machine learning.

Their first tool: a **differentiable Boltzmann solver**, a numerical simulation engine built using PyTorch that calculates exactly how changing any input parameter affects the output. This differentiable property enabled **gradient ascent** — essentially asking: "Given the current configuration, which direction should I nudge the parameters to maximize stasis *e*-folds?" An *e*-fold measures how much the universe expands by a factor of *e* ≈ 2.718; more *e*-folds means longer stasis.

![Figure 1](/iaifi-research-blog/figures/2408_00835/figure_1.png)

The optimized configurations didn't look like power-law distributions. They looked *exponential* — rates and abundances spaced geometrically, spanning many orders of magnitude. This pointed to a new family: **log-uniform distributions**, where the logarithm of each parameter is drawn uniformly at random, equally likely to produce a value in the range 1–10 as in 10–100 or 100–1,000.

The team then ran three complementary analyses:

1. **Random sampling**: Drawing rates and abundances from both log-uniform and power-law distributions showed stasis occurs *generically*, with log-uniform distributions consistently yielding longer stasis epochs.
2. **Bayesian inference with normalizing flows**: Using **normalizing flows** — neural networks that warp simple probability distributions into complex ones, trained via **stochastic variational inference** (a method that adjusts the network by sampling random batches of configurations) — they mapped which corners of parameter space produce the most robust stasis. The posteriors consistently pointed toward exponential structure.
3. **Direct analysis of the exponential model**: Armed with the ML-motivated insight, they proved the exponential model exactly solves the stasis equations, demonstrated it's an **attractor** (nearby configurations evolve toward it), and showed its stasis duration scales as *e*-folds ∝ N — *linearly* in the number of species.

![Figure 3](/iaifi-research-blog/figures/2408_00835/figure_2.png)

That last point is crucial. Previous power-law models showed duration ∝ log(N): doubling the species count adds only marginally more stasis. The exponential model blows past this — double the species, double the stasis duration. With a few hundred species, you can match the *e*-folding count of cosmic inflation.

![Figure 5](/iaifi-research-blog/figures/2408_00835/figure_3.png)

## Why It Matters

The physics implications reach all the way to string theory. String theory generically predicts **towers of particles** — Kaluza-Klein states from extra dimensions, strings with different excitation levels, axions from the "string axiverse." These are exactly the hierarchical matter species that stasis requires.

The **emergent string conjecture**, which characterizes which field-theory limits of string theory are consistent with quantum gravity, predicts specific patterns of tower spacings — and the exponential model maps naturally onto these patterns. If stasis occurred in the early universe, it could leave observable imprints on the cosmic microwave background or the spectrum of gravitational waves.

The machine learning methodology is itself worth noting. The differentiable Boltzmann solver is a general tool: any system of ODEs describing early-universe dynamics could be optimized this way. Normalizing flows applied to Boltzmann equations offer a new route to physics discovery — letting gradient-based optimization and flexible posterior modeling explore high-dimensional parameter spaces that would defeat brute-force search. This paper shows that "ML for physics" isn't just about replacing simulations with neural networks; it's about using ML to *discover* analytic models that humans might not have written down otherwise.

> **Bottom Line:** Cosmological stasis is not a fine-tuned accident — it's a robust feature of universes with towers of decaying species, and the newly identified exponential model achieves stasis durations that rival inflation, with profound implications for string theory and early-universe cosmology.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly applies modern machine learning tools — differentiable programming, normalizing flows, and stochastic variational inference — to solve a fundamental open question in early-universe cosmology, exemplifying IAIFI's mission to bridge AI and physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper demonstrates a generalizable workflow for physics discovery: differentiable ODE solvers enable gradient-based optimization of physical parameters, while normalizing flows model complex high-dimensional posteriors that encode physical constraints.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The discovery of the exponential stasis model, with its linear *e*-folding scaling, opens a new class of cosmological histories compatible with — and motivated by — string theory's tower structures and the emergent string conjecture.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will explore connections to specific string compactifications, observational signatures in gravitational wave backgrounds, and the viability of stasis after Big Bang nucleosynthesis; the full paper and code are available at arXiv and github.com/snehjp2/diff-stasis.</span></div></div>
</div>
