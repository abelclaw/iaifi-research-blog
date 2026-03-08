---
abstract: Characterizing the host galaxies of astrophysical transients is important
  to many areas of astrophysics, including constraining the progenitor systems of
  core-collapse supernovae, correcting Type Ia supernova distances, and probabilistically
  classifying transients without photometric or spectroscopic data. Given the increasing
  transient discovery rate in the coming years, there is substantial utility in providing
  public, transparent, reproducible, and automatic characterization for large samples
  of transient host galaxies. Here we present Blast, a web application that ingests
  live streams of transient alerts, matches transients to their host galaxies, and
  performs photometry on coincident archival imaging data of the host galaxy. The
  photometry is then used to infer both global host-galaxy properties and galaxy properties
  within 2 kpc of the transient location by using the Prospector Bayesian inference
  framework, with an acceleration in evaluation speed achieved via simulation-based
  inference. Blast provides host-galaxy properties to users via a web browser or an
  application program interface. The software can be extended to support alternative
  photometric or SED-fitting algorithms, and can be scaled via an asynchronous worker
  queue across multiple compute nodes to handle the processing of large volumes of
  transient alerts for upcoming transient surveys. Blast has been ingesting newly
  discovered transients from the Transient Name Server since mid-2024, and has currently
  measured SED parameters for more than 6000 transients. The service is publicly available
  at https://blast.scimma.org/.
arxivId: '2410.17322'
arxivUrl: https://arxiv.org/abs/2410.17322
authors:
- D. O. Jones
- P. McGill
- T. A. Manning
- A. Gagliano
- B. Wang
- D. A. Coulter
- R. J. Foley
- G. Narayan
- V. A. Villar
- L. Braff
- A. W. Engel
- D. Farias
- Z. Lai
- K. Loertscher
- J. Kutcka
- S. Thorp
- J. Vazquez
concepts:
- transient host matching
- sed fitting
- simulation-based inference
- bayesian inference
- posterior estimation
- galaxy classification
- surrogate modeling
- supernova classification
- scientific workflows
- uncertainty quantification
- scalability
- anomaly detection
figures:
- /iaifi-research-blog/figures/2410_17322/figure_1.png
- /iaifi-research-blog/figures/2410_17322/figure_2.png
- /iaifi-research-blog/figures/2410_17322/figure_3.png
pdfUrl: https://arxiv.org/pdf/2410.17322v1
published: '2024-10-22T18:00:06+00:00'
theme: Astrophysics
title: 'Blast: a Web Application for Characterizing the Host Galaxies of Astrophysical
  Transients'
wordCount: 989
---

## The Big Picture

Imagine a detective who can only study crime scenes years after the fact, with no witnesses, no surveillance footage, just the neighborhood. That's the challenge astronomers face when a star explodes somewhere in the universe. The explosion itself, called a **transient**, may last days or weeks before fading forever. But the galaxy that hosted it remains, and it holds clues.

A host galaxy's age, mass, star formation rate, and chemical composition act like a fingerprint for the kinds of stars it breeds and the kinds of deaths those stars die. A supernova in an old, red, heavy-element-rich elliptical galaxy tells a very different story than one in a young, blue, star-forming spiral.

Astronomers have known this for decades. But measuring those properties at scale has been a logistical nightmare. Modern sky surveys now discover over 20,000 transients per year, a number set to explode further when the Vera C. Rubin Observatory comes fully online. The field needed automation badly.

**Blast** is a publicly accessible web application that automatically ingests transient alerts, identifies the host galaxy, measures its light across multiple wavelengths, and infers its physical properties, all without human intervention.

> Blast automates the full pipeline from transient detection to host galaxy characterization, combining archival multi-wavelength imaging with Bayesian inference accelerated by machine learning to process thousands of events in near real time.

## How It Works

The pipeline starts the moment a new transient is reported. Blast monitors the **Transient Name Server (TNS)**, a central clearinghouse where astronomers worldwide log new detections. When a new event appears, Blast runs a four-stage automated process:

1. **Host matching** — Blast identifies which galaxy most plausibly hosted the transient using a probabilistic framework that accounts for angular separation and galaxy brightness.
2. **Photometry** — The system queries archival imaging databases spanning ultraviolet (GALEX), optical (Pan-STARRS, SDSS, DESI Legacy Surveys), and infrared (2MASS, WISE) wavelengths, measuring the galaxy's brightness in each band.
3. **SED fitting** — Those measurements define the galaxy's **spectral energy distribution (SED)**, a fingerprint of its light across wavelengths, which Blast feeds into a physical model to infer stellar mass, star formation rate, and metallicity.
4. **Local photometry** — Blast also measures properties *within 2 kiloparsecs (roughly 6,500 light-years) of the transient's exact location*, not just the galaxy as a whole. That local neighborhood often matters more for understanding what kind of star exploded.

![Figure 1](figure:1)

The SED fitting step is where AI earns its place. Blast uses **Prospector**, a Bayesian inference framework that estimates the most probable physical explanation for observed data along with uncertainty ranges. But standard Prospector runs can take hours per galaxy. Far too slow for thousands of transients.

To fix this, the team incorporated **simulation-based inference (SBI)**. A neural network is trained on a library of simulated galaxy SEDs and their corresponding physical parameters. Instead of running a costly sampler from scratch each time, the trained network estimates full probability distributions in seconds. The accuracy holds up. The speed gain changes everything.

![Figure 2](figure:2)

The system is built for scale. Blast uses an **asynchronous worker queue**, a task management architecture where jobs are distributed across multiple compute nodes and processed independently, so it absorbs sudden spikes in transient alerts without grinding to a halt. Users access results through a web browser or a programmatic **API**, making it easy to plug Blast's outputs into classification pipelines, cosmological analyses, or follow-up scheduling tools.

![Figure 3](figure:3)

## Why It Matters

Host galaxy properties touch several subfields at once. **Type Ia supernovae** are stellar explosions that release a nearly consistent amount of energy, making them the cosmic "standard candles" that anchored the discovery of dark energy. But they are systematically affected by their host environments. Supernovae in more massive, chemically enriched galaxies appear slightly brighter after standard corrections, skewing cosmological inferences. Blast provides a scalable way to apply host-based corrections across samples of thousands, rather than the hundreds that previous dedicated efforts managed.

For **core-collapse supernovae**, the violent deaths of the most massive stars, the link between host environment and explosion mechanism is still being worked out. Different types of stellar deaths, from stripped-envelope supernovae to gamma-ray bursts, preferentially occur in different galactic environments. Mapping those preferences requires population-level statistics, and doing that by hand doesn't scale.

With Blast cataloging host properties for every newly reported transient, statistical analyses that once required years of targeted campaigns become feasible within months. And as classifiers increasingly fold host properties into their probability estimates, real-time decisions about which transients deserve precious telescope time get sharper.

> Blast transforms host galaxy characterization from a labor-intensive afterthought into automated infrastructure, delivering physical galaxy properties for 6,000+ transients already and positioned to handle the coming flood from next-generation surveys.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** Blast directly connects machine learning and observational astrophysics by embedding simulation-based inference into an automated pipeline operating on live data streams from real sky surveys.

- **Impact on Artificial Intelligence:** The application of simulation-based inference to accelerate Bayesian SED fitting shows how neural posterior estimators can replace computationally expensive samplers in scientific workflows without sacrificing inference quality.

- **Impact on Fundamental Interactions:** By enabling systematic, unbiased host galaxy characterization at scale, Blast strengthens the statistical foundation for Type Ia supernova cosmology, supporting precision measurements of dark energy and the Hubble constant.

- **Outlook and References:** With the Vera Rubin Observatory's LSST expected to deliver millions of transient alerts per year, Blast's architecture positions it as essential infrastructure for the next decade of time-domain astronomy; the paper is available at [arXiv:2410.17322](https://arxiv.org/abs/2410.17322).
