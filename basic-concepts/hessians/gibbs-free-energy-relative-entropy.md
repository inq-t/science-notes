# Gibbs-State Free Energy and Relative Entropy

For one fixed Hamiltonian and one fixed positive temperature, the nonequilibrium free-energy excess above the Gibbs state is exactly temperature times relative entropy. Its second variation at the Gibbs state is therefore the Bogoliubov--Kubo--Mori metric, but this is a coincidence statement: it does not identify a finite-history free-energy profile with a local Hessian along that history.

## The fixed-data identity

Let \(\mathcal H\) be a finite-dimensional Hilbert space, let \(H=H^*\) be a fixed Hamiltonian, and fix \(T>0\). Set

$$
\beta:=\frac{1}{k_BT},
\qquad
Z:=\operatorname{Tr}(e^{-\beta H}),
\qquad
\gamma:=\frac{e^{-\beta H}}{Z}.
$$

The Gibbs state \(\gamma\) is faithful. For a density operator \(\rho\), use the dimensionless von Neumann entropy

$$
s_{\mathrm{vN}}(\rho)
:=-\operatorname{Tr}(\rho\ln\rho)
$$

and define the fixed-\((H,T)\) free-energy functional

$$
\mathcal F_{H,T}(\rho)
:=\operatorname{Tr}(\rho H)
-k_BT\,s_{\mathrm{vN}}(\rho).
$$

Then

$$
\boxed{
\mathcal F_{H,T}(\rho)-\mathcal F_{H,T}(\gamma)
=k_BT\,D(\rho\Vert\gamma).}
$$

This is an exact identity, not a quadratic approximation. Indeed,

$$
\ln\gamma=-\beta H-(\ln Z)\mathbf 1,
$$

so

$$
\begin{aligned}
k_BT\,D(\rho\Vert\gamma)
&=k_BT\operatorname{Tr}\!\left[\rho(\ln\rho-\ln\gamma)\right]\\
&=\operatorname{Tr}(\rho H)
-k_BT\,s_{\mathrm{vN}}(\rho)
+k_BT\ln Z.
\end{aligned}
$$

Since

$$
\mathcal F_{H,T}(\gamma)=-k_BT\ln Z,
$$

the result follows. Positivity of relative entropy also shows that \(\gamma\) is the unique minimizer of \(\mathcal F_{H,T}\).

Here *Gibbs* names the equilibrium reference state. The functional is also commonly called the nonequilibrium Helmholtz free energy; it should not be confused with a thermodynamic Gibbs potential obtained by Legendre transforming with respect to pressure.

## The second variation

Let \(t\mapsto\rho_t\) be a \(C^2\) curve of faithful density operators with

$$
\rho_0=\gamma,
\qquad
X:=\dot\rho_0=X^*,
\qquad
\operatorname{Tr}X=0.
$$

Define the Kubo--Mori operator

$$
\Omega_\gamma(A)
:=\int_0^1\gamma^sA\gamma^{1-s}\,\mathrm ds.
$$

On self-adjoint trace-zero density tangents, the dual BKM form is

$$
g^{\mathrm{BKM}}_\gamma(X,Y)
:=\operatorname{Tr}\!\left[
X\,\Omega_\gamma^{-1}(Y)
\right].
$$

Faithfulness makes \(\Omega_\gamma\) invertible in finite dimensions. The generic coincidence theorem is developed in [[basic-concepts/hessians/entry#Log-partition Hessians and Fisher geometry|the Hessian account of BKM geometry]]. Applying it to the exact fixed-data identity gives

$$
\boxed{
\left.\frac{\mathrm d^2}{\mathrm dt^2}
\mathcal F_{H,T}(\rho_t)\right|_{t=0}
=k_BT\,g^{\mathrm{BKM}}_\gamma(X,X).}
$$

The first derivative vanishes because \(\gamma\) is the constrained minimum on the affine space \(\operatorname{Tr}\rho=1\). Consequently,

$$
\mathcal F_{H,T}(\rho_t)-\mathcal F_{H,T}(\gamma)
=\frac{k_BT}{2}
g^{\mathrm{BKM}}_\gamma(X,X)t^2
+o(t^2).
$$

The factor \(1/2\) is the Taylor coefficient. It is not part of the definition of the Hessian or the BKM form.

## Coincidence is not all-history dynamics

Two true statements must be kept separate:

1. For fixed \(H\), \(T\), and \(\gamma\), the scalar identity
   $$
   \mathcal F_{H,T}(\rho)-\mathcal F_{H,T}(\gamma)
   =k_BT\,D(\rho\Vert\gamma)
   $$
   holds at finite separation.
2. The replacement of that scalar difference by a BKM quadratic form is valid only to second order where \(\rho\) meets \(\gamma\).

Away from coincidence, the fixed-reference function

$$
t\longmapsto D(\rho_t\Vert\gamma)
$$

generally has a nonzero first derivative. Its value is not

$$
\frac12g^{\mathrm{BKM}}_{\rho_t}(\dot\rho_t,\dot\rho_t),
$$

nor is it obtained by inserting the instantaneous BKM norm into the quadratic Taylor formula at every point. [[causal-scale-theory/no-gos/fixed-reference-free-energy-does-not-give-the-pulse|The fixed-reference counterexample]] exhibits this failure explicitly.

If \(H\) or \(T\) varies, then the functional and its Gibbs minimizer also vary; work, temperature, and moving-reference terms enter. In infinite systems or type-III quantum field theory, density matrices and traces may not exist, so an operator-algebraic relative entropy, a common carrier, a specified class of perturbations, and renormalization control are required. None of these extensions turns a coincidence Hessian by itself into an all-history energy density, stress tensor, action, or conservation law.
