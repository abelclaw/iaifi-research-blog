---
abstract: We have performed a systematic study of the statistical behavior of non-Poissonian
  template fitting (NPTF), a method designed to analyze and characterize unresolved
  point sources in general counts datasets. In this paper, we focus on the properties
  and characteristics of the Fermi-LAT gamma-ray data set. In particular, we have
  simulated and analyzed gamma-ray sky maps under varying conditions of exposure,
  angular resolution, pixel size, energy window, event selection, and source brightness.
  We describe how these conditions affect the sensitivity of NPTF to the presence
  of point sources, for inner-galaxy studies of point sources within the Galactic
  Center excess, and for the simplified case of isotropic emission. We do not find
  opportunities for major gains in sensitivity from varying these choices, within
  the range available with current Fermi-LAT data. We provide an analytic estimate
  of the NPTF sensitivity to point sources for the case of isotropic emission and
  perfect angular resolution, and find good agreement with our numerical results for
  that case.
arxivId: '2207.13097'
arxivUrl: https://arxiv.org/abs/2207.13097
authors:
- Luis Gabriel C. Bariuan
- Tracy R. Slatyer
concepts:
- non-poissonian statistics
- signal detection
- likelihood ratio
- source count function
- point spread function
- dark matter
- monte carlo methods
- bayesian inference
- hypothesis testing
- simulation-based inference
- inverse problems
- neutrino detection
figures:
- /iaifi-research-blog/figures/2207_13097/figure_1.png
- /iaifi-research-blog/figures/2207_13097/figure_2.png
- /iaifi-research-blog/figures/2207_13097/figure_3.png
pdfUrl: https://arxiv.org/pdf/2207.13097v2
published: '2022-07-26T18:00:00+00:00'
theme: Astrophysics
title: Characterizing the Expected Behavior of Non-Poissonian Template Fitting
wordCount: 1213
---

## The Big Picture

Picture the center of our galaxy as a crime scene. Something is emitting an unusual glow of high-energy gamma rays, a faint, roughly spherical cloud extending about 5,000 light-years from the Galactic Center. The culprit could be extraordinary: dark matter particles annihilating each other, leaving a trail of gamma-ray photons. Or it could be more mundane, a hidden population of millisecond pulsars, ancient spinning neutron stars too faint to detect individually but collectively bright enough to explain the glow. Astronomers have spent a decade trying to tell these suspects apart.

Even if the glow comes from pulsars, many would be too faint to see one-by-one. Invisible as individuals, but detectable as a crowd, if you had the right statistical tools. This is the problem that **Non-Poissonian Template Fitting (NPTF)** was built to solve.

Traditional methods search for individual bright sources. NPTF takes a different approach: it looks for the statistical fingerprint that a population of faint sources leaves behind, a subtle "clumpiness" in how photons land across the sky. A truly smooth signal, like dark matter annihilation spread through the galactic halo, should look uniform. A population of individual point sources, each too faint to resolve on its own, creates tiny statistical hot spots. NPTF picks up on that difference.

Researchers Luis Gabriel Bariuan and Tracy Slatyer at MIT have now published a thorough systematic study of how well NPTF actually works, and what you can do to make it work better.

> **Key Insight:** NPTF's sensitivity to faint point sources is largely fixed by the fundamental properties of current Fermi-LAT data; no clever choice of analysis settings yields major gains, but the method's limits can now be rigorously characterized and predicted.

## How It Works

When you bin gamma-ray photons into pixels on the sky, a purely smooth emission source produces photon counts that follow a **Poisson distribution**: the expected pattern of random arrivals, where each pixel gets roughly the number of photons its average brightness predicts.

A population of faint, unresolved point sources violates that pattern. The pixel where a source sits gets a few extra photons; neighboring empty pixels get fewer. The resulting distribution has a longer tail than Poisson statistics would predict. NPTF detects this deviation.

Bariuan and Slatyer used the publicly available `NPTFit` and `NPTFit-Sim` codes to simulate thousands of gamma-ray sky maps, systematically varying six analysis parameters:

- **Exposure**: how long Fermi stares at the sky, proportional to photons collected
- **Angular resolution**: how sharply each photon's origin can be localized (the **point spread function**, or PSF)
- **Pixel size**: how finely the sky is divided into spatial bins
- **Energy window**: which range of photon energies to include
- **Event selection**: which subset of detected photons to use, trading off exposure against angular resolution
- **Source brightness**: whether the putative pulsar population consists of many faint sources or fewer bright ones

![Figure 1](/iaifi-research-blog/figures/2207_13097/figure_1.png)

For each configuration, they ran hundreds of simulated sky maps with injected point-source populations, fit them with NPTF, and measured how often the method successfully detected the sources. Their primary metric was the **test statistic (TS)**, a number summarizing how much more likely the data are if point sources are present. Higher TS means stronger evidence.

The analytic intuition is revealing. In the simplest approximation, the expected TS scales roughly as the number of photons per source squared, divided by the total photons per pixel. Brighter individual sources are dramatically easier to detect. Spreading the same total flux across more sources makes detection harder, almost regardless of how you tune the analysis.

![Figure 2](/iaifi-research-blog/figures/2207_13097/figure_2.png)

Full numerical simulations confirmed this picture, with important caveats from the complex, non-uniform Galactic diffuse background in the inner Galaxy.

## Why It Matters

The headline result is a sobering one: **within the range of choices available with current Fermi-LAT data, there are no magic settings that dramatically improve NPTF's sensitivity.** Improving angular resolution costs exposure; gaining exposure worsens the PSF. These tradeoffs largely cancel out. Sensitivity comes down to the fundamental photon statistics of the dataset, a ceiling set by physics, not by analysis choices.

![Figure 3](/iaifi-research-blog/figures/2207_13097/figure_3.png)

This matters because previous studies of the Galactic Center Excess made different analysis choices and reached different conclusions. It has been hard to know whether those disagreements reflected real astrophysics or just methodological differences. Bariuan and Slatyer's systematic mapping of the sensitivity space puts those comparisons on firmer footing.

Their analytic formula for the isotropic case, which matches numerical results closely, gives a quick sanity check for any future NPTF analysis. And their finding that sensitivity primarily depends on source brightness, not the many other tunable parameters, pins down where future progress must come from: either much more data from a next-generation instrument, or better measurements of the faint pulsar population's **luminosity function** (the distribution of brightness across sources in the population).

What does this mean for the dark matter question? NPTF hasn't been cleared of systematic issues; unmodeled background structure can mimic or mask point-source signatures. But when the method is properly applied to realistic data, its fundamental performance limits are well-defined and predictable. That kind of predictability is what trustworthy future dark matter claims will need to rest on.

> **Bottom Line:** NPTF's sensitivity to the Galactic Center's hidden point sources is set by physics, not analysis choices. We now know what that ceiling looks like, which is the first step toward surpassing it with future observatories.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Interdisciplinary Contribution</strong><br/><span style="color:#374151;">This work brings statistical inference techniques from data science into observational astrophysics, stress-testing a key analysis tool at the edge of dark matter detection.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Impact on AI and Statistics</strong><br/><span style="color:#374151;">The systematic sensitivity analysis offers a template for evaluating statistical methods on real-world, non-Gaussian count data, a problem that shows up well beyond gamma-ray astronomy.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By mapping NPTF's detection limits on current Fermi data, this study pins down which claims about dark matter annihilation versus pulsar populations in the Galactic Center are statistically supportable.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Outlook</strong><br/><span style="color:#374151;">Future sensitivity gains will likely require next-generation gamma-ray telescopes. This work ([arXiv:2207.13097](https://arxiv.org/abs/2207.13097)) sets the benchmark for NPTF performance going forward.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Characterizing the Expected Behavior of Non-Poissonian Template Fitting</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2207.13097](https://arxiv.org/abs/2207.13097)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">Luis Gabriel C. Bariuan, Tracy R. Slatyer</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We have performed a systematic study of the statistical behavior of non-Poissonian template fitting (NPTF), a method designed to analyze and characterize unresolved point sources in general counts datasets. In this paper, we focus on the properties and characteristics of the Fermi-LAT gamma-ray data set. In particular, we have simulated and analyzed gamma-ray sky maps under varying conditions of exposure, angular resolution, pixel size, energy window, event selection, and source brightness. We describe how these conditions affect the sensitivity of NPTF to the presence of point sources, for inner-galaxy studies of point sources within the Galactic Center excess, and for the simplified case of isotropic emission. We do not find opportunities for major gains in sensitivity from varying these choices, within the range available with current Fermi-LAT data. We provide an analytic estimate of the NPTF sensitivity to point sources for the case of isotropic emission and perfect angular resolution, and find good agreement with our numerical results for that case.</span></div></div>
</div>
