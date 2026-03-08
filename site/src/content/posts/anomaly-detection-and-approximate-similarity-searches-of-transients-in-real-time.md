---
abstract: 'We present LAISS (Lightcurve Anomaly Identification and Similarity Search),
  an automated pipeline to detect anomalous astrophysical transients in real-time
  data streams. We deploy our anomaly detection model on the nightly ZTF Alert Stream
  via the ANTARES broker, identifying a manageable $\sim$1-5 candidates per night
  for expert vetting and coordinating follow-up observations. Our method leverages
  statistical light-curve and contextual host-galaxy features within a random forest
  classifier, tagging transients of rare classes (spectroscopic anomalies), of uncommon
  host-galaxy environments (contextual anomalies), and of peculiar or interaction-powered
  phenomena (behavioral anomalies). Moreover, we demonstrate the power of a low-latency
  ($\sim$ms) approximate similarity search method to find transient analogs with similar
  light-curve evolution and host-galaxy environments. We use analogs for data-driven
  discovery, characterization, (re-)classification, and imputation in retrospective
  and real-time searches. To date we have identified $\sim$50 previously known and
  previously missed rare transients from real-time and retrospective searches, including
  but not limited to: SLSNe, TDEs, SNe IIn, SNe IIb, SNe Ia-CSM, SNe Ia-91bg-like,
  SNe Ib, SNe Ic, SNe Ic-BL, and M31 novae. Lastly, we report the discovery of 325
  total transients, all observed between 2018-2021 and absent from public catalogs
  ($\sim$1% of all ZTF Astronomical Transient reports to the Transient Name Server
  through 2021). These methods enable a systematic approach to finding the "needle
  in the haystack" in large-volume data streams. Because of its integration with the
  ANTARES broker, LAISS is built to detect exciting transients in Rubin data.'
arxivId: '2404.01235'
arxivUrl: https://arxiv.org/abs/2404.01235
authors:
- P. D. Aleo
- A. W. Engel
- G. Narayan
- C. R. Angus
- K. Malanchev
- K. Auchettl
- V. F. Baldassare
- A. Berres
- T. J. L. de Boer
- B. M. Boyd
- K. C. Chambers
- K. W. Davis
- N. Esquivel
- D. Farias
- R. J. Foley
- A. Gagliano
- C. Gall
- H. Gao
- S. Gomez
- M. Grayling
- D. O. Jones
- C. -C. Lin
- E. A. Magnier
- K. S. Mandel
- T. Matheson
- S. I. Raimundo
- V. G. Shah
- M. D. Soraisam
- K. M. de Soto
- S. Vicencio
- V. A. Villar
- R. J. Wainscoat
concepts:
- anomaly detection
- approximate similarity search
- ensemble methods
- supernova classification
- feature extraction
- real-time alert broker
- embeddings
- classification
- novelty detection
- scientific workflows
- signal detection
- active learning
figures:
- /iaifi-research-blog/figures/2404_01235/figure_1.png
- /iaifi-research-blog/figures/2404_01235/figure_1.png
- /iaifi-research-blog/figures/2404_01235/figure_2.png
- /iaifi-research-blog/figures/2404_01235/figure_2.png
- /iaifi-research-blog/figures/2404_01235/figure_3.png
- /iaifi-research-blog/figures/2404_01235/figure_3.png
pdfUrl: https://arxiv.org/pdf/2404.01235v2
published: '2024-04-01T16:53:04+00:00'
theme: Astrophysics
title: Anomaly Detection and Approximate Similarity Searches of Transients in Real-time
  Data Streams
wordCount: 1306
---

## The Big Picture

Imagine trying to find a single misprinted page inside every book ever published, while new books arrive by the thousands every night. That's roughly the challenge facing astronomers searching for rare cosmic explosions in modern sky surveys.

The **Zwicky Transient Facility (ZTF)** is a wide-field camera in California that scans the entire visible sky every few nights, generating roughly a million alerts per night. Each alert flags a point of light that changed: something brightened, faded, or flickered where it wasn't before. Hidden in that flood are supernovae, stars being torn apart by black holes, and phenomena we haven't yet named.

The problem isn't finding things that go bump in the night. The problem is finding the *right* bumps.

A team of researchers built a system called **LAISS** (Lightcurve Anomaly Identification and Similarity Search) to do exactly that, automatically, in real time, every single night. Astronomers call these short-lived cosmic events "transients": objects that appear, change dramatically, and fade over days to months. Instead of asking scientists to sift through thousands of candidates, LAISS delivers a curated list of roughly 1 to 5 genuinely unusual objects per night, ready for telescope follow-up.

> **Key Insight:** LAISS uses machine learning anomaly detection and millisecond-speed similarity search to systematically hunt rare cosmic transients in live data streams, and it's already found hundreds of objects that nobody knew existed.

## How It Works

The pipeline runs two major engines in tandem. The first is an **anomaly detection model**, a random forest classifier (many decision trees that vote together) trained to flag transients that look unusual compared to the broad population of known objects. The second is an **approximate similarity search** that finds the closest known analogs to any flagged event, in milliseconds, across a database of thousands of light curves.

![Figure 1](/iaifi-research-blog/figures/2404_01235/figure_1.png)

LAISS extracts two broad categories of features for each transient. **Statistical light-curve features** (a light curve is a graph of brightness over time) capture the shape of how a source brightens and fades: rise time, peak magnitude, color evolution, variability statistics. **Contextual host-galaxy features** describe the environment: stellar mass, star formation rate, galaxy morphology. Together, these paint a portrait of both the event and its neighborhood.

The classifier sorts anomalies into three types:

- **Spectroscopic anomalies** — rare-class transients whose chemical fingerprints look unusual, such as superluminous supernovae or tidal disruption events
- **Contextual anomalies** — events in unexpected environments, like a core-collapse supernova in a supposedly "dead" elliptical galaxy
- **Behavioral anomalies** — objects with peculiar light-curve shapes, including those powered by collisions between ejected material and surrounding gas shells, producing multiple peaks or extended plateaus

Once LAISS flags a candidate, **approximate nearest-neighbor algorithms** (techniques that trade a small amount of exactness for enormous speed) return a ranked list of historical analog transients. Astronomers get an instant prior on what they're looking at before any spectrum is taken.

![Figure 2](/iaifi-research-blog/figures/2404_01235/figure_1.png)

LAISS runs on the nightly ZTF Alert Stream through the **ANTARES broker**, an intermediary that receives ZTF's million-per-night alerts and applies filters before they reach scientists. By focusing on a curated stream of extragalactic transients, the system keeps the false positive rate low enough that only a manageable handful of candidates surface each night.

## Why It Matters

The scale problem LAISS is solving will only intensify. The **Vera C. Rubin Observatory**, currently being commissioned in Chile, will survey the entire southern sky every few nights and generate roughly ten million transient alerts per year.

Astronomers estimate only about 1% will ever receive spectroscopic follow-up, the gold standard for classifying what an explosion actually is. That makes automated systems like LAISS not a convenience but a necessity. Without them, genuinely novel events will slip through unnoticed, filed as ordinary supernovae or simply ignored.

The retrospective results from the paper make this concrete. Running LAISS on historical ZTF data from 2018 to 2021, the team discovered **325 transients that had never appeared in any public catalog**, roughly 1% of all ZTF reports to the Transient Name Server over that period. They also recovered about 50 previously identified rare transients that standard pipelines had missed or misclassified: superluminous supernovae, tidal disruption events, and several exotic subtypes driven by ejecta–circumstellar matter collisions.

![Figure 3](/iaifi-research-blog/figures/2404_01235/figure_2.png)

The similarity search is particularly valuable for what comes next. When an entirely new type of transient appears, something that matches no known class, astronomers can still instantly retrieve the closest known objects and use them as a guide for follow-up strategy. It's a data-driven way to bootstrap knowledge about the unknown.

![Figure 4](/iaifi-research-blog/figures/2404_01235/figure_2.png)

> **Bottom Line:** LAISS found 325 previously uncatalogued transients and ~50 rare events that automated pipelines had missed, and it runs every night in real time, already positioned to tackle the coming flood of data from the Rubin Observatory.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies machine learning anomaly detection and approximate nearest-neighbor search directly to live astrophysical data streams, showing how AI can function as a core part of observational astronomy workflows rather than a post-hoc analysis tool.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">LAISS shows how random forest classifiers and millisecond-latency similarity search can operate reliably at scale on heterogeneous real-world scientific data, with a filtering architecture that keeps expert time focused on the most scientifically valuable candidates.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By systematically recovering rare transient classes (tidal disruption events, superluminous supernovae, interaction-powered explosions), LAISS provides new observational handles on extreme astrophysical processes including black hole accretion, massive stellar death, and circumstellar matter physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">With LAISS already integrated into the ANTARES broker and built for Rubin Observatory compatibility, the pipeline is well placed to become a central discovery engine for the LSST era; the full paper is available at [arXiv:2404.01235](https://arxiv.org/abs/2404.01235).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Anomaly Detection and Approximate Similarity Searches of Transients in Real-time Data Streams</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2404.01235</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["P. D. Aleo", "A. W. Engel", "G. Narayan", "C. R. Angus", "K. Malanchev", "K. Auchettl", "V. F. Baldassare", "A. Berres", "T. J. L. de Boer", "B. M. Boyd", "K. C. Chambers", "K. W. Davis", "N. Esquivel", "D. Farias", "R. J. Foley", "A. Gagliano", "C. Gall", "H. Gao", "S. Gomez", "M. Grayling", "D. O. Jones", "C. -C. Lin", "E. A. Magnier", "K. S. Mandel", "T. Matheson", "S. I. Raimundo", "V. G. Shah", "M. D. Soraisam", "K. M. de Soto", "S. Vicencio", "V. A. Villar", "R. J. Wainscoat"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We present LAISS (Lightcurve Anomaly Identification and Similarity Search), an automated pipeline to detect anomalous astrophysical transients in real-time data streams. We deploy our anomaly detection model on the nightly ZTF Alert Stream via the ANTARES broker, identifying a manageable $\sim$1-5 candidates per night for expert vetting and coordinating follow-up observations. Our method leverages statistical light-curve and contextual host-galaxy features within a random forest classifier, tagging transients of rare classes (spectroscopic anomalies), of uncommon host-galaxy environments (contextual anomalies), and of peculiar or interaction-powered phenomena (behavioral anomalies). Moreover, we demonstrate the power of a low-latency ($\sim$ms) approximate similarity search method to find transient analogs with similar light-curve evolution and host-galaxy environments. We use analogs for data-driven discovery, characterization, (re-)classification, and imputation in retrospective and real-time searches. To date we have identified $\sim$50 previously known and previously missed rare transients from real-time and retrospective searches, including but not limited to: SLSNe, TDEs, SNe IIn, SNe IIb, SNe Ia-CSM, SNe Ia-91bg-like, SNe Ib, SNe Ic, SNe Ic-BL, and M31 novae. Lastly, we report the discovery of 325 total transients, all observed between 2018-2021 and absent from public catalogs ($\sim$1% of all ZTF Astronomical Transient reports to the Transient Name Server through 2021). These methods enable a systematic approach to finding the "needle in the haystack" in large-volume data streams. Because of its integration with the ANTARES broker, LAISS is built to detect exciting transients in Rubin data.</span></div></div>
</div>
