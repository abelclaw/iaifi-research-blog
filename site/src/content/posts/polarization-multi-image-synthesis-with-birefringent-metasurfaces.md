---
abstract: "Optical metasurfaces composed of precisely engineered nanostructures have\
  \ gained significant attention for their ability to manipulate light and implement\
  \ distinct functionalities based on the properties of the incident field. Computational\
  \ imaging systems have started harnessing this capability to produce sets of coded\
  \ measurements that benefit certain tasks when paired with digital post-processing.\
  \ Inspired by these works, we introduce a new system that uses a birefringent metasurface\
  \ with a polarizer-mosaicked photosensor to capture four optically-coded measurements\
  \ in a single exposure. We apply this system to the task of incoherent opto-electronic\
  \ filtering, where digital spatial-filtering operations are replaced by simpler,\
  \ per-pixel sums across the four polarization channels, independent of the spatial\
  \ filter size. In contrast to previous work on incoherent opto-electronic filtering\
  \ that can realize only one spatial filter, our approach can realize a continuous\
  \ family of filters from a single capture, with filters being selected from the\
  \ family by adjusting the post-capture digital summation weights. To find a metasurface\
  \ that can realize a set of user-specified spatial filters, we introduce a form\
  \ of gradient descent with a novel regularizer that encourages light efficiency\
  \ and a high signal-to-noise ratio. We demonstrate several examples in simulation\
  \ and with fabricated prototypes, including some with spatial filters that have\
  \ prescribed variations with respect to depth and wavelength.\n  Visit the Project\
  \ Page at https://deanhazineh.github.io/publications/Multi_Image_Synthesis/MIS_Home.html"
arxivId: '2307.08106'
arxivUrl: https://arxiv.org/abs/2307.08106
authors:
- Dean Hazineh
- Soon Wei Daniel Lim
- Qi Guo
- Federico Capasso
- Todd Zickler
concepts:
- birefringent metasurface
- inverse problems
- opto-electronic filtering
- loss function design
- polarization-coded imaging
- surrogate modeling
- scalability
- experimental design
figures:
- /iaifi-research-blog/figures/2307_08106/figure_1.png
- /iaifi-research-blog/figures/2307_08106/figure_1.png
- /iaifi-research-blog/figures/2307_08106/figure_2.png
- /iaifi-research-blog/figures/2307_08106/figure_2.png
- /iaifi-research-blog/figures/2307_08106/figure_3.png
- /iaifi-research-blog/figures/2307_08106/figure_3.png
pdfUrl: https://arxiv.org/pdf/2307.08106v4
published: '2023-07-16T17:14:39+00:00'
theme: Foundational AI
title: Polarization Multi-Image Synthesis with Birefringent Metasurfaces
wordCount: 995
---

## The Big Picture

Imagine capturing a photo and simultaneously applying multiple artistic filters: one sharpening edges, another blurring backgrounds by depth, a third isolating specific wavelengths of light. Today you'd capture first, then run each filter separately in software, burning computational resources proportional to filter size. In real-time embedded systems or power-constrained environments, that bottleneck is real.

People have long wanted to offload some of this computation to optics itself, letting physics do the math before a photon hits the sensor. Previous systems could pull this off, but only for one filter at a time, and only with bulky bench-sized hardware involving beamsplitters and carefully aligned parallel optical paths.

A Harvard/Purdue team has built a compact, single-optic system that captures four differently-coded images simultaneously in one exposure. From those four images, it reconstructs not just one spatial filter, but an entire continuous family of filters, all without computation beyond a simple weighted sum.

> **Key Insight:** By pairing a specially engineered flat lens with a sensor that measures light arriving at different orientations, this system offloads multi-filter image processing to optics, reducing digital computation to a per-pixel weighted sum regardless of filter size.

## How It Works

The system has two core components. The first is a **birefringent metasurface**, a flat optical element just hundreds of nanometers thick, patterned with an array of precisely shaped silicon nanofins. "Metasurface" refers to any engineered surface with structures finer than the wavelength of light. "Birefringent" means it treats light differently depending on polarization, or which direction the light wave oscillates.

Each nanofin acts as a tiny polarization prism, delaying light oscillating in one direction by a different amount than the other. By controlling each nanofin's width parameters (*wx* and *wy*), engineers sculpt how light from any scene point fans out across the sensor (the **point spread function**, or PSF) and make that spreading pattern differ by polarization.

![Figure 1](/iaifi-research-blog/figures/2307_08106/figure_1.png)

The second component is a **polarization-mosaicked photosensor**, a camera sensor tiled with tiny polarization filters, analogous to how a Bayer RGB sensor tiles red, green, and blue filters across pixels. Four linear polarization orientations (0°, 45°, 90°, 135°) cover the pixel array. When light passes through the metasurface and lands on this sensor, each of the four polarization channels records a differently-coded version of the scene. The coding is baked into the optics: the metasurface's nanofin geometry determines the four PSFs.

Here's the elegant part. Any target spatial filter can be approximated as a linear combination of those four PSFs. Synthesizing a filtered image reduces to:

1. Capture one exposure, with four polarization channels recorded simultaneously
2. Choose summation weights *α₀°, α₄₅°, α₉₀°, α₁₃₅°*
3. Compute a per-pixel weighted sum across channels

No digital convolution. No sliding a filter template pixel by pixel across an image. Filter size doesn't matter computationally because physics handles it. And by changing only the weights after capture, you select any filter from a continuous family that the metasurface was designed to span.

![Figure 2](/iaifi-research-blog/figures/2307_08106/figure_1.png)

Designing the metasurface is a non-trivial inverse problem: working backwards from desired filters to precise nanofin shapes. The team solves it with **gradient descent**, iteratively nudging the design toward better solutions. They introduce a novel **regularizer** (a penalty term that discourages theoretically valid but practically useless solutions) to steer the optimizer away from designs that are too dim or too noisy for real imaging conditions.

## Why It Matters

Previous systems combining optics and electronics for filtering could synthesize exactly one spatial filter. They required beamsplitters and parallel optical paths, and couldn't distinguish scene content from the natural polarization of materials in the scene, a fundamental limitation for real-world use.

This system changes all three constraints at once. The single flat metasurface replaces bulky conventional optics. The four-channel architecture unlocks an entire filter family from one capture. And because polarization filters are applied at the aperture rather than at the scene, the system works on unpolarized real-world scenes without assumptions about material properties. Prior compact systems couldn't close that gap.

Spatial filtering is foundational in computer vision, scientific imaging, and machine perception. It's how cameras detect edges, isolate depth layers, or distinguish materials by their light signatures. The team shows edge detection, depth-selective focus, and wavelength-selective imaging in both simulation and with fabricated prototypes, including filters with prescribed depth and wavelength dependence that have no post-capture digital equivalent.

Where computational power is scarce (embedded sensors, satellite imagers, real-time robotics), moving filtering into optics could make a serious difference. The team also releases **D-Flat**, an open-source package for end-to-end metasurface design, making it easier for other groups to build on this foundation.

![Figure 4](/iaifi-research-blog/figures/2307_08106/figure_2.png)

> **Bottom Line:** A metasurface thinner than a wavelength of light, paired with a polarization sensor and a weighted sum, can replace large digital convolutions entirely, and do so for an infinite family of filters from a single snapshot.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work sits at the intersection of nanophotonic engineering, computational imaging, and machine learning optimization. The team uses gradient-based methods from AI to solve an inverse optics problem, determining nanostructure geometry at the sub-wavelength scale.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The approach shows that AI-inspired optimization (gradient descent with task-specific regularization) can design physical systems that move computational workloads from software to hardware, pointing toward a new class of physics-accelerated inference pipelines.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By engineering the polarization-dependent interaction of light with precisely patterned nanostructures, the work deepens our understanding of how birefringent metasurfaces can independently manipulate orthogonal polarization states to encode information optically.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending the filter family to higher-dimensional spans and integrating D-Flat for automated metasurface co-design. The work was presented at the 2023 IEEE International Conference on Computational Photography ([arXiv:2307.08106](https://arxiv.org/abs/2307.08106)), with the project page at https://deanhazineh.github.io/publications/Multi_Image_Synthesis/MIS_Home.html.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Polarization Multi-Image Synthesis with Birefringent Metasurfaces</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[2307.08106](https://arxiv.org/abs/2307.08106)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">Dean Hazineh, Soon Wei Daniel Lim, Qi Guo, Federico Capasso, Todd Zickler</span></div></div>
</div>
