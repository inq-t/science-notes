# Shorted Response Filtration and the Positive Leak Cocycle

A whole positive response can be pushed to a local fact carrier without choosing a hidden antecedent: minimize the whole cost over the entire fibre of compatible backgrounds. For bounded positive operators this is Anderson--Trapp shorting. The operation is exactly transitive on nested retained carriers, and it yields two distinct positive ledgers: a monotone retained-response filtration and a frozen-versus-relaxed background residue. A single wall defect vanishes on its own retained carrier, but the weighted sum of two projection defects has an exact Cayley-type short whose possible positive floor is controlled by their Friedrichs angle. Most importantly, a positive local floor is equivalent to a Douglas range-inclusion condition. The whole operator may be globally gapless while its arbitrarily soft modes are entirely invisible to the retained quotient; the local gap is then real, but shorting has exposed rather than manufactured it.

**Status: [EXACT] for bounded positive operators on one Hilbert carrier, including variational shorting, transitivity, the two positive ledgers, the paired-projection formula, and the Douglas stopping condition; [EXACT MODEL] for a globally gapless whole with a gapped retained short; [CONDITIONAL CONSTRUCTION] for a vacuum response and nested fact carriers; [OPEN] for a canonical Type-III/Jordan/Yang--Mills carrier, an unbounded closed-form extension with the required naturality, a regulator-uniform floor, and the clock--Poincare solder.**

## A fact carrier is a quotient of compatible whole variations

Let \(\mathcal H_W\) be a Hilbert response carrier, let \(A\in B(\mathcal H_W)\) be positive, and let \(L\subseteq\mathcal H_W\) be a closed retained subspace with orthogonal projection \(P_L\). The affine set

$$
v+L^\perp
=
\{v+z:z\in L^\perp\},
\qquad v\in L,
\tag{SF1}
$$

is the linear-response analogue of an antecedent fibre: every member has the same retained projection \(P_L(v+z)=v\). It is not automatically a state-restriction fibre, gauge orbit, torsor, or collection of physical histories. Those identifications require separately constructed maps.

The short of \(A\) to \(L\) is

$$
\boxed{
S_L(A)
:=
\max\left\{
X\in B(\mathcal H_W):
0\leq X\leq A,
\operatorname{Ran}X\subseteq L
\right\}.}
\tag{SF2}
$$

[[library/shorted-operators-ii/inq|Anderson and Trapp]] prove that this maximum exists for every bounded positive \(A\) and closed \(L\). [[library/shorts-of-operators-and-some-extremal-problems/inq|Pekarev's extremal formulation]] gives its quadratic form as the infimal pushforward of the whole response:

$$
\boxed{
\langle v,S_L(A)v\rangle
=
\inf_{z\in L^\perp}
\langle v+z,A(v+z)\rangle,
\qquad v\in L.}
\tag{SF3}
$$

Thus \(S_L(A)\) operates on a retained distinction \(v\), while the forgotten background enters through the quantifier over every compatible extension \(z\). This is the linear operator promised by the reversal tactic:

$$
\text{whole response}
\longmapsto
\text{least whole cost at fixed local presentation}.
\tag{SF4}
$$

If \(\mathcal H_W=L\oplus L^\perp\) and

$$
A=
\begin{pmatrix}
G&B\\
B^*&C
\end{pmatrix},
\qquad
C\geq cI>0,
\tag{SF5}
$$

then

$$
S_L(A)|_L
=G-BC^{-1}B^*.
\tag{SF6}
$$

The inverse formula is conditional; the order definition and (SF3) still make sense when the hidden block is not invertible.

The bounded theorem is not permission to suppress continuum domains. [[library/shorting-parallel-addition-and-form-sums-of-nonnegative-selfadjoint-linear-relations/inq|Arlinskiĭ's form extension]] may return a nonnegative self-adjoint linear relation rather than a densely defined single-valued operator. A Type-III or continuum application must prove that its intended short is a closed operator form on the required physical domain.

## The leak and the retained response are different operators

Holding the hidden coordinate fixed at zero gives the hard compression

$$
G_L(A):=P_LAP_L.
\tag{SF7}
$$

Allowing it to relax gives \(S_L(A)\). Their difference is positive:

$$
\boxed{
R_L(A)
:=
G_L(A)-S_L(A)
\geq0.}
\tag{SF8}
$$

In the block situation (SF5),

$$
R_L(A)|_L=BC^{-1}B^*.
\tag{SF9}
$$

This gives a precise response-theoretic meaning to *leak*:

- \(G_L(A)\) is the cost seen when the background is artificially frozen;
- \(R_L(A)\) is the amount of that cost absorbed by compatible background relaxation;
- \(S_L(A)\) is the cost that survives every such relaxation.

The exact balance is

$$
\boxed{
G_L(A)=S_L(A)+R_L(A).}
\tag{SF10}
$$

It is a Loewner-order balance on one response carrier, not a conservation law in clock time. It is also not the relative-entropy decrement of a channel. The two can be compared only after a common tangent carrier and response form have been constructed.

The mass-bearing candidate is \(S_L(A)\), not \(R_L(A)\). The background relation helps constitute the quotient, and \(R_L(A)\) measures how strongly background adjustment affects a retained variation; but a mass gap asks whether a positive cost remains after that adjustment has been allowed.

## Nested forgetting is exactly transitive

Let

$$
L\subseteq T\subseteq U\subseteq\mathcal H_W
\tag{SF11}
$$

be closed retained carriers. Then

$$
\boxed{
S_L\!\left(S_T(A)\right)=S_L(A).}
\tag{SF12}
$$

The proof uses only the maximum property. Every positive operator below \(S_T(A)\) and supported in \(L\) is below \(A\), hence below \(S_L(A)\). Conversely, \(S_L(A)\) is supported in \(T\) and below \(A\), so \(S_L(A)\leq S_T(A)\) and is an admissible competitor for the short of \(S_T(A)\) to \(L\).

The stronger intersection identity

$$
S_L\!\left(S_T(A)\right)=S_{L\cap T}(A)
\tag{SF12a}
$$

for arbitrary closed \(L,T\) is recorded in [[library/spectral-shorted-operators/inq|the ordinary-shorting preliminaries of Antezana, Corach, and Stojanoff]]. The same paper exhibits an infinite-dimensional warning: increasing finite-dimensional retained subspaces can all have zero short even when their closed union is the whole carrier. Continuum compatibility requires a uniform estimate, not merely density of finite stages.

Therefore

$$
S_L(A)\leq S_T(A)\leq S_U(A)\leq A.
\tag{SF13}
$$

Define the positive stage loss

$$
D_{T\to L}(A)
:=
S_T(A)-S_L(A)
\geq0.
\tag{SF14}
$$

It obeys the exact additive cocycle law

$$
\boxed{
D_{U\to L}(A)
=
D_{U\to T}(A)+D_{T\to L}(A).}
\tag{SF15}
$$

This is the simplest rigorous version of consistent accounting across a descent. The stage loss acts on \(T\); it is not generally supported only in \(T\ominus L\).

The frozen-versus-relaxed residue has a second, less trivial composition law:

$$
\boxed{
R_L(A)
=
P_LR_T(A)P_L
+R_L\!\left(S_T(A)\right).}
\tag{SF16}
$$

Using (SF12),

$$
R_L\!\left(S_T(A)\right)
=
P_LD_{T\to L}(A)P_L.
\tag{SF17}
$$

Equation (SF16) separates the relaxation already paid outside \(T\) from the additional relaxation paid on passing from \(T\) to \(L\). It is an exact operator identity, not merely an inequality or a metaphor about forgotten information.

The common ambient carrier is load bearing. A tower of Type-III algebras or \(W^*\)-correspondences does not automatically provide nested Hilbert subspaces to which (SF12) applies. Compatible standard-form embeddings, expectation implementations, or another coherent realization must first be supplied.

## Paired walls produce an exact tangential response

**Exact bounded theorem.** Let \(P,Q\) be orthogonal projections on a Hilbert space \(\mathcal H\), let \(\alpha,\beta>0\), and put

$$
A_{\alpha,\beta}
:=
\alpha(I-P)+\beta(I-Q).
\tag{SF17a}
$$

Write

$$
R:=P\wedge Q,
\qquad
C:=PQP\big|_{P\mathcal H},
\qquad
E_{P,Q}:=(P-R)\mathcal H.
\tag{SF17b}
$$

Then the short to the \(P\)-retained carrier is

$$
\boxed{
\Lambda_{P\leftarrow Q}^{\alpha,\beta}
:=
S_{P\mathcal H}(A_{\alpha,\beta})\big|_{P\mathcal H}
=
\alpha\beta(I-C)(\alpha I+\beta C)^{-1}.}
\tag{SF17c}
$$

Here \(A_{\alpha,\beta}\) acts on the whole comparison carrier \(\mathcal H\), whereas \(\Lambda_{P\leftarrow Q}^{\alpha,\beta}\) acts on a retained vector \(x\in P\mathcal H\) after every hidden lift has been relaxed:

$$
\boxed{
\langle x,\Lambda_{P\leftarrow Q}^{\alpha,\beta}x\rangle
=
\inf_{z\in\ker P}
\left{
\alpha\|z\|^2
+
\beta\|(I-Q)(x+z)\|^2
\right}.}
\tag{SF17d}
$$

This typing resolves the range--kernel obstruction for a raw wall. On its own retained carrier,

$$
(I-P)\big|_{P\mathcal H}=0,
\qquad
S_{P\mathcal H}\!\left(\alpha(I-P)\right)=0.
\tag{SF17e}
$$

Any tangential response surviving in (SF17c) therefore comes from the relative position of the **second** wall, not from reinterpreting \(I-P\) as an operator it cannot be.

For the proof, decompose \(\mathcal H=P\mathcal H\oplus\ker P\) and write

$$
Q=
\begin{pmatrix}
C&B\\
B^*&D
\end{pmatrix}.
$$

The hidden block of \(A_{\alpha,\beta}\) is \(M=\alpha I+\beta(I-D)\geq\alpha I\), so the Schur formula applies. The projection identities

$$
BB^*=C-C^2,
\qquad
B M=(\alpha I+\beta C)B
$$

give

$$
\beta(I-C)-\beta^2BM^{-1}B^*
=
\alpha\beta(I-C)(\alpha I+\beta C)^{-1},
$$

which proves (SF17c). This is the bounded two-projection instance of the infimal whole-to-local pushforward in [[trace-dirichlet-descent/inq|Trace Dirichlet Descent]]. If the resulting form is also closed and Markovian, that separate theorem supplies a local semigroup generator; bounded positivity and shorting alone do not.

The common kernel and the sharp reduced floor are

$$
\ker\Lambda_{P\leftarrow Q}^{\alpha,\beta}
=R\mathcal H,
\qquad
\inf\sigma\!\left(
\Lambda_{P\leftarrow Q}^{\alpha,\beta}\big|_{E_{P,Q}}
\right)
=
\frac{\alpha\beta(1-c_F^2)}{\alpha+\beta c_F^2},
\tag{SF17f}
$$

provided \(E_{P,Q}\neq\{0\}\), where

$$
c_F
:=
\|(P-R)(Q-R)\|
$$

is the Friedrichs cosine. Indeed, \(C\) is the identity on \(R\mathcal H\), its restriction to \(E_{P,Q}\) has norm \(c_F^2\), and the scalar function \(t\mapsto\alpha\beta(1-t)/(\alpha+\beta t)\) is decreasing. Consequently the following are equivalent:

$$
\boxed{
c_F<1
\quad\Longleftrightarrow\quad
(P-R)\mathcal H+(Q-R)\mathcal H\ \text{is closed}
\quad\Longleftrightarrow\quad
E_{P,Q}\subseteq\operatorname{Ran}A_{\alpha,\beta}^{1/2}.}
\tag{SF17g}
$$

Thus a sequence of almost-common reduced vectors with \(c_F=1\) falsifies any positive paired-wall floor. For equal weights,

$$
\boxed{
\Lambda_{P\leftarrow Q}^{1,1}
=(I-C)(I+C)^{-1},
\qquad
\inf\sigma\!\left(\Lambda_{P\leftarrow Q}^{1,1}\big|_{E_{P,Q}}\right)
=
\frac{1-c_F^2}{1+c_F^2}.}
\tag{SF17h}
$$

If \(P\) and \(Q\) are the common-GNS implementations of two state-preserving conditional expectations, then the quadratic form of \(A_{\alpha,\beta}\) is the weighted sum of their squared restriction losses. This gives the paired response a canonical meaning once the state, carrier, and expectations have been constructed. A bare inclusion, correspondence, or Q-system does not by itself supply those data. Multiplying \(\alpha,\beta\) by one common scalar changes only the overall normalization; changing their ratio changes the spectral response function even though the two projection ranges, and hence their unweighted wall geometry, stay fixed.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/paired_wall_shorting_receipt.py|The paired-wall receipt]] and [[contemporary-puzzles/yang-mills-mass-gap/receipts/paired-wall-shorting-receipt-output.txt|its stored output]] verify (SF17c), the common kernel, the single-wall no-go, and the equal-weight Cayley/tanh specialization in a finite projection model. They verify operator arithmetic only.

## The exact stopping condition is a range inclusion

Let \(E\subseteq\mathcal H_W\) be the closed carrier of retained physical excitations, and let \(Q=P_E\). For every \(\kappa>0\),

$$
\boxed{
S_E(A)\geq\kappa Q
\quad\Longleftrightarrow\quad
A\geq\kappa Q.}
\tag{SF18}
$$

The forward implication follows from \(S_E(A)\leq A\). For the reverse implication, \(\kappa Q\) is itself a positive operator below \(A\) with range in \(E\), so it is an admissible competitor in (SF2).

[[library/on-majorization-factorization-and-range-inclusion-of-operators-on-hilbert-space/inq|Douglas's factorization theorem]] now gives the qualitative criterion

$$
\boxed{
\exists\,\kappa>0:\ S_E(A)\geq\kappa Q
\quad\Longleftrightarrow\quad
E\subseteq\operatorname{Ran}A^{1/2}.}
\tag{SF19}
$$

Equivalently, the inclusion \(E\hookrightarrow\mathcal H_W\) factors boundedly through \(A^{1/2}\). This is a precise geometric meaning of a retained gap: every unit local excitation has a uniformly controlled whole-response lift. A positive frozen compression \(P_EAP_E\) is insufficient because a hidden adjustment may cancel it.

For example, on \(\mathbb C^2\),

$$
A=
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\qquad
E=\mathbb C(1,0),
\tag{SF20}
$$

has \(P_EAP_E=Q\), but

$$
S_E(A)=0
\tag{SF21}
$$

because the compatible extension \((x,-x)\) has zero whole cost. Here \(E\not\subseteq\operatorname{Ran}A^{1/2}=\mathbb C(1,1)\). The range condition detects exactly the cancellation that the compression misses.

## A gapless whole can have a gapped factual quotient

Let

$$
\mathcal H_W
=
E\oplus\ell^2(\mathbb N),
\qquad
A
=
I_E\oplus
\operatorname{diag}\left(1,\frac12,\frac13,\ldots\right).
\tag{SF22}
$$

Then \(A\) is positive and injective, but

$$
\inf\sigma(A)=0,
\tag{SF23}
$$

so the whole response has no spectral gap. Nevertheless,

$$
\boxed{
S_E(A)=I_E.}
\tag{SF24}
$$

All arbitrarily soft directions lie in the hidden summand. Nothing in the shorting operation creates the unit stiffness: \(A\geq P_E\) already. What changes is the question. The whole spectrum asks whether *any* whole direction can become arbitrarily soft; the shorted spectrum asks whether a fixed retained distinction can do so after every compatible hidden direction is optimized.

This is the exact category-error mechanism suggested by Radical Copernicanism:

$$
\boxed{
\text{gaplessness of the unpointed whole}
\not\Longrightarrow
\text{gaplessness of every factual quotient}.}
\tag{SF25}
$$

Conversely, if low-cost whole variations retain a unit component in \(E\), then (SF19) fails and no local floor exists. The theorem therefore supplies both a route and a kill condition.

## Vacuum typing

Suppose a vacuum projection \(P_0\) satisfies

$$
P_0\leq P_L,
\qquad
AP_0=0,
\tag{SF26}
$$

and put

$$
E=L\cap\ker P_0,
\qquad
Q=P_E=P_L-P_0.
\tag{SF27}
$$

Every positive \(X\leq A\) annihilates the vacuum. Hence

$$
S_L(A)=S_E(A),
\qquad
S_L(A)P_0=0.
\tag{SF28}
$$

The dimensionless vacuum-gap condition is therefore

$$
\boxed{
S_L(A)P_0=0,
\qquad
S_L(A)\geq\kappa Q
\quad\Longleftrightarrow\quad
E\subseteq\operatorname{Ran}A^{1/2}.}
\tag{SF29}
$$

If \(P_0\not\leq P_L\), or if \(A\) does not annihilate the declared vacuum, one must short directly to the correctly defined excitation carrier. Compressing an already shorted operator by \(1-P_0\) is not automatically another short.

## What Type III can and cannot contribute

Type-III operator algebra is relevant because it can hold global and local observable registers without density matrices, minimal projections, or a local trace. It also provides several exact pieces:

- state restriction composes strictly, and Araki relative entropy decreases under it;
- standard form represents each normal positive functional by a unique vector in the natural cone;
- a state-preserving expectation, when Takesaki's modular criterion holds, gives an orthogonal projection onto \(\overline{N\Omega}\) in a common GNS carrier;
- operator-valued weights and \(W^*\)-correspondences provide broader noninvertible comparison arrows under additional hypotheses; and
- Connes fusion composes correspondences coherently up to canonical unitary.

None of these facts canonically supplies the whole response \(A\), the retained subspace \(L\), or the domination in (SF29). A bare correspondence has no preferred vector, state transfer, CP map, or positive quadratic form. Arbitrary inclusions need not admit expectations or operator-valued weights. Even when a finite-index expectation has a Pimsner--Popa order floor, [[gauge-index-no-go-and-four-dimensional-center-square]] and [[finite-index-duality-and-the-square-response]] show that this index floor is not a Yang--Mills Hessian or clock-energy gap.

Type III is therefore the likely **carrier grammar** for the whole/local relation, not the reason the positive edge exists. The missing theorem must construct a natural family

$$
(\mathcal H_W,A)
\longmapsto
\bigl(L_O,S_{L_O}(A)\bigr)
\tag{SF30}
$$

whose comparison maps realize nested shorting or its closed-form analogue.

## The Yang--Mills construction target

At a finite lattice regulator, reflection positivity gives an Osterwalder--Schrader Hilbert space and a positive transfer Hamiltonian form. That form is an honest whole-level \(A\), but taking it as the unexplained input makes (SF29) equivalent to proving the regulated Hamiltonian gap. The Copernican programme needs a more primitive response—such as a canonically normalized algebraic constraint Hessian, a boundary Dirichlet-to-Neumann form, or a jointly transverse causal frame—and then an independently proved comparison with the OS form.

A successful construction must provide, uniformly in lattice spacing \(a\) and volume \(L\):

1. a whole carrier \(\mathcal H_{W,a,L}\), a positive response \(A_{a,L}\), and a vacuum;
2. physical retained excitation carriers \(E_{a,L}\) obtained from the whole/local realization rather than a spectral cutoff;
3. the Douglas inclusion
   \[
   E_{a,L}\subseteq\operatorname{Ran}A_{a,L}^{1/2}
   \]
   with one uniform domination constant \(\kappa_*>0\);
4. compatible shorting under refinement, gluing, and scale descent;
5. a fixed form comparison from \(S_{E_{a,L}}(A_{a,L})\) to the normalized OS Hamiltonian form;
6. survival of the bound through infinite-volume and continuum limits; and
7. OS/Poincare reconstruction identifying the resulting clock-energy edge with the invariant mass Casimir.

Only the first four items belong to the pre-geometric response. The physical energy unit and \(\hbar\) enter in the fifth and seventh items, not in (SF2)--(SF19).

The resulting explanatory chain is

$$
\boxed{
\begin{array}{c}
\text{unpointed whole response, possibly gapless}\\
\downarrow\ \text{restriction to a factual quotient}\\
\text{shorted retained response}\\
\downarrow\ \text{Douglas inclusion with uniform constant}\\
\text{dimensionless distinction floor}\\
\downarrow\ \text{OS, clock, and Poincare solders}\\
\text{Yang--Mills mass gap}.
\end{array}}
\tag{SF31}
$$

[[contemporary-puzzles/yang-mills-mass-gap/receipts/shorted_response_filtration_receipt.py|The finite receipt]] and [[contemporary-puzzles/yang-mills-mass-gap/receipts/shorted-response-filtration-receipt-output.txt|its stored output]] check nested Schur shorting, both positive ledgers, the staged identities, the cancellation example, and finite truncations of the gapless-whole/gapped-quotient witness. They verify operator arithmetic only; they do not construct Type-III naturality, the Jordan flag response, a continuum Yang--Mills measure, or a mass scale.
