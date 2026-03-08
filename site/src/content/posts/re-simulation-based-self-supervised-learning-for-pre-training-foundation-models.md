---
abstract: Self-Supervised Learning (SSL) is at the core of training modern large machine
  learning models, providing a scheme for learning powerful representations that can
  be used in a variety of downstream tasks. However, SSL strategies must be adapted
  to the type of training data and downstream tasks required. We propose RS3L ("Re-simulation-based
  self-supervised representation learning"), a novel simulation-based SSL strategy
  that employs a method of re-simulation to drive data augmentation for contrastive
  learning in the physical sciences, particularly, in fields that rely on stochastic
  simulators. By intervening in the middle of the simulation process and re-running
  simulation components downstream of the intervention, we generate multiple realizations
  of an event, thus producing a set of augmentations covering all physics-driven variations
  available in the simulator. Using experiments from high-energy physics, we explore
  how this strategy may enable the development of a foundation model; we show how
  RS3L pre-training enables powerful performance in downstream tasks such as discrimination
  of a variety of objects and uncertainty mitigation. In addition to our results,
  we make the RS3L dataset publicly available for further studies on how to improve
  SSL strategies.
arxivId: '2403.07066'
arxivUrl: https://arxiv.org/abs/2403.07066
authors:
- Philip Harris
- Michael Kagan
- Jeffrey Krupa
- Benedikt Maier
- Nathaniel Woodward
concepts:
- self-supervised learning
- re-simulation augmentation
- contrastive learning
- data augmentation
- representation learning
- jet physics
- physics foundation model
- transfer learning
- detector simulation
- uncertainty quantification
- simulation-based inference
- transformers
figures:
- /iaifi-research-blog/figures/2403_07066/figure_1.png
- /iaifi-research-blog/figures/2403_07066/figure_1.png
- /iaifi-research-blog/figures/2403_07066/figure_2.png
- /iaifi-research-blog/figures/2403_07066/figure_2.png
- /iaifi-research-blog/figures/2403_07066/figure_3.png
- /iaifi-research-blog/figures/2403_07066/figure_3.png
pdfUrl: https://arxiv.org/pdf/2403.07066v2
published: '2024-03-11T18:00:47+00:00'
theme: Experimental Physics
title: Re-Simulation-based Self-Supervised Learning for Pre-Training Foundation Models
wordCount: 1218
---

## The Big Picture

Imagine training a child to recognize dogs. You don't just show them one photo of a golden retriever — you show them golden retrievers in rain, in sunlight, mid-leap, sitting still, photographed from every angle. The variety forces the brain to latch onto what actually defines "dog" rather than memorizing the background.

Now imagine doing the same for a physicist identifying particles at the Large Hadron Collider — where the "photos" are cascades of thousands of subatomic particles, and the "background noise" is quantum mechanics itself.

That's the challenge researchers at MIT, SLAC, and Imperial College London set out to solve. Modern machine learning models are trained using **self-supervised learning (SSL)**, where the model learns by comparing cleverly distorted versions of the same data. But those distortions need to be meaningful. For natural images, rotating or color-shifting a photo makes sense. For particle physics, what counts as a meaningful distortion?

The answer turned out to be straightforward: let the physics simulator generate the distortions. The team's method, **RS3L** (Re-simulation-based Self-Supervised Representation Learning), uses the LHC's own high-fidelity simulation software to produce physically valid "alternate versions" of particle collision events, then uses those to train a foundation model capable of tackling a broad range of physics tasks.

> **Key Insight:** Instead of inventing artificial data augmentations, RS3L intercepts the simulation mid-process and re-runs it from that point forward, generating physically grounded alternate realities of the same collision event.

## How It Works

The process starts with a particle collision simulation. Researchers can't directly observe what happened in a collision; they infer it from the wreckage. One of the most important things to identify is a **jet**: a cone-shaped spray of particles produced when a quark, gluon, or heavy particle like the Higgs boson fragments and hadronizes (breaks down into stable composite particles). Tagging a jet correctly, meaning identifying which particle initiated it, is critical for spotting rare physics phenomena.

Simulating a jet happens in stages. First, the hard collision is computed using perturbative quantum field theory. Then **parton showering** takes over ("parton" being physicist shorthand for quarks and gluons), where secondary particles radiate more particles, which radiate more, until everything stabilizes into detectable **hadrons** (composite particles like protons and pions). That showering step is inherently random: run it again with the same initial conditions and you get a different-looking jet, equally valid from a physics perspective.

RS3L exploits this randomness deliberately:

1. **Intervene** at the point where the initial particle state has been fixed, before parton showering begins.
2. **Re-run** the downstream showering and detector simulation multiple times from that fixed starting point.
3. Each re-run produces a **statistically valid but visually distinct** realization of the same underlying physics event.
4. Feed these pairs to a **contrastive learning** algorithm (specifically SimCLR), which maps both versions of the same event to similar representations while pushing representations of different events apart.

![Figure 1](/iaifi-research-blog/figures/2403_07066/figure_1.png)

The intervention point defines what counts as signal versus noise. Everything upstream of the cut, the hard-scatter physics, is what the model learns to encode. Everything downstream (shower fluctuations, detector smearing) becomes augmentation to integrate out. The researchers call this **domain-complete augmentation**: the full set of physically plausible variations the simulator can produce.

Even better: by deliberately altering simulator settings during re-simulation, such as the hadronization model or detector response, the team can train the model to be robust to **systematic uncertainties** (predictable sources of error that consistently skew measurements in one direction, rather than canceling out like random noise). This matters because real LHC data doesn't perfectly match simulations, and models that overfit to simulation artifacts can fail when deployed on actual detector data.

## Why It Matters

![Figure 2](/iaifi-research-blog/figures/2403_07066/figure_1.png)

RS3L pre-training consistently outperforms or matches supervised baselines across multiple jet-tagging benchmarks, while being far more data-efficient. Pre-trained representations transfer cleanly to tasks the model was never explicitly trained for, which is the whole point of a foundation model. The team tested discrimination of jets from Higgs bosons, top quarks, W/Z bosons, and ordinary **QCD** (quantum chromodynamics, the theory governing how quarks and gluons interact) backgrounds. Fine-tuning the RS3L-pretrained model reliably beats training from scratch, especially when labeled data is scarce.

![Figure 3](/iaifi-research-blog/figures/2403_07066/figure_2.png)

The RS3L strategy applies well beyond particle physics. It works anywhere a stochastic simulator exists and researchers want to learn robust representations: climate modeling, molecular dynamics, cosmological simulations. When the physics is understood well enough to simulate but labeled experimental data is expensive or limited, re-simulation offers a natural route to pre-training.

The publicly released RS3L dataset, hosted on Zenodo, gives the community a shared benchmark for comparing SSL strategies in science. That kind of common benchmark has been lacking compared to computer vision and NLP, where large shared datasets have driven rapid progress.

Open questions remain. How does the choice of intervention point affect what the model learns? Can re-simulation be combined with other SSL approaches like masked modeling? And can similar foundation models be built for other domains, from astrophysics and neutrino experiments to gravitational wave detection?

> **Bottom Line:** RS3L turns a high-energy physics simulator into a data augmentation engine, enabling contrastive pre-training that produces foundation models competitive with supervised learning, while being inherently robust to the systematic uncertainties that plague real experimental data.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects state-of-the-art self-supervised learning from computer vision and NLP with the domain-specific structure of high-energy physics simulations, using physics knowledge to guide representation learning directly.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">RS3L introduces a new data augmentation paradigm for contrastive learning, using stochastic simulator re-runs rather than hand-crafted transformations, that could generalize to any scientific domain with high-fidelity simulators.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Pre-trained RS3L models show strong jet-tagging performance across multiple physics benchmarks, with built-in robustness to simulation-to-reality systematic uncertainties that are a central challenge in LHC physics analysis.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work includes extending re-simulation strategies to other physics domains and combining them with masked modeling approaches; the RS3L dataset is publicly released at https://doi.org/10.5281/zenodo.10633815.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Re-Simulation-based Self-Supervised Learning for Pre-Training Foundation Models</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[arXiv:2403.07066](https://arxiv.org/abs/2403.07066)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Philip Harris", "Michael Kagan", "Jeffrey Krupa", "Benedikt Maier", "Nathaniel Woodward"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Self-Supervised Learning (SSL) is at the core of training modern large machine learning models, providing a scheme for learning powerful representations that can be used in a variety of downstream tasks. However, SSL strategies must be adapted to the type of training data and downstream tasks required. We propose RS3L ("Re-simulation-based self-supervised representation learning"), a novel simulation-based SSL strategy that employs a method of re-simulation to drive data augmentation for contrastive learning in the physical sciences, particularly, in fields that rely on stochastic simulators. By intervening in the middle of the simulation process and re-running simulation components downstream of the intervention, we generate multiple realizations of an event, thus producing a set of augmentations covering all physics-driven variations available in the simulator. Using experiments from high-energy physics, we explore how this strategy may enable the development of a foundation model; we show how RS3L pre-training enables powerful performance in downstream tasks such as discrimination of a variety of objects and uncertainty mitigation. In addition to our results, we make the RS3L dataset publicly available for further studies on how to improve SSL strategies.</span></div></div>
</div>
