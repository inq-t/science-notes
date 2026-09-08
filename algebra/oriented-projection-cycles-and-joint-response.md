# Oriented Projection Cycles Constrain Loss and Phase Together

An ordered cycle of nearby subspaces determines a contraction, its discarded-norm response, and a coherent phase generator without appending a Hamiltonian. For a cycle with \(m\) edges, the leading loss and phase obey a sharp polygon inequality. This is a worked joint-selection construction from specified complex Hilbert geometry and a composition rule. Its equally important failure test is exact: refining a smooth cycle can preserve nontrivial unitary phase while its accumulated loss disappears. Neither positive loss nor an oriented cycle therefore forces a mass gap.

**Status: [EXACT FINITE-DIMENSIONAL CONSTRUCTION AND REFINEMENT THEOREM]; [OPEN] selection of the primitive geometry, positive-energy field realization and Yang–Mills gap.** Projection-generated geometric phases are established mathematics; no novelty is claimed for that mechanism or the discrete Fourier inequality used below.

## The primitive object and the actual readout

Fix finite-dimensional complex Hilbert spaces \(V,N\), their orthogonal sum \(\mathcal K=V\oplus N\), and a closed ordered polygon of linear maps

\[
A_0=A_m=0,\qquad A_j:V\to N,\qquad m\ge3.
\tag{PC1}
\]

The initial and final retained space is \(V\), with inclusion \(\iota v=(v,0)\) and projection \(P_0=\iota\iota^*\). For a real amplitude \(\epsilon>0\), let \(P_j(\epsilon)\) be the orthogonal projection onto the graph of \(\epsilon A_j\), and \(P_m=P_0\). The declared process is successive projection in this order. Its returned operator is

\[
C_\epsilon=\iota^*P_mP_{m-1}\cdots P_1\iota:V\to V.
\tag{PC2}
\]

The Hilbert forms, complex structure, polygon and ordering are inputs. The variable \(\epsilon\) measures the graph displacement; it is not a spacetime lattice spacing. All adjoints and norms refer to those fixed Hilbert forms. The represented observable algebra can be \(B(V)\); no spatially local net has yet been constructed.

There is exact accounting of the discarded components. Set \(x_0=\iota v\), \(x_j=P_jx_{j-1}\), and

\[
\mathcal D_\epsilon v=\bigl((I-P_j)x_{j-1}\bigr)_{j=1}^m
\in\mathcal K^{\oplus m}.
\]

Orthogonality at every step gives

\[
\boxed{\mathcal D_\epsilon^*\mathcal D_\epsilon
=I-C_\epsilon^*C_\epsilon.}
\tag{PC3}
\]

Thus \(v\mapsto(C_\epsilon v,\mathcal D_\epsilon v)\) is an isometry. The orthogonal slots are mathematical residue slots, not obtained measurement records. Keeping the slots and discarding them are different operations, as in [[directed-isometric-residue-completion/inq|residue completion]]. The returned contraction is invertible for sufficiently small \(\epsilon\); positive norm defect does not itself mean noninjectivity on \(V\).

## The cycle computes its generator

Write \(\Delta A_j=A_j-A_{j-1}\). The coordinate of a projected graph vector changes by

\[
T_j=(I+\epsilon^2A_j^*A_j)^{-1}
(I+\epsilon^2A_j^*A_{j-1}),\qquad
C_\epsilon=T_{m-1}\cdots T_1.
\tag{PC4}
\]

In particular,

\[
\begin{aligned}
C_\epsilon&=I-\epsilon^2K+O(\epsilon^4),\\
K&=\sum_{j=1}^{m-1}A_j^*\Delta A_j=S+iH,\\
S&=\frac12\sum_{j=1}^{m}\Delta A_j^*\Delta A_j\ge0,\\
H&=\frac1{2i}\sum_{j=1}^{m-2}
(A_j^*A_{j+1}-A_{j+1}^*A_j)=H^*.
\end{aligned}
\tag{PC5}
\]

The edge-square expression follows by expanding the squares and using the zero endpoints. The leading normal component of the \(j\)-th residue is \(-\epsilon\Delta A_jv\). Therefore, identifying each leading component with its slot in \(N\),

\[
\epsilon^{-1}\mathcal D_\epsilon
\longrightarrow (-\Delta A_j)_{j=1}^m,\qquad
\epsilon^{-2}(I-C_\epsilon^*C_\epsilon)\longrightarrow2S.
\tag{PC6}
\]

The loss and the coherent generator have now been calculated from the same polygon. In particular, the skew part left free by [[moving-response-balance-and-a-ruble-operator-signature|the general response balance]] is no longer independently adjustable with these full primitive data held fixed.

Choose repeated-cycle duration \(\delta=\epsilon^2\). Then

\[
\boxed{C_\epsilon^{\lfloor t/\epsilon^2\rfloor}
\longrightarrow e^{-t(S+iH)}}
\tag{PC7}
\]

in operator norm, uniformly on bounded nonnegative \(t\)-intervals. This is a process-scale limit on the fixed returned carrier \(V\). Taking a different proportional cycle rate changes both generators by the same factor. On the full ambient space a process preceded by \(P_0\) is not strongly continuous at zero on \(N\); (PC7) does not assert otherwise.

For completeness, put \(M=\max_j\|A_j\|\) and \(L=\sum_{j=1}^m\|\Delta A_j\|\). The exact identity

\[
T_j=I-\epsilon^2(I+\epsilon^2A_j^*A_j)^{-1}A_j^*\Delta A_j
\]

gives

\[
\|C_\epsilon-I+\epsilon^2K\|
\le\epsilon^4\left(M^3L+\frac{M^2L^2}{2}e^{\epsilon^2ML}\right).
\tag{PC8}
\]

The first term bounds replacing each inverse by identity; the second bounds all product terms of degree at least two. The projection product makes \(C_\epsilon\) a contraction; \(S\ge0\) separately makes \(e^{-\epsilon^2K}\) a contraction. Telescoping their powers proves (PC7). Importantly, (PC8) is independent of the number of cuts when \(M,L\) stay bounded.

## A sharp invariant relation between the two responses

For every such \(m\)-edge polygon,

\[
\boxed{-\cot(\pi/m)S\ \le\ H\ \le\ \cot(\pi/m)S.}
\tag{PC9}
\]

This is a quadratic-form inequality, not the generally stronger assertion \(|H|\le\cot(\pi/m)S\). It is invariant under unitary changes of the \(V,N\) presentations, and its dimensionless coefficient is unchanged by a common rate conversion.

**Proof.** For \(v\in V\), apply the unitary discrete Fourier transform to the cyclic sequence \(z_j=A_jv\), \(0\le j<m\). With \(\theta_k=2\pi k/m\),

\[
\begin{aligned}
\langle v,Sv\rangle&=\sum_k(1-\cos\theta_k)\|\widehat z_k\|^2,\\
\langle v,Hv\rangle&=\sum_k\sin\theta_k\|\widehat z_k\|^2.
\end{aligned}
\]

The constant mode contributes neither quantity. For every other mode, \(|\sin\theta_k|/(1-\cos\theta_k)\le\cot(\pi/m)\). Summing proves (PC9). For

\[
A_j=(e^{2\pi ij/m}-1)A,
\]

one computes

\[
S=m(1-\cos(2\pi/m))A^*A,\qquad
H=m\sin(2\pi/m)A^*A.
\tag{PC10}
\]

This saturates the upper inequality, proving sharpness; reversed ordering saturates the lower one. With the usual convention \(\operatorname{Area}(z)=\tfrac12\operatorname{Im}\sum_j\langle z_j,z_{j+1}\rangle\), the form of \(H\) is twice the signed polygon area. \(\square\)

For a triangle with \(A_1=A,A_2=B\), the same bound has an elementary factorization:

\[
\boxed{S\pm\sqrt3H
=(A-e^{\pm i\pi/3}B)^*(A-e^{\pm i\pi/3}B).}
\tag{PC11}
\]

The number three here comes from a triangle inequality in the comparison polygon. It is not a derivation of three spatial dimensions or a physical gauge group.

## A reversible return requires its own composition rule

The polar factor \(U_\epsilon=C_\epsilon(C_\epsilon^*C_\epsilon)^{-1/2}\) is uniquely defined for sufficiently small \(\epsilon\). The expansion gives

\[
U_\epsilon=I-i\epsilon^2H+O(\epsilon^4),\qquad
U_\epsilon^{\lfloor t/\epsilon^2\rfloor}\longrightarrow e^{-itH}.
\tag{PC12}
\]

Thus **taking the polar factor of each microscopic cycle before composing** returns a unitary group whose generator is computed, not appended. This polar-return prescription is additional to the raw projection protocol. It is not a quotient intertwining the raw dissipative semigroup with a unitary clock, nor is the polar factor of \(e^{-t(S+iH)}\) generally \(e^{-itH}\).

An exact noncommuting example on \(V=N=\mathbb C^2\) is

\[
A=I,\quad B=i\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
S=\begin{pmatrix}2&1-i/2\\1+i/2&3\end{pmatrix},\quad
H=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}.
\tag{PC13}
\]

Here \(H>0\) and \([S,H]\ne0\). The receipt explicitly distinguishes polar-after-composition from (PC12). Its numerical discrepancy is a test of two different prescriptions, not evidence of an inconsistency.

The scalar triangle \(A=1,B=i\) is simpler:

\[
C_\epsilon=\frac{1-i\epsilon^2}{(1+\epsilon^2)^2},\qquad S=2,\quad H=1.
\tag{PC14}
\]

To make this phase visible on an observable algebra, include a common line fixed by every projection, giving \(V=\mathbb C\Omega\oplus\mathbb Ce\), with \(A\Omega=B\Omega=0\) and \(Ae=1,Be=i\). The polar return is \(\operatorname{diag}(1,e^{-it})\), so conjugation acts nontrivially on the transition \(|\Omega\rangle\langle e|\). The common line and reference vector are explicit inputs, not a derived vacuum. The state-action representation in [[quotient-clock-and-stationary-action]] can be applied to the resulting unitary group; its particular upstream quotient hypotheses have not been claimed for the raw cycles.

## Refinement can remove loss without removing phase

Let \(A(u)\), \(0\le u\le1\), be an operator-norm \(C^1\) path with \(A(0)=A(1)=0\), and sample \(A_j=A(j/m)\). Then \(M,L\) in (PC8) are bounded uniformly, while

\[
S_m=O(m^{-1}),\qquad K_m\longrightarrow
\int_0^1 A^*A'\,du=iH_\infty,\qquad
H_\infty=\frac1{2i}\int_0^1(A^*A'-A'^*A)\,du.
\tag{PC15}
\]

The boundary term in the integral of \((A^*A)'\) vanishes. Combining (PC8), contraction telescoping, and convergence of \(K_m\) proves the simultaneous limit

\[
\boxed{
C_{\epsilon,m(\epsilon)}^{\lfloor t/\epsilon^2\rfloor}
\longrightarrow e^{-itH_\infty}
\quad\text{whenever }\epsilon\downarrow0,\ m(\epsilon)\to\infty.}
\tag{PC16}
\]

Here is an explicit estimate that avoids exchanging two limits. Choose uniform bounds \(M_*,L_*\) for samples of the same fixed path, put \(B_*=M_*L_*\), and fix \(\epsilon\le\epsilon_0\). The one-cycle error against \(e^{-\epsilon^2K_m}\) is at most \(\epsilon^4Q_*\), where
\[
Q_*=M_*^3L_*+B_*^2e^{\epsilon_0^2B_*}.
\]
Contraction telescoping, the fractional final step, and Duhamel's formula give, for \(0\le t\le T\),
\[
\left\|C_{\epsilon,m}^{\lfloor t/\epsilon^2\rfloor}
-e^{-itH_\infty}\right\|
\le T\epsilon^2Q_*+\epsilon^2B_*
+T\|K_m-iH_\infty\|.
\tag{PC16a}
\]
Every term vanishes under the simultaneous limit. A family whose path amplitude or variation grows without bound is not covered by this argument.

No microscopic polar correction is needed in this different refinement. In (PC10), \(S_m\sim2\pi^2A^*A/m\) but \(H_m\to2\pi A^*A\). The entire raw norm defect therefore tends to zero at a fixed returned duration, although the phase remains nontrivial. The order and resolution of comparisons matter: a finite-cycle response law and unrestricted smooth refinement are not the same primitive protocol.

## What the construction excludes, and what it still permits

The sharp inequality is a genuine joint relation, but it gives an upper bound on phase relative to loss—not the lower bound needed to transfer a loss gap to a clock gap. Taking \(A=B=I\) yields \(S=I,H=0\). Taking \(A=I,B=e^{i\phi}I\) yields \(S=(2-\cos\phi)I,H=\sin\phi I\), so the coherent rate tends to zero while the loss stays positive. Reversing any cycle gives exactly \(C_\epsilon^*\), preserving \(S\) and negating \(H\). Directed order supplies a sign; it does not require positive energy.

There is a stronger inventory of the remaining freedom. Every finite-dimensional Hermitian pair \(S,H\) with \(S\pm\sqrt3H\ge0\) is realizable by a triangle. Choose factorizations \(C_\pm^*C_\pm=S\pm\sqrt3H\) into one normal space, then solve the two linear equations \(C_\pm=A-e^{\pm i\pi/3}B\). Equation (PC11) recovers precisely the prescribed \(S,H\). Thus triangle geometry parametrizes the whole stated sectorial cone; its mere existence does not select a preferred spectrum.

This construction passes the independent-retuning test **with its full polygon and protocol fixed**. It does not prove that those primitive choices are necessary. A further law must restrict their allowed geometry and refinement strongly enough to exclude arbitrarily soft returned excitations. The separate [[contemporary-puzzles/yang-mills-mass-gap/mass-as-casimir-and-realization#A Poincare Hamiltonian has no positive eigenvalues|boost-spectrum theorem]] also prevents identifying these finite or pure-point clocks directly with a nontrivial Poincare Hamiltonian. A new field carrier and the appropriate joint invariant are required.

[[unbounded-projection-cycles-and-inherited-spectra|The closed-graph extension]] makes this freedom precise beyond finite matrices: for every nonnegative self-adjoint \(T\), the triangle \(D=T^{1/2},\,iD\) returns phase generator \(T\) and loss form \(4T\). It includes both gapless and arbitrarily gapped continuous-spectrum carriers with the same one-dimensional kernel. Its proof uses strong limits and closed form domains; unbounded graph projections are not nearby in operator norm.

Projection-generated geometric phase has established precedents, including [[library/measuring-geometric-phases-with-a-dynamical-quantum-zeno-effect/inq|Do, Gessner, Cataliotti and Smerzi]]. The present note gives a self-contained finite graph-polygon calculation and its two refinement prescriptions. [[directed-analytic-realization/projection_cycle_receipt.py|The receipt]] checks actual ambient projection products, residue accounting, the sectorial-cone converse, and the uniform remainder estimate. It also tests simultaneous refinement of a fixed two-harmonic noncommuting path against its independently computed Fourier generator, using two distinct refinement schedules. These finite diagnostics do not replace the uniform-limit proof or establish novelty or a Yang–Mills continuum theorem.
