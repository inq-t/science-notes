# When a Scalar Response Law Determines a Spectral Bound

A calibrated response along one direction—even its entire nonlinear entropy profile, together with a fixed total response—does not determine the weakest response on the same carrier. A scalar law becomes a spectral law only when an additional relation controls all remaining directions. Irreducibility of the actual response symmetry, quantitative coverage, or genuine saturation under a proved ceiling can supply such a relation. Multiplicity spaces and poorly weighted directions are where that inference can fail.

**Status: exact finite counterexample and conditional operator theorems.** No Yang--Mills continuum bound is proved here. [[relative-response-spectrum|The relative-response spectrum]] owns the prior definition \(g(u,Rv)=q(u,v)\); this note asks when partial scalar information determines that already normalized operator.

## A fixed response profile with an arbitrarily weak direction

Take one fixed eight-point space \(X=\{-1,1\}^3\), with uniform law \(\mu\) and Hilbert norm \(L^2(\mu)\). For \(0<\varepsilon\le1/2\), define
\[
K_\varepsilon(z\mid x)
=\prod_{i=1}^3\frac{1+k_i x_i z_i}{2},
\qquad
k_1^2=\frac12,\quad
k_2^2=1-\varepsilon,\quad
k_3^2=\frac{\varepsilon}{2-\varepsilon},
\qquad k_i\ge0.
\tag{RM1}
\]
Every entry is strictly positive. The channel is symmetric, stochastic and positive as a Hilbert operator; it preserves \(\mu\) and is completely positive on the commutative observable algebra. The joint law is \(\mu(x)K_\varepsilon(z\mid x)\), so \(K_\varepsilon f(z)=\mathbb E[f(X)\mid Z=z]\) is an actual conditional prediction, not a matrix without a state.

The residual-response operator
\[
B_\varepsilon=I-K_\varepsilon^*K_\varepsilon
\tag{RM2}
\]
has quadratic form equal to the expected conditional variance of \(f(X)\) given \(Z\). On the orthonormal Walsh basis \(\chi_F(x)=\prod_{i\in F}x_i\),
\[
K_\varepsilon\chi_F
=\left(\prod_{i\in F}k_i\right)\chi_F,\qquad
B_\varepsilon\chi_F
=\left(1-\prod_{i\in F}k_i^2\right)\chi_F .
\tag{RM3}
\]
The empty character is its unique zero mode. Every nonconstant direction is detected.

For the distinguished unit tangent \(s=\chi_{\{1\}}\), and the ordinary Hilbert-space operator trace over **all eight directions**,
\[
\boxed{
\|K_\varepsilon s\|^2
=\langle s,B_\varepsilon s\rangle=\frac12,\qquad
\operatorname{Tr}B_\varepsilon
=8-\prod_{i=1}^3(1+k_i^2)=5.}
\tag{RM4}
\]
Nevertheless,
\[
\boxed{
\min_{f\perp1,\ \|f\|=1}\langle f,B_\varepsilon f\rangle
=\varepsilon\longrightarrow0.}
\tag{RM5}
\]
The largest product in (RM3) over nonempty \(F\) is \(k_2^2=1-\varepsilon\). Neither the carrier, state norm, number of directions, balanced tangent nor total response is changing. The channel changes in directions those scalar data do not determine. The trace in (RM4) is a spectral moment, not thermodynamic entropy.

The entire selected nonlinear profile is fixed too. Put
\[
\frac{d\mu_\theta}{d\mu}(x)
=\frac{e^{\theta x_1}}{\cosh\theta}
=1+m x_1,\qquad m=\tanh\theta .
\]
Its output density is \(1+k_1m z_1\); the other two bits remain uniform. With
\[
d(u)=\tfrac12\big[(1+u)\log(1+u)+(1-u)\log(1-u)\big],
\]
every finite \(\theta\) gives
\[
D(\mu_\theta\Vert\mu)=d(m),\qquad
D((K_\varepsilon)_*\mu_\theta\Vert\mu)=d(k_1m).
\tag{RM6}
\]
Both entropies, their difference, and the one-parameter Fisher profiles
\[
G_{\rm in}(\theta)=\operatorname{sech}^2\theta,\qquad
G_{\rm out}(\theta)=
\frac{k_1^2(1-m^2)^2}{1-k_1^2m^2}
\tag{RM7}
\]
are independent of \(\varepsilon\). This is genuine information geometry, but not the complete response geometry.

This strengthens the [[global-local-response-reconstruction/yang-mills-balanced-fisher-grain#Exact firewall: one balanced tangent is not a gap|balanced-grain counterexample]] by fixing the full finite trace and the entire chosen nonlinear profile. It does not show nonuniqueness after a complete wall, state, readout and dynamics have all been fixed. It identifies the directions a scalar matching law leaves undetermined.

## A relation that forces the directions together

Let a group act orthogonally or unitarily on a nonzero finite-dimensional carrier \(V\). Suppose the representation is irreducible and **both** \(q\) and its independent metric \(g\) are invariant. Then
\[
\boxed{R=cI,\qquad c=\frac{\operatorname{Tr}R}{\dim V}.}
\tag{RM8}
\]
Proof: invariance makes the self-adjoint \(R\) commute with the action. Each eigenspace is invariant; irreducibility permits only one. This proof also applies to real irreducible representations, without requiring their entire commutant to consist of real scalars.

Under these hypotheses one unit tangent with \(q(v,v)=c>0\) fixes the full lower edge. The extra content is the relation between directions, not the numerical equality alone.

[[algebra/exceptional-context-response#A complete family has a strict finite lower frame|The exceptional context frame]] is an exact instance: an oriented retraction and the full invariant context family give \(R=(9/13)I\) on the trace-free Albert carrier. The prior operation need not itself be invariant under every presentation change; its constructed response can acquire an invariant form. This is a finite meaning of **symmetry of response emerging from comparison of oriented contexts**, not an irreversible-chronology theorem.

Averaging must be an actual construction, not a hidden change of object. For a compact group with normalized Haar measure, put \(\overline R=\int U_g^*RU_g\,dg=cI\) on an irreducible carrier. If an independent bound gives
\[
\|R-\overline R\|\le\eta<c,
\quad\text{then}\quad
\boxed{R\ge(c-\eta)I.}
\tag{RM9}
\]
Here \(c\) is the averaged scalar, fixed for example by the trace. If only one unit-direction value \(q(v,v)=a\) is known, the bound is instead \(R\ge(a-2\eta)I\).

The reference law in (RM1) is invariant under every permutation of its eight points, but the channel is not. Averaging \(B_\varepsilon\) over all point permutations gives exactly \((5/7)Q\), with \(Q\) the mean-zero projection: the standard seven-dimensional representation is irreducible and the trace is five. This is a **different response**. On its actual soft character,
\[
\|B_\varepsilon-(5/7)Q\|\ge5/7-\varepsilon.
\]
The comparison error prevents averaging from manufacturing a uniform lower bound for the original channel. A symmetric reference state alone does not make its readout equivariant.

## Multiplicity is an uncontrolled carrier, not a unit convention

For a complex irreducible finite representation \(V\) and a Hilbert multiplicity space \(M\), let the action on \(V\otimes M\) be \(U_g\otimes I_M\). Every bounded commuting self-adjoint response is
\[
R=I_V\otimes B,\qquad B=B^*\in B(M).
\tag{RM10}
\]
The group relates directions inside \(V\), but does not control \(B\). In particular \(Be_n=n^{-1}e_n\) on \(\ell^2(\mathbb N)\) is strictly positive on each nonzero vector and has zero lower edge. Exact internal equivariance survives while uniform stiffness fails.

A general compact-group decomposition has one \(B_\lambda\) for each irreducible type; the gap requires a uniform floor over all physical multiplicity spaces. Gauge transformations acting trivially on gauge-invariant observables impose no such restriction.

This is the finite-to-field difficulty in [[global-local-response-reconstruction/exceptional-context-analysis-of-gauge-gradients|the differentiated-context construction]]. An internal frame can identify a configuration-gradient form without controlling collective modes of the configuration law. Physical directions cannot be discarded as “multiplicity” because they invalidate a bound.

## Genuine saturation is another sufficient relation

If \(0\le R\le CI\) in a represented operator algebra, \(C>0\), and a **faithful** state satisfies \(\omega(R)=C\), then
\[
\boxed{R=CI.}
\tag{RM11}
\]
The positive operator \(CI-R\) has zero faithful expectation and vanishes. This is genuine saturation because the ceiling was proved independently. A normalized entropy quotient equal to one is not such a ceiling.

In finite dimension, if \(\omega(R)=\operatorname{Tr}(\sigma R)\), \(\sigma\ge mI>0\), \(\operatorname{Tr}\sigma=1\), and \(\delta=C-\omega(R)\), then
\[
\delta=\operatorname{Tr}\sigma(CI-R)
\ge m\operatorname{Tr}(CI-R)\ge m\|CI-R\|,
\qquad
R\ge\left(C-\frac{\delta}{m}\right)I .
\tag{RM12}
\]
Almost-saturation requires control of \(m\). This can deteriorate under refinement; an infinite-dimensional faithful normal density need not be bounded below by a positive multiple of the identity. [[global-local-response-reconstruction/quantitative-descent-and-the-shape-of-a-gap#The continuum condition belongs to the measured law|The escaping-soft-direction example]] shows how a direction with vanishing state weight can soften while faithful averages approach saturation.

## The simpler construction target

[[program-core/ruble-equations#RE3 — State–geometry equivalence|Ruble RE3]] distinguishes an all-tangent comparison from its scalar scale-channel contraction. The missing implication requires an independently derived rigidity relation such as (RM8), a quantitative comparison such as (RM9), or genuine saturation such as (RM11), on the complete relevant carrier.

The economical mass-gap target remains
\[
q_{\rm descent}\ge\kappa\,g_{\rm physical}
\quad\text{on the full nonvacuum carrier},\qquad \kappa>0,
\]
with a scale selector and physical reconstruction supplied independently. This specifies the missing theorem, not its proof. [[global-local-response-reconstruction/quantitative-descent-and-the-shape-of-a-gap|Quantitative descent]] owns the constructive gluing and positive-certificate routes. The task is to derive a global--local relation that forces this bound along the actual continuum trajectory.

“Scale gap” is useful terminology for that search, provided it does not mean a smallest spatial pixel or merely a bound on one logarithmic-scale tangent. The [[library/quantum-yang-mills-theory/inq|Clay target]] remains a complete nontrivial pure Yang--Mills theory with a physical vacuum gap; it contains no Higgs field. A common account of Higgs reduction, cosmology and Yang--Mills would be a further return, not a substitute.

The [[receipts/response_rigidity_receipt.py|finite receipt]] checks the channel, entropy and Fisher profiles, full trace and spectrum, averaging and saturation inequalities. It validates this test, not a physical mass prediction.
