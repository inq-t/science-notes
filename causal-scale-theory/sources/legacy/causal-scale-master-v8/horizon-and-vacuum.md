# Horizon Clock and Vacuum Split

The horizon identities are strongest when their signs, temperatures, and logical roles remain separate. The same discipline is essential in the vacuum discussion: local state geometry and the trace-free gravitational channel are exactly blind to central shifts, but a global scalar mode and radiative stability remain to be supplied by an independent completion.

## Signed horizon index

For a spatially flat expanding FLRW apparent horizon,

$$
R_A=\frac{c}{H},
$$

and the Hayward surface gravity can be written

$$
\kappa_A
=-\frac{c^2}{R_A}\frac{1-q}{2}.
$$

Define the signed index

$$
\widehat\mu_A:=\frac{1-q}{2},
$$

and the nonnegative surface-gravity magnitude

$$
\mu_A:=\frac{|\kappa_A|R_A}{c^2}
=|\widehat\mu_A|.
$$

In the tractor convention used by the programme,

$$
\widehat\mu_A=-\frac{I^2}{H^2}.
$$

The signed formula $\mu_A=(1-q)/2$ is valid only on the branch $q\le1$. Outside it, replacing $\widehat\mu_A$ by the magnitude changes differential identities.

Since $\mathcal S_A\propto R_A^2\propto H^{-2}$,

$$
\frac{\mathrm d\ln\mathcal S_A}{\mathrm dN}
=2(1+q)
=4(1-\widehat\mu_A).
$$

If a signed vertical rapidity is defined by

$$
\frac{\mathrm d\widehat\eta_A}{\mathrm dN}
=\widehat\mu_A,
$$

then the identity

$$
\boxed{
\mathrm dN
=\mathrm d\widehat\eta_A
+\frac14\mathrm d\ln\mathcal S_A
}
$$

splits one scale e-fold into signed surface-gravity rapidity and horizon-entropy growth. It is a geometric allocation formula. It does not identify the horizontal state coordinate $\theta$ with $\widehat\eta_A$.

## Two temperatures that should not be conflated

The horizontal normalization used in the source law is

$$
k_BT_{\rm hor}:=\frac{\hbar c}{2\pi R_A}.
$$

The positive Kodama–Hayward temperature is instead

$$
k_BT_{\rm KH}
=\frac{\hbar|\kappa_A|}{2\pi c}
=\mu_A\frac{\hbar c}{2\pi R_A}
=\mu_A k_BT_{\rm hor}.
$$

At a generic dynamical FLRW horizon they differ. The Hawking–Friedmann product

$$
k_BT_{\rm hor}\frac{S_A}{k_B}
=\rho_{\rm crit}V_A
$$

is exact algebra after $T_{\rm hor}$, the area entropy, and the flat-horizon volume are stipulated. Why the **horizontal** modular deformation should use $T_{\rm hor}$ rather than $T_{\rm KH}$ is an **[IDENTIFICATION — HORIZONTAL TEMPERATURE] [OPEN]** question. The vertical surface-gravity clock and horizontal state-space speed occupy different slots.

The derivations and their source trail are retained in [[horizon-clock|horizon clock allocation]] and [[hawking-friedmann|the Hawking–Friedmann conversion]].

## Exact local vacuum blindness

For an ordinary normalized Gibbs state,

$$
\rho(H+C\mathbf1)
=\frac{e^{-\beta(H+C\mathbf1)}}{\operatorname{tr}e^{-\beta(H+C\mathbf1)}}
=\rho(H).
$$

Similarly,

$$
\operatorname{Var}(K+\alpha\mathbf1)
=\operatorname{Var}(K),
$$

and relative entropy or any monotone information metric is insensitive to a common central normalization shift. In the gravitational trace-free channel,

$$
(T_{ab}+\lambda g_{ab})^\circ=T^\circ_{ab}.
$$

**[ALGEBRA]** The chosen local information metric and the trace-free scale-transport equation are both blind to additive central offsets. This parallel is real and conceptually important: local distinguishability measures response to state differences, while a uniform central offset carries no local distinguishability in that channel.

For local QFT algebras, the finite-dimensional density-matrix display is only an analogy. The precise formulation must use Araki relative entropy and a specified comparison on the relevant type-III algebra or crossed product.

## What local blindness does not establish

A constant shift of a Hamiltonian on a fixed background is not the same operation as varying a gravitational effective action. The term

$$
\Gamma_\Lambda[g]
=-\int\mathrm d^4x\sqrt{-g}\,\Lambda
$$

has nonzero metric variation and therefore gravitates in the ordinary Einstein equation. Quantum loops also generate curvature counterterms such as

$$
\int\sqrt{-g}\,R,
\qquad
\int\sqrt{-g}\,R^2,
\qquad
\int\sqrt{-g}\,R_{ab}R^{ab},
$$

not merely a central constant.

Trace-free gravity moves a metric-proportional source out of the local trace-free equation, but the Bianchi identity restores a scalar integration datum. It does not determine that datum and does not by itself make it radiatively stable.

The rigorous present conclusion is therefore narrow:

> **[ALGEBRA]** The proposed local dark-response channel does not measure a common central offset.

It is not yet legitimate to conclude that vacuum energy never gravitates, that the cosmological-constant problem is solved, or that the small observed curvature has been derived.

## Global residual sectors

Let $\Lambda_{\rm res}$ be the curvature-valued scalar remainder surviving renormalization and the chosen global completion. It may be a completion-dependent combination of the bare tractor lift $\Lambda_g$, vacuum counterterms, and an integration or flux constant. Its constant Einstein-frame energy density is

$$
\rho_{\rm res}=\frac{c^4}{8\pi G}\Lambda_{\rm res}.
$$

Distinct sectors have distinct futures:

- **[SECTOR] $\Lambda_{\rm res}=0$:** the unit-width response decays as $a^{-2}$ and the future coasts;
- **[SECTOR] $\Lambda_{\rm res}>0$:** the residual eventually dominates and restores de Sitter expansion;
- **[SECTOR] $\Lambda_{\rm res}<0$:** recollapse or another global transition may occur, depending on the full matter history;
- **[CONJECTURE — FLUCTUATING RESIDUAL]:** a stochastic or volume-suppressed scalar remainder would define a different theory and different late-time statistics.

The background module selects the first branch. No local modular or tractor identity selects it.

## A plausible complementary completion

**[CONJECTURAL ROUTE — central quotient plus global constraint]** Treat the local response theory as living on observables modulo central shifts, while a separate top-form, flux, unimodular, or sequestering-like sector determines the scalar lift by a global constraint.

This division of labor is structurally attractive:

$$
\text{local noncentral response}
\quad\oplus\quad
\text{global scalar calibration}.
$$

It mirrors the tractor trace split and avoids asking a local information metric to solve a global constraint problem. But it becomes a completion only if one writes a consistent action or algebraic dynamics, derives the global constraint, checks diffeomorphism invariance and conservation, includes graviton and matter loops, and shows why the selected residual is stable.

**Upgrade condition:** derive $\Lambda_{\rm res}$ from the global equations and show its radiative behavior.

**Failure condition:** if the completed theory simply reintroduces an arbitrary radiatively sensitive integration constant, the conceptual split has reorganized the problem without solving it.

The bold but defensible claim is that the cosmological-constant problem may have been assigned to the wrong register. The framework has not yet shown that the correct register determines the answer.
