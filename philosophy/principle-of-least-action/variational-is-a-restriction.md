# Variationality Is a Restriction

Not every dynamics comes from an action, so the axiom says something about the world rather than renaming its equations. The obstruction is exact and checkable — the Fréchet derivative of the equations must be self-adjoint — but it tests a *presentation* of the dynamics rather than the dynamics itself, since multiplying the equations by an invertible matrix can repair it. The restriction is consequently weaker than usually advertised, vacuous in one degree of freedom, and its standard illustration, the damped oscillator, is not an example at all.

## The inverse problem

Given a system of equations $E_i(t,q,\dot q,\ddot q)=0$, does there exist a Lagrangian whose Euler--Lagrange expressions are exactly the $E_i$? Writing $D_E$ for the Fréchet derivative of $E$ and $D_E^{*}$ for its formal adjoint, the answer is local and exact:

$$
\boxed{
E\ \text{is variational}
\iff
D_E=D_E^{*} .
}
$$

In coordinates this becomes the Helmholtz conditions, a finite set of identities among the partial derivatives of $E$. The simplest of them is already informative and is trivial to check:

$$
\frac{\partial E_i}{\partial\ddot q^{\,j}}
=\frac{\partial E_j}{\partial\ddot q^{\,i}} .
$$

A system whose acceleration coefficients form a non-symmetric matrix admits no Lagrangian *as written*. Self-adjointness gives a Lagrangian on a suitable star-shaped domain; global existence is a further question. These $E_i$ are the mechanical case of the field expressions written $E_a$ in [[philosophy/noether-conservation/what-the-synthesis-requires|the Noether synthesis]].

## The criterion tests the presentation, not the dynamics

Consider

$$
E_1=\ddot q^{\,1}+\ddot q^{\,2},
\qquad
E_2=\ddot q^{\,2}.
$$

Here $\partial E_1/\partial\ddot q^{\,2}=1$ while $\partial E_2/\partial\ddot q^{\,1}=0$, so the first Helmholtz condition fails and there is no Lagrangian for this pair of expressions. But $E_1-E_2=\ddot q^{\,1}$ and $E_2=\ddot q^{\,2}$ describe the same solutions and are the Euler--Lagrange expressions of a free particle. The dynamics was variational; the way it had been written was not.

The invariant question is therefore the harder one. Does there exist an invertible multiplier matrix $g_{ij}(t,q,\dot q)$ such that $g_{ij}E^j$ satisfies the conditions? This is the multiplier problem, and its status is uneven:

| Degrees of freedom | Status |
|---|---|
| $n=1$ | always locally solvable, after Darboux; the restriction is vacuous |
| $n=2$ | completely classified by Douglas in 1941; some systems admit no multiplier |
| $n\geq3$ | no complete classification |

So the axiom does exclude dynamics, but a claim that a particular system is non-variational requires the multiplier problem to be settled for it, and not merely the Helmholtz conditions to fail in the coordinates at hand.

## The damped oscillator is not an example

The usual illustration of non-variational dynamics is dissipation, and it does not work. The equation

$$
m\ddot x+\gamma m\dot x+\kappa x=0
$$

is the Euler--Lagrange equation of

$$
L=e^{\gamma t}\left(\tfrac12m\dot x^{\,2}-\tfrac12\kappa x^{\,2}\right),
$$

as one verifies directly: $\partial L/\partial\dot x=e^{\gamma t}m\dot x$, whose time derivative is $e^{\gamma t}(m\ddot x+\gamma m\dot x)$, while $\partial L/\partial x=-e^{\gamma t}\kappa x$. The exponential is precisely an integrating factor of the kind the multiplier problem allows.

What dissipation costs is visible in the same formula. Here $\partial L/\partial t=\gamma L$ is not a total derivative, so time translation is not even a divergence symmetry of this action, and there is no conserved energy to be had.

$$
\boxed{
\text{dissipation is the failure of a symmetry of the action, not the failure of variationality}.
}
$$

The point generalizes into the third module. Losing a conservation law does not require losing the action; it requires losing the corresponding symmetry of the action, and the two axioms can fail independently.

## What the restriction buys

Because variationality is a genuine restriction rather than a change of notation, asserting it is informative, and a theory that satisfies it has been constrained. Any proposed cosmodynamic law must therefore earn its action rather than assume one, since a dynamics with no variational presentation is a live possibility and not a pathology. The class the axiom admits is bounded by results known in low dimension and open in general, so "physics is variational" is at present a working commitment rather than a settled classification.
