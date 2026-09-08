# State-Tangent BKM Bridge

Relative-entropy loss acts on state tangents, whereas a measured operation's GNS defect acts on vectors. An isometric intertwiner compares those forms after lazification. For a finite matrix algebra, a faithful state and a GNS-symmetric operation supply a canonical bridge through the logarithmic-mean score map. Extending that bridge to a Type-III physical carrier requires its domains, closure and range to be proved.

## Faithful state tangents

Let \(\mathcal A\) be a von Neumann algebra with faithful normal state
\(\omega\), and let \(\Phi:\mathcal A\to\mathcal A\) be normal, unital,
completely positive and \(\omega\)-preserving. These are the
[[measured-response-carriers/measured-operations-and-gns-defects#The measured operation|measured-operation hypotheses]].
The Heisenberg operation induces a map on normal states,

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

For a GNS-symmetric operation, the
[[measured-response-carriers/measured-operations-and-gns-defects#Second carrier: GNS state vectors|GNS defect (MC7)]]
is \(\mathcal E_\Phi[\xi]=\langle\xi,(I-V_\Phi)\xi\rangle\), where
\(V_\Phi(a\Omega_\omega)=\Phi(a)\Omega_\omega\). It and the BKM defect
(MC18) are not the same form by notation. They act on different carriers:

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

[[measured-response-carriers/descent-loss-cocycle-and-recovery-fork|The
descent-loss cocycle]] makes composition and output passage explicit.
Incoming state-tangent losses add with transported arguments under channel
composition. For a preserving expectation, the loss is the squared BKM norm
of the forgotten component, while its infimum over lifts of every retained
tangent is zero. A general contraction instead defines a minimum-lift output
form relative to its two supplied metrics; these output forms compose by
infimization, not ordinary addition. Neither operation turns an incoming
information defect into physical energy.

## A conditional BKM--GNS bridge

Assume now that \(\Phi\) is GNS symmetric, so \(V_\Phi\) is a
self-adjoint contraction. The
[[measured-response-carriers/lazification-and-clock-calibration#Lazification does not supply a clock|lazified implementation]]
is \(B_\Phi=(I+V_\Phi)/2\), with \(0\leq B_\Phi\leq I\).
There is an exact comparison once the tangent map is supplied. Let

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

## The canonical finite-dimensional bridge

There is an **[EXACT FINITE-DIMENSIONAL COROLLARY]**. For
\(\mathcal A=M_n(\mathbb C)\), a faithful density matrix \(\rho\), and a
GNS-symmetric measured operation as above,
[[library/christensen-evans-theorem-and-extensions-of-gns-symmetric-quantum-markov-semigroups/inq|Wirth's Proposition 2.2]]
gives modular covariance: \(\Phi\sigma_t^\rho=\sigma_t^\rho\Phi\), and
\(V_\Phi\) commutes with the modular functional calculus. If \(\Delta_\rho\) is the GNS
modular operator and

\[
f(t):=\frac{t-1}{\log t},
\qquad f(1):=1,
\]

then on centered self-adjoint scores \(A=A^*\), with
\(\operatorname{Tr}(\rho A)=0\), define

\[
\mathcal K_\rho(A):=\int_0^1\rho^sA\rho^{1-s}\,\mathrm ds.
\]

The observable BKM inner product is
\(\langle A,B\rangle_{\rho,\mathrm{obs}}=
\operatorname{Tr}(A^*\mathcal K_\rho(B))\).
The density-tangent metric is its inverse:

\[
g_\rho^{\mathrm{BKM}}(X,Y)
=\operatorname{Re}\operatorname{Tr}
\bigl(X\mathcal K_\rho^{-1}(Y)\bigr),
\qquad X=X^*,\ Y=Y^*,\quad\operatorname{Tr}X=\operatorname{Tr}Y=0.
\]

Faithfulness makes \(\mathcal K_\rho\) invertible, and
\(X=\mathcal K_\rho(A)\) identifies centered scores with all self-adjoint
trace-zero density tangents. This is a declared duality map between two
carriers; the observable and density-tangent norms do not apply the same
operator to the same matrix. The canonical map

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

To check the isometry, use the Hilbert--Schmidt GNS realization
\(\pi_\rho(A)\Omega_\rho=A\rho^{1/2}\). Modular functional calculus gives

\[
\left\|f(\Delta_\rho)^{1/2}A\rho^{1/2}\right\|_2^2
=\operatorname{Tr}(A\mathcal K_\rho(A))
=g_\rho^{\mathrm{BKM}}(\mathcal K_\rho(A),\mathcal K_\rho(A)).
\]

Also \(f(\Delta_\rho)^{1/2}\Omega_\rho=\Omega_\rho\), so centering
of the score gives centering of its image. If \(\Phi_*\) is the trace
adjoint on densities, GNS symmetry and modular covariance give

\[
\Phi_*\mathcal K_\rho(A)=\mathcal K_\rho(\Phi(A)).
\]

Together with commutation of \(V_\Phi\) and \(f(\Delta_\rho)^{1/2}\),
this proves \(S\Phi_*=V_\Phi S\), hence (MC19b) after lazification.
The finite calculation proves the tangent-to-GNS bridge on its stated
range; it does not identify that range with a separately chosen physical
excitation space.

## The Type-III domain and range obligations

In Type III, \(f(\Delta_\omega)^{1/2}\) and its inverse need not be
bounded. To extend the state-tangent bridge, declare a common invariant
Tomita core, prove the score map's domains and closability and its
intertwining relation, and prove that its closed range covers the physical
directions on which a gap is claimed.

[[library/the-differential-structure-of-generators-of-gns-symmetric-quantum-markov-semigroups/inq|The Tomita-bimodule differential theorem]]
gives the domain-sensitive nontracial grammar for generators; it does not
by itself supply a Poincare lower bound. The separate
[[measured-response-carriers/observable-bkm-gap-transfer|observable BKM gap transfer]]
already holds on arbitrary von Neumann algebras without proving this
state-tangent intertwiner or its physical range.
