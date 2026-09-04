---
inq.module: "vacuum-aligned-innovation-completion"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Vacuum-Aligned Innovation Completion

An orthogonal block decomposition need not decompose the vacuum complement block by block. If the vacuum has components in several blocks, centering each block internally misses the relative balance among those components. There is an exact canonical repair: split every block into its vacuum ray and internal orthogonal complement, then add one vacuum-balance sector—the span of all blockwise vacuum components modulo the total vacuum. Applied to boundary-framed lattice gauge theory, this completes the dual-charge innovation carrier for an interacting Perron state and identifies an additional row and column that every transfer-matrix gap estimate must control.

**Status: [EXACT] for the vacuum-aligned Hilbert decomposition, projection formulas, transfer block bound, compact-group isotypic refinement, and faithful finite-state gauge application; [OPEN] for a volume- and continuum-uniform bound on the resulting Wilson/Perron matrix; [CONDITIONAL] for an algebraic Type-III lift of the Hilbert projections.**

## The missing balance sector

Let \(\mathcal H\) be a separable Hilbert space with a finite or countable
orthogonal resolution

$$
E_\alpha E_\beta
=
\delta_{\alpha\beta}E_\alpha,
\qquad
\sum_{\alpha\in\mathcal A}E_\alpha
=I
\quad\text{strongly}.
\tag{VA1}
$$

Let \(\Omega\in\mathcal H\) be a unit vector and put

$$
\Omega_\alpha:=E_\alpha\Omega,
\qquad
p_\alpha:=\|\Omega_\alpha\|^2,
\qquad
\sum_\alpha p_\alpha=1.
\tag{VA2}
$$

For \(p_\alpha>0\), define the internally centered block

$$
\mathcal H_\alpha^\circ
:=
E_\alpha\mathcal H\ominus\mathbb C\Omega_\alpha.
\tag{VA3}
$$

If \(p_\alpha=0\), put
\(\mathcal H_\alpha^\circ:=E_\alpha\mathcal H\). Define

$$
\mathcal V_\Omega
:=
\overline{\operatorname{span}}
\{\Omega_\alpha:p_\alpha>0\},
\qquad
\mathcal B_\Omega
:=
\mathcal V_\Omega\ominus\mathbb C\Omega.
\tag{VA4}
$$

The space \(\mathcal B_\Omega\) is the **vacuum-balance sector**. Its vectors
alter the relative amplitudes among the blockwise vacuum components while
remaining orthogonal to the total vacuum.

## Vacuum-aligned completion theorem

Each block splits orthogonally as

$$
E_\alpha\mathcal H
=
\begin{cases}
\mathbb C\Omega_\alpha\oplus\mathcal H_\alpha^\circ,
&p_\alpha>0,\\
\mathcal H_\alpha^\circ,
&p_\alpha=0.
\end{cases}
\tag{VA5}
$$

The vacuum rays belonging to different blocks are orthogonal. Summing (VA5)
and then removing the one total vacuum line gives

$$
\boxed{
\Omega^\perp
=
\mathcal B_\Omega
\oplus
\widehat\bigoplus_{\alpha\in\mathcal A}
\mathcal H_\alpha^\circ .}
\tag{VA6}
$$

No independence, tensor-product, or dynamics hypothesis is used. In a finite
family,

$$
\dim\mathcal B_\Omega
=
\#\{\alpha:p_\alpha>0\}-1.
\tag{VA7}
$$

Thus internal block centering is complete exactly when the vacuum is
supported in only one block.

There is a canonical model for the part that was missed. Put
\(J:=\{\alpha:p_\alpha>0\}\), give \(J\) the probability weights
\(p_\alpha\), and define

$$
U:L^2(J,p)\longrightarrow\mathcal V_\Omega,
\qquad
Uf:=\sum_{\alpha\in J}f(\alpha)\Omega_\alpha.
\tag{VA7a}
$$

Then \(U\) is unitary, \(U1=\Omega\), and hence

$$
\boxed{
\mathcal B_\Omega
\cong
L^2(J,p)\ominus\mathbb C1.}
\tag{VA7b}
$$

The balance sector is therefore not a mysterious extra charge. It is the
centered geometry of the vacuum's relative block weights. If
\(P_{\mathbb C\Omega_\alpha}x=m_\alpha(x)\Omega_\alpha\) and
\(P_{\mathbb C\Omega}x=m(x)\Omega\), then

$$
m(x)=\sum_{\alpha\in J}p_\alpha m_\alpha(x)
\tag{VA7c}
$$

and the orthogonal decomposition gives the exact total-variance identity

$$
\boxed{
\|(I-P_\Omega)x\|^2
=
\sum_\alpha\|Q_\alpha^\circ x\|^2
+
\sum_{\alpha\in J}
p_\alpha|m_\alpha(x)-m(x)|^2.}
\tag{VA7d}
$$

The first term is within-block distinction; the second is between-block
distinction. This is an identity of pointed Hilbert geometry, not an entropy
law or a claim of stochastic ontology.

[[vacuum-balance-fisher-geometry/inq|Vacuum-Balance Fisher Geometry]]
sharpens the information-geometric face of this statement. Real balance
directions are Fisher score tangents of the law \(p\), with the usual factor
four between normalized Born-amplitude speed and Fisher speed. Imaginary
balance directions are relative phases and leave every \(p_\alpha\)
unchanged. The same note proves that this static metric selects no transfer
rate and derives the shorted defect that includes excursions through the
internal blocks.

The projections are explicit. With Dirac notation for rank-one operators,

$$
Q_\alpha^\circ
:=
\begin{cases}
E_\alpha-
\dfrac{|\Omega_\alpha\rangle\langle\Omega_\alpha|}{p_\alpha},
&p_\alpha>0,\\[1.2ex]
E_\alpha,
&p_\alpha=0,
\end{cases}
\tag{VA8}
$$

and

$$
P_{\mathcal V_\Omega}
=
\mathop{\sum_{\alpha:p_\alpha>0}}^{\mathrm s}
\frac{|\Omega_\alpha\rangle\langle\Omega_\alpha|}{p_\alpha},
\qquad
Q_{\mathrm{bal}}
:=
P_{\mathcal V_\Omega}-|\Omega\rangle\langle\Omega|.
\tag{VA9}
$$

They are pairwise orthogonal projections and obey

$$
\boxed{
I-|\Omega\rangle\langle\Omega|
=
Q_{\mathrm{bal}}
+
\mathop{\sum_{\alpha\in\mathcal A}}^{\mathrm s}
Q_\alpha^\circ .}
\tag{VA10}
$$

The plus sign in (VA10) is an orthogonal sum. The formula displays exactly
what the tempting expression
\(\bigoplus_\alpha(E_\alpha\mathcal H\cap\Omega^\perp)\) omits:

$$
E_\alpha\mathcal H\cap\Omega^\perp
=
\mathcal H_\alpha^\circ,
\qquad
\left[
\widehat\bigoplus_\alpha
(E_\alpha\mathcal H\cap\Omega^\perp)
\right]^\perp\cap\Omega^\perp
=
\mathcal B_\Omega.
\tag{VA11}
$$

Two shortcuts are thereby ruled out. A raw \(E_\alpha\) preserves
\(\Omega^\perp\) only when \(E_\alpha\Omega=0\) or
\(E_\alpha\Omega=\Omega\). Moreover,
\((I-P_\Omega)E_\alpha(I-P_\Omega)\) is generally only a positive
contraction, not a projection. The vacuum-aligned family must be constructed
before applying a block-operator estimate.

## The complete transfer matrix

Let \((\mathcal H_X,\Omega_X)\) and
\((\mathcal H_Y,\Omega_Y)\) have vacuum-aligned resolutions
\(\{Q_a^X\}_{a\in\mathcal I_X}\) and
\(\{Q_b^Y\}_{b\in\mathcal I_Y}\), including their balance projections when
nonzero. Let \(P:\mathcal H_Y\to\mathcal H_X\) be bounded and satisfy

$$
P\Omega_Y=\Omega_X,
\qquad
P^*\Omega_X=\Omega_Y.
\tag{VA12}
$$

Then \(P\) maps \(\Omega_Y^\perp\) into \(\Omega_X^\perp\). Define

$$
c_{ab}:=\|Q_a^XPQ_b^Y\|,
\qquad
C=(c_{ab}).
\tag{VA13}
$$

Whenever \(C\) defines a bounded operator
\(\ell^2(\mathcal I_Y)\to\ell^2(\mathcal I_X)\), the block-operator estimate
gives

$$
\boxed{
\|P|_{\Omega_Y^\perp}\|
\leq
\|C\|_{2\to2}.}
\tag{VA14}
$$

For a common finite index set, write

$$
r_{\mathrm{blk}}:=\max_a c_{aa},
\qquad
R_{\mathrm{off}}:=\max_a\sum_{b\neq a}c_{ab},
\qquad
S_{\mathrm{off}}:=\max_b\sum_{a\neq b}c_{ab}.
\tag{VA15}
$$

Then Schur's test gives

$$
\boxed{
\|P|_{\Omega^\perp}\|
\leq
r_{\mathrm{blk}}
+
\sqrt{R_{\mathrm{off}}S_{\mathrm{off}}}.}
\tag{VA16}
$$

If \(Q_{\mathrm{bal}}\neq0\), its row and column are load-bearing. Deleting
them destroys the resolution (VA10), so the resulting matrix cannot certify
the full physical contraction.

## Canonical charge-resolved blocks before vacuum alignment

Consider the edge cut and regional carriers in
[[gauge-boundary-frame-gluing/inq|Gauge Boundary Frames and Gauss Gluing]].
Write \(K=G^\partial\). Let

$$
F_0^A\leq F_1^A\leq\cdots\leq F_m^A=I
\tag{VA17}
$$

be coordinate conditional expectations on
\(\mathcal H_A^{\mathrm{ext}}=L^2(\nu_A)^{K_A}\), beginning with expectation
onto constants, and define

$$
D_0^A:=F_0^A,
\qquad
D_i^A:=F_i^A-F_{i-1}^A.
\tag{VA18}
$$

Use an analogous tower on \(B\). Every selected-edge sigma-algebra is stable
under the boundary action and each marginal is boundary invariant, so the
expectations commute with \(K\).

For \(\lambda\in\widehat K\), the canonical isotypic projection is

$$
Z_\lambda^A
:=
d_\lambda
\int_K
\overline{\chi_\lambda(k)}R_A(k)\,\mathrm dk,
\tag{VA19}
$$

and similarly on \(B\). Thus \(D_i^A\) commutes with every
\(Z_\lambda^A\). On the product-marginal boundary-framed physical carrier,
put

$$
E_{ij\lambda}
:=
Q_\partial
\left[
(D_i^AZ_\lambda^A)
\otimes
(D_j^BZ_{\lambda^*}^B)
\right]
Q_\partial .
\tag{VA20}
$$

Restricted to the diagonal \(K\)-invariant subspace, the nonzero
\(E_{ij\lambda}\) are mutually orthogonal projections and

$$
\boxed{
\sum_{i,j,\lambda}E_{ij\lambda}=I
\quad\text{strongly}.}
\tag{VA21}
$$

Equation (VA20) is basis-free. Choosing bases of boundary representation
spaces only writes the normalized coevaluation tensor explicitly; the
isotypic projection and the diagonal invariant do not depend on that choice.
The edge cut and regional filtrations remain analysis choices.

## The interacting vacuum creates the balance block

Let the actual faithful joint law be

$$
\mathrm d\nu(a,b)
=
r(a,b)\,\mathrm d\nu_A(a)\mathrm d\nu_B(b),
\qquad
r>0.
\tag{VA22}
$$

The gauge-equivariant unitary

$$
W:L^2(\nu)\longrightarrow L^2(\nu_A\otimes\nu_B),
\qquad
Wf=\sqrt r\,f
\tag{VA23}
$$

transports the physical carrier to the product-marginal presentation.
Conjugating (VA20) gives a complete physical block resolution on the actual
state carrier,

$$
\widetilde E_{ij\lambda}
:=
W^{-1}E_{ij\lambda}W.
\tag{VA24}
$$

But the vacuum \(1\in L^2(\nu)\) becomes

$$
\omega:=W1=\sqrt r.
\tag{VA25}
$$

Its block weights are therefore

$$
p_{ij\lambda}
=
\|E_{ij\lambda}\sqrt r\|^2.
\tag{VA26}
$$

Applying (VA6)--(VA10) to the family \(E_{ij\lambda}\) produces the complete
centered carrier. The internal spaces describe distinctions within fixed
regional-depth and boundary-charge blocks. The balance sector describes
relative changes among the components of the correlation half-density
\(\sqrt r\).

For \(r=1\), the vacuum lies entirely in the constant,
\(\lambda=\mathbf1\) block and the balance sector vanishes. For an
interacting state, \(r^{1/2}\) can occupy several dual-charge and innovation
blocks. Even if each occupied block is one-dimensional and hence has no
internal centered direction, their relative balance can contain the whole
vacuum-complement excitation.

This balance is not an entropy, a probability of ontological charge, or a
mass. It is a Hilbert-space consequence of presenting a correlated vacuum
through product regional marginals. Small \(p_{ij\lambda}\) alone does not
bound a normalized transfer mode supported there.

## The revised Yang--Mills stopping condition

Let \(\mathcal Q_{a,L}\) denote the complete family consisting of
\(Q_{\mathrm{bal}}\) and every nonzero internal projection obtained from
(VA20)--(VA26) on the physical Wilson/Perron slice. For the actual normalized
transfer \(P_{a,L}\), define

$$
C_{a,L}(q,q')
:=
\|qP_{a,L}q'\|,
\qquad
q,q'\in\mathcal Q_{a,L}.
\tag{VA27}
$$

Writing
\(\rho_{\mathrm{GI}}(P_{a,L})
:=\|P_{a,L}(I-P_{\Omega_{a,L}})\|\),
the finite-regulator physical contraction obeys

$$
\rho_{\mathrm{GI}}(P_{a,L})
\leq
\|C_{a,L}\|_{2\to2}.
\tag{VA28}
$$

At fixed physical slab thickness \(\ell_*>0\), a sufficient continuum
stopping condition is

$$
\limsup_{a\downarrow0}\sup_{L,\mathsf s}
\|C_{a,L,\mathsf s}^{(\ell_*)}\|_{2\to2}
\leq q_*<1
\tag{VA29}
$$

over every flux or boundary sector retained in the declared physical
carrier. For adjacent temporal slices of thickness \(\ell_a\), and an
independently fixed Yang--Mills scale \(\Lambda_{\mathrm{YM}}>0\), the
dimensionless finite physical-rate condition is instead

$$
\liminf_{a\downarrow0}\inf_{L,\mathsf s}
\frac{\hbar c}{\ell_a\Lambda_{\mathrm{YM}}}
\left[-\log\|C_{a,L,\mathsf s}\|_{2\to2}\right]
>0.
\tag{VA30}
$$

The balance row is a new explicit obligation in either form. It is where a
global almost-conserved mode can survive even when every internally centered
regional charge block contracts.

For changing vacua and carriers, this one-arrow estimate is replaced by
[[vacuum-aligned-transfer-cocycle/inq|the ordered block-cocycle theorem]].
The complete matrices multiply across a fixed physical slab, and the norm of
their product bounds the exact centered transfer. Individual stages may have
norm one if their untouched directions are complementary; it is the joint
product, not every factor separately, that must be subunit. The target
vacuum alignment must be rebuilt after a genuine state change rather than
transported by a nonunitary half-density as though it preserved orthogonality.

## Noncommutative and Type-III boundary

The abstract theorem (VA1)--(VA16) applies on every Hilbert space. Its safe
Type-III form is a **state-pointed correspondence theorem**, not an
expectation theorem. Let \({}_N\mathcal K_N\) be a normal correspondence and
suppose an atomic abelian algebra

$$
\mathcal D\subseteq\operatorname{End}_{N-N}(\mathcal K)
\tag{VA31}
$$

has atoms \(e_\alpha\) with strong sum one. Taking \(E_\alpha=e_\alpha\)
in (VA1) gives the same decomposition and identifies its balance part with
\(L^2(J,p)\ominus\mathbb C1\), without a trace or density matrix.

For a faithful normal expected inclusion \(N\subseteq M\), the natural place
to seek such channel projections is the higher relative commutant

$$
\operatorname{End}_{N-N}(L^2(M))
\cong
N'\cap M_1,
\tag{VA32}
$$

where \(M_1=\langle M,e_N\rangle\) is the Jones basic construction.
Finite-index correspondences and Q-systems provide one standard source of
discrete structure, while Connes fusion composes correspondences already
supplied. None of these operations selects \(\mathcal D\), the pointed
vector, or the transfer dynamics.

The restrictions are decisive:

- On the identity correspondence of a factor,
  \(\operatorname{End}_{M-M}(L^2(M))=Z(M)=\mathbb C\). A nontrivial block
  family therefore requires an enlarged boundary or inclusion
  correspondence.
- Even when the \(e_\alpha\) are bimodule projections, the rank-one
  \(P_{\mathbb C\Omega_\alpha}\) generally are not. Thus
  \(Q_\alpha^\circ\) and \(Q_{\mathrm{bal}}\) ordinarily live in
  \(B(\mathcal K)\), not in the observable algebra, the basic construction,
  or the correspondence endomorphism algebra. They are Hilbert analysis
  projections, not completely positive maps.
- A family of mutually orthogonal \(e_\alpha\) cannot consist of GNS
  implementations of unital vacuum-preserving expectations: every such
  implementation fixes the same vacuum vector. Takesaki modular invariance
  remains the gate to each state-preserving expectation, and ordinary nested
  vacuum local algebras face the Reeh--Schlieder no-go recorded in
  [[two-slice-innovation-geometry/inq|Two-Slice Innovation Geometry]].
- At a sharp Type-III cut there is no density-matrix Schmidt factorization.
  Under an independently proved split isomorphism, the analogue of
  \(\sqrt r\) is the correlated state's unique natural-cone vector in the
  tensor-product standard form. A real-parameter Connes cocycle is not
  automatically its bounded value at \(t=-i/2\); that continuation requires
  separate analytic and domination hypotheses.
- If the labels are genuinely central superselection sectors, their relative
  phases are not observable and a pure vacuum normally belongs to one global
  sector. The lattice \(\lambda\)'s must instead survive as internal cut
  channels inside one globally neutral sector before their balance may count
  as a physical excitation.

The safe present claim is Hilbert completeness on the finite
Euclidean/Perron carrier. A continuum lift must construct a pointed boundary
correspondence, place the raw dual-charge innovations in an atomic
\(N'\cap M_1\), intertwine it with the OS carrier and transfer, and then prove
the complete matrix estimate including the balance row. Collapse of the
higher relative commutant to scalars, failure of the bimodule commutators, or
loss of the fixed-slab norm bound falsifies that lift.

## Receipt and dependencies

[[vacuum-aligned-innovation-completion/receipts/vacuum_balance_receipt.py|The
finite receipt]] uses the physical carrier of two \(\mathbb Z_2\) links with
correlation density \(r(z)=1+0.6z\). The half-density has block weights
\((0.9,0.1)\) in the trivial and charged-pair sectors. Both internal centered
blocks have rank zero, while the balance projection has rank one and carries
the entire nonvacuum transfer eigenvalue. [[vacuum-aligned-innovation-completion/receipts/vacuum-balance-receipt-output.txt|The
stored output]] records the result.

[[gauge-boundary-frame-gluing/inq|Gauge Boundary Frames and Gauss Gluing]]
supplies the dual-charge carrier and correlation half-density.
[[two-slice-innovation-geometry/inq|Two-Slice Innovation Geometry]] supplies
the general endpoint block-operator estimate.
[[library/decomposition-of-entanglement-entropy-in-lattice-gauge-theory/inq|Donnelly]]
provides the primary boundary-representation gluing precedent.
[[library/local-subsystems-in-gauge-theory-and-gravity/inq|Donnelly and
Freidel]] identify physical gluing with the diagonal boundary-singlet
subspace.
[[library/spin-network-states-in-gauge-theory/inq|Baez]] supplies the
fixed-graph Peter--Weyl and spin-network basis.
[[library/some-properties-of-modular-conjugation-and-a-noncommutative-radon-nikodym-theorem-with-a-chain-rule/inq|Araki]]
supplies the natural-cone representative and the commutative square-root
Radon--Nikodym precedent.
[[library/conditional-expectations-in-von-neumann-algebras/inq|Takesaki]]
supplies the modular-invariance gate for state-preserving expectations.
[[library/tensor-categories-and-endomorphisms-of-von-neumann-algebras/inq|Bischoff--Longo--Kawahigashi--Rehren]]
supplies the finite-index correspondence and Q-system framework.
