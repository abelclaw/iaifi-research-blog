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

Imagine reconstructing a car crash from a partial recording — you can see where the vehicles ended up, but the footage of the impact itself is missing. Galactic archaeologists face a similar challenge. The Milky Way has consumed dozens of smaller galaxies over its lifetime, and the scattered wreckage of those collisions still drifts through our galaxy today, encoded in the motions of ancient stars.

To read that record, astronomers need all three dimensions of each star's velocity. But there's a catch: they can usually only measure two directly.

The European Space Agency's *Gaia* satellite has mapped the positions and motions of over a billion stars with extraordinary precision. Yet for most of them, one crucial measurement — the **line-of-sight velocity**, how fast a star moves directly toward or away from us — remains out of reach. Less than 1% of *Gaia*'s catalog has this measurement, leaving the vast majority with an incomplete picture of their motion.

Researchers at Princeton and Harvard deployed a neural network to fill that gap — inferring line-of-sight velocities for 92 million stars and using the resulting catalog to uncover nearly 450,000 survivors from the Milky Way's most dramatic collision in recent cosmic history.

> **Key Insight:** By training a neural network on the minority of stars with complete velocity data, the team unlocked the full three-dimensional motion of 92 million more stars — revealing nearly 450,000 relics from the ancient galaxy that crashed into the Milky Way roughly 8–10 billion years ago.

## How It Works

The core idea exploits a fundamental property of stellar populations: stars that share a common origin or environment also share correlated motions. If you know where a star sits in the sky, how far away it is, and how it drifts sideways over time, a well-trained network can make an educated inference about the missing speed along the line of sight.

The network takes five inputs per star:

- **Angular coordinates** — where the star sits on the sky
- **Parallax** — its distance, derived from the slight shift in apparent position as Earth orbits the Sun
- **Proper motions** — the sideways drift across the sky over time (two components)

It was trained on roughly 6.4 million *Gaia* EDR3 stars that already had all six velocity components measured — a dataset rich enough to capture the complex correlations connecting these observables to the hidden velocity component.

![Figure 1](/iaifi-research-blog/figures/2205_12278/figure_1.png)

A critical design choice sets this work apart: the network doesn't just output a predicted velocity — it also outputs an **uncertainty estimate**, its own confidence interval on each prediction. For any individual star, five observables genuinely cannot pin down the line-of-sight speed with high precision. But by mathematically folding those uncertainties into the predictions, the team reconstructs accurate statistical distributions across entire stellar populations. The whole is more trustworthy than any single part.

Validation was rigorous: the team held out a subset of stars with known velocities and confirmed that the inferred distributions closely matched ground truth.

## Why It Matters

Armed with 92 million newly enriched stellar records, the researchers turned to one of galactic archaeology's most celebrated finds: **Gaia-Sausage-Enceladus (GSE)**, the last major galaxy to merge with the Milky Way. Discovered in 2018 through the distinctive "sausage" shape its stars trace in velocity space, GSE collided with our galaxy roughly 8–10 billion years ago, when its original host galaxy — a body with 100 million to a billion solar masses — was torn apart by the Milky Way's gravity.

![Figure 2](/iaifi-research-blog/figures/2205_12278/figure_2.png)

The identification strategy exploits the debris' distinctive orbital signature. GSE stars move on highly **eccentric, radial orbits** — long, stretched paths that plunge them deep toward the galactic center and back out again, with little of the rotational motion that characterizes stars born inside the Milky Way. By selecting stars with high orbital eccentricity and examining how their orbital energies and angular momenta cluster, the team isolated roughly 450,000 GSE candidates. That's nearly twenty times more than the 6D *Gaia* dataset alone could provide.

Chemical fingerprinting confirms the identification. Cross-matching with spectroscopic surveys GALAH and APOGEE, the researchers found a **metallicity distribution** — the abundance of heavy elements — peaking near [Fe/H] ≈ −1.4 to −1.2 (where lower values indicate fewer heavy elements relative to the Sun). That's the telltale signature of a galaxy that stopped forming stars when it was stripped apart billions of years ago. Kinematics, spatial distribution, and chemistry all tell the same story.

![Figure 3](/iaifi-research-blog/figures/2205_12278/figure_3.png)

The broader implications extend well beyond this single merger. This work establishes a reusable template: train on the fraction of data with complete information, validate carefully, and deploy to recover physics hiding in incomplete datasets. Any large sky survey capturing partial motion measurements could benefit from the same approach.

The method will also compound its own value. *Gaia*'s upcoming data releases are expected to add roughly 30 million more stars with measured line-of-sight velocities, sharpening predictions further. Future applications could probe other merger events in the Milky Way's history with similar depth, and potentially map the dark matter distribution by studying how merger debris is sculpted by the galactic gravitational potential.

> **Bottom Line:** A neural network trained on 6.4 million stars just unlocked the velocity information of 92 million more, delivering the largest catalog of Gaia-Sausage-Enceladus candidates ever assembled — and laying the groundwork for machine-learning-powered galactic archaeology at unprecedented scale.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges deep learning and galactic astrophysics, using a neural network trained on incomplete observational data to recover six-dimensional phase-space information and reveal a major chapter in the Milky Way's merger history.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The team's uncertainty-aware neural network demonstrates that probabilistic inference from high-dimensional correlations — not just point prediction — is essential for reliable science from incomplete datasets, offering a generalizable template for survey-scale applications.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By identifying nearly 450,000 Gaia-Sausage-Enceladus candidate stars, the work provides the most statistically powerful sample yet for studying the kinematics, energetics, and chemical abundances of the Milky Way's last major merger event.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future *Gaia* data releases will expand the training set and sharpen predictions, enabling increasingly detailed reconstructions of the Milky Way's assembly history; the paper and its public catalog are available at arXiv:2205.12278.</span></div></div>
</div>
