---
abstract: Tens of thousands of galaxy-galaxy strong lensing systems are expected to
  be discovered by the end of the decade. These will form a vast new dataset that
  can be used to probe subgalactic dark matter structures through its gravitational
  effects, which will in turn allow us to study the nature of dark matter at small
  length scales. This work shows how we can leverage machine learning to search through
  the data and identify which systems are most likely to contain dark matter substructure
  and thus can be studied in greater depth. We use a UNet, an image segmentation architecture,
  on a simulated strongly-lensed dataset with realistic sources (COSMOS galaxies),
  lenses (power-law elliptical profiles with multipoles and external shear), and noise.
  Our machine learning algorithm is able to quickly detect most substructure at high
  image resolution and subhalo concentration. At a false positive rate of $10\%$,
  we are able to identify systems with substructure at a true positive rate of $71\%$
  for a subhalo mass range of $10^{9}\text{-}10^{9.5}\,M_\odot$. While recent detections
  are consistent with higher concentrations, we find that our algorithm fails at detecting
  subhalos with lower concentrations (expected from $Λ$CDM simulations).
arxivId: '2401.16624'
arxivUrl: https://arxiv.org/abs/2401.16624
authors:
- Arthur Tsang
- Atınç Çağan Şengül
- Cora Dvorkin
concepts:
- dark matter
- gravitational lensing
- convolutional networks
- image segmentation
- classification
- signal detection
- simulation-based inference
- inverse problems
- cosmological simulation
- subhalo concentration
- anomaly detection
- model validation
figures:
- /iaifi-research-blog/figures/2401_16624/figure_1.png
- /iaifi-research-blog/figures/2401_16624/figure_2.png
pdfUrl: https://arxiv.org/pdf/2401.16624v1
published: '2024-01-29T23:42:14+00:00'
theme: Astrophysics
title: Substructure Detection in Realistic Strong Lensing Systems with Machine Learning
wordCount: 1256
---

## The Big Picture

Imagine you're trying to find a ghost by looking for the shadows it casts. You can't see the ghost directly, but you can see how it warps the light around it, bending and distorting the shapes of things behind it. That's what physicists do when they hunt for dark matter using gravitational lensing. A team from Harvard has now taught a neural network to spot those shadows automatically.

Dark matter makes up about 85% of all matter in the universe, yet we've never directly detected a single particle of it. What we have detected are its gravitational fingerprints: the way it bends light from distant galaxies, stretching them into arcs and rings when a massive galaxy sits between us and them. These dramatic distortions are called **strong lensing systems**, and they act as cosmic laboratories. Inside them, tiny clumps of dark matter called **subhalos** leave almost imperceptible distortions in the lensed images. Almost imperceptible, but not quite.

The problem is scale. We currently know of roughly a hundred such lensing systems. By 2030, telescopes like the Vera Rubin Observatory and Euclid will push that number to tens or hundreds of thousands. Traditional analysis of a single lens takes days to weeks. Researchers Arthur Tsang, Atınç Çağan Şengül, and Cora Dvorkin set out to fix this with a machine learning system that scans enormous catalogs and flags the systems most likely to harbor detectable dark matter substructure, like a triage nurse sorting patients before the doctors arrive.

> **Key Insight:** A neural network trained on realistic simulated lenses can identify 71% of systems containing dark matter subhalos, at just a 10% false positive rate, in a fraction of the time traditional methods require.

## How It Works

The core tool is a **UNet**, a neural network architecture originally designed for biomedical image segmentation. In its medical application, a UNet identifies tumor boundaries in an MRI scan. Here, it learns to pick out regions in a lensing image that have been nudged and distorted by a dark matter subhalo. The network takes a lensed galaxy image as input and outputs a heat map (a segmentation mask highlighting where a subhalo is most likely lurking).

![Figure 1](/iaifi-research-blog/figures/2401_16624/figure_1.png)

Training required building a realistic simulated dataset, and this is where the work gets meticulous. The team used `lenstronomy` to generate thousands of synthetic lensing systems, deliberately avoiding the overly tidy simulations that undermined earlier machine learning work. Their simulations included:

- **Realistic source galaxies** from the COSMOS survey (real Hubble photographs, not smooth idealized shapes)
- **Complex main lenses** modeled with power-law elliptical potentials, external shear, and higher-order multipoles, capturing the lumpy, asymmetric mass distributions of real galaxies
- **Realistic noise** consistent with space telescope observations
- **Subhalos** modeled as truncated NFW profiles spanning 10⁸ to 10¹⁰ solar masses, placed along Einstein rings where their effect is strongest

The realism matters because earlier machine learning approaches trained on simplified lenses fell apart on real data. Using actual galaxy morphologies, realistic noise, and complex lens models goes a long way toward fixing that.

![Figure 2](/iaifi-research-blog/figures/2401_16624/figure_2.png)

The network was trained both to classify whether an image contains a subhalo and to localize it. At a **false positive rate** (FPR) of 10% (meaning one in ten subhalo-free systems would trigger a false alarm), the UNet achieved a **true positive rate** (TPR) of 71% for subhalos in the 10⁹ to 10⁹·⁵ solar mass range. Performance improved with higher image resolution and with higher subhalo concentration, which measures how centrally dense the subhalo's mass profile is.


The concentration result carries a warning. Real-world subhalo detections have tended to favor high concentrations, which the algorithm handles well. But standard **ΛCDM (Lambda Cold Dark Matter)** simulations predict that most subhalos should have lower concentrations. The algorithm struggles with these, raising an open question: are real subhalos genuinely more concentrated than simulations predict, or are we only finding the easy cases?

## Why It Matters

Two problems collide here. The first is practical: the coming data flood from next-generation surveys will be impossible to analyze with traditional statistical sampling methods, which need days of computation per system. A trained neural network evaluates an entire catalog in seconds, acting as a first-pass filter that directs expensive follow-up analysis toward the most promising targets. That speed advantage isn't incremental; it's what makes the science possible at all.

The second problem is fundamental. Dark matter models like **warm dark matter (WDM)**, in which particles move fast enough to smooth out small-scale clumping, and **self-interacting dark matter (SIDM)**, in which dark matter particles collide with each other and reshape how clumps form, predict different subhalo populations than standard ΛCDM. The differences are sharpest at the smallest scales. Measuring subhalo abundance and properties across thousands of lensing systems would test these competing theories directly.

The concentration sensitivity problem identified here is itself a clue. Either our simulations are missing something about how subhalos form and evolve, or detections to date are a biased sample, the equivalent of concluding all fish are large because your net only catches large ones. Resolving this will sharpen our picture of what dark matter actually is.

> **Bottom Line:** By applying a UNet to realistically simulated strong lenses, Tsang et al. show that machine learning can efficiently screen thousands of lensing systems for dark matter substructure. That capability will be essential when next-generation surveys deliver their enormous catalogs, and it could reshape our understanding of dark matter's small-scale behavior.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work merges computer vision techniques from medical imaging with gravitational lensing physics, showing that tools built for one domain can solve open problems in cosmology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper advances image segmentation networks for scientific discovery, pushing training data closer to the messiness of real observations rather than relying on idealized simulations.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Fast, scalable detection of dark matter subhalos enables statistical constraints on the subhalo mass function and the nature of dark matter at the smallest accessible scales.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work must address the concentration sensitivity gap and extend the method to real telescope data. The full paper is available at [arXiv:2401.16624](https://arxiv.org/abs/2401.16624).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Substructure Detection in Realistic Strong Lensing Systems with Machine Learning</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2401.16624</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Arthur Tsang", "At\u0131n\u00e7 \u00c7a\u011fan \u015eeng\u00fcl", "Cora Dvorkin"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">Tens of thousands of galaxy-galaxy strong lensing systems are expected to be discovered by the end of the decade. These will form a vast new dataset that can be used to probe subgalactic dark matter structures through its gravitational effects, which will in turn allow us to study the nature of dark matter at small length scales. This work shows how we can leverage machine learning to search through the data and identify which systems are most likely to contain dark matter substructure and thus can be studied in greater depth. We use a UNet, an image segmentation architecture, on a simulated strongly-lensed dataset with realistic sources (COSMOS galaxies), lenses (power-law elliptical profiles with multipoles and external shear), and noise. Our machine learning algorithm is able to quickly detect most substructure at high image resolution and subhalo concentration. At a false positive rate of $10\%$, we are able to identify systems with substructure at a true positive rate of $71\%$ for a subhalo mass range of $10^{9}\text{-}10^{9.5}\,M_\odot$. While recent detections are consistent with higher concentrations, we find that our algorithm fails at detecting subhalos with lower concentrations (expected from $Λ$CDM simulations).</span></div></div>
</div>
