---
abstract: We present forecasts for constraints on the matter density ($Ω_m$) and the
  amplitude of matter density fluctuations at 8h$^{-1}$Mpc ($σ_8$) from CMB lensing
  convergence maps and galaxy weak lensing convergence maps. For CMB lensing convergence
  auto statistics, we compare the angular power spectra ($C_\ell$'s) to the wavelet
  scattering transform (WST) coefficients. For CMB lensing convergence $\times$ galaxy
  weak lensing convergence statistics, we compare the cross angular power spectra
  to wavelet phase harmonics (WPH). This work also serves as the first application
  of WST and WPH to these probes. For CMB lensing convergence, we find that WST and
  $C_\ell$'s yield similar constraints in forecasts for all surveys considered in
  this work. When CMB lensing convergence is crossed with galaxy weak lensing convergence
  projected from $\textit{Euclid}$ Data Release 2 (DR2), we find that WPH outperforms
  cross-$C_\ell$'s by factors between $2.2$ and $3.4$ for individual parameter constraints.
  To compare these different summary statistics, we develop a novel learned binning
  approach. This method compresses summary statistics while maintaining interpretability.
  We find this leads to improved constraints compared to more naive binning schemes
  for our wavelet-based statistics, but not for $C_\ell$'s. By learning the binning
  and measuring constraints on distinct data sets, our method is robust to overfitting
  by construction.
arxivId: '2510.13968'
arxivUrl: https://arxiv.org/abs/2510.13968
authors:
- Kyle Boone
- Georgios Valogiannis
- Marco Gatti
- Cora Dvorkin
concepts:
- cosmic microwave background
- wavelet scattering transform
- wavelet phase harmonics
- learned binning
- cosmological simulation
- dimensionality reduction
- spectral methods
- simulation-based inference
- feature extraction
- bayesian inference
- dark matter
- likelihood estimation
figures:
- /iaifi-research-blog/figures/2510_13968/figure_1.png
- /iaifi-research-blog/figures/2510_13968/figure_2.png
- /iaifi-research-blog/figures/2510_13968/figure_3.png
pdfUrl: https://arxiv.org/pdf/2510.13968v2
published: '2025-10-15T18:00:14+00:00'
theme: Astrophysics
title: Constraining Power of Wavelet vs. Power Spectrum Statistics for CMB Lensing
  and Weak Lensing with Learned Binning
wordCount: 1391
---

## The Big Picture

Imagine trying to describe a crumpled piece of paper using only the average height of every square centimeter. You'd capture the broad hills and valleys but miss the sharp creases, the places where the paper folds abruptly into intricate patterns invisible to a simple average. Cosmologists face exactly this problem when mapping the invisible mass of the universe.

The universe's matter distribution isn't smooth. Gravity has spent 13 billion years pulling gas and dark matter into filaments, walls, and knots that make up the cosmic web. Early on, fluctuations were nearly Gaussian (random, well-described by averages), but nonlinear gravity has since introduced sharp features, edges, and asymmetries that standard statistical tools cannot see.

The workhorse of cosmology, the **angular power spectrum**, measures how much structure exists at each angular scale. It captures the Gaussian part beautifully. But it's blind to those crumpled creases.

A team from Harvard, the University of Chicago, and the Kavli Institute tested whether wavelet-based statistics could do better. These mathematical tools, borrowed from signal processing, detect patterns at multiple scales simultaneously. The team applied them for the first time to two types of cosmic maps: one from the **CMB** (the cosmic microwave background, the faint afterglow of light from the early universe) and one from the gravitational bending of distant galaxy shapes. For the right combination of probes, wavelets beat power spectra by more than a factor of three.

> **Key Insight:** Wavelet phase harmonics extract non-Gaussian structural information that power spectra miss, yielding up to 3.4× tighter cosmological constraints when combining CMB lensing with galaxy weak lensing from Euclid, all without any machine learning black box.

## How It Works

The fundamental observable is the **convergence map**, a pixelated map of how much mass is projected along each line of sight. When a massive cluster sits between us and a distant light source, it bends that light slightly. Measure enough of these tiny deflections and you can reconstruct a map of all the mass in the universe.

The researchers used the `ULAGAM` suite of 2,000 N-body simulations, numerical experiments that track how 512³ dark matter particles move and clump under gravity from the early universe to today. From these simulations, they constructed two convergence maps:

- **κ_CMB**: the lensing signal imprinted on the cosmic microwave background, accumulated over the entire observable universe back to the surface of last scattering (the boundary beyond which the early universe was opaque, roughly 380,000 years after the Big Bang)
- **κ_WL**: the lensing signal from galaxy shapes, as would be measured by the Euclid space telescope over a specific redshift slice (a narrow window in cosmic distance and time)

Rather than asking which statistic extracts the most information in general, the team focused on two cosmological parameters: **Ω_m** (the total matter density) and **σ_8** (the amplitude of matter density fluctuations at a scale of 8 h⁻¹ Mpc). These are the parameters weak lensing is most sensitive to.

![Figure 1](/iaifi-research-blog/figures/2510_13968/figure_1.png)

A traditional power spectrum (C_ℓ) asks: how much power exists at each angular frequency? It's a global, rotation-invariant measure.

The **wavelet scattering transform (WST)** cascades the field through multiple rounds of wavelet filtering and nonlinear operations, like a convolutional neural network with fixed, interpretable filters rather than learned weights. **Wavelet phase harmonics (WPH)** go further, explicitly capturing correlations between structures at different scales by tracking the phases of wavelet coefficients, not just their amplitudes.

A key methodological contribution is **learned binning**, a compression scheme that puts all statistics on equal footing. Raw wavelet coefficients can number in the thousands. Rather than manually choosing which bins to combine, learned binning trains a linear compression on half the simulation suite and tests it on the other half. Training maximizes the determinant of the **Fisher matrix**, which measures how much information a statistic carries about the target parameters. Because compression is learned on different data than it's tested on, overfitting is prevented by construction.

## Why It Matters

For the cross-correlation between CMB lensing and Euclid weak lensing, WPH outperforms cross-power spectra by factors between 2.2 and 3.4 for individual parameter constraints. That's not a modest improvement. It's equivalent to running an experiment two to three times longer, or covering several times more sky, just by changing the statistic.

![Figure 2](/iaifi-research-blog/figures/2510_13968/figure_2.png)

The story changes for CMB lensing alone. When analyzing κ_CMB in isolation, WST and standard C_ℓ's yield comparable constraints. The gain from wavelets emerges specifically in the cross-correlation regime, where non-Gaussian structure in the lower-redshift galaxy lensing maps hasn't been erased by projection effects. This makes physical sense: galaxy weak lensing probes structure closer to us, where nonlinear evolution is most advanced and the crumpled-paper creases are most pronounced.

![Figure 3](/iaifi-research-blog/figures/2510_13968/figure_3.png)

Learned binning carries a broader lesson. Cosmological analyses face a growing pile of summary statistic choices: how many ℓ-bins for a power spectrum, which angular separations for a bispectrum (a statistic capturing three-point correlations beyond what a two-point power spectrum can see), which wavelet scales to include. Learned binning gives an interpretable way to compress any statistic to a fixed dimensionality while maximizing information content.

That wavelets benefit from this compression but power spectra don't is itself a result. Standard power spectrum binning is already near-optimal, while wavelet coefficients gain substantially from data-driven compression.

What comes next is applying WPH to real Euclid data. The mission is currently surveying one-third of the sky, and its second data release (DR2) will cover thousands of square degrees overlapping with ground-based CMB telescopes like the Atacama Cosmology Telescope and the Simons Observatory. If the forecasts hold under real-world complications (intrinsic alignments, baryonic feedback, noise), wavelet phase harmonics could meaningfully sharpen constraints on the nature of dark matter and dark energy.

> **Bottom Line:** Wavelet phase harmonics extract up to 3.4× more cosmological information than power spectra when combining CMB and galaxy lensing maps, and a new learned binning method provides an overfitting-resistant way to compress any summary statistic, a roadmap for squeezing maximum science out of next-generation surveys.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work brings machine learning compression techniques together with traditional cosmological statistics, applying wavelet methods from signal processing to CMB and galaxy lensing maps for the first time. The Fisher-optimized binning scheme is general enough to apply to any summary statistic in any field.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The learned binning method offers an interpretable alternative to black-box neural network compression, using Fisher information maximization on held-out data to produce compact, overfitting-resistant statistics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Wavelet phase harmonics outperform power spectra by factors of 2.2–3.4 for cross-lensing statistics, pointing toward tighter constraints on Ω_m and σ_8 from upcoming surveys like Euclid and the Simons Observatory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will apply these methods to real Euclid and CMB data, where baryonic systematics and noise must be carefully modeled; the paper is available at [arXiv:2510.13968](https://arxiv.org/abs/2510.13968).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Constraining Power of Wavelet vs. Power Spectrum Statistics for CMB Lensing and Weak Lensing with Learned Binning</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2510.13968</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Kyle Boone", "Georgios Valogiannis", "Marco Gatti", "Cora Dvorkin"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We present forecasts for constraints on the matter density ($Ω_m$) and the amplitude of matter density fluctuations at 8h$^{-1}$Mpc ($σ_8$) from CMB lensing convergence maps and galaxy weak lensing convergence maps. For CMB lensing convergence auto statistics, we compare the angular power spectra ($C_\ell$'s) to the wavelet scattering transform (WST) coefficients. For CMB lensing convergence $\times$ galaxy weak lensing convergence statistics, we compare the cross angular power spectra to wavelet phase harmonics (WPH). This work also serves as the first application of WST and WPH to these probes. For CMB lensing convergence, we find that WST and $C_\ell$'s yield similar constraints in forecasts for all surveys considered in this work. When CMB lensing convergence is crossed with galaxy weak lensing convergence projected from $\textit{Euclid}$ Data Release 2 (DR2), we find that WPH outperforms cross-$C_\ell$'s by factors between $2.2$ and $3.4$ for individual parameter constraints. To compare these different summary statistics, we develop a novel learned binning approach. This method compresses summary statistics while maintaining interpretability. We find this leads to improved constraints compared to more naive binning schemes for our wavelet-based statistics, but not for $C_\ell$'s. By learning the binning and measuring constraints on distinct data sets, our method is robust to overfitting by construction.</span></div></div>
</div>
