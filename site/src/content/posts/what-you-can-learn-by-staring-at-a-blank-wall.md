---
abstract: We present a passive non-line-of-sight method that infers the number of
  people or activity of a person from the observation of a blank wall in an unknown
  room. Our technique analyzes complex imperceptible changes in indirect illumination
  in a video of the wall to reveal a signal that is correlated with motion in the
  hidden part of a scene. We use this signal to classify between zero, one, or two
  moving people, or the activity of a person in the hidden scene. We train two convolutional
  neural networks using data collected from 20 different scenes, and achieve an accuracy
  of $\approx94\%$ for both tasks in unseen test environments and real-time online
  settings. Unlike other passive non-line-of-sight methods, the technique does not
  rely on known occluders or controllable light sources, and generalizes to unknown
  rooms with no re-calibration. We analyze the generalization and robustness of our
  method with both real and synthetic data, and study the effect of the scene parameters
  on the signal quality.
arxivId: '2108.13027'
arxivUrl: https://arxiv.org/abs/2108.13027
authors:
- Prafull Sharma
- Miika Aittala
- Yoav Y. Schechner
- Antonio Torralba
- Gregory W. Wornell
- William T. Freeman
- Fredo Durand
concepts:
- non-line-of-sight imaging
- convolutional networks
- classification
- signal detection
- indirect illumination model
- inverse problems
- robustness
- passive scene inference
- feature extraction
- dimensionality reduction
- surrogate modeling
figures:
- /iaifi-research-blog/figures/2108_13027/figure_1.png
- /iaifi-research-blog/figures/2108_13027/figure_1.png
- /iaifi-research-blog/figures/2108_13027/figure_2.png
- /iaifi-research-blog/figures/2108_13027/figure_2.png
- /iaifi-research-blog/figures/2108_13027/figure_3.png
- /iaifi-research-blog/figures/2108_13027/figure_3.png
pdfUrl: https://arxiv.org/pdf/2108.13027v1
published: '2021-08-30T07:30:19+00:00'
theme: Foundational AI
title: What You Can Learn by Staring at a Blank Wall
wordCount: 1065
---

## The Big Picture

Imagine standing outside a room with the door closed. You can't see inside, can't hear anything, and you're not emitting any signal. All you have is a view of the blank wall opposite the doorway. Can you tell if someone is moving in that room? To the naked eye, absolutely not. But a camera and a neural network can — with 94% accuracy.

This is the premise of research from MIT that sounds like it belongs in a spy thriller but is grounded in real physics. Every time a person moves in a room, they subtly alter how light bounces around that space. They block some light paths, open up others, and create new reflections.

These changes wash over every surface — including walls that appear to be doing nothing. The signal is buried under noise, imperceptible to any human observer. But it's there.

The researchers built a system that extracts these ghost signals from ordinary video and uses them to classify hidden human activity and count hidden people — all without placing a sensor in the room or knowing anything about its geometry in advance.

> **Key Insight:** Motion in a hidden scene leaves a detectable fingerprint on the indirect illumination of a blank wall — and a convolutional neural network can read that fingerprint with 94% accuracy, even in rooms it has never seen before.

## How It Works

The physics starts with **indirect illumination** — light that reaches a wall not directly from a lamp, but after bouncing off one or more other surfaces in the room. When a person walks behind a closed door, they change which light paths are open and which are blocked, reshuffling the patchwork of faint reflected light landing on the visible wall.

The effect is extraordinarily subtle: the researchers measured the signal at between −20 dB and −35 dB below background imaging noise — roughly 100 to 3,000 times weaker than the camera's own noise floor. You'd never notice it, but it's mathematically present in every pixel.

![Figure 1](/iaifi-research-blog/figures/2108_13027/figure_1.png)

To extract this signal, the team built a multi-stage pipeline:

1. **Video capture**: A regular camera records the blank wall. No lasers, no projectors, no specialized hardware.
2. **Signal extraction**: The video is projected into a compact **2D representation** that summarizes how the wall's illumination changes over time and across space.
3. **Classification**: Two separate **convolutional neural networks (CNNs)** — neural networks designed to recognize patterns in image-like data — take this representation as input. One classifies the *number of people* present (zero, one, or two); the other classifies the *activity* (walking, jumping, waving, crouching, or none).

![Figure 2](/iaifi-research-blog/figures/2108_13027/figure_1.png)

Training required data from 20 different rooms — varying geometries, furniture arrangements, lighting setups, and wall materials. The key test: could the networks generalize to rooms they'd never seen, with no re-calibration?

The answer was yes. On five held-out test scenes, the system achieved **94.4% accuracy on people-counting** and **93.7% on activity recognition**, running in real time with negligible latency.

What distinguishes this approach among **non-line-of-sight (NLOS) sensing** methods — techniques for detecting things you can't directly see — is what it doesn't require. Most passive NLOS techniques depend on known occluders: a visible corner, a table edge, or a post sticking out of the floor that acts as an accidental lens imposing structure on the incoming light. Remove those occluders, and existing methods collapse. This system works on a featureless wall with no known geometry and no cooperation from the environment.

![Figure 3](/iaifi-research-blog/figures/2108_13027/figure_2.png)

The team also built a synthetic simulation to identify which scene parameters most affect signal quality. Distance between people and the wall, number and placement of light sources, and surface **reflectance** (how much light a surface bounces back) all shape how much signal bleeds through the noise floor — characterizing both the limits and surprising robustness of the approach.

## Why It Matters

The immediate applications are genuinely important: search and rescue teams locating survivors in collapsed buildings, autonomous vehicles detecting pedestrians around corners, or elderly care systems monitoring falls without placing cameras in private spaces. The passive nature of the system — no emitter, no active probing — makes it deployable where emitting signals would be impractical, detectable, or impossible.

The deeper significance is what this paper reveals about information hiding in plain sight. We've long assumed a blank wall carries no useful information about what's happening on the other side. This work proves that assumption wrong in a fundamental way.

Light transport is not a one-way street — it's a complex, many-bounced web of mutual dependencies, and perturbing any node leaves traces everywhere else. Machine learning, applied to carefully designed signal representations, turned out to be the key that unlocked it.

Future directions are rich. The current system classifies coarse categories — it can tell you someone is walking, but not who they are or exactly where. Extending to finer-grained localization, trajectory tracking, or more complex multi-person scenarios will require richer representations and more data.

There's also a natural question about adversarial scenarios: if someone knows this technique exists, can they defeat it? Understanding the signal's robustness to deliberate countermeasures will matter as the technology matures.

> **Bottom Line:** A blank wall is not a blank canvas — it's a noisy, low-fidelity record of everything happening in the room it faces. Researchers at MIT have shown that convolutional neural networks can decode that record well enough to classify human activity and count people with 94% accuracy, in real time, in rooms they've never visited.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits at the intersection of computational physics and machine learning, using rigorous light transport theory to motivate a signal representation that neural networks can exploit — neither field alone would have been sufficient.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper demonstrates that CNNs can generalize across highly variable physical environments when trained on well-structured signal representations, achieving near-94% accuracy on unseen rooms without fine-tuning or re-calibration.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By formalizing how motion perturbs indirect illumination through multi-bounce light transport, the work advances the theoretical understanding of passive sensing and the limits of information encoded in scattered light.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will push toward finer-grained localization and tracking in more complex scenes; the full paper, code, and data are available at wallcamera.csail.mit.edu, with the work presented at ICCV 2021.</span></div></div>
</div>
