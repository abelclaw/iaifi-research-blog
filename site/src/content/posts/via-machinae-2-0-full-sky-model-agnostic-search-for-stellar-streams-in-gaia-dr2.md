---
abstract: We present an update to Via Machinae, an automated stellar stream-finding
  algorithm based on the deep learning anomaly detector ANODE. Via Machinae identifies
  stellar streams within Gaia, using only angular positions, proper motions, and photometry,
  without reference to a model of the Milky Way potential for orbit integration or
  stellar distances. This new version, Via Machinae 2.0, includes many improvements
  and refinements to nearly every step of the algorithm, that altogether result in
  more robust and visually distinct stream candidates than our original formulation.
  In this work, we also provide a quantitative estimate of the false positive rate
  of Via Machinae 2.0 by applying it to a simulated Gaia-mock catalog based on Galaxia,
  a smooth model of the Milky Way that does not contain substructure or stellar streams.
  Finally, we perform the first full-sky search for stellar streams with Via Machinae
  2.0, identifying 102 streams at high significance within the Gaia Data Release 2,
  of which only 10 have been previously identified. While follow-up observations for
  further confirmation are required, taking into account the false positive rate presented
  in this work, we expect approximately 90 of these stream candidates to correspond
  to real stellar structures.
arxivId: '2303.01529'
arxivUrl: https://arxiv.org/abs/2303.01529
authors:
- David Shih
- Matthew R. Buckley
- Lina Necib
concepts:
- stellar streams
- anomaly detection
- normalizing flows
- model-agnostic stream search
- density estimation
- likelihood ratio
- signal detection
- novelty detection
- simulation-based inference
- clustering
- dark matter
- out-of-distribution detection
figures:
- /iaifi-research-blog/figures/2303_01529/figure_1.png
- /iaifi-research-blog/figures/2303_01529/figure_1.png
- /iaifi-research-blog/figures/2303_01529/figure_2.png
- /iaifi-research-blog/figures/2303_01529/figure_2.png
- /iaifi-research-blog/figures/2303_01529/figure_3.png
- /iaifi-research-blog/figures/2303_01529/figure_3.png
pdfUrl: https://arxiv.org/pdf/2303.01529v1
published: '2023-03-02T19:00:08+00:00'
theme: Astrophysics
title: 'Via Machinae 2.0: Full-Sky, Model-Agnostic Search for Stellar Streams in Gaia
  DR2'
wordCount: 940
---

## The Big Picture

Imagine trying to find a single thread unraveling from a sweater, except the sweater is our entire galaxy, contains a billion stars, and the thread is hundreds of light-years long. That's what astronomers are up against when they hunt for **stellar streams**: faint ribbons of stars torn from ancient **globular clusters** (tight balls of hundreds of thousands of old stars) and **dwarf galaxies** (small, faint satellite galaxies) as they spiral into the Milky Way's gravitational grip.

These streams are more than cosmic fossils. They encode the merger history of our galaxy, trace the shape of the **dark matter halo** (the vast, invisible shell of dark matter surrounding every galaxy), and reveal hidden clumps of dark matter through the gaps and distortions those clumps leave behind. The catch is that finding them means sifting through the positions and motions of over a billion stars, nearly all of them background noise.

David Shih, Matthew Buckley, and Lina Necib have now released **Via Machinae 2.0**, the first full-sky automated search of the **Gaia catalog**, a map of nearly two billion stars assembled by the European Space Agency's Gaia satellite. The haul: 102 stream candidates, 92 of them previously unknown.

> **Key Insight:** By repurposing an anomaly-detection algorithm originally built for the Large Hadron Collider, Via Machinae 2.0 finds stellar streams without any assumptions about the Milky Way's gravitational potential, turning up 92 new stream candidates in a single sweep.

## How It Works

The core technique is **ANODE** (a normalizing flow-based anomaly detector), a machine learning method built around one question: which stars look statistically *weird* compared to their neighbors?

ANODE was designed to hunt for new particles at the LHC by spotting bumps in data distributions. It uses **normalizing flows**, neural networks that learn to model how data is distributed across many dimensions, to estimate how "normal" any given star looks in its local neighborhood.

![Figure 1](figure:1)

The VM2 pipeline runs in four stages:

1. **Sky patching:** The full sky is divided into overlapping 15°-radius patches, each with its own local coordinate system. Patches near the galactic disk, the Large Magellanic Cloud, or dusty regions get thrown out as too noisy.
2. **Proper motion slicing:** Within each patch, stars are grouped into narrow search regions: 6 mas/yr-wide slices in **proper motion** space (the tiny measurable drift of a star across the sky, in milliarcseconds per year). Stream stars share nearly identical velocities, so grouping by proper motion isolates co-moving stars. VM2 now scans *both* proper motion coordinates independently, doubling the detection opportunities.
3. **Anomaly scoring:** ANODE compares each star's local density in the search region against the background density from flanking "control regions." Stars overdense relative to background receive a high anomaly score: R(x) = p_SR(x) / p_bg(x). Each star appears in many overlapping patches, providing multiple quasi-independent tests that combine for robustness.
4. **Stream reconstruction:** High-scoring stars are clustered spatially and filtered to resemble real streams: localized in proper motion, linear on the sky, and with colors consistent with old, **metal-poor** stellar populations (stars low in heavy elements, a signature of ancient clusters).

![Figure 2](figure:2)

The team also ran the algorithm on **Galaxia**, a synthetic Milky Way model containing no streams. Any "detections" in that simulation are pure false positives, giving a concrete estimate of the noise floor. The original Via Machinae had no such calibration.

## Why It Matters

The result, 102 stream candidates with roughly 90 expected to be genuine, vastly expands the known stellar stream census. Before Gaia, astronomers knew of only a handful of streams. With the right tools, it turns out we are swimming in them.

![Figure 4](figure:4)

Each new stream is a potential scientific goldmine. Dense, narrow streams like GD-1 are sensitive enough to detect dark matter substructure at the level of individual clumps, effectively turning stellar ribbons into cosmic seismometers for otherwise invisible mass. Ninety new streams greatly enlarges the sample available for dark matter searches and for mapping the Milky Way's gravitational potential.

The catalog also tells us about the galaxy's **accretion history**, the full record of smaller objects that have fallen in over billions of years. Because Via Machinae makes no assumptions about the galactic potential or stellar distances, it can find streams that orbit-based methods might systematically miss. On the methods side, Via Machinae is part of a growing trend of exporting anomaly detection tools from high-energy physics into astrophysics, a cross-pollination that is changing how astronomers search for rare signals in billion-star datasets.

> **Bottom Line:** Via Machinae 2.0 conducts the first full-sky, model-agnostic stellar stream search and identifies 102 candidates, roughly 90 of them likely real, showing that LHC-inspired machine learning can unlock discoveries hiding in plain sight within the Gaia catalog.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work imports unsupervised anomaly detection from particle physics into astrophysics, showing that tools built to find new fundamental particles can also map the large-scale structure and merger history of our galaxy.
- **Impact on Artificial Intelligence:** Via Machinae 2.0 shows how normalizing flow-based density estimation scales to full-sky surveys of over a billion stars, paired with a false positive calibration framework that raises the bar for trustworthy ML-driven discovery in astronomy.
- **Impact on Fundamental Interactions:** The 92 newly discovered stream candidates provide a much larger sample for probing the Milky Way's dark matter substructure, gravitational potential, and accretion history, all without requiring model assumptions about galactic dynamics.
- **Outlook and References:** Follow-up spectroscopic observations will be needed to confirm the candidates, and future versions may incorporate Gaia DR3's expanded radial velocity catalog; the paper is available at [arXiv:2303.01529](https://arxiv.org/abs/2303.01529) (Shih, Buckley & Necib, 2023).
