---
abstract: Signal-agnostic data exploration based on machine learning could unveil
  very subtle statistical deviations of collider data from the expected Standard Model
  of particle physics. The beneficial impact of a large training sample on machine
  learning solutions motivates the exploration of increasingly large and inclusive
  samples of acquired data with resource efficient computational methods. In this
  work we consider the New Physics Learning Machine (NPLM), a multivariate goodness-of-fit
  test built on the Neyman-Pearson maximum-likelihood-ratio construction, and we address
  the problem of testing large size samples under computational and storage resource
  constraints. We propose to perform parallel NPLM routines over batches of the data,
  and to combine them by locally aggregating over the data-to-reference density ratios
  learnt by each batch. The resulting data hypothesis defining the likelihood-ratio
  test is thus shared over the batches, and complies with the assumption that the
  expected rate of new physical processes is time invariant. We show that this method
  outperforms the simple sum of the independent tests run over the batches, and can
  recover, or even surpass, the sensitivity of the single test run over the full data.
  Beside the significant advantage for the offline application of NPLM to large size
  samples, the proposed approach offers new prospects toward the use of NPLM to construct
  anomaly-aware summary statistics in quasi-online data streaming scenarios.
arxivId: '2407.01249'
arxivUrl: https://arxiv.org/abs/2407.01249
authors:
- Gaia Grosso
concepts:
- anomaly detection
- batch aggregation
- goodness-of-fit testing
- likelihood ratio
- hypothesis testing
- new physics searches
- density estimation
- collider physics
- scalability
- signal detection
- trigger systems
- monte carlo methods
figures:
- /iaifi-research-blog/figures/2407_01249/figure_1.png
- /iaifi-research-blog/figures/2407_01249/figure_1.png
- /iaifi-research-blog/figures/2407_01249/figure_2.png
pdfUrl: https://arxiv.org/pdf/2407.01249v2
published: '2024-07-01T12:56:38+00:00'
theme: Experimental Physics
title: Anomaly-aware summary statistic from data batches
wordCount: 1129
---

## The Big Picture

Imagine trying to find a single dropped needle in a football stadium — not by searching the whole field at once, but by dividing it into sections and having teams comb each one simultaneously. When they're done, you don't just count how many needles each team found independently. You combine their maps to get a unified picture of where anything unusual was spotted. That's essentially what this new approach to particle physics anomaly detection does, and it could change how physicists hunt for new fundamental particles.

At the Large Hadron Collider (LHC), protons smash together billions of times per second, generating an ocean of data. The Standard Model of particle physics predicts with extraordinary precision what that data should look like. Any new physics beyond the Standard Model, whether dark matter, extra dimensions, or forces we've never seen, would appear as a subtle statistical wrinkle in that ocean. The catch: finding that wrinkle requires searching enormous amounts of data, and the bigger your sample, the harder it gets computationally.

Researcher Gaia Grosso at IAIFI (the NSF AI Institute for Artificial Intelligence and Fundamental Interactions) has developed a smart divide-and-combine approach for the **New Physics Learning Machine (NPLM)**, a tool that scans particle collision data for signs of unknown physics. This strategy lets physicists search far larger datasets without computing costs exploding in proportion, and in some cases, actually improves search sensitivity.

> **Key Insight:** By splitting large particle physics datasets into parallel batches and aggregating the learned statistical patterns intelligently, you can detect new physics signals as sensitively as, or better than, analyzing the entire dataset in one shot, at a fraction of the computational cost.

## How It Works

NPLM is built on the **Neyman-Pearson likelihood ratio test**, a formal method for deciding whether two collections of data came from the same process or from different ones. The core question: does this dataset look like what the Standard Model predicts, or does it look like *something else*?

Rather than specifying what that "something else" might be, NPLM trains a neural network to learn the **density ratio**, a score calculated at every point in the data measuring how much observed collisions differ from a simulated reference dataset. A ratio everywhere close to one means the data matches the Standard Model. A significant deviation signals something anomalous.

The problem: this neural network needs to train on the full dataset to be maximally sensitive. At the LHC's scale, that means potentially millions of events across dozens of variables. The split-aggregation approach solves this in four steps:

1. **Split** the full dataset into *N* batches, each processed by an independent NPLM instance running in parallel
2. Each instance learns a local density ratio, a neural network estimate of how much the data in that batch deviates from the reference model
3. **Aggregate** those local ratios by computing their weighted average across all batches
4. Run the final statistical test on this aggregated, shared hypothesis

![Figure 1](/iaifi-research-blog/figures/2407_01249/figure_1.png)

Why not just run *N* independent tests and sum their **p-values**? That treats each batch as a completely separate experiment. Aggregation does something smarter: it recognizes that all batches sample from the same underlying physics. The averaged density ratio acts as a shared hypothesis across batches, introducing regularization that prevents any single model from over-fitting to the noise in its particular data slice.

The framework offers three operational modes: full aggregation combining all batch models, streaming mode for quasi-online analysis as data arrives continuously, and resource-limited mode that maximizes sensitivity under constrained compute.

![Figure 2](/iaifi-research-blog/figures/2407_01249/figure_1.png)

## Why It Matters

Grosso tested this framework on three progressively harder problems: a one-dimensional toy model where the math can be verified analytically; a realistic **dimuon final state** (a collision outcome producing two muons, heavy cousins of the electron) with ~10,000 events described by 5 variables from a simulated CMS-like detector; and a 24-dimensional dataset simulating the **CMS Level-1 trigger system**, the hardware filter deciding in microseconds which of the billions of collisions per second are even worth recording, with over a million events.

For the 5-dimensional dimuon problem, aggregation didn't just match the sensitivity of running NPLM on the full undivided dataset. It *outperformed* it. That seeming paradox makes sense once you understand the regularization effect: averaging over multiple batch estimates smooths out statistical fluctuations that can confuse a single neural network trained on one large, noisy sample.

![Figure 3](/iaifi-research-blog/figures/2407_01249/figure_2.png)

For the 24-dimensional CMS trigger dataset, the split-aggregation approach demonstrated clear discovery potential, successfully identifying injected anomalous signals at various rates while keeping false positive rates under control.


The practical upside is immediate. Physicists can now apply NPLM to datasets they previously couldn't touch. The LHC generates petabytes of data per year, and even the fraction passing trigger filters represents a computational challenge for methods requiring joint training on the full sample. Batch parallelization opens up more inclusive, less filtered data samples, exactly where subtle new physics might hide.

But the streaming capability may matter even more in the long run. NPLM could eventually operate *during* data collection, not just after. An anomaly-aware summary statistic that updates as new data arrives could flag unusual conditions in real time, whether new physics, detector malfunctions, or unexpected beam conditions. That would connect offline analysis and online data quality monitoring, two tasks currently handled by entirely different toolchains.


There's also a broader point here about how particle physics is evolving. Rather than designing searches for specific hypothetical particles, signal-agnostic methods like NPLM let the data itself point to anomalies. As LHC datasets grow through Run 3 and toward the High-Luminosity LHC upgrade, the ability to search those datasets efficiently and thoroughly only becomes more valuable.


> **Bottom Line:** The batch-aggregation extension of NPLM makes large-scale anomaly detection at particle colliders computationally tractable without sacrificing (and sometimes actually improving) statistical sensitivity, opening the door to real-time physics discovery in streaming data environments.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects machine learning methodology with experimental particle physics, adapting distributed computing concepts to a rigorous statistical hypothesis testing framework and making anomaly detection at the LHC scalable to realistic data volumes.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Aggregating locally-trained density ratio estimators produces better generalization than single large-scale training, a concrete example of how ensemble-style neural network combination can outperform monolithic approaches.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By scaling NPLM to millions of events across dozens of dimensions, including CMS Level-1 trigger data, this approach expands the parameter space physicists can search for Standard Model deviations without assuming any specific new-physics hypothesis.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include fully online deployment for real-time anomaly monitoring during LHC data-taking and extension to higher-dimensional trigger-level datasets; the work is available at [arXiv:2407.01249](https://arxiv.org/abs/2407.01249).</span></div></div>
</div>
