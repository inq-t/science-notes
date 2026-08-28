---
inq.module: "conditioning"
inq.include:
  - "**/*.md"
---
# Conditioning, Instruments, and Postselection

Conditioning is an outcome-relative normalization, not an everywhere deterministic channel. In classical probability it restricts a law to an event of positive probability; in quantum theory an instrument first supplies completely positive trace-nonincreasing outcome operations, whose normalized branches are conditional states. Postselection keeps a declared set of those branches. These operations must remain distinct from nonselective channels, operator-algebraic conditional expectations, sufficient statistics, and dynamical decoupling.

## Classical conditioning

For a probability space \((\Omega,\mathcal F,p)\) and an event \(E\) with \(p(E)>0\), the conditional law is

$$
p(A\mid E)
:=\frac{p(A\cap E)}{p(E)}.
$$

The denominator is part of the operation. Conditioning is undefined when \(p(E)=0\) unless an additional regular-conditional-probability construction supplies a version on a richer measurable space. As a map of unnormalized measures, restriction \(p\mapsto p|_E\) is linear; the normalized update \(p\mapsto p(\cdot\mid E)\) is nonlinear because its denominator depends on the input law.

## Quantum instruments

In finite notation, a quantum instrument with outcome set \(X\) is a family of completely positive trace-nonincreasing maps

$$
\mathcal I_x:\mathcal T(\mathcal H)\longrightarrow\mathcal T(\mathcal H),
\qquad x\in X,
$$

such that the nonselective sum

$$
\Phi:=\sum_{x\in X}\mathcal I_x
$$

is trace preserving. For an input state \(\rho\), the probability and normalized conditional state of outcome \(x\) are

$$
p_x(\rho)
=\operatorname{Tr}\mathcal I_x(\rho),
\qquad
\rho_x
=\frac{\mathcal I_x(\rho)}{p_x(\rho)},
$$

when \(p_x(\rho)>0\). The branch operation \(\mathcal I_x\) is linear and trace-nonincreasing; the normalized state update \(\rho\mapsto\rho_x\) is nonlinear and outcome-relative. Forgetting the outcome label gives the deterministic channel \(\Phi\), not any one normalized branch.

For a measurable outcome space, the family is replaced by a countably additive instrument \(E\mapsto\mathcal I(E)\). The finite formula records the same typing without pretending to supply the measure-theoretic extension.

## Postselection

Postselection chooses a declared subset \(S\subseteq X\). Its success probability and conditional state are

$$
p_S(\rho)
=\operatorname{Tr}\sum_{x\in S}\mathcal I_x(\rho),
\qquad
\rho_S
=\frac{\sum_{x\in S}\mathcal I_x(\rho)}{p_S(\rho)}.
$$

It is therefore a branch choice plus normalization. Calling it a trace-preserving loss map suppresses both the success probability and the classical record specifying that selection succeeded.

For a projective measurement with projections \(P_x\), the Lüders instrument is the special case

$$
\mathcal I_x(\rho)=P_x\rho P_x.
$$

Writing \(P\rho P/\operatorname{Tr}(P\rho)\) does not by itself derive that instrument, its outcome, or its physical implementation; those are additional data.

## Four operations that are not interchangeable

1. A **nonselective channel** \(\Phi\) is completely positive and trace preserving. It averages all registered outcomes and need not be idempotent.
2. An **operator-algebraic conditional expectation** \(E:\mathcal M\to\mathcal N\) is normally a unital completely positive idempotent onto a subalgebra, with separate state-preservation and modular-invariance hypotheses. It is not a normalized outcome branch.
3. A **sufficient channel or statistic** preserves a declared family of distinctions in a precise recovery sense. Sufficiency is not postselection merely because both can reduce a carrier.
4. **Spectral gapping or dynamical decoupling** suppresses or removes a sector through dynamics or a limit. It is not conditioning unless an outcome instrument and normalization are constructed.

These operations can appear in one model, but their composition must be written rather than inferred from a shared projection symbol.

## Impact on the binary audit

[[a2-ternary-response/inq|The \(A_2\) ternary-response test]] contains a neutral third outcome. Compressing to the two oriented sheets and renormalizing is a postselected instrument only after its branch and success probability have been constructed. [[wall-construction-interface/binary-channel|The binary-channel obligation]] permits other routes, including a sufficient channel or controlled decoupling limit. Those routes need not produce the same state family, normalization, Fisher response, or ontology of what happened to the third sector.

The correct programme-level statement is therefore conditional:

$$
\boxed{
\text{ternary carrier}
+\text{constructed binary-reduction operation}
\Longrightarrow
\text{a candidate binary image}.}
$$

The algebraic presence of a two-sheet subspace does not select the operation.

## Failure conditions

A conditioning claim fails when the selected event has zero probability, the normalizing denominator is omitted, the outcome record is discarded while the branch is still treated as factual, or a nonlinear normalized branch is advertised as a linear trace-preserving channel. A proposed binary wall also fails if different admissible instruments return inequivalent binary families and no physical principle selects among them.

## Primary sources

- E. B. Davies and J. T. Lewis, “An Operational Approach to Quantum Probability,” *Communications in Mathematical Physics* **17** (1970), 239--260, [doi:10.1007/BF01647093](https://doi.org/10.1007/BF01647093). This paper introduces the instrument framework for outcomes, operations, and conditional probabilities.
- Gerhart Lüders, “Über die Zustandsänderung durch den Meßprozeß,” *Annalen der Physik* **443** (1950), 322--328, [doi:10.1002/andp.19504430510](https://doi.org/10.1002/andp.19504430510). This is the primary source for the projective state-update rule now bearing Lüders's name.
