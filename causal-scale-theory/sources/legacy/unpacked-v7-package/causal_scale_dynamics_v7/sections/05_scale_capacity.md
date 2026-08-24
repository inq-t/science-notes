# The Scale--Capacity Equivalence Principle

The previous versions contained two numbers:

$$
\vperp=\frac{\dd\theta}{\dd N}
$$

for the horizontal conversion rate and

$$
\chi_\perp
$$

for the conversion from BKM susceptibility to energy density. Background data partly degenerate them. The present closure replaces the arbitrary stiffness by an invariant relation among the state metric, horizon entropy, modular temperature, and causal volume.

## Capacity and the physical BKM norm

The normalized binary metric

$$
\sech^2\theta
$$

fixes shape but is not the extensive capacity of the whole causal wall. Write

$$
G^{\perp}_{NN}(N)
=C_{\perp,c}\vperp^2\sech^2[\vperp(N-N_c)],
$$

where

$$
C_{\perp,c}=G^{\perp}_{\theta\theta}(0)
$$

is the physical BKM capacity carried by the selected horizontal mode.

The entanglement capacity of a state is

$$
C_E=\operatorname{Var}(K).
$$

It is not equal to entropy for arbitrary states. In controlled holographic CFTs with an ordinary Einstein-gravity dual and the preferred gravitational regularization, spherical regions satisfy ([26])

$$
C_E=S_{EE}/k_B.
$$

Higher-derivative gravity and generic quantum states can change the ratio. The equality therefore characterizes an Einstein-capacity universality class rather than a tautology.

## The invariant Ruble number

Define

$$
\boxed{
\Ruble
:=\frac{k_B}{S_c}G^{\perp}_{NN}(N_c)
=\frac{k_BC_{\perp,c}}{S_c}\vperp^2.
}
$$

This combination is invariant under rescaling the coordinate $\theta$: the BKM metric and coordinate slope transform oppositely. It is the entropy-normalized squared speed of the horizontal state under one Weyl e-fold.

The fundamental law is

$$
\boxed{\Ruble=1.}
$$

Equivalently,

$$
\boxed{
\left.
\Phi^*\left(\frac{k_B}{S_c}G^{\perp}_{\BKM}\right)
\right|_{N_c}
=\dd N^2.
}
$$

This is the stopping principle of the homogeneous theory. It is analogous in logical status to an equivalence principle or a universal conversion law: it is not derived from a more primitive metric convention, and it is directly falsifiable.

Under the fundamental normal representation, $\vperp=1$, the same law implies

$$
C_{\perp,c}=S_c/k_B.
$$

Conversely, if the selected wall mode saturates the Einstein capacity, the unit Ruble number fixes $\vperp=1$.

## Relative entropy as modular free-energy curvature

Let $\omega_c$ be the self-dual KMS reference state and $\mathcal H_c=k_BT_cK_c$ its physical modular Hamiltonian. Nonequilibrium free energy obeys the exact identity

$$
F_c(\rho)-F_c(\omega_c)
=k_BT_cS(\rho\|\omega_c).
$$

For a neighboring scale state,

$$
S(\omega_{c+\delta N}\|\omega_c)
=\frac12G^{\perp}_{NN}(N_c)\delta N^2+O(\delta N^3).
$$

Therefore the quadratic free-energy curvature is

$$
\lim_{\delta N\to0}
\frac{F_c(\omega_{c+\delta N})-F_c(\omega_c)}{\delta N^2}
=\frac{k_BT_c}{2}G^{\perp}_{NN}(N_c).
$$

The homogeneous source law is defined by distributing that collective modular free energy over the causal-wall volume:

$$
\boxed{
\rho_X(N)=\frac{k_BT_c}{2V_c}G^{\perp}_{NN}(N).
}
$$

This is not a canonical local scalar kinetic term. $\theta$ is a collective state coordinate, and the energy is the free-energy curvature of the state family. The single-field ghost no-go therefore does not invalidate the homogeneous construction.

## Hawking--Friedmann conversion

For a flat FLRW apparent horizon in four spacetime dimensions,

$$
R_c=\frac{c}{H_c},
\qquad
A_c=4\pi R_c^2,
\qquad
V_c=\frac{4\pi}{3}R_c^3.
$$

Use the Bekenstein--Hawking entropy

$$
\frac{S_c}{k_B}=\frac{A_cc^3}{4G\hbar}
=\frac{\pi R_c^2c^3}{G\hbar}
$$

and the canonically normalized horizontal causal-diamond temperature

$$
k_BT_c=\frac{\hbar c}{2\pi R_c}.
$$

Then

$$
\boxed{
k_BT_c\frac{S_c}{k_B}=\frac{c^4R_c}{2G}=E_{\rm MS,c}.}
$$

The flat Friedmann relation gives

$$
E_{\rm MS,c}=\rho_{\rm crit,c}V_c.
$$

Thus

$$
\boxed{
\frac{k_BT_c}{V_c}\frac{S_c}{k_B}=\rho_{\rm crit,c}.
}
$$

This is the dimensional bridge. The BKM metric supplies dimensionless response; horizon temperature supplies energy per information unit; the causal volume supplies density; Friedmann marginality identifies the result with the critical density.

![The homogeneous amplitude closes by composing binary BKM geometry, modular free energy, and horizon thermodynamics.](figures/scale_capacity_closure.pdf){width=96%}

## Closed amplitude

Using

$$
G^{\perp}_{NN}(N)
=\Ruble\frac{S_c}{k_B}\sech^2(N-N_c),
$$

the source becomes

$$
\boxed{
\rho_X(N)=\frac{\Ruble}{2}\rho_{\rm crit,c}\sech^2(N-N_c).
}
$$

For the fundamental value $\Ruble=1$,

$$
\boxed{
\rho_X(N)=\frac12\rho_{\rm crit,c}\sech^2(N-N_c).
}
$$

At the crossing,

$$
\Omega_{X,c}=\frac12.
$$

Spatial flatness implies

$$
\rho_{\rm ordinary,c}=\rho_{\rm crit,c}-\rho_{X,c}=\frac12\rho_{\rm crit,c},
$$

and hence

$$
\boxed{
\rho_X(N_c)=\rho_{\rm ordinary}(N_c).
}
$$

The former postulate $r_c=1$ is thereby derived from the scale-capacity law. The exact equality includes radiation and any other non-dark contribution.

## General spatial dimension

Let $d$ be the number of spatial dimensions. The apparent-horizon area and volume scale as

$$
A=\Omega_{d-1}R^{d-1},
\qquad
V=\frac{\Omega_{d-1}}{d}R^d.
$$

Einstein-Friedmann geometry gives

$$
\frac{k_BT_c(S_c/k_B)}{V_c}
=\frac{2}{d-1}\rho_{\rm crit,c}.
$$

Therefore

$$
\boxed{
\Omega_{X,c}=\frac{\Ruble}{d-1},
}
$$

and

$$
\boxed{
\frac{\rho_{X,c}}{\rho_{\rm ordinary,c}}
=\frac{\Ruble}{d-1-\Ruble}.
}
$$

For $\Ruble=1$,

$$
\frac{\rho_{X,c}}{\rho_{\rm ordinary,c}}=\frac1{d-2}.
$$

Equal ordinary and response densities occur in three spatial dimensions:

$$
\boxed{
\Ruble=1,
\quad
\rho_X=\rho_{\rm ordinary}
\quad\Longleftrightarrow\quad
d=3.
}
$$

This does not independently prove that space must have three dimensions. It shows that the unit scale-capacity law and equal self-dual partition are mutually compatible precisely in the observed dimension.

![The dimension dependence of the self-dual crossing.](figures/dimension_crossing_ratio.pdf){width=78%}

## Status of the closure

The closure contains one physical law:

$$
\boxed{
\left.
\frac{k_B}{S_c}G^{\perp}_{NN}
\right|_{N_c}=1.
}
$$

The supporting evidence is:

- capacity equals entropy in controlled spherical Einstein-holographic settings ([26]);
- modular-Hamiltonian variance equal to horizon entropy has been proposed for flat, de Sitter, and suitable holographic causal diamonds ([27,28]);
- the BKM Hessian equals gravitational canonical energy in controlled holographic perturbation theory ([12]);
- apparent-horizon thermodynamics gives the exact Hawking--Friedmann dimensional conversion ([24,25]).

The law has not been proved for a dynamical FLRW causal wall. It is the theory's equivalence principle and its most direct target for independent derivation or falsification.
