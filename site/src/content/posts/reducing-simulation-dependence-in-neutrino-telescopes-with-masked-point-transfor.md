---
abstract: Machine learning techniques in neutrino physics have traditionally relied
  on simulated data, which provides access to ground-truth labels. However, the accuracy
  of these simulations and the discrepancies between simulated and real data remain
  significant concerns, particularly for large-scale neutrino telescopes that operate
  in complex natural media. In recent years, self-supervised learning has emerged
  as a powerful paradigm for reducing dependence on labeled datasets. Here, we present
  the first self-supervised training pipeline for neutrino telescopes, leveraging
  point cloud transformers and masked autoencoders. By shifting the majority of training
  to real data, this approach minimizes reliance on simulations, thereby mitigating
  associated systematic uncertainties. This represents a fundamental departure from
  previous machine learning applications in neutrino telescopes, paving the way for
  substantial improvements in event reconstruction and classification.
arxivId: '2510.01733'
arxivUrl: https://arxiv.org/abs/2510.01733
authors:
- Felix J. Yu
- Nicholas Kamp
- Carlos A. Argüelles
concepts:
- self-supervised learning
- neutrino detection
- transformers
- autoencoders
- robustness
- event reconstruction
- simulation-to-real transfer
- detector simulation
- transfer learning
- fine-tuning
- representation learning
- geometric deep learning
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2510_01733/figure_1.png
- /iaifi-research-blog/figures/2510_01733/figure_1.png
- /iaifi-research-blog/figures/2510_01733/figure_2.png
- /iaifi-research-blog/figures/2510_01733/figure_2.png
- /iaifi-research-blog/figures/2510_01733/figure_3.png
- /iaifi-research-blog/figures/2510_01733/figure_3.png
pdfUrl: https://arxiv.org/pdf/2510.01733v2
published: '2025-10-02T07:18:19+00:00'
theme: Experimental Physics
title: Reducing Simulation Dependence in Neutrino Telescopes with Masked Point Transformers
wordCount: 1010
---

## The Big Picture

Imagine teaching a detective to recognize crime scenes using only staged photographs. The fake blood looks different from real blood, the lighting is too controlled, and the props don't behave like actual evidence. When that detective arrives at a real crime scene, the mismatches cause confusion. That's essentially the problem facing physicists at IceCube, one of the world's largest neutrino detectors, buried a mile beneath the Antarctic ice.

Neutrino telescopes are extraordinary machines. Arrays of thousands of light sensors, deep in glacial ice or seawater, catch the faint flashes produced when neutrinos — ghostly particles that barely interact with matter — occasionally collide with ice molecules and produce charged particles. The problem: these detectors operate in messy, complex natural environments. The ice has bubbles, the water has currents, and the sensors degrade over time.

For decades, physicists have trained their machine learning models almost entirely on simulated data — painstakingly detailed computer models that trace every photon through the ice. When those simulations don't perfectly match reality, the models break.

Now, a team of Harvard physicists has developed the first **self-supervised learning pipeline** for neutrino telescopes — a method that learns from raw, unlabeled real detector data rather than requiring carefully labeled examples. This fundamentally changes how these instruments can be trained, dramatically reducing how much they need to trust their simulations.

> **Key Insight:** By training primarily on real, unlabeled detector data instead of simulations, this approach sidesteps the accuracy gap between simulated and observed physics, making neutrino event reconstruction far more robust to unknown detector effects.

## How It Works

The team's core innovation is **NEPTUNE** — Neutrino Efficient Point Transformer for Ultrarelativistic Neutrino Events. It treats a neutrino event not as an image or a time series, but as a **point cloud**: a collection of light sensors that fired, each tagged with its 3D position and detection time. This natural representation suits a sparse 3D detector where only a fraction of sensors register a signal in any given event.

![Figure 1](/iaifi-research-blog/figures/2510_01733/figure_1.png)

The NEPTUNE architecture has three main components:

1. **Event Tokenizer**: Raw sensor hits are grouped into 3-nanosecond time windows and processed through a small neural network that identifies local patterns. If a high-energy event lights up too many sensors, the tokenizer uses **farthest point sampling** — selecting the most spread-out subset of points to preserve spatial coverage — to choose up to 512 representative points. Each selected point also draws on its 32 nearest neighboring sensors for additional context.

2. **Transformer Encoder**: The resulting tokens feed into a standard transformer architecture — the same fundamental design behind large language models — enriched with each sensor's spatial position and first-hit time.

3. **Prediction Head**: A final task-specific layer handles the actual physics question, whether reconstructing a neutrino's direction or classifying its interaction type.

The real innovation lies in pre-training. Drawing from **masked autoencoders** — where a model learns by having portions of its input randomly hidden and then tries to reconstruct them, an approach that transformed computer vision — the team pre-trains NEPTUNE by concealing between 75% and 100% of sensor positions and timestamps, then challenging the model to reconstruct them. This requires no labels whatsoever. The model learns the internal structure of neutrino events purely from real detector data.

![Figure 2](/iaifi-research-blog/figures/2510_01733/figure_1.png)

After pre-training on unlabeled real data, the model is fine-tuned with a small amount of labeled simulation. The team used **block expansion**: inserting new processing layers — initialized to simply pass information through unchanged — on top of the frozen pre-trained layers. These fresh layers learn the downstream task without overwriting the representations learned from real data, preserving what the model knows about actual detector signals.

## Why It Matters

To test whether this actually helps, the team designed a controlled experiment. They took two simulated datasets, treated one as "real" data and the other as labeled simulation, then deliberately broke them apart by injecting random spurious signals into one at a controlled rate. This mimics a realistic scenario: a detector effect present in the data but entirely absent from the simulation.

The results were striking. Conventionally supervised models — trained entirely on simulation — held up when noise rates were slightly wrong but consistent across both datasets. When the noise effect was completely absent from the simulation, performance degraded sharply. NEPTUNE, pre-trained on the "real" data, maintained strong performance in both cases.

![Figure 3](/iaifi-research-blog/figures/2510_01733/figure_2.png)

This matters beyond IceCube. Neutrino physics is entering a golden age, with next-generation telescopes like IceCube-Gen2, KM3NeT, and Baikal-GVD coming online or under development. These instruments will collect vastly more data and face equally complex, imperfectly understood detector environments. The simulation-dependence problem only compounds at scale.

More broadly, this work opens a new direction: applying self-supervised learning not as a replacement for physics simulation, but as a way to ground models in the messy reality of actual detector data. The same approach could find applications wherever simulation-to-reality gaps create systematic biases — from particle colliders to gravitational wave detectors.

> **Bottom Line:** NEPTUNE demonstrates that training on real, unlabeled detector data can dramatically reduce vulnerability to unmodeled detector effects — a breakthrough that becomes more valuable as next-generation experiments push sensitivity limits.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges transformer-based AI architectures from computer vision with the experimental challenges of large-scale neutrino physics, showing that self-supervised pre-training strategies translate powerfully into fundamental particle detection.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces the first masked autoencoder pre-training pipeline tailored to 3D point cloud data from particle physics detectors, demonstrating that high masking ratios (75–100%) force models to learn physically meaningful representations without any supervision.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By reducing systematic uncertainties from simulation mismodeling, this approach could sharpen neutrino direction reconstruction and flavor classification at IceCube and future gigaton-scale observatories, directly improving measurements of high-energy astrophysical neutrino sources.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The NEPTUNE codebase is publicly available on GitHub; future work will explore applying this pipeline at full IceCube scale. See arXiv:2509.19431 for the full paper presented at ICRC2025.</span></div></div>
</div>
