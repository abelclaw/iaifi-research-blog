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
wordCount: 1092
---

## The Big Picture

Imagine trying to detect a ripple in spacetime so faint it would stretch a kilometer-long laser beam by less than one-thousandth the width of a proton. Now imagine that the mirror guiding your laser keeps drifting out of position because the ground is trembling and the temperature won't hold still. That's the daily reality inside a gravitational wave observatory. These machines are the most sensitive measurement devices ever built, and keeping them locked on target is a constant fight.

GEO 600 is a 600-meter precision laser detector near Hannover, Germany. Like LIGO and Virgo, it splits a laser beam, bounces it down two long arms, and recombines it to detect microscopic distortions caused by passing gravitational waves.

The mirrors doing the bouncing hang from pendulums, and they drift. Slowly, relentlessly, ground vibrations and temperature changes nudge them out of alignment. Traditional correction systems analyze tiny differences in the laser beam's shape to figure out where each mirror is pointing. They do an impressive job, but they can only respond to slow changes, they're prone to sensor noise, and they need human intervention about once a week.

A team from the Max Planck Institute for Gravitational Physics and MIT has now pulled off a first: the successful deployment of a neural network-based sensing and control system inside a real, kilometer-scale gravitational wave observatory.

> **Key Insight:** By replacing classical photodiode-based alignment sensors with a deep learning system trained on camera images, and pairing it with reinforcement learning control, researchers achieved real-time mirror alignment at GEO 600, improving the detector's astrophysical sensitivity in the process.

## How It Works

The classical approach shines laser light whose brightness is varied in a controlled pattern, then reads the result off **quadrant photodiodes (QPDs)**, sensors divided into four sections that detect where a beam is hitting. It works, but it's noisy, only responds to slow changes, and breaks down when beams drift off-center by even one beam radius. At that point, 86% of the sensing signal is lost.

The new system takes a different approach. Instead of dedicated photodiodes, it watches the **dark port camera** already installed at GEO 600, which images light leaking out of the interferometer's output. This image encodes rich information about the alignment state of multiple mirrors simultaneously, buried in subtle patterns of light and dark.

![Figure 1](/iaifi-research-blog/figures/2301_06221/figure_1.png)

To decode that information, the team trained a **CNN-LSTM network**: a hybrid combining a convolutional neural network (CNN) for extracting spatial features from images with a long short-term memory (LSTM) recurrent network for tracking how things change over time. The network pulls alignment information for *three* critical optical components from a single image stream: the signal recycling mirror, the Michelson mirror, and a third key optic.

![Figure 2](/iaifi-research-blog/figures/2301_06221/figure_1.png)

Good sensor data is only half the problem. The other half is deciding what to do with it. Here the team deployed a **soft actor-critic (SAC) reinforcement learning** controller, an algorithm that learns a control policy by maximizing a reward signal while also maximizing entropy to keep it from over-committing to any single strategy. The SAC agent handles multiple-input, multiple-output (MIMO) control, simultaneously nudging multiple mirrors based on the CNN-LSTM's alignment estimates.

The training pipeline ran in four stages:
1. Collect real interferometer data to train the CNN-LSTM sensing network
2. Use the trained sensor to estimate alignment states from dark port images
3. Train the SAC agent in simulation to learn a control policy
4. Deploy the full system in real time at GEO 600, controlling the SR mirror at low frequencies

![Figure 4](/iaifi-research-blog/figures/2301_06221/figure_2.png)

The main target was low-frequency signal recycling mirror control, the gradual drifts that classical systems handle most poorly. The signal recycling (SR) mirror sits at the output port of the interferometer and amplifies gravitational wave signals. Keeping it aligned maintains circulating power, preserves the quantum squeezing of light that boosts sensitivity, and prevents noise from contaminating the final strain readout.

![Figure 5](/iaifi-research-blog/figures/2301_06221/figure_3.png)

## Why It Matters

The sensitivity improvement here is the clearest proof yet that deep learning has moved from lab prototype to working tool in precision physics. The traditional system needed manual recalibration roughly once per week because environmental disturbances (seismic events, thermal drifts) would knock beam spots off their photodiodes. The neural approach reads directly from camera images and is far more robust to these perturbations. It sees what's happening in the detector from the light itself, no dedicated auxiliary sensors required.

![Figure 6](/iaifi-research-blog/figures/2301_06221/figure_3.png)

This has real implications for next-generation observatories. Einstein Telescope and Cosmic Explorer, planned detectors with arms stretching 10 to 40 kilometers, will face alignment challenges far more complex than today's instruments. More independently moving optical components, more intricate interactions between them, higher sensitivity stakes. A neural sensing and control system that can track multiple optics from a single camera feed and adaptively correct for their interactions is well suited to these future machines.

The GEO 600 demonstration is a proof-of-concept in a real operating environment. Not a simulation, not a tabletop test, but a live kilometer-scale detector hunting for signals from merging neutron stars. Open questions remain: how well the approach generalizes to more complex configurations, how it handles rapid transient disturbances, and how it integrates with existing classical control loops. But those are engineering questions for a maturing technology, not doubts about whether the idea works.

> **Bottom Line:** For the first time, a neural network watching a camera and guided by reinforcement learning has kept a gravitational wave detector's mirrors aligned better than the system it supplements. The result points toward AI-assisted control of the next generation of gravitational wave observatories. Full details are in [arXiv:2301.06221](https://arxiv.org/abs/2301.06221).

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects state-of-the-art deep learning (CNN-LSTM sensing, soft actor-critic reinforcement learning) with precision experimental physics, showing that AI can operate as a real-time control system inside one of the world's most sensitive scientific instruments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Deploying a MIMO soft actor-critic controller for real-time, low-frequency control in a high-stakes physical environment pushes practical reinforcement learning beyond simulation. The system stabilizes a complex multi-input, multi-output dynamical system where control quality directly affects measurement sensitivity.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By improving alignment control of the signal recycling mirror at GEO 600, the system directly enhances gravitational wave detector sensitivity, sharpening the ability to observe and characterize compact binary mergers and other astrophysical sources.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work targets higher-bandwidth control, integration with next-generation detectors like Einstein Telescope, and extension to additional optical degrees of freedom. Full details appear in [arXiv:2301.06221](https://arxiv.org/abs/2301.06221).</span></div></div>
</div>
