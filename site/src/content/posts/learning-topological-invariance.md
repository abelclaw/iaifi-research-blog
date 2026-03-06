---
abstract: Two geometric spaces are in the same topological class if they are related
  by certain geometric deformations. We propose machine learning methods that automate
  learning of topological invariance and apply it in the context of knot theory, where
  two knots are equivalent if they are related by ambient space isotopy. Specifically,
  given only the knot and no information about its topological invariants, we employ
  contrastive and generative machine learning techniques to map different representatives
  of the same knot class to the same point in an embedding vector space. An auto-regressive
  decoder Transformer network can then generate new representatives from the same
  knot class. We also describe a student-teacher setup that we use to interpret which
  known knot invariants are learned by the neural networks to compute the embeddings,
  and observe a strong correlation with the Goeritz matrix in all setups that we tested.
  We also develop an approach to resolving the Jones Unknot Conjecture by exploring
  the vicinity of the embedding space of the Jones polynomial near the locus where
  the unknots cluster, which we use to generate braid words with simple Jones polynomials.
arxivId: '2504.12390'
arxivUrl: https://arxiv.org/abs/2504.12390
authors:
- James Halverson
- Fabian Ruehle
concepts:
- topological invariance learning
- contrastive learning
- embeddings
- representation learning
- transformers
- knot invariants
- generative models
- interpretability
- self-supervised learning
- symmetry preservation
- group theory
- loss function design
- convolutional networks
figures:
- /iaifi-research-blog/figures/2504_12390/figure_1.png
- /iaifi-research-blog/figures/2504_12390/figure_2.png
- /iaifi-research-blog/figures/2504_12390/figure_3.png
pdfUrl: https://arxiv.org/pdf/2504.12390v1
published: '2025-04-16T18:00:50+00:00'
theme: Foundational AI
title: Learning Topological Invariance
wordCount: 1084
---

## The Big Picture

Imagine a tangled rope — an overhand knot — and another knotted rope across the table. You can stretch, twist, and contort either rope all you want, but you can't cut or glue. Are they the same knot? This deceptively simple question has stumped mathematicians for over a century and lies at the heart of **knot theory**.

Mathematicians have developed dozens of **topological invariants** — numerical fingerprints that remain constant no matter how you deform a knot — but no single invariant can definitively identify whether two arbitrary knots are equivalent. Computing these invariants by hand is brutally hard, and even powerful algorithms struggle with complex cases. The dream: a system that could simply *look* at two knotted configurations and recognize them as equivalent, the way a human recognizes two photos of the same face.

Researchers James Halverson and Fabian Ruehle at Northeastern University and IAIFI have built exactly that: a machine learning system that learns topological invariance from scratch, with no prior knowledge of knot invariants, then uses that knowledge to probe one of the deepest unsolved problems in knot theory.

> **Key Insight:** By training neural networks to recognize topologically equivalent knots — with no prior knowledge of knot invariants — the system autonomously discovers that a specific mathematical object called the Goeritz matrix is the most important underlying feature, and uses this to open a new computational front on the famous Jones Unknot Conjecture.

## How It Works

The team represents knots as **braid words** — sequences of integers encoding how strands cross over and under each other. The same knot can be written as many different braid words, just as the same idea can be expressed many ways. The challenge: teach a neural network that two wildly different braid words describe the same underlying knot.

They pursue this with two complementary strategies:

- **Contrastive learning:** The network trains on pairs and triplets of braid words. When two describe the same knot, the network is penalized for placing them far apart in its internal representation of knot-space; when they describe different knots, it's penalized for placing them close. Both a standard feed-forward network and a **convolutional neural network (CNN)** (which automatically recognizes that certain rearrangements of a braid word leave the knot unchanged) are tested.
- **Generative learning:** An encoder-decoder Transformer — the same architecture behind large language models — learns to read any braid word and rewrite it as the canonical representative of that knot class. Critically, the decoder *generates*: it can produce entirely new, valid braid words belonging to the same topological class as the input.

To verify equivalence, the team compares **hyperbolic knot volumes** — a powerful invariant that acts like a unique barcode for most knots. If a freshly generated braid word shares the same hyperbolic volume as the input, it's almost certainly the same knot. Both methods succeed.

![Figure 1](/iaifi-research-blog/figures/2504_12390/figure_1.png)

With the networks trained, Halverson and Ruehle ask a deeper question: *what did they actually learn?* A student-teacher experiment probes this. Large "teacher" networks produce compact numerical representations of braid words. Simpler "student" networks then try to reproduce those representations — but using only known mathematical invariants as input: the Alexander polynomial, HOMFLY polynomial, signature, and the **Goeritz matrix** (which encodes how strands link and wrap around each other).

![Figure 2](/iaifi-research-blog/figures/2504_12390/figure_2.png)

The verdict is consistent across every architecture and training method: the student finds the strongest correlation with the Goeritz matrix. Given no hints, the neural networks converged on the same object that experienced knot theorists regard as fundamental. This is automated mathematical discovery, and it raises an immediate question: could a more expressive student network point toward invariants not yet named?

The most ambitious application targets the **Jones Unknot Conjecture**: a knot has a trivial Jones polynomial *if and only if* it is the unknot — the simple loop with no crossing. The "only if" direction is easy; if it's the unknot, the polynomial is trivial. The "if" direction has resisted proof for decades.

Could there exist a genuinely knotted loop whose Jones polynomial is identical to the unknot's?

The team trains a Transformer to map Jones polynomials to braid words, then searches the network's learned space near the region where unknots cluster. This generates thousands of candidate braid words with simple Jones polynomials, which are then checked against other invariants to separate genuine unknots from imposters.

![Figure 3](/iaifi-research-blog/figures/2504_12390/figure_3.png)

No counterexample was found — but the framework itself is new: a principled, generative method for exploring a conjecture that pure mathematics has not yet cracked.

## Why It Matters

This work sits at the intersection of two major trends: deep learning as a tool for mathematical discovery, and AI applied to fundamental physics where topology plays a central role — from quantum field theory and string theory to condensed matter physics. Any method that automates the recognition or generation of topological invariants has broad reach.

The student-teacher interpretability result is particularly significant. The Goeritz matrix's consistent emergence is a concrete, verifiable claim that pure mathematicians can engage with directly. It raises a natural follow-on: what would a more expressive student network find — perhaps invariants not yet discovered? Future work could extend these methods to higher-dimensional topological spaces, link invariants, topological insulators, and quantum error-correcting codes.

The generative approach to the Jones Unknot Conjecture is equally promising. Rather than exhaustive search, the network learns the geometry of the problem and focuses exploration where counterexamples would most plausibly hide.

> **Bottom Line:** Neural networks can learn that two knots are equivalent without being told what a topological invariant is — and when you ask what they learned, they point straight at the Goeritz matrix, while opening a new computational front on the Jones Unknot Conjecture.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges pure mathematics and machine learning by training neural networks to autonomously discover topological equivalence, showing that deep learning can recover classical mathematical insights without explicit guidance.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The contrastive and generative learning framework, combined with the student-teacher interpretability setup, offers a broadly applicable template for using AI to discover abstract equivalence relations in any domain where invariants are unknown.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Topology is central to modern physics, from gauge theories to string compactifications; automating its recognition opens new computational routes through these structures.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future directions include extending these methods to higher-dimensional spaces and linking topological structures to physical observables; the paper is available at [arXiv:2504.12390](https://arxiv.org/abs/2504.12390).</span></div></div>
</div>
