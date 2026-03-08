---
abstract: 'We propose a new "Poisson flow" generative model (PFGM) that maps a uniform
  distribution on a high-dimensional hemisphere into any data distribution. We interpret
  the data points as electrical charges on the $z=0$ hyperplane in a space augmented
  with an additional dimension $z$, generating a high-dimensional electric field (the
  gradient of the solution to Poisson equation). We prove that if these charges flow
  upward along electric field lines, their initial distribution in the $z=0$ plane
  transforms into a distribution on the hemisphere of radius $r$ that becomes uniform
  in the $r \to\infty$ limit. To learn the bijective transformation, we estimate the
  normalized field in the augmented space. For sampling, we devise a backward ODE
  that is anchored by the physically meaningful additional dimension: the samples
  hit the unaugmented data manifold when the $z$ reaches zero. Experimentally, PFGM
  achieves current state-of-the-art performance among the normalizing flow models
  on CIFAR-10, with an Inception score of $9.68$ and a FID score of $2.35$. It also
  performs on par with the state-of-the-art SDE approaches while offering $10\times
  $ to $20 \times$ acceleration on image generation tasks. Additionally, PFGM appears
  more tolerant of estimation errors on a weaker network architecture and robust to
  the step size in the Euler method. The code is available at https://github.com/Newbeeer/poisson_flow
  .'
arxivId: '2209.11178'
arxivUrl: https://arxiv.org/abs/2209.11178
authors:
- Yilun Xu
- Ziming Liu
- Max Tegmark
- Tommi Jaakkola
concepts:
- generative models
- poisson field
- normalizing flows
- augmented dimension sampling
- physics-informed neural networks
- score-based models
- stochastic processes
- diffusion models
- density estimation
- inverse problems
- optimal transport
figures:
- /iaifi-research-blog/figures/2209_11178/figure_1.png
- /iaifi-research-blog/figures/2209_11178/figure_1.png
- /iaifi-research-blog/figures/2209_11178/figure_2.png
- /iaifi-research-blog/figures/2209_11178/figure_2.png
- /iaifi-research-blog/figures/2209_11178/figure_3.png
- /iaifi-research-blog/figures/2209_11178/figure_3.png
pdfUrl: https://arxiv.org/pdf/2209.11178v4
published: '2022-09-22T17:26:58+00:00'
theme: Foundational AI
title: Poisson Flow Generative Models
wordCount: 1215
---

## The Big Picture

Imagine dropping ink into honey. Unlike water, where ink diffuses chaotically, the thick fluid forces it along clean, predictable paths. Now run that process in reverse: start with ink spread uniformly through the honey and watch it concentrate back into a single drop. That's what MIT researchers Yilun Xu, Ziming Liu, Max Tegmark, and Tommi Jaakkola have built — a generative model that uses the physics of electric charges in viscous fluids to synthesize realistic images, faster than nearly any competing approach.

The challenge at the heart of generative AI is simple to state: how do you teach a computer to draw? Current best-in-class methods, **diffusion models** and **score-based models**, learn to reverse a noisy scrambling process, gradually recovering coherent images from random static. They produce beautiful results, but they're slow. Generating a single image can require hundreds of sequential neural network evaluations.

The PFGM team cracked open a textbook on electrostatics and found a better way.

> **Key Insight:** By treating image data as electric charges generating a high-dimensional **Poisson field**, PFGM creates a smooth, invertible path between noise and data. It achieves the best image quality among normalizing flow models while running 10–20× faster than competing stochastic methods.

## How It Works

The trick starts with a geometric insight from classical physics. Take your dataset, say 50,000 images of cats and airplanes from CIFAR-10. Each image lives in a high-dimensional space (3,072 dimensions for CIFAR-10). Now place each image as a positive electric charge on a flat mathematical surface, a **hyperplane**, embedded in a space with one extra dimension.

![Figure 1](/iaifi-research-blog/figures/2209_11178/figure_1.png)

Physics takes over from here. Each charge repels every other and gets pushed upward along **electric field lines**, the invisible paths that forces trace through space, like the lines visible when you scatter iron filings near a magnet. These trajectories are governed by the **Poisson equation**, a 19th-century partial differential equation describing electrostatics, gravity, and fluid flow, here pressed into service to move charges through the extra dimension.

As the charges drift upward, they spread out. The authors prove that when charges cross an imaginary hemisphere of large radius *r*, their distribution becomes perfectly uniform in the limit of large *r*. Every complicated, structured data distribution (faces, galaxies, handwritten digits) flattens into the same featureless sphere.

That's the forward process. Generating new images runs it in reverse:

1. **Sample** a random point uniformly from the high-dimensional hemisphere. This is trivially easy.
2. **Integrate backwards** along the electric field lines using a backward ODE (ordinary differential equation), moving from large *z* back toward *z*=0.
3. **Stop** when *z* hits zero. The point that lands on the hyperplane is your generated image.

![Figure 2](/iaifi-research-blog/figures/2209_11178/figure_1.png)

The Poisson field can't be computed analytically at test time, so the team trains a neural network to estimate it. They normalize field vectors to unit length during training, working with direction rather than magnitude, and this turns out to be essential for stability. The network learns to predict which direction field lines point at any location, which is enough to trace the backward path from hemisphere to data.

![Figure 3](/iaifi-research-blog/figures/2209_11178/figure_2.png)

This physical anchoring also helps with error tolerance. In score-based approaches, the "time" variable closely tracks sample norm, so small estimation errors compound in a correlated way. In PFGM, the *z*-coordinate and sample norm are more loosely coupled, so integration errors don't cascade as badly.

## Why It Matters

The numbers tell a clear story. On the standard CIFAR-10 benchmark, PFGM achieves an **FID score** (Fréchet Inception Distance, where lower means generated images match real ones more closely) of 2.35 and an **Inception score** of 9.68 (higher means greater image diversity and realism). Among normalizing flow models, that's the best reported result. PFGM also performs on par with the best SDE-based generators while requiring 10× to 20× fewer neural network evaluations. That's not a marginal speedup; it's the difference between seconds and minutes at scale.

![Figure 4](/iaifi-research-blog/figures/2209_11178/figure_2.png)

The model is also unusually forgiving. When the researchers deliberately swapped in a weaker neural architecture that causes competing ODE methods to produce garbage, PFGM continued generating decent images. Step size is similarly forgiving: whether you use 10 or 100 integration steps, performance degrades gracefully rather than catastrophically. For practical deployment, where speed-quality tradeoffs get tuned on the fly, that flexibility matters.

And the implications cut both ways across the physics-AI boundary. A 19th-century equation seeds a genuinely novel machine learning architecture. But it also raises questions the other direction: why does Poisson flow uniformize distributions so cleanly? What does the structure of those field lines reveal about the geometry of learned data manifolds? The framework's invertible ODEs open paths toward likelihood evaluation and image editing, tasks that pure diffusion models handle poorly.

> **Bottom Line:** Poisson Flow Generative Models show that an equation written down by Siméon Denis Poisson in 1823 can anchor a 2022 image generator that is faster and more error-tolerant than most of its competitors.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">PFGM translates the mathematics of high-dimensional electrostatics (Poisson's equation and *N*-dimensional Coulomb's law) into a practical generative modeling framework, showing that classical physics intuition can produce concrete algorithmic advances in AI.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">On CIFAR-10, PFGM sets the best FID score (2.35) among normalizing flow models and delivers 10–20× sampling speedups over SDE-based methods, with improved tolerance to network architecture choices and integration step size.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The work extends classical electrostatic theory to arbitrary *N* dimensions, proving new geometric results about how charge distributions transform under Poisson field flow. These are mathematical physics results that stand independently of their machine learning application.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The framework invites extension to higher-dimensional data and other physical flow equations, with potential applications to generative tasks in physics and cosmology. The paper is [arXiv:2209.11178](https://arxiv.org/abs/2209.11178), presented at NeurIPS 2022.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Poisson Flow Generative Models</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2209.11178](https://arxiv.org/abs/2209.11178)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Yilun Xu", "Ziming Liu", "Max Tegmark", "Tommi Jaakkola"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We propose a new "Poisson flow" generative model (PFGM) that maps a uniform distribution on a high-dimensional hemisphere into any data distribution. We interpret the data points as electrical charges on the $z=0$ hyperplane in a space augmented with an additional dimension $z$, generating a high-dimensional electric field (the gradient of the solution to Poisson equation). We prove that if these charges flow upward along electric field lines, their initial distribution in the $z=0$ plane transforms into a distribution on the hemisphere of radius $r$ that becomes uniform in the $r \to\infty$ limit. To learn the bijective transformation, we estimate the normalized field in the augmented space. For sampling, we devise a backward ODE that is anchored by the physically meaningful additional dimension: the samples hit the unaugmented data manifold when the $z$ reaches zero. Experimentally, PFGM achieves current state-of-the-art performance among the normalizing flow models on CIFAR-10, with an Inception score of $9.68$ and a FID score of $2.35$. It also performs on par with the state-of-the-art SDE approaches while offering $10\times $ to $20 \times$ acceleration on image generation tasks. Additionally, PFGM appears more tolerant of estimation errors on a weaker network architecture and robust to the step size in the Euler method. The code is available at https://github.com/Newbeeer/poisson_flow .</span></div></div>
</div>
