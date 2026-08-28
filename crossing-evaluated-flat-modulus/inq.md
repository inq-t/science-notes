---
inq.module: "crossing-evaluated-flat-modulus"
inq.include:
  - "**/*.md"
---
# The Crossing-Evaluated Flat Modulus

A crossing-selected gravitational calibration is most coherently typed as a scalar on the space of whole cosmological solutions, not as an instantaneous function of the Hubble rate. Once a presentation-natural event selector exists, evaluating the apparent-horizon radius at that event produces a scalar whose pullback is constant along each cut fiber. This removes the false implication that Newton's coupling switches or runs when the crossing occurs, but it does not select the crossing, calculate the modulus, or prove the state--geometry weld.

## The meaning

A fossil is not a substance left behind at one moment. It is a **global address evaluated at a distinguished event**.

Here **flat** means fiberwise constant: the pulled-back scalar has zero derivative in every direction vertical for \(\pi\). It does not mean that a horizontal connection annihilates it, that \(\pi\) is a flat morphism in algebraic geometry, that a connection has zero curvature in every direction, or that the spacetime metric is flat.

The distinction matters because the two expressions

$$
\chi(N)=\zeta\frac{R_A(N)}{\lambda_*^3}
$$

and

$$
\chi_{\mathrm{foss}}[\gamma]
=\zeta[\gamma]\frac{R_A(\Sigma_c[\gamma])}{\lambda_*[\gamma]^3}
$$

have the same dimensions and radically different types. The first is a live constitutive law on cuts and ordinarily implies a varying gravitational coupling. The second assigns one number to an entire solution \(\gamma\). Later cuts do not re-evaluate it.

This is the Copernican point. A local observer meets the same coefficient at every event, while the coefficient may encode a presentation-invariant feature of the whole history. No local time is privileged as the instant at which the laws of nature were rewritten.

## Cut space and solution space

Let \(\mathsf{Sol}\) be a space, groupoid, or stack of admissible cosmological solutions after gauge equivalence has been declared. Let \(\mathsf{Cut}\) be the corresponding family of admissible causal cuts, with projection

$$
\pi:\mathsf{Cut}\longrightarrow\mathsf{Sol}.
$$

In a homogeneous chart, a point of \(\mathsf{Cut}\) may be written \((\gamma,N)\), where \(N\) is the logarithmic scale coordinate of [[misner-log-time/inq|Misner scale age]]. A distinguished-event rule is a section

$$
c:\mathsf{Sol}\longrightarrow\mathsf{Cut},
\qquad
\pi\circ c=\operatorname{id}_{\mathsf{Sol}},
$$

so that \(c(\gamma)=\Sigma_c[\gamma]\). The section must be natural under the chosen presentation equivalences. A fitted decimal \(N_c\) is not yet such a section; [[causal-scale-theory/conjectures/event-locus-coincidence|the event-locus conjecture]] states the missing selection theorem.

This is an instance of the warning in [[basic-concepts/fibers/inq|fibers and families]]: a datum on one fiber does not extend across a family without transport, a section, or a connection. [[causal-scale-theory/reference-cut-matching-ratio|The reference-cut matching ratio]] separately distinguishes reference-cut evaluation from factual character evaluation.

Let \(R_A:\mathsf{Cut}\to\mathbb R_{>0}\) be the apparent-horizon radius, and let \(\lambda_*\) and \(\zeta\) be positive scalars on \(\mathsf{Sol}\). Define

$$
\boxed{
\chi_{\mathrm{foss}}
:=
\zeta\lambda_*^{-3}c^*R_A
}
$$

on \(\mathsf{Sol}\). It has dimensions \(L^{-2}\).

## Fiber-flatness lemma

First take \(\mathsf{Cut}\) and \(\mathsf{Sol}\) to be ordinary smooth spaces. For every vertical vector field

$$
V\in\ker(\mathrm d\pi),
$$

one has

$$
\boxed{
V\bigl(\pi^*\chi_{\mathrm{foss}}\bigr)=0.
}
$$

In a chart \((\gamma,N)\) adapted to the fibers, this is

$$
\partial_N\bigl(\pi^*\chi_{\mathrm{foss}}\bigr)=0.
$$

**Proof.** The pullback \(\pi^*\chi_{\mathrm{foss}}\) factors through \(\pi\), so \(\mathrm d(\pi^*\chi_{\mathrm{foss}})=\pi^*(\mathrm d\chi_{\mathrm{foss}})\). If \(V\in\ker(\mathrm d\pi)\), then \(V(\pi^*\chi_{\mathrm{foss}})=\mathrm d\chi_{\mathrm{foss}}(\mathrm d\pi(V))=0\). \(\square\)

The lemma is elementary because the substantive work has been isolated in the type of the definition. It says neither that \(\chi_{\mathrm{foss}}\) is constant across different solutions nor that nature realizes this assignment.

For a solution groupoid or differentiable stack, the corresponding statement must be made for an invariant function on an atlas and checked to descend under the groupoid action. The elementary differential proof above does not by itself establish stack-level descent.

Four notions of constancy must remain distinct:

| Notion | Required statement |
|---|---|
| flat along one cut fiber | \(V\pi^*\chi_{\mathrm{foss}}=0\) for every \(V\in\ker(\mathrm d\pi)\) |
| invariant under presentation | \(\chi_{\mathrm{foss}}[g\cdot\gamma]=\chi_{\mathrm{foss}}[\gamma]\) for declared equivalences \(g\) |
| common to a connected physical sector | one value on a specified family of solutions |
| universal constant | one value in every admissible realization |

Only the first follows from the definition. The second requires a natural selector and invariant ingredients. The last two are physical claims.

## Conditional fossil--Einstein closure

For a flat expanding FLRW branch, \(R_A=c/H\). If the carrier ruler is the reduced Compton length

$$
\lambda_*:=\frac{\hbar}{m_*c},
$$

then the crossing-evaluated modulus is

$$
\chi_{\mathrm{foss}}
=\zeta\frac{c}{H_c\lambda_*^3}.
$$

If, in addition, the independently constructed state modulus is proved equal to the Einstein entropy--area density

$$
\eta_E:=\frac{c^3}{4\hbar G},
$$

then

$$
\boxed{
G_\gamma
=\frac{c^3}{4\hbar\chi_{\mathrm{foss}}[\gamma]}
=\frac{\hbar^2H_c[\gamma]}
{4\zeta[\gamma]c\,m_*[\gamma]^3}.
}
$$

This is the fossil-Weinberg closure of [[deriving-g-v2/closure-family-and-kills|the closure-family audit]], correctly retyped. It is a conditional deduction, not a numerical derivation of \(G\): the event selector, carrier, coefficient, and [[program-core/causal-capacity-equivalence|state--geometry equivalence]] must all be obtained without using measured \(G\).

The value applies to the whole Einstein history. There is no pre-crossing \(G\), jump at \(N_c\), or signal sent backward from the event. [[bianchi-protection-of-the-areal-modulus/inq|Bianchi protection]] gives a separate consistency theorem: within an ordinary nonvacuum Einstein fiber, a freely varying coupling is incompatible with the stated conservation assumptions. It does not transport data through the wall.

## The wall between the two reasons

[[sufficient-reason/inq|Sufficing and necessitating reason]] do not name two unexplained fluids or two pre-existing regions of spacetime. In this programme's typing, a sufficing reason terminates in a probability measure on a contextual spectrum, while a necessitating reason terminates in a character that fixes the contextual fact.

The crossing section \(c\) therefore cannot be obtained merely by renaming a probability maximum. A wall construction must specify how a state, context, instrument, realized fact, and persistent record make the distinguished event factual. [[conservation-of-causal-charge/factive-descent-and-records|Factive descent]] owns that missing type change. The solution-space lemma begins after such a selector has been supplied; it does not perform the selection.

The reversible symmetries of presentation may still organize \(\mathsf{Sol}\) as a groupoid or stack. If the crossing cycle is constructed equivariantly and transported under a groupoid Morita equivalence with compatible coefficient data, assembly can carry its topological invariance to an analytic index class. Baum--Connes does not independently prove that an arbitrarily proposed crossing observable is presentation-invariant. [[flux-record-and-top-form-realizations/inq|The assembly and flux module]] explains why assembly cannot select the event or turn a probability law into a character.

## Three observational shadows

The same proposed modulus can appear in three registers without those appearances being three independent derivations.

| Register | Exact or conditional expression | What is actually learned |
|---|---|---|
| Planck translation | \(\ell_\chi=1/(2\sqrt{\chi})\); if \(\chi=\eta_E\), then \(\ell_\chi=\ell_P\) | a positive modulus generates a unit family; measured \(G\) merely translates it |
| Schwarzschild restriction | \(\eta_E=cM/(2\hbar r_s)\), using \(r_s=2GM/c^2\) | the same coefficient governs compactness and horizon area in the imported Einstein fiber |
| calibrated redshift history | \(H_c=H_0E(z_c)\) and \(\chi_{\mathrm{foss}}=\zeta c/(H_c\lambda_*^3)\) | a declared profile and selector infer \(z_c\) from the distance curve; absolute calibration then supplies the rate |

Uncalibrated supernovae constrain the dimensionless luminosity-distance curve, an integral of \(1/E(z)\), while projecting out the absolute magnitude--\(H_0\) degeneracy. They do not locate \(z_c\) or determine \(E(z)\) model-independently. A parametric forward fit can infer both only after a profile and event selector define what counts as the crossing; absolute calibration then supplies \(H_0\) and hence \(H_c\). [[causal-scale-theory/receipts/fit-calibrated-background|The calibrated-background receipt]] makes the distinction explicit. Supernovae do not directly observe a BKM metric, an assembly class, a causal charge, or the fossil modulus.

## Flux without running

The current horizon area and its ledger may change even though the crossing-evaluated modulus is flat:

$$
\iota_A(N)=\eta_EA(N),
\qquad
\partial_N\iota_A\ne0,
\qquad
\partial_N\eta_E=0.
$$

This is not a contradiction. An extensive quantity can change because its carrier area changes while its density remains fixed. [[bulk-area-cell-normalization/inq|Bulk--area normalization]] identifies the corresponding cell factors, while [[flux-record-and-top-form-realizations/inq|the flux module]] separates physical boundary flux from record persistence, top-form flux, and K-theoretic transgression.

## What remains to be constructed

The proposal becomes explanatory only if one construction supplies:

1. a presentation-natural event selector \(c\), rather than a cut fitted after the fact;
2. an independently identified carrier \(m_*\) and its physical ruler \(\lambda_*\);
3. the bulk-to-boundary coefficient \(\zeta\), including species and packing data;
4. a finite, regulator-independent horizontal BKM modulus on the selected wall;
5. the noncircular weld \(\chi_{\mathrm{foss}}=\eta_E\); and
6. universality across local focusing, Schwarzschild horizons, lensing, waves, and cosmology.

Failure of the fossil closure would not invalidate the solution-space lemma. It would show that nature does not use this event-evaluated scalar as its gravitational calibration.
