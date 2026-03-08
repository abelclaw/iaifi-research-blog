---
abstract: We propose to constrain the primordial (local-type) non-Gaussianity signal
  by first reconstructing the initial density field to remove the late time non-Gaussianities
  introduced by gravitational evolution. Our reconstruction algorithm combines perturbation
  theory on large scales with a convolutional neural network on small scales. We reconstruct
  the squared potential (that sources the non-Gaussian signal) out to $k=0.2\ h$/Mpc
  to an accuracy of 99.8%. We cross-correlate this squared potential field with the
  reconstructed density field and verify that this computationally inexpensive estimator
  has the same information content as the full matter bispectrum. As a proof of concept,
  our approach can yield up to a factor of three improvement in the $f_{\rm NL}$ constraints,
  although it does not yet include the complications of galaxy bias or imperfections
  in the reconstruction. These potential improvements make it a promising alternative
  to current approaches to constraining primordial non-Gaussianity.
arxivId: '2412.00968'
arxivUrl: https://arxiv.org/abs/2412.00968
authors:
- Xinyi Chen
- Nikhil Padmanabhan
- Daniel J. Eisenstein
concepts:
- primordial non-gaussianity
- initial conditions reconstruction
- bispectrum estimation
- inverse problems
- convolutional networks
- cosmological simulation
- likelihood estimation
- bayesian inference
- surrogate modeling
- regression
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2412_00968/figure_1.png
- /iaifi-research-blog/figures/2412_00968/figure_1.png
- /iaifi-research-blog/figures/2412_00968/figure_2.png
- /iaifi-research-blog/figures/2412_00968/figure_2.png
- /iaifi-research-blog/figures/2412_00968/figure_3.png
- /iaifi-research-blog/figures/2412_00968/figure_3.png
pdfUrl: https://arxiv.org/pdf/2412.00968v2
published: '2024-12-01T21:21:26+00:00'
theme: Astrophysics
title: Probing primordial non-Gaussianity by reconstructing the initial conditions
wordCount: 1213
---

## The Big Picture

Imagine trying to read the instructions for building a house after it has already been constructed, weathered by storms, renovated multiple times, and partially demolished. That's the challenge cosmologists face when hunting for clues about the earliest moments of the universe. The tiny variations in matter density that existed just after the Big Bang (the seeds that grew into today's galaxies and cosmic filaments) have been scrambled over billions of years by gravity. To find the faint imprint of inflation, researchers must somehow undo that scrambling.

**Primordial non-Gaussianity (PNG)** sits at the center of this challenge. It measures how "non-random" the early universe's density seeds were. During inflation, the violent expansion that seeded all structure, those seeds should have been almost perfectly random, distributed like a bell curve. Tiny departures from that randomness, captured by a parameter called **f_NL**, could tell us which version of inflation actually happened.

A small f_NL (close to zero) points to the simplest picture: inflation driven by a single quantum field. A large one would mean extra fields were active in the infant universe. The goal is to measure f_NL to a precision better than 1 unit, σ(f_NL) < 1, and that's ambitious enough that even the Planck satellite's best measurement (f_NL = −0.9 ± 5.1) falls far short.

A team from Yale and Harvard has proposed a new strategy: instead of wrestling with the scrambled present-day universe directly, reconstruct the initial conditions first, then measure the PNG signal from those cleaned-up fields. Their hybrid approach, combining classical physics with a convolutional neural network, achieves a factor-of-three improvement in f_NL constraints over current methods.

> **Key Insight:** By using a neural network to undo gravitational evolution and recover the primordial density field, this method extracts PNG information with the same statistical power as the full bispectrum, at a fraction of the computational cost.

## How It Works

The standard tool for measuring f_NL in galaxy surveys is the **bispectrum**, a statistic that asks whether density clumps tend to form particular triangle configurations more or less often than chance would predict. The problem: gravity itself creates similar patterns, drowning out the primordial signal. Computing the bispectrum over all triangle configurations is also computationally brutal.

The approach here is to reconstruct the **primordial gravitational potential Φ**, the "height map" of the early universe's gravitational field before gravity had time to build complex structures, and then use a simple cross-correlation instead of the full bispectrum.

Local-type PNG generates a specific fingerprint: the initial density field contains a term proportional to the **squared potential Φ²**. By reconstructing both the density field δ and Φ², the team computes their cross-correlation ⟨Φ²δ⟩, a single compressed number that captures as much PNG information as the full bispectrum.

![Figure 1](/iaifi-research-blog/figures/2412_00968/figure_1.png)

The reconstruction algorithm operates in two regimes:

1. **Large scales (low k):** Classical **perturbation theory** handles the relatively simple physics, analytically inverting the displacement of mass under gravity.
2. **Small scales (high k):** A **convolutional neural network (CNN)** takes over, learning the nonlinear mappings from observed density fields back to initial conditions. Trained on N-body simulations, the CNN undoes the mode-coupling that perturbation theory cannot handle.

The hybrid algorithm reconstructs Φ² out to spatial scales of k = 0.2 h/Mpc, well into the highly nonlinear regime, with 99.8% accuracy.

![Figure 3](/iaifi-research-blog/figures/2412_00968/figure_2.png)

To confirm that ⟨Φ²δ⟩ truly captures all PNG information, the team runs an **optimality test**: they simulate fields with and without PNG, compute both the full bispectrum and their compressed estimator, and show that the **Fisher information** (how tightly a statistic constrains f_NL) is statistically identical between the two. The estimator doesn't discard information; it packages it more efficiently.

## Why It Matters

The factor-of-three improvement matters, but the deeper point is conceptual. Current state-of-the-art f_NL analyses from surveys like DESI exploit **scale-dependent bias**, the way PNG imprints a peculiar large-scale signature on galaxy clustering. That approach is powerful but runs into practical complications: telescope imaging artifacts, finite-sky noise, and the need to carefully model galaxy bias.

The bispectrum offers more constraining power in principle, but computational cost and the difficulty of modeling gravitational and bias-induced contributions have limited its use.

This reconstruction-based approach sidesteps many of those complications. Working in a regime where the reconstructed fields are closer to Gaussian, the modeling is cleaner, the estimator is simpler, and ⟨Φ²δ⟩ is cheap to compute. The authors are candid that the current proof-of-concept omits galaxy bias, shot noise, and imperfect reconstruction, all of which will reduce the gains in practice. But even a factor-of-two improvement in real survey data would be transformative for reaching σ(f_NL) < 1 with DESI, Euclid, SPHEREx, and the Rubin Observatory.

![Figure 5](/iaifi-research-blog/figures/2412_00968/figure_3.png)

There's a broader lesson here too. Reconstruction techniques were originally developed to sharpen the **baryon acoustic oscillation** peak, the characteristic ripple in galaxy clustering used as a cosmic distance ruler. They're now proving versatile across cosmological inference. Applying them to PNG opens a new front: rather than measuring the universe as it is today, reconstruct what it was, then ask the deeper questions. The strategy could extend to other PNG shapes and to cosmological signals buried under gravitational nonlinearities.

> **Bottom Line:** A neural-network-aided reconstruction of the primordial density field achieves 99.8% accuracy on the PNG signal source, enabling a factor-of-three improvement in f_NL constraints while matching the full bispectrum in information content. It offers a practical new path toward testing inflation models with upcoming galaxy surveys.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses classical perturbation theory with a convolutional neural network to reconstruct primordial cosmic fields, putting machine learning to work on one of observational cosmology's hardest open questions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The CNN shows that learned nonlinear inversion can recover initial conditions from gravitationally evolved density fields at 99.8% accuracy, a strong benchmark for neural surrogates in cosmological field-level inference.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling up to a factor-of-three tighter constraints on f_NL, the method brings the σ(f_NL) < 1 threshold within reach, which would distinguish single-field from multi-field inflation models of the early universe.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work must incorporate galaxy bias and realistic survey systematics to translate these proof-of-concept gains into observational constraints; the paper is available at [arXiv:2412.00968](https://arxiv.org/abs/2412.00968).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Probing primordial non-Gaussianity by reconstructing the initial conditions</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2412.00968</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Xinyi Chen", "Nikhil Padmanabhan", "Daniel J. Eisenstein"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We propose to constrain the primordial (local-type) non-Gaussianity signal by first reconstructing the initial density field to remove the late time non-Gaussianities introduced by gravitational evolution. Our reconstruction algorithm combines perturbation theory on large scales with a convolutional neural network on small scales. We reconstruct the squared potential (that sources the non-Gaussian signal) out to $k=0.2\ h$/Mpc to an accuracy of 99.8%. We cross-correlate this squared potential field with the reconstructed density field and verify that this computationally inexpensive estimator has the same information content as the full matter bispectrum. As a proof of concept, our approach can yield up to a factor of three improvement in the $f_{\rm NL}$ constraints, although it does not yet include the complications of galaxy bias or imperfections in the reconstruction. These potential improvements make it a promising alternative to current approaches to constraining primordial non-Gaussianity.</span></div></div>
</div>
