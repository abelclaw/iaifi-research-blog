---
abstract: We realize bosonic string theory with ensembles of infinite width neural
  networks. The string tension is tuned by the variance of the output weights. The
  construction provides a new computation of the foundational Virasoro-Shapiro and
  Veneziano amplitudes as neural network correlators.
arxivId: '2601.06249'
arxivUrl: https://arxiv.org/abs/2601.06249
authors:
- Samuel Frank
- James Halverson
concepts:
- string theory
- neural network field theory
- conformal field theory
- scattering amplitudes
- neural network gaussian process
- infinite width limit
- quantum field theory
- stochastic processes
- symmetry preservation
- ensemble methods
figures: []
pdfUrl: https://arxiv.org/pdf/2601.06249v1
published: '2026-01-09T19:00:01+00:00'
theme: Theoretical Physics
title: String Theory from Infinite Width Neural Networks
wordCount: 974
---

## The Big Picture

Imagine training a neural network so wide (so many neurons per layer) that it stops behaving like a neural network and starts behaving like a physical field, the mathematical object physicists use to describe forces and particles. This isn't a metaphor. It's a theorem, and researchers at Northeastern University are using it to do something that sounds impossible: build string theory out of neural networks.

String theory proposes that the fundamental constituents of reality are tiny vibrating strings rather than point particles, and it remains one of the few candidates for reconciling quantum mechanics with gravity. Computing how strings interact requires elaborate mathematical machinery physicists have spent decades developing. Yet Samuel Frank and James Halverson have now shown you can reproduce those results by computing the statistics of carefully designed neural networks, deriving the foundational **Veneziano** and **Virasoro-Shapiro amplitudes**, the cornerstone formulas predicting string scattering probabilities, directly from network statistics.

> **Key Insight:** The variance of a neural network's output weights directly controls string tension. Tune one hyperparameter in your network, and you tune the fundamental physical scale of the strings.

## How It Works

The bridge rests on a deep result from machine learning theory. Send a neural network's width to infinity and its outputs become draws from a **Gaussian process**, a random function fully characterized by a probability distribution. This is the **Neural Network Gaussian Process (NNGP) correspondence**, and it means an infinite-width network's statistics are completely described by a free field theory. Frank and Halverson's work builds on the **Neural Network Field Theory (NN-FT)** program, which exploits this correspondence not for machine learning, but for physics.

Bosonic string theory, after fixing coordinates on the string's surface, has two ingredients: the **free boson** (describing string motion through spacetime) and the **bc-ghost system** (additional fields required to keep the equations consistent once that coordinate choice is made). The researchers built explicit architectures for both:

- **Free boson architecture:** Each spacetime coordinate $X^\mu(z)$ is a sum over $N$ neurons, each contributing a cosine of a complex frequency $W_i$ and random phase $c_i$, weighted by Gaussian output weights $a^\mu_i$. Frequencies are drawn uniformly from an annular region in the complex plane, bounded by IR cutoff $\epsilon$ and UV cutoff $\Lambda$.
- **Ghost architecture:** The $b$ and $c$ ghost fields are represented by **Grassmann-valued networks**, networks whose weights obey anticommuting arithmetic, the mathematical structure required for fermions, using analogous random-phase constructions.

Averaging over the free boson network's random parameters recovers the standard string propagator exactly: a logarithm of the separation $|z - w|$ in position space, a $1/p^2$ scaling in momentum space. The only non-regulator parameter is $\sigma_a$, the output weight standard deviation. This single number fixes the **Regge slope** $\alpha' = \sigma_a^2 / (\Lambda^2 - \epsilon^2)$ and therefore the string tension $T \sim 1/\alpha'$. One dial stretches or compresses the strings.

The ghost system follows the same logic with Grassmann variables replacing real numbers. Averaging over those fermionic weights recovers the $\langle bc \rangle$ propagator, the $1/(z-w)$ pole every string theorist recognizes, up to corrections that vanish as the UV cutoff grows.

With both components built, string scattering becomes a computation in network correlators. **Vertex operators** encode the quantum state of each incoming and outgoing string as insertions in the network's output. The four-point tachyon amplitude, integrated over the worldsheet (the two-dimensional surface a string sweeps through spacetime), becomes an integral over the network's parameter space. That integral produces the Veneziano amplitude: a ratio of gamma functions with characteristic crossing symmetry and Regge behavior, where high-energy scattering is exponentially soft rather than power-law divergent. The closed-string version yields the Virasoro-Shapiro amplitude. Both emerge cleanly from the network formalism.

## Why It Matters

This result pulls in two directions at once. For string theory, it offers a genuinely new computational perspective. Standard derivations live in the language of conformal field theory and path integrals. Frank and Halverson's derivation lives in the language of random functions and covariance kernels, a completely different toolkit that may illuminate corners of the theory the standard approach obscures. That $\alpha'$ is controlled by a single variance parameter makes the physical interpretation unusually transparent: string theory's fundamental length scale is literally the spread of a weight distribution.

For the NN-FT program, this is a landmark result. Previous work had realized free scalars, free fermions, supersymmetric theories, and conformal field theories in this framework. Realizing string theory, a theory of quantum gravity, represents a significant leap in complexity.

The result raises immediate questions. If bosonic string theory lives here, where do superstring theories live? What does finite-width physics look like, and does it correspond to string interactions? The researchers note their work is largely complementary to independent work by Robinson on neural network realizations of Virasoro symmetry, suggesting the field is converging on something genuinely deep.

> **Bottom Line:** A neural network's weight variance controls string tension, meaning string theory's foundational scattering amplitudes can be computed as nothing more than the statistics of a well-chosen random function, opening an entirely new computational and conceptual window into quantum gravity.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This paper builds a direct mathematical bridge between machine learning theory (the NNGP correspondence for infinite-width networks) and string theory, showing that the two languages describe the same physics.
- **Impact on Artificial Intelligence:** The Neural Network Field Theory program shows that infinite-width network statistics encode rich physical structure, deepening the theoretical foundations of why certain neural network architectures behave as they do.
- **Impact on Fundamental Interactions:** By deriving the Veneziano and Virasoro-Shapiro amplitudes from neural network correlators, the work provides a new computational route into string theory and quantum gravity.
- **Outlook and References:** Future directions include extending the construction to superstring theories, exploring finite-width corrections as string interactions, and connecting this framework to broader questions in quantum gravity; see [arXiv:2601.06249](https://arxiv.org/abs/2601.06249).
