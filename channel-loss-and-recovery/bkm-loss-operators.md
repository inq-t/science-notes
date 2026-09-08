# BKM Loss Operators

The second variation of relative-entropy loss is a nonnegative form on incoming state tangents. In finite dimensions, the inverse logarithmic-mean metric gives its adjoint, bounded defect operator and exact composition identity. For Type-III restrictions, quadratic differentiability and a declared closed Hilbert form are additional hypotheses before the representation theorem supplies an operator. Neither positivity nor that operator supplies a uniform physical gap.

## The infinitesimal cocycle is a BKM defect

Let \(\sigma\) be a faithful finite-dimensional density matrix and
\(\Phi:\mathcal A\to\mathcal B\) a completely positive trace-preserving
map on density matrices. Work with the
[[channel-loss-and-recovery/relative-entropy-loss-and-sufficiency#Relative-entropy loss is an arrow cost|state-pair loss and composition law (D1)--(D2)]].
For a regular normalized state curve through \(\sigma\), write

$$
\rho_t=\sigma+tX+O(t^2),
\qquad
X=X^*,
\qquad
\operatorname{Tr}X=0.
$$

Put $P:=\operatorname{supp}\Phi(\sigma)$. If $P$ is not the output identity, replace the output algebra $\mathcal B$ by the corner $P\mathcal BP$ and regard $\Phi$ as a channel into that corner; in finite dimension, faithfulness of $\sigma$ ensures that all channel outputs lie in this support. For a later channel $\Psi$, make the analogous restriction to $\operatorname{supp}\Psi\Phi(\sigma)$. All output adjoints and BKM inverses below are taken on these declared support algebras. The coincidence expansion is

$$
D(\rho_t\Vert\sigma)
=
\frac{t^2}{2}
g_\sigma^{\mathrm{BKM}}(X,X)
+o(t^2).
$$

Consequently

$$
\boxed{
\ell_\Phi^\sigma[X]
:=
g_\sigma^{\mathrm{BKM}}(X,X)
-
g_{\Phi\sigma}^{\mathrm{BKM}}(\Phi X,\Phi X)
\geq0,}
\tag{D4}
$$

and differentiation of the relative-entropy composition law (D2) gives

$$
\boxed{
\ell_{\Psi\circ\Phi}^\sigma[X]
=
\ell_\Phi^\sigma[X]
+
\ell_\Psi^{\Phi\sigma}[\Phi X].}
\tag{D5}
$$

This is the quadratic loss of distinguishability under a channel. The form operates on the incoming state tangent $X$, as in the
[[measured-response-carriers/state-tangent-bkm-bridge#Faithful state tangents|state-tangent carrier]]. It does not operate on an output energy carrier.

The defect operator itself can be displayed. Write

$$
\Omega_\sigma(Z)
:=
\int_0^1\sigma^sZ\sigma^{1-s}\,\mathrm ds,
\qquad
g_\sigma^{\mathrm{BKM}}(X,Y)
=
\operatorname{Tr}\!\left[X\Omega_\sigma^{-1}(Y)\right].
\tag{D5a}
$$

Here \(X,Y\) are self-adjoint trace-zero tangents, and all traces are the
declared matrix traces. The logarithmic-mean operator \(\Omega_\sigma\)
is the \(\mathcal K_\sigma\) of the
[[measured-response-carriers/state-tangent-bkm-bridge#The canonical finite-dimensional bridge|score construction]]:
the observable BKM inner product uses \(\Omega_\sigma\), whereas this
density-tangent metric uses its inverse. Their common definition and
metric interpretation are developed in
[[library/monotone-riemannian-metrics-and-relative-entropy/inq|Lesniewski--Ruskai]].

The BKM adjoint of the state-tangent map is

$$
\Phi^{\sharp_\sigma}
:=
\Omega_\sigma\circ\Phi^\dagger\circ\Omega_{\Phi\sigma}^{-1},
$$

characterized by

$$
g_\sigma^{\mathrm{BKM}}(X,\Phi^{\sharp_\sigma}Y)
=
g_{\Phi\sigma}^{\mathrm{BKM}}(\Phi X,Y).
$$

Therefore

$$
\boxed{
L_\Phi^\sigma
:=
I-\Phi^{\sharp_\sigma}\Phi
,
\qquad
(L_\Phi^\sigma)^{*_{g_\sigma}}=L_\Phi^\sigma,
\qquad
0\leq_{g_\sigma}L_\Phi^\sigma\leq_{g_\sigma}I,
\qquad
\ell_\Phi^\sigma[X]
=
g_\sigma^{\mathrm{BKM}}(X,L_\Phi^\sigma X).}
\tag{D5b}
$$

For $\Psi$ after $\Phi$, the scalar cocycle (D5) is the quadratic form of the exact operator-valued identity

$$
\boxed{
L_{\Psi\Phi}^{\sigma}
=
L_\Phi^\sigma
+
\Phi^{\sharp_\sigma}
L_\Psi^{\Phi\sigma}
\Phi.}
\tag{D5c}
$$

The identity follows from
\((\Psi\Phi)^{\sharp_\sigma}
=\Phi^{\sharp_\sigma}\Psi^{\sharp_{\Phi\sigma}}\)
and addition and subtraction of \(\Phi^{\sharp_\sigma}\Phi\).
Here positivity and self-adjointness are with respect to the input BKM
tangent metric, not Hilbert--Schmidt Loewner order or complete positivity
on the matrix algebra; $\Phi^{\sharp_\sigma}$ need not itself be a channel. This answers the operator question without changing carriers: $L_\Phi^\sigma$ operates on incoming BKM tangents. It is not a spacetime operator, a clock generator, or a mass Casimir.

## Type-III Hessians and closed operators

Let \(\mathcal N\subseteq\mathcal M\) be a unital von Neumann inclusion,
and let \(\sigma\) be a faithful normal reference state. Use the
[[channel-loss-and-recovery/relative-entropy-loss-and-sufficiency#Restriction loss and sufficiency in Type III|finite-entropy restriction loss (D5d)]].
Choose sufficiently regular faithful state curves \(\varphi_s\) through
\(\sigma\), with tangent \(\xi=\dot\varphi_0\), for which the relative
entropies are finite near coincidence and both second variations exist.
Require those variations to define quadratic Hessians on a common
real-linear tangent domain, independent of the chosen curve representing
\(\xi\). Existence of second derivatives along isolated curves alone
would not supply such a quadratic form. Define

$$
q_{\sigma,\mathcal N}[\xi]
:=
\left.
\frac{\mathrm d^2}{\mathrm ds^2}
\mathcal L_{\sigma,\mathcal N}(\varphi_s)
\right|_{s=0}
=
g_{\sigma}^{\mathcal M}(\xi,\xi)
-
g_{\sigma|_{\mathcal N}}^{\mathcal N}
(\xi|_{\mathcal N},\xi|_{\mathcal N})
\geq0.
\tag{D5f}
$$

The form operates on incoming normal-state tangents. Its kernel consists of directions with zero **quadratic** restriction loss. That infinitesimal statement is weaker than exact recoverability of an entire finite curve; the [[channel-loss-and-recovery/relative-entropy-loss-and-sufficiency#Restriction loss and sufficiency in Type III|Connes-cocycle condition (D5e)]] remains the exact state-pair criterion.

If a physical construction provides a real Hilbert tangent carrier \(\mathcal T_{\sigma,\mathcal N}\) on which \(q_{\sigma,\mathcal N}\) is densely defined and closed, the representation theorem returns a unique positive self-adjoint operator \(R_{\sigma,\mathcal N}\) satisfying

$$
\boxed{
q_{\sigma,\mathcal N}[\xi]
=
\|R_{\sigma,\mathcal N}^{1/2}\xi\|^2.}
\tag{D5g}
$$

The form domain is \(\operatorname{Dom}R_{\sigma,\mathcal N}^{1/2}\).
This is the closed positive form representation theorem, also recalled in
[[library/the-kms-and-gns-spectral-gap-of-quantum-markov-semigroups/inq|Wirth's operator-theoretic preliminaries]], section 2.1.
It is an exact implication from the declared analytic hypotheses, not a
theorem that every physically desired tangent completion has those
properties. In particular the Hilbert norm used for closure and distance
must be declared; a BKM tangent norm and a physical excitation norm are
not interchangeable. At this level one can ask the recognizable lower-frame question

$$
q_{\sigma,\mathcal N}[\xi]
\stackrel{?}{\geq}
\kappa^2
\operatorname{dist}
(\xi,\ker q_{\sigma,\mathcal N})^2.
\tag{D5h}
$$

For a general restriction and reference state, pointwise positivity gives no such uniform \(\kappa>0\). For a state-preserving ordinary expectation, however, (D5h) holds tautologically with \(\kappa=1\) on the incoming BKM quotient. [[channel-loss-and-recovery/preserving-expectation-loss|The preserving-expectation theorem]]
identifies this norm and quotient explicitly and proves that the exact
estimate is still a loss on forgotten directions. The
[[channel-loss-and-recovery/minimum-lift-output-forms|minimum-lift construction]]
is a separate passage to a form on output tangents.
