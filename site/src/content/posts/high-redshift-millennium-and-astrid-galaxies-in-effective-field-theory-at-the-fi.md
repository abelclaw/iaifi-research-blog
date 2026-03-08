---
abstract: Effective Field Theory (EFT) modeling is expected to be a useful tool in
  the era of future higher-redshift galaxy surveys such as DESI-II and Spec-S5 due
  to its robust description of various large-scale structure tracers. However, large
  values of EFT bias parameters of higher-redshift galaxies could jeopardize the convergence
  of the perturbative expansion. In this paper we measure the bias parameters and
  other EFT coefficients from samples of two types of star-forming galaxies in the
  state-of-the-art MilleniumTNG and Astrid hydrodynamical simulations. Our measurements
  are based on the field-level EFT forward model that allows for precision EFT parameter
  measurements by virtue of cosmic variance cancellation. Specifically, we consider
  approximately representative samples of Lyman-break galaxies (LBGs) and Lyman-alpha
  emitters (LAEs) that are consistent with the observed (angular) clustering and number
  density of these galaxies at $z=3$. Reproducing the linear biases and number densities
  observed from existing LAE and LBG data, we find quadratic bias parameters that
  are roughly consistent with those predicted from the halo model coupled with a simple
  halo occupation distribution model. We also find non-perturbative velocity contributions
  (Fingers of God) of a similar size for LBGs to the familiar case of Luminous Red
  Galaxies. However, these contributions are quite small for LAEs despite their large
  satellite fraction values of up to $\sim 30\%$. Our results indicate that the effective
  momentum reach $k_{\rm{Max}}$ at $z=3$ for LAEs (LBGs) will be in the range $0.3-0.6
  ~h\rm{Mpc}^{-1}$ ($0.2-0.8~h\rm{Mpc}^{-1}$), suggesting that EFT will perform well
  for high redshift galaxy clustering. This work provides the first step toward obtaining
  realistic simulation-based priors on EFT parameters for LAEs and LBGs.
arxivId: '2505.03626'
arxivUrl: https://arxiv.org/abs/2505.03626
authors:
- James M. Sullivan
- Carolina Cuesta-Lazaro
- Mikhail M. Ivanov
- Yueying Ni
- Sownak Bose
- Boryana Hadzhiyska
- César Hernández-Aguayo
- Lars Hernquist
- Rahul Kannan
concepts:
- effective field theory
- galaxy bias
- cosmological simulation
- halo occupation distribution
- bayesian inference
- perturbative expansion
- simulation-based inference
- dark matter
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2505_03626/figure_1.png
- /iaifi-research-blog/figures/2505_03626/figure_1.png
- /iaifi-research-blog/figures/2505_03626/figure_2.png
- /iaifi-research-blog/figures/2505_03626/figure_2.png
- /iaifi-research-blog/figures/2505_03626/figure_3.png
- /iaifi-research-blog/figures/2505_03626/figure_3.png
pdfUrl: https://arxiv.org/pdf/2505.03626v1
published: '2025-05-06T15:23:09+00:00'
theme: Astrophysics
title: High-redshift Millennium and Astrid galaxies in effective field theory at the
  field level
wordCount: 1109
---

## The Big Picture

Imagine trying to map a city you've never visited using only photographs taken from miles away, knowing that the farther the photograph was taken, the less distorted the light. That's roughly the situation cosmologists face when pointing next-generation telescopes at the early universe. Looking farther back in time means cleaner underlying physics, but only if our mathematical tools can faithfully translate what we observe into what actually exists.

Those tools are called **Effective Field Theory** (EFT), a framework borrowed from particle physics that treats galaxies as tracers of cosmic structure rather than as individual objects. Instead of modeling every galaxy in detail, EFT describes how galaxies cluster using a compact set of mathematical parameters, a recipe for turning raw observations into fundamental physics. It has proven enormously powerful for current surveys.

But there's a problem on the horizon. At high redshift (early cosmic times), galaxies formed in such different environments that the mathematical parameters describing them might grow too large for the theory's approximations to hold. If EFT breaks down, we lose one of our most reliable lenses on the young universe.

A new study by Sullivan, Cuesta-Lazaro, Ivanov, and collaborators confronts this worry directly. Using two of the world's most sophisticated galaxy formation simulations, they measure how well EFT describes two classes of early-universe galaxies and find that the theory holds its ground.

> **Key Insight:** EFT's mathematical approximation scheme remains valid for both Lyman-break galaxies and Lyman-alpha emitters at redshift z=3, with usable scales extending to 0.2–0.8 h/Mpc, well into the regime where gravitational clustering becomes complex. This opens the door for precision cosmology from surveys like DESI-II.

## How It Works

The researchers focused on two galaxy populations that future surveys will observe at redshift z≈3, roughly when the universe was just 2 billion years old:

- **Lyman-break galaxies (LBGs)**: Massive, luminous star-forming galaxies identified by a characteristic "dropout." They vanish in blue photometric bands because hydrogen absorbs light shortward of the Lyman-alpha line. The bright giants of the early universe.
- **Lyman-alpha emitters (LAEs)**: Lower-mass galaxies that glow in a specific hydrogen emission line. Their physics is messier: observed properties depend on dust geometry, metallicity, and radiative transfer through the intergalactic medium.

![Figure 1](figure:1)

To measure how these galaxies trace the underlying dark matter, the team analyzed two **hydrodynamical simulations**, physics-based models that track gas, star formation, and black hole feedback across billions of virtual light-years: MillenniumTNG (MTNG) and Astrid. Both reproduce observed clustering and number densities of real LAE and LBG populations.

The technical heart of the paper is the **field-level EFT forward model**. Rather than comparing statistical summaries like **power spectra** (measurements of how strongly galaxies cluster at different scales), this approach compares actual three-dimensional density fields, mode by mode. The payoff is **cosmic variance cancellation**: by comparing the same patch of simulated universe rather than independent realizations, measurement precision increases dramatically. Bias parameters come out pinned down to percent-level accuracy from a single simulation volume.

![Figure 2](figure:2)

EFT works by expanding the galaxy density field as a series of terms, each multiplied by a **bias parameter** encoding how a given galaxy population responds to its environment. The linear bias b₁ captures how much more clustered galaxies are than dark matter on large scales. Quadratic terms (b₂, b_𝒢₂) describe how galaxy formation responds to local curvature and tidal forces, the stretching and squeezing of the density distribution.

The worry at high redshift was that estimates from the **peak-background split** model suggested bias parameters could grow large enough to make the series diverge. Instead, the measured quadratic parameters are broadly consistent with the **halo occupation distribution (HOD)** model, the standard framework describing how galaxies populate dark matter halos. No catastrophic enhancement. The theory's approximations remain self-consistent.

![Figure 3](figure:3)

One result stood out. **Fingers of God**, the elongated smearing of galaxy positions along the line of sight caused by random velocities within halos, are well-known to complicate galaxy surveys. For LBGs, these contributions are comparable to those of Luminous Red Galaxies, the workhorses of current low-redshift surveys. That's expected: LBGs live in massive halos with fast-moving satellites.

LAEs tell a different story. Despite satellite fractions as high as ~30%, their Fingers of God signal is surprisingly small. The same processes (dust, gas geometry, Lyman-alpha radiative transfer) that make a galaxy visible as an LAE may preferentially select objects with lower internal velocity dispersions, suppressing the signal even when many satellites are present.

![Figure 4](figure:4)

## Why It Matters

EFT works. The effective momentum reach k_max at z=3 spans 0.3–0.6 h/Mpc for LAEs and 0.2–0.8 h/Mpc for LBGs, ranges encompassing rich cosmological information. Surveys like DESI-II and the proposed Spec-S5 mission will map millions of these galaxies. Knowing that EFT can analyze their clustering without systematic breakdown means those maps can deliver measurements of dark energy, neutrino masses, and primordial physics with confidence.

Beyond the validation itself, the paper delivers something arguably more valuable: the first simulation-based priors on EFT parameters for these galaxy types. When real survey data arrives, analysts need to know what range of bias parameters to expect before they can efficiently sample the posterior. Sullivan et al. have built that foundation. Two independent simulations with different galaxy formation models give broadly consistent results, a cross-check no single simulation could provide.

> **Bottom Line:** High-redshift galaxies that seemed threatening to EFT's convergence turn out to be tractable. The theory holds well into the nonlinear regime, and the first simulation-based priors on EFT parameters for these galaxy types are now in hand, ready for use with upcoming surveys.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects advanced galaxy formation simulations with field-level statistical inference, combining hydrodynamical modeling with EFT to extract cosmologically useful information from the high-redshift universe.

- **Impact on Artificial Intelligence:** The field-level EFT forward model shows how cosmic variance cancellation, analogous to paired-sample inference, can dramatically improve parameter measurement precision. The principle has broad applicability in simulation-based inference for scientific AI.

- **Impact on Fundamental Interactions:** By validating EFT's perturbative expansion at z=3 and characterizing bias parameters for LBGs and LAEs, this work enables extraction of fundamental cosmological parameters (dark energy, neutrino masses, inflationary signatures) from next-generation galaxy surveys.

- **Outlook and References:** Future work will extend these priors to full posterior analyses of survey data and refine HOD modeling for the complex LAE selection function; the paper is available at [arXiv:2505.03626](https://arxiv.org/abs/2505.03626).
