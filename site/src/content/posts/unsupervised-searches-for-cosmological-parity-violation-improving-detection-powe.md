---
abstract: Recent studies using four-point correlations suggest a parity violation
  in the galaxy distribution, though the significance of these detections is sensitive
  to the choice of simulation used to model the noise properties of the galaxy distribution.
  In a recent paper, we introduce an unsupervised learning approach which offers an
  alternative method that avoids the dependence on mock catalogs, by learning parity
  violation directly from observational data. However, the Convolutional Neural Network
  (CNN) model utilized by our previous unsupervised approach struggles to extend to
  more realistic scenarios where data is limited. We propose a novel method, the Neural
  Field Scattering Transform (NFST), which enhances the Wavelet Scattering Transform
  (WST) technique by adding trainable filters, parameterized as a neural field. We
  first tune the NFST model to detect parity violation in a simplified dataset, then
  compare its performance against WST and CNN benchmarks across varied training set
  sizes. We find the NFST can detect parity violation with $4\times$ less data than
  the CNN and $32\times$ less than the WST. Furthermore, in cases with limited data
  the NFST can detect parity violation with up to $6σ$ confidence, where the WST and
  CNN fail to make any detection. We identify that the added flexibility of the NFST,
  and particularly the ability to learn asymmetric filters, as well as the specific
  symmetries built into the NFST architecture, contribute to its improved performance
  over the benchmark models. We further demonstrate that the NFST is readily interpretable,
  which is valuable for physical applications such as the detection of parity violation.
arxivId: '2405.13083'
arxivUrl: https://arxiv.org/abs/2405.13083
authors:
- Matthew Craigie
- Peter L. Taylor
- Yuan-Sen Ting
- Carolina Cuesta-Lazaro
- Rossana Ruggeri
- Tamara M. Davis
concepts:
- parity violation
- wavelet scattering transform
- signal detection
- neural field
- symmetry preservation
- self-supervised learning
- hypothesis testing
- feature extraction
- interpretability
- convolutional networks
- spectral methods
- cosmological simulation
figures:
- /iaifi-research-blog/figures/2405_13083/figure_1.png
- /iaifi-research-blog/figures/2405_13083/figure_1.png
- /iaifi-research-blog/figures/2405_13083/figure_2.png
pdfUrl: https://arxiv.org/pdf/2405.13083v1
published: '2024-05-21T07:12:44+00:00'
theme: Astrophysics
title: 'Unsupervised Searches for Cosmological Parity Violation: Improving Detection
  Power with the Neural Field Scattering Transform'
wordCount: 1108
---

## The Big Picture

Imagine looking at your hand in a mirror. Your left hand becomes a right hand, and no matter how you rotate or flip it, the two are fundamentally different objects. This distinction between a thing and its mirror image is called **parity**, and for most of physics, the universe treats both equally. Gravity, electromagnetism, and the strong nuclear force work the same whether you're in the original universe or a mirror-reflected one.

But the weak nuclear force doesn't. Decades ago, physicists discovered it has a handedness built in. Now, cosmological evidence hints that something similar might be happening at the largest scales in the universe.

When astronomers map the three-dimensional positions of hundreds of thousands of galaxies, certain statistical patterns suggest that the **cosmic web** (the vast network of galaxy filaments and empty voids spanning the observable universe) might have a preferred handedness. If true, this would be one of the biggest discoveries in modern cosmology, pointing to new physics far beyond the standard model.

The trouble is, detecting such a signal is extremely hard, and previous methods have been plagued by uncertainty. A team of researchers from the University of Queensland, Ohio State, ANU, MIT, and the Harvard-Smithsonian Center for Astrophysics has developed a new tool called the **Neural Field Scattering Transform (NFST)** that can detect this mirror-symmetry breaking with far less data than any previous approach.

> **Key Insight:** By combining the stability of classical wavelet mathematics with the adaptability of neural networks, the NFST detects cosmological parity violation using 32 times less data than standard methods and achieves 6σ significance where competing approaches detect nothing at all.

## How It Works

Detecting parity violation in galaxies is fundamentally a geometry problem. A single point in space, or even a triangle of three points, has no handedness: you can always rotate it to match its mirror image. But four points forming a **tetrahedron** are different. Mirror one, and you can't rotate it back to the original.

Any statistical parity violation must therefore hide in the **four-point correlations**: the statistical relationships among groups of four galaxies, the simplest geometric arrangement that can encode handedness.

Traditional approaches compute these statistics directly (the **4PCF**, or four-point correlation function) and compare them against simulated "mock" galaxy catalogs. The problem is that the answer depends heavily on which simulation you use. One recent study showed that a claimed parity violation signal disappears entirely when you swap out one simulation package for another.

The NFST sidesteps this with an **unsupervised learning** strategy, where the model discovers patterns on its own rather than being told what to look for. Instead of comparing against simulations, the model trains directly on observational data, learning to distinguish a patch of the galaxy distribution from its mirror-flipped counterpart. If it consistently identifies the difference on held-out data, that's evidence of real parity violation, not a simulation artifact.

![Figure 1](/iaifi-research-blog/figures/2405_13083/figure_1.png)

The architecture layers three ideas:

1. **Wavelet Scattering Transform (WST):** A classical signal-processing technique, similar to how audio software analyzes sound at multiple pitches simultaneously, that filters the galaxy field at multiple scales and compresses the result into a compact summary. This summary is stable to noise and automatically ignores differences due to rotation or translation. The catch: the WST's built-in filters are symmetric by design, so they're blind to handedness.

2. **Neural Field Scattering Transform (NFST):** Here's the key innovation. The team replaces the WST's fixed filters with *trainable filters*, where each filter's shape is defined by a small **neural field**, a compact neural network that generates the filter from scratch. This lets the model learn asymmetric filters that can actually "see" the handedness of structures in the galaxy distribution while keeping the WST's noise robustness.

3. **Symmetry engineering:** The NFST enforces specific symmetries by design. It preserves rotational and translational invariance but *allows* parity asymmetry to emerge through the learned filters, so the model doesn't confuse "the universe is rotated" with "the universe has a handedness."

![Figure 2](/iaifi-research-blog/figures/2405_13083/figure_1.png)

The team first benchmarked on simplified 2D datasets with known parity violation signals, then compared the NFST against the standard WST and a Convolutional Neural Network (CNN) across a range of training set sizes. In real cosmology, data is always limited, so this comparison matters.

## Why It Matters

The performance difference is stark. The NFST detects parity violation with 4 times less data than the CNN and 32 times less than the standard WST.

In the most data-limited regimes, the NFST reaches 6σ statistical confidence (the gold standard for a discovery claim in physics) while the WST and CNN fail to register any detection at all.


Two properties drive this advantage: the ability to learn genuinely asymmetric filters (the WST's fixed wavelets are symmetric and thus parity-blind by construction), and architectural symmetry constraints that prevent the model from wasting capacity on irrelevant invariances.

The filters are also interpretable. Because they're explicitly parameterized, researchers can visualize what structures in the galaxy distribution the model responds to. In fundamental physics, understanding *why* a model detects something matters nearly as much as the detection itself.

The next step is applying the NFST to real three-dimensional galaxy survey data. The unsupervised framework means this can happen without the simulation-dependence that plagues the 4PCF approach. If parity violation is real, the NFST may be the tool that finally measures it with unambiguous confidence, pointing toward new physics at the largest scales of the cosmos.

> **Bottom Line:** The Neural Field Scattering Transform is a data-efficient, interpretable, and simulation-independent method for hunting one of cosmology's most intriguing anomalies. With 32x better data efficiency than current standard approaches, it could make the difference between a hint and a discovery.

---

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work unites classical wavelet mathematics, neural architecture design, and observational cosmology to tackle one of the field's hardest statistical challenges: detecting subtle symmetry violation hidden in the three-dimensional map of the universe.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The Neural Field Scattering Transform introduces trainable filters parameterized as neural fields that inherit the stability of wavelet theory while gaining the flexibility to learn task-specific, symmetry-breaking representations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By demonstrating a simulation-free route to detecting cosmological parity violation, achieving 6σ confidence where previous approaches fail, this work could resolve a contentious debate and point toward new physics beyond the standard cosmological model.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The team's next target is applying the NFST to real 3D galaxy survey data. The full methodology and benchmarks are available at [arXiv:2405.13083](https://arxiv.org/abs/2405.13083) (Craigie et al., "Unsupervised Searches for Cosmological Parity Violation: Improving Detection Power with the Neural Field Scattering Transform").</span></div></div>
</div>
