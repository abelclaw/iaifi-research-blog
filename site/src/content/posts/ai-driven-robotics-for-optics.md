---
abstract: Optics is foundational to research in many areas of science and engineering,
  including nanophotonics, quantum information, materials science, biomedical imaging,
  and metrology. However, the design, assembly, and alignment of optical experiments
  remain predominantly manual, limiting throughput and reproducibility. Automating
  such experiments is challenging due to the strict, non-negotiable precision requirements
  and the diversity of optical configurations found in typical laboratories. Here,
  we introduce a platform that integrates generative artificial intelligence, computer
  vision, and robotics to automate free-space optical experiments. The platform translates
  user-defined goals into valid optical configurations, assembles them using a robotic
  arm, and performs micrometer-scale fine alignment using a robot-deployable tool.
  It then executes a range of automated measurements, including beam characterization,
  polarization mapping, and spectroscopy, with consistency surpassing that of human
  operators. This work demonstrates the first flexible, AI-driven automation platform
  for optics, offering a path towards remote operation, cloud labs, and high-throughput
  discovery in the optical sciences.
arxivId: '2505.17985'
arxivUrl: https://arxiv.org/abs/2505.17985
authors:
- Shiekh Zia Uddin
- Sachin Vaidya
- Shrish Choudhary
- Zhuo Chen
- Raafat K. Salib
- Luke Huang
- Dirk R. Englund
- Marin Soljačić
concepts:
- scientific workflows
- robotic optical assembly
- llm optical agent
- fine-tuning
- micrometer alignment tool
- experimental design
- computer vision
- automated discovery
- data augmentation
- tensor networks
- inverse problems
- active learning
figures:
- /iaifi-research-blog/figures/2505_17985/figure_1.png
- /iaifi-research-blog/figures/2505_17985/figure_1.png
- /iaifi-research-blog/figures/2505_17985/figure_2.png
- /iaifi-research-blog/figures/2505_17985/figure_2.png
- /iaifi-research-blog/figures/2505_17985/figure_3.png
- /iaifi-research-blog/figures/2505_17985/figure_3.png
pdfUrl: https://arxiv.org/pdf/2505.17985v2
published: '2025-05-07T14:17:59+00:00'
theme: Experimental Physics
title: AI-Driven Robotics for Optics
wordCount: 1072
---

## The Big Picture

Picture a master optician hunched over a laser table at midnight, tweaking a tiny mirror by fractions of a millimeter, watching a pattern of alternating light and dark bands shimmer on the wall. One wrong nudge — a vibration from a passing truck, a slip of the wrist — and hours of careful alignment are undone. This is how cutting-edge optical experiments get built today: painstakingly, by hand, one human at a time.

Optics underpins an astonishing range of modern science. From gravitational wave detectors and quantum computers to cancer-screening microscopes and astronomical spectrographs, light is the universal probe. But the labs where this work happens look remarkably like they did fifty years ago — a researcher carefully sliding lenses and mirrors into position on a table engineered to absorb vibrations, iterating until the alignment is just right.

The precision required is brutal: components must sit within microns of their intended positions, and environmental disturbances can invalidate hours of work.

A team from MIT's IAIFI and Research Laboratory of Electronics has now built the first end-to-end AI-driven robotic platform that can design, assemble, align, and run optical experiments in open air — automatically, from a plain-English description of the experiment you want to perform.

> **Key Insight:** By combining fine-tuned large language models with computer vision and a robotic arm, researchers have automated every stage of a free-space optical experiment — from goal specification to physical assembly to measurement — achieving consistency that surpasses human operators.

## How It Works

The platform chains together three distinct AI-powered stages, each handling one phase of what a human experimentalist would normally do.

![Figure 1](/iaifi-research-blog/figures/2505_17985/figure_1.png)

**Stage 1: Design via fine-tuned LLMs.** A researcher types what they want — anything from "Give me a Mach-Zehnder interferometer" to "a Michelson interferometer with the beam entering at 30 degrees and the beamsplitter near coordinate (20 cm, 3 cm)." An **Optics Agent** — an AI assistant trained to interpret natural-language descriptions and translate them into physical layouts — takes that request and generates a list of optical components, their x-y positions, and orientations.

Under the hood, the Optics Agent is a LLaMA3.1-8B-Instruct model (an open-source language model from Meta) fine-tuned using **QuanTA (Quantum-informed Tensor Adaptation)** — a technique that borrows mathematical structures from quantum physics to update the model's behavior efficiently, without retraining all of its billions of parameters. The model was trained on a synthetically augmented dataset spanning four standard configurations — Michelson interferometer, Mach-Zehnder interferometer, Hong-Ou-Mandel interferometer, and a 4f imaging system — generated through geometric transformations and automatically captioned to mimic how real users describe experiments. A validation step checks whether the generated layout is physically feasible before passing it downstream.

**Stage 2: Robotic assembly.** A **Coding Agent** — an LLM that converts the validated layout into step-by-step robot instructions — then takes over. The robotic arm, equipped with a computer vision system:

- Identifies individual optical components on the table
- Picks each component and places it at its target position with sub-millimeter precision
- Applies a positional error correction loop using camera feedback
- Deploys a purpose-built **fine-alignment tool** that achieves micrometer-scale adjustments — the critical last step human operators typically spend the most time on

**Stage 3: Automated measurements.** Once assembled and aligned, the platform runs a full suite of optical measurements without further human input. The team demonstrated beam characterization, polarization mapping, transmission spectroscopy, and real-space optimization. Across repeated trials, the automated platform's measurements showed *less* variation than those from trained human operators performing the same tasks.

![Figure 2](/iaifi-research-blog/figures/2505_17985/figure_1.png)

The engineering challenge here shouldn't be underestimated. Experiments where laser light travels through open air — rather than through fiber-optic cables — are notoriously unforgiving: an angular misalignment of a fraction of a degree can walk a beam entirely off a detector. The robot-deployable fine-alignment tool is a key innovation: it lets the robotic arm handle coarse pick-and-place steps, then hand off to a specialized instrument that works at the precision the physics demands.

## Why It Matters

In the near term, this platform could dramatically accelerate the pace of optical research. A lab that currently needs days to set up a new interferometric experiment could reduce that to hours or minutes — reproducibly, across multiple setups running in parallel, with results that don't depend on which postdoc happened to be available. This matters enormously for quantum information science, where alignment is critical and reproducibility determines whether results can be trusted.

The longer arc points toward **cloud labs** — remote-access facilities where researchers anywhere in the world specify an optical experiment, have it assembled and run by a robot, and receive data back without visiting a physical laboratory. This model already exists in chemistry and genomics. This work makes it conceivable for optics. It also opens a path to high-throughput discovery: systematically scanning large spaces of optical configurations in search of new phenomena or optimal designs — something impractical for any human team to do manually.

There are also deeper questions this work raises for AI in science. The fine-tuned LLM here isn't just retrieving information — it's reasoning about spatial constraints, physical feasibility, and equipment requirements. Whether these capabilities generalize beyond the four demonstrated setup types, and how the system handles novel or ambiguous requests, remain active research questions.

> **Bottom Line:** MIT researchers have demonstrated the first flexible, AI-driven robotic platform for free-space optics, automating design, assembly, alignment, and measurement with consistency that outperforms human operators — opening a direct path to cloud labs and high-throughput optical discovery.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work exemplifies IAIFI's mission by combining frontier AI methods — LLM fine-tuning, computer vision, and generative design — with the precision demands of experimental optical physics to create a fully automated scientific instrument.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces a practical pipeline for deploying fine-tuned LLMs as physical-world design agents, where outputs must satisfy hard geometric and physical constraints — a challenging and underexplored regime for generative AI.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Automating optical experiments removes a key bottleneck in quantum information, nanophotonics, and precision measurement — fields where optical setups are essential instruments for probing fundamental physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend the platform to more complex configurations and toward fully remote cloud-lab operation; the paper is available on arXiv and was authored by researchers from MIT Physics, EECS, and the NSF IAIFI.</span></div></div>
</div>
