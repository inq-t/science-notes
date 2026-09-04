---
inq.module: "measured-response-carriers"
inq.include:
  - "**/*.md"
---
# The Three Carriers of a Measured Response

A state-preserving completely positive operation has three related but
distinct realizations: it acts on algebra elements, it contracts vectors in
the state's GNS representation, and its state-space action loses
information-geometric distinguishability on faithful tangents. Only the GNS
defect has an immediate operator spectrum, while only the tangent defect is
immediately a relative-entropy Hessian. Identifying either with spatial
precision, clock evolution, or energy requires an additional typed
comparison or carrier-realization theorem. A recent operator-monotone
interpolation theorem does transfer any GNS Markov gap to the observable BKM
norm on an arbitrary von Neumann algebra, but it does not erase the duality
between observable scores and state tangents. This distinction supplies one
reusable typing rule for Hessian response, binary information geometry,
causal-wall spectral theory, and the Yang--Mills categorical-action
programme.

**Status: [EXACT] for the GNS contraction, fixed-space intersection, pullback-radical, closed-form congruence, quotient-unitarity, and conditional implication theorems under their stated hypotheses; [PRIMARY-SOURCE THEOREM, RECENT PREPRINT] for the arbitrary-von-Neumann GNS-to-observable-BKM Markov-gap transfer; [EXACT FINITE-DIMENSIONAL] for the canonical modular BKM--GNS tangent bridge; [CONSTRUCTION] for a Type-III score intertwiner with full physical range; [OPEN] for a vacuum-ergodic normalized fusion action by state-preserving UCP maps, regional domination, clock calibration, and continuum Yang--Mills realization.**

## The measured operation

Let \(\mathcal A\) be a von Neumann algebra, let \(\omega\) be a faithful
normal state, and let

\[
(\pi_\omega,\mathcal H_\omega,\Omega_\omega)
\]

be its GNS representation. Suppose

\[
\Phi:\mathcal A\longrightarrow\mathcal A
\]

is normal, unital, completely positive, and state preserving:

\[
\omega\circ\Phi=\omega.
\tag{MC1}
\]

Assume also that \(\Phi\) has a normal unital completely positive
\(\omega\)-adjoint \(\Phi^\sharp\), meaning

\[
\omega\!\left(a^*\Phi(b)\right)
=
\omega\!\left(\Phi^\sharp(a)^*b\right)
\qquad
(a,b\in\mathcal A).
\tag{MC2}
\]

Existence of this adjoint is a genuine hypothesis outside the tracial case.
The operation is **GNS symmetric** when
\(\Phi^\sharp=\Phi\).

## First carrier: the observable algebra

On \(\mathcal A\), the map says how one declared readout, coarse graining,
defect, or correspondence transforms observables. Its fixed algebra is

\[
\mathcal A^\Phi
:=
\{a\in\mathcal A:\Phi(a)=a\}.
\tag{MC3}
\]

This is the correct carrier for multiplicative structure, complete
positivity, bimodularity, locality or regional naturality, and fusion laws.
It is not itself a Hilbert space, and the phrase “spectral gap of \(\Phi\)”
is incomplete until a normed representation has been selected.

## Descent and clock use different arrows

The Copernican global-to-local proposal becomes precise only after its
morphism types are separated. Let

\[
\Pi:\mathcal C_{\mathrm{whole}}
\longrightarrow
\mathcal C_{\mathrm{local}}
\tag{MC3a}
\]

be a realization functor. If it genuinely forgets a distinction, there are
arrows \(f\neq g\) with \(\Pi(f)=\Pi(g)\). It is then nonfaithful and cannot
be an equivalence or a unitary conjugation of represented categories. This is
the exact obstruction proved in [[algebra/nonfaithful-realization|the
nonfaithful-realization theorem]]. A Stinespring formula

\[
\Phi(a)=W^*\pi(a)W
\tag{MC3b}
\]

does not reverse this conclusion: it factors a completely positive map
through a larger representation but supplies neither an inverse to \(\Phi\)
nor a theorem that the dilation carrier is the physical ontology.

There is a second construction that must not be conflated with this
nonfaithful branch. [[directed-isometric-residue-completion/inq|For a declared
Hilbert-space contraction $A$]], the column

\[
x\longmapsto Ax\oplus(I-A^*A)^{1/2}x
\]

retains the missing norm in a new orthogonal coordinate. A quotient removes
directions from the retained carrier; this defect completion preserves them
as amplitudes in a larger codomain. Neither construction is automatically a
Stinespring environment, physical whole, measurement instrument, or record
algebra. Their common appearance as “forgetting” hides opposite carrier
operations.

Strict categorical descent is not itself the loss: it glues compatible local
objects and their cocycles into a global object and can retain every
stabilizer. Forgetting requires an additional typed operation such as a
quotient, coarse-moduli map, restriction, conditional expectation,
instrument, or nonfaithful realization. “Descent” below is shorthand for a
programme in which one of those operations occurs at the whole-to-local wall,
not a claim that the descent theorem erases data.

Clock evolution, by contrast, may be a reversible group inside one realized
algebra,

\[
\alpha_{t+s}=\alpha_t\alpha_s,
\qquad
\alpha_t(a)=U_taU_t^*,
\qquad
U_t=e^{-itH/\hbar},
\tag{MC3c}
\]

after a strongly continuous physical representation and its Hamiltonian have
been constructed. Thus the exact compatible architecture is

\[
\boxed{
\text{nonfaithful realization across registers}
\quad+\quad
\text{unitary clock evolution within a realized register}.}
\tag{MC3d}
\]

“The whole is nonunitary” is therefore safest as shorthand for a claim about
the cross-register arrow, not a predicate of the whole object. A proposed
ontological time may be the orientation of noninvertible realization or
record composition; it is not the parameter \(t\) of (MC3c). The UCP maps in
this module are candidate measured presentations of that arrow only after a
physical construction says what they forget. [[conservation-of-causal-charge/unitarity-and-ontological-time|Unitarity
and ontological time]] owns the fuller four-register distinction.
[[algebra/quotient-unitarity-and-kernel-stabilization|The kernel-stabilization
theorem]] further proves that a prequotient transformation becomes unitary on
the response completion when it preserves the wall radical and its
semidefinite form. The observed symmetry that lifts is the image of that
stabilizer, not automatically a symmetry imposed on the whole.

## Second carrier: GNS state vectors

Define initially on the dense subspace
\(\pi_\omega(\mathcal A)\Omega_\omega\)

\[
V_\Phi\pi_\omega(a)\Omega_\omega
:=
\pi_\omega(\Phi(a))\Omega_\omega.
\tag{MC4}
\]

Kadison--Schwarz and (MC1) give

\[
\begin{aligned}
\|V_\Phi\pi_\omega(a)\Omega_\omega\|^2
&=
\omega\!\left(\Phi(a)^*\Phi(a)\right)\\
&\leq
\omega\!\left(\Phi(a^*a)\right)
=
\omega(a^*a),
\end{aligned}
\]

so \(V_\Phi\) extends uniquely to a contraction on
\(\mathcal H_\omega\). Equation (MC2) gives

\[
V_\Phi^*=V_{\Phi^\sharp},
\qquad
V_\Phi\Omega_\omega=\Omega_\omega.
\tag{MC5}
\]

These are **[EXACT]** consequences of the measured-operation hypotheses.

If \(\Phi\) is GNS symmetric, then \(V_\Phi\) is a self-adjoint contraction
and

\[
D_\Phi:=I-V_\Phi\geq0.
\tag{MC6}
\]

Its closed bounded form is

\[
\mathcal E_\Phi[\xi]
:=
\langle\xi,D_\Phi\xi\rangle,
\qquad
\ker D_\Phi=\operatorname{Fix}(V_\Phi).
\tag{MC7}
\]

This is a dimensionless distinction defect on the chosen GNS carrier. Its
vacuum-reduced edge is

\[
\kappa_\Phi
:=
\inf_{\substack{\xi\perp\Omega_\omega\\\|\xi\|=1}}
\langle\xi,D_\Phi\xi\rangle.
\tag{MC8}
\]

The statement \(\kappa_\Phi>0\) is meaningful only if the intended fixed
space is exactly \(\mathbb C\Omega_\omega\). If a nonvacuum subspace is fixed,
the form assigns those distinctions zero cost.

## Families and vacuum ergodicity

Let \(\{\Phi_i\}_{i\in I}\) be a finite or countable family of
GNS-symmetric measured operations and let \(\nu_i>0\),
\(\sum_i\nu_i=1\). The countable sums below converge in operator norm. Put

\[
V_\nu:=\sum_i\nu_iV_{\Phi_i},
\qquad
D_\nu:=I-V_\nu
=
\sum_i\nu_i(I-V_{\Phi_i}).
\tag{MC9}
\]

Because every summand is positive,

\[
\boxed{
\ker D_\nu
=
\bigcap_i\operatorname{Fix}(V_{\Phi_i}).}
\tag{MC10}
\]

Thus the exact fixed-space condition needed by a vacuum-centered theory is

\[
\bigcap_i\operatorname{Fix}(V_{\Phi_i})
=
\mathbb C\Omega_\omega.
\tag{MC11}
\]

This is **vacuum ergodicity**. It removes zero-cost nonvacuum directions; it
does not by itself prove a positive lower edge, select the family, or make
the form dynamical.

Indeed, a vacuum-only fixed space and an order-one edge can be cheap. For a
product state on
\(\mathcal A_1\bar\otimes\mathcal A_2\), the preserving expectations onto
the two tensor factors have GNS projections

\[
e_1=I\otimes P_{\Omega_2},
\qquad
e_2=P_{\Omega_1}\otimes I,
\qquad
e_1e_2=P_{\Omega_\omega}.
\]

Consequently

\[
(I-e_1)+(I-e_2)
\geq
I-P_{\Omega_\omega}.
\tag{MC12}
\]

This floor exists independently of any Hamiltonian or categorical
rigidity. It proves that fixed-space engineering plus a numerical edge is
not yet evidence of mass.

## Lazification does not supply a clock

A self-adjoint \(V_\Phi\) need not be positive. The canonical lazification

\[
B_\Phi:=\frac{I+V_\Phi}{2}
\tag{MC13}
\]

obeys

\[
0\leq B_\Phi\leq I,
\qquad
I-B_\Phi=\frac12D_\Phi.
\tag{MC14}
\]

If \(D_\Phi\geq\kappa(I-P_{\Omega_\omega})\), then

\[
B_\Phi(I-P_{\Omega_\omega})
\leq
\left(1-\frac\kappa2\right)(I-P_{\Omega_\omega}).
\tag{MC15}
\]

This remains a dimensionless discrete-step statement. Only after an
independent construction identifies an **injective** \(B_\Phi\) with one
physical Euclidean transfer step of duration \(\tau\) may spectral calculus
define the positive, possibly unbounded operator

\[
H_\tau
=
-\frac{\hbar}{\tau}\log B_\Phi,
\qquad
\operatorname{Dom}(H_\tau)=\operatorname{Dom}(\log B_\Phi).
\tag{MC16}
\]

Injectivity removes a zero spectral projection but does not keep zero out of
the continuous spectrum, so \(H_\tau\) need not be bounded. Iteration
supplies the integer \(n\) in \(B_\Phi^n\). It does not supply
\(\tau\), the equation \(t=n\tau\), or the physical energy interpretation.

## Third carrier: faithful state tangents

The same Heisenberg operation induces a map on normal states,

\[
\rho\longmapsto\rho\circ\Phi,
\]

and hence on regular predual tangents \(X\),

\[
X\longmapsto X\circ\Phi.
\tag{MC17}
\]

Where the BKM metric is finite and differentiable, monotonicity of relative
entropy gives the information-loss form

\[
\mathcal Q_{\Phi,\omega}^{\mathrm{BKM}}[X]
:=
g_\omega^{\mathrm{BKM}}(X,X)
-
g_\omega^{\mathrm{BKM}}(X\circ\Phi,X\circ\Phi)
\geq0.
\tag{MC18}
\]

In finite dimensions this is an ordinary positive quadratic form on
self-adjoint trace-zero density tangents. In Type III settings its
formulation requires faithful normal states, Araki relative entropy, a
declared tangent class, and differentiability. The inequality is a
data-processing statement, not an energy inequality.

The GNS defect (MC7) and the BKM defect (MC18) are not the same form by
notation. They act on different carriers:

\[
\begin{array}{c|c|c}
\text{form}&\text{carrier}&\text{native meaning}\\
\hline
\mathcal E_\Phi&
\mathcal H_\omega&
\text{vector attenuation under a measured operation}\\
\mathcal Q_{\Phi,\omega}^{\mathrm{BKM}}&
T_\omega\mathcal S_{\mathrm{faithful}}&
\text{loss of local statistical distinguishability}
\end{array}
\tag{MC19}
\]

An equality or comparison between them requires a score, standard-form, or
other tangent-to-GNS map with its domain and normalization proved.

## A conditional BKM--GNS bridge

There is one exact comparison once that missing map is supplied. Let

\[
\Lambda_\Phi:=\frac12(\operatorname{id}+\Phi),
\]

whose GNS implementation is \(B_\Phi\). Functional calculus for
\(0\leq B_\Phi\leq I\) gives

\[
I-B_\Phi
\leq
I-B_\Phi^2
\leq
2(I-B_\Phi),
\]

and hence

\[
\boxed{
\frac12(I-V_\Phi)
\leq
I-B_\Phi^2
\leq
I-V_\Phi.}
\tag{MC19a}
\]

Now suppose a declared BKM tangent class has been completed to a real
Hilbert space \(\mathcal T_\omega^{\mathrm{BKM}}\), and suppose there is a
real-linear isometry

\[
S:\mathcal T_\omega^{\mathrm{BKM}}
\longrightarrow \mathcal H_{\omega,\mathbb R}
\]

into the underlying real GNS Hilbert space, with
\(\langle\xi,\eta\rangle_{\mathbb R}:=
\operatorname{Re}\langle\xi,\eta\rangle\), such that

\[
S(X\circ\Lambda_\Phi)=B_\Phi SX.
\tag{MC19b}
\]

Then the BKM norm loss of the lazified operation is exactly

\[
\begin{aligned}
\mathcal Q_{\Lambda_\Phi,\omega}^{\mathrm{BKM}}[X]
&=
\langle SX,(I-B_\Phi^2)SX\rangle_{\mathbb R}\\
&\geq
\frac12\langle SX,(I-V_\Phi)SX\rangle_{\mathbb R}.
\end{aligned}
\tag{MC19c}
\]

Thus the BKM loss dominates half the GNS defect on the represented score
image—and half the categorical defect when \(\Phi\) is the selected
categorical average. The isometric intertwiner (MC19b), including its
domain, centering, and range, is a substantive theorem hypothesis; it is not
supplied by notation or by BKM monotonicity. This bridge still does not
identify \(B_\Phi\) with time evolution or either defect with energy.

There is an **[EXACT FINITE-DIMENSIONAL COROLLARY]**. For
\(\mathcal A=M_n(\mathbb C)\), a faithful density matrix \(\rho\), and a
genuinely GNS-symmetric measured operation as above, complete positivity of
the GNS adjoint gives modular covariance. If \(\Delta_\rho\) is the GNS
modular operator and

\[
f(t):=\frac{t-1}{\log t},
\qquad f(1):=1,
\]

then on centered self-adjoint scores \(A\), with

\[
\mathcal K_\rho(A):=\int_0^1\rho^sA\rho^{1-s}\,\mathrm ds,
\]

the canonical map

\[
S\!\left(\mathcal K_\rho(A)\right)
:=
f(\Delta_\rho)^{1/2}\pi_\rho(A)\Omega_\rho
\tag{MC19d}
\]

is a BKM-to-GNS isometry, has centered range in
\(\Omega_\rho^\perp\), and satisfies (MC19b). Thus (MC19c) is canonical in
this finite faithful setting rather than an arbitrary choice of score map;
the modular-function form of the metric is reviewed in
[[library/monotone-riemannian-metrics-and-relative-entropy/inq]].

[[library/christensen-evans-theorem-and-extensions-of-gns-symmetric-quantum-markov-semigroups/inq|Wirth's
GNS-symmetric extension theorem]] supplies the modularly covariant Markov
setting used here. [[library/the-differential-structure-of-generators-of-gns-symmetric-quantum-markov-semigroups/inq|The
Tomita-bimodule differential theorem]] gives the domain-sensitive
nontracial grammar for generators; it does not by itself supply a Poincare
lower bound.

### An operator-monotone gap transfer on arbitrary von Neumann algebras

There is now a stronger theorem on the observable carrier. Let
\((\Phi_t)_{t\geq0}\) be a quantum Markov semigroup on an arbitrary von
Neumann algebra with faithful normal invariant state \(\omega\). Suppose it
has GNS gap \(\lambda>0\): in the scalar-fixed case,

\[
\|\Phi_t(x)\|_{\mathrm{GNS}}
\leq
e^{-\lambda t}\|x\|_{\mathrm{GNS}},
\qquad \omega(x)=0.
\tag{MC19e}
\]

[[library/the-kms-and-gns-spectral-gap-of-quantum-markov-semigroups/inq|Wirth's operator-monotone interpolation theorem]]
implies

\[
\boxed{
\|\Phi_t(x)\|_f
\leq
e^{-\lambda t}\|x\|_f}
\tag{MC19f}
\]

for every normalized operator-monotone \(f\), including
\(f_{\mathrm{BKM}}(t)=(t-1)/\log t\). If the fixed-point algebra is \(N\) rather than
\(\mathbb C\mathbf1\), the same result holds on \(\ker E\), where
\(E:\mathcal A\to N\) is the \(\omega\)-preserving conditional expectation.

This removes a formerly open comparison on one precise carrier: a GNS
Markov edge automatically persists in the **observable BKM norm**, even in
type III. It does not prove (MC19b)--(MC19c). Those equations concern the
dual BKM metric on **state tangents**, and still require the score or predual
intertwiner, its common domain, and physical range. Nor does (MC19f) identify
the Markov parameter with clock time or its generator with energy. The
same-carrier property-\((T)\) application is developed in
[[contemporary-puzzles/yang-mills-mass-gap/kazhdan-markov-process-carrier]].

The Type-III extension is not formal bookkeeping. There
\(f(\Delta_\omega)^{1/2}\) and its inverse need not be bounded. One must
declare a common invariant Tomita core, prove the domains and closability of
the score map and its intertwining relation, and prove that its closed range
covers the physical directions on which a gap is claimed.

## Parameter Hessians are pullbacks, not new carriers

Let \(\lambda\mapsto\rho_\lambda\) be a regular faithful state family on one
fixed algebra, and let

\[
J_\lambda:T_\lambda M\longrightarrow
T_{\rho_\lambda}\mathcal S_{\mathrm{faithful}},
\qquad
J_\lambda v:=D\rho_\lambda(v).
\tag{MC20}
\]

The response metric on parameter space is the bilinear pullback

\[
G_\lambda(v,w)
:=
g_{\rho_\lambda}^{\mathrm{BKM}}
\!\left(J_\lambda v,J_\lambda w\right).
\tag{MC21}
\]

Equivalently, if \(g^\flat\) denotes the metric map from the target tangent
to its cotangent and \(J_\lambda^*\) is the algebraic dual map, then

\[
G_\lambda^\flat
=
J_\lambda^*g_{\rho_\lambda}^{\mathrm{BKM},\flat}J_\lambda.
\tag{MC21'}
\]

Because the target BKM metric is positive definite, the pullback radical is
exactly

\[
\boxed{
\operatorname{rad}G_\lambda
=
\ker J_\lambda.}
\tag{MC21a}
\]

More generally, for positive target metrics \(g_\alpha\), analysis maps
\(J_\alpha\), and positive weights \(w_\alpha\),

\[
Q[v]
:=
\sum_\alpha w_\alpha
g_\alpha(J_\alpha v,J_\alpha v)
\]

obeys

\[
\boxed{
\ker Q
=
\bigcap_\alpha\ker J_\alpha.}
\tag{MC21b}
\]

This is the pullback-frame theorem. Joint infinitesimal injectivity removes
the radical in finite dimensions; a uniform positive lower frame is the
stronger requirement in an infinite-dimensional physical tangent.
For inner-unitary state paths on one von Neumann algebra,
[[modular-cocycle-tomography/inq|modular cocycle tomography]] computes this
joint kernel exactly as an intersection of state centralizers and expresses
that intersection through Connes cocycles on one reference carrier.

There is an immediate finite-rank obstruction. If the physical vacuum
complement is infinite dimensional while
\(\bigoplus_\alpha\operatorname{Ran}J_\alpha\) is finite dimensional, then
\(\bigcap_\alpha\ker J_\alpha\neq\{0\}\). No finite family of
finite-dimensional response targets can therefore satisfy

\[
Q[v]\geq\kappa\|v\|_{\mathrm{phys}}^2
\qquad(\kappa>0)
\tag{MC21c}
\]

on the complete vacuum complement. A successful construction needs a joint
analysis map with a uniform closed-range bound. This could come from a finite
family of infinite-dimensional targets, an infinite or direct-integral
family, or a genuinely same-carrier operator with its own proved
vacuum-complement edge.

For a finite affine exponential family, \(G_\lambda\) is the Hessian of the
log-partition potential. Before reduction it can be only a positive
semidefinite premetric. It becomes a metric after quotienting the radical
only on a constant-rank neighborhood where the quotient is smooth, the form
is basic, and the affine connection descends. Hessianity additionally
requires the full mixed-derivative integrability conditions developed in
[[hessian-response-geometry/inq]].

The form \(G_\lambda\) canonically defines a map
\(T_\lambda M\to T_\lambda^*M\), not an endomorphism of
\(T_\lambda M\). Matrix eigenvalues require a separately chosen source norm
or Riesz identification and change when the parameter tangents are
renormalized. Likewise, a real state-tangent form does not automatically
extend to a positive Hermitian form on a complex physical energy core.

Equation (MC21) acts on \(T_\lambda M\), not on
\(\mathcal H_\omega\). Fourier covariance inversion, spatial precision,
localized energy, and mass are later consumer maps. In particular, the
open W2 arrow in [[causal-wall-spectral-theory/inq]] is precisely a
carrier-changing map from such state response to a spatial
probability-precision operator.

## Closed-form transport across carriers

Let \(q\) be a densely defined closed nonnegative Hermitian form on a Hilbert
space \(\mathcal K\), with associated positive self-adjoint operator \(L\).
If

\[
R:\mathcal K\longrightarrow\mathcal K'
\]

is a bounded Hilbert-space isomorphism with bounded inverse, define

\[
\operatorname{Dom}(q_R):=R\,\operatorname{Dom}(q),
\qquad
q_R[R\xi,R\eta]:=q[\xi,\eta].
\tag{MC21d}
\]

Then \(q_R\) is densely defined, closed, and nonnegative. With
\(R^{-*}:=(R^{-1})^*\), its associated operator is the congruence

\[
\boxed{
L_R=R^{-*}LR^{-1},
\qquad
\operatorname{Dom}(L_R)=R\,\operatorname{Dom}(L).}
\tag{MC21e}
\]

In particular,

\[
\ker L_R=R\ker L.
\tag{MC21e'}
\]

If \(N=\ker L\) and the original form obeys

\[
q[\xi]\geq\kappa\,\operatorname{dist}_{\mathcal K}(\xi,N)^2,
\]

then the transported form obeys the norm-distorted bound

\[
q_R[u]
\geq
\frac{\kappa}{\|R\|^2}
\operatorname{dist}_{\mathcal K'}(u,RN)^2.
\tag{MC21e''}
\]

Thus positivity, closedness, the kernel, and coercivity modulo the kernel
transport exactly in the stated senses. A unitary \(R\) preserves the
numerical spectrum; a general bounded congruence is not a similarity and
need not do so.

This theorem licenses an inverse-conjugation formula only after both Hilbert
carriers, form domains, and the bounded inverse have been constructed. If
\(R\) has a kernel, nonclosed range, or changes a configuration carrier into
a phase space without a chosen polarization and state norm, (MC21e) is not
defined. One must instead quotient, pull back, short a form, or construct a
different comparison.

Form congruence transports a response; it does not change its native
register. A spatial probability precision transported by \(R\) remains a
spatial probability precision. It does not become a Hamiltonian, transfer
generator, or Poincare Casimir.

## The generic response-to-energy theorem

Let \(\mathfrak h_{\mathrm{phys}}\) be a densely defined closed nonnegative
form on a physical Hilbert space, with associated self-adjoint Hamiltonian
\(H_{\mathrm{phys}}\) and normalized vacuum \(\Omega\). Let
\(\mathcal K_{\mathrm{phys}}\subset
\operatorname{Dom}(\mathfrak h_{\mathrm{phys}})\cap\Omega^\perp\) be a
complex linear subspace, and let
\(J:\mathcal K_{\mathrm{phys}}\to\operatorname{Dom}(q)\) be complex linear.
Suppose

\[
\|J\psi\|_{\mathcal K}^2
\geq
b_J\|\psi\|_{\mathrm{phys}}^2,
\qquad
b_J>0.
\tag{MC21f}
\]

Assume the response form has an edge on the represented image,

\[
q[J\psi]\geq\kappa\|J\psi\|_{\mathcal K}^2,
\qquad
\kappa>0,
\tag{MC21g}
\]

and that an independently normalized energy comparison gives

\[
\mathfrak h_{\mathrm{phys}}[\psi]
\geq
\eta_{\mathrm{sol}}E_*\,q[J\psi],
\qquad
\eta_{\mathrm{sol}}>0,
\quad E_*>0.
\tag{MC21h}
\]

Then

\[
\boxed{
\mathfrak h_{\mathrm{phys}}[\psi]
\geq
\eta_{\mathrm{sol}}E_*\kappa b_J
\|\psi\|_{\mathrm{phys}}^2.}
\tag{MC21i}
\]

If \(\mathcal K_{\mathrm{phys}}\) is a form core for the restriction of
\(\mathfrak h_{\mathrm{phys}}\) to \(\Omega^\perp\) and
\(\ker H_{\mathrm{phys}}=\mathbb C\Omega\), then

\[
\Delta_E
:=
\inf\sigma\!\left(H_{\mathrm{phys}}\big|_{\Omega^\perp}\right)
\geq
\eta_{\mathrm{sol}}E_*\kappa b_J.
\tag{MC21j}
\]

This implication is exact; its premises contain the physical work. In
particular, a real BKM Hessian must first have a positive Hermitian extension
to the complex energy core, \(J\) must cover every physical nonvacuum
direction, and \(E_*\) must be selected without fitting the desired gap.

The operator registers are therefore:

\[
\begin{array}{c|c}
\text{object}&\text{extra datum needed before energy}\\
\hline
\text{BKM or Fisher response}&
\text{complex physical analysis map and Hermitian extension}\\
\text{spatial probability precision}&
\text{configuration-to-energy or OS/kinetic solder}\\
\text{Dirichlet or Markov defect}&
\text{identification with physical Euclidean time}\\
\text{positive transfer step}&
\text{injectivity and calibrated duration}\\
\text{Hamiltonian edge}&
\text{Poincare reconstruction before invariant mass}
\end{array}
\tag{MC21k}
\]

## Categorical fusion-action specialization

A measured action of a rigid \(C^*\)-tensor category is a family
\(\{\Phi_\alpha\}\) satisfying, in addition to (MC1)--(MC2), the
dual compatibility

\[
\Phi_{\mathbf1}=\operatorname{id},
\qquad
\Phi_\alpha^\sharp=\Phi_{\bar\alpha}
\]

and the normalized fusion law

\[
\Phi_\alpha\Phi_\beta
=
\sum_\gamma
\frac{N_{\alpha\beta}^{\ \ \gamma}d(\gamma)}
{d(\alpha)d(\beta)}
\Phi_\gamma.
\tag{MC22}
\]

Its GNS implementations obey the same normalized fusion law, and

\[
\Theta([\alpha]):=d(\alpha)V_{\Phi_\alpha}
\tag{MC23}
\]

is an algebraic fusion-\(*\)-representation. To invoke categorical property
\((T)\), this representation must additionally be annularly admissible:
it must occur as the weight-zero restriction of a full annular or tube
representation. That is a further construction, not a consequence of
(MC22).

For a symmetric finitely supported probability measure \(\mu\) on the simple
objects, set

\[
V_\mu:=\sum_\alpha\mu_\alpha V_{\Phi_\alpha},
\qquad
\mu_{\bar\alpha}=\mu_\alpha.
\tag{MC23a}
\]

If the action is admissible,
\(\operatorname{Fix}(V_\mu)=\mathbb C\Omega_\omega\), and \(\mu\) is a
categorical Kazhdan averaging measure, categorical property \((T)\) gives

\[
I-V_\mu
\geq
\kappa_{\mathcal C}(I-P_{\Omega_\omega})
\tag{MC24}
\]

For a single self-dual simple tensor generator \(X\), one may take
\(\mu=\delta_X\) only after proving that this particular normalized fusion
element has the Kazhdan estimate. This is the exact conditional shape needed
in
[[contemporary-puzzles/yang-mills-mass-gap/categorical-action-on-the-neutral-wilson-carrier]].
It is still dimensionless. A physical mass gap requires a same-core
comparison with the vacuum-subtracted clock-energy form and an independent
duration or localization-width normalization.

## The reusable carrier stack

The safe order of construction is

\[
\boxed{
\begin{aligned}
(\mathcal A,\omega,\Phi)
&\longrightarrow
(\mathcal H_\omega,\Omega_\omega,V_\Phi,D_\Phi),\\
(\mathcal A,\omega,\Phi)
&\longrightarrow
(T_\omega\mathcal S,\mathcal Q_{\Phi,\omega}^{\mathrm{BKM}}),\\
T_\lambda M
&\xrightarrow{\,J_\lambda\,}
T_{\rho_\lambda}\mathcal S,\\
\mathcal K_{\mathrm{phys}}
&\xrightarrow{\,J_{\mathrm{phys}}\,}
\mathcal H_\omega\ \text{or}\ T_\omega\mathcal S,\\
\text{response defect}
&\xrightarrow{\text{same-core comparison}}
\text{clock-energy form}.
\end{aligned}}
\tag{MC25}
\]

Each arrow names a theorem obligation. Reusing one symbol across two rows
does not construct that arrow.

The special modules then occupy precise positions:

- [[binary-information-geometry/inq]] is a commutative one-parameter
  state-family example of (MC20)--(MC21); its Witten--Darboux operator acts
  only after a separate half-density unitary moves the Fisher measure to an
  \(L^2\) carrier.
- [[hessian-response-geometry/inq]] governs when the parameter response in
  (MC21) is genuinely Hessian and when its block decomposition has a common
  potential.
- [[causal-wall-spectral-theory/inq]] seeks a carrier-changing consumer from
  state response to spatial precision and then a separate Lorentzian field
  realization.
- [[contemporary-puzzles/yang-mills-mass-gap/carrier-first-reversal]] asks
  whether an upstream defect can be compared on the complete physical
  vacuum carrier with the Hamiltonian form.
- [[transported-response-observability-solder/inq]] shows how a closed
  positive response on that carrier yields the bounded analysis
  $\sqrt\eta(I-e^{-\tau G})^{1/2}$, and how a transported lower frame for
  those analyses forces a physical transfer product to contract once the
  independent same-carrier solder is proved.

## Construction gates

1. Declare the algebra, faithful state, and direction of the operation.
2. Prove state preservation and existence of the stated adjoint.
3. Name the carrier of every form: algebra, GNS vectors, state tangents, or
   parameter tangents.
4. Identify the joint fixed space before quoting a positive edge.
5. Prove annular admissibility before importing categorical rigidity.
6. Construct any tangent-to-GNS, regional, Fourier, or physical analysis
   map and prove its kernel and lower frame.
7. Do not call a positive contraction a transfer operator until positivity,
   injectivity, clock normalization, and the OS or direct energy
   identification have been established.
8. Keep the dimensionless coercivity coefficient separate from the
   dimensional yardstick.

This carrier stack is the common formal core. Particular models must still
say what the operation operates on, what it forgets, what its fixed vectors
mean, and why its attenuation is physical time rather than merely algebraic
iteration.
