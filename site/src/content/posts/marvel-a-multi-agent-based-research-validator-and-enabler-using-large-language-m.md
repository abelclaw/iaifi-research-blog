---
abstract: We present MARVEL (https://ligogpt.mit.edu/marvel), a locally deployable,
  open-source framework for domain-aware question answering and assisted scientific
  research. It is designed to address the increasing demands of a digital assistant
  for scientific groups that can read highly technical data, cite precisely, and operate
  within authenticated networks. MARVEL combines a fast path for straightforward queries
  with a more deliberate DeepSearch mode that integrates retrieval-augmented generation
  and Monte Carlo Tree Search. It explores complementary subqueries, allocates more
  compute to promising branches, and maintains a global evidence ledger that preserves
  sources during drafting. We applied this framework in the context of gravitational-wave
  research related to the Laser Interferometer Gravitational-wave Observatory. Answers
  are grounded in a curated semantic index of research literature, doctoral theses,
  LIGO documents, and long-running detector electronic logbooks, with targeted web
  searches when appropriate. Because direct benchmarking against commercial LLMs cannot
  be performed on private data, we evaluated MARVEL on two publicly available surrogate
  datasets that capture comparable semantic and technical characteristics. On these
  benchmarks, MARVEL matches a GPT-4o mini baseline on literature-centric queries
  and substantially outperforms it on detector-operations content, where domain retrieval
  and guided reasoning are decisive. By making the complete framework and evaluation
  datasets openly available, we aim to provide a reproducible foundation for developing
  domain-specific scientific assistants.
arxivId: '2601.03436'
arxivUrl: https://arxiv.org/abs/2601.03436
authors:
- Nikhil Mukund
- Yifang Luo
- Fan Zhang
- Lisa Barsotti
- Erik Katsavounidis
concepts:
- retrieval-augmented generation
- monte carlo methods
- multi-agent orchestration
- domain-specific qa
- embeddings
- scientific workflows
- test-time scaling
- gravitational waves
- interpretability
- active learning
- signal detection
figures:
- /iaifi-research-blog/figures/2601_03436/figure_1.png
- /iaifi-research-blog/figures/2601_03436/figure_2.png
- /iaifi-research-blog/figures/2601_03436/figure_3.png
pdfUrl: https://arxiv.org/pdf/2601.03436v1
published: '2026-01-06T21:47:22+00:00'
theme: Astrophysics
title: 'MARVEL: A Multi Agent-based Research Validator and Enabler using Large Language
  Models'
wordCount: 1005
---

## The Big Picture

Imagine joining one of the most complex scientific collaborations on Earth — the LIGO gravitational-wave observatory. Your job spans a thousand interlocking systems: laser optics, vibration isolation, digital control systems, decades of detector logs. The institutional knowledge you need is scattered across hundreds of thousands of documents: technical reports, PhD theses, electronic logbooks from two detector sites, a mountain of published literature. Where do you even start?

This is the daily reality for LIGO researchers. The collaboration has detected more than 300 gravitational-wave events — ripples in spacetime from colliding black holes and neutron stars — since its landmark first detection in 2015. People rotate between roles, expertise walks out the door, and the knowledge base keeps growing. A new researcher asking "why did the detector glitch last Tuesday?" might need to trace years of logbook entries written by engineers who've long since moved on.

The bottleneck isn't intelligence. It's finding the right information at all.

Researchers at MIT's Kavli Institute and IAIFI have built **MARVEL**, a locally deployable AI assistant that doesn't just search this knowledge base but *reasons* through it — citing sources precisely, handling technical jargon fluently, and allocating its own computational effort to tackle the hardest questions.

> **Key Insight:** MARVEL combines retrieval-augmented generation with Monte Carlo Tree Search to give scientific collaborations a domain-expert AI assistant that operates on private, institutional knowledge — not just publicly available data.

## How It Works

MARVEL routes every incoming query along one of two tracks based on complexity. Straightforward factual questions take a **fast path**: rapid retrieval and synthesis. For harder queries — multi-step reasoning, conflicting sources, deeply technical detector operations — a **DeepSearch mode** kicks in.

![Figure 1](/iaifi-research-blog/figures/2601_03436/figure_1.png)

DeepSearch is where MARVEL gets interesting. It uses **Monte Carlo Tree Search (MCTS)**, an algorithm best known from game-playing AI like AlphaGo, repurposed here for scientific reasoning. Rather than exhaustively exploring every line of investigation, MCTS lets MARVEL probe multiple sub-questions simultaneously, then concentrate computational effort on the branches turning up real evidence. Think of it as a detective who pursues several leads at once, then doubles down on the ones that pay off.

The retrieval layer draws from a curated **semantic index** — a database organized by meaning, not just keywords — built from four source types:

- Published arXiv papers and preprints
- Doctoral theses from LIGO-affiliated researchers
- Internal LIGO technical documents
- Detector electronic logbooks

When those sources fall short, MARVEL triggers targeted web searches to fill gaps. Throughout, it maintains a **global evidence ledger** — a running record of every source consulted and every claim grounded — so the final answer arrives with full citation provenance intact.

![Figure 2](/iaifi-research-blog/figures/2601_03436/figure_2.png)

MARVEL runs on **open-weight language models** — AI systems whose underlying parameters are publicly available, unlike proprietary services like GPT-4 — rather than commercial APIs. This means the entire system operates within an institution's private network, which matters enormously for collaborations handling sensitive engineering data or proprietary experimental results.

## Why It Matters

Benchmarking a system trained on private institutional data presents a real challenge: there's no shared test set to compare against public models. The team's solution was to construct two **surrogate datasets** with comparable semantic and technical characteristics to LIGO's internal documents — one drawn from published scientific literature, one mirroring the operational, log-style content of detector logbooks.

On literature-centric queries, MARVEL matches a GPT-4o mini baseline. On detector-operations content — the messy, domain-specific material that constitutes the real working knowledge of a gravitational-wave observatory — MARVEL substantially outperforms it. This is exactly the regime where domain-specific retrieval and guided reasoning matter most: when the answer lives in a logbook entry from three years ago, written in engineering shorthand, that no general-purpose model has ever encountered.

![Figure 3](/iaifi-research-blog/figures/2601_03436/figure_3.png)

The broader significance extends well beyond LIGO. Every large scientific collaboration — particle physics experiments, astronomy surveys, genomics consortia — generates vast institutional knowledge that gradually becomes inaccessible as people and projects evolve. The standard response has been to rely on commercial AI tools, which are powerful but operate on public data, can't be customized to specific document collections, and require sending sensitive information off-site.

MARVEL offers a blueprint for a different approach: a reproducible, open-source framework where scientific groups control their own knowledge base, their own AI models, and their own reasoning pipeline. The architecture is domain-agnostic — adapting it to a new scientific domain requires changing datasets and adjusting prompts, not rebuilding from scratch. Both the full framework and evaluation datasets are publicly available.

Open questions remain: How does MCTS-guided reasoning scale as knowledge bases grow to millions of documents? How should the system handle contradictory information from different time periods in a logbook? How do you maintain benchmark validity as private institutional data evolves? These are the problems that will define the next generation of scientific AI assistants.

> **Bottom Line:** MARVEL demonstrates that domain-specific AI assistants, built on private institutional knowledge and guided by tree-search reasoning, can outperform general-purpose commercial LLMs on the exact queries that matter most for working scientists — and its open-source release gives every major collaboration the tools to build their own.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">MARVEL directly bridges AI systems research and gravitational-wave physics by applying Monte Carlo Tree Search — a technique from game-playing AI — to scientific question answering over LIGO's decades of detector engineering knowledge.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work advances domain-specific retrieval-augmented generation by introducing a compute-aware DeepSearch mode that strategically allocates LLM inference across promising reasoning branches, outperforming GPT-4o mini on technical operational content.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By making LIGO's dispersed institutional knowledge — logbooks, theses, technical documents — accessible through intelligent retrieval, MARVEL helps accelerate gravitational-wave science and supports operation of instruments studying the universe's most extreme events.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions could apply the framework to other large physics collaborations and improve handling of temporally evolving knowledge bases; the work is available on arXiv and the live system at ligogpt.mit.edu/marvel.</span></div></div>
</div>
