---
abstract: 'Large language models (LLMs) have demonstrated an unprecedented ability
  to perform complex tasks in multiple domains, including mathematical and scientific
  reasoning. We demonstrate that with carefully designed prompts, LLMs can accurately
  carry out key calculations in research papers in theoretical physics. We focus on
  a broadly used approximation method in quantum physics: the Hartree-Fock method,
  requiring an analytic multi-step calculation deriving approximate Hamiltonian and
  corresponding self-consistency equations. To carry out the calculations using LLMs,
  we design multi-step prompt templates that break down the analytic calculation into
  standardized steps with placeholders for problem-specific information. We evaluate
  GPT-4''s performance in executing the calculation for 15 research papers from the
  past decade, demonstrating that, with correction of intermediate steps, it can correctly
  derive the final Hartree-Fock Hamiltonian in 13 cases and makes minor errors in
  2 cases. Aggregating across all research papers, we find an average score of 87.5
  (out of 100) on the execution of individual calculation steps. Overall, the requisite
  skill for doing these calculations is at the graduate level in quantum condensed
  matter theory. We further use LLMs to mitigate the two primary bottlenecks in this
  evaluation process: (i) extracting information from papers to fill in templates
  and (ii) automatic scoring of the calculation steps, demonstrating good results
  in both cases. The strong performance is the first step for developing algorithms
  that automatically explore theoretical hypotheses at an unprecedented scale.'
arxivId: '2403.03154'
arxivUrl: https://arxiv.org/abs/2403.03154
authors:
- Haining Pan
- Nayantara Mudur
- Will Taranto
- Maria Tikhanovskaya
- Subhashini Venugopalan
- Yasaman Bahri
- Michael P. Brenner
- Eun-Ah Kim
concepts:
- hartree-fock method
- prompt engineering
- hamiltonian systems
- transformers
- llm scientific reasoning
- scientific workflows
- automated discovery
- symmetry breaking
- test-time scaling
- interpretability
figures:
- /iaifi-research-blog/figures/2403_03154/figure_1.png
- /iaifi-research-blog/figures/2403_03154/figure_1.png
- /iaifi-research-blog/figures/2403_03154/figure_2.png
- /iaifi-research-blog/figures/2403_03154/figure_2.png
- /iaifi-research-blog/figures/2403_03154/figure_3.png
- /iaifi-research-blog/figures/2403_03154/figure_3.png
pdfUrl: https://arxiv.org/pdf/2403.03154v2
published: '2024-03-05T17:47:22+00:00'
theme: Foundational AI
title: Quantum Many-Body Physics Calculations with Large Language Models
wordCount: 1000
---

## The Big Picture

Imagine hiring a research assistant who can sit down with a graduate-level physics textbook, follow a multi-page derivation filled with specialized mathematical symbols, and produce the correct answer — the first time, almost every time. Now imagine that assistant is a language model trained mostly on internet text.

For decades, theoretical physicists have relied on **Hartree-Fock mean-field theory** — a method for calculating how electrons push and pull on each other inside exotic quantum materials. Mastering it takes years of graduate study. The calculation demands physical intuition, abstract algebra, specialized notation, and a multi-step logic where one wrong sign ruins everything downstream.

It is exactly the kind of task that AI skeptics would call fundamentally human. A team from Cornell, Google Research, and Harvard decided to test that assumption head-on — and GPT-4 passed with flying colors.

> **Key Insight:** With carefully structured prompts, GPT-4 can execute graduate-level quantum physics derivations with an average score of 87.5 out of 100, correctly completing the full Hartree-Fock calculation in 13 out of 15 real research papers.

## How It Works

The team's central insight was that the Hartree-Fock calculation, however intimidating, is actually *structured*. It follows a reproducible sequence of steps that any quantum physicist working on materials would recognize. So they built the **HF template**: a multi-step prompt framework that breaks the derivation into standardized stages, with *placeholders* for the problem-specific details of each paper.

Think of it like a tax form for quantum physics. The structure stays the same every time; you fill in the numbers that change. Each prompt step tells GPT-4 exactly what to calculate next, and the model supplies the physics-specific content for whatever system is under study.

![Figure 1](/iaifi-research-blog/figures/2403_03154/figure_1.png)

The derivation unfolds across five main stages:

1. **Establish the Hilbert space** — identify the particle flavors (spin, orbital, valley, layer) and write the non-interacting Hamiltonian. (The *Hilbert space* is the mathematical space of all possible quantum states; the *Hamiltonian* encodes the system's total energy.)
2. **Fourier transform** — convert the Hamiltonian to momentum space. (A *Fourier transform* re-expresses physical information in terms of particle momenta rather than positions, making subsequent steps cleaner.)
3. **Apply Wick's theorem** — decompose the interaction Hamiltonian by replacing four-operator products with mean-field averages. (In plain terms: a shortcut that substitutes the impossible math of four particles interacting simultaneously with a simpler average-field picture.)
4. **Organize Hartree and Fock terms** — sort the resulting energy equation into its two components: direct electron-electron repulsion (Hartree) and exchange interaction (Fock).
5. **Reveal symmetry structure** — use the system's symmetries to identify the *order parameter*, the quantity that measures how "ordered" the material is — the way magnetization measures how magnetic it is — and signals what phase it might enter.

![Figure 2](/iaifi-research-blog/figures/2403_03154/figure_1.png)

The researchers assembled a benchmark of 15 real physics papers from the past decade, spanning twisted bilayer graphene, topological insulators, Moiré systems, and more. For each paper, they filled in the templates with problem-specific information and asked GPT-4 to execute the derivation step by step. The model correctly produced the final **Hartree-Fock Hamiltonian** — the simplified energy equation that is the key output of the entire procedure — in 13 of 15 cases. The two failures were minor errors, not catastrophic breakdowns.

They also pushed the automation further. Rather than manually extracting information from each paper, they asked GPT-4 to read an abstract and answer ten targeted questions — filling in its own placeholders. The model performed well here too, correctly inferring notation and physical assumptions from a few sentences of text.

## Why It Matters

Most AI benchmarks test whether models *know* facts about physics. This paper tests whether a model can *do* physics — executing a multi-step analytical calculation at the level expected of a first- or second-year PhD student. The answer, at least for this class of calculation, is yes.

![Figure 3](/iaifi-research-blog/figures/2403_03154/figure_2.png)

The broader implication is about scale. Hartree-Fock is applied to hundreds of new quantum systems every year. Each application currently requires a skilled human to spend days on the derivation. An AI system that reliably automates that step doesn't just save time — it opens the door to systematically scanning theoretical hypothesis spaces that would otherwise be inaccessible.

The authors frame this explicitly: strong performance on HF calculations is "the first step for developing algorithms that automatically explore theoretical hypotheses at an unprecedented scale." New quantum materials are discovered faster than they can be theoretically characterized; this changes the math on that problem.

Open questions remain. The study uses a human-in-the-loop correction scheme — intermediate errors can be caught before they propagate. Fully autonomous derivation is harder. And Hartree-Fock, while ubiquitous, is one framework among many. Whether LLMs can handle more exotic methods — diagrammatic perturbation theory, renormalization group flows, tensor network contractions — is an open challenge.

> **Bottom Line:** GPT-4 can execute graduate-level quantum physics calculations with near-expert accuracy when given well-structured prompts, suggesting that the analytic workhorse calculations of theoretical physics are ripe for AI-assisted automation — potentially transforming how quickly theorists can explore new quantum materials.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly bridges AI and quantum condensed matter theory by demonstrating that LLMs can reliably execute the Hartree-Fock derivation at graduate-student level, opening a new paradigm for AI-assisted theoretical research.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces a structured prompt-template methodology for multi-step analytical reasoning, showing that task decomposition and placeholder-based prompting dramatically improve LLM performance on complex, symbol-heavy scientific calculations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By automating Hartree-Fock calculations across 15 diverse quantum materials systems, this work paves the way for large-scale computational exploration of symmetry-breaking phases and emergent quantum order in correlated electron systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work aims to extend this approach to other calculational frameworks and enable fully autonomous derivation without intermediate human correction; the work is available on arXiv and represents a foundational step toward AI systems that can generate and test theoretical physics hypotheses autonomously.</span></div></div>
</div>
