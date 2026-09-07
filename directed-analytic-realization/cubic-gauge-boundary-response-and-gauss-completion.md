# Cubic Gauge Boundary Response and Gauss Completion

The positive free gauge response \(|\operatorname{curl}|\) has a compatible cubic extension for actual spatial connections. A sum-frequency denominator fixes its transverse cubic coefficient; Gauss law then forces specific longitudinal terms. This construction solves the classical squared-response and gauge Ward identities through cubic order without taking a pointwise absolute Hessian. At quartic order it exposes both a nonlocal Coulomb energy and an unresolved harmonic response. It does not construct a positive quantum vacuum or a continuum mass gap.

## The field carrier and the cubic contract

Fix the flat torus \(\mathbb T_L^3=(\mathbb R/L\mathbb Z)^3\), a compact Lie algebra \(\mathfrak g\) with positive invariant inner product, and the ordinary integrated \(L^2\) pairing. Work on real \(\mathfrak g\)-valued one-forms whose components are finite Fourier polynomials. Gauge parameters are arbitrary real Fourier polynomials. Products, brackets and variations retain every generated Fourier mode: no fixed Galerkin cutoff or projected gauge bracket is used. The statements below concern exact polynomial coefficients and infinitesimal gauge identities on this core, not a completed nonlinear gauge theory.

Let \(d^*\) be the \(L^2\) adjoint, \(\Delta_0=d^*d\) on scalar fields, and

\[
\phi=\Delta_0^{-1}d^*A,\qquad
a=A-d\phi,\qquad d^*a=0,\qquad
K=(d^*d)^{1/2}\quad\hbox{on one-forms}.
\tag{CB1}
\]

The inverse in (CB1) acts on mean-zero scalar fields, and \(\phi\) has mean zero. Thus \(a\) includes the harmonic constant connections. On a nonzero momentum \(p\), \(K=|p|P_T(p)\); it vanishes on longitudinal and harmonic slots. In particular, \(K^2=d^*d\).

With the bracket convention \(F_A=dA+g[A,A]/2\), the magnetic potential supplied by [[chern-simons-response-and-gauge-action|transgression]] is

\[
\begin{aligned}
V_g(A)&=\frac12\|F_A\|^2=V_2+gV_3+g^2V_4,\\
V_2&=\frac12\|dA\|^2,\qquad
V_3=\frac12(dA,[A,A]),\qquad
V_4=\frac18\|[A,A]\|^2.
\end{aligned}
\tag{CB2}
\]

Seek coefficients of a classical scalar response
\(W=W_2+gW_3+g^2W_4+\cdots\), with
\(W_2(A)=(A,KA)/2\). Write \(dW[A][h]=(\nabla W(A),h)\). The order-\(g\) squared-response equation and gauge Ward identity are respectively

\[
dW_3[A][KA]=V_3(A),\qquad
dW_3[A][d\omega]=-(KA,[A,\omega]).
\tag{CB3}
\]

The second follows by expanding \(dW[A][d\omega+g[A,\omega]]=0\). These are distinct constraints: a solution on transverse fields alone need not satisfy the second.

## The transverse sum-frequency inverse

For a transverse field, define

\[
C_3(a)=\int_0^\infty V_3(e^{-\tau K}a)\,d\tau.
\tag{CB4}
\]

This integral converges for every polynomial \(a\), including a nonzero harmonic part. The limiting field is constant, its exterior derivative vanishes, and every surviving cubic monomial contains a decaying nonzero-momentum leg.

More explicitly, put \(a(x)=\sum_p a_pe^{ipx}\), \(p\in(2\pi/L)\mathbb Z^3\), and write

\[
v_3(p,q,r)=\frac{L^3}{2}
\left\langle ip\wedge a_p,[a_q,a_r]\right\rangle.
\]

Here the form and Lie pairings are extended complex bilinearly; the total sum is real. Then

\[
\boxed{
C_3(a)=
\sum_{\substack{p+q+r=0\\ |p|+|q|+|r|>0}}
\frac{v_3(p,q,r)}{|p|+|q|+|r|}.}
\tag{CB5}
\]

The omitted all-harmonic vertex is zero. Translating the lower integration endpoint in (CB4) proves
\(dC_3[a][Ka]=V_3(a)\). This is the cubic coefficient of the [[algebra/positive-boundary-response-from-decaying-extensions|decaying-extension recursion]], but not an application of that finite-dimensional existence theorem: here the full field carrier has gauge and harmonic zero modes, with infinitely many possible momenta.

## Gauss law fixes the longitudinal completion

Define the full cubic functional by

\[
\boxed{
W_3(A)=C_3(a)
-(Ka,[a,\phi])
-\frac12(Ka,[d\phi,\phi]).}
\tag{CB6}
\]

It is real, homogeneous cubic, and its \(L^2\) gradient at polynomial data is again a finite Fourier polynomial, with generated modes retained. The mean-zero inverse in (CB1) fixes all inverse-Laplacian conventions.

For a mean-zero \(\omega\), variation by \(d\omega\) leaves \(a\) fixed and changes \(\phi\) by \(\omega\). Differentiation gives

\[
dW_3[A][d\omega]
=-(Ka,[a,\omega])
-\frac12(Ka,[d\omega,\phi]+[d\phi,\omega]).
\tag{CB7}
\]

Since
\([d\omega,\phi]-[d\phi,\omega]=d[\omega,\phi]\)
and \(d^*Ka=0\), (CB7) equals the Ward expression in (CB3). A constant gauge parameter is handled separately: \(K\) commutes with constant color rotations and is self-adjoint, so \((KA,[A,\omega])=0\). Thus the identity holds for every polynomial parameter, not only mean-zero ones.

For the squared-response equation, use invariant pairing and the graded Leibniz identities
\[
d[a,\phi]=[da,\phi]-[a,d\phi],
\qquad d[d\phi,\phi]=-[d\phi,d\phi].
\]
They imply

\[
V_3(a+d\phi)-V_3(a)
=-(K^2a,[a,\phi])
-\frac12(K^2a,[d\phi,\phi]).
\tag{CB8}
\]

Variation of (CB6) by \(KA=Ka\) keeps \(\phi\) fixed. Its extra derivative \((Ka,[Ka,\phi])\) vanishes by invariance of the Lie metric. Equations (CB4) and (CB8) therefore prove the first identity in (CB3).

Equivalently, the same functional has the full-flow formula

\[
W_3(A)=\int_0^\infty
V_3(e^{-\tau K}a+d\phi)\,d\tau.
\tag{CB9}
\]

Indeed (CB8), evaluated along \(a_\tau=e^{-\tau K}a\), is the \(\tau\)-derivative of
\((Ka_\tau,[a_\tau,\phi])+(Ka_\tau,[d\phi,\phi])/2\).
The terminal terms vanish because \(Ka_\tau\to0\). The longitudinal field itself need not decay.

This is a compatible scalar response, not the generally nonintegrable [[algebra/absolute-hessian-and-response-integrability|pointwise absolute-Hessian prescription]]. The positive choice has been made in the free quadratic branch; no global positivity of the cubic polynomial follows.

## The next coefficient contains a Coulomb energy

On the Coulomb slice \(A=a\), put

\[
\rho(a)=\sum_i[a_i,(Ka)_i],\qquad
N_{3,T}=\nabla_T C_3(a).
\]

Equation (CB6) gives the complete gradient

\[
\boxed{
\nabla W_3(a)=N_{3,T}+d\Delta_0^{-1}\rho(a),\qquad
d^*\nabla W_3(a)=\rho(a).}
\tag{CB10}
\]

The scalar \(\rho\) has zero spatial mean. For every constant \(\eta\),
\[
(\rho,\eta)=-(Ka,[a,\eta])=0,
\]
because constant adjoint rotations are skew, commute with \(K\), and preserve its quadratic form. Thus (CB10) uses an actual inverse on its declared domain. This is the order-\(g\) Gauss equation
\(d^*N-g\sum_i[a_i,N_i]=0\), not an extra scalar charge postulate.

Orthogonality of transverse and longitudinal one-forms yields

\[
\|\nabla W_3(a)\|^2
=\|N_{3,T}\|^2+(\rho,\Delta_0^{-1}\rho).
\tag{CB11}
\]

Consequently the necessary quartic recursion, restricted to this slice, is

\[
\boxed{
dW_4[a][Ka]
=V_4(a)-\frac12\|N_{3,T}\|^2
-\frac12(\rho,\Delta_0^{-1}\rho).}
\tag{CB12}
\]

The last term is the positive longitudinal electric energy, subtracted on the response side of the equation. Omitting it amounts to using the flat transverse kinetic form past its order of validity. For a concrete nonzero example, take
\(a_3=T_1\cos(kx_1)+T_2\cos(\ell x_2)\), \(a_1=a_2=0\), with distinct positive allowed momenta. Then
\(\rho=(\ell-k)[T_1,T_2]\cos(kx_1)\cos(\ell x_2)\).
This is data in the full polynomial carrier, not a proposed closed two-mode gauge model.

## The harmonic condition is not solved by a denominator

The prescription (CB4) sets the all-harmonic cubic to zero. At a constant connection \(h\), it also gives \(\nabla W_3(h)=0\): the linear variation of \(V_3\) there is an integral of a derivative against a constant two-form and vanishes. Equivalently, momentum conservation forbids a cubic vertex with two zero momenta and one nonzero momentum. This is important: a general semidefinite finite-dimensional system can have a cubic whose transverse derivative is nonzero on its zero-mode subspace. Since \(Kh=0\), (CB12) here would require \(0=V_4(h)\), which fails for noncommuting constant components. Thus this particular cubic prescription cannot continue through all harmonic slots by merely inverting the same operator.

This is not a theorem that no formal response exists. The cubic equations leave an all-harmonic functional undetermined. In the homogeneous \(SU(2)\) member one can add the signed cubic \(L^3\det h\); its squared gradient supplies the harmonic quartic potential. That observation neither constructs its higher mixed-mode completion nor selects a positive branch. The separate [[quantum-response-regularity-at-the-gauge-origin|regularity obstruction]] rules out a \(C^3\) classical response minimum for the nonzero quartic homogeneous potential, while allowing signed or lower-regularity possibilities.

The [[gauge_boundary_response_receipt.py|finite Fourier receipt]] checks the cubic identities, failure of the transverse-only Ward identity, the Coulomb norm and this harmonic obstruction. Its field pairings use normalized torus-average measure, so these identities are checked after removing the common volume factor, not as an independent test of the \(L^3\) in (CB5). Its selected calculations supplement the proofs; they do not supply analytic convergence.

The [[homogeneous-gauge-positive-realization|actual positive homogeneous quantum realization]] uses a different equation containing the quantum divergence term. Nothing in (CB3)–(CB12) supplies that term's field-theoretic definition, a normalizable state, or regulator-uniform control. At fixed torus size the cubic coefficients are exact; convergence of the nonlinear series, treatment of harmonic gauge geometry, infinite-volume infrared control and the physical quantum gap remain additional tasks.
