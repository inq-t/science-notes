# Horizontal perturbation geometry and the open spacetime lift

The homogeneous source is closed by the scale-capacity law. A complete physical theory must also determine inhomogeneous perturbations. This section records what is fixed by the binary state geometry and what remains open.

## Canonical Witten--Darboux pair

The binary information potential is

$$
\Psi(\theta)=\ln(2\cosh\theta),
$$

with

$$
\eta(\theta)=\Psi'(\theta)=\tanh\theta,
\qquad
\eta'(\theta)=\sech^2\theta.
$$

Define first-order operators

$$
\mathcal A=\partial_\theta+\eta,
\qquad
\mathcal A^\dagger=-\partial_\theta+\eta.
$$

Their partner Hamiltonians are

$$
\mathcal H_-:=\mathcal A^\dagger\mathcal A
=-\partial_\theta^2+\eta^2-\eta',
$$

$$
\mathcal H_+:=\mathcal A\mathcal A^\dagger
=-\partial_\theta^2+\eta^2+\eta'.
$$

Using $\eta^2+\eta'=1$ gives the exact factorization

$$
\boxed{
\mathcal H_-=-\partial_\theta^2+1-2\sech^2\theta,
}
$$

$$
\boxed{
\mathcal H_+=-\partial_\theta^2+1.
}
$$

Equivalently, define the two-component Dirac/Witten operator

$$
\boxed{
\mathcal D_\Psi=
\begin{pmatrix}
0&\mathcal A^\dagger\\
\mathcal A&0
\end{pmatrix},
\qquad
\mathcal D_\Psi^2=
\begin{pmatrix}
\mathcal H_-&0\\
0&\mathcal H_+
\end{pmatrix}.
}
$$

This pair is not an independently guessed Pöschl--Teller ansatz. It is generated canonically by the binary log-partition potential; reflectionless $\sech^2$ operators are a standard exactly solvable class ([33]).

## Bound mode, BKM density, and transparency

The zero-mode equation

$$
\mathcal A\psi_0=0
$$

has normalized solution

$$
\boxed{
\psi_0(\theta)=\frac1{\sqrt2}\sech\theta.
}
$$

Therefore

$$
\boxed{
2|\psi_0|^2=\sech^2\theta=G^{\BKM}_{\theta\theta}.
}
$$

The same function is simultaneously:

- the BKM/Fisher metric density;
- the normalized dark-history shape;
- the density of the unique bound mode of the Witten pair.

For continuum energy $1+k^2$, applying $\mathcal A^\dagger$ to a free wave gives

$$
\psi_k(\theta)=(-ik+\tanh\theta)e^{ik\theta}.
$$

At both asymptotic ends there is no $e^{-ik\theta}$ component, so

$$
\boxed{R(k)=0.}
$$

The continuum is transmitted with a phase shift; it is not absent. The correct statement is one normalizable bound mode plus a reflectionless continuum.

The Witten index is one, matching the unit topological charge of the Fisher kink. The total Fisher length is $\pi$, and the one-bound-state Levinson phase is also $\pi$; these are consequences of the same factorization rather than independent evidence.

## What this pair does and does not prove

The Witten pair closes the **internal horizontal operator geometry**. It explains why the fundamental pair is $\ell=1$, why there is one localized mode, and why the continuum is reflectionless.

It does not yet identify these operators with the physical scalar, vector, or tensor perturbation operators of an FLRW spacetime. A spacetime perturbation theory must specify:

- how inhomogeneous deformations of causal cuts induce horizontal state tangents;
- how the two-component Witten complex is embedded in spacetime constraints;
- how spatial gradients and causal propagation enter;
- which observable combination couples to matter and metric perturbations;
- whether the resulting system is ghost-free, hyperbolic, and regular at the crossing.

Thus the pair completion is canonical, but the spacetime lift remains open.

## Negative result: ordinary matter growth is not the pair operator

The standard smooth-dark-response matter-growth equation can be reduced to a Schrödinger-like zero-energy equation, but its effective potential contains ordinary matter and Hubble-friction terms. It is not proportional to $\rho_X$ and is not the Pöschl--Teller operator above.

Therefore transparency must not be imposed on the ordinary matter-growth equation. The Witten pair belongs to the internal horizontal response sector, not to a rebranding of standard growth.

## Negative result: canonical single-field completion

For a canonical single scalar, the kinetic normalization is proportional to $1+w_X$. In the rigid history,

$$
1+w_X=\frac23\tanh\theta,
$$

which is negative throughout the entire pre-crossing branch. At the crossing, the corresponding single-field mode function behaves as

$$
z\sim|\theta|^{1/2},
$$

so

$$
\frac{z''}{z}\sim-\frac1{4\theta^2},
$$

at the critical inverse-square coupling. The horizontal state coordinate therefore cannot be interpreted as an ordinary canonical local scalar field.

This is not a defect of the homogeneous free-energy construction. It says that the physical completion must be collective, constrained, multi-component, algebraic, or otherwise noncanonical.

## Perturbative stopping condition

A perturbative completion is adequate when it derives, without arbitrary functions,

1. a conserved $\delta T^X_{ab}$;
2. a regular crossing;
3. a finite number of propagating or constrained modes fixed by the Witten pair;
4. a definite gradient structure and sound/cone speed;
5. CMB, lensing, and growth responses that can be calculated in a Boltzmann code.

Until then, the background equations are closed but the theory is not a complete cosmological perturbation theory.
