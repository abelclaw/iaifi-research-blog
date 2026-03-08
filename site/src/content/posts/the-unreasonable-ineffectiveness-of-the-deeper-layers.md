---
abstract: 'How is knowledge stored in an LLM''s weights? We study this via layer pruning:
  if removing a certain layer does not affect model performance in common question-answering
  benchmarks, then the weights in that layer are not necessary for storing the knowledge
  needed to answer those questions. To find these unnecessary parameters, we identify
  the optimal block of layers to prune by considering similarity across layers; then,
  to "heal" the damage, we perform a small amount of finetuning. Surprisingly, with
  this method we find minimal degradation of performance until after a large fraction
  (up to half) of the layers are removed for some common open-weight models. From
  a scientific perspective, the robustness of these LLMs to the deletion of layers
  implies either that current pretraining methods are not properly leveraging the
  parameters in the deeper layers of the network or that the shallow layers play a
  critical role in storing knowledge. For our study, we use parameter-efficient finetuning
  (PEFT) methods, specifically quantization and Low Rank Adapters (QLoRA), such that
  each of our experiments can be performed on a single 40GB A100 GPU.'
arxivId: '2403.17887'
arxivUrl: https://arxiv.org/abs/2403.17887
authors:
- Andrey Gromov
- Kushal Tirumala
- Hassan Shapourian
- Paolo Glorioso
- Daniel A. Roberts
concepts:
- layer pruning
- fine-tuning
- transformers
- knowledge localization
- representation learning
- parameter efficiency
- interpretability
- sparse models
- scalability
- transfer learning
figures:
- /iaifi-research-blog/figures/2403_17887/figure_1.png
- /iaifi-research-blog/figures/2403_17887/figure_1.png
- /iaifi-research-blog/figures/2403_17887/figure_2.png
- /iaifi-research-blog/figures/2403_17887/figure_2.png
- /iaifi-research-blog/figures/2403_17887/figure_3.png
- /iaifi-research-blog/figures/2403_17887/figure_3.png
pdfUrl: https://arxiv.org/pdf/2403.17887v2
published: '2024-03-26T17:20:04+00:00'
theme: Foundational AI
title: The Unreasonable Ineffectiveness of the Deeper Layers
wordCount: 1098
---

## The Big Picture

Imagine building a 70-story skyscraper, only to discover that you could quietly demolish floors 30 through 65 — and the building still stands. Not just stands: it passes every safety inspection you throw at it. That's roughly the situation researchers from Meta FAIR, MIT, and collaborators stumbled upon when they started slicing through large language models layer by layer.

Large language models like Llama and Mistral are stacked structures: dozens of nearly identical processing layers, each digesting text a little further before passing it along. The conventional wisdom is that depth is what makes these models powerful — more layers means more complex reasoning, a richer internal model of language, deeper "understanding." But what if most of those layers aren't actually doing much?

That's exactly what this paper, published at ICLR 2025, investigates. By surgically removing consecutive groups of layers and applying a brief retraining step, the researchers showed that many of the deeper layers in today's best publicly available AI models are surprisingly expendable — a finding that raises uncomfortable questions about how we train AI systems.

> **Key Insight:** You can strip away up to half the layers of a 70-billion-parameter model like Llama-2-70B while preserving most of its question-answering performance — suggesting that current training methods may be squandering enormous computational resources on redundant depth.

## How It Works

The pruning strategy is elegant in its simplicity. Rather than removing random layers or naively cutting from the end, the team developed a principled method to find which layers are most redundant.

![Figure 1](/iaifi-research-blog/figures/2403_17887/figure_1.png)

The core idea exploits the **residual stream** structure of transformers — the way each layer adds its output to a running "stream" of information rather than fully transforming it. If a layer's contribution is small — if the data coming out looks almost identical to the data going in — then removing that layer should cause minimal disruption.

To measure this, the researchers compute the **angular distance** between the input and output of each layer: essentially, how different the two snapshots of information are, expressed as an angle in mathematical space. Think of it like comparing two arrows: if they point in nearly the same direction, the layer barely changed anything. The process:

1. **Measure similarity:** For a candidate block of *n* consecutive layers, compute the angular distance between the representation entering the block and the representation leaving it.
2. **Find the minimum:** Sweep across all possible starting positions and pick the block where this angular distance is smallest — these are the layers doing the least work.
3. **Remove the block:** Physically delete those layers from the model.
4. **Heal the damage:** Fine-tune the pruned model using **QLoRA** (Quantized Low-Rank Adapters), a lightweight retraining method that adjusts only a small fraction of the model's weights to compensate for the missing layers.

The entire healing step runs on a single 40GB A100 GPU — not exotic hardware. It's the kind of setup a well-funded research lab or advanced graduate student might have access to.

What the angular distance maps reveal is telling: deeper layers consistently show smaller distances to their neighbors than shallower ones. The **representations** — the internal numerical encodings of text — are barely changing as information flows through the final third of the network. This pattern led to an even simpler heuristic: just start removing layers from the deepest end. It works almost as well as the more sophisticated similarity search.

![Figure 2](/iaifi-research-blog/figures/2403_17887/figure_1.png)

For Llama-2-70B, the flagship result, performance on standard question-answering benchmarks like MMLU and BoolQ stays remarkably flat as layers are removed — until roughly the 40–50% pruning mark, where it falls off a cliff. The loss on the C4 language modeling benchmark degrades more gracefully, staying near baseline even at 80% pruning after healing. These are plateaus followed by sudden collapses, not gradual declines — a signature of genuine redundancy, not mere graceful degradation.

## Why It Matters

The title borrows from physicist Eugene Wigner's famous essay on "the unreasonable effectiveness of mathematics" — here flipped on its head. The deeper layers are unreasonably *ineffective*. That should bother anyone who cares about how we build AI systems.

There are two ways to read this result. The optimistic interpretation: these models have more capacity than current training methods know how to fill. The deeper layers are undertrained, not inherently useless — a signal that better training recipes, longer runs, or different architectures could unlock substantial gains without adding a single parameter.

The more sobering interpretation: shallow layers do most of the heavy lifting when it comes to storing factual knowledge, and depth beyond a certain point provides diminishing returns regardless of training. Either way, the trillion-parameter scaling race may need to reckon with this finding.

Practically, the implications are immediate. Compressed models that retain most of a full model's capability but run in half the memory open doors for deployment on commodity hardware, faster inference, and dramatically reduced costs. The single-GPU fine-tuning requirement makes this accessible to the broader research community, not just labs with massive clusters.

Open questions remain sharp: Does this apply to reasoning-focused models trained with reinforcement learning? Are there tasks — complex multi-step math, long-form reasoning — where the deeper layers actually matter? And most intriguingly: can training procedures be redesigned from the start to use depth more efficiently?

> **Bottom Line:** Half the layers of a 70B model can be removed with minimal performance loss — a discovery that challenges our assumptions about depth in neural networks and offers a practical path to dramatically cheaper AI inference.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies physicist-style probing — testing a system by removing parts and measuring what breaks — to study the internal structure of language models, treating the question of where knowledge lives in a neural network as an empirical science problem.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces a practical, single-GPU method for compressing large language models by up to 50% with minimal benchmark degradation, directly advancing efficient AI deployment and challenging assumptions about the necessity of deep architectures.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By framing layer pruning through residual stream dynamics and angular similarity, the work provides a new empirical handle on the representational geometry of neural networks — a question with deep connections to theoretical physics approaches to understanding learning systems.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work should probe whether reasoning-intensive models exhibit the same redundancy and whether training objectives can be redesigned to use depth more effectively; the paper is available as arXiv:2403.17887 and was published at ICLR 2025.</span></div></div>
</div>
