---
abstract: 'The quest to build a generalist robotic system is impeded by the scarcity
  of diverse and high-quality data. While real-world data collection effort exist,
  requirements for robot hardware, physical environment setups, and frequent resets
  significantly impede the scalability needed for modern learning frameworks. We introduce
  DART, a teleoperation platform designed for crowdsourcing that reimagines robotic
  data collection by leveraging cloud-based simulation and augmented reality (AR)
  to address many limitations of prior data collection efforts. Our user studies highlight
  that DART enables higher data collection throughput and lower physical fatigue compared
  to real-world teleoperation. We also demonstrate that policies trained using DART-collected
  datasets successfully transfer to reality and are robust to unseen visual disturbances.
  All data collected through DART is automatically stored in our cloud-hosted database,
  DexHub, which will be made publicly available upon curation, paving the path for
  DexHub to become an ever-growing data hub for robot learning. Videos are available
  at: https://dexhub.ai/project'
arxivId: '2411.02214'
arxivUrl: https://arxiv.org/abs/2411.02214
authors:
- Younghyo Park
- Jagdeep Singh Bhatia
- Lars Ankile
- Pulkit Agrawal
concepts:
- crowdsourced teleoperation
- augmented reality interface
- scalability
- sim-to-real transfer
- robot demonstration dataset
- transfer learning
- data augmentation
- robustness
- reinforcement learning
figures:
- /iaifi-research-blog/figures/2411_02214/figure_1.png
- /iaifi-research-blog/figures/2411_02214/figure_2.png
- /iaifi-research-blog/figures/2411_02214/figure_3.png
pdfUrl: https://arxiv.org/pdf/2411.02214v1
published: '2024-11-04T16:11:33+00:00'
theme: Foundational AI
title: 'DexHub and DART: Towards Internet Scale Robot Data Collection'
wordCount: 1036
---

## The Big Picture

Imagine teaching a child to cook by restricting them to a single kitchen, one set of dishes, and requiring every pot and pan to be reset after each attempt. Now scale that to thousands of learners, each stuck in their own cramped kitchen, exhausted by tedious resets. That's essentially the state of robot learning today, and it's a serious bottleneck.

Building robots that handle real-world unpredictability requires vast training data. Image recognition and language models only became truly capable once researchers pooled enormous shared datasets: millions of labeled photos, billions of web pages. Robot learning needs the same scale.

But robot data doesn't grow on the web. Someone has to physically move a robot arm, guide it through a task, then reset every object by hand, hundreds of times, for a single skill. Hardware costs price out most contributors. Scale up task complexity and the fatigue becomes paralyzing.

Researchers at MIT's Improbable AI Lab have proposed a different approach. Their system, **DART** (Dexterous Augmented Reality Teleoperation), lets anyone demonstrate robot skills through an augmented reality interface connected to a cloud simulation. No robot hardware required, no physical resets, no lab access needed.

> **Key Insight:** By moving robot teleoperation into AR-connected cloud simulation, DART separates data collection from physical infrastructure, enabling crowdsourced, internet-scale robot learning datasets that could grow the way language and image data grows online.

## How It Works

DART reimagines the data collection pipeline from scratch. Instead of physically controlling a robot arm, an operator uses a smartphone or AR headset to view and manipulate a high-fidelity simulated environment. The cloud-based simulation handles all physics and rendering, while the AR overlay gives operators a detailed, occlusion-minimized view (objects don't block each other from the camera) that often outperforms what a physical camera setup provides.

![Figure 1](/iaifi-research-blog/figures/2411_02214/figure_1.png)

The design eliminates three major bottlenecks in traditional teleoperation:

- **Environment setup**: No physical lab or robot required. The scene exists in simulation and configures on demand.
- **Limited observability**: AR rendering gives operators a rich, adjustable view. No camera occlusions, no blurring from video compression.
- **Resetting**: Hit a button. The environment resets instantly, with randomized object configurations for built-in diversity.

The interface is deliberately game-like, lowering the barrier for non-expert contributors. If teleoperation feels like a video game rather than operating lab equipment, the pool of potential data contributors expands dramatically.

All demonstrations flow automatically into **DexHub**, a cloud-hosted, publicly accessible database built to grow continuously, more like a living repository than a static dataset release.

## Why It Matters

The user study results are concrete. DART achieves **2.1× higher data collection throughput** compared to real-world teleoperation, with significantly lower physical and cognitive fatigue. Operators no longer constantly switch attention between controlling the robot and resetting objects, a mental tax that compounds over long sessions.

![Figure 2](/iaifi-research-blog/figures/2411_02214/figure_2.png)

Simulation also unlocks training strategies impossible with real-world data. **Domain randomization** (varying lighting, textures, object positions, and physics parameters) produces learned robot behaviors, called *policies*, that hold up better to visual disturbances than those trained on real demonstrations.

In transfer experiments, DART-trained policies successfully moved to physical robots and outperformed real-world-trained counterparts on robustness to unseen visual conditions. Data collected without any physical robot produced *better* policies than data collected with one.

![Figure 3](/iaifi-research-blog/figures/2411_02214/figure_3.png)

Today's largest robot datasets (60,000 to 110,000 task recordings from major lab efforts) represent enormous labor investments that still fall short of what modern learning frameworks demand. If DART and DexHub scale as intended, the bottleneck shifts from logistics to curation.

Open questions remain. How well does simulation fidelity hold up for increasingly complex manipulation tasks? How much does the **sim-to-real gap** (the performance drop when moving a trained robot from simulation into the physical world) grow as tasks demand finer contact dynamics, like threading a needle versus moving dishes? How will DexHub maintain data quality at internet scale, where contributor skill varies enormously? These are real challenges, but the right ones to be wrestling with.

> **Bottom Line:** DART cuts data collection time in half while eliminating the physical burden of robot teleoperation, and the policies it trains are *more* robust than those from real-world data. If DexHub scales as hoped, it could become the ImageNet moment for robot learning.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects robotics, computer graphics, and machine learning by using AR-based simulation as a physics-faithful proxy for real-world robot interaction, enabling reinforcement learning frameworks that cannot be applied to static real-world datasets.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">Crowdsourced simulation data, combined with domain randomization, can produce policies that outperform those trained on real-world demonstrations in robustness to visual distribution shift, challenging the assumption that physical data is always preferable.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">By enabling policies trained in simulation to transfer robustly to physical systems, this research advances understanding of how learned representations can span the gap between virtual and physical dynamics.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">The team plans to open DexHub as a publicly curated dataset upon release; the project and associated data are described at dexhub.ai, with the full paper at [arXiv:2411.02214](https://arxiv.org/abs/2411.02214).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">DexHub and DART: Towards Internet Scale Robot Data Collection</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2411.02214</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Younghyo Park", "Jagdeep Singh Bhatia", "Lars Ankile", "Pulkit Agrawal"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">The quest to build a generalist robotic system is impeded by the scarcity of diverse and high-quality data. While real-world data collection effort exist, requirements for robot hardware, physical environment setups, and frequent resets significantly impede the scalability needed for modern learning frameworks. We introduce DART, a teleoperation platform designed for crowdsourcing that reimagines robotic data collection by leveraging cloud-based simulation and augmented reality (AR) to address many limitations of prior data collection efforts. Our user studies highlight that DART enables higher data collection throughput and lower physical fatigue compared to real-world teleoperation. We also demonstrate that policies trained using DART-collected datasets successfully transfer to reality and are robust to unseen visual disturbances. All data collected through DART is automatically stored in our cloud-hosted database, DexHub, which will be made publicly available upon curation, paving the path for DexHub to become an ever-growing data hub for robot learning. Videos are available at: https://dexhub.ai/project</span></div></div>
</div>
