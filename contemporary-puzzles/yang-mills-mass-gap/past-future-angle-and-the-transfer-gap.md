# Past--Future Angle and the Transfer Gap

In a stationary reversible Markov--Osterwalder--Schrader path space, conditional expectation onto two **disjoint** Euclidean half-spaces produces a canonical pair of descents. Their Friedrichs cosine is exactly the vacuum-reduced transfer contraction across the intervening slab. The positive return \(qpq\), restricted to its endpoint support, is the square of that transfer operator, so its logarithm per unit slab thickness recovers the clock Hamiltonian. This realizes a precise Copernican statement: the clock-energy gap is not a raw discrete jump or a broken symmetry, but the calibrated rate at which every nonvacuum distinction fails to remain simultaneously present in opposed whole--part views. It becomes a relativistic mass gap only after the OS/Poincare reconstruction and Casimir identification.

**Status: [EXACT] for the stationary reversible Markov theorem, the support and polar identities, the endpoint-compression identity, and the transfer-gap formula; [EXACT UNDER STATED FINITE-REGULATOR HYPOTHESES] for the ground-state-transformed lattice application; [CONDITIONAL THEOREM] for Osterwalder--Schrader and continuum Yang--Mills realization; [OPEN CONSTRUCTION] for deriving a regulator-uniform angle rate from independent gauge geometry.**

## The carrier and the two cuts

Let \((S,\Sigma,\nu)\) be a standard probability space and let

$$
T:L^2(\nu)\longrightarrow L^2(\nu)
\tag{PFA1}
$$

be a Markov operator. Assume

$$
T1=1,
\qquad
T=T^*,
\qquad
0\leq T\leq I.
\tag{PFA2}
$$

Self-adjointness is detailed balance. The last condition is stronger: a reversible Markov operator can have negative spectrum, while the transfer operators relevant below are Hilbert-positive. Let

$$
Q:=\mathbf 1_{\{1\}}(T)
\tag{PFA3}
$$

be the projection onto the fixed space. The physically desired vacuum-uniqueness case is \(QL^2(\nu)=\mathbb C1\), but the theorem does not assume it.

Let \((X_k)_{k\in\mathbb Z}\) be the stationary two-sided Markov process with invariant law \(\nu\) and transition \(T\), on path space \((\Omega,\mu)\). For integers \(i<j\), put

$$
\mathcal P_i:=\sigma(X_k:k\leq i),
\qquad
\mathcal F_j:=\sigma(X_k:k\geq j),
\qquad
d:=j-i.
\tag{PFA4}
$$

Conditional expectation gives orthogonal projections on the history carrier \(\mathscr H=L^2(\Omega,\mu)\):

$$
e_-:=\mathbb E_\mu[\,\cdot\mid\mathcal P_i],
\qquad
e_+:=\mathbb E_\mu[\,\cdot\mid\mathcal F_j].
\tag{PFA5}
$$

The endpoint embeddings

$$
J_k:L^2(\nu)\longrightarrow\mathscr H,
\qquad
J_k f=f(X_k),
\tag{PFA6}
$$

are isometries. Stationarity, the Markov property, and reversibility give

$$
e_-J_j=J_iT^d,
\qquad
J_j^*J_i=T^d.
\tag{PFA7}
$$

These equations say exactly what is being forgotten. A future endpoint function is replaced by its best past-measurable prediction; no claim that nature is ontologically stochastic has entered.

The cuts must be disjoint. If both halves contain the same interface, for example \(\mathcal P_0\) and \(\mathcal F_0\), then their intersection contains all of \(L^2(\sigma(X_0))\). In the Markov case the two projections meet at the interface projection, so removing their common range erases the transfer information. A slab of positive Euclidean thickness is therefore structural, not cosmetic.

## The common whole and the exact angle

Hilbert positivity makes the common retained information precise:

$$
\operatorname{Ran}e_-\cap\operatorname{Ran}e_+
=
J_i QL^2(\nu)
=
J_j QL^2(\nu).
\tag{PFA8}
$$

To see the nontrivial direction, take \(F\) in both ranges and set \(f=J_i^*F\), \(g=J_j^*F\). Conditional-expectation contractivity and the Markov factorization give

$$
\|F\|^2
=\langle f,T^d g\rangle
\leq\|f\|\,\|g\|
\leq\|F\|^2.
\tag{PFA9}
$$

Equality forces \(F=J_i f=J_j g\), \(f=T^dg\), and \(g=T^df\). Hence \(f=T^{2d}f\). Because \(0\leq T\leq I\), spectral calculus forces \(Tf=f\). Conversely, a fixed vector has identical representatives at every time almost surely.

Let \(R\) be the projection in \(\mathscr H\) onto the common space in (PFA8), and define

$$
p:=e_--R,
\qquad
q:=e_+-R.
\tag{PFA10}
$$

The Friedrichs cosine of the two history subspaces is then

$$
\boxed{
c_F(i,j)
:=\|pq\|
=\|T^d-Q\|.}
\tag{PFA11}
$$

Indeed, for \(F\in\operatorname{Ran}p\) and \(G\in\operatorname{Ran}q\), their endpoint conditional expectations \(f=J_i^*F\) and \(g=J_j^*G\) lie in \((1-Q)L^2(\nu)\), and

$$
\langle F,G\rangle
=\langle f,T^dg\rangle.
\tag{PFA12}
$$

The endpoint expectations are contractions, giving the upper bound in (PFA11); restricting to endpoint functions gives the same supremum, whether or not that norm is attained. If

$$
\rho:=\|T-Q\|,
\tag{PFA13}
$$

then positivity and self-adjointness give the exact power law

$$
\boxed{c_F(i,j)=\rho^d.}
\tag{PFA14}
$$

There is no factor of two in the separation exponent. A factor \(2d\) appears only after one completes a past--future--past or future--past--future return, or if the cuts themselves were placed \(2d\) steps apart.

The pair form from [[oriented-descent-angle-and-emergent-symmetry]] now has the sharp edge

$$
G_{i,j}:=2I-e_--e_+,
\qquad
G_{i,j}\geq(1-\rho^d)(1-R).
\tag{PFA15}
$$

Vacuum-only intersection is not enough for a gap. In an infinite system, \(Q\) can project only onto constants while the spectrum of \(T\) still accumulates at \(1\); then \(c_F=1\) and arbitrarily persistent nonvacuum distinctions remain.

## The operator and what it operates on

Write \(J_k^0=J_k|_{(1-Q)L^2(\nu)}\). The reduced projection product itself factors as

$$
pq
=
J_i^0T^d(J_j^0)^*.
\tag{PFA16}
$$

It sends a future-slice distinction to the part recoverable from the past slice. Reversing the ordered cuts replaces \(pq\) by \((pq)^*\). Its orientation-even return is

$$
\boxed{
q p q
=
J_j^0T^{2d}(J_j^0)^*.}
\tag{PFA17}
$$

If \(T\) is injective on the centered carrier, then

$$
\begin{aligned}
s(qpq)&=J_j^0(J_j^0)^*,\\
|pq|&=(qpq)^{1/2}=J_j^0T^d(J_j^0)^*,\\
pq&=V_d|pq|,
\qquad
V_d=J_i^0(J_j^0)^*.
\end{aligned}
\tag{PFA18}
$$

Thus the pair itself identifies the correlated endpoint carrier as the support of its positive return; future innovations lie in the kernel. The partial isometry \(V_d\) remembers the arrow, while the modulus forgets orientation and retains attenuation. This is an exact algebraic split between directed order and the positive shadow later read as clock energy.

The typing is essential. The projections and \(G_{i,j}\) act on the **history comparison carrier**. The modulus in (PFA18) acts on its supported **endpoint-slice carrier**. Scaling the whole frame operator as if it were a Hamiltonian is wrong: directions orthogonal to both retained subspaces carry eigenvalue \(2\), independent of slab thickness.

Suppose one Euclidean step has length \(a>0\), the normalized transfer is injective, and the endpoint Hamiltonian satisfies

$$
T=e^{-aH_T/(\hbar c)},
\qquad
H_TQ=0.
\tag{PFA19}
$$

Functional calculus on the support in (PFA18) then gives

$$
\boxed{
J_j^0H_T(J_j^0)^*
=
-\frac{\hbar c}{da}\log|pq|
=
-\frac{\hbar c}{2da}\log(qpq).}
\tag{PFA20}
$$

The logarithms are restricted to \(s(qpq)\mathscr H\). The factor two belongs to the round trip. The logarithm converts multiplicative survival across concatenated slabs into an additive generator.

This is the promised reversal tactic in exact form. One may begin with the relative geometry of two information subspaces, take the supported positive return, and recover a generator. In the stationary Markov realization this recovers a supplied transfer Hamiltonian and is therefore a reformulation, not yet an independent proof.

## The whole slab family fixes the logarithm

A single angle together with a freely chosen thickness would be an arbitrary yardstick. The non-arbitrary structure is the family of ordered slabs. For \(i<j<k\), define

$$
A_{ij}:=J_i^0T^{j-i}(J_j^0)^*.
\tag{PFA21}
$$

Then

$$
\boxed{A_{ij}A_{jk}=A_{ik}.}
\tag{PFA22}
$$

After the stationary endpoint carriers are identified, this is the positive contraction semigroup law \(C_{\ell_1}C_{\ell_2}=C_{\ell_1+\ell_2}\). In a strongly continuous continuum family, the generator obtained from \(-\ell^{-1}\log C_\ell\) is independent of \(\ell\). Additive Euclidean clock depth is therefore derived from composition of slabs; it is not supplied by one isolated number.

## The calibrated gap

Let \(P_0=Q\) be the unique vacuum projection and let

$$
\Delta_E
:=
\inf\sigma\!\left(H_T\big|_{(1-P_0)L^2(\nu)}\right).
\tag{PFA23}
$$

Equations (PFA11) and (PFA19) imply, for every positive integer \(d\),

$$
\boxed{
c_F(d;a)
=e^{-da\Delta_E/(\hbar c)},
\qquad
\Delta_E
=-\frac{\hbar c}{da}\log c_F(d;a).}
\tag{PFA24}
$$

The angle is dimensionless. The Euclidean separation \(da\) is a length. The factor \(\hbar c\) converts the inverse-length decay rate into energy. These are three different concepts even though dimensional equations relate them.

For a family of regulators \(r\), write \(c_{F,r}(\ell)\) with \(\ell=d_ra_r\) the **actual** slab thickness. There are two correct continuum criteria:

$$
\begin{aligned}
&\text{fixed physical thickness }\ell_*>0:
&&\sup_r c_{F,r}(\ell_*)<1,\\
&\text{adjacent slices }\ell=a_r\downarrow0:
&&\inf_r\left[-\frac{\hbar c}{a_r}\log c_{F,r}(a_r)\right]>0.
\end{aligned}
\tag{PFA25}
$$

They are the same gap statement in different samplings of the semigroup. For a finite limiting gap,

$$
c_{F,r}(a_r)\longrightarrow1,
\qquad
1-c_{F,r}(a_r)
\sim
\frac{a_r\Delta_{E,r}}{\hbar c}.
\tag{PFA26}
$$

Therefore a regulator-uniform raw one-step floor \(1-c_F>0\) is not merely stronger than necessary; it rejects the ordinary continuum scaling of a massive theory. The invariant quantity is the logarithmic cosine **per calibrated thickness**. A raw fixed-angle criterion is legitimate only when the cuts remain a fixed positive physical distance apart.

If the Euclidean parameter is a duration \(s\) rather than a length, replace \(a/c\) by \(s\) throughout: \(T(s)=e^{-sH_T/\hbar}\) and \(\Delta_E=-(\hbar/s)\log c_F(s)\). This conversion must be stated rather than hidden.

## Entropy is a stronger forgetting certificate

The cosine is the maximal \(L^2\) correlation between centered past and future information. It is a Hilbert-geometric quantity, not a declaration that the underlying ontology rolls dice.

An independently proved strong data-processing inequality can bound it. If, for probability densities \(h\) with respect to \(\nu\),

$$
\operatorname{Ent}_\nu(T^dh)
\leq
\eta_d\operatorname{Ent}_\nu(h),
\qquad
0\leq\eta_d<1,
\tag{PFA27}
$$

then linearizing at \(h=1+\varepsilon f\), with \(Qf=0\), gives

$$
\|T^df\|_2^2
\leq
\eta_d\|f\|_2^2,
\qquad
c_F(d)\leq\sqrt{\eta_d}.
\tag{PFA28}
$$

Thus entropy contraction is a nonlinear route to the angle bound; its Hessian at equilibrium is the quadratic shadow. The converse need not hold, and neither inequality supplies the physical unit or Osterwalder--Schrader reconstruction by itself.

## Finite lattice Yang--Mills realization

At a finite lattice regulator, [[library/construction-of-a-selfadjoint-strictly-positive-transfer-matrix-for-euclidean-lattice-gauge-theories/inq|Luscher's transfer construction]] and [[library/gauge-field-theories-on-a-lattice/inq|Osterwalder--Seiler positivity]] provide the relevant positive self-adjoint transfer framework. Assume additionally that the gauge-invariant normalized transfer \(\widetilde T_{a,L}\) has a unique strictly positive vacuum vector \(\psi_{0,a,L}\) and the kernel properties needed for its ground-state transform. Multiplication by \(\psi_{0,a,L}\) identifies it with the reversible Markov operator

$$
M_{a,L}f
=
\psi_{0,a,L}^{-1}
\widetilde T_{a,L}(\psi_{0,a,L}f)
\tag{PFA29}
$$

on the gauge-invariant slice probability space \(\mathrm d\nu_{a,L}=\psi_{0,a,L}^2\mathrm d\mu_{\mathrm{Haar}}\). The stationary path construction then gives canonical past and future descents and

$$
c_{F,a,L}(d)
=
\left\|
\widetilde T_{a,L}^{\,d}(1-P_{0,a,L})
\right\|.
\tag{PFA30}
$$

This is an exact finite-regulator construction of the opposed pair. It is gauge-group neutral in form and does not privilege \(SU(2)\) or \(SU(3)\). It also does not prove the mass gap: the path measure was built from the transfer operator whose contraction is being restated.

The noncircular theorem target is now exceptionally sharp. Construct or characterize the two-cut history geometry without reading the desired spectral edge from \(H_T\), and prove either

$$
\sup_{a,L}c_{F,a,L}(\ell_*)\leq q_*<1
\tag{PFA31}
$$

at a fixed physical slab thickness \(\ell_*>0\), or the equivalent calibrated rate bound along the continuum trajectory. Then prove that the endpoint compression is the Osterwalder--Schrader transfer semigroup, control the varying carriers and vacuum projections, and reconstruct a nontrivial local Poincare-covariant continuum theory. Only after that last step may the clock gap be called a Yang--Mills mass gap and be rewritten as a Poincare-Casimir statement.

Reflection positivity alone does not supply the Markov separator, unique vacuum, or angle estimate. [[library/the-semigroup-characterization-of-osterwalder-schrader-path-spaces/inq|Klein]] isolates the additional semigroup structure, [[library/from-euclidean-field-theory-to-quantum-field-theory/inq|Schlingemann]] supplies an algebraic reconstruction route, and [[library/reflection-positivity-and-spectral-theory/inq|Jorgensen and Tian]] explain the projection geometry relating Markov and Osterwalder--Schrader structures.

## The noncommutative lift

The commutative path theorem is a prototype, not a demand for fundamental stochasticity. A Type-III-compatible lift would replace sigma-algebras by a standard-form history carrier and preserving expectations or pointed correspondences. Its decisive certificate is not the bare existence of two projections, but a typed slice isometry \(J_\ell\) and the identity

$$
J_\ell^*q p qJ_\ell
=
e^{-2\ell H/(\hbar c)}
\tag{PFA32}
$$

on the vacuum-reduced physical slice. Ordinary nested Lorentzian local algebras generally do not admit the required vacuum-preserving expectation shells, so a Euclidean regulator, interface algebra, or different-carrier correspondence is load bearing. A twisted spectral triple may help construct the slice metric or comparison operator, but it contributes to the gap only if it proves (PFA32), or a domain-correct inequality strong enough to replace it.

Knots, cocycles, wall-crossing classes, and descent residues can constrain which sectors survive the two cuts or help eliminate a common blind subspace. To solve the Clay problem they must ultimately control the operator norm in (PFA31) on **every** centered gauge-invariant direction, including topologically trivial sectors. A sector label, index, or Hessian analogy is not yet that estimate.

## Conceptual return

The exact chain is

$$
\begin{gathered}
\text{ordered disjoint cuts}
\longrightarrow
\text{conditional-expectation projections}
\longrightarrow
\text{dimensionless past--future angle},\\
\text{positive supported return}
\longrightarrow
\text{logarithmic rate per slab thickness}
\longrightarrow
\text{clock Hamiltonian after OS identification}.
\end{gathered}
\tag{PFA33}
$$

The whole is represented by \(QL^2(\nu)\): it survives every slab unchanged and therefore carries no decay scale. A part is a direction in \((1-Q)L^2(\nu)\); its scale is the rate at which its distinguishability survives relative to the whole. In this limited exact sense, scale is not first a coordinate painted onto an object. It is a relation between opposed presentations of information.

The arrow remains prior. Swapping the cuts adjoints \(pq\) and reverses \(V_d\); the supported moduli live on opposite endpoint carriers but have the same singular-value data, from which the self-adjoint observable generator is recovered. Symmetry and positive energy can therefore be shadows of an ordered construction without requiring a symmetric ontology that later breaks. What remains open is the hard part: derive the strictly positive calibrated rate from Yang--Mills geometry without importing the transfer spectrum, and carry it through the continuum reconstruction.

[[phase-modulus-pointing-and-euclidean-dwell]] develops two exact consequences without identifying them with a measurement outcome. The return \(A_\ell^*A_\ell\) is a Born-form effect only after a readout is declared, while its monotone quadratic-form integral over Euclidean depth is \((\hbar c/2)H^{-1}\) on the vacuum complement. A gap is therefore equivalent to a uniform finite ceiling on that integrated persistence. The same note proves that adjoining a complex structure or a flat unitary phase cannot change the Friedrichs angle or open the positive modulus gap.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/past_future_angle_receipt.py|The finite receipt]] constructs the conditional-expectation projections of a three-state reversible path pair, verifies the exponent \(d\), the round-trip square, and the frame edge, and contrasts shrinking adjacent slices with fixed physical thickness. [[contemporary-puzzles/yang-mills-mass-gap/receipts/past-future-angle-receipt-output.txt|Its stored output]] is a finite-dimensional identity check, not a continuum or Yang--Mills proof.
