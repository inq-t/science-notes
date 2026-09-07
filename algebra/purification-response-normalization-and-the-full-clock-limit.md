# Purification Response Normalization and the Full Clock Limit

A concentrating purification law has a nontrivial full fluctuation carrier, not merely surviving affine coordinates. Requiring finite nonzero covariance and a nontrivial continuous response forces the orders of amplitude and duration rescaling. Exact sphere moments then construct polynomial-compatible Hilbert comparisons under which the inherited clock is an explicit quadratic function of the Gaussian number operator. This proves norm-resolvent and positive-time heat convergence for the existing purification family. The limit is a finite-mode oscillator, not a four-dimensional field theory or a dynamically generated Yang–Mills mass.

## The same parent supplies the law and response

Fix \(d\ge2\), let \(K\ge d\), \(D=dK\), and use
[[purification-descent-and-the-matrix-response|round complex purification]]:
\(\Psi\in S^{2D-1}\), \(\rho=\Psi\Psi^*\), with inherited
generator \(L_{d,K}\) from \(\Delta_S/4\). Let
\(T_1,\ldots,T_r\), \(r=d^2-1\), be a real basis of traceless
Hermitian matrices, put \(\tau=\operatorname{Tr}/d\), and write
\[
G_{ij}=\tau(T_iT_j),\qquad f_i(\rho)=\operatorname{Tr}(\rho T_i).
\]
The exact affine identities are
\[
\nu(f_i)=0,\qquad \nu(f_if_j)=\frac{G_{ij}}{D+1},\qquad
L_{d,K}f_i=-Df_i.
\tag{FC1}
\]
The law of \(\rho\) concentrates at \(I/d\). This is a character
limit on continuous functions of density parameters, not a character of
the original noncommutative matrix algebra.

## A nondegenerate response fixes two scaling orders

Consider amplitudes \(b_Df_i\), \(b_D>0\), and response semigroups
\(e^{t\alpha_DL_{d,K}}\), \(\alpha_D>0\). Their affine pairing is
\[
\nu\big(b_Df_i\,e^{t\alpha_DL_{d,K}}b_Df_j\big)
=\frac{b_D^2}{D+1}G_{ij}e^{-t\alpha_DD}.
\tag{FC2}
\]
A finite nonzero limiting covariance requires
\(b_D^2/(D+1)\to c\in(0,\infty)\). A nontrivial strongly continuous
limiting clock on these surviving modes requires
\(\alpha_DD\to\omega\in(0,\infty)\). A zero limit freezes every
fixed polynomial degree; an infinite limit gives zero at every positive
time but a nonzero value at time zero, violating strong continuity.
If the exponential at one positive time fails to converge, the proposed
pairing limit already fails. These statements concern this fixed-degree
fluctuation limit, not every possible moving-probe limit.

Thus nondegeneracy and continuity force the orders
\[
\boxed{b_D\asymp\sqrt D,\qquad\alpha_D\asymp D^{-1}.}
\tag{FC3}
\]
More precisely their above normalized ratios must converge. The finite
constants \(c,\omega\) remain calibration choices. Set them to one by
using \(\xi_i=\sqrt{D+1}f_i\) and transporting \(L_{d,K}/D\) to
the \(\xi\) coordinates; denote its closed generator by
\(\mathcal A_D\), its law by \(\widetilde\nu_D\), and
\(H_D=-\mathcal A_D\). This normalization has not supplied seconds or
energy units. [[partial-trace-clock-consistency-and-the-fluctuation-limit|Successive partial traces]]
preserve the same total \(D\) and hence this duration normalization.

## All polynomial pairings converge, not only second moments

For any list of traceless Hermitian probes \(T_{i_1},\ldots,T_{i_m}\),
complex-sphere moments give
\[
\mathbb E\prod_{j=1}^m\xi_{i_j}
=\frac{(D+1)^{m/2}}{(D)_m}
\sum_{\pi\in S_m}D^{c(\pi)}
\prod_{(j_1\cdots j_q)\text{ cycle of }\pi}
\tau(T_{i_{j_1}}\cdots T_{i_{j_q}}),
\tag{FC4}
\]
where \((D)_m=D(D+1)\cdots(D+m-1)\), and \(c(\pi)\) counts
cycles. Products inside a cycle retain their matrix order.

To derive (FC4), take a standard complex Gaussian vector
\(g=R\Psi\). Gaussian contractions in
\(\mathbb E\prod_j g^*(T_{i_j}\otimes I_K)g\) are indexed by
permutations; each cycle contributes the trace of its matrix product.
The independent radius satisfies \(\mathbb E R^{2m}=(D)_m\).
Divide by that moment, use
\(\operatorname{Tr}_D(T_{i_{j_1}}\cdots T_{i_{j_q}}\otimes I_K)
=D\tau(T_{i_{j_1}}\cdots T_{i_{j_q}})\), and insert the fluctuation
factors. This proves the finite formula without a tail approximation.

Singleton cycles vanish. The surviving terms have
\(c(\pi)\le\lfloor m/2\rfloor\). For even \(m\), only pairings
survive the limit, with coefficient tending to one and pair values
\(G_{ij}\); all nonpairing terms vanish. Odd moments tend to zero at
order \(D^{-1/2}\). Even moments differ from their Gaussian Wick
values by \(O(D^{-1})\), for fixed probes and degree.
Consequently every mixed polynomial moment converges to that of
\(\gamma_G=N(0,G)\), strengthening the earlier weak-law limit.

## The Hilbert comparison respects polynomial observations

Let \(\mathcal P_m\) be polynomials of degree at most \(m\) in the
\(r\) coordinates, and fix one degree-ordered monomial enumeration.
For \(K\ge d\), the finite law has open support in its state body,
so its polynomial Gram matrices are positive definite. Gaussian Gram
matrices are also positive definite. Apply Gram–Schmidt with positive
leading normalization in both laws. Formula (FC4) implies coefficientwise
convergence of every resulting finite-degree orthonormal polynomial
\(h_{D,\alpha}\to h_{\infty,\alpha}\).

Polynomials are dense in each finite \(L^2\) space by compact-support
polynomial approximation, and in \(L^2(\gamma_G)\) by Hermite
completeness. Matching these bases defines a unitary
\[
U_D:L^2(\gamma_G)\longrightarrow L^2(\widetilde\nu_D),\qquad
U_Dh_{\infty,\alpha}=h_{D,\alpha}.
\tag{FC5}
\]
If \(j_Dp\) denotes the same polynomial evaluated on the finite
fluctuation body, moment convergence also gives
\[
\boxed{U_D^*j_Dp\longrightarrow p\quad\text{in }L^2(\gamma_G).}
\tag{FC6}
\]
Thus this is not an unrelated matching of abstract spectra. The chosen
enumeration is comparison data; \(U_D\) is not asserted to preserve
pointwise products, bounded readout norms or matrix-algebra products.

## Exact transport of the whole clock

The [[purification-descent-and-the-matrix-response#Exact polynomial spectrum|complete degree spectrum]]
is inherited from the parent, not fitted to the limiting Gaussian.
Equivalently, \(\mathcal A_D\) preserves \(\mathcal P_m\), with
\[
(\mathcal A_D+\lambda_m(D))\mathcal P_m\subseteq\mathcal P_{m-1},
\qquad\lambda_m(D)=m+\frac{m(m-1)}D.
\tag{FC7}
\]
Self-adjointness makes
\(\mathcal P_m\ominus\mathcal P_{m-1}\) an eigenspace with this
eigenvalue. The constant space and every higher degree exhaust the
carrier. On the Gaussian space let
\(\mathcal N=-G:\nabla^2+\xi\cdot\nabla\), closed in its Hermite
basis; it has degree eigenvalue \(m\). Therefore
\[
\boxed{U_D^*H_DU_D=\mathcal N+\frac{\mathcal N(\mathcal N-1)}D.}
\tag{FC8}
\]
This is equality of self-adjoint operators. At finite \(D\), the
transported domain is \(\operatorname{Dom}\mathcal N^2\); the limiting
operator has the larger domain \(\operatorname{Dom}\mathcal N\).
Polynomials are common operator and form cores.

For \(z>0\), scalar spectral calculus gives
\[
\begin{aligned}
&\left\|(U_D^*H_DU_D+z)^{-1}-(\mathcal N+z)^{-1}\right\|\\
&\quad=\sup_{m\ge0}
\frac{m(m-1)/D}{(z+m)(z+m+m(m-1)/D)}\le\frac1D.
\end{aligned}
\tag{FC9}
\]
The numerator is zero at \(m=0,1\). For \(t>0\),
\[
\left\|e^{-tU_D^*H_DU_D}-e^{-t\mathcal N}\right\|
\le\frac{4}{e^2Dt},
\tag{FC10}
\]
using \(1-e^{-x}\le x\) and
\(\sup_{x\ge0}x^2e^{-tx}=4/(e^2t^2)\). This is uniform away from
time zero, not a claimed uniform norm estimate on all \(t\ge0\).
The unitary groups converge strongly, uniformly on compact time
intervals: first restrict to finitely many Hermite degrees and then
bound the tail by twice its norm. Unitary norm convergence is not needed.

Together (FC6) and (FC8) also prove convergence of every fixed
polynomial time pairing, locally uniformly in time. In particular the
reflected preparation kernels converge on all finite polynomial
families, and their completed limiting carrier is the entire Gaussian
space. The constants match exactly; both clocks have a unique constant
vacuum and centered gap one in this normalization.

## Moving high-degree probes do not retain an interaction at bounded energy

Write \(B_D=U_D^*H_DU_D=h_D(\mathcal N)\), with
\(h_D(m)=m+m(m-1)/D\). This exact identity gives a stronger
constraint than the fixed-polynomial limit. If \(P_{D,E}\) is the
spectral projection of \(B_D\) onto \([0,E]\), then
\[
0\le (B_D-\mathcal N)P_{D,E}\le\frac{E^2}{D}P_{D,E},
\qquad
\|(e^{-itB_D}-e^{-it\mathcal N})P_{D,E}\|
\le\frac{|t|E^2}{D}.
\tag{FC11}
\]
Indeed \(h_D(m)\ge m\), so this projection contains only degrees
\(m\le E\). The estimate does not depend on degree multiplicities.
It remains valid for growing numbers of modes wherever the same
degree-spectrum identity holds; it does not itself construct a common
observable algebra for those growing carriers.

Even a uniform bound on mean energy suffices for dynamical indistinguishability.
For any normalized \(\psi_D\) in the form domain with
\(\|B_D^{1/2}\psi_D\|^2\le E\), spectral calculus gives
\[
\boxed{
\sup_{|t|\le T}
\|(e^{-itB_D}-e^{-it\mathcal N})\psi_D\|^2
\le 2\sqrt2\,E\sqrt{T/D}.}
\tag{FC12}
\]
To prove this, for each degree use
\[
|e^{-ith_D(m)}-e^{-itm}|^2
\le\min\{4,t^2m^4/D^2\}
\le2\sqrt2\,m\sqrt{|t|/D},
\]
then integrate and use \(\mathcal N\le B_D\).
Thus moving probes with bounded energy cannot rescue a nonlinear
finite-duration clock in this normalization. This is a statement about
this spectral correction, not a theorem that arbitrary field interactions
must be visible in the spectrum alone.

It is not convergence of all unbounded energy expectations. For a unit
degree-\(D\) vector \(u_D\), the normalized vector
\[
\psi_D=\sqrt{1-D^{-1}}\,\Omega+D^{-1/2}u_D
\]
satisfies
\[
\langle B_D\rangle_{\psi_D}=2-D^{-1},\qquad
\langle B_D-\mathcal N\rangle_{\psi_D}=1-D^{-1}.
\tag{FC13}
\]
Rare high-degree tails preserve a correction to the mean while their
effect on the bounded-time unitary response vanishes by (FC12).

The spectral curvature is especially transparent:
\[
h_D(m+2)-2h_D(m+1)+h_D(m)=2/D.
\tag{FC14}
\]
A common clock multiplier \(c_D\) preserving a finite nonzero affine
rate has \(c_D\to\omega\in(0,\infty)\), hence curvature
\(2c_D/D\to0\). Keeping that curvature finite and nonzero instead makes the
affine rate diverge. A degree of order \(\sqrt D\) can retain an
order-one correction, but its unshifted excitation energy diverges.
[[occupation-conditioned-clocks-and-the-vacuum-boundary|Conditioning on a moving background sector]]
therefore requires a different reference state and subtraction. It
returns a background-dependent visible rate, not an exception to
(FC11)--(FC12) at bounded energy above the original vacuum.

## What the limit explains

The finite correction and its complete multiplicities are retained:
\(\lambda_2/\lambda_1=2+2/D\), and the degree-\(m\) multiplicity is
\(\binom{r+m-1}{m}\). They are consequences of the same parent law and
response, not independently selected oscillator parameters.
[[directed-analytic-realization/purification-fluctuation-and-the-oscillator-return|The oscillator return]]
constructs the corresponding operator algebra and stationary action.

The source sphere was already compact and gapped. Its quotient excludes
odd parent modes; the fluctuation limit preserves the normalized
retained gap. This does not create a mass from a gapless field theory.
Moreover \(d\) is fixed, \(r=d^2-1\) counts internal modes, and no
spatial volume, causal cone or Poincare representation has been derived.
The limit removes the finite \(D^{-1}\) nonlinear degree correction and
is Gaussian. Recovering interacting four-dimensional Yang–Mills remains
a different, unfulfilled obligation.

[[directed-analytic-realization/fluctuation_clock_receipt.py|The fluctuation-clock receipt]]
checks finite moment, generator, resolvent and ladder identities. Its
[[directed-analytic-realization/fluctuation-clock-receipt-output.txt|output]]
is not a substitute for the all-degree moment and operator arguments above.
