---
abstract: 'Since diffusion models (DM) and the more recent Poisson flow generative
  models (PFGM) are inspired by physical processes, it is reasonable to ask: Can physical
  processes offer additional new generative models? We show that the answer is yes.
  We introduce a general family, Generative Models from Physical Processes (GenPhys),
  where we translate partial differential equations (PDEs) describing physical processes
  to generative models. We show that generative models can be constructed from s-generative
  PDEs (s for smooth). GenPhys subsume the two existing generative models (DM and
  PFGM) and even give rise to new families of generative models, e.g., "Yukawa Generative
  Models" inspired from weak interactions. On the other hand, some physical processes
  by default do not belong to the GenPhys family, e.g., the wave equation and the
  Schrödinger equation, but could be made into the GenPhys family with some modifications.
  Our goal with GenPhys is to explore and expand the design space of generative models.'
arxivId: '2304.02637'
arxivUrl: https://arxiv.org/abs/2304.02637
authors:
- Ziming Liu
- Di Luo
- Yilun Xu
- Tommi Jaakkola
- Max Tegmark
concepts:
- generative models
- s-generative pdes
- diffusion models
- dispersion relations
- physics-informed neural networks
- yukawa generative models
- score-based models
- density estimation
- flow matching
- stochastic processes
- inverse problems
- quantum field theory
figures:
- /iaifi-research-blog/figures/2304_02637/figure_1.png
- /iaifi-research-blog/figures/2304_02637/figure_1.png
- /iaifi-research-blog/figures/2304_02637/figure_2.png
- /iaifi-research-blog/figures/2304_02637/figure_2.png
- /iaifi-research-blog/figures/2304_02637/figure_3.png
- /iaifi-research-blog/figures/2304_02637/figure_3.png
pdfUrl: https://arxiv.org/pdf/2304.02637v1
published: '2023-04-05T17:58:16+00:00'
theme: Foundational AI
title: 'GenPhys: From Physical Processes to Generative Models'
wordCount: 1038
---

## The Big Picture

Imagine you're a physicist with a catalog of nature's most elegant equations: the heat equation describing how warmth spreads through metal, the Poisson equation governing electric fields, the Schrödinger equation at the heart of quantum mechanics. Hidden inside each of these, it turns out, is a blueprint for a machine that can generate photorealistic images, synthesize music, or simulate molecular structures. That's the idea behind GenPhys.

For years, AI researchers have borrowed from physics almost by accident. Diffusion models, the engine behind Stable Diffusion and DALL-E, were inspired by watching ink dissolve in water. Poisson Flow Generative Models drew from electrostatics, imagining data points as charged particles drifting through a field. Both approaches work extremely well, but they represent just two points in a vast, largely unexplored space of possibilities.

A team from MIT (Ziming Liu, Di Luo, Yilun Xu, Tommi Jaakkola, and Max Tegmark) asked a simple question: if two physical equations gave us two great generative models, what happens when you systematically work through the entire zoo of physics? Their answer is GenPhys, a unified framework that translates **partial differential equations (PDEs)**, the mathematical language of how physical quantities change in space and time, directly into generative models.

> **Key Insight:** Any physical process described by a PDE that smooths out information over time can, in principle, be converted into a generative model, unlocking dozens of new AI architectures inspired by heat, gravity, weak interactions, and beyond.

## How It Works

![Figure 1](/iaifi-research-blog/figures/2304_02637/figure_1.png)

The core machinery of GenPhys rests on a clean observation: generative models and physical processes are doing the same thing in reverse. A physical process takes a complicated state and gradually simplifies it. Heat diffuses until temperature is uniform. Charges redistribute until fields are smooth. A generative model runs this backward: start from simple noise, reverse the process, arrive at complex, structured data.

To formalize this, the team defines **s-generative PDEs** (the "s" is for smooth). A PDE qualifies if it satisfies two conditions:

1. **Condition C1:** The PDE can be rewritten as a density flow, a description of how all possible versions of a data point drift and spread over time, like tracking the movement of a crowd rather than a single person.
2. **Condition C2:** Solutions become smoother over time. Rapid variations die out quickly while slow, gradual patterns persist.

The second condition is the decisive one. It's what lets you run the process backward: if physics drives everything toward smoothness, then reversing it drives smoothness toward structure. You can test Condition C2 rigorously using **dispersion relations**, a standard tool physicists use to characterize how quickly fluctuations in a system decay. If fine-grained, rapid variations die out exponentially fast while broad, slow variations survive, the PDE earns its s-generative badge.

![Figure 2](/iaifi-research-blog/figures/2304_02637/figure_1.png)

With these criteria in hand, the team marches through classical physics. The diffusion equation? S-generative. That's the heat equation, exactly what diffusion models already exploit. The Poisson equation from electrostatics? S-generative. That's PFGM.

The **Yukawa equation**, describing a screened potential from the physics of weak interactions, also qualifies. It gives rise to a brand-new family of models the authors dub **Yukawa Generative Models**.

The wave equation and the Schrödinger equation fail the test. A wave doesn't smooth; it propagates. A quantum wavefunction oscillates indefinitely. Neither is s-generative in its default form. But with certain modifications (adding dissipation to a wave equation, or tweaking the Schrödinger equation) even these can be brought into the GenPhys family.

![Figure 3](/iaifi-research-blog/figures/2304_02637/figure_2.png)

Building a GenPhys model involves four steps:

1. Rewrite the PDE in continuity equation form to extract a velocity field and a source term.
2. Solve the PDE with the data distribution as an initial condition, using a **Green's function** (a mathematical shortcut expressing the solution as the accumulated response to many tiny, point-like nudges) to obtain an analytic form.
3. Train a neural network to approximate the velocity field.
4. Generate samples by drawing from the simple prior and integrating the learned dynamics backward in time.

## Why It Matters

For AI practitioners, GenPhys is a recipe book for inventing new generative architectures. Instead of waiting for the next lucky analogy, researchers can now systematically ask: is this PDE s-generative? If so, there's a generative model waiting to be built. The Yukawa model is proof of concept, a genuinely new family of AI models derived from physics rather than from intuition or trial and error.

For physicists, the work makes precise an appealing analogy. Our universe started from a nearly uniform quantum state after the Big Bang (essentially Gaussian noise) and physical laws evolved that state into the rich complexity we observe today. The formal structure that lets diffusion equations generate images turns out to be the same structure by which thermodynamics produces entropy. GenPhys pins this connection down mathematically.

The framework also opens what the authors call "bidirectional inspiration." Physics has inspired new AI models, and the AI perspective on PDEs might suggest new ways to think about physical processes in return. Future work could explore whether quantum or relativistic PDEs, properly modified, yield generative models with unusual and useful properties.

> **Bottom Line:** GenPhys provides a systematic recipe for converting any smoothing physical equation into a generative AI model, unifying diffusion models and PFGM under one roof and delivering new architectures, including Yukawa Generative Models, straight from the physics of weak interactions.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">GenPhys builds a formal mathematical bridge between the PDEs of classical and quantum physics and the design of generative AI models, revealing a deep structural duality between the two fields.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The framework expands the generative model design space from two known instances (diffusion and Poisson flow) to a potentially vast family, providing a systematic method for constructing new architectures from physical principles.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By casting the Yukawa screened potential, a staple of weak interaction theory, as a generative model, the work reveals unexpected computational structure in the mathematics of fundamental interactions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include exploring relativistic and quantum PDEs with modifications that restore s-generativity, and testing whether Yukawa and other novel models offer practical performance advantages; the paper is available at [arXiv:2304.02637](https://arxiv.org/abs/2304.02637).</span></div></div>
</div>
