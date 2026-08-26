# Trace-Fixed-Point Null No-Go

At a strict improved three-dimensional conformal fixed point with no relevant boundary, defect, virial, or anomaly contribution, the nonlocal stress-trace response vanishes. Any model that identifies scalar precision solely with a finite multiple of that trace response therefore has a null, noninvertible scalar kernel at the fixed point; the null direction is not automatically gauge.

## Conditional statement

Assume a three-dimensional Euclidean QFT has:

1. an improved conserved stress tensor;
2. exact conformal invariance at the point under consideration;
3. no boundary, defect, virial-current, or other contribution to the trace in the sector being used;
4. no relevant anomaly contribution to the nonlocal separated-point trace response; and
5. a regular continuation and finite normalization for the scalar channel.

Then, away from contact terms,

$$
T^i{}_i=0,
$$

so the nonlocal trace--trace response vanishes:

$$
\langle T(k)T(-k)\rangle_{\mathrm{nonlocal}}=0.
$$

If a proposed member additionally identifies its physical scalar precision only through

$$
\mathcal K_\zeta(k)=Z\,\rho_T(k)
$$

with finite \(Z>0\) and \(\rho_T\) the continued nonlocal trace response, then

$$
\boxed{\mathcal K_\zeta(k)=0}
$$

on that channel at the exact fixed point. It follows that \(\mathcal K_\zeta^{-1}\) does not exist there.

This is **[NO-GO]** for a finite, invertible scalar precision obtained solely from a regular strict-fixed-point stress trace under the stated assumptions.

## Null does not mean gauge

The conclusion is noninvertibility, not gauge redundancy. A null response can mean several different things:

- the proposed operator is absent at the fixed point;
- the source direction is redundant or pure gauge;
- the state family is singular or nonfaithful there;
- a finite-normalization hypothesis fails;
- an omitted boundary, defect, virial, or anomaly term is load-bearing; or
- the trace-to-precision identification is wrong.

Only an independent symmetry, constraint, or equivalence construction can establish that the null direction should be quotiented as unphysical. Deleting it merely to permit inversion would reverse the explanatory order required by [[program-core/physical-quotient|the physical quotient]].

## Controlled escape routes

Along a deformation one may have schematically

$$
T^i{}_i
=\beta^I\mathcal O_I
$$

up to the excluded terms. Then

$$
\langle TT\rangle
\sim
\beta^I\beta^J
\langle\mathcal O_I\mathcal O_J\rangle.
$$

A finite near-critical response can arise if the beta functions are nonzero, or in a controlled double scaling in which operator normalizations grow while beta functions shrink. Such a limit must be derived; it is not implied by the words *near conformal*. The deformed-CFT cosmology of [[library/on-the-power-spectrum-of-inflationary-cosmologies-dual-to-a-deformed-cft/entry|McFadden]] is a concrete literature setting in which the trace channel is tied to a deformation rather than a literal nonzero fixed-point trace.

## Failure signature

A microscopic construction that reaches an exact trace-free point while retaining no independently justified scalar operator cannot claim an infinite observable covariance from the formal reciprocal of zero. It has instead reached the boundary of the scalar trace representation. Whether the physical theory quotients, replaces, or deforms that channel is a separate decision.
