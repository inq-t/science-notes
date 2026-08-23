# Sufficing and Necessitating Reason

A necessitating reason determines which fact obtains, while a sufficing reason determines a coherent probability law without determining an outcome. The proposed distinction is modeled by the difference between a character of a commutative readout algebra and a state restricted to that algebra. Established results constrain attempts to reduce the second kind of ground to the first, but they do not yet explain outcome actuality, select the readout context, or derive a shared arrow of time.

## The distinction

Let $\mathcal M$ be a unital C\*-algebra or von Neumann algebra of pre-observables, let $\mathcal D\subseteq\mathcal M$ be a unital commutative readout context, and let $\omega$ be a state on $\mathcal M$. By Gelfand duality,

$$
\mathcal D\cong C(X_{\mathcal D}),
\qquad
X_{\mathcal D}=\operatorname{Spec}(\mathcal D).
$$

A point $x\in X_{\mathcal D}$ is equivalently a character $\chi_x:\mathcal D\to\mathbb C$. The restricted state $\omega|_{\mathcal D}$ is instead represented by a probability measure $\mu_{\omega,\mathcal D}$ satisfying

$$
\omega(d)=\int_{X_{\mathcal D}}\chi(d)\,\mathrm d\mu_{\omega,\mathcal D}(\chi),
\qquad d\in\mathcal D.
$$

The two reasons terminate in different objects:

$$
\begin{aligned}
\text{necessitating reason}&\longrightarrow \chi\in X_{\mathcal D},\\
\text{sufficing reason}&\longrightarrow \mu\in\operatorname{Prob}(X_{\mathcal D}).
\end{aligned}
$$

The measure determines the probabilities of possible readouts. It does not, merely by being a measure, determine a point in its support. Calling it sufficient *that* a fact occurs is therefore the philosophical proposal; the displayed mathematics supplies the measure but not the actuality of an outcome.

## Argument

[[facticity-and-pointing]] identifies a contextual fact with a multiplicative functional and separates multiplicativity from purity, extremality, and mere non-emptiness. [[two-species-of-reason]] then uses Gleason, Bell, and Kochen--Specker to state exactly how far a probability assignment can and cannot be replaced by predetermined values.

[[algebra-and-coalgebra]] proposes initial algebra and final coalgebra as formalisms for construction and observation. This is a research-level representation of the distinction, not a consequence of Gelfand duality or the quantum no-go theorems.

[[algebraic-arrow-of-time]] isolates the stronger claim about temporality. A many-to-one observational restriction is not yet a time evolution; an algebraic arrow requires a one-sided endomorphism semigroup or comparable structure. [[algebraic-and-statistical-arrows]] explains why that proposal is meant to differ from a Boltzmannian arrow and what the absence of a trace does and does not establish.

[[necessity-and-nonemptiness]] asks whether the availability of commutative contexts makes facts necessary. It proves the availability of characters but separates this from the realization of a normal, physically obtainable outcome. [[quantum-interpretations]] applies the distinction to measurement without pretending that a change of mathematical description is already a collapse mechanism.

## Status of the claims

| Status | Content |
|---|---|
| Established mathematics | Gelfand duality; character and state representation for commutative C\*-algebras; Gleason, Bell, and Kochen--Specker under their hypotheses; initial/final fixed-point theorems; MASA existence; modular and half-sided modular theory |
| Proposed interpretation | These results disclose two irreducible species of ground; a fact is contextual pointing; objective succession should be represented by one-sided algebraic action |
| Open construction | A behavior functor for quantum readout, an operational bisimulation theorem, a bridge to a physical endomorphism semigroup, coherent orientation across observers, and an account of realizable outcomes |

The open obligations and their failure conditions are stated in [[theorem-programme]]. [[sources]] records the principal mathematical sources by dependency.
