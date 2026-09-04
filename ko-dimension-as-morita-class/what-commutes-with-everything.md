# What Commutes with Everything

Schur's lemma is a theorem about invisibility: the operators commuting with an entire symmetry are exactly the differences in the carrier that are no difference to the symmetry. On a finite-dimensional real irreducible carrier, Frobenius bounds that undetectable residue to $\mathbb R$, $\mathbb C$, $\mathbb H$; grading the same finite-dimensional setting admits one bit of sign between odd elements and the count rises from three to ten. Three distinctions keep this from collapsing into slogan. A commutant need not be commutative — $\mathbb H$ is a commutant. Connes imposes commutation as a *relation between a left and a right action*, not as a property of one algebra, and his gauge group is a consequence of that relation. And the passage from commutant to double commutant is a Galois closure of the same shape as the invariance/automorphism connection, with the same failure of faithfulness at the bottom.

## The commutant is what the symmetry cannot see

For a set $S$ of operators, the commutant is

$$
S'=\{\,T : TS=ST\ \text{for all}\ S\in S\,\}.
$$

If $S=\rho(G)$ for a representation $\rho$ on $V$, then $T\in\rho(G)'$ is precisely a morphism of representations: applying $T$ before or after any symmetry gives the same result, so $T$ is a transformation of $V$ that is not a transformation of $\rho$. It is a difference in the carrier which no equivariant description registers.

Assume here that $V$ is a finite-dimensional real irreducible $G$-module. Schur's lemma says that every nonzero $T\in\operatorname{End}_G(V)$ has kernel and range $\{0\}$ or $V$, hence is invertible, so $\operatorname{End}_G(V)$ is a finite-dimensional real division algebra. Frobenius then says that it is exactly one of $\mathbb R$, $\mathbb C$, $\mathbb H$ (associativity is essential: the octonions are a non-associative real division algebra, and $\operatorname{End}_G(V)$ is associative by construction). Two boundaries follow in this declared setting, and both matter:

- the residue is **never trivial** — the scalars always commute with everything;
- the residue is **never large** — at most four real dimensions.

So the invisible part of a finite-dimensional real irreducible carrier is guaranteed to exist, guaranteed to be small, and comes in exactly three kinds. That census is the algebraic core of Dyson's threefold way; applying it to physical symmetry classes requires the additional Hilbert-space and antiunitary structure of that classification.

## Commuting is a relation; commutativity is that relation predicated of a thing and itself

$\mathbb H$ commutes with everything in an irreducible quaternionic representation, and $\mathbb H$ is not commutative. The two notions must be kept apart:

$$
\mathcal A\ \text{commutes with}\ \mathcal B
\iff
\mathcal A\subseteq\mathcal B' ,
\qquad
\mathcal A\ \text{is commutative}
\iff
\mathcal A\subseteq\mathcal A' ,
$$

and the centre is the place where they meet, $Z(\mathcal A)=\mathcal A\cap\mathcal A'$. Commutation is a two-place relation and requires a second term. Commutativity is the degenerate case in which the second term is the first. Frobenius' three allowed commutants include one noncommutative entry, so the inference *from* "commutes with everything" *to* "is commutative" fails in the quaternionic case — the same division-algebra block used for the weak interaction in the finite geometry.

## Double commutant as a Galois closure

The map $S\mapsto S'$ is antitone, and $S\subseteq S''$; von Neumann's theorem says that for a unital $*$-subalgebra of $\mathcal B(\mathcal H)$ the closure $\mathcal M''$ is the weak closure. So the commutant is one half of a Galois connection of a set with itself, and the double commutant is its closure operator.

This is the same shape as the connection between invariants and automorphisms recorded in [[philosophy/indiscernibility-of-identicals/symmetry-as-dual-of-discernment|the dual of discernment]]: two antitone maps, a closure that returns not the original object but its completion, and — decisively — a loss of faithfulness at the low end. There the loss is arity: at the grade of one-place properties the recovered group is only a product of symmetric groups on the blocks of a partition, so a symmetry carries more than a partition. Here the analogous loss is that a commutant records only the module structure, so an algebra is recovered only up to weak closure. Neither closure is a defect to be repaired; both say that "what cannot see it" is a coarser instrument than the thing itself.

The commutant is therefore the algebraic form of surplus structure, whose costs and benefits are audited in [[philosophy/indiscernibility-of-identicals/rigidity-and-surplus-structure|rigidity and surplus structure]] and not repeated here.

## One bit of sign turns three into ten

Grade the carrier, $V=V_0\oplus V_1$. "Commutes" is then read as *supercommutes*,

$$
ab=(-1)^{|a||b|}\,ba ,
$$

so two odd elements are permitted to anticommute. The super version of Schur's lemma makes the supercommutant of an irreducible super-representation a **super division algebra**: every nonzero *homogeneous* element is invertible. [[library/the-tenfold-way/inq|Wall]] classified these, and over $\mathbb R$ there are ten — the three purely even ones being $\mathbb R,\mathbb C,\mathbb H$, so that the threefold way sits inside the tenfold as the ungraded case, with seven further algebras generated by the single admissible sign.

This is the precise sense in which the tenfold way is a completeness theorem about differences that make no difference. Once a $\mathbb Z/2$-grading may intervene, the possible undetectable residues number exactly ten, and by Wall's second theorem these ten are the *graded* Morita classes of the real and complex Clifford algebras — graded essentially, since as ungraded algebras they collapse to far fewer classes — which is what makes them the same list as the eight KO-dimensions plus two, as in [[the-eightfold-in-the-sign-table]].

## Connes does not impose commutativity, and could not

The finite algebra

$$
\mathcal A_F=\mathbb C\oplus\mathbb H\oplus M_3(\mathbb C)
$$

is noncommutative on purpose. The entire programme is the refusal of the Gelfand identification of commutativity with space; a commutative $\mathcal A$ would return an ordinary manifold and no gauge content. What the axioms impose instead is the **order-zero condition**

$$
[a,b^0]=0,\qquad b^0:=Jb^*J^{-1},
$$

that is, $\mathcal A\subseteq(\mathcal A^0)'$: the left action and the $J$-transported right action commute *with each other*. This relation is exactly a bimodule structure on $\mathcal H$, and Connes says he takes it "as a guide" in constructing the finite geometry. The order-one condition $[[D,a],b^0]=0$ restricts $[D,a]$ the same way.

The gauge group then arises as the adjoint action

$$
\operatorname{Ad}(u)\,\xi=u\,\xi\,u^*,
$$

which is well defined only because the two actions commute. So the internal symmetry of the standard model is a consequence of an imposed commutation *relation*, not of any commutativity. The corrected form of the intuition is therefore twofold: the model does not use an algebra that commutes, it requires that an algebra and its opposite commute; and it assembles that algebra out of the pieces that are eligible to be commutants.

## The finite geometry is built by Schur, blockwise

Connes constructs $\mathcal M_F$ as the direct sum of all inequivalent irreducible **odd** bimodules over

$$
\mathcal A_{LR}=\mathbb C\oplus\mathbb H_L\oplus\mathbb H_R\oplus M_3(\mathbb C),
$$

where odd means $\operatorname{Ad}(s)=-1$ for $s=(1,-1,-1,1)$. Cutting by the minimal idempotents $e_\ell,e_L,e_R,e_q$ gives $\mathcal M=\sum e_j\mathcal M e_k$, and each block is a left module over one division algebra and a right module over another. Schur then determines it outright: $e_L\mathcal M e_\ell$ is $\mathbb H_L$-left and $\mathbb C$-right, hence a multiple of the unique two-dimensional irreducible $\pi_L$; $e_L\mathcal M e_q$ is a module over $\mathbb H_L\otimes_{\mathbb R}M_3(\mathbb C)\cong M_6(\mathbb C)$, hence a multiple of $\pi_L^3$. Summing and adjoining contragredients,

$$
\mathcal M_F=\left(\pi_L\oplus\pi_R\oplus\pi_R^3\oplus\pi_L^3\right)\oplus\left(\pi_L\oplus\pi_R\oplus\pi_R^3\oplus\pi_L^3\right)^0,
\qquad
\dim=2\,(2+2+6+6)=32 .
$$

Every step is Schur's lemma over a division algebra. And up to *ungraded* Morita equivalence — a different relation from the graded one just used — since $M_3(\mathbb C)\simeq\mathbb C$ while $\mathbb H$ is inequivalent to $\mathbb R$ over $\mathbb R$,

$$
\mathcal A_F\ \simeq_{\mathrm{Morita}}\ \mathbb C\oplus\mathbb H\oplus\mathbb C ,
$$

a direct sum of division algebras — a direct sum, that is, of the things that can be what commutes with everything. Whether any principle *generates* this algebra rather than testing it belongs to [[symmetry-groups-select/finite-algebra-filters|the finite-algebra filters]] and is not claimed here.

## The word does two jobs and they must not be merged

Commutativity appears in this programme in a second and unrelated role: a readout context is a commutative algebra, its characters are its facts by Gelfand duality, and *at once* names commutativity rather than any temporal notion — as [[philosophy/indiscernibility-of-identicals/why-there-is-difference|why there is difference]] and [[sufficient-reason/facticity-and-pointing|facticity and pointing]] have it. That is commutativity **as context**: what can be valued simultaneously.

The commutation at issue here is different in type. It is commutativity **as relation**: between an algebra and its opposite, constitutive of a bimodule, and productive of a gauge group. The first is intrinsic to one algebra and marks the classical; the second holds between two actions and is compatible with each being as noncommutative as one likes. Nature's observability follows the first. Nature's internal symmetry follows the second. They share a word and not a role.
