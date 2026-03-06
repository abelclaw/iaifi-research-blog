---
abstract: Accounting for inaccuracies in Monte Carlo simulations is a crucial step
  in any high energy physics analysis. It becomes especially important when training
  machine learning models, which can amplify simulation inaccuracies and introduce
  large discrepancies and systematic uncertainties when the model is applied to data.
  In this paper, we introduce a method to transform simulated events to better match
  data using normalizing flows, a class of deep learning-based density estimation
  models. Our proposal uses a technique called chained quantile morphing, which corrects
  a set of observables by iteratively shifting each entry according to a conditonal
  cumulative density function. We demonstrate the technique on a realistic particle
  physics dataset, and compare it to a neural network-based reweighting method. We
  also introduce a new contrastive learning technique to correct high dimensional
  particle-level inputs, which naively cannot be efficiently corrected with morphing
  strategies.
arxivId: '2309.15912'
arxivUrl: https://arxiv.org/abs/2309.15912
authors:
- Samuel Bright-Thonney
- Philip Harris
- Patrick McCormack
- Simon Rothman
concepts:
- normalizing flows
- chained quantile morphing
- density estimation
- collider physics
- monte carlo methods
- detector simulation
- contrastive learning
- uncertainty quantification
- distribution morphing
- optimal transport
- jet physics
- dimensionality reduction
- simulation-based inference
figures:
- /iaifi-research-blog/figures/2309_15912/figure_1.png
- /iaifi-research-blog/figures/2309_15912/figure_2.png
- /iaifi-research-blog/figures/2309_15912/figure_3.png
pdfUrl: https://arxiv.org/pdf/2309.15912v1
published: '2023-09-27T18:00:03+00:00'
theme: Experimental Physics
title: Chained Quantile Morphing with Normalizing Flows
wordCount: 1033
---

## The Big Picture

Imagine training a self-driving car exclusively in a video game, then expecting it to navigate real city streets. The simulated world looks close enough — same roads, same traffic lights — but subtle differences accumulate. The car has learned the quirks of the simulation, not reality.

Physicists at the Large Hadron Collider face an eerily similar problem. They rely on **Monte Carlo simulations** — computer programs that recreate the chaos of proton-proton collisions by generating millions of random events — to train the machine learning algorithms that sift through petabytes of experimental data. These simulations are extraordinarily sophisticated, but imperfect.

They struggle to capture every nuance of how particles interact with detectors, how quarks clump into composite particles, and dozens of other messy real-world effects. When a neural network trained on simulated data encounters real collision events, the gaps between simulation and reality translate directly into measurement errors.

This problem has grown more acute as physicists have embraced more powerful machine learning models operating on granular, particle-level data — models that are also more sensitive to simulation quirks. Researchers from Cornell and MIT, working under the IAIFI umbrella, have developed an elegant solution: a technique called **chained quantile morphing with normalizing flows** that systematically reshapes simulated data to match reality, without discarding the simulations entirely.

> **Key Insight:** Rather than reweighting simulated events or throwing them out, chained quantile morphing physically transforms the simulated data distribution to match experimental data — correcting the simulation itself, one observable at a time.

## How It Works

The core idea draws on a beautiful mathematical fact: any probability distribution can be transformed into any other using **cumulative distribution functions (CDFs)** — tools that describe what fraction of a dataset falls below any given value. In one dimension, this is almost trivial. If you know where a simulated particle falls in the simulated distribution, you can map it to the corresponding position in the real distribution. Same quantile, different value. The simulation measured your photon at 47 GeV; the real detector would have seen 49 GeV. Shift it accordingly.

The challenge explodes in higher dimensions. Particle collisions don't produce single numbers — they produce jets of dozens of particles, each with energy, momentum, and angular coordinates. These observables are deeply correlated. Correcting each one independently would destroy those correlations, producing physically nonsensical events.

**Chained quantile morphing (CQM)** solves this by correcting observables sequentially, each conditioned on those already corrected:

- Correct observable $x_1$ using its marginal CDF
- Correct $x_2$ conditioned on the corrected $x_1$
- Correct $x_3$ conditioned on corrected $x_1$ and $x_2$
- Continue until all observables are corrected

Each step uses a **normalizing flow** — a deep learning model that learns smooth, invertible transformations between probability distributions — to estimate the conditional CDFs continuously. Earlier implementations relied on discretized, binned approximations; normalizing flows replace those with expressive neural estimators that handle complex correlations without binning artifacts.

![Figure 1](/iaifi-research-blog/figures/2309_15912/figure_1.png)

The result is a transformed simulated dataset where each event has been physically shifted to match the real data distribution, while preserving inter-observable correlations. The authors demonstrate this on realistic jet events — the particle sprays produced when high-energy quarks and gluons scatter — correcting observables like jet mass, charged particle fraction, and track multiplicity.

For truly high-dimensional inputs (dozens or hundreds of particles per jet), CQM hits a wall. The chain of conditional CDFs becomes computationally intractable at scale.

The team's answer is clever: use **contrastive learning** — where a neural network learns to distinguish real data from simulated data — to compress the high-dimensional particle cloud into a low-dimensional summary that captures the physically relevant information. CQM then operates in this compressed space. Morphing there and mapping back to particle-level inputs corrects the full distribution without confronting the raw dimensionality.

![Figure 2](/iaifi-research-blog/figures/2309_15912/figure_2.png)

## Why It Matters

The stakes are higher than they might appear. Monte Carlo corrections don't just eliminate a technical nuisance — they directly limit the precision of Standard Model measurements and the sensitivity of searches for new physics. As the LHC enters high-luminosity operation and physicists squeeze every last bit of statistical power from their datasets, systematic uncertainties from simulation mismodeling could become the dominant limitation. A method that reduces those uncertainties isn't a convenience — it's a potential key to discoveries otherwise hidden in the noise.

CQM with normalizing flows offers concrete advantages over existing reweighting methods. When simulated and real distributions differ substantially — particularly in the tails, where rare but important events live — reweighting assigns enormous statistical weights to individual events, bloating uncertainties. Morphing sidesteps this by physically moving events rather than up-weighting them.

The authors demonstrate that CQM is robust to small levels of signal contamination, can be trained in a control region, and accurately interpolates into a blinded signal region — all essential properties for deployment in real LHC analyses. Against neural network reweighting, CQM shows competitive performance overall and excels precisely in the regimes where reweighting struggles most.

![Figure 3](/iaifi-research-blog/figures/2309_15912/figure_3.png)

> **Bottom Line:** Chained quantile morphing with normalizing flows offers a principled, powerful way to correct Monte Carlo simulations for particle physics analysis — and a new contrastive learning extension opens the door to correcting the high-dimensional particle-level data that modern ML models crave.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies state-of-the-art deep learning — normalizing flows and contrastive learning — to a central practical challenge in experimental particle physics, demonstrating that modern generative ML can serve as precision calibration tools at the LHC.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces a continuous, flow-based implementation of chained quantile morphing and a novel contrastive learning strategy for high-dimensional domain adaptation — techniques with potential applications beyond physics wherever simulation-to-reality gaps limit ML performance.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By reducing systematic uncertainties from Monte Carlo mismodeling, this method directly improves the precision of LHC measurements and the sensitivity of new physics searches, addressing one of the primary bottlenecks in cutting-edge experimental analyses.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend CQM to even higher-dimensional inputs and explore integration into end-to-end analysis pipelines; the method is detailed in arXiv:2309.xxxxx by Bright-Thonney, Harris, McCormack, and Rothman (2023).</span></div></div>
</div>
