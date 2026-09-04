---
inq.module: "collared-quasi-factorization-and-surface-response"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Collared Quasi-Factorization and Surface Response

A single two-block inequality on the whole Euclidean cylinder is enough to
force a midpoint bridge floor: combine the two separated end collars into one
block and take the open interior as the other. Conditional on complete
analyticity, Cesi's entropy quasi-factorization applies at finite regulator
after the Wilson plaquette law is retyped as a bounded finite-range
interaction of compact cell spins. The remaining obstruction is quantitative,
not categorical: Cesi's published
\(L^\infty\) certificate counts the transverse boundary cells and loses
uniformity when its complete-analyticity rate has finite physical scaling.
The sharper target is a tensorizing \(L^2\) surface-response angle derived
from the Wilson action.

**Status: [EXACT] for the two-block-to-bridge reduction, the Wilson cell-spin
encoding, and the Friedrichs-angle formulation; [ESTABLISHED INPUT] for
Cesi's quasi-factorization under complete analyticity; [OBSTRUCTION] for the
surface-cardinality loss in that sufficient estimate under the stated
scaling; [OPEN] for a
regulator-, volume-, boundary-, and sector-uniform Hilbertian response bound
along the four-dimensional Yang--Mills continuum trajectory.**

## One disconnected block is enough

Let a finite cylinder have time cells

$$
\Lambda=\{-p,\ldots,2n+p\}\times\Sigma,
$$

where \(\Sigma\) is a finite spatial cross-section. Choose \(1\leq r<n\)
and put

$$
\begin{aligned}
A_-&=\{-p,\ldots,r\}\times\Sigma,\\
A_0&=\{1,\ldots,2n-1\}\times\Sigma,\\
A_+&=\{2n-r,\ldots,2n+p\}\times\Sigma,\\
D&:=A_-\cup A_+.
\end{aligned}
\tag{CQ1}
$$

Thus \(D\cup A_0=\Lambda\), the blocks overlap in collars of width \(r\),
and \(D\) omits the midpoint cell \(n\times\Sigma\). For a block \(A\), write

$$
\operatorname{Var}_A(F)
:=
\operatorname{Var}\!\left(F\mid\mathcal F_{A^c}\right).
\tag{CQ2}
$$

Suppose the whole-cylinder law \(\mu\) satisfies the two-block inequality

$$
\operatorname{Var}_\mu(F)
\leq
C_2\,\mathbb E_\mu\!\left[
\operatorname{Var}_D(F)+\operatorname{Var}_{A_0}(F)
\right].
\tag{CQ3}
$$

Let \(X_n\) be the physical state of the midpoint slice and take
\(F=f(X_n)\). Resampling \(D\) cannot change \(F\), so

$$
\operatorname{Var}_D(f(X_n))=0.
\tag{CQ4}
$$

The complement \(A_0^c=D\setminus A_0\) contains the two marked endpoint
slices and may also contain outer preparation variables. Hence its
sigma-algebra is at least as informative as
\(\sigma(X_0,X_{2n})\). Conditional variance decreases when the conditioning
sigma-algebra is enlarged, giving

$$
\mathbb E\operatorname{Var}_{A_0}(f(X_n))
\leq
\mathbb E\operatorname{Var}
\!\left(f(X_n)\mid X_0,X_{2n}\right).
\tag{CQ5}
$$

Equations (CQ3)--(CQ5) prove

$$
\boxed{
B_n^{\mathrm{br}}
\geq C_2^{-1}Q,}
\tag{CQ6}
$$

on centered midpoint functions. In a sectorized version, \(Q\) removes the
declared common fixed subspace, and the sector must reduce both block
expectations. Equality between the middle-block compression and the bridge is
unnecessary; the one-sided inequality has the useful direction. This permits
the estimate to be proved on a larger finite cylinder with ordinary fixed
exterior data and then passed to the stationary Perron preparation limit.

If a literal three-block inequality is wanted, it follows on an open cylinder
either by tensorizing the conditional entropy on the separated components of
\(D\), or by applying a boundary-uniform two-block theorem once to
\((A_-,A_0\cup A_+)\) and again conditionally to \((A_0,A_+)\). Neither
extra step is needed for (CQ6).

## Cesi supplies the finite-regulator theorem

Cesi proves entropy quasi-factorization for two weakly dependent
sigma-algebras and applies it to finite-range summable Gibbs interactions
under Dobrushin--Shlosman complete analyticity. No topology is imposed on the
single-spin space, so compact continuous spins are included. In the present
notation, the result has the form

$$
\operatorname{Ent}_\mu(g)
\leq
C_2\,\mathbb E_\mu\!\left[
\operatorname{Ent}_D(g)+\operatorname{Ent}_{A_0}(g)
\right],
\qquad g\geq0.
\tag{CQ7}
$$

The estimate is uniform in the finite region and exterior configuration once
the complete-analyticity constants and the geometry entering its smallness
condition are fixed. Linearizing (CQ7) at \(g=1\) gives (CQ3).

For an interaction of range \(R_J\), let

$$
\ell
:=
d(\Lambda\setminus D,\Lambda\setminus A_0),
\qquad
b
:=
\left|\partial_{R_J}^{+}A_0\cap\Lambda\right|.
\tag{CQ8}
$$

Combining Cesi's complete-analyticity mixing estimate with his
quasi-factorization lemma gives a sufficient dependence defect of the form

$$
\varepsilon
\leq
e\,bK e^{-\alpha_{\mathrm{CA}}\ell}.
\tag{CQ9}
$$

One explicit proof-level condition is

$$
\vartheta(\varepsilon)
:=
\frac{84\varepsilon}{(1-\varepsilon)^2}<1,
\qquad
C_2\leq\frac{1}{1-\vartheta(\varepsilon)}.
\tag{CQ10}
$$

Here \(\alpha_{\mathrm{CA}}\) is a lattice-distance mixing rate, not a
physical mass. The exact hypothesis is complete analyticity under arbitrary
boundary conditions; ordinary covariance decay in one infinite-volume state
does not suffice. See
[[library/quasi-factorization-of-the-entropy-and-logarithmic-sobolev-inequalities-for-gibbs-random-fields/inq|Quasi-Factorization of the Entropy and Logarithmic Sobolev Inequalities for Gibbs Random Fields]]
and
[[library/the-equivalence-of-the-logarithmic-sobolev-inequality-and-the-dobrushin-shlosman-mixing-condition/inq|The Equivalence of the Logarithmic Sobolev Inequality and the Dobrushin--Shlosman Mixing Condition]].

## Wilson plaquettes are finite-range cell interactions

Let \(G=SU(N)\) and attach to each lattice site \(x\) the tuple of its
positively oriented outgoing links,

$$
\sigma_x
:=
(U_{x,1},\ldots,U_{x,4})\in G^4,
\qquad
\nu_x=\operatorname{Haar}_G^{\otimes4}.
\tag{CQ11}
$$

The plaquette based at \(x\) in the \((\mu,\nu)\)-plane is

$$
U_{x,\mu}
U_{x+\hat\mu,\nu}
U_{x+\hat\nu,\mu}^{-1}
U_{x,\nu}^{-1}.
\tag{CQ12}
$$

It depends on exactly the three cell spins

$$
\{x,x+\hat\mu,x+\hat\nu\}.
\tag{CQ13}
$$

In the lattice \(\ell^\infty\) metric this support has diameter one. The
Wilson action is therefore a bounded, range-one, three-cell interaction over
the product prior \(\bigotimes_x\nu_x\). Gauge redundancy is an invariance of
this full-support measure, not a hard support constraint. Fixing exterior
links reduces the arity of boundary factors and does not enlarge the range.

This closes the finite-regulator **interaction-typing** gap in the earlier
raw-link formulation: Cesi permits finite-range many-body interactions, so a
new pair-potential factor-graph theorem is not required for (CQ7). It does not
close the complete-analyticity, gauge-sector, stationary-limit, or continuum
parts of the problem.

An alternative is to make an entire spatial slice one spin. Temporal
plaquettes then give a nearest-neighbor pair potential in a one-dimensional
chain. That encoding proves only a finite-volume existence statement: the
spin space grows with transverse volume and the oscillation of the slice
potential is extensive, so its constants are not uniform in the limit of
interest.

## The published certificate pays for surface area

For the cover (CQ1), \(R_J=1\),

$$
\ell=r+1,
\qquad
b=2|\Sigma|.
\tag{CQ14}
$$

Thus Cesi's sufficient smallness test contains

$$
2|\Sigma|K e^{-\alpha_{\mathrm{CA}}(r+1)}.
\tag{CQ15}
$$

At fixed regulator it can be made small by taking

$$
r
\gtrsim
\frac{\log|\Sigma|+O(1)}{\alpha_{\mathrm{CA}}}.
\tag{CQ16}
$$

But on an isotropic continuum sequence with fixed physical transverse size,
\(|\Sigma|\asymp a^{-3}\). Test the favorable finite-physical-scale regime
in which \(K\) has no compensating \(a^3\) suppression and
\(\alpha_{\mathrm{CA}}(a)r(a)=O(1)\); for example, the certificate rate might
track a finite inverse correlation length as
\(\alpha_{\mathrm{CA}}(a)\asymp a/\xi_{\mathrm{phys}}\), while a fixed
physical collar has \(r(a)\asymp\delta/a\). Then the exponential in (CQ15)
is only of order \(e^{-\delta/\xi_{\mathrm{phys}}}\), whereas the displayed
surface factor grows as \(a^{-3}\). Thus this sufficient bound becomes
vacuous under that scaling. Complete analyticity is stronger than ordinary
two-point correlation decay, so the scaling itself is an assumption to be
proved, not an entailment of finite physical correlation length. The same
certificate also loses volume uniformity at fixed regulator unless its other
constants compensate the growth of \(|\Sigma|\).

This is not a no-go theorem for the desired quasi-factorization. Independent
bridges already show why: maximal correlation tensorizes by a maximum, while
an \(L^\infty\) telescoping proof can pay once for every boundary cell. The
surface-area growth may be loss in the certificate rather than loss of the
physical bridge floor.

## The Hilbertian surface-response target

On \(L^2(\mu)\), let

$$
P_D:=\mathbb E[\,\cdot\mid\mathcal F_{D^c}],
\qquad
P_0:=\mathbb E[\,\cdot\mid\mathcal F_{A_0^c}],
\tag{CQ17}
$$

and let \(R\) be the orthogonal projection onto
\(\operatorname{Ran}P_D\cap\operatorname{Ran}P_0\). For the unreduced finite
Wilson carrier, strict positivity relative to product Haar and the disjoint
retained coordinate sets make this common range the constants. A sectorized
claim additionally requires the sector projection to reduce both \(P_D\) and
\(P_0\), followed by an identification of their meet inside that sector;
arbitrary exterior data need not preserve the symmetry defining it. Define
the reduced Friedrichs cosine

$$
c_F(D,A_0)
:=
\left\|(P_D-R)(P_0-R)\right\|.
\tag{CQ18}
$$

The two-projection theorem gives the exact whole-law inequality

$$
\boxed{
(I-P_D)+(I-P_0)
\geq
(1-c_F(D,A_0))(I-R).}
\tag{CQ19}
$$

For a centered midpoint observable \(F=f(X_n)\), one has
\(P_DF=F\) and \(RF=0\). Since the norm in (CQ18) is unchanged on taking
adjoints,

$$
\|(P_0-R)F\|
\leq
c_F(D,A_0)\|F\|.
\tag{CQ19a}
$$

Direct compression therefore sharpens the general two-projection edge:

$$
\boxed{
B_n^{\mathrm{br}}
\geq
(1-c_F(D,A_0)^2)Q.}
\tag{CQ20}
$$

For a product of independent transverse bridges, the reduced maximal
correlation in (CQ18) is the maximum of the component correlations. This is
the desired surface scaling. The finite-state
[[collared-quasi-factorization-and-surface-response/receipts/collared_surface_response_receipt.py|surface-response receipt]]
and its
[[collared-quasi-factorization-and-surface-response/receipts/collared-surface-response-receipt-output.txt|recorded output]]
check the two-projection edge \(1-c_F\), the sharper midpoint bridge floor
\(1-c_F^2\), and maximum tensorization by direct weighted-matrix arithmetic.
They certify those identities only; they do not establish a Wilson measure,
a Cesi hypothesis, or any continuum limit. Interacting Wilson columns do not
tensorize, so the new analytic target is to derive

$$
\sup_{a,L,p,\tau,\mathfrak s}
c_F^{(a,L,p,\tau,\mathfrak s)}(D,A_0)
\leq
\rho_*<1
\tag{CQ21}
$$

at fixed physical collar width, uniformly in regulator \(a\), transverse
volume \(L\), preparation depth \(p\), exterior data \(\tau\), and every
neutral sector \(\mathfrak s\) proved to reduce both block expectations. An
equivalent formulation may instead take the norm on an explicitly declared
restricted midpoint subspace.

Equation (CQ21) is a stopping condition, not yet an explanation. In a
stationary Markov chain, the corresponding one-sided collar angle is exactly
\(\|T^{r+1}Q\|\); bounding it via the unknown transfer spectrum would assume
the gap. A noncircular proof must instead construct an \(L^2\)
boundary-response analysis from plaquette incidence, covariant derivatives,
Hessian or Fisher response, and finite-range geometry, then prove that it
dominates the relevant reduced projection product.

The exact bounded response on the retained central-core carrier is already
visible. Put

$$
\mathcal H_{\mathrm{core}}:=(P_D-R)L^2(\mu),
\qquad
K_{\mathrm{surf}}:=(P_0-R)|_{\mathcal H_{\mathrm{core}}}.
\tag{CQ22}
$$

Then \(\|K_{\mathrm{surf}}\|=c_F(D,A_0)\), and

$$
\mathcal B_{\mathrm{surf}}
:=
I_{\mathcal H_{\mathrm{core}}}
-K_{\mathrm{surf}}^*K_{\mathrm{surf}}
\tag{CQ23}
$$

has lower edge \(1-c_F(D,A_0)^2\). A genuinely explanatory comparison would
construct a positive response \(\mathcal R_{\mathrm{surf}}\) independently
of \(K_{\mathrm{surf}}\) and prove

$$
\mathcal B_{\mathrm{surf}}
\geq
\eta_*\mathcal R_{\mathrm{surf}},
\qquad
\mathcal R_{\mathrm{surf}}\geq\gamma_*I,
\qquad
\eta_*,\gamma_*>0,
\tag{CQ24}
$$

uniformly in the parameters of (CQ21). If the primitive geometric response
is an unbounded Hessian or Dirichlet-to-Neumann operator
\(\mathcal N_{\mathrm{surf}}\), it cannot be placed directly below the bounded
defect (CQ23). One first needs a same-carrier bounded transform such as

$$
\mathcal R_{\mathrm{surf}}
=
I-e^{-2\delta\mathcal N_{\mathrm{surf}}},
\tag{CQ25}
$$

together with an explicit score or flux map. A linear Hessian estimate is
also insufficient unless a comparison theorem extends it to the complete
nonlinear \(L^2\) distinction carrier. Defining
\(\mathcal R_{\mathrm{surf}}\) from the transfer spectrum or from
\(K_{\mathrm{surf}}\) would merely rename the gap.

The distinction of time types is exact here. The whole law \(\mu\) is not an
evolution operator and therefore is neither unitary nor nonunitary. The maps
\(P_D\) and \(P_0\) are noninvertible presentation arrows on a derived
Hilbert carrier; their relative angle measures what neither presentation can
make jointly definite. Reflection-positive reconstruction independently
supplies the local clock carrier and its reversible unitary evolution. Once
the bridge operator is identified with the Euclidean transfer on that
carrier, its floor bounds the clock generator's positive edge. Descent,
attenuation, reconstruction, and clock evolution are successive typed arrows,
not four descriptions of one map.

## Claim boundary

- Cesi's theorem closes the finite-regulator many-body interaction typing; it
  does not prove complete analyticity for four-dimensional \(SU(N)\) Wilson
  theory along the weak-bare-coupling continuum trajectory.
- The strong-coupling Wilson logarithmic-Sobolev theorem concerns a
  link-gradient Langevin form on periodic volumes. It is not already the
  boundary-uniform two-block conditional inequality (CQ7).
- Exponential clustering in one vacuum is weaker than exponential decay
  under arbitrary boundary conditions. The latter is the gauge-theoretic
  input used by Chatterjee's confinement criterion.
- A finite-group weak-coupling decay theorem does not transfer to continuous
  compact \(SU(N)\), and covariance decay alone is not entropy
  quasi-factorization.
- A subunit Friedrichs cosine is a dimensionless bridge rate. Converting it
  to energy still requires a fixed physical slab thickness and the
  transfer/OS/Poincare reconstruction chain; no numerical mass has been
  derived here.

## Dependencies

- [[three-block-bridge-factorization/inq|Three-Block Bridge Factorization]]
- [[bridge-data-augmentation-solder/inq|Bridge Data-Augmentation Solder]]
- [[contemporary-puzzles/yang-mills-mass-gap/oriented-descent-angle-and-emergent-symmetry|Oriented Descent Angle and Emergent Symmetry]]
- [[hessian-response-geometry/inq|Hessian Response Geometry]]
- [[gauge-boundary-frame-gluing/inq|Gauge Boundary-Frame Gluing]]
- [[strong-coupling-gap-and-continuum-crossover/inq|Strong-Coupling Gap and Continuum Crossover]]
- [[library/quasi-factorization-of-the-entropy-and-logarithmic-sobolev-inequalities-for-gibbs-random-fields/inq|Quasi-Factorization of the Entropy and Logarithmic Sobolev Inequalities for Gibbs Random Fields]]
- [[library/the-equivalence-of-the-logarithmic-sobolev-inequality-and-the-dobrushin-shlosman-mixing-condition/inq|The Equivalence of the Logarithmic Sobolev Inequality and the Dobrushin--Shlosman Mixing Condition]]
- [[library/a-probabilistic-mechanism-for-quark-confinement/inq|A Probabilistic Mechanism for Quark Confinement]]
- [[library/correlation-decay-for-finite-lattice-gauge-theories-at-weak-coupling/inq|Correlation Decay for Finite Lattice Gauge Theories at Weak Coupling]]
- [[library/on-sequences-of-pairs-of-dependent-random-variables/inq|On Sequences of Pairs of Dependent Random Variables]]
