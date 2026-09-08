# Finite Gauss Gluing

On a finite graph with product Haar measure, imposing Gauss law only in each region's interior leaves complementary boundary representations. Diagonal gluing pairs each charge with its dual and recovers the physical whole; closing the regions separately can erase physical loops.

## The cut must leave a boundary action

Let \(G\) be a compact Lie group with normalized Haar measure. All Hilbert spaces are complex, with the usual left and right endpoint gauge actions. Let a finite graph have an edge partition

$$
E=E_A\sqcup E_B,
$$

with regional vertex sets \(V_A,V_B\) and common boundary

$$
\partial:=V_A\cap V_B.
\tag{BG1}
$$

Put

$$
K_A:=G^{V_A\setminus\partial},
\qquad
K_B:=G^{V_B\setminus\partial},
\qquad
K_\partial:=G^\partial .
\tag{BG2}
$$

With product Haar measure, the raw slice carrier factors as

$$
\mathcal H_{\mathrm{raw}}
=L^2(G^{E_A})\widehat\otimes L^2(G^{E_B}).
\tag{BG3}
$$

Average the two interior gauge groups but not \(K_\partial\):

$$
\mathcal H_A^{\mathrm{ext}}
:=L^2(G^{E_A})^{K_A},
\qquad
\mathcal H_B^{\mathrm{ext}}
:=L^2(G^{E_B})^{K_B}.
\tag{BG4}
$$

The superscript **ext** means extended only at the cut. These spaces obey
Gauss law in each interior while carrying unitary boundary representations

$$
R_A:K_\partial\to\mathcal U(\mathcal H_A^{\mathrm{ext}}),
\qquad
R_B:K_\partial\to\mathcal U(\mathcal H_B^{\mathrm{ext}}).
\tag{BG5}
$$

The boundary acts diagonally on the regional tensor product. Since gauge
transformations at distinct vertices commute, the full gauge average
factorizes as

$$
Q_{\mathrm{GI}}
=Q_\partial(Q_A\otimes Q_B)
=(Q_A\otimes Q_B)Q_\partial .
\tag{BG6}
$$

Therefore

$$
\boxed{
L^2(G^E)^{G^V}
\cong
\left(
\mathcal H_A^{\mathrm{ext}}
\widehat\otimes
\mathcal H_B^{\mathrm{ext}}
\right)^{K_\partial}.}
\tag{BG7}
$$

This is the finite Gauss-gluing theorem. It does not assume that either
regional factor is a closed physical universe. The parts are charged
presentations; their diagonal invariant is the closed whole.

## The whole is assembled from dual boundary charges

Because \(K_\partial\) is compact, decompose the two boundary
representations into irreducibles:

$$
\mathcal H_A^{\mathrm{ext}}
\cong
\widehat\bigoplus_{\lambda\in\widehat K_\partial}
M_{A,\lambda}\otimes V_\lambda,
\qquad
\mathcal H_B^{\mathrm{ext}}
\cong
\widehat\bigoplus_{\mu\in\widehat K_\partial}
M_{B,\mu}\otimes V_\mu .
\tag{BG8}
$$

Here the multiplicity spaces \(M_{A,\lambda}\) and \(M_{B,\mu}\) contain
the regional path and loop data, while \(V_\lambda,V_\mu\) carry the exposed
boundary charges. Schur orthogonality gives

$$
(V_\lambda\otimes V_\mu)^{K_\partial}
\cong
\begin{cases}
\mathbb C,&\mu\cong\lambda^*,\\
0,&\text{otherwise}.
\end{cases}
\tag{BG9}
$$

For \(\mu=\lambda^*\), the invariant line is spanned by the normalized
coevaluation vector

$$
\Omega_\lambda
=
\frac1{\sqrt{\dim V_\lambda}}
\sum_{j=1}^{\dim V_\lambda}e_j\otimes e^j .
\tag{BG9a}
$$

Consequently

$$
\boxed{
\mathcal H_{\mathrm{GI}}
\cong
\widehat\bigoplus_{\lambda\in\widehat K_\partial}
M_{A,\lambda}\widehat\otimes M_{B,\lambda^*}.}
\tag{BG10}
$$

The physical whole is not obtained by demanding that each part have zero
boundary charge. It is obtained by matching contrary charges so that their
joint presentation is neutral. This is a precise algebraic instance of the
principle that a global distinction can require locally nontrivial,
complementary presentations.

For \(K_\partial=G^\partial\), the label \(\lambda\) is a tuple of
irreducible \(G\)-representations, one per cut vertex. Orientation determines
which side carries a representation and which carries its contragredient;
the invariant intertwiner, rather than an equality of informal flux signs,
is the coordinate-free gluing datum.

## Closing the parts first loses physical loops

If one instead gauge-averages the boundary on each region separately, the
regional physical carriers are

$$
\mathcal H_A^{\mathrm{cl}}
=(\mathcal H_A^{\mathrm{ext}})^{K_\partial}
\cong M_{A,\mathbf1},
\qquad
\mathcal H_B^{\mathrm{cl}}
\cong M_{B,\mathbf1}.
\tag{BG11}
$$

Their tensor product maps only into the \(\lambda=\mathbf1\) summand of
(BG10). Hence

$$
\boxed{
\mathcal H_A^{\mathrm{cl}}\widehat\otimes
\mathcal H_B^{\mathrm{cl}}
\subseteq
\mathcal H_{\mathrm{GI}},
\quad
\text{with equality only if every nontrivial paired sector vanishes}.}
\tag{BG12}
$$

A Wilson loop crossing the cut illustrates the loss. Its segment in \(A\)
is an open path with boundary indices, and its segment in \(B\) carries the
dual indices. Contracting those indices makes the full loop invariant.
Averaging either segment over its boundary before the contraction kills the
nontrivial representation component. What looks locally like gauge-variant
presentation data can therefore be indispensable relational data of the
whole.

This refines the forest lemma in
[[gauge-cycle-innovation-filtration/inq|Gauge-Cycle Innovation
Filtration]]. A fully gauged forest contains no closed physical distinction.
A regional forest with ungauged boundary vertices can contain an open
charged path; two such paths may glue into the very cycle on which the first
global innovation lives.

## Sources and receipt

- [[library/remarks-on-entanglement-entropy-for-gauge-fields/inq|Casini--Huerta--Rosabal]] analyze regional factorization and boundary centers, principally for Abelian theories. Their discussion does not establish general non-Abelian equivalence of the center and extended-lattice constructions or construct a continuum limit.
- [[library/decomposition-of-entanglement-entropy-in-lattice-gauge-theory/inq|Donnelly]] gives the physical-to-open-region embedding and the dual boundary-representation contraction, including the normalized coevaluation factor.
- [[library/local-subsystems-in-gauge-theory-and-gravity/inq|Donnelly--Freidel]] formulate gluing as the diagonal boundary-singlet condition. The finite compact-group projection used here avoids the distributional issues of continuum quantum constraints.
- [[library/fusion-basis-for-lattice-gauge-theory-and-loop-quantum-gravity/inq|Delcamp--Dittrich--Riello]] develop a fusion basis for finite gauge groups in 2+1 dimensions; their discussion of continuous groups is an extension, not a compact-Lie-group fusion theorem.
- [[library/a-new-basis-for-hamiltonian-su-2-simulations/inq|Bauer--D'Andrea--Freytsis--Grabowska]] display maximal-tree loop variables, residual simultaneous conjugation, and the nonlocal electric action on those variables. A transported electric generator can act on several loops.

[[gauge-boundary-frame-gluing/receipts/boundary_charge_gluing_receipt.py|The finite receipt]] checks the theorem for two \(\mathbb Z_2\) links split across one effective boundary action. Each open regional link has trivial and charged components; diagonal gluing retains both the neutral--neutral and charged--charged pairs, whereas closing the two regions separately retains only the first. [[gauge-boundary-frame-gluing/receipts/boundary-charge-gluing-receipt-output.txt|The stored output]] records the dimensions and projection identities.
