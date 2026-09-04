# Localized Relative Entropy and the Energy Solder

A rigorous energy solder already exists for local state distinctions: in any wedge-dual translation-covariant QFT with positive energy, the vacuum relative entropy of a state localized in a region of width \(2R\) is at most \(2\pi R/(\hbar c)\) times its Hamiltonian energy. Differentiating this inequality at the vacuum, with explicit entropy and energy-form regularity, bounds a real local-unitary Hessian by the Hamiltonian form. A Hamiltonian gap follows only after that real Hessian has a positive Hermitian extension to a complex energy-form core, or after a compatible real structure proves the same extension. This does not prove Yang--Mills, but it identifies the remaining carrier, coercivity, and complexification obligations exactly.

**Status: [STANDARD] for Longo's finite-width relative-entropy bound; [EXACT DEDUCTION] for the real local-unitary Hessian inequality under the stated energy-form differentiability, the local-unitary centralizer kernel, the quotient-factorization criterion, and the conditional complex-core gap theorem below; [OPEN] for those differentiability domains, the Hermitian extension or compatible conjugation, energy-form-core property, globally induced descent frame, uniform lower constant, and continuum Yang--Mills construction.**

## The finite-width theorem

Let \(\mathcal A\) be a wedge-dual translation-covariant local net on Minkowski space, let \(\Omega\) be its invariant vacuum, and let \(H\geq0\) generate time translations with \(H\Omega=0\). If \(B\) is contained between two parallel causal boundaries of spatial width \(2R\), and a vector state \(\varphi_\xi\) agrees with the vacuum on the causal complement of \(B\), then [[library/a-bekenstein-type-bound-in-qft/inq|Longo's theorem]] gives

\[
S_{\mathcal A(B)}(\varphi_\xi\Vert\omega)
\leq
\frac{2\pi R}{\hbar c}
\langle\xi,H\xi\rangle.
\]

Full Poincare covariance is not needed for this inequality. Locality, positive-energy translation covariance, and wedge duality suffice; wedge duality can be replaced by the stronger assumption that the state equals the vacuum on \(\mathcal A(B)'\). The operator on the right is the physical Hamiltonian, not a modular logarithm or an independently normalized Markov generator.

## Differentiate on the same carrier

Take a bounded self-adjoint \(A\) localized in the appropriate dual algebra of \(B\), put

\[
U_s=e^{isA},
\qquad
\xi_s=U_s\Omega,
\qquad
\varphi_s=\langle\xi_s,\cdot\,\xi_s\rangle,
\]

and suppose the regional relative entropy is twice differentiable at \(s=0\). Also require the energy-form regularity

\[
U_s\Omega\in\operatorname{Dom}H^{1/2}
\quad\text{for small }|s|,
\qquad
\lim_{s\to0}
H^{1/2}\frac{(U_s-I)\Omega}{s}
=
iH^{1/2}A\Omega.
\]

Boundedness of \(A\) alone does not imply this condition. Define the half-Hessian

\[
q_B[A]
:=
\frac12
\left.\frac{\mathrm d^2}{\mathrm ds^2}
S_{\mathcal A(B)}(\varphi_s\Vert\omega)
\right|_{s=0}.
\]

The entropy has the expansion \(S_{\mathcal A(B)}(\varphi_s\Vert\omega)=q_B[A]s^2+o(s^2)\). Since \(H\Omega=0\), the energy-form condition gives the quadratic-coefficient limit

\[
\lim_{s\to0}
\frac{\langle U_s\Omega,HU_s\Omega\rangle}{s^2}
=
\|H^{1/2}A\Omega\|^2.
\]

Therefore

\[
\boxed{
q_B[A]
\leq
\frac{2\pi R}{\hbar c}
\|H^{1/2}A\Omega\|^2.}
\]

This answers the operator question without equivocation. The Hessian operates on the tangent of a localized state path. The Hamiltonian form operates on the implementing vector tangent \(iA\Omega\). The local-unitary path is the same bridge for both.

Adding a scalar to \(A\) changes only the phase of \(U_s\Omega\). Accordingly, the comparison norm is

\[
\|(1-P_\Omega)A\Omega\|,
\]

where \(P_\Omega:=|\Omega\rangle\langle\Omega|\) is the rank-one projection
onto the chosen vacuum ray.

## The local-unitary bridge has a centralizer kernel

The phrase “same bridge” does not mean that the bridge is injective. Put
\(M_B:=\mathcal A(B)\), assume the vacuum restriction \(\omega_B\) is
faithful, and for \(A=A^*\in M_B\) define

\[
u_A
:=
(1-P_\Omega)A\Omega
=
\bigl(A-\omega_B(A)\mathbf1\bigr)\Omega.
\tag{LE1}
\]

The vector tangent is \(iu_A\). The induced regional state tangent is the
real-linear map

\[
\begin{aligned}
\widetilde J_Bu_A(x)
&:=
\left.
\frac{\mathrm d}{\mathrm ds}
\omega_B(e^{-isA}xe^{isA})
\right|_{s=0}\\
&=
i\,\omega_B([x,A]),
\qquad x\in M_B.
\end{aligned}
\tag{LE2}
\]

Let

\[
M_B^{\omega_B}
:=
\{a\in M_B:\omega_B(ax)=\omega_B(xa)
\text{ for every }x\in M_B\}
\tag{LE3}
\]

be the vacuum centralizer. On any declared local class
\(\mathfrak C_B\subset M_{B,\mathrm{sa}}\), separatingness of \(\Omega\)
gives the exact kernel

\[
\boxed{
\ker\widetilde J_B
=
\left\{
\bigl(A-\omega_B(A)\mathbf1\bigr)\Omega:
A\in\mathfrak C_B\cap M_B^{\omega_B}
\right\}.}
\tag{LE4}
\]

Indeed, (LE2) vanishes exactly when \(A\) lies in the centralizer. Such a
unitary path leaves the regional state fixed even though its centered
implementing vector need not vanish. On the full projective Hilbert tangent,
commutant-unitary changes of purification supply the corresponding invisible
directions. Thus cyclicity and separatingness do not make regional
restriction informationally complete.

[[modular-cocycle-tomography/inq|Modular cocycle tomography]] gives the
exact multi-presentation completion of (LE4). For faithful normal states
\(\{\omega_i\}\) on one algebra, the joint local-unitary kernel is the
intersection of their centralizers; relative to \(\omega_0\), Connes
cocycles identify it as

\[
M_B^{\omega_0}
\cap
\{[D\omega_i:D\omega_0]_t:i,t\}'.
\tag{LE4a}
\]

A scalar intersection removes exact algebraic blind directions. It does not
give a lower frame in infinite dimension, and a generic faithful state cannot
replace the physical vacuum in the energy theorem merely because its
centralizer is scalar.

Let \(\mathcal D_B\) be the declared common real form core. Suppose the BKM
Hessian is closable there, and let \(T_B\) denote its closed analysis map,
with \(\mathcal D_B\subseteq\operatorname{Dom}T_B\), normalized so that

\[
q_B[v]=\|T_Bv\|_{\mathrm{BKM}}^2,
\qquad v\in\mathcal D_B,
\tag{LE5}
\]

and a categorical distinction form on the same real core is

\[
e_{\mathrm{cat}}[v]
=
\|D_{\mathrm{cat}}^{1/2}v\|^2,
\qquad v\in\mathcal D_B,
\tag{LE6}
\]

then the required comparison

\[
q_B[v]\geq b\,e_{\mathrm{cat}}[v],
\qquad b>0,
\qquad v\in\mathcal D_B,
\tag{LE7}
\]

has the immediate necessary condition

\[
\boxed{
\ker(T_B|_{\mathcal D_B})
\subseteq
\ker(D_{\mathrm{cat}}^{1/2}|_{\mathcal D_B}).}
\tag{LE8}
\]

More precisely, on the quotient form completions, (LE7) is equivalent to a
bounded map

\[
C_B:
\overline{T_B\mathcal D_B}
\longrightarrow
\overline{D_{\mathrm{cat}}^{1/2}\mathcal D_B}
\]

such that

\[
D_{\mathrm{cat}}^{1/2}v=C_BT_Bv,
\qquad v\in\mathcal D_B,
\qquad
\|C_B\|\leq b^{-1/2}.
\tag{LE9}
\]

For bounded operators this is the Douglas factorization criterion; for
closed forms the quotient-completion statement is the safe formulation. If
the categorical defect fixes only the vacuum while (LE4) contains a
nonvacuum vector, no positive \(b\) can exist. More generally, the estimate
fails precisely when there is a sequence in \(\mathcal D_B\), normalized by
\(e_{\mathrm{cat}}[v_n]=1\), for which \(q_B[v_n]\to0\). Nonclosed range of
\(T_B\) alone is not enough: the categorical form might vanish at the same
rate. If the categorical defect already has a vacuum-complement lower edge,
however, failure of \(T_B\) to be bounded below on that complement does
produce such an obstructing sequence. A family of regions, states, or
readouts must then have jointly trivial physical kernel and the corresponding
uniform relative lower frame. [[measured-response-carriers/inq|Measured
response carriers]] owns the general pullback-frame version of this
requirement.

There are two distinct uses of that family. A comparison with one regional
form requires the kernel inclusion (LE8) for that region individually. A
comparison with a summed or direct-integral atlas requires only the
intersection of the *pullback* kernels on the common source carrier to obey
the analogous inclusion. Centralizers of different regional algebras cannot
be intersected before those source maps and transports have been supplied.

This test is necessary for domination by the full regional Hessian and hence
for domination by any smaller restriction-loss form. It is not sufficient:
the restriction channel may have additional equality or recovery directions
on which its loss Hessian vanishes.

## A descent-loss Hessian also fits

Let \(\mathcal N\subseteq\mathcal A(B)\) be a declared descended algebra and define the relative-entropy loss along the same state path by

\[
L_{B\to\mathcal N}(s)
=
S_{\mathcal A(B)}(\varphi_s\Vert\omega)
-
S_{\mathcal N}(\varphi_s|_{\mathcal N}
\Vert\omega|_{\mathcal N}).
\]

Monotonicity gives \(0\leq L_{B\to\mathcal N}(s)\leq S_{\mathcal A(B)}(\varphi_s\Vert\omega)\). If the second derivatives exist, the half-Hessian

\[
q_{B\to\mathcal N}^{\mathrm{loss}}[A]
:=
\frac12L_{B\to\mathcal N}''(0)
\]

obeys

\[
0\leq
q_{B\to\mathcal N}^{\mathrm{loss}}[A]
\leq q_B[A]
\leq
\frac{2\pi R}{\hbar c}
\|H^{1/2}A\Omega\|^2.
\]

This places the restriction-loss construction of [[descent-loss-cocycle-and-recovery-fork]] on the correct side of the physical energy inequality. That note defines its Hessian without the factor \(1/2\); in that convention the coefficient here is \(4\pi R/(\hbar c)\).

## Conditional gap theorem

For the gap conclusion, assume additionally that the chosen vacuum is unique,
\(\ker H=\mathbb C\Omega\), so that the spectral vacuum projection is
\(P_0=P_\Omega\).

Assume there is a real linear class \(\mathfrak C_B\) of localized self-adjoint operators and put

\[
\mathcal D_{B,\mathbb R}
:=
\{(1-P_\Omega)A\Omega:A\in\mathfrak C_B\}
\]

Suppose \(\mathcal D_{B,\mathbb R}\) is a real form of a complex \(H^{1/2}\)-form core \(\mathcal D_{B,\mathbb C}\) on \((1-P_\Omega)\mathcal H\), and the real restriction-loss form admits a positive Hermitian extension \(\widehat q_{B\to\mathcal N}^{\mathrm{loss}}\) to that complex core. Agreement on the real subspace is not enough: one must prove the complex upper comparison

\[
\widehat q_{B\to\mathcal N}^{\mathrm{loss}}[\psi]
\leq
\frac{2\pi R}{\hbar c}
\|H^{1/2}\psi\|^2,
\qquad
\psi\in\mathcal D_{B,\mathbb C}.
\]

Suppose, independently of the spectrum of \(H\), that one also proves

\[
\widehat q_{B\to\mathcal N}^{\mathrm{loss}}[\psi]
\geq
\kappa_B
\|\psi\|^2,
\qquad
\psi\in\mathcal D_{B,\mathbb C},
\]

for some \(\kappa_B>0\). Combining the two inequalities and closing the Hamiltonian form gives

\[
\boxed{
H
\geq
\frac{\hbar c}{2\pi R}
\kappa_B(1-P_\Omega).}
\]

Thus

\[
\Delta_E
\geq
\frac{\hbar c}{2\pi R}\kappa_B.
\]

The theorem is noncircular if \(\mathcal N\), the state paths, the Hermitian extension, and \(\kappa_B\) are constructed from the proposed global-to-local geometry without consulting low-energy spectral data. The width \(R\) supplies the dimensional yardstick already recognized by the QFT localization theorem; \(\kappa_B\) is the dimensionless global distinction stiffness. Their quotient is a rate before \(\hbar\) converts it to energy.

A useful sufficient route to the complex extension is a conjugation \(C\) commuting with \(H^{1/2}\), with \(\mathcal D_{B,\mathbb R}=\operatorname{Fix}(C)\cap\mathcal D_{B,\mathbb C}\). If the real loss form is compatible with this structure, define

\[
\widehat q[x+iy]
:=
q[x]+q[y],
\qquad
x,y\in\mathcal D_{B,\mathbb R}.
\]

Then norm and energy split into their real and imaginary parts, so the two real inequalities imply the required complex inequalities. Absent such a structure or a directly constructed Hermitian form, a lower bound on a real subspace whose complex span is a core does not imply a spectral gap.

[[receipts/real-core-complexification-firewall-receipt.py|The finite counterexample receipt]] takes \(H=\operatorname{diag}(1/2,3/2)\) and the real form \(\{(a+ib,a-ib):a,b\in\mathbb R\}\). The energy quotient is identically one on that real form, whose complex span is all of \(\mathbb C^2\), while the actual spectral floor is \(1/2\).

## Why this is progress but not a solution

Reeh--Schlieder cyclicity makes local vectors norm dense, but it supplies
neither the kernel inclusion (LE8) nor closed range for \(T_B\), and does not
say that fixed-region local vectors are a core for the Hamiltonian quadratic
form. In a massless theory, norm approximation of a low-energy vector by
sharply localized vectors can hide unbounded high-energy tails. The carrier
kernel, complex form-core, and Hermitian-extension hypotheses are therefore
substantive and cannot be omitted.

Nor does Type \(\mathrm{III}_1\) structure make \(\kappa_B\) positive. It makes faithful regional relative entropy available, while the positive lower frame bound must come from the relative position of the whole family of presentations, inclusions, or descents. [[global-discreteness-kazhdan-rigidity-and-the-gap]] identifies the exact group-level analogue: a Kazhdan or representation-specific closed-range bound forbids almost-invariant nonvacuum directions. The missing comparison is

\[
\text{global presentation disagreement}
\ \lesssim\
q_{B\to\mathcal N}^{\mathrm{loss}},
\]

on the localized physical tangent carrier.

The promising theorem architecture is now

\[
\boxed{
\begin{array}{c}
\text{global discrete incidence}\
\Downarrow\ \text{closed-range comparison}\
\text{regional descent-loss Hessian}\
\Downarrow\ \text{Longo finite-width bound}\
\text{physical Hamiltonian gap}\
\Downarrow\ \text{Poincare reconstruction}\
\text{mass Casimir floor}.
\end{array}}
\]

The real same-path energy comparison inside the second arrow is now an established QFT theorem. Its positive Hermitian extension to a complex form core, together with the first global-to-regional coercivity arrow, remains part of the central Copernican construction problem.
