---
abstract: The intrinsic alignments (IA) of galaxies, a key contaminant in weak lensing
  analyses, arise from correlations in galaxy shapes driven by tidal interactions
  and galaxy formation processes. Accurate IA modeling is essential for robust cosmological
  inference, but current approaches rely on perturbative methods that break down on
  nonlinear scales or on expensive simulations. We introduce IAEmu, a neural network-based
  emulator that predicts the galaxy position-position ($ξ$), position-orientation
  ($ω$), and orientation-orientation ($η$) correlation functions and their uncertainties
  using mock catalogs based on the halo occupation distribution (HOD) framework. Compared
  to simulations, IAEmu achieves ~3% average error for $ξ$ and ~5% for $ω$, while
  capturing the stochasticity of $η$ without overfitting. The emulator provides both
  aleatoric and epistemic uncertainties, helping identify regions where predictions
  may be less reliable. We also demonstrate generalization to non-HOD alignment signals
  by fitting to IllustrisTNG hydrodynamical simulation data. As a fully differentiable
  neural network, IAEmu enables $\sim$10,000$\times$ speed-ups in mapping HOD parameters
  to correlation functions on GPUs, compared to CPU-based simulations. This acceleration
  facilitates inverse modeling via gradient-based sampling, making IAEmu a powerful
  surrogate model for galaxy bias and IA studies with direct applications to Stage
  IV weak lensing surveys.
arxivId: '2504.05235'
arxivUrl: https://arxiv.org/abs/2504.05235
authors:
- Sneh Pandya
- Yuanyuan Yang
- Nicholas Van Alfen
- Jonathan Blazek
- Robin Walters
concepts:
- surrogate modeling
- emulation
- galaxy intrinsic alignment
- uncertainty quantification
- halo occupation distribution
- cosmological simulation
- inverse problems
- bayesian inference
- regression
- out-of-distribution detection
- dark matter
- transfer learning
figures:
- /iaifi-research-blog/figures/2504_05235/figure_1.png
- /iaifi-research-blog/figures/2504_05235/figure_1.png
- /iaifi-research-blog/figures/2504_05235/figure_2.png
pdfUrl: https://arxiv.org/pdf/2504.05235v4
published: '2025-04-07T16:19:50+00:00'
theme: Astrophysics
title: 'IAEmu: Learning Galaxy Intrinsic Alignment Correlations'
wordCount: 1000
---

## The Big Picture

Imagine trying to measure the shape of a shadow on a wall, but the wall itself is slightly warped. That's the challenge cosmologists face when mapping dark matter using **weak gravitational lensing**. Light from distant galaxies bends as it passes through dark matter concentrations, subtly distorting the shapes of those galaxies as seen from Earth. By measuring those distortions statistically, scientists can reconstruct the invisible scaffolding of the universe.

But there's a catch: galaxies aren't randomly oriented to begin with. Galaxies that form near each other share the same gravitational neighborhood. The gravity of the surrounding cosmic web (the vast network of filaments and voids that structures the universe on the largest scales) can stretch and tilt neighboring galaxies so they point in similar directions, independent of any lensing. This effect, called **intrinsic alignment (IA)**, quietly mimics a lensing signal, corrupting the very measurements scientists are trying to make.

Next-generation telescopes like the Vera C. Rubin Observatory's LSST, the Roman Space Telescope, and Euclid all target better-than-one-percent precision in their dark matter maps. At that accuracy, even small uncorrected IA contamination could lead to wrong conclusions about dark energy or how the universe's large-scale structure has grown over time. Modeling IA accurately is not optional; it's existential for the science.

Current methods either rely on mathematical approximations that break down at small scales, or on full-galaxy simulations that can take months of compute time. Researchers at Northeastern University and the IAIFI built [IAEmu](https://arxiv.org/abs/2504.05235): a neural network emulator that predicts galaxy alignment statistics 10,000 times faster than traditional simulations, with just a few percent error.

> **Key Insight:** IAEmu replaces expensive galaxy simulations with a differentiable neural network that predicts intrinsic alignment correlations in milliseconds, fast enough to support real-time inverse modeling for future cosmic surveys.

## How It Works

The starting point is the **halo occupation distribution (HOD)**, a framework for populating dark matter halos (invisible clumps of dark matter where galaxies tend to form) with galaxies. Rather than simulating every gas particle and star, HOD models describe statistically how many and what kind of galaxies live inside halos of a given mass. Van Alfen et al. (2024) extended this framework to include galaxy shapes and orientations, generating mock catalogs that encode how galaxies cluster and align across a grid of HOD parameters.

From those catalogs, the team measured three correlation functions:

- **ξ (xi)**: position-position, capturing how galaxies cluster in space
- **ω (omega)**: position-orientation, capturing how galaxy orientations correlate with nearby galaxy positions
- **η (eta)**: orientation-orientation, capturing how the shapes of two galaxies point toward or away from each other

![Figure 1](/iaifi-research-blog/figures/2504_05235/figure_1.png)

IAEmu is a neural network trained to map HOD parameters directly to these three correlation functions, bypassing simulation entirely. The architecture outputs two types of uncertainty: aleatoric uncertainty, which captures irreducible noise like the intrinsic randomness of galaxy shapes, and epistemic uncertainty, which reflects the model's confidence based on how well its training data covered a given region of parameter space. Together, these tell users when to trust the emulator and when to be cautious.

Training used thousands of HOD mock catalogs spanning a wide parameter space. IAEmu hits roughly 3% average error on ξ and 5% on ω compared to simulated ground truth. For η, the noisiest of the three and dominated by shape noise, the model avoids overfitting and instead captures mean behavior across many realizations.

![Figure 3](/iaifi-research-blog/figures/2504_05235/figure_2.png)

Because IAEmu is fully differentiable and deployable on GPUs, it can be queried almost instantaneously. The team measured an approximately 10,000× speedup over CPU-based HOD simulations: the difference between waiting days and getting answers in seconds.

## Why It Matters

The speed gain isn't just convenient. It opens up a new mode of scientific inquiry. Traditional approaches to inverse problems, where scientists infer HOD parameters from observed galaxy data, require thousands of expensive forward simulations to explore parameter space.

With IAEmu, gradient-based sampling algorithms like Hamiltonian Monte Carlo can query the emulator directly. HMC navigates parameter space by following mathematical gradients, much like water finding the fastest route downhill, and the differentiable emulator makes this natural. The team shows this explicitly: IAEmu supports efficient parameter recovery via differentiable sampling, cutting the cost of pinning down model parameters by orders of magnitude.


IAEmu also generalizes beyond the HOD sandbox it was trained on. The researchers tested it by fitting IA parameters to data from the IllustrisTNG300 hydrodynamical simulation, a physically richer model that includes gas, star formation, and feedback processes that HOD models don't capture. IAEmu adapted, showing that its learned representations transfer beyond its training distribution.

This is a big deal for real surveys, where the true galaxy formation physics will never perfectly match any single modeling framework. Open questions include extending IAEmu to varying cosmological parameters, incorporating baryonic effects more explicitly, and integrating the emulator into full weak lensing likelihood pipelines for LSST and Euclid.

> **Bottom Line:** IAEmu makes it practical to model galaxy intrinsic alignments at the precision demanded by next-generation cosmic surveys, delivering simulation-quality predictions 10,000 times faster, with built-in uncertainty quantification and gradient-based inference support.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits at the intersection of machine learning and observational cosmology, using neural network emulation to tackle intrinsic alignment contamination, a core obstacle between current telescope capabilities and fundamental discoveries about dark matter and dark energy.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">IAEmu combines aleatoric and epistemic uncertainty estimates in a differentiable architecture that supports gradient-based inverse modeling, an approach applicable to scientific surrogate modeling well beyond astrophysics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By making accurate IA modeling computationally tractable, IAEmu supports more reliable cosmological inference from weak lensing surveys, tightening constraints on theories of gravity, dark energy, and large-scale structure.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">IAEmu is positioned as a core tool for Stage IV surveys including LSST, Roman, and Euclid. Future work will extend the emulator to varying cosmological parameters and full likelihood pipelines. The paper is available at [arXiv:2504.05235](https://arxiv.org/abs/2504.05235).</span></div></div>
</div>
