---
abstract: Machine learning can play a powerful role in inferring missing line-of-sight
  velocities from astrometry in surveys such as Gaia. In this paper, we apply a neural
  network to Gaia Early Data Release 3 (EDR3) and obtain line-of-sight velocities
  and associated uncertainties for ~92 million stars. The network, which takes as
  input a star's parallax, angular coordinates, and proper motions, is trained and
  validated on ~6.4 million stars in Gaia with complete phase-space information. The
  network's uncertainty on its velocity prediction is a key aspect of its design;
  by properly convolving these uncertainties with the inferred velocities, we obtain
  accurate stellar kinematic distributions. As a first science application, we use
  the new network-completed catalog to identify candidate stars that belong to the
  Milky Way's most recent major merger, Gaia-Sausage-Enceladus (GSE). We present the
  kinematic, energy, angular momentum, and spatial distributions of the ~450,000 GSE
  candidates in this sample, and also study the chemical abundances of those with
  cross matches to GALAH and APOGEE. The network's predictive power will only continue
  to improve with future Gaia data releases as the training set of stars with complete
  phase-space information grows. This work provides a first demonstration of how to
  use machine learning to exploit high-dimensional correlations on data to infer line-of-sight
  velocities, and offers a template for how to train, validate and apply such a neural
  network when complete observational data is not available.
arxivId: '2205.12278'
arxivUrl: https://arxiv.org/abs/2205.12278
authors:
- Adriana Dropulic
- Hongwan Liu
- Bryan Ostdiek
- Mariangela Lisanti
concepts:
- uncertainty quantification
- stellar phase-space inference
- regression
- galactic archaeology
- high-dimensional correlation learning
- semi-supervised learning
- model validation
- anomaly detection
- transfer learning
- dark matter
- cosmological simulation
figures:
- /iaifi-research-blog/figures/2205_12278/figure_1.png
- /iaifi-research-blog/figures/2205_12278/figure_2.png
- /iaifi-research-blog/figures/2205_12278/figure_3.png
pdfUrl: https://arxiv.org/pdf/2205.12278v1
published: '2022-05-24T18:00:01+00:00'
theme: Astrophysics
title: Revealing the Milky Way's Most Recent Major Merger with a Gaia EDR3 Catalog
  of Machine-Learned Line-of-Sight Velocities
wordCount: 1052
---

## The Big Picture

Imagine reconstructing a car crash from a partial recording. You can see where the vehicles ended up, but the footage of the impact itself is missing. Galactic archaeologists face a similar challenge. The Milky Way has consumed dozens of smaller galaxies over its lifetime, and the scattered wreckage of those collisions still drifts through our galaxy today, encoded in the motions of ancient stars.

To read that record, astronomers need all three dimensions of each star's velocity. But there's a catch: they can usually only measure two directly.

The European Space Agency's *Gaia* satellite has mapped the positions and motions of over a billion stars with extraordinary precision. Yet for most of them, one key measurement, the **line-of-sight velocity** (how fast a star moves directly toward or away from us), remains out of reach. Less than 1% of *Gaia*'s catalog includes this measurement, leaving the vast majority with an incomplete picture of their motion.

Researchers at Princeton and Harvard trained a neural network to fill that gap. It inferred line-of-sight velocities for 92 million stars, and the resulting catalog revealed nearly 450,000 survivors from the Milky Way's most dramatic collision in recent cosmic history.

> **Key Insight:** By training a neural network on the minority of stars with complete velocity data, the team recovered the full three-dimensional motion of 92 million more, revealing nearly 450,000 relics from the ancient galaxy that crashed into the Milky Way roughly 8–10 billion years ago.

## How It Works

The core idea rests on a basic property of stellar populations: stars that share a common origin or environment also share correlated motions. If you know where a star sits in the sky, how far away it is, and how it drifts sideways over time, a well-trained network can make a reasonable guess about the missing speed along the line of sight.

The network takes five inputs per star:

- **Angular coordinates** — where the star sits on the sky
- **Parallax** — its distance, derived from the slight shift in apparent position as Earth orbits the Sun
- **Proper motions** — the sideways drift across the sky over time (two components)

Training used roughly 6.4 million *Gaia* EDR3 stars that already had all six velocity components measured, a dataset large enough to capture the correlations connecting these observables to the hidden velocity component.

![Figure 1](figure:1)

What sets this work apart is that the network doesn't just output a predicted velocity. It also outputs an **uncertainty estimate**, its own confidence interval on each prediction. For any individual star, five observables genuinely cannot pin down the line-of-sight speed with high precision. But by folding those uncertainties into the predictions mathematically, the team reconstructed accurate statistical distributions across entire stellar populations. The whole is more trustworthy than any single part.

The team validated their approach by holding out a subset of stars with known velocities and confirming that the inferred distributions closely matched ground truth.

## Why It Matters

With 92 million newly completed stellar records in hand, the researchers turned to one of galactic archaeology's most celebrated finds: **Gaia-Sausage-Enceladus (GSE)**, the last major galaxy to merge with the Milky Way. GSE was discovered in 2018 through the distinctive "sausage" shape its stars trace in velocity space. The collision happened roughly 8–10 billion years ago, when the original host galaxy (somewhere between 100 million and a billion solar masses) was torn apart by the Milky Way's gravity.

![Figure 2](figure:2)

The identification strategy relies on the debris' distinctive orbital signature. GSE stars move on highly **eccentric, radial orbits**: long, stretched paths that plunge deep toward the galactic center and back out again, with little of the rotational motion typical of stars born inside the Milky Way. By selecting stars with high orbital eccentricity and examining how their orbital energies and angular momenta cluster, the team isolated roughly 450,000 GSE candidates. That's nearly twenty times more than the 6D *Gaia* dataset alone could provide.

Chemical fingerprinting backs up the identification. Cross-matching with spectroscopic surveys GALAH and APOGEE revealed a **metallicity distribution** peaking near [Fe/H] ≈ −1.4 to −1.2 (lower values mean fewer heavy elements relative to the Sun). That's what you'd expect from a galaxy that stopped forming stars after being stripped apart billions of years ago. Kinematics, spatial distribution, and chemistry all tell the same story.

![Figure 3](figure:3)

The approach generalizes well beyond this single merger. Train on the fraction of data with complete information, validate carefully, deploy to recover physics hiding in incomplete datasets. Any large sky survey capturing partial motion measurements could use the same playbook.

The method should also improve over time. *Gaia*'s upcoming data releases are expected to add roughly 30 million more stars with measured line-of-sight velocities, which will sharpen predictions further. Future applications could probe other merger events in the Milky Way's history with similar depth, and potentially map the dark matter distribution by studying how merger debris responds to the galactic gravitational potential.

> **Bottom Line:** A neural network trained on 6.4 million stars recovered the velocity information of 92 million more, producing the largest catalog of Gaia-Sausage-Enceladus candidates ever assembled and setting a template for machine-learning-powered galactic archaeology at scale.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects deep learning and galactic astrophysics, using a neural network trained on incomplete observational data to recover six-dimensional phase-space information and reveal a major chapter in the Milky Way's merger history.

- **Impact on Artificial Intelligence:** The team's uncertainty-aware neural network shows that probabilistic inference from high-dimensional correlations, not just point prediction, is essential for reliable science from incomplete datasets. The approach generalizes to other survey-scale applications.

- **Impact on Fundamental Interactions:** By identifying nearly 450,000 Gaia-Sausage-Enceladus candidate stars, the work provides the most statistically powerful sample yet for studying the kinematics, energetics, and chemical abundances of the Milky Way's last major merger event.

- **Outlook and References:** Future *Gaia* data releases will expand the training set and sharpen predictions, enabling increasingly detailed reconstructions of the Milky Way's assembly history. The paper and its public catalog are available at [arXiv:2205.12278](https://arxiv.org/abs/2205.12278).

## Original Paper Details
- **Title:** Revealing the Milky Way's Most Recent Major Merger with a Gaia EDR3 Catalog of Machine-Learned Line-of-Sight Velocities
- **arXiv ID:** 2205.12278
- **Authors:** ["Adriana Dropulic", "Hongwan Liu", "Bryan Ostdiek", "Mariangela Lisanti"]
- **Abstract:** Machine learning can play a powerful role in inferring missing line-of-sight velocities from astrometry in surveys such as Gaia. In this paper, we apply a neural network to Gaia Early Data Release 3 (EDR3) and obtain line-of-sight velocities and associated uncertainties for ~92 million stars. The network, which takes as input a star's parallax, angular coordinates, and proper motions, is trained and validated on ~6.4 million stars in Gaia with complete phase-space information. The network's uncertainty on its velocity prediction is a key aspect of its design; by properly convolving these uncertainties with the inferred velocities, we obtain accurate stellar kinematic distributions. As a first science application, we use the new network-completed catalog to identify candidate stars that belong to the Milky Way's most recent major merger, Gaia-Sausage-Enceladus (GSE). We present the kinematic, energy, angular momentum, and spatial distributions of the ~450,000 GSE candidates in this sample, and also study the chemical abundances of those with cross matches to GALAH and APOGEE. The network's predictive power will only continue to improve with future Gaia data releases as the training set of stars with complete phase-space information grows. This work provides a first demonstration of how to use machine learning to exploit high-dimensional correlations on data to infer line-of-sight velocities, and offers a template for how to train, validate and apply such a neural network when complete observational data is not available.
