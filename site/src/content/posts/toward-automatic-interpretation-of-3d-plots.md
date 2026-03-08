---
abstract: This paper explores the challenge of teaching a machine how to reverse-engineer
  the grid-marked surfaces used to represent data in 3D surface plots of two-variable
  functions. These are common in scientific and economic publications; and humans
  can often interpret them with ease, quickly gleaning general shape and curvature
  information from the simple collection of curves. While machines have no such visual
  intuition, they do have the potential to accurately extract the more detailed quantitative
  data that guided the surface's construction. We approach this problem by synthesizing
  a new dataset of 3D grid-marked surfaces (SurfaceGrid) and training a deep neural
  net to estimate their shape. Our algorithm successfully recovers shape information
  from synthetic 3D surface plots that have had axes and shading information removed,
  been rendered with a variety of grid types, and viewed from a range of viewpoints.
arxivId: '2106.07627'
arxivUrl: https://arxiv.org/abs/2106.07627
authors:
- Laura E. Brandt
- William T. Freeman
concepts:
- 3d surface reconstruction
- convolutional networks
- inverse problems
- shape-from-contour
- synthetic dataset generation
- feature extraction
- regression
- data augmentation
- scientific workflows
- superresolution
figures:
- /iaifi-research-blog/figures/2106_07627/figure_1.png
- /iaifi-research-blog/figures/2106_07627/figure_1.png
- /iaifi-research-blog/figures/2106_07627/figure_2.png
- /iaifi-research-blog/figures/2106_07627/figure_2.png
- /iaifi-research-blog/figures/2106_07627/figure_3.png
- /iaifi-research-blog/figures/2106_07627/figure_3.png
pdfUrl: https://arxiv.org/pdf/2106.07627v1
published: '2021-06-14T17:32:53+00:00'
theme: Foundational AI
title: Toward Automatic Interpretation of 3D Plots
wordCount: 1002
---

## The Big Picture

Imagine flipping through a scientific paper and encountering a 3D surface plot — a rippling mesh of curves representing, say, a potential energy landscape in chemistry or a risk surface in economics. Your brain processes it almost instantly. You see the peaks, the valleys, how steeply one ridge slopes into another. Now imagine asking a computer to do the same thing. What felt effortless becomes fiendishly hard.

This is the challenge that Laura Brandt and William Freeman at MIT CSAIL set out to crack. Thousands of 3D surface plots are published every year across scientific disciplines, each encoding quantitative data in a form that humans read fluently but machines cannot parse. Tools exist to extract data from 2D charts — bar graphs, scatter plots, pie charts — but for 3D plots, there has been nothing. The data locked inside those rippling grids has been essentially inaccessible to automated systems.

Brandt and Freeman's solution: build a dataset from scratch, train a deep neural network on it, and show that a machine can learn to "see" 3D shape from the same visual cues — those sparse crossing lines on the surface — that human vision uses so fluently.

> **Key Insight:** A neural network trained on a purpose-built synthetic dataset can recover 3D shape information from grid-marked surface plots — even when axes and shading are stripped away entirely.

## How It Works

The core task the researchers defined is **shape recovery from grid-marked surfaces**: given an image of a 3D surface plot stripped of axis labels, color scales, and shading, can a neural network reconstruct what the underlying surface actually looks like?

![Figure 2](/iaifi-research-blog/figures/2106_07627/figure_1.png)

The first challenge was data. No large dataset of 3D surface plots paired with ground-truth shape information existed, so the team synthesized one. They created **SurfaceGrid**, a dataset of 98,600 images of 3D grid-marked surfaces rendered alongside their corresponding **depth maps** — pixel-by-pixel records of how far each point on the surface sits from the camera. Depth maps encode 3D shape as a 2D image, making them the ideal training target for a neural approach.

Generating SurfaceGrid required careful engineering of variability. The synthetic plots were rendered with:

- **Multiple grid types** — different line densities, colors, and styles mimicking real-world figure diversity
- **Varied viewpoints** — the virtual camera orbited around surfaces to simulate how authors choose different publication angles
- **No shading or axis information** — forcing the model to rely purely on the geometry of the grid curves

Stripping auxiliary cues was deliberate. In a real extraction pipeline, shading varies wildly between software packages, and axis labels require separate handling. By training on "naked" grid surfaces, the model learns the hardest part of the problem first.

The neural network is a **convolutional encoder-decoder architecture** — a model that compresses an image into a compact internal representation, then expands it back into a structured output, here a depth map. The encoder extracts features from the input grid image; the decoder reconstructs depth from those features. The researchers also ran **ablation studies** — experiments in which individual design components are removed or altered one at a time — to identify which choices mattered most.

![Figure 1](/iaifi-research-blog/figures/2106_07627/figure_1.png)

Across diverse synthetic conditions — multiple grid types, varying viewpoints, no shading — the algorithm successfully recovers shape. The model generalizes across the visual variation baked into SurfaceGrid, a necessary prerequisite for tackling real-world published figures.

## Why It Matters

The immediate application is practical: automated data extraction from scientific literature. Millions of published figures contain quantitative information currently invisible to search engines and indexing systems. A system that could read 3D plots the way TAPAS reads tables — Google's natural-language table-querying tool that Brandt and Freeman cite as inspiration — would transform how researchers navigate the scientific record. Instead of keyword searches, you could query by data shape: *find me all papers whose potential energy surfaces have a double-well structure in this region*.

The implications reach further than literature mining. The broader problem the paper addresses — **shape-from-X**, reconstructing 3D geometry from 2D image cues — is one of the oldest challenges in computer vision. Prior work by Marr, Stevens, Weiss, and others relied on hand-crafted geometric assumptions: surfaces are locally cylindrical, contours behave like springs, viewpoints are generic. These assumptions break down in the messy, application-specific context of scientific plots.

Brandt and Freeman's data-driven approach sidesteps those assumptions entirely, letting the network learn what constraints actually hold in the distribution of real 3D plots. The SurfaceGrid dataset itself is a contribution the community can build on — a resource for figure understanding, document analysis, and scientific data recovery.

Open questions remain. The current work focuses on synthetic data; bridging to real published figures requires handling axis detection, legend separation, and calibration — steps the authors explicitly flag as future work. Recovering actual numerical values also requires a deprojection step to undo the perspective transformation applied when the figure was originally rendered.

> **Bottom Line:** Brandt and Freeman have cracked open the 3D plot problem with a neural approach, creating the first dataset and model for automated shape recovery from grid-marked surfaces — paving the way toward machines that can read scientific figures as fluently as human researchers do.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges computer vision and scientific data extraction, developing tools that could automate the interpretation of 3D figures across physics, chemistry, and other quantitative sciences.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The SurfaceGrid dataset (98,600 synthetic images with paired depth maps) and the trained encoder-decoder model establish a new benchmark and baseline for the underexplored problem of 3D chart interpretation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Automated 3D plot reading could accelerate literature discovery in physics and related fields, enabling researchers to search scientific databases by data content rather than keywords alone.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend the pipeline to handle axis calibration, deprojection, and real-world published figures; the paper is available on arXiv as an IAIFI publication.</span></div></div>
</div>
