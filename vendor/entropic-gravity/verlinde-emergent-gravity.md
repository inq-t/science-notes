# Verlinde’s Emergent Gravity and the Dark Universe

Verlinde’s 2016 proposal treats positive-dark-energy de Sitter space as a medium with long-range, volume-law entanglement. Matter displaces part of that entropy, and the residual medium is modeled elastically. Saturation first turns an elastic inequality into an approximate bulk equality; a gravitational dictionary and boundary identification then translate it; and only in a later static, isolated, approximately spherical specialization does it yield the familiar apparent-dark-mass relation.

The primary source is [[vendor/entropic-gravity/sources/papers/1611.02269-verlinde-emergent-gravity-dark-universe.pdf|Verlinde 2016/2017]]. This is a distinct construction from [[verlinde-entropic-force]].

## Microscopic hypotheses

The proposal begins from two stated hypotheses:

1. short-range entanglement among microscopic spacetime degrees of freedom produces the usual area law; and
2. de Sitter entropy is distributed through those same bulk degrees of freedom and arises from long-range entanglement.

The paper then proposes that

- de Sitter microstates equilibrate only on cosmological timescales;
- their sub-Hubble response has glass-like memory;
- localized matter removes entropy from the delocalized dark-energy medium; and
- outside the entropy-removal inclusion, the displacement can be imposed to satisfy \(\nabla_i u^i=0\) and represented by a special linear-elastic constitutive law in the low-surface-density regime.

These are physical postulates. No microscopic Hilbert space, Hamiltonian, or relaxation equation is supplied.

## De Sitter entropy as a volume law

Use \(c=k_B=1\) unless otherwise stated. Let the de Sitter radius be \(L\), with

$$
a_0=\frac{1}{L}=H_0.
$$

With dimensions restored,

$$
a_0=\frac{c^2}{L}=cH_0.
$$

The static-patch horizon entropy is

$$
S_{\mathrm{DE}}(L)
=\frac{A(L)}{4G\hbar}.
$$

Uniform distribution through the spatial volume gives

$$
S_{\mathrm{DE}}(r)
=\frac{V(r)}{V_0}
=\frac{r}{L}
\frac{A(r)}{4G\hbar},
$$

where, in \(d\) spacetime dimensions,

$$
V_0=\frac{4G\hbar L}{d-1}.
$$

The equality of the volume-law count with the horizon area law at \(r=L\) follows from the uniform-volume assumption and the horizon normalization. It is not an independent microscopic calculation.

## Entropy deficit produced by matter

For a central weak-field mass in de Sitter space, the horizon shift and area response obtained from the Schwarzschild–de Sitter geometry give

$$
\frac{dS_M}{dr}
=-\frac{2\pi M}{\hbar},
\qquad
S_M(r)
=-\frac{2\pi Mr}{\hbar}.
$$

With ordinary units restored,

$$
S_M(r)
=-2\pi k_B\frac{Mcr}{\hbar}.
$$

This imports the standard geometric response and the area law, then reinterprets their combination as entropy removed from the dark-energy medium.

Define the corresponding displaced volume by

$$
S_M(r)=-\frac{V_M(r)}{V_0}.
$$

Then

$$
V_M(r)
=\frac{8\pi G}{a_0}
\frac{Mr}{d-1}.
$$

For \(\Sigma_M=M/A(r)\),

$$
\varepsilon_M(r)
:=\frac{V_M(r)}{V(r)}
=\frac{8\pi G}{a_0}\Sigma_M(r).
$$

The proposed dark-gravity regime is \(\varepsilon_M<1\): the matter-induced deficit removes only part of the available volume-law entropy.

## Elastic dictionary

The radial displacement is identified with the Newtonian potential:

$$
u(r)=L\Phi(r)
=-\frac{V_M^*(r)}{A(r)},
$$

where

$$
V_M^*(r)
=\frac{8\pi G}{a_0}
\frac{Mr}{d-2}.
$$

For a displacement field \(u_i\), define strain

$$
\varepsilon_{ij}
=\frac12
\left(
\nabla_i u_j+\nabla_j u_i
\right).
$$

The constitutive stress law is

$$
\sigma_{ij}
=\frac{a_0^2}{8\pi G}
\left(
\varepsilon_{ij}
-\varepsilon_{kk}\delta_{ij}
\right).
$$

Thus the effective Lamé coefficients obey

$$
\mu=\frac{a_0^2}{16\pi G},
\qquad
\lambda+2\mu=0.
$$

The exterior condition \(\nabla_i u^i=0\) should not be confused with the conventional incompressible constitutive limit. Verlinde’s stated coefficients instead give a vanishing longitudinal, or P-wave, modulus \(\lambda+2\mu\).

The apparent dark surface density is identified with the largest principal deviatoric strain:

$$
\Sigma_D
=\frac{a_0}{8\pi G}\varepsilon.
$$

The moduli and this gravitational dictionary are fixed by matching to the gravitational surface relations. They are not computed from the hypothesized de Sitter microstates.

## The proved inequality

The general elastic argument establishes

$$
\boxed{
\int_{\mathcal B}\varepsilon^2\,dV
\leq
V_M(\mathcal B).
}
$$

The algebraic ingredient is

$$
\varepsilon^2
\leq
\frac{d-2}{d-1}
\varepsilon'_{ij}\varepsilon'^{ij},
$$

where \(\varepsilon'_{ij}\) is the deviatoric strain. Saturation of this principal-strain bound is equivalent to taking the principal strains transverse to the maximal direction to be mutually equal. The derivation also extends a strain-energy integral beyond \(\mathcal B\). With that saturation and a negligible exterior tail, the first-stage result is the approximate bulk equality

$$
\int_{\mathcal B}\varepsilon^2\,dV
\simeq
V_M(\mathcal B).
$$

No gradient-displacement, equipotential-boundary, or spherical assumption is needed merely for this saturation step.

## Saturated integral relation

To translate the saturated elastic relation into gravitational variables, the paper additionally takes the displacement to be a gradient field and identifies the boundary normal with the relevant baryonic equipotential structure. Under those translation assumptions,

$$
\int_{\mathcal B}
\left(
\frac{8\pi G}{a_0}\Sigma_D
\right)^2dV
=
\frac{d-2}{d-1}
\oint_{\partial\mathcal B}
\frac{\Phi_B}{a_0}n_i\,dA_i.
$$

Equivalently,

$$
\left(
\frac{8\pi G}{a_0}\Sigma_D
\right)^2
=
\frac{d-2}{d-1}
\nabla_i
\left(
\frac{\Phi_B}{a_0}n_i
\right).
$$

This local equality is a stronger claim than the unsaturated elastic bound. Isolation, equilibrium, four spacetime dimensions, and spherical symmetry enter only in the next radial specialization.

## Isolated spherical systems

For a static, isolated, approximately spherical system in four spacetime dimensions,

$$
\boxed{
\int_0^r
\frac{G M_D^2(r')}{r'^2}\,dr'
=
\frac{a_0}{6}M_B(r)r.
}
$$

Differentiation gives

$$
M_D^2(r)
=\frac{a_0r^2}{6G}
\frac{d}{dr}
\left[
rM_B(r)
\right].
$$

The apparent acceleration therefore obeys

$$
g_D^2(r)
=\frac{a_0}{6}
\left[
g_B(r)+4\pi Gr\rho_B(r)
\right].
$$

In the original aligned spherical prescription, \(g_D\) is an additional acceleration, so the total is

$$
g_{\mathrm{tot}}=g_B+g_D.
$$

Later empirical papers sometimes combine \(g_B\) and \(g_D\) differently. Those choices are additional phenomenological prescriptions, not consequences of the displayed elastic derivation.

For a point mass, or a region where the enclosed baryonic mass is effectively constant,

$$
g_D=\sqrt{a_Mg_B},
\qquad
a_M=\frac{a_0}{6},
$$

and

$$
v_f^4=GM_Ba_M.
$$

Verlinde presents this as an estimate or fitting relation, not a MOND field equation and not a modified law of inertia.

## Domain and missing theory

The spherical formula applies only where the system is approximately

- isolated;
- static and in dynamical equilibrium;
- spherical or aligned with the assumed equipotential geometry;
- in the low-surface-density response regime; and
- well approximated as a perturbation of a dark-energy-dominated de Sitter state.

The source explicitly excludes strongly dynamical systems such as the Bullet Cluster from this formula and retains only an inequality sufficiently far from the central mass or in the presence of other systems.

The paper does not provide a covariant action, generic nonspherical field equations, a lensing law, cosmological background evolution, perturbations, early-universe dynamics, structure formation, or a CMB calculation. Nor does it specify whether the relevant \(a_0\) tracks a time-dependent \(H(t)\). Its empirical status is therefore assessed in [[empirical-status]] at the level of the restricted apparent-mass relation, often with auxiliary GR or \(\Lambda\)CDM assumptions.
