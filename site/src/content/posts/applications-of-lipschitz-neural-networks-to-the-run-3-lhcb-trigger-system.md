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
- /iaifi-research-blog/figures/2312_14265/figure_2.png
- /iaifi-research-blog/figures/2312_14265/figure_3.png
pdfUrl: https://arxiv.org/pdf/2312.14265v1
published: '2023-12-21T19:29:00+00:00'
theme: Experimental Physics
title: Applications of Lipschitz neural networks to the Run 3 LHCb trigger system
wordCount: 1235
---

## The Big Picture

Imagine trying to drink from a fire hose — not just any fire hose, but one pumping 4 terabytes of data every single second. That is the reality facing physicists at CERN's LHCb experiment during the current Run 3 data-taking campaign. Inside the Large Hadron Collider, protons smash together 30 million times per second, and each collision produces a torrent of particles that must be instantly evaluated, filtered, and either saved or discarded — forever. There are no second chances. Once an event is thrown away, it is gone.

The LHCb detector is hunting for some of the rarest and most fleeting phenomena in nature: the decays of **b-hadrons** — heavy, unstable particles built around a fundamental building block called a bottom quark. These particles exist for just a few picoseconds (trillionths of a second) before disintegrating into showers of lighter particles. These decays may hold the key to explaining why the universe contains matter at all, and possibly to discovering entirely new types of particles lurking beyond our current theories.

To find them, physicists must first build a trigger system — an automated real-time decision engine — capable of slashing that 4 TB/s flood down to a manageable 10 GB/s stream, all while running at the speed of physics itself.

A team of researchers from MIT, CERN, TU Dortmund, and Meta AI has now embedded a new breed of neural network directly into LHCb's trigger system, achieving certified mathematical guarantees of robustness and dramatically improved sensitivity to rare b-hadron decay signatures.

> **Key Insight:** By constraining neural networks to be both Lipschitz-bounded and monotonic, the LHCb team built classifiers that are provably stable under detector noise — meaning they can make mission-critical, irreversible decisions at 30 MHz without falling apart when instruments hiccup.

## How It Works

The LHCb trigger operates in two stages. The first, **HLT1** (High Level Trigger 1), runs on GPUs and performs a rapid partial reconstruction of each event using charged-track information alone, achieving a 20-fold reduction in data volume. What remains flows into a buffer for real-time alignment and calibration before reaching **HLT2**, a CPU-based system that applies offline-quality reconstruction to make more refined decisions.

![Figure 1](/iaifi-research-blog/figures/2312_14265/figure_1.png)

At the heart of this paper are the **topological triggers** — specialized algorithms within HLT2 that search for decay signatures based on their geometric shape. Specifically, they look for the characteristic signature of b-hadron decays: a **displaced secondary vertex** — a point in space, shifted millimeters to centimeters from the original proton-proton collision point, where a heavy beauty particle has decayed into two or three charged tracks.

The geometry is distinctive. Because b-hadrons travel at high speed before decaying, they leave a tell-tale gap between the proton collision point and where their decay products emerge. The topological triggers reconstruct these secondary vertices in pairwise combinations (two-body) or triplets (three-body) of final-state tracks, casting a wide, inclusive net over the full spectrum of b-hadron decays.

The critical innovation is the neural network architecture powering these triggers. Standard deep learning classifiers, while powerful, can behave unpredictably when inputs shift slightly — say, because a detector module is running warm, or a calibration is off by a small margin. In a system where every discarded event is a permanent loss, that unpredictability is unacceptable.

The solution comes from **Lipschitz neural networks**, which impose a strict mathematical cap on how much the network's output can swing in response to a small change in its inputs. Think of it as a sensitivity limit built directly into the architecture: no matter what the detector throws at the network, large jumps in the classifier score are mathematically forbidden. Concretely, this means:

- A small perturbation in input features — caused by detector instabilities — can only produce a proportionally small change in the classifier score
- The bound is *certified*, not just empirically observed, but proven by construction through architectural constraints on weight matrices
- Systematic uncertainties for downstream physics analyses become far easier to evaluate

Layered on top is a second constraint: **monotonicity**. Certain physical quantities should, by physics logic, always push a classifier toward accepting an event. A longer decay distance or higher transverse momentum should always increase the likelihood that a candidate is a real b-hadron. By enforcing that the network's output is monotonically increasing with respect to such features, the team baked domain expertise directly into the model's architecture.

This matters enormously for BSM (Beyond the Standard Model) searches: exotic particles absent from training data may still carry the right kinematic fingerprint to pass the trigger, because the network is constrained to respond correctly even to outliers it has never seen.

![Figure 2](/iaifi-research-blog/figures/2312_14265/figure_2.png)

The two-body and three-body topological triggers each use a curated set of input features — vertex displacement significance, track quality, transverse momentum, vertex fit quality — with explicit monotonicity requirements assigned to the physically motivated ones. The networks are compact enough to run within HLT2's real-time compute budget, which is non-trivial given the volume flowing in from HLT1.

![Figure 3](/iaifi-research-blog/figures/2312_14265/figure_3.png)

## Why It Matters

This work sits at a genuinely important intersection: it is not just about making physics faster, it is about making physics safer. The topological triggers must remain reliable over months and years of continuous operation, across shifting detector conditions, without human intervention. Lipschitz monotonic networks provide a formal contract: the classifier will not suddenly start rejecting good events simply because a sensor drifted slightly out of calibration.

That kind of guarantee has been nearly impossible to achieve with traditional **boosted decision trees** — a well-established machine learning approach, and the technology these networks replace — or with standard unconstrained deep learning.

The implications extend well beyond LHCb. The same framework could be applied to any experiment requiring real-time, irreversible event selection under imperfect detector stability. More broadly, this work demonstrates that **certified machine learning** — models with provable behavioral guarantees — is ready for deployment in some of the most demanding real-world environments that exist: particle physics experiments running 24 hours a day, 365 days a year, at the frontiers of human knowledge.

And for BSM searches specifically, the monotonicity constraint offers a genuine advantage: the trigger becomes more sensitive, not less, to the unexpected.

> **Bottom Line:** Lipschitz monotonic neural networks are now making irreversible, mission-critical decisions at 30 million collisions per second inside CERN's LHCb detector, offering certified stability against detector noise and enhanced reach for undiscovered particles — a landmark deployment of guaranteed-safe AI in fundamental physics.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work directly embeds certified deep learning theory into an operational particle physics trigger, demonstrating that formal AI safety guarantees and experimental physics requirements can be co-designed and deployed at scale.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The deployment of Lipschitz-bounded monotonic neural networks in a real-time, safety-critical system proves that certified ML models can meet stringent performance and compute constraints in production — advancing the case for formal guarantees in high-stakes AI applications.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By replacing legacy decision-tree triggers with provably robust neural networks, LHCb gains enhanced sensitivity to displaced multi-body b-hadron decays and to potential BSM states absent from training samples, directly expanding the physics reach of Run 3.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will extend these architectures to additional inclusive triggers and higher-multiplicity decay topologies as LHCb accumulates its Run 3 dataset; full technical details are available at arXiv:2501.09080.</span></div></div>
</div>
