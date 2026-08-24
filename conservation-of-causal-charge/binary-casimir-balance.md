# The Binary Casimir Balance

The binary Casimir balance is the conservation-specific interpretation of two exact results owned by [[binary-information-geometry/involutive-casimir|the involutive Casimir identity]] and [[binary-information-geometry/balanced-exponential-family|the balanced binary exponential family]]. A fixed representation second moment can be redistributed between polarization and susceptibility, but this statewise allocation is not yet a Noether charge, a spacetime current, or a gravity theorem.

## Imported exact algebra

For a normalized state \(\omega\) and a self-adjoint involution

$$
Q^2=\mathbf1,
$$

the shared Casimir theorem defines

$$
m_\omega:=\omega(Q)
$$

and proves

$$
\boxed{
m_\omega^2+\operatorname{Var}_\omega(Q)=1.}
$$

This result requires no balanced reference state. It is the decomposition of the fixed second moment \(\omega(Q^2)=1\).

After a faithful commuting reference state with equal total weights in the \(Q=\pm1\) sectors has separately been granted, the shared balanced-family theorem gives

$$
\boxed{
m(\theta)=\tanh\theta,
\qquad
g^{\mathrm{bin}}_{\theta\theta}
=\operatorname{sech}^2\theta,
\qquad
m^2+g^{\mathrm{bin}}_{\theta\theta}=1.}
$$

The lower-case \(g^{\mathrm{bin}}_{\theta\theta}\) is the normalized response of the reduced binary family. It is not the extensive physical wall norm \(G^\perp_{NN}\). Balance selects the centered origin \(\theta=0\); neither involutivity nor the existence of two normal orientations selects that state.

## Why the identity is conservation-shaped

Along any differentiable state family,

$$
\frac{\mathrm d}{\mathrm ds}
\left(
m_s^2+\operatorname{Var}_{\omega_s}(Q)
\right)=0
$$

because the quantity in parentheses is identically one. On the balanced family this becomes

$$
2m\frac{\mathrm dm}{\mathrm ds}
+\frac{\mathrm d}{\mathrm ds}
g^{\mathrm{bin}}_{\theta\theta}=0.
$$

This is an exact exchange identity inside a fixed representation. It gives a disciplined meaning to “conservation through symmetry breaking”: the state-dependent order parameter changes while the normalized Casimir does not. It supplies no continuous spacetime symmetry, moment map, boundary flux, or equation of motion. [[causal-individuation-balance]] states the additional structure required for a genuine causal charge.

## Conditional scale and source projection

Let \(x:=N-N_c\). If the independent theorem in [[basic-concepts/soldering/affine-scale-state|affine scale--state soldering]] applies, then

$$
\theta=\varrho_\perp x,
\qquad
\nu:=|\varrho_\perp|,
$$

and the normalized pullback is

$$
g^{\mathrm{bin}}_{NN}
=\left(\frac{\mathrm d\theta}{\mathrm dN}\right)^2
g^{\mathrm{bin}}_{\theta\theta}
=\nu^2\operatorname{sech}^2(\nu x).
$$

The physical horizontal norm additionally contains an extensive factor,

$$
G^\perp_{NN}(N)
=C_\perp(N)g^{\mathrm{bin}}_{NN}(N).
$$

Neither the Casimir nor affine soldering fixes \(C_\perp\), and [[basic-concepts/soldering/continuous-character-no-go|character theory does not fix]] \(\nu=1\).

If one further assumes constant \(C_\perp\) and the anchored all-history source law in [[program-core/ruble-equations|Ruble's equations]], then

$$
\frac{\rho_X(N)}{\rho_{X,c}}
=\operatorname{sech}^2(\nu x)
=1-m(N)^2,
$$

so

$$
\boxed{
m^2+\frac{\rho_X}{\rho_{X,c}}=1.}
$$

This final equality is a **[CONDITIONAL OUTPUT]** of the constitutive cosmological projection. It is not part of the binary theorem.

## Claim boundary

The exact algebra does not establish that

- \(m\) is an actual fact rather than an expectation value;
- variance is entropy or ontological information;
- the binary quotient is the full causal-wall state;
- normalized susceptibility has a local gravitational image; or
- a linear causal charge is conserved.

Those are separate questions in [[facthood-and-symmetry-breaking]], [[state-geometry-charge-weld]], and [[causal-individuation-balance]].
