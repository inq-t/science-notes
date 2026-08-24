# KO-Dimension as a Morita Class

KO-dimension is not a dimension. It is the Morita class of a Clifford algebra, and by Wall's theorem that class is equally the supercommutant of an irreducible super-representation — the algebra of transformations that a graded symmetry cannot detect. There are exactly eight such classes over $\mathbb R$ and two more over $\mathbb C$, and that census of ten is the tenfold way. Connes' sign table for $(J,D,\gamma)$ is not a convention chosen to make the standard model work: it is the eightfold half of that census, written in operator form. This reframing dissolves one complaint and sharpens another. The complaint that the KO-dimension $6$ of the finite geometry $F$ was never derived misidentifies the free parameter — given a four-dimensional spin manifold and the demand that the fermionic action be a Pfaffian, the class is forced. What was never derived is the metric dimension $4$, the Pfaffian demand itself, and the three generations.

## The label answers a different question than the name suggests

A spectral triple carries two independent notions of size. The **metric dimension** is read off the growth of the spectrum of $D$; for a finite geometry it is $0$. The **KO-dimension** is read off three signs,

$$
J^2=\varepsilon,\qquad JD=\varepsilon' DJ,\qquad J\gamma=\varepsilon''\gamma J\ \ \text{(even case)},
$$

and is valued in $\mathbb Z/8$. Connes introduces the divorce of the two as a device and does not ground it. Wall's theorem grounds it: the second label is Morita-theoretic, an invariant of an algebra-with-grading-and-involution up to equivalence of module categories, and a Morita invariant has no reason whatever to track the growth of a spectrum. A finite-dimensional algebra with metric dimension $0$ and KO-dimension $6$ is not a paradox but a category error dissolved.

## Argument

[[two-tens]] separates the two numbers that invite the confusion. Connes' $10$ is a residue, $4+6\equiv 2 \pmod 8$, written before reduction; Baez's $10$ is a cardinality, $8+2$, counting classes in $\mathbb Z/8\sqcup\mathbb Z/2$. The identification fails, and Connes' own gloss on his $10$ points at string theory rather than at Wall. The shared structure is the $8$, not the $10$.

[[the-eightfold-in-the-sign-table]] exhibits the sign table as the mod-$8$ Morita classification of real Clifford algebras, shows that odd KO-dimension carries no grading and therefore no chirality, and adds the two complex classes — spectral triples with no real structure at all — to complete the ten. The dictionary to the Altland–Zirnbauer classes is exact: $J$ or $\gamma J$ commuting with $D$ is time reversal, the anticommuting one is particle–hole.

[[what-commutes-with-everything]] takes the commutant reading seriously. Schur's lemma says the endomorphisms of an irreducible are exactly what no symmetry can see, and Frobenius bounds that undetectable residue to $\mathbb R,\mathbb C,\mathbb H$; the graded version admits one bit of sign and the residue count rises to ten. Three distinctions are load-bearing and are made there: the commutant of an algebra need not be commutative, commutation is imposed by Connes as a relation between a left and a right action rather than as a property of one algebra, and the passage from commutant to double commutant is a Galois closure of the same shape as the one in [[philosophy/indiscernibility-of-identicals/symmetry-as-dual-of-discernment|the invariance/automorphism connection]].

[[selecting-the-class]] audits the derivation. Requiring a nonvanishing antisymmetric form $A_D(\xi',\xi)=\langle J\xi',D\xi\rangle$ on $\mathcal H^+$ forces $\varepsilon''=-1$ and $\varepsilon\varepsilon'=-1$, which among the four even classes holds only at $n=2$. Given $\dim M=4$, the class of $F$ follows as $6=2-4$ in $\mathbb Z/8$. The residual inputs are named, and the difference between a filter and a generator is kept in the terms [[symmetry-groups-select/finite-algebra-filters|already set for the finite algebra]].

## Claim levels

| Status | Content |
|---|---|
| Exact | the sign table as stated; that odd $n$ carries no $\gamma$; that $\varepsilon$ is not a homomorphism $\mathbb Z/8\to\{\pm1\}$, since $\varepsilon(2)\varepsilon(2)=+1\neq\varepsilon(4)$; that $A_D(\xi',\xi)=\varepsilon\varepsilon' A_D(\xi,\xi')$; that $\varepsilon''=+1$ makes $A_D$ vanish identically on $\mathcal H^+$; that $n=2$ is the unique even class with $\varepsilon''=-1$ and $\varepsilon\varepsilon'=-1$; Frobenius; Schur; Wall's count of ten real super division algebras and their identification with the Morita classes of real and complex Clifford algebras; the double commutant theorem; $M_3(\mathbb C)$ Morita equivalent to $\mathbb C$ and $\mathbb H$ inequivalent to $\mathbb R$ over $\mathbb R$ |
| Exact, hypotheses named | additivity of KO-dimension under products, for the standard product construction — the even–even case admits inequivalent choices of $J$ and of $D$, and the naive $J_1\otimes J_2$ cannot be additive for every pair; verified here only for $(4,6)$, where the signs reproduce $n=2$ exactly |
| Adopted convention | reading "KO-dimension" as a Morita class rather than a dimension, and treating the metric/KO divorce as thereby explained rather than merely permitted |
| Proposed reading | the commutant as the algebraic form of a difference that makes no difference, and the tenfold way as the completeness theorem for such differences once a $\mathbb Z/2$-grading may intervene |
| Contested | that anything in the coincidence $4+6=10$ carries structural content; Connes offers it as a resemblance to string theory and it is treated here as a resemblance only |
| Open | why the metric dimension is $4$; why the fermionic action should be a Pfaffian rather than a determinant; the number of generations; whether any principle selects a class of the ten rather than testing one |
| Outside this module | whether causal-scale or wall axioms generate the finite algebra at all, which belongs to [[symmetry-groups-select/entry\|symmetry selection]]; anomaly and hypercharge filters; the identity of indiscernibles and its quotient, owned by [[philosophy/indiscernibility-of-identicals/entry\|the indiscernibility module]] |
