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
wordCount: 1084
---

## The Big Picture

Imagine a star drifting peacefully through its galaxy — and then, in an instant, crossing an invisible line of no return around a supermassive black hole. In a matter of hours, gravity shreds the star apart, flinging half the debris outward while the rest spirals inward, igniting a brilliant flare visible across billions of light-years. These catastrophic stellar deaths, called **tidal disruption events (TDEs)**, are among the most spectacular — and rarest — cosmic fireworks in the universe.

The problem is finding them. Modern sky surveys like the Zwicky Transient Facility (ZTF) — a telescope scanning the entire northern sky every few nights — discover thousands of short-lived cosmic events called **transients** every month: supernovae, active galactic nuclei (galaxies with unusually bright, actively feeding black holes at their centers), stellar flares, and more. TDEs make up only about 0.5% of all spectroscopically confirmed transients — those identified through detailed spectral analysis of their light.

Manually sorting through this cosmic haystack is impossible at scale. **Spectroscopic follow-up** — the gold standard for identification, in which a telescope spreads an object's light into its component colors to reveal its true nature — covers only roughly 10% of discoveries. As the Vera C. Rubin Observatory prepares to increase the transient discovery rate by two orders of magnitude (a hundredfold increase), the problem is about to get dramatically worse.

A team led by Sebastian Gomez at the Space Telescope Science Institute has expanded FLEET — a machine learning algorithm originally built to hunt superluminous supernovae — into a purpose-built TDE classifier that can sift through thousands of candidates and flag the most promising ones in hours.

> **Key Insight:** By training on nearly 5,000 real classified transients and combining light curve shapes with host galaxy context, FLEET can identify likely TDEs two orders of magnitude more efficiently than random selection — and it's ready to deploy on tomorrow's next-generation surveys.

## How It Works

FLEET is built on a **random forest algorithm**, an ensemble method that constructs hundreds of decision trees — each a chain of yes/no questions about the data — and aggregates their votes into a probability score. Crucially, FLEET trains exclusively on real, spectroscopically confirmed events rather than simulations, which often fail when applied to actual observations.

The training set contains 4,779 classified transients, of which 45 are confirmed TDEs — a deliberately imbalanced dataset that mirrors the real-world rarity of TDEs. Each transient contributes two categories of features:

- **Light curve features:** how an event brightens and fades over time, including rise and fade timescales, and the $(g-r)$ color at peak brightness — how much brighter the object appears through a green filter versus a red one, a proxy for temperature
- **Host galaxy features:** the transient's offset from its host galaxy center, galaxy brightness, and photometric redshift estimates (distance approximations derived from galaxy color, without requiring a full spectrum)

![Figure 1](/iaifi-research-blog/figures/2210_10810/figure_1.png)

The single most powerful discriminator is the **normalized host separation** — how far a transient sits from its galaxy's center relative to the galaxy's size. Since TDEs occur when stars wander too close to a central supermassive black hole, genuine TDEs cluster tightly at their host nuclei. A transient sitting far off-center is almost certainly not a TDE. The second most powerful feature is $(g-r)$ color at peak: TDE optical emission tends to run bluer than most supernovae of comparable brightness.

With just 20 days of photometry and a threshold of $P(\text{TDE}) > 0.5$, FLEET achieves roughly 40% completeness (finding 40% of true TDEs) at 30% purity (30% of flagged candidates are genuine). Extending the photometry window to 40 days pushes purity to around 50% with comparable completeness. Raising the threshold to $P(\text{TDE}) > 0.8$ delivers 80% purity — ideal when telescope time is too precious to waste on false positives.

![Figure 2](/iaifi-research-blog/figures/2210_10810/figure_2.png)

The team also applied FLEET to the full ZTF archive and identified 39 currently unclassified transients as strong TDE candidates — a ready-made target list for any observing program aiming to expand the confirmed TDE sample.

## Why It Matters

The timing of this work is deliberate. The Rubin Observatory's Legacy Survey of Space and Time (LSST) is expected to discover roughly $10^4$ well-observed TDEs per year — more than the entire confirmed TDE catalog accumulated over decades. Without an efficient photometric classifier running in real time, the vast majority will pass unnoticed.

Simulations of Rubin's survey cadence show that FLEET can recover approximately 30% of TDEs at redshifts below $z < 0.5$ — the relatively nearby universe, within roughly 5 billion light-years — translating to around 3,000 TDE identifications per year from Rubin's data stream alone. The Nancy Grace Roman Space Telescope, operating at higher redshift, should yield around 200 additional TDEs per year.

![Figure 3](/iaifi-research-blog/figures/2210_10810/figure_3.png)

A richer TDE sample directly attacks fundamental open questions: How frequently do stars get disrupted? How do disruption rates vary with black hole mass and host galaxy type? What determines whether a TDE produces radio jets, X-ray flares, or only optical emission? Every confirmed TDE is a rare window into **accretion** physics — gas and stellar debris spiraling into the black hole — at the extreme. FLEET dramatically expands how wide that window can be opened. The algorithm is open source and available on GitHub, ready for the community to deploy on any survey dataset.

> **Bottom Line:** FLEET turns machine learning classification from a bottleneck into a multiplier — enabling the coming flood of transient data from Rubin and Roman to yield thousands of new TDE discoveries per year, each a probe of supermassive black hole physics that would otherwise go unrecognized.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies random forest machine learning to astrophysical transient classification, training on real observational data to address a fundamental challenge in time-domain astronomy at the intersection of AI and black hole physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">FLEET demonstrates that ensemble ML methods trained on imbalanced, real-world datasets — rather than simulations — can achieve classification purity nearly two orders of magnitude better than random selection.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling efficient TDE identification at scale, this work accelerates the statistical study of supermassive black hole demographics, accretion physics, and stellar dynamics at galactic centers.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">With Rubin poised to deliver a torrent of transient alerts in the mid-2020s, FLEET is positioned to become a critical real-time discovery engine; the full paper and open-source code are available at arXiv:2209.XXXXX and https://github.com/gmzsebastian/FLEET.</span></div></div>
</div>
