---
abstract: The mass assembly history (MAH) of dark matter halos plays a crucial role
  in shaping the formation and evolution of galaxies. MAHs are used extensively in
  semi-analytic and empirical models of galaxy formation, yet current analytic methods
  to generate them are inaccurate and unable to capture their relationship with the
  halo internal structure and large-scale environment. This paper introduces FLORAH,
  a machine-learning framework for generating assembly histories of ensembles of dark
  matter halos. We train FLORAH on the assembly histories from the GUREFT and VSMDPL
  N-body simulations and demonstrate its ability to recover key properties such as
  the time evolution of mass and concentration. We obtain similar results for the
  galaxy stellar mass versus halo mass relation and its residuals when we run the
  Santa Cruz semi-analytic model on FLORAH-generated assembly histories and halo formation
  histories extracted from an N-body simulation. We further show that FLORAH also
  reproduces the dependence of clustering on properties other than mass (assembly
  bias), which is not captured by other analytic methods. By combining multiple networks
  trained on a suite of simulations with different redshift ranges and mass resolutions,
  we are able to construct accurate main progenitor branches (MPBs) with a wide dynamic
  mass range from $z=0$ up to an ultra-high redshift $z \approx 20$, currently far
  beyond that of a single N-body simulation. FLORAH is the first step towards a machine
  learning-based framework for planting full merger trees; this will enable the exploration
  of different galaxy formation scenarios with great computational efficiency at unprecedented
  accuracy.
arxivId: '2308.05145'
arxivUrl: https://arxiv.org/abs/2308.05145
authors:
- Tri Nguyen
- Chirag Modi
- L. Y. Aaron Yung
- Rachel S. Somerville
concepts:
- generative models
- dark matter
- normalizing flows
- recurrent networks
- cosmological simulation
- halo assembly bias
- emulation
- merger trees
- surrogate modeling
- density estimation
- semi-analytic models
figures:
- /iaifi-research-blog/figures/2308_05145/figure_1.png
- /iaifi-research-blog/figures/2308_05145/figure_2.png
- /iaifi-research-blog/figures/2308_05145/figure_3.png
pdfUrl: https://arxiv.org/pdf/2308.05145v2
published: '2023-08-09T18:00:00+00:00'
theme: Experimental Physics
title: 'FLORAH: A generative model for halo assembly histories'
wordCount: 1024
---

## The Big Picture

Imagine trying to reconstruct someone's entire life story — their childhood, schooling, relationships, setbacks — just from knowing their age and weight today. That's roughly the challenge cosmologists face when trying to understand how galaxies formed: they can observe a galaxy now, but to understand why it looks the way it does, they need the full history of the dark matter "halo" it grew inside.

Dark matter halos are the invisible scaffolding of the universe — vast, gravitationally bound clumps of dark matter that coalesced over billions of years, merging and growing, each one hosting a galaxy.

The **mass assembly history** — the record of how a halo accumulated its mass over cosmic time — is the Rosetta Stone for galaxy formation. Feed it into a galaxy formation model, and you can predict how many stars a galaxy contains, how fast it's forming new ones, even how it clusters with its neighbors. The problem: computing accurate histories for millions of halos, across the full range of galaxy sizes and all the way back to the early universe, is computationally brutal. The standard shortcuts are fast but wrong. A team from MIT and the Flatiron Institute has now introduced a machine learning framework called **FLORAH** that is both fast *and* right.

> **Key Insight:** FLORAH uses a combination of recurrent neural networks and normalizing flows to generate statistically accurate dark matter halo assembly histories — including subtle environmental effects that all previous analytic methods simply cannot capture.

## How It Works

A halo's past isn't just a single number — it's a time-ordered *sequence* of masses and structural properties, and the space of possible histories for any given halo is enormous. FLORAH tackles this with two interlocking components.

A **recurrent neural network (RNN)** — a type of architecture designed for sequences, similar to what powers language models — learns to represent the "memory" of a halo's assembly. At each timestep, the RNN encodes what happened before and passes that context forward.

A **normalizing flow** — a generative model that transforms a simple probability distribution into a complex, structured one — sits on top of the RNN and samples the full distribution of possible next steps. Together, they generate realistic, stochastic assembly histories one timestep at a time, conditioned on a halo's current mass and concentration.

![Figure 1](/iaifi-research-blog/figures/2308_05145/figure_1.png)

Training data comes from two **N-body simulations** — computer models that track the gravitational interactions of millions of particles to simulate how matter clumps together over cosmic time. **GUREFT** covers ultra-high redshifts (up to z ≈ 20) with high mass resolution; **VSMDPL** provides a broad mass range at lower redshifts. The team trains separate FLORAH networks on each and stitches them together at overlapping redshifts, constructing **main progenitor branches (MPBs)**: the primary lineage of each halo, tracing its most massive ancestor at each moment in time.

The resulting histories span an unprecedented dynamic range — from galaxy-cluster-scale halos to dwarf-galaxy progenitors, from today (z = 0) back to z ≈ 20. Validation is rigorous:

- FLORAH accurately reproduces the median and scatter of mass assembly histories across all halo masses tested
- It recovers the time evolution of **halo concentration** — a measure of how centrally dense a halo is — something no previous analytic method could do
- When plugged into the Santa Cruz semi-analytic model (SAM), a computationally efficient framework for predicting galaxy properties from halo histories without running a full simulation, it produces a galaxy stellar mass–halo mass relation and scatter closely matching what the same SAM produces on raw N-body merger trees

## Why It Matters

The headline result isn't just accuracy — it's **assembly bias**. Halos of the same mass don't all cluster the same way; older, more concentrated halos cluster differently than younger ones of identical mass. This effect has been invisible to the Extended Press-Schechter (EPS) formalism the field has relied on for decades.

EPS trees assume a simple Markov property: the future depends only on present mass, nothing else. FLORAH conditions on both mass *and* concentration, and the results show it reproduces the assembly bias signal where EPS methods produce none.

![Figure 2](/iaifi-research-blog/figures/2308_05145/figure_2.png)

This matters enormously for next-generation galaxy surveys. Instruments like the Roman Space Telescope and Euclid will map hundreds of millions of galaxies. Interpreting their clustering statistics — and disentangling galaxy physics from cosmology — requires accurate models of how halos cluster as a function of their full formation history. FLORAH provides a path toward generating the enormous synthetic catalogs those analyses will need, at a fraction of the cost of a full N-body simulation.

![Figure 3](/iaifi-research-blog/figures/2308_05145/figure_3.png)

FLORAH is explicitly framed as a first step. The current model generates only the *main progenitor branch* — the spine of a merger tree. Full merger trees, which include all the smaller halos that merged in along the way, are the ultimate target. Extending FLORAH to generate full trees would unlock a complete, machine-learning-native alternative to expensive N-body runs for semi-analytic galaxy formation modeling.

> **Bottom Line:** FLORAH generates dark matter halo assembly histories accurate enough to recover galaxy statistics and assembly bias — effects the standard analytic toolkit simply misses — while being fast enough to scale to the demands of next-generation cosmological surveys.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">FLORAH directly bridges deep generative modeling and cosmological simulation, using normalizing flows and recurrent neural networks to emulate the statistical output of computationally expensive N-body simulations at a fraction of the cost.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work demonstrates that combining sequence models (RNNs) with density estimators (normalizing flows) can capture complex, time-dependent conditional distributions in physical systems — an architecture pattern with broad applicability beyond cosmology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By accurately reproducing assembly bias for the first time in an analytic or ML framework, FLORAH enables more precise modeling of the halo-galaxy connection, a key ingredient in interpreting large-scale structure measurements that constrain fundamental cosmological parameters.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions aim to generate full merger trees rather than just main progenitor branches, potentially replacing N-body simulations entirely for semi-analytic galaxy formation studies; the paper is available at arXiv:2408.00082.</span></div></div>
</div>
