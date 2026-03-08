---
abstract: We present Symphony, an $E(3)$-equivariant autoregressive generative model
  for 3D molecular geometries that iteratively builds a molecule from molecular fragments.
  Existing autoregressive models such as G-SchNet and G-SphereNet for molecules utilize
  rotationally invariant features to respect the 3D symmetries of molecules. In contrast,
  Symphony uses message-passing with higher-degree $E(3)$-equivariant features. This
  allows a novel representation of probability distributions via spherical harmonic
  signals to efficiently model the 3D geometry of molecules. We show that Symphony
  is able to accurately generate small molecules from the QM9 dataset, outperforming
  existing autoregressive models and approaching the performance of diffusion models.
arxivId: '2311.16199'
arxivUrl: https://arxiv.org/abs/2311.16199
authors:
- Ameya Daigavane
- Song Kim
- Mario Geiger
- Tess Smidt
concepts:
- equivariant neural networks
- symmetry preservation
- spherical harmonic signals
- generative models
- geometric deep learning
- group theory
- spectral methods
- fragment-based generation
- graph neural networks
- density estimation
- diffusion models
- materials discovery
figures:
- /iaifi-research-blog/figures/2311_16199/figure_1.png
- /iaifi-research-blog/figures/2311_16199/figure_1.png
- /iaifi-research-blog/figures/2311_16199/figure_2.png
- /iaifi-research-blog/figures/2311_16199/figure_2.png
- /iaifi-research-blog/figures/2311_16199/figure_3.png
- /iaifi-research-blog/figures/2311_16199/figure_3.png
pdfUrl: https://arxiv.org/pdf/2311.16199v3
published: '2023-11-27T05:32:21+00:00'
theme: Foundational AI
title: 'Symphony: Symmetry-Equivariant Point-Centered Spherical Harmonics for 3D Molecule
  Generation'
wordCount: 1028
---

## The Big Picture

Imagine building a LEGO molecule in the dark — no instructions, just the knowledge that certain pieces click together in certain ways. Now scale that to billions of possible molecular shapes, each governed by the strict rules of quantum mechanics. That's the challenge facing computational chemists who want to design new drugs, materials, or catalysts from scratch.

The problem isn't just hard — it's geometrically treacherous. Molecules are 3D structures where the exact position of every atom determines whether a compound is a life-saving drug or a useless blob. They also have deep symmetries: rotate a water molecule 180 degrees and it's still a water molecule. An AI model that treats rotated structures as fundamentally different wastes computing power learning the same thing over and over.

Researchers at MIT and NVIDIA developed **Symphony**, a generative model that builds molecules atom by atom while respecting these 3D symmetries more powerfully than its predecessors. It outperforms earlier step-by-step AI approaches and matches leading models that work by progressively refining random noise into molecular structure.

> **Key Insight:** Symphony uses higher-degree equivariant features and spherical harmonic projections to represent the probability distribution of where the next atom should go — baking 3D symmetry directly into the model's architecture rather than bolting it on afterward.

## How It Works

Symphony builds molecules sequentially: start with a single atom, then repeatedly ask "where should the next atom go?" until the molecule is complete. This **autoregressive** approach — predicting one piece at a time based on everything prior — is the same strategy behind language models that generate text word by word.

![Figure 1](/iaifi-research-blog/figures/2311_16199/figure_1.png)

But molecules aren't sentences. Each new atom's position isn't a single number or a category — it's a point in continuous 3D space, requiring a probability distribution over all of that space.

Previous models like G-SchNet and G-SphereNet sidestepped this with **rotationally invariant features**: representations that look the same regardless of how you orient the molecule. Simple, but limiting — you lose directionality that could sharpen predictions.

Symphony takes a different path. It uses **E(3)-equivariant features** — representations that don't stay the same when you rotate a molecule, but transform *predictably* with the rotation. Think of arrows attached to atoms: rotate the molecule, and the arrows rotate with it. These features carry directional information while still respecting symmetry.

At each generation step, Symphony:

1. **Selects a focus atom** — one atom in the current fragment that serves as the origin for the next placement decision.
2. **Runs message-passing** across the existing fragment to build rich equivariant features at the focus atom, incorporating information from neighbors.
3. **Projects a probability distribution onto spherical harmonics** — mathematical functions that tile the surface of a sphere and can represent any angular distribution. The model predicts *coefficients* for these harmonics, painting a picture of where the next atom is likely to land.
4. **Samples a position** from this distribution, handling radial distance and angular direction separately.

**Spherical harmonics** are the key ingredient. They're the same mathematical objects used in quantum mechanics to describe electron orbitals — the s, p, and d orbital shapes from chemistry class are literally spherical harmonics. They form a complete basis for functions on a sphere, so any angular distribution can be represented exactly given enough terms. Symphony uses harmonics up to degree *l* = 5, capturing features from broad blobs down to detailed directional lobes.

![Figure 2](/iaifi-research-blog/figures/2311_16199/figure_1.png)

Because the spherical harmonic coefficients are themselves equivariant features, rotating the molecule rotates the predicted distribution with it — exactly as physics demands. Symphony doesn't need to laboriously learn that a carbon-hydrogen bond pointing left is the same as one pointing right. It knows by construction.

## Why It Matters

On the QM9 benchmark — a standard dataset of small organic molecules — Symphony outperforms all previous autoregressive models and comes remarkably close to state-of-the-art diffusion models on measures of chemical validity, uniqueness, and structural accuracy. That's significant. Diffusion models, which iteratively denoise random noise into molecular structures, have dominated 3D molecule generation in recent years. Matching their performance with an autoregressive approach opens a new design space, since autoregressive models offer distinct advantages in controllability, interpretability, and the ability to build on a partial structure as a starting point.

That last point matters enormously in practice. Symphony can generate valid molecules conditioned on molecular fragments it has never seen during training — a crucial property for drug design, where you often want to grow a known **scaffold** (a core structural template) into unexplored chemical territory. The model's equivariant architecture also generalizes across orientations without data augmentation (artificially training on many rotated copies of the same molecule), making it more sample-efficient on new datasets.

Looking forward, the spherical harmonic framework could scale to protein design, crystal structure prediction, or any domain where 3D geometry and symmetry are paramount. The bispectrum-based tool the team introduces — for measuring how accurately the model captures the angular arrangement of atoms around each position — is itself a useful contribution. Current benchmarks often miss subtle geometric errors that matter for downstream applications.

> **Bottom Line:** Symphony demonstrates that baking 3D symmetry deeply into a model's mathematical language — rather than engineering it out — pays off in both accuracy and generalization, charting a compelling path for AI-driven molecular design.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">Symphony directly imports mathematical tools from quantum mechanics — spherical harmonics and group-theoretic equivariance — into deep learning architecture, exemplifying IAIFI's mission of building AI systems grounded in the symmetry principles of physics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">By representing probability distributions over 3D space using spherical harmonic signals, Symphony establishes a new paradigm for geometry-aware generative modeling that outperforms prior autoregressive baselines and rivals diffusion models on QM9.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The model's ability to capture precise 3D molecular geometry — including correct local chemical environments verified via bispectrum analysis — advances machine learning for quantum chemistry and materials discovery.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work may extend Symphony's fragment-based autoregressive framework to larger molecular systems, proteins, and crystalline materials; the paper is available at arXiv:2210.07463 and was published at ICLR 2024.</span></div></div>
</div>
