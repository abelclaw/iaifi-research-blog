---
abstract: We present a new implementation of the LLM-driven genetic algorithm {\it
  funsearch}, whose aim is to generate examples of interest to mathematicians and
  which has already had some success in problems in extremal combinatorics. Our implementation
  is designed to be useful in practice for working mathematicians; it does not require
  expertise in machine learning or access to high-performance computing resources.
  Applying {\it funsearch} to a new problem involves modifying a small segment of
  Python code and selecting a large language model (LLM) from one of many third-party
  providers. We benchmarked our implementation on three different problems, obtaining
  metrics that may inform applications of {\it funsearch} to new problems. Our results
  demonstrate that {\it funsearch} successfully learns in a variety of combinatorial
  and number-theoretic settings, and in some contexts learns principles that generalize
  beyond the problem originally trained on.
arxivId: '2503.11061'
arxivUrl: https://arxiv.org/abs/2503.11061
authors:
- Jordan S. Ellenberg
- Cristofero S. Fraser-Taliente
- Thomas R. Harvey
- Karan Srivastava
- Andrew V. Sutherland
concepts:
- llm-driven genetic algorithm
- automated discovery
- program synthesis
- generative models
- combinatorial optimization
- inverse problems
- scientific workflows
- active learning
- reinforcement learning
- interpretability
figures:
- /iaifi-research-blog/figures/2503_11061/figure_1.png
- /iaifi-research-blog/figures/2503_11061/figure_2.png
- /iaifi-research-blog/figures/2503_11061/figure_3.png
pdfUrl: https://arxiv.org/pdf/2503.11061v2
published: '2025-03-14T03:54:43+00:00'
theme: Foundational AI
title: Generative Modeling for Mathematical Discovery
wordCount: 941
---

## The Big Picture

Mathematics has always been a human endeavor — a story of flashes of insight, years of failed attempts, and the occasional eureka moment scribbled on a napkin at 2 a.m. But what if an AI could sit beside the mathematician, actively *searching* for the examples that make new theorems possible? That's the question at the heart of a new collaboration between researchers at MIT, the University of Wisconsin-Madison, Oxford, and IAIFI.

In many areas of mathematics, the hardest part isn't proving a theorem — it's finding the right example to prove it *about*. In **combinatorics** — the branch of math that studies counting, arrangement, and optimal collections of objects — mathematicians often want to find the largest possible set of numbers with some special property. Checking whether a proposed set works is easy. Finding the best one from scratch is practically impossible, even for powerful computers. It's the difference between verifying a sudoku solution in seconds and solving one from scratch.

This team has built an accessible implementation of **funsearch** — a search technique powered by large language models (LLMs) that evolves candidate solutions using principles borrowed from natural selection, originally developed by DeepMind. Tested across a range of problems in counting, number patterns, and related areas, it can genuinely *learn* mathematical structure, not just search for it.

> **Key Insight:** Funsearch uses large language models not as answer machines but as *mutation engines* in a genetic algorithm, evolving Python programs that guide the search for mathematically significant examples.

## How It Works

![Figure 1](/iaifi-research-blog/figures/2503_11061/figure_1.png)

The core loop of funsearch is simple. Instead of evolving bacteria in a petri dish, you're evolving *programs*. The population consists of hundreds of Python scripts, each encoding a strategy for solving a mathematical problem. The fittest scripts get selected, combined in a prompt, and fed to an LLM, which writes a new candidate script. Repeat until something remarkable emerges.

The key architectural insight is the separation between two types of functions:

- **The `solve` function** — written once by the human researcher, encodes the rigid mathematical rules. It guarantees that any proposed solution is valid.
- **The `priority` function** — evolved by the LLM, acts as a smart ranking system: an educated guess about which candidates are most worth exploring. It tells `solve` which options to try first.

This division of labor is clever. The LLM's output doesn't need to be mathematically rigorous — it just needs to be *useful*. If the priority function leads the solver toward better solutions, it survives. If not, it dies out. Mathematical correctness is always enforced by the human-controlled `solve` function. This hard-soft pairing keeps the system both flexible and safe.

To avoid getting trapped in local optima, the team uses an **island model**: the population splits into independent sub-populations that evolve in parallel. Periodically, the worst-performing islands are culled and repopulated from survivors. Survival of the fittest, played out across computational threads.

One thing this implementation doesn't require: GPU clusters, ML expertise, or anything exotic. A working mathematician can apply funsearch to a new problem by modifying a short Python configuration file and choosing an LLM from a standard provider.

## Why It Matters

The benchmarks are encouraging. Tested on the **cap set problem** — a classic question asking how large a collection of integers can grow without ever containing three evenly-spaced numbers (like 2, 4, 6) — and on problems in number theory, funsearch didn't just find good examples. It found *better* ones than previous automated approaches.

In some cases it discovered principles that *generalized* beyond the specific problem it was trained on. That's not brute-force search. That's something closer to learning.

![Figure 2](/iaifi-research-blog/figures/2503_11061/figure_2.png)

This points toward a genuinely new role for AI in mathematics: not replacing human insight, but dramatically accelerating the exploratory phase of research. The hardest part of mathematical discovery is often knowing *where to look*. Funsearch doesn't just search faster — it learns to search smarter. And because results are executable Python programs, mathematicians can inspect exactly *what* the LLM learned, potentially extracting new conjectures or proof strategies from the evolved code.

![Figure 3](/iaifi-research-blog/figures/2503_11061/figure_3.png)

The broader implications extend beyond pure mathematics. Many problems in theoretical physics share the same structure: easy to check, hard to find. Whether searching for optimal lattice configurations, extremal quantum states, or combinatorial structures underlying physical symmetries, funsearch could become a standard tool in the computational scientist's toolkit. The team's open-source release lowers the barrier to adoption considerably — any researcher with a laptop and an API key can try it.

> **Bottom Line:** Funsearch turns LLMs into mathematical explorers — and this new implementation means working mathematicians, not just ML engineers, can put them to work.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges AI and pure mathematics, showing that LLM-driven evolutionary search can discover novel examples in combinatorics and number theory — domains central to the mathematical foundations of physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper establishes concrete benchmarking metrics for funsearch across multiple problem types, providing a practical roadmap for applying LLM-based program synthesis to new mathematical domains.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Making funsearch accessible to working mathematicians without ML expertise puts AI-assisted discovery within reach for researchers working on the mathematical structures — extremal combinatorics, number theory — that sit at the foundations of fundamental physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will target harder open problems in combinatorics and explore whether the generalizing behavior observed here scales to richer mathematical settings. The implementation is freely available on GitHub; the paper appears in *Advances in Theoretical and Mathematical Physics* (2025) and is available at [arXiv:2503.11061](https://arxiv.org/abs/2503.11061).</span></div></div>
</div>
