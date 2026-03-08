---
abstract: We explore full-shape analysis with simulation-based priors, which is the
  simplest approach to galaxy clustering data analysis that combines effective field
  theory (EFT) on large scales and numerical simulations on small scales. The core
  ingredient of our approach is the prior density of EFT parameters which we extract
  from a suite of 10500 galaxy simulations based on the halo occupation distribution
  (HOD) model. We measure the EFT parameters with the field-level forward model, which
  enables us to cancel cosmic variance. On the theory side, we develop a new efficient
  approach to calculate field-level transfer functions using time-sliced perturbation
  theory and the logarithmic fast Fourier transform. We find that the cosmology dependence
  of EFT parameters of galaxies is approximately degenerate with the HOD parameters,
  and hence it can be ignored for the purpose of prior generation. We use neural density
  estimation to model the measured distribution of EFT parameters. Our distribution
  model is then used as a prior in a reanalysis of the BOSS full-shape galaxy power
  spectrum data. Assuming the $Λ$CDM model, we find significant ($\approx 30\%$ and
  $\approx 60\%$) improvements for the matter density fraction and the mass fluctuation
  amplitude, which are constrained to $Ω_{m}= 0.315 \pm 0.010$ and $σ_8 = 0.671 \pm
  0.027$. The value of the Hubble constant does not change, $H_0= 68.7\pm 1.1$~km/s/Mpc.
  This reaffirms earlier reports of the structure growth tension from the BOSS data.
  Finally, we use the measured EFT parameters to constrain the galaxy-dark matter
  connection.
arxivId: '2409.10609'
arxivUrl: https://arxiv.org/abs/2409.10609
authors:
- Mikhail M. Ivanov
- Andrej Obuljen
- Carolina Cuesta-Lazaro
- Michael W. Toomey
concepts:
- simulation-based inference
- effective field theory
- cosmological simulation
- density estimation
- bayesian inference
- galaxy power spectrum
- posterior estimation
- structure growth tension
- dark matter
- dark energy
- monte carlo methods
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2409_10609/figure_1.png
- /iaifi-research-blog/figures/2409_10609/figure_1.png
- /iaifi-research-blog/figures/2409_10609/figure_2.png
- /iaifi-research-blog/figures/2409_10609/figure_2.png
- /iaifi-research-blog/figures/2409_10609/figure_3.png
- /iaifi-research-blog/figures/2409_10609/figure_3.png
pdfUrl: https://arxiv.org/pdf/2409.10609v2
published: '2024-09-16T18:00:03+00:00'
theme: Astrophysics
title: 'Full-shape analysis with simulation-based priors: cosmological parameters
  and the structure growth anomaly'
wordCount: 1057
---

## The Big Picture

Imagine trying to describe the foam on a cappuccino. Fluid dynamics equations work beautifully for the large swirls but break down when you zoom into the tiny bubbles. To get the full picture, you need to switch frameworks. Cosmologists face exactly this problem when mapping the large-scale structure of the universe.

Galaxies aren't distributed randomly. They cluster into a vast cosmic web of filaments, walls, and voids, a structure shaped by gravity acting on dark matter over billions of years. Measuring this clustering pattern (the galaxy power spectrum) is one of our sharpest tools for probing the universe's fundamental properties.

But the math works well only on large scales. It breaks down precisely where the most information lives: the small, dense, tangled regions where galaxies actually form.

A team of MIT and Harvard physicists has found a cleaner path through this problem, one that delivers far more precise measurements of how quickly structure has grown across cosmic time and sharpens a nagging tension between different ways of measuring the universe.

> **Key Insight:** By training a neural network on 10,500 galaxy simulations and using the result as an informed prior, the researchers extracted 30–60% better measurements of key cosmological parameters from existing data. No new telescope required.

## How It Works

The standard theoretical tool for galaxy clustering is the **effective field theory of large-scale structure (EFT)**, a framework describing how matter clumps on scales larger than roughly thirty million light-years. EFT is elegant and flexible, but it comes with a cost: many free **nuisance parameters** that account for small-scale physics we can't directly model. Constraining these separately is expensive, and marginalizing over them blurs the cosmological signal.

But these parameters aren't truly free. Galaxies form inside **dark matter halos** (invisible concentrations of dark matter that act as gravitational cradles for galaxy formation) following physical rules that tightly correlate the EFT parameters with each other. The researchers exploited this by building a **simulation-based prior**: a probability map over EFT parameter space, learned from simulations rather than assumed by hand.

Here's the pipeline:

1. **Run 10,500 galaxy simulations** using the **halo occupation distribution (HOD)** model, which assigns galaxies to dark matter halos based on probabilistic rules. Each simulation samples a different galaxy formation parameter combination.
2. **Measure the EFT parameters** from each simulation using a **field-level forward model**, a technique that matches simulated galaxy fields against theoretical predictions point-by-point, canceling cosmic variance (the statistical noise from having only one observable universe) in the process.
3. **Train a neural density estimator** on the resulting parameter cloud. The neural network learns the shape of the physically realistic region of parameter space.
4. **Use that learned distribution as a prior** when analyzing real data from BOSS (the Baryon Oscillation Spectroscopic Survey).

![Figure 1](/iaifi-research-blog/figures/2409_10609/figure_1.png)

On the theory side, the team developed an efficient method to compute field-level transfer functions using **time-sliced perturbation theory** combined with the **logarithmic fast Fourier transform**, making forward-model calculations fast enough to run across thousands of simulations.

Something important turned up during the simulation phase: the EFT parameters' dependence on cosmology is largely degenerate with the HOD parameters. In plain terms, adjusting the galaxy formation recipe can mimic the effect of changing the cosmology. This meant the team could generate their priors at a single fixed cosmology without introducing significant bias, a major practical simplification.

![Figure 3](/iaifi-research-blog/figures/2409_10609/figure_2.png)

The neural density estimator captures the complex, irregular shape of the realistic EFT parameter region, something a simple bell-curve assumption would miss entirely. When this learned prior is applied to BOSS power spectrum data, the results sharpen considerably.

## Why It Matters

The improvements are large. Compared to a standard EFT analysis with flat priors, the simulation-informed approach tightens the matter density parameter **Ω_m = 0.315 ± 0.010** (the fraction of the universe's total energy made up of matter) by ~30%. It sharpens the **mass fluctuation amplitude σ_8 = 0.671 ± 0.027**, which measures how clumpy matter has grown today, by ~60%. The Hubble constant holds steady at H_0 = 68.7 ± 1.1 km/s/Mpc.

That σ_8 value matters. The Planck satellite, measuring the **cosmic microwave background** (the faint afterglow of light from the universe's first 380,000 years) predicts σ_8 ≈ 0.811 today under **ΛCDM**, the standard cosmological model. The BOSS measurement here comes in at 0.671: nearly five standard deviations lower.

This discrepancy is the **structure growth tension**: the universe appears to have grown less clumpy than ΛCDM predicts. The tension isn't new, but this analysis sharpens it considerably, making it harder to dismiss as statistical noise or poorly constrained nuisance parameters.

![Figure 5](/iaifi-research-blog/figures/2409_10609/figure_3.png)

There's a broader point here too. The gap between simulation-based inference and analytic EFT methods is closing. Rather than choosing between EFT's physical interpretability and simulations' small-scale power, researchers can now combine the two.

The approach is deliberately modest (HOD simulations rather than expensive hydrodynamics) yet already delivers large gains. Future surveys like DESI, Euclid, and the Roman Space Telescope will generate data orders of magnitude richer than BOSS. Methods like this will be essential to turn that flood of photons into precision cosmology. If the structure growth tension survives, it may eventually point toward physics beyond ΛCDM: modified gravity, new dark energy properties, or new light particles suppressing structure formation.

> **Bottom Line:** By teaching a neural network the physical rules of galaxy formation and using that knowledge to constrain theory parameters, this team squeezed 60% more information out of existing BOSS data and made the structure growth anomaly harder than ever to explain away.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines simulation-based machine learning with analytic field theory, using neural density estimation trained on galaxy simulations to inform a rigorous EFT cosmological analysis, a direct example of AI-physics integration.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Neural density estimators trained on simulation suites to model high-dimensional, non-Gaussian parameter distributions offer a template for learned priors in scientific inference problems well beyond cosmology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The analysis sharpens the structure growth tension to a level increasingly difficult to reconcile with standard ΛCDM, potentially pointing toward new physics in dark matter, dark energy, or gravity.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Natural next steps include applying simulation-based priors to DESI and Euclid datasets, where the gains in constraining power will be even more critical. The paper is available as [arXiv:2409.10609](https://arxiv.org/abs/2409.10609).</span></div></div>
</div>
