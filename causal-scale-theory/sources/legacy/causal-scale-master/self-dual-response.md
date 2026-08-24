# Self-Dual Scale-Capacity Response

Granting the binary unit-slope model, the Scale--Capacity Equivalence Principle, the free-energy source law, and the flat-FLRW horizon conversion produces a rigid homogeneous response. Its shape, crossing equality, and equation of state are deductions from those premises rather than independent assumptions.

## Closed density and crossing

Use

$$
N:=\ln\frac{a}{a_0},
\qquad
N_c:=\ln\frac{a_c}{a_0}.
$$

The response density is

$$
\rho_X(N)
=\frac12\rho_{\mathrm{crit},c}
\operatorname{sech}^2(N-N_c).
$$

At the self-dual point,

$$
\Omega_{X,c}=\frac12,
\qquad
\rho_X(N_c)=\rho_{\mathrm{ordinary}}(N_c).
$$

The equality is with the complete non-response sector, including radiation. Present flatness fixes the crossing date through

$$
1=\Omega_{m0}+\Omega_{r0}
+\left[
\Omega_{m0}e^{-3N_c}
+\Omega_{r0}e^{-4N_c}
\right]\operatorname{sech}^2N_c.
$$

## Equation of state and invariant

Assuming separate conservation,

$$
\frac{\mathrm d\rho_X}{\mathrm dN}
=-3(1+w_X)\rho_X,
$$

gives

$$
w_X(N)
=-1+\frac23\tanh(N-N_c).
$$

For $X:=1+w_X$,

$$
\frac{\mathrm dX}{\mathrm dN}
=\frac23-\frac32X^2,
$$

with limiting fixed points $w_X=-5/3$ and $w_X=-1/3$. Eliminating the crossing date and amplitude yields the primary shape test

$$
9(1+w_X)^2
+6\frac{\mathrm dw_X}{\mathrm dN}=4.
$$

A constant value other than four, or statistically significant redshift dependence after reconstruction covariance is included, rejects the rigid unit-slope history.

## Acceleration and future

In the declared matter+radiation branch with $\Lambda_{\mathrm{res}}=0$, the pulse is negligible in the remote past, rises to one maximum, and decays as $a^{-2}$ in the future. Its competition with ordinary dilution gives one past entry into acceleration and one future exit; the late state has $w_X\to-1/3$, $a(t)\sim t$, and no permanent future event horizon.

A positive residual can alter or remove that exit and eventually restores de Sitter acceleration. Negative-residual or recollapsing sectors are outside the stated branch and are not classified by this note.

## Claim status

- **Conditional deduction:** the density, crossing, equation of state, and invariant, given $\varrho_\perp=1$, $\mathfrak R_c=1$, the source law, flatness, and separate conservation.
- **Branch-dependent deduction:** a single finite acceleration interval and coasting future for matter+radiation plus exactly zero residual.
- **Global sector choice:** $\Lambda_{\mathrm{res}}=0$.
- **Open:** a covariant conserved response tensor, regular perturbation crossing, sound/cone speed, stability, and a full Boltzmann likelihood.

## Dependencies and uses

The result combines [[scale-soldering|unit scale soldering]], [[scale-capacity|scale--capacity closure]], [[free-energy-source|the source law]], [[hawking-friedmann|horizon conversion]], and [[flrw-kinematics|FLRW kinematics]].

## Provenance

Distilled from [[Causal_Scale_Dynamics_Master_v7_0|Causal Scale Dynamics Master v7.0]]. Benchmark numbers are kept in the entry note because they are versioned empirical outputs rather than evergreen structure.
