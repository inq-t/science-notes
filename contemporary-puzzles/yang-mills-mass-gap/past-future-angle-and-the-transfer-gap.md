# Past--Future Angle and the Transfer Gap

In a stationary reversible Markov--Osterwalder--Schrader path space, conditional expectation onto two **disjoint** Euclidean half-spaces produces a canonical pair of descents. Their Friedrichs cosine is exactly the vacuum-reduced transfer contraction across the intervening slab. The positive return \(qpq\), restricted to its endpoint support, is the square of that transfer operator, so its logarithm per unit slab thickness recovers the clock Hamiltonian. The whole two-sided history shift is unitary while the one-slice transfer is its compression; the later Lorentzian clock is a distinct reconstructed unitary. This realizes a precise Copernican statement: the clock-energy gap is not a raw discrete jump or a broken symmetry, but the calibrated rate at which every nonvacuum distinction fails to remain simultaneously present in opposed whole--part views. It becomes a relativistic mass gap only after the OS/Poincare reconstruction and Casimir identification.

**Status: [EXACT] for the stationary reversible Markov theorem, history-shift compression, support and polar identities, optimal two-block variance factor, standard-form expectation projection, Stinespring two-slice correspondence, endpoint-compression identity, and transfer-gap formula; [EXACT UNDER STATED FINITE-REGULATOR HYPOTHESES] for the ground-state-transformed lattice application; [CONDITIONAL THEOREM] for Osterwalder--Schrader and continuum Yang--Mills realization; [OPEN CONSTRUCTION] for deriving a regulator-uniform angle rate from independent gauge geometry.**

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

## The whole shift, the slice compression, and the clock are different arrows

The two-sided history also supplies a useful type-check on the word
*unitary*. Let \(\theta\) be the invertible path shift,
\((\theta\omega)_k=\omega_{k+1}\), and define its Koopman operator by

$$
(\mathscr U_{\mathrm{hist}}F)(\omega):=F(\theta\omega).
\tag{PFA7a}
$$

Stationarity makes \(\mathscr U_{\mathrm{hist}}\) unitary on
\(\mathscr H=L^2(\Omega,\mu)\), and
\(\mathscr U_{\mathrm{hist}}J_k=J_{k+1}\). Nevertheless the one-slice
Euclidean transfer is generally only the compression

$$
\boxed{
T^n
=
J_0^*\mathscr U_{\mathrm{hist}}^nJ_0,\qquad n\geq0.}
\tag{PFA7b}
$$

Thus a unitary arrow on the history carrier can present as a positive
contraction after the intermediate history coordinates are omitted. If
\(e_0=J_0J_0^*\), the semigroup consequence of the Markov property is visible
in the exact forward compression identity

$$
J_0^*\mathscr U_{\mathrm{hist}}^m
(I-e_0)
\mathscr U_{\mathrm{hist}}^nJ_0
=0,\qquad m,n\geq0,
\tag{PFA7c}
$$

because its left side is \(T^{m+n}-T^mT^n\). This zero does not say that
the omitted history component vanishes. It says that its off-slice,
leave-and-reenter contribution is invisible after the declared forward
recompression; no backward-time operation occurs.

Under the full Osterwalder--Schrader hypotheses, reconstructed Euclidean
translations give a strongly continuous self-adjoint contraction semigroup
\(C_\ell=e^{-\ell H/(\hbar c)}\) for a positive generator \(H\). Its
finite-depth members are injective, and functional calculus gives a second
unitary group

$$
U_{\mathrm{clock}}(t)=e^{-itH/\hbar}
\tag{PFA7d}
$$

on the reconstructed physical carrier. In general
\(\mathscr U_{\mathrm{hist}}\) and \(U_{\mathrm{clock}}\) have different
native carriers and are not canonically the same operator. In a Markov OS
specialization the physical carrier may be identified with \(L^2(\nu)\),
whereas \(\mathscr U_{\mathrm{hist}}\) still acts on \(L^2(\Omega,\mu)\).
The history operator \(\mathscr U_{\mathrm{hist}}\) represents stationary
relabelling of an entire two-sided Euclidean history; the clock operator
\(U_{\mathrm{clock}}\) is Lorentzian evolution reconstructed from the
positive semigroup. The joint law itself is neither unitary nor nonunitary:
those are predicates of specified arrows on specified inner-product
carriers.

The mass-gap datum is therefore not a spectral gap of the unitary history
shift. It is the strict compression angle

$$
\|T^n(I-Q)\|
=
\|J_0^*\mathscr U_{\mathrm{hist}}^nJ_0(I-Q)\|<1
\tag{PFA7e}
$$

at fixed physical slab thickness, followed by the logarithmic generator and
OS/Poincare identifications below. This is the exact sense in which a
whole-level relation, a lossy local presentation, Euclidean attenuation, and
unitary clock time can coexist without any one of them causing the others.

The orthogonal component omitted by the slice presentation is itself a
canonical operator. Define the time-zero prediction residue

$$
\mathcal R_n^{\mathrm{past}}
:=
(I-e_0)\mathscr U_{\mathrm{hist}}^nJ_0.
\tag{PFA7f}
$$

Here \(e_0\) is the projection onto functions of \(X_0\), not the projection
onto the entire past algebra. For the future endpoint observable
\(J_nf\), however, the Markov property makes those two predictors agree:

$$
\mathbb E[J_nf\mid\mathcal P_0]
=
e_0J_nf
=
J_0T^nf.
\tag{PFA7f1}
$$

Without reversibility the exact Gramian is
\(I-(T^*)^nT^n\); under the standing reversible hypothesis this becomes

$$
\boxed{
(\mathcal R_n^{\mathrm{past}})^*\mathcal R_n^{\mathrm{past}}
=
I-(T^*)^nT^n
=
I-T^{2n}.}
\tag{PFA7g}
$$

Equivalently, for every \(f\in L^2(\nu)\),

$$
\boxed{
\|f\|^2
=
\|T^nf\|^2
+
\|\mathcal R_n^{\mathrm{past}}f\|^2.}
\tag{PFA7h}
$$

Thus the unitary history norm splits into its presentable slice prediction
and an orthogonal residue. What is conserved is this Hilbert norm on the
declared dilation, not an information substance. On the nonfixed carrier, a
uniform lower frame for (PFA7g) at one fixed physical depth is equivalent to
strict transfer attenuation there. This identifies the algebraic location
of the candidate gap without deriving its lower bound or calling the residue
entropy, an outcome, or ontological chance. The successive-depth resolution
of the same operator is developed in
[[reverse-prediction-residue-archive/inq|Reverse-Prediction Residue Archive]];
that archive uses the opposite operator product for its reversed prediction
orientation before reversibility makes the two products equal. The
two-boundary bridge residue used below is smaller because both endpoints are
available to the predictor.

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

### The angle is the optimal two-block variance factor

The pair floor (PFA15) has an exact conditional-variance meaning. For every
\(F\in\mathscr H\),

$$
\langle F,G_{i,j}F\rangle
=
\|F-e_-F\|^2+\|F-e_+F\|^2.
\tag{PFA15a}
$$

Consequently,

$$
\boxed{
\|F-RF\|^2
\leq
\frac{1}{1-c_F(i,j)}
\left(
\|F-e_-F\|^2+\|F-e_+F\|^2
\right).}
\tag{PFA15b}
$$

In the classical case the two terms on the right are expected conditional
variances, while \(\|F-RF\|^2\) is the residual variance after conditioning
on the common sigma-algebra. Provided at least one reduced endpoint range is
nonzero, the sharp two-block variance-factorization constant is therefore

$$
C_{\mathrm{var}}^*(d;a)
=
\frac{1}{1-c_F(d;a)}.
\tag{PFA15c}
$$

Combining this identity with (PFA24) gives a second exact presentation of the
energy edge:

$$
\boxed{
\Delta_E
=
\frac{\hbar c}{da}
\log\frac{C_{\mathrm{var}}^*(d;a)}
{C_{\mathrm{var}}^*(d;a)-1}.}
\tag{PFA15d}
$$

The apparent divergence

$$
C_{\mathrm{var}}^*(1;a)
\sim
\frac{\hbar c}{a\Delta_E}
\qquad(a\downarrow0)
\tag{PFA15e}
$$

is the correct adjacent-slice scaling of a finite continuum gap. It is not a
loss of the gap. At fixed positive physical slab thickness, a
volume-uniform finite constant is instead the correct certificate.
[[two-slice-innovation-geometry/inq|Two-Slice Innovation Geometry]] derives
this theorem for a general pair law and supplies a local-to-global
innovation test for its coefficient.

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

The kernel ledger must remain explicit. When \(T=e^{-aH_T/(\hbar c)}\), the
finite-depth transfer \(T^d\) is injective and has dense range even when it is
not unitary or onto. Exact loss occurs in the conditional expectations
\(e_\pm\), not in the supported attenuation \(T^d\). The mass-gap predicate is
the **uniform** norm decay of \(T^d\) on the nonfixed carrier; it is not the
appearance of a finite-depth kernel. After OS reconstruction the same
self-adjoint \(H_T\) also defines unitary Lorentzian clock transport. The exact
three-arrow separation is recorded in
[[conservation-of-causal-charge/unitarity-and-ontological-time#Euclidean attenuation is not the forgetting wall|the attenuation ledger]].

This is the promised reversal tactic in exact form. One may begin with the relative geometry of two information subspaces, take the supported positive return, and recover a generator. In the stationary Markov realization this recovers a supplied transfer Hamiltonian and is therefore a reformulation, not yet an independent proof.

### The paired-wall short is a hyperbolic tangent

Apply [[contemporary-puzzles/yang-mills-mass-gap/shorted-response-filtration-and-the-leak-cocycle#Paired walls produce an exact tangential response|the paired-wall shorting theorem]] to \(q,p\) on the reduced history comparison carrier \(\mathscr H_0:=(I-R)\mathscr H\), and write \(I_0\) for its identity. The equal-weight response retained by the future wall is

$$
\boxed{
\Lambda_{i,j}
:=
S_{q\mathscr H}\!\left((I_0-q)+(I_0-p)\right)\big|_{q\mathscr H}
=
(I-qpq)(I+qpq)^{-1}.}
\tag{PFA20a}
$$

The whole operator inside the short is exactly \(G_{i,j}|_{\mathscr H_0}\). The short acts on the centered future-history carrier \(q\mathscr H\); the identities in the last Cayley expression are the identity of that carrier. Its endpoint compression, not the uncompressed history operator, is the Cayley transform of the physical transfer return:

$$
\boxed{
(J_j^0)^*\Lambda_{i,j}J_j^0
=
(I-T^{2d})(I+T^{2d})^{-1}
=
\tanh\!\left(\frac{daH_T}{\hbar c}\right).}
\tag{PFA20b}
$$

Hence, on the centered endpoint carrier and with the same functional-calculus domain convention as (PFA20),

$$
H_T\big|_{(1-Q)L^2(\nu)}
=
\frac{\hbar c}{da}\,
\operatorname{artanh}\!\left((J_j^0)^*\Lambda_{i,j}J_j^0\right),
\qquad
\inf\sigma\!\left(\Lambda_{i,j}\big|_{q\mathscr H}\right)
=
\frac{1-\rho^{2d}}{1+\rho^{2d}}
=
\tanh\!\left(\frac{da\Delta_E}{\hbar c}\right).
\tag{PFA20c}
$$

Here \(\Delta_E\) is the centered energy edge defined in (PFA23). Thus \(\Lambda_{i,j}\) is a bounded dimensionless distinction response, not the Hamiltonian itself. Equation (PFA20b) is an exact reformulation of the already supplied transfer operator; it does not independently prove a gap. Nor does positivity alone make \(e^{-s\Lambda_{i,j}}\) the path-space Markov evolution: that stronger conclusion requires the closed Markov-form hypotheses isolated by [[trace-dirichlet-descent/inq|Trace Dirichlet Descent]].

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

There is a pair-level entropy route that uses the same two descents. If
normalized densities \(h\) on history space obey

$$
\operatorname{Ent}_\mu(h)-\operatorname{Ent}_\mu(Rh)
\leq
C_{\mathrm{ent}}
\sum_{\epsilon\in\{-,+\}}
\left[
\operatorname{Ent}_\mu(h)-\operatorname{Ent}_\mu(e_\epsilon h)
\right],
\tag{PFA26a}
$$

then the expansion \(h=1+\varepsilon F\) gives

$$
\|F-RF\|^2
\leq
C_{\mathrm{ent}}
\left(
\|F-e_-F\|^2+\|F-e_+F\|^2
\right).
\tag{PFA26b}
$$

The optimality of (PFA15b) therefore implies

$$
c_F
\leq
1-\frac{1}{C_{\mathrm{ent}}}.
\tag{PFA26c}
$$

This is a sufficient nonlinear certificate, not an identity between the
entropy and Hilbert constants. Classical spatial-mixing theorems establish
related block factorizations for specified Gibbs spin systems, while
finite-dimensional noncommuting conditional expectations admit their own
approximate-tensorization theorems. Neither result automatically covers a
compact-gauge Wilson vacuum, an infinite Type-III algebra, or the physical
transfer operator.

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

The square in (PFA28) is also typed. Maximal-correlation squared is the local
Hessian coefficient for a one-channel relative-entropy contraction, but it
need not equal the optimal global relative-entropy coefficient. The pair
factorization in (PFA15b) instead contains \(1-c_F\), whereas the alternating
return contains \(1-c_F^2\). Treating those three constants as interchangeable
would conflate a frame, a return, and a nonlinear convexity statement.

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

The commutative path theorem is a prototype, not a demand for fundamental
stochasticity. The two-slice geometry itself has an exact Type-III-compatible
form. Let \(M\) be a sigma-finite von Neumann algebra, \(\varphi\) a faithful
normal state, and \(N\subset M\). By
[[library/conditional-expectations-in-von-neumann-algebras/inq|Takesaki's
theorem]], invariance of \(N\) under the modular group of \(\varphi\) is
equivalent to the existence of a normal \(\varphi\)-preserving expectation
\(E_N:M\to N\). On the symmetric standard-form embedding

$$
\jmath_\varphi(x)
:=
\Delta_\varphi^{1/4}x\Omega_\varphi,
\qquad
p_N\jmath_\varphi(x)
:=
\jmath_\varphi(E_Nx),
\tag{PFA32}
$$

\(p_N\) is the orthogonal projection onto
\(\overline{\jmath_\varphi(N)}\). Conditional descent therefore remains
literally a projection without a trace or density matrix. Modular flow is
the compatibility condition for that descent; it has not thereby become
physical clock time.

There is also an exact two-slice correspondence for a normal unital
\(\varphi\)-preserving GNS-symmetric completely positive map \(\Phi\). If
\(T_G(x\Omega_\varphi)=\Phi(x)\Omega_\varphi\), its Stinespring
correspondence

$$
\mathscr K_\Phi
:=
\overline{M\odot H_\varphi},
\qquad
\langle a\otimes\xi,b\otimes\eta\rangle
:=
\langle\xi,\Phi(a^*b)\eta\rangle
\tag{PFA32a}
$$

contains two slice isometries

$$
J_0(x\Omega_\varphi)=x\otimes\Omega_\varphi,
\qquad
J_1\eta=1\otimes\eta,
\qquad
J_0^*J_1=T_G.
\tag{PFA32b}
$$

The joint correspondence therefore carries the exact residual map

$$
L_{1\mid0}:=(I-J_0J_0^*)J_1,
\qquad
\boxed{I-T_G^*T_G=L_{1\mid0}^*L_{1\mid0}.}
\tag{PFA32b1}
$$

This is the Type-III-compatible source of the stage analysis used in
[[transported-response-observability-solder/inq|the transported-response
theorem]]. It becomes a physical transfer defect only after $T_G$ is
independently identified with the physical endpoint transfer; a generic
UCP correspondence is not clock dynamics.

Hence

$$
\frac12\|J_0\xi-J_1\xi\|^2
=
\langle\xi,(I-T_G)\xi\rangle.
\tag{PFA32c}
$$

This is the noncommutative counterpart of the stationary edge integral.
If \(T_G\geq0\), \(P\) projects onto its fixed carrier, and
\(e_k=J_kJ_k^*\), then their common range is the image of \(P\) and

$$
c_F
=
\|(e_0-e_0\wedge e_1)(e_1-e_0\wedge e_1)\|
=
\|T_G-P\|.
\tag{PFA32d}
$$

For arbitrary contractions the orientation-even return has the exact
singular-value bound

$$
I-T_G^*T_G
\geq
\left(1-\|T_G-P\|^2\right)(I-P).
\tag{PFA32e}
$$

For \(T_s=e^{-sL}\), \(L\geq0\), this is a gap statement precisely when
\(\|T_s-P\|=e^{-s\lambda}\). A self-adjoint channel with negative spectrum
needs this semigroup or positivity qualification: maximal correlation sees
the absolute spectral radius.

Two preserving expectations give an intrinsic Type-III process without
postulating a full stochastic history. If \(E_-,E_+\) have standard-form
projections \(p,q\) and \(r=p\wedge q\), then the UCP map
\(\Psi=E_-E_+E_-\) has implementation \(pqp\), and

$$
I-pqp
\geq
(1-c_F^2)(I-r),
\qquad
c_F=\|pq-r\|.
\tag{PFA32f}
$$

Its Poissonization \(e^{t(\Psi-I)}\) is a genuine quantum Markov semigroup
with dimensionless edge \(1-c_F^2\). This exact construction still does not
identify its fixed carrier with the physical vacuum or its parameter with
clock time.

Entropy requires another typing step. Araki relative entropy linearizes on
regular faithful state curves to the BKM state-tangent metric. It does not
linearize directly to the GNS or symmetric KMS \(L^2\) norm used above.
Passing from a BKM contraction to (PFA32e) requires an explicit score
transform and detailed-balance intertwiner; no universal converse
comparison may be assumed. The finite-dimensional noncommuting
approximate-tensorization theorem of
[[library/approximate-tensorization-of-the-relative-entropy-for-noncommuting-conditional-expectations/inq|Bardet--Capel--Rouze]]
does not by itself extend that inference to Type III.

Raw nested Lorentzian local algebras are also the wrong cuts.
Reeh--Schlieder makes \(\overline{A(O)\Omega}\) the whole vacuum Hilbert
space, so their vacuum-generated subspaces have trivial Friedrichs
geometry. The same density and separation obstruct a
vacuum-preserving expectation from a larger local algebra onto a proper
nested one. A Euclidean regulator, OS slab, interface algebra, RG channel,
or different-carrier correspondence is therefore load bearing.

The decisive physical certificate remains a typed slice isometry \(J_\ell\)
and

$$
J_\ell^*q p qJ_\ell
=
e^{-2\ell H/(\hbar c)}
\tag{PFA32g}
$$

on the vacuum-reduced physical slice. A twisted spectral triple may help
construct the slice metric or comparison operator, but it contributes to
the gap only if it proves (PFA32g), or a domain-correct inequality strong
enough to replace it.

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
