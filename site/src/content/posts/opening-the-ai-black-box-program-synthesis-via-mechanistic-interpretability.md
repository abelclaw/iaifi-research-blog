---
abstract: 'We present MIPS, a novel method for program synthesis based on automated
  mechanistic interpretability of neural networks trained to perform the desired task,
  auto-distilling the learned algorithm into Python code. We test MIPS on a benchmark
  of 62 algorithmic tasks that can be learned by an RNN and find it highly complementary
  to GPT-4: MIPS solves 32 of them, including 13 that are not solved by GPT-4 (which
  also solves 30). MIPS uses an integer autoencoder to convert the RNN into a finite
  state machine, then applies Boolean or integer symbolic regression to capture the
  learned algorithm. As opposed to large language models, this program synthesis technique
  makes no use of (and is therefore not limited by) human training data such as algorithms
  and code from GitHub. We discuss opportunities and challenges for scaling up this
  approach to make machine-learned models more interpretable and trustworthy.'
arxivId: '2402.05110'
arxivUrl: https://arxiv.org/abs/2402.05110
authors:
- Eric J. Michaud
- Isaac Liao
- Vedang Lad
- Ziming Liu
- Anish Mudide
- Chloe Loughridge
- Zifan Carl Guo
- Tara Rezaei Kheirkhah
- Mateja Vukelić
- Max Tegmark
concepts:
- interpretability
- program synthesis
- mechanistic interpretability
- autoencoders
- recurrent networks
- regression
- finite state machine extraction
- representation learning
- automated discovery
- clustering
- dimensionality reduction
- sparse models
figures:
- /iaifi-research-blog/figures/2402_05110/figure_1.png
- /iaifi-research-blog/figures/2402_05110/figure_1.png
- /iaifi-research-blog/figures/2402_05110/figure_2.png
- /iaifi-research-blog/figures/2402_05110/figure_2.png
- /iaifi-research-blog/figures/2402_05110/figure_3.png
- /iaifi-research-blog/figures/2402_05110/figure_3.png
pdfUrl: https://arxiv.org/pdf/2402.05110v1
published: '2024-02-07T18:59:12+00:00'
theme: Foundational AI
title: 'Opening the AI black box: program synthesis via mechanistic interpretability'
wordCount: 1002
---

## The Big Picture

Imagine hiring a brilliant but completely mute mathematician. She solves every problem you give her — long division, sorting algorithms, pattern matching — with perfect accuracy. But she can't explain her work. She just hands you the answer. You know *that* she solved it; you have no idea *how*.

That's the situation AI researchers face with modern neural networks. These systems learn to perform complex tasks — sometimes better than any human algorithm — but their internal computations remain opaque, trapped inside billions of numbers. The field of **mechanistic interpretability** — figuring out, step by step, what a network is actually doing inside — has emerged to crack this opacity open, mostly through painstaking human analysis. Now, a team at MIT and IAIFI is asking a bolder question: can we automate that process entirely?

Their answer is **MIPS** — **Mechanistic Interpretability-based Program Synthesis** — a system that watches a neural network solve problems, reverse-engineers what it learned, and automatically writes clean Python code that does the same thing. No human interpretation required.

> **Key Insight:** MIPS can look inside a trained neural network, extract the algorithm it discovered, and express it as readable Python code — solving problems that even GPT-4 can't crack, using zero human-written code as training data.

## How It Works

The MIPS pipeline transforms a black-box neural network into human-readable code in four stages.

![Figure 1](/iaifi-research-blog/figures/2402_05110/figure_1.png)

**Stage 1: Train a neural network to learn the task.** MIPS uses a **recurrent neural network (RNN)** — a network that processes sequences by maintaining a running "memory" called a hidden state. The team also runs an **AutoML** search — an automated process that tries thousands of different network designs — to find the *simplest* RNN that achieves perfect accuracy. Simpler networks are easier to reverse-engineer, and the search space spans over 75 million possible configurations.

**Stage 2: Simplify the network.** MIPS prunes and compresses the trained network to remove redundancy, making subsequent analysis cleaner.

**Stage 3: Convert to a finite state machine.** When a network processes discrete inputs — integers, tokens, symbols — its hidden states cluster into groups rather than wandering freely through space. MIPS uses an **integer autoencoder** (a compression tool that describes each cluster using only whole numbers or yes/no flags) to discover that these clusters often sit on a regular, grid-like arrangement. Each point in that grid is one possible "mode" the network can be in. The murky continuous RNN becomes a crisp **finite state machine**: a lookup table mapping state-plus-input to next state.

**Stage 4: Apply symbolic regression.** With a finite state machine in hand, MIPS applies **symbolic regression** — a search for compact mathematical formulas that fit the data — to find the rules governing state transitions. The result is Python code that faithfully implements the algorithm the network discovered on its own.

The team tested MIPS against a benchmark of 62 algorithmic tasks: detecting balanced parentheses, computing modular arithmetic, tracking state through a sequence. They compared it to GPT-4, which tackles the same benchmark by generating code from verbal problem descriptions.

![Figure 2](/iaifi-research-blog/figures/2402_05110/figure_1.png)

- **GPT-4 solved 30 of 62 tasks**
- **MIPS solved 32 of 62 tasks**
- **13 tasks solved by MIPS were *not* solved by GPT-4**
- **11 tasks solved by GPT-4 were *not* solved by MIPS**

They're not just close in score — they're solving *different* problems. GPT-4 draws on vast human-written code to recognize familiar patterns. MIPS uses zero human training data, discovering algorithms from scratch by watching a network think. Combined, the two approaches solve problems that neither could handle alone.

![Figure 3](/iaifi-research-blog/figures/2402_05110/figure_2.png)

## Why It Matters

At its core, MIPS addresses one of the most pressing problems in AI: we increasingly deploy systems we don't understand. A network that performs well on benchmarks may still fail in subtle, dangerous ways when conditions shift — and we usually can't tell why, because we don't know how it worked. Automatically extracting the algorithm a network learned would let us audit it, verify it, and trust it far more completely.

MIPS is a proof of concept that automated interpretability is achievable, at least for small RNNs on well-defined tasks. The authors are candid that scaling to large transformer models — the kind powering today's AI assistants — remains a major challenge. Transformers are vastly more complex, and their hidden states don't cluster as neatly. But the conceptual path is clear: find the right representation, and you can extract the algorithm.

There's also a physics angle that resonates with IAIFI's broader mission. The tools MIPS uses — symbolic regression, sparse representations, minimal descriptions — are the same tools physicists use to discover natural laws from data. The integer autoencoder is essentially finding the "quantum numbers" of the network's internal states: the conserved quantities that characterize its behavior. Treating neural networks as physical systems to be understood, not just engineered, is a distinctly IAIFI way of thinking.

> **Bottom Line:** MIPS proves that neural networks can be reverse-engineered automatically — turned from opaque black boxes into readable code — and solves 13 problems GPT-4 cannot, suggesting that human-free algorithm discovery may be a powerful complement to LLM-based coding.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">MIPS applies physics-inspired tools — symbolic regression, minimal representations, and finite-state abstractions — to AI interpretability, treating neural networks as physical systems whose internal "laws" can be discovered from observation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work demonstrates fully automated mechanistic interpretability at scale, solving 32 of 62 algorithmic benchmark tasks and opening a new path toward auditable, trustworthy AI systems that require no human-written training data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The integer autoencoder technique provides a general framework for discovering discrete, structured representations inside continuous neural networks — a tool with broad applications across scientific machine learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work aims to scale MIPS beyond small RNNs to larger transformer architectures; the paper is available on arXiv (arXiv:2402.05110) and represents a collaboration between MIT CSAIL and the IAIFI.</span></div></div>
</div>
