---
abstract: Suspended optics in gravitational wave (GW) observatories are susceptible
  to alignment perturbations, particularly slow drifts over time, due to variations
  in temperature and seismic levels. Such misalignments affect the coupling of the
  incident laser beam into the optical cavities, degrade both circulating power and
  optomechanical photon squeezing and thus decrease the astrophysical sensitivity
  to merging binaries. Traditional alignment techniques involve differential wavefront
  sensing using multiple quadrant photodiodes but are often restricted in bandwidth
  and are limited by the sensing noise. We present the first-ever successful implementation
  of neural network-based sensing and control at a gravitational wave observatory
  and demonstrate low-frequency control of the signal recycling mirror at the GEO
  600 detector. Alignment information for three critical optics is simultaneously
  extracted from the interferometric dark port camera images via a CNN-LSTM network
  architecture and is then used for MIMO control using soft actor-critic-based deep
  reinforcement learning. Overall sensitivity improvement achieved using our scheme
  demonstrates deep learning's capabilities as a viable tool for real-time sensing
  and control for current and next-generation GW interferometers.
arxivId: '2301.06221'
arxivUrl: https://arxiv.org/abs/2301.06221
authors:
- Nikhil Mukund
- James Lough
- Aparna Bisht
- Holger Wittel
- Séverin Landry Nadji
- Christoph Affeldt
- Fabio Bergamin
- Marc Brinkmann
- Volker Kringel
- Harald Lück
- Michael Weinert
- Karsten Danzmann
concepts:
- reinforcement learning
- optical cavity control
- gravitational waves
- convolutional networks
- recurrent networks
- mimo control
- feature extraction
- dark port imaging
- inverse problems
- surrogate modeling
- signal detection
- multi-task learning
figures:
- /iaifi-research-blog/figures/2301_06221/figure_1.png
- /iaifi-research-blog/figures/2301_06221/figure_1.png
- /iaifi-research-blog/figures/2301_06221/figure_2.png
- /iaifi-research-blog/figures/2301_06221/figure_2.png
- /iaifi-research-blog/figures/2301_06221/figure_3.png
- /iaifi-research-blog/figures/2301_06221/figure_3.png
pdfUrl: https://arxiv.org/pdf/2301.06221v2
published: '2023-01-16T00:32:46+00:00'
theme: Astrophysics
title: First demonstration of neural sensing and control in a kilometer-scale gravitational
  wave observatory
wordCount: 1135
---

## The Big Picture

Imagine trying to detect a ripple in spacetime so faint it would stretch a kilometer-long laser beam by less than one-thousandth the width of a proton — and then imagine that the mirror guiding your laser keeps drifting out of position because the ground is trembling and the temperature fluctuates. That's the daily reality inside a gravitational wave observatory. These machines are the most sensitive measurement devices ever built, and keeping them pointed at the right thing is a constant battle.

GEO 600 is a 600-meter precision laser detector near Hannover, Germany — one of the world's premier gravitational wave observatories. Like LIGO and Virgo, it splits a laser beam, bounces it down two long arms, and recombines it to detect microscopic distortions caused by passing gravitational waves.

The mirrors doing the bouncing hang from pendulums, and they drift — slowly, relentlessly — as ground vibrations and temperature changes nudge them out of alignment. Traditional correction systems analyze tiny differences in the laser beam's shape to infer where each mirror is pointing. They do an impressive job, but they can only respond to slow changes, they're prone to sensor noise, and they require human intervention about once a week.

A team from the Max Planck Institute for Gravitational Physics and MIT has now crossed a milestone: the first successful deployment of a neural network-based sensing and control system inside a real, kilometer-scale gravitational wave observatory.

> **Key Insight:** By replacing classical photodiode-based alignment sensors with a deep learning system trained on camera images, and pairing it with reinforcement learning control, researchers achieved real-time mirror alignment at GEO 600 — improving the detector's astrophysical sensitivity in the process.

## How It Works

The classical approach relies on shining laser light whose brightness is varied in a controlled pattern, then reading the result off **quadrant photodiodes (QPDs)** — sensors divided into four sections that detect where a beam is hitting. It works, but it's noisy, responds only to slow changes, and breaks down when beams drift off-center by even one beam radius, at which point 86% of the sensing signal is lost.

The new system takes a fundamentally different approach. Instead of dedicated photodiodes, it watches the **dark port camera** — already installed at GEO 600 — which images light leaking out of the interferometer's output. This image encodes rich information about the alignment state of multiple mirrors simultaneously, buried in subtle patterns of light and dark.

![Figure 1](/iaifi-research-blog/figures/2301_06221/figure_1.png)

To decode that information, the team trained a **CNN-LSTM network**: a hybrid combining a convolutional neural network (CNN), which extracts spatial features from images, with a long short-term memory (LSTM) recurrent network, which tracks how things change over time. Together, they simultaneously extract alignment information for *three* critical optical components from a single image stream: the signal recycling mirror, the Michelson mirror, and a third key optic.

![Figure 2](/iaifi-research-blog/figures/2301_06221/figure_1.png)

Good sensor data is only half the problem. The other half is deciding what to do with it. Here the team deployed a **soft actor-critic (SAC) reinforcement learning** controller — an algorithm that learns a control policy by maximizing a reward signal while also maximizing entropy, keeping it from over-committing to any single strategy. The SAC agent handles **MIMO control** (multiple-input, multiple-output), simultaneously nudging multiple mirrors based on the CNN-LSTM's alignment estimates.

The training pipeline ran in four stages:
1. Collect real interferometer data to train the CNN-LSTM sensing network
2. Use the trained sensor to estimate alignment states from dark port images
3. Train the SAC agent in simulation to learn a control policy
4. Deploy the full system in real time at GEO 600, controlling the SR mirror at low frequencies

![Figure 4](/iaifi-research-blog/figures/2301_06221/figure_2.png)

The key target was **low-frequency signal recycling mirror control** — the gradual drifts that classical systems handle most poorly. The signal recycling (SR) mirror sits at the output port of the interferometer and amplifies gravitational wave signals. Keeping it aligned maintains circulating power, preserves the quantum squeezing of light that boosts sensitivity, and prevents noise from contaminating the final strain readout.

![Figure 5](/iaifi-research-blog/figures/2301_06221/figure_3.png)

## Why It Matters

The sensitivity improvement this system delivers is the clearest proof that deep learning has crossed from laboratory curiosity to operational tool in precision physics. The traditional system required manual recalibration roughly once per week because environmental disturbances — seismic events, thermal drifts — would knock beam spots off their photodiodes. The neural approach reads directly from camera images, making it far more robust to these perturbations. It sees what's happening in the detector from the light itself, without needing dedicated auxiliary sensors to stay on-target.

![Figure 6](/iaifi-research-blog/figures/2301_06221/figure_3.png)

This matters enormously for next-generation observatories. Einstein Telescope and Cosmic Explorer — planned detectors with arms stretching 10 to 40 kilometers — will face alignment challenges dramatically more complex than today's instruments. The number of independently moving optical components grows, the interactions between them become more intricate, and the sensitivity stakes get higher. A neural sensing and control system that can simultaneously track multiple optics from a single camera feed and adaptively correct for their interactions is exactly what these future machines will need.

The GEO 600 demonstration is a proof-of-concept in a real operating environment — not a simulation, not a tabletop test, but a live kilometer-scale detector hunting for signals from merging neutron stars. Open questions remain: how well the approach generalizes to more complex configurations, how it handles rapid transient disturbances, and how it integrates with existing classical control loops. But those are the questions of a maturing technology, not an unproven idea.

> **Bottom Line:** Researchers have proven for the first time that a neural network — watching a camera, guided by reinforcement learning — can keep a gravitational wave detector's mirrors aligned better than the system it supplements, opening a direct path toward AI-assisted control of the next generation of gravitational wave observatories.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges state-of-the-art deep learning (CNN-LSTM sensing, soft actor-critic reinforcement learning) with precision experimental physics, demonstrating that AI can operate as a real-time control system inside one of the world's most sensitive scientific instruments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The deployment of a MIMO soft actor-critic controller for real-time, low-frequency control in a high-stakes physical environment advances practical reinforcement learning beyond simulation, showing it can stabilize complex multi-input, multi-output dynamical systems with real consequences for measurement quality.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By improving alignment control of the signal recycling mirror at GEO 600, the system directly enhances gravitational wave detector sensitivity — sharpening humanity's ability to observe and characterize compact binary mergers and other sources of spacetime ripples.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will target higher-bandwidth control, integration with next-generation detectors like Einstein Telescope, and extension to additional optical degrees of freedom; full details appear in arXiv:2304.13356.</span></div></div>
</div>
