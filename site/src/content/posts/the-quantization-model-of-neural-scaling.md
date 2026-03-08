---
abstract: We propose the Quantization Model of neural scaling laws, explaining both
  the observed power law dropoff of loss with model and data size, and also the sudden
  emergence of new capabilities with scale. We derive this model from what we call
  the Quantization Hypothesis, where network knowledge and skills are "quantized"
  into discrete chunks ($\textbf{quanta}$). We show that when quanta are learned in
  order of decreasing use frequency, then a power law in use frequencies explains
  observed power law scaling of loss. We validate this prediction on toy datasets,
  then study how scaling curves decompose for large language models. Using language
  model gradients, we automatically decompose model behavior into a diverse set of
  skills (quanta). We tentatively find that the frequency at which these quanta are
  used in the training distribution roughly follows a power law corresponding with
  the empirical scaling exponent for language models, a prediction of our theory.
arxivId: '2303.13506'
arxivUrl: https://arxiv.org/abs/2303.13506
authors:
- Eric J. Michaud
- Ziming Liu
- Uzay Girit
- Max Tegmark
concepts:
- scalability
- neural scaling laws
- knowledge quantization
- emergent capabilities
- interpretability
- clustering
- sparse models
- transformers
- stochastic processes
- loss function design
figures:
- /iaifi-research-blog/figures/2303_13506/figure_1.png
- /iaifi-research-blog/figures/2303_13506/figure_1.png
- /iaifi-research-blog/figures/2303_13506/figure_2.png
- /iaifi-research-blog/figures/2303_13506/figure_2.png
- /iaifi-research-blog/figures/2303_13506/figure_3.png
- /iaifi-research-blog/figures/2303_13506/figure_3.png
pdfUrl: https://arxiv.org/pdf/2303.13506v3
published: '2023-03-23T17:58:43+00:00'
theme: Foundational AI
title: The Quantization Model of Neural Scaling
wordCount: 1274
---

## The Big Picture

Every few months, a new and more powerful AI language model arrives, and researchers scramble to explain why it can suddenly do things its predecessor couldn't. GPT-4 could write working code. Earlier models couldn't. Somewhere between "small" and "large," something clicked. Here's the puzzle: if you plot overall performance against model size, the curve is perfectly smooth, following what mathematicians call a power law. Each doubling of model size produces the same proportional improvement, no surprises.

This apparent contradiction has haunted AI researchers for years. Scale a model up, and its overall error rate falls predictably, almost boringly. Yet zoom in on specific skills (solving math problems, translating rare languages, understanding scientific papers) and you see discrete jumps. Capabilities appear seemingly out of nowhere, as if a switch got flipped. The two pictures look nothing alike, and nobody had a unified explanation covering both.

A team at MIT and IAIFI now has one. In a paper published at NeurIPS 2023, Eric Michaud, Ziming Liu, Uzay Girit, and Max Tegmark propose the **Quantization Model** of neural scaling, a theoretical framework that derives both the smooth power law and sudden emergence from a single set of assumptions about how knowledge is structured inside neural networks.

> **Key Insight:** Neural networks don't learn continuously. They learn in discrete chunks, called *quanta*, each representing one indivisible skill or fact. The smooth scaling law we observe is just an average over countless tiny discrete jumps, and "emergent abilities" are what individual quanta look like up close.

## How It Works

The central idea is simple. Michaud and colleagues propose the **Quantization Hypothesis**: the knowledge required to predict text decomposes into a large number of discrete, indivisible units called quanta. You either have a given quantum or you don't. Examples include:

- Incrementing a numbered list
- Continuing a hex color code sequence
- Recognizing the syntactic pattern of a legal citation
- Predicting line breaks in fixed-width text formats

Not all quanta are equally useful. Some appear constantly in text (basic grammar); others appear rarely (formatting a specific chemical equation). When you rank all quanta by frequency of use, the distribution follows a **Zipf/power law**: the most common skill is used twice as often as the second most common, three times as often as the third. It's the same statistical pattern that governs word frequencies, city sizes, and income distributions.

From this, the researchers derive a prediction: if models learn quanta in order of decreasing frequency, and those frequencies follow a power law, then the model's overall error rate should also fall as a power law with model size. Smooth scaling emerges not because learning is continuous, but because you're averaging over thousands of discrete on/off events of varying magnitude. The illusion of a smooth curve works the same way that water flows smoothly through a pipe while being composed of billions of individual bouncing molecules.

![Figure 1](/iaifi-research-blog/figures/2303_13506/figure_1.png)

The team validates this on carefully constructed toy datasets where the ground truth is known, synthetic text distributions where each skill is explicitly defined. Models learn quanta one by one in frequency order, and the resulting scaling curves match theoretical predictions.

![Figure 2](/iaifi-research-blog/figures/2303_13506/figure_1.png)

Then they turn to real language models. To study how scaling decomposes for actual LLMs, they develop a method for **automatically discovering quanta** using model gradients, the mathematical signals that tell a network which way to adjust its weights during training. The core insight is that training samples producing similar gradient updates likely require the same underlying skill. By clustering gradient similarities across a large sample of text, the team partitions model behavior into coherent groups, each cluster a candidate quantum.

## Why It Matters

The clusters are revealing. One groups texts where the model's job is to increment a numbered list, whether of song titles, legal clauses, or book chapters. Another captures the task of predicting line breaks in fixed-width formats across wildly different content. These quanta are genuinely **universal**: the same computational skill applies across many superficially different contexts, exactly as the theory predicts.

![Figure 4](/iaifi-research-blog/figures/2303_13506/figure_2.png)

The team then asks whether the discovered quanta obey the predicted frequency distribution. The answer: yes. The frequency at which auto-discovered skill clusters appear in training data roughly follows a power law, with an exponent matching the empirical scaling exponent for language models. The circle closes. The same Zipfian structure in skill frequencies that the theory requires to produce power law scaling is actually present in the data these models train on.

This has implications beyond explaining a single phenomenon. If skills are discrete and enumerable, we could in principle catalog them, understanding what a model "knows" in a structured way rather than treating it as an inscrutable black box.

The work connects to **mechanistic interpretability**: the project of reverse-engineering the step-by-step procedures neural networks have learned to execute. If knowledge is modular and universal, understanding large models becomes tractable in a way it wouldn't be if everything were an undifferentiated blur.

The conceptual move here is worth pausing on. Borrowing from Max Planck's 1900 insight that energy comes in discrete chunks (which launched quantum mechanics), the authors apply the same quantization logic to knowledge. Both cases involve explaining smooth macroscopic behavior through an underlying discrete structure. The tools of statistical physics, power law distributions and their consequences, turn out to be exactly the right language for understanding what happens inside neural networks as they scale.

> **Bottom Line:** The Quantization Model unifies two of the most puzzling features of modern AI scaling, smooth power laws and sudden emergent abilities, by showing that both follow from a Zipf-distributed collection of discrete skills that models learn one by one. It's a physics-style theory of how AI minds are built.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work imports the conceptual machinery of quantum physics (discretization, universality, power law statistics) into the theory of neural network scaling, applying physics thinking to advance AI understanding.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The Quantization Model provides a unified theoretical explanation for both smooth scaling laws and emergent abilities, and introduces a practical gradient-based method for automatically discovering discrete skills inside language models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By showing that Zipfian distributions in skill frequencies produce power law scaling, the work ties statistical physics and information theory to the empirical behavior of large-scale machine learning systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could use this framework to predict which capabilities will emerge at specific model scales before training, and to design more interpretable architectures; the paper is available at [arXiv:2303.13506](https://arxiv.org/abs/2303.13506).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">The Quantization Model of Neural Scaling</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2303.13506</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Eric J. Michaud", "Ziming Liu", "Uzay Girit", "Max Tegmark"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We propose the Quantization Model of neural scaling laws, explaining both the observed power law dropoff of loss with model and data size, and also the sudden emergence of new capabilities with scale. We derive this model from what we call the Quantization Hypothesis, where network knowledge and skills are "quantized" into discrete chunks ($\textbf{quanta}$). We show that when quanta are learned in order of decreasing use frequency, then a power law in use frequencies explains observed power law scaling of loss. We validate this prediction on toy datasets, then study how scaling curves decompose for large language models. Using language model gradients, we automatically decompose model behavior into a diverse set of skills (quanta). We tentatively find that the frequency at which these quanta are used in the training distribution roughly follows a power law corresponding with the empirical scaling exponent for language models, a prediction of our theory.</span></div></div>
</div>
