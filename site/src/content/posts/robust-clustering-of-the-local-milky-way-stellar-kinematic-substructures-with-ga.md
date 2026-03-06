---
abstract: 'We apply the clustering algorithm HDBSCAN on the Gaia early third data
  release astrometry combined with the Gaia second data release radial velocity measurements
  of almost 5.5 million stars to identify the local stellar kinematic substructures
  in the solar neighborhood. Understanding these structures helps build a more complete
  picture of the formation of the Milky Way, as well as an empirical phase space distribution
  of dark matter that would inform detection experiments. The main goal of this study
  is to provide a list of the most stable clusters, by taking into account the measurement
  uncertainties and studying the stability of the clustering results. We apply the
  clustering algorithm in two spaces, in velocity space in order to study recently
  accreted structures, and in action-angle space to find phase-mixed structures. We
  find 23 (6) robust clusters in velocity space (action-angle space) that are consistently
  not associated with noise. They are attributed to the known structures: the Gaia
  Sausage-Enceladus, the Helmi Stream, and globular cluster NGC 3201 are found in
  both spaces, while NGC 104 and the thick disk (Sequoia) are identified in velocity
  space (action-angle space). We discuss the kinematic properties of these structures
  and study whether many of the small clusters belong to a similar larger cluster
  based on their chemical abundances. Although we do not identify any new structures,
  we find that the HDBSCAN member selection of already known structures is unstable
  to input kinematics of the stars when resampled within their uncertainties. We therefore
  present the most stable subset of local kinematic structures, which are consistently
  identified by the clustering algorithm, and emphasize the need to take into account
  error propagation during both the manual and automated identification of stellar
  structures, both for existing ones as well as future discoveries. (abridged)'
arxivId: '2208.01056'
arxivUrl: https://arxiv.org/abs/2208.01056
authors:
- Xiaowei Ou
- Lina Necib
- Anna Frebel
concepts:
- clustering
- uncertainty quantification
- stellar streams
- robustness
- dark matter
- monte carlo methods
- action-angle coordinates
- density estimation
- galactic archaeology
- anomaly detection
- dimensionality reduction
figures:
- /iaifi-research-blog/figures/2208_01056/figure_1.png
- /iaifi-research-blog/figures/2208_01056/figure_2.png
- /iaifi-research-blog/figures/2208_01056/figure_3.png
pdfUrl: https://arxiv.org/pdf/2208.01056v1
published: '2022-08-01T18:00:08+00:00'
theme: Astrophysics
title: Robust Clustering of the Local Milky Way Stellar Kinematic Substructures with
  Gaia eDR3
wordCount: 1088
---

## The Big Picture

Imagine trying to reconstruct the history of a city by studying where its residents live today — which neighborhoods they cluster in, how they move through the streets, what languages they speak. Now scale that up to hundreds of billions of stars and billions of years. That's essentially what researchers do when piecing together how the Milky Way formed. And like any good detective work, it requires knowing not just what you found, but *how confident you are* in what you found.

Our galaxy is a living record of ancient cosmic collisions. Smaller galaxies and star clusters have fallen into the Milky Way over eons, and their constituent stars — pulled apart and scattered by the Milky Way's gravity — still carry ghostly signatures of their origins in how they move. Identifying these groups of stars with shared motion patterns tells us which smaller galaxies our Milky Way devoured, and when.

Those captured stars carry a further bonus: they may trace the dark matter that fell in alongside them, providing a rare empirical map of the invisible substance that makes up most of the universe's mass.

Xiaowei Ou, Lina Necib, and Anna Frebel at MIT applied a powerful machine learning clustering algorithm to the largest stellar motion dataset ever assembled — and, crucially, stress-tested their results against measurement uncertainty in a way most previous studies haven't.

> **Key Insight:** HDBSCAN reliably identifies major known stellar structures, but the *exact membership* of those structures is surprisingly fragile — shifting when you account for observational uncertainties. Knowing which stars *consistently* appear in a cluster is as important as finding the cluster itself.

## How It Works

The team used data from **Gaia**, the European Space Agency's landmark stellar survey, combining **early third data release (eDR3)** positional and motion measurements with **second data release (DR2)** radial velocity measurements — each star's speed toward or away from Earth. The result: 5.5 million stars in the solar neighborhood, each with full 6D phase-space information (three position coordinates, three velocity components).

![Figure 1](/iaifi-research-blog/figures/2208_01056/figure_1.png)

They applied **HDBSCAN** (Hierarchical Density-Based Spatial Clustering of Applications with Noise), an algorithm that finds clusters of arbitrary shape in high-dimensional data without requiring you to specify how many clusters exist in advance. Unlike simpler algorithms that force every data point into a group, HDBSCAN explicitly labels ambiguous points as "noise" — crucial when hunting for rare stellar streams amid millions of disk stars.

The algorithm ran in two mathematical spaces:

- **Velocity space** (the 3D space of a star's vx, vy, vz motion): ideal for recently accreted structures that haven't had time to dynamically smear out.
- **Action-angle space**: a coordinate system derived from orbital mechanics where stars gravitationally scrambled over billions of years — **phase-mixed structures** — still cluster because they share conserved orbital properties.

The most novel contribution is rigorous **error propagation**. Gaia's measurements are exquisite but not perfect, and with 5.5 million stars, small errors can meaningfully shift which clusters form. The team used a **Monte Carlo bootstrap** approach: running the same analysis hundreds of times with inputs resampled within each star's measurement uncertainties, then accepting only clusters that appeared consistently across all runs.

The stability test returned a clear-eyed result: **23 robust clusters in velocity space** (1,405 stars) and **6 robust clusters in action-angle space** (497 stars).

![Figure 2](/iaifi-research-blog/figures/2208_01056/figure_2.png)

Several well-known structures emerged. The **Gaia Sausage-Enceladus (GSE)** — remnant of the Milky Way's most recent major merger — appeared prominently in both spaces, as did the **Helmi Stream**, ancient tidal debris from a disrupted dwarf galaxy. Globular cluster **NGC 3201** showed up in both spaces; **NGC 104** appeared only in velocity space; retrograde structure **Sequoia** only in action-angle space.

![Figure 3](/iaifi-research-blog/figures/2208_01056/figure_3.png)

The researchers claimed no new discoveries. This restraint is itself scientifically significant. Previous studies using similar data without rigorous uncertainty propagation have occasionally reported structures that may reflect algorithmic artifacts rather than genuine mergers. By demanding consistency across resampled datasets, Ou, Necib, and Frebel effectively publish a certified catalog — structures you can trust.

They also cross-matched their clusters with two spectroscopic surveys, **APOGEE DR17** and **LAMOST DR6**, checking whether stars in the same kinematic cluster share similar chemical abundances. Chemistry acts as stellar "DNA" — stars born in the same galaxy carry similar elemental fingerprints. Where kinematic and chemical signals agreed, confidence in a cluster's physical reality strengthened.

## Why It Matters

The stakes extend well beyond galactic archaeology. Dark matter direct detection experiments — underground detectors searching for the faint recoil when a dark matter particle scatters off an atomic nucleus — need accurate models of the local dark matter velocity distribution. If dark matter was accreted alongside infalling dwarf galaxies, the kinematic substructures identified here directly inform those models. A more accurate stellar map means better predictions for where to look, and better interpretation of null results when detectors find nothing.

This work also serves as a methodological template. As Gaia continues releasing data, and as future surveys like the **Vera Rubin Observatory** and **Roman Space Telescope** add tens of millions more stars, automated clustering will become indispensable. But automation without uncertainty quantification is a trap — the finding that HDBSCAN's membership lists shift when inputs are resampled is a clear warning that reported structures in the literature may be real, but their *boundaries* carry more ambiguity than is usually acknowledged.

> **Bottom Line:** By stress-testing their clustering algorithm against measurement uncertainties, the MIT team delivers the most rigorously validated catalog of local stellar kinematic substructures to date — and issues a clear methodological challenge to the field: always propagate your errors, or risk confusing noise for cosmic history.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges machine learning and astrophysics, deploying the HDBSCAN clustering algorithm on 5.5 million Gaia stars to map the Milky Way's merger history and constrain the local dark matter velocity distribution relevant for particle physics experiments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The study demonstrates a rigorous Monte Carlo approach to validating unsupervised clustering outputs under observational uncertainty — a methodology applicable to any domain where ML-identified clusters must be distinguished from noise.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The uncertainty-validated catalog of local stellar kinematic substructures provides the most reliable empirical input yet for modeling the dark matter phase-space distribution in the solar neighborhood, directly informing direct detection experiments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future Gaia data releases and next-generation spectroscopic surveys will expand the stellar sample dramatically, making robust uncertainty propagation even more critical; the full analysis is available at arXiv:2206.07133.</span></div></div>
</div>
