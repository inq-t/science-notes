# The Eightfold in the Sign Table

Connes' definition of a real structure fixes three signs as a function of $n\in\mathbb Z/8$. That table is not a bookkeeping convention adopted to index cases; it is the mod-$8$ Morita classification of real Clifford algebras written in terms of operators on a Hilbert space. Odd $n$ has no grading, so half the classes cannot carry a chiral theory at all. Adjoining the spectral triples that carry no real structure supplies the two complex classes, and the resulting ten are the tenfold way, in exact correspondence with the Altland–Zirnbauer symmetry classes.

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

## Why it is a Morita classification and not a convention

The three signs are exactly the data distinguishing the real Clifford algebras $\mathrm{Cl}_{p,q}$ up to Morita equivalence, and the period $8$ is real Bott periodicity. A Morita class is an invariant of the module category, so a real spectral triple of KO-dimension $n$ is not "a space of dimension $n$" but a representation whose graded commutation data lies in the $n$-th class. Two consequences follow at once.

First, the divorce of metric from KO-dimension is explained rather than merely permitted. The metric label is analytic — spectral growth of $D$ — and the KO label is Morita-theoretic. A finite-dimensional algebra can be in any class whatever while its Dirac operator has finite spectrum. Connes introduces the divorce as a device and cites the Podleś sphere as precedent; Wall's theorem says no precedent is needed.

Second, the eight classes are all of them. There is no ninth real option to look for and no continuous parameter hiding in the choice. Whatever selects a class must be a discrete, algebraic condition. That is what makes [[selecting-the-class]] a well-posed question rather than a plea.

## Odd dimensions cannot be chiral

For odd $n$ the definition assigns no $\varepsilon''$, because there is no $\gamma$: an odd spectral triple has no $\mathbb Z/2$-grading of $\mathcal H$. A chiral gauge theory needs one. So before any physics is imposed, four of the eight real classes are excluded, and the live options are

$$
n\in\{0,2,4,6\},\qquad
(\varepsilon,\varepsilon'')=(+,+),\ (-,-),\ (-,+),\ (+,-),
$$

with $\varepsilon'=+$ throughout. Four sign pairs, each occurring once — the even part of the table is a bijection onto $\{\pm1\}^2$.

## The two complex classes complete the ten

A spectral triple need not carry a real structure. Dropping $J$ entirely and keeping the even/odd distinction gives two further kinds, and these are the two Morita classes of complex Clifford algebras, period $2$. Eight plus two is Wall's ten. The census of *kinds of spectral triple* and the census of *real super division algebras* are the same census.

Krajewski's dictionary makes the physics correspondence explicit: an antiunitary that commutes with $D$ plays the role of time reversal $T$, one that anticommutes plays particle–hole $C$, and $J$ and $\gamma J$ supply the two candidates. The eight real KO-dimensions are the eight real Altland–Zirnbauer classes; the two complex ones are $\mathrm A$ and $\mathrm{AIII}$. A real spectral triple of KO-dimension $n$ **is** a symmetry class in that table, and "ten fundamentally different kinds of matter" and "eight KO-dimensions plus two" are one statement.

## A caution about products

The KO-dimension of a product is additive, but the naive product data are not automatically the witness. With $J=J_1\otimes J_2$ one gets $\varepsilon=\varepsilon_1\varepsilon_2$, and $\varepsilon$ is not a homomorphism $\mathbb Z/8\to\{\pm1\}$: $\varepsilon(2)\varepsilon(2)=+1$ while $\varepsilon(4)=-1$. So the naive formula cannot reproduce additivity for every pair, and the even–even case genuinely admits inequivalent choices of $J$ and of $D$. For the pair actually used it does work, and by direct multiplication:

$$
\varepsilon(4)\varepsilon(6)=(-)(+)=-=\varepsilon(2),
\qquad
\varepsilon''(4)\varepsilon''(6)=(+)(-)=-=\varepsilon''(2),
\qquad
\varepsilon'(4)=\varepsilon'(6)=+=\varepsilon'(2).
$$

Connes notes the corresponding hypothesis in passing — that $J_1$ must commute with $\gamma_1$ for $J$ to commute with $D$ — which is the $n=4$ entry $\varepsilon''=+$ doing the work.
