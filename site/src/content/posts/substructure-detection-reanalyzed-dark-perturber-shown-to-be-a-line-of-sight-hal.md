---
abstract: Observations of structure at sub-galactic scales are crucial for probing
  the properties of dark matter, which is the dominant source of gravity in the universe.
  It will become increasingly important for future surveys to distinguish between
  line-of-sight halos and subhalos to avoid wrong inferences on the nature of dark
  matter. We reanalyze a sub-galactic structure (in lens JVAS B1938+666) that has
  been previously found using the gravitational imaging technique in galaxy-galaxy
  lensing systems. This structure has been assumed to be a satellite in the halo of
  the main lens galaxy. We fit the redshift of the perturber of the system as a free
  parameter, using the multi-plane thin-lens approximation, and find that the redshift
  of the perturber is $z_\mathrm{int} = 1.42\substack{+0.10 \\ -0.15}$ (with a main
  lens redshift of $z=0.881$). Our analysis indicates that this structure is more
  massive than the previous result by an order of magnitude. This constitutes the
  first dark perturber shown to be a line-of-sight halo with a gravitational lensing
  method.
arxivId: '2112.00749'
arxivUrl: https://arxiv.org/abs/2112.00749
authors:
- Atınç Çağan Şengül
- Cora Dvorkin
- Bryan Ostdiek
- Arthur Tsang
concepts:
- gravitational lensing
- dark matter
- multi-plane lensing
- inverse problems
- bayesian inference
- posterior estimation
- nfw profile
- halo mass function
- simulation-based inference
- cosmological simulation
figures:
- /iaifi-research-blog/figures/2112_00749/figure_1.png
- /iaifi-research-blog/figures/2112_00749/figure_3.png
pdfUrl: https://arxiv.org/pdf/2112.00749v3
published: '2021-12-01T19:00:01+00:00'
theme: Astrophysics
title: 'Substructure Detection Reanalyzed: Dark Perturber shown to be a Line-of-Sight
  Halo'
wordCount: 1202
---

## The Big Picture

Imagine trying to identify a car's make and model from its shadow alone, and the shadow might belong to a car parked right beside you or to one miles away. That's roughly the challenge astronomers face when searching for hidden clumps of dark matter in **gravitational lens** images, where a foreground galaxy's gravity bends and distorts light from a background galaxy into stretched arcs or perfect rings.

A tiny distortion in one of those arcs might signal a dark matter satellite, a small clump of invisible matter orbiting the foreground galaxy like a dark moon around a dark planet. Or it might come from a completely separate dark matter cloud drifting somewhere between us and the distant background galaxy. For decades, researchers have assumed the former. A new analysis by Harvard physicists suggests that assumption can be badly wrong.

The system in question, **JVAS B1938+666**, is one of only a handful of galaxy-galaxy lenses where astronomers have directly imaged a dark gravitational perturber, a clump of matter with no visible stars, detectable only through tiny distortions it imprints on the lensed **Einstein ring**. (That's the complete halo of light that forms when foreground and background galaxies align nearly perfectly.) When first reported in 2012 by Vegetti and collaborators, this perturber was logged as a **subhalo** orbiting the main foreground galaxy, with a mass of roughly 190 million solar masses. A reasonable subhalo, if **cold dark matter** (the leading theory, which holds that dark matter particles move slowly and clump predictably) behaves as cosmologists expect.

Atınç Çağan Şengül, Cora Dvorkin, Bryan Ostdiek, and Arthur Tsang asked a different question: what if the perturber isn't orbiting the lens galaxy at all? What if it's a free-floating halo sitting somewhere behind it, along the line of sight? Their answer overturns a decade-old result and sounds an alarm for the entire field of dark matter substructure science.

> A gravitational lensing analysis has, for the first time, proven that a "dark perturber" previously classified as a satellite of the main lens is actually a free-floating **line-of-sight halo**, and its true mass is ten times larger than originally claimed.

## How It Works

The **gravitational imaging** technique works by forward-modeling a lensed image pixel by pixel. You build a model of the main lens galaxy's mass distribution, a model of the background source, add any small perturbers, and compare the predicted image to the real Hubble Space Telescope observation. Where the model fails, where residuals are too large, you've found substructure.

![Figure 1](/iaifi-research-blog/figures/2112_00749/figure_1.png)

The team's approach was straightforward: they treated the **redshift** of the perturber as a free parameter. Redshift measures how far an object's light has been stretched by cosmic expansion; the farther away an object is, the higher its redshift. Letting the math decide where along the line of sight the perturber actually sits, rather than assuming it shares the main lens galaxy's redshift (z = 0.881), opens up the possibility that the perturber lives somewhere else entirely.

The standard assumption makes intuitive sense: satellites orbit their hosts. But gravitational optics doesn't enforce it. A foreground or background halo can produce similar arc distortions, and without a spectroscopic redshift for a dark, invisible object, a single image can't pin down its location.

To model a perturber at a different redshift than the main lens, the team used the **multi-plane thin-lens approximation**, a framework that tracks light rays bending through multiple gravitational planes stacked along the line of sight, like a stack of curved glass sheets. A background halo's deflection pattern has a non-vanishing **curl** (a measurable twist in how light rays are redirected) that a single-plane model cannot reproduce. That geometric fingerprint breaks the degeneracy between perturber redshift and position that would otherwise make the two scenarios look identical.

Their pipeline used `lenstronomy`, an open-source Python lensing package, with these model components:

- A **Power-Law Elliptical Mass Distribution (PEMD)** for the main lens, the standard model for how mass spreads outward from the galaxy's center in an elliptical, power-law pattern
- A **Navarro-Frenk-White (NFW) profile** for the perturber, the standard theoretical shape for dark matter halos, with a dense core tapering off toward the edges
- An external shear component to account for nearby mass structures
- Two Sérsic profiles for lens-light subtraction

They sampled the full posterior over all model parameters, including the perturber's redshift, position, mass, and concentration. The result was unambiguous.

![Figure 2](/iaifi-research-blog/figures/2112_00749/figure_3.png)

## Why It Matters

The perturber's redshift converged not to z = 0.881, but to **z = 1.42** (±0.10/0.15), well behind the main lens galaxy. It's not a satellite but an interloper: a free-floating dark matter halo drifting along the line of sight between the lens and the source galaxy at z = 2.059.

The mass consequence is dramatic. As a tightly-bound subhalo, the perturber appeared to weigh ~1.9 × 10⁸ solar masses. Recast as a background NFW halo with its true geometry, it comes out an order of magnitude heavier. The difference arises because the lensing geometry, specifically how far the perturber sits from the observer-source line, changes entirely when you place it at a different redshift.


This isn't a minor calibration tweak. It's a qualitatively different physical object, living in a qualitatively different environment, obeying a qualitatively different mass function.

The stakes extend well beyond one misidentified halo. Strong gravitational lens surveys from Rubin Observatory's LSST and Euclid will detect hundreds to thousands of dark perturbers in the coming decade. If astronomers keep assuming every detected perturber is a subhalo and use those detections to constrain the **subhalo mass function** (a direct discriminant between cold dark matter and warmer or fuzzier alternatives), they will systematically bias their results with contaminating interlopers.

Previous theoretical work, including by the same Harvard group, had already predicted that most detected perturbers *should* be interlopers based on number density arguments. This paper is the first empirical confirmation using a real lensing system. Future substructure analyses must fit the perturber redshift as a free parameter, or risk drawing wrong conclusions about the fundamental nature of dark matter.

> What was thought to be a 190-million-solar-mass dark satellite turns out to be a billion-solar-mass free-floating halo sitting behind the lens. A case of mistaken cosmic identity that reveals a systematic blind spot in how the field measures dark matter substructure.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work unites gravitational lensing astrophysics with Bayesian inference and open-source computational modeling, showing how rigorous statistical reanalysis of existing data can overturn physical interpretations without new observations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The pipeline uses differentiable lensing software and full posterior sampling over high-dimensional parameter spaces, pointing toward future ML-accelerated lens modeling that can systematically fit perturber redshifts at survey scale.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By showing that a canonical "dark matter subhalo" detection is actually a line-of-sight halo, this work challenges how the field constrains subhalo mass functions, a cornerstone observable for distinguishing cold dark matter from alternative dark matter models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future strong-lensing surveys must adopt multi-plane lens modeling and treat perturber redshift as a free parameter to avoid biased inferences on dark matter properties; the full analysis is available at [arXiv:2112.00749](https://arxiv.org/abs/2112.00749).</span></div></div>
</div>
