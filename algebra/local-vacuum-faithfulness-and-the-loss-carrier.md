# Local Vacuum Faithfulness and the Loss Carrier

A faithful vacuum restriction cannot be annihilated by a nonzero operator belonging, or suitably affiliated, to that same local algebra. This limits a direct passage from finite dark-jump models to a locally faithful observable theory. It does not forbid directed processes or positive clocks: an explicit bipartite construction places the loss in a relation between opposed factors, each separately faithful, rather than inside either factor. The theorem, its approximate finite guard and that constructive alternative identify which carrier a proposed loss row must actually use.

## Exact local annihilation forces the operator to vanish

Let \(M\subseteq B(\mathcal H)\) be a von Neumann algebra, and let \(\Omega\) be a unit vector separating for \(M\):
\[
x\Omega=0,\quad x\in M\quad\Longrightarrow\quad x=0.
\tag{VF1}
\]
Equivalently, the normal vector state
\[
\omega(x)=\langle\Omega,x\Omega\rangle
\]
is faithful on \(M\). Cyclicity is not required here.

For a bounded \(L\in M\),
\[
\boxed{L\Omega=0\quad\Longrightarrow\quad L=0.}
\tag{VF2}
\]
Indeed \(\omega(L^*L)=\|L\Omega\|^2=0\), and faithfulness kills the positive operator \(L^*L\).

There is no unbounded affiliated exception with the same vacuum-domain condition.

**Affiliated version.** Suppose \(L\) is closed and densely defined, affiliated with \(M\), and
\[
\Omega\in\operatorname{Dom}L,\qquad L\Omega=0.
\]
Then \(L\) is the zero operator, with domain all of \(\mathcal H\).

To prove this, set \(|L|=(L^*L)^{1/2}\). For a closed densely defined operator,
\[
\operatorname{Dom}|L|=\operatorname{Dom}L,\qquad
\||L|\Omega\|=\|L\Omega\|=0.
\]
Affiliation puts the bounded spectral projections of \(|L|\) in \(M\). For every \(\delta>0\),
\[
E_\delta=\mathbf1_{(\delta,\infty)}(|L|)\in M,\qquad
\|E_\delta\Omega\|^2
\le\delta^{-2}\||L|\Omega\|^2=0.
\tag{VF3}
\]
Separatingness gives \(E_\delta=0\). Letting \(\delta\downarrow0\) shows that the spectral measure of \(|L|\) is concentrated at zero. Thus \(|L|\) is the everywhere-defined zero operator, and the polar decomposition gives the same conclusion for \(L\).

An unsmeared distribution, or an expression for which \(\Omega\) is not in the operator domain, has not met these hypotheses. Calling it a local annihilator does not supply the missing domain or affiliation theorem.

## Why one-site faithfulness does not rescue the graph-star row

The [[directed-analytic-realization/pure-vacuum-loss-and-the-returned-clock|pure-vacuum loss construction]] begins with a row \(L_a\Omega=0\) and returns
\[
K=\tfrac12\sum_aL_a^*L_a.
\tag{VF4}
\]
If every nonzero row entry were affiliated with an algebra on which this same vacuum were faithful, (VF2)--(VF3) would kill the row. A nontrivial realization must therefore identify which premise does not apply to its proposed local entries.

The [[directed-analytic-realization/local-loss-rows-and-the-uniform-gap|graph-star example]] makes this boundary visible at finite size. On a nonempty finite simple graph with no isolated vertices, its jumps and stabilizers are
\[
\widetilde L_j
=\tfrac12\left(Z_j-iY_j\prod_{k\sim j}Z_k\right),
\qquad
S_j=X_j\prod_{k\sim j}Z_k.
\]
Each jump is supported on the star \(O_j=\{j\}\cup\{k:k\sim j\}\), and
\[
\boxed{
\widetilde L_j^*\widetilde L_j
=\frac{I-S_j}{2}=:P_j,\qquad
P_j\ne0,\qquad
P_j\Omega_G=0.
}
\tag{VF5}
\]
The identity follows by conjugating \(b_j^*b_j=(I-X_j)/2\) with the graph entangler. The stabilizer \(S_j\) is a nonidentity traceless Pauli product with square \(I\), so \(P_j\) is a nonzero projection.

Although every one-site reduced state is \(I/2\), (VF5) gives a nonzero positive element of the full star algebra with vacuum expectation zero. The vacuum restriction to that star algebra is therefore not faithful. Its one-site restrictions do not imply faithfulness on the larger support where the jump actually lives. The finite graph model is consistent; this particular local faithfulness property does not extend to its jump supports.

## Approximate annihilation requires a quantitative state bound

For a finite region with matrix algebra \(B(\mathcal H_O)\), let \(\rho_O\) be the vacuum's reduced density matrix. For \(L=L_O\otimes I\),
\[
\|L\Omega\|^2
=\operatorname{Tr}(\rho_O L_O^*L_O).
\]
If
\[
\rho_O\ge\varepsilon I,\qquad\varepsilon>0,
\]
then
\[
\boxed{
\|L\Omega\|^2\ge\varepsilon\|L_O\|_{\mathrm{HS}}^2
\ge\varepsilon\|L_O\|^2.
}
\tag{VF6}
\]
Thus \(\|L\Omega\|\le\eta\) implies
\(\|L_O\|_{\mathrm{HS}}\le\eta/\sqrt\varepsilon\). Faithfulness gives some \(\varepsilon>0\) for each fixed finite density matrix, but does not give one uniform over a family of states, regions or refinements.

For an exact counterexample, take
\[
\Omega_\varepsilon
=\sqrt{1-\varepsilon}|00\rangle+\sqrt\varepsilon|11\rangle,
\qquad
0<\varepsilon<\tfrac12,
\]
\[
\rho_O=\operatorname{diag}(1-\varepsilon,\varepsilon),\qquad
L_O=|1\rangle\langle1|.
\]
Every \(\rho_O\) is faithful, while
\[
\|L_O\|=\|L_O\|_{\mathrm{HS}}=1,\qquad
\|(L_O\otimes I)\Omega_\varepsilon\|^2=\varepsilon\longrightarrow0.
\tag{VF7}
\]
Approximate annihilation has not made the operator small uniformly.

Even a fixed faithful state in infinite dimension need not control operator norm this way. On \(M=L^\infty([0,1])\) acting on \(L^2([0,1])\), the vector \(\Omega=1\) is separating. The multiplication projections \(L_n=\mathbf1_{[0,1/n]}\) have operator norm one and \(\|L_n\Omega\|^2=1/n\). Exact faithfulness is qualitative; small vacuum response on rare projections is not uniformly small action. A trace-density bound such as (VF6) must not be silently imported into a type-III local algebra.

## A loss can operate between two faithful factors

There is a constructive finite alternative to placing the jump inside either local factor. Let
\[
\mathcal H=\mathbb C^d\otimes\mathbb C^d,\qquad d\ge2,
\]
\[
\rho=\operatorname{diag}(p_1,\ldots,p_d)>0,\qquad
\operatorname{Tr}\rho=1,\qquad
\Omega_\rho=\sum_i\sqrt{p_i}|i\rangle\otimes|i\rangle.
\tag{VF8}
\]
The restrictions to \(M_{\mathrm L}=M_d\otimes I\) and \(M_{\mathrm R}=I\otimes M_d\) are both faithful; \(\Omega_\rho\) is cyclic and separating for each factor on this bipartite carrier.

For any \(A\in M_d\), define its state-dependent mirror
\[
B_A=\rho^{1/2}A^T\rho^{-1/2}.
\tag{VF9}
\]
The transpose uses the declared Schmidt basis. Direct coefficient comparison proves
\[
(A\otimes I)\Omega_\rho=(I\otimes B_A)\Omega_\rho.
\]
Consequently,
\[
\boxed{
D_A=A\otimes I-I\otimes B_A,\qquad
D_A\Omega_\rho=0.
}
\tag{VF10}
\]
For nonscalar \(A\), \(D_A\ne0\) and belongs to neither \(M_{\mathrm L}\) nor \(M_{\mathrm R}\): otherwise the intersection \(M_{\mathrm L}\cap M_{\mathrm R}=\mathbb C I\) would force \(B_A\), hence \(A\), to be scalar. The defect lives in the joined algebra
\(M_{\mathrm L}\vee M_{\mathrm R}=B(\mathcal H)\), where the vector state is not faithful.

The mirror reverses products:
\[
B_{AB}=B_BB_A.
\tag{VF11}
\]
It is generally not a \(*\)-homomorphism or a \(*\)-antihomomorphism. For example, when \(p_1\ne p_2\), the adjoint of
\(B_{E_{12}}=\sqrt{p_2/p_1}\,E_{21}\) differs from
\(B_{E_{21}}=\sqrt{p_1/p_2}\,E_{12}\).
The mirror encodes equality on the specified vector, not a state-independent positive identification of the two observable factors.

The full matrix row selects just that vacuum line. Identify a vector with its coefficient matrix \(T\), so that left and right actions give \(AT\) and \(TB_A^T\). Since \(\rho\) is invertible, write \(T=C\rho^{1/2}\). Then
\[
D_A T=[A,C]\rho^{1/2}.
\tag{VF12}
\]
If \(D_A T=0\) for every matrix unit \(A=E_{ij}\), then \(C\) commutes with every matrix and is scalar. Therefore
\[
\boxed{\bigcap_{i,j}\ker D_{E_{ij}}=\mathbb C\Omega_\rho.}
\tag{VF13}
\]
This is a relation-defect row with a uniquely selected null line, despite faithfulness on each opposed factor separately. It does not violate (VF2), because its nonzero entries are not in those factors.

## A complete uniform-state response, with the algebra change explicit

For \(\rho=I/d\), let
\[
\Omega_d=d^{-1/2}\sum_i|ii\rangle,\qquad
D_{ij}=E_{ij}\otimes I-I\otimes E_{ji}.
\]
The matrix units are orthonormal in the unnormalized Hilbert–Schmidt inner product. Expanding the whole row gives
\[
\begin{aligned}
\sum_{i,j}D_{ij}^*D_{ij}
&=2dI-2\sum_{i,j}E_{ij}\otimes E_{ij}\\
&=2d(I-P_{\Omega_d}).
\end{aligned}
\]
Thus
\[
\boxed{
K=\tfrac12\sum_{i,j}D_{ij}^*D_{ij}
=d(I-P_{\Omega_d}),\qquad
\operatorname{gap}K=d.
}
\tag{VF14}
\]
The [[directed-analytic-realization/pure-vacuum-loss-and-the-returned-clock|pure-vacuum theorem]] applies to this explicit row, returning both its UCP law on \(B(\mathcal H)\) and its algebra-preserving analytic clock on that same full algebra.

This uniform row is not a vacuum-attracting amplitude-damping law. Since \(D_{ij}^*=D_{ji}\) and both annihilate \(\Omega_d\), the vacuum projection reduces every jump. Both that projection and its complement are fixed by the Heisenberg process. The unique common null line of the row is not a claim of a unique stationary state of the whole UCP law.

This is also a precise comparison with the [[matrix-symbol-realization-and-the-clock-algebra|tracial symbol clock]]: up to its declared normalization, (VF14) is the same positive Hilbert operator \(I-P_\Omega\). What changed is the observable algebra. The old fixed left factor is faithful at \(\Omega_d\); the joined full operator algebra is not. By [[faithful-stationary-states-and-the-positive-clock|faithful stationary clock rigidity]], the nontrivial positive clock cannot normalize either fixed faithful factor, even though it normalizes their joined algebra. Enlarging the observable algebra is a genuine construction choice, not a repair of the old claim on its old algebra.

The factors in (VF8) are opposed algebraic partners; they have not been assigned a spatial separation. Each \(D_A\) couples both partners. This finite construction is therefore not a theorem of relativistic locality. The row normalization determines the number \(d\) in (VF14); rescaling its channel metric rescales the gap. For nonuniform \(\rho\), the mirror also depends on \(\rho^{-1/2}\), so its norms need not remain controlled as the smallest Schmidt weight tends to zero.

[[modular-mirror-response-and-the-analytic-domain|The modular continuation]]
replaces the finite Schmidt formula by a uniquely determined bounded
mirror for each entire modular-analytic observable in a cyclic-separating
representation. It also exhibits an explicit failure of bounded mirrors
outside that domain. [[expected-inclusions-and-mirror-clock-consistency|The inclusion test]]
then separates exact pullback of this response form from reduction of
its clock: correlated states can satisfy the former and fail the latter.

## The next carrier condition for a local theory

For a proposed observable net \(M(\mathcal O)\), assume its vacuum restriction is faithful on the regions under consideration. This is a hypothesis on that net and state, not a result derived here. Then a nonzero exact dark jump cannot be an ordinary bounded local operator in \(M(\mathcal O)\), or a closed affiliated operator with the vacuum in its domain.

Possible response carriers include maps between correspondences or source and target Hilbert spaces, defects comparing opposed factors as above, and annihilation operators with nonlocal positive-frequency structure. Each proposal must state its source and target and prove the appropriate locality or covariance relation; the word “loss” does not give one.

The [[directed-analytic-realization/local-weyl-realization|boundary Weyl realization]] illustrates the needed distinction without presuming a full field theorem. It constructs local algebras using real supported symbols, while its map to one-particle amplitudes selects one Fourier sign. A Fock annihilator \(a(z)\) kills the vacuum, whereas the real field combination \(a(z)+a(z)^*\) creates the one-particle vector \(z\) from it and does not annihilate the vacuum when \(z\ne0\). A support label on a real smearing does not establish that its separate annihilation part is affiliated with that same local algebra. The boundary note proves its stated Weyl locality, not the local separating property; no additional theorem is inferred here.

A candidate row \(\mathbf L:\mathcal H\to\mathcal K\) outside the local observable algebra can still define the response \(K=\tfrac12\mathbf L^*\mathbf L\), provided it is a closed densely defined operator with the claimed vacuum domain. But an infinite or unbounded row additionally needs a conservative completely positive process realization, a valid quotient intertwiner, and compatibility of its clock with the proposed net. The finite formulas do not supply those analytic statements.

The resulting task is constructive and narrower than “local dissipation is impossible”: find a nontrivial response on the correct relational carrier, prove how it returns ordinary local observables, and control its nonvacuum lower bound in the required limits. Exact local faithfulness constrains that carrier; it does not exclude every local UCP dynamics, every nonlocal response, or every deeper algebraic realization.

[[directed-analytic-realization/vacuum_loss_receipt.py|The vacuum-loss receipt]] checks the finite Schmidt mirror, its failure to preserve adjoints, the two-level opposed row and the graph-star faithfulness witness. [[directed-analytic-realization/vacuum-loss-receipt-output.txt|Its output]] records those exact finite checks; the spectral-projection proof above supplies the affiliated-operator statement.
