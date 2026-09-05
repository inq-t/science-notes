# A Grain Is a Matched-Ledger Scale

A grain is not intrinsically a smallest length or a universal packet. It is the scale selected when two independently defined presentations of the same carrier are required to return the same dimensionless count. The reusable object is this typed comparison—carrier, ledgers, comparison map, and unique positive solution—not the numerical value returned by one cosmological application. Different carriers, states, cuts, and response laws should generally produce different grains.

**Status: [EXACT SCHEMA] for the matched-ledger equation and its uniqueness under the stated hypotheses; [CONDITIONAL] for each physical choice of carrier and ledgers; [OPEN] for a common upstream construction relating the cosmological and Yang--Mills applications.**

## The elementary construction

Let \(X\) be one declared carrier in state \(\omega\). Suppose it has:

- a dimensionless whole or boundary ledger \(\mathsf C(X,\omega)>0\);
- a \(d\)-dimensional measure \(V_d(X,\omega)\);
- a dimensionless response weight \(w(X,\omega)>0\) per effective cell; and
- a fixed geometric normalization \(v_d>0\).

A trial scale \(\ell>0\) presents the corresponding local ledger as

$$
\mathsf B(X,\omega;\ell)
:=
w(X,\omega)
\frac{V_d(X,\omega)}{v_d\ell^d}.
\tag{RG1}
$$

Both sides of the matching equation must count the same typed response:

$$
\mathsf C(X,\omega)
=
\mathsf B(X,\omega;\ell_X).
\tag{RG2}
$$

Then the selected grain is uniquely

$$
\boxed{
\ell_X^d
=
\frac{w(X,\omega)V_d(X,\omega)}
{v_d\mathsf C(X,\omega)}.}
\tag{RG3}
$$

Equation (RG3) is more than dimensional analysis only when the two ledgers, their normalization, and their common codomain were fixed independently of \(\ell_X\). Otherwise any desired scale can be manufactured by hiding it in \(w\) or \(\mathsf C\).

The same method does not require a power law. If \(\mathsf B_X(\ell)\) is continuous, strictly monotone, and brackets \(\mathsf C_X\), the equation

$$
\mathsf B_X(\ell_X)=\mathsf C_X
\tag{RG4}
$$

has one positive solution. Entropy, flux, clock depth, surface response, and scale may enter, but only after maps put their numerical representatives in one common quantity line. Equality of dimensions is necessary and never sufficient for equality of concepts.

For example,

$$
\frac{S}{k_B},
\qquad
\int_I \Gamma(t)\,\mathrm dt,
\qquad
\log\frac{R_2}{R_1}
\tag{RG4a}
$$

are all dimensionless, but respectively present an entropy count, accumulated event rate, and scale interval. They may be compared only after a common carrier supplies maps explaining what is conserved or counted across the presentations. A numerical equality among them is not that map.

## Object-relative grains

The construction is a method, not a hidden universal numeral. For each admissible object \(X\), one must supply a carrier-appropriate whole ledger and local ledger:

$$
\mathsf C_X
=
\mathsf B_X(\ell_X).
\tag{RG4b}
$$

There is no reason for \(\ell_X=\ell_Y\) when \(X\) and \(Y\) are different response objects. A background-radiation anisotropy, a Yang--Mills vacuum slab, a horizon cut, and a thermodynamic transition can carry different measures, normalizations, and response laws. What can be shared is the diagrammatic form of the comparison. A common numerical scale is justified only if a further naturality theorem identifies the two carriers and their ledgers.

A scalar ledger need not identify all the geometry relevant to response. [[rg-covariance-residue/frustrated-su3-conditional-wells#Equal scalar strength does not identify the source orbit|Two realizable gauge sources]] have identical singular values and scalar strength but inequivalent determinant phases and different conditional well structures. Thus a matched count can select a yardstick while leaving essential context data unresolved. The comparison should eliminate redundant presentation choices, not distinctions that change the operator.

## The causal-scale member

For a spherical causal presentation, take

$$
\mathsf C
=
\frac{\pi R_c^2}{\ell_P^2},
\qquad
V_3
=
\frac{4\pi}{3}R_c^3,
\qquad
v_3=1,
\qquad
w=\gamma s_*.
\tag{RG5}
$$

Equation (RG3) becomes

$$
\lambda_*^3
=
\frac{4\gamma s_*}{3}\ell_P^2R_c.
\tag{RG6}
$$

The \(46\)--\(47\,\mathrm{MeV}\) presentation belongs only to one conditionally calibrated member of (RG6). The downstream [[causal-grain-cosmology/cmb-likelihood-test|chiral-acoustic likelihood test]] has a narrower, more concrete result: a frozen relation removes one fitted CMB acoustic-angle coordinate with little penalty in the archived paired Planck and ACT spectrum fits. It uses the standard transfer calculation and a post-search functional law; no independent galaxy-BAO prediction has yet been established. This supports conditional parameter economy, not a derivation of the common-count law. It does not make the returned grain universal, identify a particle, or authorize importing it into Yang--Mills. [[the-grain-of-causal-scale/filled-cell-no-go|The filled-cell no-go]] makes one of those type boundaries quantitative.

## Covariance and the word “functor”

Suppose a morphism \(f:(X,\omega)\to(Y,\eta)\) carries both ledgers naturally and rescales lengths by \(a_f>0\):

$$
\mathsf C(Y,\eta)
=
\mathsf C(X,\omega),
\qquad
\mathsf B(Y,\eta;a_f\ell)
=
\mathsf B(X,\omega;\ell).
\tag{RG7}
$$

Uniqueness then gives

$$
\ell_Y=a_f\ell_X.
\tag{RG8}
$$

Only after a category of carriers and transformations satisfying (RG7) has been specified is it justified to call the assignment \(X\mapsto\ell_X\) a grain functor. Before that, **matched-ledger construction** is the accurate name. The absence of one preferred global scale is compatible with a covariant family of selected local scales; [[contemporary-puzzles/yang-mills-mass-gap/scale-torsor-and-the-global-local-gap-invariant|the scale-torsor note]] states that distinction.

## Application to the mass-gap search

The Yang--Mills use of the method should not begin by inserting the cosmological value of \(\lambda_*\). It should begin with a new carrier-appropriate comparison:

$$
\text{whole-law or wall ledger}
=
\text{local slab-response ledger at }\ell_{\mathrm{YM}}.
\tag{RG9}
$$

The comparison must select \(\ell_{\mathrm{YM}}\) without using a measured glueball mass or the unknown transfer spectrum. On the complete regulated Wilson carrier one must then independently prove

$$
\sup_r
\left\|K_{r,\ell_{\mathrm{YM}}}Q_r\right\|
\leq\rho_*<1.
\tag{RG10}
$$

Only the conjunction of the scale selection and this uniform response angle gives

$$
\Delta_E
\geq
\frac{\hbar c}{\ell_{\mathrm{YM}}}
\log(\rho_*^{-1}),
\tag{RG11}
$$

subject to continuum and Osterwalder--Schrader reconstruction. The dimensionless attenuation \(\log(\rho_*^{-1})\) and the selected length \(\ell_{\mathrm{YM}}\) are different outputs. This prevents a numerical rhyme, a topological integer, or a universal logistic profile from being called the gap by itself.

[[global-local-response-reconstruction/yang-mills-balanced-fisher-grain|The balanced-Fisher grain]] gives one concrete candidate for (RG9): the logarithmic scale score of the blocked Wilson law is split into boundary-recoverable and midpoint-residual Fisher ledgers, and their balance selects a possible Yang--Mills scale. Its root is not yet proved to exist or survive the continuum limit.

That selected scale is still only an object-relative one-tangent selector analogous to a member of [[distinction-grain-spectrum/inq|the distinction-grain spectrum]]. Literal membership additionally requires a common transport under which the input carrier, tangent, and physical projection are fixed and the channel family is Blackwell-nested. Even if every fixed tangent eventually crosses a balance point, a gap requires a finite uniform ceiling over the complete nonvacuum carrier. This quantifier reversal is what distinguishes an informative grain diagnostic from the Clay-relevant coercivity theorem.

## A response-defined grain is not an independent explanation

There is another valid but logically weaker protocol. Given a complete response profile, define its accumulated worst-direction attenuation

$$
\mathcal R_X(\ell)
:=
-\log\left\|K_{X,\ell}Q_X\right\|
\tag{RG12}
$$

and, for a prospectively fixed dimensionless depth \(\iota_*>0\), define

$$
\ell_{X,\iota_*}
:=
\inf\left\{
\ell>0:
\mathcal R_X(\ell)\geq\iota_*
\right\}.
\tag{RG13}
$$

This is an object-relative “one-nat” or fixed-depth correlation grain. It can compare different carriers without pretending that they share one number. But it must not be used to prove the property built into it. Let \(A_X\) be nonnegative and self-adjoint, and let the nonzero orthogonal projection \(Q_X\) reduce \(A_X\). For the exact transfer semigroup on that reducing subspace,

$$
K_{X,\ell}
=
e^{-\ell A_X}Q_X,
\tag{RG14}
$$

spectral calculus gives

$$
\mathcal R_X(\ell)
=
\ell\,
\inf\sigma\!\left(A_X\!\restriction_{Q_X\mathcal H_X}\right).
\tag{RG15}
$$

Therefore \(\ell_{X,\iota_*}<\infty\) for any \(\iota_*>0\) if and only if \(A_X\) already has a positive lower edge on \(Q_X\mathcal H_X\). Equation (RG13) is then a useful presentation of the correlation length, but not a reason the edge is positive.

An explanatory matched-ledger construction must instead use a whole ledger not defined from the same worst-direction spectral quantity, or prove from upstream algebraic data that the crossing in (RG13) occurs at finite depth. This is why a mean entropy, index, or capacity may help select a scale but cannot replace the separate uniform response theorem.

## Admission test

A proposed grain is explanatory only if it specifies:

1. the carrier and state on which both ledgers are defined;
2. what each ledger counts and the map identifying their codomains;
3. why their normalizations precede the target number;
4. existence, uniqueness, and covariance of the positive solution;
5. the physical observable or operator to which that solution is soldered; and
6. a prospective prediction that distinguishes the construction from a refit.

The Copernican lesson is methodological: do not ask which pre-existing ruler is hidden inside the object. Ask which two presentations of the object must agree, and whether their agreement constructs a ruler.
