---
abstract: Fault-tolerant quantum computers will depend crucially on the performance
  of the classical decoding algorithm which takes in the results of measurements and
  outputs corrections to the errors inferred to have occurred. Machine learning models
  have shown great promise as decoders for the surface code; however, this promise
  has not yet been substantiated for the more challenging task of decoding quantum
  low-density parity-check (QLDPC) codes. In this paper, we present a recurrent, transformer-based
  neural network designed to decode circuit-level noise on Bivariate Bicycle (BB)
  codes, introduced recently by Bravyi et al (Nature 627, 778-782, 2024). For the
  $[[72,12,6]]$ BB code, at a physical error rate of $p=0.1\%$, our model achieves
  a logical error rate almost $5$ times lower than belief propagation with ordered
  statistics decoding (BP-OSD). Moreover, while BP-OSD has a wide distribution of
  runtimes with significant outliers, our model has a consistent runtime and is an
  order-of-magnitude faster than the worst-case times from a benchmark BP-OSD implementation.
  On the $[[144,12,12]]$ BB code, our model obtains worse logical error rates but
  maintains the speed advantage. These results demonstrate that machine learning decoders
  can out-perform conventional decoders on QLDPC codes, in regimes of current interest.
arxivId: '2504.13043'
arxivUrl: https://arxiv.org/abs/2504.13043
authors:
- John Blue
- Harshil Avlani
- Zhiyang He
- Liu Ziyin
- Isaac L. Chuang
concepts:
- quantum computing
- transformers
- qldpc decoding
- attention mechanisms
- recurrent networks
- syndrome-based decoding
- likelihood estimation
- scalability
- classification
- quantum states
- transfer learning
figures:
- /iaifi-research-blog/figures/2504_13043/figure_1.png
- /iaifi-research-blog/figures/2504_13043/figure_1.png
- /iaifi-research-blog/figures/2504_13043/figure_2.png
- /iaifi-research-blog/figures/2504_13043/figure_2.png
- /iaifi-research-blog/figures/2504_13043/figure_3.png
- /iaifi-research-blog/figures/2504_13043/figure_3.png
pdfUrl: https://arxiv.org/pdf/2504.13043v1
published: '2025-04-17T15:57:16+00:00'
theme: Theoretical Physics
title: Machine Learning Decoding of Circuit-Level Noise for Bivariate Bicycle Codes
wordCount: 1149
---

## The Big Picture

Imagine whispering a secret message across a crowded, noisy room. Every few feet, someone mishears a word and passes along a garbled version. To solve this, you repeat the message in a clever pattern so that even if words get mangled, the original can be reconstructed. Quantum computers face exactly this problem. The "noise" is quantum mechanical, the "words" are **qubits** (the quantum equivalent of binary bits, but far more fragile), and the stakes are whether quantum computers can ever reliably run complex calculations.

The part that doesn't get enough attention is the **classical decoder**, a conventional software algorithm running in real-time alongside the quantum processor. It watches measurement outcomes and infers which errors occurred. Without a fast, accurate decoder, error corrections pile up faster than they can be processed and the whole system grinds to a halt.

Researchers have spent years building good machine learning decoders for the most popular quantum error-correcting scheme, the **surface code**, which arranges qubits in a grid and detects errors using neighboring qubits. But a newer, more promising class called **quantum low-density parity-check (QLDPC) codes**, which protect far more logical qubits with the same hardware, has largely resisted machine learning breakthroughs. That just changed.

A team at MIT has trained a recurrent, transformer-based neural network to decode circuit-level noise on **Bivariate Bicycle (BB) codes**, a family of QLDPC codes that recently made headlines in *Nature*. Their model doesn't just match the best conventional decoder. It beats it, while running ten times faster in the worst case.

> **Key Insight:** A machine learning decoder can outperform the leading classical algorithm for QLDPC codes in both accuracy and speed, opening a credible path to real-time decoding for next-generation quantum computers.

## How It Works

After each round of **syndrome extraction** (measuring special operators on groups of qubits to detect errors without directly reading the qubits themselves), the decoder receives a string of 0s and 1s called a **syndrome**. Think of it as a fault report: it tells you *that* something went wrong, but not exactly *what*. The decoder must infer which combination of physical errors most likely produced that syndrome, then output a correction. Get it wrong and you corrupt the logical qubit. Do it too slowly and the error backlog grows exponentially.

![Figure 1](/iaifi-research-blog/figures/2504_13043/figure_1.png)

The state-of-the-art classical decoder for QLDPC codes is **BP-OSD** (Belief Propagation with Ordered Statistics Decoding), a sophisticated algorithm that propagates probability estimates across the code's structure to identify the most likely errors. BP-OSD is powerful but has a fatal flaw: its runtime is wildly variable. Some syndromes decode in microseconds; others trigger worst-case cubic-time computations. For a quantum computer that needs corrections every clock cycle, unpredictable latency is a dealbreaker.

The MIT team's approach combines three ideas:

- **Code-aware self-attention:** Standard transformers let every token attend to every other. Here, attention is restricted based on the BB code's **stabilizer generators**, the measurement patterns that define how errors are detected. This idea comes from classical coding theory and has been extended to quantum codes for the first time. It dramatically shrinks the space the model has to navigate, which speeds up training and improves accuracy.

- **Recurrent processing:** Rather than ingesting all syndrome measurement rounds at once, the architecture processes one round at a time and carries a hidden state forward. This keeps the effective input size manageable as syndrome rounds accumulate.

- **Autoregressive output:** Instead of predicting a single correction from an exponentially large set of possibilities, the model outputs a **conditional probability distribution** over logical errors, predicting each error type sequentially based on prior predictions. This approximates a **maximum-likelihood decoder** without requiring exponentially many output classes.

![Figure 2](/iaifi-research-blog/figures/2504_13043/figure_1.png)

The decoder was trained and tested on two BB codes: the [[72,12,6]] code (72 physical qubits encoding 12 logical qubits with distance 6) and the larger [[144,12,12]] code. Training used **circuit-level noise**, the most realistic and challenging noise model. It includes faulty measurements, gate errors, and error propagation between qubits during syndrome extraction.

![Figure 4](/iaifi-research-blog/figures/2504_13043/figure_2.png)

At a physical error rate of $p = 0.1\%$ on the [[72,12,6]] code, the ML decoder achieved a logical error rate nearly **5 times lower** than BP-OSD. The speed story is just as important. BP-OSD's runtime has heavy tails, with occasional slow cases that could bottleneck a real quantum processor. The ML decoder runs in consistent, predictable time and is **an order of magnitude faster** than BP-OSD's worst-case runtimes.

## Why It Matters

QLDPC codes represent the most promising route to resource-efficient fault-tolerant quantum computing. The surface code requires roughly one physical qubit of overhead per protected logical qubit. QLDPC codes like BB codes encode many more logical qubits per physical qubit, potentially slashing hardware requirements by orders of magnitude.

IBM's recent experimental demonstration of BB codes in *Nature* brought them from theory to hardware. The missing piece has been a decoder fast and accurate enough to use in practice.

Conventional wisdom said ML decoding of QLDPC codes faced fundamental obstacles: the space of possible error patterns is enormous, the structure is non-local (unlike the surface code's simple grid, which convolutional networks exploit naturally), and the number of logical qubits is large. The right architectural choices turn out to overcome those barriers. Code-aware attention, recurrence, and autoregressive outputs each address a specific difficulty at practically relevant scales.

The results are not yet definitive at all code sizes. On the [[144,12,12]] code, BP-OSD recovers its error-rate advantage at very low physical error rates. But the speed advantage holds across the board, and scaling to larger codes looks feasible.

> **Bottom Line:** MIT researchers have built the first ML decoder to outperform BP-OSD on QLDPC codes in a practically relevant regime, achieving 5× lower logical error rates and 10× faster worst-case runtimes on the [[72,12,6]] Bivariate Bicycle code. This is a significant step toward real-time decoding for next-generation quantum processors.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work fuses quantum information theory, modern deep learning architecture design, and classical coding theory. Transformer self-attention, guided by the algebraic structure of quantum error-correcting codes, solves a problem at the heart of fault-tolerant quantum computing.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper introduces code-aware self-attention for quantum codes and shows that recurrent transformer architectures can generalize to QLDPC codes, pushing ML-based decoding well beyond the surface code where prior work has been concentrated.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By delivering a practical, fast decoder for Bivariate Bicycle codes (the leading candidates for resource-efficient fault-tolerant quantum computation), this work addresses a key bottleneck on the path to quantum computers capable of simulating complex physical systems relevant to fundamental physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will need to extend these results to larger code distances and lower physical error rates, and to explore whether the ML decoder can run on quantum-compatible hardware accelerators. The paper is available at [arXiv:2504.13043](https://arxiv.org/abs/2504.13043) (Blue, Avlani, He, Ziyin, Chuang, MIT, 2025).</span></div></div>
</div>
