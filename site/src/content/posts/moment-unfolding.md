---
abstract: Deconvolving ("unfolding'') detector distortions is a critical step in the
  comparison of cross section measurements with theoretical predictions in particle
  and nuclear physics. However, most existing approaches require histogram binning
  while many theoretical predictions are at the level of statistical moments. We develop
  a new approach to directly unfold distribution moments as a function of another
  observable without having to first discretize the data. Our Moment Unfolding technique
  uses machine learning and is inspired by Generative Adversarial Networks (GANs).
  We demonstrate the performance of this approach using jet substructure measurements
  in collider physics. With this illustrative example, we find that our Moment Unfolding
  protocol is more precise than bin-based approaches and is as or more precise than
  completely unbinned methods.
arxivId: '2407.11284'
arxivUrl: https://arxiv.org/abs/2407.11284
authors:
- Krish Desai
- Benjamin Nachman
- Jesse Thaler
concepts:
- unfolding
- boltzmann reweighting
- moment estimation
- inverse problems
- generative adversarial networks
- jet physics
- collider physics
- simulation-based inference
- likelihood ratio
- monte carlo methods
- detector simulation
- loss function design
figures:
- /iaifi-research-blog/figures/2407_11284/figure_1.png
- /iaifi-research-blog/figures/2407_11284/figure_1.png
- /iaifi-research-blog/figures/2407_11284/figure_2.png
- /iaifi-research-blog/figures/2407_11284/figure_2.png
- /iaifi-research-blog/figures/2407_11284/figure_3.png
- /iaifi-research-blog/figures/2407_11284/figure_3.png
pdfUrl: https://arxiv.org/pdf/2407.11284v2
published: '2024-07-15T23:45:23+00:00'
theme: Experimental Physics
title: Moment Unfolding
wordCount: 1110
---

## The Big Picture

Imagine you're trying to measure the true height of a mountain, but your ruler keeps warping in the cold. Every measurement is distorted — and the distortion isn't uniform. To get at the real height, you need to *undo* what your faulty instrument did. Now scale that problem up to the Large Hadron Collider, where particles smash together millions of times per second and every detector is, in some sense, a warped ruler. The process of correcting for these distortions is called **unfolding**, and it sits at the heart of comparing experimental data to theoretical predictions in particle physics.

Theorists often express their most precise predictions not as full probability distributions, but as **statistical moments** — the mean, variance, skewness, and higher-order summaries of a distribution. Moments are compressed fingerprints: a few numbers that capture a distribution's overall shape without spelling out every detail. For certain measurements in **quantum chromodynamics (QCD)** — the theory of how quarks and gluons interact via the strong nuclear force — moments are more computable from first principles than the full distribution. But experimentalists have been stuck unfolding entire histograms first, then extracting moments afterward: a two-step process that introduces unnecessary noise and systematic bias.

A new paper from researchers at MIT, Lawrence Berkeley National Laboratory, and UC Berkeley proposes a smarter path: skip the histogram entirely and unfold directly to the moments you actually want.

> **Key Insight:** Moment Unfolding uses machine learning to extract corrected statistical moments from particle physics data without ever binning the data into histograms, eliminating a major source of discretization bias and improving measurement precision.

## How It Works

The core idea borrows from an unexpected corner of physics: **Boltzmann weight factors** from statistical mechanics. In thermodynamics, a Boltzmann weight encodes how likely a system is to occupy a particular state as an exponential function of energy. The Moment Unfolding team realized that a reweighting function of exactly this form — an exponential of a polynomial in the observable — has a beautiful property: its parameters *are* the cumulants (related to moments) of the distribution. You don't need to fit the shape of the distribution; you just fit the exponent, and the moments fall out directly.

The procedure works in four steps:

1. **Start with simulation.** A Monte Carlo simulation — a program that uses randomness to model complex physical processes — captures both the true underlying physics and the detector's response, serving as the bridge between theory and experiment.
2. **Learn a reweighting function.** A neural network learns to reweight simulated **particle-level** events — what the physics actually produced, before the detector — using a Boltzmann-inspired functional form. The network's learned parameters directly correspond to the moments of the unfolded distribution.
3. **Adversarial optimization.** A second network acts as a **discriminator**, trained to distinguish the **detector-level** simulation (what the detector actually records) from real experimental data. Borrowing from **Generative Adversarial Networks (GANs)** — where two networks compete, one generating realistic outputs and the other catching fakes — the reweighter tries to fool the discriminator, and the discriminator tries not to be fooled.
4. **Read off the moments.** When training converges, the parameters of the reweighting function are the unfolded moments. No histogram required.

![Figure 1](/iaifi-research-blog/figures/2407_11284/figure_1.png)

This GAN-like architecture has a decisive advantage over existing methods. Unlike OmniFold — a popular unbinned unfolding approach that iterates back and forth between particle level and detector level — Moment Unfolding solves the problem in a single pass. No iteration means less computation and greater stability.

![Figure 2](/iaifi-research-blog/figures/2407_11284/figure_1.png)

The team validated their method on **jet substructure** observables — properties of the collimated sprays of particles produced when quarks and gluons scatter at high energy. Specifically, they studied moments of the **jet groomed momentum fraction** ($z_g$), a measure of how unevenly a jet's energy splits between its two main branches after stripping away soft, wide-angle radiation, as a function of jet transverse momentum $p_T$. This is exactly where moments carry precise theoretical predictions from **DGLAP evolution equations** — mathematical rules describing how quark and gluon distributions shift with collision energy — but full spectral unfolding is overkill.

![Figure 4](/iaifi-research-blog/figures/2407_11284/figure_2.png)

The results are striking. Moment Unfolding achieves lower statistical uncertainty than traditional bin-based approaches like **Iterative Bayesian Unfolding (IBU)**, and matches or beats fully unbinned methods like OmniFold — while targeting only the moments you care about.

## Why It Matters

The precision of fundamental physics measurements hinges on cleanly separating what the detector did from what nature actually produced. Binning has been a workhorse of experimental physics for decades, but it's a blunt instrument. The bias from placing data into discrete bins and representing each by its center rather than its true mean never fully vanishes without infinitely narrow bins. In practice, you never have enough data for that. Moment Unfolding sidesteps this entire class of systematic error.

The broader implications extend well beyond QCD. Some of the most precise extractions of the strong coupling constant $\alpha_s$ — which sets the overall strength of the strong nuclear force — come from comparing measured jet shape moments to theoretical predictions. Any improvement in extracting those moments translates directly into sharper tests of the Standard Model, and potentially into greater sensitivity to new physics hiding in subtle deviations. The technique generalizes naturally to deep-inelastic scattering, heavy-ion collisions, and anywhere moments matter more than full spectra.

![Figure 5](/iaifi-research-blog/figures/2407_11284/figure_3.png)

Open questions remain. The current implementation targets moments of a single observable at a time. Extending Moment Unfolding to handle multiple correlated observables simultaneously — or to recover full distributions rather than just their summaries — is a natural next step the authors flag for future work.

> **Bottom Line:** By marrying Boltzmann weight factors with adversarial machine learning, Moment Unfolding delivers more precise extractions of statistical moments from collider data than any previous approach — no histogram required, no iterative algorithm needed.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects the mathematical structure of statistical mechanics (Boltzmann distributions) with adversarial machine learning to solve a core challenge in experimental particle physics, exemplifying the cross-disciplinary approach at IAIFI's core.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces a constrained GAN architecture where the generator's functional form is physically motivated, giving learned parameters direct interpretive meaning as statistical moments — a step toward more physically transparent ML.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Moment Unfolding enables more precise extractions of QCD observables like jet substructure moments, directly improving measurements that test quantum chromodynamics and constrain the strong coupling constant.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions could target multi-observable moment unfolding and full distribution recovery; the full paper and code are available at arXiv:2307.01686.</span></div></div>
</div>
