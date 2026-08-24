# Binary Translation Is Not the Escort Tangent

For the literal balanced two-state family, translation in the exponential coordinate and temperature rescaling of that state's modular Hamiltonian have different BKM norms. Their mismatch at the balanced point rules out their direct identification.

Let

$$
\rho_\theta
=\frac{e^{\theta Q}}{2\cosh\theta},
\qquad
Q^2=\mathbf1.
$$

By [[balanced-exponential-family|the balanced-family theorem]], translation in \(\theta\) has

$$
g^{\mathrm{bin}}_{\theta\theta}
=\operatorname{sech}^2\theta.
$$

The modular Hamiltonian of the same state is

$$
K_\theta:=-\ln\rho_\theta
=-\theta Q+\ln(2\cosh\theta)\mathbf1.
$$

Its centered variance is therefore

$$
\boxed{
\operatorname{Var}_{\rho_\theta}(K_\theta)
=\theta^2\operatorname{sech}^2\theta.}
$$

At the balanced point,

$$
g^{\mathrm{bin}}_{\theta\theta}(0)=1,
\qquad
\operatorname{Var}_{\rho_0}(K_0)=0.
$$

No constant normalization identifies the two functions along the whole curve. Hence

$$
\boxed{
\text{binary exponential translation}
\ne
\text{escort-temperature rescaling of the same reduced state}.}
$$

This **[NO-GO]** excludes only the direct identification. A larger wall sector may possess an escort tangent whose sufficient binary reduction preserves the physical norm, but that requires a channel and tangent-alignment theorem.
