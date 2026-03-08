---
abstract: 'Integrable partial differential equation (PDE) systems are of great interest
  in natural science, but are exceedingly rare and difficult to discover. To solve
  this, we introduce OptPDE, a first-of-its-kind machine learning approach that Optimizes
  PDEs'' coefficients to maximize their number of conserved quantities, $n_{\rm CQ}$,
  and thus discover new integrable systems. We discover four families of integrable
  PDEs, one of which was previously known, and three of which have at least one conserved
  quantity but are new to the literature to the best of our knowledge. We investigate
  more deeply the properties of one of these novel PDE families, $u_t = (u_x+a^2u_{xxx})^3$.
  Our paper offers a promising schema of AI-human collaboration for integrable system
  discovery: machine learning generates interpretable hypotheses for possible integrable
  systems, which human scientists can verify and analyze, to truly close the discovery
  loop.'
arxivId: '2405.04484'
arxivUrl: https://arxiv.org/abs/2405.04484
authors:
- Subhash Kantamneni
- Ziming Liu
- Max Tegmark
concepts:
- integrable system discovery
- conservation laws
- conserved quantity optimization
- automated discovery
- eigenvalue decomposition
- interpretability
- scientific workflows
- sparse models
- inverse problems
- loss function design
- dimensionality reduction
- symmetry preservation
figures:
- /iaifi-research-blog/figures/2405_04484/figure_1.png
- /iaifi-research-blog/figures/2405_04484/figure_1.png
- /iaifi-research-blog/figures/2405_04484/figure_2.png
- /iaifi-research-blog/figures/2405_04484/figure_2.png
- /iaifi-research-blog/figures/2405_04484/figure_3.png
- /iaifi-research-blog/figures/2405_04484/figure_3.png
pdfUrl: https://arxiv.org/pdf/2405.04484v1
published: '2024-05-07T16:53:29+00:00'
theme: Foundational AI
title: 'OptPDE: Discovering Novel Integrable Systems via AI-Human Collaboration'
wordCount: 974
---

## The Big Picture

Imagine searching for a needle in an infinite haystack where the needle can take almost any shape. That's roughly the challenge facing physicists hunting for **integrable systems**, special mathematical equations so perfectly balanced they can be solved exactly and predicted indefinitely into the future.

Most equations describing nature are messy, chaotic, resistant to exact solutions. Integrable systems are the rare exceptions. They've yielded some of physics' greatest triumphs, from the mathematics of water waves to the behavior of magnetic materials at the quantum scale.

These equations, technically called **partial differential equations (PDEs)**, describe how quantities like pressure or energy change across space and time. The integrable ones are special because they possess **conserved quantities**, aspects of the system that never change. Think of how total energy in a frictionless pendulum stays constant forever.

Finding integrable PDEs has always required brilliant intuition and painstaking symbolic calculation. The search space is astronomically large: even restricting to relatively simple polynomial equations, you're sifting through a 33-dimensional space of possible coefficients.

Researchers at MIT's IAIFI have now built a machine learning system that navigates that space automatically, and found three families of equations nobody had written down before.

> **Key Insight:** OptPDE is the first machine learning approach that actively *designs* integrable PDEs by optimizing their coefficients to maximize conserved quantities, discovering genuinely novel integrable systems through AI-human collaboration.

## How It Works

The central insight behind OptPDE is simple: instead of searching for conserved quantities in a fixed equation, flip the problem around. Treat the equation's coefficients as adjustable knobs, and turn those knobs until the number of conserved quantities is as large as possible.

![Figure 1](/iaifi-research-blog/figures/2405_04484/figure_1.png)

This requires two interlocking pieces. The first is **CQFinder**, a routine that takes any PDE and a library of candidate basis functions, then computes how many conserved quantities that PDE actually has. It translates the conservation condition into a linear system, then uses **singular value decomposition (SVD)** to enumerate all solutions. In effect, CQFinder counts how many directions in function space remain perfectly frozen as the equation evolves.

The second piece is **OptPDE** itself. Because CQFinder runs in PyTorch, the entire pipeline is **differentiable**: the system can compute *gradients* (mathematical pointers indicating which direction leads uphill) to determine which coefficient changes will increase the conserved-quantity count.

OptPDE uses a hybrid optimization strategy:

- **Gradient ascent** to climb toward higher conserved-quantity counts
- **Simulated annealing**, which deliberately accepts occasional backward steps to avoid getting permanently stuck in local maxima
- **Sparsification** to trim discovered equations to their simplest interpretable forms

The team ran this optimization 5,000 times from random starting points, each time reshaping a 33-parameter PDE. After collecting solutions, they applied dimensionality reduction to find clusters, each pointing toward a distinct family of PDEs.

Four families emerged. One was immediately familiar: the **Korteweg–De Vries (KdV) equation**, one of the most celebrated integrable PDEs in mathematical physics. It describes shallow water waves and self-reinforcing wave packets called **solitons**. Finding it confirmed the method works.

![Figure 2](/iaifi-research-blog/figures/2405_04484/figure_1.png)

The other three families were new. The most striking was *u_t = (u_x + a²u_xxx)³*. Its special case *a = 0* gives *u_t = u_x³*, which looks deceptively simple but hides rich behavior. It supports wave-like solutions and develops breaking similar to Burgers' equation. Before breaking, it possesses infinitely many conserved quantities; afterward, the solution's magnitude decays following a power law, converging to a triangular wave shape.

![Figure 3](/iaifi-research-blog/figures/2405_04484/figure_2.png)

The machine generates a clean symbolic expression, not a black-box network, and human mathematicians step in to verify properties, prove theorems, and understand the physics. That closed loop is the whole point.

## Why It Matters

For physics, this is evidence that machine learning can expand the catalog of known integrable systems, not just rediscover what humans already found, but surface equations that might have gone unnoticed for years.

The authors point to fusion as a potential application. Inside a **tokamak** (the donut-shaped reactor at the heart of nuclear fusion research) plasma behaves according to a particular PDE. More conserved quantities could mean more controllable plasma. Whether PDE optimization can actually be applied to plasma dynamics remains to be seen, but the possibility is tantalizing.

For AI, the paper shows something worth paying attention to: the right role for machine learning in science isn't to replace human reasoning, but to handle the combinatorial search that humans can't. The system doesn't hide its answers in opaque weights. It returns symbolic equations a physicist can write on a whiteboard.

The method has clear limitations. The current search space is restricted to polynomials with a fixed maximum degree and a single spatial dimension. Extending to higher dimensions, vector fields, or more complex function spaces will require both algorithmic advances and more compute. But the framework is modular: swap in a different PDE basis, adjust the CQ basis, and the same pipeline applies.

> **Bottom Line:** OptPDE discovered three previously unknown families of integrable PDEs by teaching a machine to hunt for conservation laws, showing that AI and human scientists working together can push the boundaries of mathematical physics in ways neither could alone.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">OptPDE combines machine learning with mathematical physics, using differentiable optimization and SVD to solve an open problem in PDE theory that resisted purely analytical approaches for decades.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work introduces a fully differentiable pipeline for symbolic scientific discovery, showing that gradient-based optimization can handle discrete-valued objectives like conserved-quantity counts through careful continuous relaxation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Three novel families of integrable PDEs were discovered, including *u_t = (u_x + a²u_xxx)³*, which exhibits wave breaking, infinitely many conserved quantities, and power-law decay.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending OptPDE to higher-dimensional PDEs and physically realistic systems like tokamak plasma dynamics; the work is available at [arXiv:2405.04484](https://arxiv.org/abs/2405.04484).</span></div></div>
</div>
