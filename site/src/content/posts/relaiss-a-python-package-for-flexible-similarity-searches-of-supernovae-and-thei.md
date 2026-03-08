---
abstract: Discovery rates of supernovae are expected to surpass one million events
  annually with the Vera C. Rubin Observatory. With unprecedented sample sizes of
  both common and rare transient types, photometric classification alone will be insufficient
  for finding one-in-a-million events and prioritizing the 1% of events for spectroscopic
  follow-up observations. Here, we present reLAISS, a modified framework for similarity
  searches of supernovae using extracted features of ZTF light curves and Pan-STARRS
  host galaxy photometry and built on the original LAISS framework. Unlike its predecessor,
  reLAISS couples interpretable light curve morphology features with extinction-corrected
  host-galaxy colors to probe both explosion physics and associated stellar populations
  simultaneously. The library allows users to customize the number of neighbors retrieved,
  the weight of host and light curve features, and the use of Monte Carlo simulations
  to ensure relevant matches when features are poorly constrained. We release reLAISS
  as a pip-installable package with an accompanying reference set of 20,000 features,
  and a set of tutorials that demonstrate the code's expanded functionality. All source
  code can be found at https://github.com/evan-reynolds/re-laiss .
arxivId: '2507.13449'
arxivUrl: https://arxiv.org/abs/2507.13449
authors:
- E. Reynolds
- A. Gagliano
- V. A. Villar
concepts:
- transient similarity search
- supernova classification
- feature extraction
- anomaly detection
- monte carlo methods
- out-of-distribution detection
- galaxy classification
- bayesian inference
- scientific workflows
- uncertainty quantification
- dimensionality reduction
figures:
- /iaifi-research-blog/figures/2507_13449/figure_1.png
- /iaifi-research-blog/figures/2507_13449/figure_2.png
- /iaifi-research-blog/figures/2507_13449/figure_3.png
pdfUrl: https://arxiv.org/pdf/2507.13449v1
published: '2025-07-17T18:00:13+00:00'
theme: Astrophysics
title: 'reLAISS: A Python Package for Flexible Similarity Searches of Supernovae and
  Their Host Galaxies'
wordCount: 1213
---

## The Big Picture

Imagine finding a specific face in a crowd of one million strangers, not by name, but by resemblance. That's the challenge astronomers will face when the Vera C. Rubin Observatory begins cataloging stellar explosions at a rate that dwarfs everything before it. Over one million supernovae per year will flood our databases, and the conventional approach of classifying each one individually will collapse under that weight.

The problem isn't just volume. It's rarity. Some of the most scientifically valuable supernovae are one-in-a-million oddities: explosions so unusual they could rewrite our understanding of how stars die. Spectroscopy (breaking a supernova's light into a chemical fingerprint that reveals its composition) is the gold standard for confirming what kind of explosion you're looking at, but it can only be applied to roughly 1% of detected events. With so many candidates and so few slots, astronomers need a smarter triage system, one that can rapidly flag the weird, the rare, and the scientifically precious.

A team from IAIFI and the Center for Astrophysics at Harvard & Smithsonian has built exactly that. Their new open-source Python package, **reLAISS**, lets astronomers search a database of 20,000 supernovae for events that resemble any target they care about, in both light and galactic environment.

> **Key Insight:** reLAISS combines how a supernova's light evolves *and* what kind of galaxy it exploded in, enabling similarity searches that reflect both the explosion's physics and the stellar population that produced it.

## How It Works

reLAISS builds on an earlier tool called LAISS with two major upgrades. The pipeline starts simply: give it a supernova's identifier from the Zwicky Transient Facility (ZTF), a sky survey that systematically scans for transient events, and it gets to work.

![Figure 1](/iaifi-research-blog/figures/2507_13449/figure_1.png)

**Step 1: Light curve features.** A **light curve** is a graph of a supernova's brightness from ignition to fade. reLAISS extracts compact numerical summaries of that graph's shape: peak magnitude, rise time, decline time, duration above half-brightness, and rolling variance, in both ZTF's green and red filters, plus how the explosion's color evolves over time.

The team replaced the black-box features from the original LAISS with **morphology features**: numbers with physical meaning an astronomer can actually reason about. One neat addition is a **local curvature metric**, which captures how sharply the brightness curve bends near its peak, encoding the light curve's shape in a single compact number.

**Step 2: Host galaxy context.** Where a supernova explodes matters enormously. An explosion in a massive, old, red elliptical galaxy tells a very different story than one in a star-forming blue spiral. reLAISS uses a library called Prost to probabilistically identify the most likely host galaxy in Pan-STARRS, then extracts colors in four optical filters corrected for Milky Way dust. These host features are independently weighted, so a bad measurement in one band won't silently contaminate the whole match.

**Step 3: Nearest-neighbor search.** The similarity engine uses **ANNOY** (Approximate Nearest Neighbors Oh Yeah), a Spotify-developed algorithm that indexes a vector space using random projection trees, grouping similar objects into shared regions so close matches can be found quickly without brute-force comparison. Users can search by light curve alone, by host galaxy alone, or by both, with a tunable weighting term.

Two additional capabilities round out the package:

- **Uncertainty-aware matching.** When a light curve only caught half the rise, reLAISS runs repeated Monte Carlo simulations, re-querying neighbors based on measured uncertainties rather than silently failing on partial data.
- **Anomaly detection.** A statistical model characterizes the typical spread of distances between objects in the reference set, then converts a query object's deviation into an anomaly score from 0 to 100. This replaces an older random forest classifier and makes it easier to flag genuinely strange events for rapid spectroscopic follow-up.

## Why It Matters

The timing of this release is deliberate. The Rubin Observatory's Legacy Survey of Space and Time (LSST) will deliver more supernovae per year than all previous surveys combined. At that scale, photometric classification alone (typing a supernova from its brightness rather than its chemical fingerprint) isn't sufficient.

Photometric classification can tell you *what type* something probably is. It can't tell you whether this particular Type Ia supernova is the most extreme example of its kind, or whether it resembles a handful of unexplained events from five years ago. Similarity search fills that gap.

By coupling explosion physics with host environment, reLAISS captures a more complete picture of what makes two supernovae truly alike. A tool like this could accelerate the discovery of new supernova sub-classes, flag **progenitor systems** (the stars or stellar pairs whose deaths triggered the explosion) that don't fit known templates, and help astronomers allocate precious spectroscopic telescope time to the events most likely to teach us something new.

The team plans to extend the feature set beyond ZTF's current filters and to test performance on partial-phase and low-cadence light curves, challenges that will only intensify as Rubin data arrives.

> **Bottom Line:** reLAISS turns the coming supernova data deluge into a navigable map: a nearest-neighbor search engine for stellar explosions that's fast, flexible, and physically interpretable. It arrives just in time for the era of million-event-per-year astronomy.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">reLAISS applies machine learning nearest-neighbor search, originally developed for recommendation systems, to astrophysical transient discovery, connecting scalable AI indexing with the physics of stellar explosions and their galactic environments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The package shows how approximate nearest-neighbor algorithms combined with uncertainty-aware Monte Carlo resampling can deliver interpretable similarity search at scale across noisy, heterogeneous scientific datasets.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By jointly modeling supernova light curve morphology and host galaxy stellar populations, reLAISS opens a path to discovering rare or anomalous explosion mechanisms that could reveal progenitor physics beyond the standard core-collapse and thermonuclear channels.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The reLAISS package is pip-installable with a 20,000-event reference set and tutorials; future work will extend its reach to Rubin/LSST cadences and additional photometric passbands (Reynolds, Gagliano & Villar 2025, [arXiv:2507.13449](https://arxiv.org/abs/2507.13449)).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">reLAISS: A Python Package for Flexible Similarity Searches of Supernovae and Their Host Galaxies</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2507.13449](https://arxiv.org/abs/2507.13449)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["E. Reynolds", "A. Gagliano", "V. A. Villar"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Discovery rates of supernovae are expected to surpass one million events annually with the Vera C. Rubin Observatory. With unprecedented sample sizes of both common and rare transient types, photometric classification alone will be insufficient for finding one-in-a-million events and prioritizing the 1% of events for spectroscopic follow-up observations. Here, we present reLAISS, a modified framework for similarity searches of supernovae using extracted features of ZTF light curves and Pan-STARRS host galaxy photometry and built on the original LAISS framework. Unlike its predecessor, reLAISS couples interpretable light curve morphology features with extinction-corrected host-galaxy colors to probe both explosion physics and associated stellar populations simultaneously. The library allows users to customize the number of neighbors retrieved, the weight of host and light curve features, and the use of Monte Carlo simulations to ensure relevant matches when features are poorly constrained. We release reLAISS as a pip-installable package with an accompanying reference set of 20,000 features, and a set of tutorials that demonstrate the code's expanded functionality. All source code can be found at https://github.com/evan-reynolds/re-laiss .</span></div></div>
</div>
