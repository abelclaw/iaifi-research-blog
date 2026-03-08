---
abstract: We present PAPERCLIP (Proposal Abstracts Provide an Effective Representation
  for Contrastive Language-Image Pre-training), a method which associates astronomical
  observations imaged by telescopes with natural language using a neural network model.
  The model is fine-tuned from a pre-trained Contrastive Language-Image Pre-training
  (CLIP) model using successful observing proposal abstracts and corresponding downstream
  observations, with the abstracts optionally summarized via guided generation using
  large language models (LLMs). Using observations from the Hubble Space Telescope
  (HST) as an example, we show that the fine-tuned model embodies a meaningful joint
  representation between observations and natural language through tests targeting
  image retrieval (i.e., finding the most relevant observations using natural language
  queries) and description retrieval (i.e., querying for astrophysical object classes
  and use cases most relevant to a given observation). Our study demonstrates the
  potential for using generalist foundation models rather than task-specific models
  for interacting with astronomical data by leveraging text as an interface.
arxivId: '2403.08851'
arxivUrl: https://arxiv.org/abs/2403.08851
authors:
- Siddharth Mishra-Sharma
- Yiding Song
- Jesse Thaler
concepts:
- contrastive learning
- fine-tuning
- representation learning
- multi-modal foundation model
- embeddings
- astronomical image retrieval
- transfer learning
- guided llm generation
- feature extraction
- galaxy classification
- self-supervised learning
figures:
- /iaifi-research-blog/figures/2403_08851/figure_1.png
- /iaifi-research-blog/figures/2403_08851/figure_1.png
- /iaifi-research-blog/figures/2403_08851/figure_2.png
- /iaifi-research-blog/figures/2403_08851/figure_2.png
- /iaifi-research-blog/figures/2403_08851/figure_3.png
- /iaifi-research-blog/figures/2403_08851/figure_3.png
pdfUrl: https://arxiv.org/pdf/2403.08851v1
published: '2024-03-13T18:00:00+00:00'
theme: Astrophysics
title: 'PAPERCLIP: Associating Astronomical Observations and Natural Language with
  Multi-Modal Models'
wordCount: 1057
---

## The Big Picture

Imagine walking into the world's largest library and asking for "a photo of a barred spiral galaxy with evidence of active star formation." Now imagine the librarian only speaks a private cataloging language that took decades to develop. That's roughly the situation astronomers face when trying to search through the billions of images captured by space telescopes.

The images exist. The data is there. But searching it with plain human language? Essentially impossible.

The Hubble Space Telescope has spent over three decades accumulating an archive of breathtaking observations — from dying stars to colliding galaxies. Each image comes with an associated observing proposal, a document written by scientists explaining what they want to look at and why. These proposals are dense with scientific language, but they are *language*. And that turns out to be the key.

Researchers at MIT's Institute for AI and Fundamental Interactions (IAIFI) have built PAPERCLIP, a system that teaches a neural network to directly link Hubble images with natural language descriptions — making it possible to search astronomical archives the same way you'd search Google Images.

> **Key Insight:** By fine-tuning a general-purpose AI model on pairs of Hubble observations and their scientific proposal abstracts, PAPERCLIP creates a shared "language" between telescope images and human text — enabling free-form natural language search over astronomical data.

## How It Works

The foundation of PAPERCLIP is **CLIP** (Contrastive Language-Image Pre-training), a model originally developed by OpenAI to understand relationships between photographs and captions. CLIP learns by being shown millions of image-text pairs and trained to match them: it pulls matching pairs closer together in a shared mathematical map — an invisible coordinate system where similar concepts cluster nearby — while pushing non-matching pairs apart. A photo of a dog and the word "dog" end up near each other; a photo of a nebula and the word "dog" end up far apart.

The problem is that CLIP was trained on everyday internet images, not on scientific telescope data. Hubble's observations look nothing like the photographs CLIP learned from. The solution: **fine-tuning**, taking a pre-trained model and giving it additional training on domain-specific data to sharpen its skills for a new area.

![Figure 1](/iaifi-research-blog/figures/2403_08851/figure_1.png)

Here's where the dataset construction gets clever. Every successful Hubble observing proposal comes with an abstract — a concise scientific description of what the researchers want to observe and why. These abstracts are publicly available in the **Mikulski Archive for Space Telescopes (MAST)**, NASA's repository for Hubble data. By pairing each observation with the abstract of the proposal that generated it, the researchers assembled a natural training set: images linked to text, no hand-labeling required.

There's a catch. Proposal abstracts are written for expert audiences and focus on scientific justification rather than simple description. To make them more useful for training, the team used **guided LLM generation** — running the abstracts through a large language model (the technology behind systems like ChatGPT) to produce concise, structured summaries. These extracted key information like target object type, relevant physical properties, and scientific use case, using a fixed template to keep results consistent.

The training pipeline then works as follows:
1. Retrieve matched (observation, abstract) pairs from Hubble's public archive
2. Summarize abstracts using guided LLM generation
3. Fine-tune CLIP on these pairs using **contrastive loss** — rewarding the model when it correctly matches images to their corresponding texts

## Results: Asking Hubble in Plain English

The team tested PAPERCLIP on two retrieval tasks. In **image retrieval**, they queried the model with a text description and asked it to find the most relevant Hubble observations from a large candidate pool. In **text retrieval**, they fed it an image and asked it to identify which astrophysical category — "spiral galaxy," "planetary nebula," "globular cluster" — best describes it.

![Figure 2](/iaifi-research-blog/figures/2403_08851/figure_1.png)

PAPERCLIP substantially outperforms the base CLIP model on both tasks, confirming that domain-specific fine-tuning transfers real scientific knowledge into the model's understanding of astronomical imagery. The version trained on LLM-summarized abstracts consistently outperformed the version trained on raw abstracts, validating the guided summarization approach.

In practice, the results are striking. When asked to search for "barred spiral galaxy," PAPERCLIP retrieves images that are recognizably barred spirals. When shown an image of a planetary nebula, it correctly identifies the object class and associated scientific context. The model has learned something genuinely meaningful about astronomical imagery — not just surface-level pattern matching.

![Figure 3](/iaifi-research-blog/figures/2403_08851/figure_2.png)

## Why It Matters

The implications stretch well beyond Hubble. Astronomy is entering an era of data abundance: the Vera Rubin Observatory will soon generate 20 terabytes of images every night. The Square Kilometre Array will produce data volumes that dwarf anything that exists today. Navigating these archives with hand-crafted, task-specific tools simply won't scale.

PAPERCLIP demonstrates a different path: take a generalist foundation model and adapt it with a relatively small amount of domain-specific data. The training signal — proposal abstracts — was always there, hiding in the archive. The insight was recognizing that this existing text could serve as a powerful bridge between human language and scientific imagery.

Future extensions could apply the same approach to other telescopes, other wavelengths (radio, X-ray, infrared), and other data types like light curves or spectra — building toward a truly universal interface for astronomical data.

> **Bottom Line:** PAPERCLIP shows that fine-tuning a general-purpose vision-language model on astronomy's own existing documentation creates a powerful search tool — and points toward a future where scientists interact with telescope archives using nothing more than natural language.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">PAPERCLIP directly merges foundation model AI and observational astrophysics by repurposing observing proposal abstracts as a training signal to bridge telescope images and human language — a creative use of existing scientific infrastructure.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work demonstrates that guided LLM summarization can meaningfully improve contrastive fine-tuning, offering a generalizable technique for adapting vision-language models to specialized scientific domains with limited labeled data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By creating a natural-language interface to Hubble's archive of over a million observations, PAPERCLIP makes decades of astronomical data more accessible and discoverable, potentially accelerating research across astrophysics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend PAPERCLIP to multi-wavelength surveys, spectral data, and other telescope archives; the paper is available on arXiv and the code is open-source at github.com/smsharma/PAPERCLIP-Hubble.</span></div></div>
</div>
