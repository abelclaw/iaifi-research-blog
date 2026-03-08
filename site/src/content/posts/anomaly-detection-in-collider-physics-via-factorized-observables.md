---
abstract: 'To maximize the discovery potential of high-energy colliders, experimental
  searches should be sensitive to unforeseen new physics scenarios. This goal has
  motivated the use of machine learning for unsupervised anomaly detection. In this
  paper, we introduce a new anomaly detection strategy called FORCE: factorized observables
  for regressing conditional expectations. Our approach is based on the inductive
  bias of factorization, which is the idea that the physics governing different energy
  scales can be treated as approximately independent. Assuming factorization holds
  separately for signal and background processes, the appearance of non-trivial correlations
  between low- and high-energy observables is a robust indicator of new physics. Under
  the most restrictive form of factorization, a machine-learned model trained to identify
  such correlations will in fact converge to the optimal new physics classifier. We
  test FORCE on a benchmark anomaly detection task for the Large Hadron Collider involving
  collimated sprays of particles called jets. By teasing out correlations between
  the kinematics and substructure of jets, our method can reliably extract percent-level
  signal fractions. This strategy for uncovering new physics adds to the growing toolbox
  of anomaly detection methods for collider physics with a complementary set of assumptions.'
arxivId: '2312.00119'
arxivUrl: https://arxiv.org/abs/2312.00119
authors:
- Eric M. Metodiev
- Jesse Thaler
- Raymond Wynne
concepts:
- anomaly detection
- factorization-based anomaly detection
- collider physics
- jet physics
- conditional expectation regression
- new physics searches
- likelihood ratio
- regression
- effective field theory
- hypothesis testing
- semi-supervised learning
- density estimation
figures:
- /iaifi-research-blog/figures/2312_00119/figure_1.png
- /iaifi-research-blog/figures/2312_00119/figure_2.png
pdfUrl: https://arxiv.org/pdf/2312.00119v2
published: '2023-11-30T19:00:00+00:00'
theme: Theoretical Physics
title: Anomaly Detection in Collider Physics via Factorized Observables
wordCount: 1223
---

## The Big Picture

Imagine finding a counterfeit coin not by examining it under a microscope, but by noticing its weight doesn't match its size, a relationship real coins always obey. You've found the anomaly not by knowing what fakes look like, but by knowing what authentic coins *shouldn't* do.

That's the challenge physicists face at the Large Hadron Collider. Since the Higgs boson discovery in 2012, the LHC has collected vast amounts of data and found nothing conclusively new. But that absence doesn't mean new physics isn't there. It might simply be hiding in forms theorists haven't thought to look for yet.

Targeted searches, which hunt for specific predicted particles, could be blind to genuinely novel phenomena. What physicists need is a way to spot the unexpected *without* knowing what they're looking for.

A team at MIT's Center for Theoretical Physics, working through IAIFI, has developed a new strategy called **FORCE** (Factorized Observables for Regressing Conditional Expectations). By exploiting a deep principle of **QCD** (Quantum Chromodynamics, the theory of how quarks and gluons build matter) called factorization, they can train a machine learning model to flag new physics purely by detecting correlations that *shouldn't exist*.

> **Key Insight:** In the Standard Model, a **jet** (a narrow spray of particles produced when quarks fly apart in a collision) has its energy set largely independently of its internal shape. If a machine learning model discovers these *are* correlated, that's a red flag for new physics. No simulation required.

## How It Works

The method centers on factorization. In QCD, the physics governing high-energy collisions (the hard scatter that sends quarks flying apart) is approximately independent from the low-energy physics that determines how those quarks shower into a collimated spray of particles. In plain terms: what a jet *looks like* on the inside shouldn't depend on how fast it's moving.

A neural network is trained to predict a jet's transverse momentum (pT, essentially how hard it was kicked sideways) using only its substructure observables: quantities describing the jet's internal geometry, such as N-subjettiness ratios (measures of how many prongs a jet has) and D₂ (how clustered its energy is).

In a Standard Model world, factorization holds. Substructure and kinematics are largely uncorrelated, and the model finds nothing interesting to learn. But if new physics is present, say jets from a hypothetical heavy particle decaying hadronically, factorization breaks down in a specific, detectable way. The model suddenly finds predictive power it shouldn't have.

The math is clean. For a mixture of QCD background jets and signal jets from new physics, the model's learned ranking (its predicted pT given jet shape) becomes monotonically related to the likelihood ratio between signal and background. One quantity increases whenever the other does, so the model's output *automatically* becomes the best possible discriminator for separating new physics from background.

That's the optimal classifier, derived purely from the data's own structure. No simulation. No prior hypothesis about what the signal looks like.

In practice, the workflow is:

1. Collect jet data from the LHC.
2. Train a neural network to predict pT from substructure observables using mean-squared error loss (a standard measure of prediction accuracy).
3. If predictions correlate strongly with true pT, factorization has been violated, and new physics is likely present.
4. Use the model's output directly as an anomaly score to rank candidate events.

## Why It Matters

The team tested FORCE on a standard benchmark: finding jets from a hypothetical $W'$ boson decaying to $WZ$, mixed into a large background of QCD jets.

![Figure 1](/iaifi-research-blog/figures/2312_00119/figure_1.png)

FORCE reliably extracts signal fractions at the percent level, a needle in a 99% background haystack, with no injected knowledge about the signal. It outperforms several existing unsupervised approaches and, under the strict factorization assumption, is provably optimal.

![Figure 2](/iaifi-research-blog/figures/2312_00119/figure_2.png)

Even when factorization holds only approximately (as it always does in practice, due to subleading QCD corrections) FORCE still performs well. It also comes with a built-in sanity check: a model trained on pure background data should be uninformative. Deviations from that baseline are quantifiable signals of genuine anomaly, not artifacts of poor modeling.


The broader field of anomaly detection at the LHC is crowded but fractured. Autoencoder-based methods define anomalies architecturally, making it hard to know what physics they're sensitive to. Resonance-hunting strategies like ANODE or CWoLa are powerful but require new physics to cluster in invariant mass. Simulation-dependent methods risk confusing detector artifacts for signals.

FORCE occupies a distinct niche: data-driven, non-resonant, and theoretically grounded. Its central assumption, factorization, is well-understood, testable, and rooted in the same QCD physicists use to calculate Standard Model predictions. When FORCE raises an alarm, physicists know exactly what assumption would have to fail to produce a false positive. That kind of interpretability is hard to come by.

Natural extensions follow: applying FORCE to event-level observables beyond jets, combining it with other anomaly detectors in ensemble strategies, or using it to constrain the *type* of new physics flagged as anomalous.

> **Bottom Line:** FORCE turns a fundamental principle of QCD into an anomaly detector, training a neural network to find correlations that physics says shouldn't exist, then proving it converges to the optimal new physics classifier when they do. It's a powerful, interpretable addition to the LHC's toolkit for hunting the unknown.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects theoretical QCD and machine learning, encoding factorization as an inductive bias to build a provably optimal, fully data-driven anomaly detector.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">FORCE shows that domain-specific physical symmetries can replace supervision signals, enabling neural networks to learn optimal classifiers without labeled data or simulation, a template for physics-informed unsupervised learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By extending model-agnostic LHC searches to non-resonant new physics at percent-level signal fractions, FORCE expands the discovery reach of the Large Hadron Collider.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will explore FORCE beyond the jet context and in combination with other anomaly detection strategies; the full paper and derivations are available at [arXiv:2312.00119](https://arxiv.org/abs/2312.00119).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Anomaly Detection in Collider Physics via Factorized Observables</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2312.00119](https://arxiv.org/abs/2312.00119)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">Eric M. Metodiev, Jesse Thaler, Raymond Wynne</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">To maximize the discovery potential of high-energy colliders, experimental searches should be sensitive to unforeseen new physics scenarios. This goal has motivated the use of machine learning for unsupervised anomaly detection. In this paper, we introduce a new anomaly detection strategy called FORCE: factorized observables for regressing conditional expectations. Our approach is based on the inductive bias of factorization, which is the idea that the physics governing different energy scales can be treated as approximately independent. Assuming factorization holds separately for signal and background processes, the appearance of non-trivial correlations between low- and high-energy observables is a robust indicator of new physics. Under the most restrictive form of factorization, a machine-learned model trained to identify such correlations will in fact converge to the optimal new physics classifier. We test FORCE on a benchmark anomaly detection task for the Large Hadron Collider involving collimated sprays of particles called jets. By teasing out correlations between the kinematics and substructure of jets, our method can reliably extract percent-level signal fractions. This strategy for uncovering new physics adds to the growing toolbox of anomaly detection methods for collider physics with a complementary set of assumptions.</span></div></div>
</div>
