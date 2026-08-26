# The Half-Sided Modular Orientation Gate

Half-sided modular inclusions provide a rigorous way for a reversible ambient modular group to determine a one-sided accessible semigroup. They are therefore an excellent candidate skeleton for causal-wall orientation, but nesting alone does not establish the required inclusion, and the theorem neither constructs cosmic time nor automatically supplies a conditional expectation or operator-valued weight.

## Exact mathematical input

In the weight form of the general half-sided modular inclusion theorem, let $M\subset B(\mathcal H)$ be in standard form with respect to a normal faithful semifinite weight $\varphi$. Let $N\subset M$, require $\psi=\varphi|_N$ to be semifinite, and require $N$ to be in standard form with respect to $\psi$. Fix the convention

$$
\Delta_M^{it}N\Delta_M^{-it}\subseteq N
\qquad(t\le 0).
$$

Araki and Zsidó then obtain a positive self-adjoint generator $P$ and a unitary group $U(s)=e^{isP}$ such that $U(s)MU(s)^*\subseteq M$ for $s\ge0$; hence $\operatorname{Ad}U(s)$ on that half-line is an endomorphism semigroup. Reversing the modular half-side reverses the semibounded generator sign unless the translation parameter is reoriented at the same time. The modular groups and $U$ also generate the corresponding affine-group representation. Thus the ambient unitary group remains invertible while the accessible action is preserved only on one half-line.

This is **[STANDARD]**. [[library/extension-of-borchers-structure-theorem|Araki--Zsidó]] is the article-level source owner and points to the already checksum-verified local PDF and source payload.

## What a wall family must prove

A totally ordered family of wall algebras is not *therefore* a chain of half-sided modular inclusions. A wall realization must first provide the theorem inputs:

1. the algebras and their common representation or compatible standard forms;
2. the common cyclic-separating vector or appropriate weight data;
3. the inclusions and the sign of half-sided modular containment;
4. the standard-form hypotheses of the selected theorem, including semifiniteness of the restricted weight; if “standard HSMI” is instead used in the Wiesbrock subfactor sense, its additional relative-commutant cyclicity condition.

It must then prove that the reconstructed outputs fit the wall family:

1. the positive generators have a consistent orientation and nontrivial action;
2. the affine-group representations and inclusions compose coherently along the chain; and
3. the preserved subalgebras have the declared physical meaning.

This is a proposed **[OPEN CONSTRUCTION]** for a dedicated future `wall-construction-interface/half-sided-modular-orientation.md` owner, which [[wall-construction-interface/construction-ladder|the Wall Construction Ladder]] should reference. If it succeeds, it gives an exact algebraic orientation. It does not yet identify that orientation with scale age, proper time, entropy increase, fact formation, or record persistence.

## A separate operator-valued-weight gate

Half-sided invariance is one-sided. The modular compatibility used in standard conditional-expectation and operator-valued-weight criteria is stronger and generally concerns compatible modular action for all $t\in\mathbb R$, together with the relevant semifiniteness hypotheses.

The work should therefore be split:

- **HSMI target:** construct a half-sided modular wall satisfying a declared theorem, its unitary one-parameter group with semibounded generator, and the induced half-line endomorphism semigroup;
- **expectation target:** independently determine whether a normal faithful conditional expectation or a normal faithful semifinite operator-valued weight $T:M_+\to\widehat N_+$ exists and composes along the wall family.

The second target belongs with [[spectral-wall-descent/conditional-expectation-balance|Conditional-Expectation Balance]]. [[library/operator-valued-weights-without-structure-theory|Falcone--Takesaki]] gives the exact modular-compatibility criterion relevant to the operator-valued-weight question. Success of the first target does not discharge it.

Failure of one chosen vacuum modular flow to preserve $N$ rules out an expectation preserving that chosen vacuum under the standard criterion. It does not by itself prove that no operator-valued weight exists for any compatible pair of weights. A genuine nonexistence claim must quantify over the relevant weight data and invoke the corresponding theorem.

## Physical boundary

The theorem shows how a group at an ambient register can present as a semigroup on a subalgebra. That is philosophically important: irreversibility need not mean that the whole mathematical structure is being destroyed. But an objective history additionally needs the record functor and persistence conditions of [[algebra/local-global-individuation|Local--Global Individuation]].
