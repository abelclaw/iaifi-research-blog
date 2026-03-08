---
abstract: 'We present a detailed study of SN 2024ahr, a hydrogen-poor superluminous
  supernova (SLSN-I), for which we determine a redshift of $z=0.0861$. SN 2024ahr
  has a peak absolute magnitude of $M_g\approx M_r\approx -21$ mag, rest-frame rise
  and decline times (50$\%$ of peak) of about 40 and 80 days, respectively, and typical
  spectroscopic evolution in the optical band. Similarly, modeling of the UV/optical
  light curves with a magnetar spin-down engine leads to typical parameters: an initial
  spin period of $\approx 3.3$ ms, a magnetic field strength of $\approx 6\times 10^{13}$
  G, and an ejecta mass of $\approx 9.5$ M$_\odot$. Due to its relatively low redshift
  we obtained a high signal-to-noise ratio near-IR spectrum about 43 rest-frame days
  post-peak to search for the presence of helium. We do not detect any significant
  feature at the location of the He I $\,λ2.058$ $μ$m feature, and place a conservative
  upper limit of $\sim 0.05$ M$_\odot$ on the mass of helium in the outer ejecta.
  We detect broad features of Mg I $\,λ1.575$ $μ$m and a blend of Co II $\,λ2.126$
  $μ$m and Mg II, $λ2.136$ $μ$m, which are typical of Type Ic SNe, but with higher
  velocities. Examining the sample of SLSNe-I with NIR spectroscopy, we find that,
  unlike SN 2024ahr, these events are generally peculiar. This highlights the need
  for a large sample of prototypical SLSNe-I with NIR spectroscopy to constrain the
  fraction of progenitors with helium (Ib-like) and without helium (Ic-like) at the
  time of the explosion, and hence the evolutionary path(s) leading to the rare outcome
  of SLSNe-I.'
arxivId: '2501.01485'
arxivUrl: https://arxiv.org/abs/2501.01485
authors:
- Harsh Kumar
- Edo Berger
- Peter K. Blanchard
- Sebastian Gomez
- Daichi Hiramatsu
- Moira Andrews
- K. Azalee Bostroem
- Yize Dong
- Joseph Farah
- Estefania Padilla Gonzalez
- D. Andrew Howell
- Curtis McCully
- Darshana Mehta
- Megan Newsome
- Aravind P. Ravi
- Giacomo Terreran
concepts:
- supernova classification
- nir spectroscopy
- magnetar spin-down
- helium shell detection
- stellar evolution
- signal detection
- bayesian inference
- surrogate modeling
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2501_01485/figure_1.png
- /iaifi-research-blog/figures/2501_01485/figure_3.png
- /iaifi-research-blog/figures/2501_01485/figure_3.png
pdfUrl: https://arxiv.org/pdf/2501.01485v1
published: '2025-01-02T19:00:00+00:00'
theme: Astrophysics
title: A Near-IR Search for Helium in the Superluminous Supernova SN 2024ahr
wordCount: 1073
---

## The Big Picture

Imagine a star so massive that when it collapses and explodes, it outshines every other star in its galaxy combined, then multiplies that by a hundred. These are **superluminous supernovae**, cosmic detonations so extreme that astronomers are still puzzling out what produces them. At the heart of the mystery: what kind of star actually dies to create one?

Stellar explosions come in flavors. Stars that explode with a thin outer helium layer still intact are called Type Ib supernovae. Stars stripped of everything, no hydrogen, no helium, just a bare carbon-oxygen core detonating, are called Type Ic. Superluminous supernovae (SLSNe-I) lack hydrogen, but the helium question has remained stubbornly open. Do these titanic blasts come from stars that still had helium at death, or from ones that were entirely naked?

A team led by Harsh Kumar and Edo Berger at Harvard's Center for Astrophysics went after that question with SN 2024ahr, a nearby superluminous supernova that offered a rare, high-quality look in the near-infrared. That's the spectral window just beyond what human eyes can see, and it turns out to be where the helium question can finally be answered cleanly.

> **Key Insight:** By obtaining a high signal-to-noise near-infrared spectrum of SN 2024ahr, the researchers placed a strict upper limit on its helium content of just 0.05 solar masses, strongly suggesting a Type Ic-like progenitor stripped of helium before explosion.

## How It Works

The challenge with detecting helium in supernovae has always been contamination. In visible light, helium's spectral lines sit uncomfortably close to signals from calcium, sodium, and carbon, all generating their own broad features. In a superluminous supernova, the **ejecta** (the material blasted outward by the explosion) move so fast that every spectral line smears into a wide blur. Optical helium detections become essentially unreliable.

The fix is to look in the near-infrared, specifically at a helium emission line at **2.058 micrometers** (He I λ2.058 μm). This feature sits in a region largely free of competing signals. Models show it can reveal helium masses as small as 0.1 solar masses, making it the cleanest diagnostic available.

![Figure 1](/iaifi-research-blog/figures/2501_01485/figure_1.png)

SN 2024ahr made an ideal target because of its low **redshift**, a measure of how fast a galaxy is receding from us and a proxy for distance. At z = 0.0861, the light traveled roughly 1.1 billion years to reach us. For a superluminous supernova, that counts as nearby, and proximity translates directly into signal strength.

The team obtained a near-infrared spectrum about 43 rest-frame days after peak brightness, using the NIRES spectrograph on the Keck I telescope in Hawaii. Timing matters. Observe too early and the expanding gas cloud is still **optically thick**, trapping light and burying the helium signal. Wait too long and the features fade into noise.

The brightness measurements came from multiple facilities:

- UV and optical light curves from Swift, the Las Cumbres Observatory network, and the Zwicky Transient Facility
- Peak absolute magnitude M_g ≈ M_r ≈ −21, firmly superluminous
- Rise time of ~40 days, decline time of ~80 days to half-peak brightness

![Figure 2](/iaifi-research-blog/figures/2501_01485/figure_3.png)

They modeled the light curve using a **magnetar spin-down engine**, the leading explanation for what powers SLSNe-I. A magnetar is a newborn neutron star spinning hundreds of times per second, with a magnetic field so strong it transfers rotational energy into the surrounding explosion debris. The fit yielded a spin period of 3.3 milliseconds, a magnetic field of 6 × 10¹³ Gauss, and an ejecta mass of ~9.5 solar masses, all typical for the SLSN-I population.


The near-infrared spectrum told the real story. No significant signal appeared at the 2.058 μm helium line. By comparing synthetic spectra modeled with varying helium masses, the team set a conservative upper limit of ~0.05 solar masses, far below the detection threshold of most optical methods. What they *did* find were features of magnesium (Mg I λ1.575 μm) and a cobalt-magnesium blend (Co II λ2.126 μm + Mg II λ2.136 μm), stretched wider by the high ejecta velocities that define SLSNe-I. These are signatures of Type Ic supernovae.

## Why It Matters

The question of what kind of star produces a superluminous supernova isn't academic. These explosions represent an extreme endpoint of massive star evolution, a path so rare that fewer than 0.3% of all stripped-envelope supernovae reach this luminosity class.

Whether progenitors were helium-poor (Ic-like) or helium-bearing (Ib-like) at explosion constrains which evolutionary channels can lead to such extreme outcomes: binary stripping by a companion star, strong stellar winds, or other mass-loss mechanisms.

Comparing SN 2024ahr to other SLSNe-I with near-infrared spectroscopy turned up something striking. Most previously studied events are *peculiar*, with bumpy light curves, unusual spectral features, or borderline luminosities. SN 2024ahr is textbook SLSN-I.

That distinction matters because a clean, representative sample is what's needed to statistically measure the Ib-like versus Ic-like fraction. Right now, the field is working with a handful of oddities. The researchers make a strong case that more near-infrared observations of ordinary superluminous supernovae are essential to real progress.


Upcoming wide-field surveys will find supernovae at low enough redshifts for high-quality near-infrared follow-up, potentially expanding the sample rapidly. Combined with improved spectral modeling, the helium fraction in SLSN-I progenitors may soon be measurable at a population level, directly informing theories of stellar mass loss and the final years of massive star life.

> **Bottom Line:** SN 2024ahr shows that typical superluminous supernovae look like helium-stripped Type Ic events in the near-infrared, not helium-bearing Type Ib events. But the field urgently needs more observations of ordinary SLSNe-I to know how universal that conclusion really is.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines UV, optical, and infrared observations with physical engine modeling, linking data-intensive observational astronomy to fundamental questions about stellar evolution and extreme astrophysical transients.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">While primarily observational, the study depends on automated transient detection pipelines and light-curve fitting frameworks that drive the machine-learning-powered survey astronomy now discovering hundreds of superluminous supernovae per year.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Constraining the helium content of a superluminous supernova progenitor to below 0.05 solar masses tightens what we know about the mass-stripping mechanisms and evolutionary pathways governing how the most massive stars end their lives.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Expanding near-infrared spectroscopic coverage to a large, representative sample of SLSNe-I is the critical next step; the full study is available at [arXiv:2501.01485](https://arxiv.org/abs/2501.01485).</span></div></div>
</div>
