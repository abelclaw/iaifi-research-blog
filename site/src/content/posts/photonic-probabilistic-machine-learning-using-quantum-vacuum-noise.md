---
abstract: Probabilistic machine learning utilizes controllable sources of randomness
  to encode uncertainty and enable statistical modeling. Harnessing the pure randomness
  of quantum vacuum noise, which stems from fluctuating electromagnetic fields, has
  shown promise for high speed and energy-efficient stochastic photonic elements.
  Nevertheless, photonic computing hardware which can control these stochastic elements
  to program probabilistic machine learning algorithms has been limited. Here, we
  implement a photonic probabilistic computer consisting of a controllable stochastic
  photonic element - a photonic probabilistic neuron (PPN). Our PPN is implemented
  in a bistable optical parametric oscillator (OPO) with vacuum-level injected bias
  fields. We then program a measurement-and-feedback loop for time-multiplexed PPNs
  with electronic processors (FPGA or GPU) to solve certain probabilistic machine
  learning tasks. We showcase probabilistic inference and image generation of MNIST-handwritten
  digits, which are representative examples of discriminative and generative models.
  In both implementations, quantum vacuum noise is used as a random seed to encode
  classification uncertainty or probabilistic generation of samples. In addition,
  we propose a path towards an all-optical probabilistic computing platform, with
  an estimated sampling rate of ~ 1 Gbps and energy consumption of ~ 5 fJ/MAC. Our
  work paves the way for scalable, ultrafast, and energy-efficient probabilistic machine
  learning hardware.
arxivId: '2403.04731'
arxivUrl: https://arxiv.org/abs/2403.04731
authors:
- Seou Choi
- Yannick Salamin
- Charles Roques-Carmes
- Rumen Dangovski
- Di Luo
- Zhuo Chen
- Michael Horodynski
- Jamison Sloan
- Shiekh Zia Uddin
- Marin Soljacic
concepts:
- photonic probabilistic neuron
- optical parametric oscillator
- stochastic processes
- generative models
- bayesian inference
- uncertainty quantification
- quantum states
- stochastic binary neural network
- monte carlo methods
- convolutional networks
- density estimation
figures:
- /iaifi-research-blog/figures/2403_04731/figure_1.png
- /iaifi-research-blog/figures/2403_04731/figure_2.png
pdfUrl: https://arxiv.org/pdf/2403.04731v1
published: '2024-03-07T18:35:18+00:00'
theme: Theoretical Physics
title: Photonic probabilistic machine learning using quantum vacuum noise
wordCount: 1282
---

## The Big Picture

Every time your phone's weather app gives a probability of rain, or a medical AI flags a scan as "possibly cancerous," it's running **probabilistic machine learning**, using controlled randomness to express uncertainty rather than pretending the world is black and white. The uncomfortable truth: the chips running those calculations are deterministic machines that have to fake randomness, burning energy and time to simulate what nature gives away for free.

What if that randomness came directly from quantum physics, from the irreducible fuzziness baked into the fabric of the universe itself?

That's exactly what a team at MIT and IAIFI has done. Researchers led by Seou Choi and Marin Soljačić built a photonic computer that harnesses **quantum vacuum noise**, the ceaseless, unpredictable flickering that exists even in a perfect vacuum. No particles, no light source. They used it to run real machine learning algorithms, performing probabilistic image classification and generation on tasks that inherently require genuine randomness.

> **Key Insight:** Quantum vacuum noise isn't just tolerated interference in optical systems. It's a resource, and this team has turned it into a programmable computational primitive for machine learning.

## How It Works

The centerpiece is the **photonic probabilistic neuron (PPN)**, an optical device that acts like a weighted coin flip you can tune on demand. The PPN is built from a **degenerate optical parametric oscillator (OPO)**: a laser-powered device that absorbs light at one frequency and emits it at half that frequency, but can settle into one of two opposite phases. Call them 0 and 1.

Which phase the OPO settles into isn't determined by any classical input. Quantum vacuum noise decides: the faintest electromagnetic fluctuations at the quantum limit. The device is exquisitely sensitive to this noise because it sits at the edge of a bistable instability, perfectly balanced between two valid output states. Think of a ball poised atop a hill with two valleys on either side.

![Figure 1](/iaifi-research-blog/figures/2403_04731/figure_1.png)

A tiny **bias field** (a whisper of injected light) tilts the probability. A slightly positive bias makes the OPO favor state "1"; a negative bias favors "0." The relationship is smooth and programmable: the PPN samples from a probability distribution you control.

The full computing system runs in a hybrid loop:

1. **Sample:** The OPO fires, snapping to 0 or 1 based on the current bias
2. **Read:** An electronic processor (an FPGA, a reprogrammable chip, or a GPU) measures the output
3. **Update:** The processor calculates the new bias for the next neuron and feeds it back
4. **Repeat:** By time-multiplexing (running the same physical OPO through each neuron's role one at a time, like a single actor playing every part in a play) the team simulates an entire network of PPNs from a single device

This hybrid optoelectronic architecture is what makes it practical. High-dimensional network bookkeeping lives in silicon; generating genuinely random binary samples from tunable probabilities is offloaded to quantum optics.

The team validated the system on two machine learning tasks using the MNIST handwritten digit dataset, one for each fundamental mode of probabilistic ML.

For **discriminative** tasks, they implemented a **stochastic binary neural network (SBNN)**, a net with probabilistic rather than fixed weights. Instead of returning a single label ("this is a 7"), it returns a distribution over labels, directly quantifying uncertainty. When an input digit is clear, probability concentrates on the correct answer; when the image is noisy or near a decision boundary, the distribution spreads honestly. Quantum vacuum noise served as the random seed throughout.

![Figure 2](/iaifi-research-blog/figures/2403_04731/figure_2.png)

For **generative** tasks, they ran a **pixel convolutional neural network (pixelCNN)**, which synthesizes images one pixel at a time, each conditioned on all previously generated pixels. Quantum vacuum noise provided the stochastic seed that, combined with learned probability distributions, produced entirely new handwritten digit images from scratch.


The researchers also mapped out a path to a fully all-optical platform that would eliminate the electronic loop entirely, projecting a sampling rate around 1 Gbps and energy consumption of roughly 5 femtojoules per multiply-accumulate operation. If those numbers hold, that's orders of magnitude faster and more efficient than conventional silicon.

## Why It Matters

Digital computers simulate randomness with **pseudorandom number generators**, deterministic algorithms whose outputs merely look random. For most applications, this is fine. But where true randomness matters (cryptography, certain optimization problems, ML systems requiring verifiable statistical properties) the simulation becomes a liability in both security and energy cost.

A cleaner division of labor emerges: use physics where physics is cheapest, computation where computation excels. Quantum vacuum noise is a perpetually-running, zero-cost random number generator operating at the speed of light. The hard part has always been programmability, shaping that noise into useful probability distributions on demand. By showing that OPOs can act as controllable stochastic neurons running real ML algorithms, the team has tackled that problem head-on.

The work also raises questions at the boundary of quantum information and machine learning. How much does the "quantumness" of the noise actually matter for ML performance? Could these devices eventually harness entanglement or other quantum correlations to go beyond what classical probabilistic computing can achieve?

> **Bottom Line:** By converting quantum vacuum fluctuations into programmable probabilistic neurons, this photonic computer shows that the universe's most fundamental randomness is a viable substrate for machine learning, at speeds and energy scales that silicon struggles to match.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work spans quantum optics, nonlinear photonics, and machine learning, showing that quantum physical phenomena can be directly harnessed as computational primitives in real ML algorithms.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The photonic probabilistic neuron provides a hardware-native implementation of stochastic sampling (the bottleneck in probabilistic ML) with projected improvements in speed and energy efficiency of up to two orders of magnitude over CMOS, potentially enabling uncertainty-aware AI at scales currently out of reach.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The experiment shows that quantum vacuum noise (the electromagnetic zero-point fluctuations of empty space) can be coherently controlled as a computational resource, connecting foundational quantum field theory to practical computation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include building a fully all-optical feedback loop targeting ~1 Gbps throughput and exploring whether quantum correlations could provide advantages beyond classical probabilistic computing. See [arXiv:2403.04731](https://arxiv.org/abs/2403.04731).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Photonic probabilistic machine learning using quantum vacuum noise</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2403.04731</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Seou Choi", "Yannick Salamin", "Charles Roques-Carmes", "Rumen Dangovski", "Di Luo", "Zhuo Chen", "Michael Horodynski", "Jamison Sloan", "Shiekh Zia Uddin", "Marin Soljacic"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Probabilistic machine learning utilizes controllable sources of randomness to encode uncertainty and enable statistical modeling. Harnessing the pure randomness of quantum vacuum noise, which stems from fluctuating electromagnetic fields, has shown promise for high speed and energy-efficient stochastic photonic elements. Nevertheless, photonic computing hardware which can control these stochastic elements to program probabilistic machine learning algorithms has been limited. Here, we implement a photonic probabilistic computer consisting of a controllable stochastic photonic element - a photonic probabilistic neuron (PPN). Our PPN is implemented in a bistable optical parametric oscillator (OPO) with vacuum-level injected bias fields. We then program a measurement-and-feedback loop for time-multiplexed PPNs with electronic processors (FPGA or GPU) to solve certain probabilistic machine learning tasks. We showcase probabilistic inference and image generation of MNIST-handwritten digits, which are representative examples of discriminative and generative models. In both implementations, quantum vacuum noise is used as a random seed to encode classification uncertainty or probabilistic generation of samples. In addition, we propose a path towards an all-optical probabilistic computing platform, with an estimated sampling rate of ~ 1 Gbps and energy consumption of ~ 5 fJ/MAC. Our work paves the way for scalable, ultrafast, and energy-efficient probabilistic machine learning hardware.</span></div></div>
</div>
