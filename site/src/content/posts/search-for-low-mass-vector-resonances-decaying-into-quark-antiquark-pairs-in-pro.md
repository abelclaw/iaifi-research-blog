---
abstract: A search for low mass narrow vector resonances decaying into quark-antiquark
  pairs is presented. The analysis is based on data collected in 2017 with the CMS
  detector at the LHC in proton-proton collisions at a center-of-mass energy of 13
  TeV, corresponding to an integrated luminosity of 41.1 fb$^{-1}$. The results of
  this analysis are combined with those of an earlier analysis based on data collected
  at the same collision energy in 2016, corresponding to 35.9 fb$^{-1}$. Signal candidates
  will be recoiling against initial state radiation and are identified as energetic,
  large-radius jets with two pronged substructure. The invariant jet mass spectrum
  is probed for a potential narrow peaking signal over a smoothly falling background.
  No evidence for such resonances is observed within the mass range of 50-450 GeV.
  Upper limits at the 95% confidence level are set on the coupling of narrow resonances
  to quarks, as a function of the resonance mass. For masses between 50 and 300 GeV
  these are the most sensitive limits to date. This analysis extends the earlier search
  to a mass range of 300-450 GeV, which is probed for the first time with jet substructure
  techniques.
arxivId: '1909.04114'
arxivUrl: https://arxiv.org/abs/1909.04114
authors:
- CMS Collaboration
concepts:
- collider physics
- jet physics
- jet substructure
- new physics searches
- signal detection
- boosted topology
- trigger systems
- hypothesis testing
- event reconstruction
- monte carlo methods
- detector simulation
- standard model
figures:
- /iaifi-research-blog/figures/1909_04114/figure_1.png
- /iaifi-research-blog/figures/1909_04114/figure_2.png
pdfUrl: https://arxiv.org/pdf/1909.04114v2
published: '2019-09-09T19:24:17+00:00'
theme: Experimental Physics
title: Search for low mass vector resonances decaying into quark-antiquark pairs in
  proton-proton collisions at $\sqrt{s} =$ 13 TeV
wordCount: 1315
---

## The Big Picture

Imagine trying to spot a single whisper in a stadium of screaming fans. That's roughly the challenge physicists face searching for new particles at the Large Hadron Collider. The LHC smashes protons together billions of times per second, generating an overwhelming flood of debris. Somewhere in that noise, exotic new particles might briefly flicker into existence before vanishing into ordinary matter.

Our best theory of the subatomic world, the Standard Model, has been enormously successful, but it leaves questions unanswered: why do the fundamental building blocks of matter have the masses they do? Why is there more matter than antimatter? Many physicists think the answers require new, undiscovered particles.

One class of candidates are new force-carrying particles, similar to the photon but heavier, that would interact with quarks (the particles inside protons and neutrons) while ignoring electrons and their relatives. Physicists call these **leptophobic vector resonances**: "quark-only" particles that would show up in some parts of the detector while remaining invisible to others.

If such particles exist at low masses (below 450 GeV, roughly 450 times the mass of a proton), they're especially hard to spot. At these energies, the LHC's detectors are swamped by ordinary collisions, and a quiet new signal becomes nearly impossible to see with conventional strategies.

The CMS Collaboration devised a clever workaround, applying it to 77 inverse femtobarns of collision data (a measure of total collisions recorded) and the largest dataset yet used for this type of search. They found no new particles but set the most stringent limits ever placed on how these hypothetical resonances could couple to quarks across a broad mass range.

> **Key Insight:** By exploiting a trick where new particles recoil against radiation before decaying, CMS extended the hunt for hidden new physics into mass territory where conventional searches go blind, ruling out a large swath of theoretical possibilities.

## How It Works

The core problem with hunting for low-mass new particles is the trigger, the electronic gatekeeper that decides which collisions are worth saving. At low energies, the rate of ordinary quark-gluon collisions governed by **Quantum Chromodynamics (QCD)** is so enormous it saturates the trigger bandwidth. Any new particle signal at, say, 100 GeV gets drowned out before it even reaches storage.

The CMS team found an elegant workaround: look for events where the new resonance was produced alongside **initial state radiation (ISR)**, a gluon or quark radiated off an incoming proton just before the collision. This ISR jet carries enough energy to satisfy trigger requirements, effectively using ordinary background physics as a lever to lift the low-mass signal above the noise threshold.

When a hypothetical Z' boson (the stand-in model for these resonances) decays into a quark-antiquark pair at high momentum, the two daughter quarks get swept together by the boost. Instead of flying apart into two well-separated jets, they merge into a single fat jet with distinctive **two-pronged substructure**, like a snowball that, on closer inspection, turns out to be two smaller snowballs stuck together.

![Figure 1](/iaifi-research-blog/figures/1909_04114/figure_1.png)

The team used two wide-jet algorithms to catch these merged decays across the full mass range:
- **AK8 jets** (anti-kT algorithm, radius R = 0.8): efficient for resonance masses below ~200 GeV where decay products are tightly collimated
- **CA15 jets** (Cambridge-Aachen algorithm, radius R = 1.5): captures wider angular spreads for heavier resonances between 200 and 450 GeV

To separate signal from QCD background, they applied a jet substructure tagger called **N-subjettiness**. This variable quantifies how well a jet's radiation pattern matches two prongs versus one: signal jets from Z' decay score high on "two-pronginess," while ordinary QCD jets tend to be more diffuse.

![Figure 2](/iaifi-research-blog/figures/1909_04114/figure_2.png)

After selecting substructure-tagged candidates, the analysis looked for a narrow bump in the **invariant jet mass spectrum**, the distribution of masses reconstructed from all particles inside the fat jet. QCD background falls smoothly as a function of mass; a new resonance would appear as a localized excess on top. The search covered masses from 50 to 450 GeV, with the 2017 dataset extending earlier work into the previously unexplored 300–450 GeV range.


No bump turned up. The collaboration used this absence to set **upper limits at 95% confidence level** on the coupling strength of such resonances to quarks, drawing a boundary on how strongly these hypothetical particles could interact and still have gone undetected. For masses between 50 and 300 GeV, these are the most sensitive constraints ever placed on leptophobic vector resonances. The 300–450 GeV window is completely new territory for jet substructure-based searches.

## Why It Matters

Null results are the unsung workhorses of particle physics. Every ruled-out region carves the map of possible new physics more precisely. Models predicting leptophobic Z' bosons aren't abstract curiosities; they're motivated by dark matter, the matter-antimatter asymmetry, and puzzling patterns in quark masses. Closing off mass ranges pushes theorists to refine their models or abandon dead ends.

The jet substructure techniques refined here have reach well beyond this particular search. The same toolkit (fat jets, substructure variables, ISR-boosted topologies) is now standard at the LHC for hunting new physics at low and intermediate masses. Future runs with more collisions will push these limits further, and machine learning is already being folded in to squeeze more sensitivity from jet substructure information. Open questions remain: can similar techniques probe below 50 GeV? What about broader resonances? Could AI-driven anomaly detection find signals that template-based searches miss?

> **Bottom Line:** CMS found no new particles between 50 and 450 GeV using an ISR-boosted jet substructure strategy, but set the world's most stringent limits on hidden quark-coupling resonances across most of that range, a significant step in mapping the boundaries of physics beyond the Standard Model.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work combines advanced detector physics with jet substructure algorithms, using variables like N-subjettiness to extract faint signals from an overwhelming QCD background.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The jet substructure and N-subjettiness techniques developed here are building blocks for machine learning-based jet taggers now used in next-generation LHC analyses.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By setting the most sensitive limits to date on leptophobic vector resonances in the 50–300 GeV range and opening the 300–450 GeV window for the first time with substructure methods, this search directly constrains models of new gauge symmetries and dark matter mediators.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future high-luminosity LHC runs and AI-powered anomaly detection will push these limits further; the full analysis is available at [arXiv:1909.04114](https://arxiv.org/abs/1909.04114), published in Physical Review D (doi:10.1103/PhysRevD.100.112007).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Search for low mass vector resonances decaying into quark-antiquark pairs in proton-proton collisions at $\sqrt{s} =$ 13 TeV</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">1909.04114</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["CMS Collaboration"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">A search for low mass narrow vector resonances decaying into quark-antiquark pairs is presented. The analysis is based on data collected in 2017 with the CMS detector at the LHC in proton-proton collisions at a center-of-mass energy of 13 TeV, corresponding to an integrated luminosity of 41.1 fb$^{-1}$. The results of this analysis are combined with those of an earlier analysis based on data collected at the same collision energy in 2016, corresponding to 35.9 fb$^{-1}$. Signal candidates will be recoiling against initial state radiation and are identified as energetic, large-radius jets with two pronged substructure. The invariant jet mass spectrum is probed for a potential narrow peaking signal over a smoothly falling background. No evidence for such resonances is observed within the mass range of 50-450 GeV. Upper limits at the 95% confidence level are set on the coupling of narrow resonances to quarks, as a function of the resonance mass. For masses between 50 and 300 GeV these are the most sensitive limits to date. This analysis extends the earlier search to a mass range of 300-450 GeV, which is probed for the first time with jet substructure techniques.</span></div></div>
</div>
