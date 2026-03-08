---
abstract: Diffusion-based generative models represent a forefront direction in generative
  AI research today. Recent studies in physics have suggested that the renormalization
  group (RG) can be conceptualized as a diffusion process. This insight motivates
  us to develop a novel diffusion-based generative model by reversing the momentum-space
  RG flow. We establish a framework that interprets RG flow as optimal transport gradient
  flow, which minimizes a functional analogous to the Kullback-Leibler divergence,
  thereby bridging statistical physics and information theory. Our model applies forward
  and reverse diffusion processes in Fourier space, exploiting the sparse representation
  of natural images in this domain to efficiently separate signal from noise and manage
  image features across scales. By introducing a scale-dependent noise schedule informed
  by a dispersion relation, the model optimizes denoising performance and image generation
  in Fourier space, taking advantage of the distinct separation of macro and microscale
  features. Experimental validations on standard datasets demonstrate the model's
  capability to generate high-quality images while significantly reducing training
  time compared to existing image-domain diffusion models. This approach not only
  enhances our understanding of the generative processes in images but also opens
  new pathways for research in generative AI, leveraging the convergence of theoretical
  physics, optimal transport, and machine learning principles.
arxivId: '2402.17090'
arxivUrl: https://arxiv.org/abs/2402.17090
authors:
- Artan Sheshmani
- Yi-Zhuang You
- Baturalp Buyukates
- Amir Ziashahabi
- Salman Avestimehr
concepts:
- diffusion models
- optimal transport
- renormalization
- generative models
- fourier-space diffusion
- scale-dependent noise schedule
- quantum field theory
- spectral methods
- score-based models
- stochastic processes
- likelihood estimation
figures:
- /iaifi-research-blog/figures/2402_17090/figure_1.png
- /iaifi-research-blog/figures/2402_17090/figure_1.png
- /iaifi-research-blog/figures/2402_17090/figure_2.png
- /iaifi-research-blog/figures/2402_17090/figure_2.png
- /iaifi-research-blog/figures/2402_17090/figure_3.png
- /iaifi-research-blog/figures/2402_17090/figure_3.png
pdfUrl: https://arxiv.org/pdf/2402.17090v2
published: '2024-02-26T23:56:34+00:00'
theme: Foundational AI
title: Renormalization Group flow, Optimal Transport and Diffusion-based Generative
  Model
wordCount: 1067
---

## The Big Picture

Imagine trying to describe a painting by zooming out, layer by layer, until all you see is a blur of average colors. That's roughly what physicists do when they apply the **renormalization group** — a mathematical procedure that progressively simplifies a system, averaging over fine details while preserving its large-scale structure. Invented to tame the runaway infinities of quantum field theory (the mathematics of subatomic particles), for decades the technique belonged almost exclusively to particle physics and statistical mechanics.

Now a team from Harvard, MIT, UC San Diego, and USC has turned that procedure inside out — and used it to build a faster, more principled image-generation AI. Their insight: the same mathematical machinery that physicists use to progressively erase small-scale variables from a physical system is mathematically equivalent to the forward diffusion process that corrupts images in modern generative AI. If you can run the renormalization group forward to destroy structure, you can run it backward to create it.

The result is the **Fourier-Domain Diffusion Model (FDDM)** — a generative model that works in frequency space (the way a sound can be broken into individual musical notes, FDDM decomposes images into their frequency components) rather than pixel space. It trains significantly faster than conventional diffusion models and is grounded in a rigorous bridge between statistical physics, information theory, and machine learning.

> **Key Insight:** By interpreting the renormalization group as an optimal transport process in Fourier space, the researchers built a diffusion model that separates image features by scale — handling broad strokes and fine details at the right stages of generation, rather than treating all pixels equally.

## How It Works

The journey from raw physics to working AI involves three conceptual steps, each one a bridge between disciplines.

**Step 1: RG as Optimal Transport.** The researchers first establish a formal equivalence between RG flow and **optimal transport** — a mathematical theory originally developed to solve logistics problems (how do you move a pile of sand to fill a hole while minimizing total work?). The key quantity is the **Wasserstein distance**, which measures how much "effort" it takes to morph one probability distribution into another. The paper shows that RG flow can be described as a process that minimizes a quantity closely related to the **Kullback-Leibler (KL) divergence** — the standard information-theoretic measure of how different two probability distributions are from each other. This isn't a metaphor; it's a precise mathematical statement.

![Figure 1](/iaifi-research-blog/figures/2402_17090/figure_1.png)

**Step 2: Move everything to Fourier space.** Rather than adding and removing noise pixel by pixel, FDDM operates in the **Fourier domain** — the space of spatial frequencies that compose an image. This is motivated directly by physics: in quantum field theory, the renormalization group eliminates high-frequency (small-scale) components first, progressively moving toward low-frequency (large-scale) structure. Natural images have a directly analogous property — they are **sparse in Fourier space**, with most image energy concentrated in relatively few frequency components. High frequencies encode sharp edges and fine textures; low frequencies encode overall composition and color.

By diffusing in Fourier space, the model selectively corrupts and recovers different scales at the right times:

- **Forward diffusion (renormalization):** High-frequency components are noised first — fine details destroyed before coarse structure, mirroring how RG eliminates microscopic degrees of freedom before macroscopic ones.
- **Reverse diffusion (generation):** The model denoises low frequencies first, establishing the large-scale layout, then progressively recovers fine details. The big picture comes before the brushstrokes.

![Figure 2](/iaifi-research-blog/figures/2402_17090/figure_1.png)

**Step 3: A physics-informed noise schedule.** Conventional diffusion models use a noise schedule that is largely empirical. FDDM replaces this with a **dispersion relation** — a concept borrowed from wave physics and the physics of materials — that describes how different frequencies decay at different rates. This ensures each frequency mode gets noised at a rate appropriate to its scale: high-frequency components decay rapidly, low-frequency components evolve slowly.

![Figure 3](/iaifi-research-blog/figures/2402_17090/figure_2.png)

The FDDM was validated on standard image benchmarks, demonstrating competitive image quality and substantially reduced training time compared to pixel-domain diffusion models — a direct consequence of the sparsity advantage in Fourier space.

![Figure 4](/iaifi-research-blog/figures/2402_17090/figure_2.png)

## Why It Matters

The practical payoff — faster training, good image quality — matters, but the deeper significance is conceptual. For years, researchers have noticed suggestive similarities between deep learning and physics: neural networks as statistical field theories, attention mechanisms and tensor networks, diffusion models and RG flows. Most of these analogies have stayed at the level of inspiration. This paper takes the analogy seriously enough to derive a working algorithm from it — and the algorithm performs well.

That changes the conversation. It suggests that the mathematical structures physicists have refined over decades to handle the complexity of quantum fields are not just metaphors for machine learning — they are generative principles that can directly inform better algorithms. The connection to optimal transport is particularly promising: it provides a mathematical framework for understanding what diffusion models are actually optimizing, which could guide future architectural choices well beyond the specific FDDM design.

The authors point to several open directions: extending the framework to other data modalities (audio, molecular structures, scientific data), exploring whether alternative RG schemes yield further gains, and deepening the theoretical connections to categorical and algebraic structures in both physics and machine learning.

![Figure 5](/iaifi-research-blog/figures/2402_17090/figure_3.png)

> **Bottom Line:** FDDM proves that the renormalization group — a tool forged in quantum field theory — can be reverse-engineered into a faster, more principled image generator. Physics didn't just inspire the model; it built it.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work establishes a rigorous mathematical bridge between renormalization group theory from quantum field theory, optimal transport from mathematics, and diffusion-based generative models from machine learning — turning a physics abstraction into a working AI algorithm.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The Fourier-Domain Diffusion Model achieves competitive image generation quality while significantly reducing training time by exploiting the sparse frequency-space structure of natural images and a physics-derived, scale-dependent noise schedule.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper formalizes RG flow as an optimal transport gradient flow minimizing a KL-divergence-like functional, providing a new information-theoretic lens on coarse-graining in statistical and quantum physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend the FDDM framework to scientific data modalities and explore alternative RG schemes for further performance gains; the paper is available on arXiv from researchers at Harvard, MIT, UC San Diego, and USC.</span></div></div>
</div>
