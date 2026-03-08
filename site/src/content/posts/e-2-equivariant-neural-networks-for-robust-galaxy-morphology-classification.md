---
abstract: We propose the use of group convolutional neural network architectures (GCNNs)
  equivariant to the 2D Euclidean group, $E(2)$, for the task of galaxy morphology
  classification by utilizing symmetries of the data present in galaxy images as an
  inductive bias in the architecture. We conduct robustness studies by introducing
  artificial perturbations via Poisson noise insertion and one-pixel adversarial attacks
  to simulate the effects of limited observational capabilities. We train, validate,
  and test GCNNs equivariant to discrete subgroups of $E(2)$ - the cyclic and dihedral
  groups of order $N$ - on the Galaxy10 DECals dataset and find that GCNNs achieve
  higher classification accuracy and are consistently more robust than their non-equivariant
  counterparts, with an architecture equivariant to the group $D_{16}$ achieving a
  $95.52 \pm 0.18\%$ test-set accuracy. We also find that the model loses $<6\%$ accuracy
  on a $50\%$-noise dataset and all GCNNs are less susceptible to one-pixel perturbations
  than an identically constructed CNN. Our code is publicly available at https://github.com/snehjp2/GCNNMorphology.
arxivId: '2311.01500'
arxivUrl: https://arxiv.org/abs/2311.01500
authors:
- Sneh Pandya
- Purvik Patel
- Franc O
- Jonathan Blazek
concepts:
- equivariant neural networks
- group theory
- galaxy classification
- geometric deep learning
- symmetry preservation
- robustness
- convolutional networks
- classification
- adversarial robustness
- out-of-distribution detection
- data augmentation
figures:
- /iaifi-research-blog/figures/2311_01500/figure_1.png
- /iaifi-research-blog/figures/2311_01500/figure_1.png
- /iaifi-research-blog/figures/2311_01500/figure_2.png
- /iaifi-research-blog/figures/2311_01500/figure_2.png
- /iaifi-research-blog/figures/2311_01500/figure_3.png
- /iaifi-research-blog/figures/2311_01500/figure_3.png
pdfUrl: https://arxiv.org/pdf/2311.01500v1
published: '2023-11-02T18:00:02+00:00'
theme: Astrophysics
title: E(2) Equivariant Neural Networks for Robust Galaxy Morphology Classification
wordCount: 1155
---

## The Big Picture

Imagine trying to identify a face in a photo, but the photo might be upside down, rotated 45 degrees, or mirrored. You have no idea which. A human handles this effortlessly. Most machine learning models do not. Now swap the face for a galaxy, and you have one of the central challenges facing astronomers as telescopes like the Vera Rubin Observatory prepare to image billions of celestial objects.

Galaxies don't come with orientation labels. A spiral galaxy viewed edge-on looks nothing like the same galaxy seen face-on, yet both are the same object. Standard image-recognition AI treats these as fundamentally different inputs unless you hand-feed the system thousands of rotated examples and hope it generalizes. That's a brute-force workaround, not a solution.

Researchers at Northeastern University and the NSF Institute for AI and Fundamental Interactions (IAIFI) took a different approach: build the symmetry directly into the network's architecture, so it understands from the start that a galaxy rotated 90 degrees is still the same galaxy.

The result? A classification system that hits 95.52% accuracy on a standard galaxy dataset and holds that accuracy even when images are deliberately corrupted with noise or attacked pixel-by-pixel.

> By baking rotational and reflectional symmetry into the neural network's mathematical structure, the researchers built a galaxy classifier that is simultaneously more accurate and far more resistant to real-world image degradation than conventional approaches.

## How It Works

The key concept is **equivariance**, a mathematical property where the output of a function transforms predictably when the input is transformed. Rotate a galaxy image 90 degrees and feed it to an equivariant network, and the network's internal representations rotate correspondingly rather than producing a wildly different result.

Standard convolutional neural networks (CNNs), the workhorse of image-recognition AI, are only translation-equivariant: they can recognize an object no matter where it appears in an image, but not how it's oriented or flipped.

The researchers built **group convolutional neural networks (GCNNs)**, which extend equivariance to the 2D Euclidean group E(2), the mathematical framework describing all the ways you can rotate, flip, and slide an object in a flat plane. They tested discrete subgroups:

- **Cyclic groups C_N**, equivariant to N evenly-spaced rotations (e.g., C_4 handles 0°, 90°, 180°, 270°)
- **Dihedral groups D_N**, equivariant to those same rotations plus reflections

![Figure 1](figure:1)

Ten GCNN architectures (C_1 through D_16) were trained alongside a standard CNN baseline on the Galaxy10 DECals dataset: 17,736 labeled galaxy images across 10 morphological classes, from smooth round galaxies to edge-on disks to cigar-shaped objects. Each GCNN uses specialized filters that recognize the same galaxy feature regardless of orientation, learning symmetry-aware representations throughout training rather than just at the final classification step.

The architecture has 11 convolutional blocks, five pooling layers, and three fully-connected layers, trained for 100 epochs on four NVIDIA A100 GPUs. To keep the comparison fair, the team also applied random rotations and augmentations during CNN training. The GCNNs still won.

![Figure 2](figure:2)

The stress testing is where this gets interesting. The team deliberately broke the images two ways:

1. **Poisson noise insertion** at 25%, 50%, and 75% levels, mimicking statistical noise from CCD detectors and atmospheric interference
2. **One-pixel adversarial attacks**, where a genetic algorithm evolves over 200 generations to find the single pixel change most likely to fool the classifier

Both tests consistently favored the GCNNs. The best model, equivariant to D_16 (16-fold rotational symmetry plus reflections), achieved 95.52 ± 0.18% test-set accuracy on clean data and lost less than 6% even at 50% noise. Every GCNN proved less susceptible to one-pixel attacks than the CNN baseline.

## Why It Matters

Next-generation surveys will generate datasets orders of magnitude larger than humans can manually classify. The machine learning pipelines processing that data need to hold up under real observational conditions: atmospheric distortion, detector noise, processing artifacts. A classifier that crumbles when a single pixel gets corrupted is a liability.

The resilience shown here, especially against one-pixel perturbations simulating hardware detector failure, goes right at that problem.

On the AI side, this is a clean demonstration that **inductive bias** (encoding known physical symmetries into architecture) outperforms **data augmentation** (brute-forcing the model to learn symmetry from examples). The GCNN uses fewer parameters than a comparable CNN to achieve better performance because it isn't wasting capacity re-learning facts the physics already guarantees.

The principle extends well beyond astronomy. Wherever data has known symmetries, equivariant architectures offer a more efficient path than augmentation. The tradeoff is compute: the D_16 model required up to five hours of A100 training time versus two for the CNN baseline.

> GCNNs that encode rotational and reflectional symmetry into their architecture achieve 95.52% galaxy classification accuracy while maintaining resilience under realistic observational noise, showing that physics-informed architectural design beats brute-force data augmentation for astronomical imaging tasks.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work applies abstract group theory to practical astronomical classification, showing that encoding physical symmetries as architectural constraints produces measurably better AI performance on real observational data.

- **Impact on Artificial Intelligence:** The study provides a rigorous side-by-side benchmark showing that equivariant architectures outperform identically constructed standard CNNs on both accuracy and adversarial resilience, adding weight to symmetry-informed network design across image recognition domains.

- **Impact on Fundamental Interactions:** More accurate, noise-resistant galaxy morphology classification at scale supports the large-scale surveys that feed into measurements of cosmological structure formation and dark energy, fundamental physics questions requiring statistical samples of millions of galaxies.

- **Outlook and References:** Future work could extend these architectures to continuous symmetry groups like SO(2) and O(2), tackle multi-label morphology classification, or apply the approach to Rubin Observatory and Euclid data; the full codebase is available at github.com/snehjp2/GCNNMorphology and the paper appeared at the Machine Learning and the Physical Sciences Workshop at NeurIPS 2023.

## Original Paper Details
- **Title:** E(2) Equivariant Neural Networks for Robust Galaxy Morphology Classification
- **arXiv ID:** [arXiv:2311.01500](https://arxiv.org/abs/2311.01500)
- **Authors:** ["Sneh Pandya", "Purvik Patel", "Franc O", "Jonathan Blazek"]
- **Abstract:** We propose the use of group convolutional neural network architectures (GCNNs) equivariant to the 2D Euclidean group, $E(2)$, for the task of galaxy morphology classification by utilizing symmetries of the data present in galaxy images as an inductive bias in the architecture. We conduct robustness studies by introducing artificial perturbations via Poisson noise insertion and one-pixel adversarial attacks to simulate the effects of limited observational capabilities. We train, validate, and test GCNNs equivariant to discrete subgroups of $E(2)$ - the cyclic and dihedral groups of order $N$ - on the Galaxy10 DECals dataset and find that GCNNs achieve higher classification accuracy and are consistently more robust than their non-equivariant counterparts, with an architecture equivariant to the group $D_{16}$ achieving a $95.52 \pm 0.18\%$ test-set accuracy. We also find that the model loses $<6\%$ accuracy on a $50\%$-noise dataset and all GCNNs are less susceptible to one-pixel perturbations than an identically constructed CNN. Our code is publicly available at https://github.com/snehjp2/GCNNMorphology.
