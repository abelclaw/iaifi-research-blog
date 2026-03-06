---
abstract: 'Machine-learned normalizing flows can be used in the context of lattice
  quantum field theory to generate statistically correlated ensembles of lattice gauge
  fields at different action parameters. This work demonstrates how these correlations
  can be exploited for variance reduction in the computation of observables. Three
  different proof-of-concept applications are demonstrated using a novel residual
  flow architecture: continuum limits of gauge theories, the mass dependence of QCD
  observables, and hadronic matrix elements based on the Feynman-Hellmann approach.
  In all three cases, it is shown that statistical uncertainties are significantly
  reduced when machine-learned flows are incorporated as compared with the same calculations
  performed with uncorrelated ensembles or direct reweighting.'
arxivId: '2401.10874'
arxivUrl: https://arxiv.org/abs/2401.10874
authors:
- Ryan Abbott
- Aleksandar Botev
- Denis Boyda
- Daniel C. Hackett
- Gurtej Kanwar
- Sébastien Racanière
- Danilo J. Rezende
- Fernando Romero-López
- Phiala E. Shanahan
- Julian M. Urban
concepts:
- normalizing flows
- lattice qcd
- correlated ensembles
- lattice gauge theory
- generative models
- uncertainty quantification
- residual flow architecture
- feynman-hellmann method
- monte carlo methods
- equivariant neural networks
- symmetry preservation
- density estimation
- renormalization
figures:
- /iaifi-research-blog/figures/2401_10874/figure_1.png
- /iaifi-research-blog/figures/2401_10874/figure_2.png
- /iaifi-research-blog/figures/2401_10874/figure_3.png
pdfUrl: https://arxiv.org/pdf/2401.10874v2
published: '2024-01-19T18:33:52+00:00'
theme: Theoretical Physics
title: Applications of flow models to the generation of correlated lattice QCD ensembles
wordCount: 1001
---

## The Big Picture

Imagine measuring how a rubber band stretches under different tensions. The smart approach isn't to cut a hundred rubber bands — it's to take the *same* rubber band and pull it to different lengths. Correlations between measurements on the same object let you subtract out noise that would otherwise swamp your signal. Physicists doing lattice QCD calculations face exactly this problem, just with quarks and gluons instead of rubber bands.

Lattice QCD is the gold-standard numerical tool for computing properties of protons, neutrons, and other particles governed by the strong nuclear force. It works by placing space-time on a grid and simulating how quarks and gluons interact at each point. Extracting physically meaningful results often requires comparing calculations at slightly different settings — different grid resolutions, quark masses, or interaction strengths — and those differences can be buried under statistical noise. Running fresh, independent simulations for every setting is brutally expensive.

A collaboration from MIT, Fermilab, Google DeepMind, and the University of Bern has now demonstrated that machine-learned **normalizing flows** — AI models that learn to convert one set of simulations into another — can solve this problem. They manufacture *correlated* ensembles: pairs of simulation sets where random fluctuations are shared rather than independent, so much of the noise cancels when you compare them. The result is dramatically sharper estimates from the same computational budget.

> **Key Insight:** By using AI to transform one set of lattice configurations into another at different physical parameters, researchers create statistically correlated ensembles where much of the noise cancels out, yielding significantly more precise results from the same computational budget.

## How It Works

A normalizing flow is a learned mapping between two probability distributions. Think of it as a coordinate transformation: configurations sampled from one physical setup (a coarse lattice) are pushed through a neural network that reshapes them into configurations statistically consistent with a different setup (a finer lattice). The transformation is invertible and tracks exactly how probabilities change — ensuring the output faithfully represents the target distribution.

![Figure 1](/iaifi-research-blog/figures/2401_10874/figure_1.png)

The team introduces a **residual flow architecture** — a design where each network layer adds a small, structured correction to a configuration rather than transforming it wholesale. When the two distributions being connected are nearby in parameter space, those corrections are naturally small and easy to learn, making this architecture well-matched to the task.

The logic runs as follows:

1. **Generate a base ensemble** at simulation setting α₀ using standard Monte Carlo methods.
2. **Train a flow** to map those configurations to samples consistent with a nearby setting α₁.
3. **Apply the flow** to produce a second ensemble statistically *correlated* with the first — the same underlying configurations, transformed.
4. **Compute observables** at both settings. Shared fluctuations cancel when you take differences, dramatically reducing variance.

The variance reduction follows the rubber band logic directly: noise affecting both ensembles cancels when you subtract one from the other. The closer the two distributions, the stronger the correlation.

The researchers validate this approach across three concrete applications. For **continuum limits**, extrapolating results to zero lattice spacing requires comparing calculations at multiple grid resolutions; flows between coarse and fine ensembles significantly reduce uncertainties in gradient flow scales. For **mass dependence**, the approach outperforms both independent ensembles and naive reweighting when tracing how QCD observables shift with quark mass. For **hadronic matrix elements via Feynman-Hellmann** — which computes quantities like the gluon momentum fraction of the pion by differentiating the action with respect to an external field — flows excel precisely because the technique requires comparing ensembles at slightly different coupling values.

![Figure 2](/iaifi-research-blog/figures/2401_10874/figure_2.png)

In all three cases, flows outperform simple **reweighting**, the naive alternative of rescaling the importance of existing configurations. The improvement is sharpest when parameter shifts are small enough that distributions overlap substantially, but large enough that direct reweighting becomes inefficient.

![Figure 3](/iaifi-research-blog/figures/2401_10874/figure_3.png)

## Why It Matters

Much of the excitement around machine learning for lattice QCD has focused on *replacing* expensive Monte Carlo sampling entirely — a goal that remains technically challenging at physically relevant scales. This work carves out a different niche: augmenting existing calculations rather than replacing them. Flow models for variance reduction are easier to train than those required for full configuration generation, because they only need to bridge nearby distributions rather than learn an entire complex probability landscape.

This opens a more near-term path to computational gains. Standard lattice QCD workflows routinely compare results across multiple lattice spacings, quark masses, and external field strengths. Wherever such comparisons appear, correlated flows could reduce statistical uncertainties — potentially bringing calculations that currently require enormous computer clusters within reach of more modest resources.

The Feynman-Hellmann application is particularly significant. Many physically important quantities — nucleon sigma terms, isospin breaking corrections, derivatives with respect to the electromagnetic coupling — can be formulated as derivatives of the action with respect to some parameter. The correlated ensemble approach offers a unified strategy for all of them.

> **Bottom Line:** Machine-learned flows act as statistical bridges between nearby lattice QCD ensembles, creating correlations that cancel noise and sharpen the precision of derivative-based observables — a practical, near-term path to squeezing more physics out of expensive simulations.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly marries modern deep generative modeling — normalizing flows and residual architectures — with one of the most computationally demanding fields in theoretical physics, demonstrating concrete speedups in real QCD calculations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The residual flow architecture and correlated-ensemble training strategy are transferable innovations applicable to any domain requiring variance reduction across related probability distributions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By reducing the statistical cost of continuum extrapolations, quark mass dependencies, and Feynman-Hellmann matrix element calculations, this method directly accelerates precision QCD predictions relevant to particle and nuclear physics experiments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include applying correlated flows to theories with a sign problem — such as finite-density QCD — where standard reweighting catastrophically fails; the full paper is available at arXiv:2404.10025.</span></div></div>
</div>
