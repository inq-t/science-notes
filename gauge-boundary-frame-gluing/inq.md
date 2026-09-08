---
inq.module: "gauge-boundary-frame-gluing"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Gauge Boundary Frames and Gauss Gluing

A gauge-invariant whole generally does not factor into gauge-invariant parts. On a finite graph cut into two edge regions, first impose Gauss law only at interior vertices; each extended regional carrier then retains a representation of the boundary gauge group. The physical whole is exactly the diagonal-invariant subspace of the tensor product of these extended carriers, so Peter--Weyl theory pairs every boundary charge with its dual. Closing each region separately keeps only the trivial boundary representation and can erase globally closed loop distinctions. This supplies the correct local frame for the gauge-cycle innovation programme: decompose charged regional paths first, glue dual fluxes second, and estimate physical transfer only after the global Gauss projection.

**Status: [EXACT] for the finite product-Haar Hilbert-space gluing theorem, its boundary-charge decomposition, and the separately-closed-sector no-go; [EXACT UP TO AN EQUIVARIANT UNITARY] for faithful gauge-invariant densities relative to product Haar; [CONDITIONAL] for separator-relative tensor products; [OPEN] for a volume- and continuum-uniform transfer estimate in these frames.**

## The cut must leave a boundary action

Let a finite graph have an edge partition

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

## Faithful Wilson weights preserve the carrier, not the factorization

Let a normalized gauge-invariant law have a faithful density relative to
product Haar,

$$
\mathrm d\nu(a,b)=w(a,b)\,
\mathrm d\mu_A(a)\mathrm d\mu_B(b),
\qquad w>0\ \text{a.e.}
\tag{BG13}
$$

Write \(\nu_A,\nu_B\) for its marginals and define its correlation density

$$
r(a,b)
:=
\frac{\mathrm d\nu}{\mathrm d(\nu_A\otimes\nu_B)}(a,b).
\tag{BG14}
$$

Multiplication by \(r^{1/2}\) defines a gauge-equivariant unitary

$$
W:L^2(\nu)\longrightarrow L^2(\nu_A\otimes\nu_B),
\qquad
Wf=r^{1/2}f.
\tag{BG15}
$$

Consequently the exact weighted carrier identity is

$$
\boxed{
L^2(\nu)^{G^V}
\cong
\left(
L^2(\nu_A)^{K_A}
\widehat\otimes
L^2(\nu_B)^{K_B}
\right)^{K_\partial}.}
\tag{BG16}
$$

The boundary-charge pairing therefore survives for any faithful finite
Wilson slice density, including a strictly positive Perron ground-state
density. This is only a carrier equivalence. If \(r\neq1\), \(W\) is a
nonfactorizing correlation half-density, sends the constant vector to
\(r^{1/2}\), and does not turn the conditional expectation into product
integration. Explicitly,

$$
\mathbb E_\nu\!\left(f\mid\mathscr F_A\right)(a)
=
\int f(a,b)r(a,b)\,\mathrm d\nu_B(b).
\tag{BG17}
$$

The interacting state and transfer therefore remain in the matrix elements.
If \(r\) vanishes, \(W\) reaches only its support subspace; a singular joint
law need not admit this regional tensorization at all.

If a separator \(S\) contains every interaction crossing the cut and the
Wilson law is conditionally independent across \(A|S|B\), the corresponding
state carrier has a direct-integral form

$$
L^2(\nu)
\cong
\int^{\oplus}
L^2(\nu_{A\mid s})\widehat\otimes
L^2(\nu_{B\mid s})\,
\mathrm d\nu_S(s).
\tag{BG18}
$$

Boundary gauge matching acts fibrewise if the separator variables are
boundary-gauge invariant. For raw separator links the action generally
moves \(s\), relating different fibres; a stabilizer or equivariant
disintegration must then be specified. Without conditional
independence, the canonical conditional-product identification (BG18) is
not available; the appropriate noncommutative
replacement is a correspondence or relative tensor product, with its state
and modular hypotheses stated explicitly.

[[overlap-kernels-and-face-refinement|Overlap kernels and face refinement]]
adds an actual joint-state construction on a supplied finite box: a
comparison law fixes the limiting heat-kernel face weight under exact
boundary integration. This is more than the carrier equivalence (BG16),
but carpet refinement leaves the full four-dimensional continuum and
physical transfer obligations open. Its temporal sewing calculation
also constructs a fixed-spatial-graph clock under explicit anisotropic
scaling and proves that same-weight sharpening on that fixed carrier
has no such clock limit. The refinement law is additional structure,
not a consequence of Gauss gluing.

[[holonomy-refinement-and-clock-compatibility|Holonomy refinement and clock compatibility]]
makes that extra structure quantitative: independent segment rates add
under holonomy pullback, and faithful vacuum dressing does not change
the induced principal form. Mixed link responses can evade that ansatz,
but must still detect closed physical loops; the natural
Ashtekar–Lewandowski response has nonconstant analytic-loop zero modes.
The additive Haar branch instead has a unique vacuum and a constructed
refinement clock whose exact threshold is the least Casimir times the
infimum of weighted cycle lengths. Refinements adding arbitrarily cheap
cycles close that threshold while preserving all old loop clocks.
[[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock|The
induced theta-loop response]] explicitly retains shared-edge mixed terms
without privileging a spanning tree; this repairs coordinate covariance,
not the shrinking-cycle obstruction.

[[heat-state-continuity-and-response-closability|The area-dependent heat-state construction]]
escapes the bounded Haar-density comparison and changes the small-loop
threshold. It also supplies a stronger failure test: consistent finite
perimeter responses need not be closable on the glued state. Nearby
disjoint loops become the same observable in the state norm. If their
energies remain uniformly bounded, a closed replacement must retain
mixed responses across their presentations. Carrier completion is an additional compatibility law,
not a consequence of finite positivity.

[[shared-driver-response-and-the-nested-holonomy-clock|A shared-driver
response]] now realizes that compatibility on the full nested-holonomy
path carrier. Its common driver produces nonzero mixed responses and an
explicit closed clock. The unit Ornstein--Uhlenbeck choice has invariant
threshold two, while a driver intensity approaching zero gives the same
state and gauge symmetry a unique vacuum but no gap. Same-clock annular
restart homogeneity selects constant intensity in this family; deriving
such a response law is distinct from constructing the heat state.
[[path-shift-fisher-geometry-before-gauge-projection|The path-shift Fisher
construction]] selects that response once a handed shift action and
Fisher-dual prescription are declared. Its first-order scores disappear
under prior gauge averaging, even though invariant observable response
does not. The extended presentation must therefore be retained through
the metric-to-operator construction; the state alone does not choose it.

[[two-sided-fisher-completion-and-the-neutral-carrier|The joint two-sided
construction]] computes the cross-score metric before choosing a handed
action. Finite smooth cylinder response forces simultaneous-conjugation
invariance, and the resulting cylinder closure has a unique constant
vacuum with non-attained threshold two. Its complete clock is compatible
with longer path horizons and heat-time reparameterization. It is not
homogeneous under deleting the past and restarting an annulus: that
explicit failure distinguishes a contextual response from the additional
restart law, and the auxiliary threshold from a physical mass.

[[two-sided-fisher-completion-and-the-neutral-carrier#Conditional restart changes both operator and carrier|Conditional rebuilding at a cut]]
restores that restart law only on a separately neutral future carrier.
It excludes a globally neutral endpoint character carrying paired
boundary/future charge. On smooth finite cylinders, requiring the same
separate neutrality through all cuts and refinements leaves only
constants for connected semisimple groups. This makes the charged gluing
requirement operative for the path-response construction itself: changing
the conditional metric must not silently shrink the observable carrier.

[[heat-factor-response-and-the-compression-defect|An independent two-factor source]]
supplies a different response on the same full neutral path carrier.
Its rebuilt clock respects neutral annular restart without discarding
globally paired observations. Full ordered cuts use a derived boundary
conjugation twist in the right response row; the two rows and twist
compose coherently without separately neutralizing either region.
The source clock itself does not descend:
an actual source-chaos component changes along a fiber that fixes the
entire output path. Thus response pullback and dynamical compression
are distinct even in this completely specified group-path example.

[[coarse-response-memory/gauge-star-state-and-hidden-clock|The actual
profile-star test]] separates the static amplitude from this clock
question. A Haar reference realizes the prescribed face integral, but
its specified product diffusion descends to the full framed boundary
only for constant profiles. The computed conditional drift covariance
measures the first dynamical defect. Even a fixed whole boundary state
and reconstructed response can conceal an arbitrarily slow visible
tail. Spatial composition must therefore carry the actual dynamical
readout, not just the integrated density and an independently rebuilt
clock.

## The charged innovation frame

The exact finite-regulator order of operations is now

$$
\boxed{
\begin{gathered}
\text{regional paths with exposed boundary charge}\\
\xrightarrow{\text{regional innovation}}
\text{charged distinction blocks}\\
\xrightarrow{\lambda\otimes\lambda^*\to\mathbf1}
\text{globally closed physical innovations}\\
\xrightarrow{\text{two-slice transfer}}
\text{attenuation matrix}.
\end{gathered}}
\tag{BG19}
$$

This is the useful reversal for the mass-gap programme. The global loop is
not reconstructed from already closed local loops; it is the invariant
pairing of open local carriers. The physical projections can now be made
canonical. Let \(D_i^A,D_j^B\) be boundary-equivariant regional innovation
projections, let \(Z_\lambda^A,Z_{\lambda^*}^B\) be the compact-boundary-group
isotypic projections, and let \(Q_\partial\) project onto diagonal
invariants. Then

$$
E_{ij\lambda}
:=
\left.
Q_\partial
\left[
(D_i^AZ_\lambda^A)
\otimes
(D_j^BZ_{\lambda^*}^B)
\right]
Q_\partial
\right|_{\mathcal H_{\mathrm{GI}}}
\tag{BG20}
$$

are mutually orthogonal physical projections whose strong sum is the
identity. The commutation follows because the selected-coordinate
sigma-algebras are stable under the boundary action and the regional
marginals are invariant. Thus the charge-and-innovation resolution is made
**after** dual-sector gluing without a basis choice.

For an interacting density, however, the product-marginal vacuum is
\(\omega=\sqrt r\), which can have components
\(\omega_{ij\lambda}=E_{ij\lambda}\omega\) in several blocks. Raw
sectorwise centering is then incomplete. The exact repair from
[[vacuum-aligned-innovation-completion/inq|Vacuum-Aligned Innovation
Completion]] is

$$
I-P_\omega
=
Q_{\mathrm{bal}}
+
\sum_{i,j,\lambda}
\left(
E_{ij\lambda}
-
P_{\mathbb C\omega_{ij\lambda}}
\right),
\tag{BG20a}
$$

with the zero-vector convention and
\(Q_{\mathrm{bal}}
=P_{\overline{\operatorname{span}}\{\omega_{ij\lambda}\}}-P_\omega\).
The balance block records centered changes among the vacuum's relative
charge-and-innovation components. It generally mixes cut channels and is
not itself a boundary charge.

The analytic object is therefore a transfer matrix indexed by every nonzero
internal block **and** the balance block. If
\(\Pi_s^X,\Pi_t^Y\) denote these complete vacuum-aligned physical
projections, its typed entries are

$$
c_{st}
:=
\left\|
\Pi_s^{X}
P_T
\Pi_t^{Y}
\right\|,
\tag{BG20b}
$$

and the complete block theorem gives
\(\|P_T|_{\omega^\perp}\|\leq\|(c_{st})\|_{2\to2}\). Raw regional charged
projectors are not operators on the physical whole, and deleting the balance
row can miss the entire centered carrier. The finite carrier construction is
now closed. Proving that this complete matrix is subunit with the required
volume- and continuum-uniform physical rate remains open.

## Where unitarity enters

Neither the edge cut nor Gauss gluing is a clock evolution. The whole datum
in (BG7) is an invariant carrier assembled from complementary presentations,
not a unitary trajectory. Unitarity requires an inner product, an identity
on a declared carrier, and a one-parameter automorphism group. Those become
meaningful only after the quotient or invariant carrier and its clock have
been reconstructed.

The exact ledger is therefore

$$
\boxed{
\text{boundary extension and Gauss gluing}
\neq
\text{conditional forgetting}
\neq
\text{Euclidean attenuation}
\neq
\text{Lorentzian unitary clock}.}
\tag{BG21}
$$

[[conservation-of-causal-charge/unitarity-and-ontological-time|Why
Unitarity Is Not the Wall Symmetry]] supplies the full typing. Strict descent
can glue compatible local data without losing anything; the nonfaithful
quotient, conditional expectation, or factual instrument is an additional
arrow. The Copernican point is not that a globally nonunitary time evolution
causes local unitarity. It is that *unitary/nonunitary* may be an ill-typed
opposition before a represented clock carrier exists, while noninvertible
formation and a later unitary clock law can coexist without contradiction.

## Claim boundary

The theorem proves a whole/part carrier identity and locates a concrete loss
caused by premature regional closure. It does not prove that boundary charge
is ontological information, that Gauss projection actualizes an outcome, or
that a flux label has energy. It does not select \(SU(3)\), spacetime
dimension, a clock, or a dimensional scale. Most importantly, it does not
show that the interacting transfer contracts every paired sector uniformly.
That last same-carrier estimate, with the correct continuum rate and uniform
coverage, is still the mass-gap obligation.

## Sources and receipt

- [[library/remarks-on-entanglement-entropy-for-gauge-fields/inq|Casini--Huerta--Rosabal]] analyze why gauge constraints obstruct regional Hilbert-space factorization, the boundary center, extended constructions, and maximal-tree choices.
- [[library/decomposition-of-entanglement-entropy-in-lattice-gauge-theory/inq|Donnelly]] gives the physical-to-open-region embedding and the dual boundary-representation contraction, including the normalized coevaluation factor.
- [[library/local-subsystems-in-gauge-theory-and-gravity/inq|Donnelly--Freidel]] formulate gluing directly as the diagonal boundary-singlet condition.
- [[library/fusion-basis-for-lattice-gauge-theory-and-loop-quantum-gravity/inq|Delcamp--Dittrich--Riello]] give a representation-theoretic fusion basis supporting hierarchical gluing in a lattice gauge setting.
- [[library/a-new-basis-for-hamiltonian-su-2-simulations/inq|Bauer--D'Andrea--Freytsis--Grabowska]] display maximal-tree loop variables and the nonlocality of the resulting gauge-fixed Hamiltonian.

[[gauge-boundary-frame-gluing/receipts/boundary_charge_gluing_receipt.py|The finite receipt]] checks the theorem for two \(\mathbb Z_2\) links split across one effective boundary action. Each open regional link has trivial and charged components; diagonal gluing retains both the neutral--neutral and charged--charged pairs, whereas closing the two regions separately retains only the first. [[gauge-boundary-frame-gluing/receipts/boundary-charge-gluing-receipt-output.txt|The stored output]] records the dimensions and projection identities.
