---
abstract: For the first time, we develop a simulation-based model for the Minkowski
  functionals (MFs) of large-scale structure, which allows us to extract the full
  information available from the MFs (including both the Gaussian and non-Gaussian
  part), and apply it to the BOSS DR12 CMASS galaxy sample. Our model is based on
  high-fidelity mock galaxy catalogs constructed from the \textsc{Abacus}\textsc{Summit}
  simulations using the halo occupation distribution (HOD) framework, which include
  the redshift-space distortions and Alcock-Paczynski distortions, incorporate survey
  realism, including survey geometry and veto masks, and account for angular plus
  radial selection effects. The cosmological and HOD parameter dependence of the MFs
  is captured with a neural network emulator trained from the galaxy mocks with various
  cosmological and HOD parameters. To benchmark the constraining power of the MFs,
  we also train an emulator for the galaxy 2-point correlation function (2PCF) using
  the same pipeline. Having validated our approach through successful parameter recovery
  tests on both internal and external mocks, including non-HOD forward models of the
  halo-galaxy connection, we apply our forward model to analyze the CMASS data in
  the redshift range $0.45<z<0.58$. We find the MFs provide stronger constraints on
  the cosmological parameters than the 2PCF. The combination of the two gives $ω_{\rm
  cdm}=0.1172^{+0.0020}_{-0.0023}$, $σ_8=0.783\pm 0.026$, and $n_s=0.966^{+0.019}_{-0.015}$,
  which are tighter by a factor of 2.0, 1.9, and 1.6 than the 2PCF alone. The derived
  constraint $fσ_8=0.453 \pm 0.016$ is also improved by a factor of 1.9, compared
  to the 2PCF, and agrees well with Planck 2018 predictions and other results from
  a series of studies in the literature.
arxivId: '2501.01698'
arxivUrl: https://arxiv.org/abs/2501.01698
authors:
- Wei Liu
- Enrique Paillas
- Carolina Cuesta-Lazaro
- Georgios Valogiannis
- Wenjuan Fang
concepts:
- minkowski functionals
- simulation-based inference
- emulation
- non-gaussian statistics
- surrogate modeling
- bayesian inference
- posterior estimation
- cosmological simulation
- halo occupation distribution
- monte carlo methods
- likelihood estimation
- dark matter
- dark energy
figures:
- /iaifi-research-blog/figures/2501_01698/figure_1.png
- /iaifi-research-blog/figures/2501_01698/figure_1.png
- /iaifi-research-blog/figures/2501_01698/figure_2.png
- /iaifi-research-blog/figures/2501_01698/figure_2.png
- /iaifi-research-blog/figures/2501_01698/figure_3.png
- /iaifi-research-blog/figures/2501_01698/figure_3.png
pdfUrl: https://arxiv.org/pdf/2501.01698v2
published: '2025-01-03T08:36:27+00:00'
theme: Astrophysics
title: Cosmological constraints from the Minkowski functionals of the BOSS CMASS galaxy
  sample
wordCount: 1077
---

## The Big Picture

Imagine trying to describe a sponge by measuring only the average size of its holes. You'd miss the most interesting parts: how its tunnels twist and connect, whether its voids are isolated bubbles or a labyrinthine network. Scale that sponge to the size of the observable universe, and you have the cosmic web — the vast filamentary structure of galaxies and dark matter that cosmologists are trying to decode.

For decades, the standard tool for mapping this structure has been the **two-point correlation function (2PCF)** — a measure of how often galaxy pairs appear at different separations. It's powerful, but incomplete. It captures regular clustering patterns while missing the complex, irregular shapes gravity has sculpted over billions of years. Those shapes encode secrets about dark matter, dark energy, and the primordial density fluctuations that seeded everything we see.

A new study from Wei Liu and collaborators unlocks that hidden information. They've built the first complete, simulation-based model for **Minkowski functionals** — mathematical tools from topology that measure the full shape and connectivity of cosmic structure — and applied it to real galaxy data from the BOSS survey. The result: constraints on key cosmological parameters up to *twice as tight* as the standard approach.

> **Key Insight:** By measuring not just how galaxies cluster but *how the cosmic web is shaped* — its volume, surface area, curvature, and connectivity — Minkowski functionals extract non-Gaussian information that two-point statistics simply cannot reach.

## How It Works

The four **Minkowski functionals** measure distinct geometric properties of the galaxy density field — a map of where matter concentrates and where it thins out. They capture: (1) the volume of overdense regions above a density threshold, (2) the surface area bounding those regions, (3) the integrated mean curvature of that surface, and (4) the **Euler characteristic** — a single number encoding overall connectivity, distinguishing isolated blobs from tunnels from enclosed voids. Sweeping across density thresholds traces how the cosmic web's topology shifts from dense filaments to empty voids.

![Figure 1](/iaifi-research-blog/figures/2501_01698/figure_1.png)

Earlier MF analyses smoothed heavily, deliberately washing out irregular features to avoid modeling them. This team took a different route: full simulation-based inference, built in four steps:

1. **Simulate:** Thousands of mock galaxy catalogs from **AbacusSummit** N-body simulations — tracking billions of gravitating particles across cosmic time — spanning a grid of cosmological parameters.
2. **Populate:** The **halo occupation distribution (HOD)** framework places galaxies inside dark matter halos, with varying HOD parameters to account for uncertainty in galaxy formation.
3. **Realism:** Full observational effects are injected — redshift-space distortions, survey geometry and veto masks, angular and radial selection effects, and the Alcock-Paczynski distortion (a geometric smearing that arises when you assume the wrong cosmology to convert observed positions into a 3D map).
4. **Emulate:** A neural network trained on all these mocks predicts MFs (and separately, the 2PCF) for any combination of cosmological and HOD parameters — fast enough to drive Markov chain Monte Carlo inference across millions of parameter combinations.

![Figure 2](/iaifi-research-blog/figures/2501_01698/figure_1.png)

The emulator covers six cosmological parameters plus six HOD parameters simultaneously. Before touching real data, the team ran extensive validation, feeding mock catalogs through the pipeline and checking whether inferred parameters matched the known truth. Crucially, they tested on mocks from a completely different galaxy formation model — the **Uchuu simulation** with an independent HOD prescription — to probe model dependence. The pipeline passed.

## Why It Matters

Applied to the BOSS DR12 CMASS sample — roughly 600,000 galaxies at redshifts 0.45–0.58 — the team measured MFs and 2PCF from the same data, fitting them separately and jointly. The MFs alone outperformed the 2PCF alone on every key parameter. Their joint analysis delivered:

- **ω_cdm** (cold dark matter density): 2.0× tighter than 2PCF alone
- **σ_8 = 0.783 ± 0.026** (amplitude of matter fluctuations): 1.9× tighter
- **n_s = 0.966** (spectral index of primordial fluctuations): 1.6× tighter
- **fσ_8 = 0.453 ± 0.016** (growth rate of cosmic structure): 1.9× tighter

![Figure 3](/iaifi-research-blog/figures/2501_01698/figure_2.png)

These results agree well with Planck 2018 predictions and with other analyses of the same dataset. That consistency matters as much as the precision — it means the non-Gaussian information is being extracted cleanly, not corrupted by modeling assumptions.

![Figure 4](/iaifi-research-blog/figures/2501_01698/figure_2.png)

We are entering an era of galaxy surveys — DESI, Euclid, the Roman Space Telescope — so vast and precise that squeezing every bit of statistical power from the data becomes essential. The two-point function leaves a significant fraction of that power untouched. Minkowski functionals are one of the most promising ways to recover it.

What distinguishes this work is the methodology as much as the result. Previous MF analyses either operated where non-Gaussian effects were negligible or applied approximate analytical corrections. This team built a full forward model — no approximations, no linearization, everything from the simulation up. That pipeline is directly transferable to current DESI data and future surveys, where galaxy samples will be orders of magnitude larger.

Open questions remain. The HOD model, while tested against alternative prescriptions, is still an idealized description of galaxy formation. How robustly MF constraints survive more exotic halo-galaxy connection models — including **assembly bias** (where galaxy properties depend on when and how their dark matter halo formed), velocity bias, and environmental effects — is the next frontier. The team showed encouraging results, but stress-testing against hydrodynamical simulations will be essential as precision demands grow.

> **Bottom Line:** By building the first simulation-based model capturing the full topology of the cosmic web — including its non-Gaussian structure — this team doubled the constraining power on key cosmological parameters, charting a clear path for next-generation surveys to extract far more from large-scale structure.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses computational topology, neural network emulation, and Bayesian inference into a single pipeline — a textbook example of AI methods enabling fundamentally new physics measurements.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">A neural network emulator accurately predicts high-dimensional summary statistics across a 12-parameter space, demonstrating how simulation-based inference with learned emulators can replace intractable analytical likelihoods in complex physical systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By extracting non-Gaussian cosmological information through Minkowski functionals applied to real galaxy data, the work delivers up to 2× tighter constraints on dark matter density and the growth rate of cosmic structure.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The pipeline is directly applicable to ongoing DESI observations and upcoming Euclid and Roman data; the full methodology is detailed in arXiv:2501.01496.</span></div></div>
</div>
