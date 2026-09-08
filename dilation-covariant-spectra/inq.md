---
inq.module: dilation-covariant-spectra
inq.include:
  - './'
keywords: [dilation covariance, self-adjoint operators, spectral gap, continuous spectrum, unitary symmetry]
---
# Dilation-Covariant Spectra

Exact unitary dilation covariance of a nonnegative self-adjoint operator on one Hilbert space forces its spectrum to be either trivial or the whole nonnegative half-line. If the dilation action is strongly continuous, it also excludes every positive eigenvalue, without a separability assumption. These conclusions concern a fixed operator and carrier; a unit change or a comparison between different scaled operators is a different assertion.

## A gap obstructs exact same-carrier dilation covariance

Let \(A\ge0\) be self-adjoint on a complex Hilbert space \(\mathcal H\), and let \(s\mapsto V_s\) be a unitary representation of \(\mathbb R\) on that same space satisfying

$$
V_sAV_s^*
=
e^{-s}A
\qquad
\text{for every }s\in\mathbb R.
\tag{D}
$$

This is equality of self-adjoint operators, including \(V_sD(A)=D(A)\), not merely a formal relation on unspecified test vectors. The spectral conclusion below needs unitary equivalence for every real \(s\); strong continuity is an additional hypothesis for the eigenvalue corollary.

Unitary equivalence gives \(\sigma(A)=e^{-s}\sigma(A)\). If \(A\ne0\), its spectrum contains some \(\lambda>0\). The orbit \(\{e^{-s}\lambda:s\in\mathbb R\}\) is all of \((0,\infty)\), and closedness adds zero. Therefore

$$
\boxed{
A=0
\quad\text{or}\quad
\sigma(A)=[0,\infty).}
\tag{D0}
$$

A nonzero operator satisfying (D) has no positive interval separating zero from its positive spectral support. The alternative \(A=0\) has no positive excitation spectrum. No ground-state multiplicity has been specified.

## A discrete exact rescaling also excludes a gap

If a single unitary \(V\) satisfies \(VAV^*=qA\) as self-adjoint operators for a fixed \(q>0\), \(q\ne1\), then the spectrum is invariant under \(q^n\), \(n\in\mathbb Z\). Any positive spectral value therefore has an orbit approaching zero. This already forbids a positive gap when \(A\ne0\), although it need not fill the entire positive half-line or exclude positive eigenvalues. Selecting a discrete dilation orbit is thus insufficient by itself to produce a gapped generator.

## Strong continuity excludes positive eigenvalues

Assume additionally that \(s\mapsto V_s\) is strongly continuous. If \(A\psi=\lambda\psi\) for \(\lambda>0\) and \(\psi\ne0\), the domain equality and (D) imply
\[
A(V_s\psi)=e^s\lambda V_s\psi.
\]
For every \(s\ne0\), self-adjointness makes \(V_s\psi\) orthogonal to \(\psi\). Hence \(\|V_s\psi-\psi\|^2=2\|\psi\|^2\), contradicting strong continuity at zero. Thus the positive spectrum has no point eigenvalues. This proof does not require \(\mathcal H\) to be separable; zero eigenvectors are not excluded.

## The covariance must act on the claimed operator

Changing a unit basis changes numerical representatives, not the fixed operator's spectrum. A relation between operators on different Hilbert carriers also does not supply (D). The theorem applies only when the comparison is realized as the stated unitary symmetry of one operator, including its domain. Choosing another vector in that representation does not alter the spectrum; changing the physical carrier or restricting to a sector requires a new operator and a fresh check of dilation covariance.
