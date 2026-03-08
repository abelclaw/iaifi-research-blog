---
abstract: 'A core challenge for both physics and artificial intellicence (AI) is symbolic
  regression: finding a symbolic expression that matches data from an unknown function.
  Although this problem is likely to be NP-hard in principle, functions of practical
  interest often exhibit symmetries, separability, compositionality and other simplifying
  properties. In this spirit, we develop a recursive multidimensional symbolic regression
  algorithm that combines neural network fitting with a suite of physics-inspired
  techniques. We apply it to 100 equations from the Feynman Lectures on Physics, and
  it discovers all of them, while previous publicly available software cracks only
  71; for a more difficult test set, we improve the state of the art success rate
  from 15% to 90%.'
arxivId: '1905.11481'
arxivUrl: https://arxiv.org/abs/1905.11481
authors:
- Silviu-Marian Udrescu
- Max Tegmark
concepts:
- regression
- symmetry preservation
- separability detection
- physics-informed neural networks
- automated discovery
- recursive decomposition
- interpretability
- compositionality
- inverse problems
- dimensionality reduction
- sparse models
figures:
- /iaifi-research-blog/figures/1905_11481/figure_1.png
- /iaifi-research-blog/figures/1905_11481/figure_1.png
- /iaifi-research-blog/figures/1905_11481/figure_2.png
- /iaifi-research-blog/figures/1905_11481/figure_2.png
- /iaifi-research-blog/figures/1905_11481/figure_3.png
- /iaifi-research-blog/figures/1905_11481/figure_3.png
pdfUrl: https://arxiv.org/pdf/1905.11481v2
published: '2019-05-27T20:03:57+00:00'
theme: Foundational AI
title: 'AI Feynman: a Physics-Inspired Method for Symbolic Regression'
wordCount: 1091
---

## The Big Picture

Johannes Kepler spent four years and made 40 failed attempts before he realized that Mars traces an ellipse around the sun. He had the data — precise astronomical tables compiled by Tycho Brahe — but extracting the underlying equation from raw numbers was brutally hard. Today, scientists face the same challenge millions of times over, staring at experimental data and asking: what formula is hiding in here?

This is **symbolic regression** — the task of discovering a mathematical expression that exactly matches a dataset. Not just a curve that fits the data, but the actual equation, written in symbols, that could appear in a textbook. It's fundamentally different from what most machine learning does.

A neural network that predicts planetary positions with 99.9% accuracy is useful. But it doesn't tell you the orbit is an ellipse. Kepler's law, written in four symbols, does.

The trouble is that the space of possible mathematical expressions grows exponentially with length — there are more candidate formulas than atoms in the observable universe. No brute-force approach could ever work. Researchers at MIT, led by Silviu-Marian Udrescu and Max Tegmark, took a different approach: instead of searching blindly through that exponential space, they asked what physicists know about how equations tend to behave, and built those insights directly into an algorithm called **AI Feynman**.

> **Key Insight:** By embedding physics-inspired heuristics — symmetry detection, dimensional analysis, separability — into a recursive neural network framework, AI Feynman discovered all 100 equations from the Feynman Lectures on Physics and improved the state-of-the-art success rate on a harder benchmark from 15% to 90%.

## How It Works

The core observation driving AI Feynman is that the equations physicists care about aren't random. They have structure. They respect units. They decompose into simpler pieces. They exhibit symmetry. AI Feynman encodes six such properties into a recursive algorithm that chips away at complex equations by exploiting whichever simplifications apply.

![Figure 1](/iaifi-research-blog/figures/1905_11481/figure_1.png)

The algorithm works like this:

1. **Dimensional analysis** first. If the variables have known physical units, the algorithm applies the Buckingham Pi theorem — a rule from physics that lets you combine variables into unit-free ratios — reducing the number of independent variables you need to track. Newton's law of gravity, with 9 variables, can collapse to 6 such ratios. Fewer variables means a dramatically simpler search.

2. **Neural network fitting** is the algorithmic workhorse. A feedforward neural network — one that processes inputs in a single pass from input to output — is trained on the mystery data. The network itself isn't the answer; it's a probe. Once trained, the algorithm uses it to test for hidden structure.

3. **Symmetry detection** uses the trained network to check whether the function remains unchanged when variables are shifted or scaled. If adding a constant to $x_3$ doesn't change the output, then $x_3$ only appears in the formula as part of a difference — and one variable disappears. This kind of **translational symmetry** detection can recursively strip variables from the problem.

4. **Separability** detection checks whether the function factors into a product or sum of two parts with no shared variables. If $f(x_1, x_2, x_3) = g(x_1) \cdot h(x_2, x_3)$, the problem splits in two. The algorithm tests this by checking whether the network's partial derivatives — measures of how the output changes when each input is nudged independently — respect a factored structure.

5. **Polynomial fitting** handles the case where the function (or a simplified sub-function) is a polynomial. This reduces to solving a linear system: fast and exact.

6. **Brute-force symbolic search** is the last resort for small, simple sub-expressions: try all formulas up to some length using a library of elementary functions.

![Figure 2](/iaifi-research-blog/figures/1905_11481/figure_1.png)

Newton's gravitational law illustrates how these steps chain together. Starting with 9 variables, dimensional analysis reduces the problem to 6 unit-free combinations. The neural network then detects two translational symmetries — the force depends only on differences of coordinates, not absolute positions — dropping the count to 4 variables.

Multiplicative separability then splits the 4-variable problem into two smaller ones. Each gets solved independently: one by polynomial fitting after a simple inversion. The original 9-variable mystery is cracked without ever searching through formulas with 9 arguments.

## Why It Matters

The immediate result is striking. AI Feynman recovers all 100 equations from the Feynman Lectures on Physics. The previous best publicly available software — Eureqa, based on genetic algorithms and widely regarded as the gold standard — found only 71. On a harder test set of physics-based equations, the gap widens further: 90% success versus 15%. These aren't marginal improvements; they represent a qualitative change in capability.

The deeper significance is methodological. AI Feynman demonstrates that the right way to bring AI into physics isn't to throw a generic optimizer at the problem and hope it converges. It's to encode what physicists already know — that real equations have units, symmetries, and compositional structure — and let the AI search within that constrained, meaningful space.

Neural networks here serve not as black-box predictors but as scientific instruments for detecting hidden structure in data. This is a template for a broader collaboration: human-encoded physical intuition guiding AI-powered search. The approach points toward automating scientific discovery in materials science, biology, and anywhere that underlying laws might be compact and structured, even when we don't yet know what they are.

> **Bottom Line:** AI Feynman doesn't just fit data better — it *understands* equations, using physics-inspired tricks to recursively decompose hard symbolic regression problems into solvable pieces, achieving a 6x improvement over previous methods on challenging benchmarks.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">AI Feynman directly bridges machine learning and theoretical physics by encoding symmetry, dimensional analysis, and separability — core concepts from physics — into a neural network-guided symbolic regression engine that recovers real physics equations from data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work establishes a new paradigm for symbolic regression, improving success rates from 15% to 90% on hard benchmarks by replacing brute-force search with physics-inspired recursive decomposition guided by neural network probes.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By automatically rediscovering equations from the Feynman Lectures — including multi-variable laws like Newton's gravitation — the method demonstrates a concrete path toward machine-assisted discovery of physical laws from experimental data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions include handling noisy data, larger equation spaces, and applications to open problems where governing equations remain unknown; the work was published in *Science Advances* (2020) and the AI Feynman benchmark dataset is publicly available.</span></div></div>
</div>
