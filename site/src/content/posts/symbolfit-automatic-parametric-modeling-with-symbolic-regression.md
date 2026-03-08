---
abstract: We introduce SymbolFit, a framework that automates parametric modeling by
  using symbolic regression to perform a machine-search for functions that fit the
  data while simultaneously providing uncertainty estimates in a single run. Traditionally,
  constructing a parametric model to accurately describe binned data has been a manual
  and iterative process, requiring an adequate functional form to be determined before
  the fit can be performed. The main challenge arises when the appropriate functional
  forms cannot be derived from first principles, especially when there is no underlying
  true closed-form function for the distribution. In this work, we develop a framework
  that automates and streamlines the process by utilizing symbolic regression, a machine
  learning technique that explores a vast space of candidate functions without requiring
  a predefined functional form because the functional form itself is treated as a
  trainable parameter, making the process far more efficient and effortless than traditional
  regression methods. We demonstrate the framework in high-energy physics experiments
  at the CERN Large Hadron Collider (LHC) using five real proton-proton collision
  datasets from new physics searches, including background modeling in resonance searches
  for high-mass dijet, trijet, paired-dijet, diphoton, and dimuon events. We show
  that our framework can flexibly and efficiently generate a wide range of candidate
  functions that fit a nontrivial distribution well using a simple fit configuration
  that varies only by random seed, and that the same fit configuration, which defines
  a vast function space, can also be applied to distributions of different shapes,
  whereas achieving a comparable result with traditional methods would have required
  extensive manual effort.
arxivId: '2411.09851'
arxivUrl: https://arxiv.org/abs/2411.09851
authors:
- Ho Fung Tsoi
- Dylan Rankin
- Cecile Caillol
- Miles Cranmer
- Sridhara Dasu
- Javier Duarte
- Philip Harris
- Elliot Lipeles
- Vladimir Loncar
concepts:
- symbolic regression
- uncertainty quantification
- regression
- new physics searches
- background parametric modeling
- collider physics
- genetic programming
- hypothesis testing
- goodness-of-fit testing
- automated discovery
- expression tree search
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2411_09851/figure_1.png
- /iaifi-research-blog/figures/2411_09851/figure_1.png
- /iaifi-research-blog/figures/2411_09851/figure_2.png
- /iaifi-research-blog/figures/2411_09851/figure_2.png
- /iaifi-research-blog/figures/2411_09851/figure_3.png
- /iaifi-research-blog/figures/2411_09851/figure_3.png
pdfUrl: https://arxiv.org/pdf/2411.09851v4
published: '2024-11-15T00:09:37+00:00'
theme: Experimental Physics
title: 'SymbolFit: Automatic Parametric Modeling with Symbolic Regression'
wordCount: 964
---

## The Big Picture

Imagine trying to describe a mountain range's shape with an equation, but having no idea what kind of equation to use. You could try a parabola, a sine wave, a polynomial. You'd guess, test, fail, tweak, and guess again for days.

Now imagine a machine that searches through millions of possible equation shapes simultaneously, finds ones that fit, and tells you how uncertain each fit is. All in one automated run. That's what physicists have built for one of the toughest fitting problems in experimental physics.

At the Large Hadron Collider, scientists hunting for signs of new physics (new particles, new forces, phenomena beyond the Standard Model) must first model the "background": ordinary collision events that look similar to, but aren't, any new physics signal. Background modeling means fitting a mathematical function to data arranged as a histogram of collision counts across some measured quantity.

Nobody knows what that function should look like. Detector quirks, filtering choices, and complex physics all distort the data's shape in ways that can't be predicted from first principles. Physicists have historically resorted to educated guessing, manual iteration, and painful trial-and-error.

A team from the University of Pennsylvania, MIT, CERN, and Cambridge has now built **SymbolFit** ([arXiv:2411.09851](https://arxiv.org/abs/2411.09851)), a framework that automates this entire process using **symbolic regression**, a machine learning approach that searches for the best functional form, not just the best parameters.

> **Key Insight:** SymbolFit treats the mathematical form of the fitting function itself as something to be discovered, not assumed in advance. A machine finds good candidate equations from scratch while simultaneously estimating their uncertainties, eliminating the need for human guesswork.

## How It Works

Traditional regression fixes the equation's shape first (say, a power law or an exponential) then optimizes its parameters. Symbolic regression throws out that constraint entirely. It explores a vast space of possible mathematical structures using **genetic programming**: an evolutionary algorithm inspired by biology.

Here's the core idea:

1. Functions are represented as **expression trees**, branching diagrams where each node is a mathematical operator (`+`, `×`, `exp`, `sin`, etc.), a variable, or a constant.
2. The algorithm starts with a population of random expression trees.
3. It evolves them through **mutation** (randomly swapping a node) and **crossover** (swapping subtrees between two candidates), just like genetic recombination in biology.
4. Over many generations, the fittest functions, those that best describe the data, survive and propagate.

![Figure 1](/iaifi-research-blog/figures/2411_09851/figure_1.png)

The result is a catalog of candidate functions at varying levels of complexity. SymbolFit then re-optimizes every promising candidate's free parameters using standard curve-fitting algorithms, computing uncertainty bands at the same time.

That second step matters more than it might sound. Raw symbolic regression outputs best-fit functions but says nothing about how uncertain they are. Without uncertainty estimates, no function can feed into the statistical inference machinery physicists use to claim a discovery or set a limit on new physics.

Under the hood, SymbolFit builds on **PySR**, Miles Cranmer's open-source symbolic regression package, wrapping it in a pipeline that handles count data in histogram bins, propagates uncertainties, and outputs results compatible with particle physics statistical analysis tools.

## Why It Matters

The team validated SymbolFit on five real CMS datasets from the LHC, covering searches involving dijets, trijets, paired-dijets, diphotons, and dimuons. These are among the highest-energy, highest-statistics datasets from the world's most powerful particle collider.

![Figure 2](/iaifi-research-blog/figures/2411_09851/figure_1.png)

In each case, a single fit configuration (defining the allowed mathematical building blocks) worked across distributions with substantially different shapes. SymbolFit generated a wide variety of candidate functions in one run, varying only the random seed. With traditional methods, each new distribution requires a physicist to start over: rethink the functional form, rerun fits, manually vet results. SymbolFit collapses all of that into an automated pipeline.

![Figure 3](/iaifi-research-blog/figures/2411_09851/figure_2.png)

For a single dataset, SymbolFit might return dozens of valid candidates, from simple power laws to exotic combinations of exponentials and polynomials, each with its own uncertainty band. A physicist picks the best-performing ones for downstream analysis, rather than struggling to construct even one good option by hand.

None of this is limited to the LHC. Any field that fits mathematical models to data (astrophysics, genomics, climate science, economics) faces the same problem: the right functional form is unknown, and searching for it is expensive and human-intensive. Symbolic regression automates that search in a reproducible way.

Within particle physics, the stakes are concrete. A wrong background model can generate a fake discovery signal, or bury a real one. By offering many candidate functions with proper uncertainties, SymbolFit gives analysts a more transparent toolkit and reduces a source of human bias: physicists' prior intuitions inevitably shape which functional forms they try first.

The team plans to extend SymbolFit to two-dimensional distributions and joint signal-plus-background modeling. The framework is already publicly available and open-source.

> **Bottom Line:** SymbolFit automates one of experimental physics' most tedious and error-prone tasks, finding the right equation to describe messy LHC data, by treating the function's mathematical form itself as something a machine can discover and validate automatically.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">SymbolFit connects machine learning and experimental high-energy physics, deploying symbolic regression as a core tool in LHC data analysis workflows that require rigorous statistical uncertainty quantification.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Symbolic regression can scale to real-world scientific datasets with non-trivial distributions and tight uncertainty requirements, extending its practical reach well beyond toy benchmarks.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By automating background modeling for resonance searches at the LHC, SymbolFit removes a major manual bottleneck in new physics discovery pipelines, potentially accelerating the search for particles and phenomena beyond the Standard Model.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions include two-dimensional fitting and signal-plus-background joint modeling; the full framework is open-source and the paper is available at [arXiv:2411.09851](https://arxiv.org/abs/2411.09851).</span></div></div>
</div>
