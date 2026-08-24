# The $A_2$ Inverse Cover

Conditional on the announced three-variable Jacobian counterexample and the local unreviewed analysis, the inverse family supplies an exact algebraic-geometric model of local invertibility without global single-valued invertibility. Near its triple-root locus, the inverse discriminant is an $A_2$ cusp times a smooth parameter; away from that discriminant, the inverse is a connected degree-three finite étale cover with full $S_3=W(A_2)$ sheet monodromy. Its pushforward algebra determines an $\mathfrak{sl}_3(\mathbb C)$ endomorphism bundle: trace-zero multiplication supplies a Cartan, while six complementary off-diagonal root lines appear étale-locally. This supplies neither a compact $SU(3)$ gauge theory nor temporal direction.

## Source and status

The construction is proved internally in the local version-0.1 research note [[library/inbox/a2-spectral-geometry-of-jacobian-counterexample-3d/a2_spectral_geometry_standalone (3).tex|The $A_2$ Spectral Geometry of the 2026 Jacobian Counterexample]], which labels itself unreviewed and records AI-assisted development. Its symbolic receipt verifies five polynomial identities: the depressed-cubic normal form, discriminant identity, coordinate Jacobian, cusp certificate, and discriminant of the obstruction polynomial as a quadratic in one variable. Connectedness, full monodromy, and the Cartan/root decomposition are proof claims in the prose, not receipt outputs. The underlying announced counterexample and nonproper étale-map phenomenon are independently described by [Shuhong Gao's primary arXiv preprint](https://arxiv.org/abs/2608.00222); that paper does not establish the local note's full $A_2$--Lie-bundle package.

Accordingly, **exact** below means exact inside the local note after its counterexample and inverse-family imports are granted. External and peer-review status remain open. This note does not import the source's suggestive use of the word *spectral* as a Connes spectral triple or Hamiltonian spectrum; neither structure is present.

## The cusp in the inverse problem

After a translation removes the quadratic term, the relevant inverse equation has the depressed form

$$
u^3+au+b=0.
$$

Its multiple-root locus is

$$
\Delta(a,b)=4a^3+27b^2=0.
$$

At the triple root $(a,b)=(0,0)$ this is the cuspidal discriminant of the miniversal deformation of the simple singularity

$$
f(x,y)=x^3+y^2.
$$

For the Keller inverse family, the full local statement is the $A_2$ cusp times one smooth parameter along the triple-root curve. The singularity type concerns the discriminant of the inverse family; the polynomial map itself remains everywhere locally biholomorphic because its Jacobian determinant is nonzero.

This is the exact tension:

$$
\det DF\ne0
\quad\Longrightarrow\quad
\text{local inverse},
$$

while nonproperness prevents one global polynomial or holomorphic inverse.

## The three-sheeted inverse cover

Let $U$ be the target with the discriminant removed and restrict the inverse correspondence to the finite étale locus. Then

$$
\pi:X^\circ\longrightarrow U
$$

is a connected finite étale cover of degree three. Analytic continuation permutes the three inverse branches and gives

$$
\rho:\pi_1(U,u_0)\longrightarrow S_3.
$$

For this cover the image is all of $S_3$, identified with $W(A_2)$. Local branches exist and can be labeled on a simply connected patch, but no global labeling is invariant under the full monodromy.

The cover itself descends and exists globally. What fails is its trivialization as three globally labeled copies of $U$. This is the model behind [[algebra/local-global-individuation|local--global individuation]].

## The canonical rank-three algebra

Push forward the structure sheaf:

$$
E:=\pi_*\mathcal O_{X^\circ}.
$$

It is a locally free rank-three $\mathcal O_U$-algebra. Since three is invertible over $\mathbb C$, the trace splits it as

$$
E\cong\mathcal O_U\mathbf1\oplus E_0,
\qquad
E_0:=\ker\operatorname{Tr}_{E/\mathcal O_U}.
$$

Multiplication gives a canonical map

$$
m:E\longrightarrow\operatorname{End}_{\mathcal O_U}(E).
$$

For $x\in E_0$, the multiplication operator $m_x$ has trace zero, so

$$
m(E_0)\subseteq\operatorname{End}_0(E).
$$

After an étale base change that labels the sheets,

$$
E\cong L_1\oplus L_2\oplus L_3.
$$

Then $\operatorname{End}_0(E)$ has fiber $\mathfrak{sl}_3(\mathbb C)$. The two-dimensional diagonal trace-zero multiplication algebra is a Cartan subalgebra, and the six off-diagonal line bundles

$$
\operatorname{Hom}(L_j,L_i),
\qquad i\ne j,
$$

are the six $A_2$ root directions. Sheet monodromy permutes this local root data by the Weyl group.

This endomorphism package is natural for a connected degree-three finite étale cover. The special fact in the Keller example is its occurrence on the inverse cover of an everywhere locally invertible map whose global inverse fails through nonproperness.

## Sheet monodromy and the classical Milnor comparison

The local note constructs the **sheet monodromy** into $S_3$. It does not construct a Picard--Lefschetz identification of the Keller family with Milnor monodromy; it lists that refinement as open.

The separate classical comparison is dimension-sensitive. If \(T\) is the $A_2$ root-lattice Coxeter operator, then

$$
\chi_T(t)=t^2+t+1,
\qquad
T^3=I.
$$

For the plane cusp \(x^3+y^2\), the Milnor monodromy is represented, under the standard comparison, by \(-T\):

$$
\chi_{-T}(t)=t^2-t+1,
\qquad
(-T)^6=I,
$$

with exact order six. Adding one further quadratic suspension \(z^2\) toggles the sign back to \(T\), hence order three. These are classical singularity-theory facts, not additional monodromies already constructed for the Keller inverse cover.

The group cardinality $|S_3|=6$, the six roots, and the order-six plane-cusp Milnor operator are separate invariants. [[algebra/type-ledger|The type ledger]] records the distinction.

## What the construction does not derive

The exact conditional return value is a complex Lie-algebra bundle with local Cartan/root decomposition and Weyl monodromy. A physical color gauge theory would still require:

- a Hermitian structure selecting the compact real form $\mathfrak{su}(3)$;
- a principal $SU(3)$ bundle or equivalent global gauge carrier;
- a connection and curvature;
- a Yang--Mills or spectral action with a derived normalization;
- matter representations, chirality, hypercharges, and anomaly cancellation; and
- a physical realization map showing that this bundle acts on observed fields.

Nor does the cover contain a Connes Dirac operator, KMS state, modular flow, causal order, or record semigroup. Its monodromy is reversible. The construction is therefore an exact conditional seed for a degeneration or symmetry-selection weld, not a derivation of the Standard Model, time, or gravity.

## The bridge test

The $A_2$ package may enter the foundational programme only after a functor from the actual moduli or presentation problem has this inverse cover as its discriminant model. The required statement has the form

$$
\mathfrak F:\mathcal M_{\mathrm{foundation}}
\longrightarrow
\mathcal M_{A_2}
$$

with a proof that the physical degeneration, cover, and monodromy are the pullbacks of the objects constructed above. Choosing $A_2$ because its six roots or $S_3$ symmetry resemble desired particle data would move the unexplained choice into $\mathfrak F$.
