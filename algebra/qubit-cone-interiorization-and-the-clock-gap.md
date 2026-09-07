# Qubit Cone Interiorization and the Clock Gap

On the qubit positive cone, uniform contraction of the normalized positive base into its interior measures exactly the centered gap of a trace-symmetric quantum Markov generator. The order unit, state metric, cone and generator act on the same matrix carrier. This is a concrete bridge from a dynamic cone estimate to a positive Hilbert clock, not a claim that the static cone fixes a rate. An explicit family keeps the cone and two decay rates fixed while its remaining rate tends to zero. The Hilbert clock is not automatically an observable-algebra automorphism or a physical spacetime evolution.

## The normalized positive base covers every centered direction

Use \(M_2(\mathbb C)\), its real Hermitian subspace, normalized trace \(\tau=\operatorname{Tr}/2\), and Pauli matrices \(\sigma_1,\sigma_2,\sigma_3\). Put

\[
X=x_0I+x\cdot\sigma,\qquad
h(X,Y)=\tau(XY),\qquad
\theta(X)=\tau(X)=x_0.
\tag{QI1}
\]

Then \(h(X,X)=x_0^2+|x|^2\), the order unit \(I\) has norm one, and
\[
X\geq0\quad\Longleftrightarrow\quad x_0\geq|x|.
\tag{QI2}
\]
Thus the [[directed-response-and-lorentzian-signature|directed-response quotient]] is
\[
\mathscr Q(X)=\frac{h(X,X)}{\theta(X)^2}
=1+\frac{|x|^2}{x_0^2}\leq2
\quad(X\geq0,\ X\ne0).
\tag{QI3}
\]

The normalized positive base is exactly the ball
\[
\mathcal B=\{B\geq0:\tau B=1\}
=\{I+X:X=X^*,\ \tau X=0,\ h(X,X)\leq1\}.
\tag{QI4}
\]

This spin-factor identity is decisive: every centered real unit direction lies on the boundary of \(\mathcal B-I\). In [[positive-cone-processes-and-the-complex-corner|the positive-cone process construction]], \(\theta\) and \(h\) are also the negative first derivative and Hessian of \(-\tfrac12\log\det\) at \(I\). Thus this test uses that corner's actual order-unit response. In higher matrix rank the trace-normalized positive base is not this Euclidean ball, so the equality below cannot be copied without a new norm comparison.

## Exact interiorization–gap theorem

Let \(T_s=e^{-sL}\), \(s\geq0\), be a continuous unital completely positive semigroup preserving \(\tau\), self-adjoint for
\(\langle X,Y\rangle_\tau=\tau(X^*Y)\). Equivalently here, \(L\) is a nonnegative self-adjoint matrix on this complex Hilbert space, \(LI=0\), and the specified exponential is UCP. Positivity and trace preservation make \(T_s\mathcal B\subseteq\mathcal B\). The centered complex subspace \(\mathcal K=I^\perp\) reduces \(L\). Define

\[
\delta=\min\sigma(L|_{\mathcal K}),\qquad
M(s)=\sup_{B\in\mathcal B}
\big[\mathscr Q(T_sB)-1\big],\qquad s>0.
\tag{QI5}
\]

Then

\[
\boxed{M(s)=\|T_s|_{\mathcal K}\|^2=e^{-2s\delta}.}
\tag{QI6}
\]

Because \(\tau(T_sB)=1\), the same statement has a determinant form:
\[
\boxed{\inf_{B\in\mathcal B}\det(T_sB)
=1-M(s)=1-e^{-2s\delta}.}
\tag{QI6a}
\]
The dynamic interior margin and the generator gap are therefore two
calculations on the same specified carrier, not independently matched
positive numbers.

Indeed \(T_sI=I\), and \(\tau(T_sB)=1\), so the quantity being maximized is
\(\|T_s(B-I)\|_\tau^2\). Equation (QI4) turns its supremum into the real centered operator norm. The semigroup preserves Hermitian matrices, so its real centered norm equals its complexified norm. Self-adjoint spectral calculus gives the last equality.

Consequently, a proved finite-lag estimate has the exact implication

\[
\boxed{
M(s_0)\leq q<1,\quad 0<q<1
\quad\Longrightarrow\quad
\delta\geq-\frac{\log q}{2s_0}>0.}
\tag{QI7}
\]

This is a uniform estimate over the entire normalized positive base, not one selected density or tangent. Static cone preservation gives only \(M(s)\leq1\). Strict uniform interiorization supplies the additional dynamic datum. Here \(\delta>0\) is equivalent to the scalar fixed space: a nonzero centered fixed Hermitian matrix would yield another stationary density by a small positive perturbation of \(I/2\).

## The same generator supplies a Hilbert clock

The complex Hilbert carrier is \(M_2(\mathbb C)\) with the trace inner product, and its normalized distinguished vector is \(\Omega=I\). If (QI7) holds, \(L\) has this unique zero-energy vector and centered spectral gap \(\delta\). Its continuation
\[
U_t=e^{-itL}
\tag{QI8}
\]
is a reversible unitary group with the same generator. [[wick-real-forms-and-positive-preparation|Positive preparation]] gives the corresponding kernel quotient on the centered carrier; the zero-energy line is retained separately.

This does not make \(U_t\) an automorphism of the original matrix observable algebra. Unless \(L=0\), it cannot preserve the Hermitian subspace for every \(t\): on Hermitian \(X\), its derivative \(-iLX\) is anti-Hermitian. It is a Hilbert-state evolution, not the original UCP process run for real negative or imaginary duration as an ordered-algebra map. [[faithful-descent-rigidity-and-noiseless-unitarity|Faithful descent rigidity]] separately limits exact automorphic clocks obtained from a symmetric whole process.

The generator normalization and parameter units remain supplied. Equation (QI7) fixes the dimensionless product \(s_0\delta\); identifying a physical duration, energy, observable action or relativistic mass needs additional realization data.

In particular, (QI6a) is not an angular exclusion from a physical
four-momentum light cone. The exact determinant-preserving congruence
\[
P_r=m\,\operatorname{diag}(e^r,e^{-r}),\qquad m>0,
\]
has \(\det P_r=m^2\) but
\(\det P_r/\tau(P_r)^2=\operatorname{sech}^2r\to0\).
A fixed nonzero invariant determinant permits normalized directions
arbitrarily close to the null boundary in a fixed trace frame.
[[contemporary-puzzles/yang-mills-mass-gap/joint-causal-generators-and-the-mass-casimir|The joint-Casimir construction]]
therefore asks for a bound on the joint translation invariant, not a
uniform angular margin for boosted momenta. Here \(T_s\) acts on matrix
observables in a specified transfer model.

## A sharp family with two fixed rates

For \(0<\varepsilon\leq1\), define

\[
\begin{aligned}
L_\varepsilon(X)
&=\sum_{j=1}^3 c_j
\big(X-\sigma_jX\sigma_j\big),\\
c_1=c_2&=\frac{\varepsilon}{4},\qquad
c_3=\frac{2-\varepsilon}{4}.
\end{aligned}
\tag{QI9}
\]

All jump weights are nonnegative. To verify complete positivity directly, let \(S_j(X)=\sigma_jX\sigma_j\). These are commuting UCP involutions as superoperators, and
\[
e^{-sc_j(I-S_j)}
=\frac{1+e^{-2sc_j}}2\,\operatorname{id}
+\frac{1-e^{-2sc_j}}2\,S_j
\tag{QI10}
\]
is a convex combination of automorphisms. Their product is \(T_s^\varepsilon=e^{-sL_\varepsilon}\). Each factor preserves trace and is self-adjoint in the trace Hilbert metric; their commutation gives the same properties for the product.

Pauli conjugation immediately gives

\[
\boxed{
L_\varepsilon I=0,\quad
L_\varepsilon\sigma_1=\sigma_1,\quad
L_\varepsilon\sigma_2=\sigma_2,\quad
L_\varepsilon\sigma_3=\varepsilon\sigma_3.}
\tag{QI11}
\]

Thus \(I/2\) is the unique invariant density, the unique Hilbert vacuum is \(I\), and
\[
\delta_\varepsilon=\varepsilon,\qquad
M_\varepsilon(s)=e^{-2s\varepsilon}.
\tag{QI12}
\]
The supremum is attained by \(B=I+\sigma_3\), whose Bloch direction contracts at the slow rate. The cone, order unit, trace state and state-induced metric are identical throughout the family; the latter is contracted by the process, not preserved isometrically. Two decay rates remain exactly one, so \(\varepsilon\downarrow0\) is not an overall change of time unit. At fixed \(s_0>0\), the uniform interiorization margin vanishes.

The full Dirichlet form \(\langle X,L_\varepsilon X\rangle_\tau\) does change. The example therefore does not claim that a completely specified generator has an undetermined gap. It identifies precisely what the static cone and state metric leave unspecified, and what (QI7) would constrain.

[[peirce-context-averaging-and-the-emergent-qubit-process|Peirce context averaging]] now supplies a more constrained candidate: fixing the rank-two octonionic carrier and averaging its complex contexts with invariant weight forces the local return to contract each Bloch direction by \(1/3\). Its unit-rate Poisson generator has gap \(2/3\). The context family, averaging law and process convention are specified geometrically, not recovered from a desired eigenvalue; their physical selection and dimensional calibration remain open.

## Positive increments are not normalized state evolution

A separate order-theoretic guard is needed before interpreting this process as accumulating facts. If a unital positive map satisfies \(\Phi(X)\geq X\) for every \(X\geq0\), then for \(0\leq X\leq I\) its application to \(I-X\) also gives \(\Phi(X)\leq X\). Hence \(\Phi=\operatorname{id}\). Likewise, two density matrices of equal trace cannot have a nonzero positive-semidefinite difference.

An additive positive-increment ledger must therefore be a different accumulated quantity, with a specified source or transport, not merely a normalized density trajectory. UCP cone preservation and increasing order are different predicates.

The positive result remains substantive: one dynamic contraction estimate on a fixed ordered carrier produces an exact same-generator Hilbert gap. The sharp family shows why a master-object construction must control that estimate, not only the existence and signature of its cone. Nothing here constructs a four-dimensional observable net, a continuum Yang–Mills Hamiltonian or its physical mass gap.

[[directed-analytic-realization/positive_cone_process_receipt.py|The shared cone receipt]]
checks the Pauli jump weights, fixed rates and saturating positive-base
directions. [[directed-analytic-realization/positive-cone-process-receipt-output.txt|Its stored output]]
separates exact finite algebra from exponential sampling.
