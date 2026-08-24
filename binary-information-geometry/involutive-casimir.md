# The Involutive Casimir Identity

For a normalized self-adjoint involution, the squared expectation and variance always sum to one. This is an exact state-dependent decomposition of a fixed second moment, not a dynamical conservation law or a Noether charge.

Let \(\mathcal A\) be a unital \(*\)-algebra represented in a setting where the following expectations exist, let \(\omega\) be a normalized positive state, and suppose

$$
Q=Q^*,
\qquad
Q^2=\mathbf1.
$$

Define the polarization

$$
m_\omega:=\omega(Q)
$$

and the variance

$$
\operatorname{Var}_\omega(Q)
:=\omega\!\left((Q-m_\omega\mathbf1)^2\right).
$$

Expanding the square and using \(\omega(\mathbf1)=1\) gives

$$
\operatorname{Var}_\omega(Q)
=\omega(Q^2)-\omega(Q)^2
=1-m_\omega^2.
$$

Therefore

$$
\boxed{
m_\omega^2+\operatorname{Var}_\omega(Q)=1.}
$$

This is **[EXACT — UNDER THE STATED ALGEBRAIC HYPOTHESES]**. Positivity also gives

$$
-1\leq m_\omega\leq1,
\qquad
0\leq\operatorname{Var}_\omega(Q)\leq1.
$$

Equality \(|m_\omega|=1\) means zero variance in the \(Q\)-distribution. The midpoint \(m_\omega=0\) means maximal variance, but it does not follow from \(Q^2=\mathbf1\); it requires a state with balanced spectral weights.

## Along a family of states

For any differentiable family \(\omega_s\),

$$
\frac{\mathrm d}{\mathrm ds}
\left(
m_s^2+\operatorname{Var}_{\omega_s}(Q)
\right)=0,
$$

simply because the quantity in parentheses is identically one. This derivative is an exchange identity internal to the family. It supplies no current, flux law, Hamiltonian symmetry, or spacetime continuity equation.

If an oriented path reaches the endpoint polarizations

$$
\lim_{s\to-\infty}m_s=-1,
\qquad
\lim_{s\to+\infty}m_s=1,
$$

then

$$
\mathcal I_Q
:=\frac12\int_{-\infty}^{+\infty}
\frac{\mathrm dm_s}{\mathrm ds}\,\mathrm ds
=1.
$$

\(\mathcal I_Q\) is an oriented endpoint index. Reversing the path gives \(-1\). Calling it a conserved charge would require additional variational and symmetry structure not present here.

## Boundary of the result

The identity fails in this form if \(Q^2\neq\mathbf1\), if the state is not normalized, or if the relevant moments do not exist. For a generator with more than two spectral values, the general variance identity remains

$$
\omega(Q^2)=\omega(Q)^2+\operatorname{Var}_\omega(Q),
$$

but its right-hand side is not fixed to one unless the second moment is fixed by an independent representation condition.

