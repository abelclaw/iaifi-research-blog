---
abstract: IceCube is a Cherenkov detector instrumenting over a cubic kilometer of
  glacial ice deep under the surface of the South Pole. The DeepCore sub-detector
  lowers the detection energy threshold to a few GeV, enabling the precise measurements
  of neutrino oscillation parameters with atmospheric neutrinos. The reconstruction
  of neutrino interactions inside the detector is essential in studying neutrino oscillations.
  It is particularly challenging to reconstruct sub-100 GeV events with the IceCube
  detectors due to the relatively sparse detection units and detection medium. Convolutional
  neural networks (CNNs) are broadly used in physics experiments for both classification
  and regression purposes. This paper discusses the CNNs developed and employed for
  the latest IceCube-DeepCore oscillation measurements. These CNNs estimate various
  properties of the detected neutrinos, such as their energy, direction of arrival,
  interaction vertex position, flavor-related signature, and are also used for background
  classification.
arxivId: '2505.16777'
arxivUrl: https://arxiv.org/abs/2505.16777
authors:
- IceCube Collaboration
concepts:
- convolutional networks
- event reconstruction
- neutrino detection
- neutrino oscillation reconstruction
- classification
- regression
- feature extraction
- detector simulation
- uncertainty quantification
figures:
- /iaifi-research-blog/figures/2505_16777/figure_1.png
- /iaifi-research-blog/figures/2505_16777/figure_2.png
- /iaifi-research-blog/figures/2505_16777/figure_2.png
pdfUrl: https://arxiv.org/pdf/2505.16777v3
published: '2025-05-22T15:19:02+00:00'
theme: Experimental Physics
title: Fast Low Energy Reconstruction using Convolutional Neural Networks
wordCount: 1004
---

## The Big Picture

Imagine trying to figure out the direction, speed, and identity of a ghost — not by seeing it, but by watching how scattered candles flicker as it passes through the room. That's roughly the challenge facing physicists at the South Pole. The IceCube Neutrino Observatory tries to reconstruct the properties of neutrinos: subatomic particles so elusive that trillions pass through your body every second without interacting.

Neutrinos come in three "flavors" and they *oscillate*, spontaneously changing type as they travel. Measuring how fast and completely they oscillate reveals deep truths about the Standard Model of particle physics. But to make those measurements, you first need to know where a neutrino came from, how much energy it carried, and what type it was.

Deep in the Antarctic ice, that reconstruction is hard. IceCube's latest work deploys a suite of **convolutional neural networks (CNNs)**, deep learning models originally developed to recognize patterns in photographs, trained to extract neutrino properties from sparse light signals in glacial ice. The payoff: reconstruction speeds and accuracies that make precision oscillation measurements possible at scale.

> **Key Insight:** By treating IceCube detector data as a structured 3D image, CNNs can simultaneously estimate neutrino energy, direction, vertex position, flavor, and reject background, fast enough to power the full oscillation analysis pipeline.

## How It Works

The IceCube detector buries 5,160 optical sensors in a cubic kilometer of Antarctic ice, arranged in vertical strings. When a neutrino collides with a water molecule, it produces a charged particle that emits **Cherenkov radiation**, a faint cone of blue light picked up by the sensors. The **DeepCore** sub-array occupies the densest, clearest region and pushes the detection threshold to just a few GeV, where atmospheric neutrino oscillations are most pronounced.

![Figure 1](/iaifi-research-blog/figures/2505_16777/figure_1.png)

Below 100 GeV, events produce only a handful of photons across a small number of sensors. Traditional reconstruction methods, which fit particle tracks and cascades analytically, become slow and unreliable at these low energies. The fix: reframe the problem as computer vision.

Each event is mapped onto a **hexagonally-structured 3D grid** that preserves the geometric layout of the detector strings. CNNs, built to find faint patterns in spatially-organized data, turn out to be well suited to this structure.

The architecture processes events through several layers of learned filters:

1. **Input representation** — Raw photon arrival times and total charge at each **DOM (Digital Optical Module)** are encoded into image-like arrays, accounting for the hexagonal geometry of DeepCore strings.
2. **Convolutional layers** — Successive 3D convolutions detect local patterns (clusters of hits, timing gradients) and build up to detector-scale features.
3. **Output heads** — Separate branches predict reconstructed energy; zenith angle (the neutrino's arrival direction measured from directly overhead); interaction vertex coordinates; a **particle identification (PID)** score distinguishing track-like events (muons leaving long trails) from cascade-like events (electron or tau neutrinos producing compact, spherical bursts); and a background classifier separating genuine neutrino interactions from atmospheric muons.

![Figure 2](/iaifi-research-blog/figures/2505_16777/figure_2.png)

Speed was a hard constraint. Oscillation analyses require processing millions of simulated and real events. Likelihood-based methods can take seconds per event; the CNN reconstructions run orders of magnitude faster.

![Figure 3](/iaifi-research-blog/figures/2505_16777/figure_2.png)

The networks were trained on detailed **Monte Carlo simulations** that mimic particle interactions and detector response, including photon propagation through inhomogeneous ice with depth-dependent scattering and absorption. Validation on real data confirmed that the networks generalize from simulation to observation, which is a notoriously difficult step in particle physics machine learning.


The CNN energy estimator achieves better resolution than previous methods at low energies, and directional reconstruction similarly outperforms classical fits. The PID network cleanly separates muon neutrinos (track signatures) from electron and tau neutrinos (cascade signatures), a separation essential for measuring both the disappearance and appearance channels of neutrino oscillation.


## Why It Matters

Neutrino oscillation measurements probe physics the Standard Model barely anticipated. The precise values of the **mixing angles**, quantum mechanical parameters governing how much one neutrino flavor mixes with another, touch on some of the deepest open questions in physics: the origin of matter-antimatter asymmetry, grand unification, and potential new physics beyond the Standard Model.

IceCube-DeepCore sits in a sweet spot. It measures atmospheric neutrinos at energies and distances where the dominant oscillation channel, muon neutrino disappearance, hits maximum effect. This gives it competitive sensitivity to the mixing angle **θ₂₃** and mass-squared splitting **Δm²₃₂**, two of the most important parameters in the neutrino sector.

This CNN framework isn't a minor upgrade. It is the backbone of IceCube's current-generation oscillation analysis. Fast, accurate reconstruction makes full likelihood analyses feasible, exploiting the complete reconstructed phase space rather than a handful of binned observables. As the proposed **IceCube Upgrade** adds densely-instrumented low-energy strings, this kind of reconstruction becomes even more necessary.


The approach also offers a template for other sparse 3D Cherenkov detectors, from ORCA in the Mediterranean to future water-based neutrino telescopes. When detector geometry can be mapped to a structured grid, the full toolkit of computer vision becomes available for particle physics reconstruction.

> **Bottom Line:** IceCube's CNN-based reconstruction turns sparse light patterns in Antarctic ice into precise neutrino properties at speeds that make large-scale oscillation analyses practical. The paper is available at [arXiv:2505.16777](https://arxiv.org/abs/2505.16777).

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies convolutional neural network architectures, originally developed for image recognition, directly to 3D particle detector data, enabling precision neutrino oscillation measurements that classical methods could not achieve at scale.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Mapping irregular hexagonal detector geometry to structured CNN-compatible inputs and training simultaneous multi-task networks for regression and classification shows how deep learning can be deployed in non-standard spatial domains.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The CNNs power IceCube-DeepCore's latest measurements of mixing parameters θ₂₃ and Δm²₃₂, tightening constraints on one of the most enigmatic sectors of the Standard Model.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend these methods to the denser IceCube Upgrade geometry and deeper statistical analyses of the full reconstructed phase space; the paper ([arXiv:2505.16777](https://arxiv.org/abs/2505.16777)) is prepared for submission to JINST.</span></div></div>
</div>
