# Mutation, Recollement, and the Directed \(A_2\) Example

Mutation changes the ordered presentation of a semiorthogonal decomposition, while recollement glues a category from a closed sector and an open quotient using six adjoint functors. The derived category of the directed \(A_2\) quiver gives the smallest exact example in which one morphism direction vanishes, the reverse direction contains an extension, an admissible projector forgets a component, and mutation remains a reversible change of components.

## Mutation is not projection

Let \(i_{\mathcal A}:\mathcal A\hookrightarrow\mathcal T\) be admissible. The **left mutation through \(\mathcal A\)** and **right mutation through \(\mathcal A\)** are defined by the exact triangles

$$
i_{\mathcal A}i_{\mathcal A}^!X
\longrightarrow X
\longrightarrow \mathbb L_{\mathcal A}X
\longrightarrow,
$$

$$
\mathbb R_{\mathcal A}X
\longrightarrow X
\longrightarrow i_{\mathcal A}i_{\mathcal A}^*X
\longrightarrow.
$$

They satisfy

$$
\mathbb L_{\mathcal A}X\in\mathcal A^\perp,
\qquad
\mathbb R_{\mathcal A}X\in{}^\perp\mathcal A.
$$

For an admissible pair

$$
\mathcal T=\langle\mathcal A,\mathcal B\rangle,
$$

mutation produces new decompositions

$$
\mathcal T
=\langle\mathbb L_{\mathcal A}(\mathcal B),\mathcal A\rangle
=\langle\mathcal B,\mathbb R_{\mathcal B}(\mathcal A)\rangle.
$$

The restrictions

$$
\mathbb L_{\mathcal A}|_{\mathcal B}:
\mathcal B\xrightarrow{\sim}\mathbb L_{\mathcal A}(\mathcal B)
$$

and its corresponding right mutation are equivalences under the standard admissibility hypotheses. The whole-category functor \(\mathbb L_{\mathcal A}\) kills \(\mathcal A\), but mutation of the neighboring component is reversible. Therefore mutation should be interpreted as **transport between decompositions**, not as a physical loss law.

For exceptional collections, adjacent mutations can satisfy braid relations. This is one reason braid monodromy and categorical presentation naturally meet, but a braid action remains invertible unless a separate projection or quotient is applied.

## Recollement

A recollement is stronger than one semiorthogonal decomposition. It consists of categories \(\mathcal T_Z,\mathcal T,\mathcal T_U\) and six exact functors

$$
i^*\dashv i_*\dashv i^!,
\qquad
j_!\dashv j^*\dashv j_*,
$$

where \(i_*,j_!,j_*\) are fully faithful, \(j^*i_*=0\), and every \(X\in\mathcal T\) has two canonical triangles

$$
j_!j^*X\longrightarrow X\longrightarrow i_*i^*X\longrightarrow,
$$

$$
i_*i^!X\longrightarrow X\longrightarrow j_*j^*X\longrightarrow.
$$

Consequently,

$$
\mathcal T
=\langle i_*\mathcal T_Z,j_!\mathcal T_U\rangle
=\langle j_*\mathcal T_U,i_*\mathcal T_Z\rangle.
$$

Recollement exposes two ways of embedding the same quotient sector back into the whole. This is potentially valuable for a wall: it distinguishes restriction to what is presented from the two extension procedures that reconstruct compatible global objects. It still supplies no positivity, probability, or state by itself.

## The directed \(A_2\) quiver

Let \(Q\) be the quiver

$$
1\longrightarrow2
$$

and let \(A=kQ\) be its path algebra over a field \(k\). An \(A\)-module is a representation

$$
V_1\xrightarrow{f}V_2.
$$

The two simple modules are

$$
S_1=(k\to0),
\qquad
S_2=(0\to k).
$$

In \(\mathcal T=D^b(\operatorname{mod}A)\), each \(S_i\) is exceptional and the simples generate \(\mathcal T\). Direct calculation gives

$$
\operatorname{RHom}(S_2,S_1)\simeq0,
$$

while

$$
\operatorname{Ext}^1(S_1,S_2)\cong k.
$$

Hence

$$
\boxed{
D^b(\operatorname{mod}kQ)
=\langle\langle S_1\rangle,\langle S_2\rangle\rangle}
$$

is semiorthogonal but not orthogonal. Its direction is not cosmetic: the nonzero extension is represented by

$$
0\longrightarrow S_2
\longrightarrow P_1
\longrightarrow S_1
\longrightarrow0,
$$

where

$$
P_1=(k\xrightarrow{\operatorname{id}}k).
$$

Rotating the associated triangle gives

$$
S_1[-1]\longrightarrow S_2\longrightarrow P_1\longrightarrow S_1,
$$

so the left mutation is

$$
\mathbb L_{S_1}(S_2)\simeq P_1.
$$

The decomposition mutates from \(\langle S_1,S_2\rangle\) to \(\langle P_1,S_1\rangle\). No information was destroyed by this mutation. By contrast, the admissible projector onto \(\langle S_1\rangle\) sends \(S_2\) to zero and is genuinely noninvertible.

## Relation to the project's \(A_2\) geometry

The quiver, the \(A_2\) root system, the \(A_2\) cusp, and the three-sheet inverse cover in [[algebra/a2-inverse-cover|the \(A_2\) inverse cover]] share Dynkin and braid combinatorics, but they are different mathematical objects. No canonical functor from that cover to \(D^b(\operatorname{mod}kQ)\) has yet been constructed.

The exact bridge would require a category of vanishing cycles, matrix factorizations, constructible sheaves, or coherent objects naturally attached to the actual degeneration, followed by an equivalence or fully faithful functor identifying its relevant subcategory with the \(A_2\)-quiver model. Only then could sheet monodromy be compared with categorical mutation.

The Artin braid group of the \(A_2\) root system is \(B_3\). In suitable \(A_2\) Fukaya or Calabi--Yau categories, spherical twists can satisfy the corresponding braid relation. The single exceptional-pair calculation above demonstrates directed semiorthogonality and one adjacent mutation; it does not by itself construct that full \(B_3\) action.

## What the example proves—and what it does not

It proves that:

- one-sided exact vanishing is compatible with nontrivial reverse extension data;
- an admissible categorical projection can be noninvertible;
- mutation can change the presented components without loss; and
- \(A_2\) is a minimal laboratory for separating projection from monodromy.

It does not prove that an \(A_2\) singularity causes quantum collapse, selects a physical Hilbert-space sector, supplies a completely positive channel, or generates time. Those claims require the realization obligations in [[semiorthogonal-decompositions/categorical-wall-interface|the categorical wall interface]].
