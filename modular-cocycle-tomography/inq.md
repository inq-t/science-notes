---
inq.module: "modular-cocycle-tomography"
inq.include:
  - "**/*.md"
---
# Modular Cocycle Tomography

A faithful normal state detects an inner-unitary observable direction only modulo its centralizer. A family of state presentations detects directions modulo the intersection of their centralizers, and Connes cocycles compute that intersection on one reference carrier. Every sigma-finite factor admits a separating state atlas, while a type-III\(_1\) factor with separable predual even admits a single faithful state with scalar centralizer. These are exact injectivity statements, not spectral-gap theorems: positive mass requires a selected physical atlas with a regulator-uniform closed-range bound and an independent comparison with clock energy.

**Status: [EXACT] for the response-kernel, centralizer-atlas, cocycle-commutant, and countable tomography theorems below; [STANDARD] for the type-III\(_1\) ergodic-state theorem; [CONSTRUCTION TARGET] for a physically selected cocycle atlas and its quantitative lower frame; [OPEN] for its continuum Yang--Mills realization and energy solder.**

## A state sees only outside its centralizer

Let \(M\) be a sigma-finite von Neumann algebra and let \(\varphi\) be a
faithful normal state. For a self-adjoint \(A\in M\), consider the local
unitary presentation

\[
\varphi_{A,s}(x)
:=
\varphi(e^{-isA}xe^{isA}).
\]

Its bounded normal state differential is

\[
d_\varphi A(x)
:=
\left.\frac{\mathrm d}{\mathrm ds}\varphi_{A,s}(x)\right|_{s=0}
=
i\varphi([x,A]).
\tag{MT1}
\]

The state centralizer is

\[
M_\varphi
:=
\{a\in M:\varphi(ax)=\varphi(xa)\text{ for every }x\in M\}.
\tag{MT2}
\]

Consequently,

\[
\boxed{
\ker d_\varphi=(M_\varphi)_{\mathrm{sa}}.}
\tag{MT3}
\]

This is a type statement before it is a physical interpretation. The map
\(d_\varphi\) operates on self-adjoint algebra elements, returns normal
state tangents, and kills scalars as well as every non-scalar element of the
centralizer. Faithfulness makes the represented vector separating; it does
not make (MT1) injective.

For a nonempty family \(\mathcal F=\{\varphi_i\}_{i\in I}\) of faithful
normal states, define

\[
D_\mathcal F:
M_{\mathrm{sa}}/\mathbb R\mathbf1
\longrightarrow
\prod_{i\in I}(M_*)_{\mathrm{sa}},
\qquad
[A]\longmapsto(d_{\varphi_i}A)_i.
\tag{MT4}
\]

Then

\[
\boxed{
\ker D_\mathcal F
=
\left(\bigcap_{i\in I}M_{\varphi_i}\right)_{\mathrm{sa}}
/\mathbb R\mathbf1.}
\tag{MT5}
\]

Thus the exact algebraic stopping condition for state tomography on a factor
is

\[
\bigcap_{i\in I}M_{\varphi_i}=\mathbb C\mathbf1.
\tag{MT6}
\]

It says that no non-scalar inner-unitary direction is invisible to every
state presentation. It says nothing yet about how strongly a direction is
seen.

## All faithful presentations meet in the center

There is an elementary atlas theorem that does not depend on the factor
type:

\[
\boxed{
\bigcap_{\varphi\in\mathsf S_{\mathrm{fn}}(M)}M_\varphi
=Z(M),}
\tag{MT7}
\]

where \(\mathsf S_{\mathrm{fn}}(M)\) denotes the faithful normal states.

To prove the nontrivial inclusion, fix a faithful normal state \(\varphi_0\)
and suppose \(A\) centralizes every faithful normal state. For any nonzero
normal positive functional \(\psi\) and \(\epsilon>0\),

\[
\varphi_{\psi,\epsilon}
:=
\frac{\psi+\epsilon\varphi_0}{\psi(\mathbf1)+\epsilon}
\tag{MT8}
\]

is faithful. Subtracting the centralizer identities for
\(\varphi_{\psi,\epsilon}\) and \(\varphi_0\) gives

\[
\psi([A,x])=0
\qquad(x\in M).
\]

Normal positive functionals linearly span \(M_*\), and the predual separates
\(M\), so \([A,x]=0\) for every \(x\). Hence \(A\in Z(M)\).

If \(M_*\) is separable, a countable atlas suffices. Choose a norm-dense
sequence of faithful normal states \((\varphi_n)\); such states are dense
because mixing any normal state with a positive amount of \(\varphi_0\)
makes it faithful. Continuity in the predual norm then gives

\[
\boxed{
\bigcap_{n\geq0}M_{\varphi_n}=Z(M).}
\tag{MT9}
\]

For a factor, (MT7)--(MT9) return only \(\mathbb C\mathbf1\). This proves
that a sufficiently rich atlas can separate algebraic directions. It also
shows why an unrestricted atlas is too cheap to explain physics: neither
its states, weights, nor normalization have been selected by the system.

## Connes cocycles expose the common blind algebra

Choose \(\varphi_0\in\mathcal F\) and put

\[
u_i(t):=[D\varphi_i:D\varphi_0]_t.
\tag{MT10}
\]

Connes' Radon--Nikodym theorem gives

\[
\sigma_t^{\varphi_i}
=
\operatorname{Ad}(u_i(t))\circ\sigma_t^{\varphi_0}.
\tag{MT11}
\]

Because a centralizer is the fixed algebra of its modular flow, (MT11)
implies the exact identity

\[
\boxed{
\bigcap_{i\in I}M_{\varphi_i}
=
M_{\varphi_0}
\cap
\{u_i(t):i\in I,\ t\in\mathbb R\}'.}
\tag{MT12}
\]

Indeed, after \(A\in M_{\varphi_0}\) has been imposed,

\[
\sigma_t^{\varphi_i}(A)=A
\quad\Longleftrightarrow\quad
u_i(t)Au_i(t)^*=A.
\]

If

\[
C_\mathcal F
:=
W^*(u_i(t):i\in I,\ t\in\mathbb R),
\]

then a factor atlas is algebraically complete exactly when

\[
M_{\varphi_0}\cap C_\mathcal F'=\mathbb C\mathbf1.
\tag{MT13}
\]

The stronger equation \(C_\mathcal F=M\) is sufficient but unnecessary.
The left side of (MT12) is reference-independent. If another member of
\(\mathcal F\) is used as reference, the cocycle chain rule gives the same
intersection, although the individual cocycles change.

A decisive warning is built into the algebra. In general

\[
u_i(t+s)
=
u_i(t)\,\sigma_t^{\varphi_0}(u_i(s)),
\tag{MT14}
\]

not \(u_i(t+s)=u_i(t)u_i(s)\). A Connes cocycle is unitary-valued comparison
data, not ordinarily a one-parameter unitary group. Stone's theorem does not
assign it a Hamiltonian, and its derivative cannot be called mass without an
additional theorem. [[library/une-classification-des-facteurs-de-type-iii/inq|Connes]]
owns the modular cocycle comparison; [[library/the-radon-nikodym-theorem-for-von-neumann-algebras/inq|Pedersen--Takesaki]]
identify the extra commutation conditions under which a Radon--Nikodym
cocycle reduces to an ordinary group generated by a centralizer-affiliated
operator.

## A concrete same-algebra tomographic form

Suppose \(\mathcal F=(\varphi_n)_{n\geq0}\) is countable. Let
\((\mathcal H_0,\pi_0,\Omega_0)\) be the faithful GNS representation of
\(\varphi_0\), let \((t_k)\) be dense in \(\mathbb R\), and choose strictly
positive summable weights \(\alpha_k\) and \(\beta_{n,k}\). Omitting
\(\pi_0\) from the notation, define

\[
\begin{aligned}
Q_\mathcal F[A]
:={}&
\sum_k\alpha_k
\|\bigl(\sigma_{t_k}^{\varphi_0}(A)-A\bigr)\Omega_0\|^2\\
&+
\sum_{n,k}\beta_{n,k}
\|[A,u_n(t_k)]\Omega_0\|^2.
\end{aligned}
\tag{MT15}
\]

After declaring the modular parameter and algebra generator dimensionless,
the form is dimensionless and is unchanged by
\(A\mapsto A+c\mathbf1\). It is not intrinsically normalized:
\(A\mapsto aA\) rescales it by \(|a|^2\), so (MT15) supplies neither a
preferred unit nor a rate. Since \(\Omega_0\) is separating and the modular
and cocycle maps are continuous, vanishing on the dense time set extends to
every time. Equations (MT12)--(MT13) therefore give

\[
\boxed{
\ker Q_\mathcal F
=
\left(\bigcap_nM_{\varphi_n}\right)_{\mathrm{sa}}
/\mathbb R\mathbf1.}
\tag{MT16}
\]

This is a common-carrier form in the modest but exact sense that every term
is represented on the one faithful GNS carrier of \(\varphi_0\). It is not
yet the Yang--Mills Hilbert norm, a relative-entropy Hessian, a physical
Hamiltonian, or a rate per clock time.

## Type III\(_1\) permits one-state tomography

[[library/ergodic-states-on-type-iii-1-factors-and-ergodic-actions/inq|Marrakchi and Vaes]]
prove that for a nontrivial von Neumann algebra with separable predual,

\[
\boxed{
M\text{ is a type III}_1\text{ factor}
\quad\Longleftrightarrow\quad
\exists\varphi\in\mathsf S_{\mathrm{fn}}(M):
M_\varphi=\mathbb C\mathbf1.}
\tag{MT17}
\]

Moreover, the faithful normal states with scalar centralizer form a dense
\(G_\delta\) set. For such an ergodic state, (MT3) is already injective
modulo scalars: the atlas may contain one state.

This is a striking reason that type III\(_1\), rather than a local density
matrix algebra, is relevant to the proposed reversal. It is not a mass-gap
theorem. Baire-generic does not mean physically selected, and the theorem
does not say that the restricted Yang--Mills vacuum has scalar centralizer.
The same paper proves only weak mixing of the modular representation on the
vacuum complement. Weak mixing excludes finite-dimensional invariant
subrepresentations; it does not exclude spectrum or approximate invariant
vectors accumulating at zero.

## Injectivity is not a quantitative distinction gap

Suppose the state tangents in (MT1) belong to declared BKM or Araki metric
domains and let

\[
q_\mathcal F[A]
:=
\sum_iw_i\,
g_{\varphi_i}^{\mathrm{BKM}}
\bigl(d_{\varphi_i}A,d_{\varphi_i}A\bigr),
\qquad w_i>0.
\tag{MT18}
\]

Where every target metric is positive definite, the pullback theorem in
[[measured-response-carriers/inq#Parameter Hessians are pullbacks, not new carriers|measured response carriers]]
gives

\[
\ker q_\mathcal F
=
\left(\bigcap_iM_{\varphi_i}\right)_{\mathrm{sa}}.
\tag{MT19}
\]

On a finite-dimensional declared source sector, a scalar kernel gives a
positive least eigenvalue after quotienting scalars. On an
infinite-dimensional source it does not. The gap-bearing statement is the
additional inequality

\[
\boxed{
q_\mathcal F[A]
\geq
\kappa\|[A]\|_{\mathrm{phys}}^2,
\qquad \kappa>0,}
\tag{MT20}
\]

relative to a separately declared physical norm and common domain. This is
a closed-range or bounded-below theorem for the joint analysis map. Neither
(MT7), (MT12), nor (MT17) implies it.

For varying regions, the warning is stronger. Centralizers live in different
algebras and cannot be intersected by notation. One must first construct
maps from one physical source carrier into every regional tangent carrier;
the meaningful object is the intersection of those pullback kernels.

## The mass-gap return type

At a regulator \(r\), let \(\mathcal H_r\) be the physical Hilbert carrier,
let \(\mathcal K_r\) be a response Hilbert carrier, and let
\(\mathscr C_r\subset\mathcal H_r\) be a common complex energy-form core.
Suppose

\[
T_r:\mathscr C_r\longrightarrow\mathcal K_r
\]

is a physically selected modular or regional analysis map and \(D_r\) is an
independently constructed bounded positive categorical or Markov defect on
\(\mathcal H_r\). The sharp coverage theorem has the Douglas-type core form

\[
D_r^{1/2}\Psi=C_rT_r\Psi
\quad(\Psi\in\mathscr C_r),
\qquad
 C_r:\overline{T_r\mathscr C_r}\longrightarrow\mathcal H_r
 \text{ bounded},
\qquad
\sup_r\|C_r\|<\infty.
\tag{MT21}
\]

If, uniformly in \(r\),

\[
D_r\geq\kappa_D(I-P_{0,r}),
\qquad
\|T_r\Psi\|^2
\leq
C_E\,\mathfrak h_r[\Psi],
\tag{MT22}
\]

then

\[
\mathfrak h_r[\Psi]
\geq
\frac{\kappa_D}{C_E\sup_r\|C_r\|^2}
\|(I-P_{0,r})\Psi\|^2.
\tag{MT23}
\]

This is the exact role of modular tomography: it can remove the centralizer
kernel and formulate the required uniform coverage. It does not select
\(D_r\), produce \(C_E\), reconstruct Poincare covariance, or set a
dimensional yardstick.

The Copernican typing is therefore precise. A state atlas and its Connes
cocycles compare presentations; they are not themselves an irreversible
process. Strict [[basic-concepts/descent/inq|descent]] glues compatible
objects. Forgetting requires a nonfaithful quotient, restriction,
expectation, instrument, or other noninvertible process. Unitary clock
evolution may then act on the retained local carrier by the independent
mechanism proved in
[[algebra/quotient-unitarity-and-kernel-stabilization|quotient unitarity]].
No \(\hbar\), \(c\), or clock parameter enters (MT1)--(MT21). Equation
(MT22) is precisely where a later energy solder and its dimensional constant
first enter; Poincare reconstruction remains later still.
