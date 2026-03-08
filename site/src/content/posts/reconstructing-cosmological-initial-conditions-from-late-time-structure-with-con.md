---
abstract: 'We present a method to reconstruct the initial linear-regime matter density
  field from the late-time non-linearly evolved density field in which we channel
  the output of standard first-order reconstruction to a convolutional neural network
  (CNN). Our method shows dramatic improvement over the reconstruction of either component
  alone. We show why CNNs are not well-suited for reconstructing the initial density
  directly from the late-time density: CNNs are local models, but the relationship
  between initial and late-time density is not local. Our method leverages standard
  reconstruction as a preprocessing step, which inverts bulk gravitational flows sourced
  over very large scales, transforming the residual reconstruction problem from long-range
  to local and making it ideally suited for a CNN. We develop additional techniques
  to account for redshift distortions, which warp the density fields measured by galaxy
  surveys. Our method improves the range of scales of high-fidelity reconstruction
  by a factor of 2 in wavenumber above standard reconstruction, corresponding to a
  factor of 8 increase in the number of well-reconstructed modes. In addition, our
  method almost completely eliminates the anisotropy caused by redshift distortions.
  As galaxy surveys continue to map the Universe in increasingly greater detail, our
  results demonstrate the opportunity offered by CNNs to untangle the non-linear clustering
  at intermediate scales more accurately than ever before.'
arxivId: '2207.12511'
arxivUrl: https://arxiv.org/abs/2207.12511
authors:
- Christopher J. Shallue
- Daniel J. Eisenstein
concepts:
- convolutional networks
- inverse problems
- density field reconstruction
- baryon acoustic oscillations
- cosmological simulation
- redshift-space distortions
- regression
- dark energy
- superresolution
- dark matter
- optimal transport
figures:
- /iaifi-research-blog/figures/2207_12511/figure_1.png
- /iaifi-research-blog/figures/2207_12511/figure_2.png
- /iaifi-research-blog/figures/2207_12511/figure_3.png
pdfUrl: https://arxiv.org/pdf/2207.12511v2
published: '2022-07-25T20:14:22+00:00'
theme: Astrophysics
title: Reconstructing Cosmological Initial Conditions from Late-Time Structure with
  Convolutional Neural Networks
wordCount: 1201
---

## The Big Picture

Imagine trying to reconstruct the original shape of a crumpled piece of paper, but you can only look at the crumpled version, 14 billion years after it was folded. That's roughly the challenge cosmologists face when studying the universe's large-scale structure. The matter we observe today (sprawling filaments of galaxies, vast cosmic voids, dense clusters) has been warped and scrambled by gravity for the entirety of cosmic history. Hidden beneath that complexity are the initial conditions set in place just 380,000 years after the Big Bang.

Recovering those initial conditions is the whole game. They encode information about **baryon acoustic oscillations (BAO)**, ancient sound waves that rippled through the hot plasma of the early universe and froze in place when electrons and protons first combined into neutral atoms, a moment cosmologists call "recombination." These frozen ripples act as a cosmic ruler, letting astronomers measure the universe's expansion history and probe the nature of dark energy. But gravity has smeared out those clean signatures over billions of years. The sharper the picture we can reconstruct of the initial universe, the better our dark energy constraints become.

Christopher Shallue and Daniel Eisenstein at the Center for Astrophysics | Harvard & Smithsonian have developed a hybrid approach that pairs classical physics-based reconstruction with a convolutional neural network. Their method recovers twice as many modes (distinct spatial scales) of the initial density field as previous methods, corresponding to eight times more well-reconstructed information.

> **Key Insight:** The trick isn't replacing physics with AI. It's using physics to reshape the problem so AI can actually solve it. Standard reconstruction handles long-range gravitational flows; the neural network then cleans up the local residuals.

## How It Works

Training a neural network to map the late-time density field directly back to the initial one fails for a geometric reason. **CNNs are local models**: they predict from a *receptive field*, the finite window of data the network can "see" at once. But the relationship between initial and late-time density is emphatically non-local. A galaxy observed today may have traveled hundreds of megaparsecs (roughly 3.26 million light-years each) from its birthplace, dragged by gravitational flows spanning enormous scales. No finite window captures that.

![Figure 1](/iaifi-research-blog/figures/2207_12511/figure_1.png)

The solution is a two-stage pipeline:

- **Standard reconstruction**, a physics-based algorithm grounded in linear perturbation theory that estimates and reverses large-scale bulk flows, explicitly inverting the long-range gravitational displacements that defeat direct CNN approaches.
- **CNN residual correction**: after standard reconstruction restores large-scale structure, medium-scale non-linearities remain as residual errors. These residuals *are* local, caused by smaller-scale clustering rather than long-range bulk flows. The network learns to predict corrections at intermediate scales (roughly 0.1–0.6 *h* Mpc⁻¹), using 3D convolutions on cubic patches of the density field.

One more complication: **redshift distortions**. Galaxy distances are inferred from their redshifts (the stretching of light as a galaxy recedes), but peculiar velocities, a galaxy's own motion independent of cosmic expansion, corrupt those measurements. The result is an asymmetric warping of the density field along the line of sight. Shallue and Eisenstein developed techniques to supply the network with explicit line-of-sight direction information, enabling it to learn and correct these anisotropic distortions alongside everything else.

![Figure 2](/iaifi-research-blog/figures/2207_12511/figure_2.png)

## Why It Matters

Standard reconstruction achieves high-fidelity recovery up to wavenumber *k* ≈ 0.2 *h* Mpc⁻¹. The CNN hybrid pushes that to *k* ≈ 0.4 *h* Mpc⁻¹, a factor of 2 in wavenumber. Because the number of independent modes in a 3D volume scales as *k*³, that doubling corresponds to an eightfold increase in well-reconstructed modes. Not a marginal improvement, but a qualitative jump in how much cosmological information becomes accessible.

![Figure 3](/iaifi-research-blog/figures/2207_12511/figure_3.png)

The method also nearly eliminates redshift-distortion anisotropy, making the reconstructed field effectively isotropic. Measurements no longer depend on which direction you're probing. For precision cosmology, that directional independence matters as much as the raw resolution gains.

Surveys like DESI and Euclid are now mapping the universe at unprecedented scale, and reconstruction quality is becoming a bottleneck for BAO science. Methods that reliably recover signals at smaller scales will directly tighten constraints on the dark energy equation of state and could reveal **primordial non-Gaussianity**, subtle deviations from random initial fluctuations that may fingerprint the physics of cosmic inflation.

There's a broader lesson here, too. Neural networks carry architectural biases, and locality is the CNN's defining constraint. The approach in this paper (using domain-specific physics to transform a non-local problem into a locally tractable one) points toward a general strategy for hybrid AI-physics methods across cosmology and other fields.

> **Bottom Line:** By using classical reconstruction as a preprocessing step, this hybrid method puts eightfold more cosmological information within reach. It's a clean example of how matching the right tool to the right problem beats either AI or physics working alone.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work shows that domain knowledge in gravitational physics, specifically the locality structure of bulk flows, is essential for applying machine learning effectively in cosmological data analysis, a core theme of the IAIFI mission.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The paper provides a rigorous explanation of why CNNs fail on long-range inference tasks and offers a principled preprocessing strategy that transforms such problems into locally tractable ones, a lesson applicable well beyond cosmology.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By recovering eight times more well-reconstructed cosmological modes and nearly eliminating redshift-distortion anisotropy, the method improves the precision of BAO measurements used to probe dark energy and the expansion history of the universe.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work can extend this approach to realistic galaxy catalogs with survey masks, noise, and galaxy bias, and may push performance to even smaller scales. The paper is available as [arXiv:2207.12511](https://arxiv.org/abs/2207.12511) and was published in MNRAS 520 (2023).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Reconstructing Cosmological Initial Conditions from Late-Time Structure with Convolutional Neural Networks</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2207.12511</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Christopher J. Shallue", "Daniel J. Eisenstein"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">We present a method to reconstruct the initial linear-regime matter density field from the late-time non-linearly evolved density field in which we channel the output of standard first-order reconstruction to a convolutional neural network (CNN). Our method shows dramatic improvement over the reconstruction of either component alone. We show why CNNs are not well-suited for reconstructing the initial density directly from the late-time density: CNNs are local models, but the relationship between initial and late-time density is not local. Our method leverages standard reconstruction as a preprocessing step, which inverts bulk gravitational flows sourced over very large scales, transforming the residual reconstruction problem from long-range to local and making it ideally suited for a CNN. We develop additional techniques to account for redshift distortions, which warp the density fields measured by galaxy surveys. Our method improves the range of scales of high-fidelity reconstruction by a factor of 2 in wavenumber above standard reconstruction, corresponding to a factor of 8 increase in the number of well-reconstructed modes. In addition, our method almost completely eliminates the anisotropy caused by redshift distortions. As galaxy surveys continue to map the Universe in increasingly greater detail, our results demonstrate the opportunity offered by CNNs to untangle the non-linear clustering at intermediate scales more accurately than ever before.</span></div></div>
</div>
