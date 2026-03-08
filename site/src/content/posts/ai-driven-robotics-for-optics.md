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
wordCount: 1008
---

## The Big Picture

Picture a master optician hunched over a laser table at midnight, tweaking a tiny mirror by fractions of a millimeter, watching a pattern of alternating light and dark bands shimmer on the wall. One wrong nudge, a vibration from a passing truck or a slip of the wrist, and hours of careful alignment are undone. This is how optical experiments still get built: painstakingly, by hand, one human at a time.

Optics is behind an astonishing range of modern science. Gravitational wave detectors, quantum computers, cancer-screening microscopes, astronomical spectrographs: light is the universal probe. But the labs where this work happens look remarkably like they did fifty years ago. A researcher carefully slides lenses and mirrors into position on a vibration-isolated table, iterating until the alignment is just right. Components must sit within microns of their intended positions, and environmental disturbances can invalidate hours of work.

A team from MIT's IAIFI and Research Laboratory of Electronics has now built the first end-to-end AI-driven robotic platform that can design, assemble, align, and run optical experiments in open air, automatically, from a plain-English description of the experiment you want to perform.

> **Key Insight:** By combining fine-tuned large language models with computer vision and a robotic arm, the researchers automated every stage of a free-space optical experiment, from goal specification to physical assembly to measurement, achieving consistency that surpasses human operators.

## How It Works

The platform chains together three AI-powered stages, each handling one phase of what a human experimentalist would normally do.

![Figure 1](figure:1)

**Stage 1: Design via fine-tuned LLMs.** A researcher types what they want, anything from "Give me a Mach-Zehnder interferometer" to "a Michelson interferometer with the beam entering at 30 degrees and the beamsplitter near coordinate (20 cm, 3 cm)." An **Optics Agent**, an AI assistant trained to interpret natural-language descriptions and translate them into physical layouts, takes that request and generates a list of optical components with their x-y positions and orientations.

The Optics Agent is a LLaMA3.1-8B-Instruct model (Meta's open-source language model) fine-tuned using **QuanTA (Quantum-informed Tensor Adaptation)**, a technique that borrows mathematical structures from quantum physics to update the model's behavior efficiently without retraining all of its billions of parameters. Training data came from a synthetically augmented dataset spanning four standard configurations: Michelson interferometer, Mach-Zehnder interferometer, Hong-Ou-Mandel interferometer, and a 4f imaging system. These were generated through geometric transformations and automatically captioned to mimic how real users describe experiments. A validation step checks whether the generated layout is physically feasible before passing it downstream.

**Stage 2: Robotic assembly.** A **Coding Agent**, an LLM that converts the validated layout into step-by-step robot instructions, then takes over. The robotic arm, equipped with a computer vision system:

- Identifies individual optical components on the table
- Picks each component and places it at its target position with sub-millimeter precision
- Applies a positional error correction loop using camera feedback
- Deploys a purpose-built **fine-alignment tool** that achieves micrometer-scale adjustments, the step human operators typically spend the most time on

**Stage 3: Automated measurements.** Once assembled and aligned, the platform runs a full suite of optical measurements without further human input. The team demonstrated beam characterization, polarization mapping, transmission spectroscopy, and real-space optimization. Across repeated trials, the automated platform's measurements showed *less* variation than those from trained human operators performing the same tasks.

![Figure 2](figure:2)

The engineering difficulty here is real. Experiments where laser light travels through open air (rather than through fiber-optic cables) are notoriously unforgiving: an angular misalignment of a fraction of a degree can walk a beam entirely off a detector. The robot-deployable fine-alignment tool solves this by letting the robotic arm handle coarse pick-and-place steps, then handing off to a specialized instrument that works at the precision the physics demands.

## Why It Matters

In the near term, this platform could dramatically accelerate optical research. A lab that currently needs days to set up a new interferometric experiment could reduce that to hours or minutes, reproducibly, across multiple setups running in parallel, with results that don't depend on which postdoc happened to be available. For quantum information science, where alignment is everything and reproducibility determines whether results can be trusted, that's a big deal.

The longer arc points toward **cloud labs**: remote-access facilities where researchers anywhere in the world specify an optical experiment, have it assembled and run by a robot, and receive data back without visiting a physical laboratory. This model already exists in chemistry and genomics. The work reported here makes it conceivable for optics.

It also opens a path to high-throughput discovery, systematically scanning large spaces of optical configurations in search of new phenomena or optimal designs. No human team could do that manually.

The fine-tuned LLM here isn't just retrieving information. It reasons about spatial constraints, physical feasibility, and equipment requirements. Whether these capabilities generalize beyond the four demonstrated setup types, and how the system handles novel or ambiguous requests, remain open questions.

> **Bottom Line:** The first flexible, AI-driven robotic platform for free-space optics can design, assemble, align, and measure with consistency that outperforms human operators, opening a direct path to cloud labs and high-throughput optical discovery.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This project sits squarely at IAIFI's intersection of AI and physics, combining LLM fine-tuning, computer vision, and generative design with the precision demands of experimental optics to create a fully automated scientific instrument.

- **Impact on Artificial Intelligence:** The paper introduces a practical pipeline for deploying fine-tuned LLMs as physical-world design agents, where outputs must satisfy hard geometric and physical constraints, a challenging and underexplored regime for generative AI.

- **Impact on Fundamental Interactions:** Automating optical experiments removes a major bottleneck in quantum information, nanophotonics, and precision measurement, fields where optical setups are essential instruments for probing fundamental physics.

- **Outlook and References:** Future work could extend the platform to more complex configurations and toward fully remote cloud-lab operation; the paper is available at [arXiv:2505.17985](https://arxiv.org/abs/2505.17985) and was authored by researchers from MIT Physics, EECS, and the NSF IAIFI.
