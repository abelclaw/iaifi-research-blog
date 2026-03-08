---
abstract: Modeling symmetry breaking is essential for understanding the fundamental
  changes in the behaviors and properties of physical systems, from microscopic particle
  interactions to macroscopic phenomena like fluid dynamics and cosmic structures.
  Thus, identifying sources of asymmetry is an important tool for understanding physical
  systems. In this paper, we focus on learning asymmetries of data using relaxed group
  convolutions. We provide both theoretical and empirical evidence that this flexible
  convolution technique allows the model to maintain the highest level of equivariance
  that is consistent with data and discover the subtle symmetry-breaking factors in
  various physical systems. We employ various relaxed group convolution architectures
  to uncover various symmetry-breaking factors that are interpretable and physically
  meaningful in different physical systems, including the phase transition of crystal
  structure, the isotropy and homogeneity breaking in turbulent flow, and the time-reversal
  symmetry breaking in pendulum systems.
arxivId: '2310.02299'
arxivUrl: https://arxiv.org/abs/2310.02299
authors:
- Rui Wang
- Elyssa Hofgard
- Han Gao
- Robin Walters
- Tess E. Smidt
concepts:
- equivariant neural networks
- symmetry breaking
- relaxed group convolution
- group theory
- approximate equivariance
- phase transitions
- geometric deep learning
- interpretability
- convolutional networks
- crystal structure
- symmetry preservation
- superresolution
figures:
- /iaifi-research-blog/figures/2310_02299/figure_1.png
- /iaifi-research-blog/figures/2310_02299/figure_1.png
- /iaifi-research-blog/figures/2310_02299/figure_2.png
- /iaifi-research-blog/figures/2310_02299/figure_2.png
- /iaifi-research-blog/figures/2310_02299/figure_3.png
- /iaifi-research-blog/figures/2310_02299/figure_3.png
pdfUrl: https://arxiv.org/pdf/2310.02299v8
published: '2023-10-03T14:03:21+00:00'
theme: Foundational AI
title: Discovering Symmetry Breaking in Physical Systems with Relaxed Group Convolution
wordCount: 1072
---

## The Big Picture

Imagine you're trying to teach a machine to recognize snowflakes. You build in a rule: snowflakes have six-sided symmetry — rotate one by 60 degrees and it looks identical. The model learns beautifully — until you encounter a real snowflake that's slightly imperfect, bent by a gust of wind, or in the middle of melting. Your perfectly symmetric model has no idea what to do. It was built to see symmetry, and it cannot see the break.

This is not just a snowflake problem. Symmetry — and its violation — sits at the heart of nearly every interesting phenomenon in physics.

When water freezes into ice, the random molecular dance of the liquid snaps into a rigid, ordered crystal grid, losing its ability to look the same from every angle. A turbulent flow develops pockets of directional preference. A swinging pendulum, pushed by friction or an asymmetric kick, stops looking the same whether you play it forward or backward in time. The *breaking* of symmetry is where the real physics lives.

A team from MIT, Harvard, and Northeastern has built a neural network framework that doesn't just tolerate symmetry breaking — it actively hunts for it, identifies it, and measures it in a physically meaningful way.

> **Key Insight:** By replacing rigid, symmetric convolution weights with flexible "relaxed" weights that can learn how much symmetry to enforce, the model automatically discovers and quantifies the specific ways a physical system violates its expected symmetries.

## How It Works

Standard **equivariant neural networks** — models designed so their outputs transform predictably when you rotate or reflect the input — are workhorses of physics-informed machine learning. Baking symmetry into the architecture gives the model free generalization: rotate the input, and the output rotates in lockstep, no extra training required. But this rigidity becomes a liability when the physical system *itself* breaks that symmetry.

The researchers' solution is **relaxed group convolution**. In a standard equivariant convolution, all rotated copies of a filter must share exactly one weight — the same number, regardless of orientation. In a relaxed convolution, each rotated copy gets its own trainable weight.

These **relaxed weights** are the key diagnostic tool: after training, you can read them like a thermometer. If all the weights for different rotations converge to the same value, the system is symmetric. If they diverge, the pattern of divergence tells you *which* symmetry broke and *by how much*.

![Figure 1](/iaifi-research-blog/figures/2310_02299/figure_1.png)

The paper provides a formal theoretical guarantee: a relaxed group convolution model will learn the highest level of equivariance consistent with the data — not more, not less. If the data is fully symmetric, the relaxed weights converge to uniform values and the model behaves like a standard equivariant network. If the data breaks symmetry in a specific direction, the weights encode that exact directional preference. The authors prove this mathematically.

The team tested the framework across three distinct physical scenarios:

- **Crystal phase transitions**: As a crystal undergoes a structural phase change, its lattice symmetry drops from a higher-symmetry group to a lower one. The relaxed weights tracked this transition, functioning like Landau order parameters — the classic physics tool for measuring how "broken" a symmetry is as a system crosses a phase boundary.
- **Turbulent channel flow and isotropic flow**: Channel flow has walls that break both isotropy (directional uniformity) and homogeneity (positional uniformity), while isotropic flow develops subtle directional biases in finite simulation boxes. The relaxed weights identified both effects independently, even pinpointing *where* in a turbulent channel the symmetry broke most strongly.
- **Pendulum with time-reversal breaking**: A conservative pendulum looks identical played forward and backward. Add friction, and it doesn't. The model detected this time-reversal asymmetry through its relaxed weight pattern, and the magnitude of the learned asymmetry tracked the physical damping coefficient.

![Figure 3](/iaifi-research-blog/figures/2310_02299/figure_2.png)

Beyond symmetry discovery, relaxed convolution models outperformed both fully symmetric baselines and unconstrained baselines on fluid super-resolution tasks — more interpretable *and* more accurate.

## Why It Matters

Physics has long used symmetry as a guiding principle precisely because *broken* symmetry signals something important. The discovery of parity violation — the realization that the weak nuclear force does not treat left-handed and right-handed particles equally — was one of the most shocking results of 20th-century physics. Spontaneous symmetry breaking underlies the Higgs mechanism (the process that gives fundamental particles their mass), superconductivity, and the formation of all ordered matter.

Equivariant machine learning has mostly worked by assuming symmetry and exploiting it. This paper opens the complementary territory: assuming symmetry as a prior, then letting data reveal where and how it fails.

The implications reach well beyond the three systems studied. Any physical simulation, experimental dataset, or observational catalog where symmetry is expected but imperfect — which is to say, nearly all of them — could be interrogated by this framework. Cosmological data might reveal subtle violations of statistical isotropy. Molecular dynamics simulations could expose hidden asymmetric forces. Lattice QCD calculations — simulations of the strong nuclear force run on a discrete spacetime grid — might surface unexpected symmetry-breaking patterns at finite lattice spacing.

The relaxed weights don't just make the model more flexible. They act as a scientific instrument, returning physically interpretable measurements rather than black-box predictions.

> **Bottom Line:** Relaxed group convolutions give neural networks the ability to learn symmetry from data itself — automatically detecting, localizing, and quantifying symmetry breaking in physical systems from crystal lattices to turbulent flows, making them both more accurate and more scientifically informative than either fully symmetric or unconstrained models.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges representation theory, physics symmetry principles, and deep learning architecture design — using group theory to build neural networks that act as scientific instruments for detecting physically meaningful symmetry violations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Relaxed group convolution provides a principled, theoretically grounded method for learning the right inductive bias from data, outperforming both over-constrained symmetric models and unconstrained models on fluid super-resolution benchmarks.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The framework rediscovers known symmetry-breaking effects — phase transition order parameters, turbulent anisotropy, time-reversal violation from damping — in a purely data-driven way, validating it as a tool for exploring symmetry structure in complex physical systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include applying relaxed convolutions to high-energy physics datasets and cosmological observations where subtle symmetry violations carry deep theoretical significance; the work appeared at ICML 2024 (arXiv: 2309.xxxxx).</span></div></div>
</div>
