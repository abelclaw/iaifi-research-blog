---
abstract: 'Noise is a ubiquitous feature of the physical world. As a result, the first
  prerequisite of life is fault tolerance: maintaining integrity of state despite
  external bombardment. Recent experimental advances have revealed that biological
  systems achieve fault tolerance by implementing mathematically intricate error-correcting
  codes and by organizing in a modular fashion that physically separates functionally
  distinct subsystems. These elaborate structures represent a vanishing volume in
  the massive genetic configuration space. How is it possible that the primitive process
  of evolution, by which all biological systems evolved, achieved such unusual results?
  In this work, through experiments in Boolean networks, we show that the simultaneous
  presence of error correction and modularity in biological systems is no coincidence.
  Rather, it is a typical co-occurrence in noisy dynamic systems undergoing evolution.
  From this, we deduce the principle of error correction enhanced evolvability: systems
  possessing error-correcting codes are more effectively improved by evolution than
  those without.'
arxivId: '2303.14448'
arxivUrl: https://arxiv.org/abs/2303.14448
authors:
- Trevor McCourt
- Ila R. Fiete
- Isaac L. Chuang
concepts:
- error-correcting codes
- modularity
- evolvability
- robustness
- boolean network evolution
- stochastic processes
- fitness landscapes
- quantum computing
- phase transitions
figures:
- /iaifi-research-blog/figures/2303_14448/figure_1.png
- /iaifi-research-blog/figures/2303_14448/figure_1.png
- /iaifi-research-blog/figures/2303_14448/figure_2.png
- /iaifi-research-blog/figures/2303_14448/figure_2.png
- /iaifi-research-blog/figures/2303_14448/figure_3.png
- /iaifi-research-blog/figures/2303_14448/figure_3.png
pdfUrl: https://arxiv.org/pdf/2303.14448v2
published: '2023-03-25T11:54:18+00:00'
theme: Foundational AI
title: Noisy dynamical systems evolve error correcting codes and modularity
wordCount: 971
---

## The Big Picture

Imagine building a computer from unreliable parts — transistors that randomly flip, wires that occasionally short, memory cells that forget. How would you design a system that computes reliably despite the noise? Now imagine you couldn't design it at all. You had to let random trial-and-error find the answer over millions of generations. Most engineers would call that impossible. Evolution apparently didn't get the memo.

Life is a noisy business. Every cell in your body is bombarded by random heat energy, chemical mishaps, and DNA damage from radiation. Yet biological systems don't just cope with this chaos — they thrive in it, maintaining extraordinary accuracy across billions of generations.

What's more puzzling: the tools biology uses to achieve this — **error-correcting codes** that automatically detect and fix mistakes, and a **modular architecture** that physically separates distinct functions — represent a vanishingly tiny fraction of all possible genetic designs. Finding them by random search seems almost miraculous.

A new study from MIT researchers Trevor McCourt, Ila Fiete, and Isaac Chuang offers a compelling explanation: these structures aren't improbable outcomes of evolution. They're the *expected* ones.

> **Key Insight:** In noisy environments, evolutionary processes don't just stumble upon error-correcting codes and modularity — they are systematically drawn toward them, because error correction itself makes organisms *better at evolving*.

## How It Works

The team's experimental platform is the **Boolean network** — a model originally developed to study how genes switch each other on and off. Picture a grid of nodes, each either "on" or "off," updating according to a logical rule that takes neighboring nodes as inputs. Simple rules, chained across thousands of nodes, can perform surprisingly complex computations.

Boolean networks are simple enough to simulate millions of generations rapidly while still capturing the essential dynamics of real biological regulatory systems.

![Figure 1](/iaifi-research-blog/figures/2303_14448/figure_1.png)

The researchers evolved Boolean networks to perform primitive computational tasks — the biological equivalent of simple reflexes or cell-state decisions — under evolutionary pressure in the presence of noise. Networks that performed accurately despite noise were more likely to survive; errors brought fitness penalties. Mutations were applied each generation, tweaking logical rules or connections.

The results were striking. Across a wide range of initial conditions and task specifications:

- Networks consistently evolved to implement error-correcting codes — structured redundancy allowing them to recover correct outputs even when noise scrambled internal states
- This happened not occasionally but *almost universally*, suggesting error correction is an attractor of noisy evolution rather than a lucky accident
- When tasks were composite, networks spontaneously developed modular architectures, physically separating the sub-networks responsible for each sub-task

![Figure 2](/iaifi-research-blog/figures/2303_14448/figure_1.png)

The mechanism is a feedback loop the authors call **error correction-enhanced evolvability**. A network with error correction tolerates genetic mutations better: many mutations that would be lethal in a non-error-correcting system get quietly absorbed by the redundant coding, becoming **neutral mutations** — changes that don't affect fitness. This expanded neutral zone lets the network explore more of the genetic configuration space. Some of that exploration finds paths to *better* error-correcting codes. Error correction begets more error correction.

## Why It Matters

For evolutionary biology, this work proposes a clean mechanistic answer to a longstanding puzzle: why do biological systems converge on such elaborate, low-probability structures? Noise actively reshapes the fitness landscape, making error-correcting configurations easier to reach and easier to improve once reached.

The result aligns with observations across biology. In genetics, knockout experiments show most genes are dispensable — a signature of neutral redundancy. In neuroscience, grid cells appear to implement a topological error-correcting code for spatial navigation.

![Figure 3](/iaifi-research-blog/figures/2303_14448/figure_2.png)

For AI and computing, the implications are immediate. Modern machine learning systems are increasingly large, distributed, and deployed in noisy real-world environments. Understanding how biological systems evolved robust computation — not by design but by selection pressure — could inspire new architectures for fault-tolerant AI.

There's also a deep connection to quantum computing, where error correction is existential and the challenge of building self-correcting systems from noisy components mirrors the evolutionary challenge studied here. The principle that modularity and error correction co-emerge under noise could guide the design of future neuromorphic and quantum systems alike.

![Figure 4](/iaifi-research-blog/figures/2303_14448/figure_2.png)

Open questions remain. The Boolean network model is a simplified proxy for real genetics — how well does error correction-enhanced evolvability hold in continuous, high-dimensional systems? Does it apply to the evolution of learning itself, explaining why biological brains generalize from noisy data so much better than current artificial networks? These are ripe targets for future work.

> **Bottom Line:** Noise isn't evolution's enemy — it's the pressure that forces life to build error-correcting codes and modular architectures, and those structures then make further evolution easier. This self-reinforcing loop explains why robust, modular organization is ubiquitous in biology, and could reshape how we design fault-tolerant AI systems.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges quantum information theory, evolutionary biology, and computational neuroscience — using error-correcting code theory originally developed for quantum computing to explain the emergence of biological robustness, a quintessential IAIFI fusion of AI and fundamental physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The principle of error correction-enhanced evolvability provides a new lens for designing robust AI architectures, suggesting that building redundancy into artificial networks may not just improve reliability but could actively accelerate learning and adaptation.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By modeling evolutionary dynamics in noisy Boolean networks, the researchers uncover a deep physical principle: stochastic environments systematically select for mathematical structures — error-correcting codes — that are otherwise vanishingly rare, connecting thermodynamic noise to the emergence of complex biological organization.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work should test these principles in continuous dynamical systems and neural network models, and explore whether error correction-enhanced evolvability applies to the evolution of learning algorithms themselves; the paper is available at arXiv:2303.01529.</span></div></div>
</div>
