# Registers and Type Discipline

Cosmodynamics begins by assigning different mathematical types to structures that ordinary exposition often compresses into one variable called time, scale, state, or information. Its central method is not to forbid relations among these registers, but to require an explicit map whenever one kind of object is made to determine another.

## The principal registers

| Register | Typical object | What it supplies |
|---|---|---|
| Causal order | relation $p\preceq q$ | possible influence and temporal precedence |
| Conformal geometry | class $[g]$ | null cones and angle structure |
| Metric scale | positive section $\sigma$ or representative $g$ | local calibration of lengths and durations |
| Proper time | $\tau[\gamma]$ along a timelike curve | elapsed clock duration |
| Scale history | $N=\ln(a/a_*)$ | accumulated multiplicative change of scale |
| Modular flow | $\sigma_s^\omega$ | automorphisms at fixed algebra and state |
| State deformation | $N\mapsto\omega_N$ | motion through a family of states |
| Quantum state | positive normalized functional $\omega$ | expectations and contextual probabilities |
| Readout fact | character or outcome in a context | a definite contextual value |
| Information | dimensionless distinguishability or coding quantity | comparison of possibilities and records |
| Entropy | state or algebra-dependent quantity, with physical units via $k_B$ | thermodynamic or information-theoretic accounting |
| Energy | generator or conserved charge relative to a chosen flow | rate and capacity for change in that structure |

These types overlap in controlled theories, but they are not synonyms.

## Explicit soldering maps

Causal structure fixes a Lorentzian metric only up to conformal factor under the usual hypotheses. A positive scale section selects a representative,

$$
([g],\sigma)
\longmapsto
g_{\mathrm{phys}}=\sigma^{-2}\boldsymbol g.
$$

This exact kinematic equivalence motivates, but does not prove, the claim that scale is an independently dynamical register. The relevant distinction is maintained in [[conformal-scale-geometry/causal-order-and-metric-scale|causal order and metric scale]].

Likewise, modular evolution

$$
A\longmapsto\sigma_s^\omega(A)
$$

at fixed $(\mathcal A,\omega)$ is different from a family

$$
N\longmapsto(\mathcal A_N,\omega_N).
$$

Comparing the latter requires inclusions, transports, relative modular data, or another connection. [[wall-construction-interface/vertical-and-horizontal-motion|Modular flow and state deformation]] owns this distinction.

For a commutative readout context $\mathcal D\subseteq\mathcal M$, state restriction gives a measure on $\operatorname{Spec}(\mathcal D)$; it does not give a selected point. [[sufficient-reason/quantum-interpretations|Quantum interpretation and the type change]] states the missing outcome map precisely.

## Characteristic type errors

The following identifications require arguments and are generally false without them:

$$
\begin{aligned}
\text{causal order}&\ne\text{metric duration},\\
[g]&\ne g_{\mathrm{phys}},\\
N&\ne\tau\ne s,\\
\text{modular flow}&\ne\text{state deformation},\\
\text{probability law}&\ne\text{actual outcome},\\
\text{correlation functional}&\ne\text{ontic random mechanism},\\
\text{choice of energy zero}&\ne\text{gravitational source},\\
\text{phenomenological fit}&\ne\text{microscopic derivation}.
\end{aligned}
$$

Ontological type checking is successful only when it exposes a constructive obligation. Merely renaming familiar objects with separate vocabulary produces no new physics.
