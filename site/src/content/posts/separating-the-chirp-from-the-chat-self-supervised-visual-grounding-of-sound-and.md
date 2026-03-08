---
abstract: 'We present DenseAV, a novel dual encoder grounding architecture that learns
  high-resolution, semantically meaningful, and audio-visually aligned features solely
  through watching videos. We show that DenseAV can discover the ``meaning'''' of
  words and the ``location'''' of sounds without explicit localization supervision.
  Furthermore, it automatically discovers and distinguishes between these two types
  of associations without supervision. We show that DenseAV''s localization abilities
  arise from a new multi-head feature aggregation operator that directly compares
  dense image and audio representations for contrastive learning. In contrast, many
  other systems that learn ``global'''' audio and video representations cannot localize
  words and sound. Finally, we contribute two new datasets to improve the evaluation
  of AV representations through speech and sound prompted semantic segmentation. On
  these and other datasets we show DenseAV dramatically outperforms the prior art
  on speech and sound prompted semantic segmentation. DenseAV outperforms the previous
  state-of-the-art, ImageBind, on cross-modal retrieval using fewer than half of the
  parameters. Project Page: \href{https://aka.ms/denseav}{https://aka.ms/denseav}'
arxivId: '2406.05629'
arxivUrl: https://arxiv.org/abs/2406.05629
authors:
- Mark Hamilton
- Andrew Zisserman
- John R. Hershey
- William T. Freeman
concepts:
- audio-visual grounding
- self-supervised learning
- contrastive learning
- dense cross-modal alignment
- representation learning
- disentangled representations
- attention mechanisms
- feature extraction
- multimodal segmentation
- embeddings
- interpretability
figures:
- /iaifi-research-blog/figures/2406_05629/figure_1.png
- /iaifi-research-blog/figures/2406_05629/figure_2.png
- /iaifi-research-blog/figures/2406_05629/figure_3.png
pdfUrl: https://arxiv.org/pdf/2406.05629v1
published: '2024-06-09T03:38:21+00:00'
theme: Foundational AI
title: 'Separating the "Chirp" from the "Chat": Self-supervised Visual Grounding of
  Sound and Language'
wordCount: 1223
---

## The Big Picture

Imagine a baby learning to make sense of the world. Long before anyone explains what a dog is, the infant has already made the connection: a furry creature appears, a bark rings out, and somewhere in that developing brain, a link forms. Later, when someone says "dog," that same brain region lights up. The infant has learned, without instruction, to separate two very different kinds of knowledge: what something *sounds like* and what a word *means*.

This seemingly simple trick has eluded AI systems for years. Teaching an AI to link audio to video is one thing. Teaching it to understand that a bark is a physical event while the word "dog" is a symbolic reference, without ever being told the difference, is something else entirely.

Most modern audio-visual AI systems lump these two together, producing one-size-fits-all representations that can answer "did a dog appear in this video?" but can't tell you *where* the dog is or *which part* of the audio referred to it.

Researchers from MIT, Oxford, Google, and Microsoft built **DenseAV**, a system that watches unlabeled videos and learns to locate sounds and match spoken words to objects in images. It spontaneously separates these two types of connection without ever being told to.

> **Key Insight:** DenseAV discovers, entirely on its own, that spoken words and physical sounds represent different kinds of connections to the visual world, and it separates them into distinct processing channels using only the signal of paired video frames and audio.

## How It Works

The architecture starts with two separate neural networks (one for audio, one for images) that process their respective signals into grids of features. Each **feature** is a compact numerical summary of what's happening in a small patch of an image or a brief slice of audio. Rather than collapsing these grids into a single number, as most systems do, DenseAV keeps them dense, preserving fine-grained spatial and temporal detail.

Every image patch has its own feature summary. Every audio slice has its own. The system then computes a **similarity volume**: a structured table of match scores between every audio moment and every image patch.

Think of it as a correlation map. If the word "dog" is spoken at time *t*, and the dog occupies pixels in the upper-left corner, the match score between that audio moment and those image patches should be high. DenseAV is trained to make it so. No bounding boxes. No transcripts. Just the raw signal of co-occurrence.

![Figure 1](/iaifi-research-blog/figures/2406_05629/figure_1.png)

The researchers then introduce a **multi-head feature aggregation operator**, a way of dividing processing into separate specialized channels, each independently learning what patterns to match:

1. Dense feature maps are split into *K* separate "heads" (the paper explores K=1 and K=2).
2. Each head independently computes its own AV similarity volume.
3. Spatial dimensions are **max-pooled**, not average-pooled, forcing the system to identify the *best-matching* region rather than spreading credit across the whole image.
4. Head dimensions are also max-pooled, allowing different heads to specialize.
5. The audio time dimension is average-pooled to produce a final similarity score for training.

The max-pooling choice is subtle but it makes all the difference. Average pooling rewards a system for being vaguely right everywhere. Max pooling rewards it for being precisely right somewhere. That pressure is what drives DenseAV's localization ability.

![Figure 3](/iaifi-research-blog/figures/2406_05629/figure_3.png)

When trained on video datasets containing both narrated speech and ambient sound, something unexpected happened with the two-head model: one head spontaneously specialized in physical sounds (the bark of a dog), while the other specialized in spoken language (the word "dog"). No label ever told the system these were different. The distinction arose purely from what the training signal demanded; the only way to reduce errors was to treat these two kinds of audio differently.

## Why It Matters

The gap DenseAV exposes in existing models is significant. ImageBind, Meta's widely-used multimodal model, achieves impressive **cross-modal retrieval scores** (a measure of how well a system matches content across different media, like finding the right image for an audio clip). But when you visualize its local features, as shown in the paper's qualitative comparisons, the alignment to image regions is diffuse at best.

![Figure 2](/iaifi-research-blog/figures/2406_05629/figure_2.png)

DenseAV outperforms ImageBind on cross-modal retrieval using fewer than half the parameters. It also outperforms all prior work on new segmentation benchmarks the researchers contributed, tasks where you prompt the system with a spoken word or a sound and ask it to highlight the corresponding region of an image.

This matters beyond benchmarks. Applications from robotics to hearing aids to low-resource language documentation all require knowing not just *that* a connection exists between sound and image, but *where* and *why*.

That a machine learning system can discover, on its own, the distinction between "what something sounds like" and "what a word means" has deeper implications. It raises questions about what patterns in training data are doing the work, and whether the same pressures might explain how human infants develop the ability to connect their senses in the first place.

> **Bottom Line:** DenseAV learns to localize spoken words and environmental sounds in images, and separates them into distinct representations, using nothing but unlabeled video. It outperforms systems with twice as many parameters and points toward a richer, grounded understanding of audio-visual AI.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">DenseAV directly mirrors a core puzzle in developmental neuroscience: how infants separate semantic language grounding from acoustic event localization. It provides a computational model that achieves the same feat from raw sensory data alone.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The multi-head dense similarity aggregation operator shows that contrastive objectives over *local* features, with max-pooling over spatial and head dimensions, unlock localization and disentanglement capabilities unavailable to global-representation architectures.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By learning how physical sound events differ structurally from symbolic language references, DenseAV probes the representational geometry underlying cross-modal perception, a question relevant to how information is encoded across interacting physical systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending DenseAV to more heads for finer-grained audio category discovery and applying dense AV representations to low-resource language documentation; the work is available at https://aka.ms/denseav.

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Separating the "Chirp" from the "Chat": Self-supervised Visual Grounding of Sound and Language</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">[arXiv:2406.05629](https://arxiv.org/abs/2406.05629)</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Mark Hamilton", "Andrew Zisserman", "John R. Hershey", "William T. Freeman"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We present DenseAV, a novel dual encoder grounding architecture that learns high-resolution, semantically meaningful, and audio-visually aligned features solely through watching videos. We show that DenseAV can discover the ``meaning'' of words and the ``location'' of sounds without explicit localization supervision. Furthermore, it automatically discovers and distinguishes between these two types of associations without supervision. We show that DenseAV's localization abilities arise from a new multi-head feature aggregation operator that directly compares dense image and audio representations for contrastive learning. In contrast, many other systems that learn ``global'' audio and video representations cannot localize words and sound. Finally, we contribute two new datasets to improve the evaluation of AV representations through speech and sound prompted semantic segmentation. On these and other datasets we show DenseAV dramatically outperforms the prior art on speech and sound prompted semantic segmentation. DenseAV outperforms the previous state-of-the-art, ImageBind, on cross-modal retrieval using fewer than half of the parameters. Project Page: \href{https://aka.ms/denseav}{https://aka.ms/denseav}</span></div></div>
</div>
