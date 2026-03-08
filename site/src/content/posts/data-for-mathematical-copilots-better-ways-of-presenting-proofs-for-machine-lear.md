---
abstract: 'The datasets and benchmarks commonly used to train and evaluate the mathematical
  capabilities of AI-based mathematical copilots (primarily large language models)
  exhibit several shortcomings and misdirections. These range from a restricted scope
  of mathematical complexity to limited fidelity in capturing aspects beyond the final,
  written proof (e.g. motivating the proof, or representing the thought processes
  leading to a proof). These issues are compounded by a dynamic reminiscent of Goodhart''s
  law: as benchmark performance becomes the primary target for model development,
  the benchmarks themselves become less reliable indicators of genuine mathematical
  capability. We systematically explore these limitations and contend that enhancing
  the capabilities of large language models, or any forthcoming advancements in AI-based
  mathematical assistants (copilots or ``thought partners''''), necessitates a course
  correction both in the design of mathematical datasets and the evaluation criteria
  of the models'' mathematical ability. In particular, it is necessary for benchmarks
  to move beyond the existing result-based datasets that map theorem statements directly
  to proofs, and instead focus on datasets that translate the richer facets of mathematical
  research practice into data that LLMs can learn from. This includes benchmarks that
  supervise the proving process and the proof discovery process itself, and we advocate
  for mathematical dataset developers to consider the concept of "motivated proof",
  introduced by G. Pólya in 1949, which can serve as a blueprint for datasets that
  offer a better proof learning signal, alleviating some of the mentioned limitations.'
arxivId: '2412.15184'
arxivUrl: https://arxiv.org/abs/2412.15184
authors:
- Simon Frieder
- Jonas Bayer
- Sam Looi
- Jacob Loader
- Julius Berner
- Katherine M. Collins
- András Juhász
- Fabian Ruehle
- Sean Welleck
- Gabriel Poesia
- Ryan-Rhys Griffiths
- Adrian Weller
- Anirudh Goyal
- Cameron Freer
- Thomas Lukasiewicz
- Timothy Gowers
concepts:
- motivated proof
- mathematical benchmarking
- proof process supervision
- scientific workflows
- transformers
- interpretability
- automated discovery
- fine-tuning
- scalability
- reinforcement learning
- mixture of experts
figures:
- /iaifi-research-blog/figures/2412_15184/figure_1.png
- /iaifi-research-blog/figures/2412_15184/figure_2.png
pdfUrl: https://arxiv.org/pdf/2412.15184v2
published: '2024-12-19T18:55:17+00:00'
theme: Foundational AI
title: 'Data for Mathematical Copilots: Better Ways of Presenting Proofs for Machine
  Learning'
wordCount: 977
---

## The Big Picture

Imagine hiring a chess tutor who only ever shows you the final board position (checkmate) but never explains the strategy, the sacrifices, or the moments of doubt along the way. You might memorize winning patterns, but you'd struggle to improvise against a novel opponent. This is roughly the problem at the heart of how we currently train and evaluate AI systems for mathematics.

The field of AI-assisted mathematics has exploded in recent years. Systems like AlphaGeometry solve International Math Olympiad problems. GPT-4 demonstrates undergraduate-level performance on some tasks. The standardized tests used to measure AI math ability, called **benchmarks**, are being passed so quickly that researchers scramble to invent harder ones. Yet a team from Oxford, Cambridge, Caltech, MIT, and a dozen other institutions argues that something is deeply broken underneath all this apparent progress.

The core problem: nearly every dataset used to train and evaluate these systems focuses on a single thing (the final, polished proof) while ignoring everything that makes mathematics actually work as a human endeavor. Fixing this misdirection requires rethinking what "good data" for mathematical AI even means.

> **Key Insight:** AI math benchmarks are measuring the wrong thing. Training systems to produce correct final proofs without capturing the reasoning process is like teaching someone to recite answers without understanding questions. It optimizes for looking capable without building genuine capability.

## How It Works

The authors identify what they call a **Goodhart's law dynamic** in mathematical AI evaluation. Goodhart's law, from economics, says that when a measure becomes a target, it ceases to be a good measure. In practice: once AI developers know their model will be judged by scores on standardized test suites like MATH or GSM8K, they optimize directly for those scores, through **dataset contamination** (when test examples leak into training data), clever answer-extraction tricks, or **fine-tuning** (adapting a model directly on similar problems). The benchmark stops measuring what it was supposed to measure.

![Figure 1](/iaifi-research-blog/figures/2412_15184/figure_1.png)

But benchmark degradation is just the symptom. The authors trace the disease to how mathematical datasets are constructed in the first place.

Current datasets follow a surprisingly simple template: given a theorem statement, produce a proof. Input → output. The entire middle is missing: the failed attempts, the heuristics, the moment a mathematician decides to try **induction** rather than **contradiction** (two common proof strategies), the **auxiliary lemmas** (helper theorems) invented along the way.

The paper draws a sharp distinction between two things we might want AI to do:

- **Result-based evaluation**: Did the model produce a correct proof? (What current benchmarks measure)
- **Process-based evaluation**: Did the model reason well throughout? Did it take sensible steps? Could it explain *why* it chose a given approach?

Professional mathematicians don't experience mathematics as a lookup table. They explore, backtrack, draw analogies, make mistakes, and revise. None of this appears in existing training data.

![Figure 2](/iaifi-research-blog/figures/2412_15184/figure_2.png)

The proposed solution centers on an old idea largely ignored by machine learning: the **"motivated proof,"** introduced by problem-solving theorist G. Pólya in 1949. A motivated proof doesn't just present steps in logical order; it explains *why* each step is taken, what the mathematician was trying to achieve, and what alternatives were considered. The authors argue this concept should guide a new generation of datasets that train AI on the *process* of mathematical discovery, not just its products.

They also point to structural gaps in how the field collects data: datasets like GSM8K are vastly overstudied, while entire areas of mathematical practice (tool use, conjecture formation, informal research-level reasoning) remain almost entirely unrepresented. The gap between **formal proof languages** like Lean or Coq (software tools that verify proofs with computer-level rigor) and natural mathematical language is another blind spot few datasets have addressed.

## Why It Matters

The long-term vision behind this research is the **mathematical copilot**: an AI that doesn't just solve problems you hand it, but genuinely collaborates like a brilliant colleague, suggesting approaches, flagging when your intuition might be wrong, explaining the terrain of an unfamiliar problem. Current systems, trained on sanitized final proofs, lack the building blocks for that kind of exploratory partnership.

This matters for AI and physics research. Tools that assist in deriving equations, checking proofs in quantum field theory, or exploring **string compactifications** (how extra dimensions might curl up in string theory) could transform theoretical physics. But those tools need to reason well under uncertainty and explain their steps, capabilities that result-only training fundamentally cannot develop.

As AI scores on MATH-style evaluations approach saturation, the field risks mistaking benchmark performance for genuine mathematical understanding. An entire generation of tools could end up built on a foundation that looks solid but is quietly hollow.

> **Bottom Line:** The next leap in AI for mathematics won't come from better architectures alone. It will come from better data. Datasets that capture *how* proofs are discovered, not just what they look like when finished, are the missing ingredient for genuine mathematical reasoning in AI systems.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work, with co-author Fabian Ruehle at Northeastern University (a core IAIFI institution), directly addresses the data infrastructure needed for AI tools to accelerate mathematical discovery in theoretical physics, from algebraic geometry to quantum field theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper provides a systematic critique and course-correction framework for mathematical AI evaluation, advocating for process-aware benchmarks grounded in Pólya's "motivated proof" concept that could fundamentally improve how LLMs are trained on mathematical reasoning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Better mathematical copilots could accelerate research in string theory, lattice QCD, and quantum gravity, where progress often bottlenecks on complex derivations requiring exactly the kind of exploratory, step-by-step reasoning these new datasets would teach.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The authors call on the community to develop benchmark datasets that supervise the proof discovery process itself; the full paper is available at [arXiv:2412.15184](https://arxiv.org/abs/2412.15184).</span></div></div>
</div>
