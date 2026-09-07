# Local Loss Rows and the Uniform Gap

A directed quantum process can return an algebra-compatible positive clock through its pure vacuum quotient. Three explicit local rows show what that return does and does not force: independent loss has a uniform gap, a nearest-neighbor difference row has a unique vacuum but a gap closing as inverse length squared, and an entangling local conjugation preserves the uniform gap while making every one-site vacuum restriction faithful. The decisive distinction is a uniform lower bound for the whole row, not positivity of each loss term or uniqueness of its common zero.

## The response acts on vacuum-created distinctions

Use [[pure-vacuum-loss-and-the-returned-clock|the pure-vacuum loss theorem]]. A finite tensor carrier \(\mathcal H\), a unit vector \(\Omega\), and operators \(L_a\Omega=0\) determine
\[
\mathbf L:\mathcal H\longrightarrow\bigoplus_a\mathcal H,
\qquad
\mathbf L\psi=(L_a\psi)_a,\qquad
K=\tfrac12\mathbf L^*\mathbf L.
\tag{LR1}
\]
The same row gives a UCP process on \(B(\mathcal H)\):
\[
\mathscr L(A)=\sum_a L_a^*AL_a-KA-AK.
\]
The state quotient \(A\mapsto A\Omega\) intertwines this process with \(e^{-sK}\); continuation of this Hilbert semigroup supplies the clock automorphisms \(A\mapsto e^{itK}Ae^{-itK}\). This is not a claim that the dissipative process itself becomes an automorphism.

If \(\ker\mathbf L=\mathbb C\Omega\), the returned clock gap is
\[
\boxed{\Delta
=\tfrac12\inf_{\psi\perp\Omega,\ \|\psi\|=1}
\|\mathbf L\psi\|^2.}
\tag{LR2}
\]
The row acts on vectors representing distinctions \(A\Omega\), not on a coordinate called mass. Its lower singular bound becomes a clock spectral bound on that same carrier. A physical mass identification would require the appropriate spacetime translation representation and its joint invariant; [[algebra/positive-energy-pairs-and-the-neutral-gap|the positive-energy pair theorem]] and [[contemporary-puzzles/yang-mills-mass-gap/joint-causal-generators-and-the-mass-casimir|the Casimir construction]] keep that further step distinct.

## Independent local loss fixes a uniform bound

For \(N\ge1\), on \(\mathcal H_N=(\mathbb C^2)^{\otimes N}\), put
\[
\Omega_N=|0\cdots0\rangle,\qquad
s_j=(|0\rangle\langle1|)_j,\qquad
n_j=s_j^*s_j.
\]
Take one jump \(L_j=s_j\) at every site. Then
\[
K_N^{\mathrm{ind}}=\tfrac12\sum_{j=1}^N n_j,
\qquad
\boxed{\operatorname{gap}K_N^{\mathrm{ind}}=\tfrac12.}
\tag{LR3}
\]
The commuting \(n_j\) have eigenvalues zero and one. In the occupation basis the eigenvalue is half the number of excited sites. The vacuum is the only common zero and every nonvacuum vector has at least one occupied component. This proves the bound uniformly in \(N\), without a large-volume estimate.

It also exposes a limitation: this clock is a sum of independent on-site terms. Its positive gap does not imply interacting gauge dynamics.

## Local differences can retain the vacuum and lose the uniform bound

Keep exactly the same tensor carrier and vacuum. Replace the row by
\[
\boxed{L_0=s_1,\qquad L_j=s_j-s_{j+1}\quad(1\le j<N).}
\tag{LR4}
\]
There are again \(N\) jump operators. Each is supported on one site or one neighboring pair, with norms bounded independently of \(N\). The boundary term distinguishes this from an unanchored difference row.

If every \(L_j\psi=0\), the boundary condition gives \(s_1\psi=0\), and the differences successively give \(s_j\psi=0\) for all \(j\). Hence
\[
\ker K_N^{\mathrm{diff}}=\mathbb C\Omega_N,\qquad
K_N^{\mathrm{diff}}
=\tfrac12\left(n_1+\sum_{j=1}^{N-1}
(s_j-s_{j+1})^*(s_j-s_{j+1})\right).
\tag{LR5}
\]
No additional zero mode has been inserted. Nevertheless the gap is not uniform.

Let \(|j\rangle=s_j^*\Omega_N\) and \(\psi_f=\sum_{j=1}^N f_j|j\rangle\). These one-excitation vectors give
\[
\|\psi_f\|^2=\sum_j|f_j|^2,\qquad
\langle\psi_f,K_N^{\mathrm{diff}}\psi_f\rangle
=\tfrac12\left(|f_1|^2+\sum_{j=1}^{N-1}|f_j-f_{j+1}|^2\right).
\tag{LR6}
\]
For \(f_j=j\),
\[
\boxed{\operatorname{gap}K_N^{\mathrm{diff}}
\le
\frac{3}{(N+1)(2N+1)}\longrightarrow0.}
\tag{LR7}
\]
This is an actual normalized nonvacuum test in the complete carrier, not a mode of an unrelated comparison geometry. Long gentle distinctions pay little total difference cost relative to their norm. Directedness, bounded-range jumps and a unique finite-volume vacuum have not excluded them.

## The full many-body gap can be computed

Set \(Z_j=I-2n_j\) and introduce
\[
c_j=\left(\prod_{k<j}Z_k\right)s_j.
\tag{LR8}
\]
The elementary relations \(Zs=s\), \(sZ=-s\), and their adjoints imply
\[
\{c_i,c_j\}=0,\qquad \{c_i,c_j^*\}=\delta_{ij}I.
\]
For nearest neighbors the strings cancel:
\[
c_j^*c_j=n_j,\qquad c_j^*c_{j+1}=s_j^*s_{j+1}.
\]
Thus (LR5) is exactly \(\sum_{ij}c_i^*(h_N)_{ij}c_j\), where for \(N>1\)
\[
h_N=\tfrac12
\begin{pmatrix}
2&-1&&\\
-1&2&\ddots&\\
&\ddots&\ddots&-1\\
&&-1&1
\end{pmatrix};
\qquad h_1=(1/2).
\tag{LR9}
\]
The recurrence is
\[
(h_N f)_j=f_j-\tfrac12(f_{j-1}+f_{j+1}),
\qquad f_0=0,\quad f_{N+1}=f_N,
\]
also valid when \(N=1\). With \(f_j=\sin(j\theta)\), the second boundary condition is
\[
2\cos\!\bigl((N+\tfrac12)\theta\bigr)\sin(\theta/2)=0.
\]
The \(N\) distinct eigenvalues are therefore
\[
\lambda_r=1-\cos\frac{(2r-1)\pi}{2N+1},
\qquad 1\le r\le N.
\tag{LR10}
\]
The corresponding real orthonormal change of one-particle basis gives new operators \(d_r\) satisfying the same anticommutation relations, with
\[
K_N^{\mathrm{diff}}=\sum_r\lambda_r d_r^*d_r.
\]
The products of distinct \(d_r^*\) applied to \(\Omega_N\) give \(2^N\) orthonormal vectors: anticommutation proves orthonormality and the dimension gives completeness. The full spectrum consists of all subset sums of the positive \(\lambda_r\). Consequently
\[
\boxed{\operatorname{gap}K_N^{\mathrm{diff}}
=1-\cos\frac{\pi}{2N+1}
\sim\frac{\pi^2}{2(2N+1)^2}.}
\tag{LR11}
\]
This proves more than the upper test (LR7), but that test alone already rules out a uniform lower bound. The gap closure is not an artifact of restricting to one excitation.

## An entangled vacuum can keep the uniform gap

To separate a pure global state from faithful local restrictions, use a nonempty finite simple graph \(G=(V,E)\) with no isolated vertices. In a graph family assume bounded degree if uniform support size is required. Put
\[
|+\rangle=(|0\rangle+|1\rangle)/\sqrt2,\qquad
|-\rangle=(|0\rangle-|1\rangle)/\sqrt2,\qquad
b_j=(|+\rangle\langle-|)_j.
\]
Let
\[
U_G=\prod_{\{j,k\}\in E}\mathrm{CZ}_{jk},\qquad
\mathrm{CZ}=\operatorname{diag}(1,1,1,-1).
\]
The factors commute. Define the row and its common zero together:
\[
\Omega_G=U_G|+\rangle^{\otimes V},\qquad
\widetilde L_j=U_G b_jU_G^*.
\tag{LR12}
\]
Writing \(X,Y,Z\) for the usual Pauli matrices, \(b=(Z-iY)/2\) gives the explicit support:
\[
\boxed{\widetilde L_j
=\tfrac12\left(Z_j-iY_j\prod_{k\sim j}Z_k\right).}
\tag{LR13}
\]
The row lives on graph stars, rather than becoming a global operator after conjugation. Its returned clock is
\[
\boxed{
K_G=\tfrac14\sum_{j\in V}(I-S_j),\qquad
S_j=X_j\prod_{k\sim j}Z_k,\qquad
\operatorname{gap}K_G=\tfrac12.}
\tag{LR14}
\]
Indeed \(S_j=U_GX_jU_G^*\). They commute, square to identity, and their joint signs run independently over all \(2^{|V|}\) possibilities because those of the \(X_j\) do. The eigenvalue is half the number of minus signs, with unique common plus vector \(\Omega_G\). Both the gap and the vacuum follow from the same row; the bound is uniform over graph size.

Each one-site reduced state of \(\Omega_G\) is \(I/2\). Its three Pauli expectations vanish: conjugation leaves \(Z_j\) unchanged and takes \(X_j,Y_j\) to \(X_j\prod_{k\sim j}Z_k,Y_j\prod_{k\sim j}Z_k\). In the product plus state, the \(Z_j\) and \(Y_j\) means vanish, while the \(X_j\) expression has at least one zero-mean neighbor \(Z_k\). Thus the global pure state is entangled and nonfaithful on \(B(\mathcal H)\), but faithful on every one-site matrix algebra.

This does not contradict [[algebra/faithful-stationary-states-and-the-positive-clock|faithful-stationary clock rigidity]]. A one-site algebra is generally not invariant under the full clock. For example \([K_G,Z_j]\) contains \(Y_j\prod_{k\sim j}Z_k\), outside that site's algebra. Faithfulness on larger regions is not asserted; their reduced-state ranks require a separate check.

There is a sharper local boundary. Each
\(\widetilde L_j^*\widetilde L_j=(I-S_j)/2\) is a nonzero
star-supported projection with zero vacuum expectation. The vacuum is
therefore not faithful on that star algebra.
[[algebra/local-vacuum-faithfulness-and-the-loss-carrier|Local vacuum faithfulness]]
proves that this failure is necessary for a nonzero local jump
annihilating the vacuum. Where a proposed continuum vacuum is faithful
on every bounded-region algebra, these strictly local jumps cannot
persist as nonzero affiliated observable operators with the vacuum in
their domains. A different loss carrier or a controlled singular limit
is required; one-site faithfulness alone does not meet that condition.

## What the row geometry has selected

The three constructions distinguish concrete mechanisms:

| Row | Common Hilbert zero | Returned clock edge |
|---|---|---|
| Independent lowering at each site | One vacuum line | \(1/2\), uniform |
| Anchored nearest-neighbor lowering differences | The same vacuum line | \(1-\cos(\pi/(2N+1))\), closing |
| Star-supported entangling conjugate of independent loss | One entangled vacuum line | \(1/2\), uniform |

The second row measures neighboring differences and admits slowly varying excitations. The third retains independent local constraints after an exactly controlled entangling change of presentation. Neither the existence of a pure vacuum nor the number of local constraints decides the uniform lower bound.

The lattice support is supplied by a tensor factorization and its chosen row; it is not a derived Lorentzian spacetime. Bounded-range terms permit finite-range generator tests, not exact zero propagation tails at every positive time. These rows do not select three spatial dimensions, a compact simple gauge group, physical units, or the required interacting continuum limit. The graph-state clock is unitarily conjugate to an independent one and must not be sold as interacting Yang--Mills dynamics.

The relation to [[conditional-fisher-coercivity/tensor-local-refresh-and-inverse-square-patches|tensor-local Wilson refresh]] is methodological, not an identification: both require a bound on the complete row or its local patch geometry. Here the positive quantum clock is explicitly returned through the pure-state quotient; the Wilson sampler still needs its separate physical-clock comparison. No choice of the constant \(1/2\), which belongs to the declared process convention, supplies a dimensionful mass.

[[vacuum_loss_receipt.py|The finite vacuum-loss receipt]] and [[vacuum-loss-receipt-output.txt|its output]] check operator identities, local rows, one-excitation compressions and trial quotients. The proofs above supply the all-size statements; finite checks alone do not establish them.
