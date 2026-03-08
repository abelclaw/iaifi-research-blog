---
abstract: Flatbands emerge from a myriad of structures such as Landau levels, Lieb
  and Kagome lattices, linegraphs, and more recently moire superlattices. They enable
  unique properties including slow light in photonics, correlated phases in electronics,
  and supercollimation in both systems. Despite these intense parallel efforts, flatbands
  have never been shown to affect the core light-matter interaction between electrons
  and photons, which is limited by a dimensionality mismatch. Here, we reveal that
  a photonic flatband can overcome this mismatch between localized electrons and extended
  photons and thus remarkably boost their light-matter interaction. We design flatband
  resonances in a silicon-on-insulator photonic crystal slab to control and enhance
  the radiation emission from free electrons by tuning their trajectory and velocity.
  In particular, we record a 100-fold radiation enhancement from the conventional
  diffraction-enabled Smith-Purcell radiation, and show the potential of our approach
  to achieve $10^6$-fold enhancements and beyond. The enhancement also enables us
  to perform polarization shaping of free electron radiation from multiple flatbands
  and demonstrate an approach to measure photonic bands via angle-resolved electron-beam
  measurements. Our results suggest flatbands as ideal test beds for strong light-electron
  interaction in various systems, with particular relevance for efficient and compact
  free-electron light sources and accelerators.
arxivId: '2110.03550'
arxivUrl: https://arxiv.org/abs/2110.03550
authors:
- Yi Yang
- Charles Roques-Carmes
- Steven E. Kooi
- Haoning Tang
- Justin Beroz
- Eric Mazur
- Ido Kaminer
- John D. Joannopoulos
- Marin Soljačić
concepts:
- photonic flatband resonances
- free-electron radiation enhancement
- smith-purcell radiation
- photonic crystal slab
- momentum mismatch
- phase transitions
- signal detection
- spectral methods
- crystal structure
- symmetry breaking
figures:
- /iaifi-research-blog/figures/2110_03550/figure_1.png
- /iaifi-research-blog/figures/2110_03550/figure_1.png
- /iaifi-research-blog/figures/2110_03550/figure_2.png
- /iaifi-research-blog/figures/2110_03550/figure_2.png
- /iaifi-research-blog/figures/2110_03550/figure_3.png
- /iaifi-research-blog/figures/2110_03550/figure_3.png
pdfUrl: https://arxiv.org/pdf/2110.03550v1
published: '2021-10-07T15:16:15+00:00'
theme: Foundational AI
title: Observation of enhanced free-electron radiation from photonic flatband resonances
wordCount: 1038
---

## The Big Picture

Imagine trying to have a conversation in a crowded stadium where your voice reaches only a single seat. That's the problem physicists face when getting electrons to talk to light. A free electron, a tiny point-like particle, wants to emit a photon, but photons are sprawling wave-like entities that extend across space.

The trouble is a shape mismatch: the electron is a pinpoint, the photon is a wave, and they can only truly "meet" in one narrow way at a time. For decades, this mismatch has capped how efficiently electrons and photons interact, limiting everything from compact X-ray sources to particle accelerators.

A team at MIT, Harvard, and Technion found a way around this limitation using a concept borrowed from exotic condensed matter physics: the **flatband**. Think of it this way: hundreds of different light waves all vibrate at exactly the same frequency, like a crowd all humming the same note regardless of where they're sitting. By engineering these flatband resonances into a specially patterned silicon chip, the team coaxed free electrons into radiating light at a rate 100 times greater than the conventional benchmark. Theory suggests enhancements of a million-fold or more are within reach.

> **Key Insight:** A photonic flatband provides a continuum of modes that perfectly match the momentum of free electrons across all transverse directions simultaneously, converting a hopelessly inefficient point interaction into a sweeping line interaction and vastly boosting light emission.

## How It Works

Start with the two classic ways electrons emit light. **Cherenkov radiation** occurs when a charged particle moves faster than light in a medium, the electromagnetic equivalent of a sonic boom. **Smith-Purcell radiation** occurs when an electron skims over a periodic grating, causing its near-field to diffract and radiate. Both effects are real and useful, but share a deep inefficiency.

At any given frequency, the matching condition (where the electron's motion and the light wave's rhythm must align) is satisfied only at a single isolated point in **momentum space**, the mathematical space describing all possible directions and wavelengths of light waves. Most of the electron's potential to couple to light goes untapped.

Here's the trick. **Flatbands**, photonic modes whose frequency is nearly constant across a wide range of momenta, replace that needle-and-eye geometry with something far more accommodating. In a flatband, a broad continuum of photonic modes all sit at the same frequency simultaneously. When an electron's momentum surface sweeps through this flat region, it intersects not a point but an entire line of modes. The shape mismatch disappears.

![Figure 1](figure:1)

To build this in hardware, the team designed a **silicon-on-insulator photonic crystal slab**: a thin silicon layer patterned with a precise array of microscopic holes, atop a silica substrate. By carefully engineering the hole geometry, they created flatband resonances where the **group velocity** (the speed at which energy travels through the material) nearly vanishes and the **density of states** spikes sharply.

They then tuned the radiation by:

- Varying the **electron velocity** to satisfy the phase-matching condition at the flatband frequency
- Adjusting the **twist angle** between the electron beam trajectory and the crystal lattice orientation
- Selecting among multiple flatbands to access different radiation polarizations

![Figure 2](figure:2)

The experimental setup fired electron beams from a scanning electron microscope at grazing incidence over the photonic crystal chip and collected the emitted light. Compared to conventional Smith-Purcell radiation from a plain grating, flatband-enhanced emission was **100 times brighter**. Theoretical modeling, extrapolating to optimized device geometries, projects enhancements reaching 10⁶ or higher.

The team also used the electron beam itself as a probe. By mapping the angle-resolved emission spectrum (measuring how light is emitted at different angles as electron speed changes) they reconstructed the photonic band structure of the crystal. This technique works where conventional optical measurements can't easily reach, opening a new window onto how light propagates through complex materials.

![Figure 4](figure:4)

## Why It Matters

Free electrons interacting with photons are central to technologies from medical imaging to materials science. Electron microscopes use this interaction to probe matter at atomic scales. Free-electron lasers use it to generate brilliant X-ray beams for studying proteins and chemical reactions.

Compact light sources based on Smith-Purcell radiation have long been proposed for terahertz and X-ray generation, but weak emission has held them back. Boosting that emission by factors of millions, using a chip-scale photonic crystal rather than a room-sized accelerator hall, would change the game.

The same flatband approach applies to **dielectric laser accelerators**, devices that use light waves to push electrons to higher energies. The coupling efficiency in those devices faces the identical shape mismatch this paper addresses. The ability to shape free-electron radiation polarization through multiple flatbands also points toward new forms of structured light generation, produced by routing electrons over engineered crystal regions.

The researchers frame flatbands explicitly as "ideal test beds for strong light-electron interaction," and the work invites exploration of these resonances in two-dimensional materials, **moiré superlattices** (atomically thin layers twisted against each other to create new electronic patterns), and other photonic systems where flatbands take on unusual properties.

> **Bottom Line:** By harnessing photonic flatband resonances in a silicon chip, MIT and Harvard researchers achieved a 100-fold enhancement of free-electron light emission, with theory pointing toward million-fold gains, opening new possibilities for how electrons and photons can be coupled in compact, chip-integrated devices.

## IAIFI Research Highlights

- **Interdisciplinary Research Achievement:** This work connects condensed matter physics (flatbands in Kagome and moiré systems), photonics (photonic crystal engineering), and accelerator science (free-electron radiation), showing that a concept from quantum materials can reshape electron-photon coupling on a silicon chip.

- **Impact on Artificial Intelligence:** The experimental and theoretical frameworks developed here, including angle-resolved electron-beam band mapping, create new data-rich platforms for training AI models to design and optimize photonic structures for target emission properties.

- **Impact on Fundamental Interactions:** The experiment directly tests a long-standing prediction about the dimensionality mismatch in light-matter coupling, converting a theoretical point degeneracy into a line degeneracy via flatband engineering and measuring the resulting radiation enhancement.

- **Outlook and References:** Future work targets the predicted 10⁶-fold enhancement regime using optimized flatband geometries, with direct implications for chip-scale free-electron lasers and dielectric particle accelerators. The paper is available at [arXiv:2110.03550](https://arxiv.org/abs/2110.03550).
