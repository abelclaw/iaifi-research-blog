---
abstract: Discoveries of new phenomena often involve a dedicated search for a hypothetical
  physics signature. Recently, novel deep learning techniques have emerged for anomaly
  detection in the absence of a signal prior. However, by ignoring signal priors,
  the sensitivity of these approaches is significantly reduced. We present a new strategy
  dubbed Quasi Anomalous Knowledge (QUAK), whereby we introduce alternative signal
  priors that capture some of the salient features of new physics signatures, allowing
  for the recovery of sensitivity even when the alternative signal is incorrect. This
  approach can be applied to a broad range of physics models and neural network architectures.
  In this paper, we apply QUAK to anomaly detection of new physics events at the CERN
  Large Hadron Collider utilizing variational autoencoders with normalizing flow.
arxivId: '2011.03550'
arxivUrl: https://arxiv.org/abs/2011.03550
authors:
- Sang Eon Park
- Dylan Rankin
- Silviu-Marian Udrescu
- Mikaeel Yunus
- Philip Harris
concepts:
- anomaly detection
- new physics searches
- signal priors
- variational autoencoders
- normalizing flows
- semi-supervised learning
- collider physics
- likelihood ratio
- density estimation
- out-of-distribution detection
- jet physics
- simulation-based inference
figures:
- /iaifi-research-blog/figures/2011_03550/figure_1.png
- /iaifi-research-blog/figures/2011_03550/figure_2.png
- /iaifi-research-blog/figures/2011_03550/figure_3.png
pdfUrl: https://arxiv.org/pdf/2011.03550v4
published: '2020-11-06T19:00:02+00:00'
theme: Experimental Physics
title: 'Quasi Anomalous Knowledge: Searching for new physics with embedded knowledge'
wordCount: 1016
---

## The Big Picture

Imagine you've lost your keys somewhere in your house. You could search every room randomly — thorough but exhausting. Or you could go straight to the spots you always leave them — fast, but you'd miss anywhere unusual. Now imagine a third option: you don't know exactly where they are, but you know your habits well enough to focus your search intelligently.

That's roughly what physicists at the LHC face every time they hunt for new particles — and it's the intuition behind a clever new technique called QUAK.

For over a decade, the Large Hadron Collider at CERN has smashed protons together at record energies, generating torrents of data. Despite exhaustive searching, no clear sign of new physics has emerged beyond the Standard Model — the well-tested rulebook that describes all known particles and forces. This has pushed physicists toward a provocative question: what if we're looking in the wrong way?

Traditional searches require you to know, at least roughly, what you're looking for — you build a detailed model of a new particle, simulate its signature, and scan the data for it. But what about physics we haven't imagined yet? Purely automatic "oddity detectors" try to flag anything unusual, but without guidance about what unusual looks like in physics terms, they cast such a wide net they become nearly useless.

A team of MIT researchers — Sang Eon Park, Dylan Rankin, Silviu-Marian Udrescu, Mikaeel Yunus, and Philip Harris — developed a strategy that sits deliberately between these extremes: **Quasi Anomalous Knowledge**, or QUAK, a hybrid approach that uses approximate, possibly-wrong signal guesses to dramatically boost the power of anomaly searches.

> **Key Insight:** QUAK embeds "good enough" physics intuitions into an anomaly detector — even when the assumed signal is wrong, the detector recovers sensitivity that fully blind approaches miss.

## How It Works

The central idea is deceptively elegant. Instead of asking "does this event look normal?" (the pure anomaly approach) or "does this event look exactly like a black hole?" (the dedicated search approach), QUAK asks: "does this event look like *something physically plausible but unexpected*?"

![Figure 1](/iaifi-research-blog/figures/2011_03550/figure_1.png)

QUAK constructs a **multi-dimensional loss space** — a coordinate system where each axis measures how well a different neural network can reconstruct an event. The trick is training multiple **variational autoencoders (VAEs)** — networks that compress data into a compact representation and try to rebuild it from scratch — each on a different dataset:

- One VAE trained on **background** (ordinary Standard Model collisions)
- One or more VAEs trained on **proxy signals** — hypothetical new physics signatures that may or may not match the real unknown signal

When a collision event passes through all these networks, it produces a set of reconstruction losses. Background events reconstruct well on the background VAE and poorly on the signal VAEs; true new physics events show the reverse. The resulting multi-dimensional score separates signal from background even when the proxy signal used during training wasn't exactly right.

The paper enhances this with **normalizing flows** — generative models that transform complex probability distributions into simple, well-understood ones, enabling a precise probability score rather than just a reconstruction error. This combination of VAE plus normalizing flow gives QUAK sharper discrimination than either approach alone.

![Figure 2](/iaifi-research-blog/figures/2011_03550/figure_2.png)

The team validated QUAK on two test cases. First, the MNIST handwritten digit dataset served as proof of concept: could QUAK find a "target" digit using a "proxy" digit as a stand-in? The answer was yes — even with the wrong proxy, performance stayed dramatically better than blind anomaly detection. Then came the real test: the **LHC Olympics 2020** challenge dataset, a community benchmark with hidden new-physics signals injected into simulated LHC collisions. QUAK successfully identified the signal in the first "black box" challenge — a resonance decaying to two jets with anomalous substructure — recovering sensitivity that pure autoencoder approaches missed.

## Why It Matters

The broader implication extends well beyond any single LHC search. Physics has accumulated enormous domain knowledge about how new particles should behave: they must obey the fundamental symmetries of space and time, conserve energy and momentum, and produce collision fragments within predictable regions of the detector. Purely data-driven anomaly detectors discard all of this. QUAK offers a systematic way to inject that knowledge back in — not as a rigid constraint, but as a flexible guide that shapes the search without blinding it.

![Figure 3](/iaifi-research-blog/figures/2011_03550/figure_3.png)

This work also opens a rich space of algorithmic questions. How similar does the proxy signal need to be? Can multiple competing proxies cover more of signal space simultaneously? The results suggest robustness is genuine: performance degrades gracefully rather than catastrophically when the proxy is wrong. That's precisely the property needed for a practical search tool deployed against data where no one knows the answer in advance.

Future directions include extending QUAK to higher-dimensional final states, incorporating network designs that respect physical symmetries, and applying the framework beyond collider physics — astrophysical transients, medical anomaly detection, materials discovery — wherever domain knowledge is available but incomplete.

> **Bottom Line:** QUAK demonstrates that "approximately right" signal priors are far more valuable than no priors at all — a simple but powerful insight that could reshape how the LHC, and science more broadly, hunts for the unknown.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">QUAK directly bridges machine learning methodology and particle physics domain expertise, using learned latent representations to encode physical intuitions that guide anomaly searches at collider experiments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work advances semi-supervised anomaly detection by showing that approximate, potentially incorrect class priors still dramatically improve sensitivity over fully unsupervised baselines — a finding with broad implications beyond physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling sensitivity recovery for new physics signatures at the LHC without requiring exact signal knowledge, QUAK expands the practical reach of model-agnostic new physics searches at CERN.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will explore richer proxy signal libraries, equivariant network architectures, and application to additional LHC Olympics black boxes; see arXiv:2011.03550 for the full methodology and results.</span></div></div>
</div>
