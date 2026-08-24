# The Eightfold in the Sign Table

Connes' definition of a real structure fixes three signs as a function of $n\in\mathbb Z/8$. That table is not a bookkeeping convention adopted to index cases; it is the mod-$8$ **graded** Morita classification of real Clifford algebras written in terms of operators on a Hilbert space. Odd $n$ has no grading, so half the classes cannot carry a chiral theory at all. Adjoining the spectral triples that carry no real structure supplies the two complex classes, and the resulting ten stand in exact correspondence with the Altland–Zirnbauer symmetry classes — a correspondence derivable from the table itself, and one that Connes nowhere states.

## The table

A real structure of KO-dimension $n$ on a spectral triple $(\mathcal A,\mathcal H,D)$ is an antilinear isometry $J$ with

$$
J^2=\varepsilon,\qquad JD=\varepsilon' DJ,\qquad J\gamma=\varepsilon''\gamma J,
$$

the last only where a grading $\gamma$ exists, together with the order-zero and order-one conditions

$$
[a,b^0]=0,\qquad \left[[D,a],b^0\right]=0,\qquad b^0:=Jb^*J^{-1}.
$$

The signs are

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| $\varepsilon$ | $+$ | $+$ | $-$ | $-$ | $-$ | $-$ | $+$ | $+$ |
| $\varepsilon'$ | $+$ | $-$ | $+$ | $+$ | $+$ | $-$ | $+$ | $+$ |
| $\varepsilon''$ | $+$ | — | $-$ | — | $+$ | — | $-$ | — |

The triple $(\varepsilon,\varepsilon',\varepsilon'')$, with the presence or absence of the third entry counted as part of the datum, takes eight distinct values. It is a complete invariant of $n$.

## Why it is a classification and not a convention

The signs are exactly the data distinguishing the real Clifford algebras $\mathrm{Cl}_{p,q}$ up to graded Morita equivalence, and the period $8$ is real Bott periodicity, $\mathrm{Cl}_{p+8,q}\simeq\mathrm{Cl}_{p,q}$. The qualifier **graded** is not decorative: as ungraded algebras the real Clifford algebras collapse to far fewer classes, and Wall's $\mathbb Z/8$ exists only in the graded category. Two consequences follow.

First, the divorce of metric from KO-dimension is explained rather than merely permitted. The metric label is analytic — spectral growth of $D$ — while the KO label is an invariant of a graded module category. A finite-dimensional algebra can sit in any class whatever while its Dirac operator has finite spectrum. Connes introduces the divorce as a device and cites the Podleś sphere as precedent; Wall's theorem says no precedent is needed.

Second, the eight classes are all of them. There is no ninth real option and no continuous parameter hiding in the choice, so whatever selects a class must be a discrete algebraic condition. That is what makes [[selecting-the-class]] a well-posed question rather than a plea.

## Odd dimensions cannot be chiral

For odd $n$ the definition assigns no $\varepsilon''$, because there is no $\gamma$: an odd spectral triple has no $\mathbb Z/2$-grading of $\mathcal H$. A chiral gauge theory needs one. So before any physics is imposed, four of the eight real classes are excluded, and the live options are

$$
n\in\{0,2,4,6\},\qquad
(\varepsilon,\varepsilon'')=(+,+),\ (-,-),\ (-,+),\ (+,-),
$$

with $\varepsilon'=+$ throughout — the even part of the table is a bijection onto $\{\pm1\}^2$.

This exclusion is definitional rather than proved: Connes' definition makes *even* synonymous with carrying $\gamma$. It is also convention-relative, since in $KK$-theory an odd triple is equivalently an even $\mathrm{Cl}_1$-graded object. The content that survives both caveats is that the four sign-pairs above exhaust the graded case.

## The dictionary to the tenfold way

Read $J$ as time reversal when it commutes with $D$ and as particle–hole when it anticommutes, and let the other operator be $\gamma J$. Then

$$
T^2=\varepsilon\ \ (\varepsilon'=+1),
\qquad
C=\gamma J,
\qquad
C^2=(\gamma J)^2=\varepsilon''\,J^2\gamma^2=\varepsilon\,\varepsilon'' .
$$

Running this over the table reproduces the eight real Altland–Zirnbauer classes exactly:

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| $T^2$ | $+$ | — | $-$ | $-$ | $-$ | — | $+$ | $+$ |
| $C^2$ | $+$ | $+$ | $+$ | — | $-$ | $-$ | $-$ | — |
| class | BDI | D | DIII | AII | CII | C | CI | AI |

A spectral triple carrying no $J$ at all, even or odd, supplies the two complex classes $\mathrm A$ and $\mathrm{AIII}$. Eight plus two is Wall's ten: the census of *kinds of spectral triple* and the census of *real super division algebras* are one census, and "there are ten fundamentally different kinds of matter" and "there are eight KO-dimensions plus two" are one statement.

**Attribution.** The arithmetic above is self-contained and checkable from the table. The correspondence is stated as such in Krajewski's lectures on finite spectral triples and the tenfold way, with the same $T\leftrightarrow J$ or $\gamma J$ dictionary. In the published literature it appears in pieces rather than as a headline theorem: Kaufmann, Li and Wehefritz-Kaufmann reproduce Connes' sign table as "the KO-dimension of a KR-cycle, first introduced by Connes" in an explicitly Altland–Zirnbauer setting, and Bourne, Carey and Rennie build real spectral triples by symmetry type, citing De Nittis, Grossmann and Schulz-Baldes for the passage from a symmetric condensed-matter system to a Real spectral triple. Connes states none of this; the link is not his.

## A caution about products

The KO-dimension of a product is additive, but the naive product data are not automatically the witness. With $J=J_1\otimes J_2$ one gets $\varepsilon=\varepsilon_1\varepsilon_2$, and $\varepsilon$ is not a homomorphism $\mathbb Z/8\to\{\pm1\}$: $\varepsilon(2)\varepsilon(2)=+1$ while $\varepsilon(4)=-1$. So the naive formula cannot reproduce additivity for every pair, and the even–even case genuinely admits inequivalent choices of $J$ and two candidate Dirac operators. For the pair actually used it does work, by direct multiplication:

$$
\varepsilon(4)\varepsilon(6)=(-)(+)=-=\varepsilon(2),
\qquad
\varepsilon''(4)\varepsilon''(6)=(+)(-)=-=\varepsilon''(2),
\qquad
\varepsilon'(4)=\varepsilon'(6)=+=\varepsilon'(2).
$$

Connes notes the corresponding hypothesis in passing — that $J_1$ must commute with $\gamma_1$ for $J$ to commute with $D$ — which is the $n=4$ entry $\varepsilon''=+$ doing the work.
