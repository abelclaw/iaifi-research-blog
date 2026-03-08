---
abstract: We present an expansion of FLEET, a machine learning algorithm optimized
  to select transients that are most likely to be tidal disruption events (TDEs).
  FLEET is based on a random forest algorithm trained on the light curves and host
  galaxy information of 4,779 spectroscopically classified transients. For transients
  with a probability of being a TDE, \ptde$>0.5$, we can successfully recover TDEs
  with a $\approx40$\% completeness and a $\approx30$\% purity when using the first
  20 days of photometry, or a similar completeness and $\approx50$\% purity when including
  40 days of photometry. We find that the most relevant features for differentiating
  TDEs from other transients are the normalized host separation, and the light curve
  $(g-r)$ color during peak. Additionally, we use FLEET to produce a list of the 39
  most likely TDE candidates discovered by the Zwicky Transient Facility that remain
  currently unclassified. We explore the use of FLEET for the Legacy Survey of Space
  and Time on the Vera C. Rubin Observatory (\textit{Rubin}) and the \textit{Nancy
  Grace Roman Space Telescope} (\textit{Roman}). We simulate the \textit{Rubin} and
  \textit{Roman} survey strategies and estimate that $\sim 10^4$ TDEs could be discovered
  every year by \textit{Rubin}, and $\sim200$ TDEs per year by \textit{Roman}. Finally,
  we run FLEET on the TDEs in our \textit{Rubin} survey simulation and find that we
  can recover $\sim 30$\% of those at a redshift $z <0.5$ with \ptde$>0.5$. This translates
  to $\sim3,000$ TDEs per year that FLEET could uncover from \textit{Rubin}. FLEET
  is provided as a open source package on GitHub https://github.com/gmzsebastian/FLEET
arxivId: '2210.10810'
arxivUrl: https://arxiv.org/abs/2210.10810
authors:
- Sebastian Gomez
- V. Ashley Villar
- Edo Berger
- Suvi Gezari
- Sjoert van Velzen
- Matt Nicholl
- Peter K. Blanchard
- Kate. D. Alexander
concepts:
- classification
- tidal disruption events
- ensemble methods
- feature extraction
- photometric transient classification
- supernova classification
- transfer learning
- survey simulation
- anomaly detection
- calibration
- signal detection
- galaxy classification
figures:
- /iaifi-research-blog/figures/2210_10810/figure_1.png
- /iaifi-research-blog/figures/2210_10810/figure_2.png
- /iaifi-research-blog/figures/2210_10810/figure_3.png
pdfUrl: https://arxiv.org/pdf/2210.10810v1
published: '2022-10-19T18:01:41+00:00'
theme: Astrophysics
title: Identifying Tidal Disruption Events with an Expansion of the FLEET Machine
  Learning Algorithm
wordCount: 1332
---

## The Big Picture

Imagine a star drifting through its galaxy and then, without warning, crossing an invisible boundary around a supermassive black hole. Within hours, gravity tears the star apart. Half the debris gets flung outward; the rest spirals inward, igniting a flare visible across billions of light-years. These stellar deaths are called **tidal disruption events (TDEs)**, and they rank among the rarest cosmic events we can observe.

The problem is finding them. Modern sky surveys like the Zwicky Transient Facility (ZTF), a telescope that scans the entire northern sky every few nights, discover thousands of short-lived cosmic events called **transients** every month: supernovae, active galactic nuclei (galaxies with unusually bright, actively feeding black holes at their centers), stellar flares, and more. TDEs make up only about 0.5% of all spectroscopically confirmed transients, those identified through detailed spectral analysis of their light.

Sorting through this haystack by hand doesn't scale. **Spectroscopic follow-up**, the gold standard for identification where a telescope spreads an object's light into its component colors to reveal its true nature, covers only about 10% of discoveries. As the Vera C. Rubin Observatory prepares to increase the transient discovery rate by a factor of a hundred, the problem is about to get much worse.

A team led by Sebastian Gomez at the Space Telescope Science Institute has expanded FLEET, a machine learning algorithm originally built to hunt superluminous supernovae, into a TDE classifier that can sift through thousands of candidates and flag the most promising ones in hours.

> **Key Insight:** By training on nearly 5,000 real classified transients and combining light curve shapes with host galaxy context, FLEET can identify likely TDEs two orders of magnitude more efficiently than random selection, and it's ready to deploy on next-generation surveys.

## How It Works

FLEET is built on a **random forest algorithm**, an ensemble method that constructs hundreds of decision trees (each a chain of yes/no questions about the data) and aggregates their votes into a probability score. The algorithm trains exclusively on real, spectroscopically confirmed events rather than simulations, which often fail when applied to actual observations.

The training set contains 4,779 classified transients, of which 45 are confirmed TDEs, a deliberately imbalanced dataset that mirrors how rare TDEs actually are. Each transient contributes two categories of features:

- **Light curve features:** how an event brightens and fades over time, including rise and fade timescales, and the $(g-r)$ color at peak brightness (how much brighter the object appears through a green filter versus a red one, a proxy for temperature)
- **Host galaxy features:** the transient's offset from its host galaxy center, galaxy brightness, and photometric redshift estimates (distance approximations derived from galaxy color, without requiring a full spectrum)

![Figure 1](/iaifi-research-blog/figures/2210_10810/figure_1.png)

The single most powerful discriminator is the **normalized host separation**, which measures how far a transient sits from its galaxy's center relative to the galaxy's size. TDEs occur when stars wander too close to a central supermassive black hole, so genuine TDEs cluster tightly at their host nuclei. A transient sitting far off-center is almost certainly something else. The second most important feature is $(g-r)$ color at peak: TDE optical emission tends to run bluer than most supernovae of comparable brightness.

With just 20 days of photometry and a threshold of $P(\text{TDE}) > 0.5$, FLEET achieves roughly 40% completeness (finding 40% of true TDEs) at 30% purity (30% of flagged candidates are genuine). Extending to 40 days of photometry pushes purity to around 50% with comparable completeness. At a stricter threshold of $P(\text{TDE}) > 0.8$, purity reaches 80%, which matters when telescope time is too precious to waste on false positives.

![Figure 2](/iaifi-research-blog/figures/2210_10810/figure_2.png)

The team also ran FLEET across the full ZTF archive and identified 39 currently unclassified transients as strong TDE candidates, a ready-made target list for observers looking to expand the confirmed sample.

## Why It Matters

The timing here is no accident. The Rubin Observatory's Legacy Survey of Space and Time (LSST) is expected to discover roughly $10^4$ well-observed TDEs per year, more than the entire confirmed TDE catalog accumulated over decades. Without an efficient photometric classifier running in real time, most of them will slip by unnoticed.

Simulations of Rubin's survey cadence show that FLEET can recover about 30% of TDEs at redshifts below $z < 0.5$ (the relatively nearby universe, within roughly 5 billion light-years), translating to around 3,000 TDE identifications per year from Rubin's data stream alone. The Nancy Grace Roman Space Telescope, operating at higher redshift, should add around 200 more per year.

![Figure 3](/iaifi-research-blog/figures/2210_10810/figure_3.png)

A larger TDE sample goes straight at the open questions in the field. How frequently do stars get disrupted? How do disruption rates vary with black hole mass and host galaxy type? What determines whether a TDE produces radio jets, X-ray flares, or only optical emission? Every confirmed TDE is a rare window into **accretion** physics, the process of gas and stellar debris spiraling into a black hole at the extreme. FLEET widens that window considerably. The algorithm is open source and available on GitHub, ready for deployment on any survey dataset.

> **Bottom Line:** FLEET turns machine learning classification from a bottleneck into a multiplier, enabling the coming flood of transient data from Rubin and Roman to yield thousands of new TDE discoveries per year, each a probe of supermassive black hole physics that would otherwise go unrecognized.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This paper applies random forest machine learning to astrophysical transient classification, training on real observational data to tackle a core challenge in time-domain astronomy at the intersection of AI and black hole physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">FLEET shows that ensemble ML methods trained on imbalanced, real-world datasets (rather than simulations) can achieve classification purity nearly two orders of magnitude better than random selection.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Efficient TDE identification at scale accelerates the statistical study of supermassive black hole demographics, accretion physics, and stellar dynamics at galactic centers.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">With Rubin poised to deliver a torrent of transient alerts in the mid-2020s, FLEET is positioned to become a real-time discovery engine; the full paper and open-source code are available at [arXiv:2210.10810](https://arxiv.org/abs/2210.10810) and https://github.com/gmzsebastian/FLEET.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Identifying Tidal Disruption Events with an Expansion of the FLEET Machine Learning Algorithm</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2210.10810</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Sebastian Gomez", "V. Ashley Villar", "Edo Berger", "Suvi Gezari", "Sjoert van Velzen", "Matt Nicholl", "Peter K. Blanchard", "Kate. D. Alexander"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We present an expansion of FLEET, a machine learning algorithm optimized to select transients that are most likely to be tidal disruption events (TDEs). FLEET is based on a random forest algorithm trained on the light curves and host galaxy information of 4,779 spectroscopically classified transients. For transients with a probability of being a TDE, \ptde$>0.5$, we can successfully recover TDEs with a $\approx40$\% completeness and a $\approx30$\% purity when using the first 20 days of photometry, or a similar completeness and $\approx50$\% purity when including 40 days of photometry. We find that the most relevant features for differentiating TDEs from other transients are the normalized host separation, and the light curve $(g-r)$ color during peak. Additionally, we use FLEET to produce a list of the 39 most likely TDE candidates discovered by the Zwicky Transient Facility that remain currently unclassified. We explore the use of FLEET for the Legacy Survey of Space and Time on the Vera C. Rubin Observatory (\textit{Rubin}) and the \textit{Nancy Grace Roman Space Telescope} (\textit{Roman}). We simulate the \textit{Rubin} and \textit{Roman} survey strategies and estimate that $\sim 10^4$ TDEs could be discovered every year by \textit{Rubin}, and $\sim200$ TDEs per year by \textit{Roman}. Finally, we run FLEET on the TDEs in our \textit{Rubin} survey simulation and find that we can recover $\sim 30$\% of those at a redshift $z <0.5$ with \ptde$>0.5$. This translates to $\sim3,000$ TDEs per year that FLEET could uncover from \textit{Rubin}. FLEET is provided as a open source package on GitHub https://github.com/gmzsebastian/FLEET</span></div></div>
</div>
