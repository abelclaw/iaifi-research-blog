---
abstract: Analyses of the cosmic 21-cm signal are hampered by astrophysical foregrounds
  that are far stronger than the signal itself. These foregrounds, typically confined
  to a wedge-shaped region in Fourier space, often necessitate the removal of a vast
  majority of modes, thereby degrading the quality of the data anisotropically. To
  address this challenge, we introduce a novel deep generative model based on stochastic
  interpolants to reconstruct the 21-cm data lost to wedge filtering. Our method leverages
  the non-Gaussian nature of the 21-cm signal to effectively map wedge-filtered 3D
  lightcones to samples from the conditional distribution of wedge-recovered lightcones.
  We demonstrate how our method is able to restore spatial information effectively,
  considering both varying cosmological initial conditions and astrophysics. Furthermore,
  we discuss a number of future avenues where this approach could be applied in analyses
  of the 21-cm signal, potentially offering new opportunities to improve our understanding
  of the Universe during the epochs of cosmic dawn and reionization.
arxivId: '2407.21097'
arxivUrl: https://arxiv.org/abs/2407.21097
authors:
- Nashwan Sabti
- Ram Reddy
- Julian B. Muñoz
- Siddharth Mishra-Sharma
- Taewook Youn
concepts:
- generative models
- flow matching
- 21-cm foreground wedge
- stochastic processes
- posterior estimation
- inverse problems
- lightcone tomography
- diffusion models
- uncertainty quantification
- cosmological simulation
- superresolution
- convolutional networks
figures:
- /iaifi-research-blog/figures/2407_21097/figure_1.png
- /iaifi-research-blog/figures/2407_21097/figure_1.png
- /iaifi-research-blog/figures/2407_21097/figure_2.png
pdfUrl: https://arxiv.org/pdf/2407.21097v1
published: '2024-07-30T18:00:00+00:00'
theme: Astrophysics
title: A Generative Modeling Approach to Reconstructing 21-cm Tomographic Data
wordCount: 1201
---

## The Big Picture

Imagine trying to hear a whisper in a thunderstorm. That's roughly the challenge facing astronomers who want to study the early universe using radio telescopes. The cosmic "whisper" is the 21-centimeter radio signal emitted by neutral hydrogen, encoding a detailed map of the universe when it was just a few hundred million years old, during **cosmic dawn** (when the first stars switched on) and **reionization** (when radiation from those stars stripped surrounding hydrogen of its electrons). The "thunderstorm" is radio noise from our own galaxy, millions of times louder than the signal astronomers are chasing.

The standard workaround is blunt: throw away the contaminated data. Foreground noise clusters into a predictable wedge-shaped zone in frequency space, so astronomers excise that entire region, a technique called **wedge filtering**. The problem is that this discards the majority of the data, leaving a distorted, incomplete picture of hydrogen distribution during reionization.

A team from MIT, Harvard, UT Austin, Johns Hopkins, and Cornell has a better idea. Instead of accepting that lost data as gone, they trained a deep generative AI model to reconstruct it.

> **Key Insight:** By exploiting statistical patterns in the 21-cm signal itself, a generative model can plausibly restore the signal components deleted by foreground filtering, recovering spatial structure once thought irretrievably lost.

## How It Works

The reconstruction relies on **stochastic interpolants**, a mathematical framework that unifies diffusion models and flow-matching models into a single formulation. Think of it as a principled recipe for teaching a neural network to transform one collection of signals into another.

The core intuition: the 21-cm signal is highly **non-Gaussian**. Its statistical structure is rich and complex, shaped by the physics of reionization. Ionized bubbles create sharp edges, holes, and filamentary patterns that leave fingerprints in the signal components *outside* the wedge. A network trained on simulations can learn those fingerprints and use surviving data to guess, probabilistically, what the missing parts looked like.

![Figure 1](/iaifi-research-blog/figures/2407_21097/figure_1.png)

The pipeline works in three stages:

1. **Data generation:** The team ran 21-cm simulations across a wide range of cosmological and astrophysical parameters, including the efficiency of early galaxies at ionizing hydrogen. Each simulation produced a paired "before and after": the original lightcone and its wedge-filtered counterpart.

2. **Neural network training:** Those pairs trained a network to learn a time-dependent **velocity field**, a function that encodes how to smoothly push one probability distribution toward another, transporting wedge-filtered lightcones toward reconstructed ones.

3. **Inference via stochastic differential equations:** At inference time, the model takes a new wedge-filtered lightcone and solves a **stochastic differential equation** (a process with both a systematic direction and a random component) using the trained network as the drift. This pushes the input toward a plausible reconstruction. Running it multiple times on the same input produces different but statistically consistent outputs, directly quantifying reconstruction uncertainty.

That last point marks the sharpest break from prior work. Earlier machine learning approaches, including a key 2021 paper this work builds on, were **deterministic**: one input in, one output out. This method instead produces a *distribution* of outputs, each consistent with the wedge-filtered data.

That's not a bug; it's the point. The universe is one realization of a random process, and any honest reconstruction method should represent its own uncertainty.

![Figure 2](/iaifi-research-blog/figures/2407_21097/figure_1.png)

The team also used **lightcones** rather than coeval boxes. A coeval box treats all data as coming from the same cosmic moment, a simplification no real telescope can achieve. A lightcone accounts for the fact that looking further away means looking further back in time, making reconstructed data directly comparable to actual measurements from instruments like HERA.

## Why It Matters

The 21-cm signal is among the most information-rich datasets humanity will ever collect about the early universe. A future radio array with full tomographic capability could measure far more modes of the primordial density field than the cosmic microwave background and galaxy surveys combined. That information, however, is locked behind the foreground problem.

The stochastic interpolant approach opens a way to recover more of it. Because the model returns a full posterior distribution (not a single best guess, but a range of statistically valid reconstructions) downstream analyses can properly propagate uncertainty. The authors show this directly for **power spectrum** estimation, which measures how much signal exists at each spatial scale: run the reconstruction many times, compute the power spectrum from each sample, and build a rigorous error budget. That matters when the science goal is extracting precise cosmological parameters from the 21-cm signal.

Future extensions could combine reconstructed 21-cm maps with other cosmic tracers: the **Lyman-alpha forest** (absorption features in quasar spectra that trace ancient hydrogen gas), photometric galaxy surveys, or **CMB lensing maps** (charts of how the cosmic microwave background was bent by intervening matter). These cross-correlations would otherwise be undetectable. As next-generation 21-cm experiments begin producing data at scale, tools like this could shift from supplementary to essential.

> **Bottom Line:** A generative AI model trained on simulated 21-cm lightcones can reconstruct the data destroyed by foreground filtering, and returns not one answer but a probabilistic distribution of answers, enabling rigorous uncertainty quantification in analyses of the early universe.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies stochastic interpolant flow matching, an advanced generative AI framework, to a core unsolved problem in observational cosmology. It shows that field-level reconstruction of the foreground-corrupted 21-cm signal is feasible with modern deep learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper extends stochastic interpolant frameworks to high-dimensional, non-Gaussian scientific datasets, showing that these generative models can learn physically meaningful conditional distributions over cosmological 3D fields.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By recovering modes lost to wedge filtering, the method expands the usable information content of 21-cm observations, potentially sharpening constraints on the astrophysics of reionization and on cosmological parameters at high redshift.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include combining reconstructed 21-cm maps with galaxy surveys and CMB data for cross-correlation science, and extending the approach to real interferometric data from HERA. The paper and code are available on arXiv (public repository: github.com/NNSSA/Rec21).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">A Generative Modeling Approach to Reconstructing 21-cm Tomographic Data</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2407.21097</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Nashwan Sabti", "Ram Reddy", "Julian B. Mu\u00f1oz", "Siddharth Mishra-Sharma", "Taewook Youn"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Analyses of the cosmic 21-cm signal are hampered by astrophysical foregrounds that are far stronger than the signal itself. These foregrounds, typically confined to a wedge-shaped region in Fourier space, often necessitate the removal of a vast majority of modes, thereby degrading the quality of the data anisotropically. To address this challenge, we introduce a novel deep generative model based on stochastic interpolants to reconstruct the 21-cm data lost to wedge filtering. Our method leverages the non-Gaussian nature of the 21-cm signal to effectively map wedge-filtered 3D lightcones to samples from the conditional distribution of wedge-recovered lightcones. We demonstrate how our method is able to restore spatial information effectively, considering both varying cosmological initial conditions and astrophysics. Furthermore, we discuss a number of future avenues where this approach could be applied in analyses of the 21-cm signal, potentially offering new opportunities to improve our understanding of the Universe during the epochs of cosmic dawn and reionization.</span></div></div>
</div>
