---
abstract: Cosmological analyses of redshift space clustering data are primarily based
  on using luminous ``red'' galaxies (LRGs) and ``blue'' emission line galaxies (ELGs)
  to trace underlying dark matter. Using the large high-fidelity high-resolution MillenniumTNG
  (MTNG) and Astrid simulations, we study these galaxies with the effective field
  theory (EFT)-based field level forward model. We confirm that both red and blue
  galaxies can be accurately modeled with EFT at the field level and their parameters
  match those of the phenomenological halo-based models. Specifically, we consider
  the state of the art Halo Occupation Distribution (HOD) and High Mass Quenched (HMQ)
  models for the red and blue galaxies, respectively. Our results explicitly confirm
  the validity of the halo-based models on large scales beyond the two-point statistics.
  In addition, we validate the field-level HOD/HMQ-based priors for EFT full-shape
  analysis. We find that the local bias parameters of the ELGs are in tension with
  the predictions of the LRG-like HOD models and present a simple analytic argument
  explaining this phenomenology. We also confirm that ELGs exhibit weaker non-linear
  redshift-space distortions (``fingers-of-God''), suggesting that a significant fraction
  of their data should be perturbative. We find that the response of EFT parameters
  to galaxy selection is sensitive to assumptions about baryonic feedback, suggesting
  that a detailed understanding of feedback processes is necessary for robust predictions
  of EFT parameters. Finally, using neural density estimation based on paired HOD-EFT
  parameter samples, we obtain optimal HOD models that reproduce the clustering of
  Astrid and MTNG galaxies.
arxivId: '2412.01888'
arxivUrl: https://arxiv.org/abs/2412.01888
authors:
- Mikhail M. Ivanov
- Carolina Cuesta-Lazaro
- Andrej Obuljen
- Michael W. Toomey
- Yueying Ni
- Sownak Bose
- Boryana Hadzhiyska
- César Hernández-Aguayo
- Lars Hernquist
- Rahul Kannan
- Volker Springel
concepts:
- effective field theory
- cosmological simulation
- galaxy-halo connection models
- galaxy bias expansion
- density estimation
- redshift-space distortions
- dark matter
- bayesian inference
- simulation-based inference
- posterior estimation
- baryonic feedback
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2412_01888/figure_1.png
- /iaifi-research-blog/figures/2412_01888/figure_1.png
- /iaifi-research-blog/figures/2412_01888/figure_2.png
- /iaifi-research-blog/figures/2412_01888/figure_2.png
- /iaifi-research-blog/figures/2412_01888/figure_3.png
- /iaifi-research-blog/figures/2412_01888/figure_3.png
pdfUrl: https://arxiv.org/pdf/2412.01888v1
published: '2024-12-02T19:00:00+00:00'
theme: Astrophysics
title: 'The Millennium and Astrid galaxies in effective field theory: comparison with
  galaxy-halo connection models at the field level'
wordCount: 1130
---

## The Big Picture

Imagine trying to understand the entire ocean by studying a handful of floats drifting on its surface. That's roughly the challenge cosmologists face when using galaxies to map the invisible dark matter scaffolding that structures our Universe. The galaxies we observe, catalogued by surveys like DESI and BOSS, are just tracers, like dye injected into a river.

To extract the fundamental physics hidden in how galaxies clump together, we need accurate models connecting what we see to what's really there. Those models come in three main flavors. **Hydrodynamical simulations** directly compute how gas, stars, and dark matter co-evolve from the Big Bang forward: accurate but computationally brutal. **Effective field theory (EFT)** describes galaxy clustering on large scales using a small set of parameters, much like describing a gas without tracking every individual molecule. And **Halo Occupation Distribution (HOD) models** are empirical recipes specifying how many galaxies inhabit a given clump, or "halo," of dark matter.

HOD models are cheap, flexible, and widely used. But nobody had rigorously checked whether HOD and EFT descriptions agree at the deepest level, or whether this holds for both "red" old elliptical galaxies (**Luminous Red Galaxies**, or LRGs) and "blue" star-forming ones (**Emission Line Galaxies**, or ELGs).

Using two powerful cosmological simulations, MillenniumTNG and Astrid, a team of IAIFI researchers confirmed that EFT accurately describes both galaxy types at the field level, validated HOD-based priors used in precision cosmology analyses, and applied neural density estimation to extract optimal galaxy-halo connection models.

> **Key Insight:** Both red and blue galaxies can be faithfully described by effective field theory at the field level, and EFT parameters extracted from full hydrodynamical simulations are consistent with those from HOD models, but only when baryonic feedback physics is properly accounted for.

## How It Works

The researchers worked with two simulations. **MillenniumTNG (MTNG)** combines the IllustrisTNG galaxy formation model with a gigantic simulation volume. **Astrid** uses a different galaxy formation model, in particular a different treatment of **AGN feedback** (the energetic jets and winds driven by supermassive black holes), providing a cross-check on how sensitive results are to uncertain physics.

![Figure 1](figure:1)

From each simulation, the team selected galaxy samples mimicking real surveys: LRGs matching BOSS selection criteria and ELGs matching DESI targets. They then applied the EFT field-level forward model, a technique that operates directly on the full three-dimensional map of galaxy positions rather than compressing it into summary statistics like the **power spectrum** (a measure of how strongly galaxies cluster at different scales).

Working at the field level cancels much of the **cosmic variance**, the statistical noise that comes from having only one observable Universe. That normally plagues analyses of small simulation volumes. Here, it meant the team could get high-precision EFT parameter measurements even from boxes that would otherwise be too small.

The EFT model parametrizes galaxy bias (how galaxies trace the underlying dark matter) using a hierarchy of terms:

- **Local bias** ($b_1$, $b_2$): how galaxy density responds to local matter density
- **Tidal bias** ($b_{\mathcal{G}_2}$): sensitivity to the gravitational tidal field
- **Higher-derivative terms**: dependence on environment beyond the local density
- **Stochastic terms**: shot noise and small-scale physics below the model's resolution

These parameters were compared against predictions from the standard HOD model for LRGs and the **High Mass Quenched (HMQ) model** for ELGs. The HMQ model was designed specifically for blue, star-forming galaxies that tend to avoid the densest halo environments.

![Figure 2](figure:2)

The comparison showed strong agreement, with some important caveats. LRG bias parameters match HOD predictions well. For ELGs, local bias parameters are systematically offset from what an LRG-like model would predict. The team traced this to a simple physical explanation: blue galaxies preferentially live at halo outskirts rather than centers, and that different spatial distribution naturally gives them different large-scale bias parameters. Not a numerical quirk, but real physics about where star-forming galaxies live.

## Why It Matters

The practical stakes are high. DESI is already collecting spectra of tens of millions of ELGs, and extracting cosmological parameters from that data (the Universe's expansion history, tests of general relativity, constraints on dark energy) requires accurate forward models and well-calibrated priors on bias parameters.

This paper validates the HOD-based EFT priors now used in **full-shape analyses** of DESI data, where fits use the complete shape of the clustering signal across all scales simultaneously rather than just broad summary statistics. Wrong priors would bias inferences about the Universe's fundamental properties.

![Figure 3](figure:3)

There's also a useful result on **fingers-of-God**, the smearing of galaxy clustering along the line of sight caused by random motions inside halos. LRGs sit near dense halo centers and experience strong fingers-of-God effects that push the EFT perturbative framework to its limits. ELGs show weaker effects. That means a larger fraction of ELG data can be modeled perturbatively, potentially extending EFT analyses to smaller scales and yielding tighter cosmological constraints.

The team also found that EFT parameter values depend sensitively on the assumed baryonic feedback model, the energetic outflows from supernovae and AGN that reshape how galaxies populate their halos. As surveys push to higher precision, this baryonic physics will matter more, not less.

To close the loop, the team used **neural density estimation** (a machine learning technique for learning probability distributions from simulation samples) to find which HOD parameters best reproduce field-level clustering in both simulations. The workflow goes: start from hydro simulations, extract EFT parameters, compare with HOD predictions, then use neural inference to identify which HOD configurations reproduce the full three-dimensional galaxy field. It connects simulation-based inference with perturbative theory in a way that should generalize to other precision cosmology problems.

> **Bottom Line:** Red and blue galaxies both fit neatly into the EFT framework, but ELGs play by subtly different rules than LRGs. The difference traces back to where blue galaxies live in their halos, and it matters for cosmological analyses of current and future galaxy surveys.

## IAIFI Research Highlights

**Interdisciplinary Research Achievement:** This work combines hydrodynamical simulations, perturbative field theory, and neural density estimation into a unified framework connecting galaxy observations to fundamental cosmological parameters.

**Impact on Artificial Intelligence:** The team applied neural density estimation to learn the mapping between HOD parameters and EFT bias parameters from paired simulation samples, showing how machine learning can extract optimal physical models from high-dimensional simulation data.

**Impact on Fundamental Interactions:** By validating EFT bias priors against two independent hydrodynamical simulations with distinct galaxy formation physics, this work puts the theoretical foundation for extracting cosmological parameters (including dark energy and the neutrino mass sum) from surveys like DESI on firmer ground.

**Outlook and References:** Future work will extend these comparisons to higher redshifts and smaller scales, and test the framework against actual DESI data; see [arXiv:2412.01888](https://arxiv.org/abs/2412.01888) for the full paper.

## Original Paper Details
- **Title:** The Millennium and Astrid galaxies in effective field theory: comparison with galaxy-halo connection models at the field level
- **arXiv ID:** 2412.01888
- **Authors:** ["Mikhail M. Ivanov", "Carolina Cuesta-Lazaro", "Andrej Obuljen", "Michael W. Toomey", "Yueying Ni", "Sownak Bose", "Boryana Hadzhiyska", "César Hernández-Aguayo", "Lars Hernquist", "Rahul Kannan", "Volker Springel"]
- **Abstract:** Cosmological analyses of redshift space clustering data are primarily based on using luminous ``red'' galaxies (LRGs) and ``blue'' emission line galaxies (ELGs) to trace underlying dark matter. Using the large high-fidelity high-resolution MillenniumTNG (MTNG) and Astrid simulations, we study these galaxies with the effective field theory (EFT)-based field level forward model. We confirm that both red and blue galaxies can be accurately modeled with EFT at the field level and their parameters match those of the phenomenological halo-based models. Specifically, we consider the state of the art Halo Occupation Distribution (HOD) and High Mass Quenched (HMQ) models for the red and blue galaxies, respectively. Our results explicitly confirm the validity of the halo-based models on large scales beyond the two-point statistics. In addition, we validate the field-level HOD/HMQ-based priors for EFT full-shape analysis. We find that the local bias parameters of the ELGs are in tension with the predictions of the LRG-like HOD models and present a simple analytic argument explaining this phenomenology. We also confirm that ELGs exhibit weaker non-linear redshift-space distortions (``fingers-of-God''), suggesting that a significant fraction of their data should be perturbative. We find that the response of EFT parameters to galaxy selection is sensitive to assumptions about baryonic feedback, suggesting that a detailed understanding of feedback processes is necessary for robust predictions of EFT parameters. Finally, using neural density estimation based on paired HOD-EFT parameter samples, we obtain optimal HOD models that reproduce the clustering of Astrid and MTNG galaxies.
