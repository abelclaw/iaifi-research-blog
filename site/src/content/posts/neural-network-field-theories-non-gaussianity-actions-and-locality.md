---
abstract: Both the path integral measure in field theory and ensembles of neural networks
  describe distributions over functions. When the central limit theorem can be applied
  in the infinite-width (infinite-$N$) limit, the ensemble of networks corresponds
  to a free field theory. Although an expansion in $1/N$ corresponds to interactions
  in the field theory, others, such as in a small breaking of the statistical independence
  of network parameters, can also lead to interacting theories. These other expansions
  can be advantageous over the $1/N$-expansion, for example by improved behavior with
  respect to the universal approximation theorem. Given the connected correlators
  of a field theory, one can systematically reconstruct the action order-by-order
  in the expansion parameter, using a new Feynman diagram prescription whose vertices
  are the connected correlators. This method is motivated by the Edgeworth expansion
  and allows one to derive actions for neural network field theories. Conversely,
  the correspondence allows one to engineer architectures realizing a given field
  theory by representing action deformations as deformations of neural network parameter
  densities. As an example, $φ^4$ theory is realized as an infinite-$N$ neural network
  field theory.
arxivId: '2307.03223'
arxivUrl: https://arxiv.org/abs/2307.03223
authors:
- Mehmet Demirtas
- James Halverson
- Anindita Maiti
- Matthew D. Schwartz
- Keegan Stoner
concepts:
- nn-ft correspondence
- quantum field theory
- connected correlators
- edgeworth expansion
- stochastic processes
- effective field theory
- symmetry breaking
- density estimation
- bayesian inference
- renormalization
- kernel methods
figures: []
pdfUrl: https://arxiv.org/pdf/2307.03223v2
published: '2023-07-06T18:00:01+00:00'
theme: Theoretical Physics
title: 'Neural Network Field Theories: Non-Gaussianity, Actions, and Locality'
wordCount: 1034
---

## The Big Picture

Imagine describing a turbulent ocean two ways: write down the fundamental equations governing every swirl and eddy, or simulate it as an enormous ensemble of tiny interacting particles and let collective statistics do the work. These sound completely different — yet under the right conditions, they describe exactly the same physics.

Researchers at IAIFI have been exploring this situation, not for oceans but for quantum fields and neural networks. Both systems, at their core, are machines for generating random functions. A neural network, when its parameters are randomized at initialization, produces a random function mapping inputs to outputs. A **quantum field theory** — physics' framework for describing particles and forces — uses a sum over all possible field configurations to produce a distribution over the shapes that field can take. The question the authors ask is deceptively simple: when are these two descriptions the same thing?

The team — Mehmet Demirtas, James Halverson, Anindita Maiti, Matthew Schwartz, and Keegan Stoner — has built a systematic mathematical bridge between neural network architecture and the **action functionals** of field theory, complete with new Feynman diagram rules and a concrete realization of φ⁴ theory using an infinite-width neural network.

> **Key Insight:** By treating neural networks as probability distributions over functions, the researchers show you can read off a field theory's governing equations directly from measurements of how network outputs relate to each other — and, running the logic backward, engineer a network architecture that *is* a given field theory.

## How It Works

The story begins with the **Central Limit Theorem (CLT)** — the bedrock result that sums of many independent random quantities converge to a Gaussian distribution. In neural networks, the infinite-width limit (where neuron count N → ∞) is exactly the CLT regime. Each neuron contributes a tiny random piece; their sum is Gaussian. In field theory language, a Gaussian distribution over functions is a **free field theory** — one with no interactions. This is the **Neural Network / Gaussian Process (NNGP) correspondence**: infinite-width networks are free field theories.

Free field theories are boring — the real world has interactions. The paper explores two routes to introduce them:

- **The 1/N expansion:** Work at finite width. The CLT breaks down in a controlled way, and corrections at each order in 1/N introduce **connected correlators** — statistics capturing genuine interdependencies between network outputs, beyond what a Gaussian predicts. These correspond to interaction vertices in field theory.
- **Independence breaking:** Keep N large but allow network parameters to develop correlations, violating the statistical independence the CLT requires. This subtler deformation can outperform the 1/N expansion with respect to the **universal approximation theorem**, meaning the resulting field theories can represent a wider class of target functions.

Once non-Gaussianities are generated by either method, the key challenge is: given the correlators, what is the action? The team's answer uses the **Edgeworth expansion** — a classical statistics tool for describing near-Gaussian distributions as a series of corrections built from Hermite polynomials, each capturing a specific type of deviation from a bell curve. Each term in the expansion maps onto a contribution to the action.

The new Feynman diagram prescription is where things get elegant. Normally, Feynman diagrams have vertices defined by coupling constants in the action. Here, the authors flip the logic: **the vertices are the connected correlators themselves**. You measure how the field's statistics at different points are wired together — **n-point functions** — draw the corresponding diagrams, and reconstruct the action order by order. It's Feynman rules built from network statistics rather than a Lagrangian written from first principles.

As a concrete demonstration, they work through **non-local φ⁴ theory** — the quartic interaction ubiquitous in particle physics and statistical mechanics, but with couplings that depend on position in a non-local way. This non-locality arises naturally from the neural network construction, where the Gaussian process kernel introduces spatial structure.

## Why It Matters

The ability to engineer network architectures that realize specific field theories is more than mathematical curiosity. φ⁴ theory appears in the Higgs mechanism, in models of phase transitions, and as a testbed for renormalization group methods. Having a neural network that *is* φ⁴ theory — not an approximation — opens the door to studying field theory phenomena using ML tools: optimization, gradient descent, generative modeling.

Running in the other direction, the correspondence gives physicists a new vocabulary for understanding what neural networks actually compute. The **locality** question is particularly important: physical field theories are local (interactions happen at the same spacetime point), but neural network field theories generically produce non-local actions. The paper analyzes when locality emerges, connecting to the **cluster decomposition principle** — the foundational requirement that distant experiments be statistically independent. Understanding when a neural network satisfies cluster decomposition is a step toward knowing when ML-based approaches to physics capture genuine physical structure.

The framework also points toward a constructive program: rather than discovering field theories by guessing Lagrangians, one might design network architectures encoding desired symmetries and interactions, then train them. This paper provides the dictionary for that translation.

> **Bottom Line:** Neural networks and quantum field theories speak the same mathematical language, and this paper hands you the translation guide — complete with Feynman rules built from network statistics and a proof-of-concept realization of φ⁴ theory as an infinite-width neural network.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work establishes an explicit, bidirectional dictionary between neural network architecture and quantum field theory, enabling ideas from each domain to inform the other with mathematical precision.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces independence breaking as a new expansion scheme that can outperform the standard 1/N expansion under the universal approximation theorem, along with a systematic method for deriving network statistics from a desired target distribution.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By realizing φ⁴ theory as an infinite-N neural network field theory and analyzing conditions for locality and cluster decomposition, this work provides new tools for constructing and studying interacting quantum field theories through an ML lens.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending the framework to gauge theories and studying renormalization group flows within the correspondence; the full paper is available on arXiv (2307.03223).</span></div></div>
</div>
