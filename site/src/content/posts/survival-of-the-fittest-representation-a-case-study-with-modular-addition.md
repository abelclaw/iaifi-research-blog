---
abstract: 'When a neural network can learn multiple distinct algorithms to solve a
  task, how does it "choose" between them during training? To approach this question,
  we take inspiration from ecology: when multiple species coexist, they eventually
  reach an equilibrium where some survive while others die out. Analogously, we suggest
  that a neural network at initialization contains many solutions (representations
  and algorithms), which compete with each other under pressure from resource constraints,
  with the "fittest" ultimately prevailing. To investigate this Survival of the Fittest
  hypothesis, we conduct a case study on neural networks performing modular addition,
  and find that these networks'' multiple circular representations at different Fourier
  frequencies undergo such competitive dynamics, with only a few circles surviving
  at the end. We find that the frequencies with high initial signals and gradients,
  the "fittest," are more likely to survive. By increasing the embedding dimension,
  we also observe more surviving frequencies. Inspired by the Lotka-Volterra equations
  describing the dynamics between species, we find that the dynamics of the circles
  can be nicely characterized by a set of linear differential equations. Our results
  with modular addition show that it is possible to decompose complicated representations
  into simpler components, along with their basic interactions, to offer insight on
  the training dynamics of representations.'
arxivId: '2405.17420'
arxivUrl: https://arxiv.org/abs/2405.17420
authors:
- Xiaoman Delores Ding
- Zifan Carl Guo
- Eric J. Michaud
- Ziming Liu
- Max Tegmark
concepts:
- training dynamics
- representation learning
- representation competition
- interpretability
- embeddings
- spectral methods
- disentangled representations
- grokking
- sparse models
- group theory
- stochastic processes
figures:
- /iaifi-research-blog/figures/2405_17420/figure_1.png
- /iaifi-research-blog/figures/2405_17420/figure_2.png
- /iaifi-research-blog/figures/2405_17420/figure_3.png
pdfUrl: https://arxiv.org/pdf/2405.17420v1
published: '2024-05-27T17:59:04+00:00'
theme: Foundational AI
title: 'Survival of the Fittest Representation: A Case Study with Modular Addition'
wordCount: 1085
---

## The Big Picture

Imagine you're dropped into a forest where hundreds of plant species compete for the same sunlight and soil. Most will wither. A few — the ones best adapted to local conditions — will thrive and eventually dominate.

The same drama unfolds inside a neural network during training. Instead of plants, you have mathematical structures called **representations** — the internal "languages" a network uses to solve a problem. And just like in the forest, most of them die.

This is the central metaphor driving new research from MIT's IAIFI group. When a network has access to many possible ways of solving a task, which one wins?

The researchers propose the **Survival of the Fittest hypothesis**: at the start of training, a network implicitly contains many competing solutions. Under pressure from limited resources — only so much internal space, penalties that discourage complexity — these solutions fight for dominance. The fittest survive; the rest collapse to nothing.

To test this rigorously, the team focused on one of the cleanest test cases in the study of how neural networks work internally: modular addition. Their findings reveal that competition between representations follows predictable mathematical laws — and that you can forecast which solution will win before training even finishes.

> **Key Insight:** Neural networks don't just learn one algorithm — they start with many, and training is a competitive elimination process where early signals at the start of training predict the ultimate winners.

## How It Works

The task is deceptively simple: given two numbers *a* and *b*, compute *(a + b) mod p* — arithmetic on a clock face where numbers wrap around after reaching *p*. Prior work established that neural networks solve this by learning **circular representations** — internal arrangements where numbers 0 through *p*−1 are placed around a circle. Different circles correspond to different **Fourier frequencies** *k* — different "rhythms" of stepping around the clock — where frequency *k* places token *t* at the point (cos(2πkt/p), sin(2πkt/p)).

Because the embedding is randomly initialized, every frequency starts with a roughly equal shot. The network could use any of the (p−1)/2 possible circular frequencies. But it doesn't use them all — it ends up using only 3 to 5.

![Figure 1](/iaifi-research-blog/figures/2405_17420/figure_1.png)

The researchers tracked all these frequencies throughout training by computing **Fourier signals** — measuring how strongly each circular pattern appears in the network's internal state at each step. The dynamics are dramatic: early in training, a handful of frequencies begin amplifying rapidly, their signals separating from the pack on a logarithmic scale.

The rest collapse toward zero. The survivors stabilize into crisp circles visible in the embedding space. The losers dissolve into noise.

![Figure 2](/iaifi-research-blog/figures/2405_17420/figure_2.png)

Two factors determine who survives:

- **Initial signal strength**: Frequencies with larger magnitudes at random initialization were more likely to survive — they had a head start.
- **Initial gradient**: Frequencies whose signals were growing fastest in the first few steps were also more likely to dominate — the "fittest" in the sense of most responsive to the training signal.

Neither factor alone perfectly predicts the winner. The result is probabilistic, not deterministic. But across many training runs with different random seeds, the pattern holds strongly.

## The Ecology of Representations

The most elegant part of the paper is its mathematical description of how circles interact. Inspired by the **Lotka-Volterra equations** — the classic predator-prey model from ecology — the researchers modeled each frequency's signal as a variable evolving under the influence of all others. The result is a set of **linear differential equations** — describing how each frequency's strength changes over time based on its interactions with the rest — that fits the observed training dynamics surprisingly well, even when simplified via sparse regression to highlight only the most important interactions.

This means you can characterize any two frequencies as either **collaborative** (both grow together) or **competitive** (one suppresses the other). The interaction matrix tells you the full story of how representations negotiate coexistence.

The researchers also varied the embedding dimension — the total space available inside the network. With a larger embedding, more circles survive. With a tighter one, fewer do. This mirrors ecological resource partitioning: a richer environment supports greater biodiversity.

![Figure 3](/iaifi-research-blog/figures/2405_17420/figure_3.png)

## Why It Matters

Mechanistic interpretability — the field that tries to understand what neural networks have learned by examining their internals — has spent years asking *what* is inside these systems. This work takes a step toward understanding *why* they learned it.

If training is fundamentally a competitive selection process, then "which algorithm did the network use?" becomes "which algorithm happened to be fittest given this initialization and these constraints?" That reframes the whole enterprise: from archaeology — digging up what's there — to evolutionary biology — understanding the pressures that shaped it.

The implications extend beyond toy models. Modular addition is a proof-of-concept: clean enough to analyze rigorously, rich enough to reveal general principles. If complex high-dimensional representations can be decomposed into simpler competing components with well-defined interactions, the same framework might eventually apply to large language models — and to steering their internal development toward safer or more efficient solutions.

Open questions remain. Does the Lotka-Volterra analogy hold in deeper networks? Can initialization be deliberately engineered to guarantee a desired algorithm wins? What counts as "fitness" beyond the metrics explored here?

> **Bottom Line:** Neural networks run a hidden evolutionary tournament during training — this paper cracks open the rulebook, showing that a few measurable properties at initialization predict which internal representations will dominate, with dynamics that follow the same equations ecologists use to model competing species.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly imports a foundational model from theoretical ecology — the Lotka-Volterra equations — to describe neural network training dynamics, establishing a quantitative bridge between population biology and deep learning theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper advances mechanistic interpretability by decomposing training dynamics into competing low-dimensional representations with measurable interactions, offering a new lens for understanding *why* networks converge to particular solutions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By applying tools from mathematical physics — Fourier analysis, differential equations, sparse regression — to representation learning, the work demonstrates that abstract physical modeling frameworks can yield genuine insight into artificial neural systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend this competition framework to real-world architectures and explore whether "fitness engineering" at initialization can reliably guide networks toward desired algorithms; the paper is available at arXiv and code is public at github.com/carlguo866/circle-survival.</span></div></div>
</div>
