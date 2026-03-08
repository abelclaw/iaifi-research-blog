---
abstract: Machine learning has become an effective tool for processing the extensive
  data sets produced by large physics experiments. Gravitational-wave detectors are
  now listening to the universe with quantum-enhanced sensitivity, accomplished with
  the injection of squeezed vacuum states. Squeezed state preparation and injection
  is operationally complicated, as well as highly sensitive to environmental fluctuations
  and variations in the interferometer state. Achieving and maintaining optimal squeezing
  levels is a challenging problem and will require development of new techniques to
  reach the lofty targets set by design goals for future observing runs and next-generation
  detectors. We use machine learning techniques to predict the squeezing level during
  the third observing run of the Laser Interferometer Gravitational-Wave Observatory
  (LIGO) based on auxiliary data streams, and offer interpretations of our models
  to identify and quantify salient sources of squeezing degradation. The development
  of these techniques lays the groundwork for future efforts to optimize squeezed
  state injection in gravitational-wave detectors, with the goal of enabling closed-loop
  control of the squeezer subsystem by an agent based on machine learning.
arxivId: '2305.13780'
arxivUrl: https://arxiv.org/abs/2305.13780
authors:
- Chris Whittle
- Ge Yang
- Matthew Evans
- Lisa Barsotti
concepts:
- gravitational waves
- quantum states
- squeezed state optimization
- interpretability
- surrogate modeling
- regression
- feature extraction
- genetic feature selection
- active learning
- reinforcement learning
- signal detection
figures:
- /iaifi-research-blog/figures/2305_13780/figure_1.png
- /iaifi-research-blog/figures/2305_13780/figure_1.png
- /iaifi-research-blog/figures/2305_13780/figure_2.png
pdfUrl: https://arxiv.org/pdf/2305.13780v1
published: '2023-05-23T07:47:16+00:00'
theme: Foundational AI
title: Machine Learning for Quantum-Enhanced Gravitational-Wave Observatories
wordCount: 872
---

## The Big Picture

Imagine trying to hear a whisper from a billion light-years away through a wall of thundering noise. That's what LIGO does every time it listens for gravitational waves, the faint ripples in spacetime produced when black holes collide or neutron stars merge. Catching those whispers means operating at the very edge of what physics permits.

One of LIGO's most powerful tools is **quantum squeezing**, a technique that exploits quantum mechanics to sharpen measurements. Quantum mechanics places a fundamental noise floor on any measurement, a limit you can't beat by building better equipment alone. But squeezing finds a loophole: by deliberately making one aspect of a light beam noisier, you can make another aspect quieter. It's the quieter one that LIGO needs.

During LIGO's third observing run (O3), squeezing cut quantum noise by up to 3.2 dB. That's a meaningful gain in a world where every fraction of a decibel matters. But the squeezer is finicky, and keeping it performing at its best over months-long observing runs remains an unsolved problem.

A team of researchers from MIT and IAIFI used machine learning to predict squeezing performance from environmental sensor data, a first step toward building AI systems that can automatically tune these quantum instruments in real time.

> **Key Insight:** Machine learning models trained on historical LIGO data can accurately predict how well the quantum squeezer is performing at any given moment and identify which environmental factors are degrading it, opening the door to AI-driven, closed-loop control of quantum noise reduction.

## How It Works

LIGO's squeezed light comes from an **optical parametric oscillator (OPO)**, a specialized crystal device that produces pairs of light particles with linked quantum properties. The squeezing level that actually reaches the interferometer depends on a cascade of factors: crystal temperature, pump power, mirror alignment, ground motion, thermal drifts, and dozens more.

Over O3, the Livingston detector averaged only 2.23 dB of squeezing, nearly 1 dB below peak, with a standard deviation of 0.36 dB. For next-generation detectors targeting 10 dB of squeezing, those fluctuations would be catastrophic.

![Figure 1](/iaifi-research-blog/figures/2305_13780/figure_1.png)

The researchers framed this as a prediction problem. They trained neural networks on O3 data, using **auxiliary channels** (sensor streams that monitor the detector's physical environment) as inputs to predict squeezing level. Input selection wasn't done by hand. Instead, they used a **genetic algorithm**, a search strategy modeled on natural selection where candidate input combinations compete and only the most informative survive, to identify which channels carry the most signal about squeezing performance.

The workflow breaks into three connected stages:

1. **Data curation** — pulling relevant auxiliary channels from the O3 dataset at LIGO Livingston Observatory
2. **Model training** — fitting neural networks to predict squeezing level, with genetic algorithm-driven feature selection
3. **Interpretation** — sensitivity analysis to rank and quantify the sources of squeezing degradation

The models weren't black boxes. The team performed **sensitivity analysis**, systematically varying each input to measure its effect on the output, to understand which factors drove predictions most strongly. This turned the model from a predictor into a diagnostic tool: an AI that can tell engineers what's degrading squeezing right now and by how much.

![Figure 2](/iaifi-research-blog/figures/2305_13780/figure_1.png)

## Why It Matters

Future detectors like Einstein Telescope and Cosmic Explorer are designed to reach up to 10 dB of squeezing. The light-loss fluctuations behind O3's variability, extrapolated to a 10 dB source, would drag performance well below target. That's not a minor inconvenience; it's a barrier to the science these detectors exist to do.

![Figure 3](/iaifi-research-blog/figures/2305_13780/figure_2.png)

The natural next step is a self-correcting AI control system for quantum instruments. This paper handles the sensing side: predicting squeezing from auxiliary data. What remains is actuation, having the model not just watch but intervene, adjusting squeezer parameters to push performance back toward optimum.

That's a harder problem, real-time control with physical consequences, but the prediction and diagnostic capability shown here is a necessary prerequisite. The implications also extend beyond gravitational-wave astronomy. Squeezed light is used broadly in quantum sensing, and maintaining quantum performance gains under real-world operating conditions is a universal challenge.

> **Bottom Line:** By training neural networks to predict LIGO's quantum squeezing performance from environmental sensors, this team built a diagnostic AI that pinpoints the sources of noise degradation, a necessary foundation for the AI-controlled quantum instruments that next-generation detectors will require.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses quantum optics engineering with modern machine learning, applying neural networks and genetic algorithms to optimize one of the most sensitive quantum instruments ever built.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The combination of neural network prediction with genetic algorithm-based feature selection and post-hoc sensitivity analysis shows how interpretable ML can function as a scientific diagnostic tool, not just a black-box predictor, in high-stakes experimental settings.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By identifying and quantifying the dominant sources of squeezing degradation in LIGO's O3 data, this research directly informs the design and operation of next-generation gravitational-wave observatories targeting squeezing levels up to 10 dB.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The authors frame this as the sensing half of a future closed-loop control system, with actuation on the squeezer subsystem as the next step; the full paper is available at [arXiv:2305.13780](https://arxiv.org/abs/2305.13780).</span></div></div>
</div>
