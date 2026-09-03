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
\varphi\circ\alpha=\varphi,\ 
E_\pm\alpha=\alpha E_\pm
\right\}.
\tag{OD30}
$$

Exchanging the descents is an additional symmetry only if a separate intertwiner proves it.

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

on the form domain of \(\mathcal C\). Then

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

## Mass engagement as loss of asymptotic coincidence

For a scale-ordered family \((E_{+,N},E_{-,N})\), define

$$
\kappa_{\mathrm{ang}}(N):=1-c_F(N).
\tag{OD44}
$$

A theorem-shaped meaning of “mass engaged” is a regulator-uniform post-wall transversality estimate

$$
\inf_{N\in I_{\mathrm{post}}}
\kappa_{\mathrm{ang}}(N)>0,
\tag{OD45}
$$

while upstream the realized pair is absent or \(c_F(N)\to1\). The wall is then a change in the relative position of two whole--part presentations: beyond it, a nonvacuum direction cannot masquerade indefinitely as compatible with both.

Equation (OD45) is a proof certificate, not necessarily a thermodynamic phase transition. Identifying its wall address with the causal grain requires construction of the scale functor, persistence through the continuum limit, and a downstream cosmological response. A BAO or CMB match cannot define the family retroactively.

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

For the usual even spectral-action test function,

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
c_F<1
\tag{OD51}
$$

on the full physical carrier. Center one-form symmetry labels only some sectors and is trivial for some compact simple groups, so it cannot be the universal origin of the Clay gap. Any knot contribution must control the topologically trivial sector as well.

## Promotion and kill conditions

The asymmetry-first route advances only if it constructs:

1. a primitive ordered pair of descents from gauge, boundary, modular, or RG geometry without using an observed mass;
2. a common Hilbert carrier and the required state-preserving maps;
3. the exact common fixed space and a regulator-uniform estimate \(c_F\leq1-\kappa\);
4. reversal-sensitive data that survives rather than disappearing in the positive shadow;
5. on each regulator, a domain-correct comparison with the physical transfer-Hamiltonian form;
6. vacuum-controlled convergence to a local Poincaré-covariant continuum theory;
7. only then, the Casimir comparison (OD41) and an independent physical yardstick.

The route is killed or downgraded if the symmetry group is inserted before the arrow and then announced as derived; if \(E_\pm\) are tautological expectations onto scalars; if \(c_F<1\) follows only after a spectral cutoff selected from the desired gap; if a twist or index is called an energy; if a Markov, modular, RG, or record-order generator is silently identified with the clock Hamiltonian; if the spectral action is asked to choose temporal orientation; or if a cosmological yardstick replaces rather than supplements the gravity-free Yang--Mills scale theorem.

The Copernican statement is therefore exact but conditional in its physical application:

> Symmetry may be the automorphism shadow of a prior asymmetric descent. Its orientation-even relative-position form can possess a dimensionless lower edge, but that edge becomes mass only after a noncircular comparison with physical translation energy.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/oriented_descent_angle_receipt.py|The finite receipt]] checks the two-dimensional principal-angle spectrum, alternating contraction, reversal parity of the orientation operator, and finite Weyl-pair floor; [[contemporary-puzzles/yang-mills-mass-gap/receipts/oriented-descent-angle-receipt-output.txt|the stored output]] records the run. It is a finite witness, not a type-III, continuum, or Yang--Mills construction.
