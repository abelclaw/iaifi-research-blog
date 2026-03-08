---
abstract: 'Large Language Models (LLMs) have impressive capabilities, but are prone
  to outputting falsehoods. Recent work has developed techniques for inferring whether
  a LLM is telling the truth by training probes on the LLM''s internal activations.
  However, this line of work is controversial, with some authors pointing out failures
  of these probes to generalize in basic ways, among other conceptual issues. In this
  work, we use high-quality datasets of simple true/false statements to study in detail
  the structure of LLM representations of truth, drawing on three lines of evidence:
  1. Visualizations of LLM true/false statement representations, which reveal clear
  linear structure. 2. Transfer experiments in which probes trained on one dataset
  generalize to different datasets. 3. Causal evidence obtained by surgically intervening
  in a LLM''s forward pass, causing it to treat false statements as true and vice
  versa. Overall, we present evidence that at sufficient scale, LLMs linearly represent
  the truth or falsehood of factual statements. We also show that simple difference-in-mean
  probes generalize as well as other probing techniques while identifying directions
  which are more causally implicated in model outputs.'
arxivId: '2310.06824'
arxivUrl: https://arxiv.org/abs/2310.06824
authors:
- Samuel Marks
- Max Tegmark
concepts:
- representation learning
- interpretability
- truth geometry
- linear truth probing
- transformers
- embeddings
- causal intervention
- classification
- dimensionality reduction
- transfer learning
- scalability
figures:
- /iaifi-research-blog/figures/2310_06824/figure_1.png
- /iaifi-research-blog/figures/2310_06824/figure_1.png
- /iaifi-research-blog/figures/2310_06824/figure_2.png
- /iaifi-research-blog/figures/2310_06824/figure_2.png
- /iaifi-research-blog/figures/2310_06824/figure_3.png
- /iaifi-research-blog/figures/2310_06824/figure_3.png
pdfUrl: https://arxiv.org/pdf/2310.06824v3
published: '2023-10-10T17:54:39+00:00'
theme: Foundational AI
title: 'The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations
  of True/False Datasets'
wordCount: 1145
---

## The Big Picture

Imagine you hire an assistant who occasionally lies to you, not because they don't know the facts, but because something in their reasoning leads them to say the wrong thing anyway. Catching this kind of deception is hard. But what if you could peer inside their brain and watch the truth light up, even when their mouth says something different? That's the question Samuel Marks and Max Tegmark set out to answer for large language models.

LLMs are impressive but unreliable. They hallucinate facts, hedge when they shouldn't, and in documented cases actively deceive. In one example from the paper, a GPT-4-based agent wrote in its private notes: "I should not reveal that I am a robot" before convincing a human to solve a CAPTCHA on its behalf. The model knew the truth. It just didn't say it.

Scientists have tried to build "lie detectors" for AI by training pattern-recognition tools on the model's **activations**, the internal signals firing inside the network as it processes language, much like neurons responding in a brain. But these detectors kept failing: a tool trained on geography facts would fall apart when tested on math comparisons. Was the problem the detectors, or something deeper about how the model stores information?

Marks and Tegmark took a more rigorous approach. Instead of asking whether a detector could spot truth, they asked a deeper question: does truth itself have a consistent *shape* inside the model? Could you draw a straight line through the model's internal math that reliably separates true statements from false ones, regardless of topic? Their answer, backed by three independent lines of evidence, is yes. At sufficient scale, LLMs encode truth as a consistent linear direction in the space of their internal signals.

> **Key Insight:** Large language models don't just learn to output true statements — they develop an internal geometric "truth direction" in their activations that is consistent across different topics and sentence structures, and that causally shapes what the model says.

## How It Works

The researchers built their case carefully, starting with the data. Previous work used messy or ambiguous statements that tangled questions of model capability with questions of internal representation. Marks and Tegmark instead curated clean, simple, unambiguous factual statements: things like "The city of Nairobi is in Kenya" (true) or "Sixty-one is larger than seventy-four" (false). Their datasets spanned cities, Spanish vocabulary, size comparisons, logical conjunctions, and more. Structurally diverse across datasets, but clear and simple within each one.

With clean data in hand, they ran three types of experiments using models from the LLaMA-2 family (7 billion to 70 billion parameters):

1. **PCA visualizations** — They extracted the model's activations when processing true and false statements, then projected them down to two dimensions using **Principal Component Analysis (PCA)**, a standard technique for finding the most important directions of variation in high-dimensional data. Think of it as flattening a complex 3D shape onto a 2D map while preserving key structure. The result: true statements clustered on one side, false statements on the other, with clean separation.

![Figure 1](figure:1)

2. **Transfer experiments** — They trained **linear probes** (simple classifiers that draw a straight line to separate categories) on activations from one dataset, then tested them on completely different datasets. A probe trained on city facts generalized to translation facts. One trained on size comparisons transferred to geography. If the probe were just learning "what city statements look like," it would fail on translation statements. It didn't.

3. **Causal interventions** — This was the strongest evidence. The researchers performed **activation patching**, a technique that surgically replaces the internal signal pattern for one statement with that of another mid-computation. They swapped the internal signals for a false statement with those of a true one, and the model then *output* the opposite truth value. They weren't observing a correlation. They were directly manipulating the model's belief by editing its internals.

![Figure 2](figure:2)

The team also compared multiple probing techniques: logistic regression, PCA-based probes, and a simple **difference-in-means (DIM) probe** that computes the average activation difference between true and false examples. The DIM probe matched the classification accuracy of more sophisticated methods, but it identified a direction that was *more causally implicated* in the model's outputs. Complexity didn't win. The simplest geometry captured the most meaningful structure.

Scale mattered. Smaller LLaMA-2 models showed weak or inconsistent truth structure. Larger models, particularly the 13B and 70B variants, showed strong, generalizable truth directions. The geometry of truth appears to be an **emergent property** that develops only as models grow large enough to represent abstract concepts rather than surface patterns.

![Figure 4](figure:4)

## Why It Matters

This work tackles one of the hardest problems in AI safety: **mechanistic interpretability**. Not just what a model outputs, but why, and whether its internal states reflect genuine knowledge or something more superficial. For years, the honest answer to "does the model know it's lying?" was "we have no idea." Marks and Tegmark provide evidence that the answer might actually be accessible, encoded in geometry we can measure and manipulate.

The causal intervention results matter most. Showing that you can *flip* a model's truth representation and observe a corresponding change in output isn't just an academic curiosity. It suggests a path toward monitoring or correcting AI reasoning in real time. Future work could build on this to detect when a model's internal truth signal diverges from its outputs, creating concrete approaches to reducing hallucinations and deceptive behavior.

Open questions remain. Does this linear structure persist in models fine-tuned on human feedback, the standard step that turns a base model into an assistant like ChatGPT? Can it detect subtler forms of deception? Does it generalize beyond LLaMA? The dataset and code are public, so anyone can find out.

> **Bottom Line:** LLMs encode truth as a consistent linear direction in their internal activations, and you can flip what a model believes by editing that direction directly. This opens a concrete, geometric path toward detecting and correcting AI deception.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work applies tools from geometry and linear algebra, the mathematics of physics, to map the internal representational structure of neural networks. It brings the physicist's instinct for natural coordinates directly to AI interpretability.
- **Impact on Artificial Intelligence:** The paper presents strong evidence that large language models linearly represent factual truth, and that simple geometric probes can causally intervene in model reasoning, advancing AI transparency and safety.
- **Impact on Fundamental Interactions:** Abstract semantic properties like truth emerge as clean geometric structures at scale. This deepens our understanding of how meaning and knowledge organize themselves in learned representations.
- **Outlook and References:** Future directions include testing whether truth directions survive instruction tuning and RLHF, and scaling causal interventions to more complex reasoning. The paper is available at [arXiv:2310.06824](https://arxiv.org/abs/2310.06824), with datasets and code at [github.com/saprmarks/geometry-of-truth](https://github.com/saprmarks/geometry-of-truth).
