---
abstract: We introduce LINX (Light Isotope Nucleosynthesis with JAX), a new differentiable
  public Big Bang Nucleosynthesis (BBN) code designed for fast parameter estimation.
  By leveraging JAX, LINX achieves both speed and differentiability, enabling the
  use of Bayesian inference, including gradient-based methods. We discuss the formalism
  used in LINX for rapid primordial elemental abundance predictions and give examples
  of how LINX can be used. When combined with differentiable Cosmic Microwave Background
  (CMB) power spectrum emulators, LINX can be used for joint CMB and BBN analyses
  without requiring extensive computational resources, including on personal hardware.
arxivId: '2408.14538'
arxivUrl: https://arxiv.org/abs/2408.14538
authors:
- Cara Giovanetti
- Mariangela Lisanti
- Hongwan Liu
- Siddharth Mishra-Sharma
- Joshua T. Ruderman
concepts:
- primordial nucleosynthesis
- differentiable bbn
- bayesian inference
- cosmic microwave background
- monte carlo methods
- posterior estimation
- simulation-based inference
- emulation
- surrogate modeling
- scalability
- neutrino detection
- dark matter
figures:
- /iaifi-research-blog/figures/2408_14538/figure_1.png
- /iaifi-research-blog/figures/2408_14538/figure_1.png
- /iaifi-research-blog/figures/2408_14538/figure_2.png
- /iaifi-research-blog/figures/2408_14538/figure_2.png
- /iaifi-research-blog/figures/2408_14538/figure_3.png
- /iaifi-research-blog/figures/2408_14538/figure_3.png
pdfUrl: https://arxiv.org/pdf/2408.14538v2
published: '2024-08-26T18:00:02+00:00'
theme: Astrophysics
title: 'LINX: A Fast, Differentiable, and Extensible Big Bang Nucleosynthesis Package'
wordCount: 1038
---

## The Big Picture

In the first few minutes after the Big Bang, the universe was a cosmic pressure cooker — temperatures in the billions of degrees, protons and neutrons smashing together to forge the lightest elements: hydrogen, helium, lithium. This process, **Big Bang Nucleosynthesis (BBN)**, left a chemical fingerprint that scientists can still read today by measuring elemental abundances in ancient, pristine gas clouds billions of light-years away. The agreement between theory and observation is one of the great triumphs of modern cosmology.

But computing those predictions accurately — and fast enough to be useful — has been a persistent bottleneck. Cosmologists need to run BBN codes millions of times to fit models to data, testing vast combinations of physical parameters and hunting for new physics hiding in a slight mismatch between predicted and observed helium abundance.

Existing tools work, but weren't built for the modern era of precision cosmology. They're slow. They lack *differentiability* — the ability to compute how outputs respond to small changes in inputs — which is required to unlock far more powerful statistical methods. And they resist integration into the sophisticated analysis workflows now standard elsewhere in cosmology.

A team led by researchers at NYU, Princeton, MIT, and IAIFI has built a new BBN code from scratch, one that speaks the language of modern machine learning. **LINX** (Light Isotope Nucleosynthesis with JAX) is fast, fully differentiable, and designed to slot seamlessly into gradient-powered inference pipelines.

> **Key Insight:** LINX brings Big Bang Nucleosynthesis into the era of differentiable programming, enabling gradient-based Bayesian inference for the first time and making joint CMB+BBN analyses tractable on a laptop.

## How It Works

The core innovation in LINX is its foundation in **JAX**, Google's numerical computing library that compiles Python to fast machine instructions and — crucially — can automatically compute derivatives of any function. This isn't just a software engineering detail; it transforms how cosmologists can work.

![Figure 1](/iaifi-research-blog/figures/2408_14538/figure_1.png)

Traditional BBN codes solve a coupled system of **nuclear reaction network equations** — differential equations tracking how abundances of hydrogen, deuterium, helium-3, helium-4, lithium-7, and other light isotopes evolve as the universe cools. LINX implements the same physics with an architecture that keeps every step differentiable end-to-end:

1. **Thermodynamic background**: LINX computes how temperature, energy density, and expansion rate evolve in the early universe — the stage on which nucleosynthesis plays out — including contributions from photons, electrons, positrons, and neutrinos, with precision inputs from the code `nudecBSM`.
2. **Weak reaction rates**: The neutron-to-proton ratio — a key input to element formation — is set by weak interactions (responsible for certain types of radioactive decay) in the first seconds. LINX computes these rates using a mathematical technique that dramatically speeds up the calculation without sacrificing accuracy.
3. **Nuclear network integration**: Using JAX's equation-solving tools, LINX integrates the full reaction network forward in time, tracking isotope abundances from ~10 MeV down to ~10 keV (energy units serving as a proxy for the universe's temperature) until abundances freeze out — reaching their final values.
4. **Likelihood evaluation**: Predicted abundances are compared directly to observations and combined with cosmic microwave background data for joint statistical analysis.

Differentiability means users can compute *gradients* — precise measures of how final elemental abundances respond to any change in the inputs — analytically rather than numerically. Those inputs can be anything: baryon density, neutrino count, nuclear reaction rates, or exotic new-physics parameters.

This unlocks **Hamiltonian Monte Carlo (HMC)** and **variational inference** — gradient-based statistical methods that navigate parameter space by following mathematical slopes rather than wandering randomly. They are exponentially more efficient than the traditional random-walk samplers BBN codes have historically been stuck with.

![Figure 3](/iaifi-research-blog/figures/2408_14538/figure_2.png)

In validation tests, LINX matches the established code PRIMAT to better than 0.1% for helium-4 abundance and within a few percent for deuterium and lithium-7 — well within current observational uncertainties. A single evaluation takes milliseconds on a standard laptop; after JIT compilation, full parameter scans run orders of magnitude faster than comparable legacy codes.

## Why It Matters

Cosmology is entering a golden age of precision. Experiments like the Simons Observatory and CMB-S4 will deliver exquisite measurements of the cosmic microwave background that demand equally precise theoretical predictions. The angular pattern of temperature fluctuations in the CMB depends on the primordial helium abundance — which a BBN code must compute before a CMB simulation code can even begin. BBN is a critical bottleneck in the analysis pipelines for these next-generation experiments.

![Figure 5](/iaifi-research-blog/figures/2408_14538/figure_3.png)

LINX dissolves that bottleneck. Combining LINX with differentiable CMB emulators like CosmoPower, the team demonstrates a fully-differentiable joint CMB+BBN pipeline that constrains the baryon density and effective number of neutrino species simultaneously — on personal hardware, no supercomputer required. This opens the door to richer searches for new physics: light dark matter species, non-standard neutrino interactions, exotic particle decays during BBN — analyses that previously required weeks of cluster time.

LINX is also built to grow. Written in high-level Python with JAX, adding new physics — say, a particle species that injects entropy during nucleosynthesis — means modifying a few Python functions, not rewriting Fortran from scratch.

> **Bottom Line:** LINX makes the cosmic chemical record of the Big Bang more accessible to precision analysis than ever before, bringing the full toolkit of modern machine learning to bear on one of cosmology's oldest and most powerful observational probes.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">LINX directly applies differentiable programming techniques from modern AI infrastructure (JAX) to Big Bang Nucleosynthesis, enabling gradient-based inference methods that were previously unavailable to BBN analyses.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work establishes a concrete template for integrating JAX-based differentiable physics simulators with probabilistic inference tools like HMC and variational inference — a pattern applicable across simulation-based inference problems in physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">LINX enables self-consistent joint constraints on early-universe cosmological parameters from BBN and CMB data simultaneously, sharpening tests of the Standard Model and sensitivity to new physics from the first minutes of cosmic time.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend LINX to a broader range of new-physics scenarios and integration with next-generation CMB experiments; the code and companion analysis paper are available at arXiv (MIT-CTP/5736) and at https://github.com/cgiovanetti/LINX.</span></div></div>
</div>
