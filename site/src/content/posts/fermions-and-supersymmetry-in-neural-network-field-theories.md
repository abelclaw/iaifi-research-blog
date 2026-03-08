---
abstract: We introduce fermionic neural network field theories via Grassmann-valued
  neural networks. Free theories are obtained by a generalization of the Central Limit
  Theorem to Grassmann variables. This enables the realization of the free Dirac spinor
  at infinite width and a four fermion interaction at finite width. Yukawa couplings
  are introduced by breaking the statistical independence of the output weights for
  the fermionic and bosonic fields. A large class of interacting supersymmetric quantum
  mechanics and field theory models are introduced by super-affine transformations
  on the input that realize a superspace formalism.
arxivId: '2511.16741'
arxivUrl: https://arxiv.org/abs/2511.16741
authors:
- Samuel Frank
- James Halverson
- Anindita Maiti
- Fabian Ruehle
concepts:
- quantum field theory
- grassmann neural networks
- neural network field theory
- supersymmetric field theory
- stochastic processes
- symmetry breaking
- group theory
- renormalization
- monte carlo methods
- conformal field theory
figures: []
pdfUrl: https://arxiv.org/pdf/2511.16741v1
published: '2025-11-20T19:00:05+00:00'
theme: Theoretical Physics
title: Fermions and Supersymmetry in Neural Network Field Theories
wordCount: 1164
---

## The Big Picture

Bosons (photons, Higgs bosons) are sociable: they pile into the same quantum state without complaint. Fermions (electrons, quarks, neutrinos) are antisocial loners. No two fermions can occupy the same quantum state at once, a rule called the Pauli exclusion principle. This single distinction drives the structure of chemistry, nuclear physics, and the universe itself.

For years, physicists have known that wide neural networks share deep mathematical similarities with quantum field theories, the language physicists use to describe particles and forces. But this connection described only bosons. Fermions, with their rule that swapping any two of them flips the sign of the entire expression, seemed out of reach.

A new [paper](https://arxiv.org/abs/2511.16741) by Samuel Frank, James Halverson, Anindita Maiti, and Fabian Ruehle closes that gap. They introduce fully fermionic neural network field theories, then go further: they show how to build **supersymmetry**, a proposed symmetry of nature pairing every boson with a fermion partner, directly into neural network architecture.

> **Key Insight:** By replacing ordinary numbers in neural networks with Grassmann variables, the anticommuting "numbers" that describe fermions, the team proves that neural networks can realize fermionic quantum field theories, including interactions and supersymmetry, purely from their statistical structure.

## How It Works

The foundation is a celebrated result from the 1990s: in the infinite-width limit, a randomly initialized neural network becomes a **Gaussian process**, a probability distribution over functions determined entirely by its mean and correlations. Physicists recognized this as equivalent to a **free field theory**, the quantum field theory of non-interacting particles. Finite-width corrections introduce interactions. This is the NN-FT correspondence.

Gaussian processes describe bosons, though. Fermions require **Grassmann variables**, exotic mathematical objects that anticommute: if η and ξ are Grassmann numbers, then ηξ = −ξη. Swapping the order flips the sign, and that single property encodes everything strange about fermionic statistics.

The central mathematical result is a **Grassmann Central Limit Theorem**. In ordinary probability theory, summing many independent random variables produces a Gaussian distribution. The authors prove the analogous statement for Grassmann-valued random variables: a scaled sum of N independent, identically distributed Grassmann variables converges to a Gaussian Grassmann distribution as N → ∞. Free fermionic field theories then follow immediately as infinite-width limits of Grassmann-valued neural networks.

With this in hand, the team constructs **Grassmann neural network field theories** in two ways:

- **Grassmann weights:** Output layer weights are drawn from Grassmann-valued distributions; hidden layer computations remain ordinary
- **Grassmann post-activations:** Intermediate network features are Grassmann-valued, flowing into the outputs

Both constructions yield free fermionic theories at infinite width. Finite-width corrections generate interactions, the same mechanism that produces interacting bosonic theories in the standard NN-FT framework, now applied to fermions.

What does this buy you physically? The team explicitly realizes the **free Dirac spinor**, the field theory describing free electrons and quarks, at infinite width. At finite width, they find a **four-fermion interaction**, a direct contact interaction that shows up in many models of nuclear and particle physics.

They also introduce **Yukawa couplings**, the interactions between fermionic and bosonic fields responsible for giving particles mass through the Higgs mechanism in the Standard Model. These arise by correlating the weight distributions of the fermionic and bosonic sectors: a straightforward architectural choice with rich physical consequences.

The most ambitious part of the paper reaches for supersymmetry. Implementing SUSY requires **superspace**, a geometric arena with both ordinary and Grassmann-valued coordinates that lets bosons and fermions live in a single framework. The team realizes superspace via **super-affine transformations** on the network's inputs: coordinate changes that mix ordinary inputs with Grassmann-valued inputs according to superspace geometry.

Networks built this way automatically satisfy the **Ward identities** of supersymmetry, the mathematical consistency conditions confirming a theory genuinely has the symmetry, without any fine-tuning. From this single architectural choice, the team constructs a broad class of supersymmetric quantum mechanics and supersymmetric field theory models, including models with supersymmetry breaking, where the symmetry is present in the theory's structure but absent from its ground state.

## Why It Matters

For theoretical physics, this is a new constructive tool for building and studying fermionic and supersymmetric field theories. The parameter-space formulation, where expectation values are computed by sampling neural network weights rather than evaluating path integrals, gives a genuinely different computational handle. Monte Carlo sampling of randomly initialized Grassmann networks could give access to fermionic correlators in interacting theories that are otherwise hard to compute.

For machine learning, the results show that neural network architecture contains far more physics than previously appreciated. Yukawa couplings emerge from weight correlations. Supersymmetry emerges from super-affine input transformations. High-level physical symmetries can be encoded at the level of initialization and architecture, before any training happens. This raises questions about whether supersymmetric inductive biases could improve learning in specific domains, or whether fermionic weight statistics might offer new regularization mechanisms.

The work also deepens a broader program treating neural networks as a laboratory for field theory, complementary to lattice methods and perturbation theory, and potentially capable of probing strongly coupled, finite-N regimes with specific symmetry constraints that are difficult to access by other means.

> **Bottom Line:** Frank, Halverson, Maiti, and Ruehle have extended the neural network–field theory correspondence to fermions and supersymmetry, proving that Grassmann-valued neural networks realize free and interacting fermionic theories and that supersymmetric architectures naturally encode SUSY Ward identities.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work establishes a rigorous mathematical connection between neural network theory and fermionic quantum field theory, showing that deep learning architectures can natively encode the anticommuting statistics of fundamental particles and the symmetries relating them to bosons.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces Grassmann-valued neural networks as a new class of architecture with provable connections to fermionic statistics, suggesting directions for physically motivated inductive biases and novel approaches to sampling and representation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By realizing the free Dirac spinor, Yukawa couplings, four-fermion interactions, and a broad class of supersymmetric models within the neural network framework, the work provides new computational tools for studying fermionic and supersymmetric field theories.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include Monte Carlo studies of interacting fermionic NN-FTs, exploration of supersymmetry breaking patterns, and connections to lattice field theory methods; the paper by Frank, Halverson, Maiti, and Ruehle is available at [arXiv:2511.16741](https://arxiv.org/abs/2511.16741).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Fermions and Supersymmetry in Neural Network Field Theories</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2511.16741](https://arxiv.org/abs/2511.16741)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Samuel Frank", "James Halverson", "Anindita Maiti", "Fabian Ruehle"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We introduce fermionic neural network field theories via Grassmann-valued neural networks. Free theories are obtained by a generalization of the Central Limit Theorem to Grassmann variables. This enables the realization of the free Dirac spinor at infinite width and a four fermion interaction at finite width. Yukawa couplings are introduced by breaking the statistical independence of the output weights for the fermionic and bosonic fields. A large class of interacting supersymmetric quantum mechanics and field theory models are introduced by super-affine transformations on the input that realize a superspace formalism.</span></div></div>
</div>
