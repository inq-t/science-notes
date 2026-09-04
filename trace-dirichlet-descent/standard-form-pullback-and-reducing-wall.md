# Standard-Form Pullback and the Reducing Wall

A local state is obtained covariantly by restriction along a normal unital
\(*\)-monomorphism, while a local observable moves contravariantly into the
whole algebra.  If that observable inclusion is expected relative to the
reference state, then its standard-form isometry preserves the real structure
and every amplified Markov interval.  Restricting a closed completely
Dirichlet whole form along this isometry is therefore again closed and
completely Dirichlet.  This safe pullback agrees with the infimal quotient only
under the additional reducing, or lumpability, condition; the six-vertex
counterexample proves that expectation alone cannot replace that condition.

**Status: [EXACT CONSEQUENCE] for the pullback theorem and reducing-wall
identity under the hypotheses below; [EXACT NO-GO] for arbitrary infimal
pushforward through a conditional expectation; [CONDITIONAL APPLICATION] for
the Yang--Mills carrier.**  The pullback theorem is a direct standard-form
argument assembled from the Markov-interval definition and the projection
identities for an expected subalgebra.  It is not quoted verbatim from one
source.

## The variance reversal

Let \(N\) and \(M\) be \(\sigma\)-finite von Neumann algebras and let

$$
\iota:N\longrightarrow M
\tag{SP1}
$$

be a normal unital faithful \(*\)-homomorphism.  A faithful normal state
\(\varphi\) on \(M\) has the marginal

$$
\psi:=\varphi\circ\iota
\tag{SP2}
$$

on \(N\).  Thus states move from whole to local by precomposition, whereas a
local observable \(x\in N\) moves into the whole algebra as \(\iota(x)\).
After identifying \(N\) with \(\iota(N)\), assume

$$
\sigma_t^\varphi(N)=N
\qquad(t\in\mathbb R).
\tag{SP3}
$$

By [[library/conditional-expectations-in-von-neumann-algebras/inq|Takesaki's
conditional-expectation theorem]], (SP3) is equivalent to the existence of the
\(\varphi\)-preserving normal faithful conditional expectation

$$
E:M\longrightarrow N,
\qquad
\varphi\circ E=\varphi.
\tag{SP4}
$$

This expectation supplies the adjoint Hilbert-space projection, but the local
form constructed below is pulled back through the multiplicative map
\(\iota\).  It is not minimized through \(E\).

## The standard-form carrier and its matrix intervals

Write

$$
H_M=L^2(M,\varphi),
\qquad
H_N=L^2(N,\psi)
\tag{SP5}
$$

for the GNS Hilbert spaces in their canonical standard forms.  The inclusion
has a canonical isometry

$$
V:H_N\longrightarrow H_M,
\qquad
V\Lambda_\psi(x)=\Lambda_\varphi(\iota(x)),
\tag{SP6}
$$

and \(p:=VV^*\) is the \(L^2\)-implementation of \(E\):

$$
p\Lambda_\varphi(a)=\Lambda_\varphi(E(a)).
\tag{SP7}
$$

The expectation and modular invariance give

$$
VJ_N=J_MV,
\qquad
V\Delta_\psi^{it}=\Delta_\varphi^{it}V.
\tag{SP8}
$$

The matrix levels are part of the hypothesis, not optional notation.  For
\(n\geq1\), put

$$
\varphi_n=\varphi\mathbin{\overline\otimes}\operatorname{tr}_n,
\qquad
\psi_n=\psi\mathbin{\overline\otimes}\operatorname{tr}_n,
\qquad
E_n=E\mathbin{\overline\otimes}\operatorname{id}_{M_n},
\tag{SP9}
$$

where \(\operatorname{tr}_n\) is normalized, and let \(V_n\), \(p_n=V_nV_n^*\)
be the corresponding standard-form maps between
\(H_{N,n}=L^2(N\overline\otimes M_n,\psi_n)\) and
\(H_{M,n}=L^2(M\overline\otimes M_n,\varphi_n)\).  Define the closed Markov intervals

$$
\mathcal C_{M,n}
:=
\overline{
\left\{
\Delta_{\varphi_n}^{1/4}\Lambda_{\varphi_n}(a):
0\leq a\leq1
\right\}},
\tag{SP10}
$$

and analogously \(\mathcal C_{N,n}\).  Then

$$
\boxed{
p_n\mathcal C_{M,n}
=V_n\mathcal C_{N,n}
=\mathcal C_{M,n}\cap V_nH_{N,n}.}
\tag{SP11}
$$

Indeed, \(E_n\) is unital positive and hence sends \([0,1]\) into \([0,1]\);
it commutes with the modular group, and

$$
p_n\Delta_{\varphi_n}^{1/4}\Lambda_{\varphi_n}(a)
=
\Delta_{\varphi_n}^{1/4}\Lambda_{\varphi_n}(E_n(a)).
\tag{SP12}
$$

The reverse inclusion in (SP11) follows because \(p_n\) fixes the embedded
copy of \(N\overline\otimes M_n\).  The proof of Lemma 4.3 in
[[library/modular-completely-dirichlet-forms-as-squares-of-derivations/inq|Wirth's
modular completely Dirichlet paper]] records (SP7), modular commutation, and
the unamplified interval image; applying the same calculation to
\(E\overline\otimes\operatorname{id}_{M_n}\) gives (SP11) at every matrix
level.

For a normal semifinite faithful weight, the same statement holds when its
restriction to \(N\) is semifinite and the elements in (SP10) are restricted
to the two-sided definition ideal.  The state version already covers
\(\sigma\)-finite Type-III factors and keeps the order unit visible.

## Exact pullback theorem

The following formulation isolates the true sufficient structure.

**Theorem (matrix-Markov standard-form pullback).**  Let \(V:H_N\to H_M\)
be an isometry between the standard-form Hilbert spaces of two von Neumann
algebras.  Suppose, for every \(n\geq1\), that its canonical amplification
\(V_n\) satisfies

$$
V_nJ_{N,n}=J_{M,n}V_n,
\qquad
p_n\mathcal C_{M,n}
=V_n\mathcal C_{N,n}
=\mathcal C_{M,n}\cap V_nH_{N,n},
\qquad
p_n=V_nV_n^*.
\tag{SP13}
$$

Let \(\mathcal E_M\) be a closed completely Dirichlet quadratic form on
\(H_M\).  Set

$$
D(\mathcal E_N)
:=
\{\eta\in H_N:V\eta\in D(\mathcal E_M)\},
\qquad
\mathcal E_N[\eta]
:=
\mathcal E_M[V\eta].
\tag{SP14}
$$

Entrywise amplification gives the exact domain identity

$$
D(\mathcal E_N^{(n)})
=
\{\eta\in H_{N,n}:V_n\eta\in D(\mathcal E_M^{(n)})\},
\qquad
\mathcal E_N^{(n)}
=
\mathcal E_M^{(n)}\circ V_n.
\tag{SP14a}
$$

Assume explicitly that \(D(\mathcal E_N)\) is dense in \(H_N\).  Then
\(\mathcal E_N\) is closed and completely Dirichlet.

If, in addition,

$$
V\Delta_N^{it}=\Delta_M^{it}V
\tag{SP15}
$$

and \(\mathcal E_M\) is modular, then \(\mathcal E_N\) is modular.  For
faithful normal states, if
\(\Omega_M\in D(\mathcal E_M)\),
\(\mathcal E_M[\Omega_M]=0\), and \(V\Omega_N=\Omega_M\), then
\(\mathcal E_N[\Omega_N]=0\).  Hence conservativity, and therefore unitality
of the associated completely positive semigroup, is inherited.

The expected inclusion (SP1)--(SP4) satisfies (SP13)--(SP15).  If
\(\jmath_\theta(x):=\Delta_\theta^{1/4}\Lambda_\theta(x)\) denotes the
symmetric GNS embedding for a faithful normal state \(\theta\), then the
theorem applies to

$$
\boxed{
\mathcal E_N[\jmath_\psi(x)]
=
\mathcal E_M[\jmath_\varphi(\iota(x))]}
\tag{SP16}
$$

whenever \(\jmath_\psi(x)\in D(\mathcal E_N)\).  The full form is the
graph-closed restriction (SP14); no claim is made that its finite-energy
algebraic vectors form a core.  Equation (SP16) is the precise meaning of the
shorthand \(\mathcal E_N[x]=\mathcal E_M[\iota(x)]\).  A completely Dirichlet
form gives the \(L^2\)-implementation of a
KMS-symmetric semigroup of normal contractive completely positive maps.  The
modular conclusion gives GNS symmetry, equivalently KMS symmetry plus modular
commutation.  Unitality requires the separate zero-energy condition above.

### Proof

Closedness is immediate but domain-sensitive.  If \((\eta_k)\) is Cauchy for
the graph norm

$$
\|\eta\|_{\mathcal E_N}^2
=
\|\eta\|_{H_N}^2+\mathcal E_N[\eta],
\tag{SP17}
$$

then \((V\eta_k)\) is graph-Cauchy for \(\mathcal E_M\).  Closedness of the
whole form gives a limit in \(D(\mathcal E_M)\), and the closed range of the
isometry \(V\) forces that limit to be \(V\eta\).  Thus \(\eta\in
D(\mathcal E_N)\).

Reality follows from the first identity in (SP13):

$$
\mathcal E_N[J_N\eta]
=
\mathcal E_M[J_MV\eta]
=
\mathcal E_M[V\eta].
\tag{SP18}
$$

It remains to prove the Markov inequality at every amplification.  Let
\(\Pi_{M,n}\) and \(\Pi_{N,n}\) be the metric projections onto the two closed
intervals in (SP13), and take \(\zeta=V_n\eta\) in the real part of
\(V_nH_{N,n}\).  If \(y=\Pi_{M,n}\zeta\), then \(p_ny\in\mathcal C_{M,n}\) by
(SP13), while orthogonality gives

$$
\|\zeta-p_ny\|\leq\|\zeta-y\|.
\tag{SP19}
$$

Uniqueness of the metric projection forces \(y=p_ny\).  Using (SP13) once
more,

$$
\Pi_{M,n}V_n=V_n\Pi_{N,n}
\quad\text{on the real subspace.}
\tag{SP20}
$$

Complete Dirichletness of the whole form therefore yields

$$
\mathcal E_N^{(n)}[\Pi_{N,n}\eta]
=
\mathcal E_M^{(n)}[\Pi_{M,n}V_n\eta]
\leq
\mathcal E_M^{(n)}[V_n\eta]
=
\mathcal E_N^{(n)}[\eta].
\tag{SP21}
$$

This also proves that every amplified projection preserves the restricted
form domain.  Equation (SP15) proves modular invariance by substitution, and
the assertion about the cyclic vector follows from \(V\Omega_N=\Omega_M\).

The density assumption in the theorem cannot be silently discarded: a dense
linear form domain in \(H_M\) need not have dense intersection with an
arbitrary closed subspace.  It is automatic if the projection \(p\) preserves
the whole form domain, and in finite dimensions.

## Tracial and Type-III specializations

For a finite von Neumann algebra with faithful normal trace \(\tau\), every
von Neumann subalgebra has its \(\tau\)-preserving conditional expectation.
The modular groups are trivial, \(H_M=L^2(M,\tau)\), and \(Vx=\iota(x)\).
Thus the theorem reduces to the familiar fact that a completely Dirichlet
form restricted to a multiplicative, expected \(L^2\)-subspace remains
completely Dirichlet, provided its restricted domain is dense.

For a \(\sigma\)-finite Type-III algebra, choose a faithful normal state
\(\varphi\).  No trace or density matrix is required.  The nontrivial extra
condition is (SP3): a subalgebra need not admit a \(\varphi\)-preserving
expectation.  Once modular invariance, density, and the amplified standard-form
identities are supplied, the proof above is unchanged.  Type III therefore
creates no new obstruction to pullback, but it also does not supply the
expectation automatically.

## The reducing wall makes pullback and quotient coincide

Let \(K=VH_N\), \(p=VV^*\), \(q=V^*\), and let \(T_t=e^{-tA}\) be the
self-adjoint \(L^2\)-semigroup associated with \(\mathcal E_M\).  The wall is
**reducing for the form** when

$$
pD(\mathcal E_M)\subset D(\mathcal E_M),
\qquad
\mathcal E_M(p\xi,(1-p)\zeta)=0
\quad
(\xi,\zeta\in D(\mathcal E_M)).
\tag{SP22}
$$

For a closed symmetric form, this is equivalent to \(T_tK\subseteq K\) for
all \(t\geq0\): self-adjointness then also preserves \(K^\perp\).  Equivalently,
\(p\) commutes with the semigroup and resolvent.  It is also equivalent to the
extended-form contraction

$$
\mathcal E_M[p\xi]\leq\mathcal E_M[\xi]
\qquad(\xi\in H_M),
\tag{SP23}
$$

where finite energy on the right includes domain preservation.  The
semigroup/form criterion is the closed-subspace case of Ouhabaz's invariance
criterion; the implication from (SP23) is also obtained directly by applying
it to \(p\xi+\lambda(1-p)\xi\) for every \(\lambda\in\mathbb C\), which forces
the cross term in (SP22) to vanish.

Define the genuine infimal quotient by

$$
\check{\mathcal E}_N[\eta]
:=
\inf\left\{
\mathcal E_M[\xi]:
\xi\in D(\mathcal E_M),\ q\xi=\eta
\right\},
\tag{SP24}
$$

with infimum \(+\infty\) for an empty fibre.  Under (SP22), every admissible
lift has the orthogonal decomposition

$$
\xi=V\eta+z,
\qquad
z\in K^\perp,
\qquad
\mathcal E_M[\xi]
=
\mathcal E_M[V\eta]+\mathcal E_M[z].
\tag{SP25}
$$

Moreover, \(p\xi=V\eta\) belongs to the form domain.  The infimum is therefore
attained at \(V\eta\), the finite domains agree, and

$$
\boxed{
\check{\mathcal E}_N[\eta]
=
\mathcal E_N[\eta]
=
\mathcal E_M[V\eta].}
\tag{SP26}
$$

This is the strongest simple condition under which the expectation quotient
inherits complete Dirichletness from the pullback theorem: the hidden and
retained directions do not couple in the whole form.

Reduction is also necessary for the equality (SP26), though not for complete
Dirichletness of every possible short.  Indeed, suppose (SP26) holds as an
identity of extended forms.  Any \(\xi\in D(\mathcal E_M)\) makes the quotient
finite at \(q\xi\), so (SP26) forces \(p\xi=Vq\xi\in D(\mathcal E_M)\).
For \(k\in pD(\mathcal E_M)\), \(z\in(1-p)D(\mathcal E_M)\), and every
\(\lambda\in\mathbb C\), the vector \(k+\lambda z\) is a lift of \(V^*k\).
Hence

$$
\mathcal E_M[k]
\leq
\mathcal E_M[k+\lambda z]
\qquad(\lambda\in\mathbb C),
\tag{SP26a}
$$

which forces \(\mathcal E_M(k,z)=0\).  Thus (SP22) holds.  Consequently,
pullback equals infimal quotient exactly when the retained standard-form
subspace reduces the whole form, provided equality is meant on the full
extended domains.

At the algebra level, let \((\Phi_t)\) be the KMS-symmetric quantum dynamical
semigroup represented by \((T_t)\).  If

$$
\Phi_t(N)\subseteq N
\qquad(t\geq0),
\tag{SP27}
$$

then \(T_tK\subseteq K\), hence (SP22) holds.  The local semigroup is literally
\(\Phi_t|_N\), and the \(L^2\) commutation implies

$$
E\Phi_t=\Phi_tE.
\tag{SP28}
$$

Thus invariant-subalgebra restriction, infimal quotient, and pullback agree
in this reducing case.  Without (SP27), the pullback theorem still constructs
a local completely positive semigroup from the restricted form, but that
semigroup is new; it is not generally a restriction of \(\Phi_t\).

## The operations that must not be conflated

1. **Observable pullback or form restriction.**  Equation (SP14) restricts the
   form to the closed standard-form copy \(K\).  In a bounded block generator
   it keeps the principal block \(A_{11}\).  Expectedness makes this operation
   completely Dirichlet; dynamical invariance is not needed.

2. **Invariant-subspace restriction.**  This adds (SP22) or (SP27).  It makes
   the whole semigroup reduce on \(K\), so the local semigroup is inherited
   rather than reconstructed.

3. **Infimal quotient or short.**  Equation (SP24) minimizes over
   \(q^{-1}(\eta)\).  For a finite-dimensional positive block with positive
   definite hidden block, or for a bounded positive block operator whose
   hidden block satisfies \(C\geq cI\) for some \(c>0\),

   $$
   A=
   \begin{pmatrix}
   A_{11}&B\\
   B^*&C
   \end{pmatrix},
   \qquad C>0,
   \tag{SP29}
   $$

   it gives \(A_{11}-BC^{-1}B^*\), not \(A_{11}\).  If \(C\) is singular, a
   Moore--Penrose formula needs the relevant range condition, and the
   intrinsic short must otherwise be used.  Positivity survives; complete
   Markovianity need not.  Under the reducing condition \(B=0\), so the two
   formulas agree.  [[library/shorted-operators-ii/inq|Anderson and
   Trapp]] treat bounded shorting, while
   [[library/shorting-parallel-addition-and-form-sums-of-nonnegative-selfadjoint-linear-relations/inq|Arlinskiĭ]]
   shows why an unbounded formal Schur complement must be replaced by a
   self-adjoint-relation or closed-form construction.

4. **Semigroup compression.**  The maps

   $$
   R_t:=V^*T_tV
   \tag{SP30}
   $$

   implement the completely positive maps \(E\Phi_t\iota\) one time at a
   time, but generally do not form a semigroup.  Their exact defect is

   $$
   R_{s+t}-R_sR_t
   =
   V^*T_s(1-p)T_tV.
   \tag{SP31}
   $$

   The reducing condition kills this defect.  In the bounded case, the
   semigroup of the pullback form is \(e^{-tA_{11}}\), which is generally not
   \(V^*e^{-tA}V\).

5. **Adiabatic elimination.**  This is a singular-limit theorem for a family
   of dynamics with a fast scale, a slow subspace, decoupling hypotheses, and
   a specified convergence topology.  A Schur or Feshbach expression may
   occur in the limiting generator, but algebraic shorting alone is not such a
   theorem.  Bouten and Silberfarb's Theorem 2.1 obtains strong convergence of
   quantum stochastic dynamics only under their Assumptions 1--4.  Conversely,
   Tokieda--Elouard--Sarlette--Rouchon give explicit higher-order eliminated
   dynamics that violate complete positivity.  Complete positivity must come
   from the limit theorem and its hypotheses, not from the visual shape of a
   Schur complement.

## The six-vertex obstruction is sharp for expectation alone

The [[trace-dirichlet-descent/inq#Conditional expectation alone does not preserve Markovianity|six-vertex
tree counterexample]] already lies in the finite commutative, tracial case.
Its whole graph energy is completely Dirichlet, and conditional expectation
onto the three blocks

$$
\{0,1\},\qquad\{2,3\},\qquad\{4,5\}
\tag{SP32}
$$

is state-preserving.  The safe pullback to block-constant observables is

$$
\mathcal E_N(a,b,c)
=
2(a-b)^2+2(a-c)^2,
\tag{SP33}
$$

which is again a graph Dirichlet form, exactly as the theorem predicts.  The
infimal quotient is instead

$$
\check{\mathcal E}_N(a,b,c)
=
2(a-b)^2+2(a-c)^2-\frac12(b-c)^2.
\tag{SP34}
$$

For \(f=(0,-3,1)\),

$$
\check{\mathcal E}_N[f]=12,
\qquad
\check{\mathcal E}_N[|f|]=18.
\tag{SP35}
$$

Thus the quotient is not Markov.  The example satisfies expectedness,
closedness, finite-dimensional domain density, and whole complete
Dirichletness.  What fails is precisely reduction: block-constant functions
are not invariant under the graph heat semigroup.  Consequently there can be
no theorem of the form

$$
\text{conditional expectation + closed completely Dirichlet whole form}
\Longrightarrow
\text{completely Dirichlet infimal quotient}.
\tag{SP36}
$$

Any more general noncommutative or Type-III claim with only those hypotheses
is already refuted by this commutative corner.  More explicitly, tensor the
whole and retained algebras, the state, the expectation, and the graph
semigroup with the identity on any \(\sigma\)-finite Type-III factor.  The
resulting direct sums are Type-III von Neumann algebras, though not factors,
and the same violation survives on vectors \(f\otimes\Omega\).  This refutes
a claim for arbitrary Type-III algebras; a theorem explicitly restricted to
Type-III factors would require a factor-specific counterexample.  In any
case, merely passing to a Type-III standard form does not repair the quotient.

## Yang--Mills consequence

At a regulator \(r\), the safe route is to construct a genuine normal unital
observable inclusion

$$
\iota_r:N_r\hookrightarrow M_r,
\tag{SP37}
$$

restrict the whole state \(\varphi_r\) to
\(\psi_r=\varphi_r\circ\iota_r\), and prove modular invariance of the retained
algebra, equivalently existence of a \(\varphi_r\)-preserving expectation
\(E_r\).  A closed completely Dirichlet whole form then gives

$$
\mathcal E_{N,r}[\eta]
=
\mathcal E_{M,r}[V_r\eta]
\tag{SP38}
$$

as a closed completely Dirichlet local form whenever its domain is dense.
This upgrades the coordinate or cylinder-form branch in
[[contemporary-puzzles/yang-mills-mass-gap/gauge-dirichlet-trace-carrier|the
regulated gauge carrier]]: local complete Markovianity follows from
the expected multiplicative observable pullback together with domain density
and whole complete Dirichletness, not from minimization through conditional
expectation or from multiplicativity alone.

If the regulated whole process is ergodic and obeys the centered Poincaré
bound

$$
\mathcal E_{M,r}[\xi]
\geq
\kappa_r
\|\xi-\langle\Omega_{M,r},\xi\rangle\Omega_{M,r}\|^2,
\tag{SP39}
$$

then \(V_r\Omega_{N,r}=\Omega_{M,r}\) and isometry give the same bound locally:

$$
\mathcal E_{N,r}[\eta]
\geq
\kappa_r
\|\eta-\langle\Omega_{N,r},\eta\rangle\Omega_{N,r}\|^2.
\tag{SP40}
$$

For a nontrivial whole kernel, the corresponding kernel projections must be
shown compatible with \(V_rH_{N,r}\); it is not enough to reuse (SP40)
formally.

This conclusion is narrower than a trace-wall theorem.  It assigns to an
actual local observable its whole response; it does not choose the
least-response whole representative of a conditional local presentation.
Equality with that infimal meaning requires the reducing/lumpability theorem
(SP22).  Even after (SP38)--(SP40), a continuum Yang--Mills mass gap still
requires neutral-algebra coverage, gauge and net covariance, a
regulator-uniform calibrated lower bound, continuum and infinite-volume
control, and a same-carrier OS or positive-energy comparison.  The pullback
theorem closes the complete-Markov arrow; it does not supply those remaining
physical arrows.

## Primary theorem anchors

- Masamichi Takesaki, “Conditional Expectations in von Neumann Algebras,”
  *Journal of Functional Analysis* **9** (1972), 306--321,
  [DOI](https://doi.org/10.1016/0022-1236(72)90004-3): the first main theorem
  gives (SP3) \(\Leftrightarrow\) (SP4).  Accardi--Cecchini restate the state
  version as Theorem 5.2 and identify GNS symmetry as KMS symmetry plus modular
  commutation in Proposition 6.1,
  [DOI](https://doi.org/10.1016/0022-1236(82)90022-2).
- Melchior Wirth, “Modular Completely Dirichlet Forms as Squares of
  Derivations,” [arXiv:2307.04502](https://arxiv.org/abs/2307.04502),
  [DOI](https://doi.org/10.1093/imrn/rnae092): Section 1.2 gives the
  matrix-interval definition; the proof of Lemma 4.3 gives (SP7), modular
  commutation, and the expected-subalgebra interval image; Theorem 4.4 is the
  modular completely Dirichlet derivation theorem.
- Stanisław Goldstein and J. Martin Lindsay, “KMS-Symmetric Markov
  Semigroups,” *Mathematische Zeitschrift* **219** (1995), 591--608,
  [DOI](https://doi.org/10.1007/BF02572383), Theorem 5.7; and “Markov
  Semigroups KMS-Symmetric for a Weight,” *Mathematische Annalen* **313**
  (1999), 39--67, [DOI](https://doi.org/10.1007/s002080050249), Theorems 4.9
  and 5.7: form--semigroup correspondence in the state and weight settings.
  Fabio Cipriani gives the equivalent standard-form correspondence in Theorem
  4.11 of “Dirichlet Forms and Markovian Semigroups on Standard Forms of von
  Neumann Algebras,” *Journal of Functional Analysis* **147** (1997),
  259--300, [DOI](https://doi.org/10.1006/jfan.1996.3063).
- El Maati Ouhabaz, “Invariance of Closed Convex Sets and Domination Criteria
  for Semigroups,” *Potential Analysis* **5** (1996), 611--625,
  [DOI](https://doi.org/10.1007/BF00275797), Corollary 2.4: the form criterion
  for invariant closed subspaces used in (SP22)--(SP23).
- Luc Bouten and Andrew Silberfarb, “Adiabatic Elimination in Quantum
  Stochastic Models,” *Communications in Mathematical Physics* **283**
  (2008), 491--505, [arXiv:0707.0686v4](https://arxiv.org/abs/0707.0686v4),
  [DOI](https://doi.org/10.1007/s00220-008-0513-6), Theorem 2.1 under
  Assumptions 1--4.
- Masaaki Tokieda, Cyril Elouard, Alain Sarlette, and Pierre Rouchon,
  “Complete Positivity Violation of the Reduced Dynamics in Higher-Order
  Quantum Adiabatic Elimination,”
  [arXiv:2303.04495](https://arxiv.org/abs/2303.04495), Sections III--IV:
  finite-dimensional examples in which higher-order eliminated dynamics are
  not completely positive.
