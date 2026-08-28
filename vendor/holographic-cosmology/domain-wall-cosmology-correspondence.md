# The Domain-Wall/Cosmology Correspondence

The domain-wall/cosmology correspondence pairs homogeneous cosmological solutions with domain-wall solutions after a controlled analytic continuation that reverses the relevant potential and curvature signs. In the spatially flat single-scalar case the pairing extends to perturbation equations and response functions; this classical correspondence is the first stage of holographic cosmology, not itself a gauge/gravity duality.

## Background pairing

Consider gravity coupled to scalar fields. A domain wall has a transverse spatial coordinate, whereas an FLRW cosmology has a time coordinate. After symmetry reduction, both systems can be written in one one-dimensional formalism with a sign parameter distinguishing the two signatures. The reduced equations pair a domain-wall solution with potential \(V\) with a cosmological solution with potential \(-V\); for nonflat slicings the curvature sign is reversed as well.

In the notation of [[library/pseudo-supersymmetry-and-the-domain-wall-cosmology-correspondence/inq|Skenderis and Townsend]], the continuation exchanges the transverse coordinate and cosmological time and maps the scalar profile accordingly. This is a correspondence between solutions of related theories. It does not assert that the wall worldvolume literally is the cosmological spatial slice.

For a four-dimensional spatially flat single-scalar member, write

$$
\mathrm ds^2
=\eta\,\mathrm dz^2
+a^2(z)\bigl(\delta_{ij}+h_{ij}\bigr)
\mathrm dx^i\mathrm dx^j,
\qquad
\Phi=\varphi(z)+\delta\varphi,
$$

with \(\eta=-1\) for cosmology and \(\eta=+1\) for the Euclidean domain wall. A fake-superpotential description of a monotone background gives first-order equations for \(a\) and \(\varphi\). Monotonicity and the existence of the required asymptotic region are substantive restrictions, not notation.

## Perturbations

The scalar variable used by the correspondence is already the standard gauge-invariant cosmological curvature perturbation,

$$
\zeta
=\psi+\frac{H}{\dot\varphi}\,\delta\varphi,
$$

together with the transverse-traceless metric perturbation \(\gamma_{ij}\). Their linearized equations can be continued between the cosmology and domain wall by

$$
\boxed{
\bar\kappa^2=-\kappa^2,
\qquad
\bar q=-iq,}
$$

where barred quantities belong to the Euclidean domain-wall description. The momentum branch is selected so that positive-frequency Bunch--Davies behavior maps to a solution regular in the domain-wall interior.

This extension to perturbations is **[CONDITIONAL THEOREM]** within the single-clock class analyzed in [[library/holography-for-cosmology/inq|Holography for Cosmology]]. A background correspondence alone would not imply it.

## Response functions

Let the canonical momenta of scalar and tensor perturbations be written as

$$
\Pi_q^{(\zeta)}=\Omega(q,z)\zeta_q,
\qquad
\Pi_q^{(\gamma)}=E(q,z)\gamma_q.
$$

After the state and mode normalization have been fixed, the late-time imaginary parts of \(\Omega\) and \(E\) determine the cosmological two-point functions. Their domain-wall analogues are real before continuation and are read holographically from renormalized radial canonical momenta. The continuation relates the domain-wall and cosmological response functions; it does not identify an arbitrary Euclidean correlator with a Lorentzian observable.

## Domain of the original result

The most controlled original classes are:

- asymptotically AdS domain walls, corresponding to cosmologies asymptotically de Sitter in the relevant regime;
- asymptotically power-law domain walls associated with generalized conformal structure; and
- their single-scalar perturbations, with regular domain-wall interior data mapping to the selected cosmological state.

Multifield, noncanonical, nonflat, or nonperturbative extensions require their own construction. The correspondence is broader than exact de Sitter/AdS continuation but narrower than a universal statement about every FLRW spacetime.
