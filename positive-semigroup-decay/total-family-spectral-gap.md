# Total-Family Spectral Gap

A single positive decay exponent on a Hilbert-total family of diagonal semigroup correlations gives a spectral gap for the whole ground-state complement. The proof allows vector-dependent prefactors and onsets and requires no differentiability of the test vectors. Positivity of the scalar spectral measure, rather than uniform control of the test-vector norms, is the decisive input.

## The generator and the total family

Let \(A\ge0\) be a self-adjoint operator on a complex Hilbert space \(\mathcal H\), and put \(P_0=\mathbf1_{\{0\}}(A)\), \(Q=I-P_0\). Its semigroup \(e^{-sA}\), \(s\ge0\), consists of bounded positive self-adjoint contractions. Positivity here is Hilbert-operator positivity; no order-preserving Markov realization is assumed.

Suppose \(\mathcal D_{\mathrm{loc}}\subset Q\mathcal H\) has Hilbert-norm dense complex linear span in \(Q\mathcal H\). The subscript is retained for applications, but the abstract family need not have a spatial meaning. Let \(\sigma_*>0\) be common to the family and assume, for each \(\psi\in\mathcal D_{\mathrm{loc}}\),

$$
0\leq
\langle\psi,e^{-sA}\psi\rangle
\leq
C_\psi e^{-\sigma_*s}
\qquad(s\geq s_\psi),
\tag{ARL17}
$$

with finite \(C_\psi\ge0\) and finite \(s_\psi\ge0\). The family need not itself be linear, and its vectors need not belong to \(D(A)\) or \(D(A^{1/2})\).

Then
\[
\mathbf1_{(0,\sigma_*)}(A)=0,\qquad
A\ge\sigma_*Q
\]
in quadratic-form sense. Equivalently,
\[
\|e^{-sA}Q\|\le e^{-\sigma_*s}\qquad(s\ge0).
\]
The reverse implication holds with \(C_\psi=\|\psi\|^2\) and \(s_\psi=0\) for every vector in \(Q\mathcal H\). The theorem permits any ground-space multiplicity, including a trivial ground space. If \(Q\mathcal H=0\), the estimate is vacuous and does not establish a nontrivial excitation sector.

## Positive spectral weight cannot cancel

The spectral theorem supplies the finite positive measure

$$
\nu_\psi(B)
:=
\langle\psi,\mathbf1_B(A)\psi\rangle,
\qquad
B\in\mathcal B([0,\infty)).
\tag{ARL19}
$$

Its Laplace transform is \(\langle\psi,e^{-sA}\psi\rangle\). If it charges \((0,\sigma_*)\), countable continuity from below supplies some \(0<\delta<\sigma_*\) with positive weight in \((0,\delta]\). Consequently

$$
\langle\psi,e^{-sA}\psi\rangle
\geq
e^{-\delta s}\|\mathbf1_{(0,\delta]}(A)\psi\|^2,
\tag{ARL19a}
$$

contradicting (ARL17) as \(s\to\infty\). Thus the bounded projection \(\mathbf1_{(0,\sigma_*)}(A)\) annihilates every vector of the test family, hence its linear span and closure. It also annihilates the ground space. This proves the claim on all of \(\mathcal H\).

No limit of the vector-dependent constants was taken. A fixed-time estimate on the test family with uncontrolled constants would not give the same conclusion; the argument uses arbitrarily large separations for each fixed vector. Likewise an off-diagonal correlation can cancel and cannot replace these positive diagonal tests without a further argument.

## The quantifiers must survive the application

One positive diagonal channel excludes low spectral weight only from the subspace it observes. Totality is what promotes that channel statement to the complete complement. A different positive exponent for each member is also insufficient: in the [[distinction-grain-spectrum/inq#Every distinction may have a grain while the theory is gapless|existing diagonal counterexample]], the basis is total but its decay rates approach zero.

The theorem concerns one Hilbert space, one generator and one ground-space projection. Passing through changing regulators, observation maps or vacuum representations requires a separate convergence and coverage argument. The [[positive-semigroup-decay/physical-reconstruction-and-units|physical reconstruction contract]] spells out those requirements for Euclidean correlations.
