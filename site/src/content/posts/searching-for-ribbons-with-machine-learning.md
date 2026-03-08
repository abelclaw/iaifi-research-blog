---
abstract: 'We apply Bayesian optimization and reinforcement learning to a problem
  in topology: the question of when a knot bounds a ribbon disk. This question is
  relevant in an approach to disproving the four-dimensional smooth Poincaré conjecture;
  using our programs, we rule out many potential counterexamples to the conjecture.
  We also show that the programs are successful in detecting many ribbon knots in
  the range of up to 70 crossings.'
arxivId: '2304.09304'
arxivUrl: https://arxiv.org/abs/2304.09304
authors:
- Sergei Gukov
- James Halverson
- Ciprian Manolescu
- Fabian Ruehle
concepts:
- knot ribbon detection
- low-dimensional topology
- reinforcement learning
- bayesian inference
- poincaré conjecture search
- automated discovery
- monte carlo methods
- scientific workflows
figures:
- /iaifi-research-blog/figures/2304_09304/figure_1.png
- /iaifi-research-blog/figures/2304_09304/figure_2.png
- /iaifi-research-blog/figures/2304_09304/figure_3.png
pdfUrl: https://arxiv.org/pdf/2304.09304v2
published: '2023-04-18T21:12:56+00:00'
theme: Theoretical Physics
title: Searching for ribbons with machine learning
wordCount: 1022
---

## The Big Picture

Imagine holding a loop of string tangled into a complicated knot. Mathematicians who study shapes ask a surprising question: can you "fill in" that knotted loop with a disk, like stretching a soap film across a wire frame, but reaching into a fourth dimension? This connects to one of mathematics' most famous unsolved problems: the smooth four-dimensional Poincaré conjecture (SPC4), which asks whether every four-dimensional shape that looks like a sphere really is one.

A team from IAIFI (Sergei Gukov, James Halverson, Ciprian Manolescu, and Fabian Ruehle) brought machine learning into this arena. They trained algorithms to play a mathematical game involving knots and **ribbon disks**, disks that a knot can bound, with only controlled, allowable self-intersections. In doing so, they eliminated 843 potential counterexamples to SPC4 and proved that 1,705 knots are ribbon.

When their algorithms succeed, they don't just give a probabilistic answer. They produce a rigorous mathematical proof.

> **Key Insight:** Unlike typical machine learning applications that output approximations, this approach generates verifiable certificates. When the algorithm finds a ribbon disk, it produces a concrete sequence of moves that any mathematician can check step-by-step, making the result 100% rigorous.

## How It Works

The researchers frame ribbon-disk detection as a combinatorial game, much like chess or Go. The "board" is a **knot diagram**, a 2D projection of a knotted loop showing which strands cross over or under each other. The "moves" are four local operations:

- Three **Reidemeister moves**, the classic operations that transform any diagram of a knot into any other diagram of the same knot
- One **band addition**, which connects two strands with a twisted strip, effectively fusing parts of the knot

![Figure 1](/iaifi-research-blog/figures/2304_09304/figure_1.png)

The goal: starting from a diagram of knot *K*, use these moves to reach a **trivial link**, a collection of simple, unlinked loops. If you can do this using exactly *k*−1 band moves (where *k* is the number of resulting loops), the knot is ribbon, meaning it bounds a disk with only mild, allowed self-intersections in 3D space. Ribbon knots are also **slice**: they bound a smoothly embedded disk in four-dimensional half-space, which is exactly the property relevant to SPC4.

The catch: the search space is astronomically large. A band can be added in infinitely many ways at each step, and a typical proof might require dozens of moves. No known algorithm navigates this systematically.

The team deployed two kinds of intelligent search:

1. **Bayesian optimization (BO)**: A probabilistic framework that builds a model of which move sequences look promising, then guides search toward ribbon-proving sequences. As it accumulates experience, it learns which regions of the search space are fruitful.
2. **Reinforcement learning (RL)**: An agent learns a policy (a mapping from diagram states to good moves) by playing the game repeatedly and receiving rewards for success. Like AlphaGo learning Go, the agent improves through self-play.

Both methods output the same thing when successful: an explicit sequence of moves that anyone can verify transforms the knot into a trivial link. The certificate *is* the proof.

![Figure 2](/iaifi-research-blog/figures/2304_09304/figure_2.png)

The team tested their methods on three datasets. First, knots with up to 14 crossings, establishing 1,705 ribbon knots independently confirmed by Dunfield and Gong. Second, two families of ribbon knots at high crossing numbers (15 to 70 crossings), constructed with known ground truth to serve as challenging benchmarks. Third, they applied the algorithms to 843 candidate pairs from a large family studied by Manolescu and Piccirillo. These were pairs that could have been counterexamples to SPC4 if one knot turned out to be slice and the other not. The algorithms proved both knots in every pair are ribbon, eliminating all 843 candidates.

One result caught the team off guard: on the high-crossing-number benchmarks, Bayesian optimization outperformed RL. RL still beat a naive random search, but the more sophisticated learning approach didn't win every race. The ribbon-knot search space appears to have structure that BO exploits efficiently, and understanding why is an open question.

![Figure 3](/iaifi-research-blog/figures/2304_09304/figure_3.png)

## Why It Matters

Ruling out 843 potential counterexamples to SPC4 is real progress on one of topology's grand challenges. But the bigger story here is about method. Machine learning can now participate in rigorous mathematics, not just as a conjecture-generator that flags patterns for humans to prove, but as a direct prover that outputs certificates. The line between "AI suggests" and "AI proves" just got blurrier.

For the AI community, the comparison between BO and RL on this task raises useful questions. The ribbon-search problem features sparse rewards, an enormous action space, and highly irregular structure. That BO-guided searches sometimes beat RL here tells us something about which algorithmic families suit which kinds of mathematical search, a question with implications well beyond topology. The team's code is publicly available at [github.com/ruehlef/ribbon](https://github.com/ruehlef/ribbon) for others to probe further.

> **Bottom Line:** By treating the ribbon-disk problem as a combinatorial game and deploying Bayesian optimization and reinforcement learning, this team produced mathematically rigorous proofs (not estimates) that ruled out hundreds of counterexamples to a major open conjecture in four-dimensional topology, while raising new questions about when and why different learning algorithms excel at mathematical search.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">Reinforcement learning and Bayesian optimization, tools developed for games and engineering, here produce verified, rigorous proofs in low-dimensional topology. The project sits squarely at the intersection of AI and fundamental mathematics that defines IAIFI's research program.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper shows that ML algorithms can output mathematical certificates rather than probabilistic guesses, and reveals a surprising benchmark where Bayesian optimization outperforms reinforcement learning, informing algorithm selection for combinatorial search problems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Ruling out 843 candidate counterexamples to the smooth four-dimensional Poincaré conjecture and verifying 1,705 ribbon knots up to 70 crossings represents concrete progress on one of the deepest open questions in four-dimensional topology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include scaling to larger crossing numbers, understanding why BO sometimes beats RL in this setting, and extending the approach to related slice-ribbon problems. The paper is available at [arXiv:2304.09304](https://arxiv.org/abs/2304.09304) and the ribbon-finder tool is open-source at [github.com/ruehlef/ribbon](https://github.com/ruehlef/ribbon).</span></div></div>
</div>
