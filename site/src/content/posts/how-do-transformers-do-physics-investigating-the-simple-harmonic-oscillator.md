---
abstract: 'How do transformers model physics? Do transformers model systems with interpretable
  analytical solutions, or do they create "alien physics" that are difficult for humans
  to decipher? We take a step in demystifying this larger puzzle by investigating
  the simple harmonic oscillator (SHO), $\ddot{x}+2γ\dot{x}+ω_0^2x=0$, one of the
  most fundamental systems in physics. Our goal is to identify the methods transformers
  use to model the SHO, and to do so we hypothesize and evaluate possible methods
  by analyzing the encoding of these methods'' intermediates. We develop four criteria
  for the use of a method within the simple testbed of linear regression, where our
  method is $y = wx$ and our intermediate is $w$: (1) Can the intermediate be predicted
  from hidden states? (2) Is the intermediate''s encoding quality correlated with
  model performance? (3) Can the majority of variance in hidden states be explained
  by the intermediate? (4) Can we intervene on hidden states to produce predictable
  outcomes? Armed with these two correlational (1,2), weak causal (3) and strong causal
  (4) criteria, we determine that transformers use known numerical methods to model
  trajectories of the simple harmonic oscillator, specifically the matrix exponential
  method. Our analysis framework can conveniently extend to high-dimensional linear
  systems and nonlinear systems, which we hope will help reveal the "world model"
  hidden in transformers.'
arxivId: '2405.17209'
arxivUrl: https://arxiv.org/abs/2405.17209
authors:
- Subhash Kantamneni
- Ziming Liu
- Max Tegmark
concepts:
- transformers
- interpretability
- mechanistic interpretability
- in-context learning
- regression
- eigenvalue decomposition
- world models
- hamiltonian systems
- feature extraction
- spectral methods
figures:
- /iaifi-research-blog/figures/2405_17209/figure_1.png
- /iaifi-research-blog/figures/2405_17209/figure_1.png
- /iaifi-research-blog/figures/2405_17209/figure_2.png
- /iaifi-research-blog/figures/2405_17209/figure_2.png
- /iaifi-research-blog/figures/2405_17209/figure_3.png
- /iaifi-research-blog/figures/2405_17209/figure_3.png
pdfUrl: https://arxiv.org/pdf/2405.17209v1
published: '2024-05-23T01:14:22+00:00'
theme: Foundational AI
title: How Do Transformers "Do" Physics? Investigating the Simple Harmonic Oscillator
wordCount: 1277
---

## The Big Picture

Hand a black box to a physicist and ask: "Does this thing actually understand the laws of motion, or is it just memorizing patterns?" That's one of the most pressing open questions in AI research today.

Transformers (the architecture behind GPT, Claude, and a growing number of scientific models) have proven eerily good at predicting physical systems. But nobody really knows *how*. Do they rediscover the same equations physicists use? Or do they invent some alien internal calculus that happens to give the right answers?

A team at MIT led by Subhash Kantamneni, Ziming Liu, and Max Tegmark set out to answer this by studying one of the simplest physical systems imaginable: the **simple harmonic oscillator** (SHO), the equation governing everything from pendulums to quantum fields. Instead of guessing how the transformer works, they built a rigorous framework to test specific hypotheses about its internal computations.

What they found: transformers appear to solve the SHO the same way a careful physicist would, by computing the **matrix exponential**, a standard mathematical recipe for projecting a system's state forward in time. The "alien physics" worry, at least for this system, doesn't hold up.

> **Key Insight:** When trained to predict oscillator trajectories, transformers internally compute the same matrix exponential that physicists use, suggesting they learn interpretable, human-recognizable methods rather than inscrutable shortcuts.

## How It Works

The researchers framed their investigation as a hypothesis-testing problem. Given a known solution method *g* (say, the matrix exponential), does the transformer actually use *g* internally? If so, then *g*'s intermediate computational quantities should be encoded somewhere in the transformer's hidden states.

![Figure 1](/iaifi-research-blog/figures/2405_17209/figure_1.png)

To build their toolkit, they first studied a simpler stand-in: **in-context linear regression**, a task where a model estimates the relationship between inputs and outputs (a slope *w*) purely from examples, without being told the underlying formula. The model never sees *w* directly but must implicitly compute it to predict *y = wx* correctly. They defined three ways an intermediate can live inside a hidden state:

- **Linearly encoded**: a simple linear test can recover *w* from the hidden state
- **Nonlinearly encoded**: a more complex function *f(w)* is recoverable using a novel "Taylor probe," which searches for polynomial combinations of *w* via a statistical technique for finding shared structure between two sets of measurements
- **Not encoded**: neither approach finds the intermediate

From there, they formalized four criteria for establishing that a transformer actually *uses* a given method, ordered from weak to strong evidence:

1. **Correlational**: Can the intermediate be predicted from hidden states?
2. **Correlational**: Does encoding quality correlate with model performance?
3. **Weak causal**: Does the intermediate explain most of the variance in the hidden states?
4. **Strong causal**: Can you *intervene* on the hidden states to predictably change model output?

That fourth criterion is the gold standard. If you can surgically edit the transformer's hidden representation of an intermediate and watch the output change in exactly the predicted way, you have genuine causal evidence, not just correlation.

![Figure 2](/iaifi-research-blog/figures/2405_17209/figure_1.png)

With these criteria in hand, the team turned to the main event: the simple harmonic oscillator, governed by *ẍ + 2γẋ + ω₀²x = 0*. They trained transformers to predict the next position and velocity from past observations, varying the damping parameter *γ* and natural frequency *ω₀* across training examples. They generated five candidate hypotheses for how the model might solve the problem, ranging from directly inferring *γ* and *ω₀* to running numerical solvers like Euler's method (a step-by-step approximation) or the matrix exponential.

The matrix exponential hypothesis won on all four criteria. The transformer's hidden states encode the matrix exponential of the system's **dynamics matrix**, the compact mathematical object summarizing how position and velocity evolve together. Encoding quality tracks model accuracy across training checkpoints, and the matrix exponential explains the dominant variance in hidden states.

The strongest piece of evidence: when the researchers manually modified the hidden state's representation of the matrix exponential, model predictions shifted in exactly the direction the formula predicted. The model's internal representation isn't just correlated with the matrix exponential. It's driving the output.

## Why It Matters

This result matters well beyond the harmonic oscillator. A persistent worry in AI-for-science is that neural networks might build world models that are *functionally correct* but *conceptually alien*, getting right answers through representations so foreign that humans can never audit, trust, or build on them. This study counters that worry. A transformer trained on physics data reached for the same mathematical tool a physicist would.

The framework itself may be the bigger contribution. The four-criteria methodology (two correlational, one weak causal, one strong causal) gives researchers a principled ladder for making mechanistic claims about what any model computes internally. The authors designed it to generalize: the same approach can probe transformers trained on high-dimensional linear systems, nonlinear dynamics, and more complex physical scenarios.

If future work confirms that transformers consistently rediscover standard numerical methods, it would suggest these architectures have a built-in inductive bias toward human-interpretable computation. That would be a surprising and important finding.

> **Bottom Line:** Transformers trained on oscillator physics internally compute the matrix exponential, the same method physicists use, and a new four-criteria framework can rigorously prove it, opening a path toward auditing the "world models" hidden inside large AI systems.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects mechanistic interpretability in AI with classical physics, using the simple harmonic oscillator as a testbed to show that transformer architectures rediscover standard numerical methods physicists have used for decades.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The four-criteria framework (two correlational, two causal) provides a rigorous, generalizable methodology for probing whether any transformer uses a specific computational method, expanding the toolkit of mechanistic interpretability research.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By showing that transformers learn the matrix exponential for oscillator dynamics, the study suggests AI models trained on physical data may encode interpretable physics, supporting their use in scientific simulation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend this framework to high-dimensional linear systems and nonlinear dynamics, potentially revealing the full "world model" encoded in transformers trained on physical data. See the full paper: [arXiv:2405.17209](https://arxiv.org/abs/2405.17209) by Kantamneni, Liu, and Tegmark.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">How Do Transformers "Do" Physics? Investigating the Simple Harmonic Oscillator</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2405.17209</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Subhash Kantamneni", "Ziming Liu", "Max Tegmark"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">How do transformers model physics? Do transformers model systems with interpretable analytical solutions, or do they create "alien physics" that are difficult for humans to decipher? We take a step in demystifying this larger puzzle by investigating the simple harmonic oscillator (SHO), $\ddot{x}+2γ\dot{x}+ω_0^2x=0$, one of the most fundamental systems in physics. Our goal is to identify the methods transformers use to model the SHO, and to do so we hypothesize and evaluate possible methods by analyzing the encoding of these methods' intermediates. We develop four criteria for the use of a method within the simple testbed of linear regression, where our method is $y = wx$ and our intermediate is $w$: (1) Can the intermediate be predicted from hidden states? (2) Is the intermediate's encoding quality correlated with model performance? (3) Can the majority of variance in hidden states be explained by the intermediate? (4) Can we intervene on hidden states to produce predictable outcomes? Armed with these two correlational (1,2), weak causal (3) and strong causal (4) criteria, we determine that transformers use known numerical methods to model trajectories of the simple harmonic oscillator, specifically the matrix exponential method. Our analysis framework can conveniently extend to high-dimensional linear systems and nonlinear systems, which we hope will help reveal the "world model" hidden in transformers.</span></div></div>
</div>
