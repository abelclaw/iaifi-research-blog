---
abstract: Integrating physical inductive biases into machine learning can improve
  model generalizability. We generalize the successful paradigm of physics-informed
  learning (PIL) into a more general framework that also includes what we term physics-augmented
  learning (PAL). PIL and PAL complement each other by handling discriminative and
  generative properties, respectively. In numerical experiments, we show that PAL
  performs well on examples where PIL is inapplicable or inefficient.
arxivId: '2109.13901'
arxivUrl: https://arxiv.org/abs/2109.13901
authors:
- Ziming Liu
- Yunyue Chen
- Yuanqi Du
- Max Tegmark
concepts:
- physics-augmented learning
- physics-informed neural networks
- generative physics properties
- lagrangian methods
- loss function design
- symmetry preservation
- hamiltonian systems
- equivariant neural networks
- generative adversarial networks
- group theory
- inverse problems
- interpretability
figures:
- /iaifi-research-blog/figures/2109_13901/figure_1.png
- /iaifi-research-blog/figures/2109_13901/figure_1.png
- /iaifi-research-blog/figures/2109_13901/figure_2.png
pdfUrl: https://arxiv.org/pdf/2109.13901v1
published: '2021-09-28T17:53:32+00:00'
theme: Foundational AI
title: 'Physics-Augmented Learning: A New Paradigm Beyond Physics-Informed Learning'
wordCount: 1129
---

## The Big Picture

Imagine teaching someone to paint portraits. One approach: show them a finished painting, then correct every brushstroke that violates proportion. Another: hand them a brush that physically cannot make out-of-proportion marks.

Both methods enforce the same rules, but they work differently — and for different kinds of rules, one will outperform the other. This tension runs through how physicists and machine learning researchers have been trying to teach neural networks about the laws of nature.

The dominant strategy has been **physics-informed learning (PIL)**, which embeds physical knowledge into a model's training by penalizing outputs that violate known physics. Enforce energy conservation by punishing solutions that break it. Enforce governing equations by adding a penalty whenever the model strays from them. Powerful, widely used, and well-understood.

But PIL carries a hidden assumption: it only works when you can efficiently *check* whether a solution violates the physics. Not all physical properties are checkable this way.

Ziming Liu, Max Tegmark, and collaborators at MIT and IAIFI identified this blind spot and built a complementary framework to fix it. Their proposal, **physics-augmented learning (PAL)**, flips the script: instead of penalizing violations, PAL embeds physical properties directly into the model's architecture, making violations structurally impossible from the start.

> **Key Insight:** Physics-informed learning can only enforce properties you can *test* for — but some of the most important physical structures, like Lagrangian dynamics and hidden symmetries, can be *generated* but not efficiently *tested*. PAL handles exactly these cases.

## How It Works

The paper draws a conceptual line that has real practical consequences. Physical properties fall into two categories:

- **Discriminative properties** — those for which you can write an efficient test that detects violations. If a function satisfies the property, the test returns zero; if not, it returns something nonzero.
- **Generative properties** — those for which you can *construct* objects satisfying the property, but have no efficient way to check whether an arbitrary object satisfies it.

This distinction maps directly onto how machine learning can use each type. PIL exploits discriminative properties: it adds a penalty term to the training loss using a discriminator operator, essentially a mathematical test for whether the physics is satisfied. For differential equation constraints, separability conditions, or directly visible symmetries, this works well.

![Figure 1](/iaifi-research-blog/figures/2109_13901/figure_1.png)

Now consider the **Lagrangian property**, whether a given set of equations of motion can be derived from an underlying energy function (a Lagrangian). Generation is trivial: pick a Lagrangian and derive the dynamics. But determining whether an arbitrary acceleration field is Lagrangian has no known efficient solution. PIL simply cannot enforce this structure.

The same goes for **positive definiteness**, the guarantee that a quantity like energy always stays non-negative. And for **hidden symmetries**, patterns in the physics that aren't obvious from the surface form of equations but deeply constrain the solutions. In all these cases, you can build objects with the property, but you can't cheaply test whether a given object has it.

PAL's solution is architectural. Rather than starting with a generic network and constraining it, PAL builds the property into the network's structure. For Lagrangian systems, the model directly parameterizes the Lagrangian function $L(q, \dot{q}; \theta)$ and derives accelerations via the Euler-Lagrange equations, the classical rules connecting an energy function to the motion it implies. The model *cannot* output non-Lagrangian dynamics, not because it's penalized, but because the architecture makes it impossible.

![Figure 2](/iaifi-research-blog/figures/2109_13901/figure_1.png)

The paper uses **additive separability**, the property that $f(x_1, x_2) = f_1(x_1) + f_2(x_2)$, as a benchmark where both approaches go head-to-head. Separability is both discriminative (via the cross-derivative test $\partial^2 f / \partial x_1 \partial x_2 = 0$) and generative, so it allows a direct comparison. In the PAL approach, the network is structured as $f_1(x_1; \theta_1) + f_2(x_2; \theta_2) + f_{12}(x_1, x_2; \theta_{12})$, with a loss penalizing the residual $f_{12}$ term. PIL uses a single network with a cross-derivative penalty. Both work here. For purely generative properties, only PAL succeeds.

The full taxonomy covers Lagrangian structure, positive definiteness, manifest symmetry, hidden symmetry, separability, and PDE satisfiability, organized into a table showing which properties are generative, discriminative, or both. PIL covers the discriminative column. PAL covers the generative column. Together, they span the full space.

![Figure 3](/iaifi-research-blog/figures/2109_13901/figure_2.png)

## Why It Matters

Much of modern physics involves quantities that are easy to construct but hard to verify. Action principles say physical systems follow paths that minimize a certain quantity. Gauge symmetries encode real physical structure through mathematical redundancies in how we describe forces. Symplectic structures and integrability conditions impose powerful constraints on dynamics. PIL's penalty-based approach doesn't apply to any of them. PAL provides the missing piece.

There's a practical efficiency argument too. Even when a property is discriminative and PIL could in principle be used, a PAL-style architectural embedding may train faster and generalize better, because the constraint is exact by construction rather than approximately enforced through a tuned penalty coefficient. The paper shows cases where PIL fails to converge or requires enormous penalty weights, while PAL succeeds out of the box.

Neural networks are pushing deeper into scientific computing: modeling molecular dynamics, predicting gravitational wave signals, emulating cosmological simulations. Whether these models are trustworthy depends increasingly on their ability to encode rich physical structure faithfully.

The framework also points toward a clear research agenda. One direction is systematically cataloguing physical properties by their generative and discriminative nature. Another is developing PAL architectures for increasingly complex structures, or hybrid approaches combining both paradigms. The connections to equivariant neural networks, Hamiltonian neural networks, and neural ODEs are natural starting points, since all three already embed specific physical constraints into network design.

> **Bottom Line:** PAL fills a gap PIL cannot. By building physical properties into network architecture rather than penalizing their violation, it handles the broad class of generative physical structures like Lagrangian dynamics and hidden symmetries that conventional physics-informed methods simply can't reach.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work formalizes a precise mathematical distinction between discriminative and generative physical properties, connecting GAN-inspired machine learning concepts with classical structures like Lagrangian mechanics and Lie group symmetries.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">PAL provides a principled way to embed physical inductive biases directly into network architecture, covering cases that existing loss-based approaches cannot encode and expanding the range of physical knowledge that ML models can reliably learn.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling neural networks to represent Lagrangian systems, hidden symmetries, and positive-definite operators, PAL opens ML-based modeling to a much wider class of fundamental physics problems where no efficient discriminator is known.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend PAL to more complex physical symmetries and hybrid PIL+PAL architectures; the paper appeared at the NeurIPS 2021 AI for Science Workshop and is available as [arXiv:2109.13901](https://arxiv.org/abs/2109.13901).</span></div></div>
</div>
