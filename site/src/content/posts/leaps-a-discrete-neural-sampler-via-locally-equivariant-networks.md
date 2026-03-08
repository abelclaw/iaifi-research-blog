---
abstract: We propose "LEAPS", an algorithm to sample from discrete distributions known
  up to normalization by learning a rate matrix of a continuous-time Markov chain
  (CTMC). LEAPS can be seen as a continuous-time formulation of annealed importance
  sampling and sequential Monte Carlo methods, extended so that the variance of the
  importance weights is offset by the inclusion of the CTMC. To derive these importance
  weights, we introduce a set of Radon-Nikodym derivatives of CTMCs over their path
  measures. Because the computation of these weights is intractable with standard
  neural network parameterizations of rate matrices, we devise a new compact representation
  for rate matrices via what we call "locally equivariant" functions. To parameterize
  them, we introduce a family of locally equivariant multilayer perceptrons, attention
  layers, and convolutional networks, and provide an approach to make deep networks
  that preserve the local equivariance. This property allows us to propose a scalable
  training algorithm for the rate matrix such that the variance of the importance
  weights associated to the CTMC are minimal. We demonstrate the efficacy of LEAPS
  on problems in statistical physics.
arxivId: '2502.10843'
arxivUrl: https://arxiv.org/abs/2502.10843
authors:
- Peter Holderrieth
- Michael S. Albergo
- Tommi Jaakkola
concepts:
- locally equivariant networks
- discrete measure transport
- stochastic processes
- monte carlo methods
- equivariant neural networks
- physics-informed neural networks
- radon-nikodym path measures
- flow matching
- diffusion models
- attention mechanisms
- phase transitions
- bayesian inference
figures:
- /iaifi-research-blog/figures/2502_10843/figure_1.png
- /iaifi-research-blog/figures/2502_10843/figure_2.png
- /iaifi-research-blog/figures/2502_10843/figure_3.png
pdfUrl: https://arxiv.org/pdf/2502.10843v2
published: '2025-02-15T16:16:45+00:00'
theme: Foundational AI
title: 'LEAPS: A discrete neural sampler via locally equivariant networks'
wordCount: 1037
---

## The Big Picture

Imagine trying to find a needle in a haystack the size of a continent — most of it empty. This is **sampling from complex probability distributions**: drawing representative examples from a distribution you can't fully describe, while navigating a vast space of possibilities. In physics, the problem appears everywhere — from simulating magnets to understanding protein folding. In AI, it underlies Bayesian inference, language modeling, and generative systems.

The workhorse solution has long been **Markov chain Monte Carlo (MCMC)**: run a random process long enough and it eventually explores the distribution. But "long enough" can mean astronomically long, especially when the distribution has multiple peaks separated by low-probability valleys. Algorithms get stuck. Convergence stalls.

Researchers have layered on techniques like annealed importance sampling (AIS) and sequential Monte Carlo (SMC) to help — but these introduce their own problem. The **importance weights** — correction factors that compensate for the gap between your approximate sampler and the true target — can have enormous variance, making estimates unreliable.

Now, a team from MIT and Harvard has proposed LEAPS: a method that learns a transport process over **discrete state spaces** — settings where the system exists in distinct, countable configurations (like spins that are either up or down) rather than a continuous range — moving samples from a simple starting distribution to a complex target while keeping those correction weights tightly controlled through a novel neural network architecture.

> **Key Insight:** LEAPS learns a dynamic transport process over discrete state spaces that minimizes the variance of importance weights — making sampling both statistically rigorous and practically scalable for the first time in this setting.

## How It Works

Instead of running a Markov chain until it equilibrates, LEAPS constructs a **time-dependent path**: a continuous interpolation between a simple distribution at time *t* = 0 and the hard-to-sample target at time *t* = 1. A **continuous-time Markov chain (CTMC)** — a process where the system jumps between configurations at random moments in continuous time, rather than at fixed discrete steps — is trained to follow this path.

![Figure 1](/iaifi-research-blog/figures/2502_10843/figure_1.png)

The engine driving this transport is a **rate matrix** *Q_t(y, x)* — encoding, at each moment, how likely the chain is to jump from state *x* to state *y*. If the rate matrix satisfies the **Kolmogorov forward equation** — a classical result from probability theory describing how a distribution must evolve over time — then walkers initialized from the simple distribution will automatically arrive at the target at *t* = 1.

In practice, any learned rate matrix will be imperfect. LEAPS corrects for this using **Radon-Nikodym derivatives** — reweighting factors that account for the difference between the trajectory your chain actually took and the one it should have taken. The paper shows that minimizing the **variance** of these weights is equivalent to optimizing a **physics-informed neural network (PINN) loss** — a loss function borrowed from scientific computing that penalizes deviations from the governing equations.

The catch: computing these weights naively requires summing over all possible transitions at every time step. For *S* states, a naive rate matrix has *S²* entries — intractable at realistic scale. The team's solution is the paper's most original contribution: the **locally equivariant function**.

For physical systems on a **lattice** — a regular grid of sites, like squares on a chessboard, each holding a value — the transition from state *x* to state *y* differs by only a local flip. A **locally equivariant network** exploits this: the output *f(y; x)* for a target state differing from *x* by flipping site *i* depends only on the local neighborhood of *i*. This reduces complexity from *O(S²)* to *O(S · d)*, where *d* is the number of sites.

The researchers construct locally equivariant versions of:

- **Multilayer perceptrons (MLPs)** — by processing local difference vectors
- **Attention layers** — by applying equivariant attention over site neighborhoods
- **Convolutional networks** — which inherit local equivariance naturally from their structure

They also prove that composing locally equivariant layers preserves the property, enabling deep networks that capture complex dependencies while remaining computationally tractable.

![Figure 2](/iaifi-research-blog/figures/2502_10843/figure_2.png)

## Why It Matters

The physics application in the paper — sampling from the **Ising model** — is a canonical benchmark. The Ising model describes a lattice of binary spins interacting with neighbors, producing the kind of multimodal, correlated distributions that defeat naive MCMC. LEAPS demonstrates correct sampling in high dimensions, validating both the theoretical machinery and the architectural innovations.

But the implications reach well beyond spin systems. Discrete distributions are everywhere: protein sequences, genomic data, combinatorial optimization, language. The field has made spectacular progress on continuous generative models — diffusion, flow matching — but discrete analogues have lagged behind. LEAPS provides the theoretical foundations and practical tools to close that gap.

The locally equivariant architecture is a reusable building block: any application where transitions are local and the state space is structured stands to benefit. Open questions remain — how LEAPS scales to far larger state spaces, whether the framework extends to non-lattice structures like graphs or trees, and whether learned CTMCs can combine with modern sampling techniques to push into genuinely intractable posteriors.

> **Bottom Line:** LEAPS solves a long-standing gap in machine learning by bringing learned measure transport to discrete distributions — using a novel locally equivariant architecture that makes the math tractable and the sampling provably correct.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">LEAPS applies deep learning architecture design to a core problem in statistical physics — constructing efficient samplers for spin models — with theoretical foundations drawn from measure theory and non-equilibrium dynamics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The locally equivariant neural network framework enables scalable parameterization of rate matrices over large discrete state spaces, opening a path for learned discrete generative models with statistical guarantees.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By providing a rigorous, efficient sampler for distributions like the Ising model, LEAPS offers a new computational tool for studying phase transitions, lattice field theories, and other problems in statistical and quantum physics where exact normalization constants are unknown.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend LEAPS to protein design, language, and lattice QCD applications; the paper appeared at ICML 2025 and code is available at github.com/malbergo/leaps.</span></div></div>
</div>
