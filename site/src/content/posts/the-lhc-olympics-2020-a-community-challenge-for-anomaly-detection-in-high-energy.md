---
abstract: 'A new paradigm for data-driven, model-agnostic new physics searches at
  colliders is emerging, and aims to leverage recent breakthroughs in anomaly detection
  and machine learning. In order to develop and benchmark new anomaly detection methods
  within this framework, it is essential to have standard datasets. To this end, we
  have created the LHC Olympics 2020, a community challenge accompanied by a set of
  simulated collider events. Participants in these Olympics have developed their methods
  using an R&D dataset and then tested them on black boxes: datasets with an unknown
  anomaly (or not). This paper will review the LHC Olympics 2020 challenge, including
  an overview of the competition, a description of methods deployed in the competition,
  lessons learned from the experience, and implications for data analyses with future
  datasets as well as future colliders.'
arxivId: '2101.08320'
arxivUrl: https://arxiv.org/abs/2101.08320
authors:
- Gregor Kasieczka
- Benjamin Nachman
- David Shih
- Oz Amram
- Anders Andreassen
- Kees Benkendorfer
- Blaz Bortolato
- Gustaaf Brooijmans
- Florencia Canelli
- Jack H. Collins
- Biwei Dai
- Felipe F. De Freitas
- Barry M. Dillon
- Ioan-Mihail Dinu
- Zhongtian Dong
- Julien Donini
- Javier Duarte
- D. A. Faroughy
- Julia Gonski
- Philip Harris
- Alan Kahn
- Jernej F. Kamenik
- Charanjit K. Khosa
- Patrick Komiske
- Luc Le Pottier
- Pablo Martín-Ramiro
- Andrej Matevc
- Eric Metodiev
- Vinicius Mikuni
- Inês Ochoa
- Sang Eon Park
- Maurizio Pierini
- Dylan Rankin
- Veronica Sanz
- Nilai Sarda
- Urous Seljak
- Aleks Smolkovic
- George Stein
- Cristina Mantilla Suarez
- Manuel Szewc
- Jesse Thaler
- Steven Tsan
- Silviu-Marian Udrescu
- Louis Vaslin
- Jean-Roch Vlimant
- Daniel Williams
- Mikaeel Yunus
concepts:
- anomaly detection
- new physics searches
- collider physics
- model-agnostic search
- jet physics
- autoencoders
- variational autoencoders
- density estimation
- normalizing flows
- bump hunting
- semi-supervised learning
- clustering
- graph neural networks
- generative adversarial networks
- simulation-based inference
figures:
- /iaifi-research-blog/figures/2101_08320/figure_1.png
- /iaifi-research-blog/figures/2101_08320/figure_2.png
- /iaifi-research-blog/figures/2101_08320/figure_3.png
pdfUrl: https://arxiv.org/pdf/2101.08320v1
published: '2021-01-20T21:03:06+00:00'
theme: Experimental Physics
title: 'The LHC Olympics 2020: A Community Challenge for Anomaly Detection in High
  Energy Physics'
wordCount: 1039
---

## The Big Picture

Imagine you're a detective, but you have no idea what the crime even looks like. You have millions of fingerprints, footprints, and fragments of evidence, yet no suspect profile, no witness account, no theory of what happened. Your only clue: something unusual is probably hiding in the noise. That's the challenge physicists face when hunting for new particles at the Large Hadron Collider (LHC).

For decades, the dominant strategy at the LHC has been **model-dependent**: physicists pick a specific theory (say, supersymmetry, the idea that every known particle has a heavier "partner"), simulate what that particle would look like, and search the data for exactly that signature. This approach led to the 2012 discovery of the Higgs boson. But what if the new physics doesn't look like anything theorists have imagined? What if we've been carrying a shopping list to a store that sells something entirely different?

That worry drove a different approach: **model-agnostic anomaly detection**, where machine learning algorithms learn what "normal" looks like and flag anything that doesn't fit, without being told what to look for. Think of it as teaching a computer to spot forgeries without showing it what every possible fake looks like. To put this idea through its paces, a large consortium of physicists organized the **LHC Olympics 2020**, a community challenge that pitted over a dozen algorithms against hidden datasets containing unknown, or possibly absent, signals.

> **Key Insight:** The LHC Olympics 2020 created a shared testing ground for anomaly detection in particle physics, showing which approaches can identify unknown new physics buried in realistic collider data and which fall short.

## How It Works

The challenge was built around blind testing. Organizers provided an **R&D dataset** of simulated proton-proton collisions at 13 TeV, the highest collision energy ever achieved. This dataset contained a known injected signal: a hypothetical heavy **resonance** (a short-lived particle that decays almost instantly into two **boosted jets**, fast-moving, tightly bundled sprays of particles). Teams used it to develop and tune their methods.

Then came the hard part: three **black boxes**, each containing either no signal, the same type of signal, or something completely different. Teams had to figure out not just what the anomaly was, but whether one existed at all.

![Figure 1](/iaifi-research-blog/figures/2101_08320/figure_1.png)

Participants deployed methods across three broad categories:

- **Unsupervised methods** learn background structure with no labeled signal examples. These included **variational autoencoders (VAEs)**, which compress each collision event into a compact internal representation and flag events the network struggles to reconstruct, since rare signals are harder to reproduce than common background. Density estimation techniques model normal events and score outliers by how improbable they are. Clustering approaches like **UCluster** group similar events and look for outlier clusters.

- **Weakly supervised methods** distinguish signal from background without explicit signal labels. The most prominent, **CWoLa Hunting** (Classification Without Labels), trains a classifier to tell apart two **mass sidebands**, the data regions flanking the mass range of interest. If a localized signal sits between those sidebands, it makes them statistically distinguishable.

- **(Semi)-supervised methods** inject theoretical priors about what signals might look like. **QUAK** (Quasi-Anomalous Knowledge) trained on a library of plausible-but-wrong signal hypotheses to build a general-purpose anomaly score.

The target observable was the **dijet invariant mass** spectrum, the combined-mass distribution of jet pairs produced in a collision. A genuine new resonance would show up as a localized **bump** on an otherwise smooth, falling distribution. Most methods tried to enhance any such bump by reweighting or filtering events based on anomaly scores.

![Figure 2](/iaifi-research-blog/figures/2101_08320/figure_2.png)

## Why It Matters

The results were mixed, and instructively so. Black Box 1 contained the same resonance as the R&D dataset, and many methods cracked it. CWoLa Hunting and several autoencoder-based approaches recovered statistically significant excesses. Black Box 3 was a different beast: a signal with unusual jet substructure that looked nothing like the training data. Methods tuned on the R&D signal struggled, while more general unsupervised approaches fared better. Black Box 2 contained no signal at all, testing whether methods would cry wolf.

The real takeaway isn't which method won. No single algorithm dominated across all scenarios. Weakly supervised methods were powerful when the signal was resonant and localized in mass, but blind to non-resonant anomalies. Unsupervised methods were more general but often less sensitive.

This suggests that **ensemble strategies**, combining multiple complementary algorithms, may be the most reliable path forward. The challenge also exposed a hard practical problem: **decorrelation**. If an anomaly score inadvertently sculpts artificial bumps in the mass spectrum (false positives from the algorithm's own biases, not real physics), the whole search is compromised. This remains an open problem across the field.

![Figure 3](/iaifi-research-blog/figures/2101_08320/figure_3.png)

The LHC Olympics model matters for what comes next. Run 3 of the LHC and the forthcoming **High-Luminosity LHC** will deliver vastly larger datasets where rare signals become statistically accessible. Follow-up challenges are already being planned with more diverse signal types, higher-dimensional inputs, and real detector effects. For future colliders like the FCC or a muon collider, model-agnostic searches may be even more important: we know even less about what to expect at those energy frontiers.

> **Bottom Line:** The LHC Olympics 2020 showed that machine learning can find hidden signals in collider data without being told what to look for, and it produced the community infrastructure, datasets, and benchmarks to keep this effort moving.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits at the intersection of modern machine learning (variational autoencoders, GANs, density estimation, weakly supervised classification) and particle physics. It shows that AI techniques can function as real discovery tools at the LHC, not just analysis aids.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The challenge produced a domain-specific benchmark for anomaly detection algorithms, exposing failure modes and generalization limits that matter well beyond particle physics, anywhere unsupervised or weakly supervised learning is applied to messy real-world data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Model-agnostic searches expand the LHC's discovery reach to signatures no theorist has specifically predicted, opening up parts of the search space that traditional analyses miss entirely.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future LHC Olympics editions will incorporate more complex signals, real detector data, and higher-dimensional inputs. Full challenge results and datasets are described in [arXiv:2101.08320](https://arxiv.org/abs/2101.08320).</span></div></div>
</div>
