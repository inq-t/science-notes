# Exact Wilson Interface Statistics

A finite Wilson law can be reduced exactly to the regional data entering its cross plaquettes. This removes both discarded-core and boundary-leakage losses without a small-coupling assumption. It does not remove the interacting problem: the induced interface law retains the bulk free energies, relative gauge frames and, after collar integration, potentially nonlocal dependence.

**Status: [EXACT FINITE-LAW FACTORIZATION AT ARBITRARY FINITE COUPLING]; [OPEN] for a useful continuum interface estimate and physical midpoint reconstruction.**

## Factor the interaction, not a preferred average

Use the active raw-link split \(Y,Z\), fixed exterior configuration, product Haar measure and Wilson normalization of [[nonlinear-conditional-gauge-response|the nonlinear conditional law]]. Assign every plaquette term to a \(Y\)-only term, a \(Z\)-only term, or a cross term according to its active-link dependence.

Let \(T(Y)\) retain the \(Y\)-links occurring in cross plaquettes and \(S(Z)\) the corresponding \(Z\)-links. Then exactly
\[
S_\beta(Y,Z)=S_Y(Y)+S_Z(Z)+C(T(Y),S(Z)).
\tag{WI1}
\]
No curvature or perturbation estimate is used. Empty interfaces mean the original regions are independent.

Define the normalized regional reference laws
\[
\pi_Y\propto e^{-S_Y}dY,\qquad \pi_Z\propto e^{-S_Z}dZ.
\]
The actual interface law is
\[
\boxed{
\eta(dt,ds)=
\frac{e^{-C(t,s)}\,T_*\pi_Y(dt)\,S_*\pi_Z(ds)}
{\int e^{-C}\,d(T_*\pi_Y)\,d(S_*\pi_Z)}.}
\tag{WI2}
\]
The conditional laws \(\pi_Y(dY\mid t)\), \(\pi_Z(dZ\mid s)\) do not depend on the opposite region. Therefore [[bridge-data-augmentation-solder/predictive-sufficient-interfaces|predictive sufficiency]] gives
\[
\boxed{B_{Y,Z}\simeq B_{T,S}\oplus I,\qquad
\kappa_{Y,Z}=\kappa_{T,S}.}
\tag{WI3}
\]
In the relative lifting theorem, \(b=1\) and \(r_\partial=0\). This is an equality of complete response operators on the actual marginal Hilbert spaces, not a Gaussian tangent calculation.

For coordinate interfaces, \(T_*\pi_Y\) and \(S_*\pi_Z\) have positive densities relative to their product-Haar coordinate measures at finite volume. They are generally not Haar laws. Smaller transport statistics may have constrained or singular images. The measure-theoretic theorem covers such images, but a differential Fisher theorem requires their actual metric and form domain.

## Noncommuting transport order cannot be forgotten

One may retain each maximal same-region run in each cyclic cross-plaquette word instead of every raw link. Keep each run's order, orientation and endpoints. For a single active link, the complementary runs combine into the familiar matrix-valued staple. General alternating cuts need more information.

For example, the cross word
\[
\operatorname{Tr}(A_1B_1A_2B_2)
\]
is not determined by \(A_1A_2\) and \(B_1B_2\). In \(SU(2)\), take
\[
A_1=A,\ A_2=A^{-1},\quad B_1=B,\ B_2=B^{-1},
\qquad A=i\sigma_x,\quad B=i\sigma_z.
\tag{WI4}
\]
Both same-region products are identity, but the cross commutator is \(-I\). With \(A_1=A_2=I\), the same retained products give cross holonomy \(I\). Their Wilson cross energies differ. These are admissible values of a plaquette's independent edge transports; the matrix assignment is a counterexample to reordering, not a spacetime dynamics.

Open transports transform at their endpoints. Shared boundary frames are part of the coupling. Independently quotienting each region by endpoint transformations can erase the very distinctions needed to evaluate \(C\). With fixed exterior links, covariance is understood under transformation of that background as well, or under its stabilizer.

The criterion differs from [[thin-skeleton-and-block-average-coercivity|a sparse coarse skeleton]]: retain all cross-predictive dependence, not merely an exactly disintegrable selection of paths.

## Exact reduction is not a closed effective theory

The regional measures in (WI2) include all integrated interior self-interactions. They need not be Wilson measures on a smaller lattice or factor over interface cells. Thus the exact equality does not supply a dimension-free or regulator-uniform estimate for \(B_{T,S}\).

If a collar \(H\) is integrated between a prescribed core \(C_0\) and boundary \(D_0\), the relevant potential is instead
\[
V_{\rm eff}(c,d)=-\log\int e^{-S_\beta(c,h,d)}\,dh.
\tag{WI5}
\]
Its cross dependence can involve every retained coordinate. [[collared-quasi-factorization-and-surface-response/fisher-collar-bound-for-wilson-laws|The Fisher collar estimate]] controls a mixed operator norm under its hypotheses; it does not prove a finite-rank sufficient statistic. The [[gaussian-bridge-gap-calibration/predictive-rank-and-physical-separation|Gaussian Schur example]] makes that distinction exact.

For a whole slab interior, the raw cross interface sits next to its outer boundary. It is not the midpoint separated from that boundary by a fixed physical length. A complete all-interior response floor can vanish as lattice spacing shrinks even in a gapped Gaussian model. A sufficient lower bound on a larger carrier is valid when available, but its failure cannot be promoted to a failure of the midpoint mass-gap test.

The useful route is therefore conditional: construct the predictive interface for the actual separated midpoint law, keep its induced measure and gauge framing, then prove a complete norm bound. [[bridge-data-augmentation-solder/predictive-sufficient-interfaces|Discarded-prediction control]] also permits an approximate interface when exact retention is too large. Neither route follows from cross-plaquette counting alone.

[[bridge-data-augmentation-solder/receipts/predictive_interface_receipt.py|The finite receipt]] verifies interacting interface factorizations and the noncommuting transport counterexample. It does not prove an interacting continuum bound.
