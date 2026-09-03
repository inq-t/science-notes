# Paired Scale Filtrations and the Invariant Incidence Wall

A regulator- or RG-defined filtration canonically decomposes a centered carrier into orthogonal distinction shells and thereby defines a self-adjoint scale-address operator without using a Hamiltonian spectrum. One filtration whose active addresses are unbounded above necessarily gives a gapless inverse-scale operator. Two strongly commuting, oppositely oriented filtrations contain strictly more information: their nonzero joint shell intersections form an incidence geometry, and a ceiling on the **sum** of the two scale addresses is exactly a floor for their positive product while the relative address may remain unbounded. This is a precise candidate meaning of a causal wall: not a smallest spatial pixel and not a potential acting on a thing, but an algebraic restriction on which reciprocal distinctions can be jointly realized. It becomes a mass statement only after an all-direction construction and a noncircular solder to the reconstructed Poincare Casimir.

**Status: [EXACT FILTRATION-ADDRESS THEOREM]; [EXACT PAIRED-INCIDENCE THEOREM]; [EXACT ALL-DIRECTION CASIMIR TOMOGRAPHY]; [CANDIDATE PRE-QFT REALIZATION]; [OPEN YANG--MILLS FILTRATION, WALL, AND CONTINUUM CONSTRUCTION].** The exact results begin with supplied projections and scale labels. They do not construct the Yang--Mills filtrations or prove their incidence ceiling.

## One filtration constructs an address operator

Let \(\mathcal H\) be a complex Hilbert space, let \(P_0\) be a distinguished projection, and put \(P=1-P_0\). Suppose a decreasing filtration has orthogonal GNS implementations

$$
E_0=1,
\qquad
E_jE_k=E_{\max\{j,k\}},
\qquad
E_j\xrightarrow[j\to\infty]{\mathrm{strong}}P_0.
\tag{PF1}
$$

In the applications envisioned here, the \(E_j\) arise from state-preserving conditional expectations onto nested regulator or RG algebras, as in [[physical-distinction-coercivity#A Takesaki-admissible distinction filtration|the Takesaki-admissible filtration]]. They are not assumed to be expectations between ordinary nested vacuum AQFT region algebras, which are obstructed under the standard cyclic and separating hypotheses.

Define the martingale shell projections

$$
D_j:=E_j-E_{j+1}.
\tag{PF2}
$$

Then

$$
D_jD_k=\delta_{jk}D_j,
\qquad
\sum_{j\geq0}D_j=P
\tag{PF3}
$$

in the strong operator topology. Choose real addresses \(N_j\), fixed from the geometry of the filtration rather than from the target spectrum. For an RG blocking factor \(b>1\), the natural affine candidate is

$$
N_j=N_0+j\log b,
\tag{PF4}
$$

provided \(N\) has first been declared to log length. Logging an operator parameter of differential order \(d\) instead multiplies this increment by \(d\); [[resolvent-logistic-scale-transform]] records why this normalization cannot be guessed from the logistic profile.

On \(P\mathcal H\), define the diagonal address operator

$$
A_{\mathcal F}
:=
\sum_jN_jD_j,
\qquad
\operatorname{Dom}A_{\mathcal F}
=
\left\{
f:\sum_jN_j^2\|D_jf\|^2<\infty
\right\}.
\tag{PF5}
$$

The orthogonal decomposition makes \(A_{\mathcal F}\) self-adjoint. Its positive inverse-scale operator is

$$
K_{\mathcal F}
:=
0\oplus e^{-A_{\mathcal F}}
=
\sum_je^{-N_j}D_j
\tag{PF6}
$$

on \(P_0\mathcal H\oplus P\mathcal H\), with the natural functional-calculus domain if it is unbounded.

The direct-sum notation is essential. No everywhere-finite self-adjoint operator on all of \(\mathcal H\) can exponentiate to a positive operator with nonzero kernel. The address is defined on the active carrier \(P\mathcal H\) and is formally \(+\infty\) on the terminal vacuum line. Its kernel is

$$
\ker K_{\mathcal F}=P_0\mathcal H.
\tag{PF7}
$$

This closes the operator-selection problem only conditionally: once a physical filtration and its scale character are supplied, the operator is fixed. It operates on centered GNS or interface vectors. The component \(D_jf\) is the distinction first removed between the \(j\)-th and \((j+1)\)-st retained algebras, and \(K_{\mathcal F}\) weights that component by inverse scale. It is not a clock generator.

Applying the resolvent--logistic transform to \(K_{\mathcal F}\) centers the \(j\)-th shell at exactly \(N_j\). Thus the earlier discrete martingale transform and continuous logistic scale transform are not rival descriptions:

$$
f
\longmapsto
(D_jf)_j
\longmapsto
\left(
N\longmapsto
\sum_j
\frac{(e^{N-N_j})^{1/2}}{1+e^{N-N_j}}
D_jf
\right).
\tag{PF8}
$$

The second arrow is canonical after (PF6), preserves the shell multiplicities and complex phases, and has coverage one on \(P\mathcal H\).

## A one-sided address unbounded above is necessarily gapless

Assume \(P\mathcal H\neq\{0\}\). The spectral theorem gives

$$
\inf\sigma\!\left(K_{\mathcal F}\restriction_{P\mathcal H}\right)
=
\exp\!\left(-\sup_{j:D_j\neq0}N_j\right),
\tag{PF9}
$$

with \(e^{-\infty}=0\). Therefore

$$
\boxed{
\sup_{j:D_j\neq0}N_j=+\infty
\quad\Longrightarrow\quad
\inf\sigma(K_{\mathcal F}|_{P\mathcal H})=0.}
\tag{PF10}
$$

An infinite coarse-depth filtration does not produce a positive floor merely because its individual shells are discrete or orthogonal. Its centers simply run away. This is the discrete filtration version of the no-gap theorem for one dilation-covariant causal generator.

It is also a type warning. A spatial RG address can be arbitrarily large in a massive theory: a massive particle may have arbitrarily small spatial momentum, and a wave packet may have arbitrarily large extent. Hence bounding one spatial coarse-graining address would generally be the wrong physical target. The invariant must be relational.

## Two commuting filtrations define an incidence geometry

For the operator-algebraic realization, both filtrations must lie in one ambient von Neumann algebra \(\mathfrak M\), preserve the same faithful normal state \(\omega\), and therefore have GNS implementations on the same carrier \(\mathcal H_\omega\). Abstractly, let \(\{D_j^+\}_{j\in J_+}\) and \(\{D_k^-\}_{k\in J_-}\) be two orthogonal shell resolutions of that centered carrier satisfying

$$
\sum_jD_j^+=P,
\qquad
\sum_kD_k^-=P,
\tag{PF11}
$$

Equation (PF11) is already the strong common-vacuum completeness condition. The more general terminal-sector decomposition below shows why it cannot be replaced merely by an intersection condition.

Assume also the cross-shell commutation condition

$$
[D_j^+,D_k^-]=0
\qquad
\text{for every }j,k.
\tag{PF12}
$$

Then

$$
Q_{jk}:=D_j^+D_k^-
\tag{PF13}
$$

are mutually orthogonal projections with

$$
\sum_{j,k}Q_{jk}=P
\tag{PF14}
$$

strongly. For a faithful normal state, [[library/conditional-expectations-in-von-neumann-algebras/inq|Takesaki's theorem]] supplies each state-preserving conditional expectation under modular invariance; its orthogonal GNS implementation is then elementary. The theorem does not supply (PF12). More generally, Takesaki's weight form requires a faithful normal semifinite weight whose restriction to the subalgebra remains semifinite. In the finite tracial setting, [[library/orthogonal-pairs-of-star-subalgebras-in-finite-von-neumann-algebras/inq|Popa's orthogonal-pair framework]] is the historical commuting-square model. The standard commuting-square law is a statement about the conditional expectations and implies the required projection commutation. Commutation of the subalgebras as sets is not enough.

The algebraic incidence support is

$$
\Sigma
:=
\{(j,k):Q_{jk}\neq0\}.
\tag{PF15}
$$

This set is more than two lists of scales. It records which positive and negative causal distinctions coexist on a nonzero vector. Conditional expectations or martingale orthogonality within each tower do not determine \(\Sigma\); the relative position of the towers does.

### Terminal tails and one-sided sectors

Before imposing (PF11), suppose instead that the two full towers have terminal projections \(P_\infty^\pm\), and put

$$
S_\pm:=1-P_\infty^\pm.
\tag{PF15a}
$$

Under cross-commutation, their joint shell sum is only

$$
P_{\leftrightarrow}:=S_+S_-,
\tag{PF15b}
$$

and the carrier splits orthogonally as

$$
\mathcal H
=
S_+S_-\mathcal H
\oplus
S_+P_\infty^-\mathcal H
\oplus
P_\infty^+S_-\mathcal H
\oplus
P_\infty^+P_\infty^-\mathcal H.
\tag{PF15c}
$$

When the operators below are constructed, extend \(K_\pm=e^{-A_\pm}\) by zero on \(P_\infty^\pm\mathcal H\). The address \(A_\pm\) is defined only on the active carrier; it is formally \(+\infty\) on the terminal tail. Interpret \(K_+K_-\) in the following formula as the positive joint-spectral-calculus product, not as a naive composition of possibly unbounded operators. Joint functional calculus then gives

$$
\ker(K_+K_-)
=
\left(P_\infty^+\vee P_\infty^-\right)\mathcal H.
\tag{PF15d}
$$

If the physical vacuum projection satisfies \(P_0\leq P_\infty^\pm\), a product floor on the whole vacuum complement is possible only when

$$
P_\infty^+\vee P_\infty^-=P_0,
\tag{PF15e}
$$

which in this case is equivalent to \(P_\infty^+=P_\infty^-=P_0\). The weaker equation \(P_\infty^+P_\infty^-=P_0\) leaves the two middle summands in (PF15c) as nonvacuum one-sided null sectors. The clean hypothesis (PF11) assumes precisely that they have already been excluded.

From this point through (PF26), return to the common-vacuum completeness hypothesis (PF11), so both active carriers are \(P\mathcal H\). Assign addresses \(N_j^+\) and \(N_k^-\), and define self-adjoint operators

$$
A_+=\sum_jN_j^+D_j^+,
\qquad
A_-=\sum_kN_k^-D_k^-.
\tag{PF16}
$$

Their domains are

$$
\operatorname{Dom}A_\varepsilon
=
\left\{
f\in P\mathcal H:
\sum_{\ell\in J_\varepsilon}|N_\ell^\varepsilon|^2
\|D_\ell^\varepsilon f\|^2<\infty
\right\},
\qquad \varepsilon\in\{+,-\},
$$

and their spectral measures strongly commute by (PF12). Define the mean address directly by their joint shell calculus,

$$
A_M
:=
\sum_{j,k}
\frac{N_j^++N_k^-}{2}Q_{jk},
$$

with maximal spectral domain

$$
\operatorname{Dom}A_M
=
\left\{
f\in P\mathcal H:
\sum_{j,k}
\left|\frac{N_j^++N_k^-}{2}\right|^2
\|Q_{jk}f\|^2<\infty
\right\}.
$$

This definition matters: opposite divergences may cancel, so \(\operatorname{Dom}A_M\) can strictly exceed \(\operatorname{Dom}A_+\cap\operatorname{Dom}A_-\), and \(A_M\) is not being defined as an unqualified algebraic sum.

Put

$$
K_+=0\oplus e^{-A_+},
\qquad
K_-=0\oplus e^{-A_-},
\qquad
M_{\mathcal F}:=e^{-A_M}=(K_+K_-)^{1/2}.
\tag{PF17}
$$

Because the address operators may be unbounded, both the product and its square root in (PF17) mean the joint spectral-calculus constructions, not an unqualified algebraic composition. Joint functional calculus gives

$$
M_{\mathcal F}
=
\sum_{(j,k)\in\Sigma}
e^{-\overline N_{jk}}Q_{jk},
\qquad
\overline N_{jk}
:=
\frac{N_j^++N_k^-}{2}.
\tag{PF18}
$$

The difference coordinate

$$
N^{\mathrm{fr}}_{jk}
:=
\frac{N_j^+-N_k^-}{2}
\tag{PF19}
$$

does not enter \(M_{\mathcal F}\). It is the candidate frame or rapidity address. The mean coordinate \(\overline N_{jk}\) is the candidate invariant scale address.

## The paired-incidence wall theorem

Assume \(P\mathcal H\neq\{0\}\). All inequalities between possibly unbounded operators in this section are spectral inequalities, equivalently inequalities of their closed quadratic forms. For any finite \(N_*\), (PF18) proves the exact equivalence

$$
\boxed{
M_{\mathcal F}\geq e^{-N_*}P
\quad\Longleftrightarrow\quad
Q_{jk}=0
\text{ whenever }
\overline N_{jk}>N_*.}
\tag{PF20}
$$

Equivalently,

$$
\inf\sigma(M_{\mathcal F}|_{P\mathcal H})
=
\exp\!\left(
-\sup_{(j,k)\in\Sigma}\overline N_{jk}
\right).
\tag{PF21}
$$

The proof contains no dynamics. On the joint shell \(Q_{jk}\mathcal H\), the operator \(M_{\mathcal F}\) is multiplication by \(e^{-\overline N_{jk}}\). A uniform lower bound is therefore exactly the absence of nonzero joint shells beyond the diagonal line \(N_j^++N_k^-=2N_*\).

This is the **invariant incidence wall**. It is not a boundary at a spatial location. It is a boundary of the relation \(\Sigma\): beyond it, the two distinctions have no common realization. The relative coordinate (PF19) may remain unbounded on the allowed support.

For example, on \(\ell^2(\mathbb Z)\) take

$$
D_j^+=|e_j\rangle\langle e_j|,
\qquad
D_k^-=|e_{-k}\rangle\langle e_{-k}|,
\qquad
N_j^+=N_0+j\delta,
\quad
N_k^-=N_0+k\delta.
\tag{PF22}
$$

Then \(Q_{jk}\neq0\) exactly when \(k=-j\). Each of \(K_+\) and \(K_-\) has no positive lower edge, but

$$
K_+K_-=e^{-2N_0}P,
\qquad
M_{\mathcal F}=e^{-N_0}P.
\tag{PF23}
$$

The gapless individual addresses are the price of unlimited frame displacement; the fixed mean address is the joint invariant. This is the discrete counterpart of the massive rapidity witness in [[joint-causal-generators-and-the-mass-casimir#Exact massive witness]].

## Reciprocal shifts preserve the wall

The incidence geometry has the right covariance if \(n\mapsto U_n\) is a unitary representation of \(\mathbb Z\) satisfying

$$
U_nD_j^+U_n^*=D_{j+n}^+,
\qquad
U_nD_k^-U_n^*=D_{k-n}^-,
\tag{PF24}
$$

and the addresses obey the exact affine laws

$$
N^+_{j+n}=N^+_j+n\delta,
\qquad
N^-_{k-n}=N^-_k-n\delta.
$$

Then, on \(P\mathcal H\),

$$
U_nA_+U_n^*=A_+-n\delta,
\qquad
U_nA_-U_n^*=A_-+n\delta,
\tag{PF25}
$$

so

$$
U_nK_+U_n^*=e^{n\delta}K_+,
\qquad
U_nK_-U_n^*=e^{-n\delta}K_-,
\qquad
U_nM_{\mathcal F}U_n^*=M_{\mathcal F}.
\tag{PF26}
$$

A semi-infinite RG tower does not carry this bilateral group exactly, and a discrete shift is not the continuous Lorentz boost group. A countable atomic shell resolution can realize only discrete \(\delta\mathbb Z\) translation covariance: a nontrivial strongly continuous \(\mathbb R\)-action cannot continuously permute its atoms. Recovering continuous covariance requires a continuous projection-valued resolution or direct integral, in which there is generally no pointwise projection density \(D_t\), only Stieltjes interval projections, or else a controlled scaling limit. Equation (PF26) is a signature to be realized, not permission to call ordinary block spin a boost.

## Every spatial direction recovers the full Casimir

One null pair is insufficient in \(3+1\) dimensions, but an all-direction family is exact. Let \((H,\mathbf P)\) be the strongly commuting translation generators of a positive-energy Poincare representation, let \(P_0\) be its invariant vacuum projection, assume that \(P_0\) reduces their joint spectral measure, and put \(P=1-P_0\). For a unit vector \(\mathbf n\in S^2\), define

$$
P_\pm(\mathbf n)
:=
H\pm c\,\mathbf P\cdot\mathbf n.
\tag{PF27}
$$

The spectrum condition makes these operators nonnegative, and

$$
M_{\mathbf n}^2
:=
P_+(\mathbf n)P_-(\mathbf n)
=
\mathcal C
+c^2\left(
|\mathbf P|^2-(\mathbf P\cdot\mathbf n)^2
\right),
\tag{PF28}
$$

where

$$
\mathcal C:=H^2-c^2|\mathbf P|^2.
\tag{PF29}
$$

Assume \(P\mathcal H\neq\{0\}\), and read the following as spectral, equivalently closed-quadratic-form, inequalities. Let \(\mathcal D\subset S^2\) be any countable dense set. For every \(\Delta>0\), joint spectral calculus gives

$$
\boxed{
\mathcal C\geq\Delta^2P
\quad\Longleftrightarrow\quad
M_{\mathbf n}^2\geq\Delta^2P
\text{ for every }\mathbf n\in\mathcal D.}
\tag{PF30}
$$

The forward implication follows from the nonnegative transverse term in (PF28). Conversely, all inequalities in the countable family hold on one common full-measure subset of the joint energy--momentum spectrum. At a point \((E,\mathbf p)\) in that subset, choose \(\mathbf n_r\in\mathcal D\) approaching \(\mathbf p/|\mathbf p|\), or any direction when \(\mathbf p=0\). Continuity in \(\mathbf n\) sends the transverse term to zero and yields \(E^2-c^2|\mathbf p|^2\geq\Delta^2\).

Thus Jacobson-style “all-cut tomography” has a sharp mass-gap analogue: a common paired floor in every causal orientation is equivalent to a full Casimir floor. The direction family supplies tensorial completeness; it does not supply the positive constant. By [[joint-causal-generators-and-the-mass-casimir#Energy gap and Casimir floor are equivalent only after Lorentz reconstruction|the Lorentz-orbit theorem]], (PF30) then gives the Hamiltonian gap. Before Poincare reconstruction, neither (PF27) nor this conclusion is available.

## What the operator operates on

The proposed chain is now typed as

$$
\boxed{
\begin{aligned}
\text{two causal/RG filtrations on one centered carrier}
&\longrightarrow
\text{joint shell projections }Q_{jk},\\
\text{scale character}
&\longrightarrow
\text{address operators }A_\pm,\\
\text{relative position of the filtrations}
&\longrightarrow
\text{incidence support }\Sigma,\\
\text{diagonal ceiling on }\Sigma
&\longrightarrow
\text{dimensionless joint floor},\\
\text{all-direction Casimir solder and }E_*
&\longrightarrow
\text{physical energy gap}.
\end{aligned}}
\tag{PF31}
$$

Nothing here operates on bare spacetime. The projections operate on already formed, gauge-reduced, centered state-vector directions. The address operators measure at which coarse-graining transition each distinction is lost. The incidence wall constrains the joint realization of reciprocal distinctions. The physical Casimir operates only after those causal directions have been reconstructed as one translation representation.

This gives a rigorous version of “space is scale.” The primitive data are not points with sizes but an ordered family of retained distinctions and the relation describing which opposite distinctions coexist. A metric scale is a later numerical coordinate on that order. Mass is not identical to the coordinate; it is a possible lower bound on the joint invariant produced after reciprocal coordinates are paired.

## What could impose the incidence wall

Equation (PF20) moves the explanatory burden into a specific algebraic question:

$$
\boxed{
\text{Why must }D_j^+D_k^-=0
\text{ beyond a common diagonal depth?}}
\tag{PF32}
$$

Several workspace themes can now be tested against that question:

- **Gluing and gauge flux.** A boundary matching law or Gauss constraint could forbid incompatible incoming and outgoing shell labels. It must prove an actual joint-support restriction or a uniform form inequality, not merely conservation of a scalar expectation.
- **Torsors and Connes transport.** Opposite addresses may have no preferred origins while their sum descends to an invariant. Cocycle covariance can explain changes of presentation; it does not by itself bound the descended sum.
- **Knots and topological sectors.** A topological or index class could restrict which two-sided flux sectors meet. Index stability alone does not give the diagonal ceiling, and positive soliton energy does not exclude gapless fluctuations in the trivial sector.
- **Entropy and Hessians.** Conditional entropy measures what a blocking map forgets, while a BKM or logarithmic-Sobolev Hessian can estimate the cost of the corresponding tangent. Finite entropy penalties suppress amplitudes but do not make \(Q_{jk}\) vanish. They provide a softer coercivity route unless an independent saturation or admissibility theorem produces exact support loss.
- **A conserved total grade.** If geometry forces \(N_j^++N_k^-=2N_q\) on one sector, then (PF23) generalizes and the joint floor is fixed there while the frame coordinate remains free. Calling that grade causal charge is justified only after its composition, transport, and physical-carrier laws are constructed.

A commuting square supplies (PF12), not (PF20). It turns products of shell projections into joint intersection projections but does not itself constrain which intersections vanish. A finite tower supplies a temporary maximum address, not a regulator-uniform wall. A chosen truncation supplies the conclusion by definition. The desired result must survive increasing volume and cutoff removal without deleting legitimate low-energy physical states.

[[compensated-incidence-response-and-four-dimensional-balance]] proves the exact softer alternative. Let \(R\) be an independently constructed positive response on the presented joint-shell carrier. Then the relevant form is \(q[f]=\|\overline{R^{1/2}M_{\mathcal F}}f\|^2\), and in the shell-reducing case it has a floor exactly when \(\inf_{jk}\rho_{jk}e^{-2\overline N_{jk}}>0\), where \(\rho_{jk}\) is the bottom response on \(Q_{jk}\mathcal H\). The hard support wall is the special case \(R=I\). Thus deep incidences need not vanish if flux, Hessian, or boundary geometry charges them strongly enough. On a bilateral logarithmic-scale carrier, a homogeneous response exponent \(q\) compensates an order-\(p\) presentation only when \(q=2p\). The further observation that a codimension-two response has homogeneous power character \(D-2\), and hence balances first inverse-length order at \(D=4\), is conditional on an address/log-length solder, bilateral support, and independently derived two-sided response scaling; a lower frame alone gives sufficiency in four dimensions but not unique dimensional selection. Boundary area or entropy multiplicity supplies none of those theorems.

## Yang--Mills realization and recovery obligations

At a finite regulator, the most conservative carrier is the gauge-invariant ground-state-transformed \(L^2(\nu_r)\) space or the exact OS interface carrier supplied by [[vacuum-boundary-gluing-and-wall-response]]. Candidate filtrations can come from declared gauge-equivariant block maps, conditional expectations onto block observables, or a continuous interpolation of the RG martingale shells in [[two-scale-rg-descent-and-the-crossover-lemma]]. They must be selected before inspecting the transfer spectrum.

The following are independent obligations:

1. construct both filtrations and their common faithful carrier from gauge/RG geometry;
2. prove completeness at the vacuum and exclude any extra common or one-sided null sector;
3. prove the cross-commutation or replace (PF13) by a controlled noncommuting frame construction;
4. derive the scale addresses and their normalization from the RG character, including the length-versus-operator-order distinction;
5. prove a regulator-uniform incidence ceiling or softer same-carrier coercive substitute without a spectral truncation;
6. construct enough compatible causal orientations to invoke (PF30);
7. identify their generators with one positive-energy Poincare representation and compare the filtration product with its Casimir;
8. supply an independently normalized energy yardstick; and
9. pass the carrier, vacuum projection, forms, local net, covariance, and inequalities through infinite volume and continuum removal.

Compatibility with QFT is downstream and stricter than coexistence. [[library/modular-theory-and-the-reconstruction-of-four-dimensional-quantum-field-theories/inq|Kahler--Wiesbrock reconstruction]] shows that a specified modular constellation can generate a Poincare representation and local net, while [[library/modular-localization-and-wigner-particles/inq|Brunetti--Guido--Longo]] show the reverse direction when the Poincare representation, including its Wigner mass data, is supplied. Neither selects the incidence wall. [[library/extension-of-borchers-structure-theorem/inq|Araki--Zsido]] supplies the one-sided modular translation skeleton; its exact dilation covariance is why that individual generator is not the mass operator.

## Stopping and kill conditions

By the Schrodinger stopping rule in `inbox/operator-signature-verdict/commentary/the-schrodinger-stopping-rule.md`, (PF20) is mature enough to serve as part of a **signature**: it defines a research class and a sharp failure contract. It is not yet a physical **correspondence**. The Yang--Mills filtrations, their incidence law, the all-direction reconstruction, and the Casimir solder cannot be relabeled as interpretation or absorbed into a freely chosen member. A numerical wall location may eventually be member data; the form of the wall and the return map to observables must be frozen before confronting the spectrum.

The paired-filtration route has made progress only when the incidence support is computed or bounded from independently frozen algebraic data. It is killed if:

- either filtration is defined using spectral projections of the Hamiltonian or Casimir;
- the ceiling is imposed by deleting all shells above a chosen observed mass;
- a response weight is chosen as \(R=e^{2A_M}\) merely to manufacture the desired floor;
- boundary area, channel count, or entropy extensivity is substituted for a shellwise lower-frame estimate;
- two noncommuting expectations are multiplied as though their differences were joint projections;
- a one-sided spatial RG address is called mass;
- a floor for one null pair in \(3+1\) dimensions is called the full mass gap;
- the kernel contains nonvacuum one-sided sectors;
- a discrete RG shift is silently promoted to continuous Lorentz covariance; or
- a dimensionless support ceiling is converted to MeV without an independent yardstick and scheme comparison.

## Claim ledger

| Status | Claim |
|---|---|
| Exact | one complete orthogonal filtration plus frozen addresses defines the self-adjoint operator (PF5) and positive inverse-scale operator (PF6) |
| Exact no-go | a one-sided address unbounded above forces the inverse-scale spectrum to accumulate at zero |
| Exact | two strongly commuting complete shell families define the joint incidence projections and support (PF13)--(PF15) |
| Exact | general terminal tails split into joint-active, two one-sided, and common-tail sectors; a vacuum-complement product floor requires both tails to equal the vacuum |
| Exact | a ceiling on mean joint address is equivalent to a positive floor for \((K_+K_-)^{1/2}\) |
| Exact | a shell-reducing response gives the softer floor precisely when its bottom coefficients compensate the squared inverse-scale weights; the hard wall is the neutral-response special case |
| Exact | reciprocal affine shell shifts preserve the mean-address operator and its floor |
| Exact | a uniform null-pair floor on a countable dense family of spatial directions is equivalent to the full Poincare-Casimir floor |
| Candidate interpretation | the incidence ceiling is a precise algebraic model of a pre-spatial causal wall or conserved paired grade |
| Open | physical filtration selection, cross-commutation, wall derivation, all-direction realization, Casimir solder, yardstick, and continuum Yang--Mills construction |

[[contemporary-puzzles/yang-mills-mass-gap/receipts/paired_scale_incidence_wall_receipt.py|The numerical receipt]] checks finite shell resolutions, the diagonal support equivalence, a gapless-pair/gapped-product family, reciprocal shifts, the necessity of commutation, the terminal-tail kernel warning, and all-direction Casimir minimization; [[contemporary-puzzles/yang-mills-mass-gap/receipts/paired-scale-incidence-wall-receipt-output.txt|its stored output]] records the passing run. It does not construct a physical filtration or test a Yang--Mills mass gap.
