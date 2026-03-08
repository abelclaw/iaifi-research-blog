---
abstract: The intrinsic alignments (IA) of galaxies, regarded as a contaminant in
  weak lensing analyses, represents the correlation of galaxy shapes due to gravitational
  tidal interactions and galaxy formation processes. As such, understanding IA is
  paramount for accurate cosmological inferences from weak lensing surveys; however,
  one limitation to our understanding and mitigation of IA is expensive simulation-based
  modeling. In this work, we present a deep learning approach to emulate galaxy position-position
  ($ξ$), position-orientation ($ω$), and orientation-orientation ($η$) correlation
  function measurements and uncertainties from halo occupation distribution-based
  mock galaxy catalogs. We find strong Pearson correlation values with the model across
  all three correlation functions and further predict aleatoric uncertainties through
  a mean-variance estimation training procedure. $ξ(r)$ predictions are generally
  accurate to $\leq10\%$. Our model also successfully captures the underlying signal
  of the noisier correlations $ω(r)$ and $η(r)$, although with a lower average accuracy.
  We find that the model performance is inhibited by the stochasticity of the data,
  and will benefit from correlations averaged over multiple data realizations. Our
  code will be made open source upon journal publication.
arxivId: '2404.13702'
arxivUrl: https://arxiv.org/abs/2404.13702
authors:
- Sneh Pandya
- Yuanyuan Yang
- Nicholas Van Alfen
- Jonathan Blazek
- Robin Walters
concepts:
- intrinsic alignment
- emulation
- surrogate modeling
- uncertainty quantification
- halo occupation distribution
- cosmological simulation
- simulation-based inference
- weak gravitational lensing
- dark matter
- regression
- multi-task learning
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2404_13702/figure_1.png
- /iaifi-research-blog/figures/2404_13702/figure_1.png
- /iaifi-research-blog/figures/2404_13702/figure_2.png
- /iaifi-research-blog/figures/2404_13702/figure_2.png
- /iaifi-research-blog/figures/2404_13702/figure_3.png
- /iaifi-research-blog/figures/2404_13702/figure_3.png
pdfUrl: https://arxiv.org/pdf/2404.13702v1
published: '2024-04-21T16:16:56+00:00'
theme: Astrophysics
title: Learning Galaxy Intrinsic Alignment Correlations
wordCount: 1011
---

## The Big Picture

Imagine measuring the curvature of a glass lens while someone keeps smearing fingerprints on it. That's roughly the challenge cosmologists face when mapping the universe's invisible scaffolding — dark matter — using the subtle distortion of light from distant galaxies. The technique is called **weak gravitational lensing**: massive objects warp space, bending background light, and by measuring those tiny distortions in galaxy shapes, astronomers can chart where dark matter lurks.

But there's a persistent smudge. Galaxies don't point in random directions — gravity tugs them into alignments with each other and with the vast filamentary web of matter filling the universe, creating a fake lensing signal that bleeds into the real one.

This contamination is called **intrinsic alignment (IA)** — the tendency of galaxies to orient themselves based on gravitational tugs from surrounding matter, rather than from light being bent along our line of sight. Ignore IA and your cosmological measurements go badly wrong. Modeling it properly requires enormous, expensive computer simulations with no cheap analytical shortcut.

A team from Northeastern University and the NSF AI Institute for Artificial Intelligence and Fundamental Interactions (IAIFI) trained a neural network to stand in for those simulations — predicting IA statistics in milliseconds rather than hours.

> **Key Insight:** A deep learning emulator can predict galaxy intrinsic alignment correlation functions from seven physical parameters with roughly 10% accuracy, potentially replacing costly simulation runs in cosmological analyses.

## How It Works

The researchers built their training data using a layered pipeline. They started with **N-body simulations** — numerical experiments tracking how gravity moves billions of dark matter particles through a simulated universe. From these, they extracted catalogs of dark matter **halos**, the gravitational knots where galaxies form, then populated those halos with galaxies using a **Halo Occupation Distribution (HOD) model**: a statistical recipe governing how many galaxies live in a halo of a given mass and where they sit.

The key addition was an IA extension to the standard HOD framework. Central galaxies — the massive ones at a halo's core — were aligned with their host halo's **major axis** (its longest physical dimension), while satellite galaxies orbiting within were aligned radially toward the center. Both models include stochasticity, random scatter reflecting the messiness of real galaxy formation. Seven parameters control the whole system: five HOD occupation parameters governing galaxy counts, plus two IA strength parameters (one for centrals, one for satellites).

![Figure 1](/iaifi-research-blog/figures/2404_13702/figure_1.png)

From each mock catalog, the team measured three distinct correlation functions across 20 radial bins:

- **ξ(r)**: position-position — how galaxies cluster in space
- **ω(r)**: position-orientation — whether a galaxy's orientation correlates with its neighbors' positions
- **η(r)**: orientation-orientation — whether two galaxies tend to point toward each other

These three functions together paint a complete statistical picture of how galaxy shapes and positions are linked. Computing them from simulations is the expensive part. The neural network's job is to skip that computation entirely.

![Figure 2](/iaifi-research-blog/figures/2404_13702/figure_1.png)

The architecture is an **encoder-decoder network**. The encoder compresses the seven HOD+IA input parameters into a compact internal summary; the decoder expands that summary into the full set of correlation values across all radial bins. Crucially, the model also predicts **aleatoric uncertainties** — the irreducible noise from galaxy formation's stochasticity — using a **mean-variance estimation** procedure: the network learns to output both its best guess and a calibrated error bar. This is essential for any downstream statistical analysis.

![Figure 4](/iaifi-research-blog/figures/2404_13702/figure_2.png)

## Why It Matters

The position-position correlation ξ(r) comes out cleanest, with predictions accurate to ≤10% and strong Pearson correlation values — a standard measure of how closely predictions track true values. Clustering statistics are relatively smooth and well-behaved.

The orientation correlations ω(r) and η(r) are harder. Galaxy orientations are more sensitive to the stochastic scatter in the alignment models, and the emulator's accuracy drops accordingly. The model captures the underlying signal, but individual predictions carry larger errors. The root cause is the training data itself: when each simulation realization is somewhat random, the network must learn average behavior from noisy examples. Averaging measurements over multiple simulation runs would sharpen the training signal significantly.

![Figure 5](/iaifi-research-blog/figures/2404_13702/figure_3.png)

Weak lensing surveys are entering a golden age. Experiments like the Rubin Observatory's LSST, the Euclid satellite, and the Nancy Grace Roman Space Telescope are collecting galaxy shapes for billions of objects. Extracting cosmological constraints — how fast the universe is expanding, how clumpy dark matter is — requires modeling IA with high precision. Getting it wrong biases everything downstream.

The traditional solution is to run many expensive N-body simulations across a wide parameter range, compute statistics from each, and build an interpolating model. This work short-circuits that chain. Once trained, the neural network generates predictions in milliseconds on a GPU, enabling the rapid Monte Carlo parameter inference needed to explore high-dimensional parameter spaces — a qualitative change in what's computationally feasible.

> **Bottom Line:** This neural network emulator predicts all three galaxy intrinsic alignment correlation functions from seven physical parameters in milliseconds, achieving ~10% accuracy on clustering statistics and laying the groundwork for fast, simulation-free IA modeling in next-generation lensing surveys.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines neural network emulation with physical cosmological simulations, using HOD-based galaxy catalogs to train a model predicting statistics central to weak lensing cosmology — a direct example of AI accelerating fundamental physics inference.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The mean-variance estimation framework produces calibrated aleatoric uncertainty predictions alongside correlation function estimates, demonstrating how uncertainty quantification can be built into scientific emulators rather than treated as an afterthought.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By making intrinsic alignment modeling orders of magnitude faster, this emulator directly addresses one of the main systematic uncertainties limiting cosmological constraints from weak gravitational lensing — a measurement sensitive to dark matter distribution across cosmic scales.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will focus on training with averaged realizations to reduce stochasticity-driven errors and extending to hydrodynamic simulations; the paper appeared in the Journal of Data-centric Machine Learning Research (2024) and code will be released open source upon publication.</span></div></div>
</div>
