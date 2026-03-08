---
abstract: We propose a data-driven approach to identifying the functionally independent
  invariants that can be constructed from a tensor with a given symmetry structure.
  Our algorithm proceeds by first enumerating graphs, or tensor networks, that represent
  inequivalent contractions of a product of tensors, computing instances of these
  scalars using randomly generated data, and then seeking linear relations between
  invariants using numerical linear algebra. Such relations yield syzygies, or functional
  dependencies relating different invariants. We apply this approach in an extended
  case study of the independent invariants that can be constructed from an antisymmetric
  $3$-form $H_{μνρ}$ in six dimensions, finding five independent invariants. This
  result confirms that the most general Lagrangian for such a $3$-form, which depends
  on $H_{μνρ}$ but not its derivatives, is an arbitrary function of five variables,
  and we give explicit formulas relating other invariants to the five independent
  scalars in this generating set.
arxivId: '2512.23750'
arxivUrl: https://arxiv.org/abs/2512.23750
authors:
- Athithan Elamaran
- Christian Ferko
- Sterling Scarlett
concepts:
- group theory
- symmetry preservation
- invariant enumeration
- tensor networks
- syzygy detection
- spectral methods
- effective field theory
- quantum field theory
- automated discovery
- monte carlo methods
- string theory
- quantum states
figures:
- /iaifi-research-blog/figures/2512_23750/figure_1.png
- /iaifi-research-blog/figures/2512_23750/figure_1.png
- /iaifi-research-blog/figures/2512_23750/figure_2.png
- /iaifi-research-blog/figures/2512_23750/figure_2.png
- /iaifi-research-blog/figures/2512_23750/figure_3.png
- /iaifi-research-blog/figures/2512_23750/figure_3.png
pdfUrl: https://arxiv.org/pdf/2512.23750v1
published: '2025-12-26T21:22:25+00:00'
theme: Theoretical Physics
title: Machine Learning Invariants of Tensors
wordCount: 981
---

## The Big Picture

Imagine describing the shape of a crystal. No matter how you rotate or flip it, certain properties stay the same: the number of faces, the angles between them, the overall symmetry. These unchanging quantities are called **invariants**, and physicists have been hunting them for over a century.

The problem scales badly. A single electromagnetic field has two independent invariants. A gravitational field in ten dimensions? Dozens, tangled in hidden relationships. Sorting which invariants are truly independent and which are disguised combinations of others has traditionally required years of mathematical heroics.

A team of researchers has automated much of that heroism. Their algorithm uses random sampling, numerical linear algebra, and graph enumeration to discover the independent invariants of any **tensor** (a structured mathematical object, like a matrix but with potentially more dimensions). It turns a centuries-old grind into an overnight computation.

Their test case: an antisymmetric 3-form field in six-dimensional space, a structure prominent in string theory. The algorithm confirmed it has exactly five independent invariants, a result that constrains the entire space of physical theories built from that field.

> **Key Insight:** By generating random instances of a tensor and hunting for linear dependencies between candidate scalars, this algorithm can experimentally identify which invariants are truly independent, turning a hard algebraic problem into a tractable numerical one.

## How It Works

The core idea is elegant: compute two quantities for thousands of random inputs; if some weighted sum always equals zero, the quantities are secretly related. The algorithm runs in three stages.

**Stage 1: Graph enumeration.** Every number computable from a tensor, called a **scalar**, can be drawn as a **tensor network**: a diagram where nodes represent the tensor's components and lines represent pairs of indices being summed. The algorithm systematically enumerates all inequivalent diagrams at each order, building a complete candidate list. For a rank-3 antisymmetric tensor (one where swapping any two indices flips the sign), the count at low orders is manageable. Higher orders grow combinatorially, but the graphs remain systematic.

![Figure 1](/iaifi-research-blog/figures/2512_23750/figure_1.png)

**Stage 2: Numerical evaluation.** For each candidate scalar, the algorithm draws many random instances of the tensor, with components sampled from Gaussian distributions, and computes every invariant for every draw. This produces a large matrix: rows are random samples, columns are candidate invariants.

**Stage 3: Linear algebra.** The team searches for **syzygies**, linear relations of the form $c_1 I_1 + c_2 I_2 + \ldots = 0$ holding across all draws. Numerically, this means finding the **null space** of the data matrix. A nonzero null vector reveals a genuine algebraic identity: one invariant is a combination of the others. When no new independent invariants appear across several consecutive orders, the list is considered complete.

**The 3-form test case.** The team applied the algorithm to an antisymmetric 3-form $H_{\mu\nu\rho}$ in six dimensions. This is not an exotic curiosity; it appears centrally in string theory and supergravity as the **B-field** of the NS-NS (Neveu-Schwarz) sector. The algorithm builds scalars from $H$ three ways:

- **Trace variables**: Multiply copies of $H$ and sum over shared indices using the metric, forming combinations like $H_{\mu\nu\rho}H^{\mu\nu\rho}$ and higher-order versions.
- **Hodge dual variables**: Use the six-dimensional **Levi-Civita symbol** $\epsilon_{\mu\nu\rho\sigma\lambda\kappa}$ to construct a "mirror image" of $H$, then build invariants from that.
- **Spinor variables**: Rewrite the tensor in spinor indices via six-dimensional Weyl matrices, revealing invariants invisible in the original picture.

![Figure 2](/iaifi-research-blog/figures/2512_23750/figure_1.png)

After running the algorithm across all three families, the result was unambiguous: only five invariants are truly independent. All others can be expressed as explicit algebraic functions of these five, with exact formulas provided in the paper.

![Figure 4](/iaifi-research-blog/figures/2512_23750/figure_2.png)

This has immediate consequences. Any **Lagrangian** for a 3-form in six dimensions (the master function from which all equations of motion and physical predictions derive) is a function $L(x_1, x_2, x_3, x_4, x_5)$ of exactly five variables. No more, no less. Theories that look different on the surface may secretly be the same theory in disguise.

## Why It Matters

In **string theory**, understanding the independent invariants of the Riemann tensor in ten dimensions is essential for classifying higher-derivative corrections to supergravity, the so-called $\alpha'$ expansion. Traditional approaches require painstaking manual algebra that experts have labored over for decades. Automating invariant-finding could speed that work up considerably.

In **quantum information**, the independent invariants of a multi-partite quantum state under local unitary transformations are exactly the entanglement measures. Identifying them is the mathematical backbone of classifying what kinds of entanglement are genuinely distinct. The same algorithm, pointed at a different tensor, could push that classification further.

More broadly, the work shows that numerical linear algebra and random sampling can serve as experimental tools in pure mathematics. Not approximations, but hypothesis generators later confirmed analytically. That's a mode of doing mathematics that deserves more attention.

> **Bottom Line:** By treating invariant theory as a data problem, this team confirmed that a 6D antisymmetric 3-form has exactly five independent invariants and built a reusable algorithm that can answer the same question for any tensor, with applications in string theory, quantum information, and algebraic geometry.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies machine learning techniques (random sampling and numerical linear algebra) to a fundamental problem in mathematical physics, showing how data-driven methods can make progress on questions in pure theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The algorithm provides a general-purpose tool for automated symbolic discovery, showing that neural-network-free ML methods can solve open problems in algebraic geometry and invariant theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By confirming that the most general 3-form Lagrangian in six dimensions depends on exactly five variables, the work constrains the space of string-inspired effective field theories and clarifies B-field dynamics in supergravity.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future applications include classifying invariants of the Riemann tensor for higher-derivative gravity and mapping entanglement invariants in quantum information; the full paper is available at [arXiv:2512.23750](https://arxiv.org/abs/2512.23750).</span></div></div>
</div>
