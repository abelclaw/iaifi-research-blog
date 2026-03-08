---
abstract: Hydrogen-poor superluminous supernovae (SLSNe) are among the most energetic
  explosions in the universe, reaching luminosities up to 100 times greater than those
  of normal supernovae. Detailed spectral analysis hold the potential to reveal their
  progenitors and underlying energy sources. This paper presents the largest compilation
  of SLSN photospheric spectra to date, encompassing data from ePESSTO+, the FLEET
  search and all published spectra up to December 2022. The dataset includes a total
  of 974 spectra of 234 SLSNe. By constructing average phase binned spectra, we find
  SLSNe initially exhibit high temperatures (10000 to 11000 K), with blue continua
  and weak lines. A rapid transformation follows, as temperatures drop to 5000 to
  6000 K by 40 days post peak, leading to stronger P-Cygni features. These averages
  also suggest a fraction of SLSNe may contain some He at explosion. Variance within
  the dataset is slightly reduced when defining the phase of spectra relative to explosion,
  rather than peak, and normalising to the population's median e-folding time. Principal
  Component Analysis (PCA) supports this, requiring fewer components to explain the
  same level of variation when binning data by scaled days from explosion, suggesting
  a more homogeneous grouping. Using PCA and K-Means clustering, we identify outlying
  objects with unusual spectroscopic evolution and evidence for energy input from
  interaction, but find not support for groupings of two or more statistically significant
  subpopulations. We find Fe II λ5169 lines velocities closely track the radius implied
  from blackbody fits, indicating formation near the photosphere. We also confirm
  a correlation between velocity and velocity gradient, which can be explained if
  all SLSNe are in homologous expansion but with different scale velocities. This
  behaviour aligns with expectations for an internal powering mechanism.
arxivId: '2503.21874'
arxivUrl: https://arxiv.org/abs/2503.21874
authors:
- Aysha Aamer
- Matt Nicholl
- Sebastian Gomez
- Edo Berger
- Peter Blanchard
- Joseph P. Anderson
- Charlotte Angus
- Amar Aryan
- Chris Ashall
- Ting-Wan Chen
- Georgios Dimitriadis
- Lluis Galbany
- Anamaria Gkini
- Mariusz Gromadzki
- Claudia P. Gutierrez
- Daichi Hiramatsu
- Griffin Hosseinzadeh
- Cosimo Inserra
- Amit Kumar
- Hanindyo Kuncarayakti
- Giorgos Leloudas
- Paolo Mazzali
- Kyle Medler
- Tomás E. Müller-Bravo
- Mauricio Ramirez
- Aiswarya Sankar. K
- Steve Schulze
- Avinash Singh
- Jesper Sollerman
- Shubham Srivastav
- Jacco H. Terwel
- David R. Young
concepts:
- supernova classification
- spectral time-series analysis
- dimensionality reduction
- magnetar central engine
- clustering
- velocity gradient analysis
- stellar evolution
- anomaly detection
- circumstellar interaction
- hypothesis testing
- bayesian inference
figures:
- /iaifi-research-blog/figures/2503_21874/figure_1.png
- /iaifi-research-blog/figures/2503_21874/figure_1.png
- /iaifi-research-blog/figures/2503_21874/figure_2.png
- /iaifi-research-blog/figures/2503_21874/figure_2.png
- /iaifi-research-blog/figures/2503_21874/figure_3.png
- /iaifi-research-blog/figures/2503_21874/figure_3.png
pdfUrl: https://arxiv.org/pdf/2503.21874v2
published: '2025-03-27T18:00:04+00:00'
theme: Astrophysics
title: 'The Type I Superluminous Supernova Catalogue II: Spectroscopic Evolution in
  the Photospheric Phase, Velocity Measurements, and Constraints on Diversity'
wordCount: 1450
---

## The Big Picture

Imagine the most powerful explosion you can conceive, then multiply it by 100. That's a **superluminous supernova (SLSN)**: a cosmic detonation so extreme that astronomers still can't fully explain where all that energy comes from. These aren't just brighter supernovae. They're a genuinely different class of phenomenon, blazing for months across billions of light-years.

The mystery runs deep. Normal supernovae draw their light from radioactive nickel forged in the explosion. SLSNe are so bright they'd need several solar masses of nickel to explain their luminosity, yet the light shows no trace of it. Something else is powering them: perhaps a rapidly spinning, ultra-magnetized neutron star called a **magnetar**, or perhaps a violent collision between the explosion and a shell of material the dying star shed beforehand. Astronomers have debated these options for over a decade without a definitive answer.

Now, an international team led by Aysha Aamer at Queen's University Belfast has assembled the largest collection of light spectra from these explosions ever compiled. A spectrum is a detailed fingerprint of light, spread out by wavelength like a rainbow, that reveals composition, temperature, and velocity. The team gathered 974 spectra from 234 SLSNe and applied statistical machine learning to hunt for hidden patterns.

> **Key Insight:** By treating the spectra of 234 superluminous supernovae as a statistical population rather than individual curiosities, the team found that SLSNe are strikingly uniform underneath their apparent diversity, and that uniformity points toward a single class of internal engine powering them all.

## How It Works

The team drew data from three major sources: the ePESSTO+ survey, the FLEET transient search program at Harvard, and every published SLSN spectrum through December 2022. The result is a database nearly three times larger than any previous compilation.

Different spectra were taken at different points in each explosion's evolution, and SLSNe change rapidly. The researchers normalized timing not just relative to peak brightness but relative to the explosion itself, then scaled by each event's characteristic decline time. Think of it as comparing aging across individuals by biological age rather than calendar date.

![Figure 1](/iaifi-research-blog/figures/2503_21874/figure_1.png)

Once aligned, the team constructed **phase-binned average spectra**: composite snapshots of what a typical SLSN looks like at each evolutionary stage. The pattern that emerged is clear:

- **At peak brightness:** SLSNe burn at 10,000–11,000 K, displaying a steep blue continuum with weak absorption features. Most elements are fully ionized and can't absorb light efficiently. A characteristic W-shaped feature from doubly-ionized oxygen between 3700 and 4650 Å marks this phase.
- **40 days after peak:** Temperatures drop to 5,000–6,000 K. Strong **P-Cygni features** emerge, double-humped profiles where expanding gas absorbs light on one side and re-emits it on the other.
- **A subtle surprise:** The average spectra hint that a fraction of SLSNe carry helium into the explosion, a clue about progenitor stars not previously established at population scale.

To probe diversity more rigorously, the team deployed **Principal Component Analysis (PCA)**, a mathematical technique that distills a complex dataset to its most essential axes of variation. Think of it as finding the fewest "ingredients" needed to reconstruct any spectrum in the collection. When spectra were grouped using the explosion-scaled timeline rather than peak-brightness dates, PCA required fewer components to explain the same fraction of variance. The population became statistically more coherent.

![Figure 3](/iaifi-research-blog/figures/2503_21874/figure_2.png)

The team then used **K-means clustering**, an algorithm that automatically sorts data into groups by similarity, to search for distinct subpopulations. Despite a handful of outliers showing signs of interaction with surrounding material, they found no statistically significant evidence for multiple distinct subclasses. SLSNe, for all their apparent variety, form a single continuous population.

![Figure 5](/iaifi-research-blog/figures/2503_21874/figure_3.png)

The final piece came from velocity measurements. The researchers tracked **Fe II λ5169**, an iron absorption line that traces the photosphere, the visible "surface" of the expanding explosion. Its velocity closely matched the radius inferred from blackbody fits to the continuum, confirming the iron line forms right at the photosphere.

They also confirmed a correlation between a SLSN's velocity and how quickly that velocity declines. All SLSNe undergo **homologous expansion**, where each layer of gas moves outward at a speed proportional to its distance from the center, like sections of a uniformly inflating balloon, but at different overall scales. Faster-expanding SLSNe slow down faster; slower ones coast more gently. This is what you'd expect if an internal engine, a magnetar spinning down, pumps energy into the ejecta from the inside out.

## Why It Matters

If magnetars are the engines, SLSNe become rare but extreme laboratories for physics impossible to recreate on Earth: magnetic fields a trillion times stronger than a hospital MRI, rotating hundreds of times per second, radiating energy at rates that dwarf the Sun's total output. The statistical uniformity found here strengthens the case that a single mechanism governs most of them.

The machine learning methods used here, PCA, clustering, variance decomposition, aren't exotic tricks bolted onto an astronomy problem. They're essential tools for making sense of a dataset no human could eyeball effectively. With the Vera Rubin Observatory set to discover thousands of new SLSNe in the coming decade, this statistical framework will become the standard. The 234 SLSNe analyzed here will look like a pilot study.

> **Bottom Line:** The largest spectroscopic survey of superluminous supernovae to date finds they form a single, coherent population whose velocity structure and spectral evolution both point to internal powering, most likely a magnetar engine, rather than external interaction as the dominant energy source.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines observational astrophysics and statistical machine learning, using PCA and K-means clustering on nearly 1,000 spectra to extract physical constraints from a high-dimensional dataset that would be intractable by traditional inspection alone.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper shows how dimensionality reduction and unsupervised clustering can serve as rigorous hypothesis-testing tools in astronomy, revealing population structure, or the absence of it, in ways conventional analysis cannot.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By establishing spectroscopic homogeneity across 234 superluminous supernovae and linking velocity behavior to homologous expansion, the study provides the strongest statistical argument yet that a single internal mechanism, consistent with magnetar spin-down, powers this entire class of explosion.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">With next-generation surveys poised to find thousands more SLSNe, this catalogue framework will scale to definitively test magnetar models against alternatives; the paper is available at [arXiv:2503.21874](https://arxiv.org/abs/2503.21874).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">The Type I Superluminous Supernova Catalogue II: Spectroscopic Evolution in the Photospheric Phase, Velocity Measurements, and Constraints on Diversity</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2503.21874</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Aysha Aamer", "Matt Nicholl", "Sebastian Gomez", "Edo Berger", "Peter Blanchard", "Joseph P. Anderson", "Charlotte Angus", "Amar Aryan", "Chris Ashall", "Ting-Wan Chen", "Georgios Dimitriadis", "Lluis Galbany", "Anamaria Gkini", "Mariusz Gromadzki", "Claudia P. Gutierrez", "Daichi Hiramatsu", "Griffin Hosseinzadeh", "Cosimo Inserra", "Amit Kumar", "Hanindyo Kuncarayakti", "Giorgos Leloudas", "Paolo Mazzali", "Kyle Medler", "Tomás E. Müller-Bravo", "Mauricio Ramirez", "Aiswarya Sankar. K", "Steve Schulze", "Avinash Singh", "Jesper Sollerman", "Shubham Srivastav", "Jacco H. Terwel", "David R. Young"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Hydrogen-poor superluminous supernovae (SLSNe) are among the most energetic explosions in the universe, reaching luminosities up to 100 times greater than those of normal supernovae. Detailed spectral analysis hold the potential to reveal their progenitors and underlying energy sources. This paper presents the largest compilation of SLSN photospheric spectra to date, encompassing data from ePESSTO+, the FLEET search and all published spectra up to December 2022. The dataset includes a total of 974 spectra of 234 SLSNe. By constructing average phase binned spectra, we find SLSNe initially exhibit high temperatures (10000 to 11000 K), with blue continua and weak lines. A rapid transformation follows, as temperatures drop to 5000 to 6000 K by 40 days post peak, leading to stronger P-Cygni features. These averages also suggest a fraction of SLSNe may contain some He at explosion. Variance within the dataset is slightly reduced when defining the phase of spectra relative to explosion, rather than peak, and normalising to the population's median e-folding time. Principal Component Analysis (PCA) supports this, requiring fewer components to explain the same level of variation when binning data by scaled days from explosion, suggesting a more homogeneous grouping. Using PCA and K-Means clustering, we identify outlying objects with unusual spectroscopic evolution and evidence for energy input from interaction, but find not support for groupings of two or more statistically significant subpopulations. We find Fe II λ5169 lines velocities closely track the radius implied from blackbody fits, indicating formation near the photosphere. We also confirm a correlation between velocity and velocity gradient, which can be explained if all SLSNe are in homologous expansion but with different scale velocities. This behaviour aligns with expectations for an internal powering mechanism.</span></div></div>
</div>
