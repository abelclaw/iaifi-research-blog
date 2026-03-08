---
abstract: Anomaly detection - identifying deviations from Standard Model predictions
  - is a key challenge at the Large Hadron Collider due to the size and complexity
  of its datasets. This is typically addressed by transforming high-dimensional detector
  data into lower-dimensional, physically meaningful features. We tackle feature extraction
  for anomaly detection by learning powerful low-dimensional representations via contrastive
  neural embeddings. This approach preserves potential anomalies indicative of new
  physics and enables rare signal extraction using novel machine learning-based statistical
  methods for signal-independent hypothesis testing. We compare supervised and self-supervised
  contrastive learning methods, for both MLP- and Transformer-based neural embeddings,
  trained on the kinematic observables of physics objects in LHC collision events.
  The learned embeddings serve as input representations for signal-agnostic statistical
  detection methods in inclusive final states. We achieve significant improvement
  in discovery power for both rare new physics signals and rare Standard Model processes
  across diverse final states, demonstrating its applicability for efficiently searching
  for diverse signals simultaneously. We study the impact of architectural choices,
  contrastive loss formulations, supervision levels, and embedding dimensionality
  on anomaly detection performance. We show that the optimal representation for background
  classification does not always maximize sensitivity to new physics signals, revealing
  an inherent trade-off between background structure preservation and anomaly enhancement.
  We demonstrate that combining compression with domain knowledge for label encoding
  produces the most effective data representation for statistical discovery of anomalies.
arxivId: '2502.15926'
arxivUrl: https://arxiv.org/abs/2502.15926
authors:
- Kyle Metzger
- Lana Xu
- Mia Sodini
- Thea K. Arrestad
- Katya Govorkova
- Gaia Grosso
- Philip Harris
concepts:
- contrastive learning
- anomaly detection
- representation learning
- embeddings
- new physics searches
- collider physics
- self-supervised learning
- signal-agnostic search
- dimensionality reduction
- feature extraction
- hypothesis testing
- transformers
- semi-supervised learning
figures:
- /iaifi-research-blog/figures/2502_15926/figure_1.png
- /iaifi-research-blog/figures/2502_15926/figure_1.png
- /iaifi-research-blog/figures/2502_15926/figure_2.png
- /iaifi-research-blog/figures/2502_15926/figure_2.png
- /iaifi-research-blog/figures/2502_15926/figure_3.png
- /iaifi-research-blog/figures/2502_15926/figure_3.png
pdfUrl: https://arxiv.org/pdf/2502.15926v2
published: '2025-02-21T20:47:08+00:00'
theme: Experimental Physics
title: Anomaly preserving contrastive neural embeddings for end-to-end model-independent
  searches at the LHC
wordCount: 1025
---

## The Big Picture

Imagine searching for a single misspelled word in every book ever printed — not knowing what word you're looking for, or even what language it might be in. That's roughly the challenge physicists face at the Large Hadron Collider. Every second, the LHC produces roughly 40 million proton collisions, and somewhere buried in that avalanche of data might be a particle or interaction that rewrites the textbook on fundamental physics. The catch: you don't know what it looks like.

This is the core problem of **model-independent anomaly detection** — hunting for signs of new physics without a specific theory to guide the search. Standard approaches compress the LHC's raw sensor data into a handful of physically meaningful numbers: particle energies, momenta (direction and force of motion), masses, and directions. But measurements hand-picked to capture known physics might inadvertently discard exactly the subtle patterns that signal something genuinely new.

A new study from MIT and ETH Zürich, led by Kyle Metzger and collaborators at IAIFI, takes a different route: let the machine learn its own compact representation of collision events — one designed from the ground up to preserve anomalies rather than smooth them away.

> **Key Insight:** Contrastive neural embeddings can learn low-dimensional representations of LHC collision data that are far more sensitive to rare new physics signals than classical feature engineering, but only when the right balance is struck between organizing background events and leaving room for anomalies to stand out.

## How It Works

The core idea borrows from **contrastive learning** — a technique that teaches a neural network what "similar" and "different" mean without explicit labels. The network sees pairs or groups of events and learns to map them into a compact geometric space: events that look alike cluster together, while unusual events get pushed to the outskirts.

![Figure 1](/iaifi-research-blog/figures/2502_15926/figure_1.png)

The researchers trained two flavors of contrastive **embeddings** — compact mathematical fingerprints of each collision event:

- **Supervised contrastive learning**, where physics labels (particle types, process categories) guide the clustering
- **Self-supervised contrastive learning**, where the network discovers structure on its own by randomly dropping or perturbing particle objects within an event to create "views" of the same underlying collision

Both were tested with two neural architectures: **multilayer perceptrons (MLPs)** — a classic type of neural network that processes a fixed set of particle-level features — and **Transformers**, the same architecture behind modern language models, which treat each collision event as a variable-length sequence of physics objects and capture relationships between particles more effectively.

The inputs are measured properties of motion — energies, directions, and masses — of reconstructed physics objects: jets (sprays of particles from quark or gluon scattering), leptons (fundamental particles like electrons and muons), and missing energy (a signature of particles that escape the detector unseen). The network compresses all of this into an embedding with as few as 4 to 16 dimensions.

![Figure 2](/iaifi-research-blog/figures/2502_15926/figure_1.png)

These embeddings feed into **signal-agnostic statistical detection methods** — algorithms that scan for unusual clusters in the embedding space without being told what signal to look for. Tested against a suite of benchmark new-physics signals and rare Standard Model processes, the contrastive embeddings consistently outperform hand-crafted features, achieving substantially higher sensitivity to injected rare signals at fixed false-positive rates.

## Why It Matters

The most striking finding isn't a benchmark number — it's a conceptual warning. The researchers discovered an **inherent tension** between two goals that might seem aligned: learning to classify background events accurately and learning to detect anomalies.

![Figure 3](/iaifi-research-blog/figures/2502_15926/figure_2.png)

When you optimize a representation to organize known background processes as cleanly as possible, you inadvertently suppress the very irregularities that make new physics stand out. A perfectly organized background leaves no room for the unexpected. The best representation for known physics is *not* the best representation for discovering unknown physics — a subtle but consequential distinction that shapes how future searches should be designed.

The sweet spot lies in combining two things: **data compression** (forcing the network to be selective about what it preserves) and domain knowledge (using physics-motivated labels to guide which background structures get organized). Supervised labels without compression risk encoding too much background detail; compression without guidance can lose signal-relevant structure. Together, they produce embeddings that strike the right balance.

![Figure 4](/iaifi-research-blog/figures/2502_15926/figure_2.png)

The LHC's Run 3 is generating data at unprecedented rates, and the High-Luminosity LHC upgrade will push this further still. Model-independent searches are increasingly viewed as essential complements to targeted searches — but their power depends entirely on the quality of the representation feeding into them. This work demonstrates that a single trained embedding can simultaneously search for diverse signals across different final states, standing watch across the full complexity of LHC collision data.

Open questions remain. How do these embeddings behave under detector systematics and real experimental noise? Can self-supervised versions be deployed in real-time trigger systems to catch anomalies before data is written to disk? The path from benchmark study to deployed LHC analysis is long, but this work charts a clear direction.

![Figure 5](/iaifi-research-blog/figures/2502_15926/figure_3.png)

> **Bottom Line:** By learning compact, anomaly-preserving representations of LHC collision events through contrastive training, researchers have built a more sensitive radar for new physics — one that searches broadly across diverse signals without needing to know what it's looking for.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges contrastive representation learning from computer vision and NLP with the demands of high-energy physics anomaly detection, adapting self-supervised and supervised contrastive objectives to the structure of LHC collision data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The study uncovers a fundamental trade-off between background classification performance and anomaly sensitivity in learned representations — a broadly applicable insight for any ML system tasked with open-ended anomaly detection in complex domains.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The contrastive embeddings deliver significant gains in discovery power for rare new physics signals at the LHC, advancing the toolkit for model-independent searches that could reveal physics beyond the Standard Model.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will explore deploying these embeddings in real-time LHC trigger systems and testing robustness under realistic experimental conditions; the full study is available at arXiv:2501.01496.</span></div></div>
</div>
