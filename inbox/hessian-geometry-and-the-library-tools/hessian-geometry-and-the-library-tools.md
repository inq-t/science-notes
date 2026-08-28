# Four Tools in the Library, and the One the Programme Already Owns

An audit of `library/complex-structure-on-s6`, `library/hodge-atoms-spectral-triples-bps`, and the postquantum-gravity cluster, against the open obligations of [[program-core/common-response-form|the common response matrix]] and [[causal-wall-spectral-theory/conjectures/bkm-to-spatial-precision|the W2 conjecture]]. The result is one positive finding, one negative finding, one identification, and one genuine import. The positive finding is that the response matrix has independently rediscovered Hessian geometry, and that the missing real-form datum $\tau$ follows from it. The negative finding is that the $S^6$ manuscript's own Remark 3.23 forbids the use the programme would want from it.

Receipts: `hessian-library-audit-receipts.py` (requires `numpy`; prints PASS/FAIL per claim, nonzero exit on failure). Every numerical claim below carries a receipt line.

## 1. The response matrix is a Hessian manifold, and BKM is forced by that

[[program-core/common-response-form|The common response matrix]] asks for, in its own notation,

$$
G_{IJ}=\partial_I\partial_J\Psi,
\qquad
\mathcal C_{IJK}=\partial_I\partial_J\partial_K\Psi,
\qquad
\mathcal C_{N\zeta\zeta}=\partial_NG_{\zeta\zeta},
$$

together with the remark that "the equality of mixed third derivatives supplies an integrability test." That package has a name it is not given anywhere in the vault. A manifold with a flat connection $\nabla$ and a metric $g=\nabla d\Psi$ is a **Hessian manifold** (Shima); the same object is a **dually flat manifold** in information geometry (Amari), and $\mathcal C_{IJK}$ is the **Amari--Chentsov tensor**. The integrability test the note asks for is the Codazzi condition: $(\nabla,g)$ is Hessian exactly when $\nabla g$ is totally symmetric.

Receipts, on a three-parameter quantum exponential family $\rho_\theta=\exp(\theta^iA_i-\psi)$ with noncommuting $A_i$ in $M_4(\mathbb C)$:

- `BKM metric == Hessian of log Z` — agreement to the finite-difference floor.
- `BKM != symmetrized (SLD-style) covariance` — they differ at $O(10^{-1})$; the choice is real, not notational.
- `cubic response tensor C_ijk is totally symmetric`.
- `C_ijk == d_i G_jk` — this is the note's $\mathcal C_{N\zeta\zeta}=\partial_NG_{\zeta\zeta}$.

The generators are drawn at random on each run, so the printed magnitudes are run-dependent; the pass/fail verdicts are not.

The commitment to BKM and the demand for that integrable structure are **the same commitment**, by a theorem the vault currently keeps only in retired material. Grasselli and Streater, *On the uniqueness of the Chentsov metric in quantum information geometry* (arXiv:math-ph/0006030), Theorem 19: *if the connections $\nabla^{(1)}$ and $\nabla^{(-1)}$ are dual with respect to a monotone Riemannian metric $g$ on $\mathcal M$, then $g$ is a scalar multiple of the BKM metric* — for invertible density operators in finite dimensions. So:

$$
\boxed{\text{dually flat}+\text{monotone}\;\Longrightarrow\;\text{BKM, up to scale.}}
$$

[[causal-scale-theory/inq|CST]] and [[basic-concepts/hessians/inq|the Hessian module]] motivate BKM as the coincidence Hessian of relative entropy and stop there. The uniqueness statement is stronger and is the one the programme actually needs, because it converts "we use BKM" from a choice into a consequence of wanting $G$ and $\mathcal C$ to come from one potential. It belongs in a canonical note, not in `scale-as-modular-observable/misc/`.

What the identification buys, beyond a name: the dual potential and Legendre (e/m) coordinates, so that the covariance-versus-precision step of [[basic-concepts/hessians/fourier-covariance-and-precision|Fourier precision]] is the canonical coordinate duality of the manifold rather than an imported operation; the Koszul forms and Hessian curvature as invariants of the response; and a developed literature on when a Hessian structure exists globally on a given affine manifold.

## 2. The missing real-form datum is produced by the Hessian structure

[[algebra/real-forms-and-factive-spacetime|Real forms and factive spacetime]] proves that an antiholomorphic involution $\tau$ on a complex threefold has a real three-dimensional fixed locus, and then records the gap: "It is still conditional on the additional datum $\tau$. A complex threefold by itself does not select a real form."

A Hessian manifold selects both. On $TM$ with adapted coordinates $z^j=x^j+iy^j$ and $\Phi(z,\bar z):=\Psi(\operatorname{Re}z)$:

$$
\frac{\partial^2\Phi}{\partial z^i\partial\bar z^j}
=\tfrac14\bigl(\partial_{x^i}\partial_{x^j}+\partial_{y^i}\partial_{y^j}\bigr)\Phi
=\tfrac14\,(\operatorname{Hess}\Psi)_{ij},
$$

so the Kähler metric on $TM$ restricted to $\{y=0\}$ *is* the Hessian metric, and $\tau(z)=\bar z$, i.e. $(x,y)\mapsto(x,-y)$, is an antiholomorphic involution with fixed locus the zero section. Satoh's theorem (quoted in arXiv:2507.23264) makes this a biconditional: the induced almost Hermitian structure on $TM$ is **Kählerian if and only if** $(\nabla,g)$ is a Hessian structure on $M$.

Receipts: `Levi form of Kahler potential Phi(z)=psi(Re z) equals (1/4)*Hess(psi)`, 300 random points at $\dim_{\mathbb C}=3$; `Hess psi positive definite`; `tau(z)=conj(z) ... fixed locus {y=0}`.

Hence

$$
\boxed{
\begin{aligned}
&\text{physical tangent is dually flat (BKM) and 3-dimensional}\\
\Longrightarrow\;&\text{complex threefold }TM,\ \tau=\text{conjugation},\ \dim_{\mathbb R}(TM)^\tau=3,\\
&\text{with K\"ahler potential }=\text{the log-partition function.}
\end{aligned}}
$$

This is the boxed implication of the real-forms note, run backwards, with the conditional datum supplied. Two honest limits travel with it. The three is the dimension of **the physical tangent quotient**, not of physical space; it does not by itself deliver a carrier for [[causal-wall-spectral-theory/open-questions/bkm-source-kernel-comparison|W2]], whose target is a $k$-indexed mode space. And $TM$ is noncompact and Kähler, so this route and the $S^6$ route are mutually exclusive rather than complementary — see §3.

## 3. The $S^6$ manuscript is a negative result for the response programme

[[algebra/s6-manuscript-branch|The $S^6$ branch]] lists six construction obligations, all downstream. There is a prior obstruction, stated by the manuscript itself.

**Remark 3.23.** On $F^1(z)$ the Hermitian form $h(v,v')=iQ_0(v,\overline{v'})$ has Gram matrix

$$
-\begin{pmatrix}12\operatorname{Im}\tau&12\operatorname{Im}\mu\\12\operatorname{Im}\mu&2\operatorname{Im}\beta\end{pmatrix},
\qquad
\det=24\operatorname{Im}\tau\cdot D,
\qquad
D:=\operatorname{Im}\beta-\frac{6(\operatorname{Im}\mu)^2}{\operatorname{Im}\tau}<0 ,
$$

the last inequality being the manuscript's own condition $(\beta3)$. Receipts, over 20 000 random admissible $(\operatorname{Im}\tau>0,\ D<0)$: `S6 Gram determinant identity` and `S6 Hodge form signature is (1,1) for BOTH signs of Q0`.

The manuscript draws the consequences: "the fibres of $J$ carry no monodromy-compatible polarisation"; "$(V,Q_0,N)$ supports no polarised limit mixed Hodge structure"; and the nilpotent orbit theorem "does not apply in the present setting." Separately, $b_2(X)=0$, so $X$ carries no Kähler metric and no Kähler current, and $a(X)=1$.

So this threefold supplies **no positive Hodge metric, no polarisation, no Kähler potential, and no limit mixed Hodge structure**. It cannot carry a positive response block, and it cannot be a $TM$ of §2. Whatever the branch is eventually good for, it is not a carrier for $G^{\mathrm{BKM}}$.

The signature is informative rather than merely negative. The one positive direction is $\operatorname{Im}\tau$ — the modular, i.e. scale, direction — and the extra directions of the rank-four lattice are the negative one. Transcribed into [[program-core/common-response-form|CRM]] variables that reads $G_{NN}>0$ with the nonconstant sector **negative**, contradicting $G_{\zeta\zeta}\succeq0$. Positivity of the mean-zero block is therefore a load-bearing hypothesis with a concrete counter-model in the library, not a formality.

One correction to the branch note's obligation list. Proposition 2.11(ii) records that $\Delta(3,4,\infty)$ is the orientation-preserving index-two subgroup of the reflection group of the hyperbolic triangle with angles $\pi/3,\pi/4,0$. The base therefore *does* carry a canonical antiholomorphic involution. Whether any $\sigma_a,\sigma_b,\sigma_c$ lifts to $X$ compatibly with $\Pi(z)$ and the lattice $\Lambda$ is a sharp, checkable question and is obligation zero for any real-form use of the branch. By §2 it is not the cheapest route to a $\tau$.

## 4. The decoherence--diffusion trade-off is the vault's own Schur complement

[[vendor/postquantum-gravity/cq-construction|The CQ construction]] records the trade-off $4D_0\succeq D_2^{-1}$ and its saturation $4D_2=D_1D_0^{-1}D_1$; [[library/stochastic-modes-in-postquantum-gravity/inq|Oppenheim and Sajjad]] write it as $\mathcal D_0\geq64\pi^2G_N^2\mathcal D_2^{-1}$ with $\mathcal D_1=8\pi G_N$. [[program-core/common-response-form|The response matrix]] independently records hidden-mode elimination as $G^{\mathrm{eff}}_{xx}=G_{xx}-G_{xh}G_{hh}^{+}G_{hx}$.

These are one piece of algebra. For a symmetric block matrix,

$$
\begin{pmatrix}D_0&D_1\\D_1&D_2\end{pmatrix}\succeq0
\iff
D_0-D_1D_2^{-1}D_1\succeq0
\iff
D_2-D_1D_0^{-1}D_1\succeq0 ,
$$

and saturation is exactly vanishing of the Schur complement. Receipts, 4000 random $2\times2$ blocks each: `trade-off <=> block PSD, form A`, `form B`, `saturation ... makes the Schur complement exactly 0`.

Three consequences.

**Conditional purity is a Schur complement equal to zero.** [[vendor/postquantum-gravity/commentary/descent-instead-of-diffusion|The descent reading]] argues in words that at saturation nothing is lost along a history. In the CRM's own grammar that is the statement that the eliminated sector contributes no correction to the retained block. The vendor's central interpretive claim is computable with machinery the core already has.

**The trade-off is a worked instance of the W2 arrow's type.** In the linearised theory $\langle\Phi\Phi\rangle=\frac{3}{2\alpha k^4}+\cdots$ with $\alpha:=D_2^{-1}$, so at saturation the spatial precision is $\propto D_2^{-1}=D_1^{-1}D_0D_1^{-1}$: a state-space positive kernel, conjugated by the coupling, returned as a spatial kernel. That is $\mathcal W_{\mathrm{BKM}\to\mathrm{spatial}}$'s type — an $L$ and an $M_\omega$ with no free function — obtained as a consequence of complete positivity rather than postulated. The decoherence kernel $D_0$ is not itself a BKM form, and closing that gap is the actual work; but the arrow's existence in a covariant theory is no longer hypothetical.

**It answers the unrestricted-response no-go.** [[critical-scale-kernels/unrestricted-response-no-go|That no-go]] says predictive content begins only once independent structure restricts the response function, and lists "a flow equation with independently fixed boundary data" among the admissible restrictions. A trade-off inequality is precisely such a restriction: it **bounds the spatial kernel by the state-space kernel**, so $C(k)$ cannot be chosen pointwise from the target spectrum. This is the most direct answer in the vault to the objection that broke [[causal-wall-spectral-theory/inq|CWST]]'s predictive claim.

## 5. The one genuinely new import: semiorthogonal decompositions

[[program-core/common-response-form|CRM]] wants a wall that is "genuinely noninvertible," and currently realises it by a state-preserving conditional expectation with the Pythagorean split $\mathbb G^{\mathrm{pre}}=\mathbb G^{\mathrm{obs}}+\mathbb G^{\mathrm{wall}}$. [[spectral-wall-descent/conditional-expectation-balance|The modular existence gate]] then records that by Takesaki's theorem such an expectation exists only when $\sigma_t^\varphi(\mathcal N)=\mathcal N$, so "a generic measurement context therefore does not admit the expectation required by the exact theorem."

A **semiorthogonal decomposition** is the standard mathematics of an exact decomposition that is orthogonal in one direction only:

$$
\mathrm{RHom}(\mathcal O_X(i),A)=0\ \ \forall A\in\mathcal A_X,
\qquad
\mathrm{RHom}(A,\mathcal O_X(i))\ \text{unconstrained},
$$

with mutation functors supplying the transport between decompositions. That is the asymmetry the wall is supposed to have, and it does not require a two-sided projection. The audit finds **zero canonical uses** of semiorthogonal decompositions, Kuznetsov components, derived categories, or mutations anywhere in the vault.

[[library/hodge-atoms-spectral-triples-bps/inq|Raugas]] is the natural bridge, because it puts a JLO cyclic cocycle on the same object as a semiorthogonal decomposition — and the JLO Chern character, transgression, and index pairings are already canonical in [[spectral-wall-descent/index-and-curvature-transgression|index and curvature transgression]]. Its Conjecture (selection rule) is also the right shape for a programme that wants a categorical vanishing to *be* a physical selection rule rather than to model one. Two cautions: the vault's "wall-crossing" is explicitly disclaimed as not the Bridgeland invariant in [[conservation-of-causal-charge/inq|the charge module]], and its "Stokes" is Stokes' theorem, so both terms collide with the imported vocabulary.

## 6. What not to import

Polarised variation of Hodge structure, period maps, and special geometry, *as such*. The structure the programme needs — one potential yielding both a metric and a symmetric cubic, with an integrability condition — is the Hessian/dually-flat structure of §1, which it already has. A Frobenius manifold is a different object (flat metric, cubic from a separate potential, WDVV), and polarised VHS requires a polarisation that the only concrete threefold in the library provably lacks. Importing Hodge theory would be a harder framework delivering a package already in hand.

## Ordered recommendations

1. Write the BKM-uniqueness theorem into a canonical note (`basic-concepts/hessians/` or `program-core/`), citing Grasselli--Streater Thm 19, and retire the retired-document version. Status: **[EXACT, FINITE DIMENSIONS]**.
2. Rename the CRM structure as a Hessian/dually-flat manifold and state the Codazzi condition as the integrability test. Status: **[IDENTIFICATION]**.
3. Add the $TM$ construction to [[algebra/real-forms-and-factive-spacetime|the real-forms note]] as a canonical source of $\tau$, with the honest caveat that the three is the tangent dimension. Status: **[EXACT, WITH DECLARED CARRIER CAVEAT]**.
4. Record Remark 3.23 in [[algebra/s6-manuscript-branch|the $S^6$ branch]] as a prior obstruction, above the six existing obligations. Status: **[NO-GO FOR RESPONSE-CARRIER USE]**.
5. Identify the CQ trade-off with the CRM Schur complement, and open the question whether $D_0$ can be exhibited as a BKM form. Status: **[OPEN CONSTRUCTION]**; this is the highest-value item, because it is the only recorded route past the unrestricted-response no-go.
6. Consume `library/hodge-atoms-spectral-triples-bps` into a vendor module, scoped to semiorthogonal decomposition as a model of one-sided wall loss. Status: **[PROPOSED IMPORT]**.
