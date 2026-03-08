---
abstract: Low-mass dark matter (DM) subhalos are pivotal in understanding the small-scale
  structure of the universe, thereby offering a sensitive method to discriminate between
  different cosmological models. In this study, we estimate the local number density
  of cold DM subhalos in the solar neighborhood, and demonstrate that their sparse
  distribution makes their detection via direct detection experiments highly improbable.
  However, it is plausible to expect that an $\mathcal{O}(1)$ number of subhalos could
  be detected by Paleo-detectors, a proposed new technique to look for DM by reading
  out damage tracks left by past DM interactions in minerals, due to their extended
  exposure times. Hence, we explore how Paleo-detectors can serve as effective probes
  for the properties of low-mass subhalos, $\mathcal{O}(10^{-5}-10^8) M_{\odot}$.
  We find that Paleo-detectors might be able to constrain certain regions of the subhalo
  mass-concentration relation (for subhalo masses of $10-10^4 M_\odot$ if DM has a
  mass of $\sim5$GeV). This is a new and complementary type of study that seeks to
  combine information from the particle nature of DM to that of small scale structures.
arxivId: '2504.13247'
arxivUrl: https://arxiv.org/abs/2504.13247
authors:
- Xiuyuan Zhang
- Lina Necib
- Denis Erkal
concepts:
- dark matter
- paleo-detectors
- subhalo mass function
- mass-concentration relation
- cosmological simulation
- signal detection
- monte carlo methods
- bayesian inference
- inverse problems
- neutrino detection
- cosmic microwave background
figures:
- /iaifi-research-blog/figures/2504_13247/figure_1.png
- /iaifi-research-blog/figures/2504_13247/figure_2.png
pdfUrl: https://arxiv.org/pdf/2504.13247v1
published: '2025-04-17T18:00:00+00:00'
theme: Astrophysics
title: 'Darkness in the Crust: Searching for the truly "Dark" Subhalos with Paleo-detectors'
wordCount: 1026
---

## The Big Picture

Imagine the Milky Way as a vast ocean, our solar system a tiny boat floating through it. Now imagine that ocean is filled with countless invisible icebergs: clumps of dark matter so small and so dark that no telescope can see them, no galaxy inhabits them, and no instrument we've built has ever detected their passage. These are **dark matter subhalos**, and they are one of the most basic predictions of our standard cosmological model. Whether they exist in the predicted numbers, with the predicted properties, could make or break our best theory of how the universe assembled itself.

The smallest subhalos, those lighter than a few thousand solar masses, leave no stars behind, bend light too weakly to detect, and are too subtle to disturb the faint stellar tracers astronomers use to map the galaxy. They are, in the most literal sense, invisible.

Yet if our models are correct, subhalos should be drifting through our solar neighborhood right now, passing through the Earth occasionally, leaving almost nothing behind. Almost nothing.

A new study by Xiuyuan Zhang, Lina Necib, and Denis Erkal argues that rocks, ancient and deeply buried, could be our best hope of catching these structures in the act.

> **Key Insight:** Traditional dark matter detectors would need to wait an astronomically unlikely 100 million years for a subhalo to fly through. Paleo-detectors, which read billion-year-old damage tracks in ancient minerals, naturally accumulate exactly that kind of exposure.

## How It Works

The researchers start with a sobering calculation. Using the **subhalo mass function** (a census of how many subhalos of each mass are expected in a Milky Way-like galaxy) they compute the **encounter rate**: how often a subhalo would pass through a detector on Earth. The answer is brutal: roughly 10⁻⁸ encounters per year. You would need to run a conventional detector for 100 million years to expect even one event.

**Paleo-detectors** flip the problem. Rather than building a sensitive instrument and waiting, the concept uses minerals that have been accumulating damage for hundreds of millions, even billions, of years as natural archives. The mechanism is simple:

- A dark matter particle scatters off a nucleus inside a crystal lattice
- The recoiling nucleus is knocked from its position, carving a nanometer-scale **damage track**
- Modern microscopy can read those tracks today, like fossilized particle physics experiments embedded in stone

![Figure 1](/iaifi-research-blog/figures/2504_13247/figure_1.png)

Over an exposure of roughly 10⁹ years, what was a 10⁻⁸ chance per year becomes a near-certain probability. Roughly one subhalo encounter could be recorded in a paleo-detector sample, turning the question from "can we ever see these?" to "what can we actually learn from them?"

The team models subhalos using **NFW profiles**, a standard description of how dark matter density rises steeply toward a halo's center. The key parameter is the **mass-concentration relation c(M)**, which describes how centrally concentrated a halo is as a function of its total mass. Different dark matter candidates predict different c(M) curves, especially at small masses where simulations and observations diverge. This makes c(M) a sensitive discriminant between cosmological models.


Their analysis spans 13 orders of magnitude in subhalo mass, from 10⁻⁵ to 10⁸ solar masses. They consider multiple dark matter particle masses and **cross-sections** (a measure of how readily a dark matter particle interacts with ordinary matter), examining both **spin-independent** interactions (where a particle's spin doesn't affect how it scatters) and **spin-dependent** ones (where it does). The central question: given a particular c(M) relation and particle properties, what signal would a paleo-detector array observe, and could a non-detection rule out certain models?

## Why It Matters

The result is a new kind of constraint. For subhalo masses between 10 and 10⁴ solar masses, a regime completely inaccessible to gravitational lensing, stellar stream analysis, or any other current probe, paleo-detectors could constrain the mass-concentration relation if dark matter has a mass around 5 GeV (roughly five times the proton mass, a relatively light candidate). That range is not yet excluded by current underground experiments like LZ or XENON, making this live, testable territory.


The paper also points toward a conceptually different kind of experiment: using a single detector to probe both the *particle* nature of dark matter and the *large-scale structure* predictions of **ΛCDM** (the standard cosmological model describing how dark matter clumps and builds structure across cosmic time). Until now, these questions have lived in separate experimental programs. Direct detection experiments ask: what are the microphysical properties of dark matter particles? Cosmological observations ask: how does dark matter cluster on small scales?

Paleo-detectors do both. They are sensitive to the flux of dark matter particles *and* the statistical distribution of subhalos passing through the solar neighborhood over cosmic time. A detected subhalo signature would constrain not just whether dark matter interacts with nuclei, but how the universe assembled its smallest structures billions of years ago.

The paleo-detector concept is still experimental. No one has demonstrated a full readout of nuclear damage tracks at the required sensitivity. But the physics case keeps getting stronger. Paleo-detectors aren't just dark matter detectors. They're cosmic archaeology tools.

> **Bottom Line:** Ancient minerals could carry a billion-year record of dark matter subhalo encounters, our only realistic shot at probing structure at mass scales far below anything telescopes can see, and at connecting particle physics directly to cosmological structure formation.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects particle physics and cosmology by showing that paleo-detectors can simultaneously probe the microphysical cross-section of dark matter and the small-scale structure predictions of ΛCDM in a single measurement.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The study motivates future machine learning approaches to analyze complex nanoscale track patterns in mineral samples and distinguish subhalo signals from background, a pattern-recognition challenge well-suited to advanced AI methods.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Paleo-detectors could constrain the dark matter mass-concentration relation for subhalo masses between 10 and 10⁴ solar masses, a regime completely inaccessible to any current astrophysical or terrestrial experiment.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will require advances in mineral readout technology and better simulations of small-scale structure; the full analysis appears at [arXiv:2504.13247](https://arxiv.org/abs/2504.13247).</span></div></div>
</div>
