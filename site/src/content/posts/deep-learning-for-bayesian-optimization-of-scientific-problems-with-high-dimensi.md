---
abstract: Bayesian optimization (BO) is a popular paradigm for global optimization
  of expensive black-box functions, but there are many domains where the function
  is not completely a black-box. The data may have some known structure (e.g. symmetries)
  and/or the data generation process may be a composite process that yields useful
  intermediate or auxiliary information in addition to the value of the optimization
  objective. However, surrogate models traditionally employed in BO, such as Gaussian
  Processes (GPs), scale poorly with dataset size and do not easily accommodate known
  structure. Instead, we use Bayesian neural networks, a class of scalable and flexible
  surrogate models with inductive biases, to extend BO to complex, structured problems
  with high dimensionality. We demonstrate BO on a number of realistic problems in
  physics and chemistry, including topology optimization of photonic crystal materials
  using convolutional neural networks, and chemical property optimization of molecules
  using graph neural networks. On these complex tasks, we show that neural networks
  often outperform GPs as surrogate models for BO in terms of both sampling efficiency
  and computational cost.
arxivId: '2104.11667'
arxivUrl: https://arxiv.org/abs/2104.11667
authors:
- Samuel Kim
- Peter Y. Lu
- Charlotte Loh
- Jamie Smith
- Jasper Snoek
- Marin Soljačić
concepts:
- bayesian optimization
- surrogate modeling
- bayesian inference
- uncertainty quantification
- active learning
- experimental design
- graph neural networks
- convolutional networks
- scalability
- auxiliary signal modeling
- materials discovery
- kernel methods
- inverse problems
figures:
- /iaifi-research-blog/figures/2104_11667/figure_1.png
- /iaifi-research-blog/figures/2104_11667/figure_1.png
- /iaifi-research-blog/figures/2104_11667/figure_2.png
- /iaifi-research-blog/figures/2104_11667/figure_2.png
- /iaifi-research-blog/figures/2104_11667/figure_3.png
- /iaifi-research-blog/figures/2104_11667/figure_3.png
pdfUrl: https://arxiv.org/pdf/2104.11667v4
published: '2021-04-23T15:46:37+00:00'
theme: Foundational AI
title: Deep Learning for Bayesian Optimization of Scientific Problems with High-Dimensional
  Structure
wordCount: 960
---

## The Big Picture

Imagine designing the perfect light-manipulating material — a so-called *photonic crystal*, engineered at a scale far smaller than a human hair to control which frequencies of light it blocks or transmits. You can't test every possible arrangement; each simulation takes hours to run. You need to be smart about which designs to evaluate next. This is Bayesian optimization: using what you've already learned to make educated guesses about where the best answer lies, minimizing expensive experiments.

Scientists have long relied on **Gaussian Processes (GPs)** to guide this search. Think of a GP as a principled bookkeeper: it tracks not just its best guess about any untested design, but also its confidence in that guess. That built-in uncertainty estimate is what makes the search smart — it helps the algorithm decide whether to dig deeper into a promising area or venture somewhere entirely new.

But GPs have a serious problem: they slow to a crawl as inputs grow complex. Design a molecule? GPs struggle. Optimize an image-like grid of material? GPs choke. The more variables you're juggling, and the more structure in your data, the worse they perform — in both accuracy and speed.

Researchers from MIT and Google Research have now shown a better path: replace the GP with a **Bayesian neural network** purpose-built to understand the structure of your data. The result is a Bayesian optimization engine that handles molecules, images, and high-dimensional physical problems with far greater efficiency.

> **Key Insight:** By using Bayesian neural networks — which can encode physical symmetries and structural knowledge — as surrogate models, researchers can run smarter scientific searches in regimes where traditional Gaussian Processes simply can't compete.

## How It Works

At the heart of any Bayesian optimization loop is the **surrogate model**: a learned function that predicts how good an untested design will be, along with an estimate of uncertainty. That uncertainty is crucial — it tells the optimizer whether to *exploit* a promising region or *explore* somewhere new.

Traditional GPs compute uncertainty analytically, but at steep cost: computation scales with the cube of the number of data points. A few hundred experiments? Manageable. A few thousand? Painful. And when inputs are images or molecular graphs rather than simple numerical vectors, you'd need to hand-engineer a custom kernel function for every new domain — slow, expert work.

![Figure 1](/iaifi-research-blog/figures/2104_11667/figure_1.png)

Instead, the team turns to **Bayesian neural networks (BNNs)**, which approximate uncertainty through **Monte Carlo dropout** — randomly disabling neurons during prediction to produce a spread of possible answers that collectively stand in for uncertainty. The key advantage: any neural network architecture can serve as the surrogate. Convolutional neural networks for image-like inputs. Graph neural networks for molecules. The architecture naturally encodes the structure of the problem.

The framework tackles two especially important scenarios:

- **High-dimensional observations:** When an experiment produces rich output — like the full optical scattering spectrum of a nanoparticle across hundreds of wavelengths — the BNN predicts the entire spectrum, then computes the optimization target from it. This auxiliary information dramatically improves accuracy compared to predicting a single number.
- **Structured input spaces:** For photonic crystal design, the input is a binary image; a convolutional neural network processes this naturally. For molecular design, each molecule is a graph of atoms and bonds — perfect territory for a graph neural network.

![Figure 2](/iaifi-research-blog/figures/2104_11667/figure_1.png)

On the photonic crystal task, the goal was to maximize photonic bandgap — the range of light frequencies the material blocks. The GP surrogate, faced with an image-like input, performed poorly. The CNN-based BNN found significantly better crystal designs in the same number of evaluations.

For molecule optimization, the team worked with the **QM9 dataset**, a widely used reference library of small organic molecules with precisely calculated physical and chemical properties. Using a graph neural network surrogate, the BNN-based optimizer consistently found higher-quality molecules faster than the GP baseline — at a fraction of the computational cost.

![Figure 3](/iaifi-research-blog/figures/2104_11667/figure_2.png)

## Why It Matters

Scientific optimization problems — drug discovery, materials design, optical engineering, nuclear physics simulations — share a common structure: each evaluation is costly, the input space is complex, and there's structure the optimizer could exploit if its surrogate understood it. GPs were the best available tool for decades, but they were designed for a simpler world.

This work demonstrates that the deep learning revolution isn't just about making predictions — it's about making *better decisions*. A BNN that understands molecular graphs doesn't just predict properties; it enables an entire optimization loop to run in domains previously out of reach. As neural architectures continue to improve — equivariant networks, transformers, physics-informed models — the surrogates plugged into this framework will only get more powerful. The approach extends naturally to settings with multiple competing objectives or hard physical constraints.

> **Bottom Line:** Replacing Gaussian Processes with domain-aware Bayesian neural networks unlocks Bayesian optimization for the complex, high-dimensional, structured problems that arise in real science — and does so while running faster and finding better solutions.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges modern deep learning architectures with the practical demands of scientific discovery, applying graph and convolutional neural networks to real optimization tasks in photonics and quantum chemistry.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The research extends Bayesian optimization to high-dimensional structured domains by using BNNs as flexible, scalable surrogates that encode inductive biases inaccessible to traditional Gaussian Processes.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling efficient topology optimization of photonic crystals and quantum chemistry property optimization, the framework accelerates exploration of materials and molecules with specific, physically meaningful properties.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions could integrate equivariant architectures or multi-objective acquisition functions, broadening applicability across computational science; the work is available on OpenReview at `openreview.net/forum?id=tPMQ6Je2rB`.</span></div></div>
</div>
