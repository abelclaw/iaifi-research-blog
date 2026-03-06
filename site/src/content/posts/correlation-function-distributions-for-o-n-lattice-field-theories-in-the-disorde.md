---
abstract: Numerical computations in strongly-interacting quantum field theories are
  often performed using Monte-Carlo sampling methods. A key task in these calculations
  is to estimate the value of a given physical quantity from the distribution of stochastic
  samples that are generated using the Monte-Carlo method. Typically, the sample mean
  and sample variance are used to define the expectation values and uncertainties
  of computed quantities. However, the Monte-Carlo sample distribution contains more
  information than these basic properties and it is useful to investigate it more
  generally. In this work, the exact form of the probability distributions of two-point
  correlation functions at zero momentum in O(N) lattice field theories in the disordered
  phase and in infinite volume are determined. These distributions allow for a robust
  investigation of the efficacy of the Monte-Carlo sampling procedure and are shown
  also to allow for improved estimators of the target physical quantity to be constructed.
  The theoretical expectations are shown to agree with numerical calculations in the
  O(2) model.
arxivId: '2304.03820'
arxivUrl: https://arxiv.org/abs/2304.03820
authors:
- Cagin Yunus
- William Detmold
concepts:
- correlation function pdf
- monte carlo methods
- quantum field theory
- lattice gauge theory
- stochastic processes
- uncertainty quantification
- improved estimators
- phase transitions
- signal detection
- symmetry breaking
- goodness-of-fit testing
- bayesian inference
figures:
- /iaifi-research-blog/figures/2304_03820/figure_1.png
- /iaifi-research-blog/figures/2304_03820/figure_2.png
- /iaifi-research-blog/figures/2304_03820/figure_3.png
pdfUrl: https://arxiv.org/pdf/2304.03820v1
published: '2023-04-07T19:25:18+00:00'
theme: Theoretical Physics
title: Correlation function distributions for O(N) lattice field theories in the disordered
  phase
wordCount: 1066
---

## The Big Picture

Imagine measuring the weight of a single atom by weighing millions of atoms and dividing by the count. That works — but what if a few extraordinarily heavy outliers dominate your measurement? Averaging alone misleads you. You'd want to know the *shape* of the weight distribution to extract the best estimate.

This is precisely the problem physicists face computing properties of **quantum field theories** — the mathematical frameworks describing fundamental particles and forces, from quarks inside protons to phase transitions in materials. These theories resist exact solutions, so the standard approach is **Monte Carlo sampling**: draw thousands of random snapshots of the quantum system and average them.

Statistical fluctuations are enormous. The signal — say, a particle mass — drowns in noise that grows exponentially with distance. Physicists typically extract just two numbers from their data: the sample mean and variance. Those samples encode far more information than anyone has been using.

A new paper from MIT researchers Cagin Yunus and William Detmold changes this. They derive, analytically and exactly, the full probability distributions of **two-point correlation functions** — measures of how strongly two field values, separated in time, are correlated — for an important class of models called **O(N) field theories**. They then use those distributions to build better measurement tools.

> **Key Insight:** By deriving the exact probability distribution of Monte Carlo samples — not just their average — physicists can run sharper statistical tests on simulations *and* construct improved estimators that squeeze more signal from the same data.

## How It Works

The paper focuses on **O(N) lattice field theories** — models where fields have N interchangeable components, with symmetry under rotations among them (the "O" stands for orthogonal). O(1) is the Ising model of magnetism. O(2) describes superfluids. O(4) appears in electroweak symmetry breaking. Cracking the general O(N) case covers a vast swath of fundamental physics.

The central object is the **two-point correlation function**: how strongly two field measurements, separated in time, are correlated. This quantity encodes particle masses — the rate at which correlations decay with time reveals the mass of the lightest particle in the theory.

![Figure 1](/iaifi-research-blog/figures/2304_03820/figure_1.png)

The authors' strategy unfolds in four steps:

1. **Start with the free field.** For a simple non-interacting scalar field, the **path integral** — the mathematical sum over all possible field configurations — is **Gaussian** (bell-curve shaped). Integrating out all field variables except the two time slices relevant to the correlation yields an exact joint probability distribution.

2. **Compute the characteristic function.** Rather than working with the distribution directly, they calculate its **characteristic function** — a transform that converts the distribution into a more tractable form. This handles the key difficulty: a correlation function is a *product* of two field values, a nonlinear operation that resists direct treatment.

3. **Invert to get the PDF.** The resulting distributions are expressible in terms of **modified Bessel functions** — special functions that arise naturally in rotational problems. These distributions are not Gaussian; they have fat tails and asymmetric shapes that reflect the underlying physics.

4. **Extend to interacting O(N) theories.** The real achievement: this result generalizes to interacting O(N) models in the **disordered phase** — the high-temperature, symmetric phase where the field has no preferred direction. In the infinite-volume limit, the **central limit theorem** (which guarantees that averages of many independent random quantities converge to Gaussian) forces the spatially-averaged fields to become Gaussian even with interactions. The correlation function's distribution then inherits its shape from this Gaussian structure in a computable way.

![Figure 2](/iaifi-research-blog/figures/2304_03820/figure_2.png)

The authors validate everything against numerical simulations of the O(2) model in two dimensions. The match between theoretical predictions and Monte Carlo histograms is striking — high precision across a range of temporal separations and coupling strengths.

![Figure 3](/iaifi-research-blog/figures/2304_03820/figure_3.png)

## Why It Matters

The immediate payoff is practical: knowing the true distribution of your samples lets you build **improved estimators** of the correlation function's mean. The sample mean is unbiased but not optimal when the underlying distribution is non-Gaussian. Estimators built from the known probability distribution have lower variance — the same physical information from less data, or more information from the same compute budget. In a field where simulations routinely consume millions of CPU-hours, that efficiency gain is substantial.

Beyond better arithmetic, these distributions enable principled statistical diagnostics. Monte Carlo simulations can suffer from **thermalization failures** (the sampler hasn't fully explored configuration space) or **autocorrelation** (successive samples aren't truly independent). Currently, researchers check for these pathologies with heuristic methods.

A known theoretical distribution provides a rigorous null hypothesis: if your samples don't match the predicted distribution, something is wrong with your sampling. This turns a qualitative eyeball test into a quantitative, falsifiable check — exactly the kind of rigor that matters as simulations scale up in complexity and cost.

Looking forward, the framework could extend to correlation functions at nonzero spatial momentum, to observables beyond two-point functions, and to theories outside the disordered phase. The signal-to-noise problem — exponential degradation of information with particle separation — remains a central obstacle in **lattice quantum chromodynamics** (the computational framework for studying the strong nuclear force that binds quarks inside protons and neutrons). Tools that extract more signal from fixed resources bring the field closer to first-principles predictions for nuclear physics.

> **Bottom Line:** Yunus and Detmold derive the exact probability distributions of Monte Carlo samples in O(N) quantum field theories, enabling both rigorous simulation diagnostics and mathematically optimal estimators — a quiet but significant upgrade to the statistical toolkit of fundamental physics computation.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies rigorous mathematical analysis — characteristic functions, Bessel transforms, and infinite-volume limits — to sharpen the statistical machinery underlying quantum field theory simulations, directly bridging probability theory and fundamental physics computation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The improved estimators developed here exemplify how knowing a generative distribution enables more efficient inference — a principle with broad relevance to machine learning and Bayesian methods well beyond physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By characterizing the full distribution of Monte Carlo correlation function samples in O(N) models, this work provides new diagnostic and estimation tools for lattice calculations central to nuclear and particle physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions to nonzero-momentum correlators and the ordered phase could further reduce the computational cost of lattice QCD and nuclear physics calculations; the full paper is available at arXiv:2407.XXXXX (MIT-CTP-5550).</span></div></div>
</div>
