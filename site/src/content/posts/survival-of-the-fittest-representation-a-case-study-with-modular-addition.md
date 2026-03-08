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
wordCount: 975
---

## The Big Picture

Imagine you're dropped into a forest where hundreds of plant species compete for the same sunlight and soil. Most will wither. A few, the ones best adapted to local conditions, will thrive and eventually dominate.

The same drama plays out inside a neural network during training. Instead of plants, you have mathematical structures called **representations**, the internal "languages" a network uses to solve a problem. Most of them die.

This is the central metaphor in new research from MIT's IAIFI group. When a network has access to many possible ways of solving a task, which one wins?

The researchers propose the **Survival of the Fittest hypothesis**: at the start of training, a network implicitly contains many competing solutions. Under pressure from limited resources (only so much internal space, penalties that discourage complexity) these solutions fight for dominance. The fittest survive; the rest collapse to nothing.

To test this, the team focused on one of the cleanest settings in mechanistic interpretability: modular addition. Their findings show that competition between representations follows predictable mathematical laws, and that you can forecast which solution will win before training even finishes.

> **Key Insight:** Neural networks don't just learn one algorithm. They start with many, and training is a competitive elimination process where early signals predict the ultimate winners.

## How It Works

The task sounds simple: given two numbers *a* and *b*, compute *(a + b) mod p*, arithmetic on a clock face where numbers wrap around after reaching *p*. Prior work established that neural networks solve this by learning **circular representations**, internal arrangements where numbers 0 through *p*−1 are placed around a circle. Different circles correspond to different **Fourier frequencies** *k*, different "rhythms" of stepping around the clock. Frequency *k* places token *t* at the point (cos(2πkt/p), sin(2πkt/p)).

Because the embedding is randomly initialized, every frequency starts with a roughly equal shot. The network could use any of the (p−1)/2 possible circular frequencies. But it doesn't use them all. It ends up using only a handful.

![Figure 1](figure:1)

The researchers tracked all these frequencies throughout training by computing **Fourier signals**, measuring how strongly each circular pattern appears in the network's internal state at each step. Early in training, a few frequencies begin amplifying rapidly, their signals separating from the pack on a logarithmic scale.

The rest collapse toward zero. The survivors stabilize into crisp circles visible in the embedding space. The losers dissolve into noise.

![Figure 2](figure:2)

Two factors determine who survives:

- **Initial signal strength**: Frequencies with larger magnitudes at random initialization had a head start, and were more likely to survive.
- **Initial gradient**: Frequencies whose signals were growing fastest in the first few steps were also more likely to dominate, the "fittest" in the sense of most responsive to the training signal.

Neither factor alone perfectly predicts the winner. The result is probabilistic, not deterministic. But across many training runs with different random seeds, the pattern holds.

## The Ecology of Representations

The paper's sharpest contribution is its mathematical description of how circles interact. Borrowing the **Lotka-Volterra equations** from classical ecology (the predator-prey model), the researchers modeled each frequency's signal as a variable evolving under the influence of all others. The resulting set of **linear differential equations** fits the observed training dynamics well, even when simplified via sparse regression to highlight only the strongest interactions.

This means you can characterize any two frequencies as either **collaborative** (both grow together) or **competitive** (one suppresses the other). The interaction matrix tells you the full story of how representations negotiate coexistence.

The researchers also varied the embedding dimension, the total space available inside the network. With a larger embedding, more circles survive. With a tighter one, fewer do. The parallel to ecological resource partitioning is direct: a richer environment supports greater biodiversity.

![Figure 3](figure:3)

## Why It Matters

Mechanistic interpretability has spent years asking *what* is inside these systems. This work starts to address *why* they learned it.

If training is a competitive selection process, then "which algorithm did the network use?" turns into "which algorithm happened to be fittest given this initialization and these constraints?" That shifts the framing from archaeology (digging up what's there) to evolutionary biology (understanding the pressures that shaped it).

Modular addition is a proof-of-concept, chosen because it's clean enough to analyze rigorously while still revealing general principles. If complex high-dimensional representations can be broken into simpler competing components with well-defined interactions, the same framework might eventually apply to large language models, and to steering their internal development toward safer or more efficient solutions.

Open questions remain. Does the Lotka-Volterra analogy hold in deeper networks? Can initialization be deliberately engineered to guarantee a desired algorithm wins? What counts as "fitness" beyond the metrics explored here?

> **Bottom Line:** Neural networks run a hidden evolutionary tournament during training. A few measurable properties at initialization predict which internal representations will dominate, and the dynamics follow the same equations ecologists use to model competing species.

---

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work imports a foundational model from theoretical ecology, the Lotka-Volterra equations, to describe neural network training dynamics, building a quantitative bridge between population biology and deep learning theory.

- **Impact on Artificial Intelligence:** The paper advances mechanistic interpretability by decomposing training dynamics into competing low-dimensional representations with measurable interactions, offering a new lens for understanding *why* networks converge to particular solutions.

- **Impact on Fundamental Interactions:** By applying tools from mathematical physics (Fourier analysis, differential equations, sparse regression) to representation learning, the work shows that abstract physical modeling frameworks can yield genuine insight into artificial neural systems.

- **Outlook and References:** Future work may extend this competition framework to real-world architectures and explore whether "fitness engineering" at initialization can reliably guide networks toward desired algorithms. The paper is available at [arXiv:2405.17420](https://arxiv.org/abs/2405.17420) and code is public at github.com/carlguo866/circle-survival.
