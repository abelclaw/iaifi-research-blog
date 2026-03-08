---
abstract: The operating conditions defining the current data taking campaign at the
  Large Hadron Collider, known as Run 3, present unparalleled challenges for the real-time
  data acquisition workflow of the LHCb experiment at CERN. To address the anticipated
  surge in luminosity and consequent event rate, the LHCb experiment is transitioning
  to a fully software-based trigger system. This evolution necessitated innovations
  in hardware configurations, software paradigms, and algorithmic design. A significant
  advancement is the integration of monotonic Lipschitz neural networks into the LHCb
  trigger system. These deep learning models offer certified robustness against detector
  instabilities, and the ability to encode domain-specific inductive biases. Such
  properties are crucial for the inclusive heavy-flavour triggers and, most notably,
  for the topological triggers designed to inclusively select $b$-hadron candidates
  by exploiting the unique kinematic and decay topologies of beauty decays. This paper
  describes the recent progress in integrating Lipschitz neural networks into the
  topological triggers, highlighting the resulting enhanced sensitivity to highly
  displaced multi-body candidates produced within the LHCb acceptance.
arxivId: '2312.14265'
arxivUrl: https://arxiv.org/abs/2312.14265
authors:
- Blaise Delaney
- Nicole Schulte
- Gregory Ciezarek
- Niklas Nolte
- Mike Williams
- Johannes Albrecht
concepts:
- trigger systems
- lipschitz neural networks
- robustness
- classification
- monotonic constraints
- collider physics
- particle tracking
- event reconstruction
- new physics searches
- interpretability
- physics-informed neural networks
- anomaly detection
figures:
- /iaifi-research-blog/figures/2312_14265/figure_1.png
pdfUrl: https://arxiv.org/pdf/2312.14265v1
published: '2023-12-21T19:29:00+00:00'
theme: Experimental Physics
title: Applications of Lipschitz neural networks to the Run 3 LHCb trigger system
wordCount: 1084
---

## The Big Picture

Imagine trying to drink from a fire hose pumping 4 terabytes of data every single second. That is what physicists at CERN's LHCb experiment face during Run 3. Inside the Large Hadron Collider, protons smash together 30 million times per second, and each collision produces a torrent of particles that must be instantly evaluated, filtered, and either saved or discarded forever. Once an event is thrown away, it is gone.

The LHCb detector hunts for some of the rarest phenomena in nature: the decays of **b-hadrons**, heavy, unstable particles built around a bottom quark. They exist for just a few picoseconds before disintegrating into showers of lighter particles. Their decays may help explain why the universe contains matter at all, and could reveal entirely new types of particles beyond our current theories.

Finding them requires a trigger system, an automated real-time decision engine that slashes the 4 TB/s flood down to a manageable 10 GB/s stream, running at the speed of the collisions themselves.

A team from MIT, CERN, TU Dortmund, and Meta AI has now embedded a new breed of neural network directly into LHCb's trigger system. The result: certified mathematical guarantees of robustness and improved sensitivity to rare b-hadron decay signatures.

> **Key Insight:** By constraining neural networks to be both Lipschitz-bounded and monotonic, the LHCb team built classifiers that are provably stable under detector noise. They can make irreversible decisions at 30 MHz without falling apart when instruments hiccup.

## How It Works

The LHCb trigger operates in two stages. **HLT1** (High Level Trigger 1) runs on GPUs, performing a rapid partial reconstruction of each event using charged-track information alone and cutting the data volume by a factor of 20. What survives flows into a buffer for real-time alignment and calibration before reaching **HLT2**, a CPU-based system that applies offline-quality reconstruction for more refined decisions.

![Figure 1](/iaifi-research-blog/figures/2312_14265/figure_1.png)

The **topological triggers** sit inside HLT2. They search for decay signatures based on geometric shape, specifically the hallmark of b-hadron decays: a **displaced secondary vertex**, a point in space shifted millimeters to centimeters from the original proton-proton collision. Because b-hadrons travel at high speed before decaying, they leave a gap between the collision point and where their decay products appear. The topological triggers reconstruct these secondary vertices from pairs (two-body) or triplets (three-body) of final-state tracks, casting a wide net across the full spectrum of b-hadron decays.

The real advance is the neural network architecture powering these triggers. Standard deep learning classifiers can behave unpredictably when inputs shift slightly, say because a detector module is running warm or a calibration drifts by a small margin. In a system where every discarded event is a permanent loss, that unpredictability is unacceptable.

Enter **Lipschitz neural networks**. These impose a strict mathematical cap on how much the network's output can swing in response to a small change in its inputs. Think of it as a sensitivity limit baked into the architecture: no matter what the detector throws at the network, large jumps in the classifier score are forbidden. In practice:

- A small perturbation in input features, caused by detector instabilities, can only produce a proportionally small change in the classifier score
- The bound is *certified*: not just empirically observed, but proven by construction through architectural constraints on weight matrices
- Systematic uncertainties for downstream physics analyses become far easier to evaluate

On top of the Lipschitz constraint, the team also enforces **monotonicity**. Certain physical quantities should, by straightforward physics reasoning, always push a classifier toward accepting an event. A longer decay distance or higher transverse momentum should always increase the likelihood that a candidate is a real b-hadron. Monotonicity bakes that domain knowledge directly into the model.


This is especially useful for BSM (Beyond the Standard Model) searches. Exotic particles absent from training data may still carry the right kinematic fingerprint to pass the trigger, because the network is constrained to respond correctly to outliers it has never seen.

The two-body and three-body topological triggers each use a curated set of input features: vertex displacement significance, track quality, transverse momentum, vertex fit quality. Explicit monotonicity requirements are assigned to the physically motivated ones. The networks are compact enough to run within HLT2's real-time compute budget, no small feat given the data volume flowing in from HLT1.


## Why It Matters

This is not just about making physics faster. It is about making it safer. The topological triggers must stay reliable over months and years of continuous operation, across shifting detector conditions, without human intervention. Lipschitz monotonic networks provide a formal contract: the classifier will not suddenly start rejecting good events because a sensor drifted out of calibration.

That kind of guarantee has been nearly impossible to achieve with the boosted decision trees these networks replace, or with standard unconstrained deep learning.

The same framework could apply to any experiment that must make real-time, irreversible event selections under imperfect detector stability. More broadly, it shows that certified machine learning, models with provable behavioral guarantees, is ready for deployment in some of the most demanding environments that exist: particle physics experiments running around the clock at the boundary of known physics.

For BSM searches specifically, the monotonicity constraint offers a genuine advantage: the trigger becomes more sensitive, not less, to the unexpected.

> **Bottom Line:** Lipschitz monotonic neural networks are now making irreversible decisions at 30 million collisions per second inside CERN's LHCb detector, with certified stability against detector noise and enhanced reach for undiscovered particles. It is one of the first deployments of guaranteed-safe AI in fundamental physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work embeds certified deep learning theory into an operational particle physics trigger, showing that formal AI safety guarantees and experimental physics requirements can be co-designed and deployed at scale.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Deploying Lipschitz-bounded monotonic neural networks in a real-time, safety-critical system proves that certified ML models can meet stringent performance and compute constraints in production, strengthening the case for formal guarantees in high-stakes AI applications.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By replacing legacy decision-tree triggers with provably robust neural networks, LHCb gains enhanced sensitivity to displaced multi-body b-hadron decays and to potential BSM states absent from training samples, directly expanding the physics reach of Run 3.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend these architectures to additional inclusive triggers and higher-multiplicity decay topologies as LHCb accumulates its Run 3 dataset; full technical details are available at [arXiv:2312.14265](https://arxiv.org/abs/2312.14265).</span></div></div>
</div>
