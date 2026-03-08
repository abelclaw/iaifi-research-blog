---
abstract: State-of-the-art (SOTA) semi-supervised learning (SSL) methods have been
  highly successful in leveraging a mix of labeled and unlabeled data by combining
  techniques of consistency regularization and pseudo-labeling. During pseudo-labeling,
  the model's predictions on unlabeled data are used for training and thus, model
  calibration is important in mitigating confirmation bias. Yet, many SOTA methods
  are optimized for model performance, with little focus directed to improve model
  calibration. In this work, we empirically demonstrate that model calibration is
  strongly correlated with model performance and propose to improve calibration via
  approximate Bayesian techniques. We introduce a family of new SSL models that optimizes
  for calibration and demonstrate their effectiveness across standard vision benchmarks
  of CIFAR-10, CIFAR-100 and ImageNet, giving up to 15.9% improvement in test accuracy.
  Furthermore, we also demonstrate their effectiveness in additional realistic and
  challenging problems, such as class-imbalanced datasets and in photonics science.
arxivId: '2210.04783'
arxivUrl: https://arxiv.org/abs/2210.04783
authors:
- Charlotte Loh
- Rumen Dangovski
- Shivchander Sudalairaj
- Seungwook Han
- Ligong Han
- Leonid Karlinsky
- Marin Soljacic
- Akash Srivastava
concepts:
- semi-supervised learning
- calibration
- pseudo-labeling
- uncertainty quantification
- bayesian inference
- confirmation bias mitigation
- ensemble methods
- data augmentation
- representation learning
- classification
- self-supervised learning
figures:
- /iaifi-research-blog/figures/2210_04783/figure_1.png
- /iaifi-research-blog/figures/2210_04783/figure_1.png
- /iaifi-research-blog/figures/2210_04783/figure_2.png
- /iaifi-research-blog/figures/2210_04783/figure_2.png
- /iaifi-research-blog/figures/2210_04783/figure_3.png
- /iaifi-research-blog/figures/2210_04783/figure_3.png
pdfUrl: https://arxiv.org/pdf/2210.04783v1
published: '2022-10-10T15:41:44+00:00'
theme: Theoretical Physics
title: On the Importance of Calibration in Semi-supervised Learning
wordCount: 986
---

## The Big Picture

Imagine you're a student learning from a mix of textbook problems with answer keys and a massive pile of practice problems with no answers. The smart strategy: attempt the unlabeled problems, check your confidence, and use your best guesses to keep learning. But if you're wildly overconfident in your wrong answers, you'll drill the mistakes into memory and get worse over time. That's the trap modern AI systems fall into, and the fix has been hiding in plain sight.

**Semi-supervised learning (SSL)** is one of the most practical areas in AI research. Labeled data is expensive and scarce (think of the cost of having expert radiologists annotate thousands of medical scans). Unlabeled data, by contrast, is everywhere. SSL methods try to have it both ways: train on a small labeled set while extracting signal from a vast unlabeled pool.

The dominant approach works in two stages. First, **pseudo-labeling**: the model generates its own guesses for unlabeled examples and uses them as training data. Second, **consistency regularization**: slightly different versions of the same input, say a photo rotated or brightened differently, should still yield the same prediction.

The problem is that these methods can spiral. When a model generates wrong pseudo-labels with high confidence, it trains itself to be even more wrong, a phenomenon researchers call **confirmation bias**. Most state-of-the-art SSL systems have had no principled defense against it. This team from MIT and the MIT-IBM Watson AI Lab shows that better-calibrated confidence is the answer, and that probability-based modeling techniques deliver it.

> **Key Insight:** A model's calibration (how well its confidence matches its actual accuracy) is strongly correlated with its final performance in semi-supervised learning, and improving calibration through approximate Bayesian methods yields up to 15.9% gains in test accuracy.

## How It Works

**Model calibration** is the alignment between a model's stated confidence and its real accuracy: a well-calibrated model that says "I'm 80% sure" should be right about 80% of the time. The researchers analyze two leading SSL families: threshold-mediated methods like **FixMatch** (which only accepts pseudo-labels above a confidence threshold) and representation-learning methods like **PAWS** (which learns visual features before fine-tuning on labels). Both use indirect tricks to maintain calibration, but neither was designed with calibration as an explicit goal.

![Figure 1](/iaifi-research-blog/figures/2210_04783/figure_1.png)

The core finding: calibration during training predicts final performance. Models that stay well-calibrated throughout the pseudo-labeling process end up more accurate. So instead of engineering ever-more-clever confidence thresholds after the fact, why not improve how the model quantifies its own uncertainty?

The proposed fix draws on **approximate Bayesian inference**, techniques that average over many plausible weight configurations rather than finding one "best" set of model weights. A single confident neural network can overfit to its mistakes. But a committee of slightly different networks, each trained with a bit of randomness, is far less likely to all agree on the same wrong answer. The researchers explore two concrete implementations:

- **Bayesian neural networks (BNNs)** using variational inference, representing each model weight as a probability distribution rather than a single number, capturing uncertainty directly in the model's parameters
- **Weight-averaging techniques** (specifically Stochastic Weight Averaging, or SWA), averaging model snapshots taken throughout training to mimic running many slightly different models simultaneously

Both slot into existing SSL frameworks as modular upgrades. FixMatch and PAWS get Bayesian-enhanced variants, dubbed BayFixMatch and BayPAWS.

![Figure 2](/iaifi-research-blog/figures/2210_04783/figure_1.png)

On CIFAR-10 with only 40 labeled examples, BayFixMatch achieves up to 15.9% higher test accuracy than the standard FixMatch baseline. Across CIFAR-100 and ImageNet experiments, the improvements hold: better calibration reliably translates into better classification. The gains come not from architectural changes or more compute, but purely from improved uncertainty quantification.

## Why It Matters

The team puts their approach to a harder test: a real-world **photonics** problem, designing nanoscale structures for manipulating light, where labeled examples are scarce because simulations are expensive. The class distribution is severely imbalanced, which notoriously breaks SSL methods that assume all categories are equally common. The Bayesian methods handle this gracefully, maintaining calibration even when some classes have only a handful of examples.

![Figure 3](/iaifi-research-blog/figures/2210_04783/figure_2.png)

There's a broader principle here. Whenever a learning system relies on its own predictions as training signal (and that increasingly describes much of modern AI), calibration isn't a secondary concern. It's load-bearing. A model that doesn't know what it doesn't know can't improve reliably.

The Bayesian framing provides generalization bounds, giving the approach mathematical backing beyond empirical results. But open questions remain. Approximate Bayesian methods add computational overhead, and the tradeoff between calibration quality and training cost is still being mapped. Scaling to the largest modern models is an active area of research, and distribution shift (when test data looks fundamentally different from training data) is exactly the scenario where miscalibration tends to be worst.

> **Bottom Line:** By treating model calibration as a first-class objective and using Bayesian averaging to achieve it, this work unlocks substantial accuracy gains in semi-supervised learning, showing that knowing what you don't know is just as important as knowing what you do.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects fundamental Bayesian inference theory, a probabilistic framework rooted in mathematics and physics, to the practical challenge of training AI on scarce labeled data, validated on a real photonics design problem.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Showing that calibration causally drives performance in semi-supervised learning reframes how SSL systems should be designed, with Bayesian model averaging delivering up to 15.9% accuracy improvements over state-of-the-art baselines.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The photonics application shows that better-calibrated AI can reliably learn from limited experimental data in physical science domains, opening a path to more trustworthy AI-assisted design of optical and electromagnetic devices.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will explore scaling Bayesian calibration techniques to larger architectures and more extreme label-scarcity regimes; the paper is available at [arXiv:2210.04783](https://arxiv.org/abs/2210.04783) as part of ongoing MIT-IBM Watson AI Lab research.</span></div></div>
</div>
