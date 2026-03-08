---
abstract: Discovering conservation laws for a given dynamical system is important
  but challenging. In a theorist setup (differential equations and basis functions
  are both known), we propose the Sparse Invariant Detector (SID), an algorithm that
  auto-discovers conservation laws from differential equations. Its algorithmic simplicity
  allows robustness and interpretability of the discovered conserved quantities. We
  show that SID is able to rediscover known and even discover new conservation laws
  in a variety of systems. For two examples in fluid mechanics and atmospheric chemistry,
  SID discovers 14 and 3 conserved quantities, respectively, where only 12 and 2 were
  previously known to domain experts.
arxivId: '2305.19525'
arxivUrl: https://arxiv.org/abs/2305.19525
authors:
- Ziming Liu
- Patrick Obin Sturm
- Saketh Bharadwaj
- Sam Silva
- Max Tegmark
concepts:
- conservation laws
- sparse invariant detection
- sparse models
- automated discovery
- eigenvalue decomposition
- interpretability
- null space enumeration
- hamiltonian systems
- inverse problems
- symmetry preservation
- scientific workflows
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2305_19525/figure_1.png
- /iaifi-research-blog/figures/2305_19525/figure_1.png
- /iaifi-research-blog/figures/2305_19525/figure_2.png
- /iaifi-research-blog/figures/2305_19525/figure_2.png
- /iaifi-research-blog/figures/2305_19525/figure_3.png
- /iaifi-research-blog/figures/2305_19525/figure_3.png
pdfUrl: https://arxiv.org/pdf/2305.19525v3
published: '2023-05-31T03:26:18+00:00'
theme: Foundational AI
title: Discovering New Interpretable Conservation Laws as Sparse Invariants
wordCount: 946
---

## The Big Picture

Imagine watching a pendulum swing. Without measuring anything, you know its total energy never changes. That invisible constant, unchanged while everything else moves, is a conservation law. In physics, these laws are gold.

They're the skeleton of every theory, from planetary orbits to particle physics. Energy, momentum, angular momentum: these aren't textbook definitions. They're rules the universe refuses to break.

For complex systems (a swirling fluid, a soup of reacting atmospheric chemicals) finding those rules is brutally hard. Researchers have spent decades doing it by hand, guided by intuition and mathematical muscle. Machine learning has tried to help, but most approaches treat conservation laws as outputs of black-box neural networks: technically impressive, nearly impossible to trust. What good is a conserved quantity if you can't write it down?

A team from MIT and collaborators built the **Sparse Invariant Detector**, or SID, to automate this discovery and produce clean, readable symbolic formulas. The payoff is concrete: SID found conservation laws that human experts had missed.

> **Key Insight:** SID reduces conservation law discovery to a linear algebra problem, making results both mathematically guaranteed and human-readable. It uncovered previously unknown conserved quantities in two real scientific systems.

## How It Works

A conserved quantity *H(x)* must satisfy one condition: as the system evolves, *H* cannot change. In math: ∇*H* · f(x) = 0. This is not a new observation. What SID does is exploit it cleverly.

![Figure 1](figure:1)

Rather than training a neural network, SID expresses *H* as a **linear combination of basis functions**, mathematical building blocks like polynomials or trigonometric terms that domain experts suspect might appear in the answer. With that assumption, the conservation condition becomes a system of linear equations. Computers solve linear equations exactly, without risk of getting stuck at imperfect solutions.

The workflow:

1. **Construct the matrix G.** For each basis function and each sampled point in phase space, compute how the basis function changes along the system's trajectory. Stack these into a matrix.
2. **Find the null space via SVD.** Apply **singular value decomposition** to G. The null space (directions where the matrix produces exactly zero output) yields valid conserved quantities. Its dimension tells you exactly how many independent conservation laws exist.
3. **Sparsify for interpretability.** The null space basis isn't unique. SID applies L1 minimization over orthogonal rotations to find the sparsest representation, turning a dense algebraic mess into a clean formula with only a few nonzero terms.
4. **Check functional independence.** A final Jacobian-rank check confirms the discovered laws are genuinely distinct, not disguised versions of each other.

The result is a complete, independent, and interpretable set of conserved quantities. Prior methods struggled to guarantee all three at once.

![Figure 2](figure:2)

## Why It Matters

SID's sharpest results come from outside pure physics.

In 2D and 3D fluid mechanics, SID analyzed the vorticity equations governing how rotation in a fluid evolves. Domain experts knew of 12 conserved quantities for 3D flow. SID found 14.

![Figure 3](figure:3)

The two new ones weren't exotic. In hindsight, experts called them "somewhat expected." But finding them by hand would have taken months. SID found them in seconds.

The atmospheric chemistry case is even more revealing. Applied to a simplified chemical network modeling atmospheric reactions, SID found 3 conserved quantities where experts knew of 2. The third was unintended by the model designers: an accidental algebraic structure in how the equations were written, a hidden constraint nobody had searched for because nobody thought to look.

![Figure 4](figure:4)

This has practical consequences. If you're simulating a system numerically and don't know it has an extra conserved quantity, your simulation may drift in ways you can't explain. SID catches these hidden structures automatically.

The approach deliberately restricts itself to linear methods, plus one sparsification step, because that limitation makes its outputs trustworthy. Every result is a formula. Every formula can be checked by hand.

![Figure 5](figure:5)

Scientists still bring domain knowledge: choosing basis functions, formulating the hypothesis space, interpreting results. SID handles the exhaustive symbolic search, which is exactly the kind of tedious, systematic work where computers outperform humans.

SID currently works in what the authors call the "theorist" setup, where the governing equations are already known. Extending it toward a data-only setting, where you have observations but no equations, remains open. Hybrid approaches that use neural networks to learn equations first, then feed them to SID, are a natural next step. There's also the deeper question of Noether's theorem, which links every conservation law to an underlying symmetry of nature. Could SID's discoveries reverse-engineer hidden symmetries in physical systems?

![Figure 6](figure:6)

> **Bottom Line:** SID is a simple, linear-algebraic algorithm that discovers conservation laws guaranteed to be complete, independent, and interpretable. It already found new conserved quantities in fluid mechanics and atmospheric chemistry that experts had missed.

---

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work brings together symbolic AI, linear algebra, and physics by turning conservation law discovery into a sparse null-space problem, showing that mathematical rigor and machine automation can work hand in hand across fluid mechanics and atmospheric chemistry.
- **Impact on Artificial Intelligence:** SID shows that deliberately simple, interpretable algorithms can outperform black-box neural networks for structured scientific discovery tasks, offering a template for trustworthy AI in high-stakes research settings.
- **Impact on Fundamental Interactions:** By discovering previously unknown conserved quantities in real physical and chemical systems, SID provides a new automated tool for probing the deep mathematical structure of dynamical systems in physics and beyond.
- **Outlook and References:** Future work may extend SID toward data-driven settings and connect its discoveries to Noether's theorem and hidden symmetry detection; the full paper is available at [arXiv:2305.19525](https://arxiv.org/abs/2305.19525).
