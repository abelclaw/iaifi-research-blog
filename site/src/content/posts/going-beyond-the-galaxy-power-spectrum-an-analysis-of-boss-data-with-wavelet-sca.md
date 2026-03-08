---
abstract: We perform the first application of the wavelet scattering transform (WST)
  to actual galaxy observations, through a WST analysis of the BOSS DR12 CMASS dataset.
  We included the effects of redshift-space anisotropy, non-trivial survey geometry,
  systematic weights, and the Alcock-Paczynski distortion effect, following the commonly
  adopted steps for the power spectrum analysis. In order to capture the cosmological
  dependence of the WST, we use galaxy mocks obtained from the state-of-the-art ABACUSSUMMIT
  simulations, tuned to match the anisotropic correlation function of the BOSS CMASS
  sample in the redshift range $0.46<z<0.60$. Using our model for the WST coefficients,
  as well as for the first 2 multipoles of the galaxy power spectrum, that we use
  as reference, we perform a likelihood analysis of the CMASS data. We obtain the
  posterior probability distributions of 4 cosmological parameters, $\{ω_b,ω_c,n_s,σ_8\}$,
  as well as the Hubble constant, derived from a fixed value of the angular size of
  the sound horizon at last scattering measured by the Planck satellite, all of which
  are marginalized over the 7 nuisance parameters of the Halo Occupation Distribution
  model. The WST is found to deliver a substantial improvement in the values of the
  predicted $1σ$ errors compared to the regular power spectrum, which are tighter
  by a factor of $3-5$ in the case of flat and uninformative priors and by a factor
  of $3-8$, when a Big Bang Nucleosynthesis prior is applied on the value of $ω_b$.
  Our results are investigative and subject to certain approximations, which we discuss
  in the text.
arxivId: '2204.13717'
arxivUrl: https://arxiv.org/abs/2204.13717
authors:
- Georgios Valogiannis
- Cora Dvorkin
concepts:
- wavelet scattering transform
- simulation-based inference
- posterior estimation
- bayesian inference
- cosmological simulation
- emulation
- feature extraction
- spectral methods
- redshift-space distortions
- halo occupation distribution
- dark energy
- dark matter
figures:
- /iaifi-research-blog/figures/2204_13717/figure_1.png
- /iaifi-research-blog/figures/2204_13717/figure_2.png
- /iaifi-research-blog/figures/2204_13717/figure_3.png
pdfUrl: https://arxiv.org/pdf/2204.13717v3
published: '2022-04-28T18:00:07+00:00'
theme: Astrophysics
title: 'Going Beyond the Galaxy Power Spectrum: an Analysis of BOSS Data with Wavelet
  Scattering Transforms'
wordCount: 1100
---

## The Big Picture

Imagine trying to understand a symphony by tracking only its average volume. You'd miss the melody, harmony, and rhythm, all the structure that makes music meaningful. Cosmologists face a similar problem when studying the universe's large-scale structure using the galaxy power spectrum, a mathematical tool that measures how strongly galaxies cluster at different scales. The power spectrum tells you *how much* clustering exists at each scale but discards the complex patterns gravity has sculpted into the cosmic web over billions of years.

That missing information isn't trivial. The vast network of galaxy filaments, sheets, and voids encodes signatures of dark matter, dark energy, massive neutrinos, and early-universe physics. But gravitational collapse is deeply nonlinear. It generates interlocking patterns that pairwise correlations between galaxies simply cannot capture. The power spectrum, by design, only hears the simpler, bell-curve-shaped part of the distribution and stays silent about everything else.

Georgios Valogiannis and Cora Dvorkin at Harvard have taken a major step toward listening to the full cosmic symphony. In the first application of the **Wavelet Scattering Transform (WST)** to real galaxy data, they analyzed the BOSS DR12 CMASS dataset (a major sky survey cataloging hundreds of thousands of galaxies) and showed that this technique extracts cosmological parameters with dramatically tighter precision than the power spectrum alone.

> **Key Insight:** By replacing the galaxy power spectrum with Wavelet Scattering Transform coefficients, the researchers achieved constraints on cosmological parameters that are 3 to 8 times tighter, pointing toward a new standard for extracting information from galaxy surveys.

## How It Works

The Wavelet Scattering Transform borrows its architecture from deep learning, but with a twist: its internal filters are fixed, not learned. Think of it as a convolutional neural network where someone has already chosen the optimal lens prescription. The WST passes the galaxy density field through a series of wavelet convolutions (mathematically defined filters tuned to different spatial scales and orientations) and applies an absolute value operation at each layer. This cascade of filtering produces a compact set of numerical coefficients that characterize clustering at multiple scales, including non-Gaussian features the power spectrum ignores.

![Figure 1](figure:1)

Applying WST to real data is hard. Real galaxy surveys are far from clean, uniform snapshots of the sky. They carry **redshift-space distortions**, where galaxy peculiar velocities warp their apparent positions, along with irregular survey edges, systematic observational weights, and the **Alcock-Paczynski effect** (a geometric distortion that emerges when you assume the wrong cosmology to convert observed redshifts into physical distances). Valogiannis and Dvorkin carefully incorporated all of these effects, following the same rigorous pipeline used for standard power spectrum analyses.

To model how WST coefficients depend on cosmology, the team used the **ABACUSSUMMIT** simulation suite, one of the largest sets of N-body simulations ever produced. (N-body simulations track the gravitational interactions of billions of particles to model cosmic evolution.) They generated hundreds of galaxy mock catalogs matched to the BOSS CMASS sample, which consists of luminous red galaxies in the redshift range 0.46 < z < 0.60, varying cosmological parameters across the parameter space. Galaxy formation physics was absorbed into a **Halo Occupation Distribution (HOD)** model with 7 free parameters, averaged over so that uncertainties in how galaxies populate dark matter halos don't contaminate the cosmological inference.

With this emulator in hand, the team performed a full Bayesian likelihood analysis targeting four fundamental cosmological parameters:

- **ω_b**: the physical baryon density (the protons and neutrons that make up ordinary matter)
- **ω_c**: the physical cold dark matter density
- **n_s**: the scalar spectral index, describing the shape of primordial fluctuations
- **σ_8**: the amplitude of matter fluctuations

The Hubble constant was derived indirectly, anchored to the angular size of the sound horizon (the farthest distance pressure waves could travel in the early universe before atoms formed) as measured by the Planck satellite.

![Figure 2](figure:2)

## Why It Matters

Compared to the standard power spectrum analysis, the WST delivered posterior uncertainties 3 to 5 times smaller with flat priors, and 3 to 8 times smaller when a Big Bang Nucleosynthesis prior constrains ω_b. This is not a marginal improvement. It's the difference between a blurry photograph and a sharp one, wrung from the same underlying data.

![Figure 3](figure:3)

That gain matters for the next generation of galaxy surveys. Instruments like DESI, the Vera C. Rubin Observatory's LSST, Euclid, and the Nancy Grace Roman Space Telescope will map the universe with unprecedented precision over the next decade. They need statistical tools equal to the task.

The standard power spectrum has been the default for decades, but it leaves substantial cosmological information on the table. The WST offers a principled, interpretable alternative to black-box neural networks, one that can be validated and trusted for inference on real data. The authors are transparent that their results rest on certain approximations, including the choice of simulation suite and HOD model, but the magnitude of improvement is large enough to motivate serious investment in WST-based analyses.

There's a deeper point here, too. Galaxy surveys have always been information-rich in principle but information-poor in practice, because we lacked the statistical tools to access what gravity has written into the cosmic web. The WST reads that text directly, without requiring us to trust an inscrutable neural network to do the reading.

> **Bottom Line:** Applying the Wavelet Scattering Transform to real BOSS galaxy data for the first time, Valogiannis and Dvorkin obtain constraints on cosmological parameters 3–8 times tighter than the standard power spectrum, a result that could change how cosmologists analyze the next generation of galaxy surveys.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects modern machine learning methodology with observational cosmology, showing for the first time that AI-adjacent techniques can be applied rigorously to real galaxy survey data with major gains in constraining power.

- **Impact on Artificial Intelligence:** The WST provides an interpretable, physics-motivated alternative to black-box deep learning for scientific data analysis. Fixed, mathematically principled network architectures can outperform traditional statistical estimators while remaining fully understandable.

- **Impact on Fundamental Interactions:** The dramatic improvement in constraints on σ_8 and n_s opens a path toward resolving outstanding cosmological tensions and probing dark matter, dark energy, and neutrino masses with existing survey data.

- **Outlook and References:** Future work will refine the simulation-based modeling and extend the WST framework to next-generation surveys like DESI and Euclid; see [arXiv:2204.13717](https://arxiv.org/abs/2204.13717) for the full analysis.

## Original Paper Details
- **Title:** Going Beyond the Galaxy Power Spectrum: an Analysis of BOSS Data with Wavelet Scattering Transforms
- **arXiv ID:** 2204.13717
- **Authors:** ["Georgios Valogiannis", "Cora Dvorkin"]
- **Abstract:** We perform the first application of the wavelet scattering transform (WST) to actual galaxy observations, through a WST analysis of the BOSS DR12 CMASS dataset. We included the effects of redshift-space anisotropy, non-trivial survey geometry, systematic weights, and the Alcock-Paczynski distortion effect, following the commonly adopted steps for the power spectrum analysis. In order to capture the cosmological dependence of the WST, we use galaxy mocks obtained from the state-of-the-art ABACUSSUMMIT simulations, tuned to match the anisotropic correlation function of the BOSS CMASS sample in the redshift range $0.46<z<0.60$. Using our model for the WST coefficients, as well as for the first 2 multipoles of the galaxy power spectrum, that we use as reference, we perform a likelihood analysis of the CMASS data. We obtain the posterior probability distributions of 4 cosmological parameters, $\{ω_b,ω_c,n_s,σ_8\}$, as well as the Hubble constant, derived from a fixed value of the angular size of the sound horizon at last scattering measured by the Planck satellite, all of which are marginalized over the 7 nuisance parameters of the Halo Occupation Distribution model. The WST is found to deliver a substantial improvement in the values of the predicted $1σ$ errors compared to the regular power spectrum, which are tighter by a factor of $3-5$ in the case of flat and uninformative priors and by a factor of $3-8$, when a Big Bang Nucleosynthesis prior is applied on the value of $ω_b$. Our results are investigative and subject to certain approximations, which we discuss in the text.
