---
abstract: The DeepCore sub-detector of the IceCube Neutrino Observatory provides access
  to neutrinos with energies above approximately 5 GeV. Data taken between 2012-2021
  (3,387 days) are utilized for an atmospheric $ν_μ$ disappearance analysis that studied
  150,257 neutrino-candidate events with reconstructed energies between 5-100 GeV.
  An advanced reconstruction based on a convolutional neural network is applied, providing
  increased signal efficiency and background suppression, resulting in a measurement
  with both significantly increased statistics compared to previous DeepCore oscillation
  results and high neutrino purity. For the normal neutrino mass ordering, the atmospheric
  neutrino oscillation parameters and their 1$σ$ errors are measured to be $Δ$m$^2_{32}$
  = $2.40\substack{+0.05 \\ -0.04} \times 10^{-3} \textrm{ eV}^2$ and sin$^2$$θ_{23}$=$0.54\substack{+0.04
  \\ -0.03}$. The results are the most precise to date using atmospheric neutrinos,
  and are compatible with measurements from other neutrino detectors including long-baseline
  accelerator experiments.
arxivId: '2405.02163'
arxivUrl: https://arxiv.org/abs/2405.02163
authors:
- IceCube Collaboration
concepts:
- neutrino detection
- neutrino oscillation parameters
- convolutional networks
- event reconstruction
- classification
- monte carlo methods
- bayesian inference
- simulation-based inference
- likelihood ratio
- uncertainty quantification
- hypothesis testing
- feature extraction
figures:
- /iaifi-research-blog/figures/2405_02163/figure_1.png
- /iaifi-research-blog/figures/2405_02163/figure_1.png
- /iaifi-research-blog/figures/2405_02163/figure_2.png
pdfUrl: https://arxiv.org/pdf/2405.02163v1
published: '2024-05-03T15:09:11+00:00'
theme: Experimental Physics
title: Measurement of atmospheric neutrino oscillation parameters using convolutional
  neural networks with 9.3 years of data in IceCube DeepCore
wordCount: 1014
---

## The Big Picture

Imagine building a particle detector the size of a cubic kilometer, burying it under a mile of Antarctic ice, and using it to catch ghostly subatomic particles that pass through the entire Earth as if it weren't there. That's IceCube. Its innermost region, DeepCore, has just delivered the most precise measurement of neutrino oscillations ever made using atmospheric neutrinos, with a major assist from artificial intelligence.

Neutrinos come in three "flavors" (electron, muon, and tau) and as they travel, they quantum-mechanically morph from one flavor to another. This phenomenon, **neutrino oscillation**, was revolutionary when discovered: it proved neutrinos have mass, which the Standard Model originally said was impossible.

Two parameters govern this shape-shifting. The **mass-squared splitting** (Δm²₃₂) sets the rate of oscillation, how quickly neutrinos cycle through flavors, while the **mixing angle** (sin²θ₂₃) controls how completely the flavors blend. Pinning these numbers down is a central goal of modern particle physics.

The IceCube Collaboration has now done exactly that, combining 9.3 years of data with a convolutional neural network to produce the most precise atmospheric neutrino oscillation measurement to date.

> **Key Insight:** By deploying deep learning to reconstruct neutrino events in Antarctic ice, IceCube DeepCore has measured the fundamental parameters governing neutrino flavor change with precision that rivals dedicated long-baseline accelerator experiments.

## How It Works

The raw material is **atmospheric neutrinos**: particles born when cosmic rays slam into Earth's upper atmosphere. Muon neutrinos streaming downward arrive at IceCube nearly unaltered, while those traveling upward have traversed thousands of kilometers through Earth, enough time to oscillate into tau neutrinos. Comparing these populations lets physicists measure oscillation parameters directly.

![Figure 1](/iaifi-research-blog/figures/2405_02163/figure_1.png)

IceCube DeepCore detects neutrinos through **Cherenkov radiation**. When a neutrino interacts with ice, it produces a charged particle moving faster than light travels through ice (though not faster than light in vacuum). This generates a cone of blue photons that spreads outward and is caught by more than 5,000 optical sensors. The spatial and temporal pattern of these hits encodes the neutrino's energy, direction, and flavor.

The reconstruction challenge is steep. Three factors work against clean measurements:

- **Non-uniform ice:** Antarctic ice contains layers and bubbles that scatter photons unpredictably.
- **Sensor variation:** Individual optical sensors have different efficiencies and calibrated responses.
- **Atmospheric muon background:** Cosmic-ray showers rain muons down from above, outnumbering signal neutrinos by thousands to one before filtering.

Previous analyses used traditional likelihood-based methods, algorithms that score each event against an explicit mathematical model of the detector. This analysis instead deploys a **convolutional neural network (CNN)**, a type of deep learning originally developed for image recognition, trained to extract signal from noise far more effectively.

The CNN processes raw photon hit data directly, learning to distinguish genuine neutrino interactions from muon contamination without being told exactly what to look for. Its output feeds into an oscillation analysis comparing 150,257 neutrino-candidate events, spanning 5 to 100 GeV, against detailed **Monte Carlo simulations** across a grid of oscillation parameter values. (Monte Carlo simulations are computer-generated synthetic datasets that statistically model every step of the physics.)

![Figure 2](/iaifi-research-blog/figures/2405_02163/figure_1.png)

The results, assuming **normal neutrino mass ordering** (where the two lighter mass states are grouped together, rather than apart from the heaviest): Δm²₃₂ = 2.40 ⁺⁰·⁰⁵₋₀.₀₄ × 10⁻³ eV² and sin²θ₂₃ = 0.54 ⁺⁰·⁰⁴₋₀.₀₃. The CNN simultaneously boosted signal statistics and maintained high neutrino purity, a combination that traditional approaches typically cannot achieve without painful tradeoffs.


The value sin²θ₂₃ = 0.54 is particularly telling. Exactly 0.5 would mean muon and tau neutrinos mix with perfect symmetry, or **maximal mixing**. IceCube's result nudges above 0.5, hinting at a preference for the upper **octant** (θ₂₃ > 45°), though the uncertainty still admits maximal mixing.

## Why It Matters

Neutrino physics sits at a frontier where precision measurements can expose physics beyond the Standard Model. The parameters measured here feed directly into global fits that combine data from reactor detectors, solar neutrino experiments, and long-baseline accelerators like T2K in Japan and NOvA in the United States. IceCube's result is now consistent with these dedicated beam experiments, and it arrives from an entirely different systematic environment: real cosmic-ray neutrinos, a different detector technology, and different oscillation baselines. Agreement between methods strengthens the oscillation picture. Disagreement would be a major discovery signal.

The machine learning approach here points toward a shift in how experimental particle physics gets done. Traditional reconstruction algorithms encode human understanding of detector physics into hand-crafted likelihood functions. These are powerful but slow to develop and bounded by what humans can explicitly model. CNNs learn directly from simulated data, capturing correlations humans might miss.


As detectors grow more complex and datasets larger, that advantage grows with them. The upcoming IceCube-Upgrade will add denser instrumentation to DeepCore, and these CNN techniques will scale with it, potentially reaching sub-percent precision on oscillation parameters from atmospheric neutrinos alone.

> **Bottom Line:** IceCube DeepCore combined 9.3 years of Antarctic ice data with convolutional neural network reconstruction to deliver the most precise atmospheric neutrino oscillation measurement ever made: Δm²₃₂ = 2.40 × 10⁻³ eV² and sin²θ₂₃ = 0.54. Deep learning is transforming precision particle physics at kilometer-scale detectors.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits at the intersection of AI and fundamental physics, using convolutional neural networks inside a cubic-kilometer ice detector to push precision measurements of neutrino mass and mixing beyond what traditional algorithms could achieve.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The CNN-based event reconstruction framework shows that deep learning can simultaneously improve signal efficiency and background rejection in complex, high-dimensional particle physics datasets, a methodology applicable across many detector technologies.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The measurement of Δm²₃₂ = 2.40 ⁺⁰·⁰⁵₋₀.₀₄ × 10⁻³ eV² and sin²θ₂₃ = 0.54 ⁺⁰·⁰⁴₋₀.₀₃ is the world's most precise atmospheric neutrino oscillation result, providing essential constraints on the mass ordering and octant questions at the frontier of the Standard Model.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">These methods carry over directly to the IceCube-Upgrade and next-generation detectors, with the potential to resolve the neutrino mass ordering definitively. See [arXiv:2405.02163](https://arxiv.org/abs/2405.02163) for complete technical details.</span></div></div>
</div>
