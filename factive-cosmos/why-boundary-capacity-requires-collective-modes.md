# Why Boundary Capacity Requires Collective Modes

An arena with area-order information capacity cannot realize that capacity through fixed-size local cells whose excitation costs add at the inverse-grain energy. Even all sparse occupation patterns supply too few states under the gravitational energy budget. The resulting conditional theorem sharpens the collective-encoding conjecture: a positive global gap is compatible with large boundary capacity, but an additive charge per excited grain is not. Persistent record growth gives a second consequence of the same capacity law.

## The adopted cosmic branch

Use the [[factive-cosmos/boundaries-and-collective-encoding|common-count and energy premises]] in a spherical realization:
\[
\lambda^3=\alpha\ell_P^2R,\qquad
E_R=\frac{c^4R}{2G},\qquad
\ell_P^2=\frac{\hbar G}{c^3},
\qquad \alpha>0.
\tag{BC1}
\]
The grain relation is the module's proposed bulk–boundary matching. The energy budget is its spherical Schwarzschild benchmark, with a common energy reference. Their simultaneous application is a constitutive choice for this branch.

Set \(X=R/\ell_P\). The number of candidate cells is
\[
N=\left\lfloor\frac{4\pi R^3}{3\lambda^3}\right\rfloor
=\left\lfloor\frac{4\pi}{3\alpha}X^2\right\rfloor.
\tag{BC2}
\]
The boundary-capacity completion asserts that admissible states below \(E_R\) actually realize area-order distinguishability:
\[
\log\dim\mathcal C_R\ge sX^2,\qquad s>0
\tag{BC3}
\]
for arbitrarily large \(X\), with \(s\) fixed. This is a lower realization requirement. An entropy upper bound alone would not imply it. \(\mathcal C_R\) is a subspace of mutually distinguishable admissible states within the energy budget, not a list of simultaneously occupied cells.

## Test the independent-cell interpretation

Assume a fixed finite dimension \(q\ge2\) per cell,
\[
\mathcal H_N=(\mathbb C^q)^{\otimes N}.
\]
Each cell has one vacuum vector and a projection \(Q_j\) onto its \(q-1\) excited directions. The independent energetic interpretation is the operator inequality
\[
\boxed{
H_N\ge e_\lambda\mathcal N,\qquad
\mathcal N=\sum_{j=1}^NQ_j,\qquad
e_\lambda=\beta\frac{\hbar c}{\lambda},\quad \beta>0,}
\tag{BC4}
\]
with \(\beta\) fixed as \(X\) grows. The Hamiltonian can contain interactions; the inequality demands that they cannot reduce the total energy below the stated additive excitation cost.

The maximum occupation count allowed by the budget in the comparison operator is
\[
K=\left\lfloor\frac{E_R}{e_\lambda}\right\rfloor
=\left\lfloor
\frac{\alpha^{1/3}}{2\beta}X^{4/3}
\right\rfloor.
\tag{BC5}
\]
For large \(X\), \(K/N\to0\).

Let \(\mathcal C_R\subseteq\operatorname{Ran}1_{[0,E_R]}(H_N)\). The min–max principle and (BC4) give
\[
\boxed{
\dim\mathcal C_R
\le\sum_{k=0}^{\min(K,N)}{N\choose k}(q-1)^k.}
\tag{BC6}
\]
No commutation of \(H_N\) with \(\mathcal N\) is needed. The ordered eigenvalues of \(H_N\) are at least those of \(e_\lambda\mathcal N\); the latter operator has eigenvalue \(e_\lambda k\) with multiplicity \({N\choose k}(q-1)^k\).

For sufficiently large \(X\), the summands increase up to \(K\), so
\[
\begin{aligned}
\log\dim\mathcal C_R
&\le\log(K+1)+
K\log\frac{eN(q-1)}{K}\\
&=O\!\left(X^{4/3}\log X\right)
=o(X^2).
\end{aligned}
\tag{BC7}
\]
This contradicts (BC3).

**Collective-capacity theorem.** The common-count grain, gravitational energy budget, realized area-order capacity and fixed finite cell dimension cannot coexist with a uniform additive inverse-grain excitation cost.

This strengthens the observation that exciting every cell exceeds the budget. Sparse excitation patterns also fail to provide the required information capacity. The estimates count the entire low-energy subspace, including its superpositions.

The same limitation holds for a mean-energy budget. For any density operator \(\rho\) with \(\operatorname{Tr}(H_N\rho)\le E_R\), set \(p_R=E_R/(Ne_\lambda)\). For sufficiently large \(X\), \(p_R\le1-1/q\), and
\[
S(\rho)\le
N\bigl[h_2(p_R)+p_R\log(q-1)\bigr]
=O(X^{4/3}\log X).
\tag{BC7a}
\]
Here \(h_2\) is binary entropy in nats. To see the bound, write \(p_j=\operatorname{Tr}(\rho Q_j)\). The mean occupation is at most \(p_R\); each cell has entropy at most \(h_2(p_j)+p_j\log(q-1)\). Subadditivity, concavity and monotonicity up to \(1-1/q\) give the bound. The equiprobable mixture of \(M\) perfectly distinguishable record states has entropy at least \(\log M\), so the same capacity obstruction holds when each record meets only the mean-energy budget.

## What the theorem forces

Keeping the capacity and gravitational branch, the low-energy organization must escape (BC4) or the fixed finite local-cell description. Possible realizations include collective modes, large binding effects, constrained source algebras, or a different relation between spatial presentations and independent energy costs. The proposed [[scale-bearing-descent/principle-of-stable-realization|law of stable realization]] selects which of these is admissible.

This is a claim about energetic organization. It does not prove that every low-energy state is entangled or that no tensor-product presentation can be written.

A finite example separates the global gap from an additive cell gap. On the same \(\mathcal H_N\), choose a vacuum \(\Omega\) and
\[
H_N=e_\lambda(I-|\Omega\rangle\langle\Omega|).
\tag{BC8}
\]
Every vector in the vacuum complement is an \(e_\lambda\) eigenvector, so the global gap is positive. When \(E_R\ge e_\lambda\), the available space has dimension \(q^N\), with logarithmic capacity \(N\log q\). Its excitation energies are organized collectively; they do not grow with the number of occupied cell labels. This example illustrates logical compatibility, not a local Yang–Mills construction.

The [[scale-bearing-descent/principle-of-stable-realization#The Yang–Mills theorem|Yang–Mills gap theorem]] supplies a lower bound on the nonvacuum spectrum. It does not imply (BC4). That distinction allows stable local excitations and a collectively encoded arena to be returns of one law.

## Persistent novelty requires growing capacity

For a separate record consequence, adopt an operational area bound on one consistently identified recording channel:
\[
I_{\mathrm{rec}}\le\frac{A}{a_*},
\qquad a_*>0.
\tag{BC9}
\]
Here \(I_{\mathrm{rec}}\) is the logarithm of the number of admissible histories that remain jointly recoverable through that channel. The Einstein area normalization is \(a_*=4\ell_P^2\). Applying it to persistent records is an explicit completion of the capacity law; thermodynamic entropy bounds on other regions do not supply that identification automatically.

Suppose all combinations of \(n\) successive binary alternatives are admissible and perfectly recoverable, with the earlier values preserved. Then
\[
I_{\mathrm{rec},n}\ge n\log2
\quad\Longrightarrow\quad
\boxed{A_n\ge a_*n\log2.}
\tag{BC10}
\]
The [[conservation-of-causal-charge/factive-descent-and-records|record algebra]] can be \(\bigotimes_{j=1}^n\mathbb C^2\), with compatible obtained characters. Its \(2^n\) possible histories are distinct from the one character actually realized. Repeated copies of one bit do not supply \(n\) independent alternatives.

The consequence persists with a fixed decoding error \(0\le p<1/2\). For equiprobable histories and one joint decoder with error at most \(p\), let \(I_{\mathrm{acc}}\) be the mutual information between the whole history and that decoder's output. Adopt the corresponding operational bound \(I_{\mathrm{acc}}\le A_n/a_*\). The entropy bound for decoding gives
\[
\frac{A_n}{a_*}\ge I_{\mathrm{acc}}\ge
(1-p)n\log2-h_2(p),
\qquad
h_2(p)=-p\log p-(1-p)\log(1-p).
\tag{BC11}
\]
Indeed the conditional uncertainty after decoding is at most \(h_2(p)+p\log(2^n-1)\). Thus a fixed nontrivial reliability still demands unbounded area as independent retained history grows.

These are absolute lower bounds. Spare capacity can absorb new records without immediate area growth. On the perfectly recoverable branch, if a stronger economical-realization clause keeps the slack
\[
\frac{A_n}{a_*}-I_{\mathrm{rec},n}
\]
bounded, then \(A_n=a_*I_{\mathrm{rec},n}+O(1)\). Fixed slack gives an exact incremental law. This additional optimization rule is distinct from the capacity bound.

**A bounded arena cannot be both an inexhaustible producer of independent novelty and a permanent archive of its entire history.** Its recording capacity must grow, records must become inaccessible, or independent novelty must stop. Record export changes the channel being considered.

Growing required area becomes a statement about cosmic metric expansion only through [[program-core/record-scale-soldering|the record–scale realization]]. Its clock dynamics determines acceleration. The capacity theorem itself predicts the incompatibility of bounded permanent storage with unlimited retained novelty, and applies equally to a finite apparatus, a causal patch or a cosmic branch meeting its stated premises.
