---
abstract: We introduce Nuclear Co-Learned Representations (NuCLR), a deep learning
  model that predicts various nuclear observables, including binding and decay energies,
  and nuclear charge radii. The model is trained using a multi-task approach with
  shared representations and obtains state-of-the-art performance, achieving levels
  of precision that are crucial for understanding fundamental phenomena in nuclear
  (astro)physics. We also report an intriguing finding that the learned representation
  of NuCLR exhibits the prominent emergence of crucial aspects of the nuclear shell
  model, namely the shell structure, including the well-known magic numbers, and the
  Pauli Exclusion Principle. This suggests that the model is capable of capturing
  the underlying physical principles and that our approach has the potential to offer
  valuable insights into nuclear theory.
arxivId: '2306.06099'
arxivUrl: https://arxiv.org/abs/2306.06099
authors:
- Ouail Kitouni
- Niklas Nolte
- Sokratis Trifinopoulos
- Subhash Kantamneni
- Mike Williams
concepts:
- representation learning
- nuclear shell emergence
- multi-task learning
- embeddings
- interpretability
- nuclear observables
- dimensionality reduction
- regression
- surrogate modeling
- disentangled representations
- transfer learning
figures:
- /iaifi-research-blog/figures/2306_06099/figure_1.png
- /iaifi-research-blog/figures/2306_06099/figure_2.png
- /iaifi-research-blog/figures/2306_06099/figure_3.png
pdfUrl: https://arxiv.org/pdf/2306.06099v2
published: '2023-06-09T17:59:16+00:00'
theme: Experimental Physics
title: 'NuCLR: Nuclear Co-Learned Representations'
wordCount: 1089
---

## The Big Picture

Imagine learning a language by reading millions of sentences without ever being taught grammar. You'd never see the explicit rules — but you'd start noticing patterns. Words that go together. Structures that repeat. Rules emerging naturally from the data itself.

That's essentially what a team of physicists at MIT's IAIFI just did with atomic nuclei.

The atomic nucleus is one of physics' oldest unsolved puzzles. We've known about it for over a century, and we have a fundamental theory — **quantum chromodynamics (QCD)** — that should describe everything about it. But "in principle" does heavy lifting here. In practice, QCD calculations become hopelessly slow, even for supercomputers, once you go beyond a handful of protons and neutrons.

For the hundreds of **isotopes** — different forms of elements defined by their neutron count — that matter for astrophysics, nuclear medicine, and fundamental physics, we're still relying on simplified models patched together with experimental measurements.

The team behind **NuCLR** (Nuclear Co-Learned Representations) set out to change that — not just by building a better predictive model, but by asking a deeper question: can a neural network actually *learn* the underlying physics of the nucleus, rather than just memorize data?

> **Key Insight:** NuCLR doesn't just predict nuclear properties with record-breaking accuracy — it spontaneously rediscovers the nuclear shell model, including magic numbers and the Pauli Exclusion Principle, entirely from data.

## How It Works

The core idea is elegantly simple: rather than train a separate model for each nuclear property, train one model to predict *all* of them simultaneously using shared internal representations.

This is **multi-task learning (MTL)** — a technique from machine learning where a model trained on related tasks simultaneously generalizes better than one trained on each task alone. If your model learns to predict binding energies *and* charge radii *and* decay energies all at once, it must build a representation of the nucleus that captures what all those properties share. That shared representation becomes richer and more physical than any single-task model could achieve.

Here's how NuCLR is structured:

1. **Tokenized inputs.** The model takes two numbers as input: proton count *Z* and neutron count *N*. Rather than feeding these as raw integers, NuCLR *embeds* them — treating each like a word token in a language model, mapping it into a high-dimensional vector space where similar numbers can cluster together. These embedding vectors are learned, not hand-crafted.
2. **Shared backbone.** The proton and neutron embeddings are concatenated and passed through a stack of **residual blocks** — layers that pass information forward while also providing shorter "skip" connections, a technique that helps deep networks train reliably.
3. **Task-specific heads.** Separate output layers branch off from the shared representation to predict each nuclear observable: binding energy, separation energies, charge radius, and more.

![Figure 2](/iaifi-research-blog/figures/2306_06099/figure_2.png)

NuCLR achieves state-of-the-art precision on binding energies — approaching the sub-100 keV threshold that nuclear astrophysicists need to model the *r*-process, the rapid neutron capture process responsible for forging heavy elements in neutron star mergers. For context: the best physics-based analytic formula, WS4, achieves roughly 300 keV precision. NuCLR beats it — without using WS4's predictions as a crutch, unlike some previous ML approaches.

But the benchmark numbers aren't the real story.

After training, the researchers applied **principal component analysis (PCA)** — a standard technique for finding the most important axes of variation in high-dimensional data — to the learned neutron embeddings.

![Figure 1](/iaifi-research-blog/figures/2306_06099/figure_1.png)

What they found was extraordinary. Even early in training, the first two principal components already encode two of the most fundamental features of nuclear physics:

- **Shell structure and magic numbers.** The numbers 2, 8, 20, 28, 50, and 82 — the "magic numbers" where nuclear shells fill up and nuclei become especially stable — appear as prominent discontinuities in the representation space. No one told the model about magic numbers. It found them.
- **The Pauli Exclusion Principle.** Quantum mechanics forbids two identical particles from occupying the same quantum state. Since protons and neutrons each come in two spin orientations, each energy level holds exactly two, making even counts energetically preferred. NuCLR's representations show even and odd neutron numbers splitting into two distinct geometric tracks — a direct reflection of this quantum rule.

By late in training, the structure evolves further: the representations form **three-dimensional spirals**, with magic numbers appearing at local maxima and each nuclear shell corresponding to one revolution around an approximately conic surface.

![Figure 3](/iaifi-research-blog/figures/2306_06099/figure_3.png)

The researchers describe interpreting this spiral structure as ongoing work — perhaps the most tantalizing sentence in the paper.

## Why It Matters

NuCLR sits at the intersection of two big questions in modern science.

The first is practical: can we build nuclear models precise enough to support next-generation experiments in astrophysics, rare isotope physics, and nuclear medicine? The sub-100 keV binding energy precision NuCLR approaches is a genuine target for the field, and multi-task deep learning offers a credible path to get there.

The second is more philosophical — and potentially more profound. For decades, physicists have worried that machine learning models are black boxes: they predict, but they don't explain. NuCLR pushes back on that narrative.

The fact that the nuclear shell model emerges *spontaneously* from the learned representations — without any physics hard-coded into the architecture — suggests that sufficiently expressive models, trained on sufficiently rich data, may genuinely internalize physical principles rather than merely approximate them. If that's true, these models become tools for *discovery*, not just prediction. The unexplained spiral structure in NuCLR's late-stage representations may be pointing at something new.

> **Bottom Line:** NuCLR achieves state-of-the-art nuclear predictions using multi-task learning — and in doing so, spontaneously rediscovers century-old physics, raising the tantalizing possibility that deep learning models can genuinely learn the laws of nature from data alone.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">NuCLR demonstrates that multi-task deep learning can simultaneously advance nuclear physics predictions and reveal emergent physical structure, exemplifying IAIFI's mission to fuse AI and fundamental science.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The work provides a compelling case study for interpretable multi-task representation learning, showing that shared latent representations can encode known scientific laws without explicit supervision.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">NuCLR achieves state-of-the-art precision on nuclear binding energies and charge radii, approaching the thresholds needed to model *r*-process nucleosynthesis and other fundamental nuclear astrophysics phenomena.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work aims to interpret the emergent spiral structure in NuCLR's representations and extend the model to unstable and exotic nuclei; the paper is available at arXiv:2306.06099.</span></div></div>
</div>
