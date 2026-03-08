---
abstract: We present the first measurement of local-type primordial non-Gaussianity
  from the cross-correlation between $1.2$ million spectroscopically confirmed quasars
  from the first data release (DR1) of the Dark Energy Spectroscopic Instrument (DESI)
  and the Planck PR4 CMB lensing reconstructions. The analysis is performed in three
  tomographic redshift bins covering $0.8 < z < 3.5$, covering a sky fraction of $\sim
  20\%$. We adopt a catalog-based pseudo-$C_\ell$ estimator and apply linear imaging
  weights validated on noiseless mocks. Compared to previous analyses using photometric
  quasar samples, our results benefit from the high purity of the DESI spectroscopic
  sample, the reduced noise of PR4 lensing, and the absence of excess large-scale
  power in the spectroscopic quasar auto-correlation. Fitting simultaneously for the
  non-Gaussianity parameter $f_{\mathrm{NL}}$ and the linear bias amplitude in each
  redshift bin, we obtain $f_{\mathrm{NL}} = 2^{+28}_{-34}$ for a response parameter
  $p=1.6$, and $f_{\mathrm{NL}} = 6^{+20}_{-24}$ for $p=1.0$. These results improve
  the constraints on $f_{\mathrm{NL}}$ by $\sim 35\%$ compared to the previous analysis
  based on the Legacy Imaging Survey DR9. Our results demonstrate the statistical
  power of DESI quasars for probing inflationary physics, and highlight the promise
  of future DESI data releases.
arxivId: '2512.17865'
arxivUrl: https://arxiv.org/abs/2512.17865
authors:
- Sofia Chiarenza
- Alex Krolewski
- Marco Bonici
- Edmond Chaussidon
- Roger de Belsunce
- Will Percival
- Jessica Nicole Aguilar
- Steven Ahlen
- Anton Baleato Lizancos
- Davide Bianchi
- David Brooks
- Todd Claybaugh
- Andrei Cuceu
- Kyle Dawson
- Axel de la Macorra
- Peter Doel
- Simone Ferraro
- Andreu Font-Ribera
- Jaime E. Forero-Romero
- Enrique Gaztañaga
- Satya Gontcho A Gontcho
- Gaston Gutierrez
- Hiram K. Herrera-Alcantar
- Klaus Honscheid
- Dragan Huterer
- Mustapha Ishak
- Dick Joyce
- David Kirkby
- Anthony Kremin
- Ofer Lahav
- Claire Lamman
- Martin Landriau
- Laurent Le Guillou
- Michael Levi
- Marc Manera
- Paul Martini
- Aaron Meisner
- Ramon Miquel
- Seshadri Nadathur
- Jeffrey A. Newman
- Gustavo Niz
- Nathalie Palanque-Delabrouille
- Claire Poppett
- Francisco Prada
- Ignasi Pérez-Ràfols
- Graziano Rossi
- Eusebio Sanchez
- David Schlegel
- Michael Schubnell
- Hee-Jong Seo
- Joseph Harry Silber
- David Sprayberry
- Gregory Tarlé
- Benjamin Alan Weaver
- Christophe Yèche
- Rongpu Zhou
- Hu Zou
concepts:
- primordial non-gaussianity
- scale-dependent bias
- cmb lensing cross-correlation
- cosmic microwave background
- spectral methods
- tomographic redshift binning
- optimal weighting
- bayesian inference
- cosmological simulation
- monte carlo methods
- effective field theory
- dark energy
figures:
- /iaifi-research-blog/figures/2512_17865/figure_1.png
- /iaifi-research-blog/figures/2512_17865/figure_1.png
- /iaifi-research-blog/figures/2512_17865/figure_2.png
- /iaifi-research-blog/figures/2512_17865/figure_2.png
- /iaifi-research-blog/figures/2512_17865/figure_3.png
- /iaifi-research-blog/figures/2512_17865/figure_3.png
pdfUrl: https://arxiv.org/pdf/2512.17865v1
published: '2025-12-19T18:14:50+00:00'
theme: Theoretical Physics
title: Constraining primordial non-Gaussianity from DESI DR1 quasars and Planck PR4
  CMB Lensing
wordCount: 1102
---

## The Big Picture

Imagine trying to read a message written in the very first moments after the Big Bang, encoded not in light or matter but in the subtle statistical patterns of how matter was distributed across the infant universe. That message is still out there, imprinted on the large-scale structure of the cosmos. Physicists are slowly learning to decode it.

The decoder ring is **primordial non-Gaussianity**, often written as f_NL. In the simplest inflation models, where a single quantum energy field drove the explosive expansion of the early universe, the primordial ripples in matter density (tiny variations that would later grow into galaxies and the cosmic web) should follow a nearly perfect Gaussian distribution. More complex models, involving multiple interacting quantum fields, predict small but detectable deviations from that symmetry.

Measuring a non-zero f_NL would be like catching the universe in a lie about how simple it really was at birth.

A team using the Dark Energy Spectroscopic Instrument (DESI) and the Planck satellite has now produced the tightest cross-correlation constraint on f_NL to date. They studied 1.2 million quasars, intensely luminous cores of distant galaxies powered by supermassive black holes, and compared their positions on the sky to distortions in the **cosmic microwave background** (the faint heat afterglow of the Big Bang, detectable today as microwaves filling the entire sky).

> **Key Insight:** By cross-correlating spectroscopically confirmed quasars with CMB lensing maps rather than relying on galaxy clustering alone, this analysis sidesteps the systematic errors that have plagued previous measurements, tightening the constraint on inflationary physics by 35%.

## How It Works

Local-type primordial non-Gaussianity changes how galaxies and quasars cluster. It introduces a **scale-dependent bias**: an extra boost in clustering visible only at the very largest cosmic scales, scaling as k⁻² (meaning it grows dramatically stronger at larger distances) and amplifying at higher redshifts. The more distant the objects, the more pronounced the effect. Quasars are ideal tracers precisely because they exist at high redshift and span enormous cosmic volumes, where this signal is loudest.

But measuring structure on those ultra-large scales is treacherous. Subtle observational artifacts like varying sky brightness, dust extinction, and stellar density gradients can masquerade as real cosmological signal. Every previous large-scale structure constraint on f_NL has been limited by systematics rather than statistical noise.

The team's solution: measure quasars cross-talking with the CMB. **CMB lensing** is the bending of ancient microwave photons by the mass distribution along their 14-billion-year journey to us. Planck maps these distortions across the whole sky. The systematics plaguing ground-based galaxy surveys (telescope optics, atmospheric effects, dust) have nothing to do with how Planck measures the CMB. When you cross-correlate the two, contaminations don't bias the signal; they only add noise. That's a far more manageable problem.

The analysis pipeline:

- **Sample selection:** 1.2 million spectroscopically confirmed quasars from DESI DR1, split into three tomographic redshift bins (three distance slices at progressively greater cosmic depths) spanning 0.8 < z < 3.5, covering ~20% of the sky
- **Lensing maps:** Planck's PR4 CMB lensing reconstruction, with improved noise performance over the 2018 maps thanks to additional data and better filtering
- **Power spectrum estimation:** A catalog-based **pseudo-Cℓ estimator**, a method that extracts the angular power spectra (how much structure exists at each angular scale) between the quasar density field and the lensing map
- **Imaging systematics:** Linear imaging weights, validated on noiseless simulated catalogs, to remove residual correlations between quasar density and observational artifacts

![Figure 1](figure:1)

One particularly clever element is the optimal redshift weighting for f_NL. Rather than treating all quasars equally, the team derived weights that maximize sensitivity to scale-dependent bias, giving more statistical leverage to quasars at the redshifts and angular scales where the f_NL signature is strongest. This is the first time such weighting has been applied to lensing cross-correlations.

![Figure 3](figure:3)

## Why It Matters

The measurement yields f_NL = 2 ⁺²⁸₋₃₄ (response parameter p = 1.6) and f_NL = 6 ⁺²⁰₋₂₄ (p = 1.0), both consistent with zero. That's exactly what standard single-field inflation predicts. The uncertainties translate to σ_fNL ≈ 20–30, a 35% improvement over the previous cross-correlation analysis using photometric quasars from the Legacy Imaging Survey DR9.

For context, the best CMB-only constraint (Planck bispectrum) sits at f_NL = −0.9 ± 5.1, and recent 3D large-scale structure results from DESI DR1 reach roughly σ_fNL ~ 9. This cross-correlation analysis isn't yet at those precision levels, but it measures something complementary and systematically cleaner. The DESI spectroscopic quasar sample shows no excess large-scale power in its auto-correlation, a validation that photometric samples simply cannot guarantee.

![Figure 5](figure:5)

The race to measure f_NL is one of the defining cosmological experiments of the next decade. Reaching σ_fNL ~ 1 would genuinely discriminate between broad classes of inflation models, ruling out multi-field scenarios if the result stays consistent with zero. DESI spectroscopic quasars paired with CMB lensing are now a viable, competitive path toward that goal.

The cross-correlation approach is systematically orthogonal to 3D power spectrum analyses. If both methods converge on the same f_NL, that convergence is strong evidence the signal is real. Future DESI data releases will multiply the quasar sample dramatically, and the Simons Observatory will provide lower-noise lensing maps. Together, σ_fNL < 10 is within reach. Stage 4 surveys like SPHEREx and LSST, paired with next-generation CMB lensing, may finally crack the σ_fNL ~ 1 barrier.

> **Bottom Line:** Using 1.2 million DESI quasars cross-correlated with Planck CMB lensing maps, this analysis achieves a 35% tighter constraint on primordial non-Gaussianity than previous cross-correlation methods, showing that spectroscopic surveys can probe inflation with a systematic cleanliness that auto-correlation analyses cannot match.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work combines cosmological survey science and CMB analysis, drawing on data from fundamentally different instruments through statistical methods (optimal redshift weighting, pseudo-Cℓ cross-correlation, and noiseless mock validation) to probe inflationary physics at scales inaccessible to either dataset alone.

- **Impact on Artificial Intelligence:** The imaging systematics pipeline relies on linear weighting schemes validated against noiseless simulated catalogs, illustrating how careful statistical modeling and synthetic data validation can enable reliable signal extraction at the threshold of observational noise, with natural extensions to machine-learning-based approaches.

- **Impact on Fundamental Interactions:** Constraining f_NL to within ±20–30 tests whether inflation was driven by a single quantum field or required multiple interacting fields, directly probing the particle physics of the universe's first moments.

- **Outlook and References:** Future DESI data releases and next-generation CMB lensing from the Simons Observatory promise to push σ_fNL below 10, potentially reaching the decisive σ_fNL ~ 1 threshold; this work appears as [arXiv:2512.17865](https://arxiv.org/abs/2512.17865).
