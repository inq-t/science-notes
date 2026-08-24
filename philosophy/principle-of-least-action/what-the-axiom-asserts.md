# What the Variational Axiom Asserts

The axiom is a claim about the *type* of a dynamical law: the law is a stationarity condition on a real-valued functional of whole histories, not a rule for propagating a state. That the two agree is a theorem with hypotheses. The global form is also the less well-behaved of the two, since the boundary-value problem it poses can have no solution or many where the initial-value problem has exactly one, which bounds how fundamental the axiom can be taken to be.

## Two types of law

Let $\mathcal H$ be a set of admissible histories. The axiom supplies

$$
S:\mathcal H\longrightarrow\mathbb R,
\qquad
\text{physical histories}=\{\gamma\in\mathcal H:\delta S[\gamma]=0\},
$$

where $\delta S$ is the first variation over a declared class of variations. Compare the alternative type, in which a law is a rule for propagation:

$$
\dot x=X(x),
\qquad
x(t_0)=x_0 .
$$

The first selects from a space of completed histories; the second generates one. Nothing in the notion of a dynamical law prefers either, and the axiom is the assertion that the first is the right one. The programme-wide type declaration in [[program-core/ontological-registers|the register declaration]] carries *action* as a functional on histories or fields; the discipline it imposes applies here as elsewhere, and an explicit map is owed whenever one register is made to determine another.

## Localization is earned

That map exists under conditions. For a first-order Lagrangian, with fixed endpoints, sufficient differentiability, and the fundamental lemma of the calculus of variations, integration by parts converts $\delta S=0$ into the Euler--Lagrange equations, which are then local and second order; the derivation is in [[classical-action]]. A Lagrangian depending on higher jets gives equations of correspondingly higher order.

This is what dissolves the appearance that a history must know its own endpoint. The dissolution is a consequence of the theorem, not a feature of the axiom, and it fails exactly where the theorem's hypotheses do — with free boundary data, nonholonomic constraints, or variations not required to vanish at the ends.

## The global form is the weaker one

The equivalence is not a symmetry between two equally good formulations. For a regular Lagrangian the initial-value problem has a unique local solution, while the two-point problem that $\delta S=0$ actually poses may have none, one, or infinitely many stationary histories.

$$
\text{unique IVP solution}
\;\not\Longrightarrow\;
\text{unique stationary history between endpoints}.
$$

Conjugate points produce this, the harmonic oscillator over a half-period being the standard case. It is the same degeneracy that costs a stationary history its minimality in [[classical-action]], appearing there as a loss of minimality and here as a loss of uniqueness — two consequences of one mechanism, not one claim stated twice.

A principle that does not determine its object cannot by itself be the ground of determination. The defensible reading is that $\delta S=0$ *characterizes* the solution set and does not *produce* it: a condition satisfied by physical histories, locally equivalent to a production rule, and not a replacement for one.

## What the axiom does not assert

It does not assert that the stationary history is least, unique, or stable.

It does not fix $S$; the non-uniqueness is catalogued under equivalent Lagrangians in [[classical-action]]. What matters at this level is the asymmetry it produces. Classical dynamics sees the action only through the location of its stationary points, while the quantum weight $e^{iS/\hbar}$ is sensitive to normalization and to boundary terms modulo $2\pi\hbar$ — so the classical axiom underdetermines an object that the quantum theory partly fixes. That asymmetry is the subject of [[why-an-action-at-all]].

It does not assert that all dynamics is variational. That is a substantive further claim, and its exact obstruction is [[variational-is-a-restriction]].

## Off shell and on shell

The distinction the third module will need is already visible. $S$ is defined on all of $\mathcal H$, so any property of $S$ — invariance in particular — holds off shell, of histories that solve nothing. Conservation is asserted along solutions and holds on shell. Noether's construction is a transfer from the first to the second, which is why an off-shell invariance is the hypothesis and an on-shell conservation the conclusion.
