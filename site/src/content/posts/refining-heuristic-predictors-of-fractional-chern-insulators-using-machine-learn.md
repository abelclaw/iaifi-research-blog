---
abstract: 'We develop an interpretable, data-driven framework to quantify how single-particle
  band geometry governs the stability of fractional Chern insulators (FCIs). Using
  large-scale exact diagonalization, we evaluate an FCI metric that yields a continuous
  spectral measure of FCI stability across parameter space. We then train Kolmogorov-Arnold
  networks (KANs) -- a recently developed interpretable neural architecture -- to
  regress this metric from two band-geometric descriptors: the trace violation $T$
  and the Berry curvature fluctuations $σ_B$. Applied to spinless fermions at filling
  $ν=1/3$ in models on the checkerboard and kagome lattices, our approach yields compact
  analytical formulas that predict FCI stability with over $>80 \%$ accuracy in both
  regression and classification tasks, and remain reliable even in data-scarce regimes.
  The learned relations reveal model-dependent trends, clarifying the limits of Landau-level-mimicking
  heuristics. Our framework provides a general method for extracting simple, phenomenological
  "laws" that connect many-body phase stability to chosen physical descriptors, enabling
  rapid hypothesis formation and targeted design of quantum phases.'
arxivId: '2512.01873'
arxivUrl: https://arxiv.org/abs/2512.01873
authors:
- Oriol Mayné i Comas
- André Grossi Fonseca
- Sachin Vaidya
- Marin Soljačić
concepts:
- fractional chern insulators
- kolmogorov-arnold networks
- band geometry
- interpretability
- regression
- exact diagonalization
- phase transitions
- classification
- quantum states
- surrogate modeling
- loss function design
- entanglement
figures:
- /iaifi-research-blog/figures/2512_01873/figure_1.png
- /iaifi-research-blog/figures/2512_01873/figure_1.png
- /iaifi-research-blog/figures/2512_01873/figure_2.png
- /iaifi-research-blog/figures/2512_01873/figure_2.png
- /iaifi-research-blog/figures/2512_01873/figure_3.png
- /iaifi-research-blog/figures/2512_01873/figure_3.png
pdfUrl: https://arxiv.org/pdf/2512.01873v1
published: '2025-12-01T16:53:53+00:00'
theme: Theoretical Physics
title: Refining Heuristic Predictors of Fractional Chern Insulators using Machine
  Learning
wordCount: 1196
---

## The Big Picture

Imagine trying to predict whether a material will become a superconductor just by looking at its crystal structure — before running a single expensive experiment. That's roughly the challenge facing physicists who study **fractional Chern insulators (FCIs)**: exotic materials where electrons pool into collective states that behave as if each carries only a *fraction* of a single electron's charge.

It sounds impossible. Electrons are elementary particles — their charge is fixed. But in the right quantum environment, collective behavior can mimic particles that don't exist on their own. The phenomenon is so strange it borders on science fiction.

The problem is that verifying whether a material hosts this behavior requires enormous computational effort: simulating all electrons interacting simultaneously quickly becomes intractable. And the results depend sensitively on subtle mathematical properties of how electrons move through the crystal.

A team of MIT physicists has now turned machine learning into a kind of crystal ball for this problem. By feeding a neural network those mathematical properties, they taught it to predict whether exotic fractional behavior would emerge — with over 80% accuracy — then distilled those predictions into compact formulas a physicist can actually read and reason with.

The result isn't just a black-box predictor. It's a window into the hidden rules governing some of the most exotic states of quantum matter.

> **Key Insight:** Kolmogorov-Arnold Networks can extract simple, interpretable formulas connecting a material's single-particle band geometry to its many-body FCI stability — achieving >80% accuracy while revealing model-dependent physics invisible to older heuristics.

## How It Works

In traditional two-dimensional electron gases under magnetic fields, electrons occupy **Landau levels** — quantum energy levels with vast degeneracy, like a perfectly flat energy landscape. This structure is what enables fractional charge behavior. When physicists discovered similar behavior could arise in crystal lattices *without* any magnetic field, a key question emerged: what makes a **Chern band** (the lattice analog of a Landau level) structured enough to support fractionalization?

Two geometric quantities emerged as prime suspects. The first, the **trace violation** *T*, measures how much a band's **quantum metric** — a mathematical measure of distance between nearby quantum states — deviates from the relationship that holds exactly in ideal Landau levels. The second, **Berry curvature fluctuations** σ_B, captures how unevenly **Berry curvature** is spread across the **Brillouin zone**. Think of Berry curvature as an invisible magnetic field living in the abstract space of electron momenta: Landau levels have perfectly uniform Berry curvature; real lattice systems don't.

Together, T and σ_B form a two-number summary of how "Landau-level-like" a given band is. But how predictive are they, exactly?

![Figure 1](/iaifi-research-blog/figures/2512_01873/figure_1.png)

To find out, the team built a large dataset using **exact diagonalization (ED)** — a brute-force numerical method that computes full quantum behavior by constructing and directly solving enormous matrices. They swept across parameter space in two prototypical lattice models (the checkerboard and kagome lattices) at filling fraction ν = 1/3, evaluating a continuous **FCI quality metric** at each point. This metric captures both the many-body gap and the ground-state energy spread under flux insertion — a richer target than a simple binary FCI/not-FCI label.

With this dataset in hand, the team turned to **Kolmogorov-Arnold Networks (KANs)** — a neural architecture introduced in 2024 that places learnable activation functions on each *edge* of the network graph rather than fixed activations on nodes. After training, those learned functions can often be matched to known mathematical expressions — logarithms, polynomials, exponentials — enabling symbolic extraction of the underlying formula.

![Figure 2](/iaifi-research-blog/figures/2512_01873/figure_1.png)

The pipeline:
1. Train a KAN to regress the FCI quality metric from (T, σ_B) pairs
2. Prune and retrain iteratively to find the simplest structure that still performs well
3. Fit the learned activation functions to symbolic expressions
4. Evaluate the resulting analytical formula on held-out data

The formulas that emerged were genuinely compact — the kind a physicist could write on a whiteboard.

![Figure 3](/iaifi-research-blog/figures/2512_01873/figure_2.png)

A naive expectation would suggest that both large T and large σ_B uniformly hurt FCI stability — both measure departures from ideal Landau-level geometry. The KAN formulas told a more nuanced story. In the **kagome lattice**, large σ_B does indeed destabilize the FCI, consistent with standard heuristics. But in the **checkerboard lattice**, the relationship inverts: larger Berry curvature fluctuations *enhance* FCI stability in certain parameter regimes. This isn't a numerical artifact — it reflects genuine model-dependent physics that one-size-fits-all heuristics simply cannot capture.

![Figure 4](/iaifi-research-blog/figures/2512_01873/figure_2.png)

The framework also proved remarkably data-efficient. With as few as ~100 exact diagonalization samples — a tiny fraction of what standard studies use — the KAN approach still captured dominant trends in FCI stability. Since ED is computationally expensive, this data efficiency opens the door to scanning far larger material spaces.

![Figure 5](/iaifi-research-blog/figures/2512_01873/figure_3.png)

Classification accuracy exceeded 80% for both lattice models, and the regression formulas tracked the continuous quality metric closely enough to distinguish stable FCI regions from marginal ones.

![Figure 6](/iaifi-research-blog/figures/2512_01873/figure_3.png)

## Why It Matters

This work sits at a productive intersection: it uses a cutting-edge ML architecture not to replace physical intuition, but to sharpen it. The KAN framework functions here as a "law extractor" — taking numerical data and producing the compact, interpretable relationships that physicists actually want.

The implications for quantum materials research are significant. Designing systems with topologically ordered ground states is currently a slow, expensive process of compute-and-check. A validated, interpretable formula connecting band geometry to phase stability could guide synthesis of new moiré superlattice materials, metamaterials, and photonic systems where FCI-like physics has recently been predicted or observed.

The discovery that σ_B plays opposite roles in different lattices also warns against over-applying universal heuristics — a caution that becomes actionable only when you have quantitative tools to probe deviations.

Open questions remain: How do the learned formulas extend to other lattice models, other fillings, or systems with spin? Can the same pipeline disentangle the roles of additional geometric descriptors beyond T and σ_B? The framework is ready to tackle these questions.

> **Bottom Line:** By training interpretable KAN networks on exact diagonalization data, this MIT team extracted simple analytical formulas that predict fractional Chern insulator stability with >80% accuracy — and revealed that standard Landau-level heuristics break down in model-dependent ways that matter for real material design.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work bridges interpretable machine learning with condensed matter physics, using Kolmogorov-Arnold Networks to distill complex many-body quantum simulations into compact physical laws governing exotic topological phases.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The study demonstrates that KANs can function as "law extractors" in a scientific context — producing human-readable formulas from numerical data with high accuracy even in data-scarce regimes, advancing the case for interpretable ML in physical discovery.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By quantitatively mapping band geometry to FCI stability and revealing model-dependent deviations from Landau-level heuristics, the work deepens our understanding of what makes topologically ordered quantum phases arise in lattice systems without magnetic fields.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work can extend this pipeline to other lattice geometries, fillings, and geometric descriptors, potentially accelerating the design of moiré and photonic systems hosting fractionalized phases; the paper is available at arXiv:2502.10843.</span></div></div>
</div>
