# The Two-Expectation Angle Process

Two trace-preserving conditional expectations canonically determine a GNS-symmetric quantum Markov semigroup without an independently chosen Markov kernel: the palindromic channel \(E_PE_QE_P\) has fixed space \(L^2(P\cap Q)\), and its reduced generator has the exact Friedrichs-angle gap \(1-c_F(P,Q)^2\). This gives a genuine process construction from an ordered pair of information-losing realizations, but it does not make the retained local carrier stiff: the common range remains the entire kernel, and a Yang--Mills consequence requires a separate, uniformly bounded-below analysis map from the physical vacuum complement into the reduced disagreement carrier, followed by an energy-form comparison.

**Status: [EXACT] for the finite tracial UCP/GNS theorem, the one-expectation retained-sector no-go, and the fixed-index nonuniformity counterexample; [CONDITIONAL] for transfer through the stated carrier and form inequalities; [OPEN] for a net-natural Yang--Mills pair, a vacuum-complete analysis map, regulator-uniform constants, continuum passage, and Poincare calibration.**

## The exact angle-process theorem

Let \(M\) be a finite von Neumann algebra with faithful normal trace \(\tau\), and let \(P,Q\subset M\) be unital von Neumann subalgebras. Write

$$
E_P:M\to P,
\qquad
E_Q:M\to Q
$$

for the unique \(\tau\)-preserving conditional expectations. On

$$
\mathcal H=L^2(M,\tau)
$$

their GNS implementations are the orthogonal projections

$$
p=e_P,
\qquad
q=e_Q.
$$

Let

$$
r=e_{P\cap Q}=p\wedge q
$$

be the projection onto \(L^2(P\cap Q,\tau)\), and define the Friedrichs cosine

$$
c_F(P,Q)
:=
\|pq-r\|
=
\sqrt{\|pqp-r\|}.
$$

In [[library/angles-between-two-subfactors/inq|the Sano--Watatani finite-index subfactor setting]], this is the largest cosine of their angle after the common range has been removed.

**Theorem.** Define

$$
\Phi:=E_PE_QE_P
$$

and Poissonize it by

$$
\mathsf P_t
:=
\exp\!\bigl(t(\Phi-I)\bigr)
=
e^{-t}\sum_{n=0}^{\infty}\frac{t^n}{n!}\Phi^n,
\qquad t\geq0.
$$

Then:

1. \(\Phi\) is normal, unital, completely positive, \(\tau\)-preserving, and GNS-self-adjoint. Its GNS implementation is the positive contraction

   $$
   A_\Phi=pqp.
   $$

2. \((\mathsf P_t)_{t\geq0}\) is a uniformly continuous, \(\tau\)-preserving, GNS-symmetric quantum Markov semigroup. Its GNS implementation and positive generator are

   $$
   V_t=e^{-tL_{P,Q}},
   \qquad
   L_{P,Q}=I-pqp.
   $$

3. Its bounded completely Dirichlet form has the exact decomposition

   $$
   \begin{aligned}
   \mathcal D_{P,Q}[\xi]
   &:=\langle\xi,(I-pqp)\xi\rangle\\
   &=\|(I-p)\xi\|^2+\|(I-q)p\xi\|^2,
   \end{aligned}
   $$

   and therefore

   $$
   \ker L_{P,Q}
   =\operatorname{Fix}_{\mathcal H}(pqp)
   =\operatorname{Fix}_{\mathcal H}(V_t)
   =L^2(P\cap Q,\tau).
   $$

   Here the \(V_t\) identity holds for every \(t>0\). On the algebra itself, for every \(t>0\),

   $$
   \operatorname{Fix}_M(\mathsf P_t)
   =
   \operatorname{Fix}_M(\Phi)
   =\{x\in M:\Phi(x)=x\}
   =P\cap Q.
   $$

4. On the reduced carrier

   $$
   \mathcal H_{\mathrm{dis}}
   :=(I-r)L^2(M,\tau),
   $$

   the sharp spectral bound is

   $$
   \boxed{
   L_{P,Q}
   \geq
   \bigl(1-c_F(P,Q)^2\bigr)(I-r).}
   $$

   If \(\mathcal H_{\mathrm{dis}}\neq0\), the bottom of the reduced spectrum is exactly

   $$
   \gamma_{P,Q}=1-c_F(P,Q)^2.
   $$

5. If the expectations form a commuting square,

   $$
   E_PE_Q=E_QE_P=E_{P\cap Q},
   $$

   then \(pqp=r\) and the reduced gap is exactly \(1\).

The palindromic order matters. The shorter composition \(E_PE_Q\) is UCP but need not be GNS-self-adjoint; inserting the final \(E_P\) produces the positive self-adjoint implementation \(pqp=(qp)^*(qp)\).

The construction is canonical only after the pair is marked or ordered. Reversing the base gives \(E_QE_PE_Q\), with GNS implementation \(qpq\); it has the same nonzero angle spectrum and the same reduced gap, but a different ambient range. An unordered pair does not choose between these two channels. The coefficient of \(t\) in the Poissonization is likewise a dimensionless clock convention: replacing \(t\) by \(at\) multiplies the generator and gap by \(a>0\). The expectations determine the normalized process shape and angle edge, not a physical time or energy unit.

**Proof.** Conditional expectations are normal UCP trace-preserving maps, so the same is true of their composition. Their GNS implementations are \(p\) and \(q\), hence \(\Phi\) is implemented by the positive self-adjoint contraction \(pqp\). The Poisson series is a norm-convergent convex combination of the UCP maps \(\Phi^n\), and the exponential law gives the semigroup property. At every matrix level it remains a conservative Markov semigroup, so its symmetric form is completely Dirichlet.

The form identity follows from

$$
I-pqp=(I-p)+p(I-q)p.
$$

Its two nonnegative summands vanish simultaneously exactly when \(p\xi=\xi=q\xi\), which proves the kernel statement. Since \(r\leq p,q\),

$$
pqp-r=(pq-r)(qp-r)
$$

and therefore

$$
\|pqp-r\|=\|pq-r\|^2=c_F(P,Q)^2.
$$

The positive operator \(pqp-r\) is supported on \((I-r)\mathcal H\). Thus its norm is the top of its reduced spectrum, giving

$$
pqp-r\leq c_F(P,Q)^2(I-r)
$$

and the claimed sharp lower edge for \(I-pqp\). In a commuting square \(pq=r\), so the last assertion follows. \(\square\)

This theorem differs from the even two-projection operator \(2I-p-q\) analyzed in [[subfactor-angle-coercivity-and-the-index-firewall]]. That operator has reduced edge \(1-c_F\); the palindromic Markov generator has reduced edge \(1-c_F^2\). Both have the same full-carrier kernel \(L^2(P\cap Q)\).

## One expectation gaps only what it discards

Let \(E:M\to N\subsetneq M\) be the \(\tau\)-preserving expectation and \(e=e_N\) its GNS projection. The expectation alone canonically determines

$$
\mathsf S_t
:=
E+e^{-t}(I-E)
=
e^{-t}I+(1-e^{-t})E.
$$

Idempotency of \(E\) gives \(\mathsf S_s\mathsf S_t=\mathsf S_{s+t}\). Its GNS implementation, generator, form, and fixed space are

$$
e+e^{-t}(I-e),
\qquad
L_E=I-e,
\qquad
\mathcal D_E[\xi]=\|(I-e)\xi\|^2,
\qquad
\ker L_E=L^2(N,\tau).
$$

For every \(t>0\), its fixed algebra is \(\operatorname{Fix}_M(\mathsf S_t)=N\).

Thus \(L_E\) has the exact dimensionless gap \(1\), in the displayed unit-rate convention, on \(L^2(N)^\perp\), while

$$
L_E\!\restriction_{L^2(N)}=0.
$$

If \(N\) is the retained local algebra, the canonical expectation process supplies no coercivity at all on its retained vacuum complement. It measures only departure from the range. This remains true even though \(E\) is faithful in the operator-algebraic sense: \(\tau(E(x^*x))=\tau(x^*x)\) implies \(E(x^*x)=0\Rightarrow x=0\). The relevant realization loss is linear noninjectivity, not failure of positivity-faithfulness. [[algebra/nonfaithful-realization|Nonfaithful realization]] owns the separate categorical obstruction.

The two-expectation construction improves the geometry of this lost sector, but does not reverse the conclusion. Its entire common retained carrier \(L^2(P\cap Q)\) is still fixed pointwise.

## Fixed index does not make the edge uniform

[[subfactor-angle-coercivity-and-the-index-firewall|The index firewall]] owns
the fixed-index and relative-position audit. Its Bakshi--Guin spin-model
family has, for nonzero \(\delta=\alpha-\beta\),

$$
[R:R_\alpha]=[R:R_\beta]=2,
\qquad
[R:R_\alpha\cap R_\beta]=4,
$$

while \(c_F(\delta)=|\cos\delta|\). Therefore the present palindromic
process has

$$
\boxed{
\gamma_\Phi(\delta)
=1-c_F(\delta)^2
=\sin^2\delta
\longrightarrow0}
$$

as \(\delta\to0\), although all three indices remain fixed. Thus the fixed
pair theorem \(c_F<1\) does not become an index-only uniform estimate, and
neither one inclusion's Q-system nor its standard invariant determines this
mixed-process gap.

## The precise physical carrier obligation

The angle process acts on the disagreement carrier \((I-r)L^2(M,\tau)\). A Yang--Mills Hamiltonian acts on a different object: a reconstructed physical Hilbert space \(\mathcal K_{\mathrm{phys}}\) with vacuum projection \(P_0\) and closed nonnegative energy form \(\mathfrak h\), where \(\ker\mathfrak h=\operatorname{Ran}P_0\). The two gaps can be compared only by an additional typed map.

Let \(\mathcal C\subset D(\mathfrak h)\) be a complex form core invariant under \(P_0\), put \(\mathcal C_\perp=(I-P_0)\mathcal C\), and let

$$
J:
\mathcal C_\perp
\longrightarrow
(I-r)L^2(M,\tau)
$$

be a complex-linear analysis map. Suppose there are constants \(b>0\) and \(0<C<\infty\), obtained independently of the desired spectrum, such that for every \(\Psi\in\mathcal C_\perp\),

$$
\boxed{
\|J\Psi\|^2
\geq
b\|\Psi\|^2}
\tag{TA1}
$$

and

$$
\boxed{
\mathcal D_{P,Q}[J\Psi]
\leq
C\,\mathfrak h[\Psi].}
\tag{TA2}
$$

Then the exact angle inequality gives

$$
\mathfrak h[\Psi]
\geq
\frac{b\bigl(1-c_F(P,Q)^2\bigr)}{C}
\|\Psi\|^2.
$$

Because \(\mathcal C\) is a form core and \(P_0\) is the kernel projection,
this lower bound extends to
\(D(\mathfrak h)\cap(I-P_0)\mathcal K_{\mathrm{phys}}\), not to the vacuum
direction. Equivalently, on the full form domain,

$$
\mathfrak h[\Psi]
\geq
\frac{b\bigl(1-c_F(P,Q)^2\bigr)}{C}
\|(I-P_0)\Psi\|^2.
$$

Thus the conditional physical energy gap is

$$
\boxed{
\Delta_E
\geq
\frac{b\bigl(1-c_F(P,Q)^2\bigr)}{C}.}
$$

Condition (TA1) is the missing visibility theorem: every physical nonvacuum direction must register in the reduced angle carrier with a uniform lower frame. Condition (TA2) is the same-carrier energy solder: the derived distinction cost must be bounded above by physical energy on one complex form core. Neither follows from conditional expectations, finite index, a commuting square, or the standard invariant.

For a regulator family indexed by \(\rho\), the nonclosing requirement is the combined bound

$$
\boxed{
\inf_\rho
\frac{b_\rho\bigl(1-c_{F,\rho}^2\bigr)}{C_\rho}
>0.}
$$

Separate positivity at every regulator does not suffice. Passing this inequality to a continuum theory additionally requires compatible carrier identifications, convergence of the closed physical forms and vacuum projections strong enough to prevent low-energy escape, and identification of \(\mathfrak h\) with reconstructed time translation. Calling the resulting energy edge a Yang--Mills **mass** gap further requires the Poincare representation and its invariant mass operator.

[[measured-response-carriers/inq|The measured-response carrier stack]] owns the general analysis-map and lower-frame grammar. [[trace-dirichlet-descent/inq|Trace Dirichlet descent]] owns a different construction: it derives a local Dirichlet form by infimizing a supplied whole-register response over forgotten lifts. The present theorem supplies no whole response and performs no such pushforward; it derives only a bounded angle process on the ambient \(L^2(M,\tau)\). Its virtue is exactness, and its limit is equally exact: relative position can stiffen disagreement, but only a proved carrier transfer can make that stiffness physical.
