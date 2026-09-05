# Hardy Compression and Boundary Response

For a real function on an oriented circle, the trace of the positive multiplication defect created by Hardy compression is exactly its harmonic Dirichlet response, up to the declared boundary-length normalization. This relates an algebraic loss of multiplicativity to a geometric quadratic form without fitting an operator. The equality concerns a form on the space of readout symbols, not the identification of one compressed defect operator with a Hamiltonian.

## What compression forgets

Let \(P\) be an orthogonal projection on a complex Hilbert space \(\mathcal L\), and let a unital \(C^*\)-algebra act on \(\mathcal L\). On \(\mathcal H=P\mathcal L\), define

\[
T_a=PaP|_{\mathcal H},\qquad
H_a=(1-P)aP:\mathcal H\longrightarrow(1-P)\mathcal L.
\tag{HC1}
\]

Compression retains an operator's action only after returning to \(\mathcal H\). Inserting \(1=P+(1-P)\) gives

\[
T_{ab}-T_aT_b=Pa(1-P)bP,
\qquad
T_{a^*a}-T_a^*T_a=H_a^*H_a\geq0.
\tag{HC2}
\]

The missing intermediate channel is explicit: leave the retained space, act in its complement, and return. This is a compositional residue, not an assertion about entropy, emitted radiation or actualized outcomes. The map \(a\mapsto T_a\) is unital and completely positive: compressing a positive operator matrix remains positive at every matrix size. It need not preserve products.

For commuting self-adjoint \(a,b\),

\[
[T_a,T_b]=H_b^*H_a-H_a^*H_b.
\tag{HC3}
\]

The even positive defect and the odd failure of commutation therefore come from the same discarded intermediate channel. This is distinct from the exact corner-algebra isomorphism in [[algebra/retract-corners-and-local-unitarity|retract corners]]: operators already supported in the corner multiply exactly; arbitrary operators compressed into it need not.

## The circle fixes the residue exactly

Take \(\mathcal L=L^2(S^1,d\theta/(2\pi))\). Write

\[
f(\theta)=\sum_{k\in\mathbb Z}f_k e^{ik\theta},
\qquad
\mathcal H_-=\overline{\operatorname{span}}\{e^{-in\theta}:n\geq0\},
\tag{HC4}
\]

and let \(P=P_-\) project onto \(\mathcal H_-\). In (HC1), use multiplication \(a=M_f\). Begin with trigonometric polynomials so all products and traces below have elementary domains.

For the retained basis \(e_n=e^{-in\theta}\),

\[
H_fe_n=\sum_{k>n}f_k e^{i(k-n)\theta}.
\]

Thus every positive Fourier coefficient \(f_k\) contributes to exactly \(k\) discarded channels, indexed by \(n=0,\ldots,k-1\). Consequently

\[
\boxed{\operatorname{Tr}(H_f^*H_f)
=\sum_{k>0}k|f_k|^2.}
\tag{HC5}
\]

For real \(f\), \(f_{-k}=\overline{f_k}\), \(T_f=T_f^*\), and

\[
\Delta_f:=T_{f^2}-T_f^2=H_f^*H_f.
\tag{HC6}
\]

The natural-number factor \(k\) counts lost intermediate channels. It is not a fitted degeneracy or a physical energy unit.

## The same form is a harmonic boundary response

Give the circle radius \(R>0\), with \(x=R\theta\). Let \(u_f\) be the harmonic extension to the Euclidean disk \(B_R\):

\[
u_f(r,\theta)=\sum_k f_k(r/R)^{|k|}e^{ik\theta}.
\tag{HC7}
\]

Define the normalized boundary response

\[
\mathcal E_R(f)
:=\frac{1}{2\pi R}\int_{B_R}|\nabla u_f|^2\,dA.
\tag{HC8}
\]

The normalization is boundary length, not disk area. Green's identity and the outward derivative
\(\partial_r u_f|_{r=R}=\sum_k(|k|/R)f_ke^{ik\theta}\)
give

\[
\mathcal E_R(f)
=\sum_k\frac{|k|}{R}|f_k|^2.
\tag{HC9}
\]

Combining conjugate Fourier modes in (HC5) proves, for real \(f\),

\[
\boxed{\mathcal E_R(f)=\frac{2}{R}\operatorname{Tr}\Delta_f.}
\tag{HC10}
\]

This is an exact response comparison, not a hypothesis that a positive defect ought to bound an independently supplied operator. The [[directed-analytic-realization/harmonic-boundary-realization|oriented harmonic member]] derives a clock whose quadratic form is this very boundary response.

For \(v\in H^1(B_R)\) with the same Sobolev boundary trace, write \(v=u_f+w\) with \(w\in H^1_0(B_R)\). Harmonicity gives

\[
\int_{B_R}|\nabla v|^2
=\int_{B_R}|\nabla u_f|^2+\int_{B_R}|\nabla w|^2.
\tag{HC11}
\]

This is the harmonic least-response representative of [[trace-dirichlet-descent/inq|trace Dirichlet descent]]. Here it follows from the stated harmonic extension law; it does not establish stationary action as an upstream axiom of nature.

## Closure and the type of the equality

For bounded real \(f\), (HC6) is an identity of bounded operators. It is trace class precisely when
\(\sum_{k>0}k|f_k|^2<\infty\), equivalently \(f\in H^{1/2}(S^1)\).
Indeed the displayed matrix for \(H_f\) has exactly this squared Hilbert–Schmidt norm.

For unbounded real \(H^{1/2}\) symbols, use the closure of the nonnegative quadratic form

\[
\mathfrak q_R(f):=\frac{2}{R}\|H_f\|_{\mathrm{HS}}^2
\tag{HC12}
\]

from trigonometric polynomials on real \(L^2\). Its form domain is \(H^{1/2}\), its kernel is the constants, and its associated operator is the Fourier multiplier \(|k|/R\), with domain \(H^1\). The Hilbert–Schmidt matrix still defines \(H_f\); an unqualified subtraction of unbounded Toeplitz products is not needed.

Two type restrictions matter.

First, \(\mathfrak q_R\) is a form on the **symbol** \(f\). For one fixed polynomial \(f\), \(\Delta_f\) has finite rank on the Hardy **state** space. It cannot equal a positive multiple of an unbounded clock generator there, nor control every state orthogonal to the vacuum.

Second, reality of the symbol is essential. For \(f=e^{-i\theta}\), multiplication preserves \(\mathcal H_-\), so \(H_f=0\), although its harmonic Dirichlet response is \(1/R\). For a complex symbol the replacement is

\[
\mathcal E_R(f)=\frac1R
\left(\|H_f\|_{\mathrm{HS}}^2+
\|H_{\bar f}\|_{\mathrm{HS}}^2\right).
\tag{HC13}
\]

Real self-adjoint readouts tie the two orientations together. No equality of the concepts “observable” and “state” is being assumed.

## The odd trace is a local central form

For smooth real \(f,g\), the same Hankel matrices give

\[
\operatorname{Tr}(H_g^*H_f)
=\sum_{n>0}n f_n\overline{g_n},
\qquad
\boxed{\operatorname{Tr}[T_f,T_g]
=\frac{i}{2\pi}\int_0^{2\pi}f g'\,d\theta.}
\tag{HC13a}
\]

The first identity follows by the same channel count as (HC5); its imaginary part and (HC3) give the second. Thus the even trace measures the positive response while the odd trace gives a local antisymmetric bilinear form.

There is no violation of trace cyclicity: the commutator is trace class, but the two products being subtracted need not individually be trace class. A finite matrix cut introduces a second boundary whose contribution cancels this trace. It is not a faithful way to compute the single Hardy-boundary central term.

For disjoint supports, the traced commutator in (HC13a) vanishes, even though the operator commutator below need not. [[directed-analytic-realization/local-weyl-realization|The local Weyl realization]] uses this **central scalar form**, rather than compressed multiplication, to construct commuting local algebras. That is a specified new realization, not the claim that taking a trace preserves all operator information.

## Local support does not survive as commuting compressed algebras

For real \(a,b\), multiplication commutes before compression. It can fail after compression even when \(ab=0\).

Let \(\Omega=1\), and choose nonnegative nonzero smooth functions supported in separated arcs \(A,B\), with

\[
0<\phi-\theta<\pi
\quad(\theta\in A,\ \phi\in B).
\]

Off the diagonal, the Abel limit of the Hardy kernel is
\((1-e^{-i(\theta-\phi)})^{-1}\). Using (HC3), or subtracting this kernel from its reversal, gives

\[
\langle\Omega,[T_a,T_b]\Omega\rangle
=-i\int_A\int_B a(\theta)b(\phi)
\cot\frac{\theta-\phi}{2}\,
\frac{d\phi\,d\theta}{(2\pi)^2}\neq0.
\tag{HC14}
\]

The cotangent has one strict sign throughout these supports. Thus compressed boundary effects are not already a local commuting observable net. A different realization of local observables must be constructed; their existence cannot be inferred from the support of the original multiplication symbols.

For a finite-mode calibration, \(a=\cos\theta\) and \(b=\sin\theta\) give

\[
\Delta_a=\Delta_b=\frac14|\Omega\rangle\langle\Omega|,
\qquad
[T_a,T_b]=\frac i2|\Omega\rangle\langle\Omega|.
\tag{HC15}
\]

## What survives a change of scale

On mean-zero real symbols,

\[
\operatorname{Tr}\Delta_f\geq\frac12\|f\|_{L^2}^2,
\qquad
\mathcal E_R(f)\geq\frac1R\|f\|_{L^2}^2.
\tag{HC16}
\]

The first bound is dimensionless. The second uses the declared metric normalization.
Under a period cover \(R'=kR\), an old mode with label \(n\) becomes label \(kn\). Its norm and rate \(n/R=kn/R'\) are unchanged, while its unnormalized compression trace is multiplied by \(k\). New modes of rate \(1/R'\) are also admitted.

Therefore the trace count alone is not an invariant clock rate under these covers. The ratio in (HC10) transports the old response correctly, but the gap still closes along the [[directed-analytic-realization/inq|factorial-period refinement]]. This exact comparison removes a freely fitted response-to-clock map; it does not select an absolute period or solve the four-dimensional mass-gap problem.

Dimension changes the comparison itself. [[algebra/three-dimensional-weighted-compression-response|The three-dimensional Clifford calculation]] has divergent ordinary trace; its finite order-one response uses the geometry's Neumann-to-Dirichlet map on the input source carrier. Its scalar odd trace then vanishes, so the [[algebra/cauchy-response-and-local-action|opposed Green pairing]] supplies a different route to local commutation. Neither the circle's trace nor its phase pairing is a dimension-independent formula.
