---
abstract: We present the first joint-likelihood analysis of Big Bang Nucleosynthesis
  (BBN) and Cosmic Microwave Background (CMB) data. Bayesian inference is performed
  on the baryon abundance and the effective number of neutrino species, $N_{\rm eff}$,
  using a CMB Boltzmann solver in combination with LINX, a new flexible and efficient
  BBN code. We marginalize over Planck nuisance parameters and nuclear rates to find
  $N_{\rm{eff}} = 3.08_{-0.13}^{+0.13},\,2.94 _{-0.16}^{+0.16},$ or $2.98_{-0.13}^{+0.14}$,
  for three separate reaction networks. This framework enables robust testing of the
  Lambda Cold Dark Matter paradigm and its variants with CMB and BBN data.
arxivId: '2408.14531'
arxivUrl: https://arxiv.org/abs/2408.14531
authors:
- Cara Giovanetti
- Mariangela Lisanti
- Hongwan Liu
- Siddharth Mishra-Sharma
- Joshua T. Ruderman
concepts:
- cosmic microwave background
- bayesian inference
- big bang nucleosynthesis
- joint likelihood analysis
- monte carlo methods
- posterior estimation
- uncertainty quantification
- nuclear rate marginalization
- simulation-based inference
- neutrino detection
- dark matter
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2408_14531/figure_1.png
- /iaifi-research-blog/figures/2408_14531/figure_1.png
- /iaifi-research-blog/figures/2408_14531/figure_2.png
- /iaifi-research-blog/figures/2408_14531/figure_2.png
- /iaifi-research-blog/figures/2408_14531/figure_3.png
- /iaifi-research-blog/figures/2408_14531/figure_3.png
pdfUrl: https://arxiv.org/pdf/2408.14531v2
published: '2024-08-26T18:00:00+00:00'
theme: Astrophysics
title: Cosmological Parameter Estimation with a Joint-Likelihood Analysis of the Cosmic
  Microwave Background and Big Bang Nucleosynthesis
wordCount: 955
---

## The Big Picture

Imagine trying to read the history of the universe from two ancient manuscripts — one dating to 380,000 years after the Big Bang, the other to its first three minutes. Scientists have had both for decades. But they've never truly read them together, letting each inform the other. That's the gap this research closes.

The two "manuscripts" are the **Cosmic Microwave Background** (CMB) — radiation that filled the universe when it first became transparent, like light escaping a fog — and **Big Bang Nucleosynthesis** (BBN), the process by which protons and neutrons fused into the first light elements in the universe's opening three minutes. Those elements include helium and deuterium, a heavy hydrogen isotope carrying an extra neutron. Both encode complementary information about the infant cosmos: how much ordinary matter exists, and how many types of particles were present.

Combining them rigorously has always meant compromises — either ignoring uncertainties in nuclear reaction rates, or treating the CMB as a rough guide rather than a precisely measured dataset.

A team of physicists has now built the first complete joint analysis of BBN and CMB data, simultaneously varying every relevant parameter — cosmological, experimental, and nuclear — in a single coherent statistical framework.

> **Key Insight:** By treating BBN and CMB as a unified dataset for the first time, this analysis accounts for correlated uncertainties no previous study could capture, producing the most self-consistent constraints yet on fundamental cosmological parameters.

## How It Works

The central quantity is **N_eff**, the effective number of neutrino species — a sensitive thermometer for the early universe. The Standard Model of particle physics (the reigning theory of all known particles and forces) predicts N_eff = 3.044, corresponding to the three known neutrino types. Any deviation would signal new physics: extra light particles, unexpected interactions, or exotic energy sources in the primordial plasma. Both CMB and BBN are sensitive to N_eff, but in subtly different ways — exactly why combining them is powerful.

The key enabler is **LINX** (Light Isotope Nucleosynthesis with JAX), a new BBN code built on Google's JAX framework. JAX compiles and GPU-accelerates the calculation, making it fast enough to pair with **Markov-Chain Monte Carlo** (MCMC) samplers — statistical algorithms that map the space of possible parameter values by taking millions of guided random steps. Previous BBN codes were too slow for high-dimensional parameter exploration or couldn't vary nuclear reaction rates on the fly. LINX solves both problems.

![Figure 1](/iaifi-research-blog/figures/2408_14531/figure_1.png)

The pipeline works in three stages:

1. **BBN likelihood:** LINX computes predicted primordial abundances of helium-4 (Y_P, the fraction of ordinary matter ending up as helium) and deuterium (D/H) for given values of the baryon density Ω_b h² and N_eff, while simultaneously varying nuclear reaction rate nuisance parameters — small corrections for imprecisely known rates, modeled as log-normally distributed. Mean values and uncertainties are drawn from three published reaction networks: PRIMAT, PArthENoPE, and YOF.

2. **CMB likelihood:** The Boltzmann code CLASS — software simulating how photons and matter evolved in the early universe — computes the CMB power spectrum, a map of temperature fluctuations at different angular scales. Crucially, instead of pulling Y_P from a pre-computed table (standard practice), it fetches the prediction directly from LINX at each MCMC step, ensuring the helium fraction is always consistent with the current Ω_b h² and N_eff.

3. **Joint sampling:** The MCMC sampler varies cosmological parameters, all Planck satellite calibration nuisance parameters, and all BBN nuclear rate nuisance parameters simultaneously, computing the combined likelihood at each step.

![Figure 2](/iaifi-research-blog/figures/2408_14531/figure_1.png)

The results across three reaction networks: **N_eff = 3.08 ± 0.13**, **2.94 ± 0.16**, and **2.98 ± 0.13** — all consistent with the Standard Model prediction of 3.044. The spread across networks reflects genuine theoretical uncertainty in nuclear rates, something previous analyses couldn't honestly propagate. The baryon density Ω_b h² is pinned at roughly the 1% level, consistent between BBN-only and CMB+BBN runs.

![Figure 3](/iaifi-research-blog/figures/2408_14531/figure_2.png)

## Why It Matters

The **ΛCDM model** — our standard cosmological framework built on cold dark matter and a cosmological constant — has survived every precision test thrown at it for decades. But tests are only as trustworthy as the analysis frameworks behind them. If BBN and CMB have been analyzed without fully accounting for their interconnections, subtle inconsistencies could go undetected — or appear where none exist.

This framework changes that. Future extensions could incorporate next-generation CMB experiments like the Simons Observatory or CMB-S4, additional light element observations, or new physics scenarios such as sterile neutrinos and early dark energy. LINX's modular design makes swapping in alternative reaction networks or cosmological models straightforward. Physicists hunting for cracks in ΛCDM now have a more honest toolset.

![Figure 5](/iaifi-research-blog/figures/2408_14531/figure_3.png)

> **Bottom Line:** This is the first analysis that truly unifies the two earliest probes of the cosmos into a single coherent inference — confirming the Standard Model while building the statistical machinery needed to test what lies beyond it.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work exemplifies AI-physics integration: LINX is built on JAX, a machine-learning-era automatic differentiation framework, enabling Bayesian inference at scales that were computationally prohibitive with traditional physics codes.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Using JAX for a compiled, differentiable nuclear astrophysics solver demonstrates how ML infrastructure can accelerate scientific simulation far beyond its original domain, opening pathways for gradient-based inference throughout cosmology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By jointly constraining N_eff and baryon density with full nuclear rate marginalization, this analysis sets the most rigorous limits yet on non-standard neutrino physics and exotic light particles in the early universe.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend this framework to next-generation CMB surveys and alternative cosmological models; the paper and LINX code are available on arXiv (MIT-CTP/5737).</span></div></div>
</div>
