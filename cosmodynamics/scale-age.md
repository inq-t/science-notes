# Scale-Age and Cosmic History

The e-fold $N=\ln(a/a_*)$ is the natural additive coordinate on multiplicative changes of a positive scale factor. It measures scale-age rather than elapsed proper time: it orders a monotonic cosmological branch by accumulated ratios, but it neither supplies a physical clock on every worldline nor derives the branch's temporal orientation. [[conformal-scale-geometry/scale-coordinate-reference|The scale-coordinate ledger]] separately fixes how a reference epoch and a distinguished crossing enter this notation.

## Logarithmic composition

Positive scale ratios compose multiplicatively,

$$
\frac{a_3}{a_1}
=\frac{a_3}{a_2}\frac{a_2}{a_1}.
$$

Their logarithms compose additively,

$$
N_{31}=N_{32}+N_{21},
\qquad
N_{ji}:=\ln\frac{a_j}{a_i}.
$$

Thus $N$ is a group coordinate on positive global rescalings. On an expanding FLRW branch,

$$
\frac{\mathrm dN}{\mathrm dt}=H>0,
$$

so it can parameterize the background history.

## Four temporal quantities

Scale-age must remain distinct from:

- proper time $\tau$, measured along a timelike worldline;
- [[conformal-time/inq|conformal time]] $\eta$, defined by $\mathrm d\eta=\mathrm dt/a(t)$;
- [[misner-log-time/inq|Misner logarithmic time]] $\Omega=-\ln(a/a_*)$, often used as an internal clock on a monotonic Hamiltonian-cosmology branch; and
- modular parameters, which label automorphisms associated with an algebra and state.

Relations among these variables depend on the metric solution, lapse, branch, and chosen state. Equality of notation or dimensionlessness would not identify them.

## Coordinate does not give an arrow

The same FLRW solution can be parameterized by $N$ or $-N$. A monotonic coordinate labels an already oriented branch; it does not explain why that branch is realized, why records accumulate in one direction, or why different observers share the orientation. Those are obligations of [[fact-record-history]] and [[sufficient-reason/algebraic-arrow-of-time|the algebraic arrow programme]].

## Horizon allocation

For the flat expanding FLRW apparent horizon, define a signed horizon index $\widehat\mu_A$ and signed rapidity by

$$
\frac{\mathrm d\widehat\zeta_A}{\mathrm dN}=\widehat\mu_A.
$$

With $\mathcal S_A=S_A/k_B\propto H^{-2}$, the geometric identities give

$$
\boxed{
\mathrm dN
=\mathrm d\widehat\zeta_A
+\frac14\,\mathrm d\ln\mathcal S_A
}.
$$

This allocates one e-fold between a signed surface-gravity rapidity and horizon-entropy growth under the stated FLRW definitions. It does not identify $\widehat\zeta_A$ with proper time, horizontal state displacement, or fact formation. The sign conditions are kept in [[conformal-scale-geometry/horizon-allocation|the horizon-allocation note]], while [[causal-scale-theory/horizontal-temperature|the horizontal-temperature note]] keeps the distinct temperature notions separate.
