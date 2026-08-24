# Why There Is an Action

The axiom can be given a partial ground rather than merely posited. If weights attach to histories and multiply under concatenation in an abelian group, their logarithm is additive over concatenation; with a regularity condition that logarithm is an integral along the history, which is an action. This grounds the *form* of the principle in a composition law. It does not supply the Lagrangian, does not derive the composition law, and delivers a circle-valued functional rather than the real-valued $S$ the axiom posits.

## The composition argument

Histories concatenate. If $\gamma_1$ runs from $a$ to $b$ and $\gamma_2$ from $b$ to $c$, there is a history $\gamma_2\circ\gamma_1$ from $a$ to $c$. Suppose each history carries a weight $W(\gamma)$ in an **abelian** multiplicative group — the hypothesis matters, since for noncommuting values the concatenation law produces path-ordered exponentials and no additive functional — and require

$$
W(\gamma_2\circ\gamma_1)=W(\gamma_2)\,W(\gamma_1).
$$

Then $A:=\log W$ is additive over concatenation:

$$
A(\gamma_2\circ\gamma_1)=A(\gamma_2)+A(\gamma_1).
$$

An additive interval function need not be an integral — a singular measure or a crossing count is additive too — so the passage to a density is a second hypothesis, absolute continuity in the endpoints, after which Radon--Nikodym gives

$$
A(\gamma)=\int_\gamma\mathcal L .
$$

Adding $|W|=1$ makes $\mathcal L$ imaginary and yields

$$
\boxed{
W(\gamma)=e^{\,iS[\gamma]/\hbar},
\qquad
S=-i\hbar\log W .
}
$$

Unimodularity is a further postulate and not a consequence of unitarity, which constrains the evolution operator rather than the weight of an individual history: Euclidean weights $e^{-S_E}$ obey the same composition law without it. Nothing in the argument asserts that anything is minimized, and it never mentions stationarity.

## The action is circle-valued

On $U(1)$ the logarithm is multivalued, so additivity holds modulo $2\pi i$ and the reconstruction produces an $\mathbb R/2\pi\hbar\mathbb Z$-valued functional. Lifting it to a genuine $S:\mathcal H\to\mathbb R$ is an extra hypothesis, and the obstruction is not an artifact — it is the same ambiguity that makes theta angles, Wess--Zumino terms, and Dirac quantization meaningful, and it is why [[what-the-axiom-asserts]] records that the quantum weight is sensitive to the action only modulo $2\pi\hbar$.

## Stationarity as a shadow

Stationarity then arrives as an asymptotic statement rather than a postulate. When action differences among neighboring histories are large compared with $\hbar$, phases interfere destructively away from stationary histories, and a stationary-phase expansion is organized around those that remain; the construction and its qualifications belong to [[quantum-action]].

The consequence is an inversion in the order of grounding. Read from the classical side, $\delta S=0$ is the axiom and the quantum phase a later discovery. Read from the composition side, the composition law is the axiom, the action is its logarithm, and $\delta S=0$ is a limit theorem. Both readings agree on all the mathematics. They disagree about what is fundamental.

## What the argument grounds

| Grounded, given the hypotheses named above | Not grounded here |
|---|---|
| that the weight is exponential in an additive functional | the multiplicative composition law itself |
| that the functional is an integral of a local density | absolute continuity, and locality |
| that the density is imaginary, given $\vert W\vert=1$ | unimodularity |
| that stationary histories dominate a semiclassical limit | the specific Lagrangian, its field content, and its couplings |
| | the lift from a circle-valued to a real-valued action |

The composition law is the assumption that a history's weight factorizes through its segments, a strong locality-in-time condition that could fail. The Lagrangian is left entirely open: what selects it is symmetry together with field content, which is the business of [[philosophy/symmetry-principle/entry|the invariance axiom]] and, in the local sector, of [[symmetry-groups-select/entry|symmetry selection]].

## The shape of answer this project wants

The argument replaces a teleological-sounding principle with a structural one: not that nature optimizes, but that an arena in which histories compose multiplicatively carries an additive functional along them. That is the pattern [[cosmodynamics/entry|cosmodynamics]] asks for, and a candidate instance of the demand in [[sufficient-reason/entry|Sufficing and Necessitating Reason]] that a structure be shown necessary rather than exhibited. It remains a reconstruction: until the composition law, absolute continuity, and unimodularity are themselves grounded, the variational axiom has been moved rather than eliminated.
