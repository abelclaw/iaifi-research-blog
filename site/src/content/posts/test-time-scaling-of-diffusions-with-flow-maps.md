---
abstract: A common recipe to improve diffusion models at test-time so that samples
  score highly against a user-specified reward is to introduce the gradient of the
  reward into the dynamics of the diffusion itself. This procedure is often ill posed,
  as user-specified rewards are usually only well defined on the data distribution
  at the end of generation. While common workarounds to this problem are to use a
  denoiser to estimate what a sample would have been at the end of generation, we
  propose a simple solution to this problem by working directly with a flow map. By
  exploiting a relationship between the flow map and velocity field governing the
  instantaneous transport, we construct an algorithm, Flow Map Trajectory Tilting
  (FMTT), which provably performs better ascent on the reward than standard test-time
  methods involving the gradient of the reward. The approach can be used to either
  perform exact sampling via importance weighting or principled search that identifies
  local maximizers of the reward-tilted distribution. We demonstrate the efficacy
  of our approach against other look-ahead techniques, and show how the flow map enables
  engagement with complicated reward functions that make possible new forms of image
  editing, e.g. by interfacing with vision language models.
arxivId: '2511.22688'
arxivUrl: https://arxiv.org/abs/2511.22688
authors:
- Amirmojtaba Sabour
- Michael S. Albergo
- Carles Domingo-Enrich
- Nicholas M. Boffi
- Sanja Fidler
- Karsten Kreis
- Eric Vanden-Eijnden
concepts:
- flow map trajectory tilting
- diffusion models
- test-time scaling
- flow matching
- reward optimization
- reward-tilted distribution
- monte carlo methods
- normalizing flows
- thermodynamic length
- stochastic processes
- score-based models
- optimal transport
figures:
- /iaifi-research-blog/figures/2511_22688/figure_1.png
- /iaifi-research-blog/figures/2511_22688/figure_2.png
- /iaifi-research-blog/figures/2511_22688/figure_3.png
pdfUrl: https://arxiv.org/pdf/2511.22688v1
published: '2025-11-27T18:44:12+00:00'
theme: Foundational AI
title: Test-time scaling of diffusions with flow maps
wordCount: 1022
---

## The Big Picture

Imagine navigating by dead reckoning in fog. You know your speed and heading at every moment, but can't see where you'll land. Now imagine consulting a map that tells you directly: "From this position, sailing these currents, you'll arrive *here*." That's the fundamental shift this paper makes in how AI image generators can be steered toward exactly what you want.

Diffusion models (the engines behind tools like Stable Diffusion and DALL-E) generate images by gradually denoising random static into structured pictures. Researchers have long wanted to steer this process at inference time, nudging the model toward images that score well on some goal: "make the clock read 3:47" or "match this text description." The standard approach calculates, at each generation step, the mathematical direction that would most improve the image's score, like adding a current to push a ship toward port. But there's a catch.

Scoring functions work only on clean, finished images, not on the blurry, half-formed noise mid-generation. The standard workaround is a **denoiser**, a neural network that predicts what the final image will look like from any intermediate state. It's a rough approximation, and as the researchers show, it fails badly at the early, most-critical stages of generation. Their solution: skip the approximation entirely and work with a **flow map**, a mathematical object that does what the denoiser tries to do, only provably better. The result is Flow Map Trajectory Tilting (FMTT), an algorithm that reliably generates images matching precise specifications that confound state-of-the-art models.

> **Key Insight:** By replacing the standard one-step denoiser with a learned flow map that directly predicts where a trajectory will land, FMTT achieves provably superior reward ascent during image generation, without any retraining of the underlying model.

## How It Works

The core framework uses two complementary descriptions of how noise becomes an image. The **velocity field** gives the instantaneous drift at each moment. The **flow map** encodes the full solution: given a particle's position at time *t*, where does it end up at time *T*? These descriptions are related by a fundamental identity that the researchers exploit.

![Figure 2](/iaifi-research-blog/figures/2511_22688/figure_2.png)

Figure 2 makes the advantage concrete. At early noise levels, the one-step denoiser produces blurry, nearly useless predictions of the final image. A one-step flow map already does better. Four steps yield strikingly clear predictions even from heavily corrupted inputs.

This matters because reward guidance depends on accurate look-ahead: garbage prediction, garbage gradient.

The FMTT algorithm works as follows:

1. **Start with noise** drawn from a base distribution and define the target as a **tilted distribution**, a mathematically adjusted version of normal image output tuned to favor images that score higher on the goal.
2. **At each generation step**, query the flow map to predict where the current trajectory will terminate. This gives an accurate "look-ahead" at the clean image.
3. **Apply the reward gradient** with respect to this predicted terminal point. Because the flow map prediction is accurate, this gradient faithfully points toward high-reward outputs.
4. **Account for thermodynamic length** (a measure, borrowed from non-equilibrium statistical mechanics, of how inefficiently the guidance process pushes the model away from its natural behavior) by applying time-dependent weights that compensate for the guidance signal's tendency to be too weak early in generation.

The framework supports two distinct modes: **importance weighting** (a statistical technique that adjusts how often different outputs are selected, enabling exact sampling from the tilted distribution) and **principled search** for finding local maximizers of the reward. Both outperform baseline guidance methods. The importance weighting approach connects to the **Jarzynski equality** from statistical physics, a well-established result that gives the method formal guarantees about sampling correctness.

![Figure 1](/iaifi-research-blog/figures/2511_22688/figure_1.png)

The clock example in Figure 1 illustrates the practical impact. Without FMTT, standard diffusion models routinely generate clocks showing the wrong time (the model has strong biases toward common times). FMTT's test-time search overcomes these biases and reliably produces images matching precise specifications that baselines cannot reach.

## Why It Matters

This work sits at a productive intersection: it solves a core AI systems problem using mathematical tools from physics. The thermodynamic length formalism gives researchers a principled lens for diagnosing and improving test-time adaptation methods, rare in a guidance literature where most methods are, as the authors put it, "somewhat ad hoc."

The immediate practical impact is in image editing. FMTT demonstrates the first successful use of **vision-language models** (VLMs, AI systems that understand both images and text) as reward functions for diffusion guidance, enabling natural-language-directed editing with unusual specificity. The framework is also architecture-agnostic: any flow-based or diffusion-based generative model, including those used in protein structure prediction or molecular design, could benefit from FMTT-style guidance.

Open questions remain. How do the theoretical guarantees on thermodynamic length translate into practical performance bounds? Can flow maps be trained specifically to optimize look-ahead quality for guidance? And how does FMTT scale when the reward function itself is expensive to evaluate, as in physics simulations?

> **Bottom Line:** Flow Map Trajectory Tilting replaces a fundamental approximation at the heart of reward-guided diffusion with a provably superior alternative, achieving reliable test-time steering toward user-specified goals that previous methods could not reach.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work draws on non-equilibrium statistical mechanics (specifically the Jarzynski equality and thermodynamic length) to provide theoretical foundations for a practical AI inference algorithm, exemplifying IAIFI's mission to bridge physics and machine learning.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">FMTT establishes a new state of the art for test-time scaling of diffusion and flow-based generative models, enabling reliable reward-guided generation including the first demonstrated use of vision-language models as reward functions for diffusion guidance.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The flow map framework, and its connections to transport theory and non-equilibrium statistical mechanics, offers new mathematical tools for understanding generative modeling as a physical process, with potential applications in scientific domains where precise control over generated structures is critical.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend FMTT to scientific domains where fine-grained control over generated structures matters. The paper is available at [arXiv:2511.22688](https://arxiv.org/abs/2511.22688) and is co-authored by IAIFI affiliate Michael S. Albergo at Harvard/Kempner Institute.</span></div></div>
</div>
