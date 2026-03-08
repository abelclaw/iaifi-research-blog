---
abstract: We study the minimal error of the Empirical Risk Minimization (ERM) procedure
  in the task of regression, both in the random and the fixed design settings. Our
  sharp lower bounds shed light on the possibility (or impossibility) of adapting
  to simplicity of the model generating the data. In the fixed design setting, we
  show that the error is governed by the global complexity of the entire class. In
  contrast, in random design, ERM may only adapt to simpler models if the local neighborhoods
  around the regression function are nearly as complex as the class itself, a somewhat
  counter-intuitive conclusion. We provide sharp lower bounds for performance of ERM
  for both Donsker and non-Donsker classes. We also discuss our results through the
  lens of recent studies on interpolation in overparameterized models.
arxivId: '2102.12066'
arxivUrl: https://arxiv.org/abs/2102.12066
authors:
- Gil Kur
- Alexander Rakhlin
concepts:
- empirical risk minimization
- regression
- local complexity
- minimax lower bounds
- overparameterized models
- stochastic processes
- sparse models
- robustness
- loss function design
- kernel methods
figures: []
pdfUrl: https://arxiv.org/pdf/2102.12066v1
published: '2021-02-24T04:47:55+00:00'
theme: Foundational AI
title: On the Minimal Error of Empirical Risk Minimization
wordCount: 1004
---

## The Big Picture

Imagine trying to find your keys in a messy house. You could search only the bedroom — the "simple" model — or ransack every room at once. The question is: does a whole-house search automatically zero in on the bedroom answer, or does the mess of the entire house contaminate your results?

This is the puzzle at the heart of one of machine learning's most fundamental questions.

Modern AI relies on a deceptively simple idea: **Empirical Risk Minimization (ERM)** — find the rule that best fits your training data. In practice, AI systems are trained on enormous, flexible collections of possible rules — far richer than the true underlying pattern requires. The hope is that the learning procedure will automatically "adapt," recognizing when the data comes from something simple and landing on a solution competitive with that simpler rule, not the bloated whole collection.

This hope undergirds much of deep learning's success story. But is it justified?

Researchers Gil Kur and Alexander Rakhlin at MIT have delivered a rigorous, sometimes jarring answer: adaptation is far more fragile than the machine learning community has assumed. The conditions under which it occurs reveal something deep and counterintuitive about how ERM actually behaves.

> **Key Insight:** ERM's ability to adapt to simple underlying models depends not on the simplicity of the true model itself, but on whether the *neighborhood* surrounding that model is complex — a finding that reframes how we should think about generalization in models trained with far more adjustable parameters than the problem strictly requires.

## How It Works

The setup is clean. You have a large, flexible **function class** F — the full menu of models your learner can choose from. Somewhere inside F sits a much smaller, simpler class H containing the true data-generating function f₀. ERM minimizes squared error over F. The question: does prediction error scale with the complexity of H or of F?

The paper attacks this with **sharp lower bounds** — mathematical proofs that ERM *cannot* beat a certain error rate, no matter what. This is harder than proving upper bounds, because you must show that no clever tie-breaking rule or solution selection can escape the trap.

The analysis splits into two settings that behave very differently:

- **Fixed design:** Training points are fixed in advance, not drawn randomly. The verdict is unforgiving — ERM's error is governed by the **global complexity** of the entire class F, period. Even if f₀ is maximally simple within F, ERM cannot escape F's shadow. Adaptivity is impossible.
- **Random design:** Training points are drawn independently and at random from some distribution. Here the story gets subtle. ERM *can* sometimes adapt to the simplicity of f₀ — but only under a surprising condition.

The key technical tool is the **Gaussian average** — a measure of how wildly a function class fluctuates under random noise. For a function class G evaluated at n points, this captures the typical maximum spread of outputs when each is nudged by an independent random signal. The larger this quantity, the richer and more unruly the class. The paper characterizes ERM's error precisely in terms of these complexity measures, evaluated both globally over F and locally in small neighborhoods around f₀.

The counterintuitive punchline for random design: ERM adapts to the simpler model f₀ *only if the local neighborhood of f₀ in F is itself nearly as complex as F globally*. If f₀ sits in a "quiet corner" — a region of low local complexity — ERM actually performs *worse*, not better. The optimizer gets pulled toward solutions far from f₀ in out-of-sample loss, precisely because those distant, complex solutions better explain the training data.

These results hold for both **Donsker classes** (function classes tame enough that their statistical behavior stabilizes predictably as more data arrives, so the empirical process converges uniformly) and **non-Donsker classes** (rougher classes where that stabilization never fully arrives), making the findings broadly applicable.

## Why It Matters

The most immediate connection is to **benign overfitting** in overparameterized models — AI systems with far more adjustable parameters than the problem strictly requires. Recent work by Belkin, Bartlett, and others showed that perfectly fitting noisy training data doesn't necessarily destroy generalization. Kur and Rakhlin's framework illuminates why: interpolating models often live in function classes with rich local neighborhoods everywhere, so ERM's pull toward complex solutions still lands near the truth. There is no quiet corner to fall into.

The "double descent" curve and benign overfitting aren't magic — they're manifestations of the local-complexity structure this paper formalizes.

The work also directly challenges a quiet assumption in deep learning: that bigger models automatically adapt to simpler data. The lower bounds here show adaptation is not generic. It requires specific structural conditions on the function class — conditions that may or may not hold for neural networks in practice. Understanding when neural network architectures satisfy the "rich local neighborhoods" condition could become a central question for theorists trying to explain empirical generalization.

> **Bottom Line:** ERM's adaptivity to simple models is an exception, not a rule — it works only when the model's neighborhood is itself complex. This precise result reframes decades of intuition about overfitting, regularization, and generalization.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies rigorous statistical learning theory to clarify the foundations of overparameterized model training, bridging mathematical analysis of function class geometry with practical questions about modern deep learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The sharp lower bounds establish fundamental limits on ERM's adaptivity, directly informing when practitioners can trust large overparameterized models to generalize to simpler underlying structure.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The theoretical framework has direct implications for physics-informed machine learning, where large neural architectures are routinely used to fit data generated by simpler physical laws.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work should characterize which neural network architectures satisfy the rich-local-neighborhood conditions identified here; the paper is available on arXiv and represents ongoing work from MIT's learning theory group by Kur and Rakhlin.</span></div></div>
</div>
