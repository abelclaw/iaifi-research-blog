---
abstract: The Vera C. Rubin Observatory will soon survey the southern sky, delivering
  a depth and sky coverage that is unprecedented in time domain astronomy. As part
  of commissioning, Data Preview 1 (DP1) has been released. It comprises a LSSTComCam
  observing campaign between November and December 2024 with multi-band imaging of
  seven fields, covering roughly 0.4 square degrees each, providing a first glimpse
  into the data products that will become available once the Legacy Survey of Space
  and Time begins. In this work, we search three fields for extragalactic transients.
  We identify eight new likely supernovae, and three known ones from a sample of 369,644
  difference image analysis objects. Photometric classification using Superphot+ assigns
  sub-classes with >95% confidence to only one SN Ia and one SN II in this sample.
  Our findings are in agreement with supernova detection rate predictions of $15\pm4$
  supernovae from simulations using simsurvey. The supernova detection rate in the
  data is possibly affected by the lack of suitable templates. Nevertheless, this
  work demonstrates the quality of the data products delivered in DP1 and indicates
  that the Rubin Observatory's Legacy Survey of Space and Time (LSST) is well placed
  to fulfill its discovery potential in time domain astronomy.
arxivId: '2507.22864'
arxivUrl: https://arxiv.org/abs/2507.22864
authors:
- James Freeburn
- Igor Andreoni
- Kaylee M. de Soto
- Cristina Andrade
- Akash Anumarlapudi
- Tyler Barna
- Jonathan Carney
- Sushant Sharma Chaudhary
- Michael W. Coughlin
- Felipe Fontinele Nunes
- Sarah Teague
- Mickael Rigault
- V. Ashley Villar
- Gloria Fonseca Alvarez
- Federica B. Bianco
- Alexandre Boucaud
- Dominique Boutigny
- Andrew Bradshaw
- Hsin-Fang Chiang
- Phil N. Daly
- Felipe Daruich
- Guillaume Daubard
- Holger Drass
- Laurent Le Guillou
- Leanne P. Guy
- Patrick Ingraham
- M. James Jee
- Steven M. Kahn
- Yijung Kang
- Arun Kannawadi
- Lee S. Kelvin
- Didier Laporte
- Shuang Liang
- Nate B. Lust
- Mostafa Lutfi
- Gabriele Mainetti
- Andrés A. Plazas Malagón
- Felipe Menanteau
- David J. Mills
- Marc Moniez
- Erfan Nourbakhsh
- Russell E. Owen
- Maria T. Patterson
- John R. Peterson
- Wouter van Reeven
- Vincent J. Riot
- William Roby
- David Sanmartim
- Jacques Sebag
- Nima Sedaghat
- Richard A. Shaw
- Alysha Shugart
- Krzysztof Suberlak
- John D. Swinbank
- Dan S. Taranu
- Charlotte Ward
- Christopher Z. Waters
- W. M. Wood-Vasey
concepts:
- supernova classification
- difference image analysis
- classification
- signal detection
- photometric light curve fitting
- calibration
- uncertainty quantification
- anomaly detection
- transient survey pipeline
- monte carlo methods
- simulation-based inference
- scientific workflows
figures:
- /iaifi-research-blog/figures/2507_22864/figure_1.png
- /iaifi-research-blog/figures/2507_22864/figure_2.png
- /iaifi-research-blog/figures/2507_22864/figure_3.png
pdfUrl: https://arxiv.org/pdf/2507.22864v2
published: '2025-07-30T17:39:52+00:00'
theme: Astrophysics
title: Identification and photometric classification of extragalactic transients in
  the Vera C. Rubin Observatory's Data Preview 1
wordCount: 999
---

## The Big Picture

Imagine trying to spot a single flickering candle from across a crowded city while thousands of other lights turn on and off every second. That's roughly what astronomers face when hunting for supernovae. The night sky is chaotic and full of change. Finding a star detonating in a galaxy millions of light-years away requires not just a powerful telescope, but a pipeline that can sort signal from noise at massive scale.

The Vera C. Rubin Observatory, perched in the Chilean Andes, is about to become the most powerful survey telescope ever built for tracking changes in the night sky. Its full survey, the **Legacy Survey of Space and Time (LSST)**, will generate up to 10 million alerts per night, each flagging a difference compared to a stored reference image. That's more than ten times what the current frontrunner, the Zwicky Transient Facility, produces.

But before that firehose opens, astronomers needed to test the plumbing. A team led by James Freeburn at UNC Chapel Hill, including IAIFI affiliate V. Ashley Villar at Harvard, did exactly that. Using an early test dataset called **Data Preview 1 (DP1)**, collected with a prototype camera before the full telescope goes live, they showed that Rubin's detection and classification pipeline can handle the flood.

> **Key Insight:** Searching just a fraction of Rubin's commissioning data, the team identified eight new likely supernovae from nearly 370,000 candidate events, confirming that both the telescope's detection pipeline and its machine learning classifier are ready ahead of the full survey launch.

## How It Works

The commissioning campaign used **LSSTComCam**, a smaller prototype camera, to observe seven sky fields between November and December 2024. Each field covers roughly 0.4 square degrees. The team focused on three of these fields for their supernova search.

First comes **difference image analysis (DIA)**: subtract a stored "template" image from a new observation, and anything that has changed shows up as a residual. This produced 369,644 candidate sources. The vast majority were not supernovae. Cosmic rays, instrument artifacts, poorly subtracted galaxy cores, and other false positives (collectively called **"bogus" detections**) dominated the catalog.

To cut through the noise, the team required each candidate to have at least five detections, show an association with a galaxy beyond the Milky Way, and pass quality checks on its **light curve** (the graph of how brightness changes over time). Cross-matching against existing astronomical databases recovered three previously catalogued supernovae. Eight additional candidates passed all cuts as new, unreported events.

![Figure 1](figure:1)

Classification relied on **Superphot+**, a machine learning tool trained on simulated supernova light curves that assigns probabilistic sub-type labels. The two main categories: **Type Ia** (thermonuclear explosions of white dwarf stars, used as cosmological distance markers) and **Type II** (core-collapse explosions of massive stars). The algorithm needs multi-band photometry and enough data points to pin down the light curve shape. Of the eleven supernovae in the sample, only two got confident classifications above 95% probability: one Type Ia and one Type II. The rest lacked sufficient observations, a limitation that LSST's continuous cadence should largely solve.

![Figure 2](figure:2)

The team also ran **simsurvey** simulations to predict how many supernovae the campaign should have detected given its depth, cadence, and sky coverage. The answer: 15 ± 4. Finding eleven falls within that range. The shortfall is probably explained by a known DP1 quirk: template images were sometimes taken during the same campaign, causing some supernovae to be subtracted away before analysis even began.

![Figure 3](figure:3)

## Why It Matters

The stakes extend well beyond eleven faint smudges of light. Type Ia supernovae are the primary "standard candles" astronomers use to measure cosmic distances and map the expansion history of the universe. LSST is expected to detect hundreds of thousands over its ten-year run, enabling precision measurements of dark energy that will either confirm the standard cosmological model or crack it open. None of that science arrives if the pipeline doesn't work at scale, reliably, in near-real time.

This commissioning study is the proof-of-concept. Rubin's difference imaging produces clean, scientifically useful subtractions. Classifiers like Superphot+ can meaningfully categorize events even with sparse photometric coverage. And the bottlenecks are now visible: template quality, observation cadence, spectroscopic follow-up capacity. Engineers can address all of these before the full survey begins.

The next phase brings **LSSTCam**, the 3.2-gigapixel instrument, covering 9.6 square degrees per exposure and generating data at many times the commissioning rate. The pipeline tested here will face that torrent head-on. This paper is the fire drill.

> **Bottom Line:** Eight new supernovae found in a sliver of commissioning data, results matching simulation predictions, and a classification pipeline that works under real-world constraints. Rubin's system has passed its first real test, and the full LSST survey is cleared for launch.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work sits squarely at the intersection of observational astrophysics and machine learning, deploying AI-powered photometric classification on real commissioning data from a next-generation telescope and establishing automated supernova typing as a working capability for LSST.

- **Impact on Artificial Intelligence:** The study stress-tests probabilistic light curve classification under real-world constraints: sparse cadence, missing filter bands, template contamination. It reveals where ML classifiers hold up and where they break down.

- **Impact on Fundamental Interactions:** Accurate, automated supernova classification at LSST scale will produce the largest Type Ia sample in history, tightening constraints on dark energy and the universe's expansion rate.

- **Outlook and References:** As LSSTCam begins full operations, future work will focus on improved template strategies and spectroscopic confirmation workflows. See [Freeburn et al. (2025)](https://arxiv.org/abs/2507.22864) for full details.
