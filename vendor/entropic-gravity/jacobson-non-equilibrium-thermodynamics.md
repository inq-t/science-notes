# Jacobson’s Non-Equilibrium Extension

Eling, Guedens, and Jacobson showed that replacing the constant area entropy density by a curvature-dependent density generally destroys the 1995 equilibrium construction. Consistency with stress-energy conservation requires an internal entropy-production term, and the resulting balance law yields metric \(f(R)\) gravity under specific hypotheses.

The primary source is [[library/non-equilibrium-thermodynamics-of-spacetime/inq|Eling, Guedens, and Jacobson 2006]]. This note uses \(c=k_B=1\).

## Curvature-dependent entropy density

Let the local horizon entropy density be

$$
s=\alpha f(R),
$$

where \(f(R)=1+O(R)\). The entropy variation along the horizon generators is

$$
\delta S
=\alpha\int_{\mathcal H}
\bigl(\theta f+\dot f\bigr)
\,d\lambda\,d^2A,
$$

with \(\dot f:=k^a\nabla_af\).

The heat flux divided by temperature begins at first order in the affine parameter. Its zeroth-order entropy counterpart must therefore vanish:

$$
(\theta f+\dot f)|_p=0.
$$

For nonconstant \(f\), this requires

$$
\theta|_p=-\frac{\dot f}{f},
$$

which is generically nonzero. The horizon element is no longer in the equilibrium state used in the 1995 proof.

## Entropy balance rather than Clausius equality

Differentiating the entropy integrand and using Raychaudhuri produces a gradient term proportional to

$$
\frac32f^{-1}\nabla_af\nabla_bf.
$$

Without an additional term, the resulting tensor equation is not generally compatible with \(\nabla^aT_{ab}=0\). The proposed law is therefore

$$
dS=\frac{\delta Q}{T}+d_iS,
$$

where \(d_iS\) is internal entropy production. Along the local horizon,

$$
d_iS
=\int_{\mathcal H}\sigma\,d\lambda\,d^2A,
$$

with

$$
\sigma
=-\frac32\alpha f^{-1}\dot f^{\,2}\lambda
=-\frac32\alpha f\theta^2\lambda.
$$

When expressed in the appropriate Killing-flow parameter this is positive and has the form of bulk-viscous entropy production. Its effective bulk viscosity is

$$
\zeta_{\mathrm{bulk}}
=\frac32\alpha fT
=\frac{3\hbar\alpha f}{4\pi}.
$$

The same framework permits shear-viscous production in pure Einstein gravity, with

$$
\eta_{\mathrm{shear}}
=\frac{\hbar\alpha}{4\pi}
=\frac{1}{16\pi G}.
$$

## Resulting field equation

Define a curvature Lagrangian \(\mathcal L(R)\) by

$$
f(R)=\frac{d\mathcal L}{dR}.
$$

The entropy-balance law gives

$$
fR_{ab}
-\nabla_a\nabla_bf
+\left(\Box f-\frac12\mathcal L\right)g_{ab}
=\frac{2\pi}{\hbar\alpha}T_{ab}.
$$

This is the metric field equation obtained from an action proportional to

$$
\frac{\hbar\alpha}{4\pi}
\int d^4x\,\sqrt{-g}\,\mathcal L(R).
$$

## Claim boundary

- The field equation follows conditionally from the chosen entropy functional and balance law.
- The production term is selected by consistency with stress-energy conservation; its microscopic dissipative mechanism is not derived.
- The calculation concerns entropy density depending on the Ricci scalar. It is not a construction of arbitrary higher-curvature gravity.
- Higher-order ambiguities in the approximate local Killing field can be as large as the Planck-suppressed corrections one hopes to read from horizon thermodynamics.

This result corrects the tempting but false inference that one can insert a curvature-dependent entropy into the equilibrium 1995 proof without changing its thermodynamic type.
