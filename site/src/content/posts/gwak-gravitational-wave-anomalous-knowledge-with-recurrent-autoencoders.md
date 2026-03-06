---
abstract: Matched-filtering detection techniques for gravitational-wave (GW) signals
  in ground-based interferometers rely on having well-modeled templates of the GW
  emission. Such techniques have been traditionally used in searches for compact binary
  coalescences (CBCs), and have been employed in all known GW detections so far. However,
  interesting science cases aside from compact mergers do not yet have accurate enough
  modeling to make matched filtering possible, including core-collapse supernovae
  and sources where stochasticity may be involved. Therefore the development of techniques
  to identify sources of these types is of significant interest. In this paper, we
  present a method of anomaly detection based on deep recurrent autoencoders to enhance
  the search region to unmodeled transients. We use a semi-supervised strategy that
  we name Gravitational Wave Anomalous Knowledge (GWAK). While the semi-supervised
  nature of the problem comes with a cost in terms of accuracy as compared to supervised
  techniques, there is a qualitative advantage in generalizing experimental sensitivity
  beyond pre-computed signal templates. We construct a low-dimensional embedded space
  using the GWAK method, capturing the physical signatures of distinct signals on
  each axis of the space. By introducing signal priors that capture some of the salient
  features of GW signals, we allow for the recovery of sensitivity even when an unmodeled
  anomaly is encountered. We show that regions of the GWAK space can identify CBCs,
  detector glitches and also a variety of unmodeled astrophysical sources.
arxivId: '2309.11537'
arxivUrl: https://arxiv.org/abs/2309.11537
authors:
- Ryan Raikman
- Eric A. Moreno
- Ekaterina Govorkova
- Ethan J Marx
- Alec Gunny
- William Benoit
- Deep Chatterjee
- Rafia Omer
- Muhammed Saleem
- Dylan S Rankin
- Michael W Coughlin
- Philip C Harris
- Erik Katsavounidis
concepts:
- anomaly detection
- autoencoders
- gravitational waves
- semi-supervised learning
- recurrent networks
- representation learning
- unmodeled transient search
- embeddings
- out-of-distribution detection
- dimensionality reduction
- signal detection
- transformers
figures:
- /iaifi-research-blog/figures/2309_11537/figure_1.png
- /iaifi-research-blog/figures/2309_11537/figure_2.png
- /iaifi-research-blog/figures/2309_11537/figure_3.png
pdfUrl: https://arxiv.org/pdf/2309.11537v1
published: '2023-09-20T18:00:00+00:00'
theme: Experimental Physics
title: 'GWAK: Gravitational-Wave Anomalous Knowledge with Recurrent Autoencoders'
wordCount: 1084
---

## The Big Picture

Imagine trying to identify every bird species by sound, but you only have recordings of robins. Your identification system would be excellent at spotting robins — and utterly blind to everything else. That's roughly the situation gravitational-wave astronomers have been living with.

Every detection made by LIGO and Virgo — the world's most sensitive gravitational-wave detectors — has relied on **matched filtering**, a technique that compares incoming data against a library of pre-computed signal templates. If your signal isn't in the library, it's invisible.

For compact binary mergers — black holes and neutron stars spiraling together — this works beautifully. Physicists can solve Einstein's equations and generate precise waveform predictions ahead of time. But the universe has other tricks up its sleeve.

Core-collapse supernovae (the violent deaths of massive stars), cosmic strings (hypothetical filaments left over from the earliest moments after the Big Bang), neutron star glitches, and exotic primordial black holes all either lack accurate theoretical models or involve too much randomness for any single template to capture. The gravitational-wave sky is almost certainly full of signals we've never heard, and current detectors would walk right past them.

A team from MIT, the University of Minnesota, and the University of Pennsylvania built a system to change that. Their method, **GWAK** (Gravitational-Wave Anomalous Knowledge), uses deep learning to hunt for signals no one has thought to look for yet.

> **Key Insight:** GWAK learns what "interesting" looks like in gravitational-wave data without needing precise signal models — enabling the first systematic search for genuinely unknown astrophysical transients.

## How It Works

The core of GWAK is a **recurrent autoencoder** — a neural network that ingests a time-series signal, compresses it into a compact internal representation, and then reconstructs the original. Think of it as a smart compression algorithm: important signal structure survives; random noise gets discarded.

The network learns this compression using **Long Short-Term Memory (LSTM)** units, specialized memory cells that capture patterns unfolding over time — well-suited for the oscillating, chirping nature of gravitational waves.

But reconstruction loss alone isn't enough. An autoencoder trained only on background noise will happily reconstruct some signals too, blurring the distinction between noise and something real. GWAK takes a different path.

Instead of a single general-purpose autoencoder, the team trains **multiple specialized autoencoders**, each optimized to reconstruct a different class of signal:

- **Background noise** — the normal detector output
- **Compact binary coalescences (CBCs)** — the chirp-and-merge waveforms already in the detection catalog
- **Sine-Gaussians** — simple oscillating bursts serving as a proxy for generic transients
- **Glitches** — non-astrophysical artifacts from the detectors themselves

![Figure 1](/iaifi-research-blog/figures/2309_11537/figure_1.png)

Each autoencoder produces a reconstruction error score for any incoming data. A signal resembling a CBC will have low loss on the CBC autoencoder and high loss on the others. These scores assemble into a single **low-dimensional embedded space** — the GWAK space — a map where each axis represents one signal class and data points with similar properties cluster together. Real signals separate from noise not by any single score, but by where they land in this multi-dimensional map.

This semi-supervised strategy is what makes GWAK genuinely novel. Rather than labeling data as "signal" or "noise" and training a classifier directly, GWAK lets the geometry of the embedded space do the work. A previously unknown signal type should still cluster somewhere distinct, because it will preferentially resemble some priors more than others and appear coherently across multiple detectors simultaneously.

![Figure 2](/iaifi-research-blog/figures/2309_11537/figure_2.png)

The researchers also enforced **cross-detector coherence** as a hard constraint. A real gravitational wave must appear consistently at both LIGO Hanford and LIGO Livingston, with the appropriate light-travel-time delay. Detector glitches, by contrast, appear in only one instrument. This requirement dramatically suppresses false alarms without requiring any signal model at all.

When tested on real LIGO data, GWAK successfully carved out distinct regions of its embedded space for CBCs, for glitches, and — crucially — for simulated core-collapse supernovae never used in training. The system recovered sensitivity to unmodeled sources because those sources share qualitative features (coherence, oscillatory content) with the known priors.

![Figure 3](/iaifi-research-blog/figures/2309_11537/figure_3.png)

## Why It Matters

Every gravitational-wave detection to date has confirmed something theorists already expected. Black holes merge. Neutron stars merge. The matches between observation and template are spectacular — and also slightly circular. We find what we know to look for.

GWAK represents a genuine expansion of sensitivity to the unknown. Core-collapse supernovae are among the most energetic events in the universe; detecting their gravitational-wave signatures would give astrophysicists a window directly into the collapsing stellar core — a region permanently hidden from light. Cosmic strings, if they exist, would be direct relics of phase transitions in the early universe. These aren't marginal science cases; they're among the most consequential open questions in fundamental physics.

The broader lesson extends well beyond gravitational waves. Semi-supervised anomaly detection — learning rich structure from both labeled and unlabeled data, then using that structure to identify genuinely novel phenomena — is increasingly important anywhere theoretical priors are incomplete. Particle physics, cosmology, medical imaging: supervised methods excel at finding what you expect; GWAK-style approaches are designed for the surprises.

Future work could expand the prior library, incorporate data from Virgo and KAGRA, or adapt the architecture for real-time low-latency alerts. The researchers frame GWAK as complementary to matched filtering, not a replacement — a tool for the part of the sky that templates don't reach.

> **Bottom Line:** GWAK proves that a carefully designed semi-supervised autoencoder can locate genuine astrophysical signals in gravitational-wave data without knowing what those signals look like in advance — opening the detector network to a much wider universe.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges deep learning methodology from high-energy physics anomaly detection with gravitational-wave observational astronomy, deploying recurrent neural networks to solve a fundamental signal-discovery problem in the LIGO/Virgo network.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">GWAK demonstrates a semi-supervised architecture in which multiple specialized autoencoders jointly construct a geometrically meaningful embedding space — a transferable design pattern for anomaly detection in any domain with incomplete signal priors.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By extending gravitational-wave searches beyond matched-filter templates, GWAK opens experimental sensitivity to core-collapse supernovae, cosmic strings, and exotic sources whose discovery could reveal new physics inaccessible through any other observational channel.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions include real-time deployment and integration with additional IGWN detectors; the full method is described in arXiv:2209.02538 and code is publicly available at github.com/ML4GW/gwak.</span></div></div>
</div>
