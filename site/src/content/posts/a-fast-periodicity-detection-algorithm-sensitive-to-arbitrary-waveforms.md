---
abstract: A reexamination of period finding algorithms is prompted by new large area
  astronomical sky surveys that can identify billions of individual sources having
  a thousand or more observations per source. This large increase in data necessitates
  fast and efficient period detection algorithms. In this paper, we provide an initial
  description of an algorithm that is being used for detection of periodic behavior
  in a sample of 1.5 billion objects using light curves generated from Zwicky Transient
  Facility (ZTF) data (Bellm et al. 2019; Masci et al. 2018). We call this algorithm
  "Fast Periodicity Weighting" (FPW), derived using a Gaussian Process (GP) formalism.
  A major advantage of the FPW algorithm for ZTF analysis is that it is agnostic to
  the details of the phase-folded waveform. Periodic sources in ZTF show a wide variety
  of waveforms, some quite complex, including eclipsing objects, sinusoidally varying
  objects also exhibiting eclipses, objects with cyclotron emission at various phases,
  and accreting objects with complex waveforms. We describe the FPW algorithm and
  its application to ZTF, and provide efficient code for both CPU and GPU.
arxivId: '2502.00243'
arxivUrl: https://arxiv.org/abs/2502.00243
authors:
- Douglas P. Finkbeiner
- Thomas A. Prince
- Samuel E. Whitebook
concepts:
- phase-folded periodogram
- signal detection
- bayesian inference
- scalability
- stochastic processes
- spectral methods
- hypothesis testing
- gpu acceleration
- stellar evolution
- anomaly detection
- sparse models
figures:
- /iaifi-research-blog/figures/2502_00243/figure_1.png
- /iaifi-research-blog/figures/2502_00243/figure_1.png
- /iaifi-research-blog/figures/2502_00243/figure_2.png
- /iaifi-research-blog/figures/2502_00243/figure_2.png
- /iaifi-research-blog/figures/2502_00243/figure_3.png
- /iaifi-research-blog/figures/2502_00243/figure_3.png
pdfUrl: https://arxiv.org/pdf/2502.00243v1
published: '2025-02-01T00:48:05+00:00'
theme: Astrophysics
title: A Fast Periodicity Detection Algorithm Sensitive to Arbitrary Waveforms
wordCount: 1026
---

## The Big Picture

Imagine finding a heartbeat in a crowd of 1.5 billion people — simultaneously, in real time, using nothing but faint flickering light. That's the challenge facing modern astronomers as sky surveys like the **Zwicky Transient Facility (ZTF)** — a robotic telescope that automatically scans the night sky — generate torrents of data on billions of stars, each observed hundreds or thousands of times. Hidden in those brightness records are pulsing stars, eclipsing binaries, and exotic objects feeding off companion stars — but only if you can detect their rhythms fast enough to keep pace.

The problem with existing period-finding algorithms is that they are picky. The **Lomb-Scargle periodogram** — the gold standard for decades — assumes stars brighten and dim in a smooth, repeating wave, like a perfectly even heartbeat. Nature rarely cooperates. An eclipsing binary produces sharp, sudden dips. A white dwarf feeding on a companion creates jagged, asymmetric spikes. Stars with powerful magnetic fields pulse in complex, multi-humped patterns. Use a tool tuned for smooth waves and you'll miss half the zoo.

Researchers Douglas Finkbeiner (Harvard), Thomas Prince, and Samuel Whitebook (Caltech) have developed **Fast Periodicity Weighting (FPW)**: an algorithm that detects periodic signals of *any* waveform shape, derived from statistical first principles, and fast enough to process over a billion objects on modern hardware.

> **Key Insight:** FPW detects periodicity without assuming anything about waveform shape, making it sensitive to the full diversity of variable stars and transients that traditional sinusoid-fitting algorithms routinely miss.

## How It Works

FPW belongs to the family of **phase-binning algorithms** — methods that test whether a signal truly repeats by folding observations together in time. Given a candidate period, every data point gets assigned to one of *M* phase bins based on where it falls in the cycle. If the source is truly periodic, the same bins consistently land brighter or fainter. If the period is wrong, flux scrambles randomly across bins.

The core computation proceeds in three steps:

1. For each phase bin, compute a **weighted sum** of mean-subtracted flux values, where each observation is weighted by its inverse-variance — precise measurements carry more weight than noisy ones.
2. Square that weighted sum and divide by the total bin weight, normalizing by how many observations fell there.
3. Sum across all *M* bins to get the FPW score *S_FPW*.

The algorithm handles **non-uniform photometric errors** naturally — each brightness measurement carries its own uncertainty. For ZTF, errors are calibrated using all sources in a 47-square-degree camera quadrant, capturing systematic effects like variations in the **point spread function** (the way a star's light spreads across the detector) that affect entire regions simultaneously.

![Figure 1](/iaifi-research-blog/figures/2502_00243/figure_1.png)

The mathematical grounding comes from **Gaussian Process (GP) theory**. The FPW statistic is formally the difference in χ² between two hypotheses: "this source is periodic at this trial frequency" versus "this source is constant." That means FPW isn't heuristic — it optimizes the detection of any signal that creates coherent structure when folded in phase.

![Figure 2](/iaifi-research-blog/figures/2502_00243/figure_1.png)

One trade-off: for pure sinusoids, FPW is slightly less sensitive than Lomb-Scargle. But the gain is overwhelming. ZTF contains eclipsing binaries, cataclysmic variables, accreting white dwarfs, and contact binaries — sources whose complex waveforms are nearly invisible to a sine-wave detector. FPW recovers all of them.

The algorithm's versatility shows in the variety it handles. Eclipsing systems produce sharp dips with flat tops — nothing like a sinusoid. Accreting compact objects generate asymmetric multi-peaked patterns that shift with orbital phase. Cyclotron emitters pulse in ways that depend on the viewer's angle relative to the magnetic field axis.

![Figure 3](/iaifi-research-blog/figures/2502_00243/figure_2.png)

![Figure 4](/iaifi-research-blog/figures/2502_00243/figure_2.png)

For each candidate period, FPW constructs a periodogram — a landscape of *S_FPW* values versus frequency. A real period stands out as a sharp peak above the noise floor. The team validates FPW on known ZTF variable stars, recovering periods cleanly across all these morphologies where Lomb-Scargle produces weak or aliased detections.

![Figure 5](/iaifi-research-blog/figures/2502_00243/figure_3.png)

FPW also handles **irregularly sampled time series** naturally. ZTF doesn't observe every source on a perfect schedule, and the algorithm takes uneven gaps in stride. The implementation runs efficiently on both CPUs and GPUs, with open code available for both platforms.

![Figure 6](/iaifi-research-blog/figures/2502_00243/figure_3.png)

## Why It Matters

The timing of this work is no accident. The **Vera Rubin Observatory's Legacy Survey of Space and Time (LSST)** will push object counts higher and observation cadences denser. Algorithms adequate for millions of sources become bottlenecks at billions. FPW was designed with this scaling crisis in mind — its explicit target is ZTF's full 1.5-billion-object dataset, and it's already running in production.

Beyond scale, the waveform-agnostic design unlocks astrophysics that model-specific algorithms obscure. The diversity of periodic variable stars is a window into stellar physics: mass transfer, magnetic fields, orbital dynamics, interior structure. A period-finder blind to non-sinusoidal signals is systematically blind to entire classes of objects. FPW removes that bias.

A companion paper will provide the full Gaussian Process derivation, quantitative comparisons across waveform types, and rigorous statistical characterization — laying the groundwork for FPW to become a community standard.

> **Bottom Line:** FPW delivers waveform-agnostic period detection grounded in Bayesian statistics, running fast enough to process 1.5 billion ZTF light curves — a critical capability as the era of billion-source sky surveys arrives.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies Gaussian Process machine learning methodology to classical astrophysical time-series analysis, producing a period-finding algorithm that is both theoretically grounded and computationally scalable to billion-source surveys.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">FPW demonstrates how GP-derived probabilistic frameworks can be condensed into simple, hardware-accelerated statistics — a template for deploying ML-inspired inference at production scale in data-intensive science.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By detecting periodic signals across the full waveform diversity of variable stars, FPW expands access to compact object physics — accreting white dwarfs, eclipsing binaries, cyclotron emitters — encoding fundamental interactions in extreme environments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">A follow-up paper will provide rigorous statistical benchmarking and full GP derivations; the algorithm and GPU code are publicly available, with application to ZTF's 1.5 billion-object dataset ongoing (arXiv forthcoming from Finkbeiner, Prince & Whitebook).</span></div></div>
</div>
