# Local Observables from the Boundary Response

The harmonic boundary response can support a local observable algebra even though compressed multiplication fails locality. Its real quadratic form and orientation determine an antisymmetric derivative pairing; a bosonic Weyl realization turns this pairing into commuting algebras for disjoint boundary arcs. The same tangential derivative supplies their positive clock. This is an explicit local circle model with an additional CCR/Fock realization choice, not a four-dimensional interacting gauge theory.

## Change the observable realization, not the response

Use smooth real boundary symbols modulo constants,

\[
\mathscr V=C^\infty(S^1,\mathbb R)/\mathbb R,
\qquad
f(\theta)=\sum_n f_n e^{in\theta}.
\tag{LW1}
\]

The mean-zero representative is convenient for formulas. The response already derived from [[algebra/hardy-compression-and-boundary-response|Hardy compression]] is

\[
\mu(f):=\operatorname{Tr}\Delta_f
=\sum_{n>0}n|f_n|^2.
\tag{LW2}
\]

It vanishes precisely on constants before quotienting. It defines a real Hilbert norm after completion of (LW1).

The orientation operator \(J\) from [[harmonic-boundary-realization|the harmonic member]] acts as \(Jf_n=-i\operatorname{sign}(n)f_n\). Define the real-linear map

\[
\kappa f=(\sqrt n\,f_{-n})_{n\geq1}
\in\mathfrak h:=\ell^2(\mathbb N).
\tag{LW3}
\]

Then \(\|\kappa f\|^2=\mu(f)\), \(\kappa Jf=i\kappa f\), and \(\kappa\mathscr V\) is dense as a real subspace of \(\mathfrak h\). The real space equipped with this \(J\) and norm is therefore precisely the one-particle Hilbert space in a different presentation.

This differs from the earlier unweighted map \(\Phi\), which uses the boundary \(L^2\) norm. On mean-zero polynomials the maps obey

\[
\kappa=\sqrt{R/2}\,A^{1/2}\Phi.
\tag{LW4}
\]

The response is now the **one-particle norm**, not the one-particle energy in the old \(L^2\) norm. Changing the carrier's norm changes the type of the same quadratic expression; these two readings must not be interchanged.

## A nonlocal norm has a local antisymmetric partner

Pairing conjugate Fourier coefficients gives

\[
\boxed{
\sigma(f,g):=2\operatorname{Im}\langle\kappa f,\kappa g\rangle
=\frac1{2\pi}\int_0^{2\pi}f(\theta)g'(\theta)\,d\theta.}
\tag{LW5}
\]

Equivalently, \(\operatorname{Tr}[T_f,T_g]=i\sigma(f,g)\), by the same Hankel channel count that gives (LW2). The norm and this central commutation form are therefore the even and odd traced parts of the same compositional residue.

This is real, antisymmetric and independent of the representatives modulo constants. If it vanishes against every \(g\), the distributional derivative of \(f\) vanishes, so its class is zero.

In particular, \(\sigma(f,g)=0\) whenever smooth representatives have disjoint supports. The quadratic norm \(\mu\) involves \(|D|\) and is nonlocal in boundary position; its orientation-odd partner involves \(D\) and is local. The geometric relation between them is

\[
\mu(f)=\frac R2(f,Af)_R,\qquad
\sigma(f,g)=R(f,Dg)_R,\qquad
D=-JA.
\tag{LW6}
\]

The same real oriented derivative thus constrains both the positive state geometry and the commutation relation. We did not assume an unrelated symplectic space or choose a second operator to enforce locality.

## The additional realization choice

Choose the bosonic canonical-commutation-relations realization. On symmetric Fock space

\[
\mathcal F_s(\mathfrak h)
=\bigoplus_{m=0}^{\infty}\operatorname{Sym}^m\mathfrak h,
\tag{LW7}
\]

let \(\Omega\) be its degree-zero vector. The displacement operators \(W(f)\) obey

\[
W(f)W(g)=e^{-i\sigma(f,g)/2}W(f+g),
\qquad
W(f)^*=W(-f),
\tag{LW8}
\]

with

\[
\langle\Omega,W(f)\Omega\rangle=e^{-\mu(f)/2}.
\tag{LW9}
\]

These constants can be checked without a formal unbounded-field exponential. On coherent exponential vectors
\(\varepsilon(v)=\bigoplus_m v^{\otimes m}/\sqrt{m!}\), define

\[
W(f)\varepsilon(v)
=e^{-\|\kappa f\|^2/2-\langle\kappa f,v\rangle}
\varepsilon(v+\kappa f).
\tag{LW10}
\]

The identity \(\langle\varepsilon(u),\varepsilon(v)\rangle=e^{\langle u,v\rangle}\) proves this is an isometry with inverse \(W(-f)\); density gives a unitary. Applying (LW10) twice proves (LW8), and its vacuum matrix element is (LW9).

The Gaussian vacuum is positive because this Hilbert representation constructs it. Nothing here says that nature must choose Gaussian statistics, bosons or this vacuum representation. The CCR functor is an explicit additional modeling choice whose consistency and local return can now be tested.

The vacuum line is the empty-particle sector of (LW7), not the complexification of a real constant boundary function. Constants were quotiented out of the source space and act trivially in (LW8).

## Locality and the clock are actual operator statements

For a proper open arc \(I\), set

\[
\mathcal A(I)
:=\{W(f): f\text{ has a smooth real representative supported in }I\}^{\prime\prime}.
\tag{LW11}
\]

The double commutant is taken in \(B(\mathcal F_s(\mathfrak h))\). Inclusion of arcs gives inclusion of algebras. If \(I\cap J=\varnothing\), (LW5) and (LW8) imply

\[
[\mathcal A(I),\mathcal A(J)]=0.
\tag{LW12}
\]

Every nonempty arc supplies a nontrivial algebra: a nonconstant supported \(f\) has \(\mu(f)>0\), so the modulus of (LW9) is strictly less than one and \(W(f)\) cannot be a scalar unitary. Support is imposed on a representative before passing to the quotient; subtracting its mean need not preserve support.

This is exact commuting locality on the circle, not merely a support label attached to noncommuting compressed effects. It does not equate these Weyl operators with \(P_-M_fP_-\).

Let \(\tau_s f(\theta)=f(\theta+s/R)\). The already determined translation has

\[
\kappa\tau_s f=U_s\kappa f,\qquad
(U_sz)_n=e^{-ins/R}z_n.
\tag{LW13}
\]

Second quantization gives

\[
\mathbb U_s=\Gamma(U_s)=e^{-is\mathbb H_R},\qquad
\mathbb H_R=d\Gamma(K_R),\qquad K_Rz=(n/R)z_n,
\tag{LW14}
\]

and, directly from (LW10),

\[
\mathbb U_sW(f)\mathbb U_s^*=W(\tau_s f),
\qquad
\mathbb U_s\mathcal A(I)\mathbb U_s^*
=\mathcal A(I-s/R).
\tag{LW15}
\]

The sign in the last formula follows from the declared argument shift. No independent field Hamiltonian is appended.

The vacuum is globally cyclic: \(W(f)\Omega\) is a nonzero scalar multiple of \(\varepsilon(\kappa f)\), and \(\kappa\mathscr V\) contains all finite complex sequences, since arbitrary negative coefficients extend to real symbols. Exponential vectors over this set are total. This proves the stated global cyclicity, not additional local cyclicity or a full set of spacetime axioms.

On the occupation-number basis, \(\mathbb H_R\) has the maximal self-adjoint diagonal domain for energies
\(\sum_{n\geq1}(n/R)N_n\). Hence

\[
\ker\mathbb H_R=\mathbb C\Omega,\qquad
\mathbb H_R\geq R^{-1}(1-|\Omega\rangle\langle\Omega|).
\tag{LW16}
\]

The [[algebra/quotient-clock-and-stationary-action|state-action representation]] applies to this derived Fock clock as well. It is still a state-space action over the translation parameter, not a four-dimensional field-action integral.

The carrier change has a measurable algebraic consequence. For smooth \(f\), the normalized coherent vector \(W(f)\Omega\) has

\[
\langle W(f)\Omega,\mathbb H_R W(f)\Omega\rangle
=\langle\kappa f,K_R\kappa f\rangle
=\sum_{n\geq1}\frac{n^2}{R}|f_{-n}|^2.
\tag{LW17}
\]

It contains one extra generator factor compared with \(\mu(f)\). Thus the compression trace supplies the vacuum covariance in this realization, not the coherent state's energy. The clock was still inherited from translation; its quadratic form must be calculated in the new carrier.

## The preserved scope of the construction

This member now constructs a Hilbert carrier, vacuum, local circle algebras, positive clock and covariance from the boundary response plus a stated bosonic realization. It demonstrates that failed locality of one compression map is not failed locality of every realization of that geometry.

Circle-arc locality also does not repair the original [[inq|finite-initial-cut obstruction]]: an asymptotic tail still cannot be determined from an arbitrary finite prefix of a presented history. The net is built on retained boundary data. A finite operational readout from upstream histories remains a separate construction.

It does not derive an interacting gauge field, three spatial dimensions, Lorentz covariance, a physical clock or a physical mass Casimir. In particular, the finite-circle clock gap (LW16) is not a Yang–Mills mass gap.

Under the old period embedding \(R'=kR\), preserve one-particle vectors by sending mode \(n\) to mode \(kn\). In source symbols this requires the rescaled pullback
\(f(\theta')\mapsto k^{-1/2}f(k\theta')\):
it preserves \(\mu,\sigma\) and the old rates. It is not the unrescaled \(L^2\)-tail inclusion, and the preimage of one arc has \(k\) components. Thus a period cover also has a nontrivial effect on the proposed notion of locality.

Second quantization preserves those old modes, while new unit one-particle vectors have rate \(1/R'\). The factorial tower therefore retains its soft-mode obstruction on this enlarged observable construction. A local net, positive response and exact stationary state action together still do not supply a refinement-uniform mass edge.
