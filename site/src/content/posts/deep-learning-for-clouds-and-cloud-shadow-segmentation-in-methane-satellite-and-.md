---
abstract: 'Effective cloud and cloud shadow detection is a critical prerequisite for
  accurate retrieval of concentrations of atmospheric methane (CH4) or other trace
  gases in hyperspectral remote sensing. This challenge is especially pertinent for
  MethaneSAT, a satellite mission launched in March 2024, to fill a significant data
  gap in terms of resolution, precision and swath between coarse-resolution global
  mappers and fine-scale point-source imagers of methane, and for its airborne companion
  mission, MethaneAIR. MethaneSAT delivers hyperspectral data at an intermediate spatial
  resolution (approx. 100 x 400, m), whereas MethaneAIR provides even finer resolution
  (approx. 25 m), enabling the development of highly detailed maps of concentrations
  that enable quantification of both the sources and rates of emissions. In this study,
  we use machine learning methods to address the cloud and cloud shadow detection
  problem for sensors with these high spatial resolutions. Cloud and cloud shadows
  in remote sensing data need to be effectively screened out as they bias methane
  retrievals in remote sensing imagery and impact the quantification of emissions.
  We deploy and evaluate conventional techniques-including Iterative Logistic Regression
  (ILR) and Multilayer Perceptron (MLP)-with advanced deep learning architectures,
  namely U-Net and a Spectral Channel Attention Network (SCAN) method. Our results
  show that conventional methods struggle with spatial coherence and boundary definition,
  affecting the detection of clouds and cloud shadows. Deep learning models substantially
  improve detection quality: U-Net performs best in preserving spatial structure,
  while SCAN excels at capturing fine boundary details... Our data and code is publicly
  available at: https://doi.org/10.7910/DVN/IKLZOJ'
arxivId: '2509.19665'
arxivUrl: https://arxiv.org/abs/2509.19665
authors:
- Manuel Perez-Carrasco
- Maya Nasr
- Sebastien Roche
- Chris Chan Miller
- Zhan Zhang
- Core Francisco Park
- Eleanor Walker
- Cecilia Garraffo
- Douglas Finkbeiner
- Sasha Ayvazov
- Jonathan Franklin
- Bingkun Luo
- Xiong Liu
- Ritesh Gautam
- Steven Wofsy
concepts:
- convolutional networks
- hyperspectral segmentation
- attention mechanisms
- methane remote sensing
- ensemble methods
- classification
- spectral channel attention
- feature extraction
- transfer learning
- semi-supervised learning
- superresolution
figures:
- /iaifi-research-blog/figures/2509_19665/figure_1.png
- /iaifi-research-blog/figures/2509_19665/figure_2.png
- /iaifi-research-blog/figures/2509_19665/figure_3.png
pdfUrl: https://arxiv.org/pdf/2509.19665v3
published: '2025-09-24T00:49:52+00:00'
theme: Foundational AI
title: Deep Learning for Clouds and Cloud Shadow Segmentation in Methane Satellite
  and Airborne Imaging Spectroscopy
wordCount: 996
---

## The Big Picture

Imagine trying to photograph a gas leak through a foggy window. The fog doesn't just obscure the view — it distorts the light, creating false signals that could convince you the leak is somewhere it isn't. That's the problem facing satellites tasked with tracking one of climate change's most potent villains: methane.

Methane packs more than 80 times the warming punch of carbon dioxide over its first two decades in the atmosphere. Cutting methane emissions is one of the fastest levers we have for slowing climate change in the near term — which is why over 150 countries signed the Global Methane Pledge to cut emissions 30% by 2030.

Enforcing that pledge requires knowing exactly where methane is leaking, and in what quantities. That requires satellites. And satellites have a cloud problem.

When clouds or their shadows fall across a methane-sensing instrument, they don't just block the signal — they corrupt it, introducing false readings that can make clean sky look like a methane hotspot, or vice versa. A team of researchers from Harvard, the Environmental Defense Fund, and the Universidad de Concepción tackled this problem head-on, training **deep learning models** — AI systems that learn to recognize patterns from labeled examples — to identify and filter out clouds and shadows in data from MethaneSAT and its airborne sibling, MethaneAIR. They achieved processing speeds of 4.1 milliseconds per 1,000 km² while meaningfully outperforming traditional detection methods.

> **Key Insight:** Clouds and cloud shadows don't just hide methane data — they actively corrupt it, and deep learning can screen them out fast enough for real-world satellite operations, unlocking more accurate global emission tracking.

## How It Works

MethaneSAT, launched in March 2024, operates at roughly 100 × 400 meters per pixel, covering a 220-kilometer swath. MethaneAIR, its airborne counterpart used for algorithm development and validation, offers finer detail at around 25 meters per pixel. Both instruments capture **hyperspectral data** — hundreds of narrow wavelength bands across the shortwave infrared, where methane absorbs strongly.

That spectral richness is what makes precise methane retrieval possible. It's also what makes cloud contamination so insidious: clouds and shadows distort the signal differently across wavelengths, leaving distinct spectral signatures that rule-based detection methods miss.

![Figure 1](/iaifi-research-blog/figures/2509_19665/figure_1.png)

The researchers benchmarked four machine learning approaches. The conventional methods — **Iterative Logistic Regression (ILR)** and **Multilayer Perceptron (MLP)** — classify pixels one at a time without considering spatial context. These pixel-by-pixel approaches struggle at cloud edges, where the transition is gradual, producing patchy, inconsistent masks.

The deep learning architectures fared far better:

- **U-Net** — a neural network originally developed for medical image segmentation that analyzes full images rather than individual pixels — excels at preserving spatial structure. By passing information both down (to extract features) and back up (to reconstruct spatial detail), it produces clean, coherent masks that respect the physical extent of cloud systems.
- **SCAN (Spectral Channel Attention Network)** applies **attention mechanisms** — a technique that lets the model focus on the most informative inputs and downweight the rest — to the spectral dimension, learning which wavelength bands carry the strongest signal for each pixel. Where U-Net wins on spatial coherence, SCAN wins on boundary sharpness. Notably, SCAN outperforms U-Net specifically on MethaneSAT data, suggesting that coarser spatial resolution makes spectral discrimination more important than spatial reasoning.

The researchers then combined both models using a **convolutional ensemble** — a small neural network trained to intelligently merge U-Net and SCAN predictions. This ensemble achieved the best results on both platforms: an **F1 score** — a standard detection accuracy measure that balances catching real clouds against falsely flagging clear sky — of 78.50% (±3.08%) on MethaneAIR and 78.80% (±1.28%) on MethaneSAT. Against conventional methods, that represents improvements of 2% and 10% respectively. The larger gain on MethaneSAT highlights just how much conventional approaches struggled with the satellite's lower resolution.

![Figure 2](/iaifi-research-blog/figures/2509_19665/figure_2.png)

## Why It Matters

The immediate payoff is operational. A 4.1-millisecond processing time per 1,000 square kilometers means this system can keep pace with satellite data volumes without becoming a bottleneck. MethaneSAT covers massive stretches of oil and gas basins and agricultural regions globally — screening that data for clouds in near-real-time is a prerequisite for everything downstream, from emission maps to regulatory accountability reports.

The deeper contribution is methodological. This work establishes that different deep learning architectures encode different types of information about hyperspectral scenes — U-Net captures geometry, SCAN captures spectral identity — and that combining them recovers signal that neither captures alone. That principle extends well beyond methane: any mission doing gas retrieval from hyperspectral data faces the same cloud contamination problem. With publicly released code and labeled datasets, this pipeline provides a reusable foundation for the next generation of hyperspectral missions.

![Figure 3](/iaifi-research-blog/figures/2509_19665/figure_3.png)

> **Bottom Line:** By pairing spatial and spectral deep learning architectures in an ensemble, this team cut cloud contamination errors by up to 10% over conventional methods while achieving real-time inference speeds — clearing a critical obstacle between satellite methane data and the global emissions accounting that climate pledges demand.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work applies deep learning architectures from computer vision — U-Net and attention-based networks — to a geophysics problem with direct climate policy implications, demonstrating how AI methods generalize from medical imaging to atmospheric remote sensing.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The study provides a systematic comparison of pixel-wise, fully convolutional, and spectral-attention architectures on hyperspectral segmentation tasks, showing that ensembles combining spatial and spectral inductive biases outperform any single architecture.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Accurate cloud masking directly enables high-fidelity retrieval of atmospheric methane concentrations, improving humanity's ability to monitor and quantify one of the most significant greenhouse gas contributors to climate forcing.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work could extend these models to additional trace gases and next-generation hyperspectral missions; data and code are publicly available at https://doi.org/10.7910/DVN/IKLZOJ, and the paper is submitted to IEEE Transactions on Geoscience and Remote Sensing.</span></div></div>
</div>
