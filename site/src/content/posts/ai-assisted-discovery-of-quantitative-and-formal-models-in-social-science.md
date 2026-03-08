---
abstract: In social science, formal and quantitative models, such as ones describing
  economic growth and collective action, are used to formulate mechanistic explanations,
  provide predictions, and uncover questions about observed phenomena. Here, we demonstrate
  the use of a machine learning system to aid the discovery of symbolic models that
  capture nonlinear and dynamical relationships in social science datasets. By extending
  neuro-symbolic methods to find compact functions and differential equations in noisy
  and longitudinal data, we show that our system can be used to discover interpretable
  models from real-world data in economics and sociology. Augmenting existing workflows
  with symbolic regression can help uncover novel relationships and explore counterfactual
  models during the scientific process. We propose that this AI-assisted framework
  can bridge parametric and non-parametric models commonly employed in social science
  research by systematically exploring the space of nonlinear models and enabling
  fine-grained control over expressivity and interpretability.
arxivId: '2210.00563'
arxivUrl: https://arxiv.org/abs/2210.00563
authors:
- Julia Balla
- Sihao Huang
- Owen Dugan
- Rumen Dangovski
- Marin Soljacic
concepts:
- symbolic regression
- neuro-symbolic integration
- interpretability
- automated discovery
- scientific workflows
- sparse models
- regression
- longitudinal panel learning
- multi-task learning
- complexity-accuracy tradeoff
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2210_00563/figure_1.png
- /iaifi-research-blog/figures/2210_00563/figure_1.png
- /iaifi-research-blog/figures/2210_00563/figure_2.png
- /iaifi-research-blog/figures/2210_00563/figure_2.png
- /iaifi-research-blog/figures/2210_00563/figure_3.png
- /iaifi-research-blog/figures/2210_00563/figure_3.png
pdfUrl: https://arxiv.org/pdf/2210.00563v3
published: '2022-10-02T16:25:47+00:00'
theme: Foundational AI
title: AI-Assisted Discovery of Quantitative and Formal Models in Social Science
wordCount: 972
---

## The Big Picture

Imagine you're a detective trying to figure out what drives economic growth across nations. You have decades of data: total output, capital stock, workforce size, savings rates. But the underlying equation is hidden, buried in noise. You could fit a statistical model and call it a day, or you could trust your theoretical intuitions. Neither approach can actually see the true shape of the relationship.

That's the problem a new framework from MIT and IAIFI takes on. Social science has long relied on two imperfect tools: hand-crafted equations built on human intuition, or black-box machine learning that produces predictions nobody can explain. Both carry real costs. Intuition-driven models embed hidden assumptions. Black-box models can't tell you *why* anything happens, making them nearly useless for understanding mechanisms or designing policy.

The MIT team, led by Julia Balla and collaborators, shows that **symbolic regression**, an AI-powered search for interpretable mathematical expressions, can occupy the space between these extremes. By extending a hybrid system called OccamNet, they find compact, human-readable equations from messy real-world social science data. Not just accurate predictions, but actual equations that explain *why* social phenomena behave as they do.

## How It Works

The core tool is OccamNet, a system that combines neural networks with symbolic math to search for equations (think `Y = AK^α L^(1-α)` rather than neural network weights). OccamNet uses **genetic algorithms**, nature-inspired search methods that "breed" and refine candidate solutions, alongside deep learning. It samples candidate equations and evolves toward better fits, running in parallel on GPUs to explore enormous spaces of possible mathematical forms.

![Figure 1](/iaifi-research-blog/figures/2210_00563/figure_1.png)

Raw OccamNet wasn't built for social science data. The researchers made two key extensions:

1. **Noise tolerance via complexity regularization.** Social science datasets are small and messy. Adding a complexity penalty discourages overly complicated equations and produces a **Pareto front** of solutions, a curve showing the trade-off between equation complexity and accuracy. Researchers can then choose the right balance rather than accepting an arbitrary model.

2. **Weight-sharing for panel data.** Many social science datasets are **panel datasets**: the same variables measured across many countries or groups over time. Each country may have different parameter values, but the *form* of the equation is shared. The team's weight-sharing approach trains one model simultaneously across all panels, sharing structural knowledge while allowing panel-specific parameters. This matters most when individual time series are short.

The framework supports human-machine collaboration. Researchers supply a dataset, optionally inject **inductive priors** (known constants, preferred functional forms), and let OccamNet explore the model space. The output is a ranked list of symbolic equations with error distributions, ready for scientific interpretation.

Three benchmark tests show what this looks like in practice.

**Solow-Swan growth model.** The researchers fed OccamNet data from 18 OECD countries and asked it to discover the governing growth equation from scratch, with no theoretical guidance. It recovered the correct form. The Pareto complexity map also revealed which countries fit the standard model well and which showed systematic deviations, pointing toward where theory needs updating.

![Figure 2](/iaifi-research-blog/figures/2210_00563/figure_1.png)

**Epidemic dynamics.** Using real COVID-19 wave data, the system recovered the **Lotka-Volterra equations**, the classic predator-prey framework that also describes disease spread. The weight-sharing approach, trained across multiple epidemic waves simultaneously, outperformed models trained on single waves. Panel structure genuinely helps when individual time series are short.

**Production functions.** OccamNet didn't just recover the standard Cobb-Douglas form. It found higher-order corrections, suggesting where the standard model breaks down. The Pareto front gives researchers a systematic way to compare models rather than anchoring on whatever equation their theory happened to suggest first.

![Figure 3](/iaifi-research-blog/figures/2210_00563/figure_2.png)

## Why It Matters

One of the hardest problems in social science is that many plausible theories can fit the same data. Researchers' priors, cultural backgrounds, and theoretical commitments shape which models they even think to test. Symbolic regression doesn't eliminate human judgment, but it systematically explores the space of possible equations, reducing the risk that an analyst's blind spots determine the answer.

The approach also makes **counterfactual exploration** practical. Once you have a symbolic equation, you can ask "what alternative models fit the data almost as well?" and "what would happen if I changed this one term?" These questions are nearly impossible with a neural network, but straightforward with an interpretable equation. For policymakers, that explainability isn't a luxury.

Open questions remain. How do you handle variables that are fundamentally unobservable, like institutional quality or social norms? Can symbolic regression guide theory development in real time as new data arrives? And as language models become more capable of mathematical reasoning, could they collaborate with systems like OccamNet to propose candidate functional forms before the search even begins?

The upshot: by teaching AI to search for interpretable equations rather than just patterns, this framework gives social scientists a new scientific instrument, one that can find the hidden mathematics in human behavior while remaining transparent enough to actually be trusted.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work brings physics-inspired symbolic regression, originally developed for discovering laws of nature, directly into the social sciences. The same AI tools that find physical equations can also reveal mathematical structure in economic and sociological data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The team extended neuro-symbolic regression with two advances: improved noise tolerance via complexity regularization and a novel weight-sharing scheme for longitudinal panel data. Together, these make symbolic AI workable for small, messy real-world datasets.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By recovering governing equations like the Solow-Swan growth model and Lotka-Volterra epidemic dynamics from empirical data alone, the work shows that the mechanistic modeling paradigm central to physics transfers to complex social phenomena.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could integrate large language models to propose candidate functional forms and extend the framework to handle latent variables and causal inference; the full paper is available as [arXiv:2210.00563](https://arxiv.org/abs/2210.00563).</span></div></div>
</div>
