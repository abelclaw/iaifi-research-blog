---
abstract: 'The human visual system is well-tuned to detect faces of all shapes and
  sizes. While this brings obvious survival advantages, such as a better chance of
  spotting unknown predators in the bush, it also leads to spurious face detections.
  ``Face pareidolia'''' describes the perception of face-like structure among otherwise
  random stimuli: seeing faces in coffee stains or clouds in the sky. In this paper,
  we study face pareidolia from a computer vision perspective. We present an image
  dataset of ``Faces in Things'''', consisting of five thousand web images with human-annotated
  pareidolic faces. Using this dataset, we examine the extent to which a state-of-the-art
  human face detector exhibits pareidolia, and find a significant behavioral gap between
  humans and machines. We find that the evolutionary need for humans to detect animal
  faces, as well as human faces, may explain some of this gap. Finally, we propose
  a simple statistical model of pareidolia in images. Through studies on human subjects
  and our pareidolic face detectors we confirm a key prediction of our model regarding
  what image conditions are most likely to induce pareidolia. Dataset and Website:
  https://aka.ms/faces-in-things'
arxivId: '2409.16143'
arxivUrl: https://arxiv.org/abs/2409.16143
authors:
- Mark Hamilton
- Simon Stent
- Vasha DuTell
- Anne Harrington
- Jennifer Corbett
- Ruth Rosenholtz
- William T. Freeman
concepts:
- face pareidolia
- human-machine perceptual gap
- convolutional networks
- fine-tuning
- transfer learning
- visual psychophysics
- robustness
- feature extraction
- representation learning
- stochastic processes
- classification
- data augmentation
figures:
- /iaifi-research-blog/figures/2409_16143/figure_1.png
- /iaifi-research-blog/figures/2409_16143/figure_2.png
- /iaifi-research-blog/figures/2409_16143/figure_3.png
pdfUrl: https://arxiv.org/pdf/2409.16143v1
published: '2024-09-24T14:50:21+00:00'
theme: Foundational AI
title: 'Seeing Faces in Things: A Model and Dataset for Pareidolia'
wordCount: 1040
---

## The Big Picture

Look at the front of a car. Do you see a face staring back at you? Most people do — the headlights become eyes, the grille a grinning mouth. This isn't imagination running wild. It's one of the most deeply wired reflexes in the human brain: **face pareidolia**, the irresistible tendency to perceive faces in random objects, from wood grain to burnt toast to cloud formations.

For most of human evolutionary history, this hair-trigger face detector was a survival advantage. Spot a predator's eyes in the brush a fraction of a second sooner, and you live. The cost — occasionally "seeing" a face in a rock — was cheap. But here's the twist: AI face-recognition systems that match or exceed human performance on real faces are essentially blind to pareidolic ones. A model trained on millions of face photos will stare at a cloud shaped like a grinning skull and see nothing at all.

A team of researchers from MIT, Microsoft, Toyota Research Institute, and NVIDIA set out to close that gap. They built the first large-scale dataset of pareidolic faces, investigated why the machine-human divide exists, and proposed a mathematical model that predicts when and why pareidolia strikes.

> **Key Insight:** Face pareidolia isn't a quirk or a bug in human perception — it may be a direct consequence of our evolutionary need to detect *all kinds* of animal faces, not just human ones. AI systems trained only on human faces miss this broader tuning almost entirely.

## How It Works

The researchers built their investigation on a new foundation: **"Faces in Things"**, a dataset of five thousand web-collected images, each containing a pareidolic face. Human annotators marked each image with **bounding boxes** — rectangles drawn around face-like regions — and labeled them for perceived emotion, gender, and whether the face-like quality seemed intentional.

![Figure 1](/iaifi-research-blog/figures/2409_16143/figure_1.png)

With the dataset in hand, the team ran **RetinaFace** — a state-of-the-art detector trained on the WIDER FACE benchmark, a standard industry measure of face-detection performance — against the pareidolic images. The model almost completely failed to detect what humans found obvious. Even when the detector's confidence threshold was lowered far below normal operating levels, the machine struggled. This "behavioral gap" wasn't merely quantitative; it was qualitative.

To understand why, the researchers tried several interventions:

- **Image augmentation** — digitally manipulating training images to resemble pareidolic scenes
- **Threshold relaxation** — lowering the model's bar for what counts as a detection
- **Fine-tuning on animal faces** — adapting the model by continuing to train it on images of dogs, cats, and primates

The animal face result was the most revealing. Fine-tuning on non-human animals closed roughly **half** the performance gap without ever showing the model a single pareidolic image. Human pareidolia, it turns out, isn't purely about human face detection. It emerges from a broader, evolutionarily ancient system tuned to recognize faces across species.

![Figure 2](/iaifi-research-blog/figures/2409_16143/figure_2.png)

Why doesn't pareidolia trigger everywhere? Any sufficiently blurry texture could, in principle, trip the face detector — yet it doesn't. The researchers tackled this with a mathematical model.

They proposed two complementary frameworks. The first treats image patches as samples from a **Gaussian process** — a statistical model describing how similar neighboring pixels tend to be across a surface. The second uses **deep feature similarity**, measuring how closely the patterns a neural network extracts from an image patch match a typical face template. Both converge on the same prediction: pareidolia occurs in a "Goldilocks zone" of visual complexity.

Images that are too uniform (a flat gray wall) contain nothing face-like. Images that are too chaotic (static noise) overwhelm the face-detection mechanism. Pareidolia peaks in between — where texture is structured enough to suggest faces but random enough to produce them spuriously. Perception experiments on human subjects confirmed the prediction: both humans and trained detectors showed the same upside-down U-shaped curve, peaking at intermediate complexity and dropping off at both extremes.

![Figure 3](/iaifi-research-blog/figures/2409_16143/figure_3.png)

## Why It Matters

This research turns pareidolia into a **controlled probe of visual object recognition**. When a human sees a face in random texture, we get a rare window into the visual system — what face templates it carries, how sensitive they are, what triggers them. Building machines that replicate this behavior lets us ask whether they're doing the same thing for the same reasons, or solving the same test with entirely different internal machinery.

The animal face finding is particularly significant for AI development. It suggests that general-purpose visual systems need to be trained on the full diversity of natural scenes — not just human faces. Human-only datasets, however large, produce systematically narrow perceptual systems. For real-world face detection, this matters across surveillance in complex environments, accessibility tools, and social robotics.

Open questions remain rich. Can pareidolia be used as a deliberate test of **perceptual generalization** — the ability to recognize objects across varied conditions? Could the Goldilocks model guide synthetic training data generation? What happens when large vision-language models, trained on internet-scale data saturated with pareidolic content, face this benchmark?

> **Bottom Line:** "Faces in Things" gives the computer vision community its first serious tool for studying pareidolia at scale, and the results reveal a fundamental gap in how machines learn to see — one that points back to millions of years of evolutionary pressure on the animal recognition systems we carry in our skulls.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges cognitive neuroscience, evolutionary biology, and computer vision, using a rigorously curated perceptual dataset to test computational models against human psychophysics — exactly the cross-disciplinary synthesis that defines modern AI and science research.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The "Faces in Things" dataset and pareidolic face detector establish a new evaluation benchmark for visual generalization, demonstrating that diversity of training categories — not just scale — is critical to robust perceptual systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The Goldilocks statistical model provides a principled mathematical account of when structured randomness triggers face perception, connecting information-theoretic ideas to a concrete observable phenomenon in visual cognition.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could use this benchmark to probe large vision-language models and guide synthetic data generation; the dataset and models are publicly available at https://aka.ms/faces-in-things.</span></div></div>
</div>
