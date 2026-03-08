---
abstract: Combining galaxy clustering information from regions of different environmental
  densities can help break cosmological parameter degeneracies and access non-Gaussian
  information from the density field that is not readily captured by the standard
  two-point correlation function (2PCF) analyses. However, modelling these density-dependent
  statistics down to the non-linear regime has so far remained challenging. We present
  a simulation-based model that is able to capture the cosmological dependence of
  the full shape of the density-split clustering (DSC) statistics down to intra-halo
  scales. Our models are based on neural-network emulators that are trained on high-fidelity
  mock galaxy catalogues within an extended-$Λ$CDM framework, incorporating the effects
  of redshift-space, Alcock-Paczynski distortions and models of the halo-galaxy connection.
  Our models reach sub-percent level accuracy down to $1\,h^{-1}{\rm Mpc}$ and are
  robust against different choices of galaxy-halo connection modelling. When combined
  with the galaxy 2PCF, DSC can tighten the constraints on $ω_{\rm cdm}$, $σ_8$, and
  $n_s$ by factors of 2.9, 1.9, and 2.1, respectively, compared to a 2PCF-only analysis.
  DSC additionally puts strong constraints on environment-based assembly bias parameters.
  Our code is made publicly available on Github.
arxivId: '2309.16539'
arxivUrl: https://arxiv.org/abs/2309.16539
authors:
- Carolina Cuesta-Lazaro
- Enrique Paillas
- Sihan Yuan
- Yan-Chuan Cai
- Seshadri Nadathur
- Will J. Percival
- Florian Beutler
- Arnaud de Mattia
- Daniel Eisenstein
- Daniel Forero-Sanchez
- Nelson Padilla
- Mathilde Pinon
- Vanina Ruhlmann-Kleider
- Ariel G. Sánchez
- Georgios Valogiannis
- Pauline Zarrouk
concepts:
- density-split clustering
- simulation-based inference
- emulation
- cosmological simulation
- surrogate modeling
- bayesian inference
- halo-galaxy connection
- dark matter
- posterior estimation
- dark energy
- assembly bias
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2309_16539/figure_1.png
- /iaifi-research-blog/figures/2309_16539/figure_1.png
- /iaifi-research-blog/figures/2309_16539/figure_2.png
- /iaifi-research-blog/figures/2309_16539/figure_2.png
- /iaifi-research-blog/figures/2309_16539/figure_3.png
- /iaifi-research-blog/figures/2309_16539/figure_3.png
pdfUrl: https://arxiv.org/pdf/2309.16539v2
published: '2023-09-28T15:53:30+00:00'
theme: Astrophysics
title: 'SUNBIRD: A simulation-based model for full-shape density-split clustering'
wordCount: 979
---

## The Big Picture

Imagine trying to understand a city by only measuring the average distance between buildings. You'd miss everything interesting: the dense downtown core, the sprawling suburbs, the empty parks.

Cosmologists face a similar problem when they map the universe. For decades, the standard tool has been the **two-point correlation function (2PCF)**, a measure of how likely any two galaxies are to be near each other, averaged across all environments. It's powerful, but it can't tell a crowded galaxy cluster from a vast cosmic void.

The universe isn't average. It's lumpy, with dense filaments threading between enormous empty voids. These extremes follow different rules and carry different information about fundamental parameters. Dark matter density, the rate at which structure grows, the pattern of matter laid down just after the Big Bang: all leave distinct fingerprints depending on whether galaxies live in rich or barren neighborhoods.

Turning that intuition into a rigorous measurement tool is hard. Modeling galaxy clustering across different environments, down to small scales where gravity has tangled structures into patterns no simple equation can describe, has long resisted solution. SUNBIRD, a neural network trained on thousands of expensive simulations, was built by a team including IAIFI researchers at MIT and Harvard to crack this problem.

> By training neural networks on high-fidelity simulations, SUNBIRD predicts how galaxies cluster in dense vs. sparse regions with sub-percent accuracy, pulling out information that standard analyses throw away.

## How It Works

The core idea is **density-split clustering (DSC)**: divide the surveyed volume into regions ranked by local galaxy density, then measure how galaxies cluster within each density slice separately. Instead of one correlation function averaged over everything, you get a family of them. One for voids, one for average regions, one for the densest knots. Each carries complementary information.

![Figure 1](/iaifi-research-blog/figures/2309_16539/figure_1.png)

To use these statistics scientifically, you need a model. Given a set of cosmological parameters, you need to predict what the DSC signal should look like, accounting for how gravity amplifies tiny density differences into filaments and voids, galaxy formation physics, and observational effects, all at once. Standard mathematical approximations break down well before reaching the scales where the signal is richest.

The SUNBIRD team's approach:

1. **Run a large suite of N-body simulations** spanning an extended ΛCDM parameter space, varying dark matter density (ω_cdm), the amplitude of matter fluctuations (σ_8), the spectral index (n_s), and parameters describing the galaxy-halo connection.
2. **Populate dark matter halos with galaxies** using **halo occupation distribution (HOD)** models, which describe statistically how many galaxies of a given type live in halos of a given mass.
3. **Measure density-split clustering statistics** across all mock catalogs, building a training dataset that spans realistic parameter space.
4. **Train neural-network emulators** to interpolate those measurements. Given any point in parameter space, the network predicts the full DSC signal across all scales and density quantiles.

![Figure 3](/iaifi-research-blog/figures/2309_16539/figure_2.png)

The emulators reach sub-percent precision down to scales of 1 h⁻¹ Mpc, well into the regime where individual halos dominate and simple equations fail. They also hold up when tested against galaxy catalogs generated with different HOD prescriptions than those used in training, which suggests the cosmological signal is genuinely captured rather than overfitted to a particular galaxy formation recipe.

The model correctly handles two important observational effects: **redshift-space distortions** (apparent squashing and stretching of galaxy distributions caused by galaxies' own peculiar motions along the line of sight) and **Alcock-Paczynski distortions** (geometric distortions that appear when the wrong cosmology is assumed in converting redshifts to distances).

![Figure 4](/iaifi-research-blog/figures/2309_16539/figure_2.png)

## Why It Matters

When the researchers combine DSC with a standard 2PCF analysis, parameter constraints tighten considerably. The uncertainty on ω_cdm, the physical density of cold dark matter, shrinks by a factor of 2.9. Constraints on σ_8, the amplitude of matter fluctuations at the center of the ongoing S8 tension between early- and late-universe measurements, improve by 1.9×. The spectral index n_s, which encodes information about inflation, improves by 2.1×. These aren't incremental gains. They come from extracting information that was already in the data but invisible to the standard two-point analysis.

![Figure 6](/iaifi-research-blog/figures/2309_16539/figure_3.png)

Beyond cosmological parameters, DSC turns out to be uniquely sensitive to **assembly bias**, the phenomenon where galaxy clustering depends not just on halo mass but on the broader environment in which those halos formed. This is exactly the kind of subtle effect that density-sensitive statistics are built to detect, and it could help distinguish competing models of galaxy formation.

The framework is also a natural starting point for testing modified gravity theories, which tend to predict their strongest deviations in low-density environments. SUNBIRD's code is publicly available on [GitHub](https://github.com/florpi/sunbird), so other groups can apply it directly to real survey data from DESI, Euclid, and future missions.

> SUNBIRD turns the overlooked environmental dependence of galaxy clustering into a precision cosmological tool, tightening constraints on dark matter and structure growth by up to a factor of three without requiring any new observations.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">SUNBIRD is a clean example of AI-for-physics: neural-network emulators trained on cosmological simulations make it possible to do rigorous inference from statistics that were previously impossible to model analytically, connecting machine learning methods directly to observational cosmology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work shows that simulation-based inference with neural emulators can achieve sub-percent accuracy across extended parameter spaces while remaining insensitive to specific modeling choices, a useful proof-of-concept for emulator-based forward modeling more broadly.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By extracting non-Gaussian information from the large-scale structure of the universe, SUNBIRD tightens constraints on dark matter density and the growth of cosmic structure, with direct bearing on the S8 tension and tests of gravity.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">SUNBIRD is ready to apply to current and upcoming surveys including DESI and Euclid. The code is publicly available at [github.com/florpi/sunbird](https://github.com/florpi/sunbird), and the paper is available as [arXiv:2309.16539](https://arxiv.org/abs/2309.16539).</span></div></div>
</div>
