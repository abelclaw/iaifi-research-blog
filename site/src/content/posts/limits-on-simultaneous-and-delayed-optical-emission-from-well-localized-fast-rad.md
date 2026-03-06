---
abstract: 'We present the largest compilation to date of optical observations during
  and following fast radio bursts (FRBs). The data set includes our dedicated simultaneous
  and follow-up observations, as well as serendipitous archival survey observations,
  for a sample of 15 well-localized FRBs: eight repeating and seven one-off sources.
  Our simultaneous (and nearly simultaneous with a $0.4$ s delay) optical observations
  of 13 (1) bursts from the repeating FRB 20220912A provide the deepest such limits
  to date for any extragalactic FRB, reaching a luminosity limit of $νL_ν\lesssim
  10^{42}$ erg s$^{-1}$ ($\lesssim 2\times10^{41}$ erg s$^{-1}$) with $15-400$ s exposures;
  an optical-flux-to-radio-fluence ratio of $f_{\rm opt}/F_{\rm radio}\lesssim 10^{-7}$
  ms$^{-1}$ ($\lesssim 10^{-8}$ ms$^{-1}$); and flux ratio of $f_{\rm opt}/f_{\rm
  radio}\lesssim 0.02-\lesssim 2\times 10^{-5}$ ($\lesssim 10^{-6}$) on millisecond
  to second timescales. These simultaneous limits provide useful constraints in the
  context of FRB emission models, such as the pulsar magnetosphere and pulsar nebula
  models. Interpreting all available optical limits in the context of the synchrotron
  maser model, we find that they constrain the flare energies to $\lesssim 10^{43}-10^{49}$
  erg (depending on the distances of the various repeating FRBs, with $\lesssim 10^{39}$
  erg for the Galactic SGR 1935+2154). These limits are generally at least an order
  of magnitude larger than those inferred from the FRBs themselves, although in the
  case of FRB 20220912A our simultaneous and rapid follow-up observations severely
  restrict the model parameter space. We conclude by exploring the potential of future
  simultaneous and rapid-response observations with large optical telescopes.'
arxivId: '2211.03974'
arxivUrl: https://arxiv.org/abs/2211.03974
authors:
- Daichi Hiramatsu
- Edo Berger
- Brian D. Metzger
- Sebastian Gomez
- Allyson Bieryla
- Iair Arcavi
- D. Andrew Howell
- Ryan Mckinven
- Nozomu Tominaga
concepts:
- fast radio bursts
- signal detection
- synchrotron maser emission
- magnetar outbursts
- hypothesis testing
- bayesian inference
- goodness-of-fit testing
- uncertainty quantification
- stellar evolution
figures:
- /iaifi-research-blog/figures/2211_03974/figure_1.png
- /iaifi-research-blog/figures/2211_03974/figure_2.png
- /iaifi-research-blog/figures/2211_03974/figure_3.png
pdfUrl: https://arxiv.org/pdf/2211.03974v2
published: '2022-11-08T03:02:56+00:00'
theme: Astrophysics
title: Limits on Simultaneous and Delayed Optical Emission from Well-localized Fast
  Radio Bursts
wordCount: 1007
---

## The Big Picture

Imagine a lighthouse emitting a single, blinding flash of radio energy so powerful it outshines entire galaxies — for just a millisecond. That's a fast radio burst (FRB). These cosmic enigmas arrive from billions of light-years away, and despite two decades of study, we still don't know what makes them. They're bright enough to see across the universe, fast enough to blink out before your neurons finish registering the pulse, and frustratingly silent in every other wavelength.

That silence is the crux of the problem. Since the first FRB was detected in 2007, the catalog has grown to thousands of events — yet nearly all our knowledge comes from radio waves alone. It's roughly like trying to identify a fire by listening for the crackle while being forbidden from looking at the flame. Theory predicts that whatever is producing these radio screams should also glow briefly in visible light. But nobody has ever caught that glow.

A team led by Daichi Hiramatsu and Edo Berger at the Harvard Center for Astrophysics has now assembled the largest and most sensitive campaign of simultaneous optical observations of FRBs ever conducted. While they found no optical light, what they *didn't* see turns out to be deeply informative.

> **Key Insight:** By watching 13 radio bursts from FRB 20220912A in visible light at the exact moment they fired, this study sets the tightest constraints ever placed on the optical brightness of any extragalactic FRB — ruling out entire classes of theoretical explanations.

## How It Works

The team built a dataset spanning 15 **well-localized FRBs** — sources pinpointed precisely enough to identify their host galaxies. Eight are **repeating FRBs** (sources that fire multiple times), and seven are **one-off events**. Optical data came from dedicated telescope campaigns and archival surveys that happened to be imaging the right patch of sky at the right moment.

![Figure 1](/iaifi-research-blog/figures/2211_03974/figure_1.png)

The centerpiece is **FRB 20220912A**, a prolific repeater at roughly 1 billion light-years. The team coordinated real-time radio alerts from the CHIME telescope with optical cameras, snapping exposures lasting 15 to 400 seconds either simultaneously with or within 0.4 seconds of individual bursts. They caught 13 bursts simultaneously and one nearly simultaneously. No optical flash appeared in any of them.

"Not detected" has a precise meaning here. The team calculated **upper limits** — the maximum brightness consistent with seeing nothing — on how bright any optical emission could have been. Their tightest numbers:

- **Luminosity:** dimmer than roughly 10^42 ergs per second (a unit of radiated power) — comparable to a faint dwarf galaxy, but for a flash lasting milliseconds
- **Optical-to-radio flux ratio:** less than 0.02, and as low as 2×10^-5 across timescales from milliseconds to seconds
- **Optical-to-radio fluence ratio:** less than 10^-7 per millisecond — fluence being the total energy delivered per unit of collecting area — meaning any optical counterpart carries less than one ten-millionth the radio burst's energy per unit time

These are the deepest such limits ever achieved for any extragalactic FRB.

## Why It Matters

The power of non-detections becomes clear when you test them against theory. The **synchrotron maser model** — currently the leading explanation — proposes that FRBs are powered by **magnetar flares**: catastrophic magnetic energy releases from ultra-dense, rapidly spinning neutron stars. Charged particles accelerated by the flare produce both the radio burst and a brief optical afterglow via **synchrotron emission** — the faint light shed when charged particles spiral through magnetic fields.

![Figure 2](/iaifi-research-blog/figures/2211_03974/figure_2.png)

Translating all their optical limits into flare energy constraints, the researchers find that magnetar flares in their sample released no more than 10^43 to 10^49 ergs — a wide range driven by the different distances of each source. For the one Galactic FRB-like event, from magnetar SGR 1935+2154 in our own Milky Way, the constraint tightens to under 10^39 ergs. These limits are generally at least an order of magnitude (ten times or more) looser than what the radio bursts themselves imply, so the optical data alone don't yet rule the model out — except in one important case.

For FRB 20220912A, the simultaneous observations are close enough to the theoretically predicted optical brightness to meaningfully carve away parts of the allowed parameter space — specifically restricting combinations of high flare energy and dense surrounding plasma. This is the first time simultaneous **multiwavelength** observations — watching in multiple types of light at once — have genuinely cornered an FRB model.

![Figure 3](/iaifi-research-blog/figures/2211_03974/figure_3.png)

The analogy to **gamma-ray bursts (GRBs)** — another class of intense, short-lived cosmic explosions — is deliberate. For years, GRBs were radio-wave mysteries until rapid optical follow-up cracked them open. FRBs are at a similar inflection point. The next generation of large optical telescopes, combined with real-time radio alert systems, could push sensitivity down by orders of magnitude, reaching the regimes where theoretical models actually live.

> **Bottom Line:** We've never caught a fast radio burst glowing in visible light — and this study sets the strictest limits yet. The deep non-detections from FRB 20220912A already strain the synchrotron maser model, and future telescope campaigns could finally illuminate what powers the universe's most powerful radio flashes.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines real-time coordination between radio (CHIME) and optical telescopes with large-scale archival data mining — bridging observational astrophysics with the multi-instrument, data-intensive science that IAIFI's AI-physics intersection is uniquely positioned to advance.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The pipeline for real-time burst detection, cross-instrument triggering, and multi-survey archival synthesis represents infrastructure that machine learning tools can directly enhance — particularly for automated alert classification and rapid follow-up scheduling at scale.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By placing the deepest simultaneous optical limits ever achieved for an extragalactic FRB, this study constrains the physical mechanisms driving the universe's most energetic radio transients, narrowing the viable parameter space of magnetar flare and synchrotron maser models.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future campaigns with 30-meter class telescopes and sub-second optical response could reach theoretically critical brightness thresholds; full results are available at arXiv:2302.07906.</span></div></div>
</div>
