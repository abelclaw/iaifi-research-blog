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
pdfUrl: https://arxiv.org/pdf/2408.14531v2
published: '2024-08-26T18:00:00+00:00'
theme: Astrophysics
title: Cosmological Parameter Estimation with a Joint-Likelihood Analysis of the Cosmic
  Microwave Background and Big Bang Nucleosynthesis
wordCount: 1093
---

## The Big Picture

Imagine trying to read the history of the universe from two ancient manuscripts, one dating to 380,000 years after the Big Bang, the other to its first three minutes. Scientists have had both for decades. They've never truly read them together, letting each inform the other. That's what this research finally does.

The two "manuscripts" are the **Cosmic Microwave Background** (CMB), radiation that filled the universe when it first became transparent, like light escaping a fog, and **Big Bang Nucleosynthesis** (BBN), the process by which protons and neutrons fused into the first light elements during the universe's opening three minutes. Those elements include helium and deuterium, a heavy hydrogen isotope carrying an extra neutron. Both encode complementary information about the infant cosmos: how much ordinary matter exists and how many types of particles were present.

Combining them rigorously has always meant compromises. Either you ignore uncertainties in nuclear reaction rates, or you treat the CMB as a rough guide rather than the precisely measured dataset it actually is.

A team of physicists has now built the first complete joint analysis of BBN and CMB data, simultaneously varying every relevant parameter (cosmological, experimental, and nuclear) in a single coherent statistical framework.

> **Key Insight:** By treating BBN and CMB as a unified dataset for the first time, this analysis accounts for correlated uncertainties that no previous study could capture, producing the most self-consistent constraints yet on fundamental cosmological parameters.

## How It Works

The central quantity is **N_eff**, the effective number of neutrino species, which acts as a sensitive thermometer for the early universe. The Standard Model of particle physics predicts N_eff = 3.044, corresponding to the three known neutrino types. Any deviation would signal new physics: extra light particles, unexpected interactions, or exotic energy sources in the primordial plasma. Both CMB and BBN respond to N_eff, but in subtly different ways, which is precisely why combining them has real teeth.

What made this possible is **LINX** (Light Isotope Nucleosynthesis with JAX), a new BBN code built on Google's JAX framework. JAX compiles and GPU-accelerates the calculation, making it fast enough to pair with **Markov-Chain Monte Carlo** (MCMC) samplers, statistical algorithms that map the space of possible parameter values by taking millions of guided random steps. Previous BBN codes were too slow for high-dimensional parameter exploration or couldn't vary nuclear reaction rates on the fly. LINX solves both problems.

![Figure 1](/iaifi-research-blog/figures/2408_14531/figure_1.png)

The pipeline works in three stages:

1. **BBN likelihood:** LINX computes predicted primordial abundances of helium-4 (Y_P, the fraction of ordinary matter ending up as helium) and deuterium (D/H) for given values of the baryon density Ω_b h² and N_eff. It simultaneously varies nuclear reaction rate nuisance parameters, small corrections for imprecisely known rates modeled as log-normal distributions. Mean values and uncertainties come from three published reaction networks: PRIMAT, PArthENoPE, and YOF.

2. **CMB likelihood:** The Boltzmann code CLASS, software simulating how photons and matter evolved in the early universe, computes the CMB power spectrum: a map of temperature fluctuations at different angular scales. Instead of pulling Y_P from a pre-computed table (standard practice), it fetches the prediction directly from LINX at each MCMC step. This ensures the helium fraction always stays consistent with the current Ω_b h² and N_eff.

3. **Joint sampling:** The MCMC sampler varies cosmological parameters, all Planck satellite calibration nuisance parameters, and all BBN nuclear rate nuisance parameters simultaneously, computing the combined likelihood at each step.

![Figure 2](/iaifi-research-blog/figures/2408_14531/figure_1.png)

The results across three reaction networks: N_eff = 3.08 ± 0.13, 2.94 ± 0.16, and 2.98 +0.14/−0.13. All three are consistent with the Standard Model prediction of 3.044. The spread across networks reflects genuine theoretical uncertainty in nuclear rates, something previous analyses couldn't honestly propagate. The baryon density Ω_b h² is pinned at roughly the 1% level, consistent between BBN-only and CMB+BBN runs.

![Figure 3](/iaifi-research-blog/figures/2408_14531/figure_2.png)

## Why It Matters

The **ΛCDM model**, our standard cosmological framework built on cold dark matter and a cosmological constant, has survived every precision test thrown at it for decades. But tests are only as trustworthy as the analysis behind them. If BBN and CMB have been analyzed without fully accounting for their interconnections, subtle inconsistencies could go undetected, or show up where none actually exist.

This framework fixes that problem. Future extensions could incorporate next-generation CMB experiments like the Simons Observatory or CMB-S4, additional light element observations, or new physics scenarios such as sterile neutrinos and early dark energy. LINX is modular enough that swapping in alternative reaction networks or cosmological models is practical rather than painful. For physicists hunting cracks in ΛCDM, the inference toolset just got more honest.


> **Bottom Line:** This is the first analysis that truly unifies the two earliest probes of the cosmos into a single coherent inference, confirming the Standard Model while building the statistical machinery to test what lies beyond it.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits squarely at the intersection of AI and physics. LINX is built on JAX, a machine-learning-era automatic differentiation framework, and it enables Bayesian inference at scales that were computationally out of reach with traditional physics codes.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Using JAX to build a compiled, differentiable nuclear astrophysics solver shows how ML infrastructure can speed up scientific simulation well outside its original domain. The same approach could bring gradient-based inference to other corners of cosmology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By jointly constraining N_eff and baryon density with full nuclear rate marginalization, this analysis sets tight limits on non-standard neutrino physics and exotic light particles in the early universe.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend this framework to next-generation CMB surveys and alternative cosmological models. The paper and LINX code are available at [arXiv:2408.14531](https://arxiv.org/abs/2408.14531).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Cosmological Parameter Estimation with a Joint-Likelihood Analysis of the Cosmic Microwave Background and Big Bang Nucleosynthesis</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2408.14531](https://arxiv.org/abs/2408.14531)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Cara Giovanetti", "Mariangela Lisanti", "Hongwan Liu", "Siddharth Mishra-Sharma", "Joshua T. Ruderman"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We present the first joint-likelihood analysis of Big Bang Nucleosynthesis (BBN) and Cosmic Microwave Background (CMB) data. Bayesian inference is performed on the baryon abundance and the effective number of neutrino species, $N_{\rm eff}$, using a CMB Boltzmann solver in combination with LINX, a new flexible and efficient BBN code. We marginalize over Planck nuisance parameters and nuclear rates to find $N_{\rm{eff}} = 3.08_{-0.13}^{+0.13},\,2.94 _{-0.16}^{+0.16},$ or $2.98_{-0.13}^{+0.14}$, for three separate reaction networks. This framework enables robust testing of the Lambda Cold Dark Matter paradigm and its variants with CMB and BBN data.</span></div></div>
</div>
