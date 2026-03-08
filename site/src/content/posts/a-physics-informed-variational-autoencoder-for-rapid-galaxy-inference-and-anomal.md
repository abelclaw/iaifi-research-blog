---
abstract: The Vera C. Rubin Observatory is slated to observe nearly 20 billion galaxies
  during its decade-long Legacy Survey of Space and Time. The rich imaging data it
  collects will be an invaluable resource for probing galaxy evolution across cosmic
  time, characterizing the host galaxies of transient phenomena, and identifying novel
  populations of anomalous systems. To facilitate these studies, we introduce a convolutional
  variational autoencoder trained to estimate the redshift, stellar mass, and star-formation
  rates of galaxies from multi-band imaging data. We train and test our physics-informed
  CVAE on a spectroscopic sample of $\sim$26,000 galaxies within $z<1$ imaged through
  the Dark Energy Camera Legacy Survey. We show that our model can infer redshift
  and stellar mass more accurately than the latest image-based self-supervised learning
  approaches, and is >100x faster than more computationally-intensive SED-fitting
  techniques. Using a small sample of Green Pea and Red Spiral galaxies reported in
  the literature, we further demonstrate how this CVAE can be used to rapidly identify
  rare galaxy populations and interpret what makes them unique.
arxivId: '2312.16687'
arxivUrl: https://arxiv.org/abs/2312.16687
authors:
- Alexander Gagliano
- V. Ashley Villar
concepts:
- variational autoencoders
- physics-informed neural networks
- disentangled representations
- anomaly detection
- convolutional networks
- galaxy classification
- photometric redshift estimation
- out-of-distribution detection
- representation learning
- uncertainty quantification
- self-supervised learning
- simulation-based inference
figures:
- /iaifi-research-blog/figures/2312_16687/figure_1.png
- /iaifi-research-blog/figures/2312_16687/figure_1.png
- /iaifi-research-blog/figures/2312_16687/figure_2.png
- /iaifi-research-blog/figures/2312_16687/figure_2.png
- /iaifi-research-blog/figures/2312_16687/figure_3.png
- /iaifi-research-blog/figures/2312_16687/figure_3.png
pdfUrl: https://arxiv.org/pdf/2312.16687v1
published: '2023-12-27T18:59:59+00:00'
theme: Astrophysics
title: A Physics-Informed Variational Autoencoder for Rapid Galaxy Inference and Anomaly
  Detection
wordCount: 1218
---

## The Big Picture

Imagine trying to sort and analyze the entire population of a continent, not just counting people, but understanding their age, health, occupation, and life history, from aerial photographs alone. That's roughly the challenge facing astronomers as the Vera C. Rubin Observatory prepares to begin its decade-long Legacy Survey of Space and Time (LSST). When it comes online, it will photograph nearly **20 billion galaxies**. Twenty billion. That's more galaxies than there are seconds in 630 years.

Traditional methods for extracting physical properties from galaxy images are too slow for this scale. The standard approach, **SED fitting**, works by matching a galaxy's brightness across many colors of light to known templates, reconstructing a "color fingerprint" that reveals what kinds of stars a galaxy contains. It's thorough, but so computationally demanding that running it on billions of galaxies would take centuries.

Machine learning approaches that skip the physics trade away interpretability: they tell you what a galaxy looks like, but not what it *is*.

Alexander Gagliano and V. Ashley Villar at IAIFI have built a neural network that learns to see galaxies the way physicists do, storing fundamental properties like mass and distance directly in its internal working memory.

> **Key Insight:** By forcing a neural network's hidden representation to encode physical quantities (redshift, stellar mass, star-formation rate), researchers can do in milliseconds what conventional tools take minutes to accomplish, while also uncovering rare, exotic galaxies hiding in plain sight.

## How It Works

The architecture at the heart of this work is a **convolutional variational autoencoder (CVAE)**, a neural network that compresses data into a compact representation and then reconstructs it. Think of it as a game of telephone: the encoder reduces a galaxy's image to just a few numbers, and the decoder tries to rebuild the original from those numbers alone.

What makes this CVAE different is what those numbers are *forced* to mean. Most autoencoders let the network invent whatever abstract features it finds useful. Here, four of the five **latent dimensions** (the compressed numbers encoding everything the network "knows" about a galaxy) must correspond to measurable physical quantities: orientation, **redshift** (a proxy for distance), **stellar mass**, and **star-formation rate**. A fifth dimension is left free to capture any remaining structure.

![Figure 1](figure:1)

Three components make up the **loss function**, the mathematical score the network minimizes during training:

1. **Reconstruction quality**: How well does the decoded image match the original, measured pixel by pixel.
2. **Latent regularization**: The free fifth dimension is kept well-behaved using **KL divergence**, a statistical penalty that prevents the representation from collapsing into meaningless noise.
3. **Physical accuracy**: The four physics-constrained dimensions are penalized whenever they disagree with spectroscopically measured values from the training catalog.

The team trained on roughly 26,000 galaxies imaged in three optical bands (g, r, z) from the Dark Energy Camera Legacy Survey (DECaLS), all within redshift z < 1. Images were preprocessed with nonlinear normalization to handle the enormous dynamic range of galaxy brightnesses, then resized to 69×69 pixels. Training ran for 1,000 epochs on two Nvidia A100 GPUs.

## Why It Matters

On predicting redshift from images, the physics-informed CVAE achieves an R² of **0.83**, explaining 83% of the variance in true values. For stellar mass, it hits **0.75**. The best prior image-based method scores only 0.71 and 0.66 on those same tasks. The new approach beats every image-based competitor in the comparison.

Speed is where the gap gets serious. SED fitting typically processes a single galaxy in seconds to minutes. The CVAE handles the same task more than 100 times faster, making it practical to run on the billions of galaxies LSST will deliver.

But the most useful capability may be anomaly detection. Because the latent space is structured around physics, objects that don't fit known populations stand out geometrically. The researchers tested this with two exotic types: **Green Pea galaxies** (tiny, intensely star-forming systems) and **Red Spiral galaxies** (spirals that have inexplicably stopped forming stars). Both populations, absent from the training set, cluster in distinctive regions of latent space. The model doesn't just flag them as unusual; it shows *what* makes them unusual, pointing to exactly which physical dimensions deviate from the norm.

The broader lesson here is that physics can be embedded into the geometry of machine learning representations, not just bolted on afterward. Similar ideas could apply to particle physics detectors, gravitational wave observatories, or any domain where the data are images and the questions concern underlying physical parameters.

Open questions remain. The model currently works within z < 1; extending to higher redshifts, where galaxy morphologies are less regular and training data is scarcer, will require careful work. And the fifth free latent dimension captures something real. Interpreting that residual structure could itself lead to new science.

> **Bottom Line:** A physics-informed variational autoencoder extracts galaxy properties from images more accurately than competing machine learning approaches, more than 100 times faster than conventional SED fitting, and identifies rare galaxy populations by their position in a physically meaningful latent space. For a survey of 20 billion galaxies, that kind of speed and interpretability is not optional.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work fuses deep learning architecture design with physical domain knowledge, encoding astrophysical observables (redshift, stellar mass, star-formation rate) into the latent geometry of a convolutional neural network. It is a concrete example of AI and physics informing each other at the model level.

- **Impact on Artificial Intelligence:** The physics-informed loss function achieves better regression performance than purely data-driven self-supervised approaches, suggesting that domain-constrained representation learning is a productive direction for scientific machine learning well beyond astrophysics.

- **Impact on Fundamental Interactions:** Rapid, interpretable characterization of galaxy populations at scale creates new opportunities for studying galaxy evolution across cosmic time and identifying rare systems that challenge existing formation models.

- **Outlook and References:** Future work will extend coverage to higher redshifts and investigate the scientific content of the free latent dimension. The method and trained models are publicly available. The paper appeared at the Machine Learning and the Physical Sciences Workshop at NeurIPS 2023: [arXiv:2312.16687](https://arxiv.org/abs/2312.16687).

## Original Paper Details
- **Title:** A Physics-Informed Variational Autoencoder for Rapid Galaxy Inference and Anomaly Detection
- **arXiv ID:** [arXiv:2312.16687](https://arxiv.org/abs/2312.16687)
- **Authors:** Alexander Gagliano, V. Ashley Villar
- **Abstract:** The Vera C. Rubin Observatory is slated to observe nearly 20 billion galaxies during its decade-long Legacy Survey of Space and Time. The rich imaging data it collects will be an invaluable resource for probing galaxy evolution across cosmic time, characterizing the host galaxies of transient phenomena, and identifying novel populations of anomalous systems. To facilitate these studies, we introduce a convolutional variational autoencoder trained to estimate the redshift, stellar mass, and star-formation rates of galaxies from multi-band imaging data. We train and test our physics-informed CVAE on a spectroscopic sample of ~26,000 galaxies within z<1 imaged through the Dark Energy Camera Legacy Survey. We show that our model can infer redshift and stellar mass more accurately than the latest image-based self-supervised learning approaches, and is >100x faster than more computationally-intensive SED-fitting techniques. Using a small sample of Green Pea and Red Spiral galaxies reported in the literature, we further demonstrate how this CVAE can be used to rapidly identify rare galaxy populations and interpret what makes them unique.
