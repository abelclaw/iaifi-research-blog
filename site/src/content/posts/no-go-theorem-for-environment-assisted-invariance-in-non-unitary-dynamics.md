---
abstract: We elucidate the requirements for quantum operations that achieve environment-assisted
  invariance (envariance), a symmetry of entanglement. While envariance has traditionally
  been studied within the framework of local unitary operations, we extend the analysis
  to consider non-unitary local operations. First, we investigate the conditions imposed
  on operators acting on pure bipartite entanglement to attain envariance. We show
  that the local operations must take a direct-sum form in their Kraus operator representations,
  establishing decoherence-free subspaces. Furthermore, we prove that this also holds
  for the multipartite scenario. As an immediate consequence, we demonstrate that
  environment-assisted shortcuts to adiabaticity cannot be achieved through non-unitary
  operations. In addition, we show that the static condition of the eternal black
  hole in AdS/CFT is violated when the CFTs are coupled to the external baths.
arxivId: '2503.10400'
arxivUrl: https://arxiv.org/abs/2503.10400
authors:
- Akira Sone
- Akram Touil
- Kenji Maeda
- Paola Cappellaro
- Sebastian Deffner
concepts:
- envariance
- quantum states
- entanglement
- decoherence-free subspaces
- open quantum systems
- shortcuts to adiabaticity
- symmetry breaking
- conformal field theory
- quantum computing
- quantum field theory
figures:
- /iaifi-research-blog/figures/2503_10400/figure_1.png
- /iaifi-research-blog/figures/2503_10400/figure_1.png
- /iaifi-research-blog/figures/2503_10400/figure_2.png
- /iaifi-research-blog/figures/2503_10400/figure_2.png
- /iaifi-research-blog/figures/2503_10400/figure_3.png
- /iaifi-research-blog/figures/2503_10400/figure_3.png
pdfUrl: https://arxiv.org/pdf/2503.10400v3
published: '2025-03-13T14:24:47+00:00'
theme: Theoretical Physics
title: No-go theorem for environment-assisted invariance in non-unitary dynamics
wordCount: 1183
---

## The Big Picture

Imagine trying to perfectly reverse a magic trick, not just the visible part, but the hidden mechanism too. In quantum mechanics, this idea has a precise name: **envariance**, or environment-assisted invariance. If you disturb a quantum particle, the environment surrounding it can silently undo that disturbance without anyone touching the particle again.

Physicist Wojciech Zurek introduced envariance to derive one of quantum mechanics' most fundamental results: **Born's rule**, which tells us the probability of a measurement outcome. What are the odds of finding a particle at a given location when you look for it? Born's rule provides the answer.

Until now, physicists assumed this reversal trick required perfect, lossless operations, the mathematical equivalent of frictionless gears. Real quantum systems are messy. They leak energy, couple to heat baths and fluctuating electromagnetic fields, and gradually lose **quantum coherence**, the delicate superposition of states that underlies all quantum behavior.

Can envariance survive when operations are noisy and irreversible? A team from UMass Boston, Los Alamos National Laboratory, MIT, and the University of Maryland set out to find out. Their answer is a mathematically proven no, with consequences for quantum control and the physics of black holes.

> **Key Insight:** Imperfect, irreversible operations (the kind found in any real physical system) can only achieve envariance within a very special protected corner of quantum state space. This single constraint rules out entire classes of quantum control strategies once thought possible.

## How It Works

The researchers started with the standard definition of envariance. A quantum state of system S entangled with environment E is envariant under an operation on S if there exists a compensating operation on E alone that restores the original state. Apply Φ_S to the system, then find a Φ_E that undoes the damage, without touching S again.

For unitary operations (reversible, energy-conserving), the compensating maps are well understood. System and environment swap phases in a symmetric dance dictated by the **Schmidt decomposition**, the unique way to write any entangled two-part quantum state as a sum of matched pairs.

![Figure 1](/iaifi-research-blog/figures/2503_10400/figure_1.png)

The new paper extends this to **CPTP maps**: completely positive, trace-preserving operations that represent the most general physically allowed quantum processes, including noise, measurement, and dissipation. These are described using **Kraus operators**, a mathematical toolkit for encoding how a quantum state transforms under open dynamics. The central technical result is a proof of what form Kraus operators must take for envariance to hold.

The answer is quite restrictive. For envariance to work under non-unitary dynamics, the Kraus operators must decompose as a direct sum, meaning each piece of the quantum state evolves in complete isolation with no mixing between pieces. In concrete terms:

- The operation must partition the **Hilbert space** (the full mathematical arena of all possible quantum states) into independent blocks
- Each block evolves completely independently, with no mixing between them
- This is precisely the condition defining a **decoherence-free subspace** (DFS): a protected corner of state space immune to environmental noise

A DFS arises only when the environment interacts with the system in a highly symmetric way. Generic open dynamics, the kind encountered in any real lab, destroys this structure.

![Figure 2](/iaifi-research-blog/figures/2503_10400/figure_1.png)

So envariance under non-unitary operations isn't merely difficult. It is structurally impossible in generic open systems.

The team also proved this extends from two-part (bipartite) systems to multipartite systems with arbitrarily many entangled subsystems, confirming the constraint is universal and not an artifact of simplified two-body physics.

## Why It Matters

The first consequence hits environment-assisted **shortcuts to adiabaticity**. These are techniques that drive a quantum system from one state to another quickly, without the errors that come from moving too fast. Previous work proposed engineering the environment's dynamics to achieve these shortcuts through envariant maps acting on E rather than directly on S. The idea was appealing: instead of delicately operating on a fragile qubit, outsource the hard work to its environment.

The no-go theorem kills this strategy for non-unitary dynamics. If your environment interacts dissipatively with the system (as real environments inevitably do), the envariance condition cannot be satisfied and the shortcut collapses. No loopholes; the math is airtight.

![Figure 3](/iaifi-research-blog/figures/2503_10400/figure_2.png)

The second implication lands in a very different part of physics: the **eternal black hole** in Anti-de Sitter space, a theoretical curved spacetime central to high-energy physics. The **AdS/CFT correspondence** maps a black hole in (d+1)-dimensional gravity to a pair of coupled quantum field theories (CFTs) living on the boundary. Maintaining the eternal black hole requires these two boundary CFTs to stay in a specific entangled state, upheld by a symmetry condition that the authors show is equivalent to envariance.

When those CFTs couple to external thermal baths, the envariance condition breaks, the symmetry fails, and the static black hole geometry cannot be maintained.

![Figure 4](/iaifi-research-blog/figures/2503_10400/figure_2.png)

This ties quantum information theory to a basic question in theoretical physics: how does classical spacetime geometry emerge from quantum entanglement? The answer, it turns out, depends on whether quantum operations preserve the right kind of symmetry.

> **Bottom Line:** Non-unitary operations can only achieve envariance within decoherence-free subspaces, a condition almost never met in real open systems. This rules out environment-assisted shortcuts to adiabaticity in dissipative dynamics and shows that the eternal black hole geometry in AdS/CFT cannot survive coupling to realistic baths.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work unifies quantum information theory, open quantum systems, and quantum gravity by proving that a single symmetry condition (envariance) constrains dynamics across all three domains simultaneously.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The decoherence-free subspace constraint directly informs the design of quantum error correction protocols and quantum generative models, establishing a fundamental limit on environment-assisted quantum control strategies relevant to near-term quantum hardware.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By showing that external dissipation violates the static condition of the eternal black hole in AdS/CFT, the paper provides a concrete quantum-information diagnostic for when classical spacetime geometry breaks down.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will explore whether approximate or weaker forms of envariance can survive realistic noise models and what this implies for holographic entanglement. See [arXiv:2503.10400](https://arxiv.org/abs/2503.10400) for the full technical treatment.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">No-go theorem for environment-assisted invariance in non-unitary dynamics</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2503.10400</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Akira Sone", "Akram Touil", "Kenji Maeda", "Paola Cappellaro", "Sebastian Deffner"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We elucidate the requirements for quantum operations that achieve environment-assisted invariance (envariance), a symmetry of entanglement. While envariance has traditionally been studied within the framework of local unitary operations, we extend the analysis to consider non-unitary local operations. First, we investigate the conditions imposed on operators acting on pure bipartite entanglement to attain envariance. We show that the local operations must take a direct-sum form in their Kraus operator representations, establishing decoherence-free subspaces. Furthermore, we prove that this also holds for the multipartite scenario. As an immediate consequence, we demonstrate that environment-assisted shortcuts to adiabaticity cannot be achieved through non-unitary operations. In addition, we show that the static condition of the eternal black hole in AdS/CFT is violated when the CFTs are coupled to the external baths.</span></div></div>
</div>
