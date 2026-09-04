# Oriented Descent, the Two-Wall Angle, and Emergent Symmetry

An asymmetric arrow need not be produced by breaking a prior symmetry: the arrow itself determines a symmetry as the automorphisms that preserve it. When two opposed, state-preserving descents act on one Hilbert carrier, their relative position splits exactly into an orientation-even positive form and orientation-odd ordered data. A positive Friedrichs angle supplies a dimensionless spectral floor; only an independent comparison with the physical Poincaré Casimir and an independent energy yardstick can turn that floor into a Yang--Mills mass gap.

**Status: [EXACT ARROW-STABILIZER AND TWO-PROJECTION THEOREMS]; [EXACT STANDARD-FORM REALIZATION UNDER TAKESAKI'S HYPOTHESES]; [CONDITIONAL CASIMIR-GAP THEOREM]; [CANDIDATE ASYMMETRY-FIRST INTERPRETATION]; [OPEN YANG--MILLS CONSTRUCTION].**

## The arrow is prior to its symmetry

Let

$$
W:X_-\longrightarrow X_+
\tag{OD1}
$$

be an oriented realization arrow in a concrete category. It need not be invertible. Its intrinsic symmetry is

$$
\boxed{
\operatorname{Aut}(W)
:=
\left\{
(u_-,u_+)\in
\operatorname{Aut}(X_-)\times\operatorname{Aut}(X_+):
u_+W=Wu_-
\right\}.}
\tag{OD2}
$$

The arrow is logically prior in this definition. Symmetry is the group of presentation changes that preserve the asymmetric relation. Nothing in (OD2) selects \(SU(2)\), \(SU(3)\), or any other group in advance.

When \(X_\pm\) are Hilbert spaces, \(W\) is bounded, and a group \(G\) is independently represented by unitaries \(u_\pm(g)\), let \(G\) act on the bounded-arrow space by

$$
g\cdot T:=u_+(g)Tu_-(g)^*.
\tag{OD3}
$$

The equivariance defect

$$
\beta_W(g):=g\cdot W-W
\tag{OD4}
$$

obeys the affine cocycle identity

$$
\boxed{
\beta_W(gh)=g\cdot\beta_W(h)+\beta_W(g).}
\tag{OD5}
$$

Its zero set is the stabilizer

$$
G_W=\{g\in G:\beta_W(g)=0\}.
\tag{OD6}
$$

Here \(\beta_W\) is a coboundary, so its cohomology class is not a new conserved charge. Its value measures failure of equivariance. For norm-differentiable representations, or on a common invariant smooth-vector core for strongly continuous representations,

$$
\dot\beta_W(\xi)
=\mathrm du_+(\xi)W-W\,\mathrm du_-(\xi).
\tag{OD7}
$$

This is the group-direction analogue of the scale-direction defect in [[wall-crossing-defect-and-the-fossil-of-mass-engagement]]. The two may be components of a connection on a bundle of arrow spaces; neither is automatically an energy operator.

When \(X_\pm\) are Hilbert spaces and \(W:X_-\to X_+\) is bounded and Fredholm, there is an exact conservation-like datum:

$$
\operatorname{ind}W
:=
\dim\ker W-\dim\ker W^*.
\tag{OD8}
$$

For unitary presentation changes,

$$
\operatorname{ind}\!\left(u_+Wu_-^*\right)
=\operatorname{ind}W,
\tag{OD9}
$$

and the index is constant along every norm-continuous path that remains Fredholm. The representative defect \(\beta_W\), the stabilizer \(G_W\), and a metric Hessian may vary while this integer persists. For a graded Fredholm Dirac arrow \(D^+:\mathcal H^+\to\mathcal H^-\), the same index records oriented chiral imbalance. This is a precise candidate for conservation *across* changing symmetry and asymmetry: the persistent object is a relative class of the arrow, not a Noether charge generated inside one already symmetric phase.

[[order-three-orientation-and-the-exceptional-stabilizer]] is now an exact exceptional instance of this reversal. Yokota's oriented operation \(w\in F_4\) has connected symmetry \(C_{F_4}(w)\), adjoining the pointed idempotent \(\ell\) reduces that symmetry to \(S(U(2)\times U(3))\), and the cyclic average \((1+w+w^2)/3\) forgets the distinction \(w\leftrightarrow w^{-1}\). The reversal-odd residue \((w-w^2)/\sqrt3\) is a complex structure on the forgotten complement. Thus the observed group is literally the stabilizer of prior oriented algebraic data. [[exceptional-normal-holonomy-and-the-residual-gauge-form]] then shows why this kinematic success is not yet a mass gap: the intrinsic flag normal is not a faithful module for the surviving group, and the faithful full normal must be promoted to a field-valued physical response before any coercivity theorem applies.

## The whole carries two opposed descents

Let \(\mathcal M\) be a von Neumann algebra with faithful normal state \(\varphi\), represented on its GNS-standard Hilbert space

$$
\mathcal H_\varphi=L^2(\mathcal M,\varphi),
\qquad
\Omega_\varphi\in\mathcal H_\varphi.
\tag{OD10}
$$

Suppose two von Neumann subalgebras \(\mathcal N_\pm\subseteq\mathcal M\) admit \(\varphi\)-preserving normal conditional expectations

$$
E_\pm:\mathcal M\longrightarrow\mathcal N_\pm,
\qquad
\varphi\circ E_\pm=\varphi.
\tag{OD11}
$$

Takesaki's theorem makes the existence gate exact: there is a unique \(\varphi\)-preserving normal conditional expectation onto \(\mathcal N_\pm\) if and only if

$$
\sigma_t^\varphi(\mathcal N_\pm)=\mathcal N_\pm
\quad\text{for every }t\in\mathbb R.
\tag{OD11a}
$$

Each expectation extends from the GNS core to an orthogonal projection

$$
e_\pm(a\Omega_\varphi)
=E_\pm(a)\Omega_\varphi
\tag{OD12}
$$

with range \(\overline{\mathcal N_\pm\Omega_\varphi}\). No trace or density matrix is required, so this Hilbert-space construction is compatible with type-III algebras.

Let \(P_0\) be the orthogonal projection onto the common retained subspace:

$$
P_0\mathcal H_\varphi
=e_+\mathcal H_\varphi\cap e_-\mathcal H_\varphi.
\tag{OD13}
$$

The desired completeness condition for a mass-gap application is

$$
P_0
=|\Omega_\varphi\rangle\langle\Omega_\varphi|.
\tag{OD14}
$$

It must be proved, not obtained by appending a tautological expectation onto \(\mathbb C1\). Under the Reeh--Schlieder hypotheses recorded in [[causal-frame-coercivity]], ordinary nested local AQFT algebras cannot furnish a nontrivial vacuum-preserving expectation tower of this form. Regulator blocks, split collars, comparison cores, or another nonlocal whole--part carrier are required.

## Exact two-wall angle theorem

Because \(P_0\leq e_\pm\), the reduced operators

$$
p:=e_+-P_0,
\qquad
q:=e_--P_0
\tag{OD15}
$$

are orthogonal projections on \((1-P_0)\mathcal H_\varphi\) with zero common range. Their Friedrichs cosine is

$$
c_F:=\|pq\|\in[0,1].
\tag{OD16}
$$

The two descent defects form the analysis operator

$$
\mathfrak D_{\mathrm{pair}}f
:=
\bigl((1-e_+)f,(1-e_-)f\bigr)
\in\mathcal H_\varphi\oplus\mathcal H_\varphi.
\tag{OD17}
$$

Its positive frame operator and quadratic form are

$$
\boxed{
G_{\mathrm{pair}}
:=\mathfrak D_{\mathrm{pair}}^*
\mathfrak D_{\mathrm{pair}}
=2I-e_+-e_-,
}
\tag{OD18}
$$

$$
q_{\mathrm{pair}}[f]
=\|(1-e_+)f\|^2+\|(1-e_-)f\|^2.
\tag{OD19}
$$

The kernel is exactly the common retained subspace:

$$
\ker G_{\mathrm{pair}}
=e_+\mathcal H_\varphi\cap e_-\mathcal H_\varphi
=P_0\mathcal H_\varphi.
\tag{OD20}
$$

On its orthogonal complement,

$$
G_{\mathrm{pair}}=2I-p-q.
\tag{OD21}
$$

For a nonzero reduced pair, the two-projection norm identity gives

$$
\|p+q\|=1+\|pq\|=1+c_F.
\tag{OD22}
$$

Consequently,

$$
\boxed{
q_{\mathrm{pair}}[f]
\geq
(1-c_F)\|f\|^2,
\qquad
f\perp P_0\mathcal H_\varphi.}
\tag{OD23}
$$

The constant is optimal whenever at least one reduced range is nonzero. If \(p=q=0\), then \(G_{\mathrm{pair}}=2I\) on \((1-P_0)\mathcal H_\varphi\); when that complement is zero, any statement about an optimal positive constant is vacuous. For a nonzero reduced pair, the following are equivalent:

$$
\begin{aligned}
c_F&<1,\\
\operatorname{Ran}p+\operatorname{Ran}q
&\text{ is closed},\\
G_{\mathrm{pair}}\!\restriction_{(1-P_0)\mathcal H_\varphi}
&\text{ has a positive lower edge}.
\end{aligned}
\tag{OD24}
$$

This is an exact geometric meaning of distinction. Each retained presentation may contain arbitrarily many directions. The positive floor is the uniform impossibility of approaching both presentations at once without approaching their common core.

It is also a precise whole--part meaning of *relative scale*. A single nontrivial orthogonal projection has only the spectrum \(\{0,1\}\) and carries no principal angle by itself. The pair carries \(c_F\). Under every simultaneous unitary change of presentation,

$$
e_\pm\longmapsto Ue_\pm U^*,
\qquad
P_0\longmapsto UP_0U^*,
\tag{OD24a}
$$

one has

$$
G_{\mathrm{pair}}\longmapsto UG_{\mathrm{pair}}U^*,
\qquad
c_F\longmapsto c_F.
\tag{OD24b}
$$

Thus the construction does not assign an absolute ruler to the whole. It assigns a dimensionless invariant to the relative placement of two partial presentations inside the whole. The physical unit enters only through the later kinetic/Casimir solder.

[[library/the-friedrichs-angle-and-alternating-projections-in-hilbert-c-star-modules/inq|Mesland and Rennie]] prove the corresponding closed-sum and alternating-projection structure for complemented Hilbert-\(C^*\)-submodules. Equation (OD23) is the Hilbert-space specialization used here.

## The positive shadow forgets order

The ordered products

$$
T_{\rightarrow}:=pq,
\qquad
T_{\leftarrow}:=qp=T_{\rightarrow}^*
\tag{OD25}
$$

are generally different. Their positive alternating operator

$$
K_{\mathrm{alt}}:=qpq
\tag{OD26}
$$

obeys

$$
\|K_{\mathrm{alt}}\|=\|pq\|^2=c_F^2.
\tag{OD27}
$$

Thus \(c_F<1\) is also strict contraction of alternating descent away from the common core. The iteration count is dimensionless, and \(c_F^2\) is the worst-case contraction factor per \(qpq\) cycle. Calling the iteration parameter physical time requires an independent transfer or modular-time identification.

[[past-future-angle-and-the-transfer-gap]] realizes that identification exactly in a stationary reversible Markov--Osterwalder--Schrader path space, but only for **disjoint** half-spaces separated by a positive Euclidean slab. There, \(c_F\) is the normalized transfer contraction across the slab, while the supported modulus \(|pq|\) is the endpoint transfer itself. The logarithm of \(|pq|\) per calibrated slab thickness recovers the clock Hamiltonian. Touching halves share the entire time-zero carrier and do not encode the gap in their reduced Friedrichs angle.

The bounded self-adjoint orientation operator

$$
\boxed{
\Omega_{\mathrm{ord}}
:=\frac{1}{2i}[e_+,e_-]
}
\tag{OD28}
$$

changes sign under \(+\leftrightarrow-\), whereas \(G_{\mathrm{pair}}\) is unchanged:

$$
\begin{array}{c|c|c}
\text{component}&\text{under reversal}&\text{role}\\
\hline
G_{\mathrm{pair}}&\text{even}&\text{symmetric distinction form}\\
\Omega_{\mathrm{ord}}&\text{odd}&\text{orientation witness}.
\end{array}
\tag{OD29}
$$

A positive angle does not require a nonzero orientation operator: orthogonal descents have \(c_F=0\) and commute. Conversely, a nonzero commutator does not force \(c_F<1\) uniformly in an infinite system. Chirality and coercivity can inhabit one ordered carrier without being the same concept.

The primitive datum may therefore be the ordered pair \((E_+,E_-)\). Its observable symmetry is the derived stabilizer

$$
\operatorname{Aut}(\mathcal M,\varphi;E_+,E_-)
:=
\left\{
\alpha\in\operatorname{Aut}(\mathcal M):
\varphi\circ\alpha=\varphi,
E_\pm\alpha=\alpha E_\pm
\right\}.
\tag{OD30}
$$

Exchanging the descents is an additional symmetry only if a separate intertwiner proves it.

This reverses the question but does not answer it automatically. A generic completed arrow may have trivial stabilizer, while a bare projection has the enormous stabilizer \(U(\operatorname{Ran}e)\times U(\ker e)\). Neither fact resembles the observed internal symmetries by itself. The object whose symmetry is physically relevant must include all structure that is claimed to be preserved, schematically

$$
\mathbb W
=
\bigl(
\mathcal A_\pm,\varphi_\pm,
E_\pm,J_\sigma,A_\pm,
\Gamma,\text{regional maps}
\bigr),
\tag{OD30a}
$$

and the candidate observed group is the common stabilizer \(\operatorname{Aut}(\mathbb W)\), not the stabilizer of one conveniently chosen component. A reconstruction may instead require the full tensor category of sectors or correspondences. [[symmetry-groups-select/inq|Selecting internal symmetry from causal-scale structure]] owns that stronger obligation. The present mass-gap mechanism is intentionally group neutral: it could apply memberwise to a supplied compact simple gauge group without claiming to derive the Standard Model group.

## Complex phase does not supply the modulus; Jordan idempotency supplies a normal one

The imaginary unit can retain orientation without producing the positive floor. If \(M,N\) are closed subspaces of a real Hilbert space and \(M_{\mathbb C},N_{\mathbb C}\) are their complexifications, then their projections complexify and

$$
c_F(M_{\mathbb C},N_{\mathbb C})
=c_F(M,N).
\tag{OD30b}
$$

Likewise, left multiplication of \(pq\) by a unitary changes its polar presentation but preserves \((pq)^*(pq)\), its norm, and its gap rate. [[phase-modulus-pointing-and-euclidean-dwell]] develops the exact division of labor: \(i\) and the polar partial isometry carry an oriented grammar; the positive modulus carries attenuation; an obtained character supplies a fact. A phase or chirality label can affect the modulus only through a separately constructed dynamical coupling or coherent sum.

The compact exceptional Jordan algebra gives an exact finite witness for symmetry after a selection. For

$$
J=\mathfrak h_3(\mathbb O),
\qquad
X\cong\mathfrak h_2(\mathbb C)
\subset
B\cong\mathfrak h_3(\mathbb C)
\subset J,
\tag{OD30c}
$$

the simultaneous stabilizer in the theorem recorded by [[library/standard-model-from-exceptional-jordan-algebra/inq]] is

$$
\operatorname{Stab}(X)\cap\operatorname{Stab}(B)_0
\cong
S(U(2)\times U(3))
\cong
\frac{U(1)\times SU(2)\times SU(3)}{\mathbb Z_6}.
\tag{OD30d}
$$

The familiar group is therefore the symmetry of a selected complex flag in an exceptional whole, not the premise from which that selection must be broken. This proves an order-of-explanation precedent, not that this flag is nature's carrier or that it supplies the Yang--Mills Hamiltonian.

[[jordan-idempotency-and-the-stabilizer-gap]] adds a positive operator that was missing from the earlier audit. In any Euclidean Jordan algebra, let

$$
C(x)=x\circ x-x,
\qquad
V(x)=\frac12\lVert C(x)\rVert^2.
\tag{OD30d1}
$$

At an idempotent \(e\), Peirce decomposition gives

$$
\boxed{
\operatorname{Hess}_eV
=
(2L_e-I)^2
=
I-P_{1/2}.}
\tag{OD30d2}
$$

Its kernel is exactly the tangent space of the fixed-rank idempotent orbit, while its normal complement has unit edge in the canonical dimensionless convention. For a primitive idempotent in \(\mathfrak h_3(\mathbb O)\), this gives multiplicities \(0^{(16)}\) and \(1^{(11)}\). Thus the exceptional product can generate both a presentation orbit with a stabilizer and a positive transverse response; one need not append a gauge group and a quadratic cost as unrelated inputs.

There is now an exact bridge between those two facts. The selected-flag
stabilizer preserves the Jordan product, the trace form, the idempotent, and
hence the Hessian and its radical. It therefore induces an orthogonal
representation on the normal quotient. This is a finite exceptional instance
of [[algebra/quotient-unitarity-and-kernel-stabilization|quotient unitarity by
kernel stabilization]]: the familiar unitary factors act after selection as
symmetries of the retained response. The theorem neither proves that this
quotient is the physical Hilbert carrier nor that its unit normal edge is an
energy gap.

The direction of this Hessian is also its most important limitation. It penalizes leaving the valid idempotent locus. If physical Yang--Mills excitations instead live tangent to a space of valid fields, the Jordan Hessian is a constraint-violation stiffness and misses precisely the physical sector. A recovery theorem must therefore construct a flag field or analysis map whose **normal response covers every gauge-invariant nonvacuum direction**, and compare that response with the OS Hamiltonian form. Without that carrier-and-coverage theorem, the normal edge is not a mass edge.

Two Jordan walls must remain separate. For a Jordan-frame spectrum \((\lambda_1,\lambda_2,\lambda_3)\),

$$
\Delta_J=\prod_{i<j}(\lambda_i-\lambda_j)^2=0
\tag{OD30e}
$$

is the spectral-discriminant wall of eigenframe ambiguity and stabilizer enhancement, whereas

$$
N_J=\lambda_1\lambda_2\lambda_3=0
\tag{OD30f}
$$

is the determinant wall of rank loss. Neither implies the other: \(\operatorname{diag}(1,1,2)\) lies only on the first, while \(\operatorname{diag}(1,2,0)\) lies only on the second. The \(A_2\) cusp, Jordan-rank transition, idempotency-defect normal edge, black-hole entropy dictionary, and physical mass gap are consequently five different claims. [[inbox/black-holes-as-jordan-spectra/black-holes-as-jordan-spectra]] is a useful presentation-versus-invariant model, but it contains no slab semigroup or all-physical-direction coercive modulus.

## Exact flux witness

The same even--odd split occurs in a finite loop algebra. Let \(N\geq2\) and let \(U,V\in M_N(\mathbb C)\) be the irreducible clock and shift unitaries satisfying

$$
UV=\omega VU,
\qquad
\omega=e^{2\pi i/N}.
\tag{OD31}
$$

The phase is oriented: reversing the linking orientation conjugates \(\omega\). On the Hilbert--Schmidt carrier define

$$
\delta_{UV}(X)
:=
\bigl([U,X],[V,X]\bigr),
\tag{OD32}
$$

$$
q_{UV}[X]
:=
\|[U,X]\|_2^2+\|[V,X]\|_2^2.
\tag{OD33}
$$

The Weyl basis \(U^aV^b\), \(a,b\in\mathbb Z_N\), diagonalizes the quadratic form:

$$
\boxed{
\frac{q_{UV}[U^aV^b]}
{\|U^aV^b\|_2^2}
=
4\left(
\sin^2\frac{\pi a}{N}
+
\sin^2\frac{\pi b}{N}
\right).}
\tag{OD34}
$$

Therefore,

$$
\ker\delta_{UV}=\mathbb C1,
\qquad
\boxed{
q_{UV}[X]
\geq
4\sin^2\frac{\pi}{N}\,\|X\|_2^2,
\quad
\operatorname{Tr}X=0.}
\tag{OD35}
$$

Orientation reversal changes the directed commutation phase but leaves the positive floor unchanged. This is an exact finite witness of the grammar

$$
\text{oriented asymmetric relation}
\longrightarrow
\text{orientation-even positive shadow}.
\tag{OD36}
$$

[[library/reading-between-the-lines-of-four-dimensional-gauge-theories/inq|Aharony, Seiberg, and Tachikawa]] supply the physical charge-space precedent: electric and magnetic line classes carry an alternating mutual-locality pairing, and a local theory selects a maximal mutually local set. [[library/entropic-order-parameters-for-the-phases-of-qft/inq|Casini, Huerta, Magán, and Pontello]] supply the complementary-algebra precedent in which Wilson and 't Hooft class expectations obey an entropic certainty relation.

The matrix witness does not place mutually nonlocal line operators in one local observable algebra. It represents their relative algebra on a comparison carrier. Its floor is not a Yang--Mills mass gap: \(4\sin^2(\pi/N)\to0\) as \(N\to\infty\); trivial-center groups supply no nontrivial center-flux Weyl pair by this mechanism; finite center data do not control every topologically trivial excitation; and (OD35) supplies neither a physical rate nor an energy scale. Its legitimate role is to seed the noncommuting response in [[compensated-incidence-response-and-four-dimensional-balance]], where a regulator-uniform scale law and a physical solder are still required.

## A non-arbitrary metric for the wall defect

The wall-crossing defect

$$
\mathfrak D_\sigma
=J_\sigma'+J_\sigma A_--A_+J_\sigma
\tag{OD37}
$$

is generally rectangular and has no positivity order. If its output lies in \(\mathcal H_\varphi\), the opposed descents provide a geometrically selected positive pullback:

$$
q_{\mathrm{wall}}[x]
:=
\left\|
\mathfrak D_{\mathrm{pair}}
(1-P_0)\mathfrak D_\sigma x
\right\|^2.
\tag{OD38}
$$

Equation (OD23) gives

$$
q_{\mathrm{wall}}[x]
\geq
(1-c_F)
\|(1-P_0)\mathfrak D_\sigma x\|^2.
\tag{OD39}
$$

This supplies a non-arbitrary candidate for the previously open post-wall metric \(G_+\). It still does not give a lower bound in the incoming norm. That stronger result requires injectivity modulo the declared null space together with closed range for the restricted map \((1-P_0)\mathfrak D_\sigma\), equivalently a positive lower singular value on the orthogonal complement of that null space. A wall can be transverse after it acts while remaining blind to many incoming directions.

## Conditional mass-gap theorem

Suppose the post-wall carrier has already been identified with a positive-energy Hilbert space, and suppose the intersection projection \(P_0\) from (OD13) is exactly the projection onto its unique joint-translation-invariant vacuum. Let the nonnegative Poincaré Casimir be

$$
\mathcal C=H^2-c^2|\mathbf P|^2.
\tag{OD40}
$$

Let \(E_*>0\) be an independently fixed energy scale. Assume the descents were constructed without using the spectrum of \(\mathcal C\), \(c_F<1\), and the dynamics proves the same-carrier quadratic-form comparison

$$
\frac{\mathcal C}{E_*^2}
\geq
\eta_{\mathrm{sol}}G_{\mathrm{pair}},
\qquad
\eta_{\mathrm{sol}}>0,
\tag{OD41}
$$

on the quadratic-form domain \(D(\mathcal C^{1/2})\). Then

$$
\boxed{
\mathcal C
\geq
E_*^2\eta_{\mathrm{sol}}(1-c_F)(1-P_0).}
\tag{OD42}
$$

Under the Poincaré reconstruction hypotheses in [[joint-causal-generators-and-the-mass-casimir]], \(0\leq\mathcal C\leq H^2\), so this implies

$$
\boxed{
\Delta_E
\geq
E_*\sqrt{\eta_{\mathrm{sol}}(1-c_F)}.}
\tag{OD43}
$$

The theorem separates three returns:

1. \(1-c_F\) is the dimensionless geometric separation of the descents;
2. \(\eta_{\mathrm{sol}}\) compares that geometry with physical translation cost; and
3. \(E_*\) supplies the dimensional yardstick.

None can be manufactured from the other two. In pure Yang--Mills, \(E_*\) must arise from the renormalized coupling and dimensional transmutation, or from an equivalent noncircular normalization. A cosmological combination of \(G\), \(H\), \(c\), and \(\hbar\) may define a separate common-origin proposal, but it cannot replace the gravity-independent construction required for every compact simple gauge group.

There is no legitimate finite-lattice Poincaré-Casimir solder. At a regulator one must first compare the geometric form with the Osterwalder--Schrader or transfer-Hamiltonian energy form on the same carrier. The Casimir statement becomes available only after continuum locality and Poincaré covariance have been reconstructed.

For the canonical separated past--future pair, (OD41) is not the natural finite-regulator comparison. The whole operator \(G_{\mathrm{pair}}\) is neither \(H\) nor \(H^2\). Instead, after compression to the correlated endpoint support,

$$
J_\ell^0H_T(J_\ell^0)^*
=
-\frac{\hbar c}{2\ell}
\log\!\left(
(qpq)\big|_{s(qpq)\mathcal H}
\right),
\tag{OD43a}
$$

where \(\ell\) is the actual Euclidean slab length and \(J_\ell^0\) is the centered endpoint isometry of [[past-future-angle-and-the-transfer-gap]]. This is an exact logarithmic solder on the supported correlated endpoint carrier when the Markov and transfer hypotheses hold. It also shows why a regulator-independent coefficient in (OD41) should not be expected for adjacent slices: the raw frame edge is first order in \(\ell\), while the logarithmic rate remains finite.

## Mass engagement as a calibrated angle rate

For a regulated scale-ordered family, do not let the regulator label and the separation label collapse into one symbol. Write

$$
\kappa_{\mathrm{ang},r}(\ell)
:=1-c_{F,r}(\ell),
\qquad
\gamma_{\mathrm{ang},r}(\ell)
:=-\frac{1}{\ell}\log c_{F,r}(\ell),
\tag{OD44}
$$

A raw regulator-uniform transversality estimate is legitimate when the descents remain separated by a fixed positive physical thickness \(\ell_*\):

$$
\inf_{r\in I_{\mathrm{post}}}
\kappa_{\mathrm{ang},r}(\ell_*)>0.
\tag{OD45}
$$

For adjacent regulator slices with \(\ell=a_r\to0\), the correct certificate is instead

$$
\inf_{r\in I_{\mathrm{post}}}
\gamma_{\mathrm{ang},r}(a_r)>0.
\tag{OD45a}
$$

In a theory with a finite clock gap, \(c_{F,r}(a_r)\to1\) and \(1-c_{F,r}(a_r)\sim a_r\Delta_E/(\hbar c)\). Thus raw asymptotic coincidence at one shrinking step is not an upstream signature of masslessness; it is also the ordinary short-distance behavior of a massive continuum theory. The wall must be a change in the **calibrated logarithmic rate**, or in a fixed-thickness relative position, not merely a change in an uncalibrated angle.

Equations (OD45) and (OD45a) are proof certificates, not necessarily a thermodynamic phase transition. Identifying their wall address with the causal grain requires construction of the scale functor, persistence through the continuum limit, and a downstream cosmological response. A BAO or CMB match cannot define the family retroactively.

## What twisted spectral geometry contributes

For a twisted spectral triple, the ordinary commutator is replaced by

$$
[D,a]_\rho:=Da-\rho(a)D.
\tag{OD46}
$$

[[library/type-iii-and-spectral-triples/inq|Connes and Moscovici]] show that twisted commutators admit natural type-III examples and, for finitely summable twisted triples, still support a cyclic-cohomology Chern character and an index pairing with \(K\)-theory. This is important for the inversion proposed here: a twist can modify the local metric presentation while a more stable index class persists. The twist \(\rho\) is nevertheless invertible and supplies neither (OD23) nor (OD41).

When a nontrivial normal involutive \(*\)-automorphism \(\rho\) acts on a von Neumann algebra, the map

$$
E_\rho=\frac{1+\rho}{2}
\tag{OD47}
$$

is a genuinely noninvertible conditional expectation onto the fixed algebra. [[spectral-wall-descent/twist-fixed-point-wall]] studies this project-level extraction. Read upside down, the observable symmetry is the invariant shadow retained by a descent; it need not be an ontologically prior symmetry that was later broken.

[[library/lorentz-signature-and-twisted-spectral-triples/inq|Devastato, Farnsworth, Lizzi, and Martinetti]] obtain a Krein structure and Wick-rotation relation in their specific minimal-twist/Standard-Model setting after a spectral triple has been supplied. This is a rigorous model showing that a twist can encode Lorentzian-signature structure; it is not a theorem for arbitrary twists. It does not by itself produce irreversible order, a stable record, or the positive-energy translation generator.

Likewise, the modular flow in [[library/von-neumann-algebra-automorphisms-and-the-time-thermodynamics-relation/inq|Connes and Rovelli]] is a reversible automorphism group selected by a faithful state; Connes cocycle equivalence makes its class state independent in the outer automorphism group. It is a possible source of relational clock flow. Noninvertible descent and record order are additional structures. Ontological order, modular parameter, Euclidean preparation depth, and laboratory clock time must not be denoted by one variable until an explicit intertwiner identifies them.

## Why the spectral action cannot choose the primitive arrow

For the usual even test function in [[library/the-spectral-action-principle/inq|the spectral action]],

$$
S_\Lambda(D)=\operatorname{Tr}f(D/\Lambda)
\tag{OD48}
$$

obeys, whenever the trace is defined,

$$
S_\Lambda(UDU^*)=S_\Lambda(D),
\qquad
S_\Lambda(-D)=S_\Lambda(D).
\tag{OD49}
$$

It is blind to unitary presentation and to the bare sign orientation of \(D\). It can assign dynamics to already represented fluctuations, but it cannot alone explain why one oriented descent rather than its reversal is factual. A grading, real structure, boundary condition, index pairing, fermionic action, or record process must retain the missing orientation.

If \(W_s\) is a norm-continuous Fredholm family, its index is invariant while its representative and stabilizer may vary. An index jump requires leaving that continuous Fredholm family or changing the carrier or domain. A self-adjoint Fredholm path may separately possess nonzero spectral flow as discrete eigenvalues cross zero while the essential gap remains open; spectral flow is not an index jump of one fixed Fredholm arrow.

If \(D\) is odd on a graded carrier, \(D^+\) is Fredholm, and \(e^{-tD^2}\) is trace class under the required summability or ellipticity hypotheses, the ungraded spectral trace and the graded index trace retain different information:

$$
\operatorname{Tr}f(D^2/\Lambda^2)
\quad\text{is chirality even},
\qquad
\operatorname{Str}e^{-tD^2}
=\operatorname{ind}D^+.
\tag{OD50}
$$

An ungraded spectral action may encode symmetric metric response while the grading and index retain oriented imbalance. Treating the first as the origin of the second reverses the dependency. Index invariance itself still supplies no positive energy floor.

## Knots and flux are possible channels, not the mass

Linked Wilson--'t Hooft channels may enlarge a physically constructed family of descents or reduce a common blind subspace. Their relevant contribution would not be that a knot *is* a mass, but that opposed loop channels help prove

$$
e_+\mathcal H\cap e_-\mathcal H=\mathbb C\Omega,
\qquad
c_F(\ell_*)<1
\tag{OD51}
$$

on the full physical carrier at a declared positive separation \(\ell_*\). Center one-form symmetry labels only some sectors and is trivial for some compact simple groups, so it cannot be the universal origin of the Clay gap. Any knot contribution must control the topologically trivial sector as well.

## Promotion and kill conditions

The asymmetry-first route advances only if it constructs:

1. a primitive ordered pair of descents from gauge, boundary, modular, or RG geometry without using an observed mass;
2. a common Hilbert carrier and the required state-preserving maps;
3. the exact common fixed space and either a regulator-uniform estimate \(c_{F,r}(\ell_*)\leq1-\kappa\) at fixed positive thickness or a regulator-uniform lower bound on \(-\ell^{-1}\log c_{F,r}(\ell)\);
4. reversal-sensitive data that survives rather than disappearing in the positive shadow;
5. on each regulator, a domain-correct comparison with the physical transfer-Hamiltonian form;
6. vacuum-controlled convergence to a local Poincaré-covariant continuum theory;
7. only then, the Casimir comparison (OD41) and an independent physical yardstick.

The route is killed or downgraded if the symmetry group is inserted before the arrow and then announced as derived; if \(E_\pm\) are tautological expectations onto scalars; if touching Euclidean halves are treated as a vacuum-only pair despite their shared time-zero carrier; if \(c_F<1\) follows only after a spectral cutoff selected from the desired gap; if a raw adjacent-slice angle is required to stay uniformly open as the spacing vanishes; if complexification or a unitary phase is claimed to change the positive modulus; if the Jordan discriminant, rank wall, and idempotency Hessian are conflated; if the normal Hessian is called a physical gap without a coverage theorem; if a twist or index is called an energy; if a Markov, modular, RG, or record-order generator is silently identified with the clock Hamiltonian; if the spectral action is asked to choose temporal orientation; or if a cosmological yardstick replaces rather than supplements the gravity-free Yang--Mills scale theorem.

The Copernican statement is therefore exact but conditional in its physical application:

> Symmetry may be the automorphism shadow of a prior asymmetric descent. Its orientation-even relative-position form can possess a dimensionless lower edge, but that edge becomes mass only after a noncircular comparison with physical translation energy.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/oriented_descent_angle_receipt.py|The finite receipt]] checks the two-dimensional principal-angle spectrum, alternating contraction, reversal parity of the orientation operator, and finite Weyl-pair floor; [[contemporary-puzzles/yang-mills-mass-gap/receipts/oriented-descent-angle-receipt-output.txt|the stored output]] records the run. It is a finite witness, not a type-III, continuum, or Yang--Mills construction.
