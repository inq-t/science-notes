# Two Tens

Two numbers written $10$ occur in the neighbourhood of the spectral standard model, and they are of different logical types. Connes' $10$ is a residue in $\mathbb Z/8$, obtained as $4+6$ and immediately reduced to $2$; Wall's $10$ is the cardinality of a classification, obtained as $8+2$ where the summands index two different periodicities. Nothing passes between them. What the two constructions do share is the $8$, and the $8$ is one fact stated twice.

## Connes' ten is a sum before reduction

The finite geometry $F$ has KO-dimension $6$, the spin manifold $M$ has KO-dimension $4$, and the product has $4+6=10\equiv 2$. There are eight KO-dimensions, not ten; $10$ is an unreduced representative of $2$, and the choice to display it unreduced is rhetorical. [[library/ncg-standard-model-neutrino-mixing/inq|Connes]] says so in the same breath in which he writes it:

> Of course the above $10$ is very reminiscent of string theory, in which the finite space $F$ might be a good candidate for an "effective" compactification at least for low energies.

with a footnote conceding that the model at hand is not supersymmetric. [[library/why-the-standard-model/inq|Chamseddine and Connes]] later make the same presentational choice — "the raison d'être for $F$ is to correct the K-theoretic dimension from four to ten (modulo eight)" — where the parenthesis does all the mathematical work and *ten* does none.

## Wall's ten is a count of classes

[[library/the-tenfold-way/inq|Wall's classification]] of real super division algebras yields ten, decomposing as

$$
8+2,\qquad
8=\left|\,\mathrm{BW}(\mathbb R)\,\right|=\left|\mathbb Z/8\right|,
\qquad
2=\left|\,\mathrm{BW}(\mathbb C)\,\right|=\left|\mathbb Z/2\right| ,
$$

the **graded** Morita classes of real and of complex Clifford algebras respectively. This is a cardinality of a disjoint union of two cyclic groups of different orders. It is not an element of either.

## Why the identification fails

An element of $\mathbb Z/8$ and the size of $\mathbb Z/8\sqcup\mathbb Z/2$ are not comparable quantities, and the arithmetic that produces them is unrelated: $4+6$ is addition in the group, $8+2$ is addition of the sizes of two sets. A structural link would have to make Connes' KO-dimension of the *product geometry* into a *count* of something, and no such count is available.

Nor does anyone claim otherwise. A search of the arXiv for papers pairing "tenfold way" with "spectral triple", "noncommutative geometry", "KO-dimension" or "Connes" returns nothing; the nLab entries for *ten-fold way* and for *KO-dimension* do not cross-reference each other; and Baez's article, its Notices version, and the accompanying blog posts contain no occurrence of "Connes", "KO-dimension" or "spectral triple". The nearest thing to a collision is Kaufmann, Li and Wehefritz-Kaufmann's "generalized $\mathrm{KR}_{10}$-cycle with KO-dimension $2\ (=10\bmod 8)$", which is a third $10$ — two coupled $\mathrm{KR}_5$-cycles — with no super-division-algebra content whatever.

The resemblance is therefore of the same species as the one Connes himself flags, and it should be filed with it. The real connection runs through the sign table, as in [[the-eightfold-in-the-sign-table]], and that connection has nothing to say about $4+6$.

## The eight is shared, and is one fact

Real Clifford algebras are graded-Morita-periodic with period $8$:

$$
U(\mathrm{Cl}_{p+8,q})
\cong
U(\mathrm{Cl}_{p,q})\otimes M_{16}(\mathbb R),
$$

after forgetting the grading, while

$$
\mathrm{Cl}_{p+8,q}
\simeq_{\mathrm{gr\text{-}Morita}}
\mathrm{Cl}_{p,q},
$$

where (U) is the forgetful functor from graded to ordinary algebras. The first relation is an ordinary algebra isomorphism after explicit matrix stabilization; the second is the graded categorical equivalence that forgets that matrix size. This Clifford-module periodicity is the algebraic input to real Bott periodicity, rather than the complete topological theorem itself. Connes' sign table repeats with period $8$ for exactly that reason, and Wall's eight real classes are the eight residues of exactly that periodicity. The complex algebras are periodic with period $2$, which supplies Wall's remaining two and, on Connes' side, the two kinds of spectral triple that carry no real structure at all.

So the honest statement of the link is: Connes' $\mathbb Z/8$ **is** the eightfold part of the tenfold way. His $10$ is not the tenfold way's $10$.
