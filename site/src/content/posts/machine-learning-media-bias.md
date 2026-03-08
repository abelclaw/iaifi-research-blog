---
abstract: We present an automated method for measuring media bias. Inferring which
  newspaper published a given article, based only on the frequencies with which it
  uses different phrases, leads to a conditional probability distribution whose analysis
  lets us automatically map newspapers and phrases into a bias space. By analyzing
  roughly a million articles from roughly a hundred newspapers for bias in dozens
  of news topics, our method maps newspapers into a two-dimensional bias landscape
  that agrees well with previous bias classifications based on human judgement. One
  dimension can be interpreted as traditional left-right bias, the other as establishment
  bias. This means that although news bias is inherently political, its measurement
  need not be.
arxivId: '2109.00024'
arxivUrl: https://arxiv.org/abs/2109.00024
authors:
- Samantha D'Alonzo
- Max Tegmark
concepts:
- dimensionality reduction
- spectral methods
- phrase bias
- representation learning
- media bias landscape
- embeddings
- classification
- likelihood estimation
- feature extraction
- interpretability
- sparse models
- scalability
figures:
- /iaifi-research-blog/figures/2109_00024/figure_1.png
- /iaifi-research-blog/figures/2109_00024/figure_1.png
- /iaifi-research-blog/figures/2109_00024/figure_2.png
- /iaifi-research-blog/figures/2109_00024/figure_2.png
- /iaifi-research-blog/figures/2109_00024/figure_3.png
- /iaifi-research-blog/figures/2109_00024/figure_3.png
pdfUrl: https://arxiv.org/pdf/2109.00024v1
published: '2021-08-31T18:06:32+00:00'
theme: Foundational AI
title: Machine-Learning media bias
wordCount: 869
---

## The Big Picture

Imagine you're handed a random newspaper clipping with no masthead, no byline, no date. Could you tell just from the words whether it came from Fox News or MSNBC? From a scrappy independent outlet or an establishment broadsheet? Most people could take a reasonable guess, and it turns out a machine can too, with surprising accuracy.

Political polarization is accelerating across the United States and internationally, and a growing body of research points to media as a key driver. Yet measuring media bias objectively has long been a thorny problem: any person or organization tasked with judging bias is themselves subject to accusations of the same. Fact-checkers get called partisan. Bias-raters get dismissed.

Researchers Samantha D'Alonzo and Max Tegmark at MIT's Department of Physics and IAIFI offer a simple idea: let the language itself reveal the bias. They use machine learning (software that learns patterns in data without explicit programming) to discover structure that no human pre-labeled.

> **Key Insight:** By training a model to predict which newspaper published an article based purely on phrase frequencies, the researchers automatically uncovered a two-dimensional bias map, capturing both left-right and establishment dimensions, that matches human expert classifications without ever asking for human opinion.

## How It Works

The core method is elegant. Take roughly a million articles from about a hundred newspapers. For each article, don't analyze topic, sentiment, or meaning in any deep sense. Just count phrases.

Consider how newspapers diverge on politically charged word choices:

- "Undocumented immigrant" vs. "illegal immigrant"
- "Demonstrators" vs. "rioters"
- "Estate tax" vs. "death tax"

These **phrase frequency signatures**, numerical fingerprints of which words appear and how often, become the raw material the algorithm learns from.

The team frames the problem as a classification task: given an article's phrase counts, predict which of the ~100 newspapers published it. But they don't actually care about getting the classification right. What matters is the **conditional probability distribution**, the underlying statistical patterns the model builds to distinguish one newspaper from another. Those learned patterns are themselves the signal about bias.

![Figure 1](/iaifi-research-blog/figures/2109_00024/figure_1.png)

Technically, the method centers on a **generalized Singular Value Decomposition (SVD)**, a mathematical technique that compresses thousands of phrase-count columns down to just two or three key dimensions. Standard SVD fails here for two reasons: it can produce nonsensical negative phrase counts, and it treats all observations equally even when some phrase counts are measured far more precisely than others.

D'Alonzo and Tegmark instead maximize a **Poisson likelihood**, a statistically principled choice since word counts are discrete events, exactly what the Poisson distribution was designed to model. The method tests two parameterizations (a ReLU, which floors negative values to zero, and an exponential form) and selects whichever fits the data better.

The algorithm then maps both newspapers and phrases into a low-dimensional **bias space**, a compact coordinate system where publications with similar language habits cluster together. No human tells it what the axes mean; it discovers structure from the data alone. When the researchers examine those axes, one maps cleanly onto the traditional left-right political spectrum. The other captures what they call **establishment bias**: how much a publication aligns with or challenges mainstream institutional narratives, independent of left-right positioning.

## Why It Matters

Here's what's striking: this purely data-driven method recovers the same two-dimensional structure that human experts have identified through years of careful qualitative analysis. Left-right bias and establishment bias emerge not because the researchers encoded those categories, but because those are genuinely the dominant axes along which newspapers differ in their word choices. The machine didn't need to be told about politics. Politics showed up anyway, baked into the language.

This result points toward real-time, scalable, transparent bias monitoring. Because the method is fully automated and relies only on publicly available text, it can be applied to new outlets, new topics, and new time periods without any additional human labeling. The team analyzes dozens of distinct news topics and finds that biases are correlated across them in consistent ways, which is precisely what allows the two-dimensional structure to emerge at all.

![Figure 2](/iaifi-research-blog/figures/2109_00024/figure_1.png)

Natural extensions include other languages, tracking how newspaper bias shifts over time, and applying similar techniques to social media, political speeches, or corporate press releases.

> **Bottom Line:** Machine learning can measure media bias from phrase statistics alone, no human labels required. The resulting bias map matches expert classifications while being far more scalable and transparent than any human-driven alternative.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies physics-inspired mathematical tools (Poisson likelihood maximization and generalized SVD) to a social science problem, bringing quantitative rigor from physics to bear on the study of media institutions.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces a scalable, unsupervised NLP method that discovers interpretable bias dimensions directly from a million-article corpus, with no hand-crafted features or human-labeled training data.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Political polarization structures (left-right and establishment axes) emerge automatically from language statistics, contributing to a quantitative understanding of how information ecosystems shape society.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future extensions could track bias evolution over time or across languages; the paper is available at [arXiv:2109.00024](https://arxiv.org/abs/2109.00024) with open-source tools for reproducible bias measurement.</span></div></div>
</div>
