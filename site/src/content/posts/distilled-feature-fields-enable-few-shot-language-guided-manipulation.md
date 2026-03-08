---
abstract: Self-supervised and language-supervised image models contain rich knowledge
  of the world that is important for generalization. Many robotic tasks, however,
  require a detailed understanding of 3D geometry, which is often lacking in 2D image
  features. This work bridges this 2D-to-3D gap for robotic manipulation by leveraging
  distilled feature fields to combine accurate 3D geometry with rich semantics from
  2D foundation models. We present a few-shot learning method for 6-DOF grasping and
  placing that harnesses these strong spatial and semantic priors to achieve in-the-wild
  generalization to unseen objects. Using features distilled from a vision-language
  model, CLIP, we present a way to designate novel objects for manipulation via free-text
  natural language, and demonstrate its ability to generalize to unseen expressions
  and novel categories of objects.
arxivId: '2308.07931'
arxivUrl: https://arxiv.org/abs/2308.07931
authors:
- William Shen
- Ge Yang
- Alan Yu
- Jansen Wong
- Leslie Pack Kaelbling
- Phillip Isola
concepts:
- distilled feature fields
- representation learning
- neural radiance fields
- few-shot manipulation
- embeddings
- feature extraction
- self-supervised learning
- transfer learning
- contrastive learning
- transformers
- fine-tuning
figures:
- /iaifi-research-blog/figures/2308_07931/figure_1.png
- /iaifi-research-blog/figures/2308_07931/figure_1.png
- /iaifi-research-blog/figures/2308_07931/figure_2.png
- /iaifi-research-blog/figures/2308_07931/figure_2.png
- /iaifi-research-blog/figures/2308_07931/figure_3.png
- /iaifi-research-blog/figures/2308_07931/figure_3.png
pdfUrl: https://arxiv.org/pdf/2308.07931v2
published: '2023-07-27T17:59:14+00:00'
theme: Foundational AI
title: Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation
wordCount: 1234
---

## The Big Picture

Imagine handing a new employee a warehouse manifest and asking them to find "the red ceramic mug with the chipped handle" among hundreds of cluttered bins. They can do it. They understand language, recognize objects by shape and texture, and know how to grip a fragile cup differently from a metal wrench. Now imagine asking a robot to do the same thing. Suddenly, nearly every piece of that sentence becomes a hard open problem in robotics.

Modern AI models trained on enormous collections of internet images have become very good at understanding *what* things are. But robots live in a three-dimensional world. They don't just need to recognize a mug; they need to know exactly where to wrap their fingers around it in 3D space. That's fundamentally different knowledge, and the two have been hard to combine.

Image-based AI systems are blind to depth and geometry: they can't tell you where an object sits in space or how to reach for it. Systems that work with 3D geometry, meanwhile, can't understand what objects *mean* or connect them to language. This disconnect has been a stubborn obstacle in robotics.

A team from MIT CSAIL and IAIFI went after the problem head-on. The result is **F3RM** (Feature Fields for Robotic Manipulation), a system that teaches robots to grasp and place objects in the wild, guided by a few examples or a plain English description.

> **Key Insight:** By baking rich 2D language and visual features into a 3D neural scene representation, F3RM gives robots a world model that is simultaneously geometrically precise and semantically aware, enabling generalization to novel objects and open-ended language commands with just a handful of demonstrations.

## How It Works

The pipeline starts with something almost comically low-tech: the robot takes a series of photos of a tabletop scene using an RGB camera mounted on a selfie stick. Those photos feed into the first major component.

![Figure 1](figure:1)

**Step 1: Build a feature field.** The team trains a **Neural Radiance Field (NeRF)**, a neural network that reconstructs a 3D scene from ordinary 2D photos by predicting color and density at every point in space. F3RM adds a twist: alongside RGB color, the NeRF simultaneously predicts *feature vectors* from a pre-trained 2D vision model at every 3D location.

The result is a **Distilled Feature Field (DFF)**, a 3D scene map where every point carries rich descriptive information inherited from massive internet-trained models. Think of it as a 3D sponge that has absorbed both geometry and meaning.

Training a NeRF used to take hours, which would be impractical for real-time robotics. The researchers address this by adopting **hierarchical hashgrids**, which analyze scene structure at multiple spatial scales simultaneously, cutting modeling time to a workable window.

**Step 2: Extract the right features.** The system draws on two pre-trained AI models, each serving a different purpose:

- **DINO ViT**, a visual model trained without human labels, whose internal features act as powerful fingerprints for matching object parts across different instances of the same category
- **CLIP**, a vision-language model trained on image-text pairs, whose features align visual concepts with natural language

There's a subtlety here. CLIP produces image-level features: a single descriptor for a whole photo. Baking features into a 3D field requires *dense*, pixel-level descriptors. The researchers solve this with the **MaskCLIP reparameterization trick**, which tweaks CLIP's internal processing to produce location-specific features for each image patch while preserving its ability to connect images to language.

**Step 3: Generalize from demos or language.** Given a few demonstrations of grasping a particular object category (say, a mug grabbed by its handle), the system matches the 3D feature signature of that demo to the best corresponding location on a new, unseen object. Because DINO features encode structural similarity across instances, a robot that learned to hold one mug can transfer that grip to a different mug it has never seen.

For language-guided manipulation, a user types a query like "the green toy" or "the object you would pour water from," and the system queries the CLIP feature field to generate a 3D heatmap of relevance. The highest-activation region identifies the target object, and the robot infers a full **6-DOF grasp pose** from that location: three values for position, three for orientation.

![Figure 2](figure:2)

That full six-degrees-of-freedom precision is what allows the system to handle objects in arbitrary poses, not just upright items sitting neatly on a flat surface.

## Why It Matters

The interesting thing about F3RM is not just that it works, but *what* it generalizes across. The robot handles objects that differ from demonstrations in shape, size, material, and orientation. It responds to language queries never seen during training, including novel phrasings and entirely new object categories. Open-ended generalization like this has been the white whale of robotic manipulation research for years.

The deeper implication is architectural. F3RM shows that knowledge locked inside large vision-and-language models, distilled from billions of internet images and text-image pairs, can be transplanted into 3D representations without losing that richness. This points toward a new class of robot world models: not hand-crafted geometric representations, not purely visual neural networks, but hybrid structures that inherit the best of both.

As large AI models continue to scale and improve, robotic systems built on this foundation stand to benefit automatically.

> **Bottom Line:** F3RM shows that a robot armed with a few demos and a semantic 3D feature field can pick up objects it has never seen before, guided by nothing but plain English. That's a meaningful step toward warehouse robots, assistive systems, and any machine that must act intelligently in an uncontrolled world.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work fuses techniques from computer vision (NeRF, CLIP, DINO), natural language processing, and robotic manipulation into a single pipeline, a clear example of the cross-disciplinary work at the core of IAIFI's mission.

- **Impact on Artificial Intelligence:** F3RM provides a general method for lifting rich 2D foundation model features into 3D neural representations, opening a path for grounding language and vision in physical 3D space.

- **Impact on Fundamental Interactions:** Giving robots the ability to reason jointly about 3D geometry and semantics pushes forward the physical understanding needed for machines to interact precisely and safely with the material world.

- **Outlook and References:** Future directions include extending F3RM to dynamic scenes and multi-step manipulation tasks. The work was presented at CoRL 2023, with code and demos available at f3rm.csail.mit.edu.

## Original Paper Details
- **Title:** Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation
- **arXiv ID:** [arXiv:2308.07931](https://arxiv.org/abs/2308.07931)
- **Authors:** William Shen, Ge Yang, Alan Yu, Jansen Wong, Leslie Pack Kaelbling, Phillip Isola
- **Abstract:** Self-supervised and language-supervised image models contain rich knowledge of the world that is important for generalization. Many robotic tasks, however, require a detailed understanding of 3D geometry, which is often lacking in 2D image features. This work bridges this 2D-to-3D gap for robotic manipulation by leveraging distilled feature fields to combine accurate 3D geometry with rich semantics from 2D foundation models. We present a few-shot learning method for 6-DOF grasping and placing that harnesses these strong spatial and semantic priors to achieve in-the-wild generalization to unseen objects. Using features distilled from a vision-language model, CLIP, we present a way to designate novel objects for manipulation via free-text natural language, and demonstrate its ability to generalize to unseen expressions and novel categories of objects.
