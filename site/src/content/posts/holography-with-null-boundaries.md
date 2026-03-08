---
abstract: One of the key issues in holography is going beyond $\mathrm{AdS}$ and defining
  quantum gravity in spacetimes with a null boundary. Recent examples of this type
  involve linear dilaton asymptotics and are related to the $T \overline{T}$ deformation.
  We present a holographic correspondence derived from string theory, which is an
  example of a kind of celestial holography. The holographic definition is a spacetime
  non-commutative open string theory supported on D1-D5 branes together with fundamental
  strings. The gravity solutions interpolate between $\mathrm{AdS}_3$ metrics and
  six-dimensional metrics. Radiation can escape to null infinity, which makes both
  the encoding of quantum information in the boundary and the dynamics of black holes
  quite different from $\mathrm{AdS}$ spacetimes.
arxivId: '2506.20765'
arxivUrl: https://arxiv.org/abs/2506.20765
authors:
- Christian Ferko
- Savdeep Sethi
concepts:
- holography
- null boundary holography
- string theory
- non-commutative open string theory
- conformal field theory
- quantum field theory
- tt-bar deformation
- black hole thermodynamics
- quantum computing
- entanglement
figures: []
pdfUrl: https://arxiv.org/pdf/2506.20765v2
published: '2025-06-25T18:57:48+00:00'
theme: Theoretical Physics
title: Holography with Null Boundaries
wordCount: 1127
---

## The Big Picture

Imagine a cosmic fishbowl. In the leading framework for quantum gravity, the AdS/CFT correspondence, the universe behaves like one: light and radiation can never truly escape. They race to the boundary, bounce back, and return. This "reflecting wall" property is what makes the theory work. It keeps black holes stable, lets information circulate, and gives theorists a clean mathematical framework for encoding everything inside onto the surface.

Now imagine punching a hole in the bowl. Radiation streams out and disappears forever. Black holes evaporate. Information behaves in completely alien ways.

This is the world of spacetimes with **null boundaries**, regions where the edge of spacetime is swept by light rays rather than fixed in time. Defining a coherent theory of quantum gravity in such a universe is one of the deepest unsolved problems in theoretical physics. Ferko and Sethi have done exactly that: starting from first principles of string theory, they derive a holographic correspondence for a family of these exotic spacetimes. The boundary theory turns out to be stranger than almost anyone expected.

> **Key Insight:** When the cosmic fishbowl has a null boundary instead of a reflecting wall, the holographic dual isn't a conventional quantum field theory. It's a *non-commutative open string theory*, where the very coordinates of space fail to commute, behaving instead like quantum operators.

## How It Works

The starting point is the **D1-D5 brane system**, a configuration in Type IIB string theory that has been a workhorse of holography for thirty years. In the classic setup, a stack of D1-branes (string-like, one-dimensional objects) and D5-branes (membrane-like, five-dimensional objects) wraps a compact four-torus, and their near-horizon geometry reproduces AdS₃, the familiar fishbowl.

Ferko and Sethi add a crucial ingredient: fundamental F1-strings bound into the mix, along with a background **NS B₂-field**, an electromagnetic-like field that threads the D1-brane worldvolume and twists the surrounding geometry.

This extra field changes everything. It deforms the geometry so that, instead of asymptoting to AdS₃ at large distances, the spacetime opens up into a full six-dimensional metric where radiation pours freely to null infinity. Deep in the interior, the solutions still look like AdS₃. The old fishbowl lives on inside. But zoom out toward the boundary and the geometry transitions into something genuinely new.

To construct these solutions systematically, the authors use a **TsT transformation**: T-duality (a string theory symmetry that swaps large distances for small ones), then a coordinate shift, then another T-duality. Applied to the known D1-D5 geometry, TsT generates the entire family of solutions in closed form. The key parameters are:

- $n_1$: number of D1-branes
- $n_5$: number of D5-branes
- $m_1$: number of fundamental F1-strings
- A non-commutativity parameter $\hat{\theta}$ set by the background B-field

The causal structure of the resulting spacetimes repays careful analysis. Unlike AdS, which has a timelike boundary allowing signals to bounce back and forth with the interior indefinitely, these spacetimes have a *null* boundary, swept by light itself. Signals from the interior reach it once and never return.

So what lives on the holographic "screen" encoding the bulk physics? It turns out to be **Non-Commutative Open String theory (NCOS)**: an open string theory where spacetime coordinates satisfy $[x^i, x^j] = i\theta^{ij}$, failing to commute just like quantum mechanical position and momentum. At low energies it resembles a field theory deformed by an infinite tower of irrelevant operators, organized through a **Moyal star product**, a phase-twisted multiplication that keeps track of the underlying non-commutativity. This NCOS theory lives on a two-dimensional worldsheet even though the ambient spacetime is six-dimensional, and it contains no massless graviton.

## Why It Matters

Several frontier areas feel the effects at once. Because radiation escapes to null infinity, large black holes in these spacetimes cannot reach stable thermal equilibrium with their own Hawking radiation. They *must* evaporate. Whatever replaces the standard holographic dictionary here has to handle information that genuinely leaks away, not information bouncing back and forth forever. Working out that dictionary is now a concrete, tractable problem.

The work also exposes hidden connections between independently studied frameworks. The **TT-bar deformation**, a specific deformation of two-dimensional field theories that has drawn enormous attention in recent years, appears to lurk behind holography with null boundaries. It shows up both in asymptotically linear dilaton spacetimes from F1-NS5 systems and, in a different guise, in the NCOS theory studied here. Ferko and Sethi's cleanly derived example may help explain why TT-bar keeps appearing across so many different contexts.

The paper also makes contact with **celestial holography**, the program of defining quantum gravity in open, asymptotically flat spacetimes using data recorded at null infinity. Rather than speculative bottom-up constructions, this gives the celestial holography community a concrete, top-down stringy example to stress-test their ideas against.

> **Bottom Line:** By adding fundamental strings to the D1-D5 brane system and taking a precise decoupling limit, Ferko and Sethi derive a holographic correspondence for spacetimes that genuinely allow radiation to escape. The boundary dual is a non-commutative string theory, opening a new window onto quantum gravity beyond the AdS fishbowl.

<div style="margin-top:2rem;"><h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;">IAIFI Research Highlights</h2>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f5f5f5;border:1px solid #d4d4d4;"><img src="/iaifi-research-blog/images/logo-fi-black.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#1a1a1a;">Interdisciplinary Research Achievement</strong><br/><span style="color:#374151;">This work connects string theory, non-commutative geometry, and TT-bar deformations, showing how a single string-theoretic construction reveals deep links between three previously distinct research programs.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#eff6ff;border:1px solid #bfdbfe;"><img src="/iaifi-research-blog/images/logo-ai-blue.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#2c5f8a;">Impact on Artificial Intelligence</strong><br/><span style="color:#374151;">The non-commutative star-product structure defining the boundary theory has formal similarities to algebraic structures studied in geometric approaches to machine learning, which may motivate future cross-disciplinary exploration.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#faf5ff;border:1px solid #e9d5ff;"><img src="/iaifi-research-blog/images/logo-fi-purple.svg" alt="" style="width:32px;height:32px;flex-shrink:0;" /><div><strong style="color:#7b2d8e;">Impact on Fundamental Interactions</strong><br/><span style="color:#374151;">The paper provides the first rigorously derived holographic dictionary for spacetimes with null boundaries, directly tackling the long-standing problem of defining quantum gravity outside the AdS framework and supplying new tools for studying black hole evaporation and information loss.</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#ecfdf5;border:1px solid #a7f3d0;"><div><strong style="color:#059669;">Outlook and References</strong><br/><span style="color:#374151;">Future work will aim to extract concrete physical observables from the NCOS dual, determine how information is encoded at null infinity, and explore connections to celestial holography and flat-space S-matrix theory; the paper is available at [arXiv:2506.20765](https://arxiv.org/abs/2506.20765).

## Original Paper Details</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Title</strong><br/><span style="color:#374151;">Holography with Null Boundaries</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">arXiv ID</strong><br/><span style="color:#374151;">2506.20765</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Authors</strong><br/><span style="color:#374151;">["Christian Ferko", "Savdeep Sethi"]</span></div></div>
<div style="display:flex;gap:0.75rem;align-items:flex-start;padding:1rem;margin-bottom:0.75rem;border-radius:0.5rem;background:#f9fafb;border:1px solid #e5e7eb;"><div><strong style="color:#374151;">Abstract</strong><br/><span style="color:#374151;">One of the key issues in holography is going beyond $\mathrm{AdS}$ and defining quantum gravity in spacetimes with a null boundary. Recent examples of this type involve linear dilaton asymptotics and are related to the $T \overline{T}$ deformation. We present a holographic correspondence derived from string theory, which is an example of a kind of celestial holography. The holographic definition is a spacetime non-commutative open string theory supported on D1-D5 branes together with fundamental strings. The gravity solutions interpolate between $\mathrm{AdS}_3$ metrics and six-dimensional metrics. Radiation can escape to null infinity, which makes both the encoding of quantum information in the boundary and the dynamics of black holes quite different from $\mathrm{AdS}$ spacetimes.</span></div></div>
</div>
