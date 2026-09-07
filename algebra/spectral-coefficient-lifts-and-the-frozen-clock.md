# Spectral Coefficient Lifts and the Frozen Clock

Keeping a spectral label fixed while acting only on its vector coefficient gives a bounded observable \(*\)-representation exactly when every spectral effect commutes with the supplied observable algebra. Such lifts preserve energy sectors and cannot create positive-energy excitations from the vacuum. This is a sharp restriction on the coefficient-only prescription, not a prohibition of observable realization: a two-level example has a valid energy-changing observable precisely where that prescription fails.

## The proposed action has a declared carrier

Let \(\mathsf M\) be a normalized positive operator-valued measure on \(\Lambda=[0,\infty)\), acting on \(\mathcal R\). Use the minimal dilation from [[global-local-response-reconstruction/compatible-spectral-readouts-and-positive-clock|compatible spectral assembly]]:
\[
\langle[B,\xi],[C,\eta]\rangle
=\langle\xi,\mathsf M(B\cap C)\eta\rangle,\qquad
E(B)[C,\eta]=[B\cap C,\eta],\qquad
J\xi=[\Lambda,\xi].
\tag{FC1}
\]
The symbols are quotiented by the null space and completed to \(\mathcal K\). Thus \(J\) is an isometry and \(\mathsf M(B)=J^*E(B)J\). Set \(H=\int\lambda\,dE(\lambda)\).

Given a concrete unital \(C^*\)-algebra \(\mathcal A\subseteq B(\mathcal R)\), consider only the coefficient rule
\[
\pi_0(a)[B,\xi]=[B,a\xi].
\tag{FC2}
\]
It is initially a rule on formal finite sums. Preservation of the null space, boundedness and compatibility with the supplied adjoint must be proved.

## Exact boundedness criterion for one coefficient operator

For \(a\in B(\mathcal R)\) and a finite \(C\ge0\), the rule (FC2) descends to a bounded operator of norm at most \(C\) if and only if
\[
\boxed{
a^*\mathsf M(B)a\le C^2\mathsf M(B)
\quad\text{for every Borel }B.
}
\tag{FC3}
\]
Necessity follows by applying the operator norm bound to a single symbol:
\[
\|[B,a\xi]\|^2
=\langle\xi,a^*\mathsf M(B)a\xi\rangle
\le C^2\langle\xi,\mathsf M(B)\xi\rangle.
\]
For sufficiency, refine the finitely many sets in a symbol sum into disjoint Boolean atoms \(F\). If \(\xi_F\) is the coefficient on atom \(F\), then
\[
\|\pi_0(a)f\|^2
=\sum_F\langle a\xi_F,\mathsf M(F)a\xi_F\rangle
\le C^2\sum_F\langle\xi_F,\mathsf M(F)\xi_F\rangle
=C^2\|f\|^2.
\]
Null vectors are therefore preserved, and the bounded operator extends uniquely to the completion. The smallest admissible \(C\) is its norm.

## The observable adjoint forces effect commutation

**Theorem.** The rules (FC2), for all \(a\in\mathcal A\), give a bounded unital \(*\)-representation on \(\mathcal K\) if and only if
\[
\boxed{[a,\mathsf M(B)]=0
\quad\text{for every }a\in\mathcal A,\ B\subseteq\Lambda\text{ Borel}.}
\tag{FC4}
\]
In that case the representation is faithful and isometric.

For necessity, the required equality
\(\pi(a)^*=\pi(a^*)\), paired on \([B,\xi]\) and \([\Lambda,\eta]\), gives
\[
\langle\xi,a^*\mathsf M(B)\eta\rangle
=\langle\xi,\mathsf M(B)a^*\eta\rangle.
\tag{FC5}
\]
Since \(\mathcal A\) is \(*\)-closed, this is (FC4).

Conversely, effect commutation gives
\[
a^*\mathsf M(B)a
=\mathsf M(B)^{1/2}a^*a\mathsf M(B)^{1/2}
\le\|a\|^2\mathsf M(B).
\]
Criterion (FC3) supplies bounded lifts. The same pairings prove the adjoint relation, while the formal rules give \(\pi(a)\pi(b)=\pi(ab)\) and \(\pi(I)=I\). Finally
\[
\boxed{\pi(a)J=Ja,\qquad\|\pi(a)\|=\|a\|,}
\tag{FC6}
\]
because contractivity gives one norm inequality and the isometry \(J\) gives the other.

Boundedness alone is weaker. On a two-point spectral space, take
\[
\mathsf M(\{0\})=\operatorname{diag}(1/4,3/4),\qquad
\mathsf M(\{1\})=\operatorname{diag}(3/4,1/4).
\]
The coefficient rules for \(M_2\) are bounded and multiplicative on this finite weighted symbol space; (FC3) holds with \(C=\sqrt3\|a\|\). But for \(a=X\), the Pauli flip, \(f=[\{0\},e_0]\) and \(g=[\{0\},e_1]\),
\[
\langle\pi_0(X)f,g\rangle=3/4,\qquad
\langle f,\pi_0(X)g\rangle=1/4.
\]
The self-adjoint input \(X\) has not lifted to a self-adjoint operator.

## These lifts preserve energy, not just the embedding

Whenever a coefficient lift is bounded, it commutes with every spectral projection:
\[
\pi(a)E(B)[C,\xi]
=[B\cap C,a\xi]
=E(B)\pi(a)[C,\xi].
\tag{FC7}
\]
For the \(*\)-representation above this implies commutation with every bounded spectral function and with \(e^{-itH}\). It also gives preservation of \(\operatorname{Dom}H\) and \(H\pi(a)\xi=\pi(a)H\xi\) there. In particular, disjoint spectral sets have no transition block:
\[
\boxed{E(C)\pi(a)E(B)=0\qquad(B\cap C=\varnothing).}
\tag{FC8}
\]
Conversely, a representation satisfying \(\pi(a)J=Ja\) and commuting with every \(E(B)\) must obey (FC2), since the symbols \(E(B)J\xi\) span a dense space. These are exactly the embedding-intertwining, energy-diagonal lifts.

Let \(\Omega_0\) be a zero-energy vector. Then
\[
\pi(a)\Omega_0\in\ker H,\qquad
\overline{\pi(\mathcal A)\Omega_0}\subseteq\ker H.
\tag{FC9}
\]
If \(\Omega_0\) is cyclic for this observable representation, \(H=0\) on all of \(\mathcal K\). Without cyclicity, nonzero-energy sectors may remain, but these observables cannot reach them from the vacuum. No assumption of a unique vacuum or of a faithful state is needed.

This differs from [[faithful-stationary-states-and-the-positive-clock|faithful stationary clock rigidity]]. There the adjoint geometry forces spectral symmetry for a stationary algebra-normalizing implementation. Here the chosen coefficient action itself forces every observable to commute with the clock. Neither theorem rules out general energy-changing observables.

## A failed coefficient lift can coexist with a valid observable

Take \(\mathcal R=\mathbb C^2\),
\[
\mathsf M(\{0\})=P_0,\qquad
\mathsf M(\{1\})=P_1,\qquad
H=P_1,
\]
where \(P_j=|e_j\rangle\langle e_j|\). The minimal dilation is already \(\mathcal K=\mathbb C^2\), \(J=I\), and \([B,\xi]=E(B)\xi\).

For \(X=|e_0\rangle\langle e_1|+|e_1\rangle\langle e_0|\),
\[
\boxed{
[\{0\},e_1]=0,\qquad
[\{0\},Xe_1]=[\{0\},e_0]\ne0.
}
\tag{FC10}
\]
The coefficient rule does not even preserve the null space. Yet the ordinary \(X\) acting on this same \(\mathbb C^2\) is a bounded self-adjoint observable, part of the defining representation of \(M_2\), and
\[
X e_0=e_1,\qquad He_0=0,\qquad He_1=e_1.
\]
It creates an excitation because it does not preserve the energy label. There is no failure of observable existence.

The missing construction is therefore an action that can relate spectral sectors while respecting the intended product, adjoint, norm and locality. [[pointed-cp-fusion-residue/inq|Pointed CP realization]] is a distinct existing example: its kernel already contains noncommutative algebra labels and supports their left action.

[[directed-analytic-realization/preparation-overlaps-and-the-transition-algebra|Preparation overlaps and transitions]] construct an off-diagonal whole compact-operator algebra and its clock from the spectral kernel. That whole algebra is not automatically a unital realization of the previously supplied local \(\mathcal A\), nor a selection of its localization. Coefficient commutation is one classified special case, not a necessary condition on all possible observable realizations.

[[directed-analytic-realization/spectral_transition_receipt.py|The spectral-transition receipt]] checks the null-space obstruction, a valid diagonal coefficient action and the contrasting whole transition operators. [[directed-analytic-realization/spectral-transition-receipt-output.txt|Its output]] records finite exact checks; the all-Borel-set criterion and cyclic-vacuum conclusion are proved above.
