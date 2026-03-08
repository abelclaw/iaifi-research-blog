---
abstract: Ever-increasing amount of data is produced by particle detectors in their
  quest to unveil the laws of Nature. The large data rate requires the use of specialized
  triggers that promptly reduce the data rate to a manageable level; however, in doing
  so, unexpected new phenomena may escape detection. Additionally, the large data
  rate is increasingly difficult to analyze effectively, which has led to a recent
  revolution on machine learning techniques. Here, we present a methodology based
  on recent quantum compression techniques that has the capacity to store exponentially
  more amount of information than classically available methods. To demonstrate this,
  we encode the full neutrino telescope event information using parity observables
  in an IBM quantum processor using 8 qubits. Then we show that we can recover the
  information stored on the quantum computer with a fidelity of 84%. Finally, we illustrate
  the use of our protocol by performing a classification task that separates electron-neutrino
  events to muon-neutrinos events in a neutrino telescope. This new capability would
  eventually allow us to solve the street light effect in particle physics, where
  we only record signatures of particles with which we are familiar.
arxivId: '2402.19306'
arxivUrl: https://arxiv.org/abs/2402.19306
authors:
- Jeffrey Lazar
- Santiago Giner Olavarrieta
- Giancarlo Gatti
- Carlos A. Argüelles
- Mikel Sanz
concepts:
- quantum computing
- quantum states
- quantum data encoding
- neutrino detection
- parity observables
- trigger systems
- classification
- dimensionality reduction
- entanglement
- anomaly detection
- feature extraction
figures:
- /iaifi-research-blog/figures/2402_19306/figure_1.png
- /iaifi-research-blog/figures/2402_19306/figure_2.png
- /iaifi-research-blog/figures/2402_19306/figure_3.png
pdfUrl: https://arxiv.org/pdf/2402.19306v3
published: '2024-02-29T16:12:56+00:00'
theme: Experimental Physics
title: New Pathways in Neutrino Physics via Quantum-Encoded Data Analysis
wordCount: 922
---

## The Big Picture

Imagine you're a detective, but you only ever search for clues under streetlights. Not because that's where the clues are, but because that's where you can see. This is exactly the trap particle physics experiments have fallen into.

Every second, the IceCube Neutrino Observatory buried beneath the South Pole generates a terabyte of raw data. The Large Hadron Collider produces nearly 300 terabytes per day. No computing system on Earth can store all of it, so physicists use automated **triggers**, real-time filters that decide in microseconds which data to keep and which to discard forever.

The problem: those triggers are built to recognize particles physicists already know about. If something genuinely novel flits through a detector, some exotic new particle or unexpected interaction, the trigger might silently delete it. Physicists call this the **streetlight effect**, a blind spot baked into the very instruments meant to push the boundaries of discovery.

A team of researchers from Harvard and the University of the Basque Country now has a potential escape route. They've shown that quantum computers can compress neutrino telescope data with exponentially greater density than any classical storage method, and that this compressed data remains useful for physics analysis.

> **Key Insight:** By encoding classical particle physics data into quantum states using parity observables, this approach can store 3ⁿ bits of information in just n qubits. That exponential advantage over classical storage could one day let detectors record far more of what they see.

## How It Works

A classical bit holds one value: 0 or 1. A qubit can be measured along three axes (x, y, or z), each yielding +1 or −1. For n qubits, you can construct **parity observables**: products of spin measurements across multiple qubits taken simultaneously. With n qubits there are 3ⁿ such observables, an exponential explosion of information capacity.

Here's how the encoding works in practice:

1. **Simulate the event.** Start with a simulated neutrino interaction in IceCube, a flash of light across hundreds of optical sensors buried in Antarctic ice. Each sensor records whether it was activated and when, producing a raw bitstring representing the full event.

2. **Map bits to parity observables.** Each bit of the classical data gets mapped to one of the 3ⁿ parity operators. The encoding algorithm finds a set of quantum states, specifically **parameterized quantum circuits** (circuits with tunable settings adjusted to match a target), whose average measurement outcomes on those operators reproduce the target bitstring.

3. **Run on real hardware.** The team executed this encoding on an IBM quantum processor using 8 qubits, which supports 3⁸ = 6,561 parity observables, enough to store the full information from a neutrino interaction event.

![Figure 2](/iaifi-research-blog/figures/2402_19306/figure_2.png)

4. **Decode and verify.** After storage, they read the quantum states back by measuring all the parity observables and reconstructing the original bitstring. The result: 84% fidelity, meaning 84% of the stored bits were recovered correctly from the quantum computer.

The encoding circuit uses a layered architecture of rotation gates (operations that tilt a qubit's state along a chosen axis) and entangling operations (operations that link qubits so their measurements affect one another). Tunable parameters α₁ through α₇ are optimized to best match the target data. The circuit is shallow enough to run on today's noisy quantum hardware, though noise remains the main limit on fidelity.

![Figure 1](/iaifi-research-blog/figures/2402_19306/figure_1.png)

With the data decoded, the team ran a classification task: distinguishing electron-neutrino events from muon-neutrino events, two flavors of neutrino that leave characteristically different detector signatures. The classification worked, showing that quantum-stored data keeps enough structure for downstream physics analysis, not just raw storage.

## Why It Matters

The immediate result (84% fidelity on 8 qubits) won't replace IceCube's data infrastructure tomorrow. The main bottleneck is finding sufficiently faithful quantum representations of high-dimensional classical data. But the conceptual advance matters: this is one of the first demonstrations that quantum compression can preserve enough physical information to support particle physics classification on real hardware.

The longer-term picture is worth paying attention to. Neutrino telescope upgrades and next-generation experiments like DUNE and Hyper-Kamiokande will push data rates another order of magnitude higher. If quantum memory can be integrated into detector systems, even as a supplementary layer alongside classical triggers, it could capture a broader slice of events and let physicists analyze anomalies that would otherwise have been filtered out before anyone noticed. The streetlight effect isn't inevitable. It's a technological constraint, and quantum storage is one credible path around it.

> **Bottom Line:** Using just 8 qubits on a real IBM quantum processor, this team stored and recovered neutrino telescope event data with 84% fidelity and used it for particle classification. It's a proof-of-concept that quantum compression could eventually help particle physics escape the observational blind spots built into its own data infrastructure.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects quantum information science with experimental particle physics, applying quantum compression techniques to the data management crisis facing next-generation neutrino observatories.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The encoding-decoding protocol shows that quantum-stored representations of classical data can support machine learning classification tasks, opening a new direction for quantum-enhanced AI in scientific data analysis.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">Quantum memory can preserve neutrino event information with sufficient fidelity for flavor classification, pointing toward detector architectures capable of capturing physics missed by conventional trigger-based data reduction.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will focus on improving quantum state representations to push fidelity toward levels needed for practical deployment. The full paper is available at [arXiv:2402.19306](https://arxiv.org/abs/2402.19306).</span></div></div>
</div>
