# Three-Dimensional Stress-Tensor Response

The QFT datum in holographic cosmology is the renormalized response of a three-dimensional Euclidean stress tensor to a boundary metric source. Homogeneity and isotropy split its parity-even two-point function into independent spin-two and spin-zero form factors \(A\) and \(B\); the trace contraction is exactly \(4B\), while the relation of these coefficients to bulk response functions requires gauge/gravity duality and holographic renormalization.

## Tensor decomposition

Strip the momentum-conserving delta function and define

$$
\pi_{ij}:=\delta_{ij}-\frac{q_iq_j}{q^2},
\qquad
\Pi_{ijkl}
:=\pi_{i(k}\pi_{l)j}
-\frac12\pi_{ij}\pi_{kl}.
$$

For a parity-even homogeneous and isotropic state,

$$
\boxed{
\langle\!\langle
T_{ij}(q)T_{kl}(-q)
\rangle\!\rangle
=A(q^2)\Pi_{ijkl}
+B(q^2)\pi_{ij}\pi_{kl}.}
$$

Because \(\delta^{ij}\pi_{ij}=2\) in three dimensions and the transverse-traceless projector has zero trace,

$$
\boxed{
\langle\!\langle T(q)T(-q)\rangle\!\rangle
=4B(q^2),
\qquad T:=T^i{}_i.}
$$

This contraction is **[EXACT]** in the displayed convention. It does not say that \(B\) is nonzero at a conformal fixed point, that the trace coefficient is a central charge, or that the same operator generates a four-dimensional Weyl deformation.

## Holographic response

In a bulk domain-wall solution, scalar and tensor radial canonical momenta admit response expansions. Holographic renormalization extracts the finite dilatation-weight component of these momenta and relates it to the renormalized QFT one-point function. At linear order this gives \(A\) and \(B\) in terms of the asymptotic tensor and scalar bulk responses. The exact coefficient attached to intermediate response symbols depends on their canonical normalization; the \(A,B\) convention above and the final spectrum convention in [[vendor/holographic-cosmology/scalar-and-tensor-spectra|the spectrum dictionary]] are held fixed here.

The radial Hamiltonian construction is developed in [[library/correlation-functions-in-holographic-rg-flows/entry|Papadimitriou--Skenderis]]. The counterterm and source-response framework is developed in [[library/holographic-renormalization/entry|de Haro--Solodukhin--Skenderis]].

## Contact terms and spectral data

Local covariant counterterms change \(A\) and \(B\) by scheme-dependent local functions, polynomial in momentum in the flat setting. Such polynomials have no discontinuity across the nonlocal spectral cut. Under the required analyticity and growth assumptions, the discontinuity or imaginary part after continuation therefore isolates the nonlocal spectral response relevant to the cosmological dictionary.

The qualified implication is one-way:

$$
\text{local polynomial counterterm}
\Longrightarrow
\operatorname{Disc}=0.
$$

The converse requires a dispersion theorem and cannot be inferred from the symbol \(\operatorname{Disc}\). Boundary terms, anomalies, parity-odd structures, and semilocal contributions at higher point require separate treatment.

## What a member must calculate

A proposed QFT member must independently return

$$
A_{\mathrm{calc}}(q^2),
\qquad
B_{\mathrm{calc}}(q^2),
$$

with a declared action, state, regulator, renormalization prescription, and continuation. Defining \(A\) or \(B\) backward from a measured cosmological spectrum produces a useful target but is not a holographic calculation.
