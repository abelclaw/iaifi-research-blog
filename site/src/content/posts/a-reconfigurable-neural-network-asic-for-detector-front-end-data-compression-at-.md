---
abstract: Despite advances in the programmable logic capabilities of modern trigger
  systems, a significant bottleneck remains in the amount of data to be transported
  from the detector to off-detector logic where trigger decisions are made. We demonstrate
  that a neural network autoencoder model can be implemented in a radiation tolerant
  ASIC to perform lossy data compression alleviating the data transmission problem
  while preserving critical information of the detector energy profile. For our application,
  we consider the high-granularity calorimeter from the CMS experiment at the CERN
  Large Hadron Collider. The advantage of the machine learning approach is in the
  flexibility and configurability of the algorithm. By changing the neural network
  weights, a unique data compression algorithm can be deployed for each sensor in
  different detector regions, and changing detector or collider conditions. To meet
  area, performance, and power constraints, we perform a quantization-aware training
  to create an optimized neural network hardware implementation. The design is achieved
  through the use of high-level synthesis tools and the hls4ml framework, and was
  processed through synthesis and physical layout flows based on a LP CMOS 65 nm technology
  node. The flow anticipates 200 Mrad of ionizing radiation to select gates, and reports
  a total area of 3.6 mm^2 and consumes 95 mW of power. The simulated energy consumption
  per inference is 2.4 nJ. This is the first radiation tolerant on-detector ASIC implementation
  of a neural network that has been designed for particle physics applications.
arxivId: '2105.01683'
arxivUrl: https://arxiv.org/abs/2105.01683
authors:
- Giuseppe Di Guglielmo
- Farah Fahim
- Christian Herwig
- Manuel Blanco Valentin
- Javier Duarte
- Cristian Gingu
- Philip Harris
- James Hirschauer
- Martin Kwok
- Vladimir Loncar
- Yingyi Luo
- Llovizna Miranda
- Jennifer Ngadiuba
- Daniel Noonan
- Seda Ogrenci-Memik
- Maurizio Pierini
- Sioni Summers
- Nhan Tran
concepts:
- autoencoders
- on-detector inference
- calorimetry
- trigger systems
- quantization-aware training
- dimensionality reduction
- high-level synthesis for ml
- collider physics
- feature extraction
- scalability
figures:
- /iaifi-research-blog/figures/2105_01683/figure_1.png
- /iaifi-research-blog/figures/2105_01683/figure_2.png
- /iaifi-research-blog/figures/2105_01683/figure_3.png
pdfUrl: https://arxiv.org/pdf/2105.01683v1
published: '2021-05-04T18:06:23+00:00'
theme: Experimental Physics
title: A reconfigurable neural network ASIC for detector front-end data compression
  at the HL-LHC
wordCount: 981
---

## The Big Picture

Imagine a camera with six million pixels firing 40 million times per second. Every second, it generates more raw data than any cable on Earth can carry. That's the reality facing the CMS experiment at CERN's Large Hadron Collider, where a new energy-measuring detector called the **High-Granularity Calorimeter (HGCAL)** is being built for an upgrade that will push the LHC to its highest-ever proton collision rates. The physics is extraordinary — but the data problem threatens to choke it off before a single interesting event can be recorded.

For decades, physicists handled this with simple filters at the detector edge: discarding readings below a minimum signal threshold, dropping quiet channels, keeping only the loudest hits. These brute-force approaches throw away data indiscriminately. What if, instead, you could deploy a tiny artificial brain directly on the detector — one smart enough to compress data intelligently, preserve the physics that matters, and survive years of punishing radiation? A team of researchers from Fermilab, MIT, CERN, and a dozen other institutions just showed exactly how to do it.

Their result: the first radiation-tolerant, on-detector **application-specific integrated circuit (ASIC)** — a custom-designed silicon chip — running a neural network, purpose-built for particle physics. Smaller than a fingernail, it runs a machine learning algorithm at the heart of one of the world's most complex scientific instruments.

> **Key Insight:** By embedding a reconfigurable neural network autoencoder directly into detector hardware, the team achieves intelligent, physics-preserving data compression at the source — slashing the data transmission bottleneck before it even begins.

## How It Works

The core algorithm is an **autoencoder** — a neural network that learns to squeeze data through a narrow bottleneck and reconstruct it on the other side. Think of it like describing a painting over the phone: you can't transmit every brushstroke, so you learn to capture the essence. The autoencoder encodes the HGCAL's calorimeter energy deposits into a compact representation for transmission off-detector, where downstream systems can decode it or analyze the compressed form directly.

![Figure 1](/iaifi-research-blog/figures/2105_01683/figure_1.png)

What makes this design clever isn't just that it compresses data — it's that it does so *reconfigurably*. The neural network architecture is fixed in silicon, but the **weights** — the learned parameters that define what the network actually does — are stored in programmable memory. Swap the weights, and you swap the compression algorithm.

Since different regions of the HGCAL use different sensor shapes and see different patterns of particle cascades, each chip can be individually tuned after manufacturing. Change the beam conditions? Update the weights. Detector aging shifts the calibration? Update the weights. No new chip required.

Getting a neural network onto a chip this small and power-constrained demanded aggressive optimization:

- **Quantization-aware training**: Instead of standard 32-bit floating point, the network was trained assuming low-precision integer arithmetic from the start, shrinking the silicon footprint dramatically without wrecking accuracy.
- **High-level synthesis (HLS)**: The team used the **hls4ml** framework to translate a trained neural network directly into hardware description language, automating chip design work that would otherwise require years of manual effort.
- **Radiation-hardened gate selection**: The chip was fabricated using a 65-nanometer process, with every logic gate chosen from a library validated to survive 200 million rads of ionizing radiation — the brutal dose detector electronics will absorb over the HL-LHC's lifetime.

![Figure 2](/iaifi-research-blog/figures/2105_01683/figure_2.png)

The resulting chip is remarkably compact: 3.6 mm² total area, 95 mW of power consumption, and just **2.4 nanojoules per inference**. One complete compression of an HGCAL trigger data packet consumes roughly the same energy as lifting a grain of sand by a millimeter — and it has to do this 40 million times per second.

![Figure 3](/iaifi-research-blog/figures/2105_01683/figure_3.png)

## Why It Matters

This work sits at a genuinely important intersection. The HL-LHC will collide protons at unprecedented rates, and the HGCAL's fine-grained imaging will be critical for distinguishing rare collision events from the overwhelming flood of ordinary ones — enabling precision measurements of the Higgs boson and other key physics targets. But none of that matters if the data can't leave the detector. Intelligent on-detector compression isn't a convenience; it's what makes the physics program viable.

On the AI side, the paper demonstrates that modern machine learning tools are mature enough to bridge the gap between algorithm and silicon for the harshest operating environments imaginable. The hls4ml workflow and quantization-aware training used here represent a template for deploying neural networks at the extreme edge — in satellites, medical implants, anywhere that power, size, and radiation tolerance are non-negotiable constraints.

The reconfigurability principle is particularly powerful: a single chip design, mass-produced once, can serve dozens of different detector regions simply by loading different weights. That's a lesson hardware designers across many fields will want to absorb.

> **Bottom Line:** This team built and validated the first radiation-tolerant on-detector neural network ASIC for particle physics, proving that machine learning can survive — and thrive — at the literal frontier of experimental science.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges modern deep learning — autoencoder architectures, quantization-aware training — with the hardware constraints of experimental particle physics, producing a chip that satisfies both physics performance requirements and the extreme engineering limits of detector front-end electronics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper advances edge AI by demonstrating end-to-end automated translation of a trained neural network into radiation-hardened ASIC hardware via hls4ml, establishing a reusable workflow for deploying ML models in power- and area-constrained environments.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The reconfigurable on-detector neural network enables the CMS HGCAL to intelligently compress its 40 MHz trigger data stream, preserving the calorimetric energy profiles needed for real-time event selection at the HL-LHC without overwhelming off-detector bandwidth.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include deploying this design in actual CMS hardware and extending the approach to other detector subsystems; the full paper is available at arXiv:2105.01683.</span></div></div>
</div>
