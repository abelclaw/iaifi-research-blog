---
abstract: We study a class of supersymmetric Froggatt-Nielsen (FN) models with multiple
  U(1) symmetries and Standard Model (SM) singlets inspired by heterotic string compactifications
  on Calabi-Yau threefolds. The string-theoretic origin imposes a particular charge
  pattern on the SM fields and FN singlets, dividing the latter into perturbative
  and non-perturbative types. Employing systematic and heuristic search strategies,
  such as genetic algorithms, we identify charge assignments and singlet VEVs that
  replicate the observed mass and mixing hierarchies in the quark sector, and subsequently
  refine the Yukawa matrix coefficients to accurately match the observed values for
  the Higgs VEV, the quark and charged lepton masses and the CKM matrix. This bottom-up
  approach complements top-down string constructions and our results demonstrate that
  string FN models possess a sufficiently rich structure to account for flavour physics.
  On the other hand, the limited number of distinct viable charge patterns identified
  here indicates that flavour physics imposes tight constraints on string theory models,
  adding new constraints on particle spectra that are essential for achieving a realistic
  phenomenology.
arxivId: '2410.17704'
arxivUrl: https://arxiv.org/abs/2410.17704
authors:
- Andrei Constantin
- Kit Fraser-Taliente
- Thomas R. Harvey
- Lucas T. Y. Leung
- Andre Lukas
concepts:
- froggatt-nielsen mechanism
- string theory
- effective field theory
- flavour hierarchy
- calabi-yau compactification
- standard model
- symmetry breaking
- group theory
- automated discovery
- new physics searches
- renormalization
figures:
- /iaifi-research-blog/figures/2410_17704/figure_1.png
- /iaifi-research-blog/figures/2410_17704/figure_1.png
- /iaifi-research-blog/figures/2410_17704/figure_2.png
- /iaifi-research-blog/figures/2410_17704/figure_2.png
- /iaifi-research-blog/figures/2410_17704/figure_3.png
- /iaifi-research-blog/figures/2410_17704/figure_3.png
pdfUrl: https://arxiv.org/pdf/2410.17704v2
published: '2024-10-23T09:27:14+00:00'
theme: Theoretical Physics
title: Fermion Masses and Mixing in String-Inspired Models
wordCount: 1141
---

## The Big Picture

Why is the top quark roughly 85,000 times heavier than the up quark? Both are fundamental particles, both quarks, yet their masses differ by nearly five orders of magnitude. This is the **flavor hierarchy problem**, one of the deepest unsolved puzzles in particle physics.

The Standard Model catalogs this hierarchy with embarrassing precision but explains nothing about it. One elegant proposal, the **Froggatt-Nielsen (FN) mechanism**, suggests a hidden symmetry is at work: particles couple to a new scalar field that settles to a fixed, nonzero value throughout space, and mass differences emerge from integer-valued "charges" the symmetry assigns to each particle.

Think of it like a musical scale: different notes arise not from chaos, but from simple integer ratios.

A team from Oxford and MIT has pushed this idea further, asking whether the FN mechanism doesn't just fit the data but actually emerges from string theory itself. Using systematic search strategies and **genetic algorithms**, they found charge assignments that reproduce observed quark masses and mixing angles. They also showed that flavor physics places tight constraints on which string theory models are viable.

> **Key Insight:** String theory doesn't just permit Froggatt-Nielsen-type models; it predicts a specific class of them. Demanding agreement with observed particle masses leaves only a handful of viable charge patterns, giving theorists a concrete filter on the vast string landscape.

## How It Works

The starting point is **heterotic string theory** compactified on **Calabi-Yau threefolds**, a leading framework for building realistic particle physics from strings. The extra spatial dimensions are curled into intricate geometric shapes. When the mathematical structures encoding forces across those extra dimensions (called "gauge bundles") split apart at special configurations, **anomalous U(1) symmetries** emerge. These behave exactly like Froggatt-Nielsen symmetries, assigning hidden charges to quarks and leptons that determine which **Yukawa couplings** are permitted in the low-energy theory. Yukawa couplings govern how strongly each particle couples to the Higgs field, and thus how massive it becomes.

These string-derived models differ from textbook FN models in three ways:

- **Multiple U(1) symmetries**, up to four independent factors (the simplest type of symmetry, like rotations by a phase), parameterized by integer partitions of 5, such as (1,1,1,1,1) or (1,2,2)
- **Two types of FN scalars**: "perturbative" singlets tied to the force-carrying structures in the extra dimensions, calculable via standard expansion methods, and "non-perturbative" singlets tied to the geometry itself, where strong quantum effects require different techniques
- **GUT-organized charges**: the underlying SU(5) grand unified symmetry groups quarks and leptons into related families, so charges cluster by family, sharply reducing free parameters

![Figure 1](/iaifi-research-blog/figures/2410_17704/figure_1.png)

With this structure fixed, the challenge is navigating the enormous space of possible charge assignments, millions of candidates across all partition types. The team turned to **genetic algorithms**, computational search methods inspired by biological evolution. Candidate charge assignments that better reproduce observed mass ratios get selected, mutated, and recombined across generations. Those that don't get culled.

The fitness function measures agreement with observed quark mass ratios and **CKM mixing angles**, the matrix governing how quarks from different generations mix during interactions. Once the algorithm identified promising patterns, the team refined them by numerically optimizing the dimensionless coefficients in the Yukawa couplings (expected to be close to 1) to match experimental values.

![Figure 3](/iaifi-research-blog/figures/2410_17704/figure_2.png)

The result: specific models that correctly predict all quark and charged lepton masses, the Higgs field's vacuum value, and the full CKM matrix to high accuracy.

## Why It Matters

The broader significance cuts in two directions. From the string theory side, the results are both encouraging and constraining. String FN models are rich enough to accommodate realistic flavor physics, but only a very limited number of distinct charge patterns actually work.

Flavor physics isn't a free parameter in string model building. It's a filter.

![Figure 5](/iaifi-research-blog/figures/2410_17704/figure_3.png)

This complements "top-down" approaches, which start from a specific string compactification and derive what low-energy physics falls out. Here the researchers work bottom-up: they demand realistic particle masses and ask what string structures could produce them. The two approaches are converging.

Earlier work at MIT applied neural network techniques to compute Yukawa couplings directly from the mathematics of string geometry, a formidable calculation. The present work provides phenomenological targets to guide those computations, pointing toward which regions of the string configuration space are actually worth exploring.

The framework extends to the neutrino sector, where lepton mixing angles and neutrino masses remain unexplained. The tight constraints identified here also sharpen the broader string landscape problem: any realistic string vacuum must thread the needle of flavor physics, and now the needle is sharper.

> **Bottom Line:** By applying genetic algorithms to string-inspired Froggatt-Nielsen models, this team reproduced observed quark masses and mixings from first principles, and found that very few charge patterns survive the filter of flavor physics. String theorists now have a concrete target to aim for.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects string theory and machine learning by deploying genetic algorithms to search the space of string-inspired flavor models, translating a fundamental physics constraint problem into an evolutionary optimization task.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Genetic algorithms can efficiently navigate high-dimensional discrete parameter spaces in theoretical physics. The approach here offers a template for AI-assisted model building across fundamental theory.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Only a handful of viable string Froggatt-Nielsen charge patterns are compatible with observed quark masses and CKM mixing, imposing tight new phenomenological constraints on heterotic string compactifications.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend these methods to the neutrino sector and connect with direct Yukawa coupling calculations in string geometry; the paper is available at [arXiv:2410.17704](https://arxiv.org/abs/2410.17704).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Fermion Masses and Mixing in String-Inspired Models</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2410.17704</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Andrei Constantin", "Kit Fraser-Taliente", "Thomas R. Harvey", "Lucas T. Y. Leung", "Andre Lukas"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We study a class of supersymmetric Froggatt-Nielsen (FN) models with multiple U(1) symmetries and Standard Model (SM) singlets inspired by heterotic string compactifications on Calabi-Yau threefolds. The string-theoretic origin imposes a particular charge pattern on the SM fields and FN singlets, dividing the latter into perturbative and non-perturbative types. Employing systematic and heuristic search strategies, such as genetic algorithms, we identify charge assignments and singlet VEVs that replicate the observed mass and mixing hierarchies in the quark sector, and subsequently refine the Yukawa matrix coefficients to accurately match the observed values for the Higgs VEV, the quark and charged lepton masses and the CKM matrix. This bottom-up approach complements top-down string constructions and our results demonstrate that string FN models possess a sufficiently rich structure to account for flavour physics. On the other hand, the limited number of distinct viable charge patterns identified here indicates that flavour physics imposes tight constraints on string theory models, adding new constraints on particle spectra that are essential for achieving a realistic phenomenology.</span></div></div>
</div>
